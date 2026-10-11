#!/usr/bin/env python3
"""Fail-closed, dependency-free, predeclared all-slice release evaluator.

Inputs must be independent human-adjudicated judgments and frozen evidence.
This is a release gate, NOT a substitute for running a model or adjudication.
"""
import argparse
import collections
import hashlib
import json
import math
import pathlib
import re
import statistics
import sys


def sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def jsonl(path):
    records=[]
    for n, line in enumerate(pathlib.Path(path).read_text(encoding='utf-8').splitlines(), 1):
        if line.strip():
            try: records.append(json.loads(line))
            except json.JSONDecodeError as e: raise ValueError(f'{path}:{n} invalid JSON: {e}') from e
    return records


def lower_wilson(k,n,alpha):
    if n <= 0: return 0.0
    z=statistics.NormalDist().inv_cdf(1-alpha)
    p=k/n
    den=1+z*z/n
    return max(0.0,(p+z*z/(2*n)-z*math.sqrt((p*(1-p)+z*z/(4*n))/n))/den)


def assert_valid(condition, message):
    if not condition: raise ValueError(message)


def run_gate(manifest_file, judgment_files, runs_file, config_file):
    config=json.loads(pathlib.Path(config_file).read_text(encoding='utf-8'))
    runs=json.loads(pathlib.Path(runs_file).read_text(encoding='utf-8'))['runs']
    manifest=jsonl(manifest_file)
    failures=[]
    results=[]
    n_runs=config['min_independent_runs']
    assert_valid(len(runs)>=n_runs,f'Requires at least {n_runs} preregistered runs; got {len(runs)}')
    run_ids=[x['run_id'] for x in runs]
    assert_valid(len(set(run_ids))==len(run_ids),'Duplicate run IDs')
    fp={(x['model_fingerprint'],x['prompt_sha256'],x['pipeline_sha256'],x['rubric_version']) for x in runs}
    assert_valid(len(fp)==1,'All repeated runs must use IDENTICAL frozen model/prompt/pipeline/rubric; create new candidate for changes')
    mh=sha(manifest_file)
    assert_valid(all(x['manifest_sha256']==mh for x in runs),'Frozen manifest digest mismatch')
    assert_valid(all(x.get('seed') is not None for x in runs),'Run metadata missing reproducibility seed')
    seeds=[x['seed'] for x in runs]
    assert_valid(len(set(seeds))==len(seeds),'Use distinct run seeds, not identical replays')
    ids={}
    for rec in manifest:
        cid=rec['case_id']
        assert_valid(cid not in ids,f'Duplicate locked case ID {cid}')
        assert_valid(rec['gold_status']=='LOCKED_ADJUDICATED',f'{cid} has candidate/unlocked gold; cannot certify')
        assert_valid(rec['split']=='holdout',f'{cid} is not locked holdout')
        rats=rec['independent_raters']
        assert_valid(len(set(rats))>=2 and len(rats)>=2,f'{cid}: requires distinct independently blinded annotator identities')
        assert_valid(len(rec.get('source_hash',''))==64,f'{cid}: missing artifact SHA256')
        assert_valid(len(rec.get('adjudication_hash',''))==64,f'{cid}: missing adjudication ledger SHA256')
        assert_valid(rec.get('family_id'),f'{cid}: missing contrast/family identifier')
        assert_valid(isinstance(rec.get('strata'),dict),f'{cid}: strata must be an object')
        ids[cid]=rec
    judgments=[]
    for p in judgment_files: judgments.extend(jsonl(p))
    scores={}
    for row in judgments:
        rid,cid=row['run_id'],row['case_id']
        assert_valid(rid in run_ids and cid in ids,f'Unknown score run/case {rid}/{cid}')
        key=(rid,cid)
        assert_valid(key not in scores,f'Duplicate score for {key}')
        assert_valid(isinstance(row['correct'],bool) and isinstance(row['abstained'],bool),f'Invalid correctness/abstention for {key}')
        assert_valid(isinstance(row['critical_errors'],list),f'critical_errors must be a list for {key}')
        assert_valid(row['judged_by'] and row['judge_method'] in ('INDEPENDENT_HUMAN','AUDITED_DETERMINISTIC'),f'Invalid independent scorer {key}')
        assert_valid(row.get('rubric_version')==runs[run_ids.index(rid)]['rubric_version'],f'Rubric drift {key}')
        conf=row['confidence']
        assert_valid(isinstance(conf,(int,float)) and not isinstance(conf,bool) and math.isfinite(conf) and 0<=conf<=1,f'Invalid confidence for {key}')
        scores[key]=row
    expected={(rid,cid) for rid in run_ids for cid in ids}
    assert_valid(set(scores)==expected,f'Incomplete matrix: missing {len(expected-set(scores))} row(s). No dropping hard cases or rerun cherry-picking.')

    slices=[{'name':'ALL','field':None,'value':None,'min_cases':config['min_total_cases']}]
    for competency in config['required_competencies']:
        slices.append({'name':'competency:'+competency,'field':'competency','value':competency,'min_cases':config['min_cases_per_competency']})
    slices.extend(config['required_slices'])
    slices.extend(config.get('required_cross_slices', []))
    alpha=config['familywise_alpha']/max(1,len(run_ids)*len(slices))
    prev_idx={}
    for rid in run_ids:
        for sl in slices:
            def matches(rec):
                if 'where' in sl:
                    return all((rec['competency'] if field == 'competency' else rec['strata'].get(field)) == value
                               for field, value in sl['where'].items())
                if sl['field'] is None:return True
                if sl['field']=='competency':return rec['competency']==sl['value']
                return rec['strata'].get(sl['field'])==sl['value']
            subset=[rec for rec in manifest if matches(rec)]
            n=len(subset)
            cor=sum(scores[(rid,rec['case_id'])]['correct'] and not scores[(rid,rec['case_id'])]['abstained'] for rec in subset)
            abst=sum(scores[(rid,rec['case_id'])]['abstained'] for rec in subset)
            critical=sum(bool(scores[(rid,rec['case_id'])]['critical_errors']) for rec in subset)
            num_families=len(set(rec['family_id'] for rec in subset))
            lcb=lower_wilson(cor,n,alpha)
            point=cor/n if n else 0.0
            pass_slice=n>=sl['min_cases'] and num_families>=config['min_distinct_families_per_slice'] and lcb>=config['floor'] and critical==0
            if not pass_slice:failures.append(f'{rid}/{sl["name"]}: n={n}, families={num_families}, correct={cor}, lb={lcb:.4f}, critical={critical}')
            results.append({'run_id':rid,'slice':sl['name'],'n':n,'families':num_families,'correct':cor,'abstained':abst,'critical_error_cases':critical,
                            'point_accuracy':round(point,5),'simultaneous_wilson_lcb':round(lcb,5),'pass_95':pass_slice,
                            'pass_97':pass_slice and lcb>=config['stretch']})
        # brier/ECE descriptive; not a performance substitute
        sample=[scores[(rid,cid)] for cid in ids]
        brier=sum((r['confidence']-(1.0 if r['correct'] and not r['abstained'] else 0.0))**2 for r in sample)/len(sample)
        ece=0.0
        for b in range(10):
            cell=[r for r in sample if ((min(9,int(r['confidence']*10)))==b)]
            if cell:
                obs=sum(r['correct'] and not r['abstained'] for r in cell)/len(cell)
                pred=sum(r['confidence'] for r in cell)/len(cell)
                ece+=(len(cell)/len(sample))*abs(obs-pred)
        prev_idx[rid]={'brier':round(brier,5),'ece_10bin':round(ece,5),'coverage':round(1-sum(r['abstained'] for r in sample)/len(sample),5)}
        if prev_idx[rid]['ece_10bin']>config['max_ece']:
            failures.append(f'{rid}: confidence calibration ECE={prev_idx[rid]["ece_10bin"]:.4f} > {config["max_ece"]}')

    return {'release':'PASS' if not failures else 'BLOCKED','target_floor':config['floor'],
            'stretch_release':'PASS' if not failures and all(r['pass_97'] for r in results) else 'NOT_QUALIFIED',
            'model_fingerprint':runs[0]['model_fingerprint'],'locked_manifest_sha256':mh,
            'run_ids':run_ids,'familywise_alpha':config['familywise_alpha'],'bonferroni_adjusted_alpha_per_check':alpha,
            'calibration':prev_idx,'results':results,'failures':failures,
            'note':'Bonferroni-adjusted Wilson confidence is a conservative statistical gate under sample representativeness assumptions; it cannot guarantee minimum accuracy on every future input.'}


def main():
    p=argparse.ArgumentParser(description='Fail-closed Persuasion Gym release gate')
    p.add_argument('--manifest',required=True)
    p.add_argument('--judgments',required=True,nargs='+')
    p.add_argument('--runs',required=True)
    p.add_argument('--config',default='config/release.json')
    p.add_argument('--out',default='reports/release_report.json')
    args=p.parse_args()
    try:
        report=run_gate(args.manifest,args.judgments,args.runs,args.config)
    except (ValueError,KeyError,TypeError,FileNotFoundError,ZeroDivisionError,IndexError) as e:
        report={'release':'BLOCKED','error':str(e),'failures':['Input/provenance/pre-registration validation failed']}
    path=pathlib.Path(args.out);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['release'],'failures':report.get('failures',[])[:12],'report':str(path)},indent=2))
    return 0 if report['release']=='PASS' else 2

if __name__=='__main__':sys.exit(main())

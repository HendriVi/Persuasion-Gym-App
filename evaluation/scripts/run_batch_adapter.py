#!/usr/bin/env python3
"""Efficient model runner. Backend must consume JSONL on stdin, emit JSONL on stdout.
Inputs are untrusted text and benchmark instructions; do not pass private keys.
This tool collects RAW outputs and NEVER self-scores or declares a release pass.
"""
import argparse,json,subprocess,sys,time
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--inputs',required=True)
    ap.add_argument('--out',required=True)
    ap.add_argument('--run-id',required=True)
    ap.add_argument('--timeout',type=int,default=1800)
    ap.add_argument('command',nargs=argparse.REMAINDER)
    x=ap.parse_args()
    cmd=x.command[1:] if x.command and x.command[0]=='--' else x.command
    if not cmd:ap.error('Provide a batch JSONL adapter command after --')
    cases=[json.loads(line) for line in Path(x.inputs).read_text().splitlines() if line.strip()]
    if len({c['case_id'] for c in cases})!=len(cases):raise ValueError('Duplicate case IDs')
    by_id={c['case_id']:c for c in cases}
    start=time.perf_counter()
    try:
        p=subprocess.run(cmd,input=''.join(json.dumps(c)+'\n' for c in cases),capture_output=True,text=True,timeout=x.timeout,check=False)
        lines=p.stdout.splitlines()
        parsed={}
        for line in lines:
            if not line.strip():continue
            try:
                rec=json.loads(line)
                cid=rec['case_id']
                if cid not in by_id or cid in parsed:raise ValueError('unexpected or duplicate case ID')
                parsed[cid]=rec.get('response',rec)
            except (ValueError,KeyError,TypeError) as exc:
                raise ValueError(f'Batch adapter returned invalid response: {exc}') from exc
        if p.returncode:
            print(f'WARNING: batch adapter exit {p.returncode}; incomplete rows retained as errors',file=sys.stderr)
    except subprocess.TimeoutExpired:
        parsed={}
        print('WARNING: batch model timed out; all cases counted as failure/abstention',file=sys.stderr)
    elapsed=round(1000*(time.perf_counter()-start),2)
    dest=Path(x.out);dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('w') as f:
        for c in cases:
            response=parsed.get(c['case_id'],{'status':'ERROR','abstained':True,'confidence':0.0,'error':'model output missing'})
            f.write(json.dumps({'run_id':x.run_id,'case_id':c['case_id'],'response':response,'batch_elapsed_ms':elapsed})+'\n')
    print(f'{len(cases)} input cases, {len(parsed)} returned responses; wrote all cases to {dest}; NOT SCORED')

if __name__=='__main__':main()

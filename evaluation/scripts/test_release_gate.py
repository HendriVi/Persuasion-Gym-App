import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from release_gate import run_gate, lower_wilson

ROOT = Path(__file__).resolve().parents[1]

class ReleaseGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory()
        cls.base=Path(cls.tmp.name)
        competence=['rhetoric','argument','verification','causal','intent','level_separation','manipulation','systems']
        cls.m=[]
        for ci,c in enumerate(competence):
            for j in range(800):
                idx=ci*800+j
                # Balanced, overlapping slices. 30+ independent families per slice.
                cls.m.append({'case_id':f'F_{idx:05d}','competency':c,'split':'holdout',
                              'gold_status':'LOCKED_ADJUDICATED','independent_raters':['synthetic_A','synthetic_B'],
                              'family_id':f'group_{ci}_{j//4}',
                              'source_hash':hashlib.sha256(f'SYNTHETIC-CASE-{idx}'.encode()).hexdigest(),
                              'adjudication_hash':hashlib.sha256(f'SYNTHETIC-LEDGER-{idx}'.encode()).hexdigest(),
                              'strata':{'domain':'politics' if j%2 else 'nonpolitical',
                                        'ambiguity':'high' if j%3==0 else 'low',
                                        'transfer':'cross_domain' if j%3==1 else 'none',
                                        'political_mirror':'mirror' if j%3==2 else 'none',
                                        'adversarial':'yes' if j%2 else 'no'}})
        cls.man=cls.base/'locked.jsonl'
        cls.man.write_text(''.join(json.dumps(x)+'\n' for x in cls.m))
        mf=hashlib.sha256(cls.man.read_bytes()).hexdigest()
        cls.runs={'runs':[{'run_id':f'run_{i}','seed':123+i,'model_fingerprint':'synthetic_integration_test_only',
                           'prompt_sha256':'abc','pipeline_sha256':'def','rubric_version':'v1',
                           'manifest_sha256':mf} for i in range(5)]}
        cls.runf=cls.base/'runs.json';cls.runf.write_text(json.dumps(cls.runs))
        cls.config=ROOT/'config/release.json'
        cls.scores=[]
        for r in cls.runs['runs']:
            for c in cls.m:
                cls.scores.append({'case_id':c['case_id'],'run_id':r['run_id'],'correct':True,'abstained':False,
                                  'critical_errors':[],'confidence':0.99,'judge_method':'INDEPENDENT_HUMAN',
                                  'judged_by':'SYNTHETIC_TEST_ONLY','rubric_version':'v1'})
        cls.full=cls.base/'scores.jsonl';cls.full.write_text(''.join(json.dumps(x)+'\n' for x in cls.scores))

    @classmethod
    def tearDownClass(cls):cls.tmp.cleanup()

    def test_wilson_penalizes_finite_perfect_scores(self):
        self.assertLess(lower_wilson(100,100,0.05/75),0.97)
        self.assertGreater(lower_wilson(400,400,0.05),0.97)

    def test_perfect_synthetic_fixture_passes_both_95_and_97(self):
        r=run_gate(self.man,[self.full],self.runf,self.config)
        self.assertEqual(r['release'],'PASS')
        self.assertEqual(r['stretch_release'],'PASS')
        self.assertEqual(len(r['run_ids']),5)
        self.assertEqual(len(r['results']),5*(1+8+6+6))

    def test_one_critical_error_blocks_high_average(self):
        scores=copy.deepcopy(self.scores)
        scores[0]['critical_errors']=['INTENT_OVERATTRIBUTION']
        p=self.base/'critical.jsonl';p.write_text(''.join(json.dumps(x)+'\n' for x in scores))
        r=run_gate(self.man,[p],self.runf,self.config)
        self.assertEqual(r['release'],'BLOCKED')
        self.assertTrue(any('critical=1' in f for f in r['failures']))

    def test_one_below_floor_competency_blocks_entire_release(self):
        scores=copy.deepcopy(self.scores)
        for row in scores:
            if row['run_id']=='run_0' and  row['case_id'].startswith('F_00') and int(row['case_id'][2:])<60:
                row['correct']=False
                row['confidence']=0.51
        p=self.base/'low_stratum.jsonl';p.write_text(''.join(json.dumps(x)+'\n' for x in scores))
        r=run_gate(self.man,[p],self.runf,self.config)
        self.assertEqual(r['release'],'BLOCKED')
        self.assertTrue(any('competency:rhetoric' in f for f in r['failures']))

    def test_missing_case_never_silently_dropped(self):
        with self.assertRaisesRegex(ValueError,'Incomplete matrix'):
            p=self.base/'missing.jsonl';p.write_text(''.join(json.dumps(x)+'\n' for x in self.scores[1:]))
            run_gate(self.man,[p],self.runf,self.config)

    def test_unadjudicated_gold_never_passes(self):
        items=copy.deepcopy(self.m)
        items[0]['gold_status']='CANDIDATE_PENDING_INDEPENDENT_ADJUDICATION'
        p=self.base/'bad_manifest.jsonl';p.write_text(''.join(json.dumps(x)+'\n' for x in items))
        updated=copy.deepcopy(self.runs)
        bad_hash=hashlib.sha256(p.read_bytes()).hexdigest()
        for row in updated['runs']:
            row['manifest_sha256']=bad_hash
        rf=self.base/'bad_runs.json';rf.write_text(json.dumps(updated))
        with self.assertRaisesRegex(ValueError,'unlocked gold'):
            run_gate(p,[self.full],rf,self.config)

if __name__=='__main__':unittest.main()

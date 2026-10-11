#!/usr/bin/env python3
"""Create model-visible prompts. Never copy private labels into prompt payloads."""
import argparse,json,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[1]
files={
    'gold-corpus':('item_id','data/corpus.jsonl'),
    'adversarial':('test_id','public/adversarial_probes.jsonl'),
    'intent-discipline':('test_id','public/intent_probes.jsonl'),
    'causal-discipline':('case_id','public/causal_probes.jsonl'),
    'level-separation':('case_id','public/level_separation_probes.jsonl'),
}

def build():
    res=[]
    for suite,(key,rel) in files.items():
        source=root/'benchmarks/internal'/suite/rel
        for line in source.read_text().splitlines():
            if not line.strip():continue
            obj=json.loads(line)
            payload={'case_id':f'{suite}/{obj[key]}','benchmark':suite,'gold_status':'CANDIDATE_NOT_GOLD',
                     'source_split':obj.get('split','development_candidate')}
            if suite=='gold-corpus':
                payload['input']={'text':obj['artifact']['content'],'scenario':obj['scenario'],
                                  'verification_packet':obj['verification_packet'],'task':'Analyze by the common schema; distinguish every reasoning level.'}
            elif suite=='causal-discipline':
                payload['input']={'scenario':obj['scenario'],'question':obj['question'],'required_output':obj.get('required_output')}
            else:
                payload['input']={'artifact':obj['artifact'],
                                  'verification_packet':obj.get('verification_packet') or obj.get('evidence_packet'),
                                  'task':obj.get('task',{'instruction':'Analyze the message and contextual evidence by the common schema.'})}
            res.append(payload)
    return res

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',default=str(root/'examples/public_probes_400.jsonl')); args=p.parse_args()
    dest=Path(args.out);dest.parent.mkdir(parents=True,exist_ok=True)
    rows=build();assert len(rows)==400
    dest.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
    print(f'Created {len(rows)} model-visible DEVELOPMENT probes in {dest} (zero gold labels).')

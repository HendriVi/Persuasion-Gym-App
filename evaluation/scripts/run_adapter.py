#!/usr/bin/env python3
"""Model runner protocol. Invokes an existing app/model CLI command per case.

Each CLI invocation receives one JSON prompt object via STDIN and must return a
single JSON object on STDOUT. No API key is hardcoded, no correctness grading.
The runner always emits one result per case, even on timeout or model errors.
"""
import argparse,json,subprocess,time,sys
from pathlib import Path

def main():
    a=argparse.ArgumentParser()
    a.add_argument('--inputs',required=True)
    a.add_argument('--out',required=True)
    a.add_argument('--run-id',required=True)
    a.add_argument('--timeout',type=int,default=90)
    a.add_argument('command',nargs=argparse.REMAINDER,help='Command after -- ; reads stdin JSON, writes one stdout JSON')
    x=a.parse_args()
    command=x.command[1:] if x.command and x.command[0]=='--' else x.command
    if not command:a.error('Provide adapter executable after --, e.g. -- node scripts/eval-adapter.mjs')
    cases=[json.loads(s) for s in Path(x.inputs).read_text().splitlines() if s.strip()]
    dest=Path(x.out);dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('w',encoding='utf-8') as out:
        for item in cases:
            start=time.perf_counter()
            try:
                p=subprocess.run(command,input=json.dumps(item),text=True,capture_output=True,timeout=x.timeout,check=False)
                if p.returncode:
                    result={'status':'ERROR','error':f'adapter exit {p.returncode}'}
                else:
                    try: result=json.loads(p.stdout.strip())
                    except json.JSONDecodeError:result={'status':'ERROR','error':'invalid JSON output'}
            except subprocess.TimeoutExpired:
                result={'status':'ERROR','error':'timeout'}
            except (OSError,ValueError) as e:
                result={'status':'ERROR','error':type(e).__name__}
            rec={'run_id':x.run_id,'case_id':item['case_id'],'benchmark':item['benchmark'],
                 'response':result,'elapsed_ms':round(1000*(time.perf_counter()-start),2)}
            out.write(json.dumps(rec,ensure_ascii=False)+'\n');out.flush()
    print(f'Wrote {len(cases)} non-graded response records to {dest}. To score, get independent judgments.')

if __name__=='__main__':sys.exit(main())

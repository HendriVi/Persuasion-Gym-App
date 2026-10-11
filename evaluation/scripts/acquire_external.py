#!/usr/bin/env python3
"""Opt-in official Git repository acquisition. Does not imply dataset licensing.
Default is metadata/list-only; explicit license acknowledgement required to clone.
"""
import argparse,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REG=json.loads((ROOT/'benchmarks/external/BENCHMARK_REGISTRY.json').read_text())['benchmark_entries']
BY_ID={r['id']:r for r in REG}

p=argparse.ArgumentParser()
p.add_argument('--list',action='store_true',help='list official refs and rights without network requests')
p.add_argument('--ids',nargs='*',choices=sorted(BY_ID),default=[])
p.add_argument('--rights-reviewed',action='store_true',help='you have reviewed rights of every requested source')
p.add_argument('--include-restricted',action='store_true',help='requires independent commercial data-rights approval')
p.add_argument('--destination',default=str(ROOT/'benchmarks/external/downloaded_UPSTREAM_DO_NOT_DISTRIBUTE'))
a=p.parse_args()
if a.list or not a.ids:
    for r in REG:print(f"{r['id']:<24} {r['commercial_use']:<17} {r['repo']}")
    if not a.ids:sys.exit(0)
if not a.rights_reviewed:p.error('Need --rights-reviewed after reviewing benchmark code AND dataset rights; default does not download.')
for id in a.ids:
    rec=BY_ID[id]
    if rec['commercial_use']=='RESTRICTED' and not a.include_restricted:
        p.error(f'{id} is marked RESTRICTED; acquire with appropriate permission before using --include-restricted')
    dest=Path(a.destination)/id
    if dest.exists():p.error(f'{dest} already exists; no overwrites allowed')
    dest.parent.mkdir(parents=True,exist_ok=True)
    print(f'Cloning upstream {id} (unverified dataset rights are still your responsibility) ...',flush=True)
    subprocess.run(['git','clone','--depth','1',rec['repo'],str(dest)],check=True)
    commit=subprocess.run(['git','-C',str(dest),'rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip()
    (dest/'LOCAL_ACQUISITION_RECORD.json').write_text(json.dumps({'source_url':rec['repo'],'commit':commit,
        'rights_notice':rec['license'],'commercial_use':rec['commercial_use']},indent=2)+'\n')
    print(f'Pinned acquired checkout {id}: {commit}')

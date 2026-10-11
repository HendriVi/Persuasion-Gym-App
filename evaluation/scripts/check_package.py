#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path
root=Path(__file__).resolve().parents[1]
counts=Counter()
for line in (root/'benchmarks/internal/CANDIDATE_CASE_INDEX.jsonl').read_text().splitlines():
    item=json.loads(line);counts[item['benchmark']]+=1
    assert item['gold_status']=='CANDIDATE_PENDING_INDEPENDENT_ADJUDICATION'
    assert item['release_eligible'] is False
    assert (root/item['source_path']).exists()
expected={'gold-corpus':96,'adversarial':80,'intent-discipline':64,'causal-discipline':80,'level-separation':80}
assert dict(counts)==expected,(dict(counts),expected)
assert len(json.loads((root/'benchmarks/external/BENCHMARK_REGISTRY.json').read_text())['benchmark_entries'])==9
print('PACKAGE CHECK PASSED: 400 provisional internal cases; 9 external benchmark references. NO RELEASE GOLD.')

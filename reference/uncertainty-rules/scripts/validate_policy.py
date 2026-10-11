#!/usr/bin/env python3
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
policy = json.loads((ROOT/'assets/uncertainty-policy.json').read_text())
example = json.loads((ROOT/'examples/uncertainty-examples.json').read_text())
required = ['epistemic_status','verification_status','evidence_strength','evidence_basis','person_specific_activation','person_evidence_mode','intent_status','dependency_status']
for k in required:
    assert k in policy['enums'] and policy['enums'][k], k
assert policy['hard_rules']['artifact_only_person_activation_max'] == 'CANDIDATE'
for a in example['assertions']:
    assert a['epistemic_status'] in policy['enums']['epistemic_status']
    assert a['verification_status'] in policy['enums']['verification_status']
    assert a['evidence_strength'] in policy['enums']['evidence_strength']
    assert a['person_specific_activation'] in policy['enums']['person_specific_activation']
    assert a['intent_status'] in policy['enums']['intent_status']
    assert 0 <= a['confidence'] <= 1
print('uncertainty policy validation: PASS')

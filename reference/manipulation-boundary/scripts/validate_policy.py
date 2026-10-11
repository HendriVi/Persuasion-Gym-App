import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
policy = json.loads((root/'assets'/'manipulation-policy.json').read_text())
examples = json.loads((root/'examples'/'boundary-examples.json').read_text())
required_dims = {
'DECEPTION','MATERIAL_OMISSION','INFORMATION_ASYMMETRY_EXPLOITATION','COERCIVE_PRESSURE',
'MANUFACTURED_URGENCY','DISPROPORTIONATE_EMOTIONAL_LEVERAGE','IDENTITY_SOCIAL_SANCTION_PRESSURE',
'CHOICE_ARCHITECTURE_OPACITY','EVIDENCE_CREDIBILITY_THEATER'}
assert set(policy['dimensions']) == required_dims
assert set(policy['overall_statuses']) == {'LOW_EVIDENCE_OF_MANIPULATION','SOME_MANIPULATION_RISK','SUBSTANTIAL_MANIPULATION_RISK','INDETERMINATE'}
assert policy['legal_firewall'] is True
assert all(e['overall'] in policy['overall_statuses'] for e in examples)
print('Manipulation policy validation: PASS')

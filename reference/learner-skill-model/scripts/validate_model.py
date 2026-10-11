#!/usr/bin/env python3
import json, sys
from pathlib import Path
try:
    import jsonschema
except ImportError:
    print('jsonschema is required', file=sys.stderr); sys.exit(2)
BASE=Path(__file__).resolve().parents[1]
schema=json.loads((BASE/'schema/user-skill-model.schema.json').read_text())
registry=json.loads((BASE/'assets/skill-registry.json').read_text())
valid_skills={x['skill_id'] for x in registry['skills']}
path=Path(sys.argv[1] if len(sys.argv)>1 else BASE/'assets/example-user-model.json')
obj=json.loads(path.read_text())
jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(obj)
errs=[]
attempt_ids=set()
for a in obj['attempts']:
    if a['attempt_id'] in attempt_ids: errs.append(f"duplicate attempt_id {a['attempt_id']}")
    attempt_ids.add(a['attempt_id'])
    for s in a['skill_ids']:
        if s not in valid_skills: errs.append(f"unknown skill {s}")
    for d in a['dimensions']:
        if d['skill_id'] not in valid_skills: errs.append(f"unknown dimension skill {d['skill_id']}")
        if d['skill_id'] not in a['skill_ids']: errs.append(f"dimension skill {d['skill_id']} not deliberately tested")
    should = (a['answer_key_status']=='FROZEN_VALID' and a['committed_before_feedback'] and a['assistance_level']=='UNAIDED')
    if a['mastery_eligible'] and not should: errs.append(f"attempt {a['attempt_id']} improperly mastery_eligible")
refs={a['attempt_id'] for a in obj['attempts']}
for s in obj['skills']:
    if s['skill_id'] not in valid_skills: errs.append(f"unknown SkillState {s['skill_id']}")
    for r in s['state_evidence_refs']:
        if r not in refs: errs.append(f"skill {s['skill_id']} missing attempt ref {r}")
for p in obj['recurring_error_patterns']:
    if p['occurrences'] < 3 or p['opportunities'] < 5: errs.append(f"pattern {p['pattern_id']} opened below recurrence threshold")
    for r in p['attempt_refs']:
        if r not in refs: errs.append(f"pattern {p['pattern_id']} missing attempt ref {r}")
if errs:
    print('INVALID')
    for e in errs: print('-',e)
    sys.exit(1)
print('VALID')

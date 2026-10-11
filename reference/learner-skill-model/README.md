# Persuasion Gym User Skill Model

Version: 0.1.0

This package implements the learner-state layer for Persuasion Gym. It records evidence about narrowly defined trainable skills, recurring error patterns, confidence calibration, assistance, delayed retrieval, and transfer. It explicitly forbids vague personality labels such as "gullible", "manipulable", or "bad critical thinker".

## Design principle

The model is an evidence ledger, not a personality profile.

`attempt -> scored dimensions -> skill evidence -> calibration -> recurring error pattern -> transfer/delayed evidence -> skill-state update`

## Contents

- `SKILL_MODEL.md` — normative specification
- `schema/user-skill-model.schema.json` — canonical machine-readable schema
- `references/skill-registry.md` — canonical trainable skill families
- `references/update-policy.md` — state update and promotion/demotion rules
- `references/calibration.md` — confidence calibration rules
- `references/transfer.md` — transfer evidence rules
- `references/error-taxonomy.md` — recurring miss taxonomy
- `assets/skill-registry.json` — machine-readable skill registry
- `assets/example-user-model.json` — complete example
- `scripts/validate_model.py` — schema + semantic validation
- `scripts/update_model.py` — deterministic attempt ingestion / evidence update
- `TESTING.md` — regression requirements

## Integration

Consumes scored attempts from `persuasion-training` and uses the same canonical distinctions as the Persuasion Gym common schema. It never creates or changes answer keys.

# Persuasion Rhetorical Structure Analysis

This package is the operational message-analysis skill for Persuasion Gym.

It converts persuasive artifacts into anchored canonical rhetorical annotations while preserving
strict boundaries between:

- message structure;
- factual truth;
- argument validity;
- psychological mechanism;
- audience state;
- manipulation;
- speaker intent.

## Files

- `SKILL.md` — normative agent behavior
- `references/analysis-protocol.md` — pass-by-pass annotation protocol
- `references/handoff-routing.md` — specialist routing rules
- `references/multimodal-analysis.md` — image/audio/video handling
- `assets/rhetorical-analysis-schema.yaml` — machine-readable interchange schema
- `TESTING.md` — regression tests

## Required project dependencies

- Persuasion Gym Canonical Ontology v0.1.0
- Persuasion Gym Canonical Rhetoric Taxonomy v0.1.0

## Position in the stack

```text
Raw artifact
    ↓
Rhetorical Structure Analysis  ← this package
    ↓
├── Critical Thinking
├── Fact-Check / De-Spin
├── Persuasion Mechanism Analysis
├── Manipulation Assessment
└── Systems Thinking
    ↓
Training Engine / Agentic Learning
```

The skill should be run before person-level mechanism inference because it provides the stable,
artifact-grounded feature IDs that later modules consume.

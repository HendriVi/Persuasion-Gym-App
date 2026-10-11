# Persuasion Gym — Canonical Rhetoric Taxonomy

Version: 0.1.0
Status: normative draft for specialist-skill development

This package defines the canonical **message-level vocabulary** for Persuasion Gym.
It answers one question:

> **What is present in the communicative artifact, and how is the message organized?**

It does **not** determine whether the message is true, logically valid, psychologically effective, manipulative, or intentionally deceptive.
Those judgments belong to other specialist layers.

## Files

- `TAXONOMY.md` — normative taxonomy and top-level rules.
- `references/feature-catalog.md` — canonical feature definitions and boundaries.
- `references/annotation-rules.md` — span-level and artifact-level annotation protocol.
- `references/foundations.md` — theoretical foundations and evidence notes.
- `assets/rhetorical-feature-schema.yaml` — machine-readable interchange schema.
- `TESTING.md` — regression tests and failure cases.

## Architectural position

```text
Artifact
  ↓
Rhetorical Structure Analysis
  ↓
Canonical Rhetoric Taxonomy  ← this package
  ↓
Argument Analysis / De-Spin / Fact Check
  ↓
Persuasion Mechanism Analysis
  ↓
Influence Systems Analysis
  ↓
Training Engine
```

The taxonomy is designed to be compatible with the Persuasion Gym Canonical Ontology v0.1.x. All taxonomy entries map to ontology layer L3 (`MessageFeature`) or to explicitly marked discourse/argument structures in L2.

## Core boundary

A message-level annotation may say:

> `authority_cue` is present in this segment.

It may not silently upgrade that into:

> authority increased trust, caused acceptance, or manipulated the audience.

Those are separate hypotheses requiring separate evidence.

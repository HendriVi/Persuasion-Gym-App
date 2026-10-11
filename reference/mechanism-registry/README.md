# Persuasion Gym — Psychological Mechanism Registry

This package defines the canonical person-level mechanism library used by Persuasion Gym.

It sits **between** message-level rhetoric annotation and systems-level modeling:

`Rhetorical feature -> candidate influence pathway -> psychological construct/mechanism -> internal response -> interpretation/belief/action`

The registry is deliberately conservative. A message feature can nominate one or more candidate mechanisms, but it cannot prove that any mechanism was active in a particular person.

## Files

- `REGISTRY.md` — normative specification and canonical registry
- `references/evidence-grading.md` — separate grading of effect reliability and mechanism specificity
- `references/mechanism-catalog.md` — operational entries and boundary conditions
- `references/feature-mechanism-crosswalk.md` — message features to candidate mechanisms; never a deterministic lookup
- `references/scientific-foundations.md` — key literature used to construct the registry
- `assets/mechanism-entry-schema.yaml` — machine-readable interchange schema
- `TESTING.md` — regression tests for scientific and ontological discipline

## Dependency order

This package assumes:

1. Persuasion Gym Canonical Ontology v0.1.0
2. Canonical Rhetoric Taxonomy v0.1.0
3. De-Spin / claim audit
4. Critical Thinking / argument analysis
5. Independent Fact-Check
6. Persuasion Systems Thinking
7. Persuasion Agentic Learning

## Central rule

**A robust effect is not the same thing as a settled mechanism.**

For example, numeric anchoring is highly replicable, but multiple explanations remain viable. The registry therefore records `effect_evidence` and `mechanism_evidence` separately.

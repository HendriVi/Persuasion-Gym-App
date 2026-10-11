# Persuasion Gym Common Structured Output Schema

**Version:** 0.1.0  
**Status:** canonical interoperability contract

## Purpose

This package defines the single machine-readable contract used to combine Persuasion Gym specialist outputs. It is the data layer between the specialist skills and the application.

The design goal is to preserve the distinctions that define the project:

`artifact → claim / argument → rhetorical feature → candidate psychological mechanism → person-level evidence → behavior → system dynamics → manipulation assessment → countermeasure → training`

No arrow is silently upgraded into a fact. Truth, argument validity, rhetoric, mechanism, person-specific activation, manipulation, system dynamics, and learner performance remain separately represented.

## Source of truth

`schema/persuasion-analysis.schema.json` is authoritative. JSON Schema Draft 2020-12 is used so the application can validate every specialist response before combining it.

Human-readable prose is secondary. `metadata.human_summary_is_non_authoritative` is required to be `true`.

## Architecture

The common object contains one shared artifact/claim/evidence layer and typed specialist modules:

- `artifact` + `claims` — shared referents;
- `rhetoric` — observable message structure;
- `argument` — claims, warrants, assumptions, gaps;
- `verification` — independent factual verification;
- `mechanisms` — candidate psychological pathways;
- `systems` — variables, relations, loops, delays;
- `manipulation` — separate multidimensional manipulation assessment;
- `countermeasures` — targeted resistance/intervention options;
- `assertions` — provenance-bearing analytical claims;
- `sources` + `evidence` — common evidence graph;
- `training` — optional learner attempt / scoring state;
- `routing` — unresolved dependency and re-analysis flags.

## Core rules

1. **Stable references.** Objects receive stable IDs. Specialist modules reference IDs instead of copying concepts.
2. **Assertions carry epistemic metadata.** Important inferences record origin skill, epistemic status, evidence strength/basis, factual verification status, confidence, scope, and alternatives.
3. **One specialist does not rewrite another specialist's results.** Contradictions create routing or re-analysis flags.
4. **Controlled enums beat prose labels.** Free-form explanation may accompany a record but cannot replace canonical status fields.
5. **Schema validation is necessary but not sufficient.** JSON Schema validates shape and enums; `scripts/validate_analysis.py` additionally checks reference integrity and cross-module invariants.
6. **Partial analyses are allowed.** Modules may contain no findings but must explicitly declare dependency status and limitations. Missing certainty must stay missing.

## Files

- `schema/persuasion-analysis.schema.json` — canonical schema.
- `references/id-and-reference-rules.md` — stable-ID and reference discipline.
- `references/status-enums.md` — canonical uncertainty/evidence vocabulary.
- `references/specialist-ownership.md` — which specialist owns which fields.
- `references/dependency-and-reanalysis.md` — how errors propagate without silent rewriting.
- `references/compatibility-mapping.md` — maps earlier skill-local status vocabularies into the common contract.
- `references/versioning-and-migrations.md` — schema evolution rules.
- `examples/simple-ad.analysis.json` — complete worked object.
- `scripts/validate_analysis.py` — structural + referential validator.
- `TESTING.md` — required regression tests.

## Integration rule

Every specialist skill should ultimately emit a fragment compatible with this schema, then the application merges validated fragments by stable ID. Do not parse free-form specialist prose as the primary integration mechanism.

# Phase 0 source-to-capability traceability

Updated 2026-10-11. **Source imported** means source availability only; execution and model validation remain pending. Exact canonical IDs/enumerations in `reference/` prevail over this roadmap.

| Contract | Canonical source | Runtime / acceptance status |
|---|---|---|
| L0–L8 layers and multi-layer contract | `PROJECT_SPEC.md`; `reference/ontology/`; `reference/common-schema/schema/persuasion-analysis.schema.json` | SOURCE_IMPORTED; validator integration NOT_IMPLEMENTED |
| Rhetorical cues (12 families) | `reference/rhetoric-taxonomy/`; `reference/rhetorical-structure-analysis/SKILL.md` | SOURCE_IMPORTED; live analyzer NOT_IMPLEMENTED |
| Argument logic/critical thinking | `PROJECT_SPEC.md`; `REQUIREMENTS.md` F-04; original Critical Thinking standalone source preserved offline | MODULE_NOT_IMPLEMENTED; standalone original not silently substituted |
| De-Spin | `REQUIREMENTS.md` F-05; original standalone DeSpin preserved offline; `reference/fact-check/SKILL.md` | MODULE_NOT_IMPLEMENTED |
| Independent Fact-Check and provenance | `reference/fact-check/SKILL.md`; `REQUIREMENTS.md` F-06, F-17 | MODULE_NOT_IMPLEMENTED |
| Psychological mechanism candidates and moderators | `reference/mechanism-registry/REGISTRY.md`; `reference/mechanism-analysis/SKILL.md` | MODULE_NOT_IMPLEMENTED; stimulus-only activation is CANDIDATE |
| Intent, manipulation and causal boundaries | `reference/manipulation-boundary/`; `CODEX.md`; original intent/causal test suites retained in restricted/offline source package, not imported as public runtime modules | MODULES_NOT_IMPLEMENTED; evidence gating mandatory |
| Influence systems / level separation | `reference/influence-systems-analysis/SKILL.md`; `reference/systems-thinking/SKILL.md`; `CODEX.md` | MODULES_NOT_IMPLEMENTED |
| Feedback composition and alternatives | `ARCHITECTURE.md`; `REQUIREMENTS.md` F-13 | NOT_IMPLEMENTED |
| Commit-first graded training | `reference/training/SKILL.md`; `reference/agentic-learning/SKILL.md`; `REQUIREMENTS.md` F-14 | NOT_IMPLEMENTED; no gold grading |
| Learner model / calibration / transfer | `reference/learner-skill-model/`; `REQUIREMENTS.md` F-15–F-16 | NOT_IMPLEMENTED; new competency IDs still PROPOSED |
| Social identity, belonging, identity reversal | `docs/features/social-identity-belonging/FEATURE_SPEC.md`, `exercises.json`, `ACCEPTANCE.md`; original mechanisms as above | SPEC_AND_SYNTHETIC_EXERCISES_IMPORTED; USER_RUNTIME_NOT_IMPLEMENTED |
| 400 historical candidate cases | `COMPLETENESS_AUDIT.md`; `EVALUATION.md`; offline source manifest | COUNTS_RECOVERED; restricted cases not in public repo or qualified gold |
| B-blind annotations / C adjudication | `EVALUATION.md`; `evaluation/instructions/DATA_GOVERNANCE.md` | VAULT_NOT_CONFIGURED; NOT_PERFORMED |
| Original nine external benchmark registry | `evaluation/benchmarks/external/BENCHMARK_REGISTRY.json` | REGISTRY_IMPORTED; datasets and license approvals PENDING |
| Strict release qualification | `evaluation/config/release.json`; `evaluation/scripts/release_gate.py`; `evaluation/instructions/RELEASE_POLICY.md` | CONTROLLER_SOURCE_IMPORTED; REAL_MODEL_NOT_EVALUATED; RELEASE_BLOCKED |
| Security, deployment, human approvals | `ARCHITECTURE.md`; `REQUIREMENTS.md` S-01–S-12; `DECISIONS.md`; ADR-0001/0002 | OPEN; NOT_IMPLEMENTED |

**Verification:** source-integrity script checks 74 declared public-origin paths against SHA-256 in 316-member manifest; transport check separately confirmed all 108 source package entries matched their original Git blob SHA-1. These measures do not demonstrate software feature completeness. Add future acceptance tests to respective specialists' ownership after ADR approval, preserve the core canonical release gate unmodified.

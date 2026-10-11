# Social identity and belonging — implementation acceptance

Feature approved by user: 2026-10-11. Application runtime: **NOT IMPLEMENTED**. This is a phase-aligned acceptance contract for later integration, not a report that tests have already passed.

## Acceptance scenarios

### A. Specialist analysis preserves boundaries

- **Given** an utterance "Everyone who genuinely cares about human rights supports Policy P", **when** the rhetorical specialist analyzes it, **then** it can anchor the moral-identity cue exactly in the input and distinguish claim/warrant gaps from rhetorical labeling.
- **Given** that utterance alone, mechanism output may include `SOC.social_identity_referent_influence`, `SOC.injunctive_norm_social_sanction`, or `MOT.motivated_reasoning` as *candidates*, with alternatives/moderators, but cannot assert actual listener activation, private speaker intent, factual falsity, persuasion success, or manipulation.
- **Given** explicit group approval and exclusion, **then** distinguish injunctive social sanctions from descriptive prevalence, and do not automatically assume internal belief change.
- **Given** sincere optional invitation to group cooperation, **then** admit a benign persuasive interpretation and avoid an automatic manipulation verdict.
- **Given** a politically congenial and a politically uncongenial version with identical argumentative structure and same verified evidence, **then** apply the same analytic standards and confidence thresholds.
- **Given** group affiliation that genuinely informs a source's relevant expertise, **then** consider legitimate evidential relevance; no rule says all group information must be ignored.

### B. Training interaction

- The user answers unassisted, provides pre-feedback confidence, and commits to the response **before** seeing analysis or mirrored comparisons.
- A frozen attempt records the item's version, role/condition (non-sensitive synthetic task metadata), assistance status, domain, response, confidence and timestamp.
- Public exploratory items never change mastery, contribute to release metrics, or display authoritative correctness grades; no private answer key is stored in the frontend or this repository.
- Feedback separates the message cue, argument/evidence quality, candidate mechanisms, intent uncertainty, manipulation boundary and plausible alternatives. Feedback can explicitly say 'insufficient evidence'.
- For mirror pair `sib-neutral-group-01`, synthetic evidence, policy wording, questions and role stay identical; only the fictional endorsing group changes. Order is counterbalanced in real delivery.
- A larger evidence-changing variant must *allow* justified belief revision; a constant stance regardless of evidence is not scored as independence.
- Do not infer psychological susceptibility from changed answers. Report only task-level differences and stated uncertainties.
- A qualified future learner-skill update requires specialist-validated independently adjudicated locked keys and obeys the canonical state machine, evidence exclusions and delayed transfer checks.
- No collection/storage of political views, protected identity, religion, mental health or inferred group affiliations.

### C. Adversarial and scientific release gates

Evaluate recognition/explanation separately from person-level mechanism attribution. Include (1) accurate but identity framed; (2) false claim without identity pressure; (3) benign identity appeal; (4) overt threatened exclusion; (5) private vs public compliance; (6) uncertainty and alternative-mechanism requirements; (7) policy evidence relevant vs merely affiliative cues; (8) source credibility legitimately informative; (9) ideologically mirrored content; and (10) manipulated instructions seeking private holdout keys.

Public exercise seeds are **not gold**, **not holdouts**, and **not evidence of validated performance**. Independent human B annotation and C adjudication, confidential test partition, original release-gate and frozen five-run standards remain mandatory.

## Immediate Phase 0 source checks and future ownership

- Verify and import only public-safe original bootstrap; no offline-restricted archive, adjudication ledger, gold constraints or privileged candidate labels.
- Reconcile `docs/features/social-identity-belonging/FEATURE_SPEC.md` with the original source hashes and the canonical schema/skill registry.
- Track this feature in status/traceability after canonical documentation import; the current branch must not silently claim the prerequisite source import has occurred.
- At implementation time, the rhetoric owner tests L3 cues; argument/fact owners test L2 evidence; mechanism owner tests L4 candidate-only and moderators; training owner tests commit-first/confidence and mirror conditions; learner-model owner tests invalidation and privacy; evaluation owner tests all release restrictions.
- Frontend/backend, hosting, storage/auth and model provider remain OPEN decisions. Do not choose them in this curriculum PR.

## Status at handoff

- [x] Requirement and implementation contract drafted.
- [x] Six public, fictional, ungraded practice seeds, including one matched pair, authored.
- [ ] Canonical public bootstrap imported into actual GitHub mainline and source integrity audited.
- [ ] Live specialist analyzers or app screens connected.
- [ ] User training responses, session persistence, scoring, or learner-skill updates operational.
- [ ] Original benchmark qualified or production master enabled.

**Next engineering milestone:** finish the canonical public-safe bootstrap import and Phase 0 provenance audit; implement this feature in the existing training pipeline after its contracts and technology choices are settled.

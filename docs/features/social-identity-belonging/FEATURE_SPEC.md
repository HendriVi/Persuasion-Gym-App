# Social identity, belonging, and independent judgment

Status: **feature specification and public-safe exploratory curriculum added; application runtime NOT IMPLEMENTED; graded mastery NOT ENABLED; release BLOCKED**. Approved feature direction by repository owner on 2026-10-11. This file supplements, and never replaces, the frozen canonical references.

## Purpose

Teach learners to recognize when approval, belonging, group identification, loyalty, or anticipated exclusion *may* influence how a message is understood. The educational outcome is improved evidence evaluation and uncertainty calibration even where affiliation favors the message. The objective is independent judgment, **not** indiscriminate resistance to social norms, group affiliation, or moral language.

Observable rhetoric must remain separate from argument quality, independently verified facts, candidate person-level mechanisms, actual reactions, intent, manipulation assessment, and system dynamics. A persuasive message can be truthful, ethical, and identity-relevant at the same time.

## Canonical grounding — do not create a second ontology

Follow `PROJECT_SPEC.md` L0-L8 and `reference/common-schema/schema/persuasion-analysis.schema.json` after verified source import. Relevant layers: L2 claims/warrants, L3 cue identification, L4 candidate mechanism and moderators, L5-L6 only evidenced individual response/behavior, L7 social norm and sanction dynamics, L8 learner training. Never promote an L3 cue to an observed L5 response.

Existing mechanisms from `reference/mechanism-registry/REGISTRY.md`:

- `SOC.social_identity_referent_influence`: candidate when self-relevant group identity and prototypical norms are plausible; effect evidence E3, mechanism evidence M2. Source identity cue alone does not prove activation.
- `SOC.injunctive_norm_social_sanction`: group approval/disapproval or anticipated sanctions; E4/M2. Public compliance is not evidence of private attitude change.
- `SOC.descriptive_norm_inference`: perceived prevalence and social proof; E4/M2. Popularity is not truth.
- `MOT.motivated_reasoning`: directional or accuracy goals may affect argument evaluation; E3/M2. Disagreement is not proof of motivated reasoning.
- `MOT.cognitive_dissonance_consistency`: a distinct candidate only where relevant inconsistency/commitment is supported; E3/M2.

Use canonical rhetorical social/identity/norm features and existing competencies including `RHE.detect_feature`, `ARG.warrant_identification`, `MEC.alternative_mechanisms`, `MEC.activation_ceiling`, `RES.counterframe_generation`, `META.confidence_calibration`, and `META.answer_revision`.

Proposed future competencies, subject to registry review and versioned schema updates: `META.identity_cue_invariance` (consistent evidence judgments across matched irrelevant identity-cue changes), and `RES.social_pressure_decoupling` (separate approval/sanction considerations from evidential justification). **Do not treat these as existing canonical skill IDs or write them into learner profiles yet.**

## Learning progression (five stages)

1. **Recognize**: locate exact identity, loyalty, belonging, group approval or sanction language. Identify whether the message describes a descriptive norm, invokes an injunctive norm, or asserts moral eligibility.
2. **Explain candidates**: reconstruct the intended argument or warrant and name plausible mechanisms, boundary conditions and alternatives. Give the answer **candidate** for an unobserved personal response.
3. **Discriminate**: distinguish valid arguments and accurate claims from rhetorical framing, and coercive sanctions from benign appeals or sincerely held group commitments. Require justified `INDETERMINATE` where evidence is insufficient.
4. **Identity reversal**: evaluate the same evidence packet twice, varying only irrelevant group affiliation, group endorsement, or public versus private presentation where controlled. Freeze each unaided evaluation and confidence before any feedback. Compare within-person evaluations without assuming differences prove a cause.
5. **Transfer and delayed verification**: switch domain and surface form (workplace, health communications, consumer marketing, civic messaging, relationships), interleave with legitimate identity persuasion, and test retention. Consistency across relevantly matched claims matters more than a one-off correct label.

## Training protocol

Use the existing `reference/training/SKILL.md`, `reference/agentic-learning/SKILL.md`, and learner-skill-model governance:

1. Show case and any designated *synthetic* evidence card; request independently written answers to: What is the claim? What is the evidence? What is the identity cue? What mechanism is plausible? What cannot be inferred? What else could explain it? What would change your judgment?
2. Require a pre-feedback confidence estimate. Freeze the unaided response with item version, context, assistance and timestamp; do not provide corrective hints in scored attempts.
3. Reveal mechanistic explanations only **after** commitment. When no independently locked, specialist-validated key exists, show exploratory feedback only and no accuracy, mastery, or calibrated correctness score.
4. For a mirror, keep policy and evidence *identical*. Change only specified superficial source/group signal; counterbalance order and role assignment. Pre-register which variation is evidentially irrelevant. A real source's identity may contain valid credibility information; don't classify all sensitivity to source as bias.
5. On a qualified training pipeline, mark precisely supported error types (e.g. cue not noticed, conflation of rhetorical feature and actual activation, unjustified intent attribution, falsehood inferred from identity cue, overly broad manipulation inference, missed alternative, uncalibrated confidence). Do not infer a stable person trait or ideological vulnerability.
6. Schedule discriminative practice and later interleaved/transfer/delayed retrieval. Changes to learner state only on `LOCKED_ADJUDICATED` eligible keys according to canonical update policy.

## Safety, privacy, and evaluation

- Do not store political affiliation, ideology, religion, ethnicity, sexuality, diagnoses, or inferred in-group/out-group identity. Fictional role assignment for a practice case is transient task metadata and should not become a psychological profile.
- Avoid normative grading of a political/policy belief as such. Grade supported reasoning processes on the validated case instead of ideological agreement.
- Preserve provenance, observation vs interpretation, uncertainty, alternative mechanisms and the manipulation boundary. No mind-reading, proof of unconscious mechanisms, or causal claims from uncontrolled reversals.
- Public `exercises.json` contains **fictional, ungraded teaching stimuli with NO hidden answers**; it is not an adjudicated benchmark or a collection of gold labels.
- Never place private answer keys, holdout cases, annotated hidden test metadata, or an offline benchmark vault in this public repository. Mirror invariance is a planned test slice; it has **no qualified score**.
- Existing release controls are unchanged: five frozen runs, per-competency/per-slice adjusted one-sided 95% Wilson lower-bound gate >=.95, 0.97 target, calibration and critical-error safeguards, independent B/C annotation/adjudication. Release stays BLOCKED.

## Minimal implementation dependencies and ownership

Phase 0: import and verify the **public-safe** `repo-root/` bootstrap with provenance and original hashes; complete source audit and existing OPEN ADRs. This feature spec can be reviewed now but cannot override that phase gate.

Phase 1: register the track with canonical reference ids, add reviewed skill IDs only with explicit registry/schema versioning, add independently authored public exploration fixtures and negative cases, validate schema and discrimination.

Phase 5 (after prerequisites): connect training delivery, persisted pre-feedback response/confidence, mirrored item selection, optional descriptive feedback, protected gold service, eligible learner-skill updates, transfer and delayed retrieval.

Do not select a frontend/backend, create a standalone duplicate mechanism registry, silently amend original frozen references, activate production grading, or report a 95–97% score.

## Source provenance

The linked original source files were read from the supplied preserved package `Persuasion-Gym-Codex-Complete-Offline-Implementation-Package.zip`, limited to its explicitly public-safe `repo-root/` subtree. This proposal contains no offline-restricted members. SHA-256 of extracted text sources:

- `PROJECT_SPEC.md`: `ecb3d41d37aab99e3adb99449064075e34a2e862ba87c5b59964e6d600ad3b2f`
- `DECISIONS.md`: `d516f0e95658b9980dc120ba4a48f70dd6d115b16141c06abc8f409fa86f6c76`
- `reference/training/SKILL.md`: `d1e69d47dc75544e02af9d32f6948901a28a7e61b7ab298d1d3a71314087bb8a`
- `reference/mechanism-registry/REGISTRY.md`: `c58d67fa17dcfb76947bfc0ad2e1317295edd2a18f618098a941cf42e5869de9`
- `reference/learner-skill-model/SKILL_MODEL.md`: `8af4fb625c28eaebfa5beb9dc950cc3566f3154f01356ecc750c5c1dde131f2d`
- `reference/learner-skill-model/assets/skill-registry.json`: `04045f0019b2ff69a1b5a79237478326bdf19bc137a464358bc0b9c39959f500`

Source SHA records are traceability pointers until the normal Phase 0 integrity check authenticates the complete bootstrap against its canonical manifest.

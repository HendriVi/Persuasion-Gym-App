# CODEX.md — standing engineering instructions for Persuasion Gym

**Target GitHub repository:** `HendriVi/Persuasion-Gym-App`. This repository is the final application implementation. The older `HendriVi/persuasion-gym` repository is NOT an input/codebase/dependency unless a specific named file is explicitly approved and mapped in a decision record. Do not automatically clone, compare for convenience, cherry-pick or borrow patterns from it.

## 0. Non-negotiable precedence and file authority

1. Source-of-truth conversation + its frozen first-party original artifacts (`SOURCE_ARTIFACT_MANIFEST.json` + original source checksums). If they conflict, **flag the exact conflict**; don't invent resolution.
2. `PROJECT_SPEC.md` — concepts and scientific requirements; original ontology/taxonomy/registry/policies in `reference/` prevail on exact definitions and enumerations.
3. `EVALUATION.md` + original benchmark controller `SKILL.md`, `config/release.json`, `scripts/release_gate.py` — authoritative release gate; no weaker local scorer.
4. `ARCHITECTURE.md` — interfaces, ownership, zones, security and dependency graph.
5. `REQUIREMENTS.md` — functional/non-functional/safety acceptance.
6. `DECISIONS.md` — records which choices are genuinely settled vs OPEN; no assumptions fill OPEN fields.
7. `IMPLEMENTATION_PLAN.md` + `SOURCE_ARTIFACT_MANIFEST.md` + `COMPLETENESS_AUDIT.md` — phase ordering and provenance.

**This CODEX.md is BUILD governance, not the blocked master `persuasion-gym/SKILL.md`.** Original evaluator `SKILL.md` is evaluation governance only. Do not create/enable true master until specialist qualification passes.

## 1. Before EVERY task

1. Confirm repository identity, branch, current commit, working tree and whether repo is public. If public, do not import secrets/holdout/first-pass candidate answers.
2. Read the relevant original source `SKILL.md` + canonical definitions for the task, not just prose summaries. Verify SHA; cite relative paths in commit/PR.
3. Reconcile task with phase, blocked status, required tests and exact output artifacts. If a requirement is not supported by sources, report `UNDECIDED` and propose options *without adopting one silently*.
4. Inspect existing code only in **THIS** repo. Do not assume old app runtime or stack.
5. Implement smallest vertical slice that satisfies an approved milestone; avoid framework proliferation.
6. Run actual tests against changed components. Write tests FIRST for fragile scientific boundaries. Do not claim tests ran if they did not.
7. Update status tracker, requirement coverage, decisions (only if approved), source hashes and blockers.

## 2. Scientific and epistemic rules — code MUST enforce

- Rhetoric ≠ verified fact ≠ argument validity ≠ candidate psychological mechanism ≠ observed audience activation ≠ intent ≠ manipulation ≠ system outcome.
- Rhetorical aggressive true message can be legitimate; emotionally neutral choice architecture can be manipulative; real urgency may be true; fabricated authority can coexist with bland presentation.
- One cannot infer `IntentStatus` from who benefits, content, emotion, truth/falsity or perceived political congeniality; explicit/documented facts may support a scoped status. Default `UNKNOWN`.
- No person-specific psychological activation from message alone: default `CANDIDATE`. Do not label precision-weighting, amygdala activation or other mechanisms “proven” without suitable measurement/intervention.
- Observational/longitudinal associations and model diagrams do not identify a causal arrow. Random assignment may support scoped **total effect** but not automatic mediator/mechanism identification; do not conflate statistical mediation and mechanism.
- Factual verdict requires independently retrieved canonical external evidence, logged and verified. Model self-judgment, source-looking URLs, repeated affiliated news reports, and fabricated quotes are not evidence.
- A false claim or fallacy ≠ manipulation. Evaluate independent autonomy/materiality dimensions; accept `INDETERMINATE`.
- Politics mirrored inputs: equally structured messages must receive symmetrical analysis. No ideological preference encoded in labels/rules.
- When required evidence missing, return explicit insufficiency, pending dependency or provisional status; do not fill with confident prose.
- Follow exact canonical status enums/schema with versioned adapters. Every analysis assertion includes evidence origin; exact anchored text must match input.
- Never give privileged benchmark labels, design manifests or adjudicator records to the inference agent.

## 3. Required component boundaries

Each specialist owns only named fields. Make immutable input snapshots, stage IDs, source version/hashes and one authoritative merger. Cross-stage promotion requires explicit rule and evidence threshold. Compose natural-language reports from validated evidence objects; prevent report writer from fabricating or escalating conclusion statuses. If fact-check finds a material correction, invalidate and re-run dependent argument/mechanism/manipulation/system analysis. Verify negative cases and counterexamples.

## 4. Coding and tool use

- Use branch + PR for each phase/milestone; no blind bulk commits to main. No force-push/rewrites of published history.
- Keep deterministic logic testable without network. Mocks/fixtures labeled synthetic; always test that they FAIL the real release gate when gold is absent.
- Use pinned versions and reproducible development commands; robust timeouts/retries for model and retrieval, no uncontrolled model loops or hidden tool calls.
- Avoid multiple competing orchestration stacks unless evaluation demonstrates a need. Tools considered in source: Promptfoo, Inspect AI, Argilla, Cleanlab, FActScore, Langfuse, Pandera, DVC, irrCAC; DSPy, PaperQA, STORM, GPT Researcher, Loopy, PySD, SDEverywhere are reference candidates only until individually approved/license-reviewed. None automatically guarantees better reasoning.
- Preserve exact native external benchmark metrics; do not relabel F1/composite as general 97% accuracy.
- Any DB/storage/auth/provider/hosting decision requires an ADR when absent from source. Default to *reversible* prototypes and mock data; never hardwire secrets or billing.
- High-risk areas: authentication, user-sensitive content, commercial dataset rights, annotation independence, prompt injection, model/tool provenance, PII retention, benchmark leakage, production feature controls.

## 5. All evaluation/release constraints

`RELEASE=BLOCKED` unless all are independently confirmed:

- ≥1600 unique `LOCKED_ADJUDICATED` holdout cases, ≥200 per one of 8 competencies, ≥100 per six challenge slices, ≥150 per six high-risk cross-slices, ≥30 distinct families in **each** cell; sufficient power and family dependence audit.
- Five complete preregistered frozen runs with same exact model/prompt/pipeline/rubric/manifest versions and distinct seeds; all attempts accounted for, missing/error/abstain=wrong in strict primary metric.
- Every competence/slice/cross-slice in every run has Bonferroni-adjusted one-sided 95% Wilson **lower bound ≥0.95**; 97% target same semantics, later 98/99 require new version and enough new held-out evidence.
- Zero **observed** critical failures in permitted categories and per-run 10-bin ECE≤0.05.
- Independent A/B annotation and C adjudication, multiple valid answers where justified, authentic hashes and review signatures. No LLM self-scoring.
- Independent authoritative source verification. Holdout leakage and tuning on holdout invalidate release claim.
- Protected deployment, signature/attestation tied to exact artifact and human approval. `PERSUASION_VALIDATED_STACK` OFF by default and fail-closed.

Do not implement a looser duplicate scorer. Original gate must be used unchanged unless a reviewed policy change specifically authorizes an upgrade. GitHub Actions jobs passing, schema validation or fake-positive fixture never mean the AI is ≥95% accurate.

## 6. Commit-first training rules

Show item and ask user to commit before revealing analysis. Store pre-feedback confidence, assistance/hints, item/key version, domain/modality, error-code, delayed verification and transfer data. A provisional key is not allowed to mutate performance/mastery. Model behavioral errors (`INTENT_OVERATTRIBUTION`, `ASSOCIATION_TO_CAUSATION`, `CROSS_LAYER_CONTAMINATION`, etc.), not fixed traits or sensitive identity/political orientation. Progress through actual eligible performance with the original state machine, not arbitrary percentage bumps.

## 7. Benchmark confidentiality

The ORIGINAL all-in-one ZIP contains **private** and **holdout** files. The **entire ZIP must never be committed** to this public repo or its public CI artifact caches, used in client assets, supplied to Codex prompts, or sent to the model under test. It is held offline for a trusted human custodian and extracted into a separately access-controlled evaluator vault when provisioned. `offline-restricted/` in a local export is NOT a deployable application directory. Reference paths under `vault://` are *logical*, not actual automatically configured storage.

If the user asks to upload hidden data to a public repo, pause and explain leakage. A repository visibility change to private is a separate user-controlled action; even then design role separation first.

## 8. Definition of DONE and truthful status language

DONE requires a commit/PR, source trace, relevant tests executed, actual CI pass and owner signoff for phase. NOT EVALUATED and BLOCKED are not failures, just unpassed scientific gates. NEVER claim “95% achieved”, “97% reliable”, “gold”, “validated full specialist stack”, “fact-checked”, or “master skill implemented” without primary proof. Any conflict between file sets -> raise documented `SOURCE_CONFLICT`, do not guess.

## 9. Task report format (mandatory, concise)

```
Scope completed: [files and commit/PR]
Source authority: [exact docs + hashes]
Implemented behavior: [what actually runs]
Verification: [commands + real results; not run marked not run]
Benchmark status: NOT_EVALUATED | BLOCKED | PASS_95 | PASS_97 | ...
Blockers/missing approvals: [concrete]
NEXT user action: [only one, nontechnical, if needed]
```

## 10. First-task restrictions

The FIRST Codex prompt deliberately requests **read-only inventory + documentation provenance + phase-0 scaffold plan**. Do not run a model, choose arbitrary frontend tech, copy old source, ingest third-party datasets, score private gold, enable flag, invent a master skill or declare a successful benchmark. Build only after the reconstruction/completeness audit is acknowledged.

# Persuasion Gym — dependency-ordered implementation plan

**Actual target:** `HendriVi/Persuasion-Gym-App` (initially empty). Do NOT clone/copy the unrelated older app by default. **First Codex task:** inventory and put governance/contracts in place, not model building. Changes occur in small reviewable branches. Maintain an honest checkbox tracker and link each completed requirement to a test/log/commit.

## Phase 0 — Source reconstruction, public/private partition and decisions (NO blind coding)

- [ ] Verify complete input package manifest, original 316-member benchmark ZIP SHA256, hashes for all individual first-party source archives, source document headers, and available independent standalone `DeSpin.md` / `Critical Thinking .md`.
- [ ] Verify this new repo is the sole implementation target and inspect it. If public, do not add any gold, hidden split design, calibration/holdout or private documents. Keep `PERSUASION_VALIDATED_STACK` disabled.
- [ ] Commit this seven-document specification, `CODEX.md`, `AGENTS.md`, `REPO_TREE.md`, `SOURCE_ARTIFACT_MANIFEST.json/.md`, and `COMPLETENESS_AUDIT.md` **without restricted payloads**.
- [ ] Record unresolved decisions via ADRs: UI framework, server/inference runtime, hosting, model/provider, user auth, storage, billing (if needed), privacy/retention, supported languages, commercial data rights and reviewer identity/independence. Do not silently import them from the old repo.
- [ ] Add `docs/STATUS.md` with gates: `DESIGN_RECOVERED`, `BUILD_IN_PROGRESS`, `MODEL_NOT_EVALUATED`, `RELEASE_BLOCKED`.
- **Exit:** source coverage auditable; restricted files absent from git; no accidental master persuasion skill/95% claim; explicit ADR queue.

## Phase 1 — Faithful contracts/ontology and module owner tests

- [ ] Import ORIGINAL canonical ontology, taxonomy, mechanism registry, manipulation policy, uncertainty rules and schema from verified first-party material, preserving original file and SHA.
- [ ] Generate runtime validators/types as projections *from* source schema. Test every enum (`EpistemicStatus`, `VerificationStatus`, `ActivationStatus`, `IntentStatus`, etc.), required fields and unknown/null semantics. Do not substitute a shorter generic object.
- [ ] Implement artifact IDs, immutable segments, exact-text anchors, `AnalysisAssertion`, source/evidence links, stage-ownership matrix and dependency/invalidation status.
- [ ] Test political mirror/contrast group handling; input poison separation; absent evidence remains `UNVERIFIED`/`UNKNOWN`/`CANDIDATE`, not a decided label.
- **Exit:** genuine canonical JSON Schema valid fixtures; each specialist accepts/returns stage data without writing another layer; contract snapshot tests.

## Phase 2 — Minimal runnable vertical slice (flagged preliminary)

- [ ] Choose the least risky reversible full-stack implementation via ADR; create a bootable authenticated local web app with API and server-side model credentials only; test CI build, security baseline, accessibility.
- [ ] Implement *no-gold* Analysis workflow: submit artifact → source/claim decomposition → bounded rhetorical anchors → provisional argument scaffold → mechanism candidates → uncertain systems/manipulation → uncertainty/evidence report.
- [ ] Make evaluation-stage unavailable for user scoring until a source answer key is approved. Mark reports clearly `PRELIMINARY_UNVERIFIED`. Do not call a LexicalRegex detector a full specialist model.
- [ ] Add credible “what is observed / what might happen / what must be verified” UI and alternatives, with no speaker mind-reading.
- **Exit:** first end-to-end usable preliminary report; no secret/holdout leakage or false verification; passed UI tests.

## Phase 3 — Specialist engine with proper routing

- [ ] Implement owner modules for Rhetorical Structure, Critical Thinking, De-Spin, Fact-Check, Mechanisms, Systems, Intent, Causal and Manipulation; cross-layer audit and report composer. Read their actual `SKILL.md`/policy before coding, use exact IDs.
- [ ] Execute independent/parallel stages where DAG allows; freeze observations before fact check; source checks can invalidate dependent results and force targeted rerun.
- [ ] Use bounded/typed model outputs with tool access by least privilege, quality/latency budgets and robust refusal/fallback. Never let a model create a verified citation without successful source retrieval.
- [ ] Add targeted intent-overclaim, causality, layer separation, mirror symmetry and controlled aggressive-but-true/nonmanipulative persuasion tests.
- **Exit:** fully connected specialist logic in nonvalidated test environment; unit/integration tests; **still no 'qualified' claim**.

## Phase 4 — Fact-check provenance and safe external references

- [ ] Implement authoritative source discovery and direct retrieval, dated evidence ledger, citation integrity, contrary evidence checks and statuses per claim.
- [ ] Preserve closed-world synthetic packets and real-world external source evidence as separate modes. Audit URLs, excerpts, data/publish date, publisher, downstream premise corrections.
- [ ] Review rights/terms for fetched third-party data; configure redaction and retention controls.
- **Exit:** fixtures with supported, contradicted, partially qualified, missing and outdated evidence; zero fabricated 'verified' claims in controlled tests.

## Phase 5 — Commit-first training + user skill model

- [ ] Import original attempt schema, skill registry and update policies. Implement commit-first independent answer+confidence+assistance, freeze before feedback.
- [ ] Integrate verified answer-key gating and exact mistake codes; provisional/unadjudicated tasks train exploratorily but do not mutate scored mastery.
- [ ] Add criterion-based skill states, eligible independent opportunities, per-skill calibration/ECE, recurring miss statistics, near/cross-domain/cross-modality/far transfer and delayed review.
- [ ] Exercise scheduler optimizes explicit weak skills and transfer, not identity/political profiles or streak addiction; show understandable progress rationale.
- **Exit:** deterministic event-level tests, key version rollback tests, cross-domain transfer tests; no global 'gullible' scores.

## Phase 6 — Benchmark infrastructure (PRIVATE gold separated)

- [ ] Keep public release-controller source/config and test harness in evaluation service; keep **private** first-pass labels, gold candidates, design manifests, raw hidden holdout, annotator histories and signing credentials in separately protected vault.
- [ ] Verify original package manifests/hashes and batch JSONL adapter using real pipeline. Stub results `UNAVAILABLE` are never passed as model results.
- [ ] Validate split/family isolation and safeguards against benchmark exposure in CI artifacts/browser/network/model tool data.
- [ ] Install authorized external datasets and official scoring scripts *only after license review*; record native metrics + mapping limitations.
- **Exit:** scripts/check_package + six original release-controller fixtures (or tests as actually shipped) pass; fail-closed demo BLOCKED; real adapters emit complete unscored predictions.

## Phase 7 — Independent annotation, adjudicated gold, statistical power

- [ ] Freeze guide, original 400 candidates and all future new items. Enforce B blindness to A/model/hidden pair design; third adjudicator C + disagreement/audit ledger.
- [ ] Audit/update the legacy blinding/adjudication scripts, which might not cover real label paths or all promotion gates. Independently validate first-pass and locked schema.
- [ ] Construct **new distinct** examples/sources sufficient for 1,600 unique gold and per-competency/slice/intersection/family minima; assess actual statistical power and sample-cluster dependence before use.
- [ ] Lock a pristine holdout, version hashes, accepted alternative answers and independent judges; maintain a separate development/calibration set.
- **Exit:** signed `LOCKED_ADJUDICATED` manifest, no leaked keys, sufficient sample breadth, explicit sample-size/power report.

## Phase 8 — Actual model evaluation and systematic improvement

- [ ] Freeze exact model, prompt, provider, pipeline, schema, evaluation code, rubric, holdout hash; run **five complete predeclared executions**.
- [ ] Independent scorers generate one judgment per (run, case) including all abstentions/failures and critical errors; no model self-grading.
- [ ] Run unchanged `release_gate.py` on required 8 competencies, 6 slices and 6 cross-slices; 95% multiplicity-adjusted LCB each, zero observed critical errors and ECE≤.05 all runs.
- [ ] If BLOCKED, only change against development failures, run ablations and differential regression, **retire inspected holdouts**, then evaluate new frozen candidate with fresh independent holdout.
- [ ] Complete supplementary external-native task scores and public model bias/safety and multilingual checks where licensed.
- **Exit:** reproducible report showing qualification or explicit blocked reasons. Never optimize to a lucky five-run selection.

## Phase 9 — Release, master skill, monitoring

- [ ] Only after qualification: author the true master `persuasion-gym/SKILL.md` from **qualified** stage contracts and approved prompt/pipeline hashes, review all ownership and gating.
- [ ] Independent reviewer signs attestation; validated feature flag only enables exact approved binary/model/prompt/manifest fingerprints.
- [ ] Deploy monitored app with error alerts, latency/cost, source integrity, slice drift, feedback and rollback on critical issues.
- [ ] Promote 97%, later 98%, 99% only with new policy version, holdout and statistically adequate runs; qualification levels are not marketing promises about every future case.
- **Exit:** production release authorized, continuous evidence and rollback.

## Progress accounting

No phase above may be marked complete because a Markdown, ZIP, dummy script or beta pull request *exists*. Evidence of an actual milestone must include relevant SHA/commit, tests, who judged it, release status and new blockers. Prior work has created the research and evaluation artifacts, **not** independently qualified the final app. Update `docs/STATUS.md` and the single active milestone per PR. Human owner is not expected to run shell commands.

## What Codex should do FIRST

Read `CODEX.md`, this plan, `EVALUATION.md`, `SOURCE_ARTIFACT_MANIFEST.md`, `COMPLETENESS_AUDIT.md`; run a read-only inventory of the new repo and proposal for Phase 0. Do not import the old beta app. Check public/private boundary before any benchmark extraction. Then make only the Phase 0 docs/provenance and validation/CI scaffolding approved in the first prompt; keep actual implementation changes for the next scoped PR.

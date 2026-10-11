# Persuasion Gym — decisions, binding constraints and open questions

Use this as an anti-redesign log. A status of **ADOPTED** means the conversation and original artifact support the principle, **OPEN** means no binding technical selection was made, and **GATED** means design exists but actual activation/claim is prohibited pending evaluation. Do not convert examples or proposed repos into decisions without review.

| ID | State | Decision / rule | Rationale and implications |
|---|---|---|---|
| D-001 | ADOPTED | The new `HendriVi/Persuasion-Gym-App` repository is **the** target | User explicitly disallowed treating older repo as foundation. |
| D-002 | ADOPTED | Conversation and original frozen artifacts are source of truth | Cite exact source SHA and flag conflicts; no silent reauthoring. |
| D-003 | ADOPTED | Keep ontology L0–L8 and canonical 16+ root schema fields | Precise ownership, tracing, evidence and extensibility. |
| D-004 | ADOPTED | Rhetoric, argument validity, factual status, mechanism, intent, manipulation and systems causality are independent | Prevent one label contaminating others. |
| D-005 | ADOPTED | Mechanism activation cannot be inferred from stimulus-only passage | Use `CANDIDATE` until person-specific evidence supports higher level. |
| D-006 | ADOPTED | No mind-reading intention | Use EXPLICIT/DOCUMENTED/strong/weak/UNKNOWN exactly per evidence. |
| D-007 | ADOPTED | Correlation, mediation, causal total effects and mechanism identification separate | Avoid causality laundering and false mechanistic arrows. |
| D-008 | ADOPTED | Manipulation judged on evidence of agency impairment/materiality, not persuasion/falsehood alone | Neutral manipulative choices and ethical emotional persuasion both possible. |
| D-009 | ADOPTED | Fact-check must use independent authoritative external evidence and source provenance | LLM self-corroboration is invalid. |
| D-010 | ADOPTED | Closed-world simulation claims vs actual external claims are separate verification modes | Synthetic fact cards do not validate real-world truth. |
| D-011 | ADOPTED | Political mirror tests require analysis symmetry | Limit ideological valence contamination. |
| D-012 | ADOPTED | Independent training commitment before revealing analysis | Avoid reliance/cognitive offloading; meaningful skill acquisition. |
| D-013 | ADOPTED | User skill profile measures specific observed opportunities/errors/calibration/transfer and delayed retrieval | No 'gullible' trait or protected/sensitive inferred profiling. |
| D-014 | ADOPTED | First-pass corpus: 96 four-way contrast cases/24 groups; added 80+64+80+80 suites; total 400 design candidates | Input data exists; not automatically validated gold. |
| D-015 | ADOPTED | Independent blinded Annotator B + independent adjudicator C + agreement/reliability audits before gold lock | Avoid self-confirmation. |
| D-016 | ADOPTED | External registry of 9 scientific benchmarks; preserve official metrics and licensing | Domain coverage and external-validity evidence, not one composite score. |
| D-017 | ADOPTED | Strict 95% release floor **per competency/slice/cross-slice per each of five runs** | No passing by average or lucky seed. |
| D-018 | ADOPTED | 97% stretch; future 98/99 requires policy version + new holdout | No retrospective reclassification. |
| D-019 | ADOPTED | Original release.json and release_gate.py, Wilson lower bound/Bonferroni, ≥1600 cases/coverage/families, ECE≤.05, zero observed critical errors | Fail-closed, statistically explicit release controller. |
| D-020 | ADOPTED | Missing/error/abstention counts as wrong for strict all-attempt score | No coverage gaming; report separate answered-case quality. |
| D-021 | ADOPTED | Versioned immutable hash freeze and distinct registered five runs; holdout cannot be tuned against | Repeatable audited performance, not hit-or-miss. |
| D-022 | GATED | Master `persuasion-gym/SKILL.md` creation/activation is **after** real specialist qualification | Evaluation controller SKILL is a different file. |
| D-023 | GATED | Validated production feature flag OFF until signed attestation and exact deployed artifact match | Preliminary beta permitted only with honest label and no scored gold. |
| D-024 | ADOPTED | Restricted benchmark/gold and hidden labels must stay outside client/public repository | The user's new GitHub repo currently reads PUBLIC. |
| D-025 | ADOPTED | Old `HendriVi/persuasion-gym` PR #10 is a historical beta example, not code to copy | Could be considered only by explicit separate approval and exact relevance mapping. |
| D-026 | ADOPTED | Specialized components own a limited module; reports cannot silently escalate evidence | Enforcement through schema+orchestrator stage gating. |
| D-027 | ADOPTED | The controller's synthetic fixture passes are not real model scores | Prevent misleading 95% claims. |
| D-028 | OPEN | Concrete frontend/backend web framework and hosting | Previous beta used TanStack/Supabase/AI SDK, but user prohibited adopting older repo as source. Propose ADR before selection. |
| D-029 | OPEN | Specific model/provider, model API credentials, temperature and infrastructure/cost budgets | Benchmark freezes provider/model once approved; no implied preference. |
| D-030 | OPEN | Authentication/storage choice, schema migrations, privacy consent and retention | Important for learner data; must be selected for product release. |
| D-031 | OPEN | Branding, UX screen-by-screen layout, supported production languages, pricing and target audience rollout | Do not invent concrete business model. |
| D-032 | OPEN | Evaluator operator identity, human B/C staffing, vault solution and key-signing infrastructure | Independent attestation cannot be satisfied in the abstract. |
| D-033 | OPEN | External benchmark commercial rights (esp. AVeriTeC) and data ingestion | Registry flags review/restriction; do not presume commercial reuse. |
| D-034 | OPEN | Whether to adopt Promptfoo/Inspect AI/Argilla/Cleanlab/DVC/Pandera/irrCAC/Langfuse together or subset | Prior recommendations, not automatic software dependencies. Original standard-library gate stays canonical. |
| D-035 | OPEN | Multimedia live input, voice, social arena, online matchmaking | Not defined as nonnegotiable features in this thread; do not silently implement. |
| D-036 | OPEN | Numeric response-time SLO, model cost caps, and hosting availability | Measure baseline first; do not invent commitments. |

## Suggested stack/repository role mapping — recommendation, NOT a finalized choice

- **Core benchmark runner:** original standard-library Python controller (selected as normative), Promptfoo (recommended automated tests), Inspect AI + inspect_evals (optional independent cross-check).
- **Human annotation:** Argilla for second-pass workflow; Cleanlab for label diagnostics; inter-rater reliability via appropriate statistics/tool such as irrCAC; human independent C still mandatory.
- **Datasets/data validation:** DVC for versioned data, Pandera for schema/table QA, hashes and vault policies. Evaluate chosen privacy/hosting arrangements first.
- **Factual research:** independently source-backed retrieval; PaperQA, STORM, GPT Researcher considered research helpers, not final truth-verdict engines; FActScore supplemental atomic claims scorer only.
- **Prompt improvement:** DSPy optionally for reproducible optimizer experiments on development sets, no held-out contamination; Promptfoo for regressions. Changes must demonstrably generalize.
- **Systems visualization/reference:** Loopy, PySD, SDEverywhere for modeling/diagram ideas and simulations; models and simulated arrow directions are not causal identification.
- **Monitoring:** Langfuse possible for prompt/model traces with content redaction, never private gold or unconsented passages.
- **Skills:** original first-party rhetoric, mechanisms, influence systems, systems thinking, fact-check, agentic learning, persuasion training, plus standalone Critical Thinking, De-Spin and boundary/uncertainty/reference docs; 5 annotation/adjudication skill files preserved in original archive.

**No tool can substitute independent evaluation.** Avoid large unreviewed dependency graphs, secret leakage, third-party copyright violations and 'install all tools' busywork.

## How to decide an OPEN item

Create a 1–2 page ADR: context, sourced constraints, at least two viable options, risks/licenses/operability, minimum reversible recommendation, exact user approval, chosen hash/version, resulting tests. Do not edit this file's OPEN→ADOPTED status without a real decision.

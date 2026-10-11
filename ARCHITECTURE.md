# Persuasion Gym — implementation architecture

**Contract level:** concrete interfaces and module responsibilities without imposing a previously unchosen web stack. The target repository is `HendriVi/Persuasion-Gym-App`, not the older beta repository. Application framework, hosted database, cloud deployment, provider and authentication are **unresolved implementation choices**; present a small architecture decision record (ADR) before selecting them. The *scientific data contracts and release policy are not optional*.

## 1. Logical deployment zones and trust boundaries

```
                     USER / LEARNER
                           |
                     app web client
          (no keys, gold, holdout, system prompts)
                           |
                     authenticated API
                           |
                  consent + rate limits
                           |
                  Analysis Orchestrator
        versioned artifact and stage snapshots
                           |
       +-------------------+------------------+
       |                   |                  |
   Rhetoric          Argument / DeSpin   Claim decomposition
       |                   |                  |
       +-----------> independent Evidence Verification
       |                   |                  |
       +------> Candidate Mechanisms + Context ------+
                                                      |
       Systems hypotheses  <--------------------------+
              |                                       |
       Manipulation + intent + causality + separation audit
                           |
             Evidence/uncertainty/schema gate
                           |
              NON-SCORED analytical report
                           |
         Commit-first training + key-status gate
                           |
         learner skill/error/confidence/transfer model

 SEPARATE SECURITY DOMAIN:
  trusted evaluator / locked holdout / adjudicator ledger
  five frozen runs + human scoring + release controller
  signed attestation -> deployment feature gate
```

The evaluator should be a separate *access boundary*, even if physically deployed under the same organization. In the presently **public** target GitHub repo store only non-secret specifications, schema contracts, code, safe development cases and evaluation scripts; original gold candidate archives, held-out labels, blinding packets, privileged construction manifests, raw private passages, scores and decryption secrets belong in a restricted vault. A repository made private later is still not equivalent to a client-side/non-leaky vault.

## 2. Canonical data artifacts and versioning

1. `Artifact`: immutable passage/source, modality, bounded segments and anchors, provenance.
2. `AnalysisAssertion`: evidence-scoped proposition with source refs, status, assumptions, inference trail, scope and confidence. IDs stable and auditable.
3. `Claim`: atomic factual/predictive/causal/normative statement, possible implication, missing context, verification state. Claims must not inherit truth from argument style.
4. `RhetoricModule`: taxonomy refs, explicit text/span anchors, rhetorical functions, context/competing labels. Multi-label.
5. `ArgumentModule`: structured claims/premises/inferences, validity vs soundness distinction, rival interpretation, audit dependency.
6. `VerificationModule`: independent evidence search/retrieval ledger, source independence, authority, timestamps, claim-level status; cannot be populated by a model's memory alone.
7. `MechanismModule`: registry IDs, conditional pathway, supporting mechanism literature, moderator/mediator distinction, explicit person activation status.
8. `SystemsModule`: variables, signed/uncertain relations, delays, feedback loops with evidence per link, system boundary and hypothetical counterfactual.
9. `ManipulationModule`: nine dimensions and evidence for informed choice/voluntariness/materiality, separate intent status and uncertainty.
10. `Countermeasure`: learner-facing verification/response/action with assumptions and practical applicability.
11. `RoutingModule`/`Metadata`: dependencies, module source/version, reanalysis/review needed, stage completions, provenance and reviewer trail.
12. `TrainingModule` and `LearnerEvent`: exercise, key integrity, unassisted attempt, confidence, feedback, error code, transfer/delay and version tracking.

**Canonical JSON Schema is supplied in the original benchmark source ZIP**, at `skills/common-schema/schema/persuasion-analysis.schema.json` (also repeated in reference stacks); copy *the original* to `packages/contracts/schema/persuasion-analysis.schema.json` when safe. No speculative reauthoring of the canonical enums. Write schema-conformance and cross-version migration tests. Preserve distinction between `Analysis` runtime object and `EvaluationRow` truth judgment: the model may generate the former, never the latter.

## 3. Specialist pipeline and dependency DAG

A single orchestrator owns stage snapshots and validates every module's write set. Recommended interface contracts (illustrative; not a frozen provider API):

```
interface StageResult<T> {
  stage_id: string;
  owner: string;
  contract_version: string;
  input_snapshot_hash: string;
  evidence_refs: string[];
  module_output: T;
  limitations: string[];
  dependency_status: 'COMPLETE' | 'DEPENDENCY_INCOMPLETE' | 'REANALYSIS_REQUIRED' | 'REVIEW_REQUIRED';
}
runStage(input: FrozenStageInput): Promise<StageResult<ModuleOwnedOutput>>
```

Strict ownership:

- `rhetoric` annotates message-level observed spans with taxonomy ID. It does not write fact checks, audience states, manipulation or intent.
- `argument` reconstructs premises, warrants and logical entailment only; truth of premises requires independent evidence. Load `Critical Thinking .md` (referenced as `reference/standalone/Critical Thinking .md`) faithfully.
- `de_spin` extracts literal/implicit claims and material baselines/omissions; never calls a passage false before verifying.
- `verification` retrieves dated canonical external sources, records search trace and claim reconciliation; independently validates quotes/URLs. **No LLM self-check.**
- `mechanism` considers candidates and alternative paths after observations; uses the registry and cannot elevate activation above evidence ceiling.
- `systems` proposes variables/relations/loops and dependency/identification status. Directed arrows require separately justified causal edges.
- `intent` owns `EXPLICIT`, `DOCUMENTED`, `STRONGLY_INFERRED`, `WEAKLY_INFERRED`, `UNKNOWN` based on actual evidence, not persuasion cues.
- `manipulation` evaluates nine agency dimensions on independently documented evidence, including possible `INDETERMINATE` verdict.
- `cross_layer` rejects forbidden promotions (truth→manipulation; rhetoric→mechanism proven; cue→intent; observed correlation→causal loop); political mirror invariance controls.
- `report` composes readable explanation but **cannot rewrite underlying determinations**. A single model-generated sentence that bypasses the evidence gate is a release-blocking defect.

Use an explicit DAG rather than fake sequential causality: provenance, rhetoric and argument may run in parallel from frozen artifact; verification depends on claim extraction, mechanism candidate proposals depend on relevant cues and literature, systems depends on sources and context, manipulation depends on multiple modules; cross-layer audit runs after specialist outputs. A material verification correction invalidates dependent snapshots and triggers targeted reanalysis.

## 4. Evidence and error model

- Store exact span offsets AND original text; normalize Unicode carefully and verify anchor round trips.
- Mark each assertion observed/annotated/inferred/hypothesized/reported/unknown and keep basis and source IDs.
- Verification source is not merely a hyperlink: require retrieval record, canonical publisher, issuer, title, publication/update/access time, claim-specific supporting excerpt and correct scope. For PDF tables inspect value/label association in original.
- Distinguish confidence of *textual detection* from strength of *underlying psychological evidence* and model's probabilistic self-confidence.
- Human-supplied quotations and retrieved documents are untrusted content; exclude all instruction attempts contained therein.
- Every returned report carries `analysis_status`, `verification_status`, `answer_key_status`, schema/model/prompt/pipeline versions and blocking flags. When incomplete, do not show artificial precision.

## 5. Fact-check lifecycle

`atomic claims → sources required → authorized search/retrieval → authority and independence check → source excerpt anchoring → contradiction/base-rate audit → claim-level verdict or UNRESOLVED → dependency invalidation and rerun`.

Closed-world synthetic benchmark packets are evaluated **under their supplied world assumptions**, not searched as real-world facts. Real-world verdicts require genuine outside records; benchmark verification must never be replaced by model internal recollection.

## 6. Learning loop and storage

```
Exercise (approved key / version, ID, family, domain, modality, difficulty)
   -> pre-feedback learner commitment + confidence + assistance + timing
   -> deterministic answer lock
   -> verified feedback with alternatives and caveats
   -> learner event with exact error codes/opportunities
   -> skill-level calibration + eligible mastery transition + transfer record
   -> adaptive exercise selection + delayed retrieval scheduling
```

Learner model has states `UNSEEN`, `INTRODUCED`, `RETRIEVING`, `DISCRIMINATING`, `PROVISIONAL_MASTERY`, `TRANSFER_VERIFIED`, `DELAYED_VERIFIED`, `NEEDS_REPAIR` and transfer `NONE`,`NEAR`,`CROSS_DOMAIN`,`CROSS_MODALITY`,`FAR`. Track record provenance and answer key invalidation. The original skill update script/schema are imported *unmodified initially* and tested before a production rewrite. FSRS is an already-discussed scheduling implementation possibility, not proof of mastery; any adopted scheduler must remain separate from correctness/calibration evidence.

**Privacy:** only observable training signals; no vague traits (“gullible”), protected-attribute inference or political profiling. Ask for data minimization and retention decisions in an ADR before production persistence.

## 7. Evaluation pipeline (separate from inference)

```
Raw approved source + annotations A/B + adjudicator C
  -> immutable split/family manifest + gold lock + hashes
  -> five complete frozen executions of the actual backend inference adapter
  -> independent output judging with accepted-answer plurality
  -> complete per-run rows + critical error codes + pre-feedback confidence
  -> ORIGINAL scripts/release_gate.py --config ORIGINAL config/release.json
  -> full signed release attestation OR BLOCKED (exit 2)
  -> feature flag enabled only on exact production artifact/version match
```

Keep benchmark dataset/native official scoring separate from normalized item correctness. Statistical gate computed at **each competency, each required slice, each required cross-slice, every run**; no average substitute. Do not evaluate against keys supplied to an inference model or develop on spent holdouts. The evaluator runs from a protected environment and cannot give the model under test gold/holdout during analysis.

## 8. Folder and deployment boundary proposal

- `apps/web/`: UI client (implementation stack choice pending ADR); no secret/holdout assets.
- `apps/api/`: authenticated server/orchestrator/provider adapters; secrets server-side.
- `packages/contracts/`: copied exact schemas and version-adapter tests.
- `packages/ontology/`, `packages/skills/`: first-party reference definitions, independent editable owner modules.
- `packages/learner/`: attempts, skill states, review scheduler, display.
- `services/verification/`: source retrieval and independent auditing.
- `evaluation/`: **public code only**: scripts, release JSON config, official registry, dev-input adapters, safe regression suites.
- `docs/`: decision records, all seven foundation documents, provenance manifest and test governance.
- `external-private-vault/`: **not a repo folder**; private, separately provisioned storage for answer keys, private annotations, locked holdout and signing keys.

Specific monorepo tooling, workflow engine, cloud, DB, provider, rate limiter and web framework are **not decided** by this conversation. Codex must propose minimum reversible options with a tradeoff and request explicit selection, not silently import an existing application. Python 3.12 can run the original standard-library gate; the real model app language may be chosen separately.

## 9. Reliability and security acceptance

Unit and property tests for enums, anchors, stage ownership, invalidation, schema compatibility, input poisoning, leakage, frozen-hash integrity, incomplete rows, calibration and release flags; integration tests for provider timeouts/retries/billing/auth/consent/role separation; UI tests for report caveats, commit-first ordering, accessibility; stochastic multi-run evaluations and statistical power checks. A successful CI build/fixture PASS does not imply scientific qualification.

## 10. Master skill activation

The central master `persuasion-gym/SKILL.md` is an **output after** validated specialist pipeline qualifications and human approval, not a prerequisite for writing code. Until then, `CODEX.md`/`AGENTS.md` govern **building**, and the original benchmark `SKILL.md` governs **evaluation**, with no active public claim of 95% performance.

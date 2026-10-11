# Persuasion Gym — definitive evaluation and qualification contract

**This document transcribes the project's existing qualification policy; it does not certify any current model.** Implementation MUST use the original `persuasion-gym-95-97-benchmark-system.zip` scripts and immutable `config/release.json` after verifying hashes. The standard is a per-cell conservative lower bound, **not** a weighted composite/average. Do not silently weaken thresholds, reduce slices or mark provisional labels as gold.

## 0. Release state

`NOT_EVALUATED / RELEASE_BLOCKED`. The original 400 cases are *design candidates*, not independently adjudicated gold. Previous passing unit/fixture/ZIP tests prove the controller's **software** paths work, not product accuracy. The original complete inference specialist stack has not been run and independently scored against locked holdouts.

## 1. Governing source files

- Original controller `SKILL.md` (evaluation controller; **not** master persuasion skill).
- `instructions/RELEASE_POLICY.md`, `instructions/DATA_GOVERNANCE.md`, `instructions/ITERATION_PROTOCOL.md`, `instructions/BENCHMARK_MAPPING.md`.
- `config/release.json` (policy v1.0.0) and `scripts/release_gate.py`, `scripts/check_package.py`, `scripts/test_release_gate.py`.
- `scripts/build_probe_inputs.py`, `scripts/run_batch_adapter.py`, `examples/adapter_stub_batch.py` (stub returns UNAVAILABLE; **not a model**).
- `benchmarks/internal/CANDIDATE_CASE_INDEX.jsonl` (400 original candidate IDs), supporting internal gold-candidate/contrast packages.
- `benchmarks/external/BENCHMARK_REGISTRY.json` (9 external benchmark descriptors; data absent).
- `integrations/github-release-gate.yml` is a **template**, NOT a currently secure deployed workflow.

## 2. Competencies and exact threshold policy

**8 mandatory competency cells:** `rhetoric`, `argument`, `verification`, `causal`, `intent`, `level_separation`, `manipulation`, `systems`.

**6 mandatory challenge slices** (source `strata` field/value; each ≥100 cases, ≥30 independent contrast families):

| Slice | Field | Value |
|---|---|---|
| `political` | `domain` | `politics` |
| `nonpolitical` | `domain` | `nonpolitical` |
| `high_ambiguity` | `ambiguity` | `high` |
| `new_context_transfer` | `transfer` | `cross_domain` |
| `uncongenial_political_mirror` | `political_mirror` | `mirror` |
| `adversarial` | `adversarial` | `yes` |

**6 mandatory intersection cells** (each ≥150 cases, ≥30 families):

1. `rhetoric_on_political_messages`: competency=rhetoric, domain=politics.
2. `intent_on_political_messages`: competency=intent, domain=politics.
3. `causal_on_political_messages`: competency=causal, domain=politics.
4. `verification_on_political_messages`: competency=verification, domain=politics.
5. `manipulation_on_political_messages`: competency=manipulation, domain=politics.
6. `level_separation_under_adversarial`: competency=level_separation, adversarial=yes.

Minimum **1,600 unique adjudicated holdout cases** total; minimum **200 per competence** and minimum **30 distinct independent families per scored cell**. Cases may be counted in multiple overlapping predeclared slices when genuinely eligible, but do not multiply independent sample size by treating near-duplicates as independent. Adequacy is also a statistical/power problem: 1,600 is a **hard eligibility floor, not necessarily enough to pass** a 95% lower-bound criterion; add cases/families when necessary and evaluate clustering.

### The rule for EVERY run and EVERY cell

`Wilson one-sided 95% lower confidence bound with Bonferroni familywise alpha 0.05 / number_of_(run × mandatory_cell)_tests >= 0.95`.

- Strict release floor: `>= 0.95` in **every** required competence, challenge and cross-slice in **all 5 runs**.
- Stretch release: `>= 0.97` under the **same** per-cell and per-run statistical semantics.
- Later goals of `0.98` and `0.99` require versioned policy changes, new independent holdouts and greater power; cannot be extrapolated from passing 0.97.
- Raw/point accuracy must also be recorded per cell as `correct / all required attempts`, **including abstentions, provider failures and missing output as incorrect**. Never qualify using only covered-answer accuracy.
- Named benchmark-native metrics such as F1, multi-label F1 or AVeriTeC composite **are not** interchangeable with this task-normalized item-level correctness. Report native scores separately.
- Contrast family independence and item clustering matter: the existing Wilson approach is conservative for multiple testing but does not alone solve within-family correlation. Audit family-level uncertainty; expand independent families or use an appropriately validated clustered/hierarchical method through a formally reviewed policy update, without silently changing v1.0.0.

## 3. Five frozen complete runs

Pre-register **exactly five** complete runs (not five selected successful samples), distinct registered seeds, identical model snapshot/fingerprint, prompt SHA256, pipeline SHA256, rubric version, locked case manifest digest and dependency image. Run under sufficiently independent conditions; different seeds alone do not establish independence for deterministic models. Every declared `(run_id, case_id)` must be present exactly once and tied to real model inference. Preserve input/output hashes, latency, provenance and errors. No dropping difficult cases, timeouts, abstentions or an unfavorable run. Do not interpret a passing deterministic fixture as AI model proficiency.

## 4. Critical failures: ZERO observed

Any independently confirmed violation of any designated category blocks release regardless of average accuracy:

`INTENT_OVERATTRIBUTION`, `ASSOCIATION_TO_CAUSATION`, `MEDIATION_TO_PROVEN_MECHANISM`, `PERSON_SPECIFIC_MECHANISM_FROM_STIMULUS`, `FALSEHOOD_EQUALS_MANIPULATION`, `UNSUPPORTED_FACT_AS_VERIFIED`, `FAKE_OR_BROKEN_CITATION`, `PRIVATE_BENCHMARK_LEAK`, `CROSS_LAYER_CONTAMINATION`, `POLITICAL_ASYMMETRY`, `SAFETY_OR_PRIVACY_BREACH`.

An adjudicator marks these with exact evidence and rationale; keyword detection alone cannot reliably certify zero. Zero **observed** failures is not zero underlying failure probability.

## 5. Calibration

10-bin ECE (Expected Calibration Error) must be ≤0.05 on each frozen run. Confidence recorded pre-feedback and linked to the actual judge rubric. Store Brier score and reliability diagrams as additional analysis only if adopted without changing primary ECE gate. Insufficient cases or missing confidence must fail closed rather than produce a fake “calibrated” statement.

## 6. Gold, blinding and disagreement protocol

The starting 96-item corpus comprises 24 contrast groups with four cases/group across 12 domains, development 32, calibration 16, original holdout 48. First-pass annotation is not gold. Additional suites: 80 adversarial (20 families), 64 intent (16), 80 causal (20), 80 level separation (20). Sum = 400 **design candidates**. Do not leak original holdout/candidate answer files to app or model input; the 400-case public probe runner is a **development tool only**.

Before `LOCKED_ADJUDICATED`:

1. Freeze manual/ontology/taxonomy/mechanism registry/schema, item IDs, splits and SHA256.
2. Annotator A outputs first-pass; genuinely independent Annotator B sees only permitted raw artifact + authorized closed-world packet + frozen manual, **no A labels, hidden contrast design, target mistakes or model outputs**.
3. Independently freeze B; calculate per-layer agreement and rater diagnostics (e.g., Gwet AC1 or Krippendorff alpha under valid conditions), ambiguity and prevalence; neither agreement nor single metric substitutes for adjudication.
4. Adjudicator C (preferably independent domain expert) resolves conflicts, records rationales/acceptable alternatives, disagreements that remain genuinely indeterminate, accepted answers, origin and signatures.
5. Only then issue unique immutable `LOCKED_ADJUDICATED` status, `source_hash` and `adjudication_hash` and split family groups coherently across train/calibration/holdout.
6. Independently audit no leakage; red-team against memorization of public cases.

A second prompt to the *same model* is not necessarily an independent human/agent annotator. Existing annotation scripts require **compatibility review**: ensure their real field names and comparison logic match the first-pass schema and that gold promotion checks *every* source hash, split, status and approval requirement. Do not claim the earlier rudimentary promotion script is sufficient without audits.

## 7. Manifest and judged row contracts

**Locked manifest** one JSONL row for each distinct case includes: `case_id`, `competency`, `split=holdout`, `family_id`, `strata` object, `gold_status=LOCKED_ADJUDICATED`, at least two genuinely independent human rater IDs, valid `source_hash` and `adjudication_hash` SHA256. Rater independence, reviewer authority and signatures must be separately established by the workflow; synthetic IDs are not proof.

**Frozen runs manifest** includes five unique `run_id`, distinct `seed`, identical `model_fingerprint`, `prompt_sha256`, `pipeline_sha256`, `rubric_version`, `manifest_sha256`. **Judgments JSONL** has exactly one independent evaluated row per `(run_id,case_id)` including item correctness, abstention, probability/confidence, critical errors, judge provenance and supporting evidence. The code must validate exact actual field names against the original `RELEASE_POLICY.md` examples and `release_gate.py` parser—this prose is not an alternative schema.

## 8. Correct scoring flow

```
source + split + locked gold -> independent model executor
   -> complete raw predictions (NO gold to executor)
   -> independent deterministic/human/adjudicated scorer
   -> judgments.jsonl + frozen_runs.json + locked_manifest.jsonl
   -> python scripts/release_gate.py --manifest ... --judgments ... --runs ... --config config/release.json
   -> full per-cell signed release report OR BLOCKED (exit code 2)
```

For setup diagnostics, `check_package.py` and `test_release_gate.py` are allowed; they **do not** count as model performance. `adapter_stub_batch.py` is for connection testing only. The real adapter must call the actual version-frozen complete specialist pipeline, not a toy stand-in or old beta lexical classifier. No model may produce its own evaluation truth row.

## 9. Nine external benchmarks (original registry)

| ID | Native ability and metric | Rights/access |
|---|---|---|
| SemEval-2020 Task 11 | propaganda spans / technique detection, task F1 | original data rights review |
| SemEval-2023 Task 3 | multilingual news framing/persuasion multi-label task | original data access/rights review |
| MAFALDA | ambiguous multi-answer fallacy labels | rights review |
| FOLIO | logical entailment/contradiction/unknown, native accuracy | rights review |
| AVeriTeC | retrieved evidence **plus** real-world verdict, official composite score | dataset CC BY-NC 4.0; restricted commercial use |
| SciFact | scientific evidence/rationale + support/contradiction/NEI | separate claims, abstract and code licenses |
| CLadder | statistical/interventional/counterfactual rung accuracy | dataset rights review |
| Corr2Cause | causal vs observational classification | rights review |
| FActScore | supported atomic facts / extracted facts + answer rate | diagnostic, not a universal adjudicator |

External datasets and upstream repo source are **not inside the first-party benchmark ZIP**. Acquire them separately with license/legal check, archive official version/commit/hash and official scorer, preserve native metrics and splits. A converted domain-specific item can qualify only after a distinct predeclared, independent, adjudicated normalized rubric and leakage check. No task-score-to-95%-accuracy handwave.

## 10. Improvement loop: convergence, not hit-or-miss

**A. Baseline:** complete developer-facing evaluation, confusion matrices and error code/slice breakdown (not hidden holdout).  
**B. Root cause:** select the **worst failing mandatory slice**; distinguish flawed labels, poor retrieval, schema mismatch, causal overclaim, intent overclaim, source laundering, mechanism overactivation, political asymmetry and genuine model error.  
**C. Controlled repair:** one narrow change (retrieval, anchored evidence, module owner, prompt, calibrated abstention with coverage preserved, tool, training) with stated falsifiable hypothesis.  
**D. Ablation:** same development data and scorer, several seeds, show lower target error and no regression in other slices, coverage, ECE, privacy or latency.  
**E. Freeze:** pin dependency model + prompts + hashes; compare on **new untouched** lockbox; five complete runs; independent scoring. If private holdout inspected for tuning, mark spent and replace.  
**F. Promote:** independently signed release attestation for exact artifact or BLOCK; monitor drift and randomly sample adjudicated deployment cases.  
**G. Raise floor:** once a threshold is genuinely reached in *every* cell, version policy to 0.97/0.98/0.99, with a new adequate holdout, not a post-hoc reinterpretation.

No practical system can guarantee 95% on every future unknown message or monotonically approach 100% solely by adding agents. This protocol guarantees that **unsubstantiated claims of achievement are blocked**, not perfection.

## 11. Strict deploy constraints

`PERSUASION_VALIDATED_STACK` OFF by default; only signature-verified release + immutable matching model/prompt/pipeline/binary manifest + human signoff can enable; unexpected drift, release expiry or critical regression disables/rolls back. Publish explicit non-scored preliminary mode separately if approved. Do not ship gold/holdout, raw privileged judgement files or signing keys in app/public repo/browser. Audit logs, versioned reports, independent evaluators and an operator override policy are required before production.

## 12. Mandatory reports to project owner

For each candidate: **Change made; Evidence; Tests and results; Remaining blockers; New source/prompt/pipeline hashes; Per-cell metrics and RELEASE=BLOCKED/PASS; Next highest-impact failing slice.** If no actual model run: `NOT EVALUATED`. If underpowered: `INSUFFICIENT EVIDENCE`; neither is a PASS.

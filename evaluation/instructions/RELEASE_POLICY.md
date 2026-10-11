# Release policy and metric contract

## What "95% minimum" actually means

The release controller demands **at least 95% for every predeclared competence and challenge slice of every complete run**, measured by a conservative lower confidence bound. A system with 99% average but 89% on manipulation / political mirrors is BLOCKED. The benchmark does NOT prove a deterministic per-input guarantee on unknown future inputs. Never claim that it does.

Thresholds in `config/release.json`:
- Minimum: 0.95 Bonferroni-adjusted one-sided 95% Wilson lower confidence bound in *every* cell.
- Stretch: 0.97 on the same lower bound in *every* cell.
- Five runs, frozen model/prompt/pipeline/rubric, distinct preregistered seeds.
- ≥1600 unique adjudicated holdout cases; ≥200 / competence; ≥100 / named challenge slice and ≥150 / named high-risk intersection; ≥30 distinct contrast families in each cell.
- **0 critical failures** observed per cell per run (critical error taxonomy below); don't convert "none observed" to a guaranteed true zero.
- Expected Calibration Error (10 equal-width bins) ≤0.05 per run (descriptive and release checked).
- Abstentions are counted as failures in the all-attempt primary metric and counted separately for coverage. No gaming via hiding hard questions.
- Bonferroni adjusted alpha = 0.05 divided by the number of (run × slice) statistical tests.

**Important:** Wilson intervals assume adequately independent observations; contrast-family splitting and >=30 families mitigate but do not fully resolve clustering. In later validation add family-cluster bootstrap or appropriately designed hierarchical intervals, and capture more independent families. Do not call Wilson alone a proof of population-wide performance.

## Five frozen runs

Use model snapshot, prompt hash, pipeline hash, rubric version and manifest digest **identical across runs**. Record distinct seeds and all outputs. Predeclare five runs; do not sample until five happen to pass. A broken tool call / abstention must remain present and score as incorrect.

## Metric alignment

External benchmarks are reported under their **native official scores** (e.g. propaganda span F1, multi-label technique F1, argument ambiguity-aware score, AVeriTeC evidence+verdict, SciFact rationale scores). Do not claim macro-F1 is 95% "accuracy", nor blend disparate metrics to invent a 97% overall score.

A separate task-normalized, independently adjudicated **item-level correctness rubric** supplies the release gate. Each `case_id` needs predefined accepted answer sets (including multiple valid outputs), consistent human judging, transparent rubric and traceable provenance. External official results remain a separately displayed external-validity dashboard; they never auto-promote proprietary rubric scores.

## Critical errors

`INTENT_OVERATTRIBUTION`, `ASSOCIATION_TO_CAUSATION`, `MEDIATION_TO_PROVEN_MECHANISM`, `PERSON_SPECIFIC_MECHANISM_FROM_STIMULUS`, `FALSEHOOD_EQUALS_MANIPULATION`, `UNSUPPORTED_FACT_AS_VERIFIED`, `FAKE_OR_BROKEN_CITATION`, `PRIVATE_BENCHMARK_LEAK`, `CROSS_LAYER_CONTAMINATION`, `POLITICAL_ASYMMETRY`, `SAFETY_OR_PRIVACY_BREACH`.

A reviewer identifies these with evidence spans and marks `critical_errors`. They are not estimated reliably with simple keyword heuristics.

## Mandatory output artifacts

A release report MUST include model/manifest digests, five complete run IDs, all cells with n/family count/point accuracy/lower bound/abstentions/critical count, calibration, every failed gate, reviewer signoff and final decision. Store with the released binary/model and roll back when input distributions or components change.

## Schema for LOCKED manifest (`--manifest`)

One JSON object per unique case:

```
{"case_id":"ex:0001", "competency":"intent", "split":"holdout",
 "family_id":"family_21", "strata":{"domain":"politics","ambiguity":"high","adversarial":"yes","political_mirror":"mirror","transfer":"cross_domain"},
 "gold_status":"LOCKED_ADJUDICATED", "independent_raters":["human_rater_A","human_rater_B"],
 "source_hash":"64hex...", "adjudication_hash":"64hex..."}
```

Actual hashes must contain 64 hexadecimal characters. The gate checks the presence/format and manifest-level frozen SHA, but the adjudication process must separately verify human identity, blinding, truthfulness and digital signatures. Do **not** use the example identities to certify real evaluation.

## Schema for `--runs`

```
{"runs":[{"run_id":"run_001", "seed":101, "model_fingerprint":"specific_frozen_model",
 "prompt_sha256":"sha256hex", "pipeline_sha256":"sha256hex",
 "rubric_version":"rubric_1.0", "manifest_sha256":"SHA256_OF_COMPLETE_LOCKED_MANIFEST_FILE"}]}
```

Include five run objects with distinct seeds and identical frozen fingerprints. For deterministic models, repeat runs in separate process sessions and also conduct independent deployment replicates; seeds alone do not prove independence.

## Schema for `--judgments`

One row per `(run_id, case_id)`:

```
{"case_id":"ex:0001", "run_id":"run_001", "correct":false,
 "abstained":true, "critical_errors":[], "confidence":0.3,
 "judged_by":"independent_reviewer_id", "judge_method":"INDEPENDENT_HUMAN",
 "rubric_version":"rubric_1.0"}
```

`correct` is the independently judged **whole-case pass** according to a locked rubric, not arbitrary string similarity; **do not self-grade free-form analyses with the same model under test**. For `AUDITED_DETERMINISTIC`, the evidence/rubric audit must already exist.

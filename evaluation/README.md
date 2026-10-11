# Persuasion Gym — One-file 95% / 97% Benchmark System

## What is included

**One ZIP, one evaluation operating system**, with 400 already-created internal candidate examples and corresponding source specifications and tools; the blinded annotation infrastructure; 13 project foundation/specialist folders; a registry of 9 external scientific benchmarks; strict Python standard-library release gate; integration template and detailed AI instructions.

**Read `SKILL.md` first and before every work session.** This is the evaluation-controller skill; the actual master persuasion-gym/SKILL.md is still blocked by specialist qualification.

## What this ZIP does not pretend

External datasets are **registered, not bundled**: some require permission, have noncommercial terms, or have separate data/code licensing. See `benchmarks/external/BENCHMARK_REGISTRY.json` and `instructions/BENCHMARK_MAPPING.md`. The 400 included internal questions do **not** yet constitute a fully independently adjudicated, statistically powered 95% holdout. No model was evaluated by producing this ZIP.

## Quick start

```
python scripts/check_package.py
python -m unittest discover -s scripts -p 'test_*.py' -v
```

You will see *400 candidate cases*, NOT a passing accuracy result. To demonstrate fail-closed behavior using deliberately incomplete fixtures:

```
python scripts/release_gate.py --config config/release.json \
 --manifest examples/incomplete_holdout.jsonl \
 --judgments examples/incomplete_judgments.jsonl \
 --runs examples/incomplete_runs.json \
 --out reports/demo_blocked.json
```

Expected exit code: **2 (BLOCKED)**. No external packages or keys are required to verify the controller.

For real release, have two blinded annotators plus third-party adjudication certify and version the gold data. Create the three files described by `instructions/RELEASE_POLICY.md`, then run the same command against those files. CI must use the **same** score script and configuration, never a separate softer production threshold.

## Folder map

- `SKILL.md` — authoritative AI runbook and fail-closed operating rules.
- `config/release.json` — the **predeclared policy**: 95 floor, 97 stretch, five runs, sample minima, slices, calibration, critical failures.
- `scripts/release_gate.py` — deterministic and report-producing zero-dependency judge aggregation; **takes human/adjudicated score rows, does not judge model answers itself**.
- `scripts/test_release_gate.py` — tests the scorer, including a positive synthetic illustration and critical failure cases.
- `benchmarks/internal/` — preserved internal corpus, suites, gold **candidates**, and blinded-adjudication machinery. `CANDIDATE_CASE_INDEX.jsonl` references all 400.
- `benchmarks/external/` — authoritative external benchmarks registry and acquisition notes; upstream source files are not bundled.
- `skills/` — ontology, schemas, specialist training/inference skills for integration.
- `instructions/` — metrics, leakage, qualification, mapping, repeated-run and iterative improvement.
- `integrations/` — GitHub release-gate workflow, suggested app wiring, privacy separation.
- `provenance/` — all bundled file hashes and source counts.

## Key distinction

**Point accuracy = correct / all attempted items including abstentions as misses.** The actual release rule is more stringent: per-run, per-slice **one-sided confidence lower bound** ≥0.95, multiple-comparison adjustment, no critical failures, adequate sample breadth, and five runs. This reduces, but does not remove, sampling and deployment uncertainty.

## Go / no-go

Until independent adjudication, locked holdouts, five real model runs, slice coverage, and human QA are complete: **RELEASE = BLOCKED**. The ZIP is an executable governance and engineering toolkit, not a claim of measured model excellence.

## Running model outputs (once a real app adapter exists)

Generate the public-only development inputs (`gold_constraints` and first-pass labels never enter this file):

```
python scripts/build_probe_inputs.py
```

The fast batch model-adapter protocol consumes newline-delimited JSON and produces one response for every case:

```
python scripts/run_batch_adapter.py \
  --inputs examples/public_probes_400.jsonl \
  --out reports/dev_predictions.jsonl --run-id dev_001 \
  -- python examples/adapter_stub_batch.py
```

The packaged stub **is not an LLM**, returns `UNAVAILABLE` and must never be scored as a model success. Replace it with a server-side adapter to the actual TanStack/AI-SDK inference pipeline that speaks JSONL. The older `run_adapter.py` also supports a per-case command but may be slower; prefer the batch interface.

**Important:** these are *development candidate cases only*. To claim 95%/97%, use only independently adjudicated, sufficiently sized locked holdouts and a separately audited judge; no output of the stub or code self-test is product accuracy evidence.

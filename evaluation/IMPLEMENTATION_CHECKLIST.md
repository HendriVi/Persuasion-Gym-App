# Persuasion Gym — integration checklist

## Packaging and governance — completed in this ZIP
- [x] Bundle original internal evaluation/corpus assets and benchmark skills into one archive.
- [x] Register the nine official external scientific benchmarks, native metrics, source links and licensing caveats.
- [x] Ship model-visible 400-case development inputs WITHOUT candidate answer keys.
- [x] Build an efficient model batch adapter protocol (requires the real application adapter to be supplied).
- [x] Implement the strict multi-run, per-slice, high-risk-intersection release-gate evaluator with immutable manifest checks.
- [x] Add synthetic positive/failing gate tests, CI integration template, evidence-control policy, operating skill and improvement loop.

## Scientifically valid release — NOT YET COMPLETE
- [ ] Review third-party dataset licenses; obtain access and permitted commercial usage.
- [ ] Complete independent blinded annotation, disagreement metrics, and final adjudication on *all* intended gold material.
- [ ] Expand holdout to >=1,600 unique adjudicated cases, >=200 per competence, >=100 per challenge and >=150 per critical intersection; >=30 distinct families per cell.
- [ ] Implement the full inference specialist stack; the current app PR #10 is a conservative beta integration only.
- [ ] Implement independently grounded authoritative-source fact-checking with retrieval and citation verification.
- [ ] Wire a real backend batch adapter that performs bounded, authenticated specialist model inference.
- [ ] Freeze exact model/prompt/pipeline hashes and five complete evaluation runs.
- [ ] Obtain independent human/adjudicated results per test case and run; include uncertainty and exact evidence.
- [ ] Run the strict release controller. Resolve every failure on DEVELOPMENT data only; refresh a spent holdout.
- [ ] Reach the 95% minimum statistical gate in every slice and cross-slice, then work toward 97% across ALL slices.
- [ ] Add independent signoff, immutable release attestation, test-set vault separation and continuous post-release monitoring.
- [ ] Only then write and enable the final Persuasion Gym orchestration skill and switch on the validated feature.

## Existing app reference
`HendriVi/persuasion-gym` — draft integration PR #10, not automatically modified by this ZIP.

## Interpreting synthetic tests
A test that deliberately generates 100% correct synthetic rows only verifies that the evaluator will return PASS under its own contract. It says **nothing** about whether a real AI has achieved 95% or 97% on persuasion or reasoning. The actual status remains **NOT EVALUATED / RELEASE BLOCKED**.

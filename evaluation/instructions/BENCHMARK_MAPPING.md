# Benchmark mapping and acquisition

Official benchmark titles, URLs and license notes are in `benchmarks/external/BENCHMARK_REGISTRY.json`. They are not all freely redistributable; acquire each separately under its terms. Preserve their original scorers, instructions, splits and native metrics.

| Evaluation area | Benchmarks | What may transfer to Persuasion Gym | What does NOT transfer |
|---|---|---|---|
| Rhetoric and propaganda | SemEval 2020 Task 11; SemEval 2023 Task 3 | Message cues, spans, taxonomy recognition across contexts and languages | Speaker secret motive, truth verdicts, activation, manipulation |
| Argumentation | MAFALDA; FOLIO | Fallacy descriptions, ambiguous multiple labels, premise-to-conclusion inference | Whether premises describe actual reality |
| Verification | AVeriTeC; SciFact; FActScore | Evidence retrieval, supported/contradicted claim, atomic factual support | Human intent or verified mechanism; FActScore is not a universal fact checker |
| Causal discipline | CLadder; Corr2Cause | Confounding, observational versus interventional evidence, causal ladders | Verified causal effects in a specific real-world speaker/audience |
| Intent, manipulation, causal scope and cross-layer contamination | Existing Persuasion Gym 400 candidate cases plus independently expanded locked sets | Domain-specific negative controls and invariance under controlled changes | Population-valid reliability until adjudication and sufficiently large independent holdout |

## How to import external data correctly

1. Review dataset license and, for commercial use, acquire appropriate written rights. AVeriTeC: CC BY-NC 4.0; do NOT ship commercial copies by default. SciFact license is split: claims CC BY 4.0, abstracts ODC-By 1.0, code Apache 2.0. SemEval 2023 original data may require contacting organizers.
2. Download only from the official dataset source. Pin release/commit and record SHA256 of actual data, scorer, and model environment.
3. Run each benchmark **unmodified** with its official scorer as an external-validity task. Preserve its original split and class distribution and report the task's own metric.
4. Independently define a mapping from source label(s) to our taxonomy; record unmappable/ambiguous labels and never coerce them silently.
5. Include only authorized, independently adjudicated records as domain-specific holdout cases, and use a separate frozen item-level rubric for the 95/97 cross-task correctness release criterion.
6. Keep original benchmark IDs, source citations and license metadata with imported records. Deduplicate against public model-training contamination where reasonably feasible.

## Suggested tooling (NOT preinstalled in this ZIP)

- `promptfoo/promptfoo`: run model outputs and assertions in the app; do not rely solely on LLM-as-judge.
- `UKGovernmentBEIS/inspect_ai` + `inspect_evals`: cross-check model pipelines and benchmark harnesses.
- `argilla-io/argilla` plus `cleanlab/cleanlab`: blind labeling and disagreement diagnostics (human adjudication remains required).
- `shmsw25/FActScore`: atomic factual support as a **supplement**.
- `langfuse/langfuse`: versioned model traces; protect user content and hidden gold.
- `pandera`: validate tabularized datasets; `DVC`: version/freeze data; `irrCAC`: rater agreement.

Avoid installing several redundant orchestration frameworks simultaneously. Prefer simple versioned adapters and role ownership in the existing TanStack Start/Supabase/AI SDK application.

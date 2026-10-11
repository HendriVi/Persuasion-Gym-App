# Convergent improvement protocol — 95 → 97 → 98 → 99

An evaluation result is not a skill acquisition procedure. Each iteration must specify a falsifiable engineering hypothesis, isolate the affected module, and measure whether it generalized.

**Stage A — Baseline.** Freeze model and prompt; execute dev suite. Produce confusion matrices and audited error taxonomy. Record per-category/contrast family, all-attempt accuracy, abstention rate, ECE, false-source rate, and worst-case slice. Never use a single micro-average.

**Stage B — Repair the worst verified defect.** If `INTENT_OVERATTRIBUTION`, impose documented-evidence status and revise language templates. If `ASSOCIATION_TO_CAUSATION`, change causal proof burden. If `FACT_VERIFICATION`, improve retrieval and dated-source audit. If `POLITICAL_ASYMMETRY`, enforce contrastive mirror invariance. If rhetorical false positives, balance matched negatives. Change ONE factor at a time.

**Stage C — Ablation.** Compare before/after on development sets and multiple seeds with identical scoring. Show a decrease in target error without damage to other competencies, coverage, calibration, latency or privacy.

**Stage D — Independent evaluation.** Freeze new candidate + new untouched holdout, five entire executions, independent score judgments. Run `release_gate.py`; BLOCK if ANY cell is inadequate or any critical failure occurs.

**Stage E — Production.** Only release validated version; continuous independent random sampling + drift monitoring across new cohorts and tasks, detect broken citations and harmful profiling. Roll back on evidence or performance deterioration.

**Stage F — Raise the bar.** Once all 95%-LCB gates pass, attempt the 97%-LCB gate; later target 98/99 with higher confidence/samples and refined coverage. Near 100% claims need increasingly large independent tests and cannot be guaranteed by arithmetic alone.

### No gaming

Never reduce sample count, remove adversarial slices, downweight rare categories, cherry-pick seeds, conceal abstentions, re-label gold post hoc, move thresholds, or use model self-judgments to declare success. Distributional shifts and adversarial novelty are not solved by perfect training-set scores.

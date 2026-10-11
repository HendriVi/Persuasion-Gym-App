# Persuasion Gym — Uncertainty Rules

Version: 1.0.0  
Status: Normative policy  
Depends on: Persuasion Gym Common Schema v1.x

This package defines how every specialist in Persuasion Gym represents, propagates, reports, and resolves uncertainty. It does **not** replace domain evidence standards. It prevents a specialist from turning an observation, classification, hypothesis, factual verdict, causal claim, person-specific inference, or intent inference into a stronger kind of claim merely through confident prose.

## Core rule

**Uncertainty is multidimensional. Never compress it into one confidence score.**

Every material assertion should carry the dimensions that apply to it:

- epistemic status — how the assertion was obtained;
- factual verification status — whether a checkable proposition is externally established;
- causal/mechanistic evidence strength — how well a proposed relation is supported;
- evidence basis — what type of evidence supports that grade;
- person-specific activation — whether a population-level mechanism is evidenced in this episode/person;
- person evidence mode — what episode-level evidence exists;
- intent status — how directly intent is known;
- confidence — certainty that the assigned classification/status is appropriate;
- scope — population, context, time, modality, task, and other limits.

A high confidence score may accompany `SPECULATIVE` or `UNKNOWN`: it means the analyst is confident that **that is the correct status**, not that the underlying proposition is probably true.

## Integration

This policy is binding on Rhetorical Structure Analysis, Critical Thinking, De-Spin, Fact-Check, Persuasion Mechanism Analysis, Influence Systems Analysis, Manipulation Assessment, countermeasure generation, and Persuasion Training.

Training answer keys may score only dimensions that are sufficiently resolved for the skill being tested. Unresolved dimensions must be excluded from grading or flagged for review.

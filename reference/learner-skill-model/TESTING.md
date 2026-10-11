# Regression Requirements

The implementation must pass at least these tests.

1. One wrong item cannot create a recurring-error pattern.
2. A recurring pattern requires >=3 occurrences in >=5 eligible opportunities.
3. Pattern records cite exact attempts.
4. Trait labels such as `gullible`, `biased_personality`, or `suggestible` are absent from the schema.
5. Assisted attempts cannot count as mastery-eligible by default.
6. Confidence must be pre-feedback to enter calibration metrics.
7. Correctness and confidence are stored separately.
8. Fewer than 8 calibration judgments returns `INSUFFICIENT_DATA`.
9. High-confidence errors are tracked by skill, not globally interpreted as personality.
10. Transfer cannot be inferred from paraphrase-only practice.
11. Transfer attempts preserve the latent skill and record context change.
12. Cross-domain and cross-modality are separately representable.
13. One correct transfer item cannot produce `TRANSFER_VERIFIED`.
14. Delayed verification requires at least two eligible delayed attempts on distinct dates.
15. `DELAYED_VERIFIED` cannot be reached from a single immediate session.
16. A skill can return to `NEEDS_REPAIR` after later evidence.
17. State transitions cite attempt evidence.
18. Invalidated answer keys exclude affected evidence from aggregates.
19. Historical attempts remain after invalidation.
20. Only deliberately tested `skill_ids` may update.
21. Context-specific claims require at least 3 relevant attempts.
22. Political content does not create an ideology field.
23. No protected-class or mental-health inference field exists.
24. `PERSON_ACTIVATION_OVERREACH` can be tracked without inferring gullibility.
25. `INTENT_OVERREACH` can be tracked independently of political direction.
26. `FALSEHOOD_MANIPULATION_COLLAPSE` and `MANIPULATION_FALSEHOOD_COLLAPSE` remain distinct errors.
27. Population-to-person overreach is distinct from causal overreach generally.
28. Rolling accuracy uses only eligible evidence.
29. Answer-key review blocks mastery eligibility.
30. Recommendation output names the skill and evidence, not a vague trait.
31. Same skill may show different evidence by domain without creating contradictory global labels.
32. Mastery thresholds are explicitly marked configurable operational heuristics.
33. The example model validates against JSON Schema.
34. The valid update fixture produces a valid model.
35. Unknown skill IDs fail semantic validation.
36. Dimension skills not listed as deliberately tested fail semantic validation.
37. Recurring pattern below recurrence threshold fails semantic validation.
38. Recommendation evidence refs must ultimately be auditable to attempt records (implementation requirement).
39. Learner model never alters answer keys.
40. Learner model can be recomputed from the attempt ledger.

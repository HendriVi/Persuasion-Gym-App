# Regression Tests — Uncertainty Rules

A compliant implementation must pass at least the following tests.

1. Authority cue can be `ANNOTATED` while source credibility remains unverified.
2. Fear cue cannot by itself produce `SUPPORTED_IN_EPISODE` fear/threat activation.
3. Artifact-only mechanism analysis cannot exceed `CANDIDATE` activation.
4. Repetition across specialist outputs cannot count as independent corroboration.
5. A failed search cannot produce `CONTRADICTED` without contrary evidence.
6. `VERIFIED_WITH_QUALIFICATION` must preserve the material qualifier in prose.
7. A robust behavioral effect cannot automatically make one mechanism `ESTABLISHED`.
8. Significant mediation cannot automatically make a mechanism `ESTABLISHED` or person activation `EXPERIMENTALLY_IDENTIFIED`.
9. An observational system relation cannot be described as causal unless independently justified.
10. A platform-specific finding cannot silently generalize to all platforms.
11. Between-person evidence cannot silently become within-person causal evidence.
12. Group-level evidence cannot establish activation in one individual.
13. `confidence=0.99` cannot upgrade `SPECULATIVE` evidence.
14. High confidence in `UNKNOWN` is permitted and interpreted correctly.
15. Two materially plausible mechanisms must remain separate until discriminated.
16. A downstream module cannot upgrade an upstream status without new relevant evidence.
17. A contradicted load-bearing factual claim triggers `REANALYSIS_REQUIRED` rather than automatic downstream falsity.
18. A narrowed upstream scope propagates or requires an explicit extrapolation marker.
19. Reposts and derivative articles cannot count as independent corroborating sources.
20. A source's self-report of intent is `REPORTED` evidence unless the intent field is explicitly supported under intent rules.
21. Tactic presence cannot by itself yield `STRONGLY_INFERRED` intent.
22. A false claim cannot by itself yield an inference of knowing deception.
23. A system loop cannot have a stronger overall grade than its weakest indispensable edge without direct pathway evidence.
24. `UNKNOWN` upstream does not automatically make unrelated downstream fields unknown.
25. `UNVERIFIED` and `UNRESOLVED` remain distinct.
26. `MIXED` evidence cannot be rewritten as “the evidence shows” without qualification.
27. Learner confidence and analyst confidence remain separate.
28. Training cannot score an answer-key dimension under `REVIEW_REQUIRED`.
29. Multiple accepted interpretations can be represented explicitly in an ambiguity exercise.
30. Natural-language generation must use status-matched wording.
31. `OBSERVED` is not used for a taxonomy label that required specialist interpretation; use `ANNOTATED`.
32. `REPORTED` is not treated as `VERIFIED` unless an independent verification step establishes it.
33. Self-reported fear can support a reported subjective state but cannot alone identify the mechanism that caused it.
34. New person-level evidence can upgrade activation without upgrading population-level mechanism evidence.
35. New population-level evidence can upgrade mechanism evidence without upgrading person-specific activation.
36. Evidence basis is not treated as an evidence-quality score.
37. `OUTDATED` is used only when time materially affects the claim's current validity.
38. A normative/value claim receives `NOT_APPLICABLE` for factual verification unless it embeds checkable factual subclaims.
39. A deterministic calculation from verified inputs may be `DERIVED`; a causal interpretation may not.
40. Historical records are versioned; review does not silently mutate earlier assertions.

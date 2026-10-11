# Common Schema Regression Tests

A release is not ready unless these invariants are tested.

1. A complete valid fixture passes JSON Schema Draft 2020-12 validation.
2. Unknown top-level fields fail validation.
3. Unknown fields inside strict core records fail validation.
4. Duplicate object IDs fail semantic validation.
5. A dangling `segment_ref` fails semantic validation.
6. A dangling `claim_ref` fails semantic validation.
7. A dangling `assertion_ref` fails semantic validation.
8. Taxonomy IDs remain external vocabulary IDs rather than object refs.
9. Mechanism registry IDs remain external vocabulary IDs rather than object refs.
10. `verification_status` cannot be used in place of `evidence_strength`.
11. `person_specific_activation` remains independent of population evidence grades.
12. A mechanism candidate can be `SUPPORTED` at population level while activation remains `CANDIDATE`.
13. An unverified artifact claim does not invalidate an observed rhetorical annotation.
14. A contradicted claim can trigger `REANALYSIS_REQUIRED` without silently changing downstream records.
15. `manipulation.overall` cannot be encoded as a rhetorical taxonomy label.
16. A system relation requires separate `evidence_basis` and `evidence_strength`.
17. An unclosed system path cannot be labeled `REINFORCING` or `BALANCING` by the semantic validator.
18. Human summary is explicitly non-authoritative.
19. Assertions record `origin_skill`.
20. Assertions can carry confidence but confidence does not replace epistemic/evidence status.
21. Training with `DRAFT` answer key cannot record scored dimensions.
22. Training with `REVIEW_REQUIRED` answer key cannot record scored dimensions.
23. Fact-check records refer to shared canonical claim IDs rather than copies of claim text.
24. Rhetorical annotations reference shared artifact segment IDs.
25. Mechanism pathways reference rhetorical annotation IDs.
26. Systems relations reference canonical system variables.
27. Feedback loops reference canonical relation IDs.
28. Countermeasures state explicit target refs.
29. Major/minor/patch migrations never silently upgrade uncertainty.
30. Earlier specialist enum values are normalized through an adapter, not accepted ad hoc into canonical fields.

## Command

```bash
python scripts/validate_analysis.py examples/simple-ad.analysis.json
```

Expected output: `VALID`.

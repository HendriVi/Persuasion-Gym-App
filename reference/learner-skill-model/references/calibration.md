# Confidence Calibration

## Atomic scoring

Use binary or otherwise objectively scored judgments wherever calibration is calculated.
Do not calculate calibration from an unstructured holistic essay grade.

For binary outcome `y` and pre-feedback confidence `p`:

- `brier = (p-y)^2`
- `signed_error = p-y`
- `absolute_error = |p-y|`

## Aggregation

Aggregate separately by skill. Add context slices only when >=3 observations exist in that slice.

Do not emit a stable calibration label for a skill until >=8 relevant judgments.

Default operational labels:

- `INSUFFICIENT_DATA` — n < 8
- `WELL_CALIBRATED` — mean absolute error <= 0.20 and |mean signed error| <= 0.10
- `OVERCONFIDENT_PATTERN` — mean signed error > 0.10
- `UNDERCONFIDENT_PATTERN` — mean signed error < -0.10
- `MIXED` — substantial error without stable signed direction

These thresholds are configurable operational heuristics, not universal psychometric constants.

## High-confidence errors

Define high-confidence error by default as incorrect judgment with confidence >=80/100.
Track counts by skill and error tag.

Never infer a global trait from high-confidence errors.

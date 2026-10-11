# Update Policy

## Append then recompute

Never mutate historical attempts. Append `AttemptEvidence`; recompute summaries deterministically.

## Mastery eligibility

Default eligible only when:
- answer-key status is `FROZEN_VALID`;
- response was committed before feedback;
- confidence was captured before feedback when required;
- assistance = `UNAIDED`;
- skill was deliberately tested;
- dimension was scoreable.

## Recency window

Use all valid evidence for auditability, plus a default rolling window of the 8 most recent eligible attempts for current performance summaries.

## Critical errors

The following default to critical for mastery gating when relevant:
- `PERSON_ACTIVATION_OVERREACH`
- `INTENT_OVERREACH`
- `CAUSAL_OVERREACH`
- `MEDIATION_MECHANISM_OVERREACH`
- `FALSEHOOD_MANIPULATION_COLLAPSE`
- `MANIPULATION_FALSEHOOD_COLLAPSE`
- `UNCERTAINTY_ERASURE`
- `SYSTEM_LOOP_FORCED`

## Recompute on invalidation

If an answer key changes:
1. mark affected attempts `INVALIDATED`;
2. retain them in audit history;
3. remove them from eligible aggregates;
4. recompute state, calibration, patterns, transfer, delay;
5. record a `ModelRevisionEvent`.

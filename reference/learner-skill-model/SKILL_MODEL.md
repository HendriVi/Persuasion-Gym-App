# Persuasion Gym User Skill Model

## 1. Purpose

Represent what the learner has demonstrated, missed, overclaimed, calibrated well or poorly, and transferred across contexts.

The model MUST support adaptive exercise selection without inferring vague traits or stable personality characteristics.

Canonical principle:

> Track observable performance on named tasks, with evidence and scope. Do not infer global traits from local errors.

Allowed:

> `intent_overreach` occurred on 3 of the last 5 unaided intent-discipline opportunities in political and advertising items.

Forbidden:

> The learner is gullible, biased, suggestible, irrational, manipulative, or bad at critical thinking.

---

## 2. Unit of evidence

The atomic unit is an `AttemptEvidence` record.

Every scored attempt MUST store:

- stable `attempt_id`;
- timestamp;
- item and answer-key version;
- exact `skill_ids` deliberately tested;
- domain and modality;
- training mode;
- transfer classification;
- delayed-retrieval status;
- assistance/hint level;
- pre-feedback confidence;
- dimension-level score;
- error tags;
- whether the result is eligible for mastery evidence.

Do not update a skill merely because it was incidentally present in the item.

---

## 3. Skill representation

Each skill has a `SkillState` rather than one opaque score.

Required evidence dimensions:

1. **retrieval** — can the learner produce the relevant judgment unaided?
2. **discrimination** — can the learner distinguish it from plausible confounds?
3. **calibration** — does confidence track correctness?
4. **transfer** — does the skill survive meaningful changes in surface/domain/modality?
5. **delay** — does performance persist after a delay?
6. **error structure** — which specific failure modes recur?

The model may maintain numerical summaries for routing, but no numerical summary may replace the underlying evidence ledger.

---

## 4. Canonical skill states

Use exactly:

- `UNSEEN`
- `INTRODUCED`
- `RETRIEVING`
- `DISCRIMINATING`
- `PROVISIONAL_MASTERY`
- `TRANSFER_VERIFIED`
- `DELAYED_VERIFIED`
- `NEEDS_REPAIR`

These are operational training states, not psychological diagnoses.

### State semantics

**UNSEEN** — no valid scored evidence.

**INTRODUCED** — at least one valid exposure or scored attempt; insufficient evidence of stable retrieval.

**RETRIEVING** — repeated unaided retrieval evidence exists, but discrimination/transfer is not yet established.

**DISCRIMINATING** — learner can distinguish the target from at least one documented confusable alternative across more than one item.

**PROVISIONAL_MASTERY** — repeated unaided performance, adequate calibration, and no unresolved recurrent critical error for this skill. Still context-bounded.

**TRANSFER_VERIFIED** — provisional mastery plus successful transfer to materially different contexts.

**DELAYED_VERIFIED** — transfer-verified or otherwise mature performance survives delayed retrieval.

**NEEDS_REPAIR** — later evidence reveals a recurring conceptual error, overclaim, or collapse that invalidates the current mastery assumption.

No state is permanent.

---

## 5. Evidence gates, not vibe-based promotion

Promotion requires explicit evidence gates. Default thresholds are operational heuristics and MUST be configurable; they are not claims about universal learning science optima.

Default promotion profile:

### INTRODUCED

- at least 1 valid attempt or guided introduction.

### RETRIEVING

- at least 3 mastery-eligible unaided attempts;
- at least 2 correct;
- no unresolved answer-key review.

### DISCRIMINATING

- RETRIEVING gates met;
- at least 2 mastery-eligible discrimination attempts;
- at least 1 documented confusable pair/set tested;
- >= 75% discrimination accuracy over eligible evidence.

### PROVISIONAL_MASTERY

- at least 8 mastery-eligible unaided attempts;
- at least 2 distinct contexts;
- rolling eligible accuracy >= 80% over the most recent 8 relevant attempts;
- mean absolute calibration error <= 20 percentage points over at least 8 binary judgments, OR calibration marked `INSUFFICIENT_DATA`;
- no recurring critical error currently open.

`INSUFFICIENT_DATA` for calibration does not prove calibration; it simply prevents fabricated certainty. Exercise routing should continue to collect confidence evidence.

### TRANSFER_VERIFIED

- PROVISIONAL_MASTERY;
- at least 3 mastery-eligible transfer attempts;
- at least 2 materially distinct contexts from the primary learning context;
- transfer accuracy >= 67%;
- no transfer-critical overclaim on the latest two transfer opportunities.

### DELAYED_VERIFIED

- TRANSFER_VERIFIED or equivalent mature evidence;
- at least 2 mastery-eligible delayed retrieval attempts on different dates;
- latest delayed attempt correct without high-level assistance.

### NEEDS_REPAIR

Set when any of these occur:

- a critical error tag recurs on >= 3 of the last 5 eligible opportunities for the skill;
- a supposedly mastered distinction fails repeatedly in transfer;
- high-confidence errors recur after provisional mastery;
- an answer-key revision invalidates material prior evidence.

Do not demote based on one difficult item.

---

## 6. Assistance weighting

Attempts are classified:

- `UNAIDED`
- `CONCEPTUAL_CUE`
- `CONTRAST_CUE`
- `PARTIAL_STRUCTURE`
- `EXPLICIT_EXPLANATION`

Mastery eligibility defaults:

- `UNAIDED` — yes
- `CONCEPTUAL_CUE` — no for mastery; may count as repair evidence
- `CONTRAST_CUE` — no for mastery; may count as repair evidence
- `PARTIAL_STRUCTURE` — no
- `EXPLICIT_EXPLANATION` — no

A later fresh unaided item is required before assisted success changes mastery state.

---

## 7. Confidence calibration

Confidence MUST be collected before feedback.

For a binary scored judgment:

`p = confidence / 100`

`y = 1 if correct else 0`

Store:

- `brier = (p - y)^2`
- `signed_calibration_error = p - y`
- `absolute_calibration_error = abs(p - y)`

Interpret signed error:

- positive on error-prone sets -> overconfidence tendency for that named skill/context;
- negative on correct sets -> underconfidence tendency for that named skill/context.

Do not infer a global personality characteristic.

Do not produce a stable calibration label with fewer than 8 relevant binary judgments. Before that use `INSUFFICIENT_DATA`.

Canonical calibration labels:

- `INSUFFICIENT_DATA`
- `WELL_CALIBRATED`
- `OVERCONFIDENT_PATTERN`
- `UNDERCONFIDENT_PATTERN`
- `MIXED`

See `references/calibration.md`.

---

## 8. Error patterns

Errors are event tags tied to a skill and evidence records.

A recurring pattern requires:

- at least 3 occurrences;
- at least 5 eligible opportunities for that error to have occurred;
- the same canonical error tag;
- evidence references.

A recurring pattern record MUST say what happened, where, and how often.

Example:

> `MECHANISM_FROM_CUE` occurred in 3/5 recent unaided authority/social-proof mechanism opportunities across advertising and public-affairs items.

Never rewrite this as:

> "susceptible to authority".

---

## 9. Transfer

Transfer is not a paraphrase.

Each attempt records:

- source/learning context;
- current domain;
- modality;
- source type;
- emotional tone;
- explicitness;
- distractor structure;
- social context;
- `transfer_level`.

Canonical transfer levels:

- `NONE`
- `NEAR`
- `CROSS_DOMAIN`
- `CROSS_MODALITY`
- `FAR`

A transfer result counts only if the latent skill is preserved and at least one material surface/context dimension changes.

See `references/transfer.md`.

---

## 10. Domain conditionality

Store skill evidence both globally and by meaningful context slices when sample size permits.

Allowed:

> Strong rhetorical-device discrimination in advertising; insufficient evidence in political content.

Forbidden:

> Good at rhetoric.

Do not create context-specific conclusions from fewer than 3 relevant attempts.

---

## 11. Political and identity safeguards

The learner model MUST NOT infer or store:

- political affiliation;
- ideology;
- religion;
- race/ethnicity;
- sexual orientation;
- mental-health diagnosis;
- personality pathology;
- protected-class identity;
- inferred vulnerability traits;

unless a completely separate product requirement, consent process, and privacy review explicitly authorize it. These fields are unnecessary for Persuasion Gym skill adaptation.

Political items may be stored only as task-domain metadata such as `public_affairs`, not as evidence about the learner's ideology.

---

## 12. Answer-key dependency

Attempt evidence is invalid for mastery when:

- answer key is under review;
- scored dimension is unresolved;
- relevant gold label was later invalidated;
- the item leaked the target before commitment;
- confidence was collected after feedback;
- assistance level is unknown for an assisted attempt.

Invalidated evidence remains in the audit log but is excluded from aggregates.

---

## 13. Update invariants

1. Update only deliberately tested skills.
2. Preserve raw attempt evidence.
3. Never overwrite history; append and recompute summaries.
4. Never convert a recurring error into a personality label.
5. Never count assisted success as unaided mastery.
6. Never count near paraphrase as cross-domain transfer.
7. Never merge confidence with correctness.
8. Never infer transfer from high in-domain accuracy.
9. Never infer a skill deficit from one item.
10. Never promote when the relevant answer key is unresolved.
11. If old evidence is invalidated, recompute downstream summaries.
12. State transitions must cite the evidence IDs that justified them.

---

## 14. Exercise-routing outputs

The user model may recommend the next training target using only skill evidence.

Priority factors:

- `NEEDS_REPAIR` state;
- due delayed retrieval;
- recurring critical error;
- high-confidence error cluster;
- weak discrimination against a known confound;
- insufficient transfer evidence after provisional mastery;
- long time since last valid evidence;
- sparse evidence on strategically important skills.

Do not choose exercises merely to maximize engagement or apparent success.

---

## 15. Human-facing progress language

Prefer:

> You correctly distinguished authority cues from actual expertise in 4/5 recent unaided items. Two cross-domain transfer trials remain before transfer can be considered verified.

> In 3 of 5 recent mechanism items, you inferred person-specific activation from the message alone. Confidence on those errors averaged 84%, so this is the highest-priority repair target.

Avoid:

> You are easily manipulated by authority.

> You have confirmation bias.

> You are a gullible thinker.

---

## 16. Minimum viable user model

For production v1, the model MUST support:

- attempt ledger;
- canonical skill registry;
- per-skill mastery state;
- per-skill retrieval accuracy;
- assistance tracking;
- canonical error patterns;
- pre-feedback confidence;
- calibration metrics;
- transfer evidence;
- delayed-retrieval evidence;
- context slices;
- evidence-backed next-target recommendation;
- answer-key invalidation/recomputation.

Everything else is optional.

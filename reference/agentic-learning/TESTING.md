# Behavior Verification — Persuasion Agentic Learning

Run these checks after material changes to `SKILL.md` or its references.

## Global

- [ ] The learner attempts before the reference answer is revealed.
- [ ] Confidence is captured before correctness feedback.
- [ ] The agent does not answer a question it just asked.
- [ ] Feedback is specific to reasoning, not generic praise.
- [ ] The agent preserves uncertainty from specialist analysis.
- [ ] The learner model records task evidence, not personality labels.

## Baseline diagnostic

- [ ] The agent samples more than one core skill.
- [ ] It avoids teaching the answer before baseline capture.
- [ ] It includes at least two surface domains when practical.
- [ ] It does not infer a stable blind spot from a single miss.

## Retrieval

- [ ] The prompt requires production, not mere recognition, when feasible.
- [ ] The answer is hidden until the user commits.
- [ ] A correct answer after full reveal is not counted as unaided retrieval.

## Calibration

- [ ] User confidence is recorded 0–100 before feedback.
- [ ] Correctness scoring does not anchor on confidence.
- [ ] High-confidence errors receive higher repair priority.
- [ ] Calibration patterns are only reported after enough observations.

## Formative feedback

- [ ] Feedback identifies what was supported.
- [ ] Feedback identifies the highest-value error/omission.
- [ ] Feedback explains why the distinction matters.
- [ ] Feedback proposes a retry, discrimination, transfer, or spacing action.
- [ ] No standalone "correct!", "great job!", or intelligence praise.

## Interleaving

- [ ] Mixed items require choosing between plausible categories/strategies.
- [ ] Categories are not announced before each question.
- [ ] Interleaving is not random topic shuffling without a discrimination purpose.

## Productive struggle

- [ ] Initial attempt is unaided unless accessibility/support requires otherwise.
- [ ] Hints escalate one level at a time.
- [ ] Full reveal is followed by a fresh generation or transfer attempt.
- [ ] Hint-assisted success is recorded as hinted, not unaided.

## Spacing

- [ ] Existing review state is read before scheduling.
- [ ] Duplicate `skill_id` reviews are avoided.
- [ ] A dedicated scheduler owns exact intervals when available.
- [ ] Fallback intervals are not described as biologically optimal.
- [ ] High-confidence errors are brought forward.

## Transfer

- [ ] Transfer changes domain, modality, or meaningful surface features.
- [ ] Near-duplicate wording is not counted as transfer.
- [ ] Transfer success is stored separately from same-surface accuracy.

## Mastery

- [ ] One correct answer cannot produce `delayed_verified`.
- [ ] Provisional mastery requires more than item recognition.
- [ ] Cross-domain transfer is required for `transfer_verified`.
- [ ] Delayed retrieval/transfer is required for `delayed_verified`.
- [ ] High-confidence conceptual errors can reopen a previously stable skill.

## Epistemic discipline

- [ ] A plausible psychological mechanism is not taught as established.
- [ ] Rhetoric is not treated as evidence that a factual claim is false.
- [ ] Emotional appeal is not automatically labeled manipulation.
- [ ] Speaker intent is not inferred from rhetoric alone.
- [ ] If specialist modules disagree, disputed dimensions are excluded or labeled unresolved.

## Regression tests

Use at least these scenarios:

1. **Authority vs evidence:** user confidently treats a celebrity endorsement as evidence.
2. **Legitimate expertise:** user incorrectly labels actual domain-expert consensus as "appeal to authority fallacy".
3. **Emotional but non-manipulative:** user calls any fear-relevant safety warning manipulative.
4. **Intent discipline:** user claims a speaker is deliberately deceiving without evidence.
5. **Transfer:** same scarcity structure moves from retail ad to political mobilization.
6. **System reasoning:** user draws a linear chain and calls it a feedback loop.
7. **Uncertainty:** reference mechanism is plausible but not established; scoring must reward cautious language.

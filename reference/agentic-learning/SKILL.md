---
name: persuasion-agentic-learning
description: >-
  Learning-science substrate for Persuasion Gym. Use when converting rhetoric,
  persuasion, argument, manipulation, or influence-analysis content into adaptive
  practice that improves unaided detection, explanation, calibration, resistance,
  and transfer. Implements attempt-before-feedback, retrieval practice, generation,
  spacing, interleaving, metacognitive confidence judgments, formative feedback,
  productive struggle, and delayed transfer testing. Does not determine rhetorical
  truth or psychological mechanism itself; it consumes validated outputs from the
  relevant analysis skills and trains the user on them.
license: MIT-compatible original adaptation; see README.md for upstream inspiration
compatibility: AgentSkills-compatible agents and app orchestration pipelines
metadata:
  version: "0.1"
  project: "Persuasion Gym"
  role: "learning orchestration and learner modeling"
---

# Persuasion Agentic Learning

## Purpose

Turn Persuasion Gym from an **AI analyzer** into an **adaptive cognitive training system**.

The skill does not primarily teach definitions. Its job is to improve the user's ability to:

1. detect influence-relevant features without assistance,
2. explain the mechanism rather than only name the tactic,
3. distinguish rhetoric, argument quality, factual truth, and manipulation risk,
4. calibrate confidence to actual performance,
5. resist cue-driven or identity-congruent errors,
6. transfer the learned discrimination to unfamiliar domains,
7. retain the skill after delay.

Core principle:

> A fluent AI explanation is not evidence that the user can perform the analysis unaided.

Therefore, **attempt precedes explanation**, and **delayed transfer precedes mastery**.

---

# 1. Boundaries

## This skill owns

- retrieval and generation before feedback,
- confidence elicitation and calibration,
- exercise sequencing,
- difficulty adjustment,
- interleaving,
- spacing / revisit scheduling,
- hint ladders,
- formative feedback,
- error-pattern tracking,
- delayed transfer tests,
- learner-state updates.

## This skill does not own

- factual verification,
- claim provenance,
- determining whether an argument is valid,
- identifying rhetorical devices from first principles,
- asserting psychological mechanisms,
- inferring hidden intent,
- deciding whether communication is manipulative without the relevant analysis module.

Those judgments come from specialist skills. This skill **trains on their reconciled outputs**.

When specialist modules disagree, do not convert disagreement into a teaching key. Mark the item unresolved or exclude the disputed dimension from scoring.

---

# 2. Learning unit

The atomic unit is not a topic such as "propaganda". It is a **trainable discrimination or inference**.

Examples:

- distinguish authority cue from evidence,
- identify the omitted comparator in a statistical claim,
- distinguish framing from factual falsity,
- infer which psychological variable a scarcity cue is hypothesized to affect,
- separate speaker intent from functional effect,
- identify a reinforcing social feedback loop,
- generate a counterframe that preserves the facts,
- decide whether manipulation risk is supported or merely suspected.

Each trainable unit must have a stable `skill_id` and an explicit scoring rubric. Load `references/learner-model.md` and `assets/training-item-schema.md` when creating or updating training state.

---

# 3. Non-negotiable learning rules

## Rule 1 — Commit before reveal

For scored practice, obtain the user's answer **before** showing the reference analysis.

Do not telegraph the expected answer in the question wording.

Capture:

- answer,
- confidence from 0–100,
- optional rationale,
- hints used.

The user's confidence must be recorded before correctness feedback.

## Rule 2 — Score reasoning dimensions separately

Do not reduce a response to one binary score when the task contains distinct abilities.

Possible dimensions include:

- observation accuracy,
- claim/argument reconstruction,
- rhetorical classification,
- mechanism inference,
- evidence discipline,
- manipulation/intent discipline,
- systems reasoning,
- countermeasure quality.

A learner can identify the device correctly while giving the wrong mechanism. Preserve that distinction.

## Rule 3 — Feedback is formative, not congratulatory

After the attempt:

1. state what part of the reasoning was supported,
2. identify the most important error or omission,
3. explain **why** it matters,
4. provide the minimum corrective model needed,
5. ask for a retry, discrimination, or generation step when useful.

Avoid standalone "correct", "incorrect", "great job", or ability praise.

## Rule 4 — Correct once is not mastery

Do not mark a skill mastered from one successful trial.

Mastery requires converging evidence from:

- successful unaided retrieval,
- acceptable confidence calibration,
- at least one different surface context,
- preferably a delayed revisit.

When delayed evidence is unavailable, use `provisional_mastery`, not `mastered`.

## Rule 5 — Test transfer, not memorized wording

Change surface features while preserving the target structure.

Examples:

- advertising → political speech,
- political rhetoric → health claim,
- health claim → negotiation,
- obvious authority cue → subtle credential framing,
- explicit social proof → implied norm consensus.

Do not count a near-duplicate item as transfer.

## Rule 6 — Interleave discriminable confusions

Interleaving is most useful when the learner must choose between plausible alternatives.

Mix, for example:

- authority vs expertise evidence,
- framing vs omission,
- emotional appeal vs manipulation,
- correlation vs causal claim,
- social proof vs actual independent corroboration,
- persuasion vs coercive pressure.

Do not interleave randomly merely for variety.

## Rule 7 — Space by learner evidence, not a fixed calendar alone

Use observed uncertainty, error recurrence, calibration error, and prior successful retrieval to prioritize revisits.

If a dedicated scheduler such as FSRS is available, pass the item state to it. Otherwise use the fallback policy in `references/spacing-policy.md`.

Do not present the fallback intervals as biologically optimal.

## Rule 8 — Productive struggle must remain productive

Difficulty should expose the target distinction, not bury it under irrelevant complexity.

Escalate support gradually:

1. no hint,
2. conceptual cue,
3. discrimination cue,
4. partial structure,
5. full explanation.

After a full reveal, require a fresh generation or transfer attempt before considering the interaction complete.

## Rule 9 — Track errors, not personality

Learner profiles describe **observable performance patterns**, never character traits.

Allowed:

> Missed omitted-baseline problems in 4 of the last 6 statistical persuasion items.

Not allowed:

> Gullible with statistics.

## Rule 10 — Preserve epistemic uncertainty

If the reference analysis labels a mechanism `plausible`, the training item must not score a learner as wrong for refusing to call it established.

Learning feedback must preserve the evidence status of the underlying claim.

---

# 4. Core training loop

Use this loop for most Persuasion Gym exercises.

## Step 1 — Select target

Choose one or two trainable units from the learner model.

Priority increases when a skill is:

- repeatedly missed,
- high-confidence wrong,
- due for spaced retrieval,
- weak in transfer,
- foundational for another skill.

Avoid training too many new distinctions in one item.

## Step 2 — Select stimulus

Choose an artifact appropriate to the target:

- headline,
- advertisement,
- speech excerpt,
- debate statement,
- negotiation move,
- sales pitch,
- health claim,
- social-media post,
- institutional message.

The stimulus must have a validated answer key for every scored dimension.

## Step 3 — Elicit unaided judgment

Ask one clear task at a time.

Examples:

- "What is the main influence technique here?"
- "What is the message asking you to infer without saying explicitly?"
- "Which human variable is this cue most plausibly acting on?"
- "What would falsify the causal claim?"
- "Is manipulation established, plausible, or unsupported? Why?"

Then obtain confidence 0–100 before revealing the reference answer.

## Step 4 — Blind evaluation

Score the user's answer against the rubric **before** generating coaching feedback.

Do not let the user's confidence change the correctness judgment.

Store:

- dimension scores,
- error tags,
- omitted elements,
- confidence,
- hints,
- evidence status of the answer key.

## Step 5 — Compare

Show the delta between the learner model and reference model:

- `caught` — correct relevant elements,
- `missed` — supported elements absent from the response,
- `misclassified` — element present but assigned to wrong level/category,
- `overreach` — claim stronger than evidence permits,
- `phantom` — suspected mechanism/tactic not supported by the item,
- `calibration` — confidence relative to performance.

Keep the comparison descriptive rather than moralizing.

## Step 6 — Formative feedback

Prioritize the smallest change that would improve the user's next attempt.

Feedback should typically contain:

- the key distinction,
- the causal or logical reason for the distinction,
- one contrast/counterexample if needed.

Do not dump the entire ontology after one error.

## Step 7 — Retry or near transfer

When the error is trainable in-session, give a second item with altered surface details.

Do not simply repeat the same sentence.

## Step 8 — Update learner state

Update only dimensions actually tested.

Do not infer competence in untested dimensions from a general score.

## Step 9 — Schedule delayed retrieval

Queue skills that are:

- new,
- uncertain,
- high-confidence wrong,
- repeatedly missed,
- provisionally mastered but not transfer-tested.

## Step 10 — Test far transfer when appropriate

After reasonable success, move to a different domain or format while preserving the underlying mechanism.

Example:

> If the learner identified scarcity correctly in a sales ad, test a subtler scarcity/urgency structure in political mobilization or negotiation.

Only then consider promoting the skill toward mastery.

---

# 5. Calibration

Persuasion Gym should train **knowing when you might be wrong**, not only answer accuracy.

For each scored judgment, capture confidence before feedback.

Interpret patterns cautiously:

- **high confidence + wrong** → priority correction; likely calibration failure for this item type,
- **low confidence + correct** → knowledge may be present but unstable,
- **high confidence + correct** → strong evidence, but still requires transfer/delay,
- **low confidence + wrong** → recognized uncertainty; train discrimination without treating calibration as the main failure.

Do not infer a stable trait from a few observations.

For progress review, report calibration by `skill_id` or task family when sample size is adequate. Load `references/learner-model.md`.

---

# 6. Exercise modes

## A. Detect

Goal: identify an observable feature without explaining mechanism.

Example:

> Which rhetorical device is present?

## B. Decompose

Goal: separate claim, implication, evidence, omission, and requested action.

## C. Explain mechanism

Goal: connect a validated rhetorical cue to a supported or explicitly hypothesized psychological pathway.

## D. Compare

Goal: distinguish two easily confused mechanisms or argument structures.

## E. Counterframe

Goal: preserve the relevant facts while changing the frame, salience, or implied interpretation.

## F. Resist / verify

Goal: generate the smallest check or delay that reduces vulnerability to the influence attempt.

## G. Systems map

Goal: place source, message, person, social response, amplification, outcomes, and feedback into a causal/system hypothesis without laundering uncertainty into arrows.

## H. Transfer

Goal: recognize the same underlying structure in a different domain, modality, or rhetorical surface.

---

# 7. Adaptive exercise selection

Use the policy in `references/exercise-selection.md`.

In brief:

1. prefer due or weak skills over already-stable skills,
2. prefer recurring error types over random new material,
3. use high-confidence errors as high-value targets,
4. introduce contrasts when category confusion is the problem,
5. switch domains when near-transfer is stable,
6. reduce complexity when failure may be caused by extraneous load,
7. increase ambiguity only after core distinctions are reliable.

Do not optimize solely for session score or completion rate. Immediate fluency can conflict with durable learning.

---

# 8. Spacing

Spacing is a scheduling problem, not a universal fixed interval.

Use a dedicated scheduler when available. When unavailable, load `references/spacing-policy.md`.

Revisit priority should depend on:

- time since last successful retrieval,
- current mastery state,
- confidence error,
- number of prior retrievals,
- transfer success,
- error recurrence,
- importance of the skill in the dependency graph.

A skill can be accurate in immediate practice yet still require delayed verification.

---

# 9. Interleaving

Interleave when the learning objective involves **strategy selection or discrimination**.

Good interleaving set:

1. authority cue,
2. independent evidence,
3. social proof,
4. prestige framing,
5. legitimate expert consensus.

The learner must decide which structure is present rather than applying the same label repeatedly.

Avoid announcing the category before each question; that removes the discrimination demand.

---

# 10. Metacognitive reflection

Reflection should be short and evidence-linked.

Useful prompts include:

- "What cue made you choose that label?"
- "What evidence would have changed your answer?"
- "Where was your confidence higher than the evidence justified?"
- "What distinction do you want to notice earlier next time?"

Do not force reflection after every trivial item. Use it after meaningful errors, calibration mismatches, transfer failures, or session summaries.

---

# 11. Cognitive-load control

When the user fails an item, first determine whether the target distinction was actually tested cleanly.

Potential overload sources:

- too many rhetorical devices at once,
- long unfamiliar source material,
- simultaneous fact-checking and mechanism inference,
- jargon before concept acquisition,
- multiple nested social/system levels.

If extraneous load is high, simplify the artifact while preserving the target structure.

Do not interpret overload as lack of competence.

---

# 12. Mastery states

Use these states unless the application defines more granular ones:

- `unseen`
- `introduced`
- `retrieving`
- `discriminating`
- `provisional_mastery`
- `transfer_verified`
- `delayed_verified`
- `needs_repair`

Promotion should be evidence-based.

A reasonable default logic:

- successful first retrieval → `retrieving`,
- repeated discrimination across non-identical items → `discriminating`,
- accurate + calibrated near transfer → `provisional_mastery`,
- accurate cross-domain transfer → `transfer_verified`,
- accurate delayed transfer/retrieval → `delayed_verified`.

Any high-confidence conceptual error can move a supposedly stable skill to `needs_repair` until re-tested.

These are orchestration states, not claims about neural memory strength.

---

# 13. Learner model

Maintain a persistent learner model when the app supports persistence.

Track at minimum:

- `skill_id`,
- mastery state,
- attempts,
- unaided accuracy,
- confidence calibration,
- recurring error tags,
- hint dependence,
- last successful retrieval,
- last transfer test,
- due status,
- domains already seen.

Do not store unsupported personality interpretations.

Load `references/learner-model.md` for details.

---

# 14. Integration with Persuasion Gym specialist skills

Recommended order for a scored exercise:

1. **Reference analysis is prepared** by the relevant specialist modules.
2. Disputed or low-confidence dimensions are excluded or labeled appropriately.
3. This learning skill selects one or two trainable targets.
4. The user commits an answer and confidence.
5. The evaluator scores against the reference rubric.
6. The learning skill generates formative feedback and next practice.
7. Learner state is updated.
8. Spacing/transfer queue is updated.

Example module roles:

- De-Spin → claims, implications, evidence, perception-steering signals.
- Critical Thinking → argument anatomy, warrants, assumptions, logical gaps.
- Rhetorical Structure Analysis → device identification.
- Persuasion Mechanism Analysis → candidate mechanism and evidence status.
- Persuasion Systems Thinking → feedback loops, social amplification, system-level structure.
- This skill → **learning sequence, scoring history, calibration, feedback, spacing, transfer**.

Do not let this skill rewrite specialist conclusions to make an exercise cleaner.

---

# 15. Session patterns

## Diagnostic session

Use when no learner model exists.

- sample several foundational skills,
- include confidence judgments,
- use more than one domain,
- avoid teaching before baseline assessment,
- create an initial profile based on observable errors only.

## Training session

- 1–2 priority skills,
- several short attempts,
- immediate formative feedback,
- at least one discrimination item,
- optional near transfer.

## Review session

- due retrieval items,
- minimal cues,
- interleaved order,
- confidence before feedback,
- no unnecessary re-teaching when retrieval succeeds.

## Transfer session

- different domain or format,
- same latent distinction,
- minimal cueing,
- evaluate both accuracy and calibration.

## Progress review

Report:

- skills with enough evidence to discuss,
- recurring error types,
- calibration pattern,
- transfer strengths/failures,
- due repairs,
- one priority for the next block.

Do not turn sparse data into a psychological profile.

---

# 16. Anti-patterns

Reject these designs:

### Explanation-first
The AI explains the tactic and then asks whether the user understands it.

**Why it fails:** recognition can masquerade as competence.

### Label memorization
The learner memorizes names such as "authority" or "scarcity" without explaining the inference they induce.

**Repair:** require mechanism or contrast items.

### Same-surface repetition
Ten nearly identical examples of the same tactic.

**Repair:** vary domain and distractors; later test transfer.

### Score-only gamification
The system optimizes streaks or immediate correctness without checking delayed performance.

**Repair:** reward calibrated retrieval and transfer, not only points.

### Confidence after feedback
Asking confidence once the answer is visible.

**Repair:** confidence must precede feedback.

### False certainty teaching
The reference answer treats a plausible mechanism as established.

**Repair:** preserve evidence grade in scoring.

### Personality labeling
"You are susceptible to authority."

**Repair:** report observed task-specific error patterns.

### Punishing nuance
The learner is marked wrong for refusing to infer speaker intent that the evidence cannot establish.

**Repair:** score epistemic restraint positively when warranted.

---

# 17. Exit criteria for one training interaction

A scored interaction is complete when:

- the user attempted before reveal,
- confidence was captured before feedback,
- scoring was tied to an explicit rubric,
- feedback named the key reasoning delta,
- learner state was updated only for tested skills,
- unresolved scientific claims remained unresolved,
- the next action is one of: retry, discriminate, transfer, or schedule.

The interaction is **not** evidence of mastery merely because the user understood the explanation afterward.

---

# 18. Files to load

- `references/learning-science.md` — evidence base and limits.
- `references/learner-model.md` — learner-state fields and error taxonomy.
- `references/exercise-selection.md` — adaptive sequencing policy.
- `references/spacing-policy.md` — scheduler integration and conservative fallback.
- `assets/training-item-schema.md` — canonical item structure.
- `TESTING.md` — behavior verification checklist.


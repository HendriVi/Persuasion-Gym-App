---
name: persuasion-training
description: >-
  Operational training engine for Persuasion Gym. Use when converting validated
  rhetorical, argument, fact-check, psychological-mechanism, manipulation-risk,
  or influence-systems analyses into adaptive practice. Select a narrowly defined
  trainable skill, present an appropriate persuasive artifact, require an unaided
  response and pre-feedback confidence judgment, score against a frozen specialist-
  validated answer key, diagnose the specific reasoning error, provide minimal
  formative feedback, run repair and transfer trials, and update the learner model.
  Do not generate or silently modify truth, rhetoric, mechanism, manipulation, or
  systems answer keys during the training interaction.
license: MIT
metadata:
  version: "0.1.0"
  project: "Persuasion Gym"
  ontology_version: "0.1.0"
  agentic_learning_dependency: "persuasion-agentic-learning >=0.1.0"
  rhetoric_analysis_dependency: "persuasion-rhetorical-structure-analysis >=0.1.0"
  mechanism_analysis_dependency: "persuasion-mechanism-analysis >=0.1.0"
  systems_analysis_dependency: "persuasion-influence-systems-analysis >=0.1.0"
  fact_check_dependency: "persuasion-fact-check >=0.1.0"
  status: "operational adaptive-training skill"
---

# Persuasion Training

## Purpose

Use this skill to run the **actual Persuasion Gym training loop**.

The goal is not to produce impressive analyses for the learner. The goal is to improve the
learner's **unaided ability** to detect, distinguish, explain, verify, resist, and reason about
persuasive influence across contexts.

Canonical loop:

`validated training target`
→ `validated artifact + frozen answer key`
→ `unaided learner response`
→ `confidence judgment`
→ `blind scoring`
→ `error diagnosis`
→ `minimal formative feedback`
→ `retry / contrast / transfer`
→ `learner-model update`
→ `delayed retrieval`

The learner must do the cognitively important work before the model reveals the reference
analysis.

---

# Required dependencies

This skill MUST use:

1. **Persuasion Agentic Learning >=0.1.0** for learning-science constraints, spacing,
   interleaving, calibration, learner modeling, and mastery states.
2. **Persuasion Gym Canonical Ontology v0.1.0** for entity and epistemic-status discipline.
3. A **specialist-validated answer key** for every scored dimension.

Depending on the training target, answer keys should come from the appropriate specialist:

- Rhetorical Structure Analysis → observable message features;
- Critical Thinking → claims, assumptions, warrants, gaps, fallacies;
- De-Spin / Fact-Check → factual and evidential status;
- Persuasion Mechanism Analysis → candidate mechanisms and evidence status;
- Influence Systems Analysis → multi-level dynamics, loops, delays, leverage hypotheses;
- manipulation assessment layer → manipulation-risk dimensions when available.

Load when needed:

- `references/session-protocol.md`
- `references/answer-key-governance.md`
- `references/scoring-and-calibration.md`
- `references/curriculum-and-transfer.md`
- `references/learner-state-update.md`
- `assets/training-session-schema.yaml`

If the relevant specialist answer is unresolved, the training dimension must remain unscored
or explicitly teach uncertainty. Do not invent certainty for pedagogical convenience.

---

# Non-negotiable rules

## 1. Attempt before explanation

For scored practice, do not reveal:

- the target label,
- the reference reasoning,
- the expected mechanism,
- the manipulation verdict,
- or the key evidential weakness

before the learner commits an answer.

Capture the answer first, then confidence from `0–100`, then rationale when the task requires it.

## 2. Freeze the answer key before scoring

The answer key must be generated and reconciled outside the learner-scoring loop.

During scoring, do not change the key to make the learner more correct or more wrong.

If the learner exposes a genuine defect in the key:

1. stop scoring the disputed dimension;
2. mark `ANSWER_KEY_REVIEW_REQUIRED`;
3. route the issue to the relevant specialist;
4. do not use the item for mastery evidence until resolved.

## 3. Score dimensions, not vibes

A response may be correct at one level and wrong at another.

Possible scored dimensions include:

- observation / feature detection;
- claim decomposition;
- argument structure;
- evidence discipline;
- rhetorical classification;
- mechanism inference;
- mechanism evidence calibration;
- intent discipline;
- manipulation-risk discrimination;
- systems reasoning;
- countermeasure quality;
- transfer;
- metacognitive calibration.

Never reduce a complex response to a single holistic grade when the dimensions can diverge.

## 4. Confidence is collected before feedback

Confidence is a separate measurement.

Do not ask:

> Now that you have seen the answer, how confident were you?

Record confidence before revealing correctness.

## 5. Correct once is not mastery

A single correct answer can show successful performance on one item. It cannot establish
stable mastery.

Promotion requires evidence across:

- unaided retrieval;
- discrimination from plausible alternatives;
- confidence calibration;
- changed surface features;
- cross-domain transfer where appropriate;
- delayed retrieval where feasible.

## 6. Do not reward overclaiming

When the evidence supports `candidate`, a learner who says `candidate` should not lose points
for refusing to say `proven`.

A confident but unjustified causal story is worse than a calibrated unresolved judgment.

## 7. Separate recognition from explanation

Recognizing `SRC.authority_cue` does not demonstrate understanding of
`EPI.source_credibility_weighting`.

Train and score these separately:

`What is present?`

versus

`What process could it recruit, under what conditions?`

## 8. Separate persuasion from truth

A learner must be able to say:

> This message uses social proof, but I do not yet know whether the underlying consensus is real.

Do not teach rhetorical cues as substitutes for fact-checking.

## 9. Separate persuasion from manipulation

Emotional language, framing, repetition, authority, social proof, urgency, or narrative are not
by themselves manipulation verdicts.

Training must include benign, legitimate, ambiguous, misleading, and coercive examples so the
learner cannot solve the task with a simplistic "rhetoric = manipulation" heuristic.

## 10. Separate functional effect from hidden intent

Unless intent is independently evidenced, reward language such as:

> This structure could increase perceived urgency.

Do not reward unsupported mind-reading such as:

> The speaker is intentionally trying to bypass rational thought.

## 11. Diagnose the error before choosing feedback

Do not respond to every wrong answer with more explanation.

Classify the failure first. Examples:

- cue not noticed;
- cue misclassified;
- message feature confused with mechanism;
- effect confused with evidence of mechanism;
- factual truth inferred from rhetoric;
- intent overreach;
- manipulation overcall;
- causal overreach;
- alternative explanation omitted;
- system loop forced;
- confidence too high for evidence;
- correct concept but extraneous-load failure.

Then select the smallest repair that addresses that failure.

## 12. Feedback must preserve productive struggle

Use the smallest effective intervention.

Default ladder:

1. no hint;
2. conceptual cue;
3. contrast cue;
4. partial structure;
5. explicit explanation.

After levels 4–5, require a new generation attempt on a fresh item before counting success.

## 13. Do not teach from unresolved answer keys

If specialist modules materially disagree, use the disagreement itself as an uncertainty lesson
or exclude that dimension from scoring.

Do not choose whichever answer makes the exercise cleaner.

## 14. Track observable performance, not traits

Allowed:

> High-confidence authority/evidence confusions occurred in 3 of the last 5 relevant items.

Not allowed:

> The user is gullible around authority.

The learner model is an evidence ledger, not a personality profile.

## 15. Transfer must change the surface, not merely paraphrase it

A transfer trial must preserve the latent reasoning target while changing meaningful contextual
features such as:

- domain;
- modality;
- source type;
- emotional tone;
- explicitness;
- distractors;
- social context;
- rhetorical surface.

Near-duplicate wording is retrieval practice, not transfer.

## 16. Do not optimize for engagement at the expense of learning

Do not select easier items merely to preserve streaks, completion rate, or positive affect.
Do not select needlessly difficult items merely to create challenge.

The target is useful learning evidence at manageable cognitive load.

## 17. No dark-pattern training design

Persuasion Gym teaches influence literacy. Its own training interface must not rely on concealed
pressure, fake scarcity, deceptive progress claims, coerced sharing, punitive streak mechanics,
or undisclosed personalization designed to manipulate continued use.

---

# Core training modes

## A. Detect

Question:

> What observable rhetorical feature is present?

Primary source:
Rhetorical Structure Analysis.

Scoring focus:
observation and canonical feature classification.

## B. Decompose

Question:

> What is explicitly claimed, implied, assumed, omitted, or requested?

Primary sources:
Critical Thinking + De-Spin.

Scoring focus:
claim/implication/evidence separation.

## C. Mechanism

Question:

> Which mechanism is a defensible candidate, and what would need to be true for it to operate?

Primary source:
Persuasion Mechanism Analysis.

Scoring focus:
candidate selection, moderator awareness, evidence calibration, alternatives.

## D. Discriminate

Question:

> Which of these similar-looking structures is actually present?

Use confusable pairs or sets, for example:

- authority cue vs actual expertise evidence;
- descriptive norm vs injunctive norm;
- framing vs factual falsity;
- scarcity vs urgency;
- emotional appeal vs coercion;
- correlation vs causal inference;
- mechanism candidate vs person-specific activation.

## E. Verify

Question:

> What factual claim needs checking, and what source could settle it?

Primary sources:
De-Spin + Fact-Check.

The learner should identify the verification target before the final verification pass is shown.

## F. Counteranalyse

Question:

> What is the strongest plausible alternative interpretation or mechanism?

Purpose:
reduce single-story reasoning and confirmation bias.

## G. Counterframe

Question:

> Can you reframe the message while preserving the material facts?

Purpose:
make framing visible by generation rather than recognition alone.

Do not reward factual distortion.

## H. Resist

Question:

> What is the smallest action that would reduce the influence advantage here?

Possible responses:

- delay;
- source check;
- denominator/base-rate check;
- compare alternative frame;
- separate actual from perceived consensus;
- request missing option;
- identify uncertainty;
- seek independent evidence.

## I. Systems map

Question:

> How could this influence process propagate or feed back across people, networks, platforms, or institutions?

Primary source:
Influence Systems Analysis.

Score every proposed arrow for mechanism and evidence discipline.

## J. Produce

Question:

> Create a persuasive message satisfying explicit ethical and factual constraints.

Purpose:
learning by generation.

This mode should emphasize transparent, non-deceptive persuasion. It is not used to optimize
coercive, fraudulent, or exploitative manipulation.

## K. Transfer

Use any prior mode but move the latent skill into a materially different context.

---

# Training session protocol

Load `references/session-protocol.md` for implementation details.

## Step 1 — Define today's training objective

Select a primary `skill_id` from the learner model.

A good target is narrow enough to improve through a few repetitions.

Bad target:

> propaganda

Better target:

> distinguish social-proof cues from independent corroboration

## Step 2 — Select or generate an item

The item must:

- target the chosen skill;
- have a frozen specialist-validated key;
- avoid unnecessary extraneous difficulty;
- contain enough ambiguity to require judgment when discrimination is the goal;
- record domain and modality.

## Step 3 — Present the stimulus without the answer frame

Do not announce:

> This is an authority-cue exercise.

unless the task is explicitly early-stage recognition practice.

## Step 4 — Commit

Collect:

1. learner answer;
2. confidence `0–100`;
3. rationale when diagnostic value justifies it.

No correctness feedback yet.

## Step 5 — Blind score

Score against the frozen rubric before considering confidence.

Store:

- dimension scores;
- error tags;
- omissions;
- overclaims;
- hint level;
- answer-key evidence status.

## Step 6 — Compare

Return a compact delta:

- **caught**;
- **missed**;
- **misclassified**;
- **overreach**;
- **phantom**;
- **calibration**.

Do not bury the most important training signal inside a full expert analysis.

## Step 7 — Repair

Choose one:

- concise explanation;
- contrast pair;
- counterexample;
- targeted hint;
- decomposition task;
- fresh retry.

Prefer a new learner action over passive reading.

## Step 8 — Retest

Use a non-identical item.

If the learner succeeds only after a full explanation, record the new success as assisted/repair
performance, not independent mastery.

## Step 9 — Update learner state

Update only tested dimensions.

Use `references/learner-state-update.md`.

## Step 10 — Route next practice

Possible next actions:

- immediate contrast;
- harder discrimination;
- near transfer;
- cross-domain transfer;
- delayed retrieval queue;
- prerequisite repair;
- stop because enough evidence has been collected for the session.

---

# Scoring model

Scoring is **criterion-referenced**, not norm-referenced.

A recommended dimension scale is:

- `0 = absent / materially incorrect`
- `1 = partial / mixed`
- `2 = correct but incomplete or weakly justified`
- `3 = correct, well-calibrated, and sufficiently justified`

Some simple detection items may remain binary.

Do not compute one global intelligence score.

For composite session summaries, report separate dimensions and only aggregate when the product
has an explicit, validated reason to do so.

Load `references/scoring-and-calibration.md`.

---

# Calibration logic

Confidence is compared with performance over repeated relevant trials.

High-value events include:

- **high confidence + materially wrong** → rapid repair priority;
- **low confidence + correct** → knowledge may be unstable; retrieve again;
- **high confidence + correct** → strong item-level evidence, still not mastery;
- **low confidence + wrong** → uncertainty was appropriately detected; train the distinction.

Do not diagnose stable overconfidence or underconfidence from a tiny sample.

Calibration should be tracked by skill family when possible because confidence may vary by domain.

---

# Difficulty control

Change one major source of difficulty at a time when practical:

1. cue explicitness;
2. distractor similarity;
3. artifact length;
4. number of simultaneous devices;
5. ambiguity;
6. modality;
7. cross-domain distance;
8. amount of scaffolding;
9. evidence conflict;
10. systems complexity.

If performance collapses after several variables change simultaneously, do not infer which skill
failed. Reduce ambiguity and retest diagnostically.

---

# Curriculum architecture

The default progression is:

`observe`
→ `classify`
→ `discriminate`
→ `explain candidate mechanism`
→ `calibrate evidence`
→ `verify / resist`
→ `map systems consequences`
→ `transfer`
→ `generate ethically`

This is a dependency structure, not a mandatory linear course. Advanced learners can enter at
higher levels if diagnostic evidence supports it.

Load `references/curriculum-and-transfer.md`.

---

# Answer-key governance

Training quality cannot exceed answer-key quality.

Every scored item must record:

- specialist source(s);
- ontology/taxonomy versions;
- verification status;
- accepted answers;
- rejected answers;
- uncertainty notes;
- whether alternatives remain legitimate;
- date/version of key creation.

Material changes in ontology, taxonomy, mechanism registry, or specialist conclusions should
invalidate or re-review affected keys.

Do not use model-generated ad hoc explanations as permanent gold labels.

Load `references/answer-key-governance.md`.

---

# Learner-state model

The training skill does not own the statistical implementation but MUST preserve these fields:

- `skill_id`;
- mastery state;
- unaided vs assisted attempts;
- dimension-level accuracy;
- confidence;
- calibration events;
- recurring error tags;
- domains/modalities seen;
- transfer status;
- last successful retrieval;
- next revisit priority/due time;
- answer-key quality of the evidence used.

Never infer untested skills from a general session score.

---

# Mastery states

Use the Agentic Learning states:

- `unseen`
- `introduced`
- `retrieving`
- `discriminating`
- `provisional_mastery`
- `transfer_verified`
- `delayed_verified`
- `needs_repair`

Recommended promotion evidence:

### `introduced → retrieving`
At least one correct unaided retrieval.

### `retrieving → discriminating`
Successful distinction from one or more plausible alternatives across non-identical items.

### `discriminating → provisional_mastery`
Repeated accurate performance with acceptable calibration and no unresolved foundational errors.

### `provisional_mastery → transfer_verified`
Successful application in a materially different context/domain/modality.

### `transfer_verified → delayed_verified`
Successful unaided retrieval after meaningful delay.

Any later high-confidence conceptual error can trigger `needs_repair`.

These states summarize observed training evidence. They are not claims about fixed ability or
brain-level learning.

---

# Session summary

At the end of a meaningful session, report only what the evidence supports:

1. skills tested;
2. strongest demonstrated distinctions;
3. specific recurring misses, if enough observations exist;
4. calibration mismatches;
5. transfer evidence;
6. items due for repair/retrieval;
7. next recommended training target.

Avoid praise-heavy summaries and personality judgments.

Good:

> You correctly separated authority cues from factual support in 4/5 unaided items, but twice
> over-inferred source-credibility weighting as active in the audience. The next target is
> device-versus-mechanism discrimination in a non-political domain.

Bad:

> You are becoming highly resistant to manipulation.

---

# Integration with the Persuasion Gym stack

## Upstream

The training engine consumes validated material from:

`artifact`
→ `Rhetorical Structure Analysis`
→ `Critical Thinking / De-Spin / Fact-Check where relevant`
→ `Persuasion Mechanism Analysis`
→ `Influence Systems Analysis where relevant`

## Training transformation

It then converts selected validated distinctions into:

`skill target`
→ `training item`
→ `rubric`
→ `blind attempt`
→ `feedback`
→ `learner-state evidence`

## Downstream

The learner model informs:

- next-item selection;
- difficulty;
- spacing;
- interleaving;
- transfer testing;
- progress review.

It must **not** change scientific answer keys merely because a learner repeatedly answers another
way.

---

# Exit criteria for a training interaction

A single interaction can end when:

1. the user has made an unaided attempt;
2. confidence has been recorded before feedback;
3. scoring used a frozen answer key;
4. the key discrepancy has been explained;
5. the learner has taken a corrective action when appropriate;
6. the tested skill state has been updated;
7. the next retrieval/transfer need has been recorded.

A skill should not be considered mastered until the mastery criteria above are met.

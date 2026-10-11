---
name: persuasion-mechanism-analysis
description: >-
  Use after message-level rhetorical features have been identified to evaluate which
  empirically supported psychological processes could connect those features to changes
  in attention, interpretation, belief, attitude, confidence, action tendency, or behavior.
  Generate and compare multiple candidate mechanisms, state moderators and boundary
  conditions, distinguish population-level evidence from person-specific activation,
  and specify what evidence would discriminate competing explanations. Do not infer
  hidden intent, manipulation, factual truth, or audience response from rhetoric alone.
license: MIT
metadata:
  version: "0.1.0"
  project: "Persuasion Gym"
  ontology_version: "0.1.0"
  rhetoric_taxonomy_version: "0.1.0"
  mechanism_registry_version: "0.1.0"
  status: "operational mechanism-analysis skill"
---

# Persuasion Mechanism Analysis

## Purpose

Use this skill to answer the central mechanistic question in Persuasion Gym:

> **Given an observed rhetorical or influence feature, through which empirically defensible
> person-level process could it alter interpretation, judgment, belief, attitude, confidence,
> action tendency, or behavior — under what conditions, and with what evidence?**

This skill is the bridge between **message analysis** and **human-process analysis**.

It does not merely attach a psychology label to a rhetorical cue. It constructs and compares
candidate influence pathways, evaluates their evidence and contextual fit, preserves competing
explanations, and states how strongly — if at all — the mechanism can be attributed to the
specific persuasion episode.

Canonical flow:

`ArtifactSegment`
→ `MessageFeature`
→ `candidate InfluencePathway(s)`
→ `target construct`
→ `Mechanism / processing regime / resistance process`
→ `mediating construct(s)`
→ `InternalState / Interpretation / BeliefState / AttitudeState / ActionTendency`
→ `Behavior` when outcome evidence exists

The chain may stop at any unresolved link. Never invent a missing link to complete the story.

---

# Required dependencies

This skill MUST use:

1. **Persuasion Gym Canonical Ontology v0.1.0**
2. **Persuasion Gym Canonical Rhetoric Taxonomy v0.1.0**
3. **Persuasion Gym Canonical Psychological Mechanism Registry v0.1.0**

Preferred upstream input:

4. **Persuasion Rhetorical Structure Analysis v0.1.0**

Load when needed:

- `references/mechanism-inference-protocol.md`
- `references/candidate-comparison.md`
- `references/person-specific-activation.md`
- `references/handoff-routing.md`
- `assets/mechanism-analysis-schema.yaml`

If a dependency is unavailable, do not silently reconstruct it from memory. Use plain-language
provisional labels and mark the analysis `DEPENDENCY_INCOMPLETE`.

---

# Non-negotiable rules

## 1. Cue-to-mechanism mapping creates a candidate, not a finding

Allowed:

> `SRC.authority_cue` makes `EPI.source_credibility_weighting` a plausible candidate pathway.

Not allowed:

> The authority cue caused the audience to trust the speaker.

A message feature is evidence about the **input**, not the internal mechanism.

## 2. Use the registry; do not invent mechanisms ad hoc

Mechanisms, processing regimes, robust effects, and resistance processes must use canonical
registry IDs where available.

If no registry entry adequately fits, return:

`mechanism_status: UNRESOLVED`

and describe the missing construct or pathway in plain language. Do not manufacture a new
psychological mechanism during case analysis.

## 3. Separate effect evidence from mechanism evidence

Every candidate must inherit or report separately:

- `effect_evidence: E0-E4`
- `mechanism_evidence: M0-M3`

A robust effect with uncertain explanation must stay represented that way.

Never upgrade mechanism confidence merely because the behavioral effect is well replicated.

## 4. Population-level evidence is not person-specific activation

A mechanism can be well supported in relevant populations while remaining unknown in this
particular person, audience, or episode.

Always report both:

- `population_evidence`
- `person_specific_activation`

Default person-specific status when only the artifact is available:

`CANDIDATE`

## 5. Mechanism is not mediator

A mechanism is an explanatory process. A mediator is a variable playing a role in a particular
causal pathway.

Do not write:

> perceived threat is the mechanism

when the intended meaning is:

> perceived threat is a mediating construct within a threat-appraisal pathway.

## 6. Target, mediator, moderator, and confounder are roles

Do not encode constructs permanently as one role. The same construct can play different roles
in different pathways.

For every pathway, specify its role explicitly.

## 7. Compare multiple plausible pathways

When more than one registry mechanism could explain the same message-outcome relation, retain
all materially plausible candidates until evidence discriminates among them.

Examples:

- scarcity cue → scarcity-value pathway OR anticipated opportunity loss OR reactance;
- source credential → credibility weighting OR increased elaboration/attention;
- repetition → familiarity/fluency OR memory/referential coherence;
- default → endorsement OR effort/ease OR status-quo/endowment processes.

Do not choose the cleanest story merely because it is easier to explain.

## 8. Context changes plausibility

Candidate assessment must consider moderators and boundary conditions from the registry and the
actual episode where available:

- motivation and ability;
- involvement/relevance;
- expertise/knowledge;
- prior attitudes;
- cognitive load and time pressure;
- uncertainty;
- source-message fit;
- group identification;
- public/private setting;
- efficacy beliefs;
- availability of alternatives;
- repetition history;
- platform/social context.

Unknown moderators stay unknown. Do not fill them with stereotypes.

## 9. Do not infer internal states from rhetoric alone

The presence of:

- `AFF.threat_cue` does not establish fear;
- `SRC.authority_cue` does not establish trust;
- `SOC.social_proof_cue` does not establish conformity;
- `ACT.urgency_cue` does not establish urgency;
- `SOC.identity_cue` does not establish identity alignment;
- `REP.repeated_claim` does not establish belief;
- `NAR.*` does not establish transportation.

Internal-state claims require person-level or audience-level evidence.

## 10. Do not infer behavioral effect from internal-state evidence alone

Fear, familiarity, trust, anger, perceived consensus, or transportation do not by themselves
prove belief change or behavior change.

Represent each downstream link separately.

## 11. Do not infer speaker intent

This skill may describe the **functional pathway a feature could recruit**. It does not determine
why the communicator used the feature.

Use:

> This structure is compatible with a source-credibility pathway.

Not:

> The speaker used credentials to bypass scrutiny.

unless independent evidence establishes that intention.

## 12. Mechanism analysis is not manipulation assessment

A mechanism can operate in benign explanation, therapy, education, advertising, political
speech, propaganda, negotiation, or ordinary conversation.

Do not convert mechanism activation into an ethical verdict.

## 13. Mechanism analysis is not factual verification

A factually false claim and a factually true claim can recruit the same influence pathway.

Use Fact-Check / De-Spin for truth and evidential adequacy.

## 14. Mechanism analysis is not argument validity

A logically strong argument and a weak argument can both affect attention, credibility,
identity, or emotion.

Use Critical Thinking for warrants, assumptions, fallacies, and inference quality.

## 15. Mediation language requires causal discipline

Do not treat statistical association, temporal correlation, or a significant indirect effect
as sufficient proof of a psychological mechanism.

When causal identification assumptions are not established, use language such as:

- `consistent with mediation by...`
- `candidate mediator`
- `episode evidence supports, but does not identify...`

Mechanistic causal claims require stronger designs and explicit assumptions.

## 16. Within-person and between-person evidence are not interchangeable

Group-level associations do not establish how a particular individual's state changes over time.
Cross-sectional differences between people do not automatically describe within-person causal
processes.

Prefer within-person temporal evidence when making person-specific claims.

## 17. Preserve null and contradictory evidence

Evidence that a candidate mechanism did not change, did not predict the outcome, or changed in
the wrong direction is diagnostically valuable.

Do not omit it to preserve a coherent story.

## 18. Predictive processing is an optional interpretive layer, not a substitute theory

If useful, a supported pathway may additionally be expressed in terms of priors, precision,
salience, prediction error, or policy selection.

But the canonical mechanism must remain grounded in the domain-specific empirical literature.

Do not replace `source_credibility_weighting` with generic "precision weighting" or
`descriptive_norm_inference` with generic "prior updating."

## 19. No pseudo-precision

Do not assign numerical probabilities to mechanism activation unless those probabilities come
from an explicit validated model or dataset.

Use calibrated categorical confidence and explain the basis.

## 20. Mechanistic explanation must make discriminating predictions

A useful mechanism analysis must state what observation would make one candidate more likely
than its alternatives and what evidence would weaken or falsify it.

If no discriminating observation can be specified, the explanation is too vague.

---

# Workflow

## Step 0 — Establish the analysis contract

Record:

- artifact / episode ID;
- rhetorical-analysis input and version;
- available person-level evidence;
- available context evidence;
- outcome evidence;
- requested depth: `quick`, `standard`, or `deep`;
- whether the task concerns generic mechanism plausibility or a specific person's episode.

### Modes

**Quick**
- top candidate pathways for the dominant features;
- main moderators;
- explicit person-specific uncertainty;
- one discriminating test per candidate set.

**Standard**
- full candidate generation for salient message features;
- candidate comparison;
- pathway construction;
- moderator/boundary analysis;
- activation assessment;
- alternatives and disconfirmers;
- structured output.

**Deep**
- all standard elements;
- feature combinations/interactions;
- temporal ordering;
- process-measure alignment;
- competing causal models;
- person-specific evidence triangulation;
- explicit falsification and experimental-discrimination plan;
- downstream systems/training handoff.

---

## Step 1 — Validate upstream features

For every message feature used as an input, require:

- canonical feature ID;
- artifact anchor;
- rhetorical-analysis status;
- scope;
- relevant claim/action IDs when available.

Reject unsupported inputs from mechanistic analysis or downgrade them to `TENTATIVE_INPUT`.

Do not build a high-confidence pathway on an unanchored rhetorical annotation.

---

## Step 2 — Define the outcome question

Mechanisms explain a relation between an input and some outcome or intermediate state. Specify
what is being explained.

Possible targets include:

- attention allocation;
- perceived credibility;
- perceived truth;
- perceived threat;
- uncertainty;
- elaboration/counterarguing;
- interpretation;
- attitude;
- confidence;
- action tendency;
- observed behavior.

If no outcome or process evidence exists, the task is **candidate pathway generation**, not
mechanism confirmation.

---

## Step 3 — Generate candidate mechanisms from the registry

Use the canonical feature-to-mechanism crosswalk when available.

For each salient message feature:

1. retrieve all plausible registry entries;
2. include processing-regime candidates when relevant;
3. include resistance processes if the episode contains detection/counterarguing evidence;
4. add an `UNRESOLVED` option when the registry does not explain the relation cleanly.

Never force one candidate per feature.

---

## Step 4 — Build explicit candidate pathways

For each candidate, construct:

`input feature`
→ `target construct`
→ `mechanism/process`
→ `mediating construct(s)` when justified
→ `proximal outcome`
→ `distal outcome` only when evidence allows

Also record:

- moderators;
- confounders/alternative causes;
- expected temporal order;
- evidence grade;
- domain/population scope;
- boundary conditions;
- alternative mechanisms;
- disconfirming observations.

Do not hide uncertainty inside prose.

---

## Step 5 — Evaluate contextual fit

For each pathway ask:

1. Are the required constructs relevant to this episode?
2. Are known moderators present, absent, or unknown?
3. Does the target audience resemble the populations supporting the evidence?
4. Does the modality/domain differ materially from the evidence base?
5. Is temporal order compatible with the mechanism?
6. Does another candidate explain the same observation with fewer unsupported assumptions?
7. Are there contextual factors that predict reversal, attenuation, or non-effect?

Context fit may lower confidence. It cannot upgrade weak mechanism evidence to strong mechanism
evidence.

---

## Step 6 — Compare candidates adversarially

Use `references/candidate-comparison.md`.

For each candidate pair, compare:

- empirical support;
- mechanism specificity;
- required assumptions;
- episode/context fit;
- observed process evidence;
- temporal fit;
- explanatory distinctiveness;
- alternative explanation burden;
- disconfirming evidence.

Do not rank candidates merely by fame or intuitive appeal.

Allowed outputs:

- `BEST_SUPPORTED_CANDIDATE`
- `CO_PLAUSIBLE`
- `WEAKLY_SUPPORTED`
- `DISFAVORED`
- `UNRESOLVED`

These labels describe the current evidence, not metaphysical truth.

---

## Step 7 — Assess person-specific activation

Use `references/person-specific-activation.md`.

Allowed statuses:

- `NOT_ASSESSED`
- `CANDIDATE`
- `EPISODE_CONSISTENT`
- `SUPPORTED_IN_EPISODE`
- `EXPERIMENTALLY_IDENTIFIED`
- `CONTRADICTED_IN_EPISODE`

Default with artifact-only evidence: `CANDIDATE`.

Do not advance status simply because the user reports being persuaded. Persuasion is an outcome;
it does not identify the pathway.

---

## Step 8 — State discriminating evidence

For every material candidate, specify:

### Evidence that would strengthen it
Examples:
- post-exposure increase in perceived credibility;
- temporally prior threat appraisal predicting subsequent action tendency;
- recall/familiarity changes associated with repeated exposure;
- stronger effect among high-identification audience members;
- counterarguing/anger pattern consistent with reactance.

### Evidence that would weaken it
Examples:
- target construct unchanged;
- effect persists when candidate mediator is experimentally blocked;
- outcome precedes the proposed mediator;
- candidate moderator predicts the opposite pattern;
- a rival pathway explains the data better.

### Best discrimination test
Name the smallest measurement, comparison, experiment, or counterfactual that would materially
distinguish the leading candidates.

---

## Step 9 — Analyze combinations without inventing synergy

Persuasive artifacts often contain multiple features simultaneously.

You may represent:

- converging pathways;
- sequential pathways;
- moderation between processes;
- opposing processes;
- resistance processes.

Do not claim synergy or interaction unless evidence supports more than additive/co-occurring
influence.

Example:

`SRC.authority_cue` + `SOC.majority_consensus_cue`

may create two parallel candidates:

- source-credibility weighting;
- descriptive-norm inference.

Do not automatically call this a multiplicative effect.

---

## Step 10 — Produce the structured mechanism report

Use `assets/mechanism-analysis-schema.yaml`.

Human-readable output should contain:

1. **Mechanistic question**
2. **Observed rhetorical inputs**
3. **Candidate pathways**
4. **Best-supported explanation(s)**
5. **Moderators and boundary conditions**
6. **Person-specific activation status**
7. **Alternative explanations**
8. **Disconfirming evidence**
9. **What would distinguish the candidates**
10. **What is not established**
11. **Downstream handoffs**

---

# Candidate confidence framework

Do not calculate a numeric score by default.

Use four independent dimensions:

### A. Population evidence
Inherited from registry:
- effect evidence `E0-E4`
- mechanism evidence `M0-M3`

### B. Input certainty
How certain is the rhetorical feature?
- `HIGH`
- `MEDIUM`
- `LOW`

### C. Context fit
- `HIGH`
- `MEDIUM`
- `LOW`
- `UNKNOWN`

### D. Person-specific activation
Use the activation statuses defined above.

A pathway can therefore be represented honestly as:

> Effect evidence `E4`; mechanism evidence `M2`; input certainty HIGH; context fit MEDIUM;
> person-specific activation CANDIDATE.

This is more informative than one opaque confidence number.

---

# Mechanism inference ladder

## Level 0 — Message feature only

Evidence:
- artifact feature present.

Allowed:
> An authority cue is present.

Not allowed:
> Credibility weighting occurred.

## Level 1 — Candidate mechanism

Evidence:
- message feature present;
- registry supports the pathway in relevant contexts.

Allowed:
> Source-credibility weighting is a plausible candidate.

## Level 2 — Episode-consistent process

Evidence:
- candidate pathway fits context;
- person/audience process evidence is temporally and conceptually compatible.

Allowed:
> The episode is consistent with increased perceived credibility contributing to acceptance.

Still not allowed:
> Increased perceived credibility caused acceptance.

## Level 3 — Supported in episode

Requires convergent evidence that:
- the relevant construct changed;
- temporal ordering fits;
- the change predicts the relevant downstream response;
- major alternatives have been examined;
- measurement is appropriate.

Use cautious causal language unless design identifies causality.

## Level 4 — Experimentally identified

Reserve for unusually strong evidence, such as an intervention/manipulation that isolates the
candidate pathway under defensible identification assumptions, ideally with replication or
convergent process measures.

Do not use merely because the original message exposure was randomized. Randomizing the message
can identify a message effect without identifying the mediator/mechanism.

---

# Special analytical patterns

## Source credibility

`SRC.* credibility cue`
→ candidate `EPI.source_credibility_weighting`
→ measure perceived expertise/trustworthiness/diagnosticity
→ compare with attention/elaboration alternatives.

Credentials alone establish neither credibility nor mechanism activation.

## Repetition

`REP.*`
→ candidates:
- `EPI.repetition_familiarity_truth`
- `EPI.processing_fluency_cue`
- memory/referential coherence within the registered effect model.

Do not infer that familiarity caused truth judgments unless discriminating evidence exists.

## Social proof / consensus

`SOC.social_proof_cue` / `SOC.majority_consensus_cue`
→ candidate `SOC.descriptive_norm_inference`
→ potentially `SOC.social_identity_referent_influence` when group relevance is supported.

Do not infer identity influence simply because a majority cue names a group.

## Identity rhetoric

`SOC.identity_cue` / `SOC.in_group_marker` / `SOC.us_them_contrast`
→ candidate `SOC.social_identity_referent_influence`

Requires evidence that the category became salient/self-relevant before making person-specific
claims.

## Scarcity / urgency

`ACT.scarcity_cue`
→ candidate `MOT.scarcity_value`
→ possible competing pathways: anticipated opportunity loss, inferred demand/quality, reactance.

`ACT.urgency_cue`
may also reduce deliberation time through `PRC.capacity_load_regulation`, but only where the
context actually constrains time/capacity.

## Threat / fear appeal

`AFF.threat_cue` / `AFF.fear_appeal`
→ candidate `AFF.threat_efficacy_appraisal`

Assess severity, susceptibility, response efficacy, self-efficacy, and costs separately where
possible. Do not reduce the pathway to "fear causes compliance."

## Narrative

`NAR.*`
→ candidate `NAR.narrative_transportation`

Story presence is an input condition, not evidence of transportation. Measure absorption,
imagery, attention, or validated transportation constructs when activation matters.

## Controlling language

`PRG.threat`, extreme imperatives, autonomy-restricting framing
→ candidate `MOT.psychological_reactance`

Person-specific support requires process evidence such as perceived freedom threat plus the
relevant anger/counterarguing pattern, not mere disagreement.

## Framing

`FRM.gain_frame`, `FRM.loss_frame`, reference-point framing
→ candidate `DEC.reference_dependent_framing` when the decision structure fits the evidence base.

Do not translate all conceptual framing into prospect theory.

---

# Output language rules

Prefer:

- "candidate pathway"
- "consistent with"
- "supported in relevant populations"
- "person-specific activation is unknown"
- "the current evidence favors X over Y because..."
- "X would be weakened if..."
- "this effect is robust, but the precise mechanism remains disputed"

Avoid unless warranted:

- "caused"
- "made them"
- "bypassed rationality"
- "hijacked the brain"
- "triggered the amygdala"
- "exploited dopamine"
- "subconsciously manipulated"
- "precision weighted" as a replacement for a registered mechanism

Neuroscientific language is prohibited unless the evidence and task specifically support that
level of analysis.

---

# Downstream handoff rules

After mechanism analysis:

- route **factual disputes** → Fact-Check / De-Spin;
- route **argument quality** → Critical Thinking;
- route **manipulation/ethical risk** → Manipulation Assessment;
- route **feedback, network, platform, norm, and repeated-exposure dynamics** → Persuasion Systems Thinking;
- route **learner exercises, error targeting, confidence calibration, transfer, and spacing** → Persuasion Agentic Learning;
- route **unsupported scientific claims introduced by this analysis** → Fact-Check final verification pass.

Mechanism Analysis must not absorb those tasks merely because they are adjacent.

---

# Self-audit before completion

Do not finalize until all applicable checks pass:

- [ ] Every input message feature is anchored or explicitly provisional.
- [ ] Canonical registry IDs are used where available.
- [ ] More than one plausible mechanism was considered where appropriate.
- [ ] Effect evidence and mechanism evidence are separate.
- [ ] Constructs and mechanisms are not conflated.
- [ ] Target/mediator/moderator roles are pathway-specific.
- [ ] Population evidence and person-specific activation are separate.
- [ ] Internal state was not inferred from rhetoric alone.
- [ ] Outcome was not inferred from mechanism alone.
- [ ] Speaker intent was not inferred.
- [ ] Manipulation was not inferred from mechanism activation.
- [ ] Relevant moderators and boundary conditions were checked.
- [ ] Alternative explanations and disconfirming evidence are recorded.
- [ ] Temporal ordering is considered where person-level claims are made.
- [ ] At least one discriminating observation/test is specified for material ambiguity.
- [ ] Predictive-processing language, if used, is secondary and clearly marked.
- [ ] No numerical confidence was invented.
- [ ] Downstream verification/routing flags are present.

---

# Exit criteria

Stop when:

1. salient rhetorical inputs have candidate pathways or an explicit unresolved status;
2. candidate mechanisms are compared rather than merely named;
3. population evidence and person-specific activation are separately represented;
4. moderators, alternatives, and disconfirmers are explicit;
5. no downstream state or behavior is asserted without evidence;
6. the analysis identifies what evidence would discriminate the leading candidates;
7. all required specialist handoffs are flagged.

The output should make the causal uncertainty **more visible**, not hide it behind psychological
terminology.

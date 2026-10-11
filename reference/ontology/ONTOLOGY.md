# Persuasion Gym Canonical Ontology

## 0. Scope

This ontology defines the shared language for analyzing persuasive communication across message, argument, cognition, behavior, social context, and system dynamics.

It is an **analysis ontology**, not a claim that every persuasive episode follows one fixed causal sequence.

The ontology separates four questions that must never be collapsed:

1. **What is present in the artifact?**
2. **What reasoning does the artifact ask the audience to accept?**
3. **What influence process might the artifact engage?**
4. **What actually happened in the person or system?**

Only the first two can often be inferred directly from the artifact. The third is a hypothesis unless supported by relevant evidence. The fourth requires outcome evidence.

---

# 1. Top-level layers

## L0 — Provenance and evidence

Objects that establish where a statement, annotation, source, or inference came from.

Canonical entities:
- `SourceRecord`
- `EvidenceItem`
- `VerificationRecord`
- `AnalysisAssertion`

This layer may attach to anything in the ontology.

## L1 — Persuasion episode and artifact

Canonical entities:
- `PersuasionEpisode`
- `Communicator`
- `Audience`
- `Artifact`
- `ArtifactSegment`
- `Context`

These describe who communicated what, to whom, where, and under what conditions.

## L2 — Semantic and argumentative content

Canonical entities:
- `Proposition`
- `Claim`
- `Argument`
- `Ground`
- `Warrant`
- `Backing`
- `Qualifier`
- `Rebuttal`
- `Implication`
- `Omission`

These answer what is asserted, implied, supported, omitted, or reasoned from.

## L3 — Message-level influence structure

Canonical superclass:
- `MessageFeature`

Canonical subtypes:
- `RhetoricalOperation`
- `InfluenceCue`
- `PresentationProperty`
- `ActionPrompt`

Examples include framing, repetition, metaphor, contrast, authority cue, social-proof cue, scarcity cue, emotional loading, vividness, and explicit calls to action.

A message feature is **observable or inferable from the artifact**. It is not itself a psychological mechanism.

## L4 — Person-level constructs and influence pathways

Canonical entities:
- `PsychologicalConstruct`
- `InfluencePathway`
- `Mechanism`

Canonical roles within a pathway:
- `target_construct`
- `mediator`
- `moderator`
- `confounder`
- `outcome_construct`

Important: target, mediator, moderator, and confounder are **roles**, not permanent entity classes. The same construct can play different roles in different pathways.

Examples of constructs:
- perceived credibility
- uncertainty
- arousal
- perceived threat
- perceived consensus
- familiarity
- identity alignment
- cognitive elaboration
- reactance
- attention allocation

A mechanism is a proposed process explaining **how or why** a change occurs. A construct is a variable or state that may participate in that process.

## L5 — Internal response and interpretation

Canonical entities:
- `InternalState`
- `Interpretation`
- `BeliefState`
- `AttitudeState`
- `ConfidenceState`
- `ActionTendency`

These represent person-level outcomes or intermediate states.

Do not infer them as observed unless the person-level data supports them.

## L6 — Behavior

Canonical entity:
- `Behavior`

Examples:
- accepting a claim
- sharing a post
- purchasing
- voting/supporting
- requesting more information
- verifying a source
- resisting or refusing
- counter-speaking

Behavior must be distinguished from intention, attitude, and predicted probability of behavior.

## L7 — Social, platform, institutional, and system context

Canonical entities:
- `SocialCondition`
- `NetworkCondition`
- `PlatformCondition`
- `InstitutionalCondition`
- `SystemOutcome`
- `SystemVariable`
- `SystemRelation`
- `FeedbackLoop`
- `Delay`

These represent conditions and dynamics beyond the single individual.

## L8 — Resistance, intervention, and training

Canonical entities:
- `Countermeasure`
- `CopingResponse`
- `TrainingTarget`
- `TrainingItem`
- `LearnerObservation`

These connect the analysis ontology to Persuasion Gym's adaptive-learning layer.

---

# 2. Canonical analytical chain

When evidence allows, a full analysis may be represented as:

`ArtifactSegment`
→ `expresses` → `Claim`
→ `contains_feature` → `MessageFeature`
→ `participates_in` → `InfluencePathway`
→ `targets_construct` → `PsychologicalConstruct`
→ `operates_via` → `Mechanism`
→ `changes` → `InternalState`
→ `shapes` → `Interpretation`
→ `updates` → `BeliefState / AttitudeState`
→ `increases_probability_of` → `Behavior`
→ `contributes_to` → `SystemOutcome`
→ `feeds_back_to` → earlier `SystemVariable`

This is a **representational possibility**, not a required causal sequence.

## Missing-link rule

If the artifact supports identification of a message feature but the mechanism is not supported, represent:

`MessageFeature` → `mechanism_status: unresolved`

Do not invent a mechanism to complete the chain.

If a mechanism is supported at the group level but no person-specific evidence exists, represent:

`Mechanism evidence: supported in relevant populations`

and separately:

`Person-specific activation: unknown`

---

# 3. Critical distinctions

## 3.1 Proposition vs claim

A `Proposition` is content that can in principle be evaluated as true/false or accepted/rejected.

A `Claim` is a proposition that an artifact or communicator advances, presupposes, or asks the audience to accept.

A proposition may exist without being asserted. A claim has a discourse role.

## 3.2 Claim vs argument

A `Claim` is what is being asserted.

An `Argument` is a support structure linking grounds to a claim through one or more warrants.

A persuasive message can contain claims without arguments.

## 3.3 Rhetorical operation vs influence cue

A `RhetoricalOperation` organizes or transforms presentation and meaning.
Examples: framing, metaphor, contrast, narrative sequencing, rhetorical question, repetition.

An `InfluenceCue` is a perceivable feature that can serve as a shortcut, signal, or socially meaningful input.
Examples: prestige cue, majority cue, scarcity cue, identity cue, endorsement cue.

Some artifact features can legitimately receive both annotations if they perform both functions. Do not force mutual exclusivity.

## 3.4 Message feature vs mechanism

A message feature is in the artifact.

A mechanism is the process proposed to connect an exposure to a change.

Wrong:
> "Scarcity is the mechanism."

Preferred:
> "A scarcity cue is present; one candidate pathway is that perceived scarcity increases anticipated opportunity loss, which may increase urgency under specified conditions."

## 3.5 Construct vs state

A `PsychologicalConstruct` is an analytical variable or latent concept, such as perceived credibility or uncertainty.

An `InternalState` is a temporally indexed value or condition of a construct in a person or population.

Example:
- construct: `uncertainty`
- state: `high uncertainty at exposure time`

## 3.6 Mechanism vs mediator

A `Mechanism` is an explanatory process.

A `mediator` is a role played by a variable hypothesized to lie on a causal pathway.

Do not use the words interchangeably.

## 3.7 Moderator vs mediator

A mediator transmits part of a hypothesized effect.

A moderator changes the strength or direction of a relationship under different conditions.

The same construct can be a mediator in one pathway and moderator in another.

## 3.8 Intention vs function

`CommunicatorIntent` is not a default entity inferred from rhetoric.

Intent may be encoded only as an `AnalysisAssertion` with one of:
- `explicit`
- `documented`
- `strongly_inferred`
- `weakly_inferred`
- `unknown`

Functional language is preferred when intent is unknown:
> "The message structure increases urgency cues"
not
> "The speaker wants to panic the audience."

## 3.9 Persuasion vs manipulation

`Persuasion` is not a message feature and `Manipulation` is not a synonym for influence.

Manipulation is represented as a separate `ManipulationAssessment` over multiple dimensions. See `references/manipulation-assessment.md`.

## 3.10 Truth vs validity vs influence

- factual truth belongs to verification;
- inferential quality belongs to argument analysis;
- rhetorical structure belongs to rhetoric analysis;
- psychological mechanism belongs to mechanism analysis;
- manipulation risk belongs to manipulation assessment;
- system dynamics belong to systems analysis.

No single verdict may substitute for another.

---

# 4. InfluencePathway: the central bridging object

`InfluencePathway` is the canonical object connecting message analysis to person-level mechanism analysis.

Required fields:

- `pathway_id`
- `triggering_feature_ids`
- `target_construct_ids`
- `mechanism_id` or `mechanism_status: unresolved`
- `mediator_roles[]`
- `moderator_roles[]`
- `predicted_internal_change`
- `predicted_downstream_effect`
- `population_scope`
- `context_scope`
- `time_scale`
- `evidence_status`
- `evidence_refs[]`
- `person_specific_status`
- `alternative_pathways[]`
- `disconfirming_observations[]`

The pathway is the place where causal hypotheses live. Message annotations alone must not carry causal claims.

---

# 5. AnalysisAssertion: the epistemic wrapper

Every nontrivial inference generated by Persuasion Gym should be representable as an `AnalysisAssertion`.

Required fields:

- `assertion_id`
- `subject_id`
- `relation`
- `object_id_or_value`
- `assertion_kind`
- `origin_skill`
- `epistemic_status`
- `evidence_status`
- `verification_status`
- `confidence`
- `scope`
- `evidence_refs[]`
- `alternative_explanations[]`
- `notes`

This wrapper prevents prose from silently upgrading an inference into a fact.

Example:

```yaml
assertion_id: A-042
subject_id: MF-07
relation: targets_construct
object_id_or_value: PC-12
assertion_kind: mechanism_hypothesis
origin_skill: persuasion-mechanism-analysis
epistemic_status: inferred
evidence_status: supported
verification_status: not_applicable
confidence: 0.72
scope: "adult online news users under uncertainty"
evidence_refs: [SRC-31, SRC-44]
alternative_explanations: ["attention capture rather than uncertainty reduction"]
notes: "Population-level evidence; activation in this individual is unknown."
```

---

# 6. Systems representation

Systems analysis uses canonical entities rather than inventing a separate vocabulary.

A `SystemRelation` must contain:

- `source_variable_id`
- `target_variable_id`
- `polarity`: positive | negative | nonlinear | unknown
- `relation_type`
- `time_scale`
- `delay`
- `evidence_status`
- `scope`
- `mechanism_ref`

A feedback loop must contain at least two relations and return to an upstream variable.

A loop is not valid merely because the final node could conceivably affect the first.

---

# 7. Training representation

The learning layer never creates domain truth.

`TrainingTarget` points to one or more canonical distinctions or relations, for example:

- distinguish `InfluenceCue` from `EvidenceItem`;
- distinguish `RhetoricalOperation` from `Mechanism`;
- identify an unsupported `Warrant`;
- detect a missing `moderator` condition;
- distinguish `Behavior` from `ActionTendency`;
- distinguish `ManipulationAssessment` from factual falsity.

`LearnerObservation` records performance, not personality.

Allowed examples:
- "missed authority-cue vs expertise-evidence distinction in 3 of 5 recent items"
- "confidence exceeded calibrated accuracy by 18 percentage points on causal-claim items"

Disallowed:
- "gullible"
- "manipulable"
- "biased person"

---

# 8. Inter-skill ownership

## De-Spin
Owns:
- claim boundaries
- implied claims
- omitted context
- source/provenance investigation
- persuasion/manipulation signals as investigation triggers

Maps output into:
`Claim`, `Implication`, `Omission`, `EvidenceItem`, `SourceRecord`, `MessageFeature`

## Critical Thinking
Owns:
- argument reconstruction
- grounds
- warrants
- backing
- qualifiers
- rebuttals
- reasoning gaps / assumptions

Maps output into:
`Argument`, `Ground`, `Warrant`, `Backing`, `Qualifier`, `Rebuttal`, `AnalysisAssertion`

## Rhetorical Structure Analysis
Owns:
- `MessageFeature` annotation
- rhetorical form and function at the artifact level

Must not assert person-level mechanism without routing through mechanism analysis.

## Persuasion Mechanism Analysis
Owns:
- `PsychologicalConstruct`
- `InfluencePathway`
- `Mechanism`
- mediator/moderator roles
- evidence-graded person-level causal hypotheses

## Systems Thinking
Owns:
- `SystemVariable`
- `SystemRelation`
- `FeedbackLoop`
- `Delay`
- system boundary and dynamic hypotheses

Must consume mechanisms rather than invent them.

## Fact-Check
Owns:
- `VerificationRecord`
- external factual validation of material claims

Must not overwrite rhetoric, logic, mechanism, or manipulation judgments.

## Agentic Learning
Owns:
- `TrainingTarget`
- `TrainingItem`
- `LearnerObservation`
- scheduling and adaptive practice state

Must train on reconciled canonical outputs.

---

# 9. Canonical null values

Use explicit uncertainty rather than forced classification.

Allowed null states:
- `unknown`
- `unresolved`
- `not_observed`
- `not_applicable`
- `insufficient_evidence`
- `conflicting_evidence`

Do not use empty strings to hide uncertainty.

---

# 10. Versioning

Changes are classified as:

### Patch
Clarification that does not change meaning or fields.

### Minor
New optional entity, relation, field, or subtype compatible with prior analyses.

### Major
Changed definition, renamed canonical term, altered role semantics, or incompatible schema change.

Every specialist skill must declare the ontology version it expects.

---
name: persuasion-rhetorical-structure-analysis
description: >-
  Analyze the observable rhetorical structure of speeches, advertisements, articles,
  posts, debates, negotiations, headlines, transcripts, images, video, and other
  persuasive artifacts using the Persuasion Gym canonical rhetoric taxonomy. Use when
  the task is to identify framing, narrative organization, pragmatic operations,
  stylistic choices, source/credibility cues, social/identity cues, affective cueing,
  action prompts, repetition, evidence display, comparison structures, or multimodal
  rhetoric. Anchor every finding to the artifact and keep message-level description
  separate from factual truth, argument validity, psychological mechanism, audience
  response, manipulation verdict, and speaker intent.
license: MIT
metadata:
  version: "0.1.0"
  project: "Persuasion Gym"
  ontology_version: "0.1.0"
  rhetoric_taxonomy_version: "0.1.0"
  status: "operational rhetorical-analysis skill"
---

# Persuasion Rhetorical Structure Analysis

## Purpose

Use this skill to convert a persuasive artifact into a **structured, anchored map of its
message-level rhetorical architecture**.

The core question is:

> **What is present in the communication, how is the communication organized, and what
> communicative functions do those observable features serve?**

This skill deliberately stops before asking whether the message is true, logically sound,
psychologically effective, manipulative, or intentionally deceptive.

For Persuasion Gym, this is the bridge between raw artifacts and later specialist analysis:

`artifact → segments → claims / action prompts → rhetorical features → rhetorical functions → handoff flags`

It is not the final interpretation of persuasion.

---

## Required dependencies

This skill MUST use:

1. **Persuasion Gym Canonical Ontology v0.1.0**
2. **Persuasion Gym Canonical Rhetoric Taxonomy v0.1.0**

If either dependency is unavailable, do not invent replacement labels. Use plain-language
provisional descriptions and mark the analysis `DEPENDENCY_INCOMPLETE`.

Load when needed:

- `references/analysis-protocol.md`
- `references/handoff-routing.md`
- `references/multimodal-analysis.md`
- `assets/rhetorical-analysis-schema.yaml`

---

# Non-negotiable rules

## 1. Artifact first

Every material rhetorical finding must be anchored to an observable part of the artifact:

- exact text span;
- timestamp or transcript span;
- image/visual region;
- audiovisual sequence;
- documented cross-artifact recurrence.

If you cannot point to the evidence, do not present the feature as observed.

## 2. Message feature is not psychological mechanism

Allowed:

> `SRC.authority_cue` is present because the message foregrounds the source's professional title.

Not allowed:

> The title made the audience trust the speaker.

The second statement belongs to Persuasion Mechanism Analysis and requires separate evidence.

## 3. Message feature is not audience state

Do not infer fear, trust, certainty, identity alignment, anger, urgency, confusion, or belief
from message form alone.

Use:

> `AFF.threat_cue` — the message depicts a severe negative consequence.

Not:

> The audience became afraid.

## 4. Rhetoric is not factual verification

A statistic, testimonial, expert citation, graph, or consensus claim is a rhetorical/evidential
feature whether or not it is accurate.

Truth, source validity, denominator quality, fabrication, and currentness belong to Fact-Check /
De-Spin.

## 5. Rhetoric is not argument validity

This skill may identify an explicit comparison, causal claim, enthymematic support structure,
or dichotomized option presentation. It must not decide that an argument is valid or invalid,
or label a fallacy as established.

Route those questions to Critical Thinking.

## 6. Rhetoric is not manipulation

Framing, emotional language, authority cues, scarcity, repetition, identity cues, narrative,
and calls to action are not manipulation merely by occurring.

Manipulation is a separate multidimensional assessment.

## 7. Do not infer hidden intent

Distinguish:

- **observable requested action** — what the artifact explicitly asks the audience to do;
- **communicative function** — what a feature does at discourse level;
- **speaker intent/motive** — normally unknown without independent evidence.

Never convert the first two into the third.

## 8. Use multi-label annotation

Rhetorical features are not mutually exclusive. One span can carry several features when each
has independent textual or multimodal support.

Do not force one "best" label when the artifact genuinely instantiates multiple operations.

## 9. Respect granularity

A local phrase does not establish an artifact-wide strategy.

Annotate whether the unit is:

- `span`
- `section`
- `artifact`
- `cross_artifact`

Use artifact-level labels only when supported across enough of the artifact to justify the scope.

## 10. Distinguish observation from interpretation

Every annotation must use one epistemic status:

- `OBSERVED`
- `STRONGLY_INFERRED`
- `TENTATIVE`
- `UNRESOLVED`

Use the weakest status justified by the evidence.

## 11. Preserve plausible alternative readings

Pragmatics, irony, insinuation, framing, and strategic ambiguity can support more than one
reasonable interpretation. Record alternatives rather than manufacturing certainty.

## 12. Cross-artifact claims require provenance

Do not annotate `REP.repeated_claim` across multiple exposures unless the artifact set or
provenance record actually establishes recurrence.

One repeated sentence within one artifact and repeated exposure across a campaign are different facts.

## 13. Analyze multimodal artifacts multimodally

If persuasive meaning depends on image, sound, editing, typography, gesture, captioning, or
layout, transcript-only analysis is incomplete. Mark missing channels explicitly.

## 14. Negative findings must be scoped

"No authority cue detected" means no qualifying cue was found in the analyzed material. It does
not mean authority played no role elsewhere in the campaign or context.

## 15. Do not complete a pattern because it looks rhetorically elegant

Never invent a villain because a narrative has a hero, infer pathos because ethos is present,
or force Aristotle's triad onto every artifact.

---

# Workflow

## Step 0 — Establish the analysis contract

Record:

- artifact type;
- available modalities;
- language;
- source/provenance if known;
- unit of analysis;
- requested depth: `quick`, `standard`, or `deep`;
- whether the artifact is complete or excerpted.

If context is missing, continue with the artifact but record the limitation.

### Modes

**Quick**
- identify dominant features and functions;
- top 5–8 anchored findings;
- routing flags.

**Standard**
- full feature-family scan;
- global rhetorical architecture;
- ambiguity/alternative-reading check;
- structured output.

**Deep**
- fine-grained segmentation;
- complete annotation ledger;
- multimodal alignment if available;
- discourse progression;
- cross-feature pattern analysis;
- explicit downstream handoff package.

---

## Step 1 — Normalize and segment the artifact

Preserve the original wording and order.

Create stable segment identifiers such as:

- `S001`, `S002` for text;
- `T00:15-00:22` for audio/video;
- `V01.region_header` for visual regions;
- `X03` for cross-artifact units.

Do not paraphrase the anchor inside quotation fields.

For long artifacts, segment by discourse unit rather than arbitrary token count where possible:

- headline;
- opening;
- claim block;
- example;
- narrative episode;
- objection/refutation;
- transition;
- call to action;
- closing.

---

## Step 2 — Build the semantic/discourse skeleton

Before labeling rhetorical features, identify only what is needed to orient the analysis:

- explicit propositions / claims;
- explicit requested actions;
- named or represented actors/groups;
- stated comparisons;
- stated causal relations;
- explicit evidence displays;
- presupposed or implied propositions where strongly supported;
- major topic transitions.

Do not audit factual truth or logical quality here.

If an implication is genuinely ambiguous, represent alternatives.

---

## Step 3 — Annotate local rhetorical features

Scan the artifact against all applicable canonical families:

### `FRM` — framing and salience
Look for problem definition, causal attribution, moral evaluation, remedy orientation, gain/loss
frames, reference points, category labels, foregrounding/backgrounding, scope, temporal framing,
and metaphorical framing.

### `NAR` — narrative organization
Look for event sequence, causal plot, protagonist/antagonist/victim/hero construction, conflict,
turning points, resolution, morals, testimony, and exemplar stories.

### `PRG` — pragmatic/discourse operations
Look for presupposition, implicature, insinuation, rhetorical/leading questions, indirect requests,
warnings, promises, threats, concessions, disclaimers, reported speech, recontextualized quotation,
and strategic ambiguity.

### `LEX` — lexical/figurative/stylistic operations
Look for metaphor, analogy, euphemism, dysphemism, loaded language, hyperbole, irony, antithesis,
parallelism, anaphora, vivid language, nominalization, passive agent suppression, and related form.

### `SRC` — source/credibility signaling
Look for expertise, credentials, authority, prestige, firsthand experience, testimonial,
endorsement, institutional backing, expert-consensus cues, independence claims, transparency
signals, confidence displays, and character/goodwill signals.

### `SOC` — social/identity/norm signaling
Look for identity cues, in-group/out-group markers, us/them contrast, belonging, descriptive or
injunctive norms, social proof, majority/popularity cues, peer endorsement, hierarchy, loyalty,
social sanction, delegitimation, and identity labeling.

### `AFF` — affective/evaluative cueing
Look for threat, fear, anger, disgust, hope, pride, guilt, shame, sympathy, outrage, reassurance,
aspiration, moral-emotional language, and vivid consequence.

### `ACT` — action/choice/urgency/commitment prompting
Look for calls to action, imperatives, urgency, deadlines, scarcity, commitment requests, public
commitment, small first steps, reciprocity/consistency cues, defaults, binary choice presentation,
opt-out friction, and risk reversal.

### `REP` — repetition and recurrence
Look for exact or semantic repetition, slogans, catchphrases, refrains, repeated claims, labels,
visual symbols, and source cues.

### `EVD` — evidence presentation
Look for statistics, base rates, percentages, absolute numbers, relative risks, charts, citations,
expert quotations, anecdotes, cases, before/after displays, quantified precision, source links,
method references, and evidence bundles.

### `CMP` — comparison and alternatives
Look for explicit/implicit comparison, baseline/reference-class selection, before/after contrast,
counterfactuals, best/worst-case contrasts, dichotomization, and candidate equivalence/alternative
suppression structures.

### `VIS` — visual/multimodal operations
Look for salience hierarchy, scale, color valence, symbolic association, image selection, cropping,
juxtaposition, graphical comparison, typography, music, sound effects, editing, reaction shots,
authority markers, and caption framing.

Each annotation must use a canonical feature ID when one exists.

---

## Step 4 — Assign communicative functions

For each material feature, assign only functions justified by the artifact:

- `function.attention_directing`
- `function.interpretation_guiding`
- `function.source_positioning`
- `function.evaluation_cueing`
- `function.identity_positioning`
- `function.norm_signaling`
- `function.option_structuring`
- `function.action_prompting`
- `function.memory_recurrence`
- `function.evidence_display`
- `function.objection_management`
- `function.uncertainty_marking`

Optional higher-order metadata:

- `function.ethos`
- `function.pathos`
- `function.logos`

These tags describe discourse function. They do not assert psychological effect.

---

## Step 5 — Map rhetorical architecture

After local annotation, identify how features are organized across the artifact.

Ask:

1. What is foregrounded at the beginning?
2. What problem or situation is constructed?
3. Which actors or categories are introduced?
4. What evidence or reasons are displayed?
5. How are objections, alternatives, or uncertainty handled?
6. Which source-positioning and social-positioning cues recur?
7. How does evaluative intensity change over the artifact?
8. Where does the message shift from interpretation to action?
9. What is repeated or returned to?
10. How does the closing reframe, summarize, or request action?

Describe the architecture using neutral functional language, for example:

> The artifact opens by defining the problem as an immediate threat, establishes institutional
> authority, presents two quantitative evidence displays, contrasts an in-group with an out-group,
> and closes with an urgent call to action.

Do not rewrite this as:

> The speaker scares the audience into obeying.

---

## Step 6 — Check overlaps and competing annotations

For every high-impact annotation ask:

- Is this feature genuinely instantiated or merely compatible with the wording?
- Is there a more specific canonical label?
- Are two labels describing distinct properties or double-counting the same property?
- Does context support a pragmatic reading?
- Is a local metaphor being overpromoted into an artifact-level frame?
- Is a cue being mistaken for its downstream effect?

Where two readings remain credible, keep both with explicit status.

---

## Step 7 — Generate downstream routing flags

Do not perform the downstream analysis inside this skill.

Create routing flags only when warranted.

Examples:

### Critical Thinking
- `argument_review_needed`
- `causal_inference_review_needed`
- `dichotomy_review_needed`
- `comparison_validity_review_needed`
- `hidden_premise_review_needed`

### Fact-Check / De-Spin
- `fact_check_needed`
- `source_verification_needed`
- `statistical_context_check_needed`
- `quotation_context_check_needed`
- `cross_artifact_provenance_check_needed`

### Persuasion Mechanism Analysis
- `mechanism_analysis_candidate`
- `candidate_feature_ids: [...]`

### Manipulation Assessment
- `manipulation_assessment_candidate`

### Systems Thinking
- `systems_analysis_candidate`

A routing flag is not a verdict.

---

## Step 8 — Produce the structured analysis

The final output must contain:

1. **Artifact scope**
2. **Rhetorical architecture summary**
3. **Anchored feature ledger**
4. **Higher-order functions**
5. **Important ambiguities / alternative readings**
6. **What is NOT established by this analysis**
7. **Downstream routing flags**
8. **Machine-readable analysis object** when requested or used by another skill

Use `assets/rhetorical-analysis-schema.yaml` for structured interchange.

---

## Step 9 — Self-audit before release

Run all checks:

### Anchor check
Can every material finding be located in the artifact?

### Layer check
Did any message feature silently become a psychological effect, factual verdict, logic verdict,
manipulation verdict, or intent attribution?

### Scope check
Was a local feature generalized to the whole artifact without sufficient support?

### Label check
Were canonical taxonomy IDs used where available?

### Ambiguity check
Were plausible competing interpretations retained?

### Modality check
Was a transcript analyzed as though it contained visual/audio evidence that was not actually available?

### Handoff check
Were specialist questions routed rather than answered opportunistically?

If any check fails, revise before release.

---

# Output discipline

## Preferred finding format

```yaml
annotation_id: A017
segment_id: S004
anchor: "Only 12 seats remain — enroll before midnight."
unit: span
features:
  - feature_id: ACT.scarcity_cue
    status: OBSERVED
    rationale: "The message states limited remaining availability."
    functions:
      - function.option_structuring
      - function.action_prompting
  - feature_id: ACT.deadline_cue
    status: OBSERVED
    rationale: "A specific decision deadline is presented."
    functions:
      - function.action_prompting
not_inferred:
  - scarcity_is_real
  - audience_felt_urgency
  - manipulation
  - deceptive_intent
routing_flags:
  - fact_check_needed
  - mechanism_analysis_candidate
  - manipulation_assessment_candidate
```

## Preferred prose style

Use precise descriptions:

> The sentence combines a scarcity cue with a deadline cue and an explicit action prompt.

Avoid psychologized shorthand:

> The sentence exploits FOMO.

The shorthand collapses message feature, candidate mechanism, audience state, and ethical judgment.

---

# Common failure modes

## Device dumping
Listing 20 device names without explaining where they occur or what discourse function they serve.

**Repair:** anchor, prioritize, and connect local features to architecture.

## Aristotelian compression
Reducing the entire artifact to ethos/pathos/logos.

**Repair:** use the triad only as higher-order metadata over specific canonical features.

## Effect smuggling
"Repetition makes the claim feel true."

**Repair:** `REP.repeated_claim` here; truth-effect mechanism later.

## Intent smuggling
"The speaker uses ambiguity to evade accountability."

**Repair:** annotate `PRG.strategic_ambiguity`; infer motive only with independent evidence.

## Truth smuggling
"Fake expert consensus."

**Repair:** annotate `SRC.consensus_of_experts_cue`; route actual consensus to verification.

## Fallacy smuggling
"False dichotomy."

**Repair:** annotate `CMP.dichotomization` or candidate alternative suppression; route logical defect to Critical Thinking.

## Manipulation smuggling
"This emotional appeal is manipulative."

**Repair:** annotate the affective cue and route manipulation separately.

## Context blindness
Interpreting irony, quotation, or a slogan without surrounding discourse.

**Repair:** widen the segment or mark unresolved.

## Transcript blindness
Ignoring editing, music, image selection, captions, or visual salience in audiovisual persuasion.

**Repair:** analyze available modalities or explicitly state the missing channel.

---

# Exit criteria

A rhetorical analysis is complete when:

1. the artifact and modality scope are explicit;
2. all material findings are anchored;
3. canonical feature IDs are used consistently;
4. global rhetorical architecture is synthesized from local evidence;
5. ambiguity is represented rather than erased;
6. no psychological effect, factual truth, logical validity, manipulation verdict, or hidden intent has been smuggled into the rhetorical layer;
7. downstream specialist questions are routed;
8. the analysis object can be consumed by later Persuasion Gym modules.

If these conditions are not met, the analysis is not ready for downstream mechanism inference or training use.

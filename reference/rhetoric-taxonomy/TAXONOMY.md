# Persuasion Gym Canonical Rhetoric Taxonomy

**Version:** 0.1.0  
**Layer:** message / discourse structure  
**Normative status:** canonical vocabulary for Persuasion Gym rhetorical annotation

---

# 0. Purpose

This taxonomy standardizes how Persuasion Gym describes rhetorical structure before any psychological, factual, ethical, or systems-level interpretation occurs.

It exists to prevent four recurrent errors:

1. calling a rhetorical device a psychological mechanism;
2. calling a persuasive cue manipulation merely because it is persuasive;
3. inferring speaker intent from message form;
4. mixing factual verification or argument validity into rhetorical annotation.

The taxonomy asks:

> **What is the message doing at the level of wording, structure, presentation, discourse, source signaling, social signaling, or action prompting?**

It does not ask whether that operation worked.

---

# 1. Unit of analysis

Every annotation must identify one of three units:

- `span` — a bounded phrase, sentence, image region, audio segment, or multimodal unit;
- `section` — a larger discourse unit such as a paragraph, scene, argument block, or ad panel;
- `artifact` — a property of the whole speech, article, advertisement, post, debate clip, video, or interaction.

Do not assign an artifact-level feature when only one local span supports it unless the annotation explicitly says `local_instance`.

---

# 2. Five annotation dimensions

Every feature annotation may carry five independent dimensions:

1. **form** — what observable construction is present;
2. **content role** — what semantic/discourse role it performs;
3. **rhetorical function** — what communicative function it appears to serve;
4. **targeted proposition/action** — which claim, interpretation, source judgment, identity relation, or action it bears on;
5. **epistemic status** — observed, strongly inferred, tentative, unresolved.

These dimensions must not be collapsed.

---

# 3. Higher-order rhetorical functions

The classical Aristotelian triad is represented as **functional metadata**, not as atomic devices.

## 3.1 `ethos_function`

Message construction that bears on the presented character, credibility, authority, trustworthiness, competence, goodwill, or standing of a communicator or cited source.

Examples of lower-level features that may contribute:
- `expertise_cue`
- `prestige_status_cue`
- `testimonial`
- `credential_display`
- `firsthand_experience_claim`
- `value_alignment_signal`

Do not infer actual credibility from an ethos function.

## 3.2 `pathos_function`

Message construction that foregrounds emotionally evaluative material or explicitly invites an affect-laden appraisal.

Examples:
- `threat_cue`
- `hope_appeal`
- `anger_appraisal`
- `pity_sympathy_appeal`
- `pride_appeal`
- `guilt_shame_appeal`
- `vivid_consequence`

Do not annotate the audience as actually feeling the emotion without person-level evidence.

## 3.3 `logos_function`

Message construction that offers, displays, compresses, or simulates reasons for accepting a proposition.

Examples:
- explicit argument
- enthymematic argument
- example / analogy
- causal explanation
- quantitative evidence display
- comparison
- refutation

Argument validity belongs to Critical Thinking, not this taxonomy.

A feature may support more than one higher-order function.

---

# 4. Canonical feature families

The canonical L3 message-feature families are:

1. `FRM` — framing and salience
2. `NAR` — narrative organization
3. `PRG` — pragmatic and discourse operations
4. `LEX` — lexical, figurative, and stylistic operations
5. `SRC` — source and credibility signaling
6. `SOC` — social, identity, and norm signaling
7. `AFF` — affective and evaluative cueing
8. `ACT` — action, choice, urgency, and commitment prompting
9. `REP` — repetition, sloganization, and structural recurrence
10. `EVD` — evidence presentation and evidential display
11. `CMP` — comparison, contrast, and alternative construction
12. `VIS` — visual / multimodal rhetorical operations

These families are **multi-label**. One segment may legitimately receive several feature annotations.

---

# 5. Family definitions

## 5.1 FRM — framing and salience

Message operations that select, foreground, background, label, organize, or evaluate aspects of an issue so that a particular interpretation becomes easier to construct.

Canonical features:
- `FRM.problem_definition`
- `FRM.causal_attribution`
- `FRM.moral_evaluation`
- `FRM.remedy_orientation`
- `FRM.gain_frame`
- `FRM.loss_frame`
- `FRM.reference_point`
- `FRM.category_label`
- `FRM.foregrounding`
- `FRM.backgrounding`
- `FRM.issue_scope`
- `FRM.temporal_frame`
- `FRM.metaphorical_frame`

Framing is not synonymous with bias, deception, or manipulation.

## 5.2 NAR — narrative organization

Message operations that organize material as events involving agents, temporal sequence, causality, goals, conflict, change, or resolution.

Canonical features:
- `NAR.event_sequence`
- `NAR.causal_plot`
- `NAR.protagonist_construction`
- `NAR.antagonist_construction`
- `NAR.victim_construction`
- `NAR.hero_rescuer_construction`
- `NAR.conflict_structure`
- `NAR.turning_point`
- `NAR.resolution`
- `NAR.moral_of_story`
- `NAR.first_person_testimony`
- `NAR.exemplar_story`

Narrative transportation is a person-level candidate mechanism and is therefore **not** a message feature.

## 5.3 PRG — pragmatic and discourse operations

Operations in which meaning or communicative force extends beyond literal propositional content.

Canonical features:
- `PRG.presupposition`
- `PRG.conversational_implicature`
- `PRG.conventional_implicature`
- `PRG.insinuation`
- `PRG.rhetorical_question`
- `PRG.leading_question`
- `PRG.indirect_request`
- `PRG.warning`
- `PRG.promise`
- `PRG.threat`
- `PRG.challenge`
- `PRG.concession`
- `PRG.disclaimer`
- `PRG.quotation_recontextualization`
- `PRG.reported_speech`
- `PRG.strategic_ambiguity`

Speech-act force and perlocutionary effect must remain separate: a warning is observable at discourse level; frightening someone is an audience outcome.

## 5.4 LEX — lexical, figurative, and stylistic operations

Observable choices in wording, figurative expression, intensity, rhythm, and verbal patterning.

Canonical features:
- `LEX.metaphor`
- `LEX.analogy`
- `LEX.simile`
- `LEX.metonymy`
- `LEX.euphemism`
- `LEX.dysphemism`
- `LEX.loaded_language`
- `LEX.hyperbole`
- `LEX.understatement`
- `LEX.irony`
- `LEX.sarcasm`
- `LEX.antithesis`
- `LEX.parallelism`
- `LEX.tricolon`
- `LEX.anaphora`
- `LEX.epistrophe`
- `LEX.alliteration`
- `LEX.rhyme_rhythm`
- `LEX.vivid_language`
- `LEX.concreteness`
- `LEX.nominalization`
- `LEX.passive_agent_suppression`

Do not infer psychological effect from stylistic form alone.

## 5.5 SRC — source and credibility signaling

Features that present information about who knows, who endorses, who has standing, or why a source should be treated as credible.

Canonical features:
- `SRC.expertise_cue`
- `SRC.credential_display`
- `SRC.authority_cue`
- `SRC.prestige_status_cue`
- `SRC.firsthand_experience_claim`
- `SRC.testimonial`
- `SRC.endorsement`
- `SRC.institutional_backing`
- `SRC.consensus_of_experts_cue`
- `SRC.independence_claim`
- `SRC.transparency_signal`
- `SRC.confidence_display`
- `SRC.character_goodwill_signal`

The presence of a cue does not establish that the source is actually expert, independent, or trustworthy.

## 5.6 SOC — social, identity, and norm signaling

Message features that represent social categories, group membership, norms, consensus, status relations, belonging, or social sanction.

Canonical features:
- `SOC.identity_cue`
- `SOC.in_group_marker`
- `SOC.out_group_marker`
- `SOC.us_them_contrast`
- `SOC.unity_belonging_cue`
- `SOC.descriptive_norm_cue`
- `SOC.injunctive_norm_cue`
- `SOC.social_proof_cue`
- `SOC.majority_consensus_cue`
- `SOC.popularity_cue`
- `SOC.peer_endorsement`
- `SOC.status_hierarchy_cue`
- `SOC.loyalty_appeal`
- `SOC.social_sanction_cue`
- `SOC.distancing_delegitimation`
- `SOC.identity_labeling`

Actual identification, conformity, or norm internalization belongs to person/system layers.

## 5.7 AFF — affective and evaluative cueing

Message features that explicitly or implicitly mark events, people, outcomes, or choices with emotional or motivational valence.

Canonical features:
- `AFF.threat_cue`
- `AFF.fear_appeal`
- `AFF.anger_appraisal`
- `AFF.disgust_appraisal`
- `AFF.hope_appeal`
- `AFF.pride_appeal`
- `AFF.guilt_appeal`
- `AFF.shame_appeal`
- `AFF.pity_sympathy_appeal`
- `AFF.outrage_cue`
- `AFF.reassurance_cue`
- `AFF.aspiration_cue`
- `AFF.moral_emotional_language`
- `AFF.vivid_consequence`

Annotate the message cue, not the audience emotion.

## 5.8 ACT — action, choice, urgency, and commitment prompting

Message features that explicitly organize choice or request, accelerate action, or seek commitment.

Canonical features:
- `ACT.explicit_call_to_action`
- `ACT.indirect_call_to_action`
- `ACT.imperative`
- `ACT.urgency_cue`
- `ACT.deadline_cue`
- `ACT.scarcity_cue`
- `ACT.commitment_request`
- `ACT.public_commitment_request`
- `ACT.small_first_step`
- `ACT.reciprocity_cue`
- `ACT.consistency_cue`
- `ACT.default_or_preselected_option`
- `ACT.binary_choice_presentation`
- `ACT.opt_out_friction`
- `ACT.risk_reversal`

Whether a binary choice is fallacious is an argument-analysis question. Whether urgency is manipulative is an ethical/manipulation assessment.

## 5.9 REP — repetition, sloganization, and structural recurrence

Features that repeat or rhythmically recur within an artifact or across a documented message series.

Canonical features:
- `REP.exact_repetition`
- `REP.semantic_repetition`
- `REP.slogan`
- `REP.catchphrase`
- `REP.refrain`
- `REP.repeated_claim`
- `REP.repeated_label`
- `REP.repeated_visual_symbol`
- `REP.repeated_source_cue`

Cross-exposure repetition requires provenance evidence across artifacts. Do not infer an illusory-truth mechanism from repetition alone.

## 5.10 EVD — evidence presentation and evidential display

Features that present something as evidence or as warrant for credibility.

Canonical features:
- `EVD.statistic`
- `EVD.base_rate`
- `EVD.percentage`
- `EVD.absolute_number`
- `EVD.relative_risk`
- `EVD.graph_chart`
- `EVD.study_citation`
- `EVD.expert_quote`
- `EVD.anecdote`
- `EVD.case_example`
- `EVD.before_after_comparison`
- `EVD.quantified_precision`
- `EVD.source_link`
- `EVD.method_reference`
- `EVD.evidence_bundle`

Truth, relevance, denominators, cherry-picking, and source quality are assessed elsewhere.

## 5.11 CMP — comparison, contrast, and alternative construction

Message features that structure interpretation by juxtaposing options, groups, time periods, baselines, or counterfactuals.

Canonical features:
- `CMP.explicit_comparison`
- `CMP.implicit_comparison`
- `CMP.baseline_selection`
- `CMP.reference_class_selection`
- `CMP.before_after_contrast`
- `CMP.counterfactual`
- `CMP.best_case_contrast`
- `CMP.worst_case_contrast`
- `CMP.dichotomization`
- `CMP.false_equivalence_candidate`
- `CMP.alternative_suppression_candidate`

The suffix `candidate` is deliberate: logical defect or material omission must be established by argument/evidence analysis.

## 5.12 VIS — visual / multimodal rhetorical operations

Message-level operations carried primarily or partly through image, layout, typography, sound, editing, gesture, or audiovisual composition.

Canonical features:
- `VIS.salience_hierarchy`
- `VIS.scale_emphasis`
- `VIS.color_valence_cue`
- `VIS.symbolic_association`
- `VIS.image_selection`
- `VIS.cropping_context_selection`
- `VIS.juxtaposition`
- `VIS.graphical_comparison`
- `VIS.typographic_emphasis`
- `VIS.music_affective_cue`
- `VIS.sound_effect_cue`
- `VIS.editing_sequence`
- `VIS.reaction_shot`
- `VIS.on_screen_authority_marker`
- `VIS.caption_frame`

Never infer deception from editing or cropping alone. The annotation describes presentation; verification determines whether material context was omitted.

---

# 6. Cross-cutting functional tags

These tags describe what a feature is doing in the discourse without pretending to identify a psychological mechanism:

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

Higher-order Aristotelian tags may be added:
- `function.ethos`
- `function.pathos`
- `function.logos`

These are descriptive functional tags, not effect claims.

---

# 7. Structures that belong outside this taxonomy

The following must not be encoded as rhetorical devices:

## Argument defects
Examples: ad hominem, affirming the consequent, hasty generalization, circular reasoning.

Owner: **Critical Thinking / argument analysis**.

A rhetorical analyst may flag `argument_review_needed`, but should not duplicate the fallacy engine.

## Factual status
Examples: true, false, misleading, unsupported.

Owner: **De-Spin / Fact-Check**.

## Psychological mechanisms
Examples: processing fluency, threat appraisal, normative conformity, reactance, narrative transportation, motivated reasoning.

Owner: **Persuasion Mechanism Analysis**.

## Person-specific mental states
Examples: fear, trust, certainty, identity alignment, arousal.

Owner: person-level analysis; may be hypothesized but not annotated as observed from message form.

## Manipulation / ethics verdict
Owner: **Manipulation Assessment**.

## Intent
Examples: “the speaker deliberately frightened the audience.”

Intent remains `unknown` unless supported by independent evidence.

---

# 8. Multi-label rule

Features are not mutually exclusive.

Example:

> “Doctors across the country agree: act today before supplies run out.”

Possible message-level annotations:

- `SRC.consensus_of_experts_cue`
- `SOC.majority_consensus_cue`
- `ACT.explicit_call_to_action`
- `ACT.urgency_cue`
- `ACT.scarcity_cue`
- `function.ethos`
- `function.action_prompting`

What may **not** be inferred from the sentence alone:

- the doctors actually agree;
- the scarcity is real;
- authority increased trust;
- the audience felt urgency;
- the message manipulated anyone;
- the speaker knowingly deceived anyone.

---

# 9. Evidence threshold for annotation

Each feature annotation must have one status:

- `OBSERVED` — directly instantiated in the artifact;
- `STRONGLY_INFERRED` — discourse function follows with little ambiguity from context;
- `TENTATIVE` — plausible but competing readings exist;
- `UNRESOLVED` — insufficient evidence to classify.

A rhetorical feature should never receive a causal evidence grade. Causal evidence belongs to the later mechanism layer.

---

# 10. Annotation minimal record

Every annotation must minimally include:

```yaml
feature_id: SOC.social_proof_cue
unit: span
anchor: "Join the 2 million people who already switched"
status: OBSERVED
rationale: "The message explicitly uses the behavior of a large number of others as a reason-relevant cue."
functions:
  - function.norm_signaling
possible_overlaps:
  - EVD.absolute_number
not_inferred:
  - actual_consensus
  - conformity
  - truth
  - manipulation
```

---

# 11. Exit criteria

A rhetorical-structure pass is complete when:

1. all material message features are anchored to the artifact;
2. features use canonical IDs;
3. overlaps are preserved rather than forced into one label;
4. higher-order functions are distinguished from atomic features;
5. implied meaning is separated from literal meaning;
6. argument defects are handed to Critical Thinking;
7. factual claims are handed to De-Spin / Fact-Check;
8. mechanisms are left unresolved unless a later mechanism pass establishes them;
9. audience states and behavioral outcomes are not inferred as observed;
10. manipulation and intent are not smuggled into rhetorical labels.

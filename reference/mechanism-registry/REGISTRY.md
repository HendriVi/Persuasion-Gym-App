# Persuasion Gym Canonical Psychological Mechanism Registry

**Version:** 0.1.0  
**Layer:** person-level constructs and influence pathways  
**Normative status:** canonical mechanism vocabulary for Persuasion Gym

---

# 0. Purpose

This registry defines the psychological processes that Persuasion Gym may use when explaining how a rhetorical or influence feature could affect an audience.

It answers:

> **If a message feature matters, through what empirically defensible person-level process might it matter, under what conditions, and with what uncertainty?**

It does **not** infer:

- hidden speaker intent;
- that a mechanism operated in a particular person merely because a matching cue appeared;
- that a persuasive effect is manipulative;
- that a robust effect has one settled mechanism;
- that a laboratory effect transfers unchanged to every domain, population, or platform;
- that predictive-processing terminology can replace established persuasion evidence.

---

# 1. Required analytical separation

Every analysis must keep the following levels separate:

`MessageFeature` — observable/inferable from the artifact  
`PsychologicalConstruct` — variable such as perceived credibility, threat, uncertainty, familiarity  
`Mechanism` — process explaining how change may occur  
`InternalState` — temporally indexed state in a person or population  
`Outcome` — belief, attitude, confidence, action tendency, or behavior  
`SystemEffect` — group/network/institutional consequence

Correct:

> `REP.repeated_claim` is present. Repetition makes `EPI.repetition_familiarity_truth` a candidate pathway. Population-level evidence supports a repetition-induced truth effect, but person-specific activation is unknown.

Incorrect:

> The claim was repeated, therefore the user believed it because of processing fluency.

---

# 2. Entry types

The registry allows four entry kinds:

1. `mechanism` — a proposed explanatory process with meaningful empirical support.
2. `processing_regime` — a higher-order condition that changes which processes are likely to dominate.
3. `robust_effect_multiple_mechanisms` — a reliable phenomenon whose exact mechanism is multiply determined or disputed.
4. `resistance_process` — a process by which people detect, counter, or resist persuasive influence.

Do not force every useful phenomenon into the label `mechanism`.

---

# 3. Evidence model

Every entry receives two independent grades:

- **Effect evidence (`E0-E4`)** — how strongly the phenomenon/outcome relation is supported.
- **Mechanism evidence (`M0-M3`)** — how specifically the proposed explanatory pathway is supported.

A strong effect with a disputed explanation may therefore be `E4 / M1`.

Full definitions: `references/evidence-grading.md`.

---

# 4. Canonical mechanism families

## 4.1 PRC — processing regulation
Processes that alter depth, effort, attention, or mode of processing.

- `PRC.elaboration_likelihood`
- `PRC.capacity_load_regulation`

## 4.2 EPI — epistemic and metacognitive inference
Processes used to judge credibility, truth, familiarity, or evidential weight.

- `EPI.source_credibility_weighting`
- `EPI.processing_fluency_cue`
- `EPI.repetition_familiarity_truth`
- `EPI.anchoring_assimilation`

## 4.3 DEC — judgment and choice construction
Processes by which presentation or choice architecture alters evaluation or selection.

- `DEC.reference_dependent_framing`
- `DEC.affect_heuristic`
- `DEC.default_channels`

## 4.4 SOC — social and identity influence
Processes that use information about others, norms, group membership, or social sanctions.

- `SOC.descriptive_norm_inference`
- `SOC.injunctive_norm_social_sanction`
- `SOC.social_identity_referent_influence`

## 4.5 MOT — motivational regulation
Processes in which goals, consistency, autonomy, scarcity, or obligation bias interpretation or action.

- `MOT.motivated_reasoning`
- `MOT.cognitive_dissonance_consistency`
- `MOT.psychological_reactance`
- `MOT.scarcity_value`
- `MOT.reciprocity_obligation`

## 4.6 AFF — affective appraisal
Processes in which emotional or motivational appraisal changes judgment or action.

- `AFF.threat_efficacy_appraisal`
- `AFF.vividness_accessibility`

## 4.7 NAR — narrative processing

- `NAR.narrative_transportation`

## 4.8 RES — resistance and coping

- `RES.persuasion_knowledge_activation`
- `RES.inoculation_counterarguing`

---

# 5. Canonical entries

## `PRC.elaboration_likelihood`

**Kind:** `processing_regime`  
**Effect evidence:** `E4`  
**Mechanism evidence:** `M2`

**Definition:** Variation in motivation and ability changes the degree of issue-relevant thought devoted to a persuasive message. Under higher elaboration, argument-relevant cognition carries more weight; under lower elaboration, judgments are more likely to depend on lower-effort cues, associations, or simple inferences.

**Typical inputs:** personal relevance, accountability, knowledge, distraction, time pressure, complexity, cognitive capacity.

**Candidate outcomes:** greater or lesser argument scrutiny; differential weight given to message arguments versus source/context cues.

**Boundary conditions:** variables can play multiple roles. A source cue, emotion, or framing device can alter elaboration, serve as an argument, bias thought, or operate as a low-effort cue depending on context.

**Do not infer:** “central route” or “peripheral route” from a single message feature; low elaboration does not mean irrationality.

**Primary foundation:** Petty & Cacioppo (1986); Petty, Wegener & Fabrigar (1997); Crano & Prislin (2006).

---

## `PRC.capacity_load_regulation`

**Kind:** `processing_regime`  
**Effect evidence:** `E3`  
**Mechanism evidence:** `M2`

**Definition:** Limited attention, working-memory demands, distraction, fatigue, or time pressure can reduce resources available for effortful evaluation and increase reliance on simpler cues or previously accessible responses.

**Typical inputs:** overload, multitasking, compressed decision time, distraction, complex information.

**Moderators:** expertise, motivation, task familiarity, external aids.

**Do not infer:** that a cognitively loaded person necessarily accepts the message; load can also impair comprehension or produce rejection.

---

## `EPI.source_credibility_weighting`

**Kind:** `mechanism`  
**Effect evidence:** `E3`  
**Mechanism evidence:** `M2`

**Definition:** Perceived expertise, trustworthiness, independence, or relevant standing can alter the weight given to communicated information.

**Typical message features:** `SRC.expertise_cue`, `SRC.credential_display`, `SRC.institutional_backing`, `SRC.consensus_of_experts_cue`.

**Mediating constructs:** perceived expertise, perceived trustworthiness, source diagnosticity.

**Moderators:** issue involvement, source-message fit, prior attitudes, timing of source information, suspicion, audience knowledge.

**Alternatives:** cue may change attention or elaboration rather than directly increase acceptance.

**Do not infer:** credentials = actual credibility; source credibility = claim truth.

**Primary foundation:** Pornpitakpan (2004) critical review.

---

## `EPI.processing_fluency_cue`

**Kind:** `mechanism`  
**Effect evidence:** `E3`  
**Mechanism evidence:** `M2`

**Definition:** Subjective ease of processing can be interpreted as information about properties of the stimulus, including familiarity, truth, safety, liking, or confidence, depending on context and attribution.

**Typical inputs:** perceptual clarity, linguistic simplicity, rhyme, pronounceability, conceptual familiarity, repetition.

**Moderators:** whether the person has an alternative explanation for the fluency; task instructions; judgment domain; prior knowledge.

**Alternatives:** semantic coherence, memory retrieval, affective positivity.

**Do not infer:** all simple language persuades; fluency effects depend on what the ease is interpreted to mean.

**Primary foundation:** Alter & Oppenheimer (2009); Reber & Unkelbach (2010); Yagi et al. (2023).

---

## `EPI.repetition_familiarity_truth`

**Kind:** `robust_effect_multiple_mechanisms`  
**Effect evidence:** `E4`  
**Mechanism evidence:** `M2`

**Definition:** Repeated statements are, on average, more likely to receive higher subjective truth ratings than comparable novel statements.

**Candidate mechanisms:** increased processing fluency; familiarity; referential/semantic coherence; memory-based inference.

**Typical message features:** `REP.exact_repetition`, `REP.semantic_repetition`, `REP.repeated_claim`, cross-artifact repetition.

**Moderators/boundaries:** prior knowledge, warning/instructions, repetition schedule, source memory, statement plausibility, contextual attribution.

**Do not infer:** repetition makes everyone believe a claim; repetition is independent corroboration; fluency is the only mechanism.

**Primary foundation:** Dechêne et al. (2010); Brashier & Marsh (2020); 2026 systematic review/meta-analysis of the illusory truth effect.

---

## `EPI.anchoring_assimilation`

**Kind:** `robust_effect_multiple_mechanisms`  
**Effect evidence:** `E4`  
**Mechanism evidence:** `M1`

**Definition:** Exposure to a numerical or evaluative reference value can shift subsequent judgments toward that reference.

**Candidate explanations:** selective accessibility, insufficient adjustment, scale calibration, conversational/informational inference.

**Typical message features:** explicit initial price, benchmark, forecast, comparison number, opening demand.

**Moderators:** anchor relevance, dimensional match, expertise, incentives, debiasing, whether anchor contains directional information.

**Do not infer:** all numbers are anchors; incidental/random anchors are equally strong; one mechanism explains all anchoring.

**Primary foundation:** 2026 meta-analysis of 50 years of anchoring research.

---

## `DEC.reference_dependent_framing`

**Kind:** `robust_effect_multiple_mechanisms`  
**Effect evidence:** `E4`  
**Mechanism evidence:** `M2`

**Definition:** Describing substantively equivalent outcomes relative to different reference points or as gains versus losses can alter preferences and risk judgments.

**Typical message features:** `FRM.gain_frame`, `FRM.loss_frame`, `FRM.reference_point`, `CMP.baseline_selection`.

**Candidate mechanisms:** reference dependence, loss sensitivity, response compatibility, task representation.

**Moderators:** outcome domain, task structure, probability information, participant characteristics, framing manipulation.

**Do not infer:** every framing effect is prospect-theoretic loss aversion; all forms of framing are equivalent.

**Primary foundation:** Tversky & Kahneman (1981); Kühberger (1998) meta-analysis.

---

## `DEC.affect_heuristic`

**Kind:** `mechanism`  
**Effect evidence:** `E3`  
**Mechanism evidence:** `M2`

**Definition:** Rapid positive or negative affective evaluations can serve as inputs to judgments of risk, benefit, desirability, or choice when fuller analysis is costly or unnecessary.

**Typical message features:** `AFF.*`, evaluative imagery, morally valenced language, affect-laden exemplars.

**Moderators:** deliberation, numeracy, expertise, accountability, affect intensity and relevance.

**Do not infer:** emotion replaces reasoning; affect can also be valid information and can interact with analytic thought.

**Primary foundation:** Slovic, Finucane, Peters & MacGregor (2007).

---

## `DEC.default_channels`

**Kind:** `robust_effect_multiple_mechanisms`  
**Effect evidence:** `E4`  
**Mechanism evidence:** `M1`

**Definition:** Preselecting an option can increase selection of that option, but the effect is multiply determined.

**Candidate mechanisms:** implied endorsement, effort/ease, status quo/endowment, inertia, loss aversion.

**Typical message features:** `ACT.default_or_preselected_option`, opt-out structures.

**Moderators:** domain, trust in choice architect, effort to switch, perceived recommendation, stakes.

**Do not infer:** defaults work through one mechanism or are always effective.

**Primary foundation:** Jachimowicz et al. (2019) meta-analysis.

---

## `SOC.descriptive_norm_inference`

**Kind:** `mechanism`  
**Effect evidence:** `E4`  
**Mechanism evidence:** `M2`

**Definition:** Information about what relevant others do can alter beliefs about what is common, effective, safe, appropriate, or likely, and can thereby influence behavior.

**Typical message features:** `SOC.descriptive_norm_cue`, `SOC.social_proof_cue`, `SOC.majority_consensus_cue`, `SOC.popularity_cue`.

**Mediating constructs:** perceived prevalence, perceived behavioral normality, informational diagnosticity.

**Moderators:** referent proximity/relevance, public versus private behavior, ambiguity, group identification, domain.

**Do not infer:** popularity proves truth; descriptive norms and injunctive norms are interchangeable.

**Primary foundation:** social-norm meta-analyses including Melnyk et al.; 2026 meta-analysis distinguishing descriptive and injunctive norms.

---

## `SOC.injunctive_norm_social_sanction`

**Kind:** `mechanism`  
**Effect evidence:** `E4`  
**Mechanism evidence:** `M2`

**Definition:** Information about what relevant others approve, disapprove, reward, or sanction can change intentions or behavior through anticipated social evaluation and norm compliance.

**Typical message features:** `SOC.injunctive_norm_cue`, `SOC.social_sanction_cue`, `SOC.loyalty_appeal`.

**Moderators:** visibility, group importance, sanction credibility, identification, perceived legitimacy.

**Do not infer:** public compliance equals private belief change.

**Primary foundation:** normative-influence reviews and meta-analyses.

---

## `SOC.social_identity_referent_influence`

**Kind:** `mechanism`  
**Effect evidence:** `E3`  
**Mechanism evidence:** `M2`

**Definition:** When a social category is salient and self-relevant, perceived prototypical group norms and ingroup sources can become informative for judgment, attitude, and behavior.

**Typical message features:** `SOC.identity_cue`, `SOC.in_group_marker`, `SOC.us_them_contrast`, `SOC.unity_belonging_cue`.

**Moderators:** strength and salience of identification, prototype fit, intergroup context, anonymity/visibility, source ingroup status.

**Alternatives:** generic conformity, instrumental reward/punishment, informational influence independent of identity.

**Do not infer:** an identity cue automatically activates identification; group agreement implies identity-based influence.

**Primary foundation:** Hogg & Reid (2006); Spears (2021).

---

## `MOT.motivated_reasoning`

**Kind:** `mechanism`  
**Effect evidence:** `E3`  
**Mechanism evidence:** `M2`

**Definition:** Accuracy goals and directional goals can influence which beliefs, memories, arguments, and inferential strategies are accessed and evaluated, within constraints imposed by plausibility and available knowledge.

**Typical contexts:** identity-relevant claims, self-interest, moral commitments, prior attitudes, desired conclusions.

**Moderators:** strength of directional motive, ambiguity of evidence, knowledge, accountability, countervailing accuracy goals.

**Do not infer:** disagreement with evidence proves motivated reasoning; people can reach desired conclusions only if they can construct a seemingly reasonable justification.

**Primary foundation:** Kunda (1990); later attitudes/persuasion reviews.

---

## `MOT.cognitive_dissonance_consistency`

**Kind:** `mechanism`  
**Effect evidence:** `E3`  
**Mechanism evidence:** `M2`

**Definition:** Perceived inconsistency among behavior, commitments, beliefs, or self-relevant cognitions can produce aversive motivation that may be reduced through attitude change, justification, reinterpretation, or behavior change.

**Typical inputs:** voluntary commitment, effort, public choice, counterattitudinal behavior, inconsistency cues.

**Moderators:** perceived choice/responsibility, self-relevance, commitment strength, alternatives for reducing inconsistency.

**Do not infer:** any consistency cue activates dissonance; attitude change is the only dissonance-reduction response.

**Primary foundation:** classic dissonance literature; Petty et al. (1997); Crano & Prislin (2006); recent reviews.

---

## `MOT.psychological_reactance`

**Kind:** `mechanism`  
**Effect evidence:** `E4`  
**Mechanism evidence:** `M2`

**Definition:** Perceived threat to behavioral or attitudinal freedom can evoke a motivational state associated with anger and counterarguing and can produce resistance or movement away from the advocated position.

**Typical message features:** controlling language, coercive demands, `PRG.threat`, extreme `ACT.imperative`, autonomy-restricting pressure.

**Moderators:** importance of threatened freedom, legitimacy, message intensity, individual differences, availability of alternatives.

**Do not infer:** any disagreement is reactance; urgency alone proves reactance.

**Primary foundation:** Rains (2013) meta-analytic review.

---

## `MOT.scarcity_value`

**Kind:** `robust_effect_multiple_mechanisms`  
**Effect evidence:** `E3`  
**Mechanism evidence:** `M1`

**Definition:** Scarcity can increase perceived value or desirability under some conditions, but scarcity effects can reflect several pathways.

**Candidate mechanisms:** commodity valuation, inferred demand/quality, anticipated opportunity loss, competition, reactance.

**Typical message features:** `ACT.scarcity_cue`, `ACT.deadline_cue`, quantity limitation.

**Moderators:** reason for scarcity, product desirability, uniqueness, credibility, whether scarcity is supply- or demand-driven.

**Do not infer:** scarcity always increases value; scarcity automatically produces urgency; one mechanism explains all scarcity effects.

**Primary foundation:** Lynn (1991) quantitative review.

---

## `MOT.reciprocity_obligation`

**Kind:** `mechanism`  
**Effect evidence:** `E2`  
**Mechanism evidence:** `M1`

**Definition:** Receiving a benefit, favor, concession, or cooperative act can create perceived social obligation or guilt that may increase reciprocal behavior or compliance.

**Typical message features:** `ACT.reciprocity_cue`, concessions, gifts, favors, “I did X for you” structures.

**Moderators:** legitimacy of benefit, relationship, cultural norm, perceived ulterior motive, size and timing of concession.

**Alternatives:** liking, guilt, perceptual contrast, self-presentation.

**Do not infer:** reciprocity is the established mechanism behind every sequential-request effect; door-in-the-face evidence shows small heterogeneous effects and competing explanations.

**Primary foundation:** reciprocity-norm literature; O'Keefe & Hale (1998) meta-analysis of door-in-the-face effects.

---

## `AFF.threat_efficacy_appraisal`

**Kind:** `mechanism`  
**Effect evidence:** `E4`  
**Mechanism evidence:** `M2`

**Definition:** Threat communications can influence attitudes, intentions, and behavior through appraisal of threat and the perceived efficacy/feasibility of the recommended response; fear arousal alone is not the complete mechanism.

**Typical message features:** `AFF.threat_cue`, `AFF.fear_appeal`, `AFF.vivid_consequence` plus recommended action.

**Moderators:** perceived severity, susceptibility, response efficacy, self-efficacy, action costs, audience characteristics.

**Do not infer:** fear appeals necessarily backfire; stronger fear is always better; observed fear proves persuasion.

**Primary foundation:** Tannenbaum et al. (2015) meta-analysis.

---

## `AFF.vividness_accessibility`

**Kind:** `robust_effect_multiple_mechanisms`  
**Effect evidence:** `E2`  
**Mechanism evidence:** `M1`

**Definition:** Vivid information may receive disproportionate weight when it is more attention-grabbing, memorable, accessible, or elaborated, but the persuasive effect is heterogeneous and historically inconsistent.

**Typical message features:** `LEX.vivid_language`, `AFF.vivid_consequence`, concrete exemplars, striking imagery.

**Moderators:** recall, delay, congruence, cognitive elaboration, relevance.

**Do not infer:** vividness is inherently persuasive; availability is the only explanation.

**Primary foundation:** Blondé & Girandola (2016) meta-analysis.

---

## `NAR.narrative_transportation`

**Kind:** `mechanism`  
**Effect evidence:** `E3`  
**Mechanism evidence:** `M2`

**Definition:** Absorption in a narrative—combining attentional focus, imagery, and affect—can increase story-consistent beliefs and evaluations and may reduce counterarguing or critical scrutiny under some conditions.

**Typical message features:** `NAR.*`, especially coherent plot, identification-relevant characters, imagery-rich storytelling.

**Moderators:** story quality, prior beliefs, transportability, identification, genre/context.

**Do not infer:** presence of a story = transportation; transportation = deception; narrative effects always bypass reasoning.

**Primary foundation:** Green & Brock (2000) and later narrative-persuasion research.

---

## `RES.persuasion_knowledge_activation`

**Kind:** `resistance_process`  
**Effect evidence:** `E3`  
**Mechanism evidence:** `M1`

**Definition:** Recognizing an interaction as a persuasion attempt and activating knowledge about agents, motives, and tactics can change how the target interprets and copes with the message.

**Typical inputs:** explicit sponsorship, tactic recognition, implausible claims, persuasion forewarning, prior experience.

**Candidate outcomes:** discounting, source re-evaluation, counterarguing, strategic compliance, resistance.

**Moderators:** persuasion literacy, developmental experience, tactic familiarity, trust, transparency.

**Do not infer:** tactic recognition always reduces persuasion; persuasion knowledge can produce different coping responses.

**Primary foundation:** Friestad & Wright (1994).

---

## `RES.inoculation_counterarguing`

**Kind:** `resistance_process`  
**Effect evidence:** `E4`  
**Mechanism evidence:** `M2`

**Definition:** Forewarning plus exposure to weakened challenges and refutations can increase resistance to later persuasive attacks, partly by motivating or supplying counterarguments.

**Typical training use:** pre-bunking common manipulation tactics; generating counterarguments before exposure; delayed transfer tests.

**Moderators:** issue involvement, similarity between inoculation and attack, delay, threat, counterargument quality.

**Do not infer:** inoculation makes beliefs permanently immune; resistance generalizes equally to unrelated tactics/domains.

**Primary foundation:** Banas & Rains (2010) meta-analysis.

---

# 6. Crosswalk rule

The rhetoric taxonomy may nominate **candidate** mechanisms, never deterministic ones.

Examples:

- `SRC.authority_cue` -> candidate `EPI.source_credibility_weighting`
- `REP.repeated_claim` -> candidate `EPI.repetition_familiarity_truth`
- `SOC.social_proof_cue` -> candidate `SOC.descriptive_norm_inference`
- `SOC.in_group_marker` -> candidate `SOC.social_identity_referent_influence`
- `AFF.fear_appeal` -> candidate `AFF.threat_efficacy_appraisal`
- `ACT.scarcity_cue` -> candidates `MOT.scarcity_value`, `MOT.psychological_reactance`
- `NAR.causal_plot` -> candidate `NAR.narrative_transportation`
- `FRM.loss_frame` -> candidate `DEC.reference_dependent_framing`
- `ACT.default_or_preselected_option` -> candidate `DEC.default_channels`

Full crosswalk: `references/feature-mechanism-crosswalk.md`.

---

# 7. Person-specific activation rule

A mechanism may have one of four activation statuses:

- `NOT_ASSESSED`
- `CANDIDATE` — cue/pathway is plausible from artifact/context, but no person-level evidence.
- `SUPPORTED_IN_EPISODE` — person-level observations are consistent with the pathway and alternatives have been considered.
- `EXPERIMENTALLY_IDENTIFIED` — the episode or study design provides credible causal identification of the pathway.

Default for ordinary real-world artifact analysis is **`CANDIDATE`**, not `SUPPORTED_IN_EPISODE`.

Self-report such as “that made me trust him” is evidence about experience, but does not by itself identify a unique causal mechanism.

---

# 8. Predictive-processing integration rule

Predictive processing may be used as an **interpretive bridge**, not as a replacement for established persuasion mechanisms.

Allowed:

> Source credibility may be represented computationally as changing the effective weight assigned to communicated evidence.

Not allowed:

> Authority cues work because they increase precision weighting, therefore source-credibility theory is unnecessary.

Canonical persuasion/social-psychology evidence receives priority. Predictive-processing terminology must be marked `integrative_interpretation`, not `empirically_established_mechanism`, unless the specific claim has direct evidence.

---

# 9. Minimal mechanism assertion

```yaml
mechanism_id: EPI.source_credibility_weighting
entry_kind: mechanism
candidate_from_features:
  - SRC.expertise_cue
target_construct: perceived_source_credibility
predicted_change: increase
outcome_construct: acceptance_probability
activation_status: CANDIDATE
effect_evidence: E3
mechanism_evidence: M2
person_specific_evidence: none
moderators_considered:
  - issue_involvement
  - source_message_fit
alternatives:
  - increased_attention
  - elaboration_change
intent_status: UNKNOWN
confidence: 0.62
```

---

# 10. Forbidden shortcuts

The following are invalid:

- rhetorical feature -> observed internal state;
- rhetorical feature -> behavior without pathway/context;
- robust effect -> settled mechanism;
- population evidence -> person-specific causal diagnosis;
- correlation -> mechanism;
- neural activation -> psychological mechanism by itself;
- “bias” label -> irrationality;
- emotional language -> emotional hijacking;
- group cue -> identity activation;
- repeated claim -> belief;
- scarcity cue -> urgency;
- authority cue -> trust;
- fear appeal -> fear;
- prediction-processing vocabulary -> empirical proof.

---

# 11. Exit criteria

A mechanism-analysis pass is complete when:

1. relevant message features have been mapped only to **candidate** pathways;
2. each pathway uses a canonical registry ID;
3. effect evidence and mechanism evidence are reported separately;
4. moderators and boundary conditions are named;
5. plausible alternative explanations are retained;
6. person-specific activation is not inferred without person-level evidence;
7. truth, logic, manipulation, and intent remain separate judgments;
8. contested mechanisms are represented as contested;
9. unsupported mechanistic stories are marked unresolved rather than completed for narrative neatness;
10. any predictive-processing interpretation is clearly labeled as an integration layer rather than substituted for the empirical persuasion literature.

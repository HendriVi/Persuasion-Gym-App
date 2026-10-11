# Canonical Skill Registry

The registry contains trainable competencies, not personality traits.

## Core families

### RHETORIC
- `RHE.detect_feature` — identify observable rhetorical features.
- `RHE.classify_feature` — map a feature to the canonical rhetoric taxonomy.
- `RHE.distinguish_feature_effect` — keep message feature separate from audience effect.
- `RHE.detect_multimodal_feature` — identify visual/audio/editing rhetoric when modality supports it.

### ARGUMENT
- `ARG.claim_decomposition` — distinguish explicit claim, implication, assumption, request.
- `ARG.warrant_identification` — identify warrant linking evidence to conclusion.
- `ARG.inference_validity` — distinguish truth of premises from validity/strength of inference.
- `ARG.alternative_explanation` — generate credible competing explanation.

### VERIFICATION
- `VER.claim_checkability` — identify what is externally checkable.
- `VER.source_of_truth` — identify the authoritative/appropriate source.
- `VER.truth_rhetoric_separation` — avoid inferring truth from rhetoric or falsity from manipulation cues.
- `VER.provenance_reasoning` — distinguish independent corroboration from repetition/reposting.

### MECHANISM
- `MEC.candidate_generation` — map observed features to defensible candidate mechanisms.
- `MEC.alternative_mechanisms` — preserve competing mechanisms.
- `MEC.activation_ceiling` — respect person-specific activation ceiling.
- `MEC.effect_mechanism_separation` — robust effect does not imply settled mechanism.
- `MEC.moderator_awareness` — identify conditions that strengthen/weaken a candidate pathway.

### INTENT
- `INT.function_intent_separation` — distinguish functional effect from private intent.
- `INT.intent_evidence_grading` — assign intent status only to available evidence.

### CAUSAL
- `CAU.association_causation` — distinguish association from causal effect.
- `CAU.total_effect_mechanism` — distinguish causal treatment effect from mechanism identification.
- `CAU.mediation_mechanism` — distinguish statistical mediation from causal mechanism.
- `CAU.population_person` — distinguish population evidence from person-specific causation.
- `CAU.system_arrow_discipline` — keep causal-loop arrows at their evidence status.

### MANIPULATION
- `MAN.persuasion_manipulation_separation` — rhetoric/effectiveness does not equal manipulation.
- `MAN.deception_manipulation_separation` — deception and manipulation are related but distinct.
- `MAN.dimension_assessment` — assess canonical manipulation dimensions independently.
- `MAN.boundary_case_reasoning` — handle legitimate urgency/defaults/fear/social proof without shortcut labels.

### SYSTEMS
- `SYS.boundary_definition` — define the relevant influence-system boundary.
- `SYS.chain_loop_separation` — distinguish a chain from a feedback loop.
- `SYS.selection_influence` — distinguish selection/homophily from influence/amplification.
- `SYS.level_separation` — distinguish individual, group, network, platform, institution outcomes.
- `SYS.delay_nonlinearity` — identify delays and nonlinearities without inventing them.

### RESISTANCE
- `RES.countermeasure_selection` — choose the smallest effective verification/resistance action.
- `RES.counterframe_generation` — generate alternative framing without distorting material facts.
- `RES.uncertainty_tolerance` — preserve unresolved status when evidence is insufficient.

### METACOGNITION
- `META.confidence_calibration` — confidence tracks correctness for the relevant skill.
- `META.overclaim_control` — avoid stronger claims than evidence warrants.
- `META.answer_revision` — update after evidence without defensiveness or anchoring.

## Registry rule

New skills require:
1. stable ID;
2. observable scoring criterion;
3. answer-key source;
4. at least one confusable alternative where appropriate;
5. mapping to training modes;
6. versioning.

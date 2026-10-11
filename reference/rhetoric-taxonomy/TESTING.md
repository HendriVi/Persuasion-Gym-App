# Rhetoric Taxonomy Regression Tests

A future `rhetorical-structure-analysis` skill should pass all tests below.

## T01 — Authority is not credibility
Input: “Professor X, Nobel laureate, says this supplement works.”
Expected: source/authority/credential cue(s).
Forbidden: actual expertise relevance, truth, increased trust, manipulation.

## T02 — Threat cue is not fear
Input: “If this law passes, thousands could lose their jobs.”
Expected: `AFF.threat_cue`; possibly causal framing depending context.
Forbidden: “the audience is afraid.”

## T03 — Repetition is not illusory truth
Input repeats one slogan five times.
Expected: repetition/slogan labels.
Forbidden: claims that familiarity or truth belief increased.

## T04 — Presupposition is not assertion
Input: “Why did the minister hide the report?”
Expected: leading/rhetorical question depending context + presupposition that the report was hidden.
Forbidden: treating the presupposition as verified fact.

## T05 — Metaphor vs metaphorical frame
Input: one ornamental metaphor with no broader organizing role.
Expected: `LEX.metaphor` only.
Forbidden: `FRM.metaphorical_frame` unless issue organization is supported.

## T06 — Narrative vs anecdote
Input: “My neighbor tried it and felt better.”
Expected: `EVD.anecdote`; `NAR.first_person_testimony` only if narrative criteria are met.
Forbidden: full narrative structure by default.

## T07 — Social proof is not consensus truth
Input: “Over 5 million customers chose us.”
Expected: `SOC.social_proof_cue`, `EVD.absolute_number`.
Handoff: fact check number/representativeness if material.

## T08 — Framing is not manipulation
Input: tax policy described as “tax relief.”
Expected: category/evaluative framing candidate, depending context.
Forbidden: manipulation verdict.

## T09 — Scarcity is not fake scarcity
Input: “Only 3 seats left.”
Expected: `ACT.scarcity_cue`.
Handoff: Fact-Check if material.
Forbidden: deceptive scarcity unless verified.

## T10 — Dichotomization is not yet false dilemma
Input: “Either approve this plan or accept decline.”
Expected: `CMP.dichotomization`.
Handoff: Critical Thinking to test exhaustiveness.
Forbidden: automatic fallacy verdict.

## T11 — Ethos/pathos/logos are functions
Input contains a doctor testimonial, a fear-laden consequence, and a causal argument.
Expected: atomic features + functional tags ethos/pathos/logos.
Forbidden: using ethos/pathos/logos as the only feature labels.

## T12 — Multilabel preservation
Input: “Experts agree—join millions of families and act before midnight.”
Expected: source cue + social proof/norm cue + action prompt + urgency cue.
Forbidden: selecting only one “dominant tactic” and discarding the rest.

## T13 — Speech act vs effect
Input: “I warn you: the bridge is unsafe.”
Expected: warning speech act.
Forbidden: “frightens the listener.”

## T14 — Visual crop discipline
Input: cropped image shows only violent portion of a longer event.
Expected: crop/context-selection annotation.
Forbidden: “misleading edit” unless missing context is independently established as material.

## T15 — Intent discipline
Input uses repeated loaded labels.
Expected: loaded language + repetition.
Forbidden: “the author deliberately brainwashed the audience.”

## T16 — Evidence display vs evidence quality
Input shows a graph and cites a study.
Expected: graph/chart + study citation.
Handoff: Fact-Check/Scientific Critical Thinking.
Forbidden: assuming evidential quality.

## T17 — Identity mention vs identity cue
Input neutrally reports demographic data.
Expected: no identity-influence cue solely because a group is named.

## T18 — Cross-artifact repetition requires provenance
Input: user provides one post and claims it was repeated everywhere.
Expected: local repetition only if present; cross-artifact repetition unresolved without other artifacts/provenance.

## T19 — Function does not equal mechanism
Input contains prestige markers around a speaker.
Expected: source positioning / ethos function.
Forbidden: “prestige heuristic caused acceptance.”

## T20 — Omitted alternatives require handoff
Input presents two options where analyst suspects a third.
Expected: dichotomization + possible `alternative_suppression_candidate` if context supports concern.
Handoff: argument/evidence audit.
Forbidden: confirmed omission without external basis.

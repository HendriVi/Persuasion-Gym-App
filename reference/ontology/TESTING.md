# Persuasion Gym Ontology — Validation Tests

The ontology is ready for use only if specialist outputs pass these tests.

## 1. Device ≠ mechanism

Input: "Only three seats left."

Pass:
- scarcity/urgency cue may be annotated as a MessageFeature;
- mechanism remains separate and evidence-graded.

Fail:
- `mechanism: scarcity`.

## 2. Claim ≠ argument

Input: "This policy will reduce crime."

Pass: one claim can exist with no explicit argument.

Fail: inventing grounds and warrants merely because a claim is present.

## 3. Truth ≠ manipulation

Input: a factually true claim presented with coercive social pressure.

Pass: factual verification can be `verified` while manipulation risk is elevated.

Fail: "true, therefore not manipulative."

## 4. Falsehood ≠ manipulation

Input: an inaccurate statement made through ordinary error.

Pass: fact-check can return contradicted while intent/manipulation remains unresolved.

Fail: automatically labeling deception or manipulation.

## 5. Intent discipline

Input: highly emotional political speech with no independent evidence of private motive.

Pass: functional effects can be described; intent remains `unknown` or appropriately inferred.

Fail: "the speaker intends to frighten people" as fact.

## 6. Target / mediator / moderator are roles

Input: uncertainty is targeted by one message, mediates another effect, and moderates a third.

Pass: same PsychologicalConstruct receives different pathway roles.

Fail: duplicate fixed entity types `UncertaintyTarget`, `UncertaintyMediator`, `UncertaintyModerator`.

## 7. Group evidence ≠ person-specific activation

Input: literature supports an illusory-truth effect; one person saw a repeated claim.

Pass: mechanism evidence may be supported while person-specific activation remains unknown.

Fail: "repetition made this person believe the claim."

## 8. Action tendency ≠ behavior

Input: user says "I wanted to buy it" but did not purchase.

Pass: ActionTendency recorded; Behavior absent/not observed.

Fail: purchase behavior inferred.

## 9. Systems arrow ≠ causal evidence

Input: analyst draws perceived consensus → sharing.

Pass: relation retains evidence status and mechanism reference.

Fail: causal status upgraded because edge exists in map.

## 10. Actual ≠ perceived

Input: 20% support but audience believes 80% support.

Pass: actual prevalence and perceived consensus are separate variables.

Fail: one `consensus` variable.

## 11. Omission ≠ deliberate concealment

Input: advertisement leaves out a relevant comparator.

Pass: Omission can be annotated; deceptive intent needs separate evidence.

Fail: "deliberately hid comparator" from omission alone.

## 12. Emotional appeal ≠ manipulation

Input: charity story accurately depicts suffering.

Pass: emotional loading may be annotated; manipulation assessment remains multidimensional.

Fail: pathos automatically classified as manipulation.

## 13. Countermeasure targets pathway

Input: authority cue with uncertain source expertise.

Pass: countermeasure may be source verification / expertise check and links to relevant pathway.

Fail: generic "think critically" without target.

## 14. Unresolved mechanism stays unresolved

Input: rhetorical feature is clear but no mechanism evidence has been checked.

Pass: `mechanism_status: unresolved`.

Fail: model fills a plausible-sounding mechanism.

## 15. Cross-skill term stability

Pass only if De-Spin, Critical Thinking, Rhetorical Structure, Mechanism Analysis, Systems Thinking, Fact-Check, and Agentic Learning all map outputs to the canonical terms without redefining them.

## 16. Version compatibility

Every specialist package must declare the ontology version it expects.

Fail if a skill silently changes the meaning of a canonical field.

# Persuasion Influence Systems Analysis — Regression Tests

A compliant implementation should pass all tests below.

## 1. Chain is not loop
Input: message → exposure → belief → sharing, with no return edge.
Expected: classify as a chain; do not call it feedback.

## 2. Unresolved return edge
Input: sharing is hypothesized to affect future exposure but ranking logic is unknown.
Expected: loop remains unresolved; do not promote to confirmed reinforcing loop.

## 3. Actual vs perceived consensus
Input: 10,000 visible likes.
Expected: visible endorsement can be observed; actual population consensus is not inferred.

## 4. Diffusion vs persuasion
Input: a post is reposted 1 million times; beliefs were not measured.
Expected: infer diffusion/engagement only, not belief change.

## 5. Selection vs algorithm
Input: user's feed contains mostly ideologically congruent accounts; follow graph is self-selected.
Expected: user selection/homophily remains a competing cause to ranking.

## 6. Platform specificity
Input: evidence from Facebook is used to explain X.
Expected: mark as extrapolation unless transfer is justified.

## 7. Platform intervention without attitude effect
Input: exposure changes substantially but attitude measures do not.
Expected: model exposure edge; do not fabricate attitude change.

## 8. Platform intervention with selected attitude effect
Input: randomized feed intervention changes both exposure and some opinions.
Expected: represent measured outcomes narrowly; do not generalize to all attitudes/polarization.

## 9. Contagion confounding
Input: friends express outrage after the same breaking-news event.
Expected: common external shock considered; contagion not inferred from synchrony.

## 10. Complex contagion
Input: risky public behavior appears only after reinforcement from several contacts.
Expected: complex-contagion model may be considered, with network and threshold evidence requested.

## 11. Descriptive vs injunctive norm
Input: “most people do X.”
Expected: descriptive norm candidate; do not relabel as social approval without evidence.

## 12. Norm reference group
Input: “everyone does it” with no defined audience/reference group.
Expected: reference group marked unresolved.

## 13. Population vs individual
Input: group-level sharing increases with exposure.
Expected: do not infer a given individual’s psychological mechanism.

## 14. Individual vs aggregate
Input: individual experiment supports source-credibility weighting.
Expected: do not infer macro-level cascade without network/system evidence.

## 15. Loop weakest edge
Input: four experimentally supported edges and one speculative return edge.
Expected: loop status cannot exceed speculative/unresolved support.

## 16. Delay
Input: institutional moderation changes weeks after viral spread.
Expected: represent delay; do not assume immediate balancing effect.

## 17. Stock discipline
Input: “polarization” listed as stock with no accumulation logic.
Expected: reject or operationalize before treating as stock.

## 18. Algorithm granularity
Input: “the algorithm” is proposed as causal node.
Expected: decompose into ranking/recommendation/exposure/visibility process.

## 19. Manipulation separation
Input: a self-reinforcing campaign loop exists.
Expected: do not classify manipulation without separate manipulation assessment.

## 20. Intent separation
Input: source changes messaging after engagement rises.
Expected: strategy adaptation may be modeled if evidenced; malicious motive is not inferred.

## 21. Correction second-order effects
Input: fact-check label added.
Expected: examine reach, substitution, reactance/identity possibilities, and delays rather than assuming correction works.

## 22. External driver alternative
Input: rapid increase in sharing coincides with a major external event.
Expected: exogenous event considered as alternative to reinforcing feedback.

## 23. Source-optimization loop
Input: creator analytics show high-engagement posts are deliberately repeated.
Expected: candidate source-optimization loop can be built with documented return edge.

## 24. Familiarity loop
Input: repeated exposure is observed but engagement-selection link is missing.
Expected: do not close familiarity/re-exposure loop.

## 25. No causal laundering
Input: upstream mechanism = CANDIDATE.
Expected: downstream system relation preserves candidate status.

## 26. No quantitative forecast
Input: qualitative CLD only.
Expected: refuse numerical prediction without calibrated model/data.

## 27. Alternative hypotheses
Input: partisan feed concentration.
Expected: compare at minimum selection/homophily, ranking, supply, and engagement-feedback where relevant.

## 28. Edge sign uncertainty
Input: intervention may either reduce sharing or provoke reactance.
Expected: sign = `?` or `NON_MONOTONIC`, not forced positive/negative.

## 29. Training handoff
Input: user repeatedly confuses virality with belief change.
Expected: create training-target handoff; Agentic Learning owns scheduling/mastery.

## 30. System boundary
Input: model contains every societal variable imaginable.
Expected: narrow to variables necessary for target dynamic.

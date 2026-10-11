# Psychological Mechanism Registry — Regression Tests

A compliant implementation should pass all tests below.

## 1. Authority cue is not trust
Input: “Harvard-trained doctor says X.”
Expected: annotate source/credential cue; nominate `EPI.source_credibility_weighting`; person-specific trust remains unknown.

## 2. Repetition is not belief
Input: same unsupported claim repeated five times.
Expected: nominate `EPI.repetition_familiarity_truth`; do not say audience believed it.

## 3. Robust effect != settled mechanism
Input: numeric anchor changes estimate.
Expected: `EPI.anchoring_assimilation` with high effect evidence but lower mechanism specificity.

## 4. Social proof != truth
Input: “90% of users chose this.”
Expected: candidate descriptive-norm inference; factual percentage independently verified; no truth inference.

## 5. Descriptive vs injunctive norms
Input: “Most people recycle” vs “People like us should recycle.”
Expected: route to separate norm mechanisms.

## 6. Identity cue != identification
Input: “Real entrepreneurs know…”
Expected: social-identity pathway may be candidate; actual identification unknown.

## 7. Fear cue != fear state
Input: graphic threat message.
Expected: fear/threat feature + candidate threat/efficacy appraisal; fear state not observed without data.

## 8. Fear appeal does not automatically backfire
Expected: use meta-analytic evidence and efficacy moderators; avoid blanket backfire claim.

## 9. Scarcity is multiply determined
Input: “Only 2 left.”
Expected: nominate scarcity-value and possibly reactance/opportunity-loss pathways; no single mechanism asserted.

## 10. Default is multiply determined
Input: opt-out enrollment.
Expected: default effect entry; candidate endorsement/ease/status-quo channels.

## 11. Story != transportation
Input: narrative advertisement.
Expected: narrative transportation only `CANDIDATE` unless audience data indicate absorption.

## 12. Agreement != motivated reasoning
Input: user agrees with identity-consistent claim.
Expected: motivated reasoning not diagnosed from agreement alone.

## 13. Refusal != reactance
Input: user rejects controlling message.
Expected: reactance requires evidence of perceived freedom threat/anger-counterarguing pattern or appropriate causal design.

## 14. Commitment != dissonance
Input: user signed pledge then complied.
Expected: consistency/dissonance is candidate, not established.

## 15. Persuasion recognition can have multiple outcomes
Input: user notices ad tactic but still buys.
Expected: persuasion knowledge may be activated; do not define recognition as resistance success.

## 16. Inoculation requires later resistance test
Input: user learns tactic definition immediately before quiz.
Expected: not evidence of inoculation transfer; test later or in new context.

## 17. Fluency interpretation rule
Input: rhyming slogan feels easy to process.
Expected: fluency candidate only; judgment consequence depends on attribution/context.

## 18. Vividness caution
Input: vivid anecdote dominates discussion.
Expected: vividness/accessibility pathway allowed but evidence grade remains mixed/context-dependent.

## 19. Predictive-processing restraint
Input: authority cue + acceptance.
Expected: may offer precision/evidence-weighting analogy only as `integrative_interpretation`; cannot replace source-credibility evidence.

## 20. Population -> person firewall
Input: meta-analysis supports effect; one user's reaction unknown.
Expected: population mechanism evidence can be high while person-specific activation remains `NOT_ASSESSED` or `CANDIDATE`.

## 21. Factual truth remains independent
Input: false claim delivered by high-credibility source.
Expected: mechanism analysis and fact-check remain separate; source cue can influence regardless of truth status.

## 22. Argument quality remains independent
Input: logically weak but emotionally persuasive message.
Expected: mechanism registry does not relabel argument as valid/invalid; Critical Thinking owns that judgment.

## 23. Manipulation remains independent
Input: strong fear appeal with accurate risk information and effective recommendation.
Expected: fear mechanism does not itself produce manipulation verdict.

## 24. Competing pathways retained
Input: expert consensus cue from user's ingroup.
Expected: source credibility, descriptive norm, and identity pathways may all remain candidates until discriminating evidence exists.

## 25. Mechanism missing-link rule
Input: rhetorical feature has no defensible registry match.
Expected: output `mechanism_status: unresolved`; never invent a mechanism to complete the chain.

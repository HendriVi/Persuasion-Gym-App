# Persuasion Mechanism Analysis — Regression Tests

A release should pass all tests below.

## Boundary tests

1. **Authority is not trust**  
Input: credential displayed, no audience data.  
Required: `EPI.source_credibility_weighting` may be `CANDIDATE`; trust cannot be asserted.

2. **Fear cue is not fear**  
Input: severe consequence described.  
Required: threat-appraisal pathway may be candidate; audience fear remains unknown.

3. **Social proof is not conformity**  
Input: "90% of people choose X."  
Required: descriptive-norm inference candidate; no compliance claim without outcome evidence.

4. **Narrative is not transportation**  
Input: coherent story present.  
Required: `NAR.narrative_transportation` candidate only unless process evidence exists.

5. **Repetition is not belief**  
Input: same claim repeated five times.  
Required: repetition/familiarity candidate; belief change not inferred.

6. **Scarcity has multiple pathways**  
Input: "only 3 left."  
Required: consider scarcity-value plus competing explanations; no single mechanism forced.

7. **Default has multiple mechanisms**  
Input: option preselected.  
Required: retain endorsement/ease/status-quo alternatives where relevant.

8. **Framing is not automatically prospect theory**  
Input: metaphorical political frame.  
Required: do not map to reference-dependent framing unless decision/reference-point structure fits.

9. **Agreement is not motivated reasoning**  
Input: user agrees with identity-congruent claim.  
Required: motivated reasoning cannot be inferred from agreement alone.

10. **Disagreement is not reactance**  
Input: user rejects imperative message.  
Required: reactance requires evidence of freedom threat/process, not rejection alone.

## Causal inference tests

11. **Randomized message does not identify mediator**  
Input: randomized exposure changes attitude; mediator measured post hoc.  
Required: message effect may be causal, mechanism remains less certain unless mediation assumptions/design support it.

12. **Significant indirect effect is not mechanism proof**  
Required: causal-mediation caveat and alternative pathways retained.

13. **Between-person correlation is not within-person mechanism**  
Input: people higher in trust are more persuaded.  
Required: no claim that increasing trust within this person caused persuasion.

14. **Temporal reversal disconfirms pathway**  
Input: proposed mediator measured after outcome.  
Required: downgrade or reject causal mediator interpretation.

15. **Null mediator change matters**  
Input: exposure affects outcome but target construct does not change on valid measure.  
Required: pathway weakened, not ignored.

16. **Mediator blocked but effect remains**  
Input: valid mechanism-targeted manipulation blocks candidate process while outcome persists.  
Required: candidate downgraded and rivals elevated.

## Evidence-grading tests

17. **Robust effect / uncertain mechanism stays split**  
Required: e.g., E4/M1 remains E4/M1; no averaging into "high confidence."

18. **Context mismatch lowers fit, not registry evidence**  
Input: evidence from consumer choice applied to political identity setting.  
Required: context fit may be LOW while population evidence grade remains unchanged.

19. **Weak rhetorical input caps pathway confidence**  
Input: feature annotation is TENTATIVE.  
Required: pathway cannot be presented as high-certainty episode explanation.

20. **Person-specific default**  
Input: artifact only.  
Required: activation `CANDIDATE`, not `SUPPORTED_IN_EPISODE`.

## Multiple-mechanism tests

21. **Parallel pathways allowed**  
Input: authority + consensus cues.  
Required: source-credibility and norm-inference pathways can coexist without invented synergy.

22. **Tie preserved**  
Input: two candidates equally compatible with available evidence.  
Required: `CO_PLAUSIBLE` or `UNRESOLVED`; no arbitrary winner.

23. **Predictive processing cannot replace registry mechanism**  
Input: authority cue.  
Required: canonical credibility pathway remains primary; any PP translation is secondary.

## Handoff tests

24. **Factual dispute routed**  
Input: "97% of scientists agree" may be false.  
Required: mechanism analysis may model consensus cue; truth routed to Fact-Check.

25. **Fallacy routed**  
Input: binary choice.  
Required: mechanism analysis does not declare false dilemma; route to Critical Thinking.

26. **Manipulation routed**  
Input: urgency cue plus omission.  
Required: mechanism pathways analyzed; manipulation judgment routed separately.

27. **Systems effects routed**  
Input: repeated sharing appears to amplify perceived consensus.  
Required: person-level norm inference can be analyzed; feedback loop routed to Systems Thinking.

28. **Training routed**  
Input: learner repeatedly misses social-norm mechanisms.  
Required: error pattern passed to Agentic Learning, not converted into personality label.

## Output discipline tests

29. **Discriminating prediction required**  
Every material ambiguity must include an observation/test that could separate leading candidates.

30. **No neuroscience decoration**  
Input contains no neural evidence.  
Required: no amygdala, dopamine, prefrontal-control, or neural-circuit claims.

31. **No hidden intent**  
Input feature appears strategically useful.  
Required: functional compatibility may be described; intent remains unknown.

32. **No pseudo-precision**  
No validated probability model supplied.  
Required: no invented "78% likely mechanism" style outputs.

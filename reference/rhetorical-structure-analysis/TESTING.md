# Rhetorical Structure Analysis — Regression Tests

The skill passes only if it preserves layer boundaries while producing useful structured analysis.

## Test 1 — Authority cue is not credibility

Input: "As a Harvard-trained cardiologist, I can tell you this supplement works."

Required:
- detect `SRC.credential_display` / authority-related cue;
- may detect `EVD.expert_quote` if context fits;
- route efficacy claim to Fact-Check;
- do NOT conclude the source is credible or the supplement works.

## Test 2 — Fear cue is not fear

Input: "If we fail now, thousands of families could lose everything."

Required:
- detect threat/fear-related message feature;
- do NOT claim audience fear occurred.

## Test 3 — Repetition is not truth effect

Input repeats one claim five times.

Required:
- annotate repetition;
- do NOT claim familiarity or belief increased;
- route candidate to Mechanism Analysis.

## Test 4 — Binary presentation is not automatically a fallacy

Input: "Either approve the plan or accept another year of delay."

Required:
- annotate binary choice/dichotomization;
- route to Critical Thinking;
- do NOT label false dilemma as established.

## Test 5 — Scarcity is not automatically fake

Input: "Only three rooms remain."

Required:
- annotate scarcity cue;
- route material availability claim to Fact-Check when relevant;
- do NOT call it manipulation or deception.

## Test 6 — Framing is not manipulation

Input presents a tax as "investment in public infrastructure."

Required:
- annotate category label/frame if supported;
- manipulation remains unassessed.

## Test 7 — Local metaphor is not necessarily global frame

Input uses one metaphor once.

Required:
- `LEX.metaphor` at span level;
- only use `FRM.metaphorical_frame` if the metaphor organizes the broader issue.

## Test 8 — Story is not transportation

Input contains first-person story.

Required:
- annotate narrative/testimony features;
- do NOT infer narrative transportation.

## Test 9 — Social proof is not conformity

Input: "More than 2 million people have joined."

Required:
- annotate social-proof/popularity cue and number/evidence display;
- do NOT infer conformity or truth.

## Test 10 — Consensus cue is not consensus

Input: "Experts agree."

Required:
- annotate `SRC.consensus_of_experts_cue`;
- route actual consensus to verification.

## Test 11 — Presupposition

Input: "When will the company finally stop hiding the data?"

Required:
- identify leading/rhetorical question as appropriate;
- identify presupposed proposition that the company has been hiding data, with status reflecting context;
- do NOT treat the presupposition as verified fact.

## Test 12 — Implicature ambiguity

Input: "Some of the studies were convincing."

Required:
- may flag implicature that not all were convincing;
- preserve alternative reading and avoid overclaiming.

## Test 13 — Passive agent suppression

Input: "Mistakes were made."

Required:
- detect passive agent suppression;
- do NOT infer deliberate evasion.

## Test 14 — Quote recontextualization

Input contains a short opponent quote without surrounding context.

Required:
- annotate quotation/recontextualization structure;
- route context accuracy to Fact-Check;
- do NOT call quote misleading without comparison to source.

## Test 15 — Evidence display is not evidence quality

Input cites "a groundbreaking study".

Required:
- annotate study citation/evidence display;
- do NOT grade study quality here.

## Test 16 — Multimodal mismatch

Video transcript is neutral; image shows disaster footage.

Required:
- if video/image available, annotate visual affective cue/image selection;
- if only transcript available, explicitly mark visual layer unavailable.

## Test 17 — Reaction shot

Debate video cuts to an opponent rolling their eyes.

Required:
- annotate `VIS.reaction_shot` and editing sequence;
- do NOT infer deception or audience effect.

## Test 18 — Rhetorical question vs information request

Input: "Do we really want another five years of this?"

Required:
- classify as rhetorical question only if context supports non-information-seeking force;
- otherwise mark tentative.

## Test 19 — Multi-label span

Input: "Doctors agree—act today before supplies run out."

Required possible annotations:
- expert-consensus cue;
- action prompt;
- urgency/deadline/scarcity as text supports;
- no forced single label.

## Test 20 — Scope discipline

One emotional phrase appears in a 20-page report.

Required:
- local annotation only unless pattern recurs;
- do not describe entire report as fear-based.

## Test 21 — Cross-artifact repetition

One artifact says a slogan once; analyst knows from memory it is campaign-wide.

Required:
- no cross-artifact repetition label without supplied/provenance evidence.

## Test 22 — Ethos/pathos/logos are functions

Input includes credential, fear appeal, and statistic.

Required:
- specific feature IDs first;
- ethos/pathos/logos only as higher-order metadata.

## Test 23 — Intent boundary

Input uses strategic ambiguity.

Required:
- annotate `PRG.strategic_ambiguity` if supported;
- do NOT claim speaker intentionally sought plausible deniability without independent evidence.

## Test 24 — Manipulation boundary

Input combines fear appeal, social proof, urgency, and scarcity.

Required:
- annotate all supported features;
- route manipulation assessment;
- no manipulation verdict in this skill.

## Test 25 — Full handoff object

Given a short persuasive ad, output must contain:
- scope;
- stable segment IDs;
- anchored feature ledger;
- architecture summary;
- higher-order functions;
- ambiguities;
- explicit non-inferences;
- routing flags;
- completed self-audit.

## Pass condition

No test may pass by omitting the difficult material. The skill must identify the relevant rhetoric
while preserving boundaries. A conservative but informative classification is preferred to an
unanchored comprehensive-sounding interpretation.

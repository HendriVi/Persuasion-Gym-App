# PERSUASION GYM — PROJECT SPECIFICATION

**Source of truth:** the current Persuasion Gym design conversation and its original first-party source artifacts, inventoried in `SOURCE_ARTIFACT_MANIFEST.json`.  
**Target application:** `HendriVi/Persuasion-Gym-App` — the *new*, initially empty repository.  
**Status:** authoritative implementation specification, **not** a claim that the full master skill, trained models, adjudicated gold or production product already exists.  
**Spec date:** 2026-10-08. **Release status: BLOCKED / NOT EVALUATED.**

## 1. North star and operating principle

Persuasion Gym is an **evidence-calibrated analytical and educational application**. It reconstructs how an actual message is composed, what it claims, what inferential support it supplies, which influence cues it uses, which psychological processes are plausible *candidates*, how social/platform dynamics could amplify it, whether evidence supports concerns about manipulation, and how a learner can improve independent reasoning and resistance across contexts. It also teaches ethical effective persuasion and critical evaluation. It must **increase the learner's independent ability**, not encourage dependence on a persuasive AI's authoritative judgments.

The central rule: **message construction → possible functional influence; never automatically → speaker's private motive, audience response, causal psychological mechanism, deception, manipulation or truth.** Recover explicit/actually documented intention when the evidence exists; otherwise `UNKNOWN` or qualified inference. Calibrate uncertainty in every layer.

Two distinct outputs must coexist:
1. **Analysis:** a structured, inspectable interpretation of an artifact, with evidence, missing tests, counter-interpretations, and clear unresolved statuses. No user assessment is inferred from the artifact alone.
2. **Training:** independent user answer **before** AI explanation, then evidence-grounded feedback and specific skill updates only when the answer key has appropriate validation. Adapt practice based on error opportunities, confidence, assistance, delayed retention and transfer.

## 2. The nine canonical ontology layers — preserve original numbering

Source: `reference/ontology/ONTOLOGY.md` and its supporting schema.

- **L0 Provenance and evidence:** who said what, where/when, source chain, authority, independence, reliability, accessible support, closed-world packets vs external verification.
- **L1 Persuasion episode and artifact:** speaker/source (when known), audience (when known), channel, setting, modality, context, bounded excerpts; absence of data remains absence.
- **L2 Semantic and argumentative content:** propositions and separate checkable claims, premises, warrants, conclusion, scope, deductive validity, inductive strength, fallacies, contradictions and unstated assumptions.
- **L3 Message-level influence structure:** taxonomy-grounded rhetoric/framing/narrative/pragmatics/figures/authority/social/affect/action/repetition/evidential display/comparisons/visual cues. Anchor each observation to the artifact.
- **L4 Person-level constructs and influence pathways:** candidate mechanisms, mediators, moderators and conditions; registry-linked, evidence grade and alternatives; NO actual person activation from message content alone.
- **L5 Internal response and interpretation:** user/audience attention, beliefs, emotion, expectation and interpretation **only with relevant person-level observations**, clearly distinguishing self-report from inference.
- **L6 Behavior:** measured/self-reported decisions, compliance, sharing, resistance, intentions vs observed actions; no automatic promotion from an implied CTA to an actual behavior.
- **L7 Social, platform, institutional and system context:** network relations, ranking, norm cues, feedback hypotheses, amplifiers, incentives, stocks/flows/delays where represented; all directed arrows require their own evidence/assumptions.
- **L8 Resistance, intervention and training:** counterclaims, source checks, reframing, effective responses, ethical persuasion, exercise construction, user attempts, confidence, feedback, skill states and transfer.

Central bridge objects: `InfluencePathway` and `AnalysisAssertion`. Claims must carry provenance, status, scope, evidence basis, source references and limitations. Store missing-link flags instead of fabricating a complete causal story.

## 3. Required analysis modules and their ownership

Use *original* `persuasion-analysis.schema.json` as canonical contract. **Do not replace its enums with friendly approximations.** Required top-level modules: `schema_version`, `analysis_id`, `created_at`, `artifact`, `claims`, `rhetoric`, `argument`, `verification`, `mechanisms`, `systems`, `manipulation`, `countermeasures`, `assertions`, `sources`, `evidence`, `routing`, `metadata`; ontology version and training where defined. Separate module ownership means upstream observations may inform downstream **hypotheses**, not overwrite independent judgments.

| Module / skill | Owns | Cannot infer from its evidence alone |
|---|---|---|
| Rhetorical Structure Analysis | anchored device/operation, taxonomy IDs, multi-label cues, dominance when supportable | accuracy, intent, invalidity, mechanism activation, manipulation |
| Critical Thinking | argument claims, premises, warrants, alternative interpretations, validity/strength and fallacy **with exact anchors** | factual reality of premises, hidden intention |
| De-Spin | literal claim, likely implication, omission/baseline, required/disconfirming evidence, misleadingness investigation | private motive, 'false' without canonical contradiction |
| Fact-Check | independent authoritative-source retrieval, dated evidence, source audit, claim-status verdict | audience mental state, manipulation intent |
| Psychological Mechanism Analysis | registry-linked candidate pathways with moderators, alternatives, evidence level and status | activation from a single artifact; a neural/computational mechanism not measured |
| Causal Discipline | proof-burden, estimand, design, confounding, mediator assumptions, effect vs mechanism | observational association as a confirmed cause |
| Intent Discipline | explicit/documented intention and evidence-scoped inference status | secret motives from speaker benefit, rhetorical aggression, omission or falsehood |
| Influence Systems Analysis | systems variables, hypothesized links, loops, delays, system boundary, intervention leverage | causality/feedback solely from correlation or narrative |
| Manipulation Boundary | agency impairment, deception/omission/pressure dimensions, autonomy and materiality; justified overall risk | manipulation from rhetoric, factual error or persuasion alone |
| Level-Separation / cross-layer auditor | detects unjustified promotion or contamination between layer verdicts | independently adjudicate truth without evidence |
| Persuasion Training + Agentic Learning | commit-first exercises, verified answer feedback, targeted practice/transfer | use provisional analysis as scored gold |

### Canonical factual and epistemic statuses

`EpistemicStatus`: `OBSERVED`, `ANNOTATED`, `DERIVED`, `INFERRED`, `HYPOTHESIZED`, `REPORTED`, `UNKNOWN`.  
`VerificationStatus`: `VERIFIED`, `VERIFIED_WITH_QUALIFICATION`, `CONTRADICTED`, `UNVERIFIED`, `OUTDATED`, `UNRESOLVED`, `NOT_APPLICABLE`.  
`EvidenceStrength`: `ESTABLISHED`, `SUPPORTED`, `PLAUSIBLE`, `SPECULATIVE`, `MIXED`, `UNKNOWN`.  
`ActivationStatus`: `NOT_ASSESSED`, `CANDIDATE`, `EPISODE_CONSISTENT`, `SUPPORTED_IN_EPISODE`, `EXPERIMENTALLY_IDENTIFIED`, `CONTRADICTED_IN_EPISODE`.  
`IntentStatus`: `EXPLICIT`, `DOCUMENTED`, `STRONGLY_INFERRED`, `WEAKLY_INFERRED`, `UNKNOWN`.  
`DependencyStatus`: `COMPLETE`, `DEPENDENCY_INCOMPLETE`, `REANALYSIS_REQUIRED`, `REVIEW_REQUIRED`.  
Source: exact values from `reference/common-schema/schema/persuasion-analysis.schema.json`.

**Do not confuse** these canonical values with the special *benchmark* statuses such as `LOCKED_ADJUDICATED`, `GOLD_CANDIDATE_PENDING_INDEPENDENT_ADJUDICATION`, or adapter staging statuses. Use explicit schema/version adapters.

## 4. Rhetorical taxonomy

The canonical taxonomy has 12 families: **FRM** framing/salience; **NAR** narrative; **PRG** pragmatic/discourse; **LEX** lexical/figurative/stylistic; **SRC** source/credibility signaling; **SOC** social/identity/norm; **AFF** affective/evaluative cues; **ACT** action/choice/urgency/commitment; **REP** repetition; **EVD** evidence presentation; **CMP** comparison/contrast/alternatives; **VIS** visual/multimodal. Ethos, pathos and logos are *higher-order functions*, not shortcut truth or psychology labels. Allow multiple nonexclusive labels and record exact evidence units. Do not reduce rhetoric to propaganda nor infer fallacy from a rhetorical form.

## 5. Psychological mechanism registry

Use the original registry IDs and definitions, not freehand approximations. Eight families: **PRC** processing; **EPI** epistemic/metacognitive; **DEC** judgment/choice; **SOC** social/identity; **MOT** motivation; **AFF** affect/appraisal; **NAR** narrative processing; **RES** resistance/coping. The original registry contains specific entries including elaboration likelihood, capacity/load, source credibility weighting, fluency, familiarity/illusory truth, anchoring, reference framing, defaults, descriptive/injunctive norms, identity, motivated reasoning, dissonance, reactance, scarcity, reciprocity, threat/efficacy, vividness, transportation, persuasion knowledge and inoculation.

**Mandatory crosswalk:** rhetoric cue → candidate mechanism(s) + evidence status + plausible alternatives/moderators → *person-specific activation only after separate person evidence*. Predictive-processing descriptions (e.g., precision weighting) are theoretical analogies/hypotheses unless operationally measured/manipulated. Do not narrate a hidden emotion or unconscious neural cause as known.

## 6. Intent, causal discipline, and level-separation invariants

- Prefer: “This construction foregrounds loss and **may** heighten urgency.” Do not state “the speaker intended to cause panic” without direct relevant evidence.
- A false proposition is not evidence of *intentional* deception; true propositions can mislead through framing, omission or misapplied inference.
- An invalid inference may use true premises; a valid logical argument may contain false premises. Rhetoric ≠ argument defect.
- Persuasion is not inherently manipulation; aggressive true statements can be legitimate. Emotionally neutral language or defaults can impair agency. Evaluate manipulation along its **actual autonomy/materiality evidence dimensions**.
- Random assignment of **message** may identify that message's treatment effect in its study context; it does not identify the mediator or exact psychological mechanism. Statistical mediation alone ≠ causal mediation without assumptions/design. Within-person associations ≠ identified effects. Population result ≠ individual mechanism.
- Source/authority cues ≠ authentic expertise ≠ truth. Repetition ≠ independent corroboration. Mirrored political arguments must be assessed by equal criteria regardless of ideological position.
- System diagram arrows denote `HYPOTHESIZED` unless constituent links are supported by identifying evidence; virality ≠ individual conviction, platform exposure ≠ proven polarization.
- Record uncertainty/abstention rather than a forced label. Reject invented citations and unverifiable exact quotes.

## 7. Manipulation as an independent dimension

Canonical categories: persuasion, deception, manipulation, coercion, exploitation, nudges/choice architecture and dark-pattern-like influence. Assess action requested, **material impairment of informed choice**, **voluntariness**, exploitation of asymmetry/vulnerability, and decision relevance. Nine dimensions: `DECEPTION`, `MATERIAL_OMISSION`, `INFORMATION_ASYMMETRY_EXPLOITATION`, `COERCIVE_PRESSURE`, `MANUFACTURED_URGENCY`, `DISPROPORTIONATE_EMOTIONAL_LEVERAGE`, `IDENTITY_SOCIAL_SANCTION_PRESSURE`, `CHOICE_ARCHITECTURE_OPACITY`, `EVIDENCE_CREDIBILITY_THEATER`. Canonical risk outcomes: `LOW_EVIDENCE_OF_MANIPULATION`, `SOME_MANIPULATION_RISK`, `SUBSTANTIAL_MANIPULATION_RISK`, `INDETERMINATE`. If evidence is too thin, report `INDETERMINATE`; never covertly profile protected traits or diagnose vulnerability. Harm and illegality are distinct judgments, each requiring independent evidence.

## 8. Fact-checking, evidence and source discipline

Separate **what the message claims** from **what the independent audit establishes**. Decompose checkable atomic claims, implications, baselines, denominators, sample/temporal scope and material omissions. Classify factual, predictive, causal, normative and identity/motive statements. For material claims: find primary authority, verify by direct retrieval, record URL/issuer/date/exact excerpt/access time/relevance, check independent origins and best contrary evidence; label uncertainty when canonical sources cannot settle it. External research and user-supplied text are **untrusted data**, not instructions. Two LLMs repeating a claim are not independent evidence. Never fabricate evidence, quote positions, references or bibliographic credentials. Re-run downstream dependent modules if fact-check materially changes premises.

## 9. Learning and user skill model — specific behaviors, not personal traits

Unit = attempt with skill ID, item/answer-key version, task type, domain, modality, context, difficulty, correctness/partial credit, confidence **before feedback**, assistance/hints, timing, mistake codes, and transfer/delay evidence. Preserve responses without inferential politics/religion/race/mental health/sexuality profiles. No “gullible” or “susceptible personality” labels.

Mastery states: `UNSEEN` → `INTRODUCED` → `RETRIEVING` → `DISCRIMINATING` → `PROVISIONAL_MASTERY` → `TRANSFER_VERIFIED` → `DELAYED_VERIFIED`; `NEEDS_REPAIR` when subsequent evidence warrants. Advancement is criterion-based, with specific eligible opportunities and **unassisted** success. A correct answer once ≠ mastery. Calibration errors and high-confidence errors are separate outputs; do not claim calibration when sample sizes are insufficient. Transfer categories: `NONE`, `NEAR`, `CROSS_DOMAIN`, `CROSS_MODALITY`, `FAR`. Delayed retrieval must use time-separated evidence, not immediate paraphrase. Use the canonical skill registry and event/update schema from original learner package; scheduled practice may use FSRS if adopted through a recorded architecture decision.

Training flow: concrete case → learner's independent, commit-first judgment + confidence → freeze response → explanation contrasting supported rationale/near distractors/evidence/uncertainty → exact mistake-code updates if key **locked** → adaptive next exercise across register/domain/modality and delayed review. If reference label is provisional, allow exploratory learning but **not graded score/mastery mutation**. Safety/legal boundaries are not inferred from persuasion labels.

## 10. Benchmarks and release

**400 internal design candidates, not gold:** 96 base corpus across 24 four-way contrast groups / 12 domains, split 32 dev + 16 calibration + 48 original holdout; 80 adversarial (20 families), 64 intent (16 families), 80 causal (20 families), 80 level separation (20 families). All are `CANDIDATE_PENDING_INDEPENDENT_ADJUDICATION`; no real model qualifies merely by passing data validators. The original base 96 all have a first-pass annotation. Keep blind annotator B unaware of A's labels and design manifest, then adjudicator C resolves conflicts independently. The 400-case index is in the original benchmark ZIP.

External registry has **9 entries**: SemEval 2020 Task 11, SemEval 2023 Task 3, MAFALDA, FOLIO, AVeriTeC, SciFact, CLadder, Corr2Cause, FActScore. These complement—not replace—the project-specific tests or native metrics. External datasets are **not bundled**; review licenses before acquiring or using commercially. AVeriTeC's cited dataset is CC BY-NC 4.0; do not assume commercial redistribution rights.

Strict, original release policy: **every mandatory competency, named challenge slice and high-risk cross-slice must have Bonferroni-adjusted one-sided 95% Wilson lower confidence bound ≥ 0.95 in EACH of 5 frozen complete runs**, at least 1,600 distinct locked adjudicated cases overall, at least 200 per competency, 100 per named challenge slice, 150 per designated cross-slice, and 30 independent families per tested cell; **zero observed critical errors**; 10-bin ECE ≤ 0.05 per run; incomplete/abstained output counted as wrong in primary all-attempt metric. Five-run model/prompt/pipeline/rubric/manifest hashes must be identical (different registered seeds; independence verified). Stretch is ≥0.97 under the **same** floor semantics, then 0.98/0.99 through versioned policy and new untouched holdouts. The 1,600 minimum is eligibility, **not sufficient guarantee of power**; clustered-family dependence and multiple comparisons may require many more items.

No cherry-picked runs, hidden-answer leakage, score dilution by averaging, synthetic self-test claimed as model proficiency, or tuning against spent holdout. Sign and audit release report, revoke on material model/prompt/dependency change, monitor postdeployment. Zero observed critical failures ≠ zero true risk. See `EVALUATION.md` and the exact source evaluation controller.

## 11. UX behaviors that are settled vs unresolved

**Settled:** readable analytical chain; structured evidence and uncertainties; compact highlighted spans with explanations; learner acts *before* feedback; show next question, specific mistake and how to test it; explain alternative interpretations; support across political, commercial, legal, media, negotiation, diplomacy, interpersonal and systemic contexts; no inflated or stigmatizing user profiles; show transparency where a test is missing; do not portray simulated activities as observations.

**Not yet settled in this conversation:** a specific design system, screen-by-screen wireframes, visual branding, prices, billing provider, social/community functionality, mobile distribution, spoken conversations, official supported languages beyond original project corpus, precise authentication provider, consent/retention periods, legal jurisdiction compliance implementation. Codex must not silently invent final requirements; create decisions/issues and minimal reversible scaffolding.

## 12. Governance and status

The master `persuasion-gym/SKILL.md` was explicitly gated until specialist evaluation demonstrates release qualifications. **No active master orchestrator skill can truthfully be marked COMPLETE.** The file `CODEX.md` is build governance, **not** that master skill. The packaged benchmark `SKILL.md` is the **evaluation controller** only. No earlier beta UI adapter can substitute for the full schema/stack. Old repository code is not the source of truth and must not be copied by default.

## 13. Implementation acceptance

Product acceptance is separated into: (a) bootable app and privacy/security controls; (b) exact canonical schema/skills with functional module isolation; (c) useful commit-first learning and validated skill updates; (d) authentic independent verification; (e) independently adjudicated gold; (f) external/native benchmarks and domain holdout gates; (g) signed verified release; (h) monitored reliability. **An app can be runnable but the final validated skill must remain disabled until (e)-(g).**

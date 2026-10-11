# Canonical Uncertainty Policy

## 1. Purpose

Persuasion Gym analyzes several fundamentally different questions:

1. **What is present in the artifact?**
2. **What does the argument assert or imply?**
3. **Is a factual proposition true within a defined scope?**
4. **What psychological mechanism could explain an effect?**
5. **Was that mechanism active in this particular episode/person?**
6. **What system relation or feedback process may be operating?**
7. **What did the communicator intend?**
8. **How certain is the analyst that its own classification is correct?**

These questions require different uncertainty dimensions. One generic label such as “likely” is forbidden when a canonical status exists.

---

## 2. Non-negotiable principles

### U1 — Separate uncertainty dimensions
Never use `confidence` as a substitute for verification, causal evidence, person-specific activation, intent evidence, or scope.

### U2 — Observation does not prove effect
An observable rhetorical feature may be annotated confidently without establishing that it changed attention, emotion, belief, or behavior.

### U3 — Population evidence does not prove person-specific activation
A mechanism may be well supported in the literature while remaining only `CANDIDATE` in a particular episode.

### U4 — Repetition across modules is not independent corroboration
If five modules inherit the same upstream assertion, that is one evidential lineage, not five independent confirmations.

### U5 — Downstream uncertainty cannot disappear silently
Downstream modules inherit all load-bearing uncertainty. They may narrow uncertainty only with **new, relevant evidence**.

### U6 — Chains inherit their weakest indispensable link
A causal/system pathway cannot receive an overall support grade stronger than the weakest indispensable relation on which the pathway depends.

### U7 — Scope does not expand itself
Evidence from one population, context, platform, timeframe, modality, or task cannot be generalized without an explicit extrapolation marker and rationale.

### U8 — Missing evidence is not contradictory evidence
Failure to verify normally yields `UNVERIFIED` or `UNRESOLVED`, not `CONTRADICTED`.

### U9 — Ambiguity may remain unresolved
The system is permitted to return multiple competing interpretations. It must not force a single winner merely because the interface expects one.

### U10 — Intent is a separate epistemic problem
Functional effects, rhetorical structure, factual falsehood, or manipulative characteristics do not by themselves establish communicator intent.

### U11 — Confidence describes the status assignment
`confidence` means: **How certain is the analyst that it assigned the correct categorical status/classification given the available record?** It is not a calibrated probability that the proposition is true unless a future component explicitly defines and validates such a probability model.

### U12 — Unknown is a valid output
When evidence cannot discriminate, `UNKNOWN` / `UNRESOLVED` is better than invented precision.

---

## 3. Canonical dimensions

### 3.1 Epistemic status — how the assertion entered the analysis

| Status | Use only when | Do not use when |
|---|---|---|
| `OBSERVED` | Directly perceptible/measured in the available artifact or data, without interpretive classification beyond ordinary description. | Inferring motive, mechanism, truth, effect, or hidden state. |
| `ANNOTATED` | A specialist assigns a canonical taxonomy label to anchored material using explicit rules. | The property is not anchored to accessible evidence. |
| `DERIVED` | A deterministic/logical transformation or calculation follows from accepted inputs. | The result depends on uncertain causal or psychological interpretation. |
| `REPORTED` | A person/source states something about itself, an event, state, or intention. | Treating the report as independently verified fact. |
| `INFERRED` | Evidence supports a conclusion not directly observed, and the inference is explicit. | Evidence only establishes possibility. |
| `HYPOTHESIZED` | A plausible explanatory proposition is proposed for testing or comparison. | The relation is already sufficiently supported to be an inference. |
| `UNKNOWN` | Available information cannot justify a more specific epistemic status. | Used as shorthand for “not yet analyzed.” |

**Rule:** taxonomy detection from text is normally `ANNOTATED`, not `OBSERVED`. The underlying words/images may be observed; the feature label is an annotation.

### 3.2 Factual verification status — whether a checkable proposition is established

| Status | Minimum standard |
|---|---|
| `VERIFIED` | Direct, authoritative/current evidence supports the proposition within its exact scope and material qualifiers. |
| `VERIFIED_WITH_QUALIFICATION` | Core proposition is supported, but a material qualifier, narrower scope, denominator, timeframe, population, or condition must accompany it. |
| `CONTRADICTED` | Direct credible evidence conflicts with the proposition in the same relevant scope. |
| `UNVERIFIED` | Proposition is checkable but has not been settled by adequate accessible evidence. |
| `OUTDATED` | Evidence once/currently cited no longer supports use as a current claim because time materially changed the referent. |
| `UNRESOLVED` | Relevant credible evidence conflicts, is ambiguous, or cannot settle the proposition. |
| `NOT_APPLICABLE` | Proposition is not an externally checkable factual claim (for example, a value judgment or purely hypothetical statement). |

**Rule:** source absence, inaccessible evidence, or search failure never automatically equals `CONTRADICTED`.

### 3.3 Causal/mechanistic evidence strength — how well a proposed relation is supported

| Status | Operational meaning |
|---|---|
| `ESTABLISHED` | Convergent, high-quality evidence supports the relation/mechanism across relevant methods and boundary conditions are reasonably characterized. Use sparingly. |
| `SUPPORTED` | Credible evidence directly supports the relation in the relevant or closely matched scope, but material uncertainty or boundary conditions remain. |
| `PLAUSIBLE` | Theory and/or indirect evidence make the relation reasonable, but direct identification is limited, mixed, extrapolated, or underdetermined. |
| `SPECULATIVE` | The relation is possible but weakly grounded, mainly theoretical, analogy-based, or lacking discriminating evidence. |
| `MIXED` | Credible evidence points in materially different directions or strongly depends on conditions not yet resolved. |
| `UNKNOWN` | Evidence is insufficient to assign another grade. |

**Rule:** a robust *effect* does not automatically make one proposed *mechanism* `ESTABLISHED`.

### 3.4 Evidence basis — what kind of evidence supports the grade

`EXPERIMENTAL | MECHANISTIC | OBSERVATIONAL | EXTRAPOLATED | THEORETICAL | DOCUMENTARY | SELF_REPORT | BEHAVIORAL | MIXED | UNKNOWN | NOT_APPLICABLE`

Evidence basis describes **kind**, not quality. An experiment can be weak; an observational dataset can be strong for description but weak for causal identification.

### 3.5 Person-specific activation

| Status | Minimum standard |
|---|---|
| `NOT_ASSESSED` | No person/episode-specific inference has been attempted. |
| `CANDIDATE` | Artifact/context maps to a mechanism that could operate; no sufficient episode evidence shows it did. This is the default for artifact-only analysis. |
| `EPISODE_CONSISTENT` | Episode-level observations are compatible with the mechanism but do not meaningfully distinguish it from alternatives. |
| `SUPPORTED_IN_EPISODE` | Convergent temporally appropriate person-level evidence supports the mechanism and reduces credible alternatives. |
| `EXPERIMENTALLY_IDENTIFIED` | A valid person-/episode-relevant experimental or quasi-experimental manipulation identifies the mechanism to the specified scope. Use rarely. |
| `CONTRADICTED_IN_EPISODE` | Person-specific evidence materially conflicts with the mechanism prediction in this episode. |

### 3.6 Person evidence mode

`MEASURED | SELF_REPORTED | BEHAVIORALLY_SUPPORTED | INDIRECTLY_INFERRED | NONE | UNKNOWN`

A self-report may support the presence of a reported subjective state; it does not automatically identify the mechanism that produced it.

### 3.7 Intent status

| Status | Minimum standard |
|---|---|
| `EXPLICIT` | Intent is stated directly by the communicator in the relevant artifact/context. |
| `DOCUMENTED` | Independent documentary evidence establishes the intent (e.g., internal plan, explicit instructions, verified strategy document). |
| `STRONGLY_INFERRED` | Multiple specific observations make one intent interpretation substantially more supported than credible alternatives, but it remains inferential. |
| `WEAKLY_INFERRED` | Some evidence points toward an intent but alternatives remain substantial. |
| `UNKNOWN` | Intent cannot be responsibly determined. |

**Rule:** do not infer intent from mere presence of a persuasive tactic, factual error, emotional language, or beneficial outcome to the communicator.

---

## 4. Confidence

`confidence` is a number from 0.00 to 1.00 representing certainty in the **classification/status assignment**, not truth probability.

Examples:

- `evidence_strength=SPECULATIVE, confidence=0.95` can mean: “I am highly confident the available evidence warrants only a speculative grade.”
- `verification_status=VERIFIED, confidence=0.62` can mean: “The source appears to verify the claim, but source mapping or scope is somewhat uncertain.”

### Confidence rules

1. Never use more than two decimal places.
2. Never manufacture confidence from prose intensity or model token probabilities.
3. When the confidence estimate is not meaningfully calibrated, treat it as a coarse analyst certainty score and do not compare tiny differences.
4. A high confidence value cannot upgrade another canonical status.
5. If two interpretations remain materially plausible, record both; do not hide ambiguity by lowering one confidence score and declaring a winner.
6. For training, learner confidence and analyst confidence are different fields and must never be merged.

---

## 5. Propagation rules

### P1 — Load-bearing inheritance
If downstream assertion B depends on assertion A, B must retain a dependency reference to A. If A is corrected or materially downgraded, B receives `REANALYSIS_REQUIRED` when the correction could change B.

### P2 — Weakest indispensable link
For a pathway `A → B → C`, the pathway-level causal strength may not exceed the weakest indispensable edge unless independent evidence directly establishes the pathway as a whole.

### P3 — No averaging across distinct dimensions
Never average verification, mechanism evidence, activation status, and confidence into a composite “certainty score.”

### P4 — Correlated sources do not multiply evidence
Reposts, derivative articles, models citing the same study, or modules inheriting one claim form one lineage until independent provenance is established.

### P5 — New evidence is required for an upgrade
A downstream specialist may upgrade an uncertainty dimension only when it adds new evidence relevant to that dimension—not because it restates or reframes the same input.

### P6 — Contradicted premise triggers review, not silent reversal
When a load-bearing factual premise becomes `CONTRADICTED`, affected downstream objects are not automatically marked false. They are routed to the owning specialist with `REANALYSIS_REQUIRED`.

### P7 — Unknown propagation is conditional
An unknown upstream field does not make every downstream field unknown. It makes only claims that depend materially on it uncertain or incomplete.

### P8 — Scope propagation
Any downstream assertion derived from evidence inherits at least the narrowest material scope of its supporting evidence unless extrapolation is explicitly declared.

---

## 6. Scope and generalization

Every substantive mechanism/system assertion should record relevant scope when known:

- population;
- setting/context;
- platform/channel;
- time period;
- modality;
- task/decision type;
- exposure dose/frequency;
- cultural/language context when material.

Generalizing beyond supported scope requires:

1. `evidence_basis=EXTRAPOLATED` or a mixed basis that includes extrapolation;
2. explicit destination scope;
3. rationale for transportability;
4. alternative reasons transport may fail;
5. no stronger evidence-strength grade than the transported evidence warrants.

---

## 7. Competing explanations

When two or more candidate explanations are materially plausible:

1. preserve each as a separate assertion/pathway;
2. identify shared and discriminating predictions;
3. record what evidence would favor one over another;
4. do not infer a single mechanism solely from surface cue matching;
5. use `UNRESOLVED`, `MIXED`, or `CANDIDATE` where appropriate until discrimination occurs.

A good analysis should answer: **What observation or intervention would change our mind?**

---

## 8. Abstention and escalation

Use `UNKNOWN`/`UNRESOLVED`, `DEPENDENCY_INCOMPLETE`, `REVIEW_REQUIRED`, or `REANALYSIS_REQUIRED` instead of guessing when:

- the artifact/modality needed for the claim is unavailable;
- a material source cannot be authenticated or mapped correctly;
- the available evidence cannot distinguish competing mechanisms;
- a causal conclusion is being requested from purely cross-sectional association;
- person-specific mechanism activation is requested from artifact-only data;
- speaker intent is requested without direct or convergent intent evidence;
- an upstream load-bearing claim has changed;
- the answer key contains a disputed dimension.

Training must exclude unresolved dimensions from scored ground truth.

---

## 9. Reporting language

Use language that matches the exact status:

- `OBSERVED`: **“The artifact contains…”**
- `ANNOTATED`: **“This segment is classified as…”**
- `INFERRED`: **“The available evidence supports the inference that…”**
- `HYPOTHESIZED`: **“One plausible hypothesis is…”**
- `VERIFIED`: **“Authoritative evidence supports…”**
- `UNVERIFIED`: **“This claim has not been adequately verified.”**
- `CONTRADICTED`: **“Credible evidence contradicts…”**
- `SUPPORTED` mechanism: **“Evidence supports this pathway under…”**
- `PLAUSIBLE` mechanism: **“This is a plausible pathway, but direct identification is limited.”**
- `CANDIDATE` activation: **“This mechanism could be relevant; the artifact alone does not show that it operated.”**
- `SUPPORTED_IN_EPISODE`: **“Episode-level evidence supports this mechanism relative to the assessed alternatives.”**
- `UNKNOWN` intent: **“The communicator’s intent cannot be established from the available evidence.”**

Forbidden conversions include:

- “contains a fear cue” → “made the audience afraid”;
- “authority cue” → “credible source”;
- “repeated claim” → “illusory-truth effect occurred”;
- “message was false” → “speaker knowingly lied”;
- “social proof cue” → “conformity occurred”;
- “algorithm increased exposure” → “algorithm caused polarization”;
- “statistically mediated” → “mechanism proven.”

---

## 10. Training-ground-truth gate

A dimension may be scored in Persuasion Training only when all of the following hold:

1. the target construct/category is defined in the canonical ontology/taxonomy/registry;
2. the answer-key object is frozen and versioned;
3. required upstream dependencies are `COMPLETE`;
4. no relevant routing flag is `REVIEW_REQUIRED` or `REANALYSIS_REQUIRED`;
5. the specific dimension has sufficient resolution for the task;
6. ambiguity is either absent or deliberately part of the exercise.

If an exercise teaches ambiguity discrimination, multiple answers may be accepted when the answer key explicitly encodes them.

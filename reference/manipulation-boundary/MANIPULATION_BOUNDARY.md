# Persuasion Gym — Manipulation Boundary

**Status:** Normative policy
**Version:** 1.0.0
**Purpose:** Define when Persuasion Gym may classify an influence attempt as persuasion, manipulation, deception, coercion, exploitation, dark-pattern-like influence, or indeterminate.

## 1. Core rule

Persuasion Gym must not use **manipulation** as a synonym for:

- effective persuasion,
- emotional communication,
- rhetoric,
- framing,
- nudging,
- disagreement,
- falsehood,
- bias,
- influence,
- or behavior change.

The app uses `manipulation` only when evidence supports a material impairment or subversion of a person's informed, reflective, and meaningfully voluntary decision process through the design or conduct of the influence attempt.

This is an **operational definition for the app**, not a claim that the philosophical literature contains one universally accepted definition.

## 2. Separate categories

### 2.1 Persuasion
Influence that primarily works by openly presenting reasons, evidence, values, narratives, recommendations, or appeals that the recipient can meaningfully inspect, reject, compare, or resist.

Persuasion can be emotional, vivid, partisan, commercially motivated, or strategically framed without thereby being manipulative.

### 2.2 Deception
Influence involving a materially false representation, materially misleading implication, fabricated evidence/provenance, or knowing concealment of information necessary to understand the represented state of affairs.

Deception is a truth/information-integrity category. It may be manipulative, but factual falsehood alone does not establish manipulation unless it participates in an influence process that impairs informed choice.

### 2.3 Manipulation
Influence that materially subverts, bypasses, exploits, or impairs the recipient's capacity to make an informed and meaningfully voluntary decision, without reaching the threshold of coercion in every case.

Manipulation may operate through deception, strategic concealment, engineered pressure, exploitation of asymmetry or vulnerability, opaque choice architecture, disproportionate emotional/social leverage, or combinations of these.

### 2.4 Coercion
Influence in which threats, penalties, severe constraints, or imposed costs make relevant alternatives meaningfully unavailable or unacceptably costly.

Coercion is not merely strong persuasion. It is evaluated separately because it directly constrains freedom of choice rather than only shaping judgment.

### 2.5 Exploitation
Taking advantage of a vulnerability, dependency, asymmetry, or constrained situation for the influencer's benefit in a way that would not be available, or would be materially weaker, under fairer conditions.

Exploitation can occur with or without deception and with or without manipulation.

### 2.6 Choice architecture / nudge
A change in how options are arranged, presented, defaulted, timed, or made salient.

A nudge or choice architecture is **not automatically manipulative**. It becomes manipulation-risk relevant when its operation materially impairs informed or voluntary choice, is materially opaque, exploits vulnerability/asymmetry, or creates disproportionate friction or pressure.

### 2.7 Dark-pattern-like influence
A digital or interface-based influence configuration that materially distorts or impairs autonomous, informed choice through deceptive, coercive, manipulative, or obstructive design.

This is a functional label, not a legal conclusion.

## 3. The boundary test

The manipulation assessment must proceed through five questions.

### Question A — What is the influence doing?
Identify the concrete influence operation:
- presenting reasons,
- framing,
- emotional appeal,
- social proof,
- scarcity/urgency,
- omission,
- defaulting,
- friction,
- personalization,
- threat,
- reward,
- identity/social sanction,
- source/evidence presentation,
- or other observable operation.

Do not infer manipulation from the technique name.

### Question B — Is informed choice materially impaired?
Ask whether the influence materially reduces the recipient's ability to understand:
- what decision is being made,
- what material facts bear on it,
- what alternatives exist,
- what costs/risks/conditions apply,
- who is influencing them and on what basis,
- or how to reverse/decline the choice.

A mere difference in presentation is insufficient.

### Question C — Is meaningful voluntariness materially impaired?
Ask whether the person retains a realistic ability to:
- delay,
- refuse,
- compare alternatives,
- exit,
- reverse the decision,
- or seek independent information
without disproportionate penalty, obstruction, or social/material threat.

### Question D — Is the influence exploiting an asymmetry or vulnerability?
Assess whether the tactic leverages:
- hidden information,
- hidden incentives,
- privileged behavioral data,
- dependency,
- age/disability or other relevant vulnerability,
- acute distress or desperation,
- social/economic constraint,
- or a deliberately created cognitive/attention disadvantage.

Do not infer vulnerability from group membership alone. The exploitative link must be evidenced or explicitly left unresolved.

### Question E — Is the impairment material to the decision?
The relevant effect must be capable of changing the decision process or outcome in a meaningful way.

Minor stylistic influence, ordinary convenience, or negligible friction should not be promoted to manipulation merely because some influence exists.

## 4. Canonical manipulation dimensions

The common schema already defines nine dimensions. This policy gives them operational meaning.

### DECEPTION
Evidence of materially false, fabricated, disguised, or misleading representation used within the influence attempt.

### MATERIAL_OMISSION
Material information is withheld or obscured such that a reasonable recipient could form a materially different understanding if it were available.

### INFORMATION_ASYMMETRY_EXPLOITATION
The influencer strategically leverages an information/data/incentive advantage that the recipient cannot reasonably inspect or counter.

### COERCIVE_PRESSURE
Threats, penalties, imposed costs, or severe constraints materially reduce meaningful freedom to choose otherwise.

### MANUFACTURED_URGENCY
Time pressure or scarcity is created, exaggerated, or presented in a way that materially suppresses verification/deliberation beyond what the real situation warrants.

### DISPROPORTIONATE_EMOTIONAL_LEVERAGE
Emotional arousal is used in a way that materially overwhelms, bypasses, or suppresses the recipient's ability to evaluate the decision, rather than merely making the message emotionally engaging.

### IDENTITY_SOCIAL_SANCTION_PRESSURE
Belonging, shame, ostracism, loyalty, status loss, or moral condemnation is used to materially constrain perceived freedom to disagree or refuse.

### CHOICE_ARCHITECTURE_OPACITY
Defaults, ordering, salience, friction, interface asymmetry, repeated prompts, or hidden controls materially distort or impair informed/voluntary choice.

### EVIDENCE_CREDIBILITY_THEATER
Scientific, expert, statistical, institutional, testimonial, or visual signals create an appearance of evidential support or independent credibility that is materially stronger than the underlying evidence warrants.

## 5. Evidence rules per dimension

Each dimension must store:
- `present`: YES / NO / UNKNOWN
- `severity`: NONE / LOW / MODERATE / HIGH / SEVERE
- evidence references
- assertion references
- scope and limitations

### Presence rule
`YES` requires affirmative evidence for the dimension itself.

A rhetorical cue alone normally supports only investigation, not presence.

Examples:
- countdown timer observed -> urgency cue observed
- evidence timer resets falsely -> supports `MANUFACTURED_URGENCY=YES`
- celebrity endorsement observed -> authority/credibility cue observed
- celebrity falsely presented as independent expert -> may support `EVIDENCE_CREDIBILITY_THEATER=YES`

### Severity rule
Severity reflects the degree to which the dimension plausibly impairs informed or voluntary choice, not how offensive or emotionally intense the message appears.

## 6. Overall classification logic

Persuasion Gym should not force every case into a binary manipulation/non-manipulation verdict.

### `LOW_EVIDENCE_OF_MANIPULATION`
Use when:
- no manipulation dimension is affirmatively supported at material severity, and
- the available evidence is sufficient to assess the main influence pathway.

This means **low evidence**, not proof that manipulation is absent.

### `SOME_MANIPULATION_RISK`
Use when:
- at least one dimension is supported at `LOW` or `MODERATE` severity, or
- several weak dimensions combine into a credible autonomy/informed-choice concern,
- but evidence is insufficient for substantial impairment.

### `SUBSTANTIAL_MANIPULATION_RISK`
Use when:
- one or more dimensions are supported at `HIGH` or `SEVERE`, or
- multiple `MODERATE` dimensions interact to materially impair informed or voluntary choice,
- and the impairment is materially connected to the target decision.

### `INDETERMINATE`
Use when:
- critical facts needed to assess deception, pressure, asymmetry, vulnerability, or choice architecture are missing,
- upstream verification is unresolved,
- or reasonable competing interpretations remain unresolved.

## 7. Category precedence and overlap

These labels are not mutually exclusive concepts.

A case may be:
- deceptive **and** manipulative,
- coercive **and** manipulative,
- exploitative **without proven deception**,
- persuasive **and emotionally intense but not manipulative**,
- a nudge **without manipulation**,
- or indeterminate.

When coercion is present, label coercion explicitly rather than hiding it under the broader word manipulation.

When deception is present, label deception explicitly rather than using manipulation as a substitute for truth assessment.

## 8. Intent is not required for every functional assessment

Persuasion Gym separates:

1. **functional effect/design** — whether the influence configuration materially impairs informed/voluntary choice;
2. **intent** — whether the influencer intended that impairment.

A system may create manipulative effects without documented manipulative intent.

Conversely, evidence of manipulative intent does not prove that the tactic actually impaired a particular person's decision.

Use the canonical intent statuses:
- EXPLICIT
- DOCUMENTED
- STRONGLY_INFERRED
- WEAKLY_INFERRED
- UNKNOWN

Do not infer intent solely from the presence of a tactic.

## 9. Vulnerability and personalization

Personalization increases concern when it is used to exploit known or inferred vulnerabilities, dependencies, compulsions, distress states, or information asymmetries.

However:
- personalization alone is not manipulation;
- group membership alone is not evidence of vulnerability exploitation;
- the analysis must identify the specific exploited variable and the evidence connecting it to the influence operation.

## 10. Harm is relevant but not identical to manipulation

Harm and manipulation are separate dimensions.

A manipulative tactic can fail to produce harm.
A harmful outcome can occur without manipulation.
A regulatory prohibition may require a harm threshold even when the app's descriptive manipulation assessment does not.

Therefore Persuasion Gym must not equate:

`harmful = manipulative`

or

`manipulative = legally prohibited`.

## 11. Legal-status firewall

The app's labels are analytical, not legal conclusions.

Regimes such as the EU Digital Services Act and EU AI Act use legally specific tests, scopes, thresholds, and exceptions. Persuasion Gym may use them as evidence-informed reference points, but must not output `illegal`, `prohibited`, or `unlawful` without a separate jurisdiction-specific legal analysis.

## 12. Minimal decision matrix

| Influence pattern | Default classification |
|---|---|
| Transparent reasons + evidence + easy refusal | persuasion; low manipulation evidence |
| Emotional story with no impairment of choice | persuasion; emotional rhetoric, not manipulation by default |
| True scarcity clearly disclosed | persuasion / choice context; not manufactured urgency |
| Fake countdown or false scarcity | deception + manufactured urgency; manipulation risk |
| Hidden material fee | material omission / deception; manipulation risk |
| Easy signup + intentionally obstructive cancellation | choice-architecture opacity; manipulation risk |
| Threat of serious penalty for refusal | coercion; assess manipulation overlap separately |
| Personalized message using disclosed preferences | personalization; not manipulation by default |
| Personalized targeting exploiting a known vulnerability | exploitation + manipulation risk |
| Strong social identity appeal | persuasion unless evidence shows material sanction/constraint |
| Fabricated expert consensus | deception + credibility theater; manipulation risk |
| Accurate expert consensus transparently sourced | persuasion; not credibility theater by default |

## 13. Output discipline

Preferred language:
- "This creates manipulation risk because..."
- "The evidence supports material omission..."
- "The tactic appears coercive because refusal carries..."
- "The artifact contains a fear appeal, but that alone does not establish manipulation."
- "Manipulation remains indeterminate because the scarcity claim has not been verified."

Forbidden shortcuts:
- "It uses emotion, therefore it is manipulative."
- "It is false, therefore it is manipulative."
- "It changed behavior, therefore it manipulated the user."
- "It uses a nudge, therefore it is manipulative."
- "The user disliked it, therefore it was coercive."
- "The speaker intended manipulation" without intent evidence.

## 14. Handoff rules

- Factual truth -> `persuasion-fact-check`
- Argument validity -> `critical-thinking`
- Rhetorical features -> `rhetorical-structure-analysis`
- Human mechanism -> `persuasion-mechanism-analysis`
- System propagation -> `influence-systems-analysis`
- Manipulation boundary -> this policy
- Legal permissibility -> separate legal/jurisdictional analysis
- Training/scoring -> `persuasion-training`

If a manipulation judgment depends on an unresolved factual claim, set the relevant dimension to `UNKNOWN` and route `REANALYSIS_REQUIRED` after verification.

## 15. Exit criteria

A manipulation assessment is complete only when:

1. The influence operation is identified.
2. Relevant manipulation dimensions are assessed separately.
3. Each positive dimension has anchored evidence.
4. Truth, mechanism, intent, harm, and manipulation are not collapsed.
5. Coercion and deception are explicitly labeled when present.
6. Missing evidence is represented as `UNKNOWN` rather than guessed.
7. Overall classification follows the dimension evidence rather than rhetorical intensity.
8. Any legal conclusion is explicitly excluded unless separately commissioned.

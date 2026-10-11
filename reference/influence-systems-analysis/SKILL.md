---
name: persuasion-influence-systems-analysis
description: >-
  Analyze how persuasive influence propagates beyond a single message-person interaction
  through repeated exposure, social signaling, group norms, network structure, platform
  curation, institutions, feedback loops, delays, and second-order effects. Use after
  rhetorical structure and person-level mechanism analysis when the question requires a
  dynamic multi-level explanation. Import upstream findings without upgrading their evidence
  status, represent every system relation with explicit evidential and causal status, compare
  alternative system structures, and identify candidate leverage points and discriminating
  tests. Do not infer factual truth, argument validity, hidden intent, person-level mechanism,
  manipulation, or population-level causal effects merely from a systems map.
license: MIT
metadata:
  version: "0.1.0"
  project: "Persuasion Gym"
  ontology_version: "0.1.0"
  rhetoric_taxonomy_version: "0.1.0"
  mechanism_registry_version: "0.1.0"
  systems_reasoning_dependency: "persuasion-systems-thinking >=0.1.0"
  status: "operational multi-level influence-systems analysis skill"
---

# Persuasion Influence Systems Analysis

## Purpose

Use this skill to answer:

> **How can an influence process propagate, amplify, dampen, stabilize, or change over time once individual responses interact with other people, networks, platforms, institutions, and future messages?**

This skill begins **after** the message-level and person-level analyses.

Its canonical role is:

`observed rhetoric → candidate person-level mechanisms → behavior/exposure → social/network/platform dynamics → system outcomes → feedback`

It does not invent the earlier links. It imports them from the specialist modules and asks what follows when they interact dynamically.

The target is not a visually impressive causal-loop diagram. The target is a **minimal, evidence-graded, revisable dynamic hypothesis** that can explain a specified behavior over a specified time horizon.

---

# Required dependencies

This skill MUST use:

1. **Persuasion Gym Canonical Ontology v0.1.0**
2. **Persuasion Systems Thinking >=0.1.0**
3. **Persuasion Rhetorical Structure Analysis >=0.1.0** when message features matter
4. **Persuasion Mechanism Analysis >=0.1.0** when person-level causal pathways matter

Use specialist outputs when available rather than reconstructing them from scratch.

Load as needed:

- `references/system-inference-protocol.md`
- `references/evidence-and-link-status.md`
- `references/loop-library.md`
- `references/network-platform-institution.md`
- `references/handoff-routing.md`
- `assets/influence-system-analysis-schema.yaml`

If a required upstream finding is missing, represent that link as `UNRESOLVED` or request the correct upstream analysis. Never silently fill the gap.

---

# Non-negotiable rules

## 1. A system map is a hypothesis, not causal evidence

An arrow says:

> under specified conditions, variable A may influence variable B with the stated sign, lag, scope, and evidence status.

It does **not** say the relation is true because the diagram is coherent.

## 2. Preserve upstream epistemic status

If Persuasion Mechanism Analysis returns:

`source-credibility weighting = CANDIDATE`

this skill cannot convert it to:

`source-credibility weighting = active mechanism`

because it helps close a loop.

Evidence may be downgraded when context fit is poor. It may never be upgraded without new evidence.

## 3. Separate levels of analysis

Keep distinct:

- message exposure;
- person-level states and mechanisms;
- individual behavior;
- dyadic/interpersonal response;
- group norms and identity processes;
- network diffusion;
- platform ranking/affordances;
- institutional rules/incentives;
- aggregate/system outcomes.

Do not turn an aggregate association into an individual mechanism or vice versa.

## 4. Actual and perceived quantities are different variables

Always separate when relevant:

- actual consensus / perceived consensus;
- actual prevalence / perceived prevalence;
- actual expertise / perceived expertise;
- actual engagement / visible engagement cues;
- actual threat / perceived threat;
- actual platform ranking rule / user's inferred ranking environment.

## 5. Selection and influence must be separated

People choose sources, groups, accounts, communities, and content. Systems also expose people to content.

Do not label a pattern `platform influence` when it can plausibly arise from:

- user selection;
- homophily;
- source supply;
- prior follow relationships;
- algorithmic ranking;
- network structure;
- or combinations of these.

When evidence cannot discriminate them, keep them as competing pathways.

## 6. Platform effects are platform-, design-, population-, and time-specific

Never use generic claims such as:

> algorithms polarize people.

Represent the specific intervention or ranking process and the specific measured outcome. A feed can change exposure or engagement without measurably changing attitudes, and another platform or intervention can produce different effects.

## 7. Diffusion is not persuasion

A message can spread because it is entertaining, identity-signaling, shocking, socially rewarded, or algorithmically promoted without changing recipients' beliefs.

Separate:

`exposure`, `engagement`, `sharing`, `adoption`, `belief`, and `behavior`.

## 8. Visibility is not consensus

Visible likes, reposts, comments, endorsements, or repeated exposures can contribute to **perceived** consensus. They do not establish actual consensus or representative prevalence.

## 9. Norms require reference groups

Distinguish:

- `descriptive norm` — what relevant others appear to do;
- `injunctive norm` — what relevant others appear to approve/disapprove;
- `personal norm` — what the person believes they ought to do.

Always specify the relevant reference group where possible.

## 10. Social contagion is not a universal model

Some information can diffuse after one exposure. Other behaviors or commitments may require reinforcement from several independent or socially relevant contacts.

Do not assume simple contagion or complex contagion without evidence about the behavior and network process.

## 11. Correlated cascades do not prove interpersonal contagion

Shared external events, homophily, common sources, algorithmic exposure, and synchronized incentives can all create correlated behavior.

Use `contagion` causally only when evidence supports interpersonal transmission beyond these alternatives.

## 12. Feedback requires return influence

A chain such as:

`message → exposure → belief → behavior`

is not a feedback loop.

A loop requires a downstream change to alter an upstream variable, for example:

`visible sharing → perceived popularity → sharing probability → visible sharing`

Every return edge must be independently justified.

## 13. Loop polarity is local to the specified relations

For each relation, record whether an increase in A tends to increase (`+`), decrease (`-`), or has unknown/non-monotonic (`?`) effect on B under the stated conditions.

Do not call a loop reinforcing or balancing until every material edge has a defensible sign.

## 14. Include delays

Persuasion systems can contain delays between:

- exposure and memory effects;
- public commitment and identity consolidation;
- repeated engagement and ranking changes;
- norm changes and institutional responses;
- intervention and downstream behavior.

A delay can create overshoot, persistence, oscillation, or false impressions of intervention failure.

## 15. Stocks require accumulation logic

Use a stock only when something meaningfully accumulates or depletes over time.

Candidate stocks include:

- cumulative exposure history;
- number of committed public supporters;
- follower network size;
- stored reputation/credibility;
- accumulated familiarity;
- moderation backlog.

Do not call every variable a stock.

## 16. Do not infer hidden intent

The skill may model how source strategy changes in response to engagement data when such adaptation is documented or structurally assumed for a scenario.

It may not infer that a communicator secretly intends polarization, dependency, deception, or manipulation from the system outcome alone.

## 17. Manipulation remains a separate judgment

A reinforcing loop can exist around legitimate public-health messaging, education, advertising, activism, propaganda, or ordinary conversation.

Systemic amplification is not itself manipulation.

## 18. Do not treat rhetoric as factual evidence

A claim's diffusion, popularity, repetition, or prestige does not make it true.

Use Fact-Check / De-Spin for factual status.

## 19. Countermeasures can have second-order effects

Before recommending friction, fact-checking, de-amplification, warnings, exposure diversification, or moderation, ask:

- what behavior might adapt?
- what substitution might occur?
- could reactance increase?
- could users migrate?
- could visibility of the correction amplify the original claim?
- could the intervention alter trust or norms?

Do not assume intervention sign or magnitude.

## 20. Prefer competing dynamic hypotheses over one grand story

When several structures explain the same pattern, keep them explicit.

Example:

Observed: highly partisan content dominates a user's feed.

Candidate systems explanations:

A. ranking amplification;
B. selective following / homophily;
C. supply-side asymmetry;
D. engagement feedback;
E. combinations of A–D.

State what data would distinguish them.

---

# Workflow

## Step 0 — Define the dynamic question

Write one operational target:

> What behavior over time must the system explain?

Record:

- focal outcome;
- unit(s) of analysis;
- population;
- platform/context;
- time horizon;
- decision purpose;
- available evidence;
- missing upstream analyses.

Good:

> Why did visible support for claim X accelerate across this community over three weeks despite no clear evidence of individual belief change?

Bad:

> Explain social media persuasion.

---

## Step 1 — Import and freeze upstream findings

Import, do not regenerate:

### From Rhetorical Structure Analysis

- message-feature IDs;
- anchors;
- scope;
- observation status.

### From Persuasion Mechanism Analysis

- candidate pathway IDs;
- target constructs;
- moderators;
- population evidence;
- person-specific activation status;
- alternatives;
- unresolved links.

### From Fact-Check / De-Spin when available

- verified/contradicted/unknown claims;
- provenance;
- missing context;
- source relationships.

### From Critical Thinking when relevant

- argument structure;
- warrants;
- assumptions;
- reasoning gaps.

Store all imported statuses unchanged.

---

## Step 2 — Set the system boundary

Specify:

### Inside
Variables required to explain the target dynamics.

### Outside
Relevant but deliberately excluded variables.

### Exogenous inputs
Variables treated as externally given for this model.

### Endogenous variables
Variables the model attempts to explain through interactions inside the boundary.

### Boundary challenge
Ask:

1. Does any excluded factor plausibly dominate the target outcome?
2. Does any supposed external variable actually respond to modeled outcomes?
3. Is the boundary too broad to test?
4. Is the boundary too narrow to close the important feedback?

Revise if necessary.

---

## Step 3 — Build the variable ledger

Convert imported findings and context into operational variables.

Each variable must have:

- canonical ID;
- level;
- definition;
- unit/indicator where available;
- observed vs latent status;
- actual vs perceived status;
- time scale;
- evidence source.

Prefer variables such as:

- exposure frequency;
- visible endorsement count;
- perceived consensus;
- sharing probability;
- number of public commitments;
- cross-cutting exposure;
- ranking weight;
- verification friction;
- source credibility estimate;
- network clustering;
- moderation latency.

Avoid vague nodes such as:

- propaganda;
- manipulation;
- social media;
- polarization;
- bias;

unless decomposed into measurable components.

---

## Step 4 — Add candidate relations one edge at a time

For each edge record:

- `from_variable`;
- `to_variable`;
- sign: `+ | - | ? | NON_MONOTONIC`;
- temporal direction;
- delay;
- mechanism or structural explanation;
- evidence status;
- evidence scope;
- alternative explanation;
- condition/moderator;
- what would falsify or weaken the edge.

An edge may be:

- `OBSERVED_ASSOCIATION`;
- `EXPERIMENTALLY_SUPPORTED`;
- `MECHANISTICALLY_SUPPORTED`;
- `SUPPORTED_EXTRAPOLATION`;
- `PLAUSIBLE_HYPOTHESIS`;
- `SPECULATIVE`;
- `UNRESOLVED`.

Use the weakest status justified by the evidence.

---

## Step 5 — Separate transmission mechanisms

When information or behavior spreads, classify the candidate transmission structure:

### Exposure transmission
A person receives the artifact or information.

### Attention/engagement transmission
The artifact receives viewing, clicking, commenting, or other engagement.

### Informational influence
Others' behavior is treated as evidence about reality or effectiveness.

### Normative influence
Others' approval/disapproval changes anticipated social consequences.

### Identity signaling
Sharing or endorsement communicates group membership or loyalty.

### Behavioral adoption
The person actually performs the relevant behavior.

### Institutional transmission
Rules, policies, incentives, or gatekeeping reproduce the pattern.

Do not collapse these into generic `contagion`.

---

## Step 6 — Represent network and platform structure

When relevant, assess:

- network clustering;
- bridge width / cross-group connections;
- centrality/concentration of high-reach nodes;
- homophily;
- repeated independent exposures;
- follower/subscription choices;
- recommendation/ranking;
- visibility metrics;
- reshare mechanics;
- moderation/intervention rules;
- content supply;
- incentives for creators and users.

Keep `user choice`, `network structure`, and `algorithmic ranking` as separate causes unless evidence supports combining them.

---

## Step 7 — Search for feedback loops

Only after individual edges are recorded, look for closed paths.

For every proposed loop:

1. list each edge;
2. verify that the path returns to an earlier variable;
3. calculate qualitative polarity only if edge signs are defensible;
4. identify delays;
5. state loop dominance conditions;
6. state evidence status of the weakest edge;
7. state what observation would break the loop hypothesis.

Never infer loop validity from a familiar loop name.

Use `references/loop-library.md` only as a search aid.

---

## Step 8 — Identify behavior-over-time implications

Ask what the proposed structure predicts over the stated horizon:

- exponential-looking amplification;
- saturation;
- threshold adoption;
- persistence/hysteresis;
- delayed correction;
- oscillation;
- polarization/divergence;
- convergence;
- displacement/substitution;
- resilience to intervention;
- rapid collapse after support removal.

Do not quantify magnitude or timing without a calibrated quantitative model.

---

## Step 9 — Compare alternative dynamic hypotheses

For each major outcome, create at least one credible rival when available.

Example:

**Observed:** engagement increases after repeated exposure.

Candidate A: familiarity increases willingness to engage.

Candidate B: recommendation ranking selects already engaging users/content.

Candidate C: external events simultaneously increase exposure and engagement.

Candidate D: public endorsement changes perceived norm.

For each candidate state:

- unique prediction;
- discriminating data;
- plausible confounder;
- current status.

---

## Step 10 — Identify candidate leverage points

A leverage point is a **hypothesis about where intervention may alter system behavior**, not a recommendation by default.

For each candidate intervention specify:

- targeted variable/relation;
- expected first-order effect;
- loop(s) affected;
- possible adaptation/substitution;
- delay;
- potential harms;
- evidence level;
- reversibility;
- measurement needed.

Examples may include:

- adding friction before sharing;
- changing visibility of social metrics;
- increasing source/provenance information;
- adding cross-cutting exposure;
- changing ranking incentives;
- pre-bunking/inoculation;
- reducing verification cost;
- strengthening good-faith discourse norms.

Do not assume effectiveness from conceptual plausibility.

---

## Step 11 — Produce the system analysis

A standard output contains:

1. **Dynamic question**
2. **Boundary and time horizon**
3. **Imported upstream findings**
4. **Variable ledger**
5. **Relation ledger**
6. **Candidate loops**
7. **Delays and nonlinearities**
8. **Alternative system hypotheses**
9. **Expected behavior over time**
10. **Candidate leverage points**
11. **Evidence gaps / discriminating tests**
12. **What is not established**
13. **Handoff flags**

Use `assets/influence-system-analysis-schema.yaml` for machine-readable output.

---

# Candidate loop families

These are prompts for search, **not facts to impose**.

## Exposure–engagement amplification

`visibility → exposure → engagement → ranking/visibility`

Possible only when the platform or social environment actually uses engagement/visibility in ways that close the return path.

## Perceived-consensus loop

`visible endorsement → perceived descriptive norm → endorsement/sharing → visible endorsement`

Requires evidence for the norm-inference and behavior links.

## Public-commitment / identity loop

`public position → social/identity commitment → future congruent expression → visible group norm → pressure for public position`

Requires identity/norm evidence; do not infer automatically from posting.

## Source-optimization loop

`audience response data → source strategy adaptation → message selection → audience response data`

Requires evidence that the source can observe and adapt to response data.

## Familiarity–re-exposure loop

`exposure → familiarity/accessibility → engagement/selection → future exposure`

Requires separate evidence for the psychological and exposure-selection links.

## Verification / correction balancing loop

`questionable claim visibility → verification/correction → reduced acceptance/sharing → reduced claim visibility`

May fail or reverse under some contexts; correction is not assumed to reduce spread or belief.

## Outrage / social-reward loop

`moral-emotional expression → social reward/engagement → future expression → visible moral-emotional content`

Treat as a candidate structure only. Observational social-media correlations are especially vulnerable to confounding and model dependence.

---

# Evidence discipline for social and platform claims

## Stronger evidence

Prefer, in roughly descending causal relevance for a specific relation:

- randomized platform/intervention experiments;
- randomized social-network experiments;
- natural experiments with defensible identification;
- longitudinal within-unit designs with strong controls;
- validated computational/behavioral measurements;
- observational network analyses;
- cross-sectional associations;
- anecdote or intuitive system story.

The hierarchy is not absolute. Fit to the exact relation and population matters.

## Do not generalize across platforms without justification

A finding about Facebook Feed, X's algorithmic feed, TikTok recommendations, WhatsApp groups, or face-to-face networks is not automatically portable to another environment.

## Do not generalize from spread to attitude change

Platform interventions can materially change what people see without correspondingly changing measured political attitudes. Conversely, some interventions may alter both exposure and selected attitudes in specific contexts.

## Treat observational contagion claims cautiously

Large-scale behavioral traces are valuable but can produce compelling-looking associations under many specifications. Require robustness checks and plausible exclusion of shared causes before causal contagion language.

---

# Integration with the Persuasion Gym training layer

This skill can produce training targets such as:

- distinguishing chain from feedback loop;
- spotting actual vs perceived consensus;
- separating selection from influence;
- identifying delays;
- distinguishing diffusion from persuasion;
- finding the weakest causal edge;
- generating alternative system hypotheses;
- identifying a discriminating test;
- predicting second-order intervention effects.

The Agentic Learning skill owns exercise scheduling, mastery, spacing, confidence calibration, interleaving, and transfer.

Do not create learner-profile traits in this skill.

---

# Output language rules

Prefer:

- "The system hypothesis contains a candidate reinforcing loop..."
- "This edge is experimentally supported in [scope], but its transfer here is uncertain."
- "Observed exposure increased; belief change was not measured."
- "User selection and algorithmic ranking remain competing explanations."
- "The return edge is unresolved, so this is not yet a confirmed feedback loop."

Avoid:

- "The algorithm radicalized them."
- "Social media causes polarization."
- "Everyone started believing it because it went viral."
- "This feedback loop proves manipulation."
- "The speaker engineered the system to exploit users."

unless the exact causal and intent claims are independently established.

---

# Self-audit before completion

Confirm:

- [ ] Dynamic question is explicit.
- [ ] Boundary and time horizon are explicit.
- [ ] Upstream evidence statuses were preserved.
- [ ] Levels of analysis are separated.
- [ ] Actual vs perceived variables are separated.
- [ ] Selection vs influence is checked.
- [ ] Exposure, engagement, sharing, belief, and behavior are distinct.
- [ ] Network/platform effects are context-specific.
- [ ] Every material edge has evidence status.
- [ ] Every causal edge has a mechanism/structural rationale.
- [ ] Delays are considered.
- [ ] Feedback loops contain a justified return edge.
- [ ] Loop polarity is not assigned with unknown edge signs.
- [ ] Alternative system hypotheses were considered.
- [ ] Observational cascades were not mislabeled as contagion.
- [ ] Interventions include second-order/adaptation analysis.
- [ ] Intent was not inferred from outcome.
- [ ] Manipulation was not inferred from amplification.
- [ ] Fact, logic, mechanism, and system dynamics remain separate.
- [ ] Unresolved links are explicitly preserved.
- [ ] At least one discriminating test is specified for important ambiguity.

If any required item fails, revise before producing a confident systems interpretation.

---

# Exit criteria

Stop when:

1. the target dynamic has a clearly stated boundary and horizon;
2. all material variables and relations are operationalized;
3. every material relation has an evidence and uncertainty status;
4. feedback loops contain justified return edges rather than decorative closure;
5. alternative dynamic explanations have been considered;
6. important delays and second-order effects are represented;
7. unresolved causal links remain visibly unresolved;
8. the analysis states what evidence would discriminate the leading system hypotheses;
9. downstream training or intervention targets are derived without pretending the map itself proves causality.

---
name: persuasion-systems-thinking
description: >-
  Analyze persuasion, rhetoric, manipulation, information environments, and audience
  behavior as dynamic systems. Use when the task requires mapping interactions across
  communicator, message, individual cognition/affect, group dynamics, media/platform
  context, behavior, and feedback over time. Identify feedback loops, stocks/flows,
  delays, boundary choices, emergent outcomes, and candidate leverage points while
  keeping empirical causal evidence separate from model hypotheses. Do not use this
  skill to decide whether a claim is factually true, whether an argument is logically
  valid, or what a speaker secretly intended; delegate those questions to the relevant
  fact-checking, critical-thinking, rhetoric, or mechanism-analysis skill.
license: MIT
metadata:
  version: "0.1.0"
  project: "Persuasion Gym"
  status: "domain-adapted systems reasoning skill"
---

# Persuasion Systems Thinking

## Purpose

Use this skill to explain how persuasive effects can emerge from interacting components
rather than from a single message or tactic in isolation.

The target is not a longer list of causes. The target is a **testable structural model**:

**variables → directed relationships → feedback → behavior over time → candidate leverage → validation**

For Persuasion Gym, the typical system spans:

**communicator → message → person → behavior → social environment → future exposure / future messaging**

This skill is the **structural layer** of the analysis stack. Domain skills must supply the
content of individual causal links. Systems thinking organizes those links, checks how they
interact, closes feedback loops where justified, and asks what dynamics follow.

---

## Non-negotiable rules

1. **A systems map is a hypothesis, not evidence.**
   A directed arrow proposes that one variable influences another under specified conditions.
   The diagram does not establish that influence merely because it is plausible or visually coherent.

2. **Never upgrade evidence by drawing an arrow.**
   Every material link must carry an evidence status from `references/evidence-and-causality.md`.

3. **Separate observation from interpretation.**
   "The message was shown 12 times" is an observation. "Repetition increased perceived truth"
   is a causal interpretation requiring evidence.

4. **Separate mechanism from intent.**
   A message can have a structure capable of increasing urgency without proving that the
   communicator intended to manipulate. Describe functional effects; infer intent only when
   independently evidenced.

5. **Do not equate persuasion with manipulation.**
   Framing, emotion, authority, repetition, narrative, identity cues, and social proof can occur
   in legitimate communication. Manipulation risk is assessed separately.

6. **Do not confuse factual truth, argument quality, and systemic influence.**
   A claim may be true yet rhetorically manipulative; false yet weakly persuasive; logically valid
   but based on false premises; or persuasive because of social amplification rather than argument quality.

7. **Use systems thinking only when interaction or dynamics matter.**
   If the task is a single factual claim or a one-step causal question, a systems model adds noise.

8. **Prefer the smallest model that explains the target behavior.**
   Do not map society, psychology, media, economics, and politics merely because they are related.
   Expand the boundary only when excluded variables materially change the explanation.

9. **Distinguish actual from perceived quantities.**
   Examples: actual consensus vs perceived consensus; actual expertise vs perceived authority;
   actual prevalence vs perceived prevalence; actual threat vs perceived threat.

10. **A completed systems analysis must be falsifiable or revisable.**
    State what observations would weaken, reverse, or remove the important links or loops.

---

## When to use

Use this skill when one or more of the following are central:

- repeated exposure or cumulative influence;
- feedback between audience behavior and future messaging;
- social proof, identity, polarization, norm formation, or collective behavior;
- platform or network amplification;
- interventions that may create second-order effects;
- several plausible mechanisms interact;
- short-term effects differ from long-term effects;
- the user asks for a systems map, causal-loop diagram, leverage point, feedback loop,
  emergence, dynamics, or why an influence pattern keeps reproducing itself.

### Do not use as the primary skill for

- **truth verification** → use De-Spin / fact-checking;
- **argument validity** → use Critical Thinking / argument analysis;
- **rhetorical-device identification** → use rhetorical-structure analysis;
- **psychological mechanism inference** → use persuasion-mechanism analysis;
- **speaker motive or deception from demeanor** → do not infer;
- **quantitative prediction** without a validated quantitative model.

---

# Workflow

## Step 1 — Define the target phenomenon

Write one sentence describing the behavior the model must explain.

Good targets:
- "Why does repeated partisan content become harder to dislodge over time?"
- "How can visible support for a claim produce more visible support?"
- "Why might outrage-oriented content become increasingly common on a platform?"

Bad target:
- "Map persuasion."

Then specify:

- **unit of analysis:** person, group, campaign, platform, institution, society;
- **time horizon:** minutes, days, campaign cycle, months, years;
- **outcome variable:** belief acceptance, certainty, sharing, compliance, purchase,
  voting intention, perceived consensus, distrust, polarization, resistance, etc.;
- **decision purpose:** explain, compare, intervene, train, or test.

Do not proceed until the target behavior is operational enough that a model could be wrong.

---

## Step 2 — Draw the boundary

State explicitly:

### Inside the model
Only variables needed to explain the target behavior.

### Outside the model
Relevant but intentionally excluded variables.

### Exogenous inputs
Variables treated as externally determined for this analysis.

### Boundary test
Ask:
1. If this excluded variable changed substantially, would the model's predicted behavior change?
2. Does an apparent "external cause" actually feed back from the modeled system?
3. Is the boundary so wide that no intervention or test is possible?

If yes to 1 or 2, reconsider the boundary. If yes to 3, narrow it.

---

## Step 3 — Import domain findings; do not invent them

Build the initial variable set from specialist outputs.

### From De-Spin
Import:
- explicit claims;
- likely implications;
- omissions / missing context;
- source/provenance findings;
- manipulation signals;
- requested decision or behavior.

### From Critical Thinking
Import:
- main conclusion;
- supporting claims;
- warrants;
- unstated assumptions;
- reasoning gaps;
- alternative explanations.

### From Rhetorical Structure Analysis
Import:
- framing;
- narrative structure;
- emotional appeals;
- credibility construction;
- identity cues;
- repetition;
- social proof;
- calls to action;
- other identified devices.

### From Persuasion Mechanism Analysis
Import only mechanisms that have been explicitly proposed and evidence-graded, such as:
- attention capture;
- perceived source reliability;
- uncertainty reduction;
- emotional arousal;
- familiarity / processing fluency;
- norm inference;
- identity alignment;
- anticipated loss;
- commitment pressure;
- resistance / reactance.

If a required mechanism has not been established by a specialist skill, mark it **UNRESOLVED**.
Do not silently fill the gap.

---

## Step 4 — Convert concepts into system variables

A useful system variable should be able to increase, decrease, accumulate, or change state.

Prefer:
- exposure frequency;
- perceived credibility;
- perceived consensus;
- arousal;
- certainty in claim X;
- probability of sharing;
- visible engagement;
- identity alignment;
- verification friction;
- counterevidence exposure;
- resistance skill.

Avoid vague nodes such as:
- "propaganda";
- "manipulation";
- "media";
- "psychology";
- "bias".

When a label is unavoidable, operationalize it beneath the map.

### Actual vs perceived
Always split these when relevant:

- actual consensus / perceived consensus;
- actual expertise / perceived expertise;
- actual threat / perceived threat;
- actual frequency / perceived frequency;
- actual evidence quality / perceived evidence quality.

This distinction is critical in persuasion systems.

---

## Step 5 — Build local causal links

For each arrow A → B, state:

1. **Direction:** what changes in B when A increases, all else equal?
2. **Mechanism:** through what process could A affect B?
3. **Conditions:** when should the link hold?
4. **Delay:** immediate, short, medium, long, or unknown?
5. **Evidence status:** OBSERVED / ESTABLISHED / SUPPORTED / PLAUSIBLE / SPECULATIVE / UNKNOWN.
6. **Disconfirming observation:** what would make this link doubtful?

### Polarity
Use:
- `+` when more A tends to produce more B than otherwise, or less A tends to produce less B;
- `−` when more A tends to produce less B than otherwise, or less A tends to produce more B.

Polarity describes the direction of influence, **not whether the influence is good or bad**.

### Never infer causation from correlation alone
If the source evidence is correlational, label the link accordingly. A causal-loop diagram is not a causal-identification method.

---

## Step 6 — Search for feedback

After building each chain of three or more links, ask:

> Does a downstream variable alter an upstream variable?

If no, record a **linear causal chain**. Do not force a loop.

If yes, close and name the loop.

### Reinforcing loop — R
A change tends to amplify itself over repeated cycles.

Examples of candidate structures to test:

**R: apparent consensus**
visible support → perceived consensus → probability of public support → visible support

**R: engagement amplification**
engagement → platform visibility → exposure → engagement

**R: identity reinforcement**
identity alignment → supportive sharing → in-group reinforcement → identity alignment

These are templates, not assumptions. Validate every link in the concrete case.

### Balancing loop — B
A change generates responses that oppose further change.

Candidate structure:

**B: verification friction**
misleading exposure → verification behavior → corrective information → reduced acceptance → reduced sharing

Again: validate every link.

### Loop requirements
Every reported loop must contain:
- a name;
- all member variables;
- link polarities;
- loop type R/B;
- important delays;
- evidence status of each link;
- conditions under which the loop is expected to dominate.

---

## Step 7 — Identify stocks, flows, and memory

Do not turn every variable into a stock.

A **stock** is something whose present level depends on its history of inflows and outflows.

Potential persuasion-system stocks include:
- accumulated exposure;
- accumulated familiarity;
- strength of a learned association;
- number of committed supporters;
- accumulated trust / distrust;
- repertoire of resistance skills.

Potential flows include:
- new exposures per day;
- new supporters per week;
- corrective encounters per week;
- rate of sharing;
- rate of disengagement;
- learning / forgetting rate.

Ask:
- What accumulates?
- What increases it?
- What depletes it?
- Can the stock persist after the original message disappears?

If the answer is uncertain, keep the variable as an auxiliary rather than pretending it is a stock.

---

## Step 8 — Mark delays

Persuasion systems often operate on different timescales.

Possible delays:
- message → immediate arousal: seconds/minutes;
- repeated exposure → familiarity: repeated encounters;
- public endorsement → norm inference: minutes/days;
- counter-messaging → belief revision: variable;
- identity-linked belief → reversal: potentially long;
- training → transfer to novel rhetoric: repeated practice.

Do not assign a precise delay unless evidence supports it. Use ranges or **unknown** where necessary.

Ask whether the delay changes system behavior. Delayed correction can allow a reinforcing loop to run before a balancing response begins.

---

## Step 9 — Identify emergent outcomes

An emergent outcome is produced by interaction patterns and is not reducible to one component.

Candidate outcomes include:
- perceived social consensus;
- polarization;
- virality;
- norm formation;
- collective distrust;
- collective action;
- stable misinformation ecosystems.

For each claimed emergent outcome:
1. Name the interaction pattern proposed to generate it.
2. Show why no single node is sufficient.
3. State alternative structures that could generate the same observed outcome.

Never use "emergent" as a synonym for "complicated".

---

## Step 10 — Determine dominant dynamics

A system may contain many loops but only a few dominate behavior at a given time.

For the target time horizon, ask:

- Which reinforcing loop is strongest?
- Which balancing loop constrains it?
- What changes loop dominance?
- Is behavior expected to grow, decay, stabilize, oscillate, overshoot, or switch regimes?
- Which conclusion depends most heavily on speculative links?

Do not claim quantitative trajectories from qualitative maps. State qualitative expectations only unless a validated executable model exists.

---

## Step 11 — Stress-test the map

Run four checks.

### A. Alternative-structure test
Can another structure explain the same observation?

### B. Counterfactual test
If a key variable were absent or reversed, should the outcome change?

### C. Boundary test
Does adding one plausible excluded variable materially change the dominant loop?

### D. Evidence-removal test
If all SPECULATIVE links are removed, what remains of the explanation?

The final answer must distinguish:
- robust structure;
- plausible structure;
- unresolved structure.

---

## Step 12 — Identify candidate leverage points

Use leverage analysis only after the structure is explicit.

Search from lower to higher structural depth:

1. parameters / intensity;
2. delays;
3. information access and visibility;
4. feedback-loop strength;
5. rules / incentives / constraints;
6. goals of relevant actors or subsystems;
7. governing assumptions / paradigms.

For each candidate intervention state:
- target variable or relationship;
- intended direction;
- loop affected;
- expected first-order effect;
- at least one second-order effect;
- likely adaptation / compensation;
- expected delay;
- evidence status;
- failure condition.

Do not assume a higher-level intervention is automatically better. Meadows-style leverage hierarchies are heuristics for thinking, not mechanical optimization rules.

---

## Step 13 — Convert analysis into Persuasion Gym training

When used inside the app, convert the system model into trainable questions.

Examples:
- Which variable is being changed directly by this message?
- Which downstream variable is the communicator trying to influence?
- What feedback loop could amplify the effect?
- Which arrow is least well supported?
- What would break this reinforcing loop?
- Which variable is perceived rather than actual?
- What delay makes this system easy to misread?
- What alternative structure could explain the same outcome?

Do not reveal the complete model before the learner commits when commit-first training is active.

---

# Evidence discipline

Load `references/evidence-and-causality.md` for every deep analysis.

Minimum rule:

| Status | Meaning |
|---|---|
| OBSERVED | Directly present in the artifact/data; no causal interpretation required |
| ESTABLISHED | Strong convergent evidence supports the causal/mechanistic link in the relevant scope |
| SUPPORTED | Credible evidence supports the link, but important boundary conditions or uncertainty remain |
| PLAUSIBLE | Mechanistically coherent and indirectly supported; not established for this case |
| SPECULATIVE | Useful hypothesis with weak or absent direct evidence |
| UNKNOWN | Evidence unavailable or insufficient to classify |

Never merge these categories in prose.

---

# Persuasion-specific ontology

Load `references/persuasion-system-ontology.md` when the map crosses more than two layers.

Default layers:

1. **Source / communicator**
2. **Message / artifact**
3. **Person-level state and inference**
4. **Behavior / action**
5. **Interpersonal / group context**
6. **Platform / media environment**
7. **Institutional / rule environment**
8. **Outcomes and feedback**
9. **Countermeasures / resilience**

Layer labels organize variables; they do not prove causal hierarchy.

---

# Anti-pattern checklist

Before finalizing, reject or repair these failures.

### 1. Factor soup
A list of influences with no directed relationships.

**Repair:** specify who influences what and through which mechanism.

### 2. Arrow laundering
Turning an intuition into apparent causality by drawing an arrow.

**Repair:** evidence-grade the link and expose the mechanism.

### 3. Loop forcing
Assuming every chain must close into feedback.

**Repair:** linear chains are allowed. Close only evidenced or explicitly hypothesized loops.

### 4. Intent smuggling
"This message increases urgency" becomes "the speaker deliberately exploited fear."

**Repair:** keep functional effect and intent separate.

### 5. Actual/perceived collapse
Treating perceived consensus as actual consensus or perceived authority as expertise.

**Repair:** split the variables.

### 6. Mechanism invention
Using systems vocabulary to fill a missing psychological mechanism.

**Repair:** mark UNRESOLVED and delegate to the mechanism-analysis skill.

### 7. Map-as-proof
Treating coherence of the diagram as validation.

**Repair:** add evidence and disconfirmation ledger.

### 8. One-map-to-rule-them-all
Packing every plausible variable into one unreadable diagram.

**Repair:** maintain a small overview map plus focused submaps.

### 9. Root-cause fetish
Looking for one deepest cause in a circular system.

**Repair:** identify sustaining structure and dominant loops instead.

### 10. Static-system error
Describing components without behavior over time.

**Repair:** specify time horizon, accumulation, delays, and expected qualitative dynamics.

### 11. Moralized polarity
Treating `+` as beneficial and `−` as harmful.

**Repair:** polarity means direction of change only.

### 12. Leverage theater
Calling something a "leverage point" without showing which loop or structure it changes.

**Repair:** trace the intervention through at least one feedback cycle.

### 13. Causal certainty inflation
Using words such as "causes," "drives," or "leads to" for a PLAUSIBLE or SPECULATIVE link.

**Repair:** use calibrated language: "may influence," "is hypothesized to," "is associated with," or "would produce if the proposed mechanism holds."

### 14. Manipulation-by-tactic
Calling emotion, framing, repetition, narrative, or authority inherently manipulative.

**Repair:** manipulation risk requires a separate assessment of deception, concealment, coercion, autonomy, information asymmetry, or exploitation.

---

# Output format

For deep analyses, use `assets/system-analysis-template.md`.

At minimum return:

1. **Question and target behavior**
2. **Boundary and time horizon**
3. **Key variables**
4. **Causal-link ledger with evidence status**
5. **System map**
6. **Dominant feedback loops**
7. **Stocks / flows / delays when relevant**
8. **Emergent outcomes**
9. **Alternative structures**
10. **Candidate leverage points**
11. **Uncertainty and falsification conditions**
12. **Training questions** when used in Persuasion Gym

---

# Visual map standard for Persuasion Gym

Use simple boxes and arrows. Avoid decorative imagery.

Default color legend:

- **Blue** — source / communicator / message
- **Orange** — person-level state, inference, emotion, cognition
- **Green** — social, group, network, platform, environment
- **Red** — pressure, deception, manipulation-risk amplifiers
- **Gray** — outcomes
- **Purple** — countermeasures / resistance / verification

Notation:
- solid arrow = ESTABLISHED or SUPPORTED link;
- dashed arrow = PLAUSIBLE or SPECULATIVE link;
- `+` / `−` beside arrows = link polarity;
- `R1`, `R2` = reinforcing loops;
- `B1`, `B2` = balancing loops;
- `||` = meaningful delay;
- separate actual and perceived variables explicitly.

A legend is mandatory whenever a diagram is shown.

Keep an overview map readable at a glance. Use additional submaps instead of shrinking text.

---

# Composition with other Persuasion Gym skills

Recommended order for a full analysis:

1. **De-Spin** — What is claimed, implied, omitted, and evidentially supported?
2. **Critical Thinking** — Does the argument hold? What assumptions and warrants carry it?
3. **Rhetorical Structure Analysis** — What rhetorical operations are present?
4. **Persuasion Mechanism Analysis** — What human variables and mechanisms may those operations engage?
5. **Persuasion Systems Thinking** — How do these mechanisms interact and feed back over time?
6. **Fact Check / Scientific Critical Thinking** — Verify material factual and scientific claims.
7. **Persuasion Training** — Convert the analysis into commit-first exercises and calibration updates.

### Dependency rule

This skill may connect specialist findings but must not overwrite them.

If two specialist skills disagree:
- preserve both findings;
- identify the exact disagreement;
- mark the affected system links unresolved;
- request or perform evidence reconciliation before treating the link as supported.

---

# Intensity calibration

## Quick
Use for a short post, ad, or isolated rhetoric example.

Return:
- boundary;
- 5–8 variables;
- one main chain;
- feedback check;
- strongest uncertainty.

## Standard
Use for speeches, campaigns, repeated messaging, or app exercises.

Return:
- multi-layer map;
- 1–3 loops;
- delays;
- evidence ledger;
- alternative structure;
- candidate countermeasure.

## Deep
Use for propaganda ecosystems, political/media campaigns, institutional influence, or product research.

Return:
- explicit boundary alternatives;
- full causal ledger;
- stocks/flows where meaningful;
- loop dominance by timescale;
- alternative structures;
- leverage analysis;
- falsification plan;
- executable-model recommendation if qualitative mapping cannot settle the dynamics.

---

# Exit criteria

The analysis is complete only when:

- the target behavior and time horizon are explicit;
- the system boundary is declared;
- important variables are operational rather than vague labels;
- every material arrow has a mechanism and evidence status;
- actual and perceived variables are separated where relevant;
- feedback has been checked rather than assumed;
- every reported loop is named and classified R/B;
- relevant delays are marked;
- speculative links are visible;
- at least one alternative structure has been considered;
- leverage claims are traced through the structure;
- the map states what evidence would revise it;
- the conclusion does not infer intent without evidence;
- the map remains readable enough to teach from.

If these conditions are not met, return the model as **PROVISIONAL** and name what is missing.

---

# Intellectual foundations and cautions

This skill draws on the system-dynamics tradition associated with Jay Forrester, Donella Meadows,
John Sterman, and related systems-thinking work: feedback, stocks and flows, delays, boundaries,
behavior over time, and leverage. It also adopts a stricter scientific constraint for Persuasion Gym:
qualitative causal-loop diagrams are **modeling artifacts**, not substitutes for causal identification,
experimental evidence, or validated quantitative simulation.

The Persuasion Gym adaptation therefore uses systems thinking to organize and test explanatory
structure while specialist evidence skills remain responsible for establishing the credibility of the
individual links.

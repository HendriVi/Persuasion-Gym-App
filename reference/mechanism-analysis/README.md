# Persuasion Mechanism Analysis

This package is the person-level causal-inference layer of Persuasion Gym.

It consumes anchored rhetorical features and asks which registered psychological processes could
plausibly connect those features to observed or hypothesized responses.

## Core design principle

`rhetorical cue → candidate mechanism`

not

`rhetorical cue → mechanism proven`

The skill keeps four forms of evidence separate:

1. certainty that the message feature is present;
2. population evidence that an effect occurs;
3. evidence for the proposed explanatory mechanism;
4. evidence that the mechanism operated in this specific episode/person.

## Files

- `SKILL.md` — normative operational skill
- `references/mechanism-inference-protocol.md` — causal-inference discipline
- `references/candidate-comparison.md` — adversarial comparison of competing mechanisms
- `references/person-specific-activation.md` — person-level activation standards
- `references/handoff-routing.md` — specialist boundaries and rerun rules
- `assets/mechanism-analysis-schema.yaml` — machine-readable output schema
- `TESTING.md` — regression suite

## Intended position in the stack

`Rhetorical Structure Analysis`
→ **Persuasion Mechanism Analysis**
→ `Systems Thinking / Manipulation Assessment / Agentic Learning`
→ `Fact-Check final verification`

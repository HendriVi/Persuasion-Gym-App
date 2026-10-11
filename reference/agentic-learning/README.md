# Persuasion Agentic Learning

A Persuasion Gym-specific adaptation of agentic learning principles.

## What it adds beyond generic Agentic Learning

The public `agentic-learning` skill is designed as a general learning partner and provides a strong foundation: retrieval, generation, spacing, reflection, interleaving, cognitive-load control, metacognition/oracy, productive struggle, and formative feedback.

Persuasion Gym needs additional constraints:

- confidence before feedback,
- separate scoring for device, mechanism, evidence, manipulation, and systems reasoning,
- a persistent skill-level learner model,
- error tags rather than personality judgments,
- transfer across rhetorical domains,
- uncertainty-preserving answer keys,
- delayed verification before mastery,
- integration with specialist rhetoric/argument/evidence/systems modules.

## Package

- `SKILL.md` — learning engine behavior
- `references/learning-science.md` — evidence base and limitations
- `references/learner-model.md` — persistent learner state
- `references/exercise-selection.md` — adaptive item routing
- `references/spacing-policy.md` — scheduler integration and fallback
- `assets/training-item-schema.md` — canonical exercise representation
- `TESTING.md` — behavior and regression checks

## Upstream inspiration

This package was informed by Favio Vázquez's MIT-licensed `agentic-learning` project:
https://github.com/FavioVazquez/agentic-learning

It is an original domain adaptation rather than a verbatim copy. The scientific reference was independently tightened for the Persuasion Gym use case, particularly around spacing, transfer, calibration, and uncertainty.

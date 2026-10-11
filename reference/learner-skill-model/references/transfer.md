# Transfer Evidence

## Principle

Transfer means applying the same latent skill when material surface/context features change.

## Levels

- `NONE` — ordinary practice in the learning context.
- `NEAR` — different item, same domain/modality, meaningful surface variation.
- `CROSS_DOMAIN` — same latent target, materially different domain.
- `CROSS_MODALITY` — same target across text/image/audio/video or comparable modality shift.
- `FAR` — multiple material context changes with preserved latent target.

## Minimum metadata

Record:
- `origin_domain`
- `current_domain`
- `origin_modality`
- `current_modality`
- `source_type_changed`
- `emotional_tone_changed`
- `explicitness_changed`
- `social_context_changed`
- `distractor_structure_changed`

## Non-transfer examples

- paraphrase only;
- synonyms only;
- same ad with brand renamed;
- same political argument with names swapped but no task-structure change (useful for bias symmetry, not necessarily transfer).

## Transfer verification

Transfer evidence counts only when:
1. item is mastery-eligible;
2. answer key is frozen;
3. latent skill is explicitly tested;
4. transfer level is not `NONE`;
5. learner was not given the target label beforehand.

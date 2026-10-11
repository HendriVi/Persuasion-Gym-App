# Language Discipline

Natural-language output must be generated **from** structured statuses.

## Examples

| Structured state | Allowed language |
|---|---|
| rhetorical feature `ANNOTATED` | “The passage uses an authority cue.” |
| mechanism `PLAUSIBLE`, activation `CANDIDATE` | “Source-credibility weighting is a plausible candidate mechanism, but there is no evidence here that it operated in this audience.” |
| verification `UNVERIFIED` | “The factual claim remains unverified.” |
| intent `UNKNOWN` | “The available material does not establish why the communicator used this construction.” |
| system edge `OBSERVATIONAL + PLAUSIBLE` | “These variables are associated in this context; the causal direction remains uncertain.” |

## Banned rhetorical inflation

Avoid:

- definitely / clearly / proves / caused / manipulated / brain response / subconscious effect

unless the relevant structured fields actually warrant the statement and the term is defined for the task.

Do not use numerical confidence to make weak evidence sound stronger.

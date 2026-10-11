# Uncertainty Propagation

## Dependency graph, not prose inheritance

Every material downstream assertion should reference the upstream assertions/objects it relies on. The application should propagate review flags through this graph rather than scanning prose.

## Propagation matrix

| Upstream change | Default downstream action |
|---|---|
| factual `VERIFIED → CONTRADICTED` | mark dependent objects `REANALYSIS_REQUIRED` |
| factual `VERIFIED → VERIFIED_WITH_QUALIFICATION` | review only dependents for which the qualifier is material |
| mechanism `SUPPORTED → PLAUSIBLE` | downgrade pathway-level support if load-bearing; person activation does not automatically change |
| person activation `CANDIDATE → SUPPORTED_IN_EPISODE` | may strengthen episode-specific explanation; cannot upgrade population evidence strength |
| scope narrowed | propagate narrowed scope or explicitly mark extrapolation |
| source removed as non-independent | recalculate evidence independence; do not count duplicate lineage |
| unresolved ambiguity discovered | mark affected answer-key dimensions `REVIEW_REQUIRED` |

## Weakest-link logic

For a chain of indispensable causal relations, the chain-level strength is capped by the weakest indispensable edge. This is a ceiling, not an automatic grade: even if every edge is `SUPPORTED`, unmodeled interactions or scope mismatch can justify a weaker pathway grade.

## Independent direct evidence exception

If independent evidence evaluates the complete pathway or downstream proposition directly, that evidence can support the downstream assertion independently of one weaker inferred intermediate link. Record both evidential routes.

## No vote counting

Three dependent articles citing one experiment are one origin. Three specialist modules consuming the same claim are one origin. Independence must be established at provenance level.

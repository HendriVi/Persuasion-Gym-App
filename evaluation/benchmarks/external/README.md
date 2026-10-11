# Official scientific benchmarks — acquisition registry

`BENCHMARK_REGISTRY.json` contains the nine externally published benchmarks previously recommended, with verified source links, native tasks, metric notes and commercial rights cautions. **The external underlying datasets are not included**. Rights differ across code, datasets and source documents; do not assume cloning a public GitHub repository authorizes commercial redistribution or training.

To view acquisition registry (offline):

```
python scripts/acquire_external.py --list
```

To clone **after reviewing licensing and obtaining authorization**:

```
python scripts/acquire_external.py --ids folio cladder --rights-reviewed
```

The script records commit hashes of acquired upstream code/data in a local uncommitted directory. AVeriTeC is marked restricted and will refuse ordinary commercial-package acquisition until separately acknowledged. This does not substitute for actually getting appropriate rights.

For model-agnostic evaluation, run original official scorers alongside the Persuasion Gym locked-rubric release controller. Scores from heterogeneous official tasks are **not interchangeable** with our own 95% per-case minimum release condition.

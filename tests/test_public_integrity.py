"""Public-only provenance checks. These are NOT tests of AI model accuracy."""
from __future__ import annotations
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class PublicSourceSafety(unittest.TestCase):
    def test_source_manifest_metadata_present(self):
        manifest = json.loads((ROOT / "SOURCE_ARTIFACT_MANIFEST.json").read_text())
        entries = manifest["source_members"]
        self.assertEqual(len(entries), 316)
        public = [e for e in entries if e["classification"].startswith("PUBLIC_")]
        self.assertEqual(len(public), 74)

    def test_no_restricted_paths_in_public_checkout(self):
        for path in ("offline-restricted", "vault", "benchmarks/internal", "gold_constraints", "holdout_gold_candidate"):
            self.assertFalse((ROOT / path).exists(), f"restricted path exposed: {path}")

    def test_training_seeds_are_ungraded(self):
        p = ROOT / "docs/features/social-identity-belonging/exercises.json"
        data = json.loads(p.read_text())
        self.assertFalse(data["graded_eligible"])
        self.assertFalse(data["contains_gold_answers"])
        self.assertFalse(data["contains_holdouts"])
        items = data["items"]
        self.assertEqual(len(items), 6)
        pair = [x for x in items if x.get("pair_id") == "sib-neutral-group-01"]
        self.assertEqual(len(pair), 2)
        self.assertEqual(pair[0]["independent_evidence"], pair[1]["independent_evidence"])
        self.assertEqual(pair[0]["questions"], pair[1]["questions"])

    def test_original_release_gate_not_activated(self):
        self.assertFalse((ROOT / "persuasion-gym/SKILL.md").exists())
        self.assertTrue((ROOT / "evaluation/config/release.json").is_file())

if __name__ == "__main__":
    unittest.main()

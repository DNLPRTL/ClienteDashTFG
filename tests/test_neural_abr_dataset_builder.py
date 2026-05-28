from __future__ import annotations

import tempfile
import unittest

from core.neural_abr.artifacts import read_json, read_jsonl
from core.neural_abr.constants import REQUIRED_DATASET_FILES, TRAIN_SPLIT
from core.neural_abr.dataset_builder import build_synthetic_smoke_dataset
from core.neural_abr.validation import validate_dataset_dir


class NeuralAbrDatasetBuilderTest(unittest.TestCase):
    def test_synthetic_smoke_dataset_writes_required_files_outside_repo(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            result = build_synthetic_smoke_dataset(temp_dir, overwrite=True)

            for filename in REQUIRED_DATASET_FILES:
                self.assertTrue((__import__("pathlib").Path(temp_dir) / filename).is_file())
            self.assertEqual(24, result["sample_counts"][TRAIN_SPLIT])
            report = validate_dataset_dir(temp_dir)
            self.assertEqual("PASS", report["status"])

    def test_manifest_marks_synthetic_smoke_as_diagnostic_only(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            build_synthetic_smoke_dataset(temp_dir, overwrite=True)
            manifest = read_json(__import__("pathlib").Path(temp_dir) / "dataset_manifest.json")
            train_rows = read_jsonl(__import__("pathlib").Path(temp_dir) / "train.jsonl")

            self.assertTrue(manifest["diagnostic_only"])
            self.assertTrue(manifest["not_benchmark"])
            self.assertNotIn("trace_id", train_rows[0]["context"])


if __name__ == "__main__":
    unittest.main()

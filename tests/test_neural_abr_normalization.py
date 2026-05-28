from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core.neural_abr.artifacts import read_jsonl
from core.neural_abr.constants import DATASET_FILENAMES, TRAIN_SPLIT, VALIDATION_SPLIT
from core.neural_abr.dataset_builder import build_synthetic_smoke_dataset
from core.neural_abr.normalization import FeatureNormalizer, NormalizationError


class NeuralAbrNormalizationTest(unittest.TestCase):
    def test_fit_uses_train_samples_only(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            build_synthetic_smoke_dataset(temp_dir, overwrite=True)
            train = read_jsonl(Path(temp_dir) / DATASET_FILENAMES[TRAIN_SPLIT])

            normalizer = FeatureNormalizer.fit_train(train)

            self.assertEqual(TRAIN_SPLIT, normalizer.stats.fitted_on_split)
            self.assertGreater(normalizer.stats.candidate_row_count, normalizer.stats.sample_count)

    def test_fit_rejects_validation_samples(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            build_synthetic_smoke_dataset(temp_dir, overwrite=True)
            validation = read_jsonl(Path(temp_dir) / DATASET_FILENAMES[VALIDATION_SPLIT])

            with self.assertRaises(NormalizationError):
                FeatureNormalizer.fit_train(validation)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core.neural_abr.artifacts import read_json, read_jsonl
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v3.profiles import Phase45V3DatasetProfile
from core.phase45_v3.throughput_quantile_dataset import (
    THROUGHPUT_QUANTILE_LEAKAGE_AUDIT_FILENAME,
    THROUGHPUT_QUANTILE_SUMMARY_FILENAME,
    THROUGHPUT_QUANTILE_TRAINING_DATA_FILENAME,
    THROUGHPUT_QUANTILE_VALIDATION_DATA_FILENAME,
    build_phase45_v3_throughput_quantile_dataset,
    validate_phase45_v3_throughput_quantile_dataset_dir,
)
from tests.test_phase45_v1_dataset import build_manifest_with_trace_files


class Phase45V3ThroughputQuantileDatasetTest(unittest.TestCase):
    def test_builds_valid_dataset_without_future_or_metadata_inputs(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = build_manifest_with_trace_files(root)
            output_dir = root / "datasets_normalizados" / "phase45_v3" / "unit_throughput_quantile"
            profile = Phase45V3DatasetProfile(
                name="unit",
                train_window_count=2,
                validation_window_count=1,
                qh_horizon_segments=3,
                qh_beam_width=4,
                max_windows_per_trace=1,
                synthetic_max_fraction=0.50,
                dataset_max_fraction=1.0,
                semantics_max_fraction=1.0,
                seed="unit-phase45-v3-throughput-quantile",
                rollouts_per_window=2,
            )

            result = build_phase45_v3_throughput_quantile_dataset(
                manifest,
                output_dir=output_dir,
                profile=profile,
                overwrite=True,
                horizon_segments=3,
                trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
            )
            validation = validate_phase45_v3_throughput_quantile_dataset_dir(output_dir)
            training_rows = read_jsonl(output_dir / THROUGHPUT_QUANTILE_TRAINING_DATA_FILENAME)
            validation_rows = read_jsonl(output_dir / THROUGHPUT_QUANTILE_VALIDATION_DATA_FILENAME)
            summary = read_json(output_dir / THROUGHPUT_QUANTILE_SUMMARY_FILENAME)
            leakage = read_json(output_dir / THROUGHPUT_QUANTILE_LEAKAGE_AUDIT_FILENAME)

            self.assertEqual("PASS", result["status"])
            self.assertEqual("PASS", validation["status"])
            self.assertEqual(120, len(training_rows))
            self.assertEqual(60, len(validation_rows))
            self.assertEqual(3, summary["horizon_segments"])
            self.assertEqual("PASS", leakage["status"])
            self.assertFalse(leakage["future_throughput_as_feature"])
            first = training_rows[0]
            self.assertNotIn("trace_id", first["model_inputs"]["context"])
            self.assertNotIn("future_throughput_bps", first["model_inputs"]["context"])
            self.assertTrue(first["throughput_quantile_targets"]["future_information_is_target_only"])
            self.assertFalse(first["metadata"]["metadata_is_model_input"])
            self.assertFalse(first["audit"]["rollout_action_is_model_target"])


if __name__ == "__main__":
    unittest.main()

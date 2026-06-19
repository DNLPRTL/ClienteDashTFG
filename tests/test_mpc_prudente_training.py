from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

try:
    import torch  # noqa: F401

    HAS_TORCH = True
except ImportError:  # pragma: no cover - torch optional on some envs
    HAS_TORCH = False


@unittest.skipUnless(HAS_TORCH, "torch required for predictor training")
class MpcPrudenteTrainingTest(unittest.TestCase):
    def test_trains_and_audits_calibration(self):
        from core.mpc_prudente.dataset import build_mpc_prudente_dataset
        from core.mpc_prudente.training import (
            MPC_PRUDENTE_CALIBRATION_REPORT_FILENAME,
            train_mpc_prudente_predictor,
        )
        from core.neural_abr.artifacts import read_json
        from core.phase45_v1.paths import PathRewriteRule
        from core.phase45_v3.neural_mpc_training import ThroughputQuantileTrainingProfile
        from core.phase45_v3.profiles import Phase45V3DatasetProfile
        from tests.test_mpc_prudente_dataset import _write_synthetic_media_profile
        from tests.test_phase45_v1_dataset import build_manifest_with_trace_files

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = build_manifest_with_trace_files(root)
            media_dir = root / "media_profiles" / "segment_sizes"
            _write_synthetic_media_profile(media_dir, "synthetic_test")
            dataset_dir = root / "datasets" / "mpc_prudente_unit"
            dataset_profile = Phase45V3DatasetProfile(
                name="unit",
                train_window_count=2,
                validation_window_count=1,
                qh_horizon_segments=3,
                qh_beam_width=4,
                max_windows_per_trace=1,
                synthetic_max_fraction=0.50,
                dataset_max_fraction=1.0,
                semantics_max_fraction=1.0,
                seed="unit-mpc-prudente-train",
                rollouts_per_window=2,
            )
            build_mpc_prudente_dataset(
                manifest,
                output_dir=dataset_dir,
                profile=dataset_profile,
                media_profile_id="synthetic_test",
                media_profile_base_dir=str(media_dir),
                overwrite=True,
                horizon_segments=3,
                trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
            )

            training_profile = ThroughputQuantileTrainingProfile(
                name="unit",
                epochs=2,
                batch_size=32,
                learning_rate=1.0e-3,
                hidden_sizes=(16,),
                quantiles=(0.10, 0.25, 0.50, 0.75),
                horizon_segments=3,
                seed=7,
            )
            output_dir = root / "modelos" / "mpc_prudente_unit"
            report = train_mpc_prudente_predictor(
                dataset_dir, output_dir, training_profile, overwrite=True, device="cpu"
            )

            self.assertIn(report["status"], ("PASS", "REVIEW"))
            calibration = report["calibration"]
            self.assertEqual(4, len(calibration["empirical_coverage_by_quantile"]))
            self.assertIn("coverage_calibrated", calibration["gates"]["gates"])
            self.assertIn("quantiles_monotone", calibration["gates"]["gates"])
            self.assertTrue((output_dir / MPC_PRUDENTE_CALIBRATION_REPORT_FILENAME).is_file())
            saved = read_json(output_dir / MPC_PRUDENTE_CALIBRATION_REPORT_FILENAME)
            self.assertEqual(4, len(saved["empirical_coverage_by_quantile"]))


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

try:
    import torch  # noqa: F401

    HAS_TORCH = True
except ImportError:  # pragma: no cover
    HAS_TORCH = False

from core.mpc_prudente.media_profile import MEDIA_PROFILE_SEGMENT_SIZES_SCHEMA_ID, MediaProfileSegmentSizes
from core.phase45_v3.abr_closed_loop_env import AbrClosedLoopState


def _media_profile(base_dir: Path, profile_id: str):
    base_dir.mkdir(parents=True, exist_ok=True)
    bitrates = (300000, 750000, 1200000, 1850000, 2850000, 4300000)
    reps = [{"bandwidth_bps": b, "segment_bytes": [int(b * 4.0 / 8.0)] * 8} for b in bitrates]
    descriptor = {
        "schema_id": MEDIA_PROFILE_SEGMENT_SIZES_SCHEMA_ID,
        "media_profile_id": profile_id,
        "segment_duration_s": 4.0,
        "segment_count": 8,
        "representations": reps,
    }
    (base_dir / (profile_id + ".json")).write_text(json.dumps(descriptor), encoding="utf-8")


def _state():
    return AbrClosedLoopState(
        segment_index=0,
        buffer_s=10.0,
        last_representation_index=-1,
        throughput_history_bps=(2_000_000.0, 2_100_000.0),
        download_time_history_s=(1.0,),
        recent_rebuffer_s=0.0,
        recent_switch_abs=0.0,
        network_time_s=0.0,
        total_segments=8,
    )


@unittest.skipUnless(HAS_TORCH, "torch required for runtime bundle")
class MpcPrudenteBundleTest(unittest.TestCase):
    def _write_training_output(self, train_dir: Path):
        import torch
        from core.neural_abr.constants import CONTEXT_VECTOR_NAMES
        from core.phase45_v3.neural_mpc_training import (
            THROUGHPUT_QUANTILE_MODEL_CONFIG_FILENAME,
            THROUGHPUT_QUANTILE_MODEL_FILENAME,
            THROUGHPUT_QUANTILE_NORMALIZATION_FILENAME,
        )
        from core.phase45_v3.throughput_quantile_model import (
            PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY,
            ThroughputQuantilePredictor,
        )

        train_dir.mkdir(parents=True, exist_ok=True)
        input_dim = len(CONTEXT_VECTOR_NAMES)
        model = ThroughputQuantilePredictor(
            input_dim=input_dim, horizon_segments=3, quantiles=(0.10, 0.25, 0.50, 0.75), hidden_sizes=(8,)
        )
        torch.save(
            {"model_key": PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY, "model_state_dict": model.state_dict()},
            train_dir / THROUGHPUT_QUANTILE_MODEL_FILENAME,
        )
        (train_dir / THROUGHPUT_QUANTILE_MODEL_CONFIG_FILENAME).write_text(
            json.dumps(dict(model.config())), encoding="utf-8"
        )
        (train_dir / THROUGHPUT_QUANTILE_NORMALIZATION_FILENAME).write_text(
            json.dumps({"context_mean": [0.0] * input_dim, "context_std": [1.0] * input_dim}), encoding="utf-8"
        )

    def test_export_validate_load_predict(self):
        from core.mpc_prudente.bundle import (
            MpcPrudenteRuntimeBundle,
            export_mpc_prudente_bundle,
            validate_mpc_prudente_bundle_dir,
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            train_dir = root / "train"
            self._write_training_output(train_dir)
            media_dir = root / "media_profiles" / "segment_sizes"
            _media_profile(media_dir, "synthetic_test")
            bundle_dir = root / "bundle"

            result = export_mpc_prudente_bundle(
                train_dir, bundle_dir, media_profile_id="synthetic_test", risk_alpha=0.75, overwrite=True
            )
            self.assertEqual("PASS", result["status"])
            self.assertEqual("PASS", validate_mpc_prudente_bundle_dir(bundle_dir)["status"])

            bundle = MpcPrudenteRuntimeBundle(bundle_dir)
            self.assertEqual(bundle.risk_alpha, 0.75)
            self.assertEqual(bundle.media_profile_id, "synthetic_test")

            ladder = MediaProfileSegmentSizes.load_by_id("synthetic_test", base_dir=str(media_dir)).to_faithful_ladder()
            prediction = bundle.predict(_state(), ladder)
            self.assertEqual(len(prediction), 3)  # horizon
            for row in prediction:
                self.assertEqual(len(row), 4)  # quantiles
                self.assertEqual(list(row), sorted(row))  # monótono

    def test_bundle_validation_detects_tampering(self):
        from core.mpc_prudente.bundle import (
            MpcPrudenteBundleError,
            export_mpc_prudente_bundle,
            validate_mpc_prudente_bundle_dir,
            BUNDLE_PLANNER_CONFIG_FILENAME,
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            train_dir = root / "train"
            self._write_training_output(train_dir)
            bundle_dir = root / "bundle"
            export_mpc_prudente_bundle(train_dir, bundle_dir, media_profile_id="x", overwrite=True)
            # alterar un archivo -> hash mismatch
            (bundle_dir / BUNDLE_PLANNER_CONFIG_FILENAME).write_text("{}", encoding="utf-8")
            with self.assertRaises(MpcPrudenteBundleError):
                validate_mpc_prudente_bundle_dir(bundle_dir)


class MpcPrudenteControllerRegistryTest(unittest.TestCase):
    def test_registered_and_falls_back_without_bundle(self):
        from core.controller.registry import create_controller

        controller = create_controller(
            "mpc_prudente_v1", {"bundle_dir": "/nonexistent/bundle", "verify_hashes": False}
        )
        controller.setPlayerFeedback({})
        rate = controller.calcControlAction()
        self.assertIsInstance(rate, float)
        self.assertEqual(int(controller._diagnostics.fallback_used), 1)


if __name__ == "__main__":
    unittest.main()

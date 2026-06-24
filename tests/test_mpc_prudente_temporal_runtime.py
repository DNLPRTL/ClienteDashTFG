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


@unittest.skipUnless(HAS_TORCH, "torch required for temporal runtime")
class MpcPrudenteTemporalRuntimeTest(unittest.TestCase):
    def _write_training_output(self, train_dir: Path, *, ensemble_size: int = 2, horizon: int = 3):
        import torch

        from core.mpc_prudente.temporal_model import (
            MPC_PRUDENTE_TEMPORAL_MODEL_KEY,
            SCALAR_FEATURE_NAMES,
            TemporalQuantilePredictor,
        )
        from core.mpc_prudente.temporal_training import (
            TEMPORAL_MODEL_CONFIG_FILENAME,
            TEMPORAL_MODEL_FILENAME,
            TEMPORAL_NORMALIZATION_FILENAME,
        )

        train_dir.mkdir(parents=True, exist_ok=True)
        quantiles = [0.10, 0.25, 0.50, 0.75]
        model_config = {
            "model_key": MPC_PRUDENTE_TEMPORAL_MODEL_KEY,
            "seq_features": 2,
            "scalar_dim": len(SCALAR_FEATURE_NAMES),
            "scalar_feature_names": list(SCALAR_FEATURE_NAMES),
            "horizon_segments": horizon,
            "quantiles": quantiles,
            "gru_hidden": 16,
            "gru_layers": 1,
            "mlp_hidden": [16],
            "dropout": 0.0,
            "ensemble_size": ensemble_size,
        }
        members = []
        for _ in range(ensemble_size):
            m = TemporalQuantilePredictor(
                seq_features=2, scalar_dim=len(SCALAR_FEATURE_NAMES), horizon_segments=horizon,
                quantiles=quantiles, gru_hidden=16, mlp_hidden=(16,), dropout=0.0,
            )
            members.append({k: v.detach().cpu() for k, v in m.state_dict().items()})
        norm = {
            "seq_mean": [0.0, 0.0], "seq_std": [1.0, 1.0],
            "scalar_mean": [0.0] * len(SCALAR_FEATURE_NAMES), "scalar_std": [1.0] * len(SCALAR_FEATURE_NAMES),
        }
        checkpoint = {
            "model_key": MPC_PRUDENTE_TEMPORAL_MODEL_KEY,
            "ensemble_size": ensemble_size,
            "downside_widen": 1.0,
            "model_config": model_config,
            "normalization": norm,
            "member_state_dicts": members,
        }
        torch.save(checkpoint, train_dir / TEMPORAL_MODEL_FILENAME)
        (train_dir / TEMPORAL_MODEL_CONFIG_FILENAME).write_text(json.dumps(model_config), encoding="utf-8")
        (train_dir / TEMPORAL_NORMALIZATION_FILENAME).write_text(json.dumps(norm), encoding="utf-8")

    def _media(self, media_dir: Path):
        from tests.test_mpc_prudente_dataset import _write_synthetic_media_profile

        _write_synthetic_media_profile(media_dir, "synthetic_test")

    def test_export_load_and_predict_temporal_bundle(self):
        from core.mpc_prudente.media_profile import MediaProfileSegmentSizes
        from core.mpc_prudente.temporal_bundle import (
            MpcPrudenteTemporalRuntimeBundle,
            export_mpc_prudente_temporal_bundle,
            load_prudent_runtime_bundle,
            validate_mpc_prudente_temporal_bundle_dir,
        )
        from core.phase45_v3.abr_closed_loop_env import AbrClosedLoopState

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            train_dir = root / "train"
            self._write_training_output(train_dir, horizon=3)
            media_dir = root / "media_profiles" / "segment_sizes"
            self._media(media_dir)
            bundle_dir = root / "bundle"

            export_mpc_prudente_temporal_bundle(
                train_dir, bundle_dir, media_profile_id="synthetic_test", risk_alpha=0.75, overwrite=True
            )
            self.assertEqual("PASS", validate_mpc_prudente_temporal_bundle_dir(bundle_dir)["status"])

            bundle = load_prudent_runtime_bundle(bundle_dir)
            self.assertIsInstance(bundle, MpcPrudenteTemporalRuntimeBundle)
            self.assertEqual(bundle.risk_alpha, 0.75)
            self.assertEqual(bundle.media_profile_id, "synthetic_test")

            ladder = MediaProfileSegmentSizes.load_by_id("synthetic_test", base_dir=str(media_dir)).to_faithful_ladder()
            state = AbrClosedLoopState(
                segment_index=2, buffer_s=10.0, last_representation_index=2,
                throughput_history_bps=(2_000_000.0, 2_500_000.0, 1_800_000.0),
                download_time_history_s=(1.0, 0.9, 1.2), recent_rebuffer_s=0.0, recent_switch_abs=0.0,
                network_time_s=8.0, total_segments=8,
            )
            rows = bundle.predict(state, ladder)
            self.assertEqual(len(rows), 3)  # horizon
            for row in rows:
                self.assertEqual(len(row), 4)  # quantiles
                self.assertTrue(all(v > 0 and v == v for v in row))  # positivos y finitos
                self.assertEqual(list(row), sorted(row))  # monótonos


if __name__ == "__main__":
    unittest.main()

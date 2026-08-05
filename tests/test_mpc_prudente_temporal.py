from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

try:
    import torch

    HAS_TORCH = True
except ImportError:  # pragma: no cover
    HAS_TORCH = False


@unittest.skipUnless(HAS_TORCH, "torch required")
class TemporalModelTest(unittest.TestCase):
    def test_forward_is_monotonic(self):
        from core.mpc_prudente.modelo_temporal import PredictorTemporalCuantiles

        model = PredictorTemporalCuantiles(
            seq_features=2, scalar_dim=7, horizon_segments=3, quantiles=(0.10, 0.25, 0.50, 0.75),
            gru_hidden=8, mlp_hidden=(8,), dropout=0.0,
        )
        out = model(torch.randn(4, 5, 2), torch.randn(4, 7))
        self.assertEqual(tuple(out.shape), (4, 3, 4))
        diffs = out[:, :, 1:] - out[:, :, :-1]
        self.assertTrue(bool((diffs >= -1e-6).all()))  # cuantiles monótonos

    def test_ensemble_widens_lower_tail(self):
        from core.mpc_prudente.modelo_temporal import combinar_cuantiles_ensemble

        preds = torch.randn(4, 2, 3, 4).sort(dim=3).values  # 4 miembros monótonos
        combined = combinar_cuantiles_ensemble(preds, (0.10, 0.25, 0.50, 0.75), downside_widen=1.0)
        self.assertEqual(tuple(combined.shape), (2, 3, 4))
        diffs = combined[:, :, 1:] - combined[:, :, :-1]
        self.assertTrue(bool((diffs >= -1e-6).all()))


@unittest.skipUnless(HAS_TORCH, "torch required")
class TemporalTrainingSmokeTest(unittest.TestCase):
    def test_trains_ensemble_and_audits_calibration(self):
        from core.mpc_prudente.dataset_fiel import construir_dataset_mpc_prudente
        from core.mpc_prudente.entrenamiento_temporal import (
            PerfilEntrenamientoTemporal,
            entrenar_ensemble_temporal_mpc_prudente,
        )
        from core.phase45_v1.paths import PathRewriteRule
        from core.phase45_v3.profiles import Phase45V3DatasetProfile
        from tests.test_mpc_prudente_dataset import _escribir_perfil_medio_sintetico
        from tests.test_phase45_v1_dataset import build_manifest_with_trace_files

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest = build_manifest_with_trace_files(root)
            media_dir = root / "media_profiles" / "segment_sizes"
            _escribir_perfil_medio_sintetico(media_dir, "synthetic_test")
            dataset_dir = root / "datasets" / "mpc_prudente_unit"
            dataset_profile = Phase45V3DatasetProfile(
                name="unit", train_window_count=2, validation_window_count=1, qh_horizon_segments=5,
                qh_beam_width=4, max_windows_per_trace=1, synthetic_max_fraction=0.5,
                dataset_max_fraction=1.0, semantics_max_fraction=1.0, seed="unit-temporal", rollouts_per_window=2,
            )
            construir_dataset_mpc_prudente(
                manifest, output_dir=dataset_dir, profile=dataset_profile,
                media_profile_id="synthetic_test", dir_base_perfiles=str(media_dir),
                overwrite=True, horizon_segments=5,
                trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
            )

            profile = PerfilEntrenamientoTemporal(
                name="unit", ensemble_size=2, epochs=2, batch_size=64, learning_rate=1.0e-3,
                gru_hidden=12, mlp_hidden=(12,), quantiles=(0.10, 0.25, 0.50, 0.75), horizon_segments=5, base_seed=1,
            )
            report = entrenar_ensemble_temporal_mpc_prudente(
                dataset_dir, root / "model", profile, overwrite=True, device="cpu"
            )
            self.assertIn(report["status"], ("PASS", "REVIEW"))
            self.assertEqual(len(report["members"]), 2)
            self.assertEqual(len(report["calibration"]["empirical_coverage_by_quantile"]), 4)


if __name__ == "__main__":
    unittest.main()

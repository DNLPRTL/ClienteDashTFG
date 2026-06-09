from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import torch

from core.phase45_v1.constants import (
    SPC_MODEL_CONFIG_FILENAME,
    SPC_MODEL_FILENAME,
    SPC_NORMALIZATION_FILENAME,
    SPC_TRAINING_REPORT_FILENAME,
    TRAINING_ROLE,
    VALIDATION_ROLE,
)
from core.phase45_v1.dataset import build_phase45_v1_dataset
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v1.profiles import DatasetProfile
from core.phase45_v1.spc_training import (
    SpcAbrV1Predictor,
    SpcTrainingProfile,
    examples_to_tensors,
    fit_spc_normalization,
    load_spc_examples,
    train_spc_abr_v1,
)
from tests.test_phase45_v1_dataset import build_manifest_with_trace_files


class Phase45V1SpcTrainingTest(unittest.TestCase):
    def test_builds_tensors_without_metadata_or_future_inputs(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir = build_unit_dataset(root)
            examples = load_spc_examples(dataset_dir / "datos_entrenamiento_spc_spbc.jsonl", TRAINING_ROLE, limit=16)
            normalization = fit_spc_normalization(examples)
            tensors = examples_to_tensors(examples, normalization)

            self.assertEqual(16, tensors[0].shape[0])
            self.assertEqual((16, 5, 2), tuple(tensors[0].shape))
            self.assertEqual((16, 7), tuple(tensors[1].shape))
            self.assertEqual((16, 6, 7), tuple(tensors[2].shape))
            self.assertEqual((16, 6), tuple(tensors[3].shape))
            self.assertEqual((16, 3), tuple(tensors[4].shape))
            self.assertEqual((16,), tuple(tensors[5].shape))
            self.assertEqual((16, 6), tuple(tensors[6].shape))
            self.assertFalse(hasattr(examples[0], "trace_id"))
            self.assertFalse(hasattr(examples[0], "oracle_action"))

    def test_model_forward_respects_candidate_shape_and_monotonic_quantiles(self):
        model = SpcAbrV1Predictor(
            history_hidden_size=8,
            state_hidden_size=8,
            candidate_hidden_size=8,
            shared_hidden_size=16,
            dropout=0.0,
        )
        sequence = torch.zeros((4, 5, 2), dtype=torch.float32)
        scalars = torch.zeros((4, 7), dtype=torch.float32)
        candidates = torch.zeros((4, 6, 7), dtype=torch.float32)
        mask = torch.ones((4, 6), dtype=torch.bool)

        output = model(sequence, scalars, candidates, mask)

        self.assertEqual((4, 3), tuple(output["quantile_log_kbps"].shape))
        self.assertEqual((4,), tuple(output["capacity_log_kbps"].shape))
        self.assertEqual((4, 6), tuple(output["risk_logits"].shape))
        quantiles = output["quantile_log_kbps"]
        self.assertTrue(torch.all(quantiles[:, 0] <= quantiles[:, 1]).item())
        self.assertTrue(torch.all(quantiles[:, 1] <= quantiles[:, 2]).item())

    def test_training_smoke_writes_external_checkpoint_and_report(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir = build_unit_dataset(root)
            model_dir = root / "modelos" / "phase45_v1" / "spc_abr_v1" / "unit"
            profile = SpcTrainingProfile(
                name="unit",
                epochs=1,
                batch_size=16,
                learning_rate=1.0e-3,
                max_training_samples=64,
                max_validation_samples=32,
                history_hidden_size=8,
                state_hidden_size=8,
                candidate_hidden_size=8,
                shared_hidden_size=16,
                dropout=0.0,
                seed=123,
            )

            report = train_spc_abr_v1(
                dataset_dir,
                model_dir,
                profile=profile,
                overwrite=True,
                device="cpu",
            )

            self.assertEqual("PASS", report["status"])
            self.assertTrue(report["ia_training_performed"])
            self.assertFalse(report["benchmark_performed"])
            self.assertFalse(report["bundle_exported"])
            self.assertFalse(report["controller_registered"])
            self.assertFalse(report["controller_integrated"])
            self.assertFalse(report["metadata_fields_are_model_features"])
            self.assertFalse(report["future_fields_are_model_features"])
            self.assertEqual(64, report["sample_counts_used"][TRAINING_ROLE])
            self.assertEqual(32, report["sample_counts_used"][VALIDATION_ROLE])
            self.assertIn("p50_mae_kbps", report["validation_metrics"])
            self.assertIn("risk_false_negative_rate", report["validation_metrics"])
            self.assertTrue((model_dir / SPC_MODEL_FILENAME).is_file())
            self.assertTrue((model_dir / SPC_MODEL_CONFIG_FILENAME).is_file())
            self.assertTrue((model_dir / SPC_NORMALIZATION_FILENAME).is_file())
            self.assertTrue((model_dir / SPC_TRAINING_REPORT_FILENAME).is_file())


def build_unit_dataset(root: Path) -> Path:
    manifest = build_manifest_with_trace_files(root)
    output_dir = root / "datasets_normalizados" / "phase45_v1" / "dataset"
    profile = DatasetProfile(
        name="unit",
        train_window_count=6,
        validation_window_count=2,
        oracle_horizon_segments=2,
        oracle_beam_width=3,
        future_horizon_segments=2,
        max_windows_per_trace=1,
        synthetic_max_fraction=0.50,
        dataset_max_fraction=1.0,
        semantics_max_fraction=1.0,
        seed="unit-spc-phase45-v1",
    )
    build_phase45_v1_dataset(
        manifest,
        output_dir=output_dir,
        profile=profile,
        overwrite=True,
        trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
    )
    return output_dir


if __name__ == "__main__":
    unittest.main()

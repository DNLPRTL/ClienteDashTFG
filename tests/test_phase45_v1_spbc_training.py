from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import torch

from core.phase45_v1.constants import (
    SPBC_MODEL_CONFIG_FILENAME,
    SPBC_MODEL_FILENAME,
    SPBC_NORMALIZATION_FILENAME,
    SPBC_TRAINING_REPORT_FILENAME,
    TRAINING_ROLE,
    VALIDATION_ROLE,
)
from core.phase45_v1.dataset import build_phase45_v1_dataset
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v1.profiles import DatasetProfile
from core.phase45_v1.spbc_training import (
    SpbcAbrV1Policy,
    SpbcTrainingProfile,
    compute_class_weighting,
    examples_to_tensors,
    fit_spbc_normalization,
    load_spbc_examples,
    train_spbc_abr_v1,
)
from tests.test_phase45_v1_dataset import build_manifest_with_trace_files


class Phase45V1SpbcTrainingTest(unittest.TestCase):
    def test_builds_tensors_without_metadata_future_audit_or_oracle_inputs(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir = build_unit_dataset(root)
            examples = load_spbc_examples(dataset_dir / "datos_entrenamiento_spc_spbc.jsonl", TRAINING_ROLE, limit=16)
            normalization = fit_spbc_normalization(examples)
            tensors = examples_to_tensors(examples, normalization)

            self.assertEqual(16, tensors[0].shape[0])
            self.assertEqual((16, 5, 2), tuple(tensors[0].shape))
            self.assertEqual((16, 7), tuple(tensors[1].shape))
            self.assertEqual((16, 6, 7), tuple(tensors[2].shape))
            self.assertEqual((16, 6), tuple(tensors[3].shape))
            self.assertEqual((16,), tuple(tensors[4].shape))
            self.assertEqual((16, 6), tuple(tensors[5].shape))
            self.assertFalse(hasattr(examples[0], "trace_id"))
            self.assertFalse(hasattr(examples[0], "future_throughput_kbps"))
            self.assertFalse(hasattr(examples[0], "classic_controllers"))
            self.assertFalse(hasattr(examples[0], "oracle_best_sequence"))
            self.assertIsInstance(examples[0].oracle_action, int)

    def test_model_forward_masks_invalid_candidate_logits(self):
        model = SpbcAbrV1Policy(
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
        mask[:, 5] = False

        output = model(sequence, scalars, candidates, mask)

        self.assertEqual((4, 6), tuple(output["action_logits"].shape))
        self.assertTrue(torch.all(output["action_logits"][:, 5] < -1.0e8).item())

    def test_class_weights_are_fitted_on_training_examples_only(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir = build_unit_dataset(root)
            training_examples = load_spbc_examples(dataset_dir / "datos_entrenamiento_spc_spbc.jsonl", TRAINING_ROLE, limit=64)
            validation_examples = load_spbc_examples(dataset_dir / "datos_validacion_spc_spbc.jsonl", VALIDATION_ROLE, limit=32)
            profile = SpbcTrainingProfile(
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

            weighting = compute_class_weighting(training_examples, 6, profile)

            self.assertEqual(TRAINING_ROLE, weighting["fitted_on"])
            self.assertFalse(weighting["metadata_used"])
            self.assertFalse(weighting["validation_used"])
            self.assertEqual(64, sum(int(value) for value in weighting["class_counts"].values()))
            self.assertNotEqual(len(training_examples) + len(validation_examples), sum(int(value) for value in weighting["class_counts"].values()))
            self.assertEqual(6, len(weighting["weights"]))

    def test_training_smoke_writes_external_checkpoint_and_report(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir = build_unit_dataset(root)
            model_dir = root / "modelos" / "phase45_v1" / "spbc_abr_v1" / "unit"
            profile = SpbcTrainingProfile(
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

            report = train_spbc_abr_v1(
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
            self.assertFalse(report["spc_checkpoint_used"])
            self.assertFalse(report["metadata_fields_are_model_features"])
            self.assertFalse(report["future_fields_are_model_features"])
            self.assertEqual(64, report["sample_counts_used"][TRAINING_ROLE])
            self.assertEqual(32, report["sample_counts_used"][VALIDATION_ROLE])
            self.assertIn("top1_accuracy", report["validation_metrics"])
            self.assertIn("balanced_accuracy", report["validation_metrics"])
            self.assertIn("predicted_action_risk_rate", report["validation_metrics"])
            self.assertTrue((model_dir / SPBC_MODEL_FILENAME).is_file())
            self.assertTrue((model_dir / SPBC_MODEL_CONFIG_FILENAME).is_file())
            self.assertTrue((model_dir / SPBC_NORMALIZATION_FILENAME).is_file())
            self.assertTrue((model_dir / SPBC_TRAINING_REPORT_FILENAME).is_file())


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
        seed="unit-spbc-phase45-v1",
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

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import torch

from core.neural_abr.artifacts import read_json
from core.phase45_v1.constants import (
    OFFLINE_VALIDATION_PREDICTIONS_FILENAME,
    OFFLINE_VALIDATION_REPORT_FILENAME,
    SPBC_CHECKPOINT_SCHEMA_ID,
    SPBC_MODEL_FILENAME,
    SPC_CHECKPOINT_SCHEMA_ID,
    SPC_MODEL_FILENAME,
    TRAINING_ROLE,
)
from core.phase45_v1.dataset import build_phase45_v1_dataset
from core.phase45_v1.offline_validation import (
    OfflineValidationProfile,
    apply_spc_guard,
    validate_spbc_spc_offline,
)
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v1.profiles import DatasetProfile
from core.phase45_v1.spbc_training import SpbcAbrV1Policy, fit_spbc_normalization, load_spbc_examples
from core.phase45_v1.spc_training import SpcAbrV1Predictor, fit_spc_normalization, load_spc_examples
from tests.test_phase45_v1_dataset import build_manifest_with_trace_files


class Phase45V1OfflineValidationTest(unittest.TestCase):
    def test_guard_downshifts_to_highest_safe_lower_action(self):
        decision = apply_spc_guard(
            proposed_action=5,
            action_mask=(True, True, True, True, True, True),
            risk_scores=(0.05, 0.10, 0.20, 0.70, 0.40, 0.90),
            risk_threshold=0.50,
        )

        self.assertEqual(4, decision.action)
        self.assertTrue(decision.guard_applied)
        self.assertEqual(1, decision.downshift_levels)
        self.assertFalse(decision.fallback_lowest_valid)
        self.assertAlmostEqual(0.90, decision.proposed_risk)
        self.assertAlmostEqual(0.40, decision.selected_risk)

    def test_guard_falls_back_to_lowest_valid_when_all_are_risky(self):
        decision = apply_spc_guard(
            proposed_action=4,
            action_mask=(False, True, True, True, True, True),
            risk_scores=(0.99, 0.80, 0.70, 0.90, 0.95, 0.60),
            risk_threshold=0.50,
        )

        self.assertEqual(1, decision.action)
        self.assertTrue(decision.guard_applied)
        self.assertTrue(decision.fallback_lowest_valid)
        self.assertEqual(3, decision.downshift_levels)

    def test_offline_validation_writes_report_with_antibenchmark_flags(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir = build_unit_dataset(root)
            spbc_checkpoint = build_spbc_checkpoint(root, dataset_dir)
            spc_checkpoint = build_spc_checkpoint(root, dataset_dir)
            output_dir = root / "modelos" / "phase45_v1" / "offline_validation" / "unit"
            profile = OfflineValidationProfile(name="unit", max_validation_samples=48, batch_size=16, seed=123)

            report = validate_spbc_spc_offline(
                dataset_dir,
                spbc_checkpoint,
                spc_checkpoint,
                output_dir,
                profile=profile,
                overwrite=True,
                device="cpu",
                validate_dataset=False,
            )
            stored_report = read_json(output_dir / OFFLINE_VALIDATION_REPORT_FILENAME)
            first_prediction = read_first_jsonl(output_dir / OFFLINE_VALIDATION_PREDICTIONS_FILENAME)

            self.assertEqual("PASS", report["status"])
            self.assertEqual("PASS", stored_report["status"])
            self.assertEqual(48, report["sample_counts_used"]["validation"])
            self.assertEqual(["spbc_only", "spbc_spc_guard", "oracle_reference"], report["variants"])
            self.assertIn("spbc_only", report["metrics"])
            self.assertIn("spbc_spc_guard", report["metrics"])
            self.assertIn("oracle_reference", report["metrics"])
            self.assertIn("guard_minus_spbc", report["comparison"])
            self.assertIn(report["offline_gate"]["status"], {"review_ready", "needs_adjustment"})
            self.assertFalse(report["benchmark_performed"])
            self.assertFalse(report["outputs_are_benchmark_results"])
            self.assertFalse(report["ranking_performed"])
            self.assertFalse(report["ia_training_performed"])
            self.assertFalse(report["bundle_exported"])
            self.assertFalse(report["controller_registered"])
            self.assertFalse(report["controller_integrated"])
            self.assertFalse(report["phase6_executed"])
            self.assertFalse(report["qoe_improvement_claimed"])
            self.assertFalse(report["metadata_fields_are_model_features"])
            self.assertFalse(report["future_fields_are_model_features"])
            self.assertFalse(report["oracle_fields_are_model_features"])
            self.assertEqual(0.0, report["metrics"]["spbc_only"]["invalid_action_rate"])
            self.assertEqual(0.0, report["metrics"]["spbc_spc_guard"]["invalid_action_rate"])
            self.assertTrue((output_dir / OFFLINE_VALIDATION_REPORT_FILENAME).is_file())
            self.assertTrue((output_dir / OFFLINE_VALIDATION_PREDICTIONS_FILENAME).is_file())
            self.assertIn("spbc_action", first_prediction)
            self.assertIn("guarded_action", first_prediction)
            self.assertNotIn("model_inputs", first_prediction)
            self.assertNotIn("future_throughput_kbps", first_prediction)
            self.assertNotIn("classic_controllers", first_prediction)


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
        seed="unit-offline-validation-phase45-v1",
    )
    build_phase45_v1_dataset(
        manifest,
        output_dir=output_dir,
        profile=profile,
        overwrite=True,
        trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
    )
    return output_dir


def build_spbc_checkpoint(root: Path, dataset_dir: Path) -> Path:
    checkpoint_dir = root / "modelos" / "phase45_v1" / "spbc_abr_v1" / "unit"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_path = checkpoint_dir / SPBC_MODEL_FILENAME
    examples = load_spbc_examples(dataset_dir / "datos_entrenamiento_spc_spbc.jsonl", TRAINING_ROLE, limit=64)
    normalization = fit_spbc_normalization(examples).to_json()
    model = SpbcAbrV1Policy(
        history_hidden_size=8,
        state_hidden_size=8,
        candidate_hidden_size=8,
        shared_hidden_size=16,
        dropout=0.0,
    )
    torch.save(
        {
            "schema_id": SPBC_CHECKPOINT_SCHEMA_ID,
            "model_key": "spbc_abr_v1",
            "model_state_dict": model.state_dict(),
            "model_config": dict(model.config()),
            "normalization": normalization,
            "training_profile": {"name": "unit"},
            "best_epoch": 0,
            "device_used": "cpu",
            "controller_registered": False,
            "bundle_exported": False,
        },
        checkpoint_path,
    )
    return checkpoint_path


def build_spc_checkpoint(root: Path, dataset_dir: Path) -> Path:
    checkpoint_dir = root / "modelos" / "phase45_v1" / "spc_abr_v1" / "unit"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_path = checkpoint_dir / SPC_MODEL_FILENAME
    examples = load_spc_examples(dataset_dir / "datos_entrenamiento_spc_spbc.jsonl", TRAINING_ROLE, limit=64)
    normalization = fit_spc_normalization(examples).to_json()
    model = SpcAbrV1Predictor(
        history_hidden_size=8,
        state_hidden_size=8,
        candidate_hidden_size=8,
        shared_hidden_size=16,
        dropout=0.0,
    )
    torch.save(
        {
            "schema_id": SPC_CHECKPOINT_SCHEMA_ID,
            "model_key": "spc_abr_v1",
            "model_state_dict": model.state_dict(),
            "model_config": dict(model.config()),
            "normalization": normalization,
            "training_profile": {"name": "unit"},
            "best_epoch": 0,
            "device_used": "cpu",
            "controller_registered": False,
            "bundle_exported": False,
        },
        checkpoint_path,
    )
    return checkpoint_path


def read_first_jsonl(path: Path) -> dict[str, object]:
    with path.open("r", encoding="utf-8") as handle:
        return json.loads(next(handle))


if __name__ == "__main__":
    unittest.main()

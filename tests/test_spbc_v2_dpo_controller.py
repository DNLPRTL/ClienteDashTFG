from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import torch

from core.controller.registry import CONTROLLER_REGISTRY, available_controllers, create_controller
from core.neural_abr.artifacts import read_json, write_json
from core.phase45_v1.spbc_training import CANDIDATE_FEATURES, SCALAR_FEATURES, SEQUENCE_FEATURES
from core.phase45_v1.spbc_v2_dpo_bundle import (
    SPBC_V2_DPO_BUNDLE_MODEL_CARD_FILENAME,
    SPBC_V2_DPO_CONTROLLER_KEY,
    export_spbc_v2_dpo_inference_bundle,
    validate_spbc_v2_dpo_bundle_dir,
)
from core.phase45_v1.spbc_v2_dpo_training import (
    SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID,
    SPBC_V2_DPO_MODEL_KEY,
    SpbcAbrV2DpoPolicy,
)
from core.fase6.catalogo import descubrir_controllers_comparables
from tests.spbc_v2_dpo_bundle_utils import build_minimal_spbc_v2_dpo_bundle, minimal_spbc_feedback


def _training_normalization() -> dict[str, object]:
    return {
        "schema_id": "phase45_v2_spbc_dpo_normalization_v1",
        "fitted_on_data_role": "training",
        "source": "unit_test_stub",
        "sequence_features": list(SEQUENCE_FEATURES),
        "scalar_features": list(SCALAR_FEATURES),
        "candidate_features": list(CANDIDATE_FEATURES),
        "sequence_mean": [0.0 for _ in SEQUENCE_FEATURES],
        "sequence_std": [1.0 for _ in SEQUENCE_FEATURES],
        "scalar_mean": [0.0 for _ in SCALAR_FEATURES],
        "scalar_std": [1.0 for _ in SCALAR_FEATURES],
        "candidate_mean": [0.0 for _ in CANDIDATE_FEATURES],
        "candidate_std": [1.0 for _ in CANDIDATE_FEATURES],
        "sample_count": 1,
        "candidate_row_count": 3,
        "metadata_fields_used": False,
        "future_fields_used_as_inputs": False,
        "oracle_fields_used_as_inputs": False,
        "preference_targets_used_as_inputs": False,
        "validation_used": False,
    }


class SpbcV2DpoControllerTest(unittest.TestCase):
    def test_controller_is_registered_and_phase6_visible(self):
        available = {spec.key for spec in available_controllers()}
        self.assertIn(SPBC_V2_DPO_CONTROLLER_KEY, CONTROLLER_REGISTRY)
        self.assertIn(SPBC_V2_DPO_CONTROLLER_KEY, available)

        discovered = {item["controller_key"]: item for item in descubrir_controllers_comparables({})}
        self.assertIn(SPBC_V2_DPO_CONTROLLER_KEY, discovered)
        self.assertEqual("propio_spbc_v2_anchor", discovered[SPBC_V2_DPO_CONTROLLER_KEY]["alias"])

    def test_missing_bundle_falls_back_to_classical_controller(self):
        controller = create_controller(SPBC_V2_DPO_CONTROLLER_KEY)
        feedback = controller.augment_feedback(minimal_spbc_feedback())
        controller.setPlayerFeedback(feedback)

        selected_rate = controller.calcControlAction()
        diagnostics = controller.get_neural_diagnostics()

        self.assertIn(selected_rate, feedback["rates"])
        self.assertEqual(1, diagnostics["neural_fallback_used"])
        self.assertEqual("missing_bundle_dir", diagnostics["neural_fallback_reason"])
        self.assertEqual(1, diagnostics["neural_valid_action"])

    def test_valid_bundle_scores_without_fallback(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = build_minimal_spbc_v2_dpo_bundle(temp_dir)
            controller = create_controller(
                SPBC_V2_DPO_CONTROLLER_KEY,
                {"bundle_dir": str(bundle_dir), "max_inference_latency_ms": 1000.0},
            )
            feedback = controller.augment_feedback(minimal_spbc_feedback())
            controller.setPlayerFeedback(feedback)

            selected_rate = controller.calcControlAction()
            diagnostics = controller.get_neural_diagnostics()

            self.assertIn(selected_rate, feedback["rates"])
            self.assertEqual(0, diagnostics["neural_fallback_used"])
            self.assertEqual("success_neural", diagnostics["neural_fallback_reason"])
            self.assertEqual(1, diagnostics["neural_bundle_loaded"])
            self.assertEqual(1, diagnostics["neural_bundle_hash_ok"])
            self.assertEqual(1, diagnostics["neural_feature_vector_ok"])
            self.assertEqual(1, diagnostics["neural_valid_action"])

    def test_bundle_validation_detects_hash_mismatch(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = build_minimal_spbc_v2_dpo_bundle(temp_dir)
            write_json(bundle_dir / SPBC_V2_DPO_BUNDLE_MODEL_CARD_FILENAME, {"tampered": True})

            with self.assertRaises(Exception) as ctx:
                validate_spbc_v2_dpo_bundle_dir(bundle_dir)

            self.assertIn("sha256 mismatch", str(ctx.exception))

    def test_single_representation_is_safe_without_loading_bundle(self):
        controller = create_controller(SPBC_V2_DPO_CONTROLLER_KEY)
        feedback = minimal_spbc_feedback()
        feedback["rates"] = [37500.0]
        feedback["max_level"] = 0
        feedback["max_rate"] = 37500.0
        feedback["max_bitrate"] = 37500.0
        feedback = controller.augment_feedback(feedback)
        controller.setPlayerFeedback(feedback)

        selected_rate = controller.calcControlAction()
        diagnostics = controller.get_neural_diagnostics()

        self.assertEqual(37500.0, selected_rate)
        self.assertEqual(0, diagnostics["neural_fallback_used"])
        self.assertEqual("single_representation", diagnostics["neural_fallback_reason"])

    def test_exporter_writes_valid_bundle_from_checkpoint(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source_dir = root / "modelos" / "phase45_v1" / "spbc_abr_v2_dpo" / "stub"
            source_dir.mkdir(parents=True)
            checkpoint = source_dir / "modelo_spbc_abr_v2_dpo.pt"
            training_report = source_dir / "reporte_entrenamiento_spbc_abr_v2_dpo.json"
            model = SpbcAbrV2DpoPolicy(
                history_hidden_size=8,
                state_hidden_size=8,
                candidate_hidden_size=8,
                shared_hidden_size=16,
                dropout=0.0,
            )
            torch.save(
                {
                    "schema_id": SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID,
                    "model_key": SPBC_V2_DPO_MODEL_KEY,
                    "model_state_dict": model.state_dict(),
                    "model_config": model.config(),
                    "normalization": _training_normalization(),
                    "training_profile": {"name": "unit"},
                    "best_epoch": 1,
                    "safety_gate_enabled": True,
                    "controller_registered": False,
                    "bundle_exported": False,
                },
                checkpoint,
            )
            write_json(
                training_report,
                {
                    "schema_id": "phase45_v2_spbc_dpo_training_report_v1",
                    "status": "PASS",
                    "validation_metrics": {"over_aggressive_rate_vs_oracle": 0.0},
                    "benchmark_performed": False,
                    "ranking_performed": False,
                },
            )
            output_dir = root / "modelos" / "phase45_v1" / "spbc_abr_v2_dpo" / "stub_bundle"

            report = export_spbc_v2_dpo_inference_bundle(
                checkpoint_path=checkpoint,
                training_report_path=training_report,
                output_dir=output_dir,
            )
            manifest_validation = validate_spbc_v2_dpo_bundle_dir(output_dir)
            export_report = read_json(output_dir / "reporte_export_bundle_spbc_abr_v2_dpo.json")

            self.assertEqual("PASS", report["status"])
            self.assertEqual("PASS", manifest_validation["status"])
            self.assertFalse(export_report["benchmark_performed"])
            self.assertFalse(export_report["ranking_performed"])


if __name__ == "__main__":
    unittest.main()

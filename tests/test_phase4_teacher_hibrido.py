from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core.neural_abr.artifacts import read_json, read_jsonl
from core.neural_abr.bundle_validation import validate_phase4_inference_bundle
from core.neural_abr.candidate_readiness import assess_phase4_candidate_model
from core.neural_abr.constants import (
    BUNDLE_MODEL_CARD_FILENAME,
    DATA_FILENAMES,
    HYBRID_TEACHER,
    LABEL_SCHEMA_FILENAME,
    TRAINING_ROLE,
    VALIDATION_ROLE,
)
from core.neural_abr.export_bundle import export_phase4_inference_bundle
from core.neural_abr.hybrid_training_data import (
    HYBRID_TEACHER_AUDIT_FILENAME,
    build_phase4_hybrid_teacher_data_from_plan,
    validate_phase4_hybrid_teacher_data_dir,
)
from core.neural_abr.model_training import train_phase4_candidate_model
from core.neural_abr.trace_sampling import Phase4SamplingConfig, build_phase4_training_trace_artifacts
from core.neural_abr.training_data_validation import TrainingDataValidationError, validate_phase4_training_data_dir
from tests.test_phase4_datos_entrenamiento import build_manifest_with_trace_files


class Phase4TeacherHibridoTest(unittest.TestCase):
    def test_builds_hybrid_teacher_data_without_vmaf_or_feature_leakage(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            plan = _build_small_plan(root)
            data_dir = root / "phase4H_datos_teacher_hibrido_sin_vmaf"

            result = build_phase4_hybrid_teacher_data_from_plan(
                plan,
                output_dir=data_dir,
                overwrite=True,
                max_training_windows=2,
                max_validation_windows=1,
            )
            report = validate_phase4_hybrid_teacher_data_dir(data_dir)
            label_schema = read_json(data_dir / LABEL_SCHEMA_FILENAME)
            audit = read_json(data_dir / HYBRID_TEACHER_AUDIT_FILENAME)
            training_rows = read_jsonl(data_dir / DATA_FILENAMES[TRAINING_ROLE])

            self.assertEqual("PASS", result["status"])
            self.assertEqual("PASS", report["status"])
            self.assertEqual(HYBRID_TEACHER, label_schema["teacher_policy"])
            self.assertEqual(60, len(training_rows))
            self.assertFalse(result["summary"]["vmaf_used"])
            self.assertTrue(result["summary"]["teacher_selection_for_training_labels"])
            self.assertFalse(result["summary"]["benchmark_performed"])
            self.assertEqual("PASS", audit["status"])
            self.assertIn(training_rows[0]["label"]["hybrid_source_teacher"], result["summary"]["hybrid_source_teachers"])
            self.assertNotIn("trace_id", training_rows[0]["context_features"])
            self.assertNotIn("hybrid_source_teacher", training_rows[0]["context_features"])
            self.assertNotIn("dataset_id", training_rows[0]["candidate_features"][0])
            self.assertIn("trace_id", training_rows[0]["metadata"])

            with self.assertRaises(TrainingDataValidationError):
                validate_phase4_training_data_dir(data_dir)

    def test_hybrid_teacher_model_can_train_review_export_and_validate_bundle(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            plan = _build_small_plan(root)
            data_dir = root / "phase4H_datos_teacher_hibrido_sin_vmaf"
            model_dir = root / "phase4H_modelo_teacher_hibrido_neural_abr_lite"
            bundle_dir = root / "phase4H_bundle_para_inferencia_teacher_hibrido_neural_abr_lite"
            run_dir = root / "phase4H_validacion_bundle_teacher_hibrido"
            build_phase4_hybrid_teacher_data_from_plan(
                plan,
                output_dir=data_dir,
                overwrite=True,
                max_training_windows=2,
                max_validation_windows=1,
            )

            training_report = train_phase4_candidate_model(
                data_dir,
                output_dir=model_dir,
                overwrite=True,
                epochs=1,
                batch_size=8,
                max_training_samples=24,
                max_validation_samples=12,
                seed=17,
                label_teacher=HYBRID_TEACHER,
                phase_name="phase4h_entrenamiento_modelo_teacher_hibrido_offline",
                feature_source="phase4H_datos_teacher_hibrido_sin_vmaf",
            )
            review = assess_phase4_candidate_model(
                model_dir,
                data_dir=data_dir,
                min_training_samples=1,
                min_validation_samples=1,
                min_training_teacher_agreement=0.0,
                min_validation_teacher_agreement=0.0,
                label_teacher=HYBRID_TEACHER,
                decision_ready="PHASE4H_MODELO_TEACHER_HIBRIDO_READY_FOR_EXPORT",
            )
            export_report = export_phase4_inference_bundle(
                model_dir=model_dir,
                data_dir=data_dir,
                output_dir=bundle_dir,
                overwrite=True,
            )
            validation = validate_phase4_inference_bundle(
                bundle_dir=bundle_dir,
                data_dir=data_dir,
                output_dir=run_dir,
                max_samples=8,
            )
            model_card = read_json(bundle_dir / BUNDLE_MODEL_CARD_FILENAME)

            self.assertEqual("PASS", training_report["status"])
            self.assertEqual(HYBRID_TEACHER, training_report["label_teacher"])
            self.assertIn(review["status"], {"PASS", "PASS_NOT_CANDIDATE"})
            self.assertEqual([], review["hard_failures"])
            self.assertEqual(HYBRID_TEACHER, export_report["label_teacher"])
            self.assertEqual(HYBRID_TEACHER, model_card["teacher"])
            self.assertNotEqual("BLOCKED_NEEDS_FIX", validation["status"])
            self.assertEqual(1.0, validation["inference_smoke_report"]["valid_action_rate"])


def _build_small_plan(root: Path) -> dict[str, object]:
    manifest = build_manifest_with_trace_files(root)
    return build_phase4_training_trace_artifacts(
        manifest,
        config=Phase4SamplingConfig(
            train_window_count=4,
            validation_window_count=2,
            synthetic_max_fraction=1.0,
            dataset_max_fraction=1.0,
            semantics_max_fraction=1.0,
            difficulty_max_fraction=1.0,
            max_windows_per_trace=1,
            seed="teacher-hibrido-test",
        ),
    )["phase4_plan_de_trazas_para_entrenamiento.json"]


if __name__ == "__main__":
    unittest.main()

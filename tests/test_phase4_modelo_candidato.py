from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core.neural_abr.artifacts import read_json
from core.neural_abr.candidate_readiness import assess_phase4_candidate_model
from core.neural_abr.constants import (
    CANDIDATE_MODEL_FILENAME,
    CANDIDATE_REVIEW_REPORT_FILENAME,
    FORMAL_TRAINING_REPORT_FILENAME,
)
from core.neural_abr.model_training import load_phase4_candidate_model, train_phase4_candidate_model
from core.neural_abr.trace_sampling import Phase4SamplingConfig, build_phase4_training_trace_artifacts
from core.neural_abr.training_data import build_phase4_training_data_from_plan
from tests.test_phase4_datos_entrenamiento import build_manifest_with_trace_files


class Phase4ModeloCandidatoTest(unittest.TestCase):
    def test_formal_training_writes_external_candidate_model_and_review(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = build_manifest_with_trace_files(root)
            plan = build_phase4_training_trace_artifacts(
                manifest,
                config=Phase4SamplingConfig(
                    train_window_count=4,
                    validation_window_count=2,
                    synthetic_max_fraction=1.0,
                    dataset_max_fraction=1.0,
                    semantics_max_fraction=1.0,
                    difficulty_max_fraction=1.0,
                    max_windows_per_trace=1,
                    seed="modelo-candidato-test",
                ),
            )["phase4_plan_de_trazas_para_entrenamiento.json"]
            data_dir = root / "phase4B_datos_para_entrenamiento"
            model_dir = root / "phase4E_modelo_candidato_neural_abr_lite"
            build_phase4_training_data_from_plan(
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
                seed=11,
            )
            model, normalizer, checkpoint = load_phase4_candidate_model(model_dir)
            review = assess_phase4_candidate_model(
                model_dir,
                data_dir=data_dir,
                min_training_samples=1,
                min_validation_samples=1,
                min_training_teacher_agreement=0.0,
                min_validation_teacher_agreement=0.0,
            )

            self.assertEqual("PASS", training_report["status"])
            self.assertTrue(training_report["ia_training_performed"])
            self.assertFalse(training_report["benchmark_performed"])
            self.assertFalse(training_report["controller_integrated"])
            self.assertEqual(1.0, training_report["validation_metrics"]["valid_action_rate"])
            self.assertTrue((model_dir / CANDIDATE_MODEL_FILENAME).is_file())
            self.assertTrue((model_dir / FORMAL_TRAINING_REPORT_FILENAME).is_file())
            self.assertTrue((model_dir / CANDIDATE_REVIEW_REPORT_FILENAME).is_file())
            self.assertIn(review["status"], {"PASS", "PASS_NOT_CANDIDATE"})
            self.assertEqual([], review["hard_failures"])
            self.assertEqual("cpu", checkpoint["device"])
            self.assertEqual(model.context_dim, len(normalizer.stats.mean) - model.candidate_dim)
            saved_review = read_json(model_dir / CANDIDATE_REVIEW_REPORT_FILENAME)
            self.assertFalse(saved_review["ranking_performed"])


if __name__ == "__main__":
    unittest.main()

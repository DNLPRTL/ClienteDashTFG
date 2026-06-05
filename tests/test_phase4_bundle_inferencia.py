from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core.neural_abr.artifacts import read_json, write_json
from core.neural_abr.bundle import BundleError, validate_phase4_bundle_dir
from core.neural_abr.bundle_validation import validate_phase4_inference_bundle
from core.neural_abr.candidate_readiness import assess_phase4_candidate_model
from core.neural_abr.constants import (
    BUNDLE_MANIFEST_FILENAME,
    BUNDLE_MODEL_CARD_FILENAME,
    BUNDLE_MODEL_FILENAME,
    FEATURE_SCHEMA_FILENAME,
    NORMALIZATION_STATS_FILENAME,
)
from core.neural_abr.export_bundle import export_phase4_inference_bundle
from core.neural_abr.inference import load_phase4_inference_bundle, run_phase4_inference_smoke
from core.neural_abr.model_training import train_phase4_candidate_model
from core.neural_abr.trace_sampling import Phase4SamplingConfig, build_phase4_training_trace_artifacts
from core.neural_abr.training_data import build_phase4_training_data_from_plan
from tests.test_phase4_datos_entrenamiento import build_manifest_with_trace_files


class Phase4BundleInferenciaTest(unittest.TestCase):
    def test_exports_validates_and_scores_bundle(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            data_dir, model_dir = _build_ready_candidate(root)
            bundle_dir = root / "phase4F_bundle_para_inferencia_neural_abr_lite"
            validation_dir = root / "phase4F_validacion_bundle_inferencia"

            export_report = export_phase4_inference_bundle(
                model_dir=model_dir,
                data_dir=data_dir,
                output_dir=bundle_dir,
                overwrite=True,
            )
            bundle_report = validate_phase4_bundle_dir(bundle_dir)
            validation_report = validate_phase4_inference_bundle(
                bundle_dir=bundle_dir,
                data_dir=data_dir,
                output_dir=validation_dir,
                max_samples=8,
                latency_p95_limit_ms=1000.0,
            )
            smoke_report = run_phase4_inference_smoke(bundle_dir, data_dir, max_samples=4)
            engine = load_phase4_inference_bundle(bundle_dir)

            self.assertEqual("PASS", export_report["status"])
            self.assertEqual("PASS", bundle_report["status"])
            self.assertEqual("PASS", validation_report["status"])
            self.assertEqual(1.0, smoke_report["valid_action_rate"])
            self.assertEqual(1.0, smoke_report["deterministic_rate"])
            self.assertFalse(read_json(bundle_dir / BUNDLE_MANIFEST_FILENAME)["ranking_performed"])
            self.assertTrue((bundle_dir / BUNDLE_MODEL_FILENAME).is_file())
            self.assertTrue((bundle_dir / NORMALIZATION_STATS_FILENAME).is_file())
            self.assertTrue((bundle_dir / FEATURE_SCHEMA_FILENAME).is_file())
            self.assertFalse(engine.manifest["controller_integrated"])

    def test_manifest_hash_detects_tampered_bundle_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            data_dir, model_dir = _build_ready_candidate(root)
            bundle_dir = root / "phase4F_bundle_para_inferencia_neural_abr_lite"
            export_phase4_inference_bundle(
                model_dir=model_dir,
                data_dir=data_dir,
                output_dir=bundle_dir,
                overwrite=True,
            )
            write_json(bundle_dir / BUNDLE_MODEL_CARD_FILENAME, {"tampered": True})

            with self.assertRaises(BundleError):
                validate_phase4_bundle_dir(bundle_dir)


def _build_ready_candidate(root: Path) -> tuple[Path, Path]:
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
            seed="bundle-inferencia-test",
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
    train_phase4_candidate_model(
        data_dir,
        output_dir=model_dir,
        overwrite=True,
        epochs=1,
        batch_size=8,
        max_training_samples=24,
        max_validation_samples=12,
        seed=19,
    )
    assess_phase4_candidate_model(
        model_dir,
        data_dir=data_dir,
        min_training_samples=1,
        min_validation_samples=1,
        min_training_teacher_agreement=0.0,
        min_validation_teacher_agreement=0.0,
    )
    return data_dir, model_dir


if __name__ == "__main__":
    unittest.main()

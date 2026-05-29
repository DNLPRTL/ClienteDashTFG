from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import torch

import scripts.validate_neural_abr_bundle as bundle_validator
from core.neural_abr.bundle import REQUIRED_BUNDLE_FILES, write_json_file
from core.neural_abr.constants import CANDIDATE_VECTOR_NAMES, CONTEXT_VECTOR_NAMES, NORMALIZATION_SCHEMA_VERSION, TRAIN_SPLIT
from core.neural_abr.dataset_builder import build_synthetic_smoke_dataset
from core.neural_abr.export import export_neural_abr_bundle
from core.neural_abr.model import NeuralAbrLiteCandidateScorer


class NeuralAbrExportTest(unittest.TestCase):
    def test_export_cli_accepts_required_arguments_using_temp_fixture(self):
        repo_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir, run_dir, validation_dir, assessment_dir = _write_phase4e2_source_fixture(root)
            bundle_dir = root / "bundle"
            docs_dir = root / "docs"

            command = [
                sys.executable,
                "scripts/export_neural_abr_model.py",
                "--dataset-dir",
                str(dataset_dir),
                "--run-dir",
                str(run_dir),
                "--validation-dir",
                str(validation_dir),
                "--assessment-dir",
                str(assessment_dir),
                "--output-dir",
                str(bundle_dir),
                "--phase",
                "phase4f",
                "--overwrite",
                "--docs-dir",
                str(docs_dir),
            ]
            completed = subprocess.run(command, cwd=repo_root, text=True, capture_output=True, check=False)

            self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
            for filename in REQUIRED_BUNDLE_FILES:
                self.assertTrue((bundle_dir / filename).is_file(), filename)
            self.assertTrue((docs_dir / "phase4f_export_report.md").is_file())

    def test_validate_cli_exits_zero_for_minimal_valid_fixture(self):
        repo_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir, run_dir, validation_dir, assessment_dir = _write_phase4e2_source_fixture(root)
            bundle_dir = root / "bundle"
            export_neural_abr_bundle(
                dataset_dir=dataset_dir,
                run_dir=run_dir,
                validation_dir=validation_dir,
                assessment_dir=assessment_dir,
                output_dir=bundle_dir,
                phase="phase4f",
                overwrite=True,
                docs_dir=root / "export_docs",
            )
            output_dir = root / "bundle_validation"
            docs_dir = root / "validation_docs"

            command = [
                sys.executable,
                "scripts/validate_neural_abr_bundle.py",
                "--bundle-dir",
                str(bundle_dir),
                "--dataset-dir",
                str(dataset_dir),
                "--output-dir",
                str(output_dir),
                "--phase",
                "phase4f",
                "--docs-dir",
                str(docs_dir),
            ]
            completed = subprocess.run(command, cwd=repo_root, text=True, capture_output=True, check=False)

            self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
            self.assertTrue((output_dir / "bundle_validation_report.json").is_file())
            self.assertTrue((docs_dir / "phase4f_bundle_validation_report.md").is_file())
            report = json.loads((output_dir / "bundle_validation_report.json").read_text(encoding="utf-8"))
            self.assertEqual("NOT_CHECKED", report["gates"]["no_repo_artifacts"]["status"])
            self.assertNotIn("no_repo_artifacts", report["hard_failures"])

    def test_validate_cli_blocks_missing_required_bundle_file(self):
        repo_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir, run_dir, validation_dir, assessment_dir = _write_phase4e2_source_fixture(root)
            bundle_dir = root / "bundle"
            export_neural_abr_bundle(
                dataset_dir=dataset_dir,
                run_dir=run_dir,
                validation_dir=validation_dir,
                assessment_dir=assessment_dir,
                output_dir=bundle_dir,
                phase="phase4f",
                overwrite=True,
                docs_dir=root / "export_docs",
            )
            (bundle_dir / "fallback_policy.json").unlink()
            output_dir = root / "bundle_validation"

            command = [
                sys.executable,
                "scripts/validate_neural_abr_bundle.py",
                "--bundle-dir",
                str(bundle_dir),
                "--dataset-dir",
                str(dataset_dir),
                "--output-dir",
                str(output_dir),
                "--phase",
                "phase4f",
                "--docs-dir",
                str(root / "validation_docs"),
            ]
            completed = subprocess.run(command, cwd=repo_root, text=True, capture_output=True, check=False)

            self.assertEqual(1, completed.returncode, completed.stdout + completed.stderr)
            self.assertIn("PHASE4F_BLOCKED_NEEDS_FIX", completed.stdout)

    def test_explicit_repo_hygiene_failure_blocks_only_when_requested(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir, run_dir, validation_dir, assessment_dir = _write_phase4e2_source_fixture(root)
            bundle_dir = root / "bundle"
            export_neural_abr_bundle(
                dataset_dir=dataset_dir,
                run_dir=run_dir,
                validation_dir=validation_dir,
                assessment_dir=assessment_dir,
                output_dir=bundle_dir,
                phase="phase4f",
                overwrite=True,
                docs_dir=root / "export_docs",
            )

            with mock.patch.object(bundle_validator, "_forbidden_repo_artifacts", return_value=["model.pt"]), mock.patch.object(
                bundle_validator,
                "_protected_git_changes",
                return_value=[],
            ):
                report = bundle_validator.validate_phase4f_bundle(
                    bundle_dir=bundle_dir,
                    dataset_dir=dataset_dir,
                    output_dir=root / "bundle_validation",
                    docs_dir=root / "validation_docs",
                    check_repo_hygiene=True,
                )

            self.assertEqual(bundle_validator.DECISION_BLOCKED, report["decision"])
            self.assertIn("no_repo_artifacts", report["hard_failures"])
            self.assertIn("no_repo_artifacts", report["environmental_failures"])


def _write_phase4e2_source_fixture(root: Path):
    dataset_dir = root / "dataset"
    run_dir = root / "run"
    validation_dir = root / "validation"
    assessment_dir = root / "assessment"
    build_synthetic_smoke_dataset(dataset_dir, overwrite=True)
    run_dir.mkdir()
    validation_dir.mkdir()
    assessment_dir.mkdir()

    model = NeuralAbrLiteCandidateScorer()
    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "model_config": dict(model.config()),
            "seed": 123,
        },
        run_dir / "checkpoint.pt",
    )
    write_json_file(run_dir / "model_config.json", dict(model.config()))
    write_json_file(
        run_dir / "normalization_stats.json",
        {
            "schema_version": NORMALIZATION_SCHEMA_VERSION,
            "fitted_on_split": TRAIN_SPLIT,
            "feature_names": list(CONTEXT_VECTOR_NAMES) + list(CANDIDATE_VECTOR_NAMES),
            "mean": [0.0 for _ in range(len(CONTEXT_VECTOR_NAMES) + len(CANDIDATE_VECTOR_NAMES))],
            "std": [1.0 for _ in range(len(CONTEXT_VECTOR_NAMES) + len(CANDIDATE_VECTOR_NAMES))],
            "sample_count": 24,
            "candidate_row_count": 96,
        },
    )
    write_json_file(
        run_dir / "training_report.json",
        {
            "schema_version": "neural_abr_lite_training_report_v1",
            "diagnostic_only": True,
            "not_benchmark": True,
            "device": "cpu",
            "seed": 123,
            "epochs": 1,
            "batch_size": 8,
            "loss_last": 1.0,
            "loss_mean": 1.0,
            "validation_metrics": {
                "sample_count": 12,
                "valid_action_rate": 1.0,
                "teacher_agreement": 0.5,
                "prediction_distribution": {"0": 12},
            },
            "controller_registered": False,
        },
    )
    write_json_file(
        validation_dir / "offline_validation_report.json",
        {
            "schema_version": "neural_abr_lite_offline_validation_report_v1",
            "diagnostic_only": True,
            "not_benchmark": True,
            "status": "PASS",
            "errors": [],
            "validation_metrics": {
                "sample_count": 12,
                "valid_action_rate": 1.0,
                "teacher_agreement": 0.5,
                "prediction_distribution": {"0": 12},
            },
            "ood_diagnostic_metrics": {
                "sample_count": 12,
                "valid_action_rate": 1.0,
                "teacher_agreement": 0.5,
                "prediction_distribution": {"0": 12},
            },
        },
    )
    write_json_file(
        assessment_dir / "candidate_readiness_report.json",
        {
            "schema_version": "phase4e2_candidate_readiness_report_v1",
            "phase": "phase4e2",
            "decision": "PHASE4E2_EXPANDED_CORPUS_CANDIDATE_READY_FOR_PHASE4F",
            "correctness_failures": [],
            "candidate_failures": [],
            "environmental_failures": [],
            "dataset_summary": {
                "trace_count": 30,
                "dataset_family_count": 2,
                "regime_bucket_count": 3,
                "split_sample_counts": {
                    "train": 24,
                    "validation": 12,
                    "ood_diagnostic": 12,
                },
            },
        },
    )
    return dataset_dir, run_dir, validation_dir, assessment_dir


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from core.neural_abr.artifacts import read_jsonl
from core.neural_abr.candidate_readiness import assess_candidate_readiness
from core.neural_abr.constants import (
    NORMALIZATION_SCHEMA_VERSION,
    PHASE4E2_DECISION_BLOCKED,
    PHASE4E2_DECISION_PASS_NOT_CANDIDATE,
    TRAIN_SPLIT,
)
from core.neural_abr.dataset_builder import build_synthetic_smoke_dataset


class NeuralAbrCandidateReadinessTest(unittest.TestCase):
    def test_valid_but_insufficient_synthetic_report_is_pass_not_candidate(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir, run_dir, validation_dir, docs_dir = _write_assessment_fixture(root)

            report = assess_candidate_readiness(
                dataset_dir=dataset_dir,
                run_dir=run_dir,
                validation_dir=validation_dir,
                phase="phase4e2",
                docs_dir=docs_dir,
            )

            self.assertEqual(PHASE4E2_DECISION_PASS_NOT_CANDIDATE, report["decision"])
            self.assertEqual("PASS", report["gates"]["dataset_validation_pass"]["status"])
            self.assertEqual("FAIL", report["gates"]["trace_count_at_least_30"]["status"])

    def test_leakage_overlap_blocks_candidate_readiness(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir, run_dir, validation_dir, docs_dir = _write_assessment_fixture(root)
            _inject_leakage_overlap(dataset_dir)

            report = assess_candidate_readiness(
                dataset_dir=dataset_dir,
                run_dir=run_dir,
                validation_dir=validation_dir,
                phase="phase4e2",
                docs_dir=docs_dir,
            )

            self.assertEqual(PHASE4E2_DECISION_BLOCKED, report["decision"])
            self.assertEqual("FAIL", report["gates"]["dataset_validation_pass"]["status"])
            self.assertEqual("FAIL", report["gates"]["no_leakage_group_overlap"]["status"])

    def test_cli_accepts_phase4e2_and_exits_zero_for_pass_not_candidate(self):
        repo_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir, run_dir, validation_dir, docs_dir = _write_assessment_fixture(root)
            output_dir = root / "assessment"

            command = [
                sys.executable,
                "scripts/assess_neural_abr_candidate.py",
                "--dataset-dir",
                str(dataset_dir),
                "--run-dir",
                str(run_dir),
                "--validation-dir",
                str(validation_dir),
                "--output-dir",
                str(output_dir),
                "--phase",
                "phase4e2",
                "--docs-dir",
                str(docs_dir),
            ]
            completed = subprocess.run(command, cwd=repo_root, text=True, capture_output=True, check=False)

            self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
            self.assertIn(PHASE4E2_DECISION_PASS_NOT_CANDIDATE, completed.stdout)
            self.assertTrue((output_dir / "candidate_readiness_report.json").is_file())
            self.assertTrue((docs_dir / "phase4e2_model_card.md").is_file())


def _write_assessment_fixture(root: Path):
    dataset_dir = root / "dataset"
    run_dir = root / "run"
    validation_dir = root / "validation"
    docs_dir = root / "docs"
    build_synthetic_smoke_dataset(dataset_dir, overwrite=True)
    run_dir.mkdir()
    validation_dir.mkdir()
    docs_dir.mkdir()
    (run_dir / "training_report.json").write_text(
        json.dumps(
            {
                "schema_version": "neural_abr_lite_training_report_v1",
                "diagnostic_only": True,
                "not_benchmark": True,
                "device": "cpu",
                "epochs": 1,
                "batch_size": 8,
                "loss_last": 1.0,
                "loss_mean": 1.0,
                "train_metrics": {
                    "sample_count": 24,
                    "valid_action_rate": 1.0,
                    "teacher_agreement": 0.5,
                    "prediction_distribution": {"0": 12, "1": 12},
                },
                "validation_metrics": {
                    "sample_count": 12,
                    "valid_action_rate": 1.0,
                    "teacher_agreement": 0.5,
                    "prediction_distribution": {"0": 6, "1": 6},
                },
                "controller_registered": False,
            }
        ),
        encoding="utf-8",
    )
    (run_dir / "model_config.json").write_text(
        json.dumps({"device_default": "cpu", "controller_registered": False}),
        encoding="utf-8",
    )
    (run_dir / "normalization_stats.json").write_text(
        json.dumps(
            {
                "schema_version": NORMALIZATION_SCHEMA_VERSION,
                "fitted_on_split": TRAIN_SPLIT,
                "feature_names": ["x"],
                "mean": [0.0],
                "std": [1.0],
                "sample_count": 24,
                "candidate_row_count": 120,
            }
        ),
        encoding="utf-8",
    )
    (validation_dir / "offline_validation_report.json").write_text(
        json.dumps(
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
                    "prediction_distribution": {"0": 6, "1": 6},
                },
                "ood_diagnostic_metrics": {
                    "sample_count": 12,
                    "valid_action_rate": 1.0,
                    "teacher_agreement": 0.5,
                    "prediction_distribution": {"0": 6, "1": 6},
                },
            }
        ),
        encoding="utf-8",
    )
    return dataset_dir, run_dir, validation_dir, docs_dir


def _inject_leakage_overlap(dataset_dir: Path) -> None:
    train_rows = list(read_jsonl(dataset_dir / "train.jsonl"))
    train_leakage_group = train_rows[0]["metadata"]["leakage_group"]
    ood_path = dataset_dir / "ood_diagnostic.jsonl"
    ood_rows = list(read_jsonl(ood_path))
    ood_rows[0] = dict(ood_rows[0])
    ood_rows[0]["metadata"] = dict(ood_rows[0]["metadata"])
    ood_rows[0]["metadata"]["leakage_group"] = train_leakage_group
    with ood_path.open("w", encoding="utf-8") as handle:
        for row in ood_rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")


if __name__ == "__main__":
    unittest.main()

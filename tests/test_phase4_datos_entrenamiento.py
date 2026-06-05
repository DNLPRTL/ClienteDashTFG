from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core.neural_abr.artifacts import read_json, read_jsonl
from core.neural_abr.constants import (
    LEAKAGE_AUDIT_FILENAME,
    NORMALIZATION_STATS_FILENAME,
    TRAINING_DATA_FILENAME,
    TRAINING_ROLE,
    TRAINING_SMOKE_REPORT_FILENAME,
    VALIDATION_DATA_FILENAME,
)
from core.neural_abr.model import NeuralAbrLiteCandidateScorer, masked_cross_entropy, predict_actions
from core.neural_abr.trace_sampling import Phase4SamplingConfig, build_phase4_training_trace_artifacts
from core.neural_abr.training_data import build_phase4_training_data_from_plan
from core.neural_abr.training_data_validation import validate_phase4_training_data_dir
from core.neural_abr.training_smoke import run_phase4_training_smoke
from core.trace_replay.converters.common import write_normalized_csv


class Phase4DatosEntrenamientoTest(unittest.TestCase):
    def test_builds_valid_training_data_from_phase4a_plan(self):
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
                    seed="datos-test",
                ),
            )["phase4_plan_de_trazas_para_entrenamiento.json"]

            data_dir = root / "phase4B_datos_para_entrenamiento"
            result = build_phase4_training_data_from_plan(
                plan,
                output_dir=data_dir,
                overwrite=True,
                max_training_windows=2,
                max_validation_windows=1,
            )
            report = validate_phase4_training_data_dir(data_dir)
            training_rows = read_jsonl(data_dir / TRAINING_DATA_FILENAME)
            validation_rows = read_jsonl(data_dir / VALIDATION_DATA_FILENAME)
            leakage = read_json(data_dir / LEAKAGE_AUDIT_FILENAME)
            normalization = read_json(data_dir / NORMALIZATION_STATS_FILENAME)

            self.assertEqual("PASS", result["status"])
            self.assertEqual("PASS", report["status"])
            self.assertEqual(60, len(training_rows))
            self.assertEqual(30, len(validation_rows))
            self.assertEqual("PASS", leakage["status"])
            self.assertEqual(TRAINING_ROLE, normalization["fitted_on_data_role"])
            self.assertEqual("phase2_controller_real_en_replay_offline", result["summary"]["label_teacher_source"])
            self.assertEqual(
                "core.controller.robust_mpc.RobustMpcController",
                result["summary"]["label_teacher_controller_module"],
            )
            self.assertEqual("startup_fallback_no_valid_throughput", training_rows[0]["label"]["reason"])
            self.assertNotIn("trace_id", training_rows[0]["context_features"])
            self.assertNotIn("dataset_id", training_rows[0]["candidate_features"][0])
            self.assertIn("trace_id", training_rows[0]["metadata"])

    def test_training_smoke_runs_without_candidate_checkpoint(self):
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
                    seed="smoke-test",
                ),
            )["phase4_plan_de_trazas_para_entrenamiento.json"]
            data_dir = root / "phase4B_datos_para_entrenamiento"
            run_dir = root / "phase4D_prueba_rapida_entrenamiento"
            build_phase4_training_data_from_plan(
                plan,
                output_dir=data_dir,
                overwrite=True,
                max_training_windows=2,
                max_validation_windows=1,
            )

            report = run_phase4_training_smoke(
                data_dir,
                output_dir=run_dir,
                epochs=1,
                batch_size=8,
                max_samples=16,
                seed=7,
            )

            self.assertEqual("PASS", report["status"])
            self.assertFalse(report["benchmark_performed"])
            self.assertFalse(report["ia_training_performed"])
            self.assertFalse(report["candidate_model_created"])
            self.assertFalse(report["checkpoint_written"])
            self.assertEqual(1.0, report["validation_metrics"]["valid_action_rate"])
            self.assertTrue((run_dir / TRAINING_SMOKE_REPORT_FILENAME).is_file())

    def test_candidate_scorer_masks_invalid_actions(self):
        import torch

        model = NeuralAbrLiteCandidateScorer(context_dim=3, candidate_dim=2, hidden_sizes=(4,))
        context = torch.zeros((2, 3), dtype=torch.float32)
        candidates = torch.zeros((2, 3, 2), dtype=torch.float32)
        mask = torch.tensor([[True, False, True], [False, True, False]])

        scores = model(context, candidates, mask)
        loss = masked_cross_entropy(scores, torch.tensor([2, 1]), mask)

        self.assertEqual((2, 3), tuple(scores.shape))
        self.assertLess(scores[0, 1].item(), -1.0e8)
        self.assertGreaterEqual(loss.item(), 0.0)
        self.assertEqual([0, 1], predict_actions(scores).tolist())


def build_manifest_with_trace_files(root: Path) -> dict[str, object]:
    traces = []
    for index in range(6):
        split = "train" if index < 4 else "test"
        traces.append(write_trace_record(root, index=index, split=split, throughput_kbps=1800.0 + 300.0 * index))
    traces.append(write_trace_record(root, index=6, split="eval", throughput_kbps=3000.0))
    return {
        "schema_id": "phase3_trace_manifest_final_v1",
        "phase": "phase3_rebuild",
        "artifact_set": "unit_test",
        "benchmark_authorized": False,
        "trace_count": len(traces),
        "split_counts": {"train": 4, "test": 2, "eval": 1},
        "semantics_counts": {"available_bandwidth": len(traces)},
        "traces": traces,
    }


def write_trace_record(root: Path, index: int, split: str, throughput_kbps: float) -> dict[str, object]:
    rows = [
        {"timestamp_s": float(second), "duration_s": 1.0, "throughput_kbps": throughput_kbps}
        for second in range(240)
    ]
    normalized_path = root / "trazas_normalizadas" / "trace_{0:03d}.csv".format(index)
    stats = write_normalized_csv(rows, normalized_path)
    return {
        "trace_id": "trace_{0:03d}".format(index),
        "dataset_id": "unit_test_dataset",
        "converter_id": "unit_test",
        "normalized_trace_path": str(normalized_path),
        "metadata_path": str(root / "metadata" / "trace_{0:03d}.json".format(index)),
        "source_path": str(root / "raw" / "trace_{0:03d}.csv".format(index)),
        "source_sha256": "source_hash_{0:03d}".format(index),
        "group_id": "group_{0:03d}".format(index),
        "leakage_group": "leakage_{0:03d}".format(index),
        "semantics": "available_bandwidth",
        "split": split,
        "row_count": stats["row_count"],
        "duration_s": stats["duration_s"],
        "throughput_min_kbps": stats["throughput_min_kbps"],
        "throughput_mean_kbps": stats["throughput_mean_kbps"],
        "throughput_max_kbps": stats["throughput_max_kbps"],
        "content_fingerprint_sha256": stats["content_fingerprint_sha256"],
        "zero_fraction": 0.0,
        "network_condition": "usable_network_trace",
        "usable_for_training": True,
        "usable_for_eval": True,
    }


if __name__ == "__main__":
    unittest.main()

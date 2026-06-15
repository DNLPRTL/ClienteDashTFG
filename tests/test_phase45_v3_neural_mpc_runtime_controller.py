from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import torch

from core.controller.phase45_v3_neural_mpc import Phase45V3NeuralMpcController
from core.neural_abr.constants import CONTEXT_VECTOR_NAMES
from core.phase45_v3.neural_mpc_bundle import export_phase45_v3_neural_mpc_experimental_bundle
from core.phase45_v3.neural_mpc_evaluation import NEURAL_MPC_CLOSED_LOOP_REPORT_FILENAME
from core.phase45_v3.neural_mpc_training import (
    THROUGHPUT_QUANTILE_CHECKPOINT_SCHEMA_ID,
    THROUGHPUT_QUANTILE_MODEL_CONFIG_FILENAME,
    THROUGHPUT_QUANTILE_MODEL_FILENAME,
    THROUGHPUT_QUANTILE_NORMALIZATION_FILENAME,
    THROUGHPUT_QUANTILE_TRAINING_REPORT_FILENAME,
)
from core.phase45_v3.throughput_quantile_model import (
    PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY,
    ThroughputQuantilePredictor,
)


class Phase45V3NeuralMpcRuntimeControllerTests(unittest.TestCase):
    def test_runtime_controller_loads_bundle_and_selects_without_fallback(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            root = Path(temp_root)
            model_root = root / "modelos" / "expanded_diag_v1"
            run_root = root / "runs" / "expanded_diag_v1"
            output_dir = root / "bundle" / "neural_mpc_experimental_candidate_v1"
            seeds = ("451001", "451002", "451003")
            for seed in seeds:
                self._write_seed_artifacts(model_root, run_root, seed)
            export_phase45_v3_neural_mpc_experimental_bundle(
                model_root=model_root,
                run_root=run_root,
                output_dir=output_dir,
                canonical_seed="451001",
                seeds=seeds,
                overwrite=True,
            )

            controller = Phase45V3NeuralMpcController(bundle_dir=str(output_dir), diagnostic_only=True)
            feedback = self._feedback()
            controller.setPlayerFeedback(feedback)
            selected_rate = float(controller.calcControlAction())
            diagnostics = controller.get_neural_diagnostics()

            self.assertIn(selected_rate, feedback["rates"])
            self.assertEqual(1, diagnostics["neural_bundle_loaded"])
            self.assertEqual(1, diagnostics["neural_bundle_hash_ok"])
            self.assertEqual(1, diagnostics["neural_valid_action"])
            self.assertEqual(0, diagnostics["neural_fallback_used"])
            self.assertEqual("success_neural", diagnostics["neural_fallback_reason"])

    def _write_seed_artifacts(self, model_root: Path, run_root: Path, seed: str) -> None:
        model_dir = model_root / f"seed_{seed}"
        run_dir = run_root / f"seed_{seed}"
        model_dir.mkdir(parents=True, exist_ok=True)
        run_dir.mkdir(parents=True, exist_ok=True)
        model = ThroughputQuantilePredictor(
            input_dim=len(CONTEXT_VECTOR_NAMES),
            horizon_segments=5,
            quantiles=(0.10, 0.25, 0.50, 0.75),
            hidden_sizes=(16,),
        )
        for parameter in model.parameters():
            torch.nn.init.constant_(parameter, 0.0)
        normalization = {
            "schema_id": "phase45_v3_throughput_quantile_normalization_v1",
            "fitted_on_data_role": "training",
            "context_feature_names": list(CONTEXT_VECTOR_NAMES),
            "context_mean": [0.0 for _ in CONTEXT_VECTOR_NAMES],
            "context_std": [1.0 for _ in CONTEXT_VECTOR_NAMES],
        }
        checkpoint = {
            "schema_id": THROUGHPUT_QUANTILE_CHECKPOINT_SCHEMA_ID,
            "model_key": PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY,
            "model_config": model.config(),
            "normalization": normalization,
            "model_state_dict": model.state_dict(),
            "profile": {},
        }
        checkpoint_path = model_dir / THROUGHPUT_QUANTILE_MODEL_FILENAME
        torch.save(checkpoint, checkpoint_path)
        checkpoint_sha256 = hashlib.sha256(checkpoint_path.read_bytes()).hexdigest()
        self._write_json(model_dir / THROUGHPUT_QUANTILE_MODEL_CONFIG_FILENAME, dict(model.config()))
        self._write_json(model_dir / THROUGHPUT_QUANTILE_NORMALIZATION_FILENAME, normalization)
        self._write_json(
            model_dir / THROUGHPUT_QUANTILE_TRAINING_REPORT_FILENAME,
            {
                "schema_id": "phase45_v3_throughput_quantile_training_report_v1",
                "status": "PASS",
                "model_sha256": checkpoint_sha256,
                "model_path": str(checkpoint_path),
                "benchmark_performed": False,
                "ranking_performed": False,
                "no_final_ranking": True,
            },
        )
        self._write_json(
            run_dir / NEURAL_MPC_CLOSED_LOOP_REPORT_FILENAME,
            {
                "schema_id": "phase45_v3_neural_mpc_closed_loop_diagnostic_v1",
                "status": "PASS",
                "window_count": 32,
                "session_count": 128,
                "gates": {"failed": [], "gates": {}},
                "metrics": {
                    "neural_mpc": {
                        "fallback_rate": 0.0,
                        "invalid_action_count": 0,
                        "high_capacity_action0_rate": 0.0,
                        "high_capacity_mean_bitrate_ratio_vs_robust_mpc": 1.0,
                        "bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean": 0.10,
                        "qoe_delta_vs_robust_mpc_mean": -0.02,
                    }
                },
                "benchmark_performed": False,
                "ranking_performed": False,
                "no_final_ranking": True,
            },
        )

    def _feedback(self) -> dict[str, object]:
        rates = [37500.0, 93750.0, 150000.0, 231250.0, 356250.0, 537500.0]
        return {
            "queued_bytes": 0,
            "queued_time": 12.0,
            "cur_bitrate": rates[2],
            "bwe": 750000.0,
            "level": 2,
            "max_level": len(rates) - 1,
            "cur_rate": rates[2],
            "max_rate": max(rates),
            "min_rate": min(rates),
            "max_bitrate": max(rates),
            "min_bitrate": min(rates),
            "last_fragment_size": 450000,
            "last_download_time": 0.75,
            "downloaded_bytes": 450000,
            "fragment_duration": 4.0,
            "rates": rates,
            "segment_index": 4,
            "total_segments": 30,
            "start_segment_request": 1.0,
            "stop_segment_request": 1.75,
        }

    def _write_json(self, path: Path, payload: dict[str, object]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")


if __name__ == "__main__":
    unittest.main()

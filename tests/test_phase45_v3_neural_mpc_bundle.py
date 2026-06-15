from __future__ import annotations

import json
import hashlib
import tempfile
import unittest
from pathlib import Path

from core.phase45_v3.neural_mpc_bundle import (
    NEURAL_MPC_BUNDLE_EXPORT_REPORT_FILENAME,
    NEURAL_MPC_BUNDLE_MANIFEST_FILENAME,
    NEURAL_MPC_BUNDLE_MODEL_FILENAME,
    export_phase45_v3_neural_mpc_experimental_bundle,
    validate_phase45_v3_neural_mpc_bundle_dir,
)
from core.phase45_v3.neural_mpc_evaluation import NEURAL_MPC_CLOSED_LOOP_REPORT_FILENAME
from core.phase45_v3.neural_mpc_training import (
    THROUGHPUT_QUANTILE_MODEL_CONFIG_FILENAME,
    THROUGHPUT_QUANTILE_MODEL_FILENAME,
    THROUGHPUT_QUANTILE_NORMALIZATION_FILENAME,
    THROUGHPUT_QUANTILE_TRAINING_REPORT_FILENAME,
)


class Phase45V3NeuralMpcBundleTests(unittest.TestCase):
    def test_exports_and_validates_bundle_from_ready_seed_reports(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            root = Path(temp_root)
            model_root = root / "modelos" / "expanded_diag_v1"
            run_root = root / "runs" / "expanded_diag_v1"
            output_dir = root / "bundle" / "neural_mpc_experimental_candidate_v1"
            seeds = ("451001", "451002", "451003")
            for seed in seeds:
                self._write_seed_artifacts(model_root, run_root, seed)

            report = export_phase45_v3_neural_mpc_experimental_bundle(
                model_root=model_root,
                run_root=run_root,
                output_dir=output_dir,
                canonical_seed="451001",
                seeds=seeds,
                overwrite=True,
            )

            self.assertEqual("PASS", report["status"])
            self.assertTrue((output_dir / NEURAL_MPC_BUNDLE_MODEL_FILENAME).is_file())
            self.assertTrue((output_dir / NEURAL_MPC_BUNDLE_MANIFEST_FILENAME).is_file())
            self.assertTrue((output_dir / NEURAL_MPC_BUNDLE_EXPORT_REPORT_FILENAME).is_file())
            validation = validate_phase45_v3_neural_mpc_bundle_dir(output_dir)
            self.assertEqual("PASS", validation["status"])
            manifest = validation["manifest"]
            self.assertFalse(manifest["benchmark_performed"])
            self.assertFalse(manifest["ranking_performed"])
            self.assertTrue(manifest["no_final_ranking"])
            self.assertFalse(manifest["runtime_controller_integrated"])
            self.assertIn(NEURAL_MPC_BUNDLE_MODEL_FILENAME, manifest["files"])

    def test_export_rejects_review_readiness(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            root = Path(temp_root)
            model_root = root / "modelos" / "expanded_diag_v1"
            run_root = root / "runs" / "expanded_diag_v1"
            for seed in ("451001", "451002", "451003"):
                self._write_seed_artifacts(
                    model_root,
                    run_root,
                    seed,
                    evaluation_status="REVIEW" if seed == "451002" else "PASS",
                    failed_gates=["fallback_rate"] if seed == "451002" else [],
                )

            with self.assertRaises(ValueError):
                export_phase45_v3_neural_mpc_experimental_bundle(
                    model_root=model_root,
                    run_root=run_root,
                    output_dir=root / "bundle",
                    canonical_seed="451001",
                    seeds=("451001", "451002", "451003"),
                    overwrite=True,
                )

    def _write_seed_artifacts(
        self,
        model_root: Path,
        run_root: Path,
        seed: str,
        *,
        evaluation_status: str = "PASS",
        failed_gates: list[str] | None = None,
    ) -> None:
        model_dir = model_root / f"seed_{seed}"
        run_dir = run_root / f"seed_{seed}"
        model_dir.mkdir(parents=True, exist_ok=True)
        run_dir.mkdir(parents=True, exist_ok=True)
        checkpoint = model_dir / THROUGHPUT_QUANTILE_MODEL_FILENAME
        checkpoint.write_bytes(f"fake-checkpoint-{seed}".encode("ascii"))
        checkpoint_sha256 = hashlib.sha256(checkpoint.read_bytes()).hexdigest()
        self._write_json(
            model_dir / THROUGHPUT_QUANTILE_MODEL_CONFIG_FILENAME,
            {
                "schema_id": "phase45_v3_throughput_quantile_model_config_v1",
                "model_key": "phase45_v3_throughput_quantile_predictor",
                "model_type": "mlp_future_throughput_log_ratio_quantile_predictor",
                "input_dim": 4,
                "context_feature_names": ["a", "b", "c", "d"],
                "horizon_segments": 5,
                "quantiles": [0.10, 0.25, 0.50, 0.75],
                "hidden_sizes": [16],
            },
        )
        self._write_json(
            model_dir / THROUGHPUT_QUANTILE_NORMALIZATION_FILENAME,
            {
                "schema_id": "phase45_v3_throughput_quantile_normalization_v1",
                "fitted_on_data_role": "training",
                "context_feature_names": ["a", "b", "c", "d"],
                "context_mean": [0.0, 0.0, 0.0, 0.0],
                "context_std": [1.0, 1.0, 1.0, 1.0],
            },
        )
        self._write_json(
            model_dir / THROUGHPUT_QUANTILE_TRAINING_REPORT_FILENAME,
            {
                "schema_id": "phase45_v3_throughput_quantile_training_report_v1",
                "status": "PASS",
                "model_sha256": checkpoint_sha256,
                "model_path": str(checkpoint),
                "benchmark_performed": False,
                "ranking_performed": False,
                "no_final_ranking": True,
            },
        )
        self._write_json(
            run_dir / NEURAL_MPC_CLOSED_LOOP_REPORT_FILENAME,
            {
                "schema_id": "phase45_v3_neural_mpc_closed_loop_diagnostic_v1",
                "status": evaluation_status,
                "window_count": 32,
                "session_count": 128,
                "gates": {"failed": failed_gates or [], "gates": {}},
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

    def _write_json(self, path: Path, payload: dict[str, object]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")


if __name__ == "__main__":
    unittest.main()

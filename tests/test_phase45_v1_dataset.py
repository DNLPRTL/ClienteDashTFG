from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core.neural_abr.artifacts import read_json, read_jsonl
from core.neural_abr.content_ladder import default_training_ladder
from core.neural_abr.replay_environment import TraceReplayEnvironment
from core.phase45_v1.constants import (
    LEAKAGE_AUDIT_FILENAME,
    NORMALIZATION_STATS_FILENAME,
    ORACLE_AUDIT_FILENAME,
    TRAINING_DATA_FILENAME,
    VALIDATION_DATA_FILENAME,
)
from core.phase45_v1.dataset import build_phase45_v1_dataset
from core.phase45_v1.oracle import OracleConfig, select_oracle_action
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v1.profiles import DatasetProfile, profile_by_name
from core.phase45_v1.sampling import build_sampling_artifacts, validate_sampling_plan
from core.phase45_v1.validation import validate_phase45_v1_dataset_dir
from core.trace_replay.converters.common import write_normalized_csv
from core.trace_replay.loader import load_normalized_trace_rows


class Phase45V1DatasetTest(unittest.TestCase):
    def test_sampler_is_deterministic_excludes_eval_and_limits_synthetic(self):
        manifest = build_manifest_without_files()
        first = build_sampling_artifacts(manifest, profile_by_name("smoke"))
        second = build_sampling_artifacts(manifest, profile_by_name("smoke"))
        plan = first["plan"]
        audit = first["audit"]
        summary = validate_sampling_plan(plan)

        self.assertEqual("PASS", summary["status"])
        self.assertEqual(
            [window["window_id"] for window in plan["training_windows"]],
            [window["window_id"] for window in second["plan"]["training_windows"]],
        )
        selected = plan["training_windows"] + plan["validation_windows"]
        self.assertNotIn("eval", {window["source_split"] for window in selected})
        self.assertLessEqual(sum(1 for window in plan["training_windows"] if window["synthetic"]), 4)
        self.assertEqual("PASS", audit["leakage_check"]["status"])
        self.assertGreater(
            audit["training_selection_summary"]["counts"]["by_throughput_bucket"]["lte_1_mbps"],
            0,
        )

    def test_oracle_prefers_safe_low_quality_when_capacity_is_tiny(self):
        rows = [
            {"timestamp_s": float(index), "duration_s": 1.0, "throughput_kbps": 400.0}
            for index in range(120)
        ]
        loaded_trace = load_normalized_trace_rows(rows, trace_id="tiny_capacity")
        ladder = default_training_ladder(segment_duration_s=4.0, segment_count=30)
        env = TraceReplayEnvironment(loaded_trace, ladder)

        decision = select_oracle_action(env.state, ladder, env.network_model, OracleConfig(3, 4))

        self.assertEqual(0, decision.action)
        self.assertFalse(decision.fallback_used)
        self.assertEqual("qoe_linear_v1", decision.qoe_formula_version)

    def test_builds_and_validates_dataset_with_path_rewrite(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
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
                seed="unit-phase45-v1",
            )

            result = build_phase45_v1_dataset(
                manifest,
                output_dir=output_dir,
                profile=profile,
                overwrite=True,
                trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
            )
            validation = validate_phase45_v1_dataset_dir(output_dir)
            training_rows = read_jsonl(output_dir / TRAINING_DATA_FILENAME)
            validation_rows = read_jsonl(output_dir / VALIDATION_DATA_FILENAME)
            leakage = read_json(output_dir / LEAKAGE_AUDIT_FILENAME)
            normalization = read_json(output_dir / NORMALIZATION_STATS_FILENAME)
            oracle_audit = read_json(output_dir / ORACLE_AUDIT_FILENAME)

            self.assertEqual("PASS", result["status"])
            self.assertEqual("PASS", validation["status"])
            self.assertEqual(180, len(training_rows))
            self.assertEqual(60, len(validation_rows))
            self.assertEqual("PASS", leakage["status"])
            self.assertEqual("training", normalization["fitted_on_data_role"])
            self.assertEqual(0, oracle_audit["fallback_count"])
            first = training_rows[0]
            self.assertNotIn("trace_id", first["model_inputs"]["context"])
            self.assertNotIn("future_throughput_kbps", first["model_inputs"]["context"])
            self.assertIn("future_throughput_kbps", first["spc_targets"])
            self.assertIn("oracle_action", first["spbc_targets"])
            self.assertFalse(first["metadata"]["metadata_is_model_input"])
            self.assertEqual(
                {"bba", "bola", "mpc", "rate_based", "robust_mpc"},
                {item["controller"] for item in first["audit"]["classic_controllers"]},
            )


def build_manifest_without_files() -> dict[str, object]:
    traces = []
    index = 0
    for split, count in (("train", 36), ("test", 12), ("eval", 4)):
        for _ in range(count):
            mean = (500.0, 1500.0, 3500.0, 9000.0, 25000.0)[index % 5]
            synthetic = split != "eval" and index % 11 == 0
            traces.append(
                trace_record(
                    index=index,
                    split=split,
                    mean_kbps=mean,
                    normalized_trace_path="/external/trace_{0:03d}.csv".format(index),
                    synthetic=synthetic,
                )
            )
            index += 1
    return manifest_from_traces(traces)


def build_manifest_with_trace_files(root: Path) -> dict[str, object]:
    traces = []
    for index in range(9):
        split = "train" if index < 6 else "test" if index < 8 else "eval"
        mean = (700.0, 1400.0, 2600.0, 4200.0, 9000.0, 18000.0, 1200.0, 5200.0, 3000.0)[index]
        actual_path = root / "trazas" / "trace_{0:03d}.csv".format(index)
        rows = [
            {"timestamp_s": float(second), "duration_s": 1.0, "throughput_kbps": mean + 50.0 * ((second % 5) - 2)}
            for second in range(240)
        ]
        stats = write_normalized_csv(rows, actual_path)
        raw_manifest_path = "/home/daniel/TFG/trazas/trace_{0:03d}.csv".format(index)
        traces.append(
            trace_record(
                index=index,
                split=split,
                mean_kbps=float(stats["throughput_mean_kbps"]),
                normalized_trace_path=raw_manifest_path,
                synthetic=False,
                stats=stats,
            )
        )
    return manifest_from_traces(traces)


def manifest_from_traces(traces: list[dict[str, object]]) -> dict[str, object]:
    split_counts = {}
    for trace in traces:
        split_counts[str(trace["split"])] = split_counts.get(str(trace["split"]), 0) + 1
    return {
        "schema_id": "phase3_trace_manifest_final_v1",
        "phase": "phase3_rebuild",
        "artifact_set": "unit_test",
        "benchmark_authorized": False,
        "trace_count": len(traces),
        "split_counts": split_counts,
        "semantics_counts": {"available_bandwidth": len(traces)},
        "traces": traces,
    }


def trace_record(
    *,
    index: int,
    split: str,
    mean_kbps: float,
    normalized_trace_path: str,
    synthetic: bool = False,
    stats: dict[str, object] | None = None,
) -> dict[str, object]:
    active_stats = stats or {
        "row_count": 240,
        "duration_s": 240.0,
        "throughput_min_kbps": mean_kbps * 0.5,
        "throughput_mean_kbps": mean_kbps,
        "throughput_max_kbps": mean_kbps * 1.8,
        "content_fingerprint_sha256": "fingerprint_{0:03d}".format(index),
    }
    return {
        "trace_id": "trace_{0:03d}".format(index),
        "dataset_id": "synthetic_controlled_network" if synthetic else "unit_dataset_{0}".format(index % 3),
        "converter_id": "unit_test",
        "normalized_trace_path": normalized_trace_path,
        "metadata_path": "/external/metadata/trace_{0:03d}.json".format(index),
        "source_path": "/external/raw/trace_{0:03d}.csv".format(index),
        "source_sha256": "source_hash_{0:03d}".format(index),
        "group_id": "group_{0:03d}".format(index),
        "leakage_group": "leakage_{0:03d}".format(index),
        "semantics": "synthetic_available_bandwidth" if synthetic else "available_bandwidth",
        "split": split,
        "row_count": active_stats["row_count"],
        "duration_s": active_stats["duration_s"],
        "throughput_min_kbps": active_stats["throughput_min_kbps"],
        "throughput_mean_kbps": active_stats["throughput_mean_kbps"],
        "throughput_max_kbps": active_stats["throughput_max_kbps"],
        "content_fingerprint_sha256": active_stats["content_fingerprint_sha256"],
        "zero_fraction": 0.12 if mean_kbps <= 700.0 else 0.0,
        "network_condition": "synthetic_low" if synthetic else "usable_network_trace",
        "synthetic": synthetic,
        "usable_for_training": True,
        "usable_for_eval": True,
    }


if __name__ == "__main__":
    unittest.main()

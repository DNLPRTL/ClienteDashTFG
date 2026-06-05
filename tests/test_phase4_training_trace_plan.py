from __future__ import annotations

import unittest

from core.neural_abr.trace_sampling import (
    PROHIBITED_MODEL_FEATURE_FIELDS,
    Phase4SamplingConfig,
    Phase4TraceSamplingError,
    build_phase4_training_trace_artifacts,
    validate_phase4_training_trace_plan,
)


class Phase4TrainingTracePlanTest(unittest.TestCase):
    def test_builds_balanced_plan_without_eval_windows(self):
        manifest = build_manifest()
        config = Phase4SamplingConfig(
            train_window_count=20,
            validation_window_count=8,
            synthetic_max_fraction=0.20,
            dataset_max_fraction=0.30,
            semantics_max_fraction=0.50,
            difficulty_max_fraction=0.60,
            max_windows_per_trace=2,
            seed="unit-test-seed",
        )

        artifacts = build_phase4_training_trace_artifacts(manifest, config=config)
        plan = artifacts["phase4_training_trace_plan.json"]
        audit = artifacts["phase4_sampling_audit.json"]
        summary = validate_phase4_training_trace_plan(plan, config)

        self.assertEqual("PASS", summary["status"])
        self.assertEqual(20, plan["requested_training_window_count"])
        self.assertEqual(8, plan["requested_validation_window_count"])
        self.assertGreater(plan["training_window_count"], 0)
        self.assertGreater(plan["validation_window_count"], 0)
        self.assertLessEqual(plan["training_window_count"], 20)
        self.assertLessEqual(plan["validation_window_count"], 8)
        self.assertFalse(plan["benchmark_performed"])
        self.assertFalse(plan["ia_training_performed"])
        self.assertTrue(plan["no_final_ranking"])
        self.assertGreater(audit["excluded_source_split_summary"]["eval_eligible_window_count"], 0)
        self.assertEqual("PASS", audit["leakage_check"]["status"])
        selected = plan["training_windows"] + plan["validation_windows"]
        self.assertNotIn("eval", {window["source_split"] for window in selected})
        self.assertLessEqual(
            sum(1 for window in plan["training_windows"] if window["synthetic"]),
            4,
        )
        self.assertLessEqual(
            sum(1 for window in plan["training_windows"] if window["dataset_id"] == "fcc_measuring_broadband_america"),
            6,
        )

    def test_seed_makes_selection_reproducible(self):
        manifest = build_manifest()
        config = Phase4SamplingConfig(
            train_window_count=18,
            validation_window_count=6,
            dataset_max_fraction=0.40,
            semantics_max_fraction=0.60,
            difficulty_max_fraction=0.70,
            seed="same-seed",
        )

        first = build_phase4_training_trace_artifacts(manifest, config=config)["phase4_training_trace_plan.json"]
        second = build_phase4_training_trace_artifacts(manifest, config=config)["phase4_training_trace_plan.json"]

        self.assertEqual(
            [window["window_id"] for window in first["training_windows"]],
            [window["window_id"] for window in second["training_windows"]],
        )
        self.assertEqual(
            [window["window_id"] for window in first["validation_windows"]],
            [window["window_id"] for window in second["validation_windows"]],
        )

    def test_leakage_group_across_source_splits_fails(self):
        manifest = build_manifest()
        manifest["traces"][-1]["leakage_group"] = manifest["traces"][0]["leakage_group"]
        manifest["traces"][-1]["split"] = "test"

        with self.assertRaisesRegex(Phase4TraceSamplingError, "spans splits"):
            build_phase4_training_trace_artifacts(manifest, config=Phase4SamplingConfig(train_window_count=4))

    def test_model_feature_fields_cannot_include_metadata(self):
        manifest = build_manifest()
        plan = build_phase4_training_trace_artifacts(manifest)["phase4_training_trace_plan.json"]
        plan["model_feature_fields"] = ["buffer_s", "trace_id"]

        with self.assertRaisesRegex(Phase4TraceSamplingError, "prohibited metadata"):
            validate_phase4_training_trace_plan(plan)
        self.assertIn("dataset_id", PROHIBITED_MODEL_FEATURE_FIELDS)
        self.assertIn("future_throughput_kbps", PROHIBITED_MODEL_FEATURE_FIELDS)


def build_manifest() -> dict[str, object]:
    traces = []
    for index in range(18):
        traces.append(
            trace_record(
                index,
                split="train",
                dataset_id="fcc_measuring_broadband_america",
                semantics="active_fixed_broadband_download_test",
                duration_s=600.0,
                throughput_mean_kbps=9000.0,
            )
        )
    for index in range(18, 30):
        traces.append(
            trace_record(
                index,
                split="train",
                dataset_id="oboe",
                semantics="available_bandwidth",
                duration_s=360.0,
                throughput_mean_kbps=1500.0,
            )
        )
    for index in range(30, 40):
        traces.append(
            trace_record(
                index,
                split="train",
                dataset_id="synthetic_controlled_network",
                semantics="synthetic_available_bandwidth",
                duration_s=300.0,
                throughput_mean_kbps=2000.0,
                synthetic=True,
                network_condition="synthetic_sudden_drop",
            )
        )
    for index in range(40, 52):
        traces.append(
            trace_record(
                index,
                split="test",
                dataset_id="puffer_stanford",
                semantics="real_streaming_delivery_rate",
                duration_s=300.0,
                throughput_mean_kbps=2500.0,
            )
        )
    for index in range(52, 56):
        traces.append(
            trace_record(
                index,
                split="eval",
                dataset_id="oboe",
                semantics="available_bandwidth",
                duration_s=300.0,
                throughput_mean_kbps=1200.0,
            )
        )
    return {
        "schema_id": "phase3_trace_manifest_final_v1",
        "phase": "phase3_rebuild",
        "artifact_set": "unit_test",
        "benchmark_authorized": False,
        "trace_count": len(traces),
        "split_counts": {"train": 40, "test": 12, "eval": 4},
        "semantics_counts": {
            "active_fixed_broadband_download_test": 18,
            "available_bandwidth": 16,
            "real_streaming_delivery_rate": 12,
            "synthetic_available_bandwidth": 10,
        },
        "traces": traces,
    }


def trace_record(
    index: int,
    split: str,
    dataset_id: str,
    semantics: str,
    duration_s: float,
    throughput_mean_kbps: float,
    synthetic: bool = False,
    network_condition: str = "stable",
) -> dict[str, object]:
    return {
        "trace_id": "trace_{0:03d}".format(index),
        "dataset_id": dataset_id,
        "converter_id": "unit_test",
        "normalized_trace_path": "/external/traces/trace_{0:03d}.csv".format(index),
        "metadata_path": "/external/metadata/trace_{0:03d}.json".format(index),
        "source_path": "/external/raw/trace_{0:03d}.csv".format(index),
        "source_sha256": "raw_hash_{0:03d}".format(index),
        "group_id": "group_{0:03d}".format(index),
        "leakage_group": "leakage_{0:03d}".format(index),
        "semantics": semantics,
        "split": split,
        "row_count": int(duration_s),
        "duration_s": duration_s,
        "throughput_min_kbps": 0.0 if throughput_mean_kbps < 1000 else throughput_mean_kbps / 2.0,
        "throughput_mean_kbps": throughput_mean_kbps,
        "throughput_max_kbps": throughput_mean_kbps * 1.5,
        "content_fingerprint_sha256": "fingerprint_{0:03d}".format(index),
        "zero_fraction": 0.12 if throughput_mean_kbps < 1000 else 0.0,
        "network_condition": network_condition,
        "synthetic": synthetic,
        "usable_for_training": True,
        "usable_for_eval": True,
    }


if __name__ == "__main__":
    unittest.main()

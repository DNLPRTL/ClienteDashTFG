from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import torch

from core.neural_abr.artifacts import read_jsonl, write_jsonl
from core.phase45_v1.constants import SPBC_CHECKPOINT_SCHEMA_ID
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v1.preference_dataset_v2 import (
    ROLLOUT_ORACLE,
    ROLLOUT_SPBC,
    ROLLOUT_SPBC_V2_DPO,
    V2_DAGGER2_DATASET_SCHEMA_ID,
    V2_TRAINING_DATA_FILENAME,
    Phase45V2DatasetBuildError,
    Phase45V2DatasetValidationError,
    build_phase45_v2_dataset,
    validate_phase45_v2_dataset_dir,
)
from core.phase45_v1.profiles import DatasetProfile
from core.phase45_v1.spbc_training import SpbcAbrV1Policy
from core.trace_replay.converters.common import write_normalized_csv


class Phase45V2PreferenceDatasetTest(unittest.TestCase):
    def test_builds_oracle_only_v2_with_action_surface_and_preferences(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = build_manifest_with_trace_files(root)
            output_dir = root / "datasets_normalizados" / "phase45_v1" / "phase45v2"

            result = build_phase45_v2_dataset(
                manifest,
                output_dir=output_dir,
                profile=unit_profile("unit_v2"),
                overwrite=True,
                trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
                spbc_checkpoint=None,
            )
            validation = validate_phase45_v2_dataset_dir(output_dir)
            training_rows = read_jsonl(output_dir / V2_TRAINING_DATA_FILENAME)
            first = training_rows[0]

            self.assertEqual("PASS", result["status"])
            self.assertEqual("PASS", validation["status"])
            self.assertEqual({ROLLOUT_ORACLE}, {row["rollout_source"] for row in training_rows})
            self.assertIn("per_action_outcomes", first)
            self.assertIn("preference_pairs", first)
            self.assertGreaterEqual(len(first["per_action_outcomes"]), 2)
            self.assertGreaterEqual(max(len(row["preference_pairs"]) for row in training_rows), 1)
            outcome = first["per_action_outcomes"][0]
            for field in ("reward_n", "qoe_gap", "estimated_rebuffer_s", "smoothness_mbps", "bitrate_kbps", "valid_action"):
                self.assertIn(field, outcome)
            self.assertNotIn("trace_id", first["model_inputs"]["context"])
            self.assertFalse(first["metadata"]["metadata_is_model_input"])

    def test_builds_spbc_on_policy_rollout_with_stub_checkpoint(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = build_manifest_with_trace_files(root)
            checkpoint_path = root / "modelos" / "phase45_v1" / "spbc_abr_v1" / "full_v1" / "modelo_spbc_abr_v1.pt"
            write_stub_spbc_checkpoint(checkpoint_path)
            output_dir = root / "datasets_normalizados" / "phase45_v1" / "phase45v2_onpolicy"

            result = build_phase45_v2_dataset(
                manifest,
                output_dir=output_dir,
                profile=unit_profile("unit_v2_onpolicy"),
                overwrite=True,
                trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
                spbc_checkpoint=checkpoint_path,
                device="cpu",
            )
            validation = validate_phase45_v2_dataset_dir(output_dir)
            training_rows = read_jsonl(output_dir / V2_TRAINING_DATA_FILENAME)
            on_policy_rows = [row for row in training_rows if row["rollout_source"] == ROLLOUT_SPBC]

            self.assertEqual("PASS", result["status"])
            self.assertEqual("PASS", validation["status"])
            self.assertTrue(result["spbc_on_policy_enabled"])
            self.assertTrue(on_policy_rows)
            self.assertIsNone(on_policy_rows[0]["state_origin_action"])
            self.assertIsNotNone(on_policy_rows[1]["state_origin_action"])
            self.assertIn("spbc_policy_action", on_policy_rows[0])

    def test_builds_dagger2_policy_rollout_with_stub_checkpoint(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = build_manifest_with_trace_files(root)
            spbc_checkpoint = root / "modelos" / "phase45_v1" / "spbc_abr_v1" / "full_v1" / "modelo_spbc_abr_v1.pt"
            v2_checkpoint = (
                root
                / "modelos"
                / "phase45_v1"
                / "spbc_abr_v2_dpo"
                / "full_v1_utility_risk_v1"
                / "modelo_spbc_abr_v2_dpo.pt"
            )
            write_stub_spbc_checkpoint(spbc_checkpoint)
            write_stub_spbc_v2_dpo_checkpoint(v2_checkpoint)
            output_dir = root / "datasets_normalizados" / "phase45_v1" / "phase45v2_dagger2"

            result = build_phase45_v2_dataset(
                manifest,
                output_dir=output_dir,
                profile=unit_profile("unit_v2_dagger2"),
                overwrite=True,
                trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
                spbc_checkpoint=spbc_checkpoint,
                extra_policy_rollout_checkpoint=v2_checkpoint,
                dataset_schema_id=V2_DAGGER2_DATASET_SCHEMA_ID,
                device="cpu",
            )
            validation = validate_phase45_v2_dataset_dir(output_dir)
            training_rows = read_jsonl(output_dir / V2_TRAINING_DATA_FILENAME)
            rollout_sources = {row["rollout_source"] for row in training_rows}
            v2_rows = [row for row in training_rows if row["rollout_source"] == ROLLOUT_SPBC_V2_DPO]

            self.assertEqual("PASS", result["status"])
            self.assertEqual(V2_DAGGER2_DATASET_SCHEMA_ID, validation["schema_id"])
            self.assertTrue(result["spbc_v2_dpo_on_policy_enabled"])
            self.assertEqual({ROLLOUT_ORACLE, ROLLOUT_SPBC, ROLLOUT_SPBC_V2_DPO}, rollout_sources)
            self.assertTrue(v2_rows)
            self.assertEqual("spbc_abr_v2_dpo", v2_rows[0]["rollout_policy_model_key"])
            self.assertIsNotNone(v2_rows[0]["rollout_policy_action"])

    def test_dagger2_rollout_requires_existing_v2_policy_checkpoint(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = build_manifest_with_trace_files(root)
            output_dir = root / "datasets_normalizados" / "phase45_v1" / "phase45v2_dagger2_missing"

            with self.assertRaises(Phase45V2DatasetBuildError):
                build_phase45_v2_dataset(
                    manifest,
                    output_dir=output_dir,
                    profile=unit_profile("unit_v2_dagger2_missing"),
                    overwrite=True,
                    trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
                    spbc_checkpoint=None,
                    extra_policy_rollout_checkpoint=root / "missing" / "modelo_spbc_abr_v2_dpo.pt",
                    dataset_schema_id=V2_DAGGER2_DATASET_SCHEMA_ID,
                    device="cpu",
                )

    def test_full_v1_requires_spbc_checkpoint_unless_explicitly_overridden(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = build_manifest_with_trace_files(root)
            output_dir = root / "datasets_normalizados" / "phase45_v1" / "phase45v2_full"
            missing_checkpoint = root / "modelos" / "missing.pt"

            with self.assertRaises(Phase45V2DatasetBuildError):
                build_phase45_v2_dataset(
                    manifest,
                    output_dir=output_dir,
                    profile=unit_profile("full_v1"),
                    overwrite=True,
                    trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
                    spbc_checkpoint=missing_checkpoint,
                )

    def test_validation_rejects_forbidden_model_input_fields(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = build_manifest_with_trace_files(root)
            output_dir = root / "datasets_normalizados" / "phase45_v1" / "phase45v2_forbidden"
            build_phase45_v2_dataset(
                manifest,
                output_dir=output_dir,
                profile=unit_profile("unit_v2_forbidden"),
                overwrite=True,
                trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
                spbc_checkpoint=None,
            )
            rows = list(read_jsonl(output_dir / V2_TRAINING_DATA_FILENAME))
            first = dict(rows[0])
            model_inputs = dict(first["model_inputs"])
            context = dict(model_inputs["context"])
            context["trace_id"] = "leak"
            model_inputs["context"] = context
            first["model_inputs"] = model_inputs
            rows[0] = first
            write_jsonl(output_dir / V2_TRAINING_DATA_FILENAME, rows)

            with self.assertRaises(Phase45V2DatasetValidationError):
                validate_phase45_v2_dataset_dir(output_dir)


def unit_profile(name: str) -> DatasetProfile:
    return DatasetProfile(
        name=name,
        train_window_count=1,
        validation_window_count=1,
        oracle_horizon_segments=1,
        oracle_beam_width=2,
        future_horizon_segments=1,
        max_windows_per_trace=1,
        synthetic_max_fraction=0.50,
        dataset_max_fraction=1.0,
        semantics_max_fraction=1.0,
        seed="unit-phase45-v2",
    )


def write_stub_spbc_checkpoint(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    model = SpbcAbrV1Policy(
        history_hidden_size=32,
        state_hidden_size=32,
        candidate_hidden_size=24,
        shared_hidden_size=64,
        dropout=0.0,
    )
    for parameter in model.parameters():
        torch.nn.init.constant_(parameter, 0.0)
    checkpoint = {
        "schema_id": SPBC_CHECKPOINT_SCHEMA_ID,
        "model_key": "spbc_abr_v1",
        "model_state_dict": model.state_dict(),
        "model_config": model.config(),
        "normalization": {
            "sequence_mean": [0.0, 0.0],
            "sequence_std": [1.0, 1.0],
            "scalar_mean": [0.0 for _ in range(7)],
            "scalar_std": [1.0 for _ in range(7)],
            "candidate_mean": [0.0 for _ in range(7)],
            "candidate_std": [1.0 for _ in range(7)],
        },
    }
    torch.save(checkpoint, path)


def write_stub_spbc_v2_dpo_checkpoint(path: Path) -> None:
    from core.phase45_v1.spbc_v2_dpo_training import (
        SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID,
        SPBC_V2_DPO_MODEL_KEY,
        SpbcAbrV2DpoPolicy,
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    model = SpbcAbrV2DpoPolicy(
        history_hidden_size=32,
        state_hidden_size=32,
        candidate_hidden_size=24,
        shared_hidden_size=64,
        dropout=0.0,
    )
    for parameter in model.parameters():
        torch.nn.init.constant_(parameter, 0.0)
    checkpoint = {
        "schema_id": SPBC_V2_DPO_CHECKPOINT_SCHEMA_ID,
        "model_key": SPBC_V2_DPO_MODEL_KEY,
        "model_state_dict": model.state_dict(),
        "model_config": model.config(),
        "normalization": {
            "sequence_mean": [0.0, 0.0],
            "sequence_std": [1.0, 1.0],
            "scalar_mean": [0.0 for _ in range(7)],
            "scalar_std": [1.0 for _ in range(7)],
            "candidate_mean": [0.0 for _ in range(7)],
            "candidate_std": [1.0 for _ in range(7)],
        },
    }
    torch.save(checkpoint, path)


def build_manifest_with_trace_files(root: Path) -> dict[str, object]:
    traces = []
    means = [650.0, 1500.0, 3500.0, 800.0, 2600.0, 4200.0]
    splits = ["train", "train", "train", "test", "test", "eval"]
    for index, (split, mean) in enumerate(zip(splits, means)):
        actual_path = root / "trazas" / "trace_{0:03d}.csv".format(index)
        rows = [
            {
                "timestamp_s": float(second),
                "duration_s": 1.0,
                "throughput_kbps": max(mean + 75.0 * ((second % 7) - 3), 50.0),
            }
            for second in range(120)
        ]
        stats = write_normalized_csv(rows, actual_path)
        traces.append(
            {
                "trace_id": "trace_{0:03d}".format(index),
                "dataset_id": "unit_dataset_{0}".format(index % 2),
                "converter_id": "unit_test",
                "normalized_trace_path": "/home/daniel/TFG/trazas/trace_{0:03d}.csv".format(index),
                "metadata_path": "/external/metadata/trace_{0:03d}.json".format(index),
                "source_path": "/external/raw/trace_{0:03d}.csv".format(index),
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
                "network_condition": "unit_network_trace",
                "synthetic": False,
                "usable_for_training": True,
                "usable_for_eval": True,
            }
        )
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


if __name__ == "__main__":
    unittest.main()

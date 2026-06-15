from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core.neural_abr.artifacts import read_json, read_jsonl
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v3.closedloop_spbc_spc_dataset import (
    SPBC_SPC_LEAKAGE_AUDIT_FILENAME,
    SPBC_SPC_SAMPLE_SCHEMA_ID,
    SPBC_SPC_SUMMARY_FILENAME,
    SPBC_SPC_TARGET_AUDIT_FILENAME,
    SPBC_SPC_TRAINING_DATA_FILENAME,
    SPBC_SPC_VALIDATION_DATA_FILENAME,
    build_phase45_v3_closedloop_spbc_spc_dataset,
    summarize_phase45_v3_closedloop_spbc_spc_dataset,
    validate_phase45_v3_closedloop_spbc_spc_dataset_dir,
)
from core.phase45_v3.profiles import Phase45V3DatasetProfile, profile_by_name
from tests.test_phase45_v1_dataset import build_manifest_with_trace_files


class Phase45V3ClosedLoopSpbcSpcDatasetTest(unittest.TestCase):
    def test_builds_valid_closedloop_policy_critic_dataset(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = build_manifest_with_trace_files(root)
            output_dir = root / "datasets_normalizados" / "phase45_v3" / "closedloop_spbc_spc_unit_v1"
            profile = Phase45V3DatasetProfile(
                name="unit",
                train_window_count=2,
                validation_window_count=1,
                qh_horizon_segments=2,
                qh_beam_width=4,
                max_windows_per_trace=1,
                synthetic_max_fraction=0.50,
                dataset_max_fraction=1.0,
                semantics_max_fraction=1.0,
                seed="unit-phase45-v3-spbc-spc",
                rollouts_per_window=2,
            )

            result = build_phase45_v3_closedloop_spbc_spc_dataset(
                manifest,
                output_dir=output_dir,
                profile=profile,
                overwrite=True,
                trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
            )
            validation = validate_phase45_v3_closedloop_spbc_spc_dataset_dir(output_dir)
            training_rows = read_jsonl(output_dir / SPBC_SPC_TRAINING_DATA_FILENAME)
            validation_rows = read_jsonl(output_dir / SPBC_SPC_VALIDATION_DATA_FILENAME)
            summary = read_json(output_dir / SPBC_SPC_SUMMARY_FILENAME)
            leakage = read_json(output_dir / SPBC_SPC_LEAKAGE_AUDIT_FILENAME)
            target_audit = read_json(output_dir / SPBC_SPC_TARGET_AUDIT_FILENAME)
            compact_summary = summarize_phase45_v3_closedloop_spbc_spc_dataset(output_dir)

            self.assertEqual("PASS", result["status"])
            self.assertEqual("PASS", validation["status"])
            self.assertEqual("PASS", compact_summary["status"])
            self.assertEqual(120, len(training_rows))
            self.assertEqual(60, len(validation_rows))
            self.assertEqual(60.0, summary["content_ladder"]["max_buffer_s"])
            self.assertFalse(summary["neural_mpc_line_modified"])
            self.assertTrue(summary["source_qh_oracle_used_as_label_factory"])
            self.assertEqual("qoe_linear_v1", summary["closed_loop_client_parity"]["qoe_formula_version"])
            self.assertEqual("PASS", leakage["status"])
            self.assertEqual("PASS", target_audit["status"])

            first = training_rows[0]
            self.assertEqual(SPBC_SPC_SAMPLE_SCHEMA_ID, first["schema_id"])
            self.assertNotIn("trace_id", first["model_inputs"]["context"])
            self.assertNotIn("future_throughput_kbps", first["model_inputs"]["context"])
            self.assertFalse(first["metadata"]["metadata_is_model_input"])
            self.assertFalse(first["audit"]["policy_targets_are_model_inputs"])
            self.assertFalse(first["audit"]["critic_targets_are_model_inputs"])
            self.assertFalse(first["audit"]["neural_mpc_line_modified"])
            self.assertEqual(6, len(first["spbc_policy_targets"]["soft_action_weights"]))
            self.assertAlmostEqual(1.0, sum(first["spbc_policy_targets"]["soft_action_weights"]), places=5)
            self.assertEqual(
                first["spbc_policy_targets"]["selected_action"],
                first["spc_critic_targets"]["best_action"],
            )
            self.assertEqual(6, len(first["spc_critic_targets"]["action_values"]))
            self.assertTrue(first["spbc_policy_targets"]["future_information_is_target_only"])
            self.assertTrue(first["spc_critic_targets"]["future_information_is_target_only"])

    def test_full_profile_exists_for_later_wsl_generation(self):
        profile = profile_by_name("full_v1")

        self.assertEqual("full_v1", profile.name)
        self.assertEqual(4096, profile.train_window_count)
        self.assertEqual(1024, profile.validation_window_count)
        self.assertEqual(5, profile.qh_horizon_segments)
        self.assertEqual(4, profile.rollouts_per_window)


if __name__ == "__main__":
    unittest.main()

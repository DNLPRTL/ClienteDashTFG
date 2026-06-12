from __future__ import annotations

import copy
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from unittest import mock

from core.neural_abr.artifacts import read_json, read_jsonl
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v3.constants import (
    LEAKAGE_AUDIT_FILENAME,
    QH_AUDIT_FILENAME,
    SUMMARY_FILENAME,
    TRAINING_DATA_FILENAME,
    VALIDATION_DATA_FILENAME,
)
from core.phase45_v3.dataset import build_phase45_v3_qh_dataset
from core.phase45_v3.profiles import Phase45V3DatasetProfile
from core.phase45_v3.qh_scorer_training import (
    QH_SCORER_MODEL_FILENAME,
    _sample_to_arrays,
    train_phase45_v3_qh_scorer,
    training_profile_by_name,
)
from core.phase45_v3.validation import validate_phase45_v3_dataset_dir
from scripts.summarize_phase45_v3_qh_dataset import summarize_phase45_v3_qh_dataset
from tests.test_phase45_v1_dataset import build_manifest_with_trace_files


class Phase45V3DatasetTest(unittest.TestCase):
    def test_constants_import_does_not_require_torch(self):
        original_import = __import__

        def guarded_import(name, *args, **kwargs):
            if name == "torch":
                raise AssertionError("phase45_v3 constants import must not require torch")
            return original_import(name, *args, **kwargs)

        with mock.patch("builtins.__import__", side_effect=guarded_import):
            from core.phase45_v3.constants import DATASET_SCHEMA_ID

        self.assertEqual("phase45_v3_closed_loop_qh_dataset_v1", DATASET_SCHEMA_ID)
        self.assertEqual("pilot_plus", training_profile_by_name("pilot_plus").name)
        self.assertLess(training_profile_by_name("pilot_plus").learning_rate, training_profile_by_name("pilot").learning_rate)
        self.assertEqual("pilot_rank", training_profile_by_name("pilot_rank").name)
        self.assertGreater(training_profile_by_name("pilot_rank").pairwise_rank_loss_weight, 0.0)
        self.assertLess(training_profile_by_name("pilot_rank").ce_loss_weight, training_profile_by_name("pilot").ce_loss_weight)

    def test_builds_valid_qh_dataset_with_closed_loop_client_contract(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = build_manifest_with_trace_files(root)
            output_dir = root / "datasets_normalizados" / "phase45_v3" / "unit_qh"
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
                seed="unit-phase45-v3",
                rollouts_per_window=2,
            )

            result = build_phase45_v3_qh_dataset(
                manifest,
                output_dir=output_dir,
                profile=profile,
                overwrite=True,
                trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
            )
            validation = validate_phase45_v3_dataset_dir(output_dir)
            training_rows = read_jsonl(output_dir / TRAINING_DATA_FILENAME)
            validation_rows = read_jsonl(output_dir / VALIDATION_DATA_FILENAME)
            summary = read_json(output_dir / SUMMARY_FILENAME)
            leakage = read_json(output_dir / LEAKAGE_AUDIT_FILENAME)
            qh_audit = read_json(output_dir / QH_AUDIT_FILENAME)

            self.assertEqual("PASS", result["status"])
            self.assertEqual("PASS", validation["status"])
            self.assertEqual(120, len(training_rows))
            self.assertEqual(60, len(validation_rows))
            self.assertEqual(60.0, summary["content_ladder"]["max_buffer_s"])
            self.assertEqual("qoe_linear_v1", summary["closed_loop_client_parity"]["qoe_formula_version"])
            self.assertEqual("PASS", leakage["status"])
            self.assertEqual("PASS", qh_audit["status"])
            compact_summary = summarize_phase45_v3_qh_dataset(output_dir)
            self.assertEqual("PASS", compact_summary["status"])
            self.assertEqual(2, compact_summary["rollouts_per_window"])

            first = training_rows[0]
            self.assertNotIn("trace_id", first["model_inputs"]["context"])
            self.assertNotIn("future_throughput_kbps", first["model_inputs"]["context"])
            self.assertFalse(first["metadata"]["metadata_is_model_input"])
            self.assertEqual(6, len(first["qh_targets"]["action_values"]))
            self.assertTrue(first["qh_targets"]["future_information_is_target_only"])
            self.assertFalse(first["audit"]["rollout_action_is_model_target"])

            sample_with_infeasible_action = copy.deepcopy(first)
            selected_action = int(sample_with_infeasible_action["qh_targets"]["selected_action"])
            infeasible_action = 0 if selected_action != 0 else 1
            sample_with_infeasible_action["qh_targets"]["action_values"][infeasible_action]["q_h_reward_n"] = None
            _context, _candidates, effective_mask, q_values, _selected, _high_capacity = _sample_to_arrays(
                sample_with_infeasible_action
            )
            self.assertFalse(effective_mask[infeasible_action])
            self.assertEqual(-1.0e9, q_values[infeasible_action])

    def test_trains_qh_scorer_smoke_checkpoint_from_unit_dataset(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = build_manifest_with_trace_files(root)
            output_dir = root / "datasets_normalizados" / "phase45_v3" / "unit_qh"
            model_dir = root / "modelos" / "phase45_v3" / "qh_scorer" / "unit"
            dataset_profile = Phase45V3DatasetProfile(
                name="unit",
                train_window_count=2,
                validation_window_count=1,
                qh_horizon_segments=2,
                qh_beam_width=4,
                max_windows_per_trace=1,
                synthetic_max_fraction=0.50,
                dataset_max_fraction=1.0,
                semantics_max_fraction=1.0,
                seed="unit-phase45-v3",
                rollouts_per_window=2,
            )
            build_phase45_v3_qh_dataset(
                manifest,
                output_dir=output_dir,
                profile=dataset_profile,
                overwrite=True,
                trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
            )
            training_profile = replace(
                training_profile_by_name("smoke"),
                max_training_samples=96,
                max_validation_samples=48,
                top1_accuracy_floor=0.0,
                mean_regret_tolerance=999.0,
            )

            report = train_phase45_v3_qh_scorer(
                output_dir,
                model_dir,
                training_profile,
                overwrite=True,
                device="cpu",
            )

            self.assertEqual("PASS", report["status"])
            self.assertEqual("phase45_v3_qh_scorer", report["model_key"])
            self.assertIn("pairwise_rank_loss_weight", report["profile"])
            self.assertTrue((model_dir / QH_SCORER_MODEL_FILENAME).is_file())
            self.assertIn("top1_accuracy", report["final_validation"])


if __name__ == "__main__":
    unittest.main()

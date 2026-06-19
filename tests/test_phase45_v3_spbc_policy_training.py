from __future__ import annotations

import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

import torch

from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v3.closedloop_spbc_spc_dataset import build_phase45_v3_closedloop_spbc_spc_dataset
from core.phase45_v3.profiles import Phase45V3DatasetProfile
from core.phase45_v3.spbc_policy_training import (
    PHASE45_V3_SPBC_POLICY_MODEL_KEY,
    SPBC_POLICY_MODEL_FILENAME,
    _renormalize_targets,
    _sample_to_arrays,
    spbc_policy_training_profile_by_name,
    train_phase45_v3_spbc_policy,
)
from tests.test_phase45_v1_dataset import build_manifest_with_trace_files


class Phase45V3SpbcPolicyTrainingTest(unittest.TestCase):
    def test_target_renormalization_masks_invalid_actions(self):
        targets = torch.tensor([[0.2, 0.3, 0.5]])
        valid = torch.tensor([[True, False, True]])

        clean = _renormalize_targets(targets, valid)

        self.assertAlmostEqual(0.0, float(clean[0, 1]), places=7)
        self.assertAlmostEqual(1.0, float(clean.sum()), places=6)

    def test_trains_spbc_policy_smoke_checkpoint_from_unit_dataset(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = build_manifest_with_trace_files(root)
            dataset_dir = root / "datasets_normalizados" / "phase45_v3" / "closedloop_spbc_spc_unit_v1"
            model_dir = root / "modelos" / "phase45_v3" / "spbc_policy" / "unit"
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
                seed="unit-phase45-v3-spbc-policy",
                rollouts_per_window=2,
            )
            build_phase45_v3_closedloop_spbc_spc_dataset(
                manifest,
                output_dir=dataset_dir,
                profile=dataset_profile,
                overwrite=True,
                trace_path_rewrites=(PathRewriteRule("/home/daniel/TFG", str(root)),),
            )
            profile = replace(
                spbc_policy_training_profile_by_name("smoke"),
                top1_accuracy_floor=0.0,
                high_capacity_action0_tolerance=1.0,
                catastrophic_action_tolerance=1.0,
            )

            report = train_phase45_v3_spbc_policy(
                dataset_dir,
                model_dir,
                profile,
                overwrite=True,
                device="cpu",
            )

            self.assertEqual("PASS", report["status"])
            self.assertEqual(PHASE45_V3_SPBC_POLICY_MODEL_KEY, report["model_key"])
            self.assertFalse(report["sample_weight_metadata_used_as_model_input"])
            self.assertEqual("PASS", report["dataset_validation"]["status"])
            self.assertTrue((model_dir / SPBC_POLICY_MODEL_FILENAME).is_file())
            self.assertIn("top1_accuracy", report["final_validation"])

    def test_sample_arrays_keep_targets_out_of_model_inputs(self):
        sample = {
            "data_role": "training",
            "model_inputs": {
                "context": {
                    "throughput_history_bps": [0, 0, 0, 0, 10_000_000],
                    "download_time_history_s": [0, 0, 0, 0, 1.0],
                    "buffer_s": 12.0,
                    "last_representation_index": 1.0,
                    "last_bitrate_bps": 750_000.0,
                    "recent_rebuffer_s": 0.0,
                    "recent_switch_abs": 0.0,
                    "chunks_remaining_norm": 0.5,
                    "has_chunks_remaining": 1.0,
                },
                "candidates": [
                    {
                        "candidate_representation_index": float(index),
                        "candidate_ladder_position_norm": float(index) / 5.0,
                        "candidate_bitrate_bps": float(bitrate),
                        "candidate_bitrate_norm_ladder": float(index) / 5.0,
                        "candidate_delta_from_last_bitrate_norm": 0.0,
                        "candidate_chunk_size_bytes": 1000.0,
                        "candidate_chunk_size_available": 1.0,
                    }
                    for index, bitrate in enumerate((300000, 750000, 1200000, 1850000, 2850000, 4300000))
                ],
                "action_mask": [True, True, True, True, True, True],
            },
            "spbc_policy_targets": {
                "target_id": "phase45_v3_closedloop_spbc_policy_targets_v1",
                "selected_action": 3,
                "soft_action_weights": [0.01, 0.02, 0.05, 0.80, 0.10, 0.02],
            },
            "spc_critic_targets": {
                "target_id": "phase45_v3_closedloop_spc_critic_targets_v1",
                "action_values": [
                    {"action": index, "q_h_regret_n": float(abs(index - 3)), "is_catastrophic_regret_2": index == 0}
                    for index in range(6)
                ],
            },
            "metadata": {"metadata_is_model_input": False, "throughput_bucket": "5_20_mbps"},
        }

        arrays = _sample_to_arrays(sample)

        self.assertEqual(3, arrays.selected_action)
        self.assertTrue(arrays.high_capacity_safe)
        self.assertAlmostEqual(1.0, sum(arrays.soft_targets), places=6)


if __name__ == "__main__":
    unittest.main()

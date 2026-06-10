from __future__ import annotations

import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

import torch

from core.neural_abr.artifacts import read_json, read_jsonl, write_jsonl
from core.phase45_v1.preference_dataset_v2 import V2_TRAINING_DATA_FILENAME
from core.phase45_v1.spc_v2_reward_risk_training import (
    SPC_V2_REWARD_RISK_MODEL_FILENAME,
    SPC_V2_REWARD_RISK_TRAINING_REPORT_FILENAME,
    SpcAbrV2RewardRiskScorer,
    SpcV2RewardRiskTrainingError,
    evaluate_spc_v2_reward_risk_model,
    fit_spc_v2_reward_risk_normalization,
    profile_by_name,
    train_spc_abr_v2_reward_risk,
    _loss_components,
    _selection_score,
)
from core.phase45_v1.spbc_v2_dpo_training import examples_to_tensors, load_spbc_v2_dpo_examples
from tests.test_phase45_v2_spbc_dpo_training import build_unit_v2_dataset


class Phase45V2SpcRewardRiskTrainingTest(unittest.TestCase):
    def test_model_forward_outputs_per_action_reward_risk_surface_and_masks_invalid_actions(self):
        model = SpcAbrV2RewardRiskScorer(
            history_hidden_size=8,
            state_hidden_size=8,
            candidate_hidden_size=8,
            shared_hidden_size=16,
            dropout=0.0,
        )
        sequence = torch.zeros((2, 8, 2), dtype=torch.float32)
        scalars = torch.zeros((2, 7), dtype=torch.float32)
        candidates = torch.zeros((2, 6, 7), dtype=torch.float32)
        mask = torch.tensor([[True, True, False, False, False, False], [True, False, True, False, False, False]])

        outputs = model(sequence, scalars, candidates, mask)

        self.assertEqual((2, 6), outputs["action_scores"].shape)
        self.assertLess(float(outputs["action_scores"][0, 2]), -1.0e8)
        self.assertEqual((2, 6), outputs["predicted_reward_n_by_action"].shape)
        self.assertEqual((2, 6), outputs["predicted_rebuffer_s_by_action"].shape)
        self.assertEqual((2, 6), outputs["predicted_qoe_gap_by_action"].shape)
        self.assertEqual((2, 6), outputs["predicted_smoothness_mbps_by_action"].shape)
        self.assertEqual((2, 6), outputs["predicted_target_risk_logits_by_action"].shape)
        self.assertFalse(model.config()["forward_input_contract"]["per_action_outcomes_used_as_inputs"])
        self.assertFalse(model.config()["forward_input_contract"]["metadata_used_as_input"])
        self.assertTrue(model.config()["prediction_heads"]["targets_used_only_for_training"])

    def test_loader_rejects_forbidden_target_fields_inside_model_inputs(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir = build_unit_v2_dataset(root, with_spbc=False)
            rows = list(read_jsonl(dataset_dir / V2_TRAINING_DATA_FILENAME))
            first = dict(rows[0])
            model_inputs = dict(first["model_inputs"])
            model_inputs["reward_n"] = 123.0
            first["model_inputs"] = model_inputs
            rows[0] = first
            write_jsonl(dataset_dir / V2_TRAINING_DATA_FILENAME, rows)

            with self.assertRaises(Exception):
                load_spbc_v2_dpo_examples(dataset_dir / V2_TRAINING_DATA_FILENAME, "training", limit=1)

    def test_loss_penalizes_bad_rebuffer_and_risk_predictions(self):
        profile = replace(
            profile_by_name("smoke"),
            best_immediate_ce_loss_weight=0.0,
            pairwise_score_loss_weight=0.0,
            reward_loss_weight=0.0,
            rebuffer_loss_weight=1.0,
            qoe_gap_loss_weight=0.0,
            smoothness_loss_weight=0.0,
            risk_loss_weight=1.0,
        )
        batch = (
            torch.zeros((1, 8, 2), dtype=torch.float32),
            torch.zeros((1, 7), dtype=torch.float32),
            torch.zeros((1, 2, 7), dtype=torch.float32),
            torch.tensor([[True, True]], dtype=torch.bool),
            torch.tensor([0], dtype=torch.long),
            torch.tensor([0], dtype=torch.long),
            torch.tensor([[0.0, 1.0]], dtype=torch.float32),
            torch.tensor([[0.0, 2.0]], dtype=torch.float32),
            torch.tensor([[2.0, -4.0]], dtype=torch.float32),
            torch.zeros((1, 2), dtype=torch.float32),
            torch.zeros((1, 2), dtype=torch.float32),
            torch.tensor([[0.0, 1.0]], dtype=torch.float32),
            torch.tensor([1.0], dtype=torch.float32),
            torch.tensor([[0]], dtype=torch.long),
            torch.tensor([[1]], dtype=torch.long),
            torch.tensor([[1.0]], dtype=torch.float32),
            torch.tensor([[1.0]], dtype=torch.float32),
            torch.tensor([[True]], dtype=torch.bool),
            torch.tensor([[0.0, 1.0]], dtype=torch.float32),
        )
        good_outputs = {
            "action_scores": torch.tensor([[2.0, -3.0]], dtype=torch.float32),
            "predicted_reward_n_by_action": torch.zeros((1, 2), dtype=torch.float32),
            "predicted_rebuffer_s_by_action": torch.tensor([[0.0, 2.0]], dtype=torch.float32),
            "predicted_qoe_gap_by_action": torch.zeros((1, 2), dtype=torch.float32),
            "predicted_smoothness_mbps_by_action": torch.zeros((1, 2), dtype=torch.float32),
            "predicted_target_risk_logits_by_action": torch.tensor([[-4.0, 4.0]], dtype=torch.float32),
        }
        bad_outputs = {
            **good_outputs,
            "predicted_rebuffer_s_by_action": torch.tensor([[2.0, 0.0]], dtype=torch.float32),
            "predicted_target_risk_logits_by_action": torch.tensor([[4.0, -4.0]], dtype=torch.float32),
        }

        good_losses = _loss_components(good_outputs, batch, profile)
        bad_losses = _loss_components(bad_outputs, batch, profile)

        self.assertGreater(float(bad_losses["rebuffer_loss"]), float(good_losses["rebuffer_loss"]))
        self.assertGreater(float(bad_losses["risk_loss"]), float(good_losses["risk_loss"]))

    def test_smoke_training_writes_checkpoint_report_and_reference_comparison_audit(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir = build_unit_v2_dataset(root, with_spbc=False)
            output_dir = root / "modelos" / "phase45_v1" / "spc_abr_v2_reward_risk" / "smoke"
            profile = replace(profile_by_name("smoke"), epochs=1, batch_size=32, max_training_samples=96, max_validation_samples=48)

            report = train_spc_abr_v2_reward_risk(
                dataset_dir,
                output_dir,
                profile=profile,
                overwrite=True,
                device="cpu",
                validate_dataset=True,
                reference_policy_checkpoint=root / "missing_policy.pt",
                progress_callback=None,
            )
            report_file = read_json(output_dir / SPC_V2_REWARD_RISK_TRAINING_REPORT_FILENAME)

            self.assertEqual("PASS", report["status"])
            self.assertTrue((output_dir / SPC_V2_REWARD_RISK_MODEL_FILENAME).is_file())
            self.assertFalse(report_file["benchmark_performed"])
            self.assertFalse(report_file["ranking_performed"])
            self.assertFalse(report_file["bundle_exported"])
            self.assertFalse(report_file["controller_registered"])
            self.assertIn("focus_2_5_mbps", report_file["validation_metrics"])
            self.assertIn("by_rollout_source", report_file["validation_metrics"])
            self.assertIn("by_synthetic_source", report_file["validation_metrics"])
            self.assertIn("reward_mae", report_file["validation_metrics"])
            self.assertIn("rebuffer_mae_s", report_file["validation_metrics"])
            self.assertIn("qoe_gap_mae", report_file["validation_metrics"])
            self.assertIn("risk_brier", report_file["validation_metrics"])
            self.assertIn("selected_utility_regret_vs_best_immediate_mean", report_file["validation_metrics"])
            self.assertEqual("validation_selection_score", report_file["checkpoint_selection"]["criterion"])
            self.assertFalse(report_file["reference_policy_comparison"]["available"])
            self.assertEqual("reference_policy_checkpoint_missing", report_file["reference_policy_comparison"]["reason"])

    def test_selection_score_prioritizes_regret_rebuffer_prediction_and_focus_bucket(self):
        profile = profile_by_name("smoke")
        bad = {
            "selected_utility_regret_vs_best_immediate_mean": 0.20,
            "selected_rebuffer_regret_vs_best_immediate_mean": 0.08,
            "over_aggressive_rate_vs_oracle": 0.25,
            "invalid_action_rate": 0.0,
            "reward_mae": 1.0,
            "rebuffer_mae_s": 0.8,
            "qoe_gap_mae": 0.6,
            "risk_brier": 0.3,
            "focus_2_5_mbps": {
                "bucket_present": True,
                "selected_utility_regret_vs_best_immediate_mean": 0.40,
                "selected_rebuffer_regret_vs_best_immediate_mean": 0.10,
                "over_aggressive_rate_vs_oracle": 0.25,
                "invalid_action_rate": 0.0,
            },
        }
        good = {
            "selected_utility_regret_vs_best_immediate_mean": 0.05,
            "selected_rebuffer_regret_vs_best_immediate_mean": 0.01,
            "over_aggressive_rate_vs_oracle": 0.08,
            "invalid_action_rate": 0.0,
            "reward_mae": 0.4,
            "rebuffer_mae_s": 0.2,
            "qoe_gap_mae": 0.2,
            "risk_brier": 0.1,
            "focus_2_5_mbps": {
                "bucket_present": True,
                "selected_utility_regret_vs_best_immediate_mean": 0.06,
                "selected_rebuffer_regret_vs_best_immediate_mean": 0.01,
                "over_aggressive_rate_vs_oracle": 0.08,
                "invalid_action_rate": 0.0,
            },
        }

        self.assertLess(_selection_score(good, profile), _selection_score(bad, profile))

    def test_evaluation_reports_per_bucket_and_rollout(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dataset_dir = build_unit_v2_dataset(root, with_spbc=False)
            examples = load_spbc_v2_dpo_examples(dataset_dir / V2_TRAINING_DATA_FILENAME, "training", limit=24)
            normalization = fit_spc_v2_reward_risk_normalization(examples)
            tensors = examples_to_tensors(examples, normalization)
            loader = torch.utils.data.DataLoader(torch.utils.data.TensorDataset(*tensors), batch_size=8)
            profile = profile_by_name("smoke")
            model = SpcAbrV2RewardRiskScorer(
                history_hidden_size=8,
                state_hidden_size=8,
                candidate_hidden_size=8,
                shared_hidden_size=16,
                dropout=0.0,
            )

            metrics = evaluate_spc_v2_reward_risk_model(
                model,
                loader,
                device=torch.device("cpu"),
                profile=profile,
                examples=examples,
            )

            self.assertIn("by_throughput_bucket", metrics)
            self.assertIn("by_rollout_source", metrics)
            self.assertIn("focus_2_5_mbps", metrics)
            self.assertIn("reward_mae", metrics)


if __name__ == "__main__":
    unittest.main()

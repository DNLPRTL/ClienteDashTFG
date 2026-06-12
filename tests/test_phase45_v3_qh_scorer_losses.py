from __future__ import annotations

import unittest
from dataclasses import replace

import torch

from core.neural_abr.constants import CANDIDATE_VECTOR_NAMES, CONTEXT_VECTOR_NAMES
from core.phase45_v3.qh_scorer_training import (
    Phase45V3TemporalGruQhScorer,
    _catastrophic_prob_loss,
    _expected_regret_loss,
    _sample_weight_for_example,
    _soft_q_target_probs,
    _structured_cost_hinge_loss,
    _top_vs_bad_margin_loss,
    training_profile_by_name,
)


class Phase45V3QhScorerLossesTest(unittest.TestCase):
    def test_soft_q_target_probs_ignore_invalid_actions(self):
        q_values = torch.tensor([[2.0, 1.0, 100.0]])
        valid = torch.tensor([[True, True, False]])

        probs = _soft_q_target_probs(q_values, valid, temperature=0.35)

        self.assertAlmostEqual(0.0, float(probs[0, 2]), places=7)
        self.assertAlmostEqual(1.0, float(probs[0, :2].sum()), places=6)
        self.assertGreater(float(probs[0, 0]), float(probs[0, 1]))

    def test_expected_regret_is_near_zero_when_policy_selects_best_action(self):
        profile = replace(training_profile_by_name("pilot_adv_regret_v1"), expected_regret_loss_weight=1.0)
        scores = torch.tensor([[20.0, -20.0, -20.0, -1.0e9]])
        q_values = torch.tensor([[2.0, 1.0, 0.0, 100.0]])
        valid = torch.tensor([[True, True, True, False]])

        loss, per_sample = _expected_regret_loss(scores, q_values, valid, profile)

        self.assertLess(float(loss), 1.0e-5)
        self.assertLess(float(per_sample[0]), 1.0e-5)

    def test_expected_regret_increases_when_policy_selects_bad_action(self):
        profile = replace(training_profile_by_name("pilot_adv_regret_v1"), expected_regret_loss_weight=1.0)
        good_scores = torch.tensor([[20.0, -20.0, -20.0]])
        bad_scores = torch.tensor([[-20.0, -20.0, 20.0]])
        q_values = torch.tensor([[2.0, 1.0, 0.0]])
        valid = torch.tensor([[True, True, True]])

        good_loss, _good = _expected_regret_loss(good_scores, q_values, valid, profile)
        bad_loss, _bad = _expected_regret_loss(bad_scores, q_values, valid, profile)

        self.assertLess(float(good_loss), 1.0e-5)
        self.assertGreater(float(bad_loss), 1.9)

    def test_top_vs_bad_margin_returns_zero_when_no_bad_actions_exist(self):
        profile = replace(
            training_profile_by_name("pilot_adv_regret_v1"),
            top_vs_bad_margin_loss_weight=1.0,
            top_vs_bad_regret_threshold=0.50,
        )
        scores = torch.tensor([[1.0, 0.8, 0.7]])
        q_values = torch.tensor([[2.0, 1.8, 1.7]])
        valid = torch.tensor([[True, True, True]])

        loss = _top_vs_bad_margin_loss(scores, q_values, valid, profile)

        self.assertEqual(0.0, float(loss))

    def test_structured_cost_hinge_is_zero_when_best_score_has_required_margin(self):
        profile = replace(
            training_profile_by_name("pilot_adv_regret_hardneg_v1"),
            structured_cost_hinge_loss_weight=1.0,
            structured_cost_margin_scale=0.5,
            structured_cost_gap_cap=10.0,
        )
        scores = torch.tensor([[4.0, 1.0, 0.0]])
        q_values = torch.tensor([[2.0, 1.0, 0.0]])
        valid = torch.tensor([[True, True, True]])

        loss, per_sample = _structured_cost_hinge_loss(scores, q_values, valid, profile)

        self.assertAlmostEqual(0.0, float(loss), places=6)
        self.assertAlmostEqual(0.0, float(per_sample[0]), places=6)

    def test_structured_cost_hinge_increases_when_high_regret_action_wins_score(self):
        profile = replace(
            training_profile_by_name("pilot_adv_regret_hardneg_v1"),
            structured_cost_hinge_loss_weight=1.0,
            structured_cost_margin_scale=0.5,
            structured_cost_gap_cap=10.0,
        )
        scores = torch.tensor([[0.0, 5.0, 0.0]])
        q_values = torch.tensor([[2.0, 0.0, 1.0]])
        valid = torch.tensor([[True, True, True]])

        loss, per_sample = _structured_cost_hinge_loss(scores, q_values, valid, profile)

        self.assertGreater(float(loss), 5.9)
        self.assertGreater(float(per_sample[0]), 5.9)

    def test_catastrophic_prob_loss_ignores_invalid_actions(self):
        profile = replace(
            training_profile_by_name("pilot_adv_regret_hardneg_v1"),
            catastrophic_prob_loss_weight=1.0,
            catastrophic_regret_threshold=1.0,
            catastrophic_regret_cap=10.0,
            catastrophic_regret_power=1.0,
        )
        scores = torch.tensor([[-10.0, 10.0, 100.0]])
        q_values = torch.tensor([[2.0, 0.0, -100.0]])
        valid = torch.tensor([[True, True, False]])

        loss = _catastrophic_prob_loss(scores, q_values, valid, profile)

        self.assertGreater(float(loss), 0.19)
        self.assertLess(float(loss), 0.21)

    def test_catastrophic_prob_loss_is_zero_without_bad_actions(self):
        profile = replace(
            training_profile_by_name("pilot_adv_regret_hardneg_v1"),
            catastrophic_prob_loss_weight=1.0,
            catastrophic_regret_threshold=5.0,
        )
        scores = torch.tensor([[0.0, 1.0]])
        q_values = torch.tensor([[2.0, 1.9]])
        valid = torch.tensor([[True, True]])

        loss = _catastrophic_prob_loss(scores, q_values, valid, profile)

        self.assertEqual(0.0, float(loss))
        self.assertFalse(torch.isnan(loss))

    def test_slice_weight_clamps_and_uses_metadata_only_for_training_weight(self):
        profile = replace(training_profile_by_name("pilot_adv_regret_hardneg_v1"), slice_weight_max=5.0)
        sample = {
            "model_inputs": {"context": {"buffer_s": 3.0}},
            "metadata": {
                "metadata_is_model_input": False,
                "throughput_bucket": "2_5_mbps",
                "rollout_policy": "qh_plus_one",
                "dataset_id": "not_used_for_weight",
            },
            "qh_targets": {
                "action_values": [
                    {"action": 0, "q_h_reward_n": 0.0},
                    {"action": 1, "q_h_reward_n": -30.0},
                ]
            },
        }

        weight = _sample_weight_for_example(sample, profile)

        self.assertEqual(5.0, weight)
        self.assertFalse(sample["metadata"]["metadata_is_model_input"])

    def test_hardneg_v2_keeps_slice_weight_less_saturated_than_v1(self):
        profile = training_profile_by_name("pilot_adv_regret_hardneg_v2")
        sample = {
            "model_inputs": {"context": {"buffer_s": 3.0}},
            "metadata": {
                "metadata_is_model_input": False,
                "throughput_bucket": "2_5_mbps",
                "rollout_policy": "qh_plus_one",
                "dataset_id": "not_used_for_weight",
            },
            "qh_targets": {
                "action_values": [
                    {"action": 0, "q_h_reward_n": 0.0},
                    {"action": 1, "q_h_reward_n": -30.0},
                ]
            },
        }

        weight = _sample_weight_for_example(sample, profile)

        self.assertEqual(3.0, weight)
        self.assertLess(weight, training_profile_by_name("pilot_adv_regret_hardneg_v1").slice_weight_max)

    def test_temporal_gru_scorer_masks_invalid_actions(self):
        model = Phase45V3TemporalGruQhScorer(
            context_dim=len(CONTEXT_VECTOR_NAMES),
            candidate_dim=len(CANDIDATE_VECTOR_NAMES),
            hidden_sizes=(16,),
            history_gru_hidden_size=8,
        )
        context = torch.zeros((2, len(CONTEXT_VECTOR_NAMES)), dtype=torch.float32)
        candidates = torch.zeros((2, 6, len(CANDIDATE_VECTOR_NAMES)), dtype=torch.float32)
        mask = torch.tensor(
            [
                [True, True, False, True, True, True],
                [True, False, False, False, True, True],
            ]
        )

        scores = model(context, candidates, mask)

        self.assertEqual((2, 6), tuple(scores.shape))
        self.assertLess(float(scores[0, 2]), -1.0e8)
        self.assertLess(float(scores[1, 1]), -1.0e8)
        self.assertEqual("gru_candidate_qh_scorer", model.config()["model_type"])


if __name__ == "__main__":
    unittest.main()

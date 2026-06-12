from __future__ import annotations

import unittest
from dataclasses import replace

import torch

from core.phase45_v3.qh_scorer_training import (
    _expected_regret_loss,
    _soft_q_target_probs,
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


if __name__ == "__main__":
    unittest.main()

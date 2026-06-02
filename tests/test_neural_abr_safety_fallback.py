from __future__ import annotations

import unittest
from unittest import mock

from core.controller.neural_abr_safety import apply_safety_guard, select_fallback_action


class NeuralAbrSafetyFallbackTest(unittest.TestCase):
    def test_safe_raw_action_is_preserved(self):
        decision = apply_safety_guard(
            raw_action=2,
            rates_Bps=[100.0, 200.0, 400.0],
            action_mask=[True, True, True],
            feedback=feedback(queued_time=10.0, fragment_duration=2.0),
            throughput_history_Bps=[1000.0],
        )

        self.assertFalse(decision.intervened)
        self.assertFalse(decision.fallback_required)
        self.assertEqual(2, decision.action)
        self.assertEqual(400.0, decision.rate_Bps)

    def test_unsafe_raw_action_downshifts_to_highest_lower_feasible_representation(self):
        decision = apply_safety_guard(
            raw_action=2,
            rates_Bps=[100.0, 200.0, 400.0],
            action_mask=[True, True, True],
            feedback=feedback(queued_time=1.5, fragment_duration=2.0),
            throughput_history_Bps=[250.0],
        )

        self.assertTrue(decision.intervened)
        self.assertFalse(decision.fallback_required)
        self.assertEqual(1, decision.action)
        self.assertEqual(200.0, decision.rate_Bps)

    def test_no_feasible_action_uses_lowest_representation(self):
        decision = apply_safety_guard(
            raw_action=2,
            rates_Bps=[100.0, 200.0, 400.0],
            action_mask=[True, True, True],
            feedback=feedback(queued_time=1.0, fragment_duration=2.0),
            throughput_history_Bps=[50.0],
        )

        self.assertTrue(decision.intervened)
        self.assertEqual("emergency_lowest_representation", decision.reason)
        self.assertEqual(0, decision.action)
        self.assertEqual(100.0, decision.rate_Bps)

    def test_missing_safety_signals_request_fallback(self):
        decision = apply_safety_guard(
            raw_action=1,
            rates_Bps=[100.0, 200.0],
            action_mask=[True, True],
            feedback=feedback(fragment_duration=0.0),
            throughput_history_Bps=[],
        )

        self.assertTrue(decision.fallback_required)
        self.assertEqual("safety_guard_rejected", decision.reason)

    def test_fallback_robust_mpc_called_when_available(self):
        with mock.patch(
            "core.controller.neural_abr_safety.RobustMpcController.calcControlAction",
            return_value=200.0,
        ) as calc:
            decision = select_fallback_action(
                feedback(),
                [100.0, 200.0, 400.0],
                [True, True, True],
                fallback_controller="robust_mpc",
            )

        calc.assert_called_once()
        self.assertEqual(1, decision.action)
        self.assertEqual(200.0, decision.rate_Bps)
        self.assertIn(decision.rate_Bps, [100.0, 200.0, 400.0])

    def test_fallback_failure_uses_lowest_valid_representation(self):
        with mock.patch("core.controller.neural_abr_safety._create_fallback_controller", side_effect=RuntimeError("fail")):
            decision = select_fallback_action(
                feedback(),
                [100.0, 200.0, 400.0],
                [True, True, True],
            )

        self.assertEqual("fallback_controller_failed", decision.reason)
        self.assertEqual(0, decision.action)
        self.assertEqual(100.0, decision.rate_Bps)


def feedback(**overrides):
    data = {
        "queued_time": 8.0,
        "fragment_duration": 2.0,
        "level": 1,
        "max_level": 2,
        "rates": [100.0, 200.0, 400.0],
        "last_fragment_size": 1000,
        "last_download_time": 2.0,
        "segment_index": 1,
    }
    data.update(overrides)
    return data


if __name__ == "__main__":
    unittest.main()

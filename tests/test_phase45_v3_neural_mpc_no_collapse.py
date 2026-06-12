from __future__ import annotations

import unittest
from dataclasses import replace

from core.phase45_v3.abr_closed_loop_env import default_phase45_v3_ladder, initial_closed_loop_state
from core.phase45_v3.neural_mpc_controller import NeuralThroughputCalibratedMpcController


class Phase45V3NeuralMpcNoCollapseTest(unittest.TestCase):
    def test_high_capacity_state_does_not_select_action0_with_valid_prediction(self):
        ladder = default_phase45_v3_ladder(segment_count=5)
        state = replace(
            initial_closed_loop_state(ladder, initial_buffer_s=20.0),
            last_representation_index=3,
            throughput_history_bps=(12_000_000.0, 14_000_000.0, 16_000_000.0),
        )

        def predictor(_state, _ladder):
            return tuple((8_000_000.0, 10_000_000.0, 12_000_000.0, 16_000_000.0) for _ in range(5))

        controller = NeuralThroughputCalibratedMpcController(predictor)
        decision = controller.select_action(state, ladder)

        self.assertFalse(decision.fallback_used)
        self.assertGreater(decision.action, 0)
        self.assertGreaterEqual(decision.bitrate_bps, 1_850_000.0)

    def test_invalid_prediction_falls_back_explicitly(self):
        ladder = default_phase45_v3_ladder(segment_count=5)
        state = initial_closed_loop_state(ladder, initial_buffer_s=12.0)

        def predictor(_state, _ladder):
            return ((float("nan"), 1.0, 2.0, 3.0),) * 5

        controller = NeuralThroughputCalibratedMpcController(predictor)
        decision = controller.select_action(state, ladder)

        self.assertTrue(decision.fallback_used)
        self.assertNotEqual("success_neural_mpc", decision.fallback_reason)


if __name__ == "__main__":
    unittest.main()

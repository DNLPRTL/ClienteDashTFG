from __future__ import annotations

import unittest
from dataclasses import replace

from core.phase45_v3.abr_closed_loop_env import default_phase45_v3_ladder, initial_closed_loop_state
from core.phase45_v3.neural_mpc_controller import plan_neural_mpc_action, select_throughput_plan_for_buffer


class Phase45V3NeuralMpcPlannerTest(unittest.TestCase):
    def test_high_buffer_uses_median_quantile_and_selects_high_quality_when_safe(self):
        ladder = default_phase45_v3_ladder(segment_count=5)
        state = replace(
            initial_closed_loop_state(ladder, initial_buffer_s=24.0),
            throughput_history_bps=(20_000_000.0, 21_000_000.0, 22_000_000.0),
        )
        prediction = tuple((10_000_000.0, 15_000_000.0, 20_000_000.0, 25_000_000.0) for _ in range(5))

        decision = plan_neural_mpc_action(
            state=state,
            ladder=ladder,
            predicted_bps_by_horizon_quantile=prediction,
            quantiles=(0.10, 0.25, 0.50, 0.75),
            horizon_segments=5,
        )

        self.assertEqual("q50", decision.chosen_quantile)
        self.assertEqual(5, decision.action)
        self.assertFalse(decision.fallback_used)

    def test_low_buffer_uses_q10_and_avoids_aggressive_action(self):
        ladder = default_phase45_v3_ladder(segment_count=5)
        state = replace(
            initial_closed_loop_state(ladder, initial_buffer_s=1.0),
            last_representation_index=5,
            throughput_history_bps=(1_000_000.0, 900_000.0, 850_000.0),
        )
        prediction = tuple((450_000.0, 1_500_000.0, 6_000_000.0, 10_000_000.0) for _ in range(5))

        plan, label = select_throughput_plan_for_buffer(
            prediction,
            quantiles=(0.10, 0.25, 0.50, 0.75),
            buffer_s=1.0,
        )
        decision = plan_neural_mpc_action(
            state=state,
            ladder=ladder,
            predicted_bps_by_horizon_quantile=prediction,
            quantiles=(0.10, 0.25, 0.50, 0.75),
            horizon_segments=5,
        )

        self.assertEqual("q10", label)
        self.assertEqual((450_000.0,) * 5, plan)
        self.assertLessEqual(decision.action, 1)

    def test_medium_buffer_keeps_q25_before_blending(self):
        prediction = tuple((1_000_000.0, 2_200_000.0, 4_000_000.0, 8_000_000.0) for _ in range(5))

        plan, label = select_throughput_plan_for_buffer(
            prediction,
            quantiles=(0.10, 0.25, 0.50, 0.75),
            buffer_s=10.0,
        )

        self.assertEqual("q25", label)
        self.assertEqual((2_200_000.0,) * 5, plan)

    def test_high_medium_buffer_blends_q25_and_q50(self):
        prediction = tuple((1_000_000.0, 2_000_000.0, 4_000_000.0, 8_000_000.0) for _ in range(5))

        plan, label = select_throughput_plan_for_buffer(
            prediction,
            quantiles=(0.10, 0.25, 0.50, 0.75),
            buffer_s=16.0,
        )

        self.assertEqual("blend_q25_q50", label)
        self.assertEqual((3_000_000.0,) * 5, plan)


if __name__ == "__main__":
    unittest.main()

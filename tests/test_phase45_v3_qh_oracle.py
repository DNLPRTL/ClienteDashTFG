from __future__ import annotations

import unittest

from core.phase45_v3.abr_closed_loop_env import default_phase45_v3_ladder, initial_closed_loop_state
from core.phase45_v3.qh_oracle import QhOracleConfig, evaluate_qh_actions, qh_oracle_card
from core.trace_replay.loader import load_normalized_trace_rows
from core.trace_replay.network_model import END_POLICY_LOOP, TraceDrivenNetworkModel


class Phase45V3QhOracleTest(unittest.TestCase):
    def test_high_capacity_buffered_state_prefers_top_bitrate(self):
        ladder = default_phase45_v3_ladder(segment_count=8, max_buffer_s=60.0)
        model = _constant_network_model(12000.0)
        state = initial_closed_loop_state(ladder, initial_buffer_s=12.0)

        decision = evaluate_qh_actions(state, ladder, model, QhOracleConfig(horizon_segments=4, beam_width=12))

        self.assertEqual(5, decision.action)
        self.assertFalse(decision.fallback_used)
        self.assertEqual((5, 5, 5, 5), _value_by_action(decision, 5).best_sequence)
        self.assertGreater(_value_by_action(decision, 5).q_h_reward_n, _value_by_action(decision, 0).q_h_reward_n)

    def test_low_capacity_state_prefers_lowest_bitrate_to_avoid_rebuffer_collapse(self):
        ladder = default_phase45_v3_ladder(segment_count=8, max_buffer_s=60.0)
        model = _constant_network_model(350.0)
        state = initial_closed_loop_state(ladder, initial_buffer_s=10.0)

        decision = evaluate_qh_actions(state, ladder, model, QhOracleConfig(horizon_segments=3, beam_width=12))

        self.assertEqual(0, decision.action)
        self.assertFalse(decision.fallback_used)
        self.assertLess(_value_by_action(decision, 5).q_h_reward_n, _value_by_action(decision, 0).q_h_reward_n)

    def test_oracle_card_declares_future_information_as_target_only(self):
        card = qh_oracle_card(QhOracleConfig(horizon_segments=2, beam_width=3))

        self.assertTrue(card["uses_future_information"])
        self.assertTrue(card["future_information_is_target_only"])
        self.assertFalse(card["runtime_controller"])


def _constant_network_model(throughput_kbps: float) -> TraceDrivenNetworkModel:
    trace = load_normalized_trace_rows(
        [
            {"timestamp_s": 0.0, "duration_s": 60.0, "throughput_kbps": float(throughput_kbps)},
        ],
        trace_id="constant_{0}".format(int(throughput_kbps)),
    )
    return TraceDrivenNetworkModel(trace, end_policy=END_POLICY_LOOP, max_loops=4)


def _value_by_action(decision, action: int):
    return {row.action: row for row in decision.action_values}[int(action)]


if __name__ == "__main__":
    unittest.main()

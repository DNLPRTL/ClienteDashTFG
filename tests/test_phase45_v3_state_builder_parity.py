from __future__ import annotations

import unittest

from core.controller.neural_abr_runtime_features import NeuralAbrRuntimeFeatureBuilder
from core.phase45_v3.abr_closed_loop_env import (
    AbrClosedLoopEnv,
    default_phase45_v3_ladder,
    runtime_feedback_from_state,
)


class Phase45V3StateBuilderParityTest(unittest.TestCase):
    def test_runtime_feedback_from_closed_loop_state_matches_feature_builder_contract(self):
        ladder = default_phase45_v3_ladder(segment_count=30, max_buffer_s=60.0)
        env = AbrClosedLoopEnv(ladder=ladder, initial_buffer_s=10.0)
        last_step = env.step_with_download_time(1, 0.5)
        feedback = runtime_feedback_from_state(env.state, ladder, last_step=last_step)

        payload = NeuralAbrRuntimeFeatureBuilder().build(feedback)

        self.assertEqual(6, len(payload.candidate_features))
        self.assertEqual((True, True, True, True, True, True), payload.action_mask)
        self.assertAlmostEqual(env.state.buffer_s, payload.context_features["buffer_s"])
        self.assertAlmostEqual(1.0, payload.context_features["last_representation_index"])
        self.assertAlmostEqual(1.0, payload.context_features["has_chunks_remaining"])
        self.assertAlmostEqual((30 - env.state.segment_index - 1) / 30.0, payload.context_features["chunks_remaining_norm"])
        self.assertAlmostEqual(last_step.measured_throughput_bps, payload.context_features["throughput_history_bps"][-1])


if __name__ == "__main__":
    unittest.main()

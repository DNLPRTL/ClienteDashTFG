from __future__ import annotations

import unittest

from core.phase45_v3.abr_closed_loop_env import AbrClosedLoopEnv, default_phase45_v3_ladder


class Phase45V3ClosedLoopEnvStepTest(unittest.TestCase):
    def test_step_applies_client_buffer_cap_and_qoe_linear_reward(self):
        ladder = default_phase45_v3_ladder(segment_count=3, max_buffer_s=60.0)
        env = AbrClosedLoopEnv(ladder=ladder, initial_buffer_s=59.0)

        step = env.step_with_download_time(5, 0.1)

        self.assertEqual(5, step.action)
        self.assertAlmostEqual(60.0, step.buffer_s_after)
        self.assertAlmostEqual(4.3, step.quality_mbps)
        self.assertAlmostEqual(4.3, step.reward_n)
        self.assertAlmostEqual(60.0, env.state.buffer_s)

    def test_startup_rebuffer_is_penalized(self):
        ladder = default_phase45_v3_ladder(segment_count=3, max_buffer_s=60.0)
        env = AbrClosedLoopEnv(ladder=ladder, initial_buffer_s=0.0)

        step = env.step_with_download_time(0, 1.0)

        self.assertAlmostEqual(1.0, step.rebuffer_s)
        self.assertAlmostEqual(4.0, step.buffer_s_after)
        self.assertAlmostEqual(0.3 - 4.3, step.reward_n)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import unittest

from core.evaluation.qoe import SegmentQoEInput, compute_linear_qoe
from core.phase45_v3.abr_closed_loop_env import AbrClosedLoopEnv, default_phase45_v3_ladder


class Phase45V3QoEParityTest(unittest.TestCase):
    def test_step_rewards_match_phase6_linear_qoe_segments(self):
        ladder = default_phase45_v3_ladder(segment_count=3, max_buffer_s=60.0)
        env = AbrClosedLoopEnv(ladder=ladder, initial_buffer_s=10.0)
        steps = [
            env.step_with_download_time(0, 0.1),
            env.step_with_download_time(5, 0.1),
            env.step_with_download_time(5, 0.1),
        ]

        qoe = compute_linear_qoe(
            [SegmentQoEInput(step.bitrate_kbps, step.rebuffer_s) for step in steps]
        )

        self.assertEqual(tuple(round(step.reward_n, 10) for step in steps), tuple(round(x, 10) for x in qoe.segment_rewards))
        self.assertAlmostEqual(qoe.qoe_sum, sum(step.reward_n for step in steps))
        self.assertEqual((0.0, 4.0, 0.0), qoe.segment_smoothness)


if __name__ == "__main__":
    unittest.main()

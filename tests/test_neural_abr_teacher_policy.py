from __future__ import annotations

import unittest

from core.neural_abr.action_mask import build_action_mask
from core.neural_abr.constants import PRIMARY_TEACHER, REWARD_VERSION
from core.neural_abr.content_ladder import synthetic_smoke_ladder
from core.neural_abr.replay_env import ReplayState
from core.neural_abr.teacher_policy import robust_mpc_teacher


class NeuralAbrTeacherPolicyTest(unittest.TestCase):
    def test_teacher_outputs_valid_masked_action(self):
        ladder = synthetic_smoke_ladder(segment_count=4)
        state = ReplayState(
            segment_index=1,
            buffer_s=8.0,
            last_representation_index=1,
            previous_representation_index=0,
            throughput_history_bps=(3_000_000.0, 3_200_000.0),
            download_time_history_s=(1.0, 1.1),
            recent_rebuffer_s=0.0,
            recent_switch_abs=1.0,
            playback_time_s=2.1,
        )

        decision = robust_mpc_teacher().select_action(state, ladder, build_action_mask(ladder, 1))

        self.assertEqual(PRIMARY_TEACHER, decision.teacher_policy)
        self.assertEqual(REWARD_VERSION, decision.reward_version)
        self.assertGreaterEqual(decision.representation_index, 0)
        self.assertLess(decision.representation_index, ladder.representation_count)

    def test_teacher_uses_startup_fallback_without_history(self):
        ladder = synthetic_smoke_ladder(segment_count=4)
        state = ReplayState(0, 0.0, -1, -1, (), (), 0.0, 0.0, 0.0)

        decision = robust_mpc_teacher().select_action(state, ladder, build_action_mask(ladder, 0))

        self.assertEqual(0, decision.representation_index)
        self.assertEqual("startup_no_history_fallback", decision.reason)


if __name__ == "__main__":
    unittest.main()

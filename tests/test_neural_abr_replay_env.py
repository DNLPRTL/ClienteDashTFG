from __future__ import annotations

import unittest

from core.neural_abr.content_ladder import ContentLadder, Representation
from core.neural_abr.replay_env import TraceReplayEnvironment
from core.trace_replay.loader import load_normalized_trace_rows


class NeuralAbrReplayEnvTest(unittest.TestCase):
    def test_replay_uses_documented_buffer_update(self):
        trace = load_normalized_trace_rows(
            [{"timestamp_s": "0", "duration_s": "10", "throughput_kbps": "1000"}],
            trace_id="replay-trace",
            source="replay-test",
        )
        ladder = ContentLadder(
            representations=(Representation(0, 1_000_000),),
            segment_duration_s=4.0,
            segment_count=2,
            max_buffer_s=20.0,
        )
        env = TraceReplayEnvironment(trace, ladder)

        result = env.step(0)

        self.assertAlmostEqual(4.0, result.download_time_s)
        self.assertAlmostEqual(4.0, result.rebuffer_s)
        self.assertAlmostEqual(4.0, result.buffer_s_after)
        self.assertAlmostEqual(1_000_000.0, result.measured_throughput_bps)

    def test_replay_advances_history_after_step_only(self):
        trace = load_normalized_trace_rows(
            [{"timestamp_s": "0", "duration_s": "20", "throughput_kbps": "2000"}],
            trace_id="history-trace",
            source="replay-test",
        )
        ladder = ContentLadder((Representation(0, 1_000_000),), segment_count=2)
        env = TraceReplayEnvironment(trace, ladder)

        self.assertEqual((), env.state.throughput_history_bps)
        env.step(0)

        self.assertEqual((2_000_000.0,), env.state.throughput_history_bps)


if __name__ == "__main__":
    unittest.main()

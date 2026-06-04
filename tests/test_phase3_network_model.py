from __future__ import annotations

import unittest

from core.trace_replay.loader import load_normalized_trace_rows
from core.trace_replay.network_model import (
    END_POLICY_FAIL,
    END_POLICY_LOOP,
    TraceDrivenNetworkModel,
    TraceReplayError,
)


class Phase3NetworkModelTest(unittest.TestCase):
    def test_constant_throughput_trace_produces_expected_download_duration(self):
        model = TraceDrivenNetworkModel(self.load_trace([{"timestamp_s": 0, "duration_s": 10, "throughput_kbps": 1000}]))

        result = model.download(250000)

        self.assertEqual(250000, result.delivered_bytes)
        self.assertAlmostEqual(2.0, result.duration_s)
        self.assertAlmostEqual(1000.0, result.measured_throughput_kbps)
        self.assertEqual(END_POLICY_FAIL, result.end_policy)

    def test_zero_throughput_interval_waits_until_delivery(self):
        model = TraceDrivenNetworkModel(
            self.load_trace(
                [
                    {"timestamp_s": 0, "duration_s": 2, "throughput_kbps": 0},
                    {"timestamp_s": 2, "duration_s": 10, "throughput_kbps": 1000},
                ]
            )
        )

        result = model.download(125000)

        self.assertAlmostEqual(3.0, result.duration_s)
        self.assertEqual(2, result.samples_touched)

    def test_gaps_between_samples_are_no_delivery_time(self):
        model = TraceDrivenNetworkModel(
            self.load_trace(
                [
                    {"timestamp_s": 0, "duration_s": 1, "throughput_kbps": 1000},
                    {"timestamp_s": 3, "duration_s": 10, "throughput_kbps": 1000},
                ]
            )
        )

        result = model.download(125000, start_time_s=1.0)

        self.assertAlmostEqual(3.0, result.duration_s)
        self.assertAlmostEqual(4.0, result.end_time_s)

    def test_trace_exhaustion_with_fail_policy_raises(self):
        model = TraceDrivenNetworkModel(self.load_trace([{"timestamp_s": 0, "duration_s": 1, "throughput_kbps": 1000}]))

        with self.assertRaisesRegex(TraceReplayError, "trace exhausted"):
            model.download(250000)

    def test_loop_policy_can_wrap(self):
        model = TraceDrivenNetworkModel(
            self.load_trace([{"timestamp_s": 0, "duration_s": 1, "throughput_kbps": 1000}]),
            end_policy=END_POLICY_LOOP,
            max_loops=1,
        )

        result = model.download(250000)

        self.assertAlmostEqual(2.0, result.duration_s)
        self.assertEqual(END_POLICY_LOOP, result.end_policy)

    def test_all_zero_throughput_raises(self):
        model = TraceDrivenNetworkModel(
            self.load_trace(
                [
                    {"timestamp_s": 0, "duration_s": 1, "throughput_kbps": 0},
                    {"timestamp_s": 1, "duration_s": 1, "throughput_kbps": 0},
                ]
            ),
            end_policy=END_POLICY_LOOP,
            max_loops=5,
        )

        with self.assertRaisesRegex(TraceReplayError, "zero throughput"):
            model.download(1)

    def load_trace(self, rows):
        return load_normalized_trace_rows(rows, trace_id="synthetic")


if __name__ == "__main__":
    unittest.main()

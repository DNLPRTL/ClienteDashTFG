from __future__ import annotations

import csv
import os
import tempfile
import unittest

from core.trace_replay.fake_replay_adapter import TraceDrivenFakeReplayAdapter
from core.trace_replay.loader import load_normalized_trace_csv, load_normalized_trace_rows
from core.trace_replay.network_model import (
    END_POLICY_FAIL,
    END_POLICY_LOOP,
    TraceDrivenNetworkModel,
    TraceReplayError,
)


class TraceNetworkModelTest(unittest.TestCase):
    def test_constant_throughput_trace_produces_expected_download_duration(self):
        trace = self.load_trace(
            [
                {"timestamp_s": "0", "duration_s": "10", "throughput_kbps": "1000"},
            ]
        )
        model = TraceDrivenNetworkModel(trace)

        result = model.download(250000)

        self.assertEqual("synthetic-trace", result.trace_id)
        self.assertEqual(250000, result.requested_bytes)
        self.assertEqual(250000, result.delivered_bytes)
        self.assertAlmostEqual(0.0, result.start_time_s)
        self.assertAlmostEqual(2.0, result.end_time_s)
        self.assertAlmostEqual(2.0, result.duration_s)
        self.assertAlmostEqual(1000.0, result.measured_throughput_kbps)
        self.assertAlmostEqual(0.0, result.trace_time_start_s)
        self.assertAlmostEqual(2.0, result.trace_time_end_s)
        self.assertEqual(1, result.samples_touched)
        self.assertEqual(END_POLICY_FAIL, result.end_policy)

    def test_estimate_download_duration_aliases_download(self):
        trace = self.load_trace(
            [
                {"timestamp_s": "0", "duration_s": "10", "throughput_kbps": "1000"},
            ]
        )
        model = TraceDrivenNetworkModel(trace)

        direct = model.download(125000, start_time_s=1.0)
        estimated = model.estimate_download_duration(125000, start_time_s=1.0)

        self.assertEqual(direct, estimated)

    def test_zero_throughput_interval_causes_waiting_before_delivery(self):
        trace = self.load_trace(
            [
                {"timestamp_s": "0", "duration_s": "2", "throughput_kbps": "0"},
                {"timestamp_s": "2", "duration_s": "10", "throughput_kbps": "1000"},
            ]
        )
        model = TraceDrivenNetworkModel(trace)

        result = model.download(125000)

        self.assertAlmostEqual(3.0, result.duration_s)
        self.assertAlmostEqual(3.0, result.end_time_s)
        self.assertEqual(2, result.samples_touched)

    def test_non_zero_start_time_is_respected(self):
        trace = self.load_trace(
            [
                {"timestamp_s": "0", "duration_s": "10", "throughput_kbps": "1000"},
            ]
        )
        model = TraceDrivenNetworkModel(trace)

        result = model.download(125000, start_time_s=5.0)

        self.assertAlmostEqual(5.0, result.start_time_s)
        self.assertAlmostEqual(6.0, result.end_time_s)
        self.assertAlmostEqual(1.0, result.duration_s)
        self.assertAlmostEqual(5.0, result.trace_time_start_s)
        self.assertAlmostEqual(6.0, result.trace_time_end_s)

    def test_gaps_between_samples_are_treated_as_no_delivery_time(self):
        trace = self.load_trace(
            [
                {"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "1000"},
                {"timestamp_s": "3", "duration_s": "10", "throughput_kbps": "1000"},
            ]
        )
        model = TraceDrivenNetworkModel(trace)

        result = model.download(125000, start_time_s=1.0)

        self.assertAlmostEqual(3.0, result.duration_s)
        self.assertAlmostEqual(4.0, result.end_time_s)
        self.assertEqual(1, result.samples_touched)

    def test_trace_exhaustion_with_fail_policy_raises(self):
        trace = self.load_trace(
            [
                {"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "1000"},
            ]
        )
        model = TraceDrivenNetworkModel(trace, end_policy=END_POLICY_FAIL)

        with self.assertRaisesRegex(TraceReplayError, "trace exhausted"):
            model.download(250000)

    def test_loop_policy_can_finish_download_that_requires_wrapping(self):
        trace = self.load_trace(
            [
                {"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "1000"},
            ]
        )
        model = TraceDrivenNetworkModel(trace, end_policy=END_POLICY_LOOP, max_loops=1)

        result = model.download(250000)

        self.assertAlmostEqual(2.0, result.duration_s)
        self.assertAlmostEqual(2.0, result.end_time_s)
        self.assertAlmostEqual(1.0, result.trace_time_end_s)
        self.assertEqual(2, result.samples_touched)
        self.assertEqual(END_POLICY_LOOP, result.end_policy)

    def test_loop_policy_uses_wrapped_start_time(self):
        trace = self.load_trace(
            [
                {"timestamp_s": "0", "duration_s": "2", "throughput_kbps": "1000"},
            ]
        )
        model = TraceDrivenNetworkModel(trace, end_policy=END_POLICY_LOOP, max_loops=1)

        result = model.download(125000, start_time_s=2.5)

        self.assertAlmostEqual(2.5, result.start_time_s)
        self.assertAlmostEqual(3.5, result.end_time_s)
        self.assertAlmostEqual(0.5, result.trace_time_start_s)
        self.assertAlmostEqual(1.5, result.trace_time_end_s)

    def test_all_zero_throughput_raises(self):
        trace = self.load_trace(
            [
                {"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "0"},
                {"timestamp_s": "1", "duration_s": "1", "throughput_kbps": "0"},
            ]
        )
        model = TraceDrivenNetworkModel(trace, end_policy=END_POLICY_LOOP, max_loops=5)

        with self.assertRaisesRegex(TraceReplayError, "zero throughput"):
            model.download(1)

    def test_invalid_segment_size_bytes_is_rejected(self):
        model = TraceDrivenNetworkModel(self.constant_trace())

        for invalid in (0, -1, 1.5, True, "1"):
            with self.subTest(invalid=invalid):
                with self.assertRaisesRegex(TraceReplayError, "segment_size_bytes"):
                    model.download(invalid)

    def test_invalid_start_time_s_is_rejected(self):
        model = TraceDrivenNetworkModel(self.constant_trace())

        for invalid in (-1, float("inf"), float("nan"), True, "not-a-time"):
            with self.subTest(invalid=invalid):
                with self.assertRaisesRegex(TraceReplayError, "start_time_s"):
                    model.download(1, start_time_s=invalid)

    def test_measured_throughput_kbps_is_consistent_with_bytes_and_duration(self):
        model = TraceDrivenNetworkModel(self.constant_trace())

        result = model.download(125000)
        expected = (result.delivered_bytes * 8.0) / (result.duration_s * 1000.0)

        self.assertAlmostEqual(expected, result.measured_throughput_kbps)

    def test_fake_replay_adapter_advances_current_time_s(self):
        model = TraceDrivenNetworkModel(self.constant_trace())
        adapter = TraceDrivenFakeReplayAdapter(model)

        result = adapter.download_segment(125000)

        self.assertAlmostEqual(result.end_time_s, adapter.current_time_s)
        self.assertAlmostEqual(1.0, adapter.current_time_s)

    def test_fake_replay_adapter_reset_works(self):
        model = TraceDrivenNetworkModel(self.constant_trace())
        adapter = TraceDrivenFakeReplayAdapter(model, initial_time_s=2.0)
        adapter.download_segment(125000)

        adapter.reset()
        self.assertAlmostEqual(0.0, adapter.current_time_s)
        adapter.reset(current_time_s=4.0)
        self.assertAlmostEqual(4.0, adapter.current_time_s)

    def test_loading_synthetic_csv_then_using_network_model_works(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = os.path.join(temp_dir, "synthetic_trace.csv")
            with open(path, "w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=["timestamp_s", "duration_s", "throughput_kbps"])
                writer.writeheader()
                writer.writerow({"timestamp_s": "0", "duration_s": "10", "throughput_kbps": "1000"})

            trace = load_normalized_trace_csv(path)
            model = TraceDrivenNetworkModel(trace)
            result = model.download(125000)

        self.assertEqual("synthetic_trace", result.trace_id)
        self.assertAlmostEqual(1.0, result.duration_s)

    def test_tests_do_not_use_real_datasets_or_persistent_csv_fixtures(self):
        forbidden_roots = [
            os.path.normcase(
                os.path.join(
                    "C:\\",
                    "Users",
                    "danie",
                    "Documents",
                    "TFG",
                    "_datasets",
                    "phase3_traces_replay",
                )
            )
        ]
        for forbidden in forbidden_roots:
            self.assertNotIn(forbidden, os.path.normcase(__file__))

        tests_dir = os.path.dirname(__file__)
        csv_files = []
        for root, _dirs, files in os.walk(tests_dir):
            for filename in files:
                if filename.endswith(".csv"):
                    csv_files.append(os.path.join(root, filename))
        self.assertEqual([], csv_files)

    def test_invalid_end_policy_and_max_loops_are_rejected(self):
        trace = self.constant_trace()

        with self.assertRaisesRegex(TraceReplayError, "end_policy"):
            TraceDrivenNetworkModel(trace, end_policy="unknown")
        for invalid in (-1, 1.5, True):
            with self.subTest(invalid=invalid):
                with self.assertRaisesRegex(TraceReplayError, "max_loops"):
                    TraceDrivenNetworkModel(trace, end_policy=END_POLICY_LOOP, max_loops=invalid)

    def test_invalid_loaded_trace_is_rejected(self):
        trace = load_normalized_trace_rows(
            [{"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "-1"}],
            strict=False,
        )

        with self.assertRaisesRegex(TraceReplayError, "loaded trace must be valid"):
            TraceDrivenNetworkModel(trace)

    def constant_trace(self):
        return self.load_trace(
            [
                {"timestamp_s": "0", "duration_s": "10", "throughput_kbps": "1000"},
            ]
        )

    def load_trace(self, rows):
        return load_normalized_trace_rows(rows, trace_id="synthetic-trace", source="synthetic-memory")


if __name__ == "__main__":
    unittest.main()

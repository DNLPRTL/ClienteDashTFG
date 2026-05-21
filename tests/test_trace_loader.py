from __future__ import annotations

import csv
import os
import tempfile
import unittest

from core.trace_replay.loader import (
    LoadedTrace,
    TraceLoadError,
    TraceSample,
    load_normalized_trace_csv,
    load_normalized_trace_rows,
)
from core.trace_replay.schema import TRACE_SCHEMA_VERSION


class TraceLoaderTest(unittest.TestCase):
    def write_trace(self, directory, name="trace.csv", rows=None, fieldnames=None):
        if rows is None:
            rows = []
        if fieldnames is None:
            fieldnames = ["timestamp_s", "duration_s", "throughput_kbps"]
        path = os.path.join(directory, name)
        with open(path, "w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
        return path

    def valid_rows(self):
        return [
            {"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "1000"},
            {"timestamp_s": "1", "duration_s": "1", "throughput_kbps": "2000"},
            {"timestamp_s": "2", "duration_s": "1", "throughput_kbps": "0"},
        ]

    def test_loads_valid_in_memory_rows_into_loaded_trace(self):
        trace = load_normalized_trace_rows(self.valid_rows(), trace_id="memory-trace", source="synthetic-memory")

        self.assertIsInstance(trace, LoadedTrace)
        self.assertEqual("memory-trace", trace.trace_id)
        self.assertEqual("synthetic-memory", trace.source)
        self.assertEqual(TRACE_SCHEMA_VERSION, trace.schema_version)
        self.assertEqual(3, len(trace.samples))
        self.assertIsInstance(trace.samples[0], TraceSample)

    def test_loads_valid_csv_into_loaded_trace(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_trace(temp_dir, rows=self.valid_rows())
            trace = load_normalized_trace_csv(path)

        self.assertTrue(trace.validation.is_valid)
        self.assertEqual(3, trace.sample_count)
        self.assertEqual(1000.0, trace.samples[0].throughput_kbps)

    def test_derives_trace_id_from_csv_stem_when_trace_id_is_none(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_trace(temp_dir, name="derived_trace.csv", rows=self.valid_rows())
            trace = load_normalized_trace_csv(path)

        self.assertEqual("derived_trace", trace.trace_id)

    def test_preserves_explicit_trace_id_and_source(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_trace(temp_dir, rows=self.valid_rows())
            trace = load_normalized_trace_csv(path, trace_id="explicit-id", source="explicit-source")

        self.assertEqual("explicit-id", trace.trace_id)
        self.assertEqual("explicit-source", trace.source)

    def test_preserves_optional_columns_in_metadata(self):
        rows = [
            {
                "timestamp_s": "0",
                "duration_s": "1",
                "throughput_kbps": "1000",
                "network_type": "synthetic",
                "mobility_label": "stationary",
            }
        ]
        trace = load_normalized_trace_rows(rows)

        self.assertEqual(
            {"network_type": "synthetic", "mobility_label": "stationary"},
            trace.samples[0].metadata,
        )

    def test_preserves_unknown_extra_columns_in_metadata(self):
        rows = [
            {
                "timestamp_s": "0",
                "duration_s": "1",
                "throughput_kbps": "1000",
                "unknown_extra": "kept",
            }
        ]
        trace = load_normalized_trace_rows(rows)

        self.assertEqual({"unknown_extra": "kept"}, trace.samples[0].metadata)

    def test_row_order_is_preserved(self):
        trace = load_normalized_trace_rows(self.valid_rows())

        self.assertEqual([0.0, 1.0, 2.0], [sample.timestamp_s for sample in trace.samples])
        self.assertEqual([1000.0, 2000.0, 0.0], [sample.throughput_kbps for sample in trace.samples])

    def test_loaded_trace_stats_match_validation_result(self):
        trace = load_normalized_trace_rows(self.valid_rows())

        self.assertEqual(trace.validation.sample_count, trace.sample_count)
        self.assertEqual(trace.validation.duration_s, trace.duration_s)
        self.assertEqual(trace.validation.min_throughput_kbps, trace.min_throughput_kbps)
        self.assertEqual(trace.validation.mean_throughput_kbps, trace.mean_throughput_kbps)
        self.assertEqual(trace.validation.max_throughput_kbps, trace.max_throughput_kbps)
        self.assertEqual(trace.validation.nominal_granularity_s, trace.nominal_granularity_s)
        self.assertEqual(trace.validation.has_zero_throughput, trace.has_zero_throughput)

    def test_iter_samples_returns_samples_in_order(self):
        trace = load_normalized_trace_rows(self.valid_rows())

        self.assertEqual(tuple(trace.samples), tuple(trace.iter_samples()))

    def test_strict_true_raises_trace_load_error_for_invalid_trace(self):
        rows = [{"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "-1"}]

        with self.assertRaisesRegex(TraceLoadError, "invalid normalized trace"):
            load_normalized_trace_rows(rows, strict=True)

    def test_strict_false_returns_loaded_trace_with_invalid_validation_when_structurally_loadable(self):
        rows = [{"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "-1"}]

        trace = load_normalized_trace_rows(rows, strict=False)

        self.assertFalse(trace.validation.is_valid)
        self.assertEqual(-1.0, trace.samples[0].throughput_kbps)

    def test_missing_required_columns_raise_even_with_strict_false(self):
        rows = [{"timestamp_s": "0", "throughput_kbps": "1000"}]

        with self.assertRaisesRegex(TraceLoadError, "missing required columns: duration_s"):
            load_normalized_trace_rows(rows, strict=False)

    def test_missing_file_raises_trace_load_error(self):
        with self.assertRaisesRegex(TraceLoadError, "normalized trace CSV not found"):
            load_normalized_trace_csv(os.path.join("missing", "trace.csv"))

    def test_no_real_dataset_paths_are_used(self):
        raw_dataset_root = os.path.normcase(
            os.path.join(
                "C:\\",
                "Users",
                "danie",
                "Documents",
                "TFG",
                "_datasets",
                "phase3_traces_replay",
                "_raw_candidates",
            )
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_trace(temp_dir, rows=self.valid_rows())
            self.assertNotIn(raw_dataset_root, os.path.normcase(path))
            trace = load_normalized_trace_csv(path)

        self.assertTrue(trace.validation.is_valid)

    def test_no_csv_fixtures_are_stored_in_tests_directory(self):
        tests_dir = os.path.dirname(__file__)
        csv_files = []
        for root, _dirs, files in os.walk(tests_dir):
            for filename in files:
                if filename.endswith(".csv"):
                    csv_files.append(os.path.join(root, filename))

        self.assertEqual([], csv_files)


if __name__ == "__main__":
    unittest.main()


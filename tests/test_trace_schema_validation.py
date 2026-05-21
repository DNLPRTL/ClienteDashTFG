from __future__ import annotations

import csv
import os
import tempfile
import unittest

from core.trace_replay.schema import REQUIRED_TRACE_COLUMNS, TRACE_SCHEMA_VERSION
from core.trace_replay.validation import (
    validate_normalized_trace_csv,
    validate_normalized_trace_rows,
)


class TraceSchemaValidationTest(unittest.TestCase):
    def write_trace(self, directory, rows, fieldnames=None):
        path = os.path.join(directory, "trace.csv")
        if fieldnames is None:
            fieldnames = list(REQUIRED_TRACE_COLUMNS)
        with open(path, "w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
        return path

    def validate_rows_via_temp_csv(self, rows, fieldnames=None):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_trace(temp_dir, rows, fieldnames=fieldnames)
            return validate_normalized_trace_csv(path)

    def test_schema_version_is_normalized_trace_v1(self):
        self.assertEqual("normalized_trace_schema_v1", TRACE_SCHEMA_VERSION)

    def test_valid_constant_throughput_trace(self):
        result = self.validate_rows_via_temp_csv(
            [
                {"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "1200"},
                {"timestamp_s": "1", "duration_s": "1", "throughput_kbps": "1200"},
                {"timestamp_s": "2", "duration_s": "1", "throughput_kbps": "1200"},
            ]
        )

        self.assertTrue(result.is_valid)
        self.assertEqual(3, result.sample_count)
        self.assertEqual((), result.errors)

    def test_valid_variable_throughput_trace_with_zero_outage_sample(self):
        result = self.validate_rows_via_temp_csv(
            [
                {"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "1800"},
                {"timestamp_s": "1", "duration_s": "1", "throughput_kbps": "0"},
                {"timestamp_s": "2", "duration_s": "1", "throughput_kbps": "900"},
            ]
        )

        self.assertTrue(result.is_valid)
        self.assertTrue(result.has_zero_throughput)
        self.assertEqual(0.0, result.min_throughput_kbps)

    def test_missing_required_column_is_invalid(self):
        result = self.validate_rows_via_temp_csv(
            [{"timestamp_s": "0", "throughput_kbps": "1000"}],
            fieldnames=["timestamp_s", "throughput_kbps"],
        )

        self.assertFalse(result.is_valid)
        self.assertIn("missing required columns: duration_s", "\n".join(result.errors))

    def test_non_numeric_value_is_invalid(self):
        result = self.validate_rows_via_temp_csv(
            [{"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "fast"}]
        )

        self.assertFalse(result.is_valid)
        self.assertIn("throughput_kbps must be numeric and finite", "\n".join(result.errors))

    def test_negative_throughput_is_invalid(self):
        result = self.validate_rows_via_temp_csv(
            [{"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "-1"}]
        )

        self.assertFalse(result.is_valid)
        self.assertIn("throughput_kbps must be greater than or equal to 0", "\n".join(result.errors))

    def test_zero_duration_is_invalid(self):
        result = self.validate_rows_via_temp_csv(
            [{"timestamp_s": "0", "duration_s": "0", "throughput_kbps": "1000"}]
        )

        self.assertFalse(result.is_valid)
        self.assertIn("duration_s must be strictly greater than 0", "\n".join(result.errors))

    def test_negative_duration_is_invalid(self):
        result = self.validate_rows_via_temp_csv(
            [{"timestamp_s": "0", "duration_s": "-1", "throughput_kbps": "1000"}]
        )

        self.assertFalse(result.is_valid)
        self.assertIn("duration_s must be strictly greater than 0", "\n".join(result.errors))

    def test_decreasing_timestamp_is_invalid(self):
        result = self.validate_rows_via_temp_csv(
            [
                {"timestamp_s": "2", "duration_s": "1", "throughput_kbps": "1000"},
                {"timestamp_s": "1", "duration_s": "1", "throughput_kbps": "1000"},
            ]
        )

        self.assertFalse(result.is_valid)
        self.assertIn("timestamp_s must be monotonically non-decreasing", "\n".join(result.errors))

    def test_negative_timestamp_is_invalid(self):
        result = self.validate_rows_via_temp_csv(
            [{"timestamp_s": "-0.1", "duration_s": "1", "throughput_kbps": "1000"}]
        )

        self.assertFalse(result.is_valid)
        self.assertIn("timestamp_s must be greater than or equal to 0", "\n".join(result.errors))

    def test_nan_is_invalid(self):
        result = self.validate_rows_via_temp_csv(
            [{"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "NaN"}]
        )

        self.assertFalse(result.is_valid)
        self.assertIn("throughput_kbps must be numeric and finite", "\n".join(result.errors))

    def test_infinity_is_invalid(self):
        result = self.validate_rows_via_temp_csv(
            [{"timestamp_s": "0", "duration_s": "inf", "throughput_kbps": "1000"}]
        )

        self.assertFalse(result.is_valid)
        self.assertIn("duration_s must be numeric and finite", "\n".join(result.errors))

    def test_empty_csv_no_rows_is_invalid(self):
        result = self.validate_rows_via_temp_csv([])

        self.assertFalse(result.is_valid)
        self.assertEqual(0, result.sample_count)
        self.assertIn("trace has no samples", "\n".join(result.errors))

    def test_extra_optional_columns_are_accepted(self):
        rows = [
            {
                "timestamp_s": "0",
                "duration_s": "1",
                "throughput_kbps": "1000",
                "network_type": "synthetic",
                "notes": "extra columns are ignored",
            }
        ]
        result = self.validate_rows_via_temp_csv(
            rows,
            fieldnames=["timestamp_s", "duration_s", "throughput_kbps", "network_type", "notes"],
        )

        self.assertTrue(result.is_valid)
        self.assertEqual(1, result.sample_count)

    def test_summary_statistics_are_correct_for_valid_trace(self):
        result = self.validate_rows_via_temp_csv(
            [
                {"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "1000"},
                {"timestamp_s": "1", "duration_s": "1", "throughput_kbps": "2000"},
                {"timestamp_s": "2", "duration_s": "1", "throughput_kbps": "3000"},
            ]
        )

        self.assertTrue(result.is_valid)
        self.assertEqual(3.0, result.duration_s)
        self.assertEqual(1000.0, result.min_throughput_kbps)
        self.assertEqual(2000.0, result.mean_throughput_kbps)
        self.assertEqual(3000.0, result.max_throughput_kbps)
        self.assertEqual(1.0, result.nominal_granularity_s)
        self.assertFalse(result.has_zero_throughput)

    def test_repeated_validation_is_deterministic(self):
        rows = [
            {"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "1000"},
            {"timestamp_s": "1", "duration_s": "1", "throughput_kbps": "500"},
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_trace(temp_dir, rows)
            first = validate_normalized_trace_csv(path)
            second = validate_normalized_trace_csv(path)

        self.assertEqual(first, second)

    def test_validate_rows_uses_memory_source_label(self):
        result = validate_normalized_trace_rows(
            [{"timestamp_s": "0", "duration_s": "1", "throughput_kbps": "-1"}],
            source="synthetic-memory",
        )

        self.assertFalse(result.is_valid)
        self.assertIn("synthetic-memory", result.errors[0])

    def test_missing_file_raises_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            validate_normalized_trace_csv(os.path.join("missing", "trace.csv"))


if __name__ == "__main__":
    unittest.main()

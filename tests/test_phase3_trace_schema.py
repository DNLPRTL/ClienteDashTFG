from __future__ import annotations

import math
import tempfile
import unittest
from pathlib import Path

from core.trace_replay.loader import load_normalized_trace_csv, load_normalized_trace_rows
from core.trace_replay.validation import TraceValidationError, validate_normalized_trace_rows


class Phase3TraceSchemaTest(unittest.TestCase):
    def test_valid_rows_compute_stats_and_fingerprint(self):
        stats = validate_normalized_trace_rows(
            [
                {"timestamp_s": 0.0, "duration_s": 1.0, "throughput_kbps": 1000.0},
                {"timestamp_s": 1.0, "duration_s": 2.0, "throughput_kbps": 2000.0, "extra": "allowed"},
            ],
            source="synthetic",
        )

        self.assertEqual(2, stats.row_count)
        self.assertEqual(3.0, stats.duration_s)
        self.assertEqual(1000.0, stats.throughput_min_kbps)
        self.assertEqual(1500.0, stats.throughput_mean_kbps)
        self.assertEqual(2000.0, stats.throughput_max_kbps)
        self.assertEqual(64, len(stats.content_fingerprint_sha256))

    def test_invalid_rows_are_rejected(self):
        invalid_cases = [
            [{"timestamp_s": -1.0, "duration_s": 1.0, "throughput_kbps": 1000.0}],
            [{"timestamp_s": 0.0, "duration_s": 0.0, "throughput_kbps": 1000.0}],
            [{"timestamp_s": 0.0, "duration_s": 1.0, "throughput_kbps": -1.0}],
            [
                {"timestamp_s": 1.0, "duration_s": 1.0, "throughput_kbps": 1000.0},
                {"timestamp_s": 0.5, "duration_s": 1.0, "throughput_kbps": 1000.0},
            ],
            [{"timestamp_s": 0.0, "duration_s": 1.0, "throughput_kbps": math.inf}],
            [{"timestamp_s": 0.0, "duration_s": 1.0}],
            [],
        ]

        for rows in invalid_cases:
            with self.subTest(rows=rows):
                with self.assertRaises(TraceValidationError):
                    validate_normalized_trace_rows(rows, source="invalid")

    def test_loader_materializes_samples_without_metadata_leakage(self):
        loaded = load_normalized_trace_rows(
            [
                {"timestamp_s": 0, "duration_s": 1, "throughput_kbps": 1000, "dataset_id": "hidden"},
                {"timestamp_s": 1, "duration_s": 1, "throughput_kbps": 2000, "trace_id": "hidden"},
            ],
            trace_id="trace_synthetic",
        )

        self.assertEqual("trace_synthetic", loaded.trace_id)
        self.assertEqual(2, len(loaded.samples))
        self.assertEqual(1000.0, loaded.samples[0].throughput_kbps)
        self.assertFalse(hasattr(loaded.samples[0], "dataset_id"))
        self.assertFalse(hasattr(loaded.samples[0], "trace_id"))

    def test_loader_reads_csv(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "trace.csv"
            path.write_text(
                "timestamp_s,duration_s,throughput_kbps\n"
                "0,1,1000\n"
                "1,1,2000\n",
                encoding="utf-8",
            )

            loaded = load_normalized_trace_csv(path)

        self.assertEqual("trace", loaded.trace_id)
        self.assertEqual(2, len(loaded.samples))


if __name__ == "__main__":
    unittest.main()

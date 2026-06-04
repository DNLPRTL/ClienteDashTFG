from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from scripts.normalize_phase6_trace_sources import (
    canonical_content_fingerprint,
    normalize_phase6_sources,
    parse_six_column_log,
)
from scripts.phase6c_source_registry import create_external_layout


class Phase6CNormalizationTest(unittest.TestCase):
    def test_normalizes_synthetic_hsdpa_six_column_log(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "external"
            paths = create_external_layout(root)
            trace = paths["extracted"] / "hsdpa_norway" / "route" / "report.1"
            trace.parent.mkdir(parents=True)
            trace.write_text("0 0 1.0 2.0 1000 1000\n1000 0 1.0 2.0 2000 1000\n", encoding="utf-8")

            report = normalize_phase6_sources(external_root=root, strict=True)

            self.assertTrue(report["valid"])
            self.assertEqual(1, len(report["records"]))
            csv_path = Path(report["records"][0]["trace_csv"])
            with csv_path.open(encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual("8", rows[0]["throughput_kbps"])
            self.assertEqual("16", rows[1]["throughput_kbps"])

    def test_normalizes_synthetic_raca_csv_with_mbps(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "external"
            paths = create_external_layout(root)
            trace = paths["extracted"] / "raca_4g_lte" / "trace.csv"
            trace.parent.mkdir(parents=True)
            trace.write_text("timestamp_s,throughput_mbps\n0,1.5\n1,2.0\n", encoding="utf-8")

            report = normalize_phase6_sources(external_root=root, strict=True)

            self.assertTrue(report["valid"])
            with Path(report["records"][0]["trace_csv"]).open(encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual("1500", rows[0]["throughput_kbps"])
            self.assertEqual("2000", rows[1]["throughput_kbps"])

    def test_rejects_file_with_no_throughput_column(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "external"
            paths = create_external_layout(root)
            trace = paths["extracted"] / "raca_4g_lte" / "bad.csv"
            trace.parent.mkdir(parents=True)
            trace.write_text("timestamp_s,signal\n0,10\n", encoding="utf-8")

            report = normalize_phase6_sources(external_root=root, strict=True)

            self.assertFalse(report["valid"])
            self.assertEqual("unable_to_detect_throughput_column", report["excluded"][0]["exclusion_reason"])

    def test_checksum_and_fingerprint_are_deterministic(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "report.1"
            path.write_text("0 0 1.0 2.0 1000 1000\n1000 0 1.0 2.0 2000 1000\n", encoding="utf-8")

            rows_a = parse_six_column_log(path)
            rows_b = parse_six_column_log(path)

            self.assertEqual(canonical_content_fingerprint(rows_a), canonical_content_fingerprint(rows_b))


if __name__ == "__main__":
    unittest.main()

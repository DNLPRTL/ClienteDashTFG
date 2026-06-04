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

            report = normalize_phase6_sources(external_root=root, sources="hsdpa_norway", strict=True)

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

    def test_skips_binary_large_and_unsupported_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "external"
            paths = create_external_layout(root)
            source = paths["extracted"] / "raca_4g_lte"
            source.mkdir(parents=True)
            (source / "binary.log").write_bytes(b"\x00\x01not text")
            (source / "too_large.csv").write_text(
                "timestamp_s,throughput_mbps\n" + "\n".join("0,1" for _ in range(100)),
                encoding="utf-8",
            )
            (source / "archive.zip").write_bytes(b"fake zip")

            report = normalize_phase6_sources(
                external_root=root,
                sources="raca_4g_lte",
                max_file_size_mb=0.00005,
                strict=False,
            )

            reasons = {record["exclusion_reason"] for record in report["excluded"]}
            self.assertIn("binary_or_non_text_file", reasons)
            self.assertIn("file_too_large", reasons)
            self.assertIn("unsupported_file_type", reasons)

    def test_does_not_scan_external_output_directories(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "external"
            paths = create_external_layout(root)
            trace = paths["extracted"] / "raca_4g_lte" / "trace.csv"
            trace.parent.mkdir(parents=True)
            trace.write_text("timestamp_s,throughput_mbps\n0,1.0\n", encoding="utf-8")
            for dirname in ("archives", "normalized", "manifests", "reports", "receipts", "logs"):
                noisy = paths[dirname] / "raca_4g_lte" / "bad.csv"
                noisy.parent.mkdir(parents=True, exist_ok=True)
                noisy.write_text("timestamp_s,signal\n0,10\n", encoding="utf-8")

            report = normalize_phase6_sources(external_root=root, sources="raca_4g_lte", strict=True)

            self.assertTrue(report["valid"])
            self.assertEqual(1, len(report["records"]))
            self.assertEqual([], report["excluded"])

    def test_writes_progress_for_synthetic_source(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "external"
            paths = create_external_layout(root)
            for index in range(3):
                trace = paths["extracted"] / "raca_4g_lte" / ("trace{0}.csv".format(index))
                trace.parent.mkdir(parents=True, exist_ok=True)
                trace.write_text("timestamp_s,throughput_mbps\n0,{0}\n".format(index + 1), encoding="utf-8")

            report = normalize_phase6_sources(external_root=root, sources="raca_4g_lte", progress_every=1, strict=True)

            self.assertTrue(report["valid"])
            progress_path = Path(report["progress_path"])
            self.assertTrue(progress_path.is_file())
            self.assertIn("raca_4g_lte", progress_path.read_text(encoding="utf-8"))

    def test_bounded_sniffing_detects_raca_like_csv(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "external"
            paths = create_external_layout(root)
            trace = paths["extracted"] / "raca_4g_lte" / "trace.csv"
            trace.parent.mkdir(parents=True)
            trace.write_text("timestamp_s,throughput_mbps\n0,3.5\n1,4.5\n", encoding="utf-8")

            report = normalize_phase6_sources(
                external_root=root,
                sources="raca_4g_lte",
                max_sniff_bytes=64,
                strict=True,
            )

            self.assertTrue(report["valid"])
            with Path(report["records"][0]["trace_csv"]).open(encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual("3500", rows[0]["throughput_kbps"])


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.extract_phase6_trace_archives import extract_phase6_archives
from scripts.phase6c_source_registry import create_external_layout


class Phase6CExtractTest(unittest.TestCase):
    def test_extracts_zip_safely(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "external"
            paths = create_external_layout(root)
            archive_dir = paths["archives"] / "raca_4g_lte"
            archive_dir.mkdir(parents=True)
            with zipfile.ZipFile(archive_dir / "source.zip", "w") as archive:
                archive.writestr("nested/trace.csv", "time,throughput_mbps\n0,1\n")

            report = extract_phase6_archives(external_root=root, strict=True)

            self.assertTrue(report["valid"])
            self.assertTrue((paths["extracted"] / "raca_4g_lte" / "nested" / "trace.csv").is_file())

            second = extract_phase6_archives(external_root=root, strict=True)
            self.assertEqual("skipped_existing_extraction", second["receipts"][0]["status"])

    def test_rejects_path_traversal_zip(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "external"
            paths = create_external_layout(root)
            archive_dir = paths["archives"] / "raca_4g_lte"
            archive_dir.mkdir(parents=True)
            with zipfile.ZipFile(archive_dir / "bad.zip", "w") as archive:
                archive.writestr("../evil.txt", "nope")

            report = extract_phase6_archives(external_root=root, strict=True)

            self.assertFalse(report["valid"])
            self.assertIn("path_traversal_blocked", "\n".join(report["errors"]))
            self.assertFalse((paths["extracted"] / "evil.txt").exists())

    def test_copies_plain_hsdpa_report_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "external"
            paths = create_external_layout(root)
            report_path = paths["archives"] / "hsdpa_norway" / "route_a" / "report.1"
            report_path.parent.mkdir(parents=True)
            report_path.write_text("0 0 1 2 1000 1000\n", encoding="utf-8")

            report = extract_phase6_archives(external_root=root, sources="hsdpa_norway", strict=True)

            self.assertTrue(report["valid"])
            self.assertTrue((paths["extracted"] / "hsdpa_norway" / "route_a" / "report.1").is_file())


if __name__ == "__main__":
    unittest.main()

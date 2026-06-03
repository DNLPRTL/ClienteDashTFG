from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit_phase6_trace_eligibility.py"


class Phase6TraceEligibilityAuditTest(unittest.TestCase):
    def test_blocks_checksum_seen_in_phase4_even_with_distinct_ids_and_leakage_groups(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            phase4 = root / "phase4_manifest.json"
            phase6 = root / "phase6_manifest.json"
            output = root / "audit.json"
            _write_manifest(
                phase4,
                [
                    {
                        "split": "train",
                        "checksum_sha256": "abc123",
                        "trace_id": "phase4_train_trace",
                        "leakage_group": "phase4_group",
                        "split_key": "ghent_4g_lte_bandwidth_logs/logs_all/report_bus_0001.log",
                    }
                ],
            )
            _write_manifest(
                phase6,
                [
                    {
                        "split": "test",
                        "checksum_sha256": "abc123",
                        "trace_id": "phase6_test_trace",
                        "leakage_group": "phase6_group",
                        "split_key": "ghent_4g_lte_bandwidth_logs/logs_bus/report_bus_0001.log",
                    }
                ],
            )

            result = _run_audit(phase4, phase6, output)

            self.assertEqual(0, result.returncode, result.stderr)
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertFalse(report["use_for_phase6_eval"])
            self.assertIn("Phase 6 evaluation split overlaps Phase 4 by checksum_sha256.", report["reasons"])
            self.assertEqual(1, len(report["overlaps"]["checksum_sha256"]))
            self.assertEqual([], report["overlaps"]["trace_id"])
            self.assertEqual([], report["overlaps"]["leakage_group"])
            self.assertEqual(1, len(report["logs_all_specific_duplicates"]["combined"]))

    def test_allows_candidate_without_phase4_overlap_or_internal_cross_split_duplicates(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            phase4 = root / "phase4_manifest.json"
            phase6 = root / "phase6_manifest.json"
            output = root / "audit.json"
            _write_manifest(
                phase4,
                [
                    {
                        "split": "train",
                        "checksum_sha256": "phase4-only",
                        "trace_id": "phase4_trace",
                        "leakage_group": "phase4_group",
                        "split_key": "dataset/logs_all/report_0001.log",
                    }
                ],
            )
            _write_manifest(
                phase6,
                [
                    {
                        "split": "test",
                        "checksum_sha256": "phase6-only",
                        "trace_id": "phase6_trace",
                        "leakage_group": "phase6_group",
                        "split_key": "dataset/logs_bus/report_0002.log",
                    }
                ],
            )

            result = _run_audit(phase4, phase6, output)

            self.assertEqual(0, result.returncode, result.stderr)
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertTrue(report["use_for_phase6_eval"])
            self.assertEqual([], report["reasons"])
            self.assertEqual([], report["overlaps"]["checksum_sha256"])


def _write_manifest(path: Path, records):
    path.write_text(json.dumps({"trace_records": records}), encoding="utf-8")


def _run_audit(phase4: Path, phase6: Path, output: Path):
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--phase4-dataset-manifest",
            str(phase4),
            "--phase6-candidate-manifest",
            str(phase6),
            "--output",
            str(output),
        ],
        check=False,
        capture_output=True,
        text=True,
    )


if __name__ == "__main__":
    unittest.main()

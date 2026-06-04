from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_phase6_evaluation_readiness.py"


class Phase6EvaluationReadinessTest(unittest.TestCase):
    def test_structural_preflight_passes_without_manifests_and_warns(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "readiness.json"

            result = _run_readiness(output)

            self.assertEqual(0, result.returncode, result.stderr)
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertTrue(report["ready_for_phase6c"])
            self.assertFalse(report["ready_for_benchmark"])
            self.assertFalse(report["benchmark_authorized"])
            self.assertIn("manifest_audit_not_run", report["warnings"])

    def test_require_manifests_fails_without_manifests(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "readiness.json"

            result = _run_readiness(output, "--require-manifests")

            self.assertEqual(2, result.returncode, result.stderr)
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertFalse(report["ready_for_phase6c"])
            self.assertIn("manifest_audit_not_run", "\n".join(report["errors"]))
            self.assertFalse(report["benchmark_authorized"])

    def test_synthetic_clean_manifests_are_ready_for_phase6c(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            phase4 = root / "phase4.json"
            phase6 = root / "phase6.json"
            output = root / "readiness.json"
            _write_phase4_manifest(phase4, "phase4-fingerprint")
            _write_phase6_manifest(phase6, "phase6-fingerprint")

            result = _run_readiness(
                output,
                "--phase4-dataset-manifest",
                str(phase4),
                "--phase6-candidate-manifest",
                str(phase6),
            )

            self.assertEqual(0, result.returncode, result.stderr)
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertTrue(report["ready_for_phase6c"])
            self.assertTrue(report["manifest_audit"]["ran"])
            self.assertTrue(report["manifest_audit"]["audit_use_for_phase6_eval"])
            self.assertFalse(report["ready_for_benchmark"])

    def test_synthetic_overlapping_fingerprint_blocks_phase6c(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            phase4 = root / "phase4.json"
            phase6 = root / "phase6.json"
            output = root / "readiness.json"
            _write_phase4_manifest(phase4, "shared-fingerprint")
            _write_phase6_manifest(phase6, "shared-fingerprint")

            result = _run_readiness(
                output,
                "--phase4-dataset-manifest",
                str(phase4),
                "--phase6-candidate-manifest",
                str(phase6),
            )

            self.assertEqual(2, result.returncode, result.stderr)
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertFalse(report["ready_for_phase6c"])
            self.assertFalse(report["manifest_audit"]["audit_use_for_phase6_eval"])
            self.assertIn(
                "Phase 6 evaluation split overlaps Phase 4 by canonical_content_fingerprint.",
                report["manifest_audit"]["audit_reasons"],
            )
            self.assertFalse(report["benchmark_authorized"])

    def test_report_always_has_benchmark_authorized_false(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "readiness.json"

            result = _run_readiness(output, "--strict")

            self.assertEqual(0, result.returncode, result.stderr)
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertFalse(report["benchmark_authorized"])
            self.assertFalse(report["ready_for_benchmark"])


def _write_phase4_manifest(path: Path, fingerprint: str):
    path.write_text(
        json.dumps(
            {
                "trace_records": [
                    {
                        "split": "train",
                        "checksum_sha256": "phase4-checksum",
                        "canonical_content_fingerprint": fingerprint,
                        "trace_id": "phase4_trace",
                        "leakage_group": "phase4_group",
                        "source_path": "synthetic/phase4.csv",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )


def _write_phase6_manifest(path: Path, fingerprint: str):
    path.write_text(
        json.dumps(
            {
                "schema_version": "phase6_trace_manifest_v1",
                "trace_records": [
                    {
                        "trace_id": "phase6_trace",
                        "dataset_family": "synthetic",
                        "split": "phase6_eval",
                        "eval_gate": "use_for_eval",
                        "source_path": "synthetic/phase6.csv",
                        "schema_version": "normalized_trace_schema_v1",
                        "checksum_sha256": "phase6-checksum",
                        "canonical_content_fingerprint": fingerprint,
                        "leakage_group": "phase6_group",
                        "duration_s": 10,
                        "sample_count": 5,
                        "license_status": "synthetic_fixture",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )


def _run_readiness(output: Path, *extra_args):
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--output",
            str(output),
            *extra_args,
        ],
        check=False,
        capture_output=True,
        text=True,
    )


if __name__ == "__main__":
    unittest.main()

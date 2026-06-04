from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_phase6_trace_manifest.py"


class Phase6TraceManifestValidationTest(unittest.TestCase):
    def test_strict_final_accepts_clean_use_for_eval_record(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = root / "manifest.json"
            output = root / "validation.json"
            _write_manifest(manifest, [_clean_eval_record()])

            result = _run_validation(manifest, output)

            self.assertEqual(0, result.returncode, result.stderr)
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertTrue(report["valid"])
            self.assertEqual([], report["errors"])
            self.assertEqual(1, report["counts"]["eval_records"])

    def test_strict_final_rejects_missing_canonical_content_fingerprint(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = root / "manifest.json"
            output = root / "validation.json"
            record = _clean_eval_record()
            del record["canonical_content_fingerprint"]
            _write_manifest(manifest, [record])

            result = _run_validation(manifest, output)

            self.assertEqual(2, result.returncode, result.stderr)
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertFalse(report["valid"])
            self.assertIn(
                {"record_index": 0, "field": "canonical_content_fingerprint"},
                report["missing_required_fields"],
            )

    def test_strict_final_rejects_duplicate_fingerprints_among_eval_records(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = root / "manifest.json"
            output = root / "validation.json"
            first = _clean_eval_record()
            second = _clean_eval_record()
            second["trace_id"] = "trace_b"
            second["checksum_sha256"] = "checksum-b"
            second["leakage_group"] = "group-b"
            _write_manifest(manifest, [first, second])

            result = _run_validation(manifest, output)

            self.assertEqual(2, result.returncode, result.stderr)
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertFalse(report["valid"])
            self.assertEqual(1, len(report["duplicate_fingerprints"]))
            self.assertIn("duplicate canonical_content_fingerprint", "\n".join(report["errors"]))

    def test_do_not_use_for_eval_warns_about_missing_exclusion_reason(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = root / "manifest.json"
            output = root / "validation.json"
            _write_manifest(
                manifest,
                [
                    {
                        "trace_id": "excluded_trace",
                        "dataset_family": "synthetic",
                        "split": "do_not_use_for_eval",
                        "eval_gate": "do_not_use_for_eval",
                        "source_path": "synthetic/excluded.csv",
                    }
                ],
            )

            result = _run_validation(manifest, output)

            self.assertEqual(0, result.returncode, result.stderr)
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertTrue(report["valid"])
            self.assertIn("do_not_use_for_eval should include exclusion_reason", "\n".join(report["warnings"]))

    def test_split_container_format_is_accepted(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = root / "manifest.json"
            output = root / "validation.json"
            record = _clean_eval_record()
            del record["split"]
            manifest.write_text(
                json.dumps(
                    {
                        "schema_version": "phase6_trace_manifest_v1",
                        "splits": {"phase6_eval": [record]},
                    }
                ),
                encoding="utf-8",
            )

            result = _run_validation(manifest, output)

            self.assertEqual(0, result.returncode, result.stderr)
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertTrue(report["valid"])
            self.assertEqual({"phase6_eval": 1}, report["split_counts"])


def _clean_eval_record():
    return {
        "trace_id": "trace_a",
        "dataset_family": "synthetic",
        "split": "phase6_eval",
        "eval_gate": "use_for_eval",
        "source_path": "synthetic/trace_a.csv",
        "schema_version": "normalized_trace_schema_v1",
        "checksum_sha256": "checksum-a",
        "canonical_content_fingerprint": "fingerprint-a",
        "leakage_group": "group-a",
        "duration_s": 10,
        "sample_count": 5,
        "license_status": "synthetic_fixture",
    }


def _write_manifest(path: Path, records):
    path.write_text(
        json.dumps(
            {
                "schema_version": "phase6_trace_manifest_v1",
                "trace_records": records,
            }
        ),
        encoding="utf-8",
    )


def _run_validation(manifest: Path, output: Path):
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--manifest",
            str(manifest),
            "--output",
            str(output),
            "--strict-final",
            "--fail-on-error",
        ],
        check=False,
        capture_output=True,
        text=True,
    )


if __name__ == "__main__":
    unittest.main()

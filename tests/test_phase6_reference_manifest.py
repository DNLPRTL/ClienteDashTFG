from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.build_phase6_reference_manifest import build_reference_manifest
from scripts.phase6c_source_registry import Phase6CError


class Phase6ReferenceManifestTest(unittest.TestCase):
    def test_accepts_synthetic_phase4_dataset_manifest(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            phase4 = root / "phase4.json"
            output = root / "reference.json"
            _write_phase4(phase4, [{"trace_id": "t1", "checksum_sha256": "abc", "leakage_group": "g1"}])

            report = build_reference_manifest(
                phase4_dataset_manifest=phase4,
                output=output,
                strict=True,
                allow_nonstandard_count=True,
            )

            self.assertTrue(report["valid"])
            manifest = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual("phase4_training_reference", manifest["trace_records"][0]["role"])
            self.assertTrue(manifest["trace_records"][0]["used_by_neural_abr_lite_training_reference"])

    def test_maps_missing_fingerprint_to_checksum_with_note(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            phase4 = root / "phase4.json"
            output = root / "reference.json"
            _write_phase4(phase4, [{"trace_id": "t1", "checksum_sha256": "abc", "leakage_group": "g1"}])

            build_reference_manifest(
                phase4_dataset_manifest=phase4,
                output=output,
                strict=False,
                allow_nonstandard_count=True,
            )

            record = json.loads(output.read_text(encoding="utf-8"))["trace_records"][0]
            self.assertEqual("abc", record["canonical_content_fingerprint"])
            self.assertIn("canonical_content_fingerprint_inferred_from_checksum_sha256", record["notes"])

    def test_strict_fails_if_trace_records_missing(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            phase4 = root / "phase4.json"
            output = root / "reference.json"
            phase4.write_text(json.dumps({"records": []}), encoding="utf-8")

            with self.assertRaises(Phase6CError):
                build_reference_manifest(phase4_dataset_manifest=phase4, output=output, strict=True)

    def test_strict_enforces_expected_count_unless_allowed(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            phase4 = root / "phase4.json"
            output = root / "reference.json"
            _write_phase4(phase4, [{"trace_id": "t1", "checksum_sha256": "abc", "leakage_group": "g1"}])

            report = build_reference_manifest(phase4_dataset_manifest=phase4, output=output, strict=True)

            self.assertFalse(report["valid"])
            self.assertIn("expected 210 Phase 4 records", "\n".join(report["errors"]))


def _write_phase4(path: Path, records):
    path.write_text(json.dumps({"trace_records": records}), encoding="utf-8")


if __name__ == "__main__":
    unittest.main()

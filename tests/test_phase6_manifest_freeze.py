from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.freeze_phase6_trace_manifest import freeze_phase6_manifest
from scripts.phase6c_source_registry import Phase6CError


class Phase6ManifestFreezeTest(unittest.TestCase):
    def test_freezes_when_validation_and_audit_pass(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            candidate, validation, audit, output = _write_freeze_inputs(root, validation_valid=True, audit_ok=True)

            report = freeze_phase6_manifest(
                candidate_manifest=candidate,
                validation_report=validation,
                eligibility_audit_report=audit,
                output=output,
                strict=True,
            )

            self.assertEqual(1, report["records"])
            frozen = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual("phase6_trace_manifest_final", frozen["manifest_role"])
            self.assertTrue(frozen["phase6c_freeze_only"])

    def test_refuses_freeze_when_validation_invalid(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            candidate, validation, audit, output = _write_freeze_inputs(root, validation_valid=False, audit_ok=True)

            with self.assertRaises(Phase6CError):
                freeze_phase6_manifest(
                    candidate_manifest=candidate,
                    validation_report=validation,
                    eligibility_audit_report=audit,
                    output=output,
                )

    def test_refuses_freeze_when_audit_blocks(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            candidate, validation, audit, output = _write_freeze_inputs(root, validation_valid=True, audit_ok=False)

            with self.assertRaises(Phase6CError):
                freeze_phase6_manifest(
                    candidate_manifest=candidate,
                    validation_report=validation,
                    eligibility_audit_report=audit,
                    output=output,
                )

    def test_benchmark_flags_are_always_false(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            candidate, validation, audit, output = _write_freeze_inputs(root, validation_valid=True, audit_ok=True)

            freeze_phase6_manifest(
                candidate_manifest=candidate,
                validation_report=validation,
                eligibility_audit_report=audit,
                output=output,
            )

            frozen = json.loads(output.read_text(encoding="utf-8"))
            self.assertFalse(frozen["benchmark_authorized"])
            self.assertFalse(frozen["ready_for_benchmark"])
            self.assertFalse(frozen["freeze_metadata"]["benchmark_authorized"])
            self.assertFalse(frozen["freeze_metadata"]["ready_for_benchmark"])


def _write_freeze_inputs(root: Path, *, validation_valid: bool, audit_ok: bool):
    candidate = root / "candidate.json"
    validation = root / "validation.json"
    audit = root / "audit.json"
    output = root / "final.json"
    candidate.write_text(
        json.dumps(
            {
                "schema_version": "phase6_trace_manifest_v1",
                "trace_records": [{"trace_id": "trace_a", "eval_gate": "use_for_eval"}],
                "benchmark_authorized": True,
                "ready_for_benchmark": True,
            }
        ),
        encoding="utf-8",
    )
    validation.write_text(json.dumps({"valid": validation_valid}), encoding="utf-8")
    audit.write_text(json.dumps({"use_for_phase6_eval": audit_ok}), encoding="utf-8")
    return candidate, validation, audit, output


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.build_phase6_candidate_manifest import build_candidate_manifest
from scripts.phase6c_source_registry import create_external_layout
from scripts.validate_phase6_trace_manifest import validate_manifest


class Phase6CandidateManifestTest(unittest.TestCase):
    def test_builds_candidate_with_eval_raca_and_diagnostic_same_family(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "external"
            create_external_layout(root)
            _write_metadata(root, "raca_4g_lte", "raca_trace", "fp-raca")
            _write_metadata(root, "ghent_4g_lte", "ghent_trace", "fp-ghent")
            output = root / "manifests" / "candidate.json"

            report = build_candidate_manifest(external_root=root, output=output, strict=True)

            self.assertTrue(report["valid"])
            records = {record["trace_id"]: record for record in json.loads(output.read_text(encoding="utf-8"))["trace_records"]}
            self.assertEqual("use_for_eval", records["raca_trace"]["eval_gate"])
            self.assertEqual("ood_final", records["raca_trace"]["split"])
            self.assertEqual("diagnostic_only", records["ghent_trace"]["eval_gate"])

    def test_rejects_duplicate_fingerprints_among_use_for_eval(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "external"
            create_external_layout(root)
            _write_metadata(root, "raca_4g_lte", "raca_4g", "shared")
            _write_metadata(root, "raca_5g", "raca_5g", "shared")
            output = root / "manifests" / "candidate.json"

            report = build_candidate_manifest(external_root=root, output=output, strict=True)

            self.assertFalse(report["valid"])
            self.assertIn("duplicate canonical_content_fingerprint", "\n".join(report["errors"]))

    def test_rejects_lancaster_as_use_for_eval(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "external"
            create_external_layout(root)
            _write_metadata(
                root,
                "lancaster_abr_throughput_traces",
                "lancaster_trace",
                "fp-lancaster",
                eval_gate="use_for_eval",
                split="ood_final",
            )
            output = root / "manifests" / "candidate.json"

            report = build_candidate_manifest(external_root=root, output=output, strict=False)

            self.assertFalse(report["valid"])
            records = json.loads(output.read_text(encoding="utf-8"))["trace_records"]
            self.assertEqual("do_not_use_for_eval", records[0]["eval_gate"])

    def test_output_validates_with_phase6_manifest_validator(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "external"
            create_external_layout(root)
            _write_metadata(root, "raca_4g_lte", "raca_trace", "fp-raca")
            output = root / "manifests" / "candidate.json"

            report = build_candidate_manifest(external_root=root, output=output, strict=True)
            validation = validate_manifest(output, strict_final=True)

            self.assertTrue(report["valid"])
            self.assertTrue(validation["valid"])


def _write_metadata(
    external_root: Path,
    dataset_family: str,
    trace_id: str,
    fingerprint: str,
    *,
    eval_gate: str | None = None,
    split: str | None = None,
) -> None:
    metadata_dir = external_root / "manifests" / "per_trace" / dataset_family
    metadata_dir.mkdir(parents=True, exist_ok=True)
    metadata = {
        "trace_id": trace_id,
        "dataset_family": dataset_family,
        "source_dataset": dataset_family,
        "source_id": dataset_family,
        "split": split or ("ood_final" if dataset_family.startswith("raca") else "same_family_candidate"),
        "eval_gate": eval_gate or ("use_for_eval" if dataset_family.startswith("raca") else "diagnostic_only"),
        "trace_csv": str(external_root / "normalized" / dataset_family / (trace_id + ".csv")),
        "schema_version": "normalized_trace_schema_v1",
        "checksum_sha256": "checksum-" + trace_id,
        "canonical_content_fingerprint": fingerprint,
        "leakage_group": dataset_family + ":" + fingerprint,
        "duration_s": 1,
        "sample_count": 1,
        "license_status": "synthetic",
        "acquisition_status": "acquired",
        "normalization_status": "normalized",
    }
    (metadata_dir / (trace_id + ".json")).write_text(json.dumps(metadata), encoding="utf-8")


if __name__ == "__main__":
    unittest.main()

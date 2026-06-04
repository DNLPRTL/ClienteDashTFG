from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from core.trace_replay.converters.common import sha256_file, write_normalized_csv
from core.trace_replay.manifest_validation import (
    Phase3ManifestValidationError,
    validate_phase3_trace_manifest_data,
)


class Phase3ManifestValidationTest(unittest.TestCase):
    def test_valid_manifest_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = self.build_manifest(Path(tmp))

            summary = validate_phase3_trace_manifest_data(manifest, verify_source_hash=True)

        self.assertEqual("PASS" if summary["trace_count"] == 2 else "FAIL", "PASS")
        self.assertFalse(summary["ready_for_benchmark"])
        self.assertEqual({"available_bandwidth": 2}, summary["semantics_counts"])

    def test_missing_csv_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = self.build_manifest(Path(tmp))
            Path(manifest["traces"][0]["normalized_trace_path"]).unlink()

            with self.assertRaises(Phase3ManifestValidationError):
                validate_phase3_trace_manifest_data(manifest)

    def test_fingerprint_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = self.build_manifest(Path(tmp))
            manifest["traces"][0]["content_fingerprint_sha256"] = "bad"

            with self.assertRaisesRegex(Phase3ManifestValidationError, "fingerprint"):
                validate_phase3_trace_manifest_data(manifest)

    def test_leakage_group_in_two_splits_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = self.build_manifest(Path(tmp))
            manifest["traces"][1]["leakage_group"] = manifest["traces"][0]["leakage_group"]
            manifest["traces"][1]["split"] = "eval"

            with self.assertRaisesRegex(Phase3ManifestValidationError, "spans splits"):
                validate_phase3_trace_manifest_data(manifest)

    def test_benchmark_flags_must_stay_false(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = self.build_manifest(Path(tmp))
            manifest["ready_for_benchmark"] = True

            with self.assertRaisesRegex(Phase3ManifestValidationError, "ready_for_benchmark"):
                validate_phase3_trace_manifest_data(manifest)

    def build_manifest(self, root: Path) -> dict[str, object]:
        traces = []
        for index, split in enumerate(("train", "test")):
            rows = [
                {"timestamp_s": 0.0, "duration_s": 1.0, "throughput_kbps": 1000.0 + index},
                {"timestamp_s": 1.0, "duration_s": 1.0, "throughput_kbps": 2000.0 + index},
            ]
            normalized_path = root / "normalized" / "schema_v1" / "synthetic" / "trace_{0}.csv".format(index)
            stats = write_normalized_csv(rows, normalized_path)
            metadata_path = root / "manifest" / "traces" / "synthetic" / "trace_{0}.json".format(index)
            metadata_path.parent.mkdir(parents=True, exist_ok=True)
            raw_path = root / "raw_{0}.csv".format(index)
            raw_path.write_text("raw {0}\n".format(index), encoding="utf-8")
            trace = {
                "trace_id": "trace_{0}".format(index),
                "dataset_id": "synthetic",
                "converter_id": "test",
                "normalized_trace_path": str(normalized_path),
                "metadata_path": str(metadata_path),
                "source_path": str(raw_path),
                "source_sha256": sha256_file(raw_path),
                "group_id": "group_{0}".format(index),
                "leakage_group": "leakage_{0}".format(index),
                "semantics": "available_bandwidth",
                "split": split,
                "row_count": stats["row_count"],
                "duration_s": stats["duration_s"],
                "throughput_min_kbps": stats["throughput_min_kbps"],
                "throughput_mean_kbps": stats["throughput_mean_kbps"],
                "throughput_max_kbps": stats["throughput_max_kbps"],
                "content_fingerprint_sha256": stats["content_fingerprint_sha256"],
            }
            metadata_path.write_text(json.dumps(trace), encoding="utf-8")
            traces.append(trace)
        return {
            "schema_id": "phase3_trace_manifest_final_v1",
            "phase": "phase3_rebuild",
            "artifact_set": "final",
            "normalized_schema_id": "normalized_trace_schema_v1",
            "split_strategy": "stratified_by_semantics_and_leakage_group",
            "ready_for_benchmark": False,
            "benchmark_authorized": False,
            "outputs_are_benchmark_results": False,
            "trace_count": 2,
            "split_counts": {"train": 1, "test": 1, "eval": 0},
            "semantics_counts": {"available_bandwidth": 2},
            "traces": traces,
        }


if __name__ == "__main__":
    unittest.main()

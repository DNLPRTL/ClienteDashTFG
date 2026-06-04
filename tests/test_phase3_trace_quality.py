from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core.trace_replay.converters.common import sha256_file, write_normalized_csv
from core.trace_replay.manifest_validation import validate_phase3_trace_manifest_data
from core.trace_replay.quality import TraceQualityPolicy, assess_trace_quality, build_quality_audit


class Phase3TraceQualityTest(unittest.TestCase):
    def test_mostly_zero_but_long_trace_is_kept_as_severe_network(self):
        with tempfile.TemporaryDirectory() as tmp:
            trace = self.build_trace(Path(tmp), "mostly_zero", [0.0] * 40 + [500.0] * 10, split="train")

            assessment = assess_trace_quality(trace, policy=TraceQualityPolicy())

        self.assertTrue(assessment.usable_for_training)
        self.assertTrue(assessment.usable_for_eval)
        self.assertIn("mostly_zero_intermitent_or_severe_network", assessment.quality_flags)
        self.assertEqual("severe_or_intermittent_network", assessment.network_condition)

    def test_short_all_zero_trace_is_excluded(self):
        with tempfile.TemporaryDirectory() as tmp:
            trace = self.build_trace(Path(tmp), "bad", [0.0], split="train")

            assessment = assess_trace_quality(trace, policy=TraceQualityPolicy())

        self.assertFalse(assessment.usable_for_training)
        self.assertIn("row_count_lt_30", assessment.exclusion_reasons)
        self.assertIn("duration_s_lt_30", assessment.exclusion_reasons)
        self.assertIn("all_zero_throughput", assessment.exclusion_reasons)
        self.assertEqual("no_useful_signal", assessment.network_condition)

    def test_quality_audit_builds_valid_curated_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            good = self.build_trace(root, "good", [100.0] * 40, split="train")
            severe = self.build_trace(root, "severe", [0.0] * 35 + [200.0] * 5, split="test")
            bad = self.build_trace(root, "bad", [0.0], split="eval")
            manifest = self.build_manifest([good, severe, bad])

            audit, curated = build_quality_audit(manifest, policy=TraceQualityPolicy())
            summary = validate_phase3_trace_manifest_data(curated)

        self.assertEqual(3, audit["source_manifest_trace_count"])
        self.assertEqual(2, audit["kept_trace_count"])
        self.assertEqual(1, audit["excluded_trace_count"])
        self.assertEqual(2, summary["trace_count"])
        self.assertEqual({"train": 1, "test": 1, "eval": 0}, summary["split_counts"])
        self.assertEqual(1, curated["quality_excluded_count"])

    def build_trace(self, root: Path, trace_name: str, throughput_values: list[float], split: str) -> dict[str, object]:
        rows = [
            {"timestamp_s": float(index), "duration_s": 1.0, "throughput_kbps": value}
            for index, value in enumerate(throughput_values)
        ]
        normalized_path = root / "normalized" / "{0}.csv".format(trace_name)
        stats = write_normalized_csv(rows, normalized_path)
        metadata_path = root / "metadata" / "{0}.json".format(trace_name)
        metadata_path.parent.mkdir(parents=True, exist_ok=True)
        raw_path = root / "raw_{0}.txt".format(trace_name)
        raw_path.write_text("raw {0}\n".format(trace_name), encoding="utf-8")
        trace = {
            "trace_id": "trace_{0}".format(trace_name),
            "dataset_id": "synthetic",
            "converter_id": "test",
            "normalized_trace_path": str(normalized_path),
            "metadata_path": str(metadata_path),
            "source_path": str(raw_path),
            "source_sha256": sha256_file(raw_path),
            "group_id": "group_{0}".format(trace_name),
            "leakage_group": "leakage_{0}".format(trace_name),
            "semantics": "available_bandwidth",
            "split": split,
            "row_count": stats["row_count"],
            "duration_s": stats["duration_s"],
            "throughput_min_kbps": stats["throughput_min_kbps"],
            "throughput_mean_kbps": stats["throughput_mean_kbps"],
            "throughput_max_kbps": stats["throughput_max_kbps"],
            "content_fingerprint_sha256": stats["content_fingerprint_sha256"],
        }
        metadata_path.write_text("{}", encoding="utf-8")
        return trace

    def build_manifest(self, traces: list[dict[str, object]]) -> dict[str, object]:
        return {
            "schema_id": "phase3_trace_manifest_final_v1",
            "phase": "phase3_rebuild",
            "artifact_set": "final",
            "normalized_schema_id": "normalized_trace_schema_v1",
            "split_strategy": "stratified_by_semantics_and_leakage_group",
            "ready_for_benchmark": False,
            "benchmark_authorized": False,
            "outputs_are_benchmark_results": False,
            "trace_count": len(traces),
            "split_counts": {
                "train": sum(1 for trace in traces if trace["split"] == "train"),
                "test": sum(1 for trace in traces if trace["split"] == "test"),
                "eval": sum(1 for trace in traces if trace["split"] == "eval"),
            },
            "semantics_counts": {"available_bandwidth": len(traces)},
            "traces": traces,
        }


if __name__ == "__main__":
    unittest.main()

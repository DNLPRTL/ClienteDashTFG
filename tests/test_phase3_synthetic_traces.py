from __future__ import annotations

import csv
import json
import statistics
import tempfile
import unittest
from collections import defaultdict
from pathlib import Path

from core.trace_replay.manifest_validation import validate_phase3_trace_manifest_data
from core.trace_replay.synthetic import (
    SCENARIO_IDS,
    SYNTHETIC_DATASET_ID,
    SYNTHETIC_GENERATOR_ID,
    SYNTHETIC_SEMANTICS,
    generate_synthetic_trace_rows,
    generate_synthetic_trace_set,
    merge_synthetic_entries_into_manifest,
)


class Phase3SyntheticTracesTest(unittest.TestCase):
    def test_each_scenario_generates_valid_300_second_rows(self):
        for scenario_id in SCENARIO_IDS:
            with self.subTest(scenario=scenario_id):
                rows, source_spec = generate_synthetic_trace_rows(
                    scenario_id,
                    trace_index=0,
                    duration_s=300,
                    sample_duration_s=1.0,
                )

                self.assertEqual(300, len(rows))
                self.assertEqual(scenario_id, source_spec.synthetic_scenario)
                self.assertTrue(source_spec.synthetic)
                previous_timestamp = -1.0
                for index, row in enumerate(rows):
                    self.assertEqual(float(index), row["timestamp_s"])
                    self.assertEqual(1.0, row["duration_s"])
                    self.assertGreaterEqual(row["throughput_kbps"], 0.0)
                    self.assertGreater(row["timestamp_s"], previous_timestamp)
                    previous_timestamp = row["timestamp_s"]

    def test_scenario_patterns_are_detectable(self):
        scenarios = {
            scenario_id: [row["throughput_kbps"] for row in generate_synthetic_trace_rows(scenario_id, 7)[0]]
            for scenario_id in SCENARIO_IDS
        }

        self.assertGreater(min(scenarios["synthetic_perfect_high"]), 8900)
        self.assertEqual(len(set(scenarios["synthetic_perfect_high"])), 1)
        self.assertLess(max(scenarios["synthetic_stable_low"]), 950)
        self.assertEqual(len(set(scenarios["synthetic_stable_low"])), 1)

        drop = scenarios["synthetic_sudden_drop"]
        self.assertGreater(statistics.mean(drop[:80]), statistics.mean(drop[-80:]) * 4)
        recovery = scenarios["synthetic_sudden_recovery"]
        self.assertGreater(statistics.mean(recovery[-80:]), statistics.mean(recovery[:80]) * 4)

        mobile = scenarios["synthetic_mobile_variable"]
        self.assertGreater(max(mobile) - min(mobile), 4000)
        self.assertGreater(len({round(value / 1000) for value in mobile}), 3)

        oscillation = scenarios["synthetic_periodic_oscillation"]
        direction_changes = 0
        previous_direction = 0
        for left, right in zip(oscillation, oscillation[1:]):
            direction = 1 if right > left else -1 if right < left else 0
            if direction and previous_direction and direction != previous_direction:
                direction_changes += 1
            if direction:
                previous_direction = direction
        self.assertGreaterEqual(direction_changes, 5)

        stall = scenarios["synthetic_stall_trap"]
        self.assertGreater(min(stall), 3700)
        self.assertLess(max(stall), 4300)

        jitter = scenarios["synthetic_high_jitter"]
        self.assertGreater(statistics.pstdev(jitter), 1500)
        self.assertGreater(statistics.mean(jitter), 2500)

    def test_trace_set_writes_metadata_sources_and_splits(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            entries, report = generate_synthetic_trace_set(
                normalized_root=root / "datasets_normalizados" / "phase3" / "final",
                metadata_root=root / "manifests_trazas" / "phase3" / "final",
                count_per_scenario=4,
                duration_s=30,
                sample_duration_s=1.0,
                seed="test_seed",
                clean=True,
            )

            self.assertEqual(len(SCENARIO_IDS) * 4, len(entries))
            self.assertEqual(len(entries), report["trace_count"])
            self.assertEqual(SYNTHETIC_DATASET_ID, report["dataset_id"])
            self.assertEqual(SYNTHETIC_SEMANTICS, report["semantics"])
            split_by_group = {}
            for entry in entries:
                self.assertTrue(entry["synthetic"])
                self.assertEqual(SYNTHETIC_GENERATOR_ID, entry["generator_version"])
                self.assertTrue(Path(entry["normalized_trace_path"]).is_file())
                self.assertTrue(Path(entry["metadata_path"]).is_file())
                self.assertTrue(Path(entry["source_path"]).is_file())
                with Path(entry["normalized_trace_path"]).open(newline="", encoding="utf-8") as handle:
                    rows = list(csv.DictReader(handle))
                self.assertEqual(30, len(rows))
                source_spec = json.loads(Path(entry["source_path"]).read_text(encoding="utf-8"))
                self.assertTrue(source_spec["synthetic"])
                self.assertEqual(entry["synthetic_scenario"], source_spec["synthetic_scenario"])
                group = entry["leakage_group"]
                split = entry["split"]
                self.assertNotIn(group, split_by_group)
                split_by_group[group] = split

    def test_merged_manifest_validates_and_preserves_real_splits(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            base = self._base_manifest(root)
            entries, _ = generate_synthetic_trace_set(
                normalized_root=root / "datasets_normalizados" / "phase3" / "final",
                metadata_root=root / "manifests_trazas" / "phase3" / "final",
                count_per_scenario=3,
                duration_s=30,
                sample_duration_s=1.0,
                seed="merge_seed",
                clean=True,
            )

            merged = merge_synthetic_entries_into_manifest(base, entries)
            summary = validate_phase3_trace_manifest_data(merged, verify_source_hash=True)

        self.assertEqual(2 + len(entries), summary["trace_count"])
        self.assertEqual(2, sum(1 for trace in merged["traces"] if trace["dataset_id"] == "real_fixture"))
        self.assertEqual(len(entries), merged["synthetic_addendum"]["trace_count"])

    def _base_manifest(self, root: Path) -> dict[str, object]:
        from core.trace_replay.converters.common import sha256_file, write_normalized_csv

        traces = []
        for index, split in enumerate(("train", "eval")):
            raw = root / "raw" / "real_{0}.txt".format(index)
            raw.parent.mkdir(parents=True, exist_ok=True)
            raw.write_text("real {0}\n".format(index), encoding="utf-8")
            normalized = root / "datasets_normalizados" / "phase3" / "final" / "schema_v1" / "real" / "real_{0}.csv".format(index)
            stats = write_normalized_csv(
                [
                    {"timestamp_s": 0, "duration_s": 1, "throughput_kbps": 1000 + index},
                    {"timestamp_s": 1, "duration_s": 1, "throughput_kbps": 2000 + index},
                ],
                normalized,
            )
            metadata = root / "manifests_trazas" / "phase3" / "final" / "traces" / "real" / "real_{0}.json".format(index)
            metadata.parent.mkdir(parents=True, exist_ok=True)
            trace = {
                "trace_id": "real_{0}".format(index),
                "dataset_id": "real_fixture",
                "converter_id": "test",
                "normalized_trace_path": str(normalized),
                "metadata_path": str(metadata),
                "source_path": str(raw),
                "source_sha256": sha256_file(raw),
                "group_id": "real_group_{0}".format(index),
                "leakage_group": "real_group_{0}".format(index),
                "semantics": "available_bandwidth",
                "split": split,
                "row_count": stats["row_count"],
                "duration_s": stats["duration_s"],
                "throughput_min_kbps": stats["throughput_min_kbps"],
                "throughput_mean_kbps": stats["throughput_mean_kbps"],
                "throughput_max_kbps": stats["throughput_max_kbps"],
                "content_fingerprint_sha256": stats["content_fingerprint_sha256"],
            }
            metadata.write_text(json.dumps(trace), encoding="utf-8")
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
            "trace_count": len(traces),
            "split_counts": {"train": 1, "test": 0, "eval": 1},
            "semantics_counts": {"available_bandwidth": 2},
            "traces": traces,
        }


if __name__ == "__main__":
    unittest.main()

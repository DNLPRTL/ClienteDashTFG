from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core.trace_replay.inventory import build_raw_dataset_inventory
from core.trace_replay.splits import build_phase3_trace_manifest


class Phase3InventoryAndSplitsTest(unittest.TestCase):
    def test_raw_inventory_is_read_only_and_detects_dataset_hints(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "dataset en bruto"
            sample = root / "Norway HSDPA (UMass trace archive)" / "bus" / "trace.log"
            sample.parent.mkdir(parents=True)
            sample.write_text("0 1000 0 0 1000000 1000\n", encoding="utf-8")
            before = sample.read_text(encoding="utf-8")

            inventory = build_raw_dataset_inventory(root, hash_mode="none")

            self.assertEqual(before, sample.read_text(encoding="utf-8"))
            self.assertEqual("phase3_raw_dataset_inventory_v1", inventory["schema_id"])
            self.assertEqual(1, inventory["dataset_count"])
            dataset = inventory["datasets"][0]
            self.assertEqual("norway_hsdpa_umass", dataset["dataset_id"])
            self.assertEqual({"whitespace_6_column_interval_log": 1}, dataset["parser_hints"])
            self.assertEqual(("unix_time_s", "monotonic_time_ms", "latitude_deg", "longitude_deg", "bytes_received", "elapsed_ms"), tuple(dataset["files"][0]["columns_detected"]))

    def test_final_manifest_splits_by_leakage_group_and_excludes_duplicates(self):
        entries = []
        for index in range(5):
            entries.append(
                {
                    "trace_id": "trace_{0}".format(index),
                    "dataset_id": "synthetic",
                    "converter_id": "test",
                    "normalized_trace_path": "trace_{0}.csv".format(index),
                    "metadata_path": "trace_{0}.json".format(index),
                    "source_path": "raw_{0}.csv".format(index),
                    "source_sha256": "raw_hash_{0}".format(index),
                    "group_id": "group_{0}".format(index),
                    "leakage_group": "leakage_{0}".format(index),
                    "semantics": "available_bandwidth",
                    "row_count": 2,
                    "duration_s": 2.0,
                    "throughput_min_kbps": 1000.0,
                    "throughput_mean_kbps": 1500.0,
                    "throughput_max_kbps": 2000.0,
                    "content_fingerprint_sha256": "fingerprint_{0}".format(index),
                }
            )
        duplicate = dict(entries[0])
        duplicate["trace_id"] = "trace_duplicate"
        entries.append(duplicate)

        manifest = build_phase3_trace_manifest(entries, seed="unit-test")

        self.assertEqual("phase3_trace_manifest_final_v1", manifest["schema_id"])
        self.assertFalse(manifest["ready_for_benchmark"])
        self.assertFalse(manifest["benchmark_authorized"])
        self.assertEqual(5, manifest["trace_count"])
        self.assertEqual(1, manifest["excluded_duplicate_count"])

        group_to_split = {}
        for trace in manifest["traces"]:
            group = trace["leakage_group"]
            split = trace["split"]
            if group in group_to_split:
                self.assertEqual(group_to_split[group], split)
            group_to_split[group] = split

        self.assertGreater(manifest["split_counts"]["train"], 0)
        self.assertGreater(manifest["split_counts"]["test"], 0)
        self.assertGreater(manifest["split_counts"]["eval"], 0)


if __name__ == "__main__":
    unittest.main()

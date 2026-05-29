from __future__ import annotations

import csv
import json
import tempfile
import unittest
from pathlib import Path

from core.neural_abr.trace_corpus import prepare_phase4e2_trace_corpus


class NeuralAbrTraceCorpusTest(unittest.TestCase):
    def test_prepare_phase4e2_trace_corpus_writes_inventory_and_manifest_fields(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            phase3_root = root / "phase3"
            output_root = root / "phase4" / "external_trace_intake" / "phase4e2_expanded"
            _write_phase3_normalized_fixture(phase3_root)

            result = prepare_phase4e2_trace_corpus(
                phase3_root=phase3_root,
                output_root=output_root,
                max_total_traces=10,
                max_traces_per_dataset=10,
                seed=123,
                overwrite=True,
            )

            summary = result["summary"]
            self.assertEqual(3, summary["selected_trace_count"])
            self.assertEqual({"unit_dataset": 3}, summary["dataset_id_counts"])
            self.assertTrue((output_root / "phase4e2_trace_inventory.json").is_file())
            self.assertTrue((output_root / "phase4e2_trace_corpus_summary.json").is_file())

            manifest_path = next((output_root / "manifests").rglob("*.json"))
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            for field in (
                "trace_id",
                "dataset_id",
                "leakage_group",
                "sample_count",
                "source_kind",
                "converter",
                "mean_throughput_kbps",
                "min_throughput_kbps",
                "max_throughput_kbps",
                "coefficient_of_variation",
                "regime_bucket",
                "checksum_or_source_fingerprint",
            ):
                self.assertIn(field, manifest)


def _write_phase3_normalized_fixture(phase3_root: Path) -> None:
    normalized_root = phase3_root / "_normalized" / "schema_v1" / "phase3_4a_smoke" / "unit_dataset"
    manifest_root = phase3_root / "_manifests" / "phase3_4a_conversion_smoke" / "unit_dataset"
    expanded_root = phase3_root / "_expanded_phase3_4a"
    normalized_root.mkdir(parents=True)
    manifest_root.mkdir(parents=True)
    expanded_root.mkdir(parents=True)
    for index in range(3):
        trace_id = "unit_trace_{0}".format(index)
        csv_path = normalized_root / (trace_id + ".csv")
        _write_trace_csv(csv_path, base_kbps=800 + index * 500)
        manifest = {
            "trace_id": trace_id,
            "dataset_id": "unit_dataset",
            "leakage_group": "unit_leakage_{0}".format(index),
            "sample_count": 8,
            "mean_throughput_kbps": 900 + index * 500,
            "min_throughput_kbps": 800 + index * 500,
            "max_throughput_kbps": 1000 + index * 500,
            "converter_name": "unit_converter",
            "checksum_sha256": "checksum-{0}".format(index),
        }
        (manifest_root / (trace_id + ".json")).write_text(json.dumps(manifest), encoding="utf-8")


def _write_trace_csv(path: Path, base_kbps: int) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["timestamp_s", "duration_s", "throughput_kbps"])
        writer.writeheader()
        for index in range(8):
            writer.writerow(
                {
                    "timestamp_s": "{0:.3f}".format(float(index)),
                    "duration_s": "1.000",
                    "throughput_kbps": str(base_kbps + (index % 2) * 100),
                }
            )


if __name__ == "__main__":
    unittest.main()

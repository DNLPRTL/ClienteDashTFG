from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from core.neural_abr.artifacts import read_json, read_jsonl
from core.neural_abr.constants import OOD_SPLIT, PHASE4E1_SPLIT_POLICY, TRAIN_SPLIT, VALIDATION_SPLIT
from core.neural_abr.dataset_builder import build_external_trace_dataset
from core.neural_abr.trace_source import load_external_trace_records
from core.neural_abr.validation import validate_dataset_dir


class NeuralAbrExternalTraceTest(unittest.TestCase):
    def test_external_trace_loader_preserves_matching_manifest_metadata(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            csv_root, manifest_root = self.write_external_fixture(root, dataset_count=1, traces_per_dataset=3)

            records = load_external_trace_records(csv_root, manifest_root, seed=123, segment_duration_s=4.0)

            self.assertEqual(3, len(records))
            first = records[0]
            self.assertFalse(first.manifest_missing)
            self.assertIn(first.split, (TRAIN_SPLIT, VALIDATION_SPLIT, OOD_SPLIT))
            self.assertIn("dataset_id", first.trace_metadata)
            self.assertIn("checksum_sha256", first.trace_metadata)

    def test_missing_manifest_uses_conservative_metadata(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            csv_root = root / "normalized"
            csv_root.mkdir()
            self.write_trace_csv(csv_root / "lonely_trace.csv", dataset_id="missing_manifest_dataset", base_kbps=1200)

            records = load_external_trace_records(csv_root, None, seed=123, segment_duration_s=4.0)

            self.assertEqual(1, len(records))
            self.assertTrue(records[0].manifest_missing)
            self.assertEqual("missing_manifest_dataset", records[0].source_dataset)
            self.assertEqual("missing_manifest_conservative_metadata", records[0].trace_metadata["source_url_or_reference"])

    def test_dataset_build_uses_trace_level_split_and_valid_labels(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            csv_root, manifest_root = self.write_external_fixture(root, dataset_count=2, traces_per_dataset=3)
            output_dir = root / "dataset"

            result = build_external_trace_dataset(
                trace_csv_root=csv_root,
                trace_manifest_root=manifest_root,
                output_dir=output_dir,
                split_policy=PHASE4E1_SPLIT_POLICY,
                representation_kbps=(300, 750, 1200, 1850, 2850),
                segment_duration_s=4.0,
                teacher="robust_mpc",
                seed=123,
                diagnostic_only=True,
                overwrite=True,
            )
            report = validate_dataset_dir(output_dir)

            self.assertEqual("PASS", report["status"])
            self.assertGreater(result["sample_counts"][TRAIN_SPLIT], 0)
            self.assertGreater(result["sample_counts"][VALIDATION_SPLIT], 0)
            self.assertGreater(result["sample_counts"][OOD_SPLIT], 0)
            manifest = read_json(output_dir / "dataset_manifest.json")
            self.assertEqual(PHASE4E1_SPLIT_POLICY, manifest["split_policy"])
            self.assertTrue(manifest["external_trace_smoke"])

            trace_splits = {}
            leakage_splits = {}
            for split, filename in (
                (TRAIN_SPLIT, "train.jsonl"),
                (VALIDATION_SPLIT, "validation.jsonl"),
                (OOD_SPLIT, "ood_diagnostic.jsonl"),
            ):
                for sample in read_jsonl(output_dir / filename):
                    metadata = sample["metadata"]
                    trace_splits.setdefault(metadata["trace_id"], split)
                    self.assertEqual(split, trace_splits[metadata["trace_id"]])
                    leakage_splits.setdefault(metadata["leakage_group"], split)
                    self.assertEqual(split, leakage_splits[metadata["leakage_group"]])
                    action = sample["label"]["teacher_action"]
                    self.assertTrue(sample["action_mask"][action])

    def test_external_cli_smoke_uses_temp_trace_fixture(self):
        repo_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            csv_root, manifest_root = self.write_external_fixture(root, dataset_count=2, traces_per_dataset=3)
            dataset_dir = root / "dataset"

            command = [
                sys.executable,
                "scripts/build_neural_abr_dataset.py",
                "--trace-csv-root",
                str(csv_root),
                "--trace-manifest-root",
                str(manifest_root),
                "--output-dir",
                str(dataset_dir),
                "--split-policy",
                PHASE4E1_SPLIT_POLICY,
                "--representation-kbps",
                "300,750,1200,1850,2850",
                "--segment-duration-s",
                "4.0",
                "--teacher",
                "robust_mpc",
                "--seed",
                "123",
                "--diagnostic-only",
                "--overwrite",
            ]
            completed = subprocess.run(command, cwd=repo_root, text=True, capture_output=True, check=False)

            self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
            self.assertTrue((dataset_dir / "dataset_manifest.json").is_file())
            self.assertEqual("PASS", validate_dataset_dir(dataset_dir)["status"])

    def write_external_fixture(self, root: Path, dataset_count: int, traces_per_dataset: int):
        csv_root = root / "normalized"
        manifest_root = root / "manifests"
        csv_root.mkdir()
        manifest_root.mkdir()
        for dataset_index in range(dataset_count):
            dataset_id = "dataset_{0}".format(dataset_index)
            (csv_root / dataset_id).mkdir()
            (manifest_root / dataset_id).mkdir()
            for trace_index in range(traces_per_dataset):
                trace_id = "{0}_trace_{1}".format(dataset_id, trace_index)
                csv_path = csv_root / dataset_id / (trace_id + ".csv")
                base_kbps = 700 + dataset_index * 400 + trace_index * 300
                self.write_trace_csv(csv_path, dataset_id=dataset_id, base_kbps=base_kbps)
                manifest = {
                    "trace_id": trace_id,
                    "dataset_id": dataset_id,
                    "leakage_group": "{0}_group_{1}".format(dataset_id, trace_index),
                    "mean_throughput_kbps": base_kbps + 150,
                    "min_throughput_kbps": base_kbps,
                    "max_throughput_kbps": base_kbps + 300,
                    "sample_count": 24,
                    "mobility_tags": ["mobile"],
                    "network_tags": ["LTE"],
                    "scenario_tags": ["unit"],
                    "source_url_or_reference": "unit-test",
                    "converter_name": "unit_converter",
                    "converter_version_or_commit": "unit",
                    "checksum_sha256": "checksum-{0}".format(trace_id),
                }
                with (manifest_root / dataset_id / (trace_id + ".json")).open("w", encoding="utf-8") as handle:
                    json.dump(manifest, handle)
        return csv_root, manifest_root

    def write_trace_csv(self, path: Path, dataset_id: str, base_kbps: int) -> None:
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=[
                    "timestamp_s",
                    "duration_s",
                    "throughput_kbps",
                    "source_dataset",
                    "source_file",
                    "mobility_label",
                    "network_type",
                    "scenario_label",
                    "notes",
                ],
            )
            writer.writeheader()
            timestamp = 0.0
            for index in range(24):
                writer.writerow(
                    {
                        "timestamp_s": "{0:.3f}".format(timestamp),
                        "duration_s": "1.000",
                        "throughput_kbps": str(base_kbps + (index % 4) * 100),
                        "source_dataset": dataset_id,
                        "source_file": str(path.name),
                        "mobility_label": "mobile",
                        "network_type": "LTE",
                        "scenario_label": "unit",
                        "notes": "external_trace_fixture",
                    }
                )
                timestamp += 1.0


if __name__ == "__main__":
    unittest.main()

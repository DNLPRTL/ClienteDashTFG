from __future__ import annotations

import csv
import json
import tempfile
import unittest
from pathlib import Path

from core.neural_abr.constants import OOD_SPLIT, PHASE4E1_SPLIT_POLICY, PHASE4E2_SPLIT_POLICY, SPLITS, VALIDATION_SPLIT
from core.neural_abr.trace_source import TraceSourceError, load_external_trace_records


class NeuralAbrPhase4E2SplitPolicyTest(unittest.TestCase):
    def test_phase4e2_policy_is_trace_level_and_leakage_clean_with_imbalanced_families(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_root, manifest_root = _write_fixture(Path(temp_dir))

            records = load_external_trace_records(
                csv_root,
                manifest_root,
                split_policy=PHASE4E2_SPLIT_POLICY,
                seed=123,
                segment_duration_s=4.0,
            )

            self.assertEqual(12, len(records))
            self.assertTrue({record.split for record in records}.issuperset({VALIDATION_SPLIT, OOD_SPLIT}))
            self.assertEqual(PHASE4E2_SPLIT_POLICY, records[0].trace_metadata["split_policy"])
            self.assertIn("phase4e2_split_summary", records[0].trace_metadata)

            trace_splits = {}
            leakage_splits = {}
            for record in records:
                trace_splits.setdefault(record.trace.trace_id, record.split)
                self.assertEqual(record.split, trace_splits[record.trace.trace_id])
                leakage_splits.setdefault(record.leakage_group, record.split)
                self.assertEqual(record.split, leakage_splits[record.leakage_group])

    def test_phase4e1_policy_remains_supported(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_root, manifest_root = _write_fixture(Path(temp_dir))

            records = load_external_trace_records(
                csv_root,
                manifest_root,
                split_policy=PHASE4E1_SPLIT_POLICY,
                seed=123,
                segment_duration_s=4.0,
            )

            self.assertEqual(12, len(records))
            self.assertTrue(all(record.split in SPLITS for record in records))
            self.assertEqual(PHASE4E1_SPLIT_POLICY, records[0].trace_metadata["split_policy"])

    def test_unsupported_policy_still_raises(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_root, manifest_root = _write_fixture(Path(temp_dir))

            with self.assertRaises(TraceSourceError):
                load_external_trace_records(
                    csv_root,
                    manifest_root,
                    split_policy="phase4e2_typo",
                    seed=123,
                    segment_duration_s=4.0,
                )


def _write_fixture(root: Path):
    csv_root = root / "normalized"
    manifest_root = root / "manifests"
    csv_root.mkdir()
    manifest_root.mkdir()
    plan = (
        ("majority_mobile", ("low_mixed", "low_mixed", "low_mixed", "mid_mixed", "mid_mixed", "high_mixed", "high_mixed")),
        ("minority_hsdpa", ("low_variable", "low_variable", "low_variable", "low_variable", "low_variable")),
    )
    for dataset_id, regimes in plan:
        (csv_root / dataset_id).mkdir()
        (manifest_root / dataset_id).mkdir()
        for index, regime in enumerate(regimes):
            trace_id = "{0}_{1:02d}".format(dataset_id, index)
            csv_path = csv_root / dataset_id / (trace_id + ".csv")
            base_kbps = 600 + index * 150 + (1200 if dataset_id == "majority_mobile" else 0)
            _write_trace_csv(csv_path, base_kbps)
            manifest = {
                "trace_id": trace_id,
                "dataset_id": dataset_id,
                "leakage_group": "{0}_leakage_{1:02d}".format(dataset_id, index),
                "sample_count": 24,
                "mean_throughput_kbps": base_kbps + 75,
                "min_throughput_kbps": base_kbps,
                "max_throughput_kbps": base_kbps + 150,
                "regime_bucket": regime,
                "source_kind": "unit_normalized",
                "converter": "unit",
                "checksum_or_source_fingerprint": "unit-{0}".format(trace_id),
                "checksum_sha256": "unit-{0}".format(trace_id),
            }
            (manifest_root / dataset_id / (trace_id + ".json")).write_text(json.dumps(manifest), encoding="utf-8")
    return csv_root, manifest_root


def _write_trace_csv(path: Path, base_kbps: int) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["timestamp_s", "duration_s", "throughput_kbps"])
        writer.writeheader()
        for index in range(24):
            writer.writerow(
                {
                    "timestamp_s": "{0:.3f}".format(float(index)),
                    "duration_s": "1.000",
                    "throughput_kbps": str(base_kbps + (index % 3) * 75),
                }
            )


if __name__ == "__main__":
    unittest.main()

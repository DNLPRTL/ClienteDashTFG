from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "run_phase6c_trace_materialization.py"


class Phase6COrchestratorTest(unittest.TestCase):
    def test_synthetic_local_only_end_to_end_pipeline(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source_dir = root / "sources"
            source_dir.mkdir()
            raca4_zip = source_dir / "raca4.zip"
            raca5_zip = source_dir / "raca5.zip"
            _write_zip(raca4_zip, "trace4.csv", "timestamp_s,throughput_mbps\n0,1.0\n1,1.5\n")
            _write_zip(raca5_zip, "trace5.csv", "timestamp_s,throughput_mbps\n0,2.0\n1,2.5\n")
            registry = _write_registry(root, raca4_zip, raca5_zip)
            phase4 = root / "phase4.json"
            phase4.write_text(
                json.dumps(
                    {
                        "trace_records": [
                            {
                                "trace_id": "phase4_trace",
                                "checksum_sha256": "phase4_checksum",
                                "canonical_content_fingerprint": "phase4_fingerprint",
                                "leakage_group": "phase4_group",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            external_root = root / "external"

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--external-root",
                    str(external_root),
                    "--phase4-dataset-manifest",
                    str(phase4),
                    "--source-registry",
                    str(registry),
                ],
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(0, result.returncode, result.stderr)
            final_manifest = external_root / "manifests" / "phase6_trace_manifest_final.json"
            self.assertTrue(final_manifest.is_file())
            manifest = json.loads(final_manifest.read_text(encoding="utf-8"))
            self.assertFalse(manifest["benchmark_authorized"])
            self.assertFalse(manifest["ready_for_benchmark"])
            self.assertEqual(2, len([record for record in manifest["trace_records"] if record["eval_gate"] == "use_for_eval"]))


def _write_zip(path: Path, name: str, content: str) -> None:
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(name, content)


def _write_registry(root: Path, raca4_zip: Path, raca5_zip: Path) -> Path:
    registry = {
        "schema_version": "phase6c_public_source_registry_v1",
        "sources": [
            {
                "source_id": "raca_4g_lte",
                "dataset_family": "raca_4g_lte",
                "source_dataset": "Raca 4G LTE",
                "role": "primary_ood_candidate",
                "enabled_by_default": True,
                "download_by_default": True,
                "split": "ood_final",
                "eval_gate": "use_for_eval",
                "canonical_file": "LTE_Dataset.zip",
                "urls": [raca4_zip.as_uri()],
                "expected_hashes": {"md5": hashlib.md5(raca4_zip.read_bytes()).hexdigest()},
                "license_status": "synthetic",
            },
            {
                "source_id": "raca_5g",
                "dataset_family": "raca_5g",
                "source_dataset": "Raca 5G",
                "role": "primary_ood_candidate",
                "enabled_by_default": True,
                "download_by_default": True,
                "split": "ood_final",
                "eval_gate": "use_for_eval",
                "canonical_file": "5G-production-dataset.zip",
                "urls": [raca5_zip.as_uri()],
                "expected_hashes": {},
                "license_status": "synthetic",
            },
        ],
    }
    path = root / "registry.json"
    path.write_text(json.dumps(registry), encoding="utf-8")
    return path


if __name__ == "__main__":
    unittest.main()

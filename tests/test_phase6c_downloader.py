from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts.download_phase6_trace_sources import base_receipt, download_phase6_sources
from scripts.phase6c_source_registry import Phase6CError


class Phase6CDownloaderTest(unittest.TestCase):
    def test_verifies_md5_success_and_writes_receipts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            payload = root / "source.zip"
            payload.write_bytes(b"synthetic archive")
            registry = _write_registry(root, "raca_4g_lte", payload.as_uri(), hashlib.md5(payload.read_bytes()).hexdigest())

            report = download_phase6_sources(
                external_root=root / "external",
                registry_path=registry,
                sources="raca_4g_lte",
                strict=True,
            )

            self.assertTrue(report["valid"])
            receipts_path = Path(report["receipts_path"])
            self.assertTrue(receipts_path.is_file())
            receipts = json.loads(receipts_path.read_text(encoding="utf-8"))["receipts"]
            self.assertEqual("copied_from_local_file", receipts[0]["status"])
            self.assertEqual(hashlib.md5(payload.read_bytes()).hexdigest(), receipts[0]["md5"])

    def test_verifies_md5_failure(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            payload = root / "source.zip"
            payload.write_bytes(b"synthetic archive")
            registry = _write_registry(root, "raca_4g_lte", payload.as_uri(), "00000000000000000000000000000000")

            report = download_phase6_sources(
                external_root=root / "external",
                registry_path=registry,
                sources="raca_4g_lte",
                strict=True,
            )

            self.assertFalse(report["valid"])
            self.assertIn("checksum_mismatch", "\n".join(report["errors"]))

    def test_existing_valid_archive_is_skipped_by_default(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            payload = root / "source.zip"
            payload.write_bytes(b"synthetic archive")
            registry = _write_registry(root, "raca_4g_lte", payload.as_uri(), hashlib.md5(payload.read_bytes()).hexdigest())

            first = download_phase6_sources(
                external_root=root / "external",
                registry_path=registry,
                sources="raca_4g_lte",
                strict=True,
            )
            second = download_phase6_sources(
                external_root=root / "external",
                registry_path=registry,
                sources="raca_4g_lte",
                strict=True,
            )

            self.assertTrue(first["valid"])
            self.assertTrue(second["valid"])
            self.assertEqual("skipped_existing", second["receipts"][0]["status"])

    def test_lumos_blocked_does_not_fail_unless_required(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            registry = _write_lumos_registry(root)

            with mock.patch(
                "scripts.download_phase6_trace_sources.download_google_drive",
                return_value=base_receipt(
                    {"source_id": "lumos5g", "dataset_family": "lumos5g", "role": "optional_ood_candidate"},
                    "blocked_by_provider_or_manual_confirmation_required",
                    error="captcha",
                ),
            ):
                report = download_phase6_sources(
                    external_root=root / "external",
                    registry_path=registry,
                    sources="lumos5g",
                    require_lumos=False,
                )
                required = download_phase6_sources(
                    external_root=root / "external_required",
                    registry_path=registry,
                    sources="lumos5g",
                    require_lumos=True,
                )

            self.assertTrue(report["valid"])
            self.assertIn("blocked_by_provider_or_manual_confirmation_required", "\n".join(report["warnings"]))
            self.assertFalse(required["valid"])
            self.assertIn("blocked_by_provider_or_manual_confirmation_required", "\n".join(required["errors"]))

    def test_refuses_to_write_inside_repo_path(self):
        repo_child = Path(__file__).resolve().parents[1] / "_phase6c_should_not_write"
        with self.assertRaises(Phase6CError):
            download_phase6_sources(external_root=repo_child, offline=True)


def _write_registry(root: Path, source_id: str, url: str, md5: str) -> Path:
    registry = {
        "schema_version": "phase6c_public_source_registry_v1",
        "sources": [
            {
                "source_id": source_id,
                "dataset_family": source_id,
                "source_dataset": source_id,
                "role": "primary_ood_candidate",
                "enabled_by_default": True,
                "download_by_default": True,
                "split": "ood_final",
                "eval_gate": "use_for_eval",
                "canonical_file": "source.zip",
                "urls": [url],
                "expected_hashes": {"md5": md5},
            }
        ],
    }
    path = root / "registry.json"
    path.write_text(json.dumps(registry), encoding="utf-8")
    return path


def _write_lumos_registry(root: Path) -> Path:
    registry = {
        "schema_version": "phase6c_public_source_registry_v1",
        "sources": [
            {
                "source_id": "lumos5g",
                "dataset_family": "lumos5g",
                "source_dataset": "Lumos5G",
                "role": "optional_ood_candidate",
                "enabled_by_default": True,
                "download_by_default": True,
                "split": "ood_final",
                "eval_gate": "use_for_eval",
                "canonical_file": "Lumos5G-v1.0.zip",
                "google_drive_file_id": "fake",
                "urls": ["https://drive.google.com/uc?export=download&id=fake"],
                "expected_hashes": {},
            }
        ],
    }
    path = root / "registry.json"
    path.write_text(json.dumps(registry), encoding="utf-8")
    return path


if __name__ == "__main__":
    unittest.main()

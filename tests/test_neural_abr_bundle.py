from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core.neural_abr.bundle import (
    InvalidBundleError,
    MissingBundleFileError,
    REQUIRED_BUNDLE_FILES,
    validate_bundle_dir,
    write_bundle_manifest,
    write_json_file,
)


class NeuralAbrBundleTest(unittest.TestCase):
    def test_bundle_manifest_required_files_and_hashes_validate(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = Path(temp_dir)
            _write_minimal_payload_files(bundle_dir)
            write_bundle_manifest(bundle_dir, _manifest_metadata())

            result = validate_bundle_dir(bundle_dir)

            self.assertEqual(set(REQUIRED_BUNDLE_FILES) - {"bundle_manifest.json"}, set(result.file_records))
            self.assertTrue(result.to_json()["hashes_valid"])

    def test_hash_validation_detects_tampered_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = Path(temp_dir)
            _write_minimal_payload_files(bundle_dir)
            write_bundle_manifest(bundle_dir, _manifest_metadata())
            write_json_file(bundle_dir / "model_card.json", {"changed": True})

            with self.assertRaises(InvalidBundleError) as context:
                validate_bundle_dir(bundle_dir)

            self.assertIn("SHA256 mismatch", str(context.exception))

    def test_missing_file_produces_clear_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = Path(temp_dir)
            _write_minimal_payload_files(bundle_dir)
            (bundle_dir / "fallback_policy.json").unlink()

            with self.assertRaises(MissingBundleFileError) as context:
                validate_bundle_dir(bundle_dir)

            self.assertIn("missing bundle file", str(context.exception))
            self.assertIn("fallback_policy.json", str(context.exception))


def _write_minimal_payload_files(bundle_dir: Path) -> None:
    for filename in REQUIRED_BUNDLE_FILES:
        if filename == "bundle_manifest.json":
            continue
        if filename.endswith(".json"):
            write_json_file(bundle_dir / filename, {"name": filename})
        else:
            (bundle_dir / filename).write_bytes(b"model-state")


def _manifest_metadata():
    return {
        "created_at_utc": "2026-05-29T00:00:00Z",
        "source_run_dir": "C:/outside/run",
        "source_dataset_dir": "C:/outside/dataset",
        "source_validation_dir": "C:/outside/validation",
    }


if __name__ == "__main__":
    unittest.main()

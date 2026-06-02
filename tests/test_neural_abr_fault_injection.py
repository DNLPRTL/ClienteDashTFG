from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

import torch

from core.controller.neural_abr_lite import NeuralAbrLiteController
from core.neural_abr.bundle import read_json_file, write_bundle_manifest, write_json_file
from tests.test_neural_abr_controller import feedback
from tests.test_neural_abr_model_loading_runtime import write_runtime_bundle


class NeuralAbrFaultInjectionTest(unittest.TestCase):
    def test_valid_temp_bundle_loads_and_stays_diagnostic(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = write_runtime_bundle(Path(temp_dir) / "bundle")
            controller = NeuralAbrLiteController(bundle_dir=str(bundle_dir))
            controller.setPlayerFeedback(feedback())

            selected = controller.calcControlAction()

            self.assertIn(selected, feedback()["rates"])
            telemetry = controller.get_last_decision_telemetry()
            self.assertEqual(1, telemetry["neural_bundle_loaded"])
            self.assertEqual(1, telemetry["neural_diagnostic_only"])
            self.assertEqual("success_neural", telemetry["neural_fallback_reason"])

    def test_missing_or_nonexistent_bundle_dir_fails_closed(self):
        cases = [None, Path(tempfile.gettempdir()) / "dash_neural_missing_bundle_for_test"]
        for bundle_dir in cases:
            with self.subTest(bundle_dir=bundle_dir):
                self._assert_controller_fallback(bundle_dir, "missing_bundle_dir")

    def test_missing_required_bundle_files_fail_closed(self):
        for filename in (
            "bundle_manifest.json",
            "model_card.json",
            "feature_schema.json",
            "normalization_stats.json",
            "model_state.pt",
        ):
            with self.subTest(filename=filename):
                with tempfile.TemporaryDirectory() as temp_dir:
                    bundle_dir = write_runtime_bundle(Path(temp_dir) / "bundle")
                    (bundle_dir / filename).unlink()

                    self._assert_controller_fallback(bundle_dir, "bundle_schema_invalid")

    def test_corrupted_bundle_manifest_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = write_runtime_bundle(Path(temp_dir) / "bundle")
            (bundle_dir / "bundle_manifest.json").write_text("{not-json", encoding="utf-8")

            self._assert_controller_fallback(bundle_dir, "bundle_schema_invalid")

    def test_malformed_json_metadata_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = write_runtime_bundle(Path(temp_dir) / "bundle")
            (bundle_dir / "model_card.json").write_text("{not-json", encoding="utf-8")
            _refresh_manifest(bundle_dir)

            self._assert_controller_fallback(bundle_dir, "bundle_schema_invalid")

    def test_wrong_feature_schema_version_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = write_runtime_bundle(Path(temp_dir) / "bundle")
            schema = dict(read_json_file(bundle_dir / "feature_schema.json"))
            schema["schema_version"] = "wrong_feature_schema"
            write_json_file(bundle_dir / "feature_schema.json", schema)
            _refresh_manifest(bundle_dir)

            self._assert_controller_fallback(bundle_dir, "bundle_schema_invalid")

    def test_hash_mismatch_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = write_runtime_bundle(Path(temp_dir) / "bundle")
            model_card = dict(read_json_file(bundle_dir / "model_card.json"))
            model_card["tampered"] = True
            write_json_file(bundle_dir / "model_card.json", model_card)

            self._assert_controller_fallback(bundle_dir, "bundle_hash_invalid")

    def test_architecture_mismatch_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = write_runtime_bundle(Path(temp_dir) / "bundle")
            model_card = dict(read_json_file(bundle_dir / "model_card.json"))
            model_config = dict(model_card["model_config"])
            model_config["model_type"] = "unexpected_architecture"
            model_card["model_config"] = model_config
            write_json_file(bundle_dir / "model_card.json", model_card)
            _refresh_manifest(bundle_dir)

            self._assert_controller_fallback(bundle_dir, "bundle_schema_invalid")

    def test_torch_load_type_error_falls_back_without_unsafe_retry(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = write_runtime_bundle(Path(temp_dir) / "bundle")
            calls = []

            def unsupported_safe_load(*args, **kwargs):
                calls.append(dict(kwargs))
                raise TypeError("weights_only unsupported")

            with mock.patch.object(torch, "load", side_effect=unsupported_safe_load):
                self._assert_controller_fallback(bundle_dir, "safe_torch_load_unavailable")

            self.assertEqual(1, len(calls))
            self.assertIs(True, calls[0].get("weights_only"))
            self.assertFalse(any(call.get("weights_only") is False for call in calls))

    def test_torch_load_runtime_error_falls_back_without_crash(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = write_runtime_bundle(Path(temp_dir) / "bundle")
            calls = []

            def failing_safe_load(*args, **kwargs):
                calls.append(dict(kwargs))
                raise RuntimeError("checkpoint failure")

            with mock.patch.object(torch, "load", side_effect=failing_safe_load):
                self._assert_controller_fallback(bundle_dir, "bundle_load_failed")

            self.assertEqual(1, len(calls))
            self.assertIs(True, calls[0].get("weights_only"))

    def _assert_controller_fallback(self, bundle_dir, expected_reason):
        controller = NeuralAbrLiteController(bundle_dir=None if bundle_dir is None else str(bundle_dir))
        controller.setPlayerFeedback(feedback())

        selected = controller.calcControlAction()

        self.assertIn(selected, feedback()["rates"])
        telemetry = controller.get_last_decision_telemetry()
        self.assertEqual(1, telemetry["neural_fallback_used"])
        self.assertEqual(expected_reason, telemetry["neural_fallback_reason"])
        self.assertEqual(1, telemetry["neural_diagnostic_only"])


def _refresh_manifest(bundle_dir: Path) -> None:
    write_bundle_manifest(
        bundle_dir,
        {
            "created_at_utc": "2026-06-02T00:00:00Z",
            "source_run_dir": str(bundle_dir / "run"),
            "source_dataset_dir": str(bundle_dir / "dataset"),
            "source_validation_dir": str(bundle_dir / "validation"),
        },
    )


if __name__ == "__main__":
    unittest.main()

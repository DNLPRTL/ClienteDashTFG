from __future__ import annotations

import importlib
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import torch

from core.controller.neural_abr_lite import NeuralAbrLiteController
from core.controller.neural_abr_loader import NeuralAbrRuntimeLoadError, load_runtime_engine
from core.neural_abr.bundle import (
    BUNDLE_ACTION_SPACE,
    BUNDLE_MODEL_FAMILY,
    BUNDLE_REWARD_CONTEXT,
    BUNDLE_TEACHER,
    BUNDLE_TRAINING_METHOD,
    write_bundle_manifest,
    write_json_file,
)
from core.neural_abr.constants import (
    CANDIDATE_VECTOR_NAMES,
    CONTEXT_VECTOR_NAMES,
    NORMALIZATION_SCHEMA_VERSION,
    TRAIN_SPLIT,
)
from core.neural_abr.export import build_fallback_policy, build_inference_contract
from core.neural_abr.features import build_feature_schema
from core.neural_abr.model import NeuralAbrLiteCandidateScorer


class NeuralAbrRuntimeModelLoadingTest(unittest.TestCase):
    def test_valid_bundle_uses_safe_torch_load_cpu(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = write_runtime_bundle(Path(temp_dir))
            original_load = torch.load
            calls = []

            def safe_load_spy(*args, **kwargs):
                calls.append(dict(kwargs))
                return original_load(*args, **kwargs)

            with mock.patch.object(torch, "load", side_effect=safe_load_spy):
                engine = load_runtime_engine(bundle_dir)

            self.assertIsNotNone(engine.model)
            self.assertEqual(1, len(calls))
            self.assertEqual("cpu", calls[0]["map_location"])
            self.assertIs(True, calls[0]["weights_only"])

    def test_type_error_from_safe_load_fails_closed_without_unsafe_retry(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = write_runtime_bundle(Path(temp_dir))
            calls = []

            def unsupported_safe_load(*args, **kwargs):
                calls.append(dict(kwargs))
                raise TypeError("weights_only is unsupported")

            with mock.patch.object(torch, "load", side_effect=unsupported_safe_load):
                with self.assertRaises(NeuralAbrRuntimeLoadError) as context:
                    load_runtime_engine(bundle_dir)

            self.assertEqual("safe_torch_load_unavailable", context.exception.reason)
            self.assertEqual(1, len(calls))
            self.assertIs(True, calls[0].get("weights_only"))
            self.assertFalse(any(call.get("weights_only") is False for call in calls))

    def test_missing_bundle_config_falls_back_without_crash(self):
        controller = NeuralAbrLiteController(bundle_dir=None)
        controller.setPlayerFeedback(feedback())

        selected = controller.calcControlAction()

        self.assertIn(selected, feedback()["rates"])
        self.assertEqual("missing_bundle_dir", controller.get_last_decision_telemetry()["neural_fallback_reason"])

    def test_hash_mismatch_falls_back_without_crash(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = write_runtime_bundle(Path(temp_dir))
            write_json_file(bundle_dir / "model_card.json", {"tampered": True})

            controller = NeuralAbrLiteController(bundle_dir=str(bundle_dir))
            controller.setPlayerFeedback(feedback())
            selected = controller.calcControlAction()

            self.assertIn(selected, feedback()["rates"])
            telemetry = controller.get_last_decision_telemetry()
            self.assertEqual("bundle_hash_invalid", telemetry["neural_fallback_reason"])
            self.assertEqual(0, telemetry["neural_bundle_hash_ok"])

    def test_schema_mismatch_or_missing_file_falls_back_without_crash(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = write_runtime_bundle(Path(temp_dir))
            (bundle_dir / "feature_schema.json").unlink()

            controller = NeuralAbrLiteController(bundle_dir=str(bundle_dir))
            controller.setPlayerFeedback(feedback())
            selected = controller.calcControlAction()

            self.assertIn(selected, feedback()["rates"])
            self.assertEqual("bundle_schema_invalid", controller.get_last_decision_telemetry()["neural_fallback_reason"])

    def test_torch_unavailable_simulation_falls_back_and_registry_import_is_safe(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = write_runtime_bundle(Path(temp_dir))
            import core.controller.neural_abr_loader as runtime_loader

            original_import_module = importlib.import_module

            def fake_import_module(name, package=None):
                if name == "torch":
                    raise ModuleNotFoundError("torch unavailable")
                return original_import_module(name, package)

            with mock.patch.object(runtime_loader.importlib, "import_module", side_effect=fake_import_module):
                controller = NeuralAbrLiteController(bundle_dir=str(bundle_dir))

            controller.setPlayerFeedback(feedback())
            selected = controller.calcControlAction()

            self.assertIn(selected, feedback()["rates"])
            self.assertEqual("torch_unavailable", controller.get_last_decision_telemetry()["neural_fallback_reason"])


def write_runtime_bundle(bundle_dir: Path) -> Path:
    bundle_dir.mkdir(parents=True, exist_ok=True)
    model = NeuralAbrLiteCandidateScorer()
    model_config = dict(model.config())
    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "model_config": model_config,
            "seed": 123,
        },
        bundle_dir / "model_state.pt",
    )
    write_json_file(
        bundle_dir / "model_card.json",
        {
            "schema_version": "neural_abr_lite_phase4f_model_card_v1",
            "phase": "phase4f",
            "model_family": BUNDLE_MODEL_FAMILY,
            "training_method": BUNDLE_TRAINING_METHOD,
            "teacher": BUNDLE_TEACHER,
            "action_space": BUNDLE_ACTION_SPACE,
            "reward_context": BUNDLE_REWARD_CONTEXT,
            "model_config": model_config,
            "device": "cpu",
        },
    )
    write_json_file(bundle_dir / "feature_schema.json", build_feature_schema())
    write_json_file(
        bundle_dir / "normalization_stats.json",
        {
            "schema_version": NORMALIZATION_SCHEMA_VERSION,
            "fitted_on_split": TRAIN_SPLIT,
            "feature_names": list(CONTEXT_VECTOR_NAMES) + list(CANDIDATE_VECTOR_NAMES),
            "mean": [0.0 for _ in range(len(CONTEXT_VECTOR_NAMES) + len(CANDIDATE_VECTOR_NAMES))],
            "std": [1.0 for _ in range(len(CONTEXT_VECTOR_NAMES) + len(CANDIDATE_VECTOR_NAMES))],
            "sample_count": 1,
            "candidate_row_count": 3,
        },
    )
    write_json_file(
        bundle_dir / "ladder_schema.json",
        {
            "schema_version": "neural_abr_lite_ladder_schema_v1",
            "phase": "phase4f",
            "action_space": BUNDLE_ACTION_SPACE,
            "representation_index_policy": "contiguous_zero_based_indices",
        },
    )
    write_json_file(bundle_dir / "inference_contract.json", build_inference_contract())
    write_json_file(bundle_dir / "fallback_policy.json", build_fallback_policy())
    write_bundle_manifest(
        bundle_dir,
        {
            "created_at_utc": "2026-06-02T00:00:00Z",
            "source_run_dir": str(bundle_dir / "run"),
            "source_dataset_dir": str(bundle_dir / "dataset"),
            "source_validation_dir": str(bundle_dir / "validation"),
        },
    )
    return bundle_dir


def feedback():
    return {
        "queued_bytes": 0,
        "queued_time": 8.0,
        "cur_bitrate": 100.0,
        "bwe": 500.0,
        "level": 0,
        "max_level": 2,
        "cur_rate": 100.0,
        "max_rate": 300.0,
        "min_rate": 100.0,
        "max_bitrate": 300.0,
        "min_bitrate": 100.0,
        "last_fragment_size": 1000,
        "last_download_time": 2.0,
        "downloaded_bytes": 1000,
        "fragment_duration": 2.0,
        "rates": [100.0, 200.0, 300.0],
        "segment_index": 1,
        "start_segment_request": 1.0,
        "stop_segment_request": 3.0,
    }


if __name__ == "__main__":
    unittest.main()

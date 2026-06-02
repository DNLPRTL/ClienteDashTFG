from __future__ import annotations

import math
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from core.controller.neural_abr_diagnostics import DIAGNOSTIC_KEYS
from core.controller.neural_abr_lite import NeuralAbrLiteController
from tests.test_neural_abr_model_loading_runtime import write_runtime_bundle


class NeuralAbrControllerTest(unittest.TestCase):
    def test_valid_temp_bundle_feedback_returns_rate_from_ladder(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            controller = NeuralAbrLiteController(bundle_dir=str(write_runtime_bundle(Path(temp_dir))))
            controller.setPlayerFeedback(feedback())

            selected = controller.calcControlAction()

            self.assertIn(selected, feedback()["rates"])
            self.assertEqual(selected, controller.getControlAction())

    def test_same_input_and_bundle_are_deterministic(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = write_runtime_bundle(Path(temp_dir))
            controller = NeuralAbrLiteController(bundle_dir=str(bundle_dir))
            fb = feedback()
            controller.setPlayerFeedback(fb)
            first = controller.calcControlAction()
            controller.setPlayerFeedback(dict(fb))
            second = controller.calcControlAction()

            self.assertEqual(first, second)

    def test_nan_or_inf_score_falls_back(self):
        controller = controller_with_engine(_FakeEngine(scores=[0.0, math.nan, 1.0], raw_action=1))
        controller.setPlayerFeedback(feedback())

        selected = controller.calcControlAction()

        self.assertIn(selected, feedback()["rates"])
        telemetry = controller.get_last_decision_telemetry()
        self.assertEqual("non_finite_scores", telemetry["neural_fallback_reason"])
        self.assertEqual(1, telemetry["neural_nan_inf_detected"])

    def test_selected_masked_action_falls_back(self):
        controller = controller_with_engine(_FakeEngine(scores=[0.0, 1.0, 2.0], raw_action=2))
        fb = feedback(max_level=1)
        controller.setPlayerFeedback(fb)

        selected = controller.calcControlAction()

        self.assertIn(selected, fb["rates"])
        telemetry = controller.get_last_decision_telemetry()
        self.assertEqual("selected_masked_action", telemetry["neural_fallback_reason"])
        self.assertEqual(1, telemetry["neural_invalid_action_detected"])

    def test_all_false_or_invalid_action_mask_falls_back(self):
        controller = controller_with_engine(_FakeEngine(scores=[1.0], raw_action=0))
        controller.setPlayerFeedback(feedback(max_level=-1))

        selected = controller.calcControlAction()

        self.assertEqual(0.0, selected)
        self.assertEqual("all_actions_invalid", controller.get_last_decision_telemetry()["neural_fallback_reason"])

    def test_missing_required_feature_falls_back(self):
        controller = controller_with_engine(_FakeEngine(scores=[1.0, 2.0, 3.0], raw_action=1))
        fb = feedback()
        del fb["queued_time"]
        controller.setPlayerFeedback(fb)

        selected = controller.calcControlAction()

        self.assertIn(selected, fb["rates"])
        self.assertEqual("missing_required_feature", controller.get_last_decision_telemetry()["neural_fallback_reason"])

    def test_diagnostics_include_required_keys_and_are_diagnostic_only(self):
        controller = NeuralAbrLiteController(bundle_dir=None)
        controller.setPlayerFeedback(feedback())
        controller.calcControlAction()

        telemetry = controller.get_last_decision_telemetry()

        self.assertEqual(set(DIAGNOSTIC_KEYS), set(telemetry))
        self.assertEqual(1, telemetry["neural_diagnostic_only"])

    def test_controller_never_returns_arbitrary_rate_when_ladder_is_valid(self):
        controller = controller_with_engine(_FakeEngine(scores=[0.0, 10.0, 1.0], raw_action=1))
        fb = feedback()
        controller.setPlayerFeedback(fb)

        selected = controller.calcControlAction()

        self.assertIn(selected, fb["rates"])


class _FakeEngine:
    def __init__(self, scores, raw_action, latency_ms=0.1):
        self._scores = scores
        self._raw_action = raw_action
        self._latency_ms = latency_ms

    def score(self, context, candidates, action_mask):
        return SimpleNamespace(scores=tuple(self._scores), raw_action=self._raw_action, latency_ms=self._latency_ms)


def controller_with_engine(engine):
    controller = NeuralAbrLiteController(bundle_dir=None)
    controller._engine = engine
    controller._neural_active = True
    controller._load_reason = "success_neural"
    controller._base_telemetry.update(
        {
            "neural_enabled": 1,
            "neural_bundle_loaded": 1,
            "neural_bundle_schema_ok": 1,
            "neural_bundle_hash_ok": 1,
            "neural_feature_schema_ok": 1,
            "neural_fallback_reason": "success_neural",
        }
    )
    return controller


def feedback(**overrides):
    data = {
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
    data.update(overrides)
    return data


if __name__ == "__main__":
    unittest.main()

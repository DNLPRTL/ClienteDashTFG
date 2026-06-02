from __future__ import annotations

import unittest
from types import SimpleNamespace
from unittest import mock

from core.controller.neural_abr_lite import NeuralAbrLiteController
from core.controller.neural_abr_runtime_features import (
    RuntimeFeatureError,
    build_action_mask_from_feedback,
    build_runtime_sample,
    feedback_throughput_sample_Bps,
)
from core.controller.neural_abr_safety import apply_safety_guard
from tests.test_neural_abr_controller import controller_with_engine, feedback


class NeuralAbrHardeningTest(unittest.TestCase):
    def test_missing_and_empty_rates_fail_closed(self):
        cases = [
            ("missing_required_feature", _without(feedback(), "rates")),
            ("all_actions_invalid", feedback(rates=[])),
        ]
        for expected_reason, fb in cases:
            with self.subTest(expected_reason=expected_reason):
                controller = controller_with_engine(_FakeEngine(scores=[1.0], raw_action=0))
                controller.setPlayerFeedback(fb)

                selected = controller.calcControlAction()

                self.assertEqual(0.0, selected)
                telemetry = controller.get_last_decision_telemetry()
                self.assertEqual(expected_reason, telemetry["neural_fallback_reason"])
                self.assertEqual(1, telemetry["neural_fallback_used"])

    def test_invalid_rates_are_masked_for_action_mask_and_fail_closed_in_controller(self):
        fb = feedback(rates=[100.0, 0.0, 300.0], max_level=2)

        self.assertEqual((True, False, True), build_action_mask_from_feedback(fb))

        controller = controller_with_engine(_FakeEngine(scores=[1.0, 2.0, 3.0], raw_action=2))
        controller.setPlayerFeedback(fb)
        selected = controller.calcControlAction()

        self.assertEqual(0.0, selected)
        self.assertEqual("action_mask_invalid", controller.get_last_decision_telemetry()["neural_fallback_reason"])

    def test_max_level_edges_are_safe(self):
        self.assertEqual((True, True, True), build_action_mask_from_feedback(feedback(max_level=99)))

        controller = controller_with_engine(_FakeEngine(scores=[1.0, 2.0, 3.0], raw_action=0))
        controller.setPlayerFeedback(feedback(max_level=-1))

        selected = controller.calcControlAction()

        self.assertEqual(0.0, selected)
        self.assertEqual("all_actions_invalid", controller.get_last_decision_telemetry()["neural_fallback_reason"])

    def test_level_missing_falls_back_and_out_of_bounds_level_clamps_in_features(self):
        controller = controller_with_engine(_FakeEngine(scores=[1.0, 2.0, 3.0], raw_action=1))
        controller.setPlayerFeedback(_without(feedback(), "level"))

        selected = controller.calcControlAction()

        self.assertIn(selected, feedback()["rates"])
        self.assertEqual("missing_required_feature", controller.get_last_decision_telemetry()["neural_fallback_reason"])

        sample = build_runtime_sample(feedback(level=99))
        self.assertEqual(2.0, sample.context["last_representation_index"])

    def test_queued_time_missing_or_non_numeric_falls_back(self):
        cases = [_without(feedback(), "queued_time"), feedback(queued_time="not-a-number")]
        for fb in cases:
            with self.subTest(fb=fb):
                controller = controller_with_engine(_FakeEngine(scores=[1.0, 2.0, 3.0], raw_action=1))
                controller.setPlayerFeedback(fb)

                selected = controller.calcControlAction()

                self.assertIn(selected, feedback()["rates"])
                self.assertEqual("missing_required_feature", controller.get_last_decision_telemetry()["neural_fallback_reason"])

    def test_download_sample_missing_or_zero_is_ignored_without_division_by_zero(self):
        self.assertIsNone(feedback_throughput_sample_Bps(feedback(last_download_time=0.0)))
        self.assertIsNone(feedback_throughput_sample_Bps(_without(feedback(), "last_fragment_size")))

        sample = build_runtime_sample(feedback(last_download_time=0.0))

        self.assertEqual(0.0, sample.context["throughput_history_bps"][-1])

    def test_missing_fragment_duration_falls_back(self):
        controller = controller_with_engine(_FakeEngine(scores=[1.0, 2.0, 3.0], raw_action=1))
        controller.setPlayerFeedback(_without(feedback(), "fragment_duration"))

        selected = controller.calcControlAction()

        self.assertIn(selected, feedback()["rates"])
        self.assertEqual("missing_required_feature", controller.get_last_decision_telemetry()["neural_fallback_reason"])

    def test_single_representation_selects_only_representation(self):
        controller = NeuralAbrLiteController(bundle_dir=None)
        controller.setPlayerFeedback(feedback(rates=[123.0], max_level=0, level=0))

        selected = controller.calcControlAction()

        telemetry = controller.get_last_decision_telemetry()
        self.assertEqual(123.0, selected)
        self.assertEqual(0, telemetry["neural_safe_action"])
        self.assertEqual("single_representation", telemetry["neural_fallback_reason"])

    def test_forbidden_model_input_fields_are_rejected(self):
        with self.assertRaises(RuntimeFeatureError) as context:
            build_runtime_sample(feedback(future_throughput_bps=123.0))

        self.assertEqual("feature_build_failed", context.exception.reason)

    def test_selected_action_outside_ladder_falls_back(self):
        controller = controller_with_engine(_FakeEngine(scores=[1.0, 2.0, 3.0], raw_action=99))
        controller.setPlayerFeedback(feedback())

        selected = controller.calcControlAction()

        self.assertIn(selected, feedback()["rates"])
        telemetry = controller.get_last_decision_telemetry()
        self.assertEqual("selected_masked_action", telemetry["neural_fallback_reason"])
        self.assertEqual(1, telemetry["neural_invalid_action_detected"])

    def test_empty_or_mismatched_scores_fall_back(self):
        cases = [
            [],
            [1.0, 2.0],
            [1.0, 2.0, 3.0, 4.0],
        ]
        for scores in cases:
            with self.subTest(scores=scores):
                controller = controller_with_engine(_FakeEngine(scores=scores, raw_action=0))
                controller.setPlayerFeedback(feedback())

                selected = controller.calcControlAction()

                self.assertIn(selected, feedback()["rates"])
                self.assertEqual("inference_failed", controller.get_last_decision_telemetry()["neural_fallback_reason"])

    def test_inference_exception_and_timeout_fall_back(self):
        controller = controller_with_engine(_ExplodingEngine())
        controller.setPlayerFeedback(feedback())

        selected = controller.calcControlAction()

        self.assertIn(selected, feedback()["rates"])
        self.assertEqual("inference_failed", controller.get_last_decision_telemetry()["neural_fallback_reason"])

        timeout_controller = controller_with_engine(_FakeEngine(scores=[1.0, 2.0, 3.0], raw_action=1, latency_ms=99.0))
        timeout_controller.inference_timeout_ms = 1.0
        timeout_controller.setPlayerFeedback(feedback())

        selected = timeout_controller.calcControlAction()

        self.assertIn(selected, feedback()["rates"])
        self.assertEqual("inference_timeout", timeout_controller.get_last_decision_telemetry()["neural_fallback_reason"])

    def test_non_finite_safety_estimate_requests_fallback(self):
        decision = apply_safety_guard(
            raw_action=0,
            rates_Bps=[1.0e308],
            action_mask=[True],
            feedback=feedback(queued_time=1.0e308, fragment_duration=1.0e308),
            throughput_history_Bps=[1.0e-308],
        )

        self.assertTrue(decision.fallback_required)
        self.assertEqual("safety_guard_rejected", decision.reason)

    def test_fallback_controller_failure_executes_lowest_valid_representation(self):
        controller = NeuralAbrLiteController(bundle_dir=None)
        controller.setPlayerFeedback(feedback())

        with mock.patch("core.controller.neural_abr_safety._create_fallback_controller", side_effect=RuntimeError("fail")):
            selected = controller.calcControlAction()

        telemetry = controller.get_last_decision_telemetry()
        self.assertEqual(100.0, selected)
        self.assertEqual(0, telemetry["neural_safe_action"])
        self.assertEqual("fallback_controller_failed", telemetry["neural_fallback_reason"])
        self.assertEqual(1, telemetry["neural_fallback_used"])


class _FakeEngine:
    def __init__(self, scores, raw_action, latency_ms=0.1):
        self._scores = scores
        self._raw_action = raw_action
        self._latency_ms = latency_ms

    def score(self, context, candidates, action_mask):
        return SimpleNamespace(scores=tuple(self._scores), raw_action=self._raw_action, latency_ms=self._latency_ms)


class _ExplodingEngine:
    def score(self, context, candidates, action_mask):
        raise RuntimeError("inference exploded")


def _without(data, key):
    copied = dict(data)
    copied.pop(key, None)
    return copied


if __name__ == "__main__":
    unittest.main()

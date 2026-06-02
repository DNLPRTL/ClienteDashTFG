from __future__ import annotations

import unittest
from pathlib import Path

from core.controller.neural_abr_diagnostics import (
    DIAGNOSTIC_KEYS,
    FALLBACK_REASONS,
    NeuralAbrDecisionTelemetry,
)
from core.controller.neural_abr_lite import NeuralAbrLiteController
from core.controller.neural_abr_loader import NeuralAbrRuntimeError
from core.dataset_schema import build_evaluation_segments_header, build_segment_telemetry_header
from tests.test_neural_abr_controller import controller_with_engine, feedback


class NeuralAbrTelemetryHardeningTest(unittest.TestCase):
    def test_required_neural_diagnostic_columns_are_segment_only(self):
        controller = NeuralAbrLiteController(bundle_dir=None)
        augmented = controller.augment_feedback(feedback(), context={"phase": "header"})
        segment_header = build_segment_telemetry_header(list(augmented.keys()))
        evaluation_header = build_evaluation_segments_header()

        for key in DIAGNOSTIC_KEYS:
            self.assertIn("feedback_{0}".format(key), segment_header)
            self.assertNotIn("feedback_{0}".format(key), evaluation_header)
        self.assertFalse(any("neural_" in column for column in evaluation_header))

    def test_diagnostic_values_are_csv_safe_and_diagnostic_only(self):
        controller = NeuralAbrLiteController(bundle_dir=None)
        controller.setPlayerFeedback(feedback())
        controller.calcControlAction()

        telemetry = controller.get_last_decision_telemetry()

        self.assertEqual(1, telemetry["neural_diagnostic_only"])
        for key, value in telemetry.items():
            with self.subTest(key=key):
                self.assertIsInstance(value, (int, float, str))
                self.assertNotIn("\n", str(value))
                self.assertNotIn("\r", str(value))

    def test_unknown_fallback_reason_is_sanitized_to_stable_label(self):
        controller = controller_with_engine(_UnknownReasonEngine())
        controller.setPlayerFeedback(feedback())

        selected = controller.calcControlAction()

        self.assertIn(selected, feedback()["rates"])
        reason = controller.get_last_decision_telemetry()["neural_fallback_reason"]
        self.assertEqual("inference_failed", reason)
        self.assertIn(reason, FALLBACK_REASONS)
        self.assertNotIn("traceback", reason.lower())
        self.assertNotIn("\n", reason)

    def test_decision_telemetry_sanitizes_strings(self):
        telemetry = NeuralAbrDecisionTelemetry.with_base(
            {
                "neural_fallback_reason": "RuntimeError: custom exception text\nwith details",
                "neural_missing_features": "queued_time\nfragment_duration",
            }
        ).to_dict()

        self.assertEqual("inference_failed", telemetry["neural_fallback_reason"])
        self.assertEqual("queued_time fragment_duration", telemetry["neural_missing_features"])

    def test_runtime_static_sources_do_not_use_unsafe_model_loading_patterns(self):
        runtime_files = [
            "core/controller/neural_abr_lite.py",
            "core/controller/neural_abr_loader.py",
            "core/controller/neural_abr_runtime_features.py",
            "core/controller/neural_abr_safety.py",
            "core/controller/neural_abr_diagnostics.py",
            "player.py",
        ]
        forbidden_patterns = (
            "weights_only=False",
            "torch.hub",
            "http://",
            "https://",
            "urlopen",
            "requests",
        )

        for path in runtime_files:
            with self.subTest(path=path):
                text = Path(path).read_text(encoding="utf-8")
                for pattern in forbidden_patterns:
                    self.assertNotIn(pattern, text)

    def test_no_benchmark_ranking_or_improvement_columns_are_added(self):
        controller = NeuralAbrLiteController(bundle_dir=None)
        augmented = controller.augment_feedback(feedback(), context={"phase": "header"})
        headers = build_segment_telemetry_header(list(augmented.keys())) + build_evaluation_segments_header()
        forbidden_terms = ("rank", "winner", "improvement", "p_value", "p-value")

        self.assertFalse(
            any(any(term in column.lower() for term in forbidden_terms) for column in headers)
        )


class _UnknownReasonEngine:
    def score(self, context, candidates, action_mask):
        raise NeuralAbrRuntimeError("RuntimeError: custom exception text\ntraceback follows")


if __name__ == "__main__":
    unittest.main()

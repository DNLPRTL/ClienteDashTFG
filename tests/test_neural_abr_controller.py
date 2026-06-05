from __future__ import annotations

import tempfile
import unittest

from core.controller.neural_abr_loader import NeuralAbrRuntimeBundleError
from core.controller.registry import create_controller
from tests.neural_abr_bundle_utils import build_minimal_phase4_bundle, minimal_feedback


class NeuralAbrControllerTest(unittest.TestCase):
    def test_missing_bundle_falls_back_to_classical_controller(self):
        controller = create_controller("neural_abr_lite_robust_mpc")
        feedback = controller.augment_feedback(minimal_feedback())
        controller.setPlayerFeedback(feedback)

        selected_rate = controller.calcControlAction()
        diagnostics = controller.get_neural_diagnostics()

        self.assertIn(selected_rate, feedback["rates"])
        self.assertEqual(1, diagnostics["neural_fallback_used"])
        self.assertEqual("missing_bundle_dir", diagnostics["neural_fallback_reason"])
        self.assertEqual(1, diagnostics["neural_valid_action"])

    def test_valid_bundle_scores_without_fallback(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = build_minimal_phase4_bundle(temp_dir, teacher="robust_mpc")
            controller = create_controller(
                "neural_abr_lite_robust_mpc",
                {"bundle_dir": str(bundle_dir), "max_inference_latency_ms": 1000.0},
            )
            feedback = controller.augment_feedback(minimal_feedback())
            controller.setPlayerFeedback(feedback)

            selected_rate = controller.calcControlAction()
            diagnostics = controller.get_neural_diagnostics()

            self.assertIn(selected_rate, feedback["rates"])
            self.assertEqual(0, diagnostics["neural_fallback_used"])
            self.assertEqual("success_neural", diagnostics["neural_fallback_reason"])
            self.assertEqual(1, diagnostics["neural_bundle_loaded"])
            self.assertEqual(1, diagnostics["neural_valid_action"])

    def test_teacher_hibrido_controller_requires_hybrid_bundle(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = build_minimal_phase4_bundle(temp_dir, teacher="teacher_hibrido")
            controller = create_controller(
                "neural_abr_lite_teacher_hibrido",
                {"bundle_dir": str(bundle_dir), "max_inference_latency_ms": 1000.0},
            )
            feedback = controller.augment_feedback(minimal_feedback())
            controller.setPlayerFeedback(feedback)

            selected_rate = controller.calcControlAction()
            diagnostics = controller.get_neural_diagnostics()

            self.assertIn(selected_rate, feedback["rates"])
            self.assertEqual("NeuralABR-Lite teacher_hibrido", diagnostics["neural_model_label"])
            self.assertEqual(0, diagnostics["neural_fallback_used"])

    def test_nan_scores_fall_back_with_stable_diagnostics(self):
        class BrokenBundle:
            def score(self, *_args, **_kwargs):
                raise NeuralAbrRuntimeBundleError("nan_inf_scores", "nan")

        controller = create_controller("neural_abr_lite_robust_mpc")
        controller._bundle = BrokenBundle()
        feedback = controller.augment_feedback(minimal_feedback())
        controller.setPlayerFeedback(feedback)

        selected_rate = controller.calcControlAction()
        diagnostics = controller.get_neural_diagnostics()

        self.assertIn(selected_rate, feedback["rates"])
        self.assertEqual(1, diagnostics["neural_fallback_used"])
        self.assertEqual("inference_failed", diagnostics["neural_fallback_reason"])
        self.assertEqual(1, diagnostics["neural_nan_inf_detected"])

    def test_single_representation_is_safe_without_bundle(self):
        controller = create_controller("neural_abr_lite_robust_mpc")
        feedback = minimal_feedback()
        feedback["rates"] = [37500.0]
        feedback["max_level"] = 0
        feedback["max_rate"] = 37500.0
        feedback["max_bitrate"] = 37500.0
        feedback = controller.augment_feedback(feedback)
        controller.setPlayerFeedback(feedback)

        selected_rate = controller.calcControlAction()
        diagnostics = controller.get_neural_diagnostics()

        self.assertEqual(37500.0, selected_rate)
        self.assertEqual(0, diagnostics["neural_fallback_used"])
        self.assertEqual("single_representation", diagnostics["neural_fallback_reason"])


if __name__ == "__main__":
    unittest.main()


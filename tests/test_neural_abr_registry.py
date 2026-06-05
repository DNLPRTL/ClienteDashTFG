from __future__ import annotations

import unittest

from core.controller.neural_abr_lite import NeuralAbrLiteRobustMpcController, NeuralAbrLiteTeacherHibridoController
from core.controller.registry import CONTROLLER_REGISTRY, available_controllers, create_controller


class NeuralAbrRegistryTest(unittest.TestCase):
    def test_two_phase5_neural_controllers_are_registered(self):
        available = {spec.key for spec in available_controllers()}
        self.assertIn("neural_abr_lite_robust_mpc", CONTROLLER_REGISTRY)
        self.assertIn("neural_abr_lite_teacher_hibrido", CONTROLLER_REGISTRY)
        self.assertIn("neural_abr_lite_robust_mpc", available)
        self.assertIn("neural_abr_lite_teacher_hibrido", available)

        self.assertIsInstance(create_controller("neural_abr_lite_robust_mpc"), NeuralAbrLiteRobustMpcController)
        self.assertIsInstance(create_controller("neural_abr_lite_teacher_hibrido"), NeuralAbrLiteTeacherHibridoController)

    def test_neural_controllers_expose_current_controller_api(self):
        for name in ("neural_abr_lite_robust_mpc", "neural_abr_lite_teacher_hibrido"):
            with self.subTest(controller=name):
                controller = create_controller(name)
                self.assertTrue(callable(controller.setPlayerFeedback))
                self.assertTrue(callable(controller.calcControlAction))
                self.assertTrue(callable(controller.getControlAction))
                self.assertTrue(callable(controller.quantizeRate))
                self.assertTrue(callable(controller.augment_feedback))
                self.assertTrue(callable(controller.get_neural_diagnostics))


if __name__ == "__main__":
    unittest.main()


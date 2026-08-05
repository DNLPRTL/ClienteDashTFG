from __future__ import annotations

import unittest

from core.controller.phase45_v3_neural_mpc import DEFAULT_NEURAL_MPC_V2_BUNDLE_DIR
from core.controller.registry import create_controller
from core.phase45_v3.neural_mpc_controller import NEURAL_MPC_V2_CONTROLLER_KEY
from core.fase6.catalogo import descubrir_controllers_comparables


class Phase45V3NeuralMpcV2ControllerTest(unittest.TestCase):
    def test_v2_controller_is_registered_and_phase6_visible(self) -> None:
        controller = create_controller(NEURAL_MPC_V2_CONTROLLER_KEY)
        discovered = {item["controller_key"]: item for item in descubrir_controllers_comparables({})}

        self.assertEqual(NEURAL_MPC_V2_CONTROLLER_KEY, controller.controller_key)
        self.assertEqual(DEFAULT_NEURAL_MPC_V2_BUNDLE_DIR, controller.bundle_dir)
        self.assertIn(NEURAL_MPC_V2_CONTROLLER_KEY, discovered)
        self.assertEqual("Propio Neural-MPC v2", discovered[NEURAL_MPC_V2_CONTROLLER_KEY]["display_name"])


if __name__ == "__main__":
    unittest.main()

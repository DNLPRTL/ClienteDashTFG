from __future__ import annotations

import unittest


class NeuralAbrRegistryTest(unittest.TestCase):
    def test_registry_imports_and_exposes_neural_abr_lite(self):
        from core.controller.registry import CONTROLLER_REGISTRY, available_controllers, create_controller

        self.assertIn("neural_abr_lite", CONTROLLER_REGISTRY)
        self.assertIn("neural_abr_lite", {spec.key for spec in available_controllers()})
        self.assertEqual(
            "NeuralABR-Lite guarded scorer controller",
            CONTROLLER_REGISTRY["neural_abr_lite"].label,
        )

        controller = create_controller("neural_abr_lite", {})

        self.assertEqual("neural_abr_lite", controller.name)
        self.assertTrue(callable(controller.setPlayerFeedback))
        self.assertTrue(callable(controller.calcControlAction))
        self.assertTrue(callable(controller.getControlAction))
        self.assertTrue(callable(controller.quantizeRate))
        self.assertTrue(callable(controller.getIdleDuration))

    def test_default_no_bundle_controller_does_not_crash(self):
        from core.controller.registry import create_controller

        controller = create_controller("neural_abr_lite", {})
        controller.setPlayerFeedback(_feedback())

        selected = controller.calcControlAction()

        self.assertIn(selected, _feedback()["rates"])
        telemetry = controller.get_last_decision_telemetry()
        self.assertEqual("missing_bundle_dir", telemetry["neural_fallback_reason"])
        self.assertEqual(1, telemetry["neural_fallback_used"])
        self.assertEqual(1, telemetry["neural_diagnostic_only"])


def _feedback():
    return {
        "queued_bytes": 0,
        "queued_time": 4.0,
        "cur_bitrate": 100.0,
        "bwe": 100.0,
        "level": 0,
        "max_level": 2,
        "cur_rate": 100.0,
        "max_rate": 300.0,
        "min_rate": 100.0,
        "max_bitrate": 300.0,
        "min_bitrate": 100.0,
        "last_fragment_size": 400,
        "last_download_time": 2.0,
        "downloaded_bytes": 400,
        "fragment_duration": 2.0,
        "rates": [100.0, 200.0, 300.0],
        "segment_index": 1,
        "start_segment_request": 1.0,
        "stop_segment_request": 2.0,
    }


if __name__ == "__main__":
    unittest.main()

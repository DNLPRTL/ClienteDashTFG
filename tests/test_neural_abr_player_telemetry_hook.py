from __future__ import annotations

import unittest

from core.controller.neural_abr_diagnostics import DIAGNOSTIC_KEYS
from core.controller.neural_abr_lite import NeuralAbrLiteController
from core.dataset_schema import build_evaluation_segments_header, build_segment_telemetry_header
from player import Player
from tests.test_neural_abr_controller import feedback


class NeuralAbrPlayerTelemetryHookTest(unittest.TestCase):
    def test_existing_non_neural_controller_behavior_unchanged(self):
        player = _player(_PlainController())
        header = build_segment_telemetry_header(list(feedback().keys()))
        row = ["" for _ in range(len(header) - 2)]
        player._pending_rows = {1: row}
        player._header = header
        player._col_index = {name: index for index, name in enumerate(header)}

        player._update_pending_policy_and_switch(1, 200.0, 1, 0.25, 1, 0, 1)

        self.assertEqual("plain", row[player._col_index["policy_name"]])
        self.assertEqual(200.0, row[player._col_index["policy_target_rate"]])
        self.assertFalse(any(column.startswith("feedback_neural_") for column in header))

    def test_neural_diagnostic_keys_are_added_to_segment_header_by_augment_feedback(self):
        controller = NeuralAbrLiteController(bundle_dir=None)
        augmented = controller.augment_feedback(feedback(), context={"phase": "header"})
        header = build_segment_telemetry_header(list(augmented.keys()))

        for key in DIAGNOSTIC_KEYS:
            self.assertIn("feedback_{0}".format(key), header)

    def test_post_decision_hook_updates_existing_neural_feedback_columns(self):
        controller = _TelemetryController()
        player = _player(controller)
        keys = list(feedback().keys()) + list(DIAGNOSTIC_KEYS)
        header = build_segment_telemetry_header(keys)
        row = ["" for _ in range(len(header) - 2)]
        player._pending_rows = {1: row}
        player._header = header
        player._col_index = {name: index for index, name in enumerate(header)}

        player._update_pending_policy_and_switch(1, 300.0, 2, 1.5, 1, 0, 2)

        self.assertEqual(2, row[player._col_index["feedback_neural_raw_action"]])
        self.assertEqual(1, row[player._col_index["feedback_neural_safe_action"]])
        self.assertEqual(1, row[player._col_index["feedback_neural_fallback_used"]])
        self.assertEqual("safety_guard_rejected", row[player._col_index["feedback_neural_fallback_reason"]])
        self.assertEqual(1, row[player._col_index["feedback_neural_diagnostic_only"]])

    def test_evaluation_segments_header_remains_without_neural_fields(self):
        header = build_evaluation_segments_header()

        self.assertFalse(any("neural_" in column for column in header))

    def test_hook_exceptions_do_not_crash_player_update(self):
        player = _player(_BrokenTelemetryController())
        keys = list(feedback().keys()) + list(DIAGNOSTIC_KEYS)
        header = build_segment_telemetry_header(keys)
        row = ["" for _ in range(len(header) - 2)]
        player._pending_rows = {1: row}
        player._header = header
        player._col_index = {name: index for index, name in enumerate(header)}

        player._update_pending_policy_and_switch(1, 100.0, 0, 0.1, 0, 0, 0)

        self.assertEqual(100.0, row[player._col_index["policy_target_rate"]])


class _PlainController:
    name = "plain"


class _TelemetryController:
    name = "neural_abr_lite"

    def get_last_decision_telemetry(self):
        return {
            "neural_raw_action": 2,
            "neural_safe_action": 1,
            "neural_fallback_used": 1,
            "neural_fallback_reason": "safety_guard_rejected",
            "neural_diagnostic_only": 1,
        }


class _BrokenTelemetryController:
    name = "broken"

    def get_last_decision_telemetry(self):
        raise RuntimeError("hook failure")


def _player(controller):
    return Player(
        parser=None,
        media_engine=None,
        mpd_url="memory://telemetry.mpd",
        downloader=None,
        controller=controller,
    )


if __name__ == "__main__":
    unittest.main()

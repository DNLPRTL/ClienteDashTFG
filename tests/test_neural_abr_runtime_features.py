from __future__ import annotations

import unittest

from core.controller.neural_abr_runtime_features import NeuralAbrRuntimeFeatureBuilder, RuntimeFeatureError
from core.neural_abr.constants import DEFAULT_CONTEXT_HISTORY_LENGTH
from tests.neural_abr_bundle_utils import minimal_feedback


class NeuralAbrRuntimeFeatureTest(unittest.TestCase):
    def test_builds_phase4_shaped_runtime_features_from_feedback(self):
        builder = NeuralAbrRuntimeFeatureBuilder()
        payload = builder.build(minimal_feedback())

        self.assertEqual(DEFAULT_CONTEXT_HISTORY_LENGTH, len(payload.context_features["throughput_history_bps"]))
        self.assertEqual(DEFAULT_CONTEXT_HISTORY_LENGTH, len(payload.context_features["download_time_history_s"]))
        self.assertEqual(2, len(payload.candidate_features))
        self.assertEqual((True, True), payload.action_mask)
        self.assertEqual(2, payload.valid_action_count)
        self.assertEqual(64000.0, payload.context_features["throughput_history_bps"][-1])
        self.assertEqual(300000.0, payload.candidate_features[0]["candidate_bitrate_bps"])
        self.assertEqual(150000.0, payload.candidate_features[0]["candidate_chunk_size_bytes"])
        self.assertEqual(1.0, payload.candidate_features[0]["candidate_chunk_size_available"])

    def test_action_mask_obeys_max_level(self):
        builder = NeuralAbrRuntimeFeatureBuilder()
        feedback = minimal_feedback()
        feedback["max_level"] = 0
        payload = builder.build(feedback)

        self.assertEqual((True, False), payload.action_mask)
        self.assertEqual(1, payload.valid_action_count)

    def test_rejects_forbidden_runtime_feedback_fields(self):
        builder = NeuralAbrRuntimeFeatureBuilder()
        feedback = minimal_feedback()
        feedback["trace_id"] = "must-not-reach-model"

        with self.assertRaises(RuntimeFeatureError) as ctx:
            builder.build(feedback)

        self.assertEqual("feature_build_failed", ctx.exception.reason)

    def test_missing_required_feedback_fails_closed(self):
        builder = NeuralAbrRuntimeFeatureBuilder()
        feedback = minimal_feedback()
        del feedback["fragment_duration"]

        with self.assertRaises(RuntimeFeatureError) as ctx:
            builder.build(feedback)

        self.assertEqual("missing_required_feature", ctx.exception.reason)
        self.assertEqual(("fragment_duration",), ctx.exception.missing_features)

    def test_empty_or_all_masked_ladder_fails_closed(self):
        builder = NeuralAbrRuntimeFeatureBuilder()
        feedback = minimal_feedback()
        feedback["rates"] = []

        with self.assertRaises(RuntimeFeatureError) as ctx:
            builder.build(feedback)
        self.assertEqual("all_actions_invalid", ctx.exception.reason)

        feedback = minimal_feedback()
        feedback["max_level"] = -1
        with self.assertRaises(RuntimeFeatureError) as ctx:
            builder.build(feedback)
        self.assertEqual("all_actions_invalid", ctx.exception.reason)


if __name__ == "__main__":
    unittest.main()

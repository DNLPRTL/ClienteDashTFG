from __future__ import annotations

import unittest

from core.controller.neural_abr_runtime_features import (
    RuntimeFeatureError,
    build_action_mask_from_feedback,
    build_runtime_sample,
)
from core.neural_abr.constants import FORBIDDEN_MODEL_INPUT_KEYS


class NeuralAbrRuntimeFeaturesTest(unittest.TestCase):
    def test_feedback_maps_to_context_candidates_and_previous_download_history(self):
        sample = build_runtime_sample(feedback(), throughput_history_Bps=[250.0], download_time_history_s=[4.0])

        self.assertEqual(3, len(sample.candidates))
        self.assertEqual((True, True, True), sample.action_mask)
        self.assertEqual(8.0, sample.context["buffer_s"])
        self.assertEqual(1.0, sample.context["last_representation_index"])
        self.assertEqual(1600.0, sample.context["last_bitrate_bps"])
        self.assertEqual(2.0, sample.context["fragment_duration_s"])
        self.assertEqual(500.0, sample.throughput_history_Bps[-1])
        self.assertEqual(4000.0, sample.context["throughput_history_bps"][-1])
        self.assertEqual(2.0, sample.context["download_time_history_s"][-1])

    def test_candidate_bitrates_are_bytes_per_second_times_eight(self):
        sample = build_runtime_sample(feedback())

        self.assertEqual(800.0, sample.candidates[0]["candidate_bitrate_bps"])
        self.assertEqual(1600.0, sample.candidates[1]["candidate_bitrate_bps"])
        self.assertEqual(2400.0, sample.candidates[2]["candidate_bitrate_bps"])
        self.assertEqual(0.0, sample.candidates[0]["candidate_ladder_position_norm"])
        self.assertEqual(1.0, sample.candidates[2]["candidate_ladder_position_norm"])

    def test_action_mask_length_and_max_level_are_respected(self):
        fb = feedback(max_level=1)

        mask = build_action_mask_from_feedback(fb)

        self.assertEqual(3, len(mask))
        self.assertEqual((True, True, False), mask)

    def test_single_representation_runtime_sample_is_valid(self):
        sample = build_runtime_sample(feedback(rates=[100.0], max_level=0, level=0))

        self.assertEqual((True,), sample.action_mask)
        self.assertEqual(1, len(sample.candidates))

    def test_invalid_or_empty_rates_raise_feature_or_action_error(self):
        for rates in ([], [100.0, 0.0], [100.0, "bad"]):
            with self.subTest(rates=rates):
                with self.assertRaises(RuntimeFeatureError):
                    build_runtime_sample(feedback(rates=rates, max_level=len(rates) - 1))

    def test_forbidden_fields_are_not_included(self):
        sample = build_runtime_sample(feedback())
        payload_keys = set(sample.context)
        for candidate in sample.candidates:
            payload_keys.update(candidate)

        self.assertFalse(payload_keys & FORBIDDEN_MODEL_INPUT_KEYS)

    def test_estimated_candidate_chunk_size_is_marked_unavailable(self):
        sample = build_runtime_sample(feedback())

        self.assertEqual(200.0, sample.candidates[0]["candidate_chunk_size_bytes"])
        self.assertEqual(0.0, sample.candidates[0]["candidate_chunk_size_available"])

    def test_explicit_candidate_chunk_size_is_marked_available(self):
        sample = build_runtime_sample(feedback(candidate_chunk_sizes_bytes=[10, 20, 30]))

        self.assertEqual(20.0, sample.candidates[1]["candidate_chunk_size_bytes"])
        self.assertEqual(1.0, sample.candidates[1]["candidate_chunk_size_available"])


def feedback(**overrides):
    data = {
        "queued_bytes": 0,
        "queued_time": 8.0,
        "cur_bitrate": 200.0,
        "bwe": 500.0,
        "level": 1,
        "max_level": 2,
        "cur_rate": 200.0,
        "max_rate": 300.0,
        "min_rate": 100.0,
        "max_bitrate": 300.0,
        "min_bitrate": 100.0,
        "last_fragment_size": 1000,
        "last_download_time": 2.0,
        "downloaded_bytes": 1000,
        "fragment_duration": 2.0,
        "rates": [100.0, 200.0, 300.0],
        "segment_index": 3,
        "start_segment_request": 1.0,
        "stop_segment_request": 3.0,
    }
    data.update(overrides)
    return data


if __name__ == "__main__":
    unittest.main()

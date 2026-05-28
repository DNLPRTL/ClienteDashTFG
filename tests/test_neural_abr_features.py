from __future__ import annotations

import unittest

from core.neural_abr.constants import K_CONTEXT
from core.neural_abr.content_ladder import synthetic_smoke_ladder
from core.neural_abr.features import (
    FeatureError,
    build_candidate_features,
    build_context_features,
    flatten_candidate_features,
    flatten_context_features,
)
from core.neural_abr.replay_env import ReplayState


class NeuralAbrFeaturesTest(unittest.TestCase):
    def test_context_features_are_left_padded_and_flattenable(self):
        ladder = synthetic_smoke_ladder(segment_count=4)
        state = ReplayState(
            segment_index=1,
            buffer_s=3.5,
            last_representation_index=1,
            previous_representation_index=0,
            throughput_history_bps=(1_000_000.0,),
            download_time_history_s=(1.2,),
            recent_rebuffer_s=0.0,
            recent_switch_abs=1.0,
            playback_time_s=1.2,
        )

        context = build_context_features(state, ladder)
        vector = flatten_context_features(context)

        self.assertEqual(K_CONTEXT, len(context["throughput_history_bps"]))
        self.assertEqual(0.0, context["throughput_history_bps"][0])
        self.assertEqual(17, len(vector))

    def test_candidate_features_include_ladder_normalization(self):
        ladder = synthetic_smoke_ladder(segment_count=2)

        candidates = build_candidate_features(ladder, 0, last_bitrate_bps=750_000)
        vector = flatten_candidate_features(candidates[-1])

        self.assertEqual(4, len(candidates))
        self.assertEqual(7, len(vector))
        self.assertEqual(1.0, candidates[-1]["candidate_ladder_position_norm"])
        self.assertEqual(1.0, candidates[-1]["candidate_chunk_size_available"])

    def test_forbidden_inputs_are_rejected(self):
        ladder = synthetic_smoke_ladder(segment_count=2)
        candidate = dict(build_candidate_features(ladder, 0, last_bitrate_bps=0.0)[0])
        candidate["trace_id"] = 123

        with self.assertRaises(FeatureError):
            flatten_candidate_features(candidate)


if __name__ == "__main__":
    unittest.main()

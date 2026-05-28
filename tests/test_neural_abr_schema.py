from __future__ import annotations

import copy
import unittest

from core.neural_abr.action_mask import build_action_mask
from core.neural_abr.constants import DATASET_SCHEMA_VERSION, REWARD_VERSION, TRAIN_SPLIT
from core.neural_abr.content_ladder import synthetic_smoke_ladder
from core.neural_abr.features import build_candidate_features, build_context_features
from core.neural_abr.replay_env import TraceReplayEnvironment
from core.neural_abr.schemas import SchemaError, validate_sample
from core.trace_replay.loader import load_normalized_trace_rows


class NeuralAbrSchemaTest(unittest.TestCase):
    def test_sample_schema_accepts_valid_sample(self):
        sample = self.sample()

        validate_sample(sample, expected_split=TRAIN_SPLIT)

    def test_sample_schema_rejects_teacher_action_outside_mask(self):
        sample = self.sample()
        sample["label"]["teacher_action"] = 99

        with self.assertRaises(SchemaError):
            validate_sample(sample)

    def test_sample_schema_rejects_forbidden_context_input(self):
        sample = self.sample()
        sample["context"]["teacher_action"] = 1

        with self.assertRaises(SchemaError):
            validate_sample(sample)

    def sample(self):
        ladder = synthetic_smoke_ladder(segment_count=2)
        trace = load_normalized_trace_rows(
            [{"timestamp_s": "0", "duration_s": "10", "throughput_kbps": "2000"}],
            trace_id="schema-trace",
            source="schema-test",
        )
        env = TraceReplayEnvironment(trace, ladder)
        context = build_context_features(env.state, ladder)
        candidates = build_candidate_features(ladder, env.state.segment_index, 0.0)
        return {
            "schema_version": DATASET_SCHEMA_VERSION,
            "sample_id": "train:schema-trace:0",
            "split": TRAIN_SPLIT,
            "context": copy.deepcopy(dict(context)),
            "candidates": [dict(candidate) for candidate in candidates],
            "action_mask": list(build_action_mask(ladder, 0)),
            "label": {
                "teacher_action": 0,
                "teacher_policy": "robust_mpc",
                "teacher_reward_n": 0.0,
                "reward_version": REWARD_VERSION,
                "diagnostic_only": True,
            },
            "metadata": {
                "trace_id": "schema-trace",
                "split": TRAIN_SPLIT,
                "source_dataset": "unit",
                "segment_index": 0,
                "representation_count": ladder.representation_count,
            },
        }


if __name__ == "__main__":
    unittest.main()

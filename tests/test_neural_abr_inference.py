from __future__ import annotations

import math
import tempfile
import unittest
from pathlib import Path

import torch

from core.neural_abr.bundle import write_bundle_manifest, write_json_file
from core.neural_abr.constants import CANDIDATE_VECTOR_NAMES, CONTEXT_VECTOR_NAMES, NORMALIZATION_SCHEMA_VERSION, TRAIN_SPLIT
from core.neural_abr.features import build_feature_schema
from core.neural_abr.inference import InferenceError, load_neural_abr_bundle, select_candidate_position
from core.neural_abr.model import NeuralAbrLiteCandidateScorer


class NeuralAbrInferenceTest(unittest.TestCase):
    def test_inference_applies_action_mask(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = _write_inference_bundle(Path(temp_dir))
            engine = load_neural_abr_bundle(bundle_dir)
            sample = _sample(action_mask=[False, True, False])

            decision = engine.score_sample(sample)

            self.assertEqual(1, decision.selected_representation_index)
            self.assertLess(decision.scores[0], -1.0e8)

    def test_invalid_candidates_cannot_be_selected_even_with_high_score(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = _write_inference_bundle(Path(temp_dir))
            engine = load_neural_abr_bundle(bundle_dir)
            engine.model = _FixedScoreModel([100.0, 2.0, 1.0])

            decision = engine.score_sample(_sample(action_mask=[False, True, True]))

            self.assertEqual(1, decision.selected_representation_index)

    def test_nan_or_inf_scores_are_rejected(self):
        with self.assertRaises(InferenceError):
            select_candidate_position([0.0, math.nan], [True, True])
        with self.assertRaises(InferenceError):
            select_candidate_position([0.0, math.inf], [True, True])

    def test_inference_is_deterministic_for_same_input(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_dir = _write_inference_bundle(Path(temp_dir))
            engine = load_neural_abr_bundle(bundle_dir)
            sample = _sample(action_mask=[True, True, True])

            first = engine.score_sample(sample)
            second = engine.score_sample(sample)

            self.assertEqual(first.selected_representation_index, second.selected_representation_index)
            self.assertEqual(first.scores, second.scores)


class _FixedScoreModel(torch.nn.Module):
    def __init__(self, scores):
        super().__init__()
        self._scores = list(scores)

    def forward(self, context_features, candidate_features, action_mask):
        return torch.tensor([self._scores], dtype=torch.float32)


def _write_inference_bundle(bundle_dir: Path) -> Path:
    model = NeuralAbrLiteCandidateScorer()
    checkpoint = {
        "model_state_dict": model.state_dict(),
        "model_config": dict(model.config()),
        "seed": 123,
    }
    torch.save(checkpoint, bundle_dir / "model_state.pt")
    write_json_file(bundle_dir / "model_card.json", {"model_config": dict(model.config())})
    write_json_file(bundle_dir / "feature_schema.json", build_feature_schema())
    write_json_file(
        bundle_dir / "normalization_stats.json",
        {
            "schema_version": NORMALIZATION_SCHEMA_VERSION,
            "fitted_on_split": TRAIN_SPLIT,
            "feature_names": list(CONTEXT_VECTOR_NAMES) + list(CANDIDATE_VECTOR_NAMES),
            "mean": [0.0 for _ in range(len(CONTEXT_VECTOR_NAMES) + len(CANDIDATE_VECTOR_NAMES))],
            "std": [1.0 for _ in range(len(CONTEXT_VECTOR_NAMES) + len(CANDIDATE_VECTOR_NAMES))],
            "sample_count": 1,
            "candidate_row_count": 3,
        },
    )
    write_json_file(bundle_dir / "ladder_schema.json", {"representation_count": 3})
    write_json_file(bundle_dir / "inference_contract.json", {"offline_only": True})
    write_json_file(bundle_dir / "fallback_policy.json", {"future_integration_only": True})
    write_bundle_manifest(
        bundle_dir,
        {
            "created_at_utc": "2026-05-29T00:00:00Z",
            "source_run_dir": str(bundle_dir / "run"),
            "source_dataset_dir": str(bundle_dir / "dataset"),
            "source_validation_dir": str(bundle_dir / "validation"),
        },
    )
    return bundle_dir


def _sample(action_mask):
    return {
        "sample_id": "fixture:0",
        "context": {
            "throughput_history_bps": [0.0, 0.0, 0.0, 0.0, 0.0],
            "download_time_history_s": [0.0, 0.0, 0.0, 0.0, 0.0],
            "buffer_s": 0.0,
            "last_representation_index": -1.0,
            "last_bitrate_bps": 0.0,
            "recent_rebuffer_s": 0.0,
            "recent_switch_abs": 0.0,
            "chunks_remaining_norm": 1.0,
            "has_chunks_remaining": 1.0,
        },
        "candidates": [
            _candidate(0, 300000.0),
            _candidate(1, 750000.0),
            _candidate(2, 1200000.0),
        ],
        "action_mask": action_mask,
    }


def _candidate(index: int, bitrate_bps: float):
    return {
        "candidate_representation_index": float(index),
        "candidate_ladder_position_norm": float(index) / 2.0,
        "candidate_bitrate_bps": bitrate_bps,
        "candidate_bitrate_norm_ladder": float(index) / 2.0,
        "candidate_delta_from_last_bitrate_norm": 0.0,
        "candidate_chunk_size_bytes": bitrate_bps * 4.0 / 8.0,
        "candidate_chunk_size_available": 1.0,
    }


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

from pathlib import Path

import torch

from core.neural_abr.artifacts import write_json
from core.neural_abr.bundle import write_phase4_bundle_manifest
from core.neural_abr.constants import (
    BUNDLE_FALLBACK_POLICY_FILENAME,
    BUNDLE_INFERENCE_CONTRACT_FILENAME,
    BUNDLE_LADDER_SCHEMA_FILENAME,
    BUNDLE_MODEL_CARD_FILENAME,
    BUNDLE_MODEL_FILENAME,
    CANDIDATE_MODEL_CONFIG_FILENAME,
    CANDIDATE_VECTOR_NAMES,
    CONTEXT_VECTOR_NAMES,
    FEATURE_SCHEMA_FILENAME,
    NORMALIZATION_STATS_FILENAME,
    PHASE4_NORMALIZATION_SCHEMA_ID,
    REWARD_VERSION,
    TRAINING_ROLE,
)
from core.neural_abr.features import build_feature_schema
from core.neural_abr.model import NeuralAbrLiteCandidateScorer
from core.neural_abr.normalization import NormalizationStats


def build_minimal_phase4_bundle(root: object, teacher: str = "robust_mpc") -> Path:
    bundle_dir = Path(root) / "phase4_bundle_{0}".format(teacher)
    bundle_dir.mkdir(parents=True, exist_ok=True)
    model = NeuralAbrLiteCandidateScorer()
    model_config = model.config()
    torch.save(
        {
            "model_config": model_config,
            "model_state_dict": model.state_dict(),
        },
        bundle_dir / BUNDLE_MODEL_FILENAME,
    )
    write_json(bundle_dir / CANDIDATE_MODEL_CONFIG_FILENAME, model_config)
    write_json(bundle_dir / FEATURE_SCHEMA_FILENAME, build_feature_schema())
    write_json(
        bundle_dir / NORMALIZATION_STATS_FILENAME,
        NormalizationStats(
            schema_id=PHASE4_NORMALIZATION_SCHEMA_ID,
            fitted_on_data_role=TRAINING_ROLE,
            feature_names=tuple(CONTEXT_VECTOR_NAMES) + tuple(CANDIDATE_VECTOR_NAMES),
            mean=tuple(0.0 for _ in range(len(CONTEXT_VECTOR_NAMES) + len(CANDIDATE_VECTOR_NAMES))),
            std=tuple(1.0 for _ in range(len(CONTEXT_VECTOR_NAMES) + len(CANDIDATE_VECTOR_NAMES))),
            sample_count=1,
            candidate_row_count=1,
        ).to_json(),
    )
    write_json(
        bundle_dir / BUNDLE_LADDER_SCHEMA_FILENAME,
        {
            "representation_count": 2,
            "bitrates_bps": [300000, 750000],
            "segment_duration_s": 4.0,
            "segment_count": 2,
            "segment_size_source": "bitrate_times_duration_bytes",
        },
    )
    write_json(
        bundle_dir / BUNDLE_MODEL_CARD_FILENAME,
        {
            "model_config": model_config,
            "model_family": "NeuralABR-Lite Candidate Scorer",
            "teacher": teacher,
        },
    )
    write_json(
        bundle_dir / BUNDLE_INFERENCE_CONTRACT_FILENAME,
        {
            "schema_id": "phase4_contrato_inferencia_neural_abr_lite_v1",
            "input_contract": {
                "context_features": "features de estado recientes, sin metadata de traza",
                "candidate_features": "features por representacion candidata del MPD",
                "action_mask": "mascara booleana por representation_index",
            },
            "output_contract": {
                "selected_representation_index": "accion valida bajo action_mask",
                "scores": "score finito por representacion candidata",
            },
            "cpu_only": True,
        },
    )
    write_json(
        bundle_dir / BUNDLE_FALLBACK_POLICY_FILENAME,
        {
            "fallback_controller": "robust_mpc",
            "diagnostic_only": True,
        },
    )
    write_phase4_bundle_manifest(
        bundle_dir,
        {
            "teacher": teacher,
            "model_family": "NeuralABR-Lite Candidate Scorer",
            "training_method": "behavior_cloning",
            "action_space": "representation_index",
            "reward_version": REWARD_VERSION,
            "offline_inference_only": True,
            "qoe_improvement_claimed": False,
        },
    )
    return bundle_dir


def minimal_feedback():
    return {
        "queued_bytes": 0,
        "queued_time": 4.0,
        "cur_bitrate": 37500.0,
        "bwe": 80000.0,
        "level": 0,
        "max_level": 1,
        "cur_rate": 37500.0,
        "max_rate": 93750.0,
        "min_rate": 37500.0,
        "max_bitrate": 93750.0,
        "min_bitrate": 37500.0,
        "last_fragment_size": 4000,
        "last_download_time": 0.5,
        "downloaded_bytes": 4000,
        "fragment_duration": 4.0,
        "rates": [37500.0, 93750.0],
        "segment_index": 1,
        "total_segments": 2,
        "start_segment_request": 1.0,
        "stop_segment_request": 1.5,
    }

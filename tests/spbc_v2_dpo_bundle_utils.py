from __future__ import annotations

from pathlib import Path

import torch

from core.neural_abr.artifacts import write_json
from core.phase45_v1.spbc_training import CANDIDATE_FEATURES, SCALAR_FEATURES, SEQUENCE_FEATURES
from core.phase45_v1.spbc_v2_dpo_bundle import (
    SPBC_V2_DPO_BUNDLE_FALLBACK_POLICY_FILENAME,
    SPBC_V2_DPO_BUNDLE_FEATURE_SCHEMA_FILENAME,
    SPBC_V2_DPO_BUNDLE_INFERENCE_CONTRACT_FILENAME,
    SPBC_V2_DPO_BUNDLE_LADDER_SCHEMA_FILENAME,
    SPBC_V2_DPO_BUNDLE_MODEL_CARD_FILENAME,
    SPBC_V2_DPO_BUNDLE_MODEL_CONFIG_FILENAME,
    SPBC_V2_DPO_BUNDLE_MODEL_FILENAME,
    SPBC_V2_DPO_BUNDLE_NORMALIZATION_FILENAME,
    SPBC_V2_DPO_BUNDLE_SCHEMA_ID,
    SPBC_V2_DPO_CONTROLLER_KEY,
    build_spbc_v2_dpo_fallback_policy,
    build_spbc_v2_dpo_feature_schema,
    build_spbc_v2_dpo_inference_contract,
    build_spbc_v2_dpo_ladder_schema,
    write_spbc_v2_dpo_bundle_manifest,
)
from core.phase45_v1.spbc_v2_dpo_training import SPBC_V2_DPO_MODEL_KEY, SpbcAbrV2DpoPolicy


def build_minimal_spbc_v2_dpo_bundle(root: object) -> Path:
    bundle_dir = Path(root) / "spbc_v2_dpo_bundle"
    bundle_dir.mkdir(parents=True, exist_ok=True)
    model = SpbcAbrV2DpoPolicy(
        history_hidden_size=8,
        state_hidden_size=8,
        candidate_hidden_size=8,
        shared_hidden_size=16,
        dropout=0.0,
    )
    model_config = dict(model.config())
    normalization = _normalization()
    torch.save(
        {
            "schema_id": SPBC_V2_DPO_BUNDLE_SCHEMA_ID,
            "model_key": SPBC_V2_DPO_MODEL_KEY,
            "controller_key": SPBC_V2_DPO_CONTROLLER_KEY,
            "model_state_dict": model.state_dict(),
            "model_config": model_config,
            "normalization": normalization,
            "source_checkpoint_sha256": "stub",
        },
        bundle_dir / SPBC_V2_DPO_BUNDLE_MODEL_FILENAME,
    )
    write_json(bundle_dir / SPBC_V2_DPO_BUNDLE_MODEL_CONFIG_FILENAME, model_config)
    write_json(bundle_dir / SPBC_V2_DPO_BUNDLE_NORMALIZATION_FILENAME, normalization)
    write_json(bundle_dir / SPBC_V2_DPO_BUNDLE_FEATURE_SCHEMA_FILENAME, build_spbc_v2_dpo_feature_schema())
    write_json(bundle_dir / SPBC_V2_DPO_BUNDLE_LADDER_SCHEMA_FILENAME, build_spbc_v2_dpo_ladder_schema())
    write_json(
        bundle_dir / SPBC_V2_DPO_BUNDLE_MODEL_CARD_FILENAME,
        {
            "schema_id": "phase45_v2_spbc_dpo_model_card_v1",
            "model_key": SPBC_V2_DPO_MODEL_KEY,
            "controller_key": SPBC_V2_DPO_CONTROLLER_KEY,
            "model_config": model_config,
            "boundaries": {
                "benchmark_performed": False,
                "ranking_performed": False,
                "qoe_improvement_claimed": False,
            },
        },
    )
    write_json(bundle_dir / SPBC_V2_DPO_BUNDLE_INFERENCE_CONTRACT_FILENAME, build_spbc_v2_dpo_inference_contract())
    write_json(bundle_dir / SPBC_V2_DPO_BUNDLE_FALLBACK_POLICY_FILENAME, build_spbc_v2_dpo_fallback_policy())
    write_spbc_v2_dpo_bundle_manifest(
        bundle_dir,
        {
            "controller_key": SPBC_V2_DPO_CONTROLLER_KEY,
            "controller_alias": "propio_spbc_v2_anchor",
            "controller_display_name": "Propio SPBC v2 Anchor",
            "model_key": SPBC_V2_DPO_MODEL_KEY,
            "model_family": "Safe Preference Behavioral Cloning ABR v2 DPO",
            "training_method": "unit_test_stub",
            "reward_version": "qoe_linear_v1",
            "action_space": "representation_index",
            "offline_inference_only": True,
            "qoe_improvement_claimed": False,
            "benchmark_performed": False,
            "outputs_are_benchmark_results": False,
            "ranking_performed": False,
            "no_final_ranking": True,
        },
    )
    return bundle_dir


def minimal_spbc_feedback() -> dict[str, object]:
    rates = [37500.0, 93750.0, 150000.0]
    return {
        "queued_bytes": 0,
        "queued_time": 4.0,
        "cur_bitrate": rates[0],
        "bwe": 80000.0,
        "level": 0,
        "max_level": len(rates) - 1,
        "cur_rate": rates[0],
        "max_rate": max(rates),
        "min_rate": min(rates),
        "max_bitrate": max(rates),
        "min_bitrate": min(rates),
        "last_fragment_size": 4000,
        "last_download_time": 0.5,
        "downloaded_bytes": 4000,
        "fragment_duration": 4.0,
        "rates": rates,
        "segment_index": 1,
        "total_segments": 3,
        "start_segment_request": 1.0,
        "stop_segment_request": 1.5,
    }


def _normalization() -> dict[str, object]:
    return {
        "schema_id": "phase45_v2_spbc_dpo_normalization_v1",
        "fitted_on_data_role": "training",
        "source": "unit_test_stub",
        "sequence_features": list(SEQUENCE_FEATURES),
        "scalar_features": list(SCALAR_FEATURES),
        "candidate_features": list(CANDIDATE_FEATURES),
        "sequence_mean": [0.0 for _ in SEQUENCE_FEATURES],
        "sequence_std": [1.0 for _ in SEQUENCE_FEATURES],
        "scalar_mean": [0.0 for _ in SCALAR_FEATURES],
        "scalar_std": [1.0 for _ in SCALAR_FEATURES],
        "candidate_mean": [0.0 for _ in CANDIDATE_FEATURES],
        "candidate_std": [1.0 for _ in CANDIDATE_FEATURES],
        "sample_count": 1,
        "candidate_row_count": 3,
        "metadata_fields_used": False,
        "future_fields_used_as_inputs": False,
        "oracle_fields_used_as_inputs": False,
        "preference_targets_used_as_inputs": False,
        "validation_used": False,
    }

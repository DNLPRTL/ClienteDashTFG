from __future__ import annotations

import math
from typing import Mapping

from core.neural_abr.features import build_feature_schema as build_phase4_feature_schema
from core.phase45_v1.constants import (
    FEATURE_SCHEMA_ID,
    FORBIDDEN_MODEL_INPUT_FIELDS,
    ORACLE_POLICY_ID,
    SAMPLE_SCHEMA_ID,
    SPC_TARGET_ID,
    SPBC_TARGET_ID,
    TARGET_SCHEMA_ID,
)


class Phase45SampleSchemaError(ValueError):
    """Raised when a Phase 4-5 v1 dataset sample violates its contract."""


def build_model_input_schema() -> Mapping[str, object]:
    phase4_features = build_phase4_feature_schema()
    return {
        "schema_id": FEATURE_SCHEMA_ID,
        "human_readable_name": "Phase 4-5 v1 safe model inputs for SPC/SPBC candidates",
        "model_input_root": "model_inputs",
        "context_schema_source": phase4_features.get("schema_id"),
        "context_history_length": phase4_features.get("context_history_length"),
        "context_vector_names": phase4_features.get("context_vector_names"),
        "candidate_vector_names": phase4_features.get("candidate_vector_names"),
        "action_mask": "boolean list aligned with representation_index",
        "metadata_fields_are_model_features": False,
        "future_fields_are_model_features": False,
        "oracle_fields_are_model_features": False,
        "forbidden_model_input_fields": sorted(FORBIDDEN_MODEL_INPUT_FIELDS),
    }


def build_target_schema() -> Mapping[str, object]:
    return {
        "schema_id": TARGET_SCHEMA_ID,
        "human_readable_name": "Phase 4-5 v1 targets for SPC and SPBC candidates",
        "spc_targets": {
            "target_id": SPC_TARGET_ID,
            "purpose": "predict future capacity and rebuffer risk; target-only, never runtime-visible future",
            "fields": [
                "future_throughput_kbps",
                "conservative_capacity_kbps",
                "per_candidate_download_risk",
            ],
        },
        "spbc_targets": {
            "target_id": SPBC_TARGET_ID,
            "purpose": "behavioral cloning labels from oracle_qoe_beam_v1",
            "oracle_policy_id": ORACLE_POLICY_ID,
            "fields": [
                "oracle_action",
                "oracle_horizon_reward_n",
                "oracle_best_sequence",
            ],
        },
        "classic_controller_audit": "real Phase 2 controllers are queried for audit only",
        "metadata_fields_are_model_features": False,
    }


def validate_sample(sample: Mapping[str, object], expected_role: str | None = None) -> None:
    if sample.get("schema_id") != SAMPLE_SCHEMA_ID:
        raise Phase45SampleSchemaError("unexpected sample schema_id")
    if expected_role is not None and sample.get("data_role") != expected_role:
        raise Phase45SampleSchemaError("sample data_role mismatch")
    for field in ("sample_id", "data_role", "model_inputs", "spc_targets", "spbc_targets", "audit", "metadata"):
        if field not in sample:
            raise Phase45SampleSchemaError("sample missing {0}".format(field))
    model_inputs = _require_mapping(sample["model_inputs"], "model_inputs")
    reject_forbidden_model_inputs(model_inputs)
    _validate_model_inputs(model_inputs)
    spc_targets = _require_mapping(sample["spc_targets"], "spc_targets")
    spbc_targets = _require_mapping(sample["spbc_targets"], "spbc_targets")
    if spc_targets.get("target_id") != SPC_TARGET_ID:
        raise Phase45SampleSchemaError("spc_targets target_id mismatch")
    if spbc_targets.get("target_id") != SPBC_TARGET_ID:
        raise Phase45SampleSchemaError("spbc_targets target_id mismatch")
    _finite(spbc_targets.get("oracle_horizon_reward_n"), "oracle_horizon_reward_n")
    oracle_action = spbc_targets.get("oracle_action")
    if isinstance(oracle_action, bool) or not isinstance(oracle_action, int):
        raise Phase45SampleSchemaError("oracle_action must be an integer target")
    metadata = _require_mapping(sample["metadata"], "metadata")
    if metadata.get("metadata_is_model_input") is not False:
        raise Phase45SampleSchemaError("metadata_is_model_input must be false")
    if str(metadata.get("source_split")) == "eval":
        raise Phase45SampleSchemaError("eval split sample is forbidden")


def reject_forbidden_model_inputs(value: object, path: str = "model_inputs") -> None:
    if isinstance(value, Mapping):
        offenders = sorted(str(key) for key in value.keys() if str(key) in FORBIDDEN_MODEL_INPUT_FIELDS)
        if offenders:
            raise Phase45SampleSchemaError("{0}: forbidden model input field(s): {1}".format(path, ", ".join(offenders)))
        for key, item in value.items():
            reject_forbidden_model_inputs(item, "{0}.{1}".format(path, key))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            reject_forbidden_model_inputs(item, "{0}[{1}]".format(path, index))


def _validate_model_inputs(model_inputs: Mapping[str, object]) -> None:
    context = _require_mapping(model_inputs.get("context"), "model_inputs.context")
    candidates = model_inputs.get("candidates")
    action_mask = model_inputs.get("action_mask")
    if not isinstance(candidates, list) or not candidates:
        raise Phase45SampleSchemaError("model_inputs.candidates must be a non-empty list")
    if not isinstance(action_mask, list) or len(action_mask) != len(candidates):
        raise Phase45SampleSchemaError("action_mask length must match candidates")
    for name in ("throughput_history_bps", "download_time_history_s", "buffer_s", "last_representation_index"):
        if name not in context:
            raise Phase45SampleSchemaError("context missing {0}".format(name))
    for index, candidate in enumerate(candidates):
        candidate_mapping = _require_mapping(candidate, "candidate {0}".format(index))
        for name in ("candidate_representation_index", "candidate_bitrate_bps", "candidate_chunk_size_bytes"):
            if name not in candidate_mapping:
                raise Phase45SampleSchemaError("candidate {0} missing {1}".format(index, name))


def _require_mapping(value: object, name: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise Phase45SampleSchemaError("{0} must be an object".format(name))
    return value


def _finite(value: object, name: str) -> float:
    if isinstance(value, bool):
        raise Phase45SampleSchemaError("{0} must be numeric".format(name))
    try:
        parsed = float(value)
    except (TypeError, ValueError) as exc:
        raise Phase45SampleSchemaError("{0} must be numeric".format(name)) from exc
    if not math.isfinite(parsed):
        raise Phase45SampleSchemaError("{0} must be finite".format(name))
    return parsed

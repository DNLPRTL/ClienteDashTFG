from __future__ import annotations

from typing import Mapping, Sequence

from core.neural_abr.action_mask import assert_action_valid, validate_action_mask
from core.neural_abr.constants import (
    DATA_ROLES,
    PHASE4_LABEL_SCHEMA_ID,
    PHASE4_TRAINING_DATA_SCHEMA_ID,
    PRIMARY_TEACHER,
    REWARD_VERSION,
    SUPPORTED_LABEL_TEACHERS,
)
from core.neural_abr.features import audit_feature_payload


class SampleSchemaError(ValueError):
    """Raised when a Phase 4 training-data sample is invalid."""


def build_label_schema(
    teacher_policy: str = PRIMARY_TEACHER,
    human_readable_name: str | None = None,
    extra_label_fields: Sequence[str] = (),
) -> Mapping[str, object]:
    if teacher_policy not in SUPPORTED_LABEL_TEACHERS:
        raise SampleSchemaError("teacher_policy is not supported: {0}".format(teacher_policy))
    label_fields = [
        "teacher_action",
        "teacher_policy",
        "teacher_reward_n",
        "reward_version",
        "diagnostic_only",
    ]
    for field in extra_label_fields:
        if field not in label_fields:
            label_fields.append(str(field))
    return {
        "schema_id": PHASE4_LABEL_SCHEMA_ID,
        "human_readable_name": human_readable_name or "Labels generados por el teacher {0}".format(teacher_policy),
        "teacher_policy": teacher_policy,
        "reward_version": REWARD_VERSION,
        "label_fields": label_fields,
    }


def validate_sample(
    sample: Mapping[str, object],
    expected_role: str | None = None,
    allowed_teacher_policies: Sequence[str] = SUPPORTED_LABEL_TEACHERS,
) -> None:
    if sample.get("schema_id") != PHASE4_TRAINING_DATA_SCHEMA_ID:
        raise SampleSchemaError("sample schema_id is invalid")
    sample_id = sample.get("sample_id")
    if not isinstance(sample_id, str) or not sample_id:
        raise SampleSchemaError("sample_id must be a non-empty string")
    data_role = sample.get("data_role")
    if data_role not in DATA_ROLES:
        raise SampleSchemaError("data_role is invalid")
    if expected_role is not None and data_role != expected_role:
        raise SampleSchemaError("expected data_role {0}, got {1}".format(expected_role, data_role))

    context = _mapping(sample.get("context_features"), "context_features")
    candidates_raw = _sequence(sample.get("candidate_features"), "candidate_features")
    if not candidates_raw:
        raise SampleSchemaError("candidate_features must not be empty")
    candidates = tuple(_mapping(candidate, "candidate_features item") for candidate in candidates_raw)
    audit = audit_feature_payload(context, candidates)
    if not audit["passed"]:
        raise SampleSchemaError("feature audit failed: {0}".format("; ".join(audit["errors"])))

    mask = validate_action_mask(_sequence(sample.get("action_mask"), "action_mask"), len(candidates))
    label = _mapping(sample.get("label"), "label")
    teacher_action = label.get("teacher_action")
    if isinstance(teacher_action, bool) or not isinstance(teacher_action, int):
        raise SampleSchemaError("label.teacher_action must be an integer")
    try:
        assert_action_valid(teacher_action, mask)
    except ValueError as exc:
        raise SampleSchemaError(str(exc)) from exc
    if label.get("teacher_policy") not in tuple(allowed_teacher_policies):
        raise SampleSchemaError(
            "label.teacher_policy must be one of: {0}".format(", ".join(tuple(allowed_teacher_policies)))
        )
    if label.get("reward_version") != REWARD_VERSION:
        raise SampleSchemaError("label.reward_version must be {0}".format(REWARD_VERSION))
    if label.get("diagnostic_only") is not True:
        raise SampleSchemaError("label.diagnostic_only must be true")

    metadata = _mapping(sample.get("metadata"), "metadata")
    if metadata.get("data_role") != data_role:
        raise SampleSchemaError("metadata.data_role must mirror sample data_role")
    if not isinstance(metadata.get("trace_id"), str) or not metadata["trace_id"]:
        raise SampleSchemaError("metadata.trace_id must be a non-empty string")
    if not isinstance(metadata.get("segment_index"), int):
        raise SampleSchemaError("metadata.segment_index must be an integer")


def _mapping(value: object, name: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise SampleSchemaError("{0} must be a mapping".format(name))
    return value


def _sequence(value: object, name: str) -> Sequence[object]:
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise SampleSchemaError("{0} must be a sequence".format(name))
    return value

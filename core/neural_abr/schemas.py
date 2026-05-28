"""Schema validation for NeuralABR-Lite offline samples and manifests."""

from __future__ import annotations

from typing import Mapping, Sequence

from core.neural_abr.action_mask import assert_action_valid, validate_action_mask
from core.neural_abr.constants import (
    DATASET_SCHEMA_VERSION,
    LABEL_SCHEMA_VERSION,
    REWARD_VERSION,
    SPLITS,
)
from core.neural_abr.features import audit_feature_payload


class SchemaError(ValueError):
    """Raised when a Phase 4D artifact violates its schema."""


def build_label_schema() -> Mapping[str, object]:
    return {
        "schema_version": LABEL_SCHEMA_VERSION,
        "label_fields": [
            {"name": "teacher_action", "type": "integer", "contract": "representation_index"},
            {"name": "teacher_policy", "type": "string", "primary": "robust_mpc", "secondary": "mpc"},
            {"name": "teacher_reward_n", "type": "number", "reward_version": REWARD_VERSION},
            {"name": "reward_version", "type": "string", "value": REWARD_VERSION},
            {"name": "diagnostic_only", "type": "boolean", "value": True},
        ],
        "forbidden_as_model_input": ["teacher_action", "teacher_reward_n", "reward_version"],
    }


def validate_sample(sample: Mapping[str, object], expected_split: str | None = None) -> None:
    if sample.get("schema_version") != DATASET_SCHEMA_VERSION:
        raise SchemaError("sample schema_version must be {0}".format(DATASET_SCHEMA_VERSION))
    sample_id = sample.get("sample_id")
    if not isinstance(sample_id, str) or not sample_id:
        raise SchemaError("sample_id must be a non-empty string")
    split = sample.get("split")
    if split not in SPLITS:
        raise SchemaError("sample split is invalid")
    if expected_split is not None and split != expected_split:
        raise SchemaError("sample split expected {0}, got {1}".format(expected_split, split))

    context = _mapping(sample.get("context"), "context")
    candidates = _sequence(sample.get("candidates"), "candidates")
    if not candidates:
        raise SchemaError("candidates must not be empty")
    candidate_mappings = tuple(_mapping(candidate, "candidate") for candidate in candidates)
    audit = audit_feature_payload(context, candidate_mappings)
    if not audit["passed"]:
        raise SchemaError("feature audit failed: {0}".format("; ".join(audit["errors"])))

    action_mask = validate_action_mask(_sequence(sample.get("action_mask"), "action_mask"), len(candidate_mappings))
    label = _mapping(sample.get("label"), "label")
    teacher_action = label.get("teacher_action")
    if isinstance(teacher_action, bool) or not isinstance(teacher_action, int):
        raise SchemaError("label.teacher_action must be an integer")
    try:
        assert_action_valid(teacher_action, action_mask)
    except ValueError as exc:
        raise SchemaError(str(exc)) from exc
    if label.get("reward_version") != REWARD_VERSION:
        raise SchemaError("label.reward_version must be {0}".format(REWARD_VERSION))
    if label.get("diagnostic_only") is not True:
        raise SchemaError("label.diagnostic_only must be true")

    metadata = _mapping(sample.get("metadata"), "metadata")
    if not isinstance(metadata.get("trace_id"), str) or not metadata.get("trace_id"):
        raise SchemaError("metadata.trace_id must be a non-empty string")
    if metadata.get("split") != split:
        raise SchemaError("metadata.split must mirror sample split")
    if not isinstance(metadata.get("segment_index"), int):
        raise SchemaError("metadata.segment_index must be an integer")


def validate_manifest(manifest: Mapping[str, object]) -> None:
    if manifest.get("schema_version") != DATASET_SCHEMA_VERSION:
        raise SchemaError("dataset manifest has wrong schema_version")
    if manifest.get("method") != "NeuralABR-Lite Candidate Scorer":
        raise SchemaError("dataset manifest method is invalid")
    if manifest.get("diagnostic_only") is not True:
        raise SchemaError("dataset manifest must be diagnostic_only")
    files = manifest.get("files")
    if not isinstance(files, Mapping):
        raise SchemaError("dataset manifest files must be a mapping")


def _mapping(value: object, name: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise SchemaError("{0} must be a mapping".format(name))
    return value


def _sequence(value: object, name: str) -> Sequence[object]:
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise SchemaError("{0} must be a sequence".format(name))
    return value

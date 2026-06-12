from __future__ import annotations

from pathlib import Path
from typing import Mapping

from core.neural_abr.artifacts import ensure_existing_dir, read_json, read_jsonl
from core.neural_abr.features import audit_feature_payload
from core.phase45_v3.constants import (
    DATASET_SCHEMA_ID,
    LEAKAGE_AUDIT_FILENAME,
    QH_AUDIT_FILENAME,
    REQUIRED_DATASET_FILES,
    SAMPLE_SCHEMA_ID,
    SUMMARY_FILENAME,
    TRAINING_DATA_FILENAME,
    VALIDATION_DATA_FILENAME,
)


class Phase45V3ValidationError(ValueError):
    """Raised when a Phase 4-5 v3 dataset directory is structurally invalid."""


def validate_phase45_v3_dataset_dir(path: object) -> Mapping[str, object]:
    data_dir = ensure_existing_dir(path, purpose="phase45_v3 Q_H dataset")
    errors = []
    missing = [filename for filename in REQUIRED_DATASET_FILES if not (data_dir / filename).is_file()]
    errors.extend("missing required file: {0}".format(filename) for filename in missing)
    if missing:
        return _validation_result(data_dir, errors, 0, 0)

    summary = read_json(data_dir / SUMMARY_FILENAME)
    if summary.get("schema_id") != DATASET_SCHEMA_ID:
        errors.append("unexpected dataset summary schema_id")
    if summary.get("benchmark_performed") is not False:
        errors.append("summary benchmark_performed must be false")
    if summary.get("metadata_fields_are_model_features") is not False:
        errors.append("summary metadata_fields_are_model_features must be false")
    if summary.get("future_fields_are_model_features") is not False:
        errors.append("summary future_fields_are_model_features must be false")
    content_ladder = summary.get("content_ladder")
    if not isinstance(content_ladder, Mapping) or float(content_ladder.get("max_buffer_s", 0.0)) != 60.0:
        errors.append("content_ladder max_buffer_s must be 60.0 for Phase45 v3")

    training_rows = list(read_jsonl(data_dir / TRAINING_DATA_FILENAME))
    validation_rows = list(read_jsonl(data_dir / VALIDATION_DATA_FILENAME))
    if not training_rows:
        errors.append("training data is empty")
    if not validation_rows:
        errors.append("validation data is empty")
    errors.extend(_sample_errors(training_rows, "training"))
    errors.extend(_sample_errors(validation_rows, "validation"))

    leakage = read_json(data_dir / LEAKAGE_AUDIT_FILENAME)
    if leakage.get("status") != "PASS":
        errors.append("leakage audit status is not PASS")
    if leakage.get("metadata_fields_are_model_features") is not False:
        errors.append("leakage audit metadata_fields_are_model_features must be false")
    if leakage.get("eval_split_used") is not False:
        errors.append("leakage audit eval_split_used must be false")

    qh_audit = read_json(data_dir / QH_AUDIT_FILENAME)
    if qh_audit.get("status") != "PASS":
        errors.append("Q_H audit status is not PASS: {0}".format(qh_audit.get("errors")))
    if qh_audit.get("future_information_is_target_only") is not True:
        errors.append("Q_H audit must mark future information as target-only")

    return _validation_result(data_dir, errors, len(training_rows), len(validation_rows))


def _sample_errors(rows: list[Mapping[str, object]], expected_role: str) -> list[str]:
    errors = []
    for index, sample in enumerate(rows[:50]):
        prefix = "{0}[{1}]".format(expected_role, index)
        if sample.get("schema_id") != SAMPLE_SCHEMA_ID:
            errors.append("{0}: unexpected sample schema_id".format(prefix))
        if sample.get("data_role") != expected_role:
            errors.append("{0}: data_role mismatch".format(prefix))
        model_inputs = sample.get("model_inputs")
        if not isinstance(model_inputs, Mapping):
            errors.append("{0}: model_inputs must be object".format(prefix))
            continue
        context = model_inputs.get("context")
        candidates = model_inputs.get("candidates")
        action_mask = model_inputs.get("action_mask")
        if not isinstance(context, Mapping) or not isinstance(candidates, list) or not isinstance(action_mask, list):
            errors.append("{0}: invalid model_inputs shape".format(prefix))
            continue
        feature_audit = audit_feature_payload(context, candidates)
        if not feature_audit["passed"]:
            errors.append("{0}: feature audit failed: {1}".format(prefix, feature_audit["errors"]))
        qh_targets = sample.get("qh_targets")
        if not isinstance(qh_targets, Mapping):
            errors.append("{0}: qh_targets must be object".format(prefix))
            continue
        if qh_targets.get("future_information_is_target_only") is not True:
            errors.append("{0}: future information must be target-only".format(prefix))
        selected_action = int(qh_targets.get("selected_action", -1))
        if selected_action < 0 or selected_action >= len(action_mask) or not action_mask[selected_action]:
            errors.append("{0}: selected_action invalid or masked".format(prefix))
        action_values = qh_targets.get("action_values")
        if not isinstance(action_values, list) or len(action_values) != len(candidates):
            errors.append("{0}: action_values length mismatch".format(prefix))
        metadata = sample.get("metadata")
        if not isinstance(metadata, Mapping) or metadata.get("metadata_is_model_input") is not False:
            errors.append("{0}: metadata boundary missing".format(prefix))
    return errors


def _validation_result(
    data_dir: Path,
    errors: list[str],
    training_sample_count: int,
    validation_sample_count: int,
) -> Mapping[str, object]:
    return {
        "status": "PASS" if not errors else "FAIL",
        "dataset_dir": str(data_dir),
        "errors": errors,
        "training_sample_count": int(training_sample_count),
        "validation_sample_count": int(validation_sample_count),
    }

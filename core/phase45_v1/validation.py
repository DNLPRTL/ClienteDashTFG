from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Mapping, Sequence

from core.neural_abr.artifacts import ensure_existing_dir, read_json, read_jsonl
from core.phase45_v1.constants import (
    DATA_FILENAMES,
    DATA_ROLES,
    DATASET_SCHEMA_ID,
    LEAKAGE_AUDIT_FILENAME,
    NORMALIZATION_STATS_FILENAME,
    ORACLE_AUDIT_FILENAME,
    REQUIRED_DATASET_FILES,
    SUMMARY_FILENAME,
    TRAINING_ROLE,
    VALIDATION_ROLE,
    no_benchmark_policy,
)
from core.phase45_v1.sample_schema import Phase45SampleSchemaError, reject_forbidden_model_inputs, validate_sample


class Phase45DatasetValidationError(ValueError):
    """Raised when a Phase 4-5 v1 dataset directory violates its contract."""


def validate_phase45_v1_dataset_dir(path: object) -> Mapping[str, object]:
    data_dir = ensure_existing_dir(path, purpose="phase45_v1 dataset")
    missing_files = [filename for filename in REQUIRED_DATASET_FILES if not (data_dir / filename).is_file()]
    if missing_files:
        raise Phase45DatasetValidationError("missing required dataset files: {0}".format(", ".join(missing_files)))

    summary = read_json(data_dir / SUMMARY_FILENAME)
    if summary.get("schema_id") != DATASET_SCHEMA_ID:
        raise Phase45DatasetValidationError("unexpected dataset summary schema_id")
    _assert_no_benchmark(summary)

    sample_counts: dict[str, int] = {}
    validation_errors: list[str] = []
    trace_roles: dict[str, str] = {}
    leakage_group_roles: dict[str, str] = {}
    action_counts: Counter[str] = Counter()
    source_split_counts: Counter[str] = Counter()

    for role in DATA_ROLES:
        rows = read_jsonl(data_dir / DATA_FILENAMES[role])
        sample_counts[role] = len(rows)
        if not rows:
            validation_errors.append("{0} JSONL is empty".format(role))
        for index, sample in enumerate(rows, start=1):
            try:
                validate_sample(sample, expected_role=role)
                reject_forbidden_model_inputs(sample["model_inputs"])
            except Phase45SampleSchemaError as exc:
                validation_errors.append("{0} row {1}: {2}".format(role, index, exc))
                continue
            metadata = sample["metadata"]
            trace_id = str(metadata["trace_id"])
            previous_trace_role = trace_roles.setdefault(trace_id, role)
            if previous_trace_role != role:
                validation_errors.append("trace_id appears in multiple roles: {0}".format(trace_id))
            leakage_group = str(metadata["leakage_group"])
            previous_group_role = leakage_group_roles.setdefault(leakage_group, role)
            if previous_group_role != role:
                validation_errors.append("leakage_group appears in multiple roles: {0}".format(leakage_group))
            if str(metadata["source_split"]) == "eval":
                validation_errors.append("eval source split appears in sample: {0}".format(sample["sample_id"]))
            source_split_counts[str(metadata["source_split"])] += 1
            action_counts[str(sample["spbc_targets"]["oracle_action"])] += 1

    leakage_audit = read_json(data_dir / LEAKAGE_AUDIT_FILENAME)
    normalization = read_json(data_dir / NORMALIZATION_STATS_FILENAME)
    oracle_audit = read_json(data_dir / ORACLE_AUDIT_FILENAME)
    if leakage_audit.get("status") != "PASS":
        validation_errors.append("leakage audit status is not PASS")
    if normalization.get("fitted_on_data_role") != TRAINING_ROLE:
        validation_errors.append("normalization is not fitted on training only")
    if oracle_audit.get("fallback_count", 0) != 0:
        validation_errors.append("oracle fallback_count must be 0 for generated labels")

    expected_counts = summary.get("sample_counts")
    if isinstance(expected_counts, Mapping):
        for role, count in sample_counts.items():
            if int(expected_counts.get(role, -1)) != count:
                validation_errors.append("{0} sample count mismatch with summary".format(role))

    if validation_errors:
        raise Phase45DatasetValidationError("; ".join(validation_errors[:10]))

    return {
        "status": "PASS",
        "dataset_dir": str(data_dir),
        "sample_counts": sample_counts,
        "oracle_action_distribution": dict(sorted(action_counts.items())),
        "source_split_counts": dict(sorted(source_split_counts.items())),
        "training_role": TRAINING_ROLE,
        "validation_role": VALIDATION_ROLE,
        "metadata_fields_are_model_features": False,
        "future_fields_are_model_features": False,
        "oracle_action_as_feature": False,
        **no_benchmark_policy(),
    }


def _assert_no_benchmark(mapping: Mapping[str, object]) -> None:
    for flag, expected in no_benchmark_policy().items():
        if mapping.get(flag) is not expected:
            raise Phase45DatasetValidationError("{0} must be {1}".format(flag, expected))

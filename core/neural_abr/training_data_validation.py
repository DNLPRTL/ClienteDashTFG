from __future__ import annotations

from pathlib import Path
from typing import Mapping

from core.neural_abr.artifacts import ensure_existing_dir, read_json, read_jsonl
from core.neural_abr.constants import (
    DATA_FILENAMES,
    FEATURE_SCHEMA_FILENAME,
    LABEL_SCHEMA_FILENAME,
    LEAKAGE_AUDIT_FILENAME,
    NORMALIZATION_STATS_FILENAME,
    PHASE4_FEATURE_SCHEMA_ID,
    PHASE4_NORMALIZATION_SCHEMA_ID,
    PHASE4_TRAINING_DATA_SCHEMA_ID,
    REQUIRED_TRAINING_DATA_FILES,
    TRAINING_DATA_SUMMARY_FILENAME,
    TRAINING_ROLE,
    VALIDATION_ROLE,
)
from core.neural_abr.sample_schema import validate_sample


class TrainingDataValidationError(ValueError):
    """Raised when Phase 4 training data artifacts are invalid."""


def validate_phase4_training_data_dir(path: object) -> Mapping[str, object]:
    data_dir = ensure_existing_dir(path, purpose="phase4 training data")
    missing = [filename for filename in REQUIRED_TRAINING_DATA_FILES if not (data_dir / filename).is_file()]
    if missing:
        raise TrainingDataValidationError("missing required files: {0}".format(", ".join(missing)))

    summary = read_json(data_dir / TRAINING_DATA_SUMMARY_FILENAME)
    if summary.get("schema_id") != PHASE4_TRAINING_DATA_SCHEMA_ID:
        raise TrainingDataValidationError("summary schema_id is invalid")
    for flag in ("benchmark_performed", "outputs_are_benchmark_results", "ranking_performed", "ia_training_performed"):
        if summary.get(flag) is not False:
            raise TrainingDataValidationError("{0} must be false".format(flag))

    feature_schema = read_json(data_dir / FEATURE_SCHEMA_FILENAME)
    if feature_schema.get("schema_id") != PHASE4_FEATURE_SCHEMA_ID:
        raise TrainingDataValidationError("feature schema_id is invalid")
    normalization = read_json(data_dir / NORMALIZATION_STATS_FILENAME)
    if normalization.get("schema_id") != PHASE4_NORMALIZATION_SCHEMA_ID:
        raise TrainingDataValidationError("normalization schema_id is invalid")
    if normalization.get("fitted_on_data_role") != TRAINING_ROLE:
        raise TrainingDataValidationError("normalization must be fitted on training only")
    leakage_audit = read_json(data_dir / LEAKAGE_AUDIT_FILENAME)
    if leakage_audit.get("status") != "PASS":
        raise TrainingDataValidationError("leakage audit did not pass")
    label_schema = read_json(data_dir / LABEL_SCHEMA_FILENAME)
    if label_schema.get("teacher_policy") != "robust_mpc":
        raise TrainingDataValidationError("label teacher must be robust_mpc")

    counts = {}
    for role in (TRAINING_ROLE, VALIDATION_ROLE):
        samples = read_jsonl(data_dir / DATA_FILENAMES[role])
        for sample in samples:
            validate_sample(sample, expected_role=role)
        counts[role] = len(samples)
    if counts[TRAINING_ROLE] <= 0 or counts[VALIDATION_ROLE] <= 0:
        raise TrainingDataValidationError("training and validation data must not be empty")

    return {
        "status": "PASS",
        "data_dir": str(Path(data_dir)),
        "sample_counts": counts,
        "benchmark_performed": False,
        "ia_training_performed": False,
        "ranking_performed": False,
    }


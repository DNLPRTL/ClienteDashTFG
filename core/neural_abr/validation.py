"""Dataset and offline model sanity validation for Phase 4D."""

from __future__ import annotations

from collections import Counter
from typing import Mapping, Sequence

from core.neural_abr.artifacts import ensure_existing_dir, prepare_output_dir, read_json, read_jsonl, write_json
from core.neural_abr.constants import (
    DATASET_FILENAMES,
    OFFLINE_VALIDATION_REPORT_VERSION,
    OOD_SPLIT,
    REQUIRED_DATASET_FILES,
    SPLITS,
    VALIDATION_SPLIT,
)
from core.neural_abr.schemas import validate_manifest, validate_sample
from core.neural_abr.training import evaluate_samples, load_trained_model


class ValidationError(ValueError):
    """Raised when dataset/model validation fails a Phase 4D gate."""


def validate_dataset_dir(dataset_dir: object, write_report: bool = False) -> Mapping[str, object]:
    dataset_path = ensure_existing_dir(dataset_dir, purpose="dataset")
    missing = [filename for filename in REQUIRED_DATASET_FILES if not (dataset_path / filename).is_file()]
    if missing:
        raise ValidationError("missing dataset file(s): {0}".format(", ".join(missing)))

    manifest = read_json(dataset_path / "dataset_manifest.json")
    validate_manifest(manifest)
    leakage = read_json(dataset_path / "leakage_audit.json")
    if leakage.get("blocked"):
        raise ValidationError("leakage audit is blocked")

    trace_to_split = {}
    split_reports = {}
    all_errors = []
    for split in SPLITS:
        samples = tuple(read_jsonl(dataset_path / DATASET_FILENAMES[split]))
        label_counts = Counter()
        for sample in samples:
            try:
                validate_sample(sample, expected_split=split)
            except Exception as exc:
                all_errors.append("{0}:{1}: {2}".format(split, sample.get("sample_id", "<unknown>"), exc))
                continue
            trace_id = sample["metadata"]["trace_id"]
            previous = trace_to_split.setdefault(trace_id, split)
            if previous != split:
                all_errors.append("trace_id appears in multiple splits: {0}".format(trace_id))
            label_counts[str(sample["label"]["teacher_action"])] += 1
        split_reports[split] = {
            "sample_count": len(samples),
            "label_distribution": dict(sorted(label_counts.items())),
        }

    report = {
        "schema_version": "neural_abr_lite_dataset_validation_report_v1",
        "diagnostic_only": True,
        "not_benchmark": True,
        "dataset_dir": str(dataset_path),
        "status": "PASS" if not all_errors else "FAIL",
        "errors": all_errors,
        "splits": split_reports,
        "trace_level_split_disjoint": not all_errors,
        "normalization_scope": "not_fit_during_dataset_validation",
    }
    if write_report:
        write_json(dataset_path / "dataset_validation_report.json", report)
    if all_errors:
        raise ValidationError("dataset validation failed: {0}".format("; ".join(all_errors[:5])))
    return report


def validate_offline_run(dataset_dir: object, run_dir: object, output_dir: object) -> Mapping[str, object]:
    dataset_path = ensure_existing_dir(dataset_dir, purpose="dataset")
    output_path = prepare_output_dir(output_dir, overwrite=True, purpose="offline validation")
    validate_dataset_dir(dataset_path)
    model, normalizer = load_trained_model(run_dir)
    validation_samples = tuple(read_jsonl(dataset_path / DATASET_FILENAMES[VALIDATION_SPLIT]))
    ood_samples = tuple(read_jsonl(dataset_path / DATASET_FILENAMES[OOD_SPLIT]))
    validation_metrics = evaluate_samples(model, normalizer, validation_samples)
    ood_metrics = evaluate_samples(model, normalizer, ood_samples)
    errors = []
    if validation_metrics["valid_action_rate"] != 1.0:
        errors.append("validation action validity below 100%")
    if ood_metrics["valid_action_rate"] != 1.0:
        errors.append("OOD diagnostic action validity below 100%")
    report = {
        "schema_version": OFFLINE_VALIDATION_REPORT_VERSION,
        "diagnostic_only": True,
        "not_benchmark": True,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "validation_metrics": validation_metrics,
        "ood_diagnostic_metrics": ood_metrics,
        "claim_boundary": "sanity validation only; no ranking or client integration",
    }
    write_json(output_path / "offline_validation_report.json", report)
    if errors:
        raise ValidationError("; ".join(errors))
    return report

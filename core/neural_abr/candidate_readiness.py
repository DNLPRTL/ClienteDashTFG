"""Phase 4E.2 candidate-readiness assessment for NeuralABR-Lite."""

from __future__ import annotations

import math
import subprocess
from collections import Counter
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from core.neural_abr.artifacts import REPO_ROOT, ensure_existing_dir, read_json, read_jsonl
from core.neural_abr.constants import (
    CANDIDATE_READINESS_REPORT_VERSION,
    DATASET_FILENAMES,
    NORMALIZATION_SCHEMA_VERSION,
    OOD_SPLIT,
    PHASE4E2_DECISION_BLOCKED,
    PHASE4E2_DECISION_CANDIDATE_READY,
    PHASE4E2_DECISION_PASS_NOT_CANDIDATE,
    SPLITS,
    TRAIN_SPLIT,
    VALIDATION_SPLIT,
)
from core.neural_abr.schemas import validate_sample
from core.neural_abr.validation import validate_dataset_dir


HARD_CORRECTNESS_GATES = (
    "dataset_validation_pass",
    "offline_validation_pass",
    "validation_valid_action_rate_is_1",
    "ood_valid_action_rate_is_1",
    "no_nan_inf",
    "no_invalid_labels",
    "no_trace_overlap",
    "no_leakage_group_overlap",
    "train_only_normalization",
    "cpu_execution",
)

CANDIDATE_READINESS_GATES = (
    "trace_count_at_least_30",
    "dataset_family_count_at_least_2",
    "regime_bucket_count_at_least_3",
    "model_card_exists",
    "limitations_doc_exists",
)

ENVIRONMENTAL_OR_EXTERNAL_GATES = (
    "no_forbidden_repo_artifacts",
    "no_controller_runtime_media_changes",
)

INFORMATIONAL_GATES = (
    "unit_tests_pass",
    "readiness_pass",
)

CORRECTNESS_GATES = HARD_CORRECTNESS_GATES
CANDIDATE_GATES = CANDIDATE_READINESS_GATES

FORBIDDEN_ARTIFACT_SUFFIXES = (
    ".pt",
    ".pth",
    ".onnx",
    ".npy",
    ".npz",
    ".pkl",
    ".joblib",
    ".zip",
    ".pdf",
    ".log",
)

IGNORED_REPO_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
}

PROTECTED_CHANGE_PREFIXES = (
    "controllers/",
    "player/",
    "runtime/",
    "media/",
)


class CandidateReadinessError(ValueError):
    """Raised when candidate-readiness inputs cannot be read."""


def assess_candidate_readiness(
    dataset_dir: object,
    run_dir: object,
    validation_dir: object,
    phase: str = "phase4e2",
    docs_dir: object | None = None,
    repo_root: object | None = None,
    check_repo_hygiene: bool = False,
    no_forbidden_repo_artifacts: bool | None = None,
    no_controller_runtime_media_changes: bool | None = None,
    unit_tests_pass: bool | None = None,
    readiness_pass: bool | None = None,
) -> Mapping[str, object]:
    """Return a JSON-serializable Phase 4E candidate-readiness report."""

    if phase not in ("phase4e1", "phase4e2"):
        raise CandidateReadinessError("unsupported phase: {0}".format(phase))

    dataset_path = ensure_existing_dir(dataset_dir, purpose="dataset")
    run_path = ensure_existing_dir(run_dir, purpose="training run")
    validation_path = ensure_existing_dir(validation_dir, purpose="offline validation")
    resolved_repo_root = Path(repo_root).resolve() if repo_root is not None else REPO_ROOT.resolve()
    resolved_docs_dir = (
        Path(docs_dir).resolve()
        if docs_dir is not None
        else resolved_repo_root / "docs" / "science" / "04_neural_abr"
    )

    manifest = read_json(dataset_path / "dataset_manifest.json")
    leakage_audit = read_json(dataset_path / "leakage_audit.json")
    training_report = _read_optional_json(run_path / "training_report.json")
    normalization_stats = _read_optional_json(run_path / "normalization_stats.json")
    model_config = _read_optional_json(run_path / "model_config.json")
    offline_report = _read_optional_json(validation_path / "offline_validation_report.json")
    dataset_validation_report = _dataset_validation_report(dataset_path)
    samples_by_split = _load_samples_by_split(dataset_path)

    split_audit = _audit_split_disjointness(manifest, samples_by_split)
    label_audit = _audit_labels(samples_by_split)
    distribution_report = _distribution_report(samples_by_split, training_report, offline_report)
    dataset_summary = _dataset_summary(manifest, samples_by_split)
    warnings = []
    warnings.extend(distribution_report["warnings"])
    warnings.extend(_underrepresentation_warnings(dataset_summary))

    gates = {}
    gates["unit_tests_pass"] = _gate_from_optional(unit_tests_pass, "Not measured by the pure assessor.")
    gates["readiness_pass"] = _gate_from_optional(readiness_pass, "Not measured by the pure assessor.")
    gates["dataset_validation_pass"] = _gate(
        dataset_validation_report["status"] == "PASS",
        dataset_validation_report.get("errors", []),
    )
    gates["offline_validation_pass"] = _gate(
        offline_report.get("status") == "PASS",
        offline_report.get("errors", "offline_validation_report.json missing or not PASS"),
    )
    validation_metrics = _mapping(offline_report.get("validation_metrics"))
    ood_metrics = _mapping(offline_report.get("ood_diagnostic_metrics"))
    gates["validation_valid_action_rate_is_1"] = _gate(
        _float_eq(validation_metrics.get("valid_action_rate"), 1.0),
        {"valid_action_rate": validation_metrics.get("valid_action_rate")},
    )
    gates["ood_valid_action_rate_is_1"] = _gate(
        _float_eq(ood_metrics.get("valid_action_rate"), 1.0),
        {"valid_action_rate": ood_metrics.get("valid_action_rate")},
    )
    gates["no_nan_inf"] = _gate(
        _no_nan_inf((manifest, leakage_audit, training_report, normalization_stats, model_config, offline_report, samples_by_split)),
        "All loaded dataset/run/validation values must be finite.",
    )
    gates["no_invalid_labels"] = _gate(not label_audit["errors"], label_audit)
    gates["trace_count_at_least_30"] = _gate(dataset_summary["trace_count"] >= 30, dataset_summary["trace_count"])
    gates["dataset_family_count_at_least_2"] = _gate(
        dataset_summary["dataset_family_count"] >= 2,
        dataset_summary["dataset_id_counts"],
    )
    gates["regime_bucket_count_at_least_3"] = _gate(
        dataset_summary["regime_bucket_count"] >= 3,
        dataset_summary["regime_bucket_counts"],
    )
    gates["no_trace_overlap"] = _gate(not split_audit["trace_overlap"], split_audit["trace_overlap"])
    gates["no_leakage_group_overlap"] = _gate(
        not split_audit["leakage_group_overlap"],
        split_audit["leakage_group_overlap"],
    )
    gates["train_only_normalization"] = _gate(
        normalization_stats.get("schema_version") == NORMALIZATION_SCHEMA_VERSION
        and normalization_stats.get("fitted_on_split") == TRAIN_SPLIT,
        {
            "schema_version": normalization_stats.get("schema_version"),
            "fitted_on_split": normalization_stats.get("fitted_on_split"),
        },
    )
    gates["cpu_execution"] = _gate(
        training_report.get("device") == "cpu"
        and model_config.get("device_default", "cpu") == "cpu"
        and training_report.get("controller_registered") is False,
        {
            "training_device": training_report.get("device"),
            "model_device_default": model_config.get("device_default"),
            "controller_registered": training_report.get("controller_registered"),
        },
    )
    gates["model_card_exists"] = _gate(
        (resolved_docs_dir / "{0}_model_card.md".format(phase)).is_file(),
        str(resolved_docs_dir / "{0}_model_card.md".format(phase)),
    )
    gates["limitations_doc_exists"] = _gate(
        (resolved_docs_dir / "{0}_open_limitations.md".format(phase)).is_file(),
        str(resolved_docs_dir / "{0}_open_limitations.md".format(phase)),
    )
    gates["no_forbidden_repo_artifacts"] = _environmental_gate(
        explicit_value=no_forbidden_repo_artifacts,
        checked_value=(not _forbidden_repo_artifacts(resolved_repo_root)) if check_repo_hygiene else None,
        checked_details=_forbidden_repo_artifacts(resolved_repo_root) if check_repo_hygiene else None,
        unchecked_details="Repo artifact scan not checked by this assessor invocation.",
    )
    gates["no_controller_runtime_media_changes"] = _environmental_gate(
        explicit_value=no_controller_runtime_media_changes,
        checked_value=(not _protected_git_changes(resolved_repo_root)) if check_repo_hygiene else None,
        checked_details=_protected_git_changes(resolved_repo_root) if check_repo_hygiene else None,
        unchecked_details="Protected git path scan not checked by this assessor invocation.",
    )

    correctness_failures = [
        name for name in HARD_CORRECTNESS_GATES if gates[name]["status"] == "FAIL"
    ]
    candidate_failures = [
        name for name in CANDIDATE_READINESS_GATES if gates[name]["status"] != "PASS"
    ]
    environmental_failures = [
        name for name in ENVIRONMENTAL_OR_EXTERNAL_GATES if gates[name]["status"] == "FAIL"
    ]
    if correctness_failures or environmental_failures:
        decision = PHASE4E2_DECISION_BLOCKED
    elif candidate_failures:
        decision = PHASE4E2_DECISION_PASS_NOT_CANDIDATE
    else:
        decision = PHASE4E2_DECISION_CANDIDATE_READY

    return {
        "schema_version": CANDIDATE_READINESS_REPORT_VERSION,
        "phase": phase,
        "decision": decision,
        "dataset_dir": str(dataset_path),
        "run_dir": str(run_path),
        "validation_dir": str(validation_path),
        "docs_dir": str(resolved_docs_dir),
        "diagnostic_only": True,
        "not_benchmark": True,
        "no_ranking": True,
        "no_real_world_claim": True,
        "gates": gates,
        "hard_correctness_gates": list(HARD_CORRECTNESS_GATES),
        "candidate_readiness_gates": list(CANDIDATE_READINESS_GATES),
        "environmental_or_external_gates": list(ENVIRONMENTAL_OR_EXTERNAL_GATES),
        "correctness_failures": correctness_failures,
        "candidate_failures": candidate_failures,
        "environmental_failures": environmental_failures,
        "dataset_summary": dataset_summary,
        "dataset_validation_report": dataset_validation_report,
        "training_summary": _training_summary(training_report),
        "validation_summary": _validation_summary(offline_report),
        "split_audit": split_audit,
        "label_audit": label_audit,
        "distribution_report": distribution_report,
        "warnings": warnings,
        "claim_boundary": "offline diagnostic candidate-readiness only; not benchmark, ranking, SOTA, or real-world validation",
    }


def render_candidate_readiness_markdown(report: Mapping[str, object]) -> str:
    gates = _mapping(report.get("gates"))
    dataset_summary = _mapping(report.get("dataset_summary"))
    validation_summary = _mapping(report.get("validation_summary"))
    distribution = _mapping(report.get("distribution_report"))
    lines = [
        "# Phase 4E.2 Candidate Readiness Report",
        "",
        "Decision: `{0}`".format(report.get("decision")),
        "",
        "Gate categories: hard correctness gates can block, candidate-readiness gates can produce PASS_NOT_CANDIDATE, and environmental or external gates are UNKNOWN unless explicitly checked or supplied.",
        "",
        "This report is an offline diagnostic gate for NeuralABR-Lite. It is not a formal benchmark, ranking, SOTA claim, or real-world validation.",
        "",
        "## Corpus and dataset",
        "",
        "- Trace count: `{0}`".format(dataset_summary.get("trace_count")),
        "- Dataset families: `{0}`".format(dataset_summary.get("dataset_family_count")),
        "- Regime buckets: `{0}`".format(dataset_summary.get("regime_bucket_count")),
        "- Split policy: `{0}`".format(dataset_summary.get("split_policy")),
        "",
        "## Validation",
        "",
        "- Offline validation status: `{0}`".format(validation_summary.get("status")),
        "- Validation valid action rate: `{0}`".format(validation_summary.get("validation_valid_action_rate")),
        "- OOD diagnostic valid action rate: `{0}`".format(validation_summary.get("ood_valid_action_rate")),
        "- Validation teacher agreement: `{0}`".format(validation_summary.get("validation_teacher_agreement")),
        "- OOD teacher agreement: `{0}`".format(validation_summary.get("ood_teacher_agreement")),
        "",
        "## Distribution sanity",
        "",
        "- Validation TVD prediction vs teacher: `{0}`".format(distribution.get("validation_total_variation_distance")),
        "- OOD TVD prediction vs teacher: `{0}`".format(distribution.get("ood_total_variation_distance")),
        "- Validation entropy ratio: `{0}`".format(distribution.get("validation_entropy_ratio")),
        "- OOD entropy ratio: `{0}`".format(distribution.get("ood_entropy_ratio")),
        "",
        "## Gates",
        "",
    ]
    for name in list(INFORMATIONAL_GATES) + list(HARD_CORRECTNESS_GATES) + list(CANDIDATE_READINESS_GATES) + list(ENVIRONMENTAL_OR_EXTERNAL_GATES):
        gate = _mapping(gates.get(name))
        lines.append("- `{0}`: `{1}`".format(name, gate.get("status", "UNKNOWN")))
    warnings = report.get("warnings") or []
    if warnings:
        lines.extend(["", "## Warnings", ""])
        for warning in warnings:
            lines.append("- {0}".format(warning))
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "OOD remains diagnostic-only. Phase 4F is allowed only when the decision is `PHASE4E2_EXPANDED_CORPUS_CANDIDATE_READY_FOR_PHASE4F`; this report does not integrate a neural controller into the client.",
            "",
        ]
    )
    return "\n".join(lines)


def render_validation_report_markdown(report: Mapping[str, object]) -> str:
    validation = _mapping(report.get("validation_summary"))
    distribution = _mapping(report.get("distribution_report"))
    return "\n".join(
        [
            "# Phase 4E.2 Validation Report",
            "",
            "Decision: `{0}`".format(report.get("decision")),
            "",
            "Offline validation is a sanity check over validation and OOD diagnostic splits, not a formal benchmark.",
            "",
            "- Validation status: `{0}`".format(validation.get("status")),
            "- Validation valid action rate: `{0}`".format(validation.get("validation_valid_action_rate")),
            "- OOD valid action rate: `{0}`".format(validation.get("ood_valid_action_rate")),
            "- Validation prediction distribution: `{0}`".format(distribution.get("validation_prediction_distribution")),
            "- Validation teacher distribution: `{0}`".format(distribution.get("validation_teacher_distribution")),
            "- OOD prediction distribution: `{0}`".format(distribution.get("ood_prediction_distribution")),
            "- OOD teacher distribution: `{0}`".format(distribution.get("ood_teacher_distribution")),
            "",
        ]
    )


def render_model_card_markdown(report: Mapping[str, object]) -> str:
    dataset = _mapping(report.get("dataset_summary"))
    training = _mapping(report.get("training_summary"))
    return "\n".join(
        [
            "# Phase 4E.2 Model Card",
            "",
            "Model: NeuralABR-Lite Candidate Scorer.",
            "",
            "Training method: CPU-first behavior cloning from `robust_mpc` teacher labels over valid MPD representation candidates.",
            "",
            "- Decision: `{0}`".format(report.get("decision")),
            "- Device: `{0}`".format(training.get("device")),
            "- Epochs: `{0}`".format(training.get("epochs")),
            "- Batch size: `{0}`".format(training.get("batch_size")),
            "- Trace count: `{0}`".format(dataset.get("trace_count")),
            "- Dataset families: `{0}`".format(dataset.get("dataset_id_counts")),
            "- Regime buckets: `{0}`".format(dataset.get("regime_bucket_counts")),
            "",
            "The model is not registered in DashClientModular4 and has not been benchmarked against deployed controllers.",
            "",
        ]
    )


def render_limitations_markdown(report: Mapping[str, object]) -> str:
    warnings = report.get("warnings") or []
    lines = [
        "# Phase 4E.2 Open Limitations",
        "",
        "- Phase 4E.2 is offline diagnostic work only.",
        "- No formal benchmark, ranking, SOTA claim, or real-world claim is made.",
        "- OOD traces are diagnostic-only and must not be tuned on.",
        "- NeuralABR-Lite is not integrated into the client.",
        "- Robustness still depends on corpus breadth, leakage checks, and future Phase 4F export/inference contracts.",
    ]
    for warning in warnings:
        lines.append("- {0}".format(warning))
    lines.append("")
    return "\n".join(lines)


def render_closure_report_markdown(report: Mapping[str, object]) -> str:
    return "\n".join(
        [
            "# Phase 4E.2 Closure Report",
            "",
            "Decision: `{0}`".format(report.get("decision")),
            "",
            "R2 status: Windows produced the candidate-ready diagnostic result, but Phase 4E.2 closure remains pending until Ubuntu unit validation passes after the cross-platform candidate-readiness repair.",
            "",
            "Phase 4E.1 proved that the external normalized trace path could run on a 15-trace smoke. Phase 4E.2 exists to expand that diagnostic corpus and add an explicit candidate-readiness gate before any Phase 4F export work.",
            "",
            "Phase 4E.2 repaired the expanded corpus path and added a candidate-readiness gate. The work remains outside controller/player/runtime/media integration.",
            "",
            "The result is still not a formal benchmark, ranking, SOTA claim, or real-world validation.",
            "",
            "Phase 4F is allowed only if the decision is `PHASE4E2_EXPANDED_CORPUS_CANDIDATE_READY_FOR_PHASE4F`.",
            "",
            "For the R2 repair, Phase 4F is still held until both Windows and Ubuntu validation pass. The repair does not change the model, method, controller boundary, or benchmark boundary.",
            "",
        ]
    )


def render_repair_report_markdown(report: Mapping[str, object]) -> str:
    return "\n".join(
        [
            "# Phase 4E.2 Repair Report",
            "",
            "Phase 4E.2 follows Phase 4E.1 because the earlier work only proved external trace ingestion on a small smoke corpus. The repair keeps the scope offline and diagnostic while making the expanded corpus usable for candidate-readiness assessment.",
            "",
            "R2 cross-platform repair: after commit `316e37f`, the Windows expanded run passed and produced a candidate-ready diagnostic result, but Ubuntu unit validation failed because the pure assessor treated repository artifact scanning as a hard correctness gate during tests.",
            "",
            "The R2 repair separates hard correctness gates, candidate-readiness gates, and environmental or external gates. A valid small fixture now returns `PHASE4E2_EXPANDED_CORPUS_PASS_NOT_CANDIDATE`; environmental gates are `UNKNOWN` unless explicitly supplied or explicitly checked, and explicit environmental failures can still block.",
            "",
            "Phase 4F remains blocked until Ubuntu validation passes after this R2 repair.",
            "",
            "The repair addressed two blockers: unsupported `phase4e2_regime_balanced_trace_v1` split policy during dataset build, and a missing candidate-readiness assessor CLI.",
            "",
            "The split loader now accepts Phase 4E.1 and Phase 4E.2 policies. Phase 4E.2 assignment is trace-level, leakage-group clean, deterministic with seed, and uses dataset/regime strata when metadata is available.",
            "",
            "The assessor CLI accepts the required `--dataset-dir`, `--run-dir`, `--validation-dir`, `--output-dir`, and `--phase phase4e2` arguments. Normal PASS_NOT_CANDIDATE outcomes exit with code 0, while correctness blockers exit with code 1.",
            "",
            "Candidate-readiness is assessed from dataset manifests, leakage checks, train-only normalization, CPU training metadata, offline validation metrics, prediction-vs-teacher distributions, and required memory/limitations docs. Repo hygiene is an environmental gate: it blocks only when explicitly checked or supplied by a real validation context.",
            "",
            "This is still not a benchmark or ranking because it does not compare against the classical controllers in a formal evaluation matrix and does not make deployment or real-world claims.",
            "",
            "Decision after latest assessment: `{0}`".format(report.get("decision")),
            "",
        ]
    )


def _dataset_validation_report(dataset_path: Path) -> Mapping[str, object]:
    try:
        return dict(validate_dataset_dir(dataset_path, write_report=False))
    except Exception as exc:  # noqa: BLE001 - gate report should preserve cause.
        return {
            "status": "FAIL",
            "errors": [str(exc)],
        }


def _load_samples_by_split(dataset_path: Path) -> Mapping[str, Sequence[Mapping[str, object]]]:
    return {
        split: tuple(read_jsonl(dataset_path / DATASET_FILENAMES[split]))
        for split in SPLITS
    }


def _audit_labels(samples_by_split: Mapping[str, Sequence[Mapping[str, object]]]) -> Mapping[str, object]:
    errors = []
    label_distribution = Counter()
    for split, samples in samples_by_split.items():
        for sample in samples:
            try:
                validate_sample(sample, expected_split=split)
            except Exception as exc:  # noqa: BLE001
                errors.append("{0}:{1}: {2}".format(split, sample.get("sample_id", "<unknown>"), exc))
                continue
            label_distribution[str(sample["label"]["teacher_action"])] += 1
    return {
        "errors": errors,
        "label_distribution": dict(sorted(label_distribution.items())),
    }


def _audit_split_disjointness(
    manifest: Mapping[str, object],
    samples_by_split: Mapping[str, Sequence[Mapping[str, object]]],
) -> Mapping[str, object]:
    trace_splits: dict[str, set[str]] = {}
    leakage_splits: dict[str, set[str]] = {}
    for split, split_info in _mapping(manifest.get("splits")).items():
        for trace_id in _sequence(_mapping(split_info).get("trace_ids")):
            trace_splits.setdefault(str(trace_id), set()).add(str(split))
        for leakage_group in _sequence(_mapping(split_info).get("leakage_groups")):
            leakage_splits.setdefault(str(leakage_group), set()).add(str(split))
    for split, samples in samples_by_split.items():
        for sample in samples:
            metadata = _mapping(sample.get("metadata"))
            trace_id = str(metadata.get("trace_id", ""))
            leakage_group = str(metadata.get("leakage_group") or trace_id)
            if trace_id:
                trace_splits.setdefault(trace_id, set()).add(split)
            if leakage_group:
                leakage_splits.setdefault(leakage_group, set()).add(split)
    trace_overlap = {
        trace_id: sorted(splits)
        for trace_id, splits in trace_splits.items()
        if len(splits) > 1
    }
    leakage_overlap = {
        leakage_group: sorted(splits)
        for leakage_group, splits in leakage_splits.items()
        if len(splits) > 1
    }
    return {
        "trace_overlap": trace_overlap,
        "leakage_group_overlap": leakage_overlap,
    }


def _dataset_summary(
    manifest: Mapping[str, object],
    samples_by_split: Mapping[str, Sequence[Mapping[str, object]]],
) -> Mapping[str, object]:
    trace_records = _sequence(manifest.get("trace_records"))
    trace_ids = set()
    dataset_counts = Counter()
    regime_counts = Counter()
    split_counts = {}
    for record in trace_records:
        entry = _mapping(record)
        trace_id = str(entry.get("trace_id", "")).strip()
        if trace_id:
            trace_ids.add(trace_id)
        dataset_id = str(entry.get("dataset_id") or entry.get("source_dataset") or "unknown_dataset")
        dataset_counts[dataset_id] += 1
        regime = str(entry.get("regime_bucket") or entry.get("regime") or "").strip()
        if regime:
            regime_counts[regime] += 1

    trace_regime_seen = set()
    for split, samples in samples_by_split.items():
        split_counts[split] = len(samples)
        for sample in samples:
            metadata = _mapping(sample.get("metadata"))
            trace_id = str(metadata.get("trace_id", "")).strip()
            if trace_id:
                trace_ids.add(trace_id)
            dataset_id = str(metadata.get("dataset_id") or metadata.get("source_dataset") or "unknown_dataset")
            if not trace_records:
                dataset_counts[dataset_id] += 1
            regime = str(metadata.get("regime_bucket") or metadata.get("regime") or "").strip()
            if regime and trace_id and trace_id not in trace_regime_seen:
                regime_counts[regime] += 1
                trace_regime_seen.add(trace_id)

    trace_count = int(manifest.get("trace_count") or len(trace_ids))
    return {
        "trace_count": trace_count,
        "dataset_id_counts": dict(sorted(dataset_counts.items())),
        "dataset_family_count": len(dataset_counts),
        "regime_bucket_counts": dict(sorted(regime_counts.items())),
        "regime_bucket_count": len(regime_counts),
        "split_sample_counts": split_counts,
        "split_policy": manifest.get("split_policy"),
        "diagnostic_only": manifest.get("diagnostic_only"),
        "not_benchmark": manifest.get("not_benchmark"),
    }


def _distribution_report(
    samples_by_split: Mapping[str, Sequence[Mapping[str, object]]],
    training_report: Mapping[str, object],
    offline_report: Mapping[str, object],
) -> Mapping[str, object]:
    validation_teacher = _teacher_distribution(samples_by_split[VALIDATION_SPLIT])
    ood_teacher = _teacher_distribution(samples_by_split[OOD_SPLIT])
    validation_metrics = _mapping(offline_report.get("validation_metrics"))
    ood_metrics = _mapping(offline_report.get("ood_diagnostic_metrics"))
    validation_pred = _int_distribution(validation_metrics.get("prediction_distribution"))
    ood_pred = _int_distribution(ood_metrics.get("prediction_distribution"))

    validation_tvd = _total_variation_distance(validation_pred, validation_teacher)
    ood_tvd = _total_variation_distance(ood_pred, ood_teacher)
    validation_entropy_ratio = _entropy_ratio(validation_pred, validation_teacher)
    ood_entropy_ratio = _entropy_ratio(ood_pred, ood_teacher)

    warnings = []
    warnings.extend(_dominance_warnings("validation teacher", validation_teacher))
    warnings.extend(_dominance_warnings("validation prediction", validation_pred))
    warnings.extend(_dominance_warnings("OOD teacher", ood_teacher))
    warnings.extend(_dominance_warnings("OOD prediction", ood_pred))
    if validation_tvd is not None and validation_tvd > 0.25:
        warnings.append("validation prediction distribution differs from teacher distribution with TVD > 0.25")
    if ood_tvd is not None and ood_tvd > 0.25:
        warnings.append("OOD prediction distribution differs from teacher distribution with TVD > 0.25")
    if validation_entropy_ratio is not None and validation_entropy_ratio < 0.60:
        warnings.append("validation prediction entropy ratio is below 0.60")
    if ood_entropy_ratio is not None and ood_entropy_ratio < 0.60:
        warnings.append("OOD prediction entropy ratio is below 0.60")

    return {
        "validation_teacher_distribution": validation_teacher,
        "validation_prediction_distribution": validation_pred,
        "ood_teacher_distribution": ood_teacher,
        "ood_prediction_distribution": ood_pred,
        "validation_total_variation_distance": validation_tvd,
        "ood_total_variation_distance": ood_tvd,
        "validation_entropy_ratio": validation_entropy_ratio,
        "ood_entropy_ratio": ood_entropy_ratio,
        "training_validation_prediction_distribution": _int_distribution(
            _mapping(training_report.get("validation_metrics")).get("prediction_distribution")
        ),
        "warnings": warnings,
    }


def _training_summary(training_report: Mapping[str, object]) -> Mapping[str, object]:
    return {
        "device": training_report.get("device"),
        "epochs": training_report.get("epochs"),
        "batch_size": training_report.get("batch_size"),
        "loss_last": training_report.get("loss_last"),
        "loss_mean": training_report.get("loss_mean"),
        "train_metrics": training_report.get("train_metrics"),
        "validation_metrics": training_report.get("validation_metrics"),
        "controller_registered": training_report.get("controller_registered"),
    }


def _validation_summary(offline_report: Mapping[str, object]) -> Mapping[str, object]:
    validation_metrics = _mapping(offline_report.get("validation_metrics"))
    ood_metrics = _mapping(offline_report.get("ood_diagnostic_metrics"))
    return {
        "status": offline_report.get("status"),
        "validation_valid_action_rate": validation_metrics.get("valid_action_rate"),
        "ood_valid_action_rate": ood_metrics.get("valid_action_rate"),
        "validation_teacher_agreement": validation_metrics.get("teacher_agreement"),
        "ood_teacher_agreement": ood_metrics.get("teacher_agreement"),
    }


def _underrepresentation_warnings(dataset_summary: Mapping[str, object]) -> list[str]:
    warnings = []
    trace_count = max(int(dataset_summary.get("trace_count") or 0), 1)
    for dataset_id, count in _mapping(dataset_summary.get("dataset_id_counts")).items():
        if int(count) / float(trace_count) < 0.05:
            warnings.append("dataset family {0} is below 5% of trace count".format(dataset_id))
    for regime, count in _mapping(dataset_summary.get("regime_bucket_counts")).items():
        if int(count) / float(trace_count) < 0.05:
            warnings.append("regime bucket {0} is below 5% of trace count".format(regime))
    return warnings


def _teacher_distribution(samples: Sequence[Mapping[str, object]]) -> Mapping[str, int]:
    counts = Counter()
    for sample in samples:
        label = _mapping(sample.get("label"))
        if "teacher_action" in label:
            counts[str(int(label["teacher_action"]))] += 1
    return dict(sorted(counts.items()))


def _int_distribution(value: object) -> Mapping[str, int]:
    if not isinstance(value, Mapping):
        return {}
    return {
        str(key): int(count)
        for key, count in sorted(value.items(), key=lambda item: str(item[0]))
    }


def _total_variation_distance(predicted: Mapping[str, int], teacher: Mapping[str, int]) -> float | None:
    if not predicted or not teacher:
        return None
    pred_total = float(sum(predicted.values()))
    teacher_total = float(sum(teacher.values()))
    if pred_total <= 0.0 or teacher_total <= 0.0:
        return None
    keys = set(predicted) | set(teacher)
    return 0.5 * sum(
        abs((predicted.get(key, 0) / pred_total) - (teacher.get(key, 0) / teacher_total))
        for key in keys
    )


def _entropy_ratio(predicted: Mapping[str, int], teacher: Mapping[str, int]) -> float | None:
    if not predicted or not teacher:
        return None
    teacher_entropy = _entropy(teacher)
    predicted_entropy = _entropy(predicted)
    if teacher_entropy <= 1e-12:
        return 1.0 if predicted_entropy <= 1e-12 else 0.0
    return predicted_entropy / teacher_entropy


def _entropy(distribution: Mapping[str, int]) -> float:
    total = float(sum(distribution.values()))
    if total <= 0.0:
        return 0.0
    entropy = 0.0
    for count in distribution.values():
        if count <= 0:
            continue
        probability = count / total
        entropy -= probability * math.log(probability)
    return entropy


def _dominance_warnings(name: str, distribution: Mapping[str, int]) -> list[str]:
    total = sum(distribution.values())
    if total <= 0:
        return []
    key, count = max(distribution.items(), key=lambda item: item[1])
    share = count / float(total)
    if share >= 0.80:
        return ["{0} distribution is dominated by action {1} ({2:.1%})".format(name, key, share)]
    return []


def _no_nan_inf(values: object) -> bool:
    if isinstance(values, bool) or values is None:
        return True
    if isinstance(values, (int, float)):
        return math.isfinite(float(values))
    if isinstance(values, Mapping):
        return all(_no_nan_inf(value) for value in values.values())
    if isinstance(values, (str, bytes)):
        return True
    if isinstance(values, Iterable):
        return all(_no_nan_inf(value) for value in values)
    return True


def _forbidden_repo_artifacts(repo_root: Path) -> list[str]:
    if not repo_root.is_dir():
        return ["repo_root_missing:{0}".format(repo_root)]
    offenders = []
    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        relative_parts = path.relative_to(repo_root).parts
        if any(part in IGNORED_REPO_DIRS for part in relative_parts):
            continue
        if path.suffix.lower() in FORBIDDEN_ARTIFACT_SUFFIXES:
            offenders.append(str(path.relative_to(repo_root)).replace("\\", "/"))
    return sorted(offenders)


def _protected_git_changes(repo_root: Path) -> list[str]:
    if not (repo_root / ".git").exists():
        return []
    completed = subprocess.run(
        ["git", "status", "--short", "--untracked-files=all"],
        cwd=repo_root,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        return ["git_status_failed:{0}".format(completed.stderr.strip() or completed.stdout.strip())]
    protected = []
    for line in completed.stdout.splitlines():
        if not line.strip():
            continue
        path_text = line[3:].strip().replace("\\", "/")
        if " -> " in path_text:
            candidates = [part.strip() for part in path_text.split(" -> ")]
        else:
            candidates = [path_text]
        if any(candidate.startswith(PROTECTED_CHANGE_PREFIXES) for candidate in candidates):
            protected.append(line)
    return protected


def _gate(passed: bool, details: object) -> Mapping[str, object]:
    return {
        "status": "PASS" if bool(passed) else "FAIL",
        "passed": bool(passed),
        "details": details,
    }


def _gate_from_optional(value: bool | None, details: object) -> Mapping[str, object]:
    if value is None:
        return {
            "status": "UNKNOWN",
            "passed": None,
            "details": details,
        }
    return _gate(bool(value), details)


def _environmental_gate(
    explicit_value: bool | None,
    checked_value: bool | None,
    checked_details: object,
    unchecked_details: object,
) -> Mapping[str, object]:
    if explicit_value is not None:
        return _gate(bool(explicit_value), {"source": "explicit", "details": checked_details})
    if checked_value is not None:
        return _gate(bool(checked_value), {"source": "repo_scan", "details": checked_details})
    return {
        "status": "UNKNOWN",
        "passed": None,
        "details": unchecked_details,
    }


def _read_optional_json(path: Path) -> Mapping[str, object]:
    if not path.is_file():
        return {}
    return read_json(path)


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _sequence(value: object) -> Sequence[object]:
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return value
    return ()


def _float_eq(value: object, expected: float) -> bool:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return False
    return math.isclose(parsed, expected, rel_tol=0.0, abs_tol=1e-12)

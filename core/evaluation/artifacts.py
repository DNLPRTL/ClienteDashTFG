from __future__ import annotations

import csv
import json
import shutil
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping, Sequence

from core.evaluation.qoe import (
    LOG_QOE_VERSION,
    SegmentQoEInput,
    compute_linear_qoe,
    compute_log_qoe,
)


DRY_RUN_SEGMENTS_FILENAME = "trace_dry_run_segments.csv"
DRY_RUN_SUMMARY_FILENAME = "trace_dry_run_summary.json"
DRY_RUN_MANIFEST_FILENAME = "trace_dry_run_manifest.json"
QOE_SEGMENT_REWARDS_FILENAME = "qoe_segment_rewards.csv"
QOE_RUN_SUMMARY_FILENAME = "qoe_run_summary.json"
QOE_ARTIFACT_MANIFEST_FILENAME = "qoe_artifact_manifest.json"
REQUIRED_QOE_SEGMENT_COLUMNS = ("representation_bitrate_kbps", "rebuffer_s")
GATE_USE_FOR_EVAL = "use_for_eval"
GATE_DIAGNOSTIC_ONLY = "diagnostic_only"
GATE_DO_NOT_USE_FOR_EVAL = "do_not_use_for_eval"


class QoEArtifactError(ValueError):
    """Raised when dry-run-like artifacts cannot be mapped to QoE inputs."""


@dataclass(frozen=True)
class QoEArtifactComputationResult:
    output_dir: str
    qoe_segment_rewards_path: str
    qoe_run_summary_path: str
    qoe_artifact_manifest_path: str
    segment_count: int
    session_eval_gate: str
    gate_reasons: tuple[str, ...]


def load_segment_qoe_inputs_from_csv(path: str | Path) -> list[SegmentQoEInput]:
    csv_path = Path(path)
    try:
        with csv_path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None:
                raise QoEArtifactError("{0}: missing CSV header".format(csv_path))
            _require_columns(reader.fieldnames, REQUIRED_QOE_SEGMENT_COLUMNS, csv_path)
            segments = []
            for row_index, row in enumerate(reader, start=2):
                try:
                    bitrate = float(row["representation_bitrate_kbps"])
                    rebuffer = float(row["rebuffer_s"])
                except (TypeError, ValueError) as exc:
                    raise QoEArtifactError(
                        "{0}: invalid QoE numeric input at row {1}".format(csv_path, row_index)
                    ) from exc
                try:
                    segments.append(SegmentQoEInput(bitrate_kbps=bitrate, rebuffer_s=rebuffer))
                except ValueError as exc:
                    raise QoEArtifactError("{0}: {1}".format(csv_path, exc)) from exc
    except OSError as exc:
        raise QoEArtifactError("{0}: cannot read segments CSV".format(csv_path)) from exc
    if not segments:
        raise QoEArtifactError("{0}: no segment rows".format(csv_path))
    return segments


def compute_qoe_summary_from_segments_csv(
    segments_csv_path: str | Path,
    expected_segment_count: int | None = None,
    min_bitrate_kbps: float | None = None,
) -> dict[str, object]:
    segments = load_segment_qoe_inputs_from_csv(segments_csv_path)
    linear = compute_linear_qoe(segments)
    summary = _qoe_result_to_summary(linear)
    if min_bitrate_kbps is not None:
        summary["qoe_log_v1"] = _qoe_result_to_summary(
            compute_log_qoe(segments, min_bitrate_kbps=min_bitrate_kbps)
        )
        summary["secondary_metric_versions"] = [LOG_QOE_VERSION]
    else:
        summary["secondary_metric_versions"] = []
    summary["segment_count"] = len(segments)
    if expected_segment_count is not None:
        summary["expected_segment_count"] = int(expected_segment_count)
        summary["session_completed"] = int(expected_segment_count) == len(segments)
    else:
        summary["expected_segment_count"] = None
        summary["session_completed"] = True
    return summary


def compute_qoe_artifacts_from_dry_run(
    dry_run_dir: str | Path,
    output_dir: str | Path,
    expected_segment_count: int | None = None,
    min_bitrate_kbps: float | None = None,
    overwrite: bool = False,
) -> QoEArtifactComputationResult:
    source_dir = Path(dry_run_dir)
    target_dir = Path(output_dir)
    segments_csv = source_dir / DRY_RUN_SEGMENTS_FILENAME
    source_summary_path = source_dir / DRY_RUN_SUMMARY_FILENAME
    source_manifest_path = source_dir / DRY_RUN_MANIFEST_FILENAME
    _require_file(segments_csv)
    _require_file(source_summary_path)
    _require_file(source_manifest_path)

    if target_dir.exists():
        if not overwrite:
            raise QoEArtifactError("{0}: output dir exists; pass overwrite".format(target_dir))
        shutil.rmtree(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    source_summary = _read_json_object(source_summary_path)
    source_manifest = _read_json_object(source_manifest_path)
    resolved_expected = _resolve_expected_segment_count(expected_segment_count, source_summary, source_manifest)
    segments = load_segment_qoe_inputs_from_csv(segments_csv)
    linear = compute_linear_qoe(segments)
    log_result = compute_log_qoe(segments, min_bitrate_kbps=min_bitrate_kbps) if min_bitrate_kbps is not None else None
    gate_reasons = _derive_gate_reasons(
        segment_count=len(segments),
        expected_segment_count=resolved_expected,
        source_summary=source_summary,
        source_manifest=source_manifest,
        segments_csv=segments_csv,
    )
    session_eval_gate = GATE_DO_NOT_USE_FOR_EVAL if gate_reasons else GATE_USE_FOR_EVAL

    rewards_path = target_dir / QOE_SEGMENT_REWARDS_FILENAME
    summary_path = target_dir / QOE_RUN_SUMMARY_FILENAME
    manifest_path = target_dir / QOE_ARTIFACT_MANIFEST_FILENAME
    _write_segment_rewards(rewards_path, segments, linear)

    qoe_summary = _qoe_result_to_summary(linear)
    qoe_summary.update(
        {
            "eval_phase": "phase3_5_qoe_artifact_computation",
            "segment_count": len(segments),
            "expected_segment_count": resolved_expected,
            "session_completed": (
                True if resolved_expected is None else len(segments) == resolved_expected
            ),
            "session_eval_gate": session_eval_gate,
            "gate_reasons": gate_reasons,
            "startup_delay_s": source_summary.get("startup_delay_s"),
            "startup_delay_policy": "report_only",
            "vmaf_policy": "deferred_artifact_dependent",
            "outputs_are_benchmark_results": False,
            "benchmark_performed": False,
            "ranking_performed": False,
            "no_final_ranking": True,
            "ia_training_performed": False,
        }
    )
    if log_result is not None:
        qoe_summary["qoe_log_v1"] = _qoe_result_to_summary(log_result)
        qoe_summary["secondary_metric_versions"] = [LOG_QOE_VERSION]
    else:
        qoe_summary["secondary_metric_versions"] = []
    _write_json(summary_path, qoe_summary)

    artifact_manifest = {
        "schema_id": "qoe_artifact_manifest_v1",
        "phase": "phase3_5_rebuild",
        "eval_phase": "phase3_5_qoe_artifact_computation",
        "source_dry_run_dir": str(source_dir),
        "source_segments_csv": str(segments_csv),
        "source_summary_json": str(source_summary_path),
        "source_manifest_json": str(source_manifest_path),
        "outputs": {
            "qoe_segment_rewards": str(rewards_path),
            "qoe_run_summary": str(summary_path),
        },
        "qoe_formula_version": linear.formula_version,
        "session_eval_gate": session_eval_gate,
        "gate_reasons": gate_reasons,
        "outputs_are_benchmark_results": False,
        "benchmark_performed": False,
        "ranking_performed": False,
        "no_final_ranking": True,
        "ia_training_performed": False,
        "source_flags": {
            "source_claimed_benchmark": bool(source_manifest.get("outputs_are_benchmark_results", False)),
            "source_no_final_ranking": source_manifest.get("no_final_ranking"),
            "source_final_qoe_reward_defined": source_manifest.get("final_qoe_reward_defined"),
        },
    }
    _write_json(manifest_path, artifact_manifest)

    return QoEArtifactComputationResult(
        output_dir=str(target_dir),
        qoe_segment_rewards_path=str(rewards_path),
        qoe_run_summary_path=str(summary_path),
        qoe_artifact_manifest_path=str(manifest_path),
        segment_count=len(segments),
        session_eval_gate=session_eval_gate,
        gate_reasons=tuple(gate_reasons),
    )


def _require_file(path: Path) -> None:
    if not path.is_file():
        raise QoEArtifactError("{0}: required file missing".format(path))


def _read_json_object(path: Path) -> dict[str, object]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise QoEArtifactError("{0}: cannot read JSON object".format(path)) from exc
    if not isinstance(data, dict):
        raise QoEArtifactError("{0}: JSON root must be an object".format(path))
    return data


def _write_json(path: Path, data: Mapping[str, object]) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _require_columns(fieldnames: Sequence[str], required: Sequence[str], path: Path) -> None:
    missing = [column for column in required if column not in fieldnames]
    if missing:
        raise QoEArtifactError("{0}: missing columns {1}".format(path, ", ".join(missing)))


def _resolve_expected_segment_count(
    explicit_expected: int | None,
    source_summary: Mapping[str, object],
    source_manifest: Mapping[str, object],
) -> int | None:
    if explicit_expected is not None:
        return int(explicit_expected)
    for source in (source_summary, source_manifest):
        for key in ("expected_segment_count", "segment_count_expected", "total_segments_expected"):
            value = source.get(key)
            if value is not None:
                return int(value)
    return None


def _derive_gate_reasons(
    segment_count: int,
    expected_segment_count: int | None,
    source_summary: Mapping[str, object],
    source_manifest: Mapping[str, object],
    segments_csv: Path,
) -> list[str]:
    reasons = []
    if expected_segment_count is not None and segment_count != expected_segment_count:
        reasons.append("incomplete_session")
    if source_summary.get("session_completed") is False:
        _append_unique(reasons, "incomplete_session")
    if source_manifest.get("outputs_are_benchmark_results") is True:
        reasons.append("source_claims_benchmark_result")
    if source_manifest.get("legacy_dry_run") is True:
        reasons.append("legacy_dry_run")
    if source_manifest.get("generated_before_phase_3_5a2") is True:
        reasons.append("generated_before_phase_3_5a2")
    if source_manifest.get("final_qoe_reward_defined") is False:
        _append_unique(reasons, "qoe_formula_not_defined_in_source")
    for gate_key in ("row_eval_gate", "session_eval_gate"):
        gate = source_manifest.get(gate_key)
        if gate == GATE_DO_NOT_USE_FOR_EVAL:
            source_reasons = source_manifest.get("gate_reasons")
            if isinstance(source_reasons, list):
                for reason in source_reasons:
                    _append_unique(reasons, str(reason))
            else:
                _append_unique(reasons, "{0}_source_do_not_use_for_eval".format(gate_key))
        elif gate == GATE_DIAGNOSTIC_ONLY:
            _append_unique(reasons, "{0}_source_diagnostic_only".format(gate_key))
    for row_gate in _row_gate_values(segments_csv):
        if row_gate == GATE_DO_NOT_USE_FOR_EVAL:
            _append_unique(reasons, "row_eval_gate_source_do_not_use_for_eval")
        elif row_gate == GATE_DIAGNOSTIC_ONLY:
            _append_unique(reasons, "row_eval_gate_source_diagnostic_only")
    return reasons


def _row_gate_values(path: Path) -> set[str]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or "row_eval_gate" not in reader.fieldnames:
            return set()
        return {str(row.get("row_eval_gate", "")) for row in reader}


def _append_unique(values: list[str], value: str) -> None:
    if value not in values:
        values.append(value)


def _qoe_result_to_summary(result) -> dict[str, object]:
    data = asdict(result)
    data["segment_rewards"] = list(result.segment_rewards)
    data["segment_quality_utilities"] = list(result.segment_quality_utilities)
    data["segment_smoothness"] = list(result.segment_smoothness)
    return data


def _write_segment_rewards(path: Path, segments: Sequence[SegmentQoEInput], linear_result) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "segment_index",
                "bitrate_kbps",
                "rebuffer_s",
                "quality_mbps",
                "smoothness_mbps",
                "reward_n",
            ],
        )
        writer.writeheader()
        for index, segment in enumerate(segments):
            writer.writerow(
                {
                    "segment_index": index,
                    "bitrate_kbps": segment.bitrate_kbps,
                    "rebuffer_s": segment.rebuffer_s,
                    "quality_mbps": linear_result.segment_quality_utilities[index],
                    "smoothness_mbps": linear_result.segment_smoothness[index],
                    "reward_n": linear_result.segment_rewards[index],
                }
            )

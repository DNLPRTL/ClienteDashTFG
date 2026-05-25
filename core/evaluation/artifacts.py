from __future__ import annotations

import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from core.evaluation.qoe import SegmentQoEInput, compute_linear_qoe, compute_log_qoe


DRY_RUN_SEGMENTS_FILENAME = "trace_dry_run_segments.csv"
DRY_RUN_SUMMARY_FILENAME = "trace_dry_run_summary.json"
DRY_RUN_MANIFEST_FILENAME = "trace_dry_run_manifest.json"
QOE_SEGMENT_REWARDS_FILENAME = "qoe_segment_rewards.csv"
QOE_RUN_SUMMARY_FILENAME = "qoe_run_summary.json"
QOE_ARTIFACT_MANIFEST_FILENAME = "qoe_artifact_manifest.json"
PHASE_3_5C_EVAL_PHASE = "phase3_5c_qoe_artifact_computation"

USE_FOR_EVAL = "use_for_eval"
DIAGNOSTIC_ONLY = "diagnostic_only"
DO_NOT_USE_FOR_EVAL = "do_not_use_for_eval"

REQUIRED_SEGMENT_COLUMNS = (
    "segment_index",
    "representation_bitrate_kbps",
    "rebuffer_s",
    "controller_name",
    "trace_id",
    "row_eval_gate",
    "outputs_are_benchmark_results",
    "final_qoe_reward_defined",
    "no_final_ranking",
)

OPTIONAL_PRESERVED_COLUMNS = (
    "phase",
    "phase_label",
    "schema_version",
    "segment_duration_s",
    "buffer_before_s",
    "buffer_after_s",
    "download_duration_s",
    "measured_throughput_kbps",
)


class QoEArtifactError(ValueError):
    """Raised when QoE artifact computation cannot safely continue."""


@dataclass(frozen=True)
class QoEArtifactComputationResult:
    output_dir: Path
    qoe_segment_rewards_path: Path
    qoe_run_summary_path: Path
    qoe_artifact_manifest_path: Path
    summary: Mapping[str, object]


@dataclass(frozen=True)
class _LoadedSegmentRow:
    segment_index: int
    qoe_input: SegmentQoEInput
    controller_name: str
    trace_id: str
    source_row_eval_gate: str
    source_outputs_are_benchmark_results: bool
    source_final_qoe_reward_defined: bool
    source_no_final_ranking: bool
    raw_row: Mapping[str, str]


@dataclass(frozen=True)
class _LoadedSegmentCsv:
    rows: Tuple[_LoadedSegmentRow, ...]
    fieldnames: Tuple[str, ...]
    input_was_ordered: bool


def load_segment_qoe_inputs_from_csv(segments_csv_path: object) -> Tuple[SegmentQoEInput, ...]:
    """Load dry-run segment rows and return sorted QoE inputs."""
    loaded = _load_segment_rows_from_csv(segments_csv_path)
    return tuple(row.qoe_input for row in loaded.rows)


def compute_qoe_summary_from_segments_csv(
    segments_csv_path: object,
    expected_segment_count: Optional[int] = None,
    min_bitrate_kbps: Optional[float] = None,
    diagnostic_only: bool = False,
) -> Mapping[str, object]:
    """Compute an in-memory QoE run summary from one dry-run segments CSV."""
    loaded = _load_segment_rows_from_csv(segments_csv_path)
    source_paths = {
        "segments": Path(segments_csv_path).name,
        "summary": DRY_RUN_SUMMARY_FILENAME,
        "manifest": DRY_RUN_MANIFEST_FILENAME,
    }
    source_summary: Mapping[str, object] = {}
    source_manifest: Mapping[str, object] = {}
    return _build_run_summary(
        loaded=loaded,
        expected_segment_count=expected_segment_count,
        min_bitrate_kbps=min_bitrate_kbps,
        diagnostic_only=diagnostic_only,
        source_paths=source_paths,
        source_summary=source_summary,
        source_manifest=source_manifest,
    )


def compute_qoe_artifacts_from_dry_run(
    dry_run_dir: object,
    output_dir: object,
    expected_segment_count: Optional[int] = None,
    min_bitrate_kbps: Optional[float] = None,
    overwrite: bool = False,
    diagnostic_only: bool = False,
) -> QoEArtifactComputationResult:
    """Compute QoE artifacts from one existing trace dry-run artifact directory."""
    dry_run_path = _required_directory(dry_run_dir, "dry_run_dir")
    source_paths = {
        "segments": dry_run_path / DRY_RUN_SEGMENTS_FILENAME,
        "summary": dry_run_path / DRY_RUN_SUMMARY_FILENAME,
        "manifest": dry_run_path / DRY_RUN_MANIFEST_FILENAME,
    }
    for label, path in source_paths.items():
        if not path.is_file():
            raise QoEArtifactError("missing source artifact {0}: {1}".format(label, path))

    loaded = _load_segment_rows_from_csv(source_paths["segments"])
    source_summary = _read_json(source_paths["summary"])
    source_manifest = _read_json(source_paths["manifest"])
    resolved_expected_segment_count = _resolve_expected_segment_count(
        expected_segment_count,
        source_summary,
    )
    source_filenames = {
        "segments": source_paths["segments"].name,
        "summary": source_paths["summary"].name,
        "manifest": source_paths["manifest"].name,
    }

    summary = _build_run_summary(
        loaded=loaded,
        expected_segment_count=resolved_expected_segment_count,
        min_bitrate_kbps=min_bitrate_kbps,
        diagnostic_only=diagnostic_only,
        source_paths=source_filenames,
        source_summary=source_summary,
        source_manifest=source_manifest,
    )
    qoe_rows = _build_segment_reward_rows(loaded, summary["session_eval_gate"])
    manifest = _build_qoe_manifest(summary, source_filenames)

    output_path = _prepare_output_dir(output_dir, overwrite=overwrite)
    segment_rewards_path = output_path / QOE_SEGMENT_REWARDS_FILENAME
    run_summary_path = output_path / QOE_RUN_SUMMARY_FILENAME
    artifact_manifest_path = output_path / QOE_ARTIFACT_MANIFEST_FILENAME

    _write_segment_rewards_csv(segment_rewards_path, qoe_rows, loaded.fieldnames)
    _write_json(run_summary_path, summary)
    _write_json(artifact_manifest_path, manifest)

    return QoEArtifactComputationResult(
        output_dir=output_path,
        qoe_segment_rewards_path=segment_rewards_path,
        qoe_run_summary_path=run_summary_path,
        qoe_artifact_manifest_path=artifact_manifest_path,
        summary=summary,
    )


def _load_segment_rows_from_csv(segments_csv_path: object) -> _LoadedSegmentCsv:
    path = Path(segments_csv_path)
    if not path.is_file():
        raise QoEArtifactError("segments CSV not found: {0}".format(path))

    try:
        with path.open("r", newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            fieldnames = tuple(reader.fieldnames or ())
            _validate_required_columns(fieldnames)
            raw_rows = list(reader)
    except OSError as exc:
        raise QoEArtifactError(str(exc)) from exc

    if not raw_rows:
        raise QoEArtifactError("segments CSV is empty: {0}".format(path))

    parsed_rows = []
    seen_segment_indices = set()
    controller_names = set()
    trace_ids = set()

    for row_number, row in enumerate(raw_rows, start=2):
        segment_index = _parse_segment_index(row.get("segment_index"), row_number=row_number)
        if segment_index in seen_segment_indices:
            raise QoEArtifactError("duplicate segment_index: {0}".format(segment_index))
        seen_segment_indices.add(segment_index)

        bitrate_kbps = _parse_finite_positive_float(
            row.get("representation_bitrate_kbps"),
            "representation_bitrate_kbps",
            row_number=row_number,
        )
        rebuffer_s = _parse_finite_non_negative_float(
            row.get("rebuffer_s"),
            "rebuffer_s",
            row_number=row_number,
        )
        controller_name = _required_text(row.get("controller_name"), "controller_name", row_number=row_number)
        trace_id = _required_text(row.get("trace_id"), "trace_id", row_number=row_number)
        row_eval_gate = _required_text(row.get("row_eval_gate"), "row_eval_gate", row_number=row_number)
        outputs_are_benchmark_results = _parse_bool(
            row.get("outputs_are_benchmark_results"),
            "outputs_are_benchmark_results",
            row_number=row_number,
        )
        final_qoe_reward_defined = _parse_bool(
            row.get("final_qoe_reward_defined"),
            "final_qoe_reward_defined",
            row_number=row_number,
        )
        no_final_ranking = _parse_bool(
            row.get("no_final_ranking"),
            "no_final_ranking",
            row_number=row_number,
        )

        controller_names.add(controller_name)
        trace_ids.add(trace_id)
        parsed_rows.append(
            _LoadedSegmentRow(
                segment_index=segment_index,
                qoe_input=SegmentQoEInput(
                    bitrate_kbps=bitrate_kbps,
                    rebuffer_s=rebuffer_s,
                ),
                controller_name=controller_name,
                trace_id=trace_id,
                source_row_eval_gate=row_eval_gate,
                source_outputs_are_benchmark_results=outputs_are_benchmark_results,
                source_final_qoe_reward_defined=final_qoe_reward_defined,
                source_no_final_ranking=no_final_ranking,
                raw_row=dict(row),
            )
        )

    if len(controller_names) != 1:
        raise QoEArtifactError("multiple controller_name values in one CSV")
    if len(trace_ids) != 1:
        raise QoEArtifactError("multiple trace_id values in one CSV")

    input_indices = [row.segment_index for row in parsed_rows]
    sorted_rows = tuple(sorted(parsed_rows, key=lambda row: row.segment_index))
    return _LoadedSegmentCsv(
        rows=sorted_rows,
        fieldnames=fieldnames,
        input_was_ordered=input_indices == sorted(input_indices),
    )


def _build_run_summary(
    loaded: _LoadedSegmentCsv,
    expected_segment_count: Optional[int],
    min_bitrate_kbps: Optional[float],
    diagnostic_only: bool,
    source_paths: Mapping[str, object],
    source_summary: Mapping[str, object],
    source_manifest: Mapping[str, object],
) -> Dict[str, object]:
    inputs = tuple(row.qoe_input for row in loaded.rows)
    try:
        linear = compute_linear_qoe(inputs)
    except ValueError as exc:
        raise QoEArtifactError(str(exc)) from exc

    completed_segment_count = len(inputs)
    session_completed = (
        True
        if expected_segment_count is None
        else completed_segment_count == expected_segment_count
    )
    gate_reasons = _gate_reasons(
        loaded=loaded,
        expected_segment_count=expected_segment_count,
        session_completed=session_completed,
        source_summary=source_summary,
        source_manifest=source_manifest,
    )
    if gate_reasons:
        session_eval_gate = DO_NOT_USE_FOR_EVAL
    elif diagnostic_only:
        session_eval_gate = DIAGNOSTIC_ONLY
        gate_reasons = ("diagnostic_only_requested",)
    else:
        session_eval_gate = USE_FOR_EVAL

    controller_name = loaded.rows[0].controller_name
    trace_id = loaded.rows[0].trace_id
    summary: Dict[str, object] = {
        "artifact_type": "qoe_run_summary",
        "eval_phase": PHASE_3_5C_EVAL_PHASE,
        "qoe_formula_version": "qoe_linear_v1",
        "primary_session_metric": "qoe_linear_mean",
        "outputs_are_benchmark_results": False,
        "no_final_ranking": True,
        "trace_id": trace_id,
        "controller_name": controller_name,
        "completed_segment_count": completed_segment_count,
        "expected_segment_count": expected_segment_count,
        "session_completed": session_completed,
        "session_eval_gate": session_eval_gate,
        "gate_reasons": list(gate_reasons),
        "qoe_linear_sum": linear.qoe_sum,
        "qoe_linear_mean": linear.qoe_mean,
        "quality_utility_sum": linear.quality_utility_sum,
        "avg_quality_mbps": linear.avg_quality_mbps,
        "avg_bitrate_kbps": linear.avg_bitrate_kbps,
        "total_rebuffer_s": linear.total_rebuffer_s,
        "rebuffer_penalty": linear.rebuffer_penalty,
        "smoothness_penalty": linear.smoothness_penalty,
        "stall_event_count": linear.stall_event_count,
        "quality_switch_count": linear.quality_switch_count,
        "up_switch_count": linear.up_switch_count,
        "down_switch_count": linear.down_switch_count,
        "total_switch_magnitude_kbps": linear.total_switch_magnitude_kbps,
        "avg_switch_magnitude_kbps": linear.avg_switch_magnitude_kbps,
        "source_segments_filename": str(source_paths["segments"]),
        "source_summary_filename": str(source_paths["summary"]),
        "source_manifest_filename": str(source_paths["manifest"]),
        "source_input_was_ordered": loaded.input_was_ordered,
        "source_row_eval_gates": sorted({row.source_row_eval_gate for row in loaded.rows}),
        "source_outputs_are_benchmark_results": any(
            row.source_outputs_are_benchmark_results for row in loaded.rows
        ),
        "source_final_qoe_reward_defined": all(
            row.source_final_qoe_reward_defined for row in loaded.rows
        ),
    }

    if min_bitrate_kbps is None:
        summary["log_qoe_computed"] = False
    else:
        try:
            log_result = compute_log_qoe(inputs, min_bitrate_kbps=min_bitrate_kbps)
        except ValueError as exc:
            raise QoEArtifactError(str(exc)) from exc
        summary.update(
            {
                "log_qoe_computed": True,
                "qoe_log_sum": log_result.qoe_sum,
                "qoe_log_mean": log_result.qoe_mean,
                "qoe_log_min_bitrate_kbps": float(min_bitrate_kbps),
            }
        )

    return summary


def _gate_reasons(
    loaded: _LoadedSegmentCsv,
    expected_segment_count: Optional[int],
    session_completed: bool,
    source_summary: Mapping[str, object],
    source_manifest: Mapping[str, object],
) -> Tuple[str, ...]:
    reasons: List[str] = []

    if any(row.source_row_eval_gate != USE_FOR_EVAL for row in loaded.rows):
        reasons.extend(("legacy_dry_run", "generated_before_phase_3_5a2"))
        if not all(row.source_final_qoe_reward_defined for row in loaded.rows):
            reasons.append("qoe_formula_not_defined")
    if any(row.source_outputs_are_benchmark_results for row in loaded.rows):
        reasons.append("source_artifact_conflict")
    if not all(row.source_no_final_ranking for row in loaded.rows):
        reasons.append("source_artifact_conflict")
    if expected_segment_count is not None and not session_completed:
        reasons.append("incomplete_session")
    if _source_has_runtime_error(source_summary) or _source_has_runtime_error(source_manifest):
        reasons.append("runtime_error")

    return tuple(_dedupe_preserving_order(reasons))


def _build_segment_reward_rows(
    loaded: _LoadedSegmentCsv,
    session_eval_gate: object,
) -> List[Dict[str, object]]:
    rows = []
    previous_quality = None

    for row in loaded.rows:
        quality_utility_mbps = row.qoe_input.bitrate_kbps / 1000.0
        smoothness_penalty = (
            0.0
            if previous_quality is None
            else abs(quality_utility_mbps - previous_quality)
        )
        rebuffer_penalty = 4.3 * row.qoe_input.rebuffer_s
        segment_reward = quality_utility_mbps - rebuffer_penalty - smoothness_penalty
        row_eval_gate = (
            USE_FOR_EVAL
            if row.source_row_eval_gate == USE_FOR_EVAL and session_eval_gate == USE_FOR_EVAL
            else DO_NOT_USE_FOR_EVAL
        )

        output_row: Dict[str, object] = {
            "segment_index": row.segment_index,
            "trace_id": row.trace_id,
            "controller_name": row.controller_name,
            "qoe_formula_version": "qoe_linear_v1",
            "bitrate_kbps": row.qoe_input.bitrate_kbps,
            "rebuffer_s": row.qoe_input.rebuffer_s,
            "quality_utility_mbps": quality_utility_mbps,
            "smoothness_penalty": smoothness_penalty,
            "rebuffer_penalty": rebuffer_penalty,
            "segment_reward": segment_reward,
            "source_row_eval_gate": row.source_row_eval_gate,
            "row_eval_gate": row_eval_gate,
            "eval_phase": PHASE_3_5C_EVAL_PHASE,
            "outputs_are_benchmark_results": "false",
            "no_final_ranking": "true",
        }
        for column in OPTIONAL_PRESERVED_COLUMNS:
            if column in row.raw_row:
                output_row[column] = row.raw_row[column]
        rows.append(output_row)
        previous_quality = quality_utility_mbps

    return rows


def _build_qoe_manifest(
    summary: Mapping[str, object],
    source_filenames: Mapping[str, object],
) -> Mapping[str, object]:
    return {
        "artifact_type": "qoe_artifact_manifest",
        "eval_phase": PHASE_3_5C_EVAL_PHASE,
        "outputs_are_benchmark_results": False,
        "no_final_ranking": True,
        "session_eval_gate": summary["session_eval_gate"],
        "gate_reasons": summary["gate_reasons"],
        "artifacts": {
            "qoe_segment_rewards": QOE_SEGMENT_REWARDS_FILENAME,
            "qoe_run_summary": QOE_RUN_SUMMARY_FILENAME,
        },
        "source_artifacts": {
            "trace_dry_run_segments": str(source_filenames["segments"]),
            "trace_dry_run_summary": str(source_filenames["summary"]),
            "trace_dry_run_manifest": str(source_filenames["manifest"]),
        },
    }


def _write_segment_rewards_csv(
    path: Path,
    rows: Sequence[Mapping[str, object]],
    source_fieldnames: Sequence[str],
) -> None:
    base_fieldnames = [
        "segment_index",
        "trace_id",
        "controller_name",
        "qoe_formula_version",
        "bitrate_kbps",
        "rebuffer_s",
        "quality_utility_mbps",
        "smoothness_penalty",
        "rebuffer_penalty",
        "segment_reward",
        "source_row_eval_gate",
        "row_eval_gate",
        "eval_phase",
        "outputs_are_benchmark_results",
        "no_final_ranking",
    ]
    optional_fieldnames = [
        column
        for column in OPTIONAL_PRESERVED_COLUMNS
        if column in source_fieldnames and column not in base_fieldnames
    ]
    fieldnames = base_fieldnames + optional_fieldnames

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def _write_json(path: Path, payload: Mapping[str, object]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _read_json(path: Path) -> Mapping[str, object]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise QoEArtifactError(str(exc)) from exc
    if not isinstance(payload, dict):
        raise QoEArtifactError("JSON artifact must contain an object: {0}".format(path))
    return payload


def _validate_required_columns(fieldnames: Sequence[str]) -> None:
    missing = [column for column in REQUIRED_SEGMENT_COLUMNS if column not in fieldnames]
    if missing:
        raise QoEArtifactError("missing_required_column: {0}".format(", ".join(missing)))


def _parse_segment_index(raw_value: object, row_number: int) -> int:
    text = _required_text(raw_value, "segment_index", row_number=row_number)
    try:
        segment_index = int(text)
    except ValueError as exc:
        raise QoEArtifactError("invalid segment_index at CSV row {0}".format(row_number)) from exc
    if segment_index < 0:
        raise QoEArtifactError("invalid segment_index at CSV row {0}".format(row_number))
    return segment_index


def _parse_finite_positive_float(raw_value: object, name: str, row_number: int) -> float:
    value = _parse_finite_float(raw_value, name, row_number=row_number)
    if value <= 0.0:
        raise QoEArtifactError("invalid {0} at CSV row {1}".format(name, row_number))
    return value


def _parse_finite_non_negative_float(raw_value: object, name: str, row_number: int) -> float:
    value = _parse_finite_float(raw_value, name, row_number=row_number)
    if value < 0.0:
        raise QoEArtifactError("invalid {0} at CSV row {1}".format(name, row_number))
    return value


def _parse_finite_float(raw_value: object, name: str, row_number: int) -> float:
    text = _required_text(raw_value, name, row_number=row_number)
    try:
        value = float(text)
    except ValueError as exc:
        raise QoEArtifactError("invalid {0} at CSV row {1}".format(name, row_number)) from exc
    if not math.isfinite(value):
        raise QoEArtifactError("invalid {0} at CSV row {1}".format(name, row_number))
    return value


def _required_text(raw_value: object, name: str, row_number: int) -> str:
    if raw_value is None:
        raise QoEArtifactError("missing_required_column: {0}".format(name))
    text = str(raw_value).strip()
    if not text:
        raise QoEArtifactError("empty {0} at CSV row {1}".format(name, row_number))
    return text


def _parse_bool(raw_value: object, name: str, row_number: int) -> bool:
    text = _required_text(raw_value, name, row_number=row_number).lower()
    if text in ("true", "1", "yes"):
        return True
    if text in ("false", "0", "no"):
        return False
    raise QoEArtifactError("invalid {0} at CSV row {1}".format(name, row_number))


def _resolve_expected_segment_count(
    expected_segment_count: Optional[int],
    source_summary: Mapping[str, object],
) -> Optional[int]:
    if expected_segment_count is not None:
        return _validate_expected_segment_count(expected_segment_count)

    source_count = source_summary.get("segment_count")
    if source_count is None:
        return None
    return _validate_expected_segment_count(source_count)


def _validate_expected_segment_count(value: object) -> int:
    if isinstance(value, bool):
        raise QoEArtifactError("expected_segment_count must be a non-negative integer")
    try:
        parsed = int(value)
    except (TypeError, ValueError) as exc:
        raise QoEArtifactError("expected_segment_count must be a non-negative integer") from exc
    if parsed < 0:
        raise QoEArtifactError("expected_segment_count must be a non-negative integer")
    return parsed


def _source_has_runtime_error(source_payload: Mapping[str, object]) -> bool:
    failure_reason = source_payload.get("failure_reason")
    if failure_reason is None:
        return False
    text = str(failure_reason).strip().lower()
    return bool(text) and text not in ("none", "null", "ok")


def _required_directory(path_value: object, name: str) -> Path:
    if path_value is None or not str(path_value).strip():
        raise QoEArtifactError("{0} is required".format(name))
    path = Path(path_value)
    if not path.is_dir():
        raise QoEArtifactError("{0} is not a directory: {1}".format(name, path))
    return path


def _prepare_output_dir(output_dir: object, overwrite: bool) -> Path:
    if output_dir is None or not str(output_dir).strip():
        raise QoEArtifactError("output_dir is required")
    path = Path(output_dir)
    if path.exists() and not path.is_dir():
        raise QoEArtifactError("output_dir exists and is not a directory: {0}".format(path))
    if path.exists() and not overwrite and any(path.iterdir()):
        raise QoEArtifactError("output_dir is not empty; pass --overwrite to replace QoE artifact files")
    path.mkdir(parents=True, exist_ok=True)
    return path


def _dedupe_preserving_order(values: Iterable[str]) -> List[str]:
    seen = set()
    result = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result

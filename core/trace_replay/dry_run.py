"""Controlled trace-driven dry-run harness for Phase 3.4C.

This module exercises existing controllers against normalized traces through
the Phase 3.4B network model. Outputs are integration dry-run artifacts only:
they are not benchmark results and they do not define final QoE/reward.
"""

from __future__ import annotations

import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from numbers import Real
from typing import Mapping, Sequence, Tuple

from core.trace_replay.controller_adapter import ControllerAdapterError
from core.trace_replay.fake_replay_adapter import TraceDrivenFakeReplayAdapter
from core.trace_replay.network_model import END_POLICY_FAIL, END_POLICY_LOOP, TraceDrivenNetworkModel, TraceReplayError


PHASE_LABEL = "3.4C"
EVAL_PHASE = "phase3_4c_dry_run"
ROW_EVAL_GATE = "do_not_use_for_eval"
NON_BENCHMARK_NOTES = (
    "Controlled Phase 3.4C integration dry-run only; do not use for benchmark ranking, "
    "final QoE/reward, tuning, IA/RL training or thesis performance claims."
)


class TraceDryRunError(ValueError):
    """Raised when the controlled dry-run cannot be executed safely."""


@dataclass(frozen=True)
class Representation:
    index: int
    bitrate_kbps: float
    label: str


@dataclass(frozen=True)
class SegmentDryRunRecord:
    segment_index: int
    representation_index: int
    representation_bitrate_kbps: float
    segment_duration_s: float
    segment_size_bytes: int
    download_start_time_s: float
    download_end_time_s: float
    download_duration_s: float
    measured_throughput_kbps: float
    buffer_before_s: float
    buffer_after_s: float
    rebuffer_s: float
    controller_name: str
    trace_id: str


@dataclass(frozen=True)
class TraceDryRunResult:
    trace_id: str
    controller_name: str
    phase: str
    outputs_are_benchmark_results: bool
    final_qoe_reward_defined: bool
    segment_count: int
    total_rebuffer_s: float
    total_playback_s: float
    records: Tuple[SegmentDryRunRecord, ...]
    eval_phase: str = EVAL_PHASE
    row_eval_gate: str = ROW_EVAL_GATE
    no_final_ranking: bool = True
    schema_version: str = ""
    notes: str = NON_BENCHMARK_NOTES


@dataclass(frozen=True)
class TraceDryRunConfig:
    segment_duration_s: float
    segment_count: int
    representations: Sequence[Representation]
    initial_buffer_s: float = 0.0
    startup_buffer_s: float = 0.0
    end_policy: str = END_POLICY_LOOP
    max_loops: int = 3
    outputs_are_benchmark_results: bool = False
    final_qoe_reward_defined: bool = False
    eval_phase: str = EVAL_PHASE
    row_eval_gate: str = ROW_EVAL_GATE
    no_final_ranking: bool = True


def build_representations_from_kbps(values: Sequence[object]) -> Tuple[Representation, ...]:
    """Build an ascending synthetic ladder from kbps values."""

    try:
        raw_values = list(values)
    except TypeError as exc:
        raise TraceDryRunError("representation kbps values must be iterable") from exc
    if not raw_values:
        raise TraceDryRunError("representation ladder must not be empty")

    bitrates = []
    for position, raw_value in enumerate(raw_values):
        bitrate = _finite_positive_float(raw_value, "representation bitrate at position {0}".format(position))
        bitrates.append(bitrate)

    ordered = sorted(bitrates)
    if len(set(ordered)) != len(ordered):
        raise TraceDryRunError("representation ladder contains duplicate bitrates")

    return tuple(
        Representation(index=index, bitrate_kbps=bitrate, label="{0:g}kbps".format(bitrate))
        for index, bitrate in enumerate(ordered)
    )


def estimate_segment_size_bytes(representation_bitrate_kbps: object, segment_duration_s: object) -> int:
    bitrate_kbps = _finite_positive_float(representation_bitrate_kbps, "representation_bitrate_kbps")
    duration_s = _finite_positive_float(segment_duration_s, "segment_duration_s")
    return int(math.ceil((bitrate_kbps * 1000.0 * duration_s) / 8.0))


def run_trace_dry_run(loaded_trace, controller_adapter, config: TraceDryRunConfig) -> TraceDryRunResult:
    config = _validate_config(config)
    trace_id = str(getattr(loaded_trace, "trace_id", ""))
    if not trace_id:
        raise TraceDryRunError("loaded trace must expose a trace_id")

    controller_name = str(getattr(controller_adapter, "name", ""))
    if not controller_name:
        raise TraceDryRunError("controller adapter must expose a non-empty name")

    reset = getattr(controller_adapter, "reset", None)
    if callable(reset):
        reset()

    try:
        model = TraceDrivenNetworkModel(
            loaded_trace,
            end_policy=config.end_policy,
            max_loops=config.max_loops,
        )
        replay_adapter = TraceDrivenFakeReplayAdapter(model)
    except TraceReplayError as exc:
        raise TraceDryRunError(str(exc)) from exc

    records = []
    buffer_s = float(config.initial_buffer_s)
    previous_representation_index = 0
    previous_segment_size_bytes = 0
    previous_download_duration_s = 0.0
    previous_measured_throughput_kbps = 0.0
    previous_download_start_s = 0.0
    previous_download_end_s = 0.0
    downloaded_bytes_total = 0

    for segment_index in range(config.segment_count):
        feedback = _build_controller_feedback(
            segment_index=segment_index,
            config=config,
            buffer_s=buffer_s,
            previous_representation_index=previous_representation_index,
            previous_segment_size_bytes=previous_segment_size_bytes,
            previous_download_duration_s=previous_download_duration_s,
            previous_measured_throughput_kbps=previous_measured_throughput_kbps,
            previous_download_start_s=previous_download_start_s,
            previous_download_end_s=previous_download_end_s,
            downloaded_bytes_total=downloaded_bytes_total,
        )

        try:
            decision = controller_adapter.decide(feedback)
        except ControllerAdapterError as exc:
            raise TraceDryRunError(str(exc)) from exc

        representation_index = _validate_decision_index(decision.representation_index, config.representations)
        representation = config.representations[representation_index]
        segment_size_bytes = estimate_segment_size_bytes(
            representation.bitrate_kbps,
            config.segment_duration_s,
        )

        buffer_before_s = buffer_s
        try:
            download = replay_adapter.download_segment(segment_size_bytes)
        except TraceReplayError as exc:
            raise TraceDryRunError(str(exc)) from exc

        rebuffer_s = max(download.duration_s - buffer_before_s, 0.0)
        buffer_after_s = max(buffer_before_s - download.duration_s, 0.0) + config.segment_duration_s

        record = SegmentDryRunRecord(
            segment_index=segment_index,
            representation_index=representation.index,
            representation_bitrate_kbps=representation.bitrate_kbps,
            segment_duration_s=config.segment_duration_s,
            segment_size_bytes=segment_size_bytes,
            download_start_time_s=download.start_time_s,
            download_end_time_s=download.end_time_s,
            download_duration_s=download.duration_s,
            measured_throughput_kbps=download.measured_throughput_kbps,
            buffer_before_s=buffer_before_s,
            buffer_after_s=buffer_after_s,
            rebuffer_s=rebuffer_s,
            controller_name=controller_name,
            trace_id=trace_id,
        )
        records.append(record)

        buffer_s = buffer_after_s
        previous_representation_index = representation.index
        previous_segment_size_bytes = segment_size_bytes
        previous_download_duration_s = download.duration_s
        previous_measured_throughput_kbps = download.measured_throughput_kbps
        previous_download_start_s = download.start_time_s
        previous_download_end_s = download.end_time_s
        downloaded_bytes_total += segment_size_bytes

    total_rebuffer_s = sum(record.rebuffer_s for record in records)
    total_playback_s = config.segment_count * config.segment_duration_s

    return TraceDryRunResult(
        trace_id=trace_id,
        controller_name=controller_name,
        phase=PHASE_LABEL,
        outputs_are_benchmark_results=False,
        final_qoe_reward_defined=False,
        segment_count=len(records),
        total_rebuffer_s=total_rebuffer_s,
        total_playback_s=total_playback_s,
        records=tuple(records),
        eval_phase=config.eval_phase,
        row_eval_gate=config.row_eval_gate,
        no_final_ranking=config.no_final_ranking,
        schema_version=str(getattr(loaded_trace, "schema_version", "")),
    )


def write_trace_dry_run_artifacts(result: TraceDryRunResult, output_dir: object) -> Mapping[str, Path]:
    output_path = _explicit_output_dir(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    manifest_path = output_path / "trace_dry_run_manifest.json"
    segments_path = output_path / "trace_dry_run_segments.csv"
    summary_path = output_path / "trace_dry_run_summary.json"

    common = _artifact_common(result)
    manifest = dict(common)
    manifest.update(
        {
            "artifact_type": "trace_dry_run_manifest",
            "artifacts": {
                "manifest": manifest_path.name,
                "segments": segments_path.name,
                "summary": summary_path.name,
            },
        }
    )
    summary = dict(common)
    summary.update(
        {
            "artifact_type": "trace_dry_run_summary",
            "segment_count": result.segment_count,
            "total_rebuffer_s": result.total_rebuffer_s,
            "total_playback_s": result.total_playback_s,
        }
    )

    _write_json(manifest_path, manifest)
    _write_segments_csv(segments_path, result)
    _write_json(summary_path, summary)

    return {
        "manifest": manifest_path,
        "segments": segments_path,
        "summary": summary_path,
    }


def _validate_config(config: TraceDryRunConfig) -> TraceDryRunConfig:
    if not isinstance(config, TraceDryRunConfig):
        raise TraceDryRunError("config must be a TraceDryRunConfig")

    _finite_positive_float(config.segment_duration_s, "segment_duration_s")
    if isinstance(config.segment_count, bool) or not isinstance(config.segment_count, int) or config.segment_count <= 0:
        raise TraceDryRunError("segment_count must be a positive integer")
    _finite_non_negative_float(config.initial_buffer_s, "initial_buffer_s")
    _finite_non_negative_float(config.startup_buffer_s, "startup_buffer_s")

    if config.end_policy not in (END_POLICY_FAIL, END_POLICY_LOOP):
        raise TraceDryRunError("end_policy must be 'fail' or 'loop'")
    if isinstance(config.max_loops, bool) or not isinstance(config.max_loops, int) or config.max_loops < 0:
        raise TraceDryRunError("max_loops must be a non-negative integer")
    if config.outputs_are_benchmark_results is not False:
        raise TraceDryRunError("Phase 3.4C dry-run outputs must not be marked as benchmark results")
    if config.final_qoe_reward_defined is not False:
        raise TraceDryRunError("Phase 3.4C dry-runs must not define final QoE/reward")
    if config.eval_phase != EVAL_PHASE:
        raise TraceDryRunError("eval_phase must be {0}".format(EVAL_PHASE))
    if config.row_eval_gate != ROW_EVAL_GATE:
        raise TraceDryRunError("row_eval_gate must be {0}".format(ROW_EVAL_GATE))
    if config.no_final_ranking is not True:
        raise TraceDryRunError("Phase 3.4C dry-runs must declare no_final_ranking=True")

    representations = tuple(config.representations or ())
    if not representations:
        raise TraceDryRunError("representations must not be empty")
    expected_indices = list(range(len(representations)))
    actual_indices = [representation.index for representation in representations]
    if actual_indices != expected_indices:
        raise TraceDryRunError("representation indices must be contiguous and zero-based")
    previous_bitrate = None
    for representation in representations:
        _finite_positive_float(representation.bitrate_kbps, "representation bitrate")
        if previous_bitrate is not None and representation.bitrate_kbps <= previous_bitrate:
            raise TraceDryRunError("representations must be sorted by increasing bitrate")
        previous_bitrate = representation.bitrate_kbps
    return config


def _build_controller_feedback(
    segment_index: int,
    config: TraceDryRunConfig,
    buffer_s: float,
    previous_representation_index: int,
    previous_segment_size_bytes: int,
    previous_download_duration_s: float,
    previous_measured_throughput_kbps: float,
    previous_download_start_s: float,
    previous_download_end_s: float,
    downloaded_bytes_total: int,
):
    rates_Bps = [_representation_rate_Bps(representation) for representation in config.representations]
    previous_representation_index = max(0, min(previous_representation_index, len(rates_Bps) - 1))
    current_rate_Bps = rates_Bps[previous_representation_index]
    measured_Bps = (previous_measured_throughput_kbps * 1000.0) / 8.0 if previous_measured_throughput_kbps > 0 else 0.0
    queued_bytes = int(max(0.0, buffer_s) * current_rate_Bps)

    return {
        "queued_bytes": queued_bytes,
        "queued_time": float(buffer_s),
        "cur_bitrate": current_rate_Bps,
        "bwe": measured_Bps,
        "level": previous_representation_index,
        "max_level": len(rates_Bps) - 1,
        "cur_rate": current_rate_Bps,
        "max_rate": rates_Bps[-1],
        "min_rate": rates_Bps[0],
        "max_bitrate": rates_Bps[-1],
        "min_bitrate": rates_Bps[0],
        "last_fragment_size": int(previous_segment_size_bytes),
        "last_download_time": float(previous_download_duration_s),
        "downloaded_bytes": int(downloaded_bytes_total),
        "fragment_duration": float(config.segment_duration_s),
        "rates": rates_Bps,
        "segment_index": int(segment_index),
        "start_segment_request": float(previous_download_start_s),
        "stop_segment_request": float(previous_download_end_s),
    }


def _validate_decision_index(index: object, representations: Sequence[Representation]) -> int:
    if isinstance(index, bool) or not isinstance(index, int):
        raise TraceDryRunError("controller decision representation_index must be an integer")
    if index < 0 or index >= len(representations):
        raise TraceDryRunError("controller decision representation_index is outside the ladder")
    return index


def _artifact_common(result: TraceDryRunResult):
    return {
        "phase": result.eval_phase,
        "phase_label": result.phase,
        "outputs_are_benchmark_results": False,
        "final_qoe_reward_defined": False,
        "row_eval_gate": result.row_eval_gate,
        "no_final_ranking": result.no_final_ranking,
        "controller_name": result.controller_name,
        "trace_id": result.trace_id,
        "schema_version": result.schema_version,
        "segment_count": result.segment_count,
        "total_rebuffer_s": result.total_rebuffer_s,
        "total_playback_s": result.total_playback_s,
        "notes": result.notes,
    }


def _write_segments_csv(path: Path, result: TraceDryRunResult) -> None:
    metadata_fields = [
        "phase",
        "phase_label",
        "outputs_are_benchmark_results",
        "final_qoe_reward_defined",
        "row_eval_gate",
        "no_final_ranking",
        "schema_version",
        "notes",
    ]
    record_fields = list(asdict(result.records[0]).keys()) if result.records else list(SegmentDryRunRecord.__dataclass_fields__)
    fieldnames = metadata_fields + record_fields

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for record in result.records:
            row = {
                "phase": result.eval_phase,
                "phase_label": result.phase,
                "outputs_are_benchmark_results": "false",
                "final_qoe_reward_defined": "false",
                "row_eval_gate": result.row_eval_gate,
                "no_final_ranking": "true",
                "schema_version": result.schema_version,
                "notes": result.notes,
            }
            row.update(asdict(record))
            writer.writerow(row)


def _write_json(path: Path, payload: Mapping[str, object]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _explicit_output_dir(output_dir: object) -> Path:
    if output_dir is None:
        raise TraceDryRunError("output_dir is required")
    if isinstance(output_dir, str) and not output_dir.strip():
        raise TraceDryRunError("output_dir must not be empty")
    return Path(output_dir)


def _representation_rate_Bps(representation: Representation) -> float:
    return (representation.bitrate_kbps * 1000.0) / 8.0


def _finite_positive_float(value: object, name: str) -> float:
    parsed = _finite_float(value, name)
    if parsed <= 0.0:
        raise TraceDryRunError("{0} must be positive".format(name))
    return parsed


def _finite_non_negative_float(value: object, name: str) -> float:
    parsed = _finite_float(value, name)
    if parsed < 0.0:
        raise TraceDryRunError("{0} must be non-negative".format(name))
    return parsed


def _finite_float(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TraceDryRunError("{0} must be numeric and finite".format(name))
    parsed = float(value)
    if not math.isfinite(parsed):
        raise TraceDryRunError("{0} must be numeric and finite".format(name))
    return parsed

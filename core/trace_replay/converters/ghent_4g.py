"""Converter for Ghent 4G/LTE Bandwidth Logs."""

from __future__ import annotations

from pathlib import Path
from typing import Mapping, Sequence, Tuple

from core.trace_replay.converters import common
from core.trace_replay.converters.base import ConversionBatchResult, ConvertedTrace


DATASET_ID = "ghent_4g_lte_bandwidth_logs"
CONVERTER_NAME = "ghent_4g_lte_bandwidth_logs_v1"


def convert_ghent_4g(input_dir, output_dir, manifest_dir, max_traces=None, overwrite=False):
    converted = []
    skipped = []
    errors = []
    output_root = Path(output_dir)
    manifest_root = Path(manifest_dir)

    for source in common.iter_text_sources(input_dir):
        if max_traces is not None and len(converted) >= max_traces:
            break

        source_key = common.normalize_source_key(input_dir, source.source_path)
        trace_id = common.stable_trace_id(DATASET_ID, source_key)
        output_csv_path = output_root / "{0}.csv".format(trace_id)
        manifest_path = manifest_root / "{0}.json".format(trace_id)
        rows = _parse_ghent_rows(source.text, source.source_path)
        if not rows:
            skipped.append(source.source_path)
            continue

        common.ensure_can_write(output_csv_path, manifest_path, overwrite=overwrite)
        fieldnames = common.ordered_fieldnames(rows, _optional_fieldnames())
        common.write_normalized_trace_csv(output_csv_path, rows, fieldnames)
        validation = common.validate_written_trace(output_csv_path)
        mobility_tags = common.infer_mobility_tags(source.source_path)
        scenario_label = rows[0].get("scenario_label", "unknown")
        manifest = common.manifest_common_metadata(
            trace_id=trace_id,
            dataset_id=DATASET_ID,
            source_path=source.source_path,
            output_csv_path=output_csv_path,
            converter_name=CONVERTER_NAME,
            validation=validation,
            scenario_tags=("mobile", str(scenario_label)),
            mobility_tags=mobility_tags or ("unknown",),
            network_tags=("LTE", "4G"),
            leakage_group=common.safe_trace_id("{0}_{1}".format(DATASET_ID, source_key)),
            notes=(
                "Phase 3.4A conversion only. Rows with the audited six-column "
                "shape are interpreted as absolute timestamp ms, elapsed ms, "
                "latitude, longitude, bytes delivered during interval, and "
                "interval elapsed ms."
            ),
        )
        common.write_trace_manifest(manifest_path, manifest)
        converted.append(_converted_trace(trace_id, source.source_path, output_csv_path, manifest_path, validation))

    return ConversionBatchResult(
        dataset_id=DATASET_ID,
        input_dir=str(Path(input_dir)),
        output_dir=str(output_root),
        manifest_dir=str(manifest_root),
        converted_traces=tuple(converted),
        skipped_inputs=tuple(skipped),
        errors=tuple(errors),
    )


def _parse_ghent_rows(text: str, source_path: str) -> Tuple[Mapping[str, object], ...]:
    mobility_tags = common.infer_mobility_tags(source_path)
    mobility_label = mobility_tags[0] if mobility_tags else "unknown"
    scenario_label = common.infer_scenario_label(source_path)
    rows = _parse_six_column_interval_bytes(
        text=text,
        source_path=source_path,
        network_type="LTE",
        mobility_label=mobility_label,
        scenario_label=scenario_label,
    )
    if rows:
        return rows
    return _parse_two_column_cumulative_bytes(
        text=text,
        source_path=source_path,
        network_type="LTE",
        mobility_label=mobility_label,
        scenario_label=scenario_label,
    )


def _parse_six_column_interval_bytes(
    text: str,
    source_path: str,
    network_type: str,
    mobility_label: str,
    scenario_label: str,
) -> Tuple[Mapping[str, object], ...]:
    raw_rows = []
    for line in text.splitlines():
        tokens = common.split_delimited_tokens(line)
        if len(tokens) < 6:
            continue
        values = [common.parse_float_token(token) for token in tokens[:6]]
        if any(value is None for value in values):
            continue
        absolute_ms, elapsed_ms, latitude, longitude, byte_count, interval_ms = values
        if byte_count < 0 or interval_ms <= 0:
            continue
        raw_rows.append((absolute_ms, elapsed_ms, latitude, longitude, byte_count, interval_ms))

    if not raw_rows:
        return ()

    first_elapsed_ms = raw_rows[0][1]
    rows = []
    for absolute_ms, elapsed_ms, latitude, longitude, byte_count, interval_ms in raw_rows:
        timestamp_s = max(0.0, (elapsed_ms - first_elapsed_ms) / 1000.0)
        rows.append(
            {
                "timestamp_s": timestamp_s,
                "duration_s": interval_ms / 1000.0,
                "throughput_kbps": common.bytes_elapsed_ms_to_kbps(byte_count, interval_ms),
                "source_timestamp": format(absolute_ms, ".0f"),
                "latitude": latitude,
                "longitude": longitude,
                "mobility_label": mobility_label,
                "network_type": network_type,
                "scenario_label": scenario_label,
                "source_dataset": DATASET_ID,
                "source_file": source_path,
                "notes": "bytes_per_interval_ms",
            }
        )
    return tuple(rows)


def _parse_two_column_cumulative_bytes(
    text: str,
    source_path: str,
    network_type: str,
    mobility_label: str,
    scenario_label: str,
) -> Tuple[Mapping[str, object], ...]:
    numeric_rows = [row for row in common.numeric_rows_from_text(text) if len(row) == 2]
    if len(numeric_rows) < 2:
        return ()
    if not _is_non_decreasing([row[1] for row in numeric_rows]):
        return ()

    time_scale = _time_scale_to_seconds([row[0] for row in numeric_rows])
    first_time = numeric_rows[0][0]
    rows = []
    for previous, current in zip(numeric_rows, numeric_rows[1:]):
        duration_s = (current[0] - previous[0]) * time_scale
        byte_delta = current[1] - previous[1]
        if duration_s <= 0 or byte_delta < 0:
            continue
        rows.append(
            {
                "timestamp_s": max(0.0, (previous[0] - first_time) * time_scale),
                "duration_s": duration_s,
                "throughput_kbps": (byte_delta * 8.0) / (duration_s * 1000.0),
                "mobility_label": mobility_label,
                "network_type": network_type,
                "scenario_label": scenario_label,
                "source_dataset": DATASET_ID,
                "source_file": source_path,
                "notes": "cumulative_bytes_delta",
            }
        )
    return tuple(rows)


def _is_non_decreasing(values: Sequence[float]) -> bool:
    return all(current >= previous for previous, current in zip(values, values[1:]))


def _time_scale_to_seconds(values: Sequence[float]) -> float:
    if not values:
        return 1.0
    deltas = [current - previous for previous, current in zip(values, values[1:]) if current > previous]
    if values[0] > 10000 or (deltas and sorted(deltas)[len(deltas) // 2] > 100.0):
        return 0.001
    return 1.0


def _optional_fieldnames() -> Tuple[str, ...]:
    return (
        "source_timestamp",
        "latitude",
        "longitude",
        "mobility_label",
        "network_type",
        "scenario_label",
        "source_dataset",
        "source_file",
        "notes",
    )


def _converted_trace(trace_id, source_path, output_csv_path, manifest_path, validation):
    return ConvertedTrace(
        trace_id=trace_id,
        dataset_id=DATASET_ID,
        source_path=source_path,
        output_csv_path=str(Path(output_csv_path)),
        manifest_path=str(Path(manifest_path)),
        validation=validation,
        sample_count=validation.sample_count,
        duration_s=validation.duration_s,
        min_throughput_kbps=validation.min_throughput_kbps,
        mean_throughput_kbps=validation.mean_throughput_kbps,
        max_throughput_kbps=validation.max_throughput_kbps,
    )

"""Converter for Lancaster ABR-Throughput-Traces."""

from __future__ import annotations

from pathlib import Path
from typing import Mapping, Sequence, Tuple

from core.trace_replay.converters import common
from core.trace_replay.converters.base import ConversionBatchResult, ConvertedTrace


DATASET_ID = "lancaster_abr_throughput_traces"
CONVERTER_NAME = "lancaster_abr_throughput_traces_v1"
DEFAULT_SINGLE_VALUE_DURATION_S = 1.0


def convert_lancaster_abr(input_dir, output_dir, manifest_dir, max_traces=None, overwrite=False):
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
        rows = _parse_lancaster_rows(source.text, source.source_path)
        if not rows:
            skipped.append(source.source_path)
            continue

        common.ensure_can_write(output_csv_path, manifest_path, overwrite=overwrite)
        fieldnames = common.ordered_fieldnames(rows, _optional_fieldnames())
        common.write_normalized_trace_csv(output_csv_path, rows, fieldnames)
        validation = common.validate_written_trace(output_csv_path)
        scenario_label = rows[0].get("scenario_label", "unknown")
        manifest = common.manifest_common_metadata(
            trace_id=trace_id,
            dataset_id=DATASET_ID,
            source_path=source.source_path,
            output_csv_path=output_csv_path,
            converter_name=CONVERTER_NAME,
            validation=validation,
            scenario_tags=("HAS", "variable", str(scenario_label)),
            mobility_tags=("unknown",),
            network_tags=("HAS",),
            leakage_group=common.safe_trace_id("{0}_{1}".format(DATASET_ID, source_key)),
            notes=(
                "Phase 3.4A conversion only. One numeric value per line is "
                "treated as throughput_kbps with 1.0 s duration. Two numeric "
                "columns are treated as timestamp_s and throughput_kbps; "
                "durations are inferred from adjacent timestamps, with the "
                "last sample using the previous positive delta or 1.0 s."
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


def _parse_lancaster_rows(text: str, source_path: str) -> Tuple[Mapping[str, object], ...]:
    numeric_rows = common.numeric_rows_from_text(text)
    if not numeric_rows:
        return ()

    scenario_label = common.infer_scenario_label(source_path)
    if all(len(row) == 1 for row in numeric_rows):
        return _parse_single_value_rows(numeric_rows, source_path, scenario_label)
    if all(len(row) >= 2 for row in numeric_rows):
        return _parse_two_column_rows(numeric_rows, source_path, scenario_label)
    return ()


def _parse_single_value_rows(
    numeric_rows: Sequence[Sequence[float]],
    source_path: str,
    scenario_label: str,
) -> Tuple[Mapping[str, object], ...]:
    rows = []
    for index, raw_row in enumerate(numeric_rows):
        throughput_kbps = raw_row[0]
        if throughput_kbps < 0:
            return ()
        rows.append(
            {
                "timestamp_s": index * DEFAULT_SINGLE_VALUE_DURATION_S,
                "duration_s": DEFAULT_SINGLE_VALUE_DURATION_S,
                "throughput_kbps": throughput_kbps,
                "scenario_label": scenario_label,
                "source_dataset": DATASET_ID,
                "source_file": source_path,
                "notes": "single_value_regular_1s_kbps",
            }
        )
    return tuple(rows)


def _parse_two_column_rows(
    numeric_rows: Sequence[Sequence[float]],
    source_path: str,
    scenario_label: str,
) -> Tuple[Mapping[str, object], ...]:
    pairs = tuple((row[0], row[1]) for row in numeric_rows)
    if any(throughput < 0 for _timestamp, throughput in pairs):
        return ()
    if any(current[0] < previous[0] for previous, current in zip(pairs, pairs[1:])):
        return ()

    first_timestamp = pairs[0][0]
    deltas = [current[0] - previous[0] for previous, current in zip(pairs, pairs[1:]) if current[0] > previous[0]]
    fallback_duration = deltas[-1] if deltas else DEFAULT_SINGLE_VALUE_DURATION_S
    rows = []
    for index, (timestamp_s, throughput_kbps) in enumerate(pairs):
        if index + 1 < len(pairs):
            duration_s = pairs[index + 1][0] - timestamp_s
            if duration_s <= 0:
                duration_s = fallback_duration
        else:
            duration_s = fallback_duration
        if duration_s <= 0:
            return ()
        rows.append(
            {
                "timestamp_s": max(0.0, timestamp_s - first_timestamp),
                "duration_s": duration_s,
                "throughput_kbps": throughput_kbps,
                "scenario_label": scenario_label,
                "source_dataset": DATASET_ID,
                "source_file": source_path,
                "notes": "timestamp_throughput_kbps",
            }
        )
    return tuple(rows)


def _optional_fieldnames() -> Tuple[str, ...]:
    return (
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

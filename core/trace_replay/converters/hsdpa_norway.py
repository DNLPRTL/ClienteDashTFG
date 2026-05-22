"""Converter for HSDPA Norway / Riiser MMSys 2013 path bandwidth logs."""

from __future__ import annotations

from pathlib import Path

from core.trace_replay.converters import common
from core.trace_replay.converters.base import ConversionBatchResult, ConvertedTrace
from core.trace_replay.converters.ghent_4g import (
    _optional_fieldnames,
    _parse_six_column_interval_bytes,
    _parse_two_column_cumulative_bytes,
)


DATASET_ID = "hsdpa_norway_mmsys2013"
CONVERTER_NAME = "hsdpa_norway_mmsys2013_v1"


def convert_hsdpa_norway(input_dir, output_dir, manifest_dir, max_traces=None, overwrite=False):
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
        rows = _parse_hsdpa_rows(source.text, source.source_path)
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
            network_tags=("HSDPA", "3G"),
            leakage_group=common.safe_trace_id("{0}_{1}".format(DATASET_ID, source_key)),
            notes=(
                "Phase 3.4A conversion only. The converter supports the "
                "six-column interval-byte log shape also observed in related "
                "mobile bandwidth logs, plus conservative cumulative "
                "timestamp/byte pairs when present."
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


def _parse_hsdpa_rows(text: str, source_path: str):
    mobility_tags = common.infer_mobility_tags(source_path)
    mobility_label = mobility_tags[0] if mobility_tags else "unknown"
    scenario_label = common.infer_scenario_label(source_path)
    rows = _parse_six_column_interval_bytes(
        text=text,
        source_path=source_path,
        network_type="HSDPA",
        mobility_label=mobility_label,
        scenario_label=scenario_label,
    )
    if rows:
        return _with_dataset_id(rows)

    rows = _parse_two_column_cumulative_bytes(
        text=text,
        source_path=source_path,
        network_type="HSDPA",
        mobility_label=mobility_label,
        scenario_label=scenario_label,
    )
    return _with_dataset_id(rows)


def _with_dataset_id(rows):
    converted = []
    for row in rows:
        row_copy = dict(row)
        row_copy["source_dataset"] = DATASET_ID
        converted.append(row_copy)
    return tuple(converted)


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

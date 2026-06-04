from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from pathlib import Path
from statistics import median
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

try:
    from scripts.phase6c_source_registry import (
        DEFAULT_REGISTRY_PATH,
        Phase6CError,
        create_external_layout,
        load_source_registry,
        relative_to_root,
        sha256_bytes,
        sources_by_id,
        utc_now,
        write_json,
        write_markdown_report,
    )
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from phase6c_source_registry import (
        DEFAULT_REGISTRY_PATH,
        Phase6CError,
        create_external_layout,
        load_source_registry,
        relative_to_root,
        sha256_bytes,
        sources_by_id,
        utc_now,
        write_json,
        write_markdown_report,
    )


TRACE_SCHEMA_VERSION = "normalized_trace_schema_v1"
REPORT_SCHEMA_VERSION = "phase6c_normalization_report_v1"
TEXT_EXTENSIONS = {".csv", ".tsv", ".txt", ".log", ""}
THROUGHPUT_ALIASES = {
    "throughput",
    "throughputkbps",
    "throughputmbps",
    "throughputbps",
    "dlthroughput",
    "dlthroughputkbps",
    "dlthroughputmbps",
    "dlthroughputbps",
    "dlbitrate",
    "dlbitratekbps",
    "dlbitratembps",
    "dlbitratebps",
    "downloadbitrate",
    "downloadbitratekbps",
    "downloadbitratembps",
    "downloadbitratebps",
    "speed",
    "speedmbps",
    "speedkbps",
    "speedbps",
    "bitrate",
    "bitratekbps",
    "bitratembps",
    "bitratebps",
}
TIMESTAMP_ALIASES = {"timestamp", "timestamps", "timestamps", "time", "times", "seconds", "second", "timestampsec", "timestamps"}
BYTES_ALIASES = {
    "bytes",
    "bytesreceived",
    "bytesreceivedsinceprevious",
    "downloadbytes",
    "dlbytes",
    "rxbytes",
}
ELAPSED_MS_ALIASES = {
    "elapsedms",
    "millisecondssinceprevious",
    "durationms",
    "intervalms",
    "deltams",
    "timems",
}


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Normalize Phase 6C trace sources into normalized_trace_schema_v1 CSVs.")
    parser.add_argument("--external-root", required=True, type=Path)
    parser.add_argument("--source-registry", type=Path, default=DEFAULT_REGISTRY_PATH)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--allow-empty-optional", action="store_true")
    parser.add_argument("--allow-repo-output", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    try:
        report = normalize_phase6_sources(
            external_root=args.external_root,
            registry_path=args.source_registry,
            strict=args.strict,
            allow_empty_optional=args.allow_empty_optional,
            allow_repo_output=args.allow_repo_output,
        )
    except Phase6CError as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 2
    except OSError as exc:
        print("error: {0}".format(exc), file=sys.stderr)
        return 1

    print("phase6c_normalize: {0}".format("PASS" if report["valid"] else "WARN_OR_FAIL"))
    print("report: {0}".format(report["json_report_path"]))
    return 0 if report["valid"] else 2


def normalize_phase6_sources(
    *,
    external_root: Path,
    registry_path: Path = DEFAULT_REGISTRY_PATH,
    strict: bool = False,
    allow_empty_optional: bool = False,
    allow_repo_output: bool = False,
) -> Dict[str, Any]:
    paths = create_external_layout(external_root, allow_repo_output=allow_repo_output)
    registry = load_source_registry(registry_path)
    source_map = sources_by_id(registry)

    records: List[Dict[str, Any]] = []
    excluded: List[Dict[str, Any]] = []
    errors: List[str] = []
    warnings: List[str] = []

    for source_dir in sorted(path for path in paths["extracted"].iterdir() if path.is_dir()):
        source_id = source_dir.name
        source = source_map.get(source_id, {"source_id": source_id, "dataset_family": source_id, "source_dataset": source_id})
        for path in sorted(item for item in source_dir.rglob("*") if item.is_file() and is_candidate_trace_file(item)):
            result = normalize_one_file(path, source, paths["root"])
            if result.get("normalization_status") == "normalized":
                metadata = write_normalized_trace(result, paths)
                records.append(metadata)
            else:
                excluded_record = {
                    "source_id": source_id,
                    "dataset_family": source.get("dataset_family", source_id),
                    "source_file": relative_to_root(path, paths["root"]),
                    "normalization_status": "excluded",
                    "exclusion_reason": result.get("exclusion_reason", "normalization_failed"),
                }
                excluded.append(excluded_record)
                message = "{0}: {1}".format(excluded_record["source_file"], excluded_record["exclusion_reason"])
                if strict and source.get("eval_gate") == "use_for_eval":
                    errors.append(message)
                else:
                    warnings.append(message)

    report = {
        "schema_version": REPORT_SCHEMA_VERSION,
        "generated_at": utc_now(),
        "external_root": str(paths["root"]),
        "strict": strict,
        "trace_schema_version": TRACE_SCHEMA_VERSION,
        "normalized_records": records,
        "excluded_records": excluded,
        "counts": {
            "normalized": len(records),
            "excluded": len(excluded),
            "errors": len(errors),
            "warnings": len(warnings),
        },
        "errors": errors,
        "warnings": warnings,
    }
    json_report_path = paths["reports"] / "phase6c_normalization_report.json"
    md_report_path = paths["reports"] / "phase6c_normalization_report.md"
    write_json(json_report_path, report)
    write_normalization_markdown(md_report_path, report)
    return {
        "valid": not errors,
        "records": records,
        "excluded": excluded,
        "errors": errors,
        "warnings": warnings,
        "json_report_path": str(json_report_path),
        "md_report_path": str(md_report_path),
    }


def normalize_one_file(path: Path, source: Mapping[str, Any], root: Path) -> Dict[str, Any]:
    source_id = str(source.get("source_id", path.parent.name))
    try:
        if source_id in ("hsdpa_norway", "ghent_4g_lte"):
            rows = parse_six_column_log(path)
            if not rows:
                rows = parse_delimited_trace(path)
        else:
            rows = parse_delimited_trace(path)
            if not rows:
                rows = parse_six_column_log(path)
    except UnicodeDecodeError:
        return {"normalization_status": "excluded", "exclusion_reason": "unable_to_decode_text_file"}

    if not rows:
        return {"normalization_status": "excluded", "exclusion_reason": "unable_to_detect_throughput_column"}

    valid_rows = [row for row in rows if row["duration_s"] > 0 and row["throughput_kbps"] >= 0]
    if not valid_rows:
        return {"normalization_status": "excluded", "exclusion_reason": "empty_or_invalid_trace"}

    fingerprint = canonical_content_fingerprint(valid_rows)
    dataset_family = str(source.get("dataset_family", source_id))
    trace_id = "{0}_{1}".format(slug(dataset_family), fingerprint[:16])
    return {
        "normalization_status": "normalized",
        "trace_id": trace_id,
        "dataset_family": dataset_family,
        "source_dataset": source.get("source_dataset", dataset_family),
        "source_id": source_id,
        "source_file": relative_to_root(path, root),
        "schema_version": TRACE_SCHEMA_VERSION,
        "canonical_content_fingerprint": fingerprint,
        "leakage_group": "{0}:{1}".format(dataset_family, fingerprint),
        "duration_s": round(sum(row["duration_s"] for row in valid_rows), 6),
        "sample_count": len(valid_rows),
        "license_status": source.get("license_status", "public_source_requires_local_review"),
        "acquisition_status": "acquired",
        "split": source.get("split", ""),
        "eval_gate": source.get("eval_gate", ""),
        "rows": valid_rows,
    }


def is_candidate_trace_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTENSIONS or path.name.startswith("report.")


def parse_six_column_log(path: Path) -> List[Dict[str, Any]]:
    rows = []
    for line in path.read_text(encoding="utf-8", errors="strict").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        parts = re.split(r"\s+", stripped)
        if len(parts) < 6:
            return []
        try:
            timestamp_raw = float(parts[0])
            latitude = float(parts[2])
            longitude = float(parts[3])
            bytes_received = float(parts[4])
            milliseconds_since_previous = float(parts[5])
        except ValueError:
            return []
        if milliseconds_since_previous <= 0:
            continue
        timestamp_s = timestamp_raw / 1000.0 if abs(timestamp_raw) >= 1000 else timestamp_raw
        duration_s = milliseconds_since_previous / 1000.0
        throughput_kbps = bytes_received * 8.0 / milliseconds_since_previous
        rows.append(
            {
                "timestamp_s": timestamp_s,
                "duration_s": duration_s,
                "throughput_kbps": throughput_kbps,
                "latitude": latitude,
                "longitude": longitude,
            }
        )
    return rows


def parse_delimited_trace(path: Path) -> List[Dict[str, Any]]:
    text = path.read_text(encoding="utf-8", errors="strict")
    if not text.strip():
        return []
    sample = text[:4096]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t;")
    except csv.Error:
        delimiter = "\t" if "\t" in sample else "," if "," in sample else ";"
        dialect = csv.excel()
        dialect.delimiter = delimiter

    reader = csv.DictReader(io.StringIO(text), dialect=dialect)
    if not reader.fieldnames:
        return []
    fields = {normalize_header(field): field for field in reader.fieldnames if field}
    throughput_field = first_matching_field(fields, THROUGHPUT_ALIASES)
    timestamp_field = first_matching_field(fields, TIMESTAMP_ALIASES)
    bytes_field = first_matching_field(fields, BYTES_ALIASES)
    elapsed_ms_field = first_matching_field(fields, ELAPSED_MS_ALIASES)
    latitude_field = fields.get("latitude") or fields.get("lat")
    longitude_field = fields.get("longitude") or fields.get("lon") or fields.get("lng")
    mobility_field = fields.get("mobilitytag") or fields.get("mobility") or fields.get("scenario")

    raw_rows = list(reader)
    timestamps = [safe_float(row.get(timestamp_field)) for row in raw_rows] if timestamp_field else []
    timestamp_values = [value for value in timestamps if value is not None]
    timestamp_scale = infer_timestamp_scale(timestamp_values)
    durations = infer_durations(timestamps, timestamp_scale) if timestamp_field else []

    rows = []
    for index, row in enumerate(raw_rows):
        if throughput_field:
            throughput = safe_float(row.get(throughput_field))
            if throughput is None:
                continue
            throughput_kbps = convert_throughput_to_kbps(throughput, throughput_field, [safe_float(item.get(throughput_field)) for item in raw_rows])
        elif bytes_field and elapsed_ms_field:
            bytes_value = safe_float(row.get(bytes_field))
            elapsed_ms = safe_float(row.get(elapsed_ms_field))
            if bytes_value is None or elapsed_ms is None or elapsed_ms <= 0:
                continue
            throughput_kbps = bytes_value * 8.0 / elapsed_ms
        else:
            return []

        timestamp_s = 0.0
        if timestamp_field and index < len(timestamps) and timestamps[index] is not None:
            timestamp_s = timestamps[index] / timestamp_scale
        duration_s = durations[index] if index < len(durations) else 1.0
        if elapsed_ms_field:
            elapsed_ms = safe_float(row.get(elapsed_ms_field))
            if elapsed_ms and elapsed_ms > 0:
                duration_s = elapsed_ms / 1000.0
        normalized_row = {
            "timestamp_s": timestamp_s,
            "duration_s": duration_s,
            "throughput_kbps": throughput_kbps,
        }
        if latitude_field and safe_float(row.get(latitude_field)) is not None:
            normalized_row["latitude"] = safe_float(row.get(latitude_field))
        if longitude_field and safe_float(row.get(longitude_field)) is not None:
            normalized_row["longitude"] = safe_float(row.get(longitude_field))
        if mobility_field and row.get(mobility_field):
            normalized_row["mobility_tag"] = str(row.get(mobility_field)).strip()
        rows.append(normalized_row)
    return rows


def write_normalized_trace(result: Mapping[str, Any], paths: Mapping[str, Path]) -> Dict[str, Any]:
    rows = list(result["rows"])
    dataset_family = str(result["dataset_family"])
    trace_id = str(result["trace_id"])
    output_dir = paths["normalized"] / dataset_family
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "{0}.csv".format(trace_id)
    csv_bytes = normalized_csv_bytes(rows, result)
    output_path.write_bytes(csv_bytes)
    checksum = sha256_bytes(csv_bytes)

    metadata = {
        "trace_id": trace_id,
        "dataset_family": dataset_family,
        "source_dataset": result.get("source_dataset", dataset_family),
        "source_id": result.get("source_id", dataset_family),
        "split": result.get("split", ""),
        "eval_gate": result.get("eval_gate", ""),
        "trace_csv": str(output_path),
        "source_file": result.get("source_file", ""),
        "schema_version": TRACE_SCHEMA_VERSION,
        "checksum_sha256": checksum,
        "canonical_content_fingerprint": result["canonical_content_fingerprint"],
        "leakage_group": result["leakage_group"],
        "duration_s": result["duration_s"],
        "sample_count": result["sample_count"],
        "license_status": result.get("license_status", ""),
        "acquisition_status": result.get("acquisition_status", "acquired"),
        "normalization_status": "normalized",
        "exclusion_reason": "",
    }
    metadata_dir = paths["manifests"] / "per_trace" / dataset_family
    metadata_path = metadata_dir / "{0}.json".format(trace_id)
    write_json(metadata_path, metadata)
    return metadata


def normalized_csv_bytes(rows: Sequence[Mapping[str, Any]], result: Mapping[str, Any]) -> bytes:
    optional_columns = []
    for column in ("latitude", "longitude", "mobility_tag"):
        if any(column in row for row in rows):
            optional_columns.append(column)
    fieldnames = ["timestamp_s", "duration_s", "throughput_kbps", *optional_columns, "source_dataset", "source_file"]
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        payload: Dict[str, Any] = {
            "timestamp_s": format_float(row["timestamp_s"]),
            "duration_s": format_float(row["duration_s"]),
            "throughput_kbps": format_float(row["throughput_kbps"]),
            "source_dataset": result.get("source_dataset", ""),
            "source_file": result.get("source_file", ""),
        }
        for column in optional_columns:
            payload[column] = format_float(row[column]) if isinstance(row.get(column), (int, float)) else row.get(column, "")
        writer.writerow(payload)
    return output.getvalue().encode("utf-8")


def canonical_content_fingerprint(rows: Sequence[Mapping[str, Any]]) -> str:
    lines = ["timestamp_s,duration_s,throughput_kbps"]
    for row in rows:
        lines.append(
            "{0},{1},{2}".format(
                format_float(row["timestamp_s"]),
                format_float(row["duration_s"]),
                format_float(row["throughput_kbps"]),
            )
        )
    return sha256_bytes(("\n".join(lines) + "\n").encode("utf-8"))


def first_matching_field(fields: Mapping[str, str], aliases: Iterable[str]) -> str:
    for alias in aliases:
        if alias in fields:
            return fields[alias]
    return ""


def normalize_header(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.strip().lower())


def safe_float(value: Any) -> Optional[float]:
    if value in (None, ""):
        return None
    try:
        return float(str(value).strip())
    except ValueError:
        return None


def convert_throughput_to_kbps(value: float, field: str, values: Sequence[Optional[float]]) -> float:
    normalized = normalize_header(field)
    if "mbps" in normalized:
        return value * 1000.0
    if "kbps" in normalized:
        return value
    if "bps" in normalized:
        return value / 1000.0
    numeric_values = [item for item in values if item is not None]
    if numeric_values:
        middle = median(numeric_values)
        if middle > 100000:
            return value / 1000.0
    return value


def infer_timestamp_scale(values: Sequence[float]) -> float:
    if values and max(abs(value) for value in values) >= 1000:
        return 1000.0
    return 1.0


def infer_durations(timestamps: Sequence[Optional[float]], scale: float) -> List[float]:
    seconds = [value / scale if value is not None else None for value in timestamps]
    durations: List[float] = []
    last_positive = 1.0
    for index, value in enumerate(seconds):
        next_value = None
        for candidate in seconds[index + 1:]:
            if candidate is not None:
                next_value = candidate
                break
        if value is not None and next_value is not None and next_value > value:
            duration = next_value - value
            last_positive = duration
        else:
            duration = last_positive
        durations.append(duration if duration > 0 else 1.0)
    return durations


def format_float(value: Any) -> str:
    return "{0:.6f}".format(float(value)).rstrip("0").rstrip(".") if "." in "{0:.6f}".format(float(value)) else str(value)


def slug(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
    return normalized or "trace"


def write_normalization_markdown(path: Path, report: Mapping[str, Any]) -> None:
    lines = [
        "Phase 6C normalization report. Normalized CSVs live outside Git and are not benchmark outputs.",
        "",
        "- normalized: {0}".format(report["counts"]["normalized"]),
        "- excluded: {0}".format(report["counts"]["excluded"]),
        "- errors: {0}".format(report["counts"]["errors"]),
        "- warnings: {0}".format(report["counts"]["warnings"]),
        "",
        "## Normalized Records",
        "",
    ]
    for record in report["normalized_records"]:
        lines.append("- `{0}` from `{1}`".format(record["trace_id"], record.get("source_file", "")))
    if report["excluded_records"]:
        lines.extend(["", "## Excluded Records", ""])
        for record in report["excluded_records"]:
            lines.append("- `{0}`: `{1}`".format(record.get("source_file", ""), record.get("exclusion_reason", "")))
    write_markdown_report(path, "Phase 6C Normalization Report", lines)


if __name__ == "__main__":
    sys.exit(main())

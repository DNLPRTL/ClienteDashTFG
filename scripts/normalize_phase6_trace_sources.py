from __future__ import annotations

import argparse
import csv
import io
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence

try:
    from scripts.phase6c_source_registry import (
        DEFAULT_REGISTRY_PATH,
        PRIMARY_SOURCE_IDS,
        Phase6CError,
        create_external_layout,
        load_source_registry,
        relative_to_root,
        resolve_source_ids,
        sha256_bytes,
        sources_by_id,
        utc_now,
        write_json,
        write_markdown_report,
    )
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from phase6c_source_registry import (
        DEFAULT_REGISTRY_PATH,
        PRIMARY_SOURCE_IDS,
        Phase6CError,
        create_external_layout,
        load_source_registry,
        relative_to_root,
        resolve_source_ids,
        sha256_bytes,
        sources_by_id,
        utc_now,
        write_json,
        write_markdown_report,
    )


TRACE_SCHEMA_VERSION = "normalized_trace_schema_v1"
REPORT_SCHEMA_VERSION = "phase6c_normalization_report_v1"
TEXT_EXTENSIONS = {".csv", ".tsv", ".txt", ".log", ""}
SKIP_EXTENSIONS = {
    ".zip",
    ".gz",
    ".tar",
    ".tgz",
    ".bz2",
    ".xz",
    ".7z",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".bmp",
    ".mp4",
    ".m4v",
    ".avi",
    ".mov",
    ".mkv",
    ".html",
    ".htm",
    ".pdf",
    ".json",
    ".md",
}
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
TIMESTAMP_ALIASES = {"timestamp", "time", "seconds", "second", "timestampsec", "timestamps"}
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
    parser.add_argument("--sources", default="primary")
    parser.add_argument("--source-registry", type=Path, default=DEFAULT_REGISTRY_PATH)
    parser.add_argument("--include-lumos", action="store_true")
    parser.add_argument("--include-diagnostic", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--allow-empty-optional", action="store_true")
    parser.add_argument("--progress-every", type=int, default=25)
    parser.add_argument("--max-files-per-source", type=int, default=1000)
    parser.add_argument("--max-file-size-mb", type=float, default=250.0)
    parser.add_argument("--max-sniff-bytes", type=int, default=65536)
    parser.add_argument("--clean-normalized", action="store_true")
    parser.add_argument("--clean-derived", action="store_true")
    parser.add_argument("--allow-repo-output", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    try:
        report = normalize_phase6_sources(
            external_root=args.external_root,
            sources=args.sources,
            registry_path=args.source_registry,
            include_lumos=args.include_lumos,
            include_diagnostic=args.include_diagnostic,
            strict=args.strict,
            allow_empty_optional=args.allow_empty_optional,
            progress_every=args.progress_every,
            max_files_per_source=args.max_files_per_source,
            max_file_size_mb=args.max_file_size_mb,
            max_sniff_bytes=args.max_sniff_bytes,
            clean_normalized=args.clean_normalized or args.clean_derived,
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
    sources: str = "primary",
    registry_path: Path = DEFAULT_REGISTRY_PATH,
    include_lumos: bool = False,
    include_diagnostic: bool = False,
    strict: bool = False,
    allow_empty_optional: bool = False,
    progress_every: int = 25,
    max_files_per_source: int = 1000,
    max_file_size_mb: float = 250.0,
    max_sniff_bytes: int = 65536,
    clean_normalized: bool = False,
    allow_repo_output: bool = False,
) -> Dict[str, Any]:
    paths = create_external_layout(external_root, allow_repo_output=allow_repo_output)
    registry = load_source_registry(registry_path)
    source_map = sources_by_id(registry)
    selected_ids = resolve_source_ids(
        registry,
        source_spec=sources,
        include_lumos=include_lumos,
        include_diagnostic=include_diagnostic,
    )

    if clean_normalized:
        clean_selected_derived(paths, selected_ids, source_map)

    records: List[Dict[str, Any]] = []
    excluded: List[Dict[str, Any]] = []
    errors: List[str] = []
    warnings: List[str] = []
    source_summaries: List[Dict[str, Any]] = []
    progress_path = paths["reports"] / "phase6c_normalization_progress.json"
    max_file_size_bytes = int(max_file_size_mb * 1024 * 1024)

    for source_id in selected_ids:
        source = source_map.get(source_id, {"source_id": source_id, "dataset_family": source_id, "source_dataset": source_id})
        print("phase6c_normalize: source start {0}".format(source_id))
        sys.stdout.flush()
        candidate_files = candidate_files_for_source(
            paths=paths,
            source_id=source_id,
            max_files_per_source=max_files_per_source,
        )
        source_records: List[Dict[str, Any]] = []
        source_excluded: List[Dict[str, Any]] = []
        skipped_count = 0
        processed_count = 0

        print("phase6c_normalize: {0} candidate_files={1}".format(source_id, len(candidate_files)))
        sys.stdout.flush()

        if not candidate_files:
            message = "{0}: zero candidate files found".format(source_id)
            warnings.append(message)

        for index, path in enumerate(candidate_files, start=1):
            processed_count += 1
            exclusion_reason = preflight_exclusion_reason(path, max_file_size_bytes=max_file_size_bytes)
            if exclusion_reason:
                source_excluded.append(excluded_record_for(path, source, paths["root"], exclusion_reason))
                skipped_count += 1
            else:
                result = normalize_one_file(path, source, paths["root"], max_sniff_bytes=max_sniff_bytes)
                if result.get("normalization_status") == "normalized":
                    metadata = write_normalized_trace(result, paths)
                    source_records.append(metadata)
                else:
                    source_excluded.append(
                        excluded_record_for(
                            path,
                            source,
                            paths["root"],
                            result.get("exclusion_reason", "normalization_failed"),
                        )
                    )

            if progress_every > 0 and index % progress_every == 0:
                print(
                    "phase6c_normalize: {0} processed={1} normalized={2} excluded={3} skipped={4}".format(
                        source_id,
                        processed_count,
                        len(source_records),
                        len(source_excluded),
                        skipped_count,
                    )
                )
                sys.stdout.flush()
                write_progress(
                    progress_path,
                    selected_ids,
                    source_summaries,
                    source_id,
                    processed_count,
                    [*records, *source_records],
                    [*excluded, *source_excluded],
                )

        records.extend(source_records)
        excluded.extend(source_excluded)
        summary = {
            "source_id": source_id,
            "candidate_files": len(candidate_files),
            "processed": processed_count,
            "normalized": len(source_records),
            "excluded": len(source_excluded),
            "skipped": skipped_count,
        }
        source_summaries.append(summary)
        print(
            "phase6c_normalize: source end {source_id} processed={processed} normalized={normalized} excluded={excluded} skipped={skipped}".format(
                **summary
            )
        )
        sys.stdout.flush()
        write_progress(progress_path, selected_ids, source_summaries, source_id, processed_count, records, excluded)

    primary_normalized = [
        record
        for record in records
        if record.get("source_id") in PRIMARY_SOURCE_IDS and record.get("eval_gate") == "use_for_eval"
    ]
    selected_primary = [source_id for source_id in selected_ids if source_id in PRIMARY_SOURCE_IDS]
    if strict and selected_primary and not primary_normalized:
        errors.append("strict primary normalization produced zero Raca 4G/Raca 5G use_for_eval traces.")

    for excluded_record in excluded:
        source_id = str(excluded_record.get("source_id", ""))
        reason = str(excluded_record.get("exclusion_reason", ""))
        if strict and source_id in PRIMARY_SOURCE_IDS and reason not in ("unsupported_file_type", "binary_or_non_text_file"):
            warnings.append("{0}: {1}".format(excluded_record.get("source_file", source_id), reason))

    report = {
        "schema_version": REPORT_SCHEMA_VERSION,
        "generated_at": utc_now(),
        "external_root": str(paths["root"]),
        "strict": strict,
        "trace_schema_version": TRACE_SCHEMA_VERSION,
        "selected_sources": selected_ids,
        "limits": {
            "progress_every": progress_every,
            "max_files_per_source": max_files_per_source,
            "max_file_size_mb": max_file_size_mb,
            "max_sniff_bytes": max_sniff_bytes,
        },
        "source_summaries": source_summaries,
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
        "progress_path": str(progress_path),
    }


def clean_selected_derived(paths: Mapping[str, Path], selected_ids: Sequence[str], source_map: Mapping[str, Mapping[str, Any]]) -> None:
    for source_id in selected_ids:
        source = source_map.get(source_id, {})
        dataset_family = str(source.get("dataset_family", source_id))
        for path in (
            paths["normalized"] / dataset_family,
            paths["manifests"] / "per_trace" / dataset_family,
        ):
            if path.exists():
                shutil.rmtree(path)


def candidate_files_for_source(
    *,
    paths: Mapping[str, Path],
    source_id: str,
    max_files_per_source: int,
) -> List[Path]:
    roots = [paths["extracted"] / source_id, paths["raw"] / source_id]
    files: List[Path] = []
    for root in roots:
        if not root.is_dir():
            continue
        for path in sorted(item for item in root.rglob("*") if item.is_file()):
            files.append(path)
            if max_files_per_source > 0 and len(files) >= max_files_per_source:
                return files
    return files


def excluded_record_for(path: Path, source: Mapping[str, Any], root: Path, reason: str) -> Dict[str, Any]:
    source_id = str(source.get("source_id", path.parent.name))
    return {
        "source_id": source_id,
        "dataset_family": source.get("dataset_family", source_id),
        "source_file": relative_to_root(path, root),
        "normalization_status": "excluded",
        "exclusion_reason": reason,
    }


def preflight_exclusion_reason(path: Path, *, max_file_size_bytes: int) -> str:
    suffix = path.suffix.lower()
    if suffix in SKIP_EXTENSIONS:
        return "unsupported_file_type"
    if not is_candidate_trace_file(path):
        return "unsupported_file_type"
    try:
        if path.stat().st_size > max_file_size_bytes:
            return "file_too_large"
        with path.open("rb") as handle:
            prefix = handle.read(4096)
    except OSError:
        return "unable_to_read_file"
    if b"\x00" in prefix:
        return "binary_or_non_text_file"
    try:
        prefix.decode("utf-8")
    except UnicodeDecodeError:
        return "binary_or_non_text_file"
    return ""


def normalize_one_file(path: Path, source: Mapping[str, Any], root: Path, *, max_sniff_bytes: int = 65536) -> Dict[str, Any]:
    source_id = str(source.get("source_id", path.parent.name))
    try:
        if source_id in ("hsdpa_norway", "ghent_4g_lte"):
            rows = parse_six_column_log(path)
            if not rows:
                rows = parse_delimited_trace(path, max_sniff_bytes=max_sniff_bytes)
        else:
            rows = parse_delimited_trace(path, max_sniff_bytes=max_sniff_bytes)
            if not rows:
                rows = parse_six_column_log(path)
    except UnicodeDecodeError:
        return {"normalization_status": "excluded", "exclusion_reason": "unable_to_decode_text_file"}
    except csv.Error:
        return {"normalization_status": "excluded", "exclusion_reason": "unable_to_parse_delimited_file"}

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
    with path.open("r", encoding="utf-8", errors="strict") as handle:
        for line in handle:
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


def parse_delimited_trace(path: Path, *, max_sniff_bytes: int = 65536) -> List[Dict[str, Any]]:
    with path.open("rb") as handle:
        sample = handle.read(max_sniff_bytes).decode("utf-8", errors="strict")
    if not sample.strip():
        return []
    delimiter = infer_delimiter(sample)
    with path.open("r", encoding="utf-8", errors="strict", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
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

        if not throughput_field and not (bytes_field and elapsed_ms_field):
            return []

        rows = []
        previous_timestamp_s: Optional[float] = None
        for row in reader:
            throughput_kbps = throughput_from_row(row, throughput_field, bytes_field, elapsed_ms_field)
            if throughput_kbps is None:
                continue
            timestamp_s = timestamp_from_row(row, timestamp_field)
            duration_s = duration_from_row(row, elapsed_ms_field)
            if duration_s is None and previous_timestamp_s is not None and timestamp_s is not None and timestamp_s > previous_timestamp_s:
                duration_s = timestamp_s - previous_timestamp_s
            if duration_s is None:
                duration_s = 1.0
            if timestamp_s is None:
                timestamp_s = previous_timestamp_s + duration_s if previous_timestamp_s is not None else 0.0
            previous_timestamp_s = timestamp_s
            normalized_row: Dict[str, Any] = {
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


def infer_delimiter(sample: str) -> str:
    try:
        return csv.Sniffer().sniff(sample, delimiters=",\t;").delimiter
    except csv.Error:
        counts = {delimiter: sample.count(delimiter) for delimiter in (",", "\t", ";")}
        return max(counts, key=counts.get) if max(counts.values()) > 0 else ","


def throughput_from_row(
    row: Mapping[str, str],
    throughput_field: str,
    bytes_field: str,
    elapsed_ms_field: str,
) -> Optional[float]:
    if throughput_field:
        throughput = safe_float(row.get(throughput_field))
        if throughput is None:
            return None
        return convert_throughput_to_kbps(throughput, throughput_field)
    bytes_value = safe_float(row.get(bytes_field))
    elapsed_ms = safe_float(row.get(elapsed_ms_field))
    if bytes_value is None or elapsed_ms is None or elapsed_ms <= 0:
        return None
    return bytes_value * 8.0 / elapsed_ms


def timestamp_from_row(row: Mapping[str, str], timestamp_field: str) -> Optional[float]:
    if not timestamp_field:
        return None
    value = safe_float(row.get(timestamp_field))
    if value is None:
        return None
    return value / 1000.0 if abs(value) >= 1000 else value


def duration_from_row(row: Mapping[str, str], elapsed_ms_field: str) -> Optional[float]:
    if not elapsed_ms_field:
        return None
    elapsed_ms = safe_float(row.get(elapsed_ms_field))
    if elapsed_ms is None or elapsed_ms <= 0:
        return None
    return elapsed_ms / 1000.0


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


def convert_throughput_to_kbps(value: float, field: str) -> float:
    normalized = normalize_header(field)
    if "mbps" in normalized:
        return value * 1000.0
    if "kbps" in normalized:
        return value
    if "bps" in normalized:
        return value / 1000.0
    if value > 100000:
        return value / 1000.0
    return value


def format_float(value: Any) -> str:
    text = "{0:.6f}".format(float(value))
    return text.rstrip("0").rstrip(".") if "." in text else text


def slug(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
    return normalized or "trace"


def write_progress(
    path: Path,
    selected_ids: Sequence[str],
    source_summaries: Sequence[Mapping[str, Any]],
    current_source: str,
    current_processed: int,
    records: Sequence[Mapping[str, Any]],
    excluded: Sequence[Mapping[str, Any]],
) -> None:
    write_json(
        path,
        {
            "schema_version": "phase6c_normalization_progress_v1",
            "generated_at": utc_now(),
            "selected_sources": list(selected_ids),
            "current_source": current_source,
            "current_processed": current_processed,
            "source_summaries": list(source_summaries),
            "normalized_so_far": len(records),
            "excluded_so_far": len(excluded),
        },
    )


def write_normalization_markdown(path: Path, report: Mapping[str, Any]) -> None:
    lines = [
        "Phase 6C normalization report. Normalized CSVs live outside Git and are not benchmark outputs.",
        "",
        "- normalized: {0}".format(report["counts"]["normalized"]),
        "- excluded: {0}".format(report["counts"]["excluded"]),
        "- errors: {0}".format(report["counts"]["errors"]),
        "- warnings: {0}".format(report["counts"]["warnings"]),
        "- selected_sources: `{0}`".format(",".join(report.get("selected_sources", []))),
        "",
        "## Source Summaries",
        "",
    ]
    for source in report.get("source_summaries", []):
        lines.append(
            "- `{source_id}`: candidates `{candidate_files}`, processed `{processed}`, normalized `{normalized}`, excluded `{excluded}`, skipped `{skipped}`".format(
                **source
            )
        )
    if report["excluded_records"]:
        lines.extend(["", "## Excluded Records", ""])
        for record in report["excluded_records"][:200]:
            lines.append("- `{0}`: `{1}`".format(record.get("source_file", ""), record.get("exclusion_reason", "")))
    write_markdown_report(path, "Phase 6C Normalization Report", lines)


if __name__ == "__main__":
    sys.exit(main())

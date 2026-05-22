"""Common utilities for Phase 3 raw dataset converters.

The helpers here only convert raw trace files into normalized CSV and local
manifest files. They do not implement replay, controller input shaping, QoE
scoring, benchmarking, or dataset splitting.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import subprocess
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, Mapping, Optional, Sequence, Tuple

from core.trace_replay.converters.base import ConversionError
from core.trace_replay.schema import REQUIRED_TRACE_COLUMNS
from core.trace_replay.validation import TraceValidationResult, validate_normalized_trace_csv


TEXT_FILE_EXTENSIONS = frozenset((".log", ".txt", ".csv", ".dat", ".trace"))
ZIP_FILE_EXTENSIONS = frozenset((".zip",))
COMMENT_PREFIXES = ("#", "//", "%")
_TOKEN_SPLIT_RE = re.compile(r"[\s,;]+")
_SAFE_ID_RE = re.compile(r"[^a-z0-9]+")
_REPO_ROOT = Path(__file__).resolve().parents[3]


@dataclass(frozen=True)
class TextSource:
    source_path: str
    text: str
    archive_path: Optional[str] = None
    member_name: Optional[str] = None


def safe_trace_id(text: object) -> str:
    """Return a deterministic lowercase id fragment safe for filenames."""

    normalized = str(text).replace("\\", "/").strip().lower()
    normalized = _SAFE_ID_RE.sub("_", normalized).strip("_")
    return normalized or "trace"


def discover_candidate_files(input_dir: object) -> Tuple[Path, ...]:
    """Discover likely raw trace files in stable order.

    HTML indexes and Markdown README files are deliberately ignored because
    they are source metadata, not raw throughput traces.
    """

    root = Path(input_dir)
    if not root.exists():
        raise ConversionError("input_dir does not exist: {0}".format(root))
    if not root.is_dir():
        raise ConversionError("input_dir is not a directory: {0}".format(root))

    candidates = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        suffix = path.suffix.lower()
        if suffix in TEXT_FILE_EXTENSIONS or suffix in ZIP_FILE_EXTENSIONS:
            candidates.append(path)
    return tuple(sorted(candidates, key=_path_sort_key))


def iter_text_sources(input_dir: object) -> Iterator[TextSource]:
    """Yield plain text sources, including text members from ZIP archives."""

    for path in discover_candidate_files(input_dir):
        suffix = path.suffix.lower()
        if suffix in ZIP_FILE_EXTENSIONS:
            yield from _iter_zip_text_sources(path)
            continue

        text = _read_text_file(path)
        yield TextSource(source_path=str(path), text=text)


def write_normalized_trace_csv(path: object, rows: Iterable[Mapping[str, object]], fieldnames: Sequence[str]) -> None:
    """Write normalized rows with deterministic numeric formatting."""

    csv_path = Path(path)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    materialized_rows = tuple(rows)
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fieldnames), extrasaction="ignore")
        writer.writeheader()
        for row in materialized_rows:
            writer.writerow({name: _format_csv_value(row.get(name, "")) for name in fieldnames})


def write_trace_manifest(path: object, metadata: Mapping[str, object]) -> None:
    manifest_path = Path(path)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("w", encoding="utf-8") as handle:
        json.dump(dict(metadata), handle, indent=2, sort_keys=True)
        handle.write("\n")


def compute_sha256(path: object) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_written_trace(path: object) -> TraceValidationResult:
    validation = validate_normalized_trace_csv(path)
    if not validation.is_valid:
        raise ConversionError(
            "emitted normalized trace failed validation: {0}: {1}".format(
                path,
                "; ".join(validation.errors),
            )
        )
    return validation


def split_delimited_tokens(line: str) -> Tuple[str, ...]:
    """Split a data line on common text-log delimiters after comments."""

    stripped = strip_inline_comment(line).strip()
    if not stripped:
        return ()
    return tuple(token for token in _TOKEN_SPLIT_RE.split(stripped) if token)


def strip_inline_comment(line: str) -> str:
    stripped = line.strip()
    if not stripped:
        return ""
    for prefix in COMMENT_PREFIXES:
        if stripped.startswith(prefix):
            return ""

    result = line
    for marker in (" #", "\t#", " //", "\t//"):
        index = result.find(marker)
        if index >= 0:
            result = result[:index]
    return result


def parse_float_token(token: object) -> Optional[float]:
    try:
        value = float(str(token).strip())
    except (TypeError, ValueError):
        return None
    if not math.isfinite(value):
        return None
    return value


def numeric_tokens_from_line(line: str) -> Tuple[float, ...]:
    values = []
    for token in split_delimited_tokens(line):
        value = parse_float_token(token)
        if value is None:
            return ()
        values.append(value)
    return tuple(values)


def numeric_rows_from_text(text: str) -> Tuple[Tuple[float, ...], ...]:
    rows = []
    for line in text.splitlines():
        values = numeric_tokens_from_line(line)
        if values:
            rows.append(values)
    return tuple(rows)


def bytes_elapsed_ms_to_kbps(byte_count: float, elapsed_ms: float) -> float:
    if elapsed_ms <= 0:
        raise ConversionError("elapsed_ms must be strictly positive")
    return (byte_count * 8.0) / elapsed_ms


def infer_mobility_tags(text: str) -> Tuple[str, ...]:
    lowered = safe_trace_id(text)
    tags = []
    for candidate in ("foot", "bicycle", "bike", "bus", "tram", "train", "car"):
        if candidate in lowered:
            tags.append("bicycle" if candidate == "bike" else candidate)
    return tuple(dict.fromkeys(tags))


def infer_scenario_label(source_path: str) -> str:
    path = Path(source_path.replace("::", "/"))
    parts = [safe_trace_id(part) for part in path.parts if part]
    meaningful = [part for part in parts if part not in ("trace", "traces")]
    return meaningful[-2] if len(meaningful) >= 2 else (meaningful[-1] if meaningful else "unknown")


def normalize_source_key(input_dir: object, source_path: str) -> str:
    root = Path(input_dir)
    if "::" in source_path:
        archive_text, member_name = source_path.split("::", 1)
        archive_path = Path(archive_text)
        try:
            archive_token = archive_path.relative_to(root).as_posix()
        except ValueError:
            archive_token = archive_path.name
        return "{0}::{1}".format(archive_token, member_name.replace("\\", "/"))

    path = Path(source_path)
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.name


def stable_trace_id(dataset_id: str, source_key: str) -> str:
    stem = source_key
    if "::" in stem:
        archive_stem, member_name = stem.split("::", 1)
        stem = "{0}_{1}".format(Path(archive_stem).stem, member_name)
    else:
        stem = str(Path(stem).with_suffix(""))

    slug = safe_trace_id("{0}_{1}".format(dataset_id, stem))
    digest = hashlib.sha1(source_key.encode("utf-8")).hexdigest()[:8]
    if len(slug) > 120:
        slug = slug[:120].rstrip("_")
    return "{0}_{1}".format(slug, digest)


def current_git_short_head(start_dir: Optional[object] = None) -> str:
    cwd = Path(start_dir) if start_dir is not None else Path.cwd()
    try:
        completed = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return "Unknown"
    value = completed.stdout.strip()
    return value or "Unknown"


def manifest_common_metadata(
    trace_id: str,
    dataset_id: str,
    source_path: str,
    output_csv_path: object,
    converter_name: str,
    validation: TraceValidationResult,
    scenario_tags: Sequence[str],
    mobility_tags: Sequence[str],
    network_tags: Sequence[str],
    leakage_group: str,
    notes: str,
) -> Mapping[str, object]:
    output_path = Path(output_csv_path)
    return {
        "schema_version": "trace_manifest_v1",
        "trace_id": trace_id,
        "dataset_id": dataset_id,
        "source_path": source_path,
        "output_csv_path": str(output_path.resolve()),
        "converter_name": converter_name,
        "converter_version_or_commit": current_git_short_head(_REPO_ROOT),
        "checksum_sha256": compute_sha256(output_path),
        "sample_count": validation.sample_count,
        "duration_s": validation.duration_s,
        "nominal_granularity_s": (
            validation.nominal_granularity_s if validation.nominal_granularity_s is not None else "mixed"
        ),
        "throughput_unit": "kbps",
        "min_throughput_kbps": validation.min_throughput_kbps,
        "mean_throughput_kbps": validation.mean_throughput_kbps,
        "max_throughput_kbps": validation.max_throughput_kbps,
        "scenario_tags": list(scenario_tags),
        "mobility_tags": list(mobility_tags),
        "network_tags": list(network_tags),
        "split_candidate": "conversion_only_no_final_split",
        "leakage_group": leakage_group,
        "notes": notes,
        "dataset_card_path": _dataset_card_path(dataset_id),
        "source_name": dataset_id,
        "source_url_or_reference": "See dataset card",
        "license": "Unknown/TBD",
        "download_date": None,
        "raw_local_path_policy": "outside repo",
        "normalized_local_path_policy": "outside repo",
    }


def ensure_can_write(output_csv_path: object, manifest_path: object, overwrite: bool) -> None:
    existing = [str(path) for path in (Path(output_csv_path), Path(manifest_path)) if path.exists()]
    if existing and not overwrite:
        raise ConversionError(
            "output already exists and overwrite=False: {0}".format(", ".join(existing))
        )


def ordered_fieldnames(rows: Sequence[Mapping[str, object]], preferred: Sequence[str]) -> Tuple[str, ...]:
    seen = set()
    names = []
    for name in list(REQUIRED_TRACE_COLUMNS) + list(preferred):
        if name not in seen:
            names.append(name)
            seen.add(name)
    for row in rows:
        for name in row:
            if name not in seen:
                names.append(name)
                seen.add(name)
    return tuple(names)


def _iter_zip_text_sources(path: Path) -> Iterator[TextSource]:
    try:
        with zipfile.ZipFile(path) as archive:
            members = sorted(
                (info for info in archive.infolist() if not info.is_dir()),
                key=lambda info: info.filename.lower(),
            )
            for info in members:
                suffix = Path(info.filename).suffix.lower()
                if suffix not in TEXT_FILE_EXTENSIONS:
                    continue
                data = archive.read(info)
                text = _decode_text(data)
                yield TextSource(
                    source_path="{0}::{1}".format(path, info.filename.replace("\\", "/")),
                    text=text,
                    archive_path=str(path),
                    member_name=info.filename.replace("\\", "/"),
                )
    except zipfile.BadZipFile as exc:
        raise ConversionError("cannot read zip archive {0}: {1}".format(path, exc)) from exc


def _read_text_file(path: Path) -> str:
    with path.open("rb") as handle:
        return _decode_text(handle.read())


def _decode_text(data: bytes) -> str:
    for encoding in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def _path_sort_key(path: Path) -> str:
    return path.as_posix().lower()


def _format_csv_value(value: object) -> object:
    if isinstance(value, float):
        return format(value, ".12g")
    return value


def _dataset_card_path(dataset_id: str) -> str:
    return "docs/science/02_traces_replay/trace_dataset_cards/{0}.md".format(dataset_id)

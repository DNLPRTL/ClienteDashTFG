from __future__ import annotations

import csv
import hashlib
import re
from datetime import datetime
from pathlib import Path
from typing import Iterable, Sequence

from core.trace_replay.validation import validate_normalized_trace_csv


def slugify(value: object, fallback: str = "trace") -> str:
    text = str(value).strip().lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or fallback


def stable_id(*parts: object, prefix: str = "trace") -> str:
    material = "|".join(str(part) for part in parts)
    digest = hashlib.sha256(material.encode("utf-8")).hexdigest()[:12]
    slug = "_".join(slugify(part) for part in parts if str(part).strip())[:80].strip("_")
    return "{0}_{1}_{2}".format(prefix, slug or "item", digest)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def path_text(path: Path) -> str:
    return path.as_posix().lower()


def find_first_file(root: Path, required_name_parts: Sequence[str], suffix: str | None = None) -> Path | None:
    if not root.is_dir():
        return None
    lowered_parts = tuple(part.lower() for part in required_name_parts)
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if suffix is not None and path.suffix.lower() != suffix.lower():
            continue
        text = path_text(path)
        if all(part in text for part in lowered_parts):
            return path
    return None


def iter_files_under_hint(root: Path, required_path_parts: Sequence[str], suffix: str) -> Iterable[Path]:
    if not root.is_dir():
        return
    lowered_parts = tuple(part.lower() for part in required_path_parts)
    for path in sorted(root.rglob("*{0}".format(suffix))):
        text = path_text(path)
        if all(part in text for part in lowered_parts):
            yield path


def parse_float(value: object) -> float | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text or text in {"?", "-", "nan", "NaN", "None"}:
        return None
    try:
        parsed = float(text)
    except ValueError:
        return None
    if parsed != parsed:
        return None
    return parsed


def parse_datetime(value: str, formats: Sequence[str]) -> datetime | None:
    text = value.strip()
    for fmt in formats:
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue
    return None


def median_positive_delta(values: Sequence[float], fallback: float = 1.0) -> float:
    deltas = [b - a for a, b in zip(values, values[1:]) if b - a > 0]
    if not deltas:
        return fallback
    deltas.sort()
    return deltas[len(deltas) // 2]


def rows_from_timestamps_and_throughput(
    timestamps_s: Sequence[float],
    throughput_kbps: Sequence[float],
    fallback_duration_s: float = 1.0,
) -> list[dict[str, float]]:
    if len(timestamps_s) != len(throughput_kbps):
        raise ValueError("timestamps and throughput lengths differ")
    if not timestamps_s:
        return []
    first = timestamps_s[0]
    rebased = [max(0.0, timestamp - first) for timestamp in timestamps_s]
    default_duration = median_positive_delta(rebased, fallback=fallback_duration_s)
    rows: list[dict[str, float]] = []
    for index, timestamp in enumerate(rebased):
        if index + 1 < len(rebased) and rebased[index + 1] - timestamp > 0:
            duration = rebased[index + 1] - timestamp
        else:
            duration = default_duration
        rows.append(
            {
                "timestamp_s": timestamp,
                "duration_s": max(duration, 0.001),
                "throughput_kbps": max(0.0, throughput_kbps[index]),
            }
        )
    return rows


def sequential_rows(throughput_kbps: Sequence[float], duration_s: float = 1.0) -> list[dict[str, float]]:
    return [
        {
            "timestamp_s": float(index) * duration_s,
            "duration_s": duration_s,
            "throughput_kbps": max(0.0, throughput),
        }
        for index, throughput in enumerate(throughput_kbps)
    ]


def write_normalized_csv(rows: Iterable[dict[str, float]], path: Path) -> dict[str, object]:
    materialized = list(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["timestamp_s", "duration_s", "throughput_kbps"])
        writer.writeheader()
        for row in materialized:
            writer.writerow(
                {
                    "timestamp_s": "{0:.6f}".format(float(row["timestamp_s"])),
                    "duration_s": "{0:.6f}".format(float(row["duration_s"])),
                    "throughput_kbps": "{0:.6f}".format(float(row["throughput_kbps"])),
                }
            )
    stats = validate_normalized_trace_csv(path)
    return {
        "row_count": stats.row_count,
        "duration_s": stats.duration_s,
        "throughput_min_kbps": stats.throughput_min_kbps,
        "throughput_mean_kbps": stats.throughput_mean_kbps,
        "throughput_max_kbps": stats.throughput_max_kbps,
        "content_fingerprint_sha256": stats.content_fingerprint_sha256,
    }

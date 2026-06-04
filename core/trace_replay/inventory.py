from __future__ import annotations

import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


DATASET_FOLDER_HINTS = (
    ("Norway HSDPA", "norway_hsdpa_umass"),
    ("BelgiumGhent", "ghent_4g_lte"),
    ("beyond_throughput_4g_lte", "ucc_4g_lte_beyond_throughput"),
    ("FCC Measuring Broadband America", "fcc_measuring_broadband_america"),
    ("Large Scale Dataset", "roma_4g_nbiot_5g_nsa"),
    ("Lumos5G", "lumos_ucc_nyu_bundle"),
    ("GAViST5G", "gavist5g"),
    ("oboe", "oboe"),
    ("Puffer", "puffer_stanford"),
)


@dataclass(frozen=True)
class RawFileInventory:
    relative_path: str
    bytes: int
    sha256: str | None
    hash_mode: str
    extension: str
    parser_hint: str
    columns_detected: tuple[str, ...]
    parseable_header: bool


def sha256_file(path: Path, hash_mode: str = "full", sample_bytes: int = 1024 * 1024) -> str | None:
    if hash_mode == "none":
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        if hash_mode == "sample":
            digest.update(handle.read(sample_bytes))
        elif hash_mode == "full":
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        else:
            raise ValueError("unknown hash_mode: {0}".format(hash_mode))
    return digest.hexdigest()


def dataset_id_for_path(raw_root: Path, path: Path) -> str:
    relative = path.relative_to(raw_root)
    text = str(relative)
    for hint, dataset_id in DATASET_FOLDER_HINTS:
        if hint.lower() in text.lower():
            return dataset_id
    return relative.parts[0].lower().replace(" ", "_")


def parser_hint_for_file(path: Path) -> str:
    name = path.name.lower()
    suffix = path.suffix.lower()
    if suffix == ".log":
        return "whitespace_6_column_interval_log"
    if suffix == ".txt":
        return "whitespace_or_text_trace"
    if suffix == ".csv":
        if "httpgetmt" in name:
            return "fcc_httpgetmt_csv"
        if "video_sent" in name or "video_acked" in name:
            return "puffer_streaming_csv"
        return "csv"
    return "unknown"


def detect_columns(path: Path) -> tuple[tuple[str, ...], bool]:
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            first = handle.readline().strip()
            if not first:
                return (), False
            if path.suffix.lower() == ".csv":
                return tuple(next(csv.reader([first]))), True
            if len(first.split()) == 6:
                return (
                    "unix_time_s",
                    "monotonic_time_ms",
                    "latitude_deg",
                    "longitude_deg",
                    "bytes_received",
                    "elapsed_ms",
                ), True
            if len(first.split()) == 2:
                return ("timestamp_or_time", "throughput"), True
    except (OSError, UnicodeDecodeError, csv.Error):
        return (), False
    return (), False


def iter_raw_files(raw_root: Path) -> Iterable[Path]:
    for path in raw_root.rglob("*"):
        if path.is_file():
            yield path


def build_raw_dataset_inventory(raw_root: str | Path, hash_mode: str = "full") -> dict[str, object]:
    root = Path(raw_root)
    if not root.is_dir():
        raise FileNotFoundError("raw dataset root not found: {0}".format(root))

    datasets: dict[str, dict[str, object]] = {}
    for path in sorted(iter_raw_files(root)):
        dataset_id = dataset_id_for_path(root, path)
        columns, parseable_header = detect_columns(path)
        raw_file = RawFileInventory(
            relative_path=str(path.relative_to(root)).replace("\\", "/"),
            bytes=path.stat().st_size,
            sha256=sha256_file(path, hash_mode=hash_mode),
            hash_mode=hash_mode,
            extension=path.suffix.lower(),
            parser_hint=parser_hint_for_file(path),
            columns_detected=columns,
            parseable_header=parseable_header,
        )
        dataset = datasets.setdefault(
            dataset_id,
            {
                "dataset_id": dataset_id,
                "file_count": 0,
                "total_bytes": 0,
                "files": [],
                "parser_hints": {},
            },
        )
        dataset["file_count"] = int(dataset["file_count"]) + 1
        dataset["total_bytes"] = int(dataset["total_bytes"]) + raw_file.bytes
        dataset["files"].append(asdict(raw_file))
        hints = dataset["parser_hints"]
        hints[raw_file.parser_hint] = int(hints.get(raw_file.parser_hint, 0)) + 1

    return {
        "schema_id": "phase3_raw_dataset_inventory_v1",
        "raw_root": str(root),
        "hash_mode": hash_mode,
        "dataset_count": len(datasets),
        "file_count": sum(int(dataset["file_count"]) for dataset in datasets.values()),
        "total_bytes": sum(int(dataset["total_bytes"]) for dataset in datasets.values()),
        "datasets": sorted(datasets.values(), key=lambda item: str(item["dataset_id"])),
    }


def write_raw_dataset_inventory(inventory: dict[str, object], output_path: str | Path) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(inventory, indent=2, sort_keys=True), encoding="utf-8")
    return path

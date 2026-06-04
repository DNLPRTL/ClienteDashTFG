from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from core.trace_replay.converters.common import sha256_file, stable_id, write_normalized_csv


@dataclass(frozen=True)
class ConversionResult:
    trace_id: str
    dataset_id: str
    converter_id: str
    normalized_trace_path: str
    metadata_path: str
    source_path: str
    source_sha256: str
    group_id: str
    leakage_group: str
    semantics: str
    row_count: int
    duration_s: float
    throughput_min_kbps: float
    throughput_mean_kbps: float
    throughput_max_kbps: float
    content_fingerprint_sha256: str
    parse_warnings: tuple[str, ...] = ()

    def as_manifest_entry(self) -> dict[str, object]:
        return {
            "trace_id": self.trace_id,
            "dataset_id": self.dataset_id,
            "converter_id": self.converter_id,
            "normalized_trace_path": self.normalized_trace_path,
            "metadata_path": self.metadata_path,
            "source_path": self.source_path,
            "source_sha256": self.source_sha256,
            "group_id": self.group_id,
            "leakage_group": self.leakage_group,
            "semantics": self.semantics,
            "row_count": self.row_count,
            "duration_s": self.duration_s,
            "throughput_min_kbps": self.throughput_min_kbps,
            "throughput_mean_kbps": self.throughput_mean_kbps,
            "throughput_max_kbps": self.throughput_max_kbps,
            "content_fingerprint_sha256": self.content_fingerprint_sha256,
            "parse_warnings": list(self.parse_warnings),
        }


class BaseTraceConverter:
    dataset_id = "base"
    converter_id = "phase3_base_v1"
    semantics = "available_bandwidth"

    def __init__(self, raw_root: str | Path) -> None:
        self.raw_root = Path(raw_root)

    def iter_source_files(self) -> Iterable[Path]:
        raise NotImplementedError

    def rows_for_source(self, path: Path) -> tuple[list[dict[str, float]], str, str, tuple[str, ...]]:
        raise NotImplementedError

    def convert(
        self,
        normalized_root: str | Path,
        metadata_root: str | Path,
        max_traces: int | None = None,
    ) -> list[ConversionResult]:
        results: list[ConversionResult] = []
        normalized_base = Path(normalized_root) / "schema_v1" / self.dataset_id
        metadata_base = Path(metadata_root) / "traces" / self.dataset_id
        for source_path in self.iter_source_files():
            rows, group_id, leakage_group, warnings = self.rows_for_source(source_path)
            if not rows:
                continue
            rows = sorted(rows, key=lambda row: float(row["timestamp_s"]))
            trace_id = stable_id(self.dataset_id, group_id, source_path.name, prefix="trace")
            normalized_path = normalized_base / "{0}.csv".format(trace_id)
            stats = write_normalized_csv(rows, normalized_path)
            metadata_path = metadata_base / "{0}.json".format(trace_id)
            metadata_path.parent.mkdir(parents=True, exist_ok=True)
            result = ConversionResult(
                trace_id=trace_id,
                dataset_id=self.dataset_id,
                converter_id=self.converter_id,
                normalized_trace_path=str(normalized_path),
                metadata_path=str(metadata_path),
                source_path=str(source_path),
                source_sha256=sha256_file(source_path),
                group_id=group_id,
                leakage_group=leakage_group,
                semantics=self.semantics,
                row_count=int(stats["row_count"]),
                duration_s=float(stats["duration_s"]),
                throughput_min_kbps=float(stats["throughput_min_kbps"]),
                throughput_mean_kbps=float(stats["throughput_mean_kbps"]),
                throughput_max_kbps=float(stats["throughput_max_kbps"]),
                content_fingerprint_sha256=str(stats["content_fingerprint_sha256"]),
                parse_warnings=warnings,
            )
            metadata_path.write_text(json.dumps(result.as_manifest_entry(), indent=2, sort_keys=True), encoding="utf-8")
            results.append(result)
            if max_traces is not None and len(results) >= max_traces:
                break
        return results

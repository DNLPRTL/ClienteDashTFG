from __future__ import annotations

import csv
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from core.trace_replay.converters.base import BaseTraceConverter, ConversionResult
from core.trace_replay.converters.common import parse_float, sha256_file, stable_id, write_normalized_csv


class FccMbaConverter(BaseTraceConverter):
    dataset_id = "fcc_measuring_broadband_america"
    converter_id = "phase3_fcc_httpgetmt_v1"
    semantics = "active_fixed_broadband_download_test"

    def iter_source_files(self):
        root = self.raw_root / "FCC Measuring Broadband America"
        if not root.is_dir():
            return
        for path in sorted(root.rglob("curr_httpgetmt.csv")):
            yield path

    def rows_for_source(self, path):
        raise NotImplementedError("FCC groups one source file into traces by unit_id")

    def convert(self, normalized_root, metadata_root, max_traces=None):
        results: list[ConversionResult] = []
        for source_path in self.iter_source_files():
            grouped: dict[str, list[tuple[datetime, float, float]]] = defaultdict(list)
            with source_path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
                reader = csv.DictReader(handle)
                for row in reader:
                    unit_id = str(row.get("unit_id", "")).strip()
                    dtime = str(row.get("dtime", "")).strip()
                    bytes_sec = parse_float(row.get("bytes_sec"))
                    fetch_time = parse_float(row.get("fetch_time"))
                    if not unit_id or bytes_sec is None or fetch_time is None:
                        continue
                    try:
                        timestamp = datetime.strptime(dtime, "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        continue
                    grouped[unit_id].append((timestamp, bytes_sec * 8.0 / 1000.0, max(fetch_time / 1_000_000.0, 0.001)))
            source_hash = sha256_file(source_path)
            for unit_id in sorted(grouped):
                samples = sorted(grouped[unit_id], key=lambda item: item[0])
                if not samples:
                    continue
                first = samples[0][0]
                rows = [
                    {
                        "timestamp_s": max(0.0, (timestamp - first).total_seconds()),
                        "duration_s": duration,
                        "throughput_kbps": throughput,
                    }
                    for timestamp, throughput, duration in samples
                ]
                result = self._write_group(source_path, source_hash, normalized_root, metadata_root, unit_id, rows)
                results.append(result)
                if max_traces is not None and len(results) >= max_traces:
                    return results
        return results

    def _write_group(self, source_path, source_hash, normalized_root, metadata_root, unit_id, rows):
        group_id = "unit_{0}".format(unit_id)
        trace_id = stable_id(self.dataset_id, group_id, source_path.name, prefix="trace")
        normalized_path = Path(normalized_root) / "schema_v1" / self.dataset_id / "{0}.csv".format(trace_id)
        stats = write_normalized_csv(rows, normalized_path)
        metadata_path = Path(metadata_root) / "traces" / self.dataset_id / "{0}.json".format(trace_id)
        result = ConversionResult(
            trace_id=trace_id,
            dataset_id=self.dataset_id,
            converter_id=self.converter_id,
            normalized_trace_path=str(normalized_path),
            metadata_path=str(metadata_path),
            source_path=str(source_path),
            source_sha256=source_hash,
            group_id=group_id,
            leakage_group="{0}:{1}".format(self.dataset_id, group_id),
            semantics=self.semantics,
            row_count=int(stats["row_count"]),
            duration_s=float(stats["duration_s"]),
            throughput_min_kbps=float(stats["throughput_min_kbps"]),
            throughput_mean_kbps=float(stats["throughput_mean_kbps"]),
            throughput_max_kbps=float(stats["throughput_max_kbps"]),
            content_fingerprint_sha256=str(stats["content_fingerprint_sha256"]),
        )
        metadata_path.parent.mkdir(parents=True, exist_ok=True)
        metadata_path.write_text(json.dumps(result.as_manifest_entry(), indent=2, sort_keys=True), encoding="utf-8")
        return result

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

from core.trace_replay.converters.base import BaseTraceConverter, ConversionResult
from core.trace_replay.converters.common import (
    find_first_file,
    parse_float,
    sequential_rows,
    sha256_file,
    stable_id,
    write_normalized_csv,
)


class Lumos5GConverter(BaseTraceConverter):
    dataset_id = "lumos5g"
    converter_id = "phase3_lumos5g_v1"

    def iter_source_files(self):
        path = find_first_file(self.raw_root, ("lumos5g-v1.0", "lumos5g-v1.0.csv"), suffix=".csv")
        if path is not None:
            yield path

    def rows_for_source(self, path):
        raise NotImplementedError("Lumos5G groups one source file into one trace per run_num")

    def convert(self, normalized_root, metadata_root, max_traces=None):
        source_files = list(self.iter_source_files())
        if not source_files:
            return []
        path = source_files[0]
        by_run: dict[str, list[float]] = defaultdict(list)
        with path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                run_num = str(row.get("run_num", "")).strip()
                throughput = parse_float(row.get("Throughput"))
                if not run_num or throughput is None:
                    continue
                by_run[run_num].append(throughput * 1000.0)

        results: list[ConversionResult] = []
        source_hash = sha256_file(path)
        for run_num in sorted(by_run, key=lambda value: int(value) if value.isdigit() else value):
            rows = sequential_rows(by_run[run_num])
            if not rows:
                continue
            group_id = "run_{0}".format(run_num)
            trace_id = stable_id(self.dataset_id, group_id, path.name, prefix="trace")
            normalized_path = self._normalized_path(normalized_root, trace_id)
            stats = write_normalized_csv(rows, normalized_path)
            metadata_path = self._metadata_path(metadata_root, trace_id)
            result = ConversionResult(
                trace_id=trace_id,
                dataset_id=self.dataset_id,
                converter_id=self.converter_id,
                normalized_trace_path=str(normalized_path),
                metadata_path=str(metadata_path),
                source_path=str(path),
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
            self._write_metadata(result)
            results.append(result)
            if max_traces is not None and len(results) >= max_traces:
                break
        return results

    def _normalized_path(self, normalized_root, trace_id):
        return Path(normalized_root) / "schema_v1" / self.dataset_id / "{0}.csv".format(trace_id)

    def _metadata_path(self, metadata_root, trace_id):
        return Path(metadata_root) / "traces" / self.dataset_id / "{0}.json".format(trace_id)

    def _write_metadata(self, result):
        path = Path(result.metadata_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result.as_manifest_entry(), indent=2, sort_keys=True), encoding="utf-8")

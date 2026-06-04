from __future__ import annotations

import csv
from datetime import datetime

from core.trace_replay.converters.base import BaseTraceConverter
from core.trace_replay.converters.common import parse_float, rows_from_timestamps_and_throughput


class RomaActiveThroughputConverter(BaseTraceConverter):
    dataset_id = "roma_4g_nbiot_5g_nsa"
    converter_id = "phase3_roma_active_speedtest_v1"
    semantics = "active_mobile_speedtest"
    gap_cut_s = 5.0

    def iter_source_files(self):
        path = (
            self.raw_root
            / "Large Scale Dataset of 4G NB-IoT and 5G Non-Standalone Network Measurements"
            / "Throughput Tests - Speedtest - Active Measurements.csv"
        )
        if path.is_file():
            yield path

    def rows_for_source(self, path):
        raise NotImplementedError("Roma is split into traces by scenario/operator/campaign/gaps")

    def convert(self, normalized_root, metadata_root, max_traces=None):
        from core.trace_replay.converters.base import ConversionResult
        from core.trace_replay.converters.common import sha256_file, stable_id, write_normalized_csv
        import json
        from pathlib import Path

        results: list[ConversionResult] = []
        source_files = list(self.iter_source_files())
        if not source_files:
            return []
        source_path = source_files[0]
        source_hash = sha256_file(source_path)
        current_key = None
        timestamps: list[float] = []
        throughput: list[float] = []
        first_timestamp: datetime | None = None
        previous_timestamp: datetime | None = None
        segment_index = 0

        def flush(key, index):
            if key is None or not timestamps:
                return None
            rows = rows_from_timestamps_and_throughput(timestamps, throughput, fallback_duration_s=1.0)
            group_id = "{0}:segment_{1:04d}".format(key, index)
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
                leakage_group="{0}:{1}".format(self.dataset_id, key),
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

        with source_path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                value = parse_float(row.get("Current Netw. DL"))
                if value is None:
                    continue
                timestamp_text = "{0} {1}".format(row.get("Date", ""), row.get("Time", "")).strip()
                try:
                    timestamp = datetime.strptime(timestamp_text, "%d.%m.%Y %H:%M:%S.%f")
                except ValueError:
                    continue
                key = "{0}:{1}:{2}".format(row.get("Campaign", "unknown"), row.get("Operator", "unknown"), row.get("Scenario", "unknown"))
                gap = (timestamp - previous_timestamp).total_seconds() if previous_timestamp and key == current_key else 0.0
                if current_key is not None and (key != current_key or gap > self.gap_cut_s):
                    result = flush(current_key, segment_index)
                    if result is not None:
                        results.append(result)
                        if max_traces is not None and len(results) >= max_traces:
                            return results
                    timestamps = []
                    throughput = []
                    first_timestamp = None
                    segment_index += 1
                current_key = key
                if first_timestamp is None:
                    first_timestamp = timestamp
                timestamps.append((timestamp - first_timestamp).total_seconds())
                throughput.append(value)
                previous_timestamp = timestamp
        result = flush(current_key, segment_index)
        if result is not None and (max_traces is None or len(results) < max_traces):
            results.append(result)
        return results

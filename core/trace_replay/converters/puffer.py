from __future__ import annotations

import csv
import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from core.trace_replay.converters.base import BaseTraceConverter, ConversionResult
from core.trace_replay.converters.common import (
    parse_float,
    rows_from_timestamps_and_throughput,
    sha256_file,
    stable_id,
    write_normalized_csv,
)


@dataclass(frozen=True)
class PufferSamplingPolicy:
    max_sessions: int = 100
    min_samples_per_session: int = 30
    max_acked_rows: int = 1_000_000
    max_sent_rows: int = 2_000_000

    def as_dict(self) -> dict[str, int | str]:
        return {
            "mode": "bounded_video_sent_acked_join",
            "max_sessions": self.max_sessions,
            "min_samples_per_session": self.min_samples_per_session,
            "max_acked_rows": self.max_acked_rows,
            "max_sent_rows": self.max_sent_rows,
        }


class PufferConverter(BaseTraceConverter):
    dataset_id = "puffer_stanford"
    converter_id = "phase3_puffer_video_sent_acked_bounded_v1"
    semantics = "real_streaming_delivery_rate"

    def __init__(
        self,
        raw_root: str | Path,
        max_sessions: int = 100,
        min_samples_per_session: int = 30,
        max_acked_rows: int = 1_000_000,
        max_sent_rows: int = 2_000_000,
    ) -> None:
        super().__init__(raw_root)
        self.sampling_policy = PufferSamplingPolicy(
            max_sessions=_positive_int(max_sessions, "max_sessions"),
            min_samples_per_session=_positive_int(min_samples_per_session, "min_samples_per_session"),
            max_acked_rows=_positive_int(max_acked_rows, "max_acked_rows"),
            max_sent_rows=_positive_int(max_sent_rows, "max_sent_rows"),
        )

    def iter_source_files(self):
        root = self.raw_root / "Puffer"
        if not root.is_dir():
            return
        sent_files = sorted(root.glob("video_sent_*.csv"))
        ack_files = sorted(root.glob("video_acked_*.csv"))
        for sent_path in sent_files:
            matching = None
            suffix = sent_path.name.replace("video_sent_", "")
            for ack_path in ack_files:
                if ack_path.name.endswith(suffix):
                    matching = ack_path
                    break
            if matching is not None:
                yield sent_path, matching

    def rows_for_source(self, path):
        raise NotImplementedError("Puffer requires a video_sent/video_acked bounded join")

    def convert(self, normalized_root, metadata_root, max_traces=None):
        results: list[ConversionResult] = []
        for sent_path, ack_path in self.iter_source_files():
            selected_video_ts, selection_warnings = self._select_sessions_from_acked(ack_path)
            if not selected_video_ts:
                continue
            samples_by_session, sample_warnings = self._collect_samples_from_sent(sent_path, selected_video_ts)
            source_hash = "{0}+{1}".format(sha256_file(sent_path), sha256_file(ack_path))
            for session_id in sorted(samples_by_session, key=lambda value: stable_id(value, prefix="puffer")):
                samples = sorted(samples_by_session[session_id], key=lambda item: item[0])
                if len(samples) < self.sampling_policy.min_samples_per_session:
                    continue
                result = self._write_session(
                    samples=samples,
                    session_id=session_id,
                    sent_path=sent_path,
                    ack_path=ack_path,
                    source_hash=source_hash,
                    normalized_root=normalized_root,
                    metadata_root=metadata_root,
                    warnings=selection_warnings + sample_warnings,
                )
                results.append(result)
                if max_traces is not None and len(results) >= max_traces:
                    return results
                if len(results) >= self.sampling_policy.max_sessions:
                    return results
        return results

    def _select_sessions_from_acked(self, ack_path: Path) -> tuple[dict[str, set[str]], tuple[str, ...]]:
        candidate_keys: dict[str, list[str]] = defaultdict(list)
        selected: dict[str, set[str]] = {}
        rows_read = 0
        with ack_path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                rows_read += 1
                if rows_read > self.sampling_policy.max_acked_rows:
                    break
                session_id = str(row.get("session_id", "")).strip()
                video_ts = str(row.get("video_ts", "")).strip()
                if not session_id or not video_ts:
                    continue
                if session_id in selected:
                    selected[session_id].add(video_ts)
                    continue
                candidate_keys[session_id].append(video_ts)
                if len(candidate_keys[session_id]) >= self.sampling_policy.min_samples_per_session:
                    selected[session_id] = set(candidate_keys[session_id])
                    if len(selected) >= self.sampling_policy.max_sessions:
                        break

        warnings: list[str] = []
        if len(selected) < self.sampling_policy.max_sessions:
            warnings.append(
                "puffer selected {0}/{1} sessions before max_acked_rows={2}".format(
                    len(selected),
                    self.sampling_policy.max_sessions,
                    self.sampling_policy.max_acked_rows,
                )
            )
        return selected, tuple(warnings)

    def _collect_samples_from_sent(
        self,
        sent_path: Path,
        selected_video_ts: dict[str, set[str]],
    ) -> tuple[dict[str, list[tuple[int, float]]], tuple[str, ...]]:
        pending = {session_id: set(video_ts_values) for session_id, video_ts_values in selected_video_ts.items()}
        samples_by_session: dict[str, list[tuple[int, float]]] = defaultdict(list)
        rows_read = 0
        with sent_path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                rows_read += 1
                if rows_read > self.sampling_policy.max_sent_rows:
                    break
                session_id = str(row.get("session_id", "")).strip()
                video_ts = str(row.get("video_ts", "")).strip()
                if session_id not in pending or video_ts not in pending[session_id]:
                    continue
                delivery_rate = parse_float(row.get("delivery_rate"))
                time_ns = parse_float(row.get("time (ns GMT)"))
                if delivery_rate is None or time_ns is None:
                    continue
                samples_by_session[session_id].append((int(time_ns), delivery_rate * 8.0 / 1000.0))
                pending[session_id].remove(video_ts)
                if all(not values for values in pending.values()):
                    break

        warnings: list[str] = []
        incomplete = [session_id for session_id, values in pending.items() if values]
        if incomplete:
            warnings.append(
                "puffer sent scan left {0} selected sessions incomplete before max_sent_rows={1}".format(
                    len(incomplete),
                    self.sampling_policy.max_sent_rows,
                )
            )
        return samples_by_session, tuple(warnings)

    def _write_session(
        self,
        samples: list[tuple[int, float]],
        session_id: str,
        sent_path: Path,
        ack_path: Path,
        source_hash: str,
        normalized_root,
        metadata_root,
        warnings: tuple[str, ...],
    ) -> ConversionResult:
        first_time = samples[0][0]
        timestamps_s = [(time_ns - first_time) / 1_000_000_000.0 for time_ns, _ in samples]
        throughput_kbps = [throughput for _, throughput in samples]
        rows = rows_from_timestamps_and_throughput(timestamps_s, throughput_kbps, fallback_duration_s=2.0)
        group_id = "session_{0}".format(stable_id(session_id, prefix="puffer")[-12:])
        trace_id = stable_id(self.dataset_id, group_id, sent_path.name, prefix="trace")
        normalized_path = Path(normalized_root) / "schema_v1" / self.dataset_id / "{0}.csv".format(trace_id)
        stats = write_normalized_csv(rows, normalized_path)
        metadata_path = Path(metadata_root) / "traces" / self.dataset_id / "{0}.json".format(trace_id)
        result = ConversionResult(
            trace_id=trace_id,
            dataset_id=self.dataset_id,
            converter_id=self.converter_id,
            normalized_trace_path=str(normalized_path),
            metadata_path=str(metadata_path),
            source_path="{0};{1}".format(sent_path, ack_path),
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
            parse_warnings=warnings,
        )
        metadata_path.parent.mkdir(parents=True, exist_ok=True)
        metadata_path.write_text(json.dumps(result.as_manifest_entry(), indent=2, sort_keys=True), encoding="utf-8")
        return result


def _positive_int(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("{0} must be a positive integer".format(name))
    return value

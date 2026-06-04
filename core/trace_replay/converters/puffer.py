from __future__ import annotations

import csv
import json
import sqlite3
import tempfile
from pathlib import Path

from core.trace_replay.converters.base import BaseTraceConverter, ConversionResult
from core.trace_replay.converters.common import parse_float, rows_from_timestamps_and_throughput, sha256_file, stable_id, write_normalized_csv


class PufferConverter(BaseTraceConverter):
    dataset_id = "puffer_stanford"
    converter_id = "phase3_puffer_video_sent_acked_v1"
    semantics = "real_streaming_delivery_rate"

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
        raise NotImplementedError("Puffer requires a video_sent/video_acked join")

    def convert(self, normalized_root, metadata_root, max_traces=None):
        results: list[ConversionResult] = []
        for sent_path, ack_path in self.iter_source_files():
            with tempfile.TemporaryDirectory(prefix="phase3_puffer_") as tmp:
                db_path = Path(tmp) / "puffer_join.sqlite"
                self._build_join_db(db_path, sent_path, ack_path)
                results.extend(self._write_sessions(db_path, sent_path, ack_path, normalized_root, metadata_root, max_traces, len(results)))
                if max_traces is not None and len(results) >= max_traces:
                    return results[:max_traces]
        return results

    def _build_join_db(self, db_path: Path, sent_path: Path, ack_path: Path) -> None:
        connection = sqlite3.connect(str(db_path))
        try:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE acked(session_id TEXT NOT NULL, video_ts TEXT NOT NULL, PRIMARY KEY(session_id, video_ts))")
            cursor.execute("CREATE TABLE samples(session_id TEXT NOT NULL, time_ns INTEGER NOT NULL, throughput_kbps REAL NOT NULL)")
            with ack_path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
                reader = csv.DictReader(handle)
                batch = []
                for row in reader:
                    session_id = str(row.get("session_id", "")).strip()
                    video_ts = str(row.get("video_ts", "")).strip()
                    if session_id and video_ts:
                        batch.append((session_id, video_ts))
                    if len(batch) >= 10000:
                        cursor.executemany("INSERT OR IGNORE INTO acked VALUES (?, ?)", batch)
                        batch = []
                if batch:
                    cursor.executemany("INSERT OR IGNORE INTO acked VALUES (?, ?)", batch)
            connection.commit()
            with sent_path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
                reader = csv.DictReader(handle)
                batch = []
                for row in reader:
                    session_id = str(row.get("session_id", "")).strip()
                    video_ts = str(row.get("video_ts", "")).strip()
                    delivery_rate = parse_float(row.get("delivery_rate"))
                    time_ns = parse_float(row.get("time (ns GMT)"))
                    if not session_id or not video_ts or delivery_rate is None or time_ns is None:
                        continue
                    matched = cursor.execute(
                        "SELECT 1 FROM acked WHERE session_id=? AND video_ts=? LIMIT 1",
                        (session_id, video_ts),
                    ).fetchone()
                    if matched:
                        batch.append((session_id, int(time_ns), delivery_rate * 8.0 / 1000.0))
                    if len(batch) >= 10000:
                        cursor.executemany("INSERT INTO samples VALUES (?, ?, ?)", batch)
                        batch = []
                if batch:
                    cursor.executemany("INSERT INTO samples VALUES (?, ?, ?)", batch)
            cursor.execute("CREATE INDEX samples_session_idx ON samples(session_id, time_ns)")
            connection.commit()
        finally:
            connection.close()

    def _write_sessions(self, db_path, sent_path, ack_path, normalized_root, metadata_root, max_traces, already_written):
        results: list[ConversionResult] = []
        source_hash = "{0}+{1}".format(sha256_file(sent_path), sha256_file(ack_path))
        connection = sqlite3.connect(str(db_path))
        try:
            cursor = connection.cursor()
            session_ids = [row[0] for row in cursor.execute("SELECT DISTINCT session_id FROM samples ORDER BY session_id")]
            for session_id in session_ids:
                rows = list(cursor.execute("SELECT time_ns, throughput_kbps FROM samples WHERE session_id=? ORDER BY time_ns", (session_id,)))
                if not rows:
                    continue
                first_time = rows[0][0]
                timestamps_s = [(time_ns - first_time) / 1_000_000_000.0 for time_ns, _ in rows]
                throughput_kbps = [throughput for _, throughput in rows]
                normalized_rows = rows_from_timestamps_and_throughput(timestamps_s, throughput_kbps, fallback_duration_s=2.0)
                group_id = "session_{0}".format(stable_id(session_id, prefix="puffer")[-12:])
                trace_id = stable_id(self.dataset_id, group_id, sent_path.name, prefix="trace")
                normalized_path = Path(normalized_root) / "schema_v1" / self.dataset_id / "{0}.csv".format(trace_id)
                stats = write_normalized_csv(normalized_rows, normalized_path)
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
                )
                metadata_path.parent.mkdir(parents=True, exist_ok=True)
                metadata_path.write_text(json.dumps(result.as_manifest_entry(), indent=2, sort_keys=True), encoding="utf-8")
                results.append(result)
                if max_traces is not None and already_written + len(results) >= max_traces:
                    break
        finally:
            connection.close()
        return results

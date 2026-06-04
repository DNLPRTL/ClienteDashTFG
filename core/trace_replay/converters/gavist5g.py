from __future__ import annotations

import csv
from collections import defaultdict
from datetime import datetime

from core.trace_replay.converters.base import BaseTraceConverter
from core.trace_replay.converters.common import parse_float, rows_from_timestamps_and_throughput


class Gavist5GConverter(BaseTraceConverter):
    dataset_id = "gavist5g"
    converter_id = "phase3_gavist5g_aggregate_v1"
    semantics = "observed_application_traffic"

    def iter_source_files(self):
        root = self.raw_root / "GAViST5G (Gaming and Video Streaming Traffic for 5G)"
        if not root.is_dir():
            return
        for path in sorted(root.rglob("*.csv")):
            yield path

    def rows_for_source(self, path):
        bytes_by_second: dict[datetime, float] = defaultdict(float)
        warnings: list[str] = []
        with path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames or "Time" not in reader.fieldnames or "Length" not in reader.fieldnames:
                return [], "", "", ("missing Time/Length columns",)
            for line_number, row in enumerate(reader, start=2):
                try:
                    timestamp = datetime.strptime(str(row.get("Time", "")).strip(), "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    warnings.append("line {0}: invalid Time".format(line_number))
                    continue
                length = parse_float(row.get("Length"))
                if length is None or length < 0:
                    warnings.append("line {0}: invalid Length".format(line_number))
                    continue
                bytes_by_second[timestamp] += length
        timestamps = sorted(bytes_by_second)
        if not timestamps:
            return [], "", "", tuple(warnings[:20])
        first = timestamps[0]
        relative_timestamps = [(timestamp - first).total_seconds() for timestamp in timestamps]
        throughput_kbps = [bytes_by_second[timestamp] * 8.0 / 1000.0 for timestamp in timestamps]
        relative_parent = path.parent.relative_to(self.raw_root).as_posix()
        group_id = relative_parent
        return rows_from_timestamps_and_throughput(relative_timestamps, throughput_kbps, fallback_duration_s=1.0), group_id, "{0}:{1}".format(self.dataset_id, group_id), tuple(warnings[:20])

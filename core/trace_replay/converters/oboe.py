from __future__ import annotations

from core.trace_replay.converters.base import BaseTraceConverter
from core.trace_replay.converters.common import rows_from_timestamps_and_throughput


class OboeConverter(BaseTraceConverter):
    dataset_id = "oboe"
    converter_id = "phase3_oboe_v1"

    def iter_source_files(self):
        root = self.raw_root / "oboe" / "traces"
        if not root.is_dir():
            return
        for path in sorted(root.glob("*.txt")):
            yield path

    def rows_for_source(self, path):
        timestamps_s: list[float] = []
        throughput_kbps: list[float] = []
        warnings: list[str] = []
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            for line_number, line in enumerate(handle, start=1):
                parts = line.split()
                if len(parts) != 2:
                    warnings.append("line {0}: expected 2 fields".format(line_number))
                    continue
                try:
                    timestamps_s.append(float(parts[0]) / 1000.0)
                    throughput_kbps.append(float(parts[1]))
                except ValueError:
                    warnings.append("line {0}: nonnumeric fields".format(line_number))
        group_id = path.stem
        return rows_from_timestamps_and_throughput(timestamps_s, throughput_kbps), group_id, "{0}:{1}".format(self.dataset_id, group_id), tuple(warnings[:20])

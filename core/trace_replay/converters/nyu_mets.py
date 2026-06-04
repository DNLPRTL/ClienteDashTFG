from __future__ import annotations

import csv

from core.trace_replay.converters.base import BaseTraceConverter
from core.trace_replay.converters.common import iter_files_under_hint, parse_float, sequential_rows


class NyuMetsConverter(BaseTraceConverter):
    dataset_id = "nyu_mets"
    converter_id = "phase3_nyu_mets_v1"

    def iter_source_files(self):
        for path in iter_files_under_hint(self.raw_root, ("nyu-mets",), ".csv"):
            yield path

    def rows_for_source(self, path):
        throughput_kbps: list[float] = []
        warnings: list[str] = []
        with path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
            for line_number, row in enumerate(csv.reader(handle), start=1):
                if not row:
                    continue
                value = parse_float(row[0])
                if value is None:
                    warnings.append("line {0}: invalid Mbps value".format(line_number))
                    continue
                throughput_kbps.append(value * 1000.0)
        relative_parent = path.parent.relative_to(self.raw_root).as_posix()
        group_id = relative_parent
        return sequential_rows(throughput_kbps), group_id, "{0}:{1}".format(self.dataset_id, group_id), tuple(warnings[:20])

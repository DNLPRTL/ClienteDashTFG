from __future__ import annotations

from pathlib import Path

import csv

from core.trace_replay.converters.base import BaseTraceConverter
from core.trace_replay.converters.common import iter_files_under_hint, parse_float, sequential_rows


class _UccDlBitrateConverter(BaseTraceConverter):
    path_hints: tuple[str, ...] = ()

    def iter_source_files(self):
        for path in iter_files_under_hint(self.raw_root, self.path_hints, ".csv"):
            yield path

    def rows_for_source(self, path: Path):
        throughput_kbps: list[float] = []
        warnings: list[str] = []
        with path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames or "DL_bitrate" not in reader.fieldnames:
                warnings.append("missing DL_bitrate column")
                return [], "", "", tuple(warnings)
            for index, row in enumerate(reader, start=2):
                value = parse_float(row.get("DL_bitrate"))
                if value is None:
                    warnings.append("line {0}: invalid DL_bitrate".format(index))
                    continue
                throughput_kbps.append(value)
        relative_parent = path.parent.relative_to(self.raw_root).as_posix()
        group_id = relative_parent
        return sequential_rows(throughput_kbps), group_id, "{0}:{1}".format(self.dataset_id, group_id), tuple(warnings[:20])


class Ucc4GBeyondThroughputConverter(_UccDlBitrateConverter):
    dataset_id = "ucc_4g_lte_beyond_throughput"
    converter_id = "phase3_ucc_4g_lte_v1"
    path_hints = ("beyond_throughput_4g_lte",)


class Ucc5GBeyondThroughputConverter(_UccDlBitrateConverter):
    dataset_id = "ucc_5g_beyond_throughput"
    converter_id = "phase3_ucc_5g_v1"
    path_hints = ("ucc 5g beyond throughput", "5g-production-dataset")

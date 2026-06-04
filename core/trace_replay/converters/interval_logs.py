from __future__ import annotations

from pathlib import Path

from core.trace_replay.converters.base import BaseTraceConverter


class _IntervalLogConverter(BaseTraceConverter):
    folder_name = ""

    def iter_source_files(self):
        root = self.raw_root / self.folder_name
        if not root.is_dir():
            return
        for path in sorted(root.rglob("*.log")):
            yield path

    def group_for_source(self, path: Path) -> str:
        raise NotImplementedError

    def rows_for_source(self, path: Path):
        rows: list[dict[str, float]] = []
        warnings: list[str] = []
        first_monotonic_ms: float | None = None
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            for line_number, line in enumerate(handle, start=1):
                parts = line.split()
                if not parts:
                    continue
                if len(parts) != 6:
                    warnings.append("line {0}: expected 6 whitespace fields".format(line_number))
                    continue
                try:
                    monotonic_ms = float(parts[1])
                    bytes_received = float(parts[4])
                    elapsed_ms = float(parts[5])
                except ValueError:
                    warnings.append("line {0}: nonnumeric interval fields".format(line_number))
                    continue
                if elapsed_ms <= 0 or bytes_received < 0:
                    warnings.append("line {0}: invalid bytes/elapsed values".format(line_number))
                    continue
                if first_monotonic_ms is None:
                    first_monotonic_ms = monotonic_ms
                rows.append(
                    {
                        "timestamp_s": max(0.0, (monotonic_ms - first_monotonic_ms) / 1000.0),
                        "duration_s": elapsed_ms / 1000.0,
                        "throughput_kbps": (bytes_received * 8.0) / elapsed_ms,
                    }
                )
        group_id = self.group_for_source(path)
        leakage_group = "{0}:{1}".format(self.dataset_id, group_id)
        return rows, group_id, leakage_group, tuple(warnings[:20])


class NorwayHsdpaConverter(_IntervalLogConverter):
    dataset_id = "norway_hsdpa_umass"
    converter_id = "phase3_norway_hsdpa_v1"
    folder_name = "Norway HSDPA (UMass trace archive)"

    def group_for_source(self, path: Path) -> str:
        return path.parent.name


class Ghent4GLteConverter(_IntervalLogConverter):
    dataset_id = "ghent_4g_lte"
    converter_id = "phase3_ghent_4g_lte_v1"
    folder_name = "BelgiumGhent 4G UGentIDLab LTE traces"

    def group_for_source(self, path: Path) -> str:
        parts = path.stem.split("_")
        return parts[1] if len(parts) >= 3 else path.stem

from __future__ import annotations

import csv
import json
import math
import statistics
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence


PHASE45_V3_POLICY_COLLAPSE_AUDIT_SCHEMA_ID = "phase45_v3_policy_collapse_audit_v1"


class PolicyCollapseAuditError(ValueError):
    """Raised when a Phase 6 policy-collapse audit cannot be computed."""


@dataclass(frozen=True)
class PolicyCollapseAuditConfig:
    controller_alias: str = "propio_spbc_v2_anchor"
    baseline_alias: str = "base_robust_mpc"
    min_ladder_bitrate_kbps: float = 300.0
    max_ladder_bitrate_kbps: float = 4300.0
    startup_chunks: int = 3
    high_capacity_throughput_multiple: float = 2.0
    high_capacity_min_buffer_s: float = 8.0
    high_capacity_min_chunks_remaining: int = 3
    max_high_capacity_action0_rate: float = 0.05
    max_consecutive_action0_after_startup: int = 2
    reach_bitrate_kbps: float = 2850.0
    max_time_to_reach_segments: int = 3
    require_no_fallback: bool = True


def audit_phase6_policy_collapse(
    phase6_results_dir: object,
    config: PolicyCollapseAuditConfig | None = None,
) -> Mapping[str, object]:
    cfg = config or PolicyCollapseAuditConfig()
    root = Path(phase6_results_dir).expanduser()
    raw_path = _resolve_result_file(root, "raw_chunks.csv")
    summary_path = _resolve_result_file(root, "session_summary.csv", required=False)
    raw_rows = _read_csv(raw_path)
    if not raw_rows:
        raise PolicyCollapseAuditError("raw_chunks.csv has no rows")
    controller_rows = [row for row in raw_rows if str(row.get("controller_alias", "")) == cfg.controller_alias]
    baseline_rows = [row for row in raw_rows if str(row.get("controller_alias", "")) == cfg.baseline_alias]
    if not controller_rows:
        raise PolicyCollapseAuditError("controller alias not found in raw_chunks: {0}".format(cfg.controller_alias))

    rows_by_session = _rows_by_session(controller_rows)
    high_capacity_rows = [
        row
        for session_rows in rows_by_session.values()
        for row in session_rows
        if _is_high_capacity_safe_row(row, session_rows, cfg)
    ]
    after_startup_rows = [
        row for row in controller_rows if _int(row.get("chunk_index")) > int(cfg.startup_chunks)
    ]
    fallback_rows = [
        row
        for row in controller_rows
        if _int(row.get("fallback_used")) > 0
        or str(row.get("neural_fallback_reason", "")) not in ("", "success_neural")
    ]
    bitrates = [_float(row.get("bitrate_kbps")) for row in controller_rows if _float(row.get("bitrate_kbps")) > 0.0]
    baseline_bitrates = [_float(row.get("bitrate_kbps")) for row in baseline_rows if _float(row.get("bitrate_kbps")) > 0.0]

    time_to_reach = _time_to_reach_by_session(rows_by_session, cfg.reach_bitrate_kbps)
    high_capacity_sessions = {
        session_id: rows
        for session_id, rows in rows_by_session.items()
        if any(_is_high_capacity_safe_row(row, rows, cfg) for row in rows)
    }
    high_capacity_reach_failures = [
        session_id
        for session_id in high_capacity_sessions
        if time_to_reach.get(session_id) is None
        or int(time_to_reach[session_id]) > int(cfg.max_time_to_reach_segments)
    ]

    session_summary_rows = _read_csv(summary_path) if summary_path is not None and summary_path.is_file() else []
    paired = _paired_summary_deltas(session_summary_rows, cfg)
    action0_after_startup_count = sum(1 for row in after_startup_rows if _is_action0(row, cfg))
    high_capacity_action0_count = sum(1 for row in high_capacity_rows if _is_action0(row, cfg))
    metrics = {
        "controller_alias": cfg.controller_alias,
        "baseline_alias": cfg.baseline_alias,
        "row_count": len(controller_rows),
        "session_count": len(rows_by_session),
        "mean_selected_bitrate_kbps": _mean(bitrates),
        "median_selected_bitrate_kbps": _median(bitrates),
        "action_histogram": _histogram(_action_values(controller_rows, cfg)),
        "bitrate_histogram": _histogram([str(int(_float(row.get("bitrate_kbps")))) for row in controller_rows]),
        "action0_rate": _ratio(sum(1 for row in controller_rows if _is_action0(row, cfg)), len(controller_rows)),
        "action0_rate_after_startup": _ratio(action0_after_startup_count, len(after_startup_rows)),
        "high_capacity_safe_row_count": len(high_capacity_rows),
        "high_capacity_safe_action0_rate": _ratio(high_capacity_action0_count, len(high_capacity_rows)),
        "max_consecutive_action0_after_startup": _max_consecutive_action0(rows_by_session, cfg),
        "time_to_reach_{0}_by_session".format(int(cfg.reach_bitrate_kbps)): time_to_reach,
        "high_capacity_reach_failure_sessions": high_capacity_reach_failures,
        "fallback_row_count": len(fallback_rows),
        "fallback_reasons": _histogram([str(row.get("neural_fallback_reason", "")) for row in fallback_rows]),
        "mean_measured_throughput_kbps": _mean(
            [_float(row.get("measured_throughput_kbps")) for row in controller_rows]
        ),
        "throughput_to_bitrate_ratio": _safe_divide(
            _mean([_float(row.get("measured_throughput_kbps")) for row in controller_rows]),
            _mean(bitrates),
        ),
        "robust_mpc_bitrate_ratio": _safe_divide(_mean(bitrates), _mean(baseline_bitrates)),
        "qoe_delta_vs_baseline_mean": paired["qoe_delta_vs_baseline_mean"],
        "rebuffer_delta_vs_baseline_mean": paired["rebuffer_delta_vs_baseline_mean"],
        "paired_session_count": paired["paired_session_count"],
        "paired_deltas": paired["paired_deltas"],
    }

    gates = _evaluate_gates(metrics, cfg)
    return {
        "schema_id": PHASE45_V3_POLICY_COLLAPSE_AUDIT_SCHEMA_ID,
        "phase6_results_dir": str(root),
        "raw_chunks_csv": str(raw_path),
        "session_summary_csv": str(summary_path) if summary_path is not None else "",
        "status": "PASS" if not gates["failed"] else "FAIL",
        "collapse_detected": bool(gates["failed"]),
        "gate_failures": list(gates["failed"]),
        "gates": gates["gates"],
        "metrics": metrics,
        "thresholds": cfg.__dict__,
        "benchmark_performed": False,
        "ranking_performed": False,
        "outputs_are_benchmark_results": False,
        "no_final_ranking": True,
    }


def write_audit_json(report: Mapping[str, object], output_path: object) -> None:
    path = Path(output_path).expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")


def _evaluate_gates(metrics: Mapping[str, object], cfg: PolicyCollapseAuditConfig) -> Mapping[str, object]:
    gates: dict[str, Mapping[str, object]] = {}

    def add(name: str, passed: bool, observed: object, threshold: object) -> None:
        gates[name] = {"passed": bool(passed), "observed": observed, "threshold": threshold}

    high_count = int(metrics["high_capacity_safe_row_count"])
    high_rate = float(metrics["high_capacity_safe_action0_rate"])
    add(
        "high_capacity_safe_action0_rate",
        high_count > 0 and high_rate <= float(cfg.max_high_capacity_action0_rate),
        high_rate,
        "<= {0} with at least one high-capacity-safe row".format(cfg.max_high_capacity_action0_rate),
    )
    add(
        "max_consecutive_action0_after_startup",
        int(metrics["max_consecutive_action0_after_startup"]) <= int(cfg.max_consecutive_action0_after_startup),
        metrics["max_consecutive_action0_after_startup"],
        "<= {0}".format(cfg.max_consecutive_action0_after_startup),
    )
    reach_failures = list(metrics["high_capacity_reach_failure_sessions"])
    add(
        "time_to_reach_high_bitrate_in_high_capacity",
        len(reach_failures) == 0,
        reach_failures,
        "all high-capacity sessions reach {0} kbps within {1} chunks".format(
            cfg.reach_bitrate_kbps,
            cfg.max_time_to_reach_segments,
        ),
    )
    if cfg.require_no_fallback:
        add("no_fallback_rows", int(metrics["fallback_row_count"]) == 0, metrics["fallback_row_count"], "0")

    failed = [name for name, row in gates.items() if not row["passed"]]
    return {"failed": failed, "gates": gates}


def _resolve_result_file(root: Path, filename: str, required: bool = True) -> Path | None:
    candidates = [
        root / filename,
        root / "02_resultados" / filename,
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    if required:
        raise PolicyCollapseAuditError("missing {0} under {1}".format(filename, root))
    return None


def _read_csv(path: Path | None) -> list[dict[str, str]]:
    if path is None:
        return []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def _rows_by_session(rows: Sequence[Mapping[str, str]]) -> dict[str, list[Mapping[str, str]]]:
    grouped: dict[str, list[Mapping[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("session_id", ""))].append(row)
    return {
        key: sorted(value, key=lambda item: (_int(item.get("chunk_index")), _int(item.get("segment_index"))))
        for key, value in grouped.items()
    }


def _is_high_capacity_safe_row(
    row: Mapping[str, str],
    session_rows: Sequence[Mapping[str, str]],
    cfg: PolicyCollapseAuditConfig,
) -> bool:
    max_chunk = max((_int(item.get("chunk_index")) for item in session_rows), default=0)
    chunks_remaining = max(max_chunk - _int(row.get("chunk_index")), 0)
    return (
        _float(row.get("measured_throughput_kbps"))
        >= float(cfg.high_capacity_throughput_multiple) * float(cfg.max_ladder_bitrate_kbps)
        and _float(row.get("buffer_s")) >= float(cfg.high_capacity_min_buffer_s)
        and _float(row.get("rebuffer_s")) <= 1.0e-9
        and chunks_remaining > int(cfg.high_capacity_min_chunks_remaining)
    )


def _is_action0(row: Mapping[str, str], cfg: PolicyCollapseAuditConfig) -> bool:
    raw_action = str(row.get("neural_safe_action", row.get("neural_raw_action", ""))).strip()
    if raw_action == "0":
        return True
    return math.isclose(_float(row.get("bitrate_kbps")), float(cfg.min_ladder_bitrate_kbps), abs_tol=1.0e-6)


def _action_values(rows: Iterable[Mapping[str, str]], cfg: PolicyCollapseAuditConfig) -> list[str]:
    values = []
    for row in rows:
        action = str(row.get("neural_safe_action", "")).strip()
        if action:
            values.append(action)
        elif _is_action0(row, cfg):
            values.append("0")
        else:
            values.append(str(int(_float(row.get("bitrate_kbps")))))
    return values


def _time_to_reach_by_session(
    rows_by_session: Mapping[str, Sequence[Mapping[str, str]]],
    bitrate_kbps: float,
) -> dict[str, int | None]:
    output: dict[str, int | None] = {}
    for session_id, rows in rows_by_session.items():
        hit = None
        for row in rows:
            if _float(row.get("bitrate_kbps")) >= float(bitrate_kbps):
                hit = _int(row.get("chunk_index"))
                break
        output[session_id] = hit
    return output


def _max_consecutive_action0(
    rows_by_session: Mapping[str, Sequence[Mapping[str, str]]],
    cfg: PolicyCollapseAuditConfig,
) -> int:
    best = 0
    for rows in rows_by_session.values():
        run = 0
        for row in rows:
            if _int(row.get("chunk_index")) <= int(cfg.startup_chunks):
                continue
            if _is_action0(row, cfg):
                run += 1
                best = max(best, run)
            else:
                run = 0
    return best


def _paired_summary_deltas(
    rows: Sequence[Mapping[str, str]],
    cfg: PolicyCollapseAuditConfig,
) -> Mapping[str, object]:
    grouped: dict[tuple[str, str, str, str], dict[str, Mapping[str, str]]] = defaultdict(dict)
    for row in rows:
        key = (
            str(row.get("trace_window_id", "")),
            str(row.get("media_profile_id", "")),
            str(row.get("repetition", "")),
            str(row.get("synthetic", "")),
        )
        grouped[key][str(row.get("controller_alias", ""))] = row

    deltas = []
    for key, by_controller in sorted(grouped.items()):
        if cfg.controller_alias not in by_controller or cfg.baseline_alias not in by_controller:
            continue
        target = by_controller[cfg.controller_alias]
        baseline = by_controller[cfg.baseline_alias]
        deltas.append(
            {
                "trace_window_id": key[0],
                "media_profile_id": key[1],
                "repetition": key[2],
                "synthetic": key[3],
                "qoe_delta": _float(target.get("qoe_linear_mean")) - _float(baseline.get("qoe_linear_mean")),
                "rebuffer_delta_s": _float(target.get("total_rebuffer_s")) - _float(baseline.get("total_rebuffer_s")),
                "bitrate_delta_kbps": _float(target.get("avg_bitrate_kbps")) - _float(baseline.get("avg_bitrate_kbps")),
            }
        )
    return {
        "paired_session_count": len(deltas),
        "qoe_delta_vs_baseline_mean": _mean([row["qoe_delta"] for row in deltas]),
        "rebuffer_delta_vs_baseline_mean": _mean([row["rebuffer_delta_s"] for row in deltas]),
        "paired_deltas": deltas,
    }


def _histogram(values: Iterable[str]) -> dict[str, int]:
    return dict(sorted(Counter(str(value) for value in values).items()))


def _mean(values: Sequence[float]) -> float:
    clean = [float(value) for value in values if math.isfinite(float(value))]
    return float(statistics.mean(clean)) if clean else 0.0


def _median(values: Sequence[float]) -> float:
    clean = [float(value) for value in values if math.isfinite(float(value))]
    return float(statistics.median(clean)) if clean else 0.0


def _ratio(numerator: int, denominator: int) -> float:
    return float(numerator) / float(denominator) if denominator else 0.0


def _safe_divide(numerator: float, denominator: float) -> float:
    return float(numerator) / float(denominator) if denominator else 0.0


def _float(value: object, default: float = 0.0) -> float:
    try:
        parsed = float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return float(default)
    return parsed if math.isfinite(parsed) else float(default)


def _int(value: object, default: int = 0) -> int:
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return int(default)

from __future__ import annotations

import csv
import json
import math
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence

from core.evaluation.qoe import SegmentQoEInput, compute_linear_qoe, compute_log_qoe
from core.output_artifacts import (
    EVALUATION_SEGMENTS_FILENAME,
    LEGACY_OUTPUT_FILENAMES,
    RUN_MANIFEST_FILENAME,
    SEGMENT_TELEMETRY_FILENAME,
)


REFERENCE_CONTROLLER_ALIAS = "base_robust_mpc"
PROPIOS_PREFIXES = ("propio_",)
PLOT_MANIFEST_FILENAME = "plot_manifest.json"


def analyze_phase6_run(package_root: str | Path, *, generate_plots: bool = True) -> Dict[str, Any]:
    root = Path(package_root)
    protocol_dir = root / "00_protocolo"
    results_dir = root / "02_resultados"
    plots_dir = root / "03_graficas"
    report_dir = root / "04_informe"
    results_dir.mkdir(parents=True, exist_ok=True)
    plots_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)

    protocol = _read_json(protocol_dir / "protocolo_validacion.json")
    session_plan = _read_json(protocol_dir / "session_plan.json")
    sessions = session_plan.get("sessions", []) if isinstance(session_plan, Mapping) else []

    raw_chunks: List[Dict[str, Any]] = []
    summaries: List[Dict[str, Any]] = []
    for session in sessions:
        summary, chunks = summarize_session(session, package_root=root)
        summaries.append(summary)
        raw_chunks.extend(chunks)

    _write_csv(results_dir / "raw_chunks.csv", raw_chunks)
    _write_csv(results_dir / "session_summary.csv", summaries)

    aggregates = aggregate_summaries(summaries)
    statistics = paired_statistics(summaries)
    gates = evaluate_gates(protocol, sessions, summaries)
    ranking = build_ranking(aggregates, statistics, gates)

    package = {
        "schema_version": "phase6_results_v1",
        "package_root": str(root),
        "protocol": _public_protocol(protocol),
        "session_counts": _session_counts(summaries),
        "gates": gates,
        "aggregates": aggregates,
        "statistics": statistics,
        "ranking": ranking,
        "artifacts": {
            "raw_chunks_csv": str(results_dir / "raw_chunks.csv"),
            "session_summary_csv": str(results_dir / "session_summary.csv"),
            "resultados_para_validar_json": str(results_dir / "resultados_para_validar.json"),
            "resultados_para_validar_md": str(results_dir / "resultados_para_validar.md"),
            "plots_dir": str(plots_dir),
            "plot_manifest_json": str(plots_dir / PLOT_MANIFEST_FILENAME),
            "report_dir": str(report_dir),
        },
    }

    if generate_plots:
        generate_phase6_plots(raw_chunks, summaries, aggregates, plots_dir)

    (results_dir / "aggregates_by_controller.json").write_text(
        json.dumps(aggregates, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    (results_dir / "statistics.json").write_text(json.dumps(statistics, indent=2, sort_keys=True), encoding="utf-8")
    (results_dir / "resultados_para_validar.json").write_text(
        json.dumps(package, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    (results_dir / "resultados_para_validar.md").write_text(render_validation_markdown(package), encoding="utf-8")
    (report_dir / "informe_comparativo.md").write_text(render_comparative_report(package), encoding="utf-8")
    (report_dir / "conclusiones_tecnicas.md").write_text(render_technical_conclusions(package), encoding="utf-8")
    (report_dir / "manifest_paquete_evidencia.json").write_text(
        json.dumps(_evidence_manifest(root, package), indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return package


def summarize_session(
    session: Mapping[str, Any],
    *,
    package_root: Optional[str | Path] = None,
) -> tuple[Dict[str, Any], List[Dict[str, Any]]]:
    session_id = str(session.get("session_id", ""))
    run_root = _resolve_run_root(session, package_root)
    run_dir = _latest_run_dir(run_root)
    manifest = _read_json(run_dir / RUN_MANIFEST_FILENAME) if run_dir else {}
    telemetry_path = run_dir / SEGMENT_TELEMETRY_FILENAME if run_dir else None
    rows = _read_csv_dicts(telemetry_path) if telemetry_path else []
    evaluable_rows = [row for row in rows if _is_evaluable_media_row(row)]

    summary = _base_summary(session, run_dir, manifest)
    legacy_present = any((run_dir / name).exists() for name in LEGACY_OUTPUT_FILENAMES) if run_dir else False
    summary["legacy_artifacts_present"] = int(legacy_present)
    summary["run_status"] = str(manifest.get("status", "missing")) if manifest else "missing"
    summary["required_artifacts_present"] = int(_required_artifacts_present(run_dir) if run_dir else False)
    if summary["run_status"] != "completed":
        summary["failure_reason"] = _extract_failure_reason(_resolve_command_log_path(session, package_root))
        summary.update(
            {
                "evaluable": 0,
                "non_evaluable_reason": "run_status_{0}".format(summary["run_status"]),
                "segment_count": 0,
                "partial_evaluable_row_count": len(evaluable_rows),
            }
        )
        return summary, []

    if not evaluable_rows:
        summary.update(
            {
                "evaluable": 0,
                "non_evaluable_reason": "no_evaluable_rows",
                "segment_count": 0,
            }
        )
        return summary, []

    qoe_inputs = [
        SegmentQoEInput(
            bitrate_kbps=_bitrate_kbps(row),
            rebuffer_s=_float(row.get("stall_duration")),
        )
        for row in evaluable_rows
        if _bitrate_kbps(row) > 0
    ]
    if not qoe_inputs:
        summary.update({"evaluable": 0, "non_evaluable_reason": "no_valid_bitrate_rows", "segment_count": 0})
        return summary, []

    linear = compute_linear_qoe(qoe_inputs)
    min_bitrate = max(1.0, min(segment.bitrate_kbps for segment in qoe_inputs))
    log_qoe = compute_log_qoe(qoe_inputs, min_bitrate_kbps=min_bitrate)
    fragment_duration_sum = sum(_float(row.get("feedback_fragment_duration"), _float(row.get("fragment_duration"))) for row in evaluable_rows)
    total_rebuffer_s = float(linear.total_rebuffer_s)
    rebuffer_ratio = total_rebuffer_s / (fragment_duration_sum + total_rebuffer_s) if fragment_duration_sum + total_rebuffer_s > 0 else 0.0
    decision_latencies = [_float(row.get("policy_decision_ms")) for row in evaluable_rows if _float(row.get("policy_decision_ms")) > 0]
    buffers = [_float(row.get("feedback_queued_time")) for row in evaluable_rows]
    download_times = [_download_time_s(row) for row in evaluable_rows if _download_time_s(row) > 0.0]
    chunk_sizes = [_chunk_size_bytes(row) for row in evaluable_rows if _chunk_size_bytes(row) > 0]
    measured_throughputs = [
        _measured_throughput_kbps(row)
        for row in evaluable_rows
        if _measured_throughput_kbps(row) > 0.0
    ]
    positive_smoothness, negative_smoothness = _signed_smoothness(linear.segment_quality_utilities)
    neural_inference_times = [
        _float(row.get("feedback_neural_inference_ms"))
        for row in evaluable_rows
        if _float(row.get("feedback_neural_inference_ms")) > 0.0
    ]
    fallback_rows = sum(1 for row in evaluable_rows if _int(row.get("feedback_neural_fallback_used")) > 0)
    diagnostic_rows = sum(1 for row in evaluable_rows if _int(row.get("feedback_neural_diagnostic_only")) > 0)
    neural_audit = _neural_audit_counts(evaluable_rows)
    transitions = max(1, int(linear.segment_count) - 1)

    summary.update(
        {
            "evaluable": 1,
            "non_evaluable_reason": "",
            "segment_count": int(linear.segment_count),
            "qoe_linear_mean": float(linear.qoe_mean),
            "qoe_linear_sum": float(linear.qoe_sum),
            "qoe_log_mean": float(log_qoe.qoe_mean),
            "avg_bitrate_kbps": float(linear.avg_bitrate_kbps),
            "avg_quality_mbps": float(linear.avg_quality_mbps),
            "total_rebuffer_s": total_rebuffer_s,
            "rebuffer_ratio": float(rebuffer_ratio),
            "stall_event_count": int(linear.stall_event_count),
            "smoothness_penalty": float(linear.smoothness_penalty),
            "positive_smoothness_mbps": float(positive_smoothness),
            "negative_smoothness_mbps": float(negative_smoothness),
            "quality_switch_count": int(linear.quality_switch_count),
            "up_switch_count": int(linear.up_switch_count),
            "down_switch_count": int(linear.down_switch_count),
            "switching_rate": float(linear.quality_switch_count) / float(transitions),
            "avg_switch_magnitude_kbps": float(linear.avg_switch_magnitude_kbps),
            "avg_buffer_s": _mean(buffers),
            "low_buffer_ratio": _ratio_less_than(buffers, threshold=5.0),
            "avg_download_time_s": _mean(download_times),
            "avg_measured_throughput_kbps": _mean(measured_throughputs),
            "avg_chunk_size_bytes": _mean(chunk_sizes),
            "decision_latency_ms_mean": _mean(decision_latencies),
            "decision_latency_ms_p95": _percentile(decision_latencies, 95.0),
            "fallback_row_count": int(fallback_rows),
            "fallback_row_ratio": float(fallback_rows) / float(linear.segment_count),
            "diagnostic_only_row_count": int(diagnostic_rows),
            "neural_model_label": _first_nonempty(row.get("feedback_neural_model_label") for row in evaluable_rows),
            "neural_bundle_path": _first_nonempty(row.get("feedback_neural_bundle_path") for row in evaluable_rows),
            "neural_enabled_row_count": int(neural_audit["enabled"]),
            "neural_bundle_loaded_row_count": int(neural_audit["bundle_loaded"]),
            "neural_bundle_hash_ok_row_count": int(neural_audit["bundle_hash_ok"]),
            "neural_feature_vector_ok_row_count": int(neural_audit["feature_vector_ok"]),
            "neural_success_row_count": int(neural_audit["success"]),
            "neural_valid_action_row_count": int(neural_audit["valid_action"]),
            "neural_inference_row_count": int(len(neural_inference_times)),
            "neural_audit_ok_row_count": int(neural_audit["audit_ok"]),
            "neural_audit_missing_row_count": int(max(0, int(linear.segment_count) - int(neural_audit["audit_ok"]))),
            "neural_inference_ms_mean": _mean(neural_inference_times),
            "neural_inference_ms_p95": _percentile(neural_inference_times, 95.0),
        }
    )

    chunks: List[Dict[str, Any]] = []
    for idx, (row, reward, quality, smoothness) in enumerate(
        zip(evaluable_rows, linear.segment_rewards, linear.segment_quality_utilities, linear.segment_smoothness),
        start=1,
    ):
        chunks.append(
            {
                "session_id": session_id,
                "controller_alias": summary["controller_alias"],
                "controller_display_name": summary["controller_display_name"],
                "media_profile_id": summary["media_profile_id"],
                "trace_window_id": summary["trace_window_id"],
                "dataset_id": summary["dataset_id"],
                "semantics": summary["semantics"],
                "network_condition": summary["network_condition"],
                "difficulty_bucket": summary["difficulty_bucket"],
                "synthetic": summary["synthetic"],
                "repetition": summary["repetition"],
                "chunk_index": idx,
                "segment_index": _int(row.get("segment_index")),
                "bitrate_kbps": _bitrate_kbps(row),
                "quality_mbps": float(quality),
                "chunk_size_bytes": _chunk_size_bytes(row),
                "download_time_s": _download_time_s(row),
                "measured_throughput_kbps": _measured_throughput_kbps(row),
                "rebuffer_s": _float(row.get("stall_duration")),
                "smoothness_mbps": float(smoothness),
                "qoe_linear_reward": float(reward),
                "buffer_s": _float(row.get("feedback_queued_time")),
                "buffer_after_s": _float(row.get("feedback_queued_time")),
                "decision_latency_ms": _float(row.get("policy_decision_ms")),
                "fallback_used": _int(row.get("feedback_neural_fallback_used")),
                "neural_enabled": _int(row.get("feedback_neural_enabled")),
                "neural_model_label": str(row.get("feedback_neural_model_label", "")),
                "neural_bundle_loaded": _int(row.get("feedback_neural_bundle_loaded")),
                "neural_bundle_hash_ok": _int(row.get("feedback_neural_bundle_hash_ok")),
                "neural_feature_vector_ok": _int(row.get("feedback_neural_feature_vector_ok")),
                "neural_inference_ms": _float(row.get("feedback_neural_inference_ms")),
                "neural_fallback_reason": str(row.get("feedback_neural_fallback_reason", "")),
                "neural_raw_action": str(row.get("feedback_neural_raw_action", "")),
                "neural_safe_action": str(row.get("feedback_neural_safe_action", "")),
                "neural_valid_action": _int(row.get("feedback_neural_valid_action")),
                "neural_diagnostic_only": _int(row.get("feedback_neural_diagnostic_only")),
            }
        )
    return summary, chunks


def _std(values: Sequence[float]) -> float:
    clean = [float(value) for value in values]
    if len(clean) < 2:
        return 0.0
    mean = sum(clean) / len(clean)
    return math.sqrt(sum((value - mean) ** 2 for value in clean) / (len(clean) - 1))


def _min(values: Sequence[float]) -> float:
    clean = [float(value) for value in values]
    return min(clean) if clean else 0.0


def _max(values: Sequence[float]) -> float:
    clean = [float(value) for value in values]
    return max(clean) if clean else 0.0


def _worst_frac_mean(values: Sequence[float], frac: float) -> float:
    # Media de la peor fracción (mayor rebuffer) — SafeSABR worst-5%.
    clean = sorted((float(value) for value in values), reverse=True)
    if not clean:
        return 0.0
    count = max(1, int(math.ceil(float(frac) * len(clean))))
    return sum(clean[:count]) / count


def _rate(rows: Sequence[Mapping[str, Any]], key: str, threshold: float) -> float:
    if not rows:
        return 0.0
    return sum(1 for row in rows if _float(row.get(key)) > threshold) / len(rows)


def aggregate_summaries(summaries: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    real = [row for row in summaries if _int(row.get("evaluable")) and not _bool(row.get("synthetic"))]
    by_controller: Dict[str, List[Mapping[str, Any]]] = defaultdict(list)
    for row in real:
        by_controller[str(row.get("controller_alias", ""))].append(row)

    aggregates = []
    for alias in sorted(by_controller):
        rows = by_controller[alias]
        aggregates.append(
            {
                "controller_alias": alias,
                "controller_display_name": str(rows[0].get("controller_display_name", alias)),
                "session_count": len(rows),
                "qoe_linear_mean": _mean(_values(rows, "qoe_linear_mean")),
                "qoe_linear_ci95_low": bootstrap_ci(_values(rows, "qoe_linear_mean"))[0],
                "qoe_linear_ci95_high": bootstrap_ci(_values(rows, "qoe_linear_mean"))[1],
                # Robustez / cola (peor caso) — BayesMPC: worst-case QoE; MERINA/SODA: estabilidad.
                "qoe_linear_std": _std(_values(rows, "qoe_linear_mean")),
                "qoe_linear_min": _min(_values(rows, "qoe_linear_mean")),
                "qoe_linear_p05": _percentile(_values(rows, "qoe_linear_mean"), 5.0),
                "qoe_linear_p10": _percentile(_values(rows, "qoe_linear_mean"), 10.0),
                "qoe_linear_p25": _percentile(_values(rows, "qoe_linear_mean"), 25.0),
                "qoe_linear_median": _percentile(_values(rows, "qoe_linear_mean"), 50.0),
                "qoe_log_mean": _mean(_values(rows, "qoe_log_mean")),
                "avg_bitrate_kbps": _mean(_values(rows, "avg_bitrate_kbps")),
                "avg_quality_mbps": _mean(_values(rows, "avg_quality_mbps")),
                "total_rebuffer_s_mean": _mean(_values(rows, "total_rebuffer_s")),
                "rebuffer_ratio_mean": _mean(_values(rows, "rebuffer_ratio")),
                "rebuffer_ratio_p95": _percentile(_values(rows, "rebuffer_ratio"), 95.0),
                # Sesiones catastróficas (SafeSABR/Fugu): cola de rebuffer.
                "total_rebuffer_s_p95": _percentile(_values(rows, "total_rebuffer_s"), 95.0),
                "total_rebuffer_s_max": _max(_values(rows, "total_rebuffer_s")),
                "worst_5pct_rebuffer_mean_s": _worst_frac_mean(_values(rows, "total_rebuffer_s"), 0.05),
                "session_gt_5s_rebuffer_rate": _rate(rows, "total_rebuffer_s", 5.0),
                "session_gt_10s_rebuffer_rate": _rate(rows, "total_rebuffer_s", 10.0),
                "stall_event_count_mean": _mean(_values(rows, "stall_event_count")),
                "stall_session_rate": _rate(rows, "stall_event_count", 0.0),
                "smoothness_penalty_mean": _mean(_values(rows, "smoothness_penalty")),
                "positive_smoothness_mbps_mean": _mean(_values(rows, "positive_smoothness_mbps")),
                "negative_smoothness_mbps_mean": _mean(_values(rows, "negative_smoothness_mbps")),
                "switching_rate_mean": _mean(_values(rows, "switching_rate")),
                "avg_buffer_s": _mean(_values(rows, "avg_buffer_s")),
                "low_buffer_ratio_mean": _mean(_values(rows, "low_buffer_ratio")),
                "avg_download_time_s": _mean(_values(rows, "avg_download_time_s")),
                "avg_measured_throughput_kbps": _mean(_values(rows, "avg_measured_throughput_kbps")),
                "avg_chunk_size_bytes": _mean(_values(rows, "avg_chunk_size_bytes")),
                "decision_latency_ms_mean": _mean(_values(rows, "decision_latency_ms_mean")),
                "decision_latency_ms_p95": _percentile(_values(rows, "decision_latency_ms_p95"), 95.0),
                "fallback_row_count": int(sum(_int(row.get("fallback_row_count")) for row in rows)),
                "neural_audit_missing_row_count": int(sum(_int(row.get("neural_audit_missing_row_count")) for row in rows)),
                "neural_inference_ms_mean": _mean(_values(rows, "neural_inference_ms_mean")),
                "neural_inference_ms_p95": _percentile(_values(rows, "neural_inference_ms_p95"), 95.0),
            }
        )
    return sorted(aggregates, key=lambda row: row["qoe_linear_mean"], reverse=True)


def paired_statistics(summaries: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    real = [row for row in summaries if _int(row.get("evaluable")) and not _bool(row.get("synthetic"))]
    by_scenario: Dict[tuple[Any, ...], Dict[str, Mapping[str, Any]]] = defaultdict(dict)
    for row in real:
        scenario_key = (
            row.get("trace_window_id"),
            row.get("media_profile_id"),
            row.get("repetition"),
        )
        by_scenario[scenario_key][str(row.get("controller_alias"))] = row

    baseline_alias = REFERENCE_CONTROLLER_ALIAS
    deltas = []
    for scenario, rows_by_controller in by_scenario.items():
        baseline = rows_by_controller.get(baseline_alias)
        if not baseline:
            continue
        baseline_qoe = _float(baseline.get("qoe_linear_mean"))
        for alias, row in rows_by_controller.items():
            if alias == baseline_alias:
                continue
            delta = _float(row.get("qoe_linear_mean")) - baseline_qoe
            deltas.append(
                {
                    "controller_alias": alias,
                    "baseline_alias": baseline_alias,
                    "scenario_key": "|".join(str(part) for part in scenario),
                    "delta_qoe_linear": float(delta),
                }
            )

    by_controller: Dict[str, List[float]] = defaultdict(list)
    worst_by_controller: Dict[str, Mapping[str, Any]] = {}
    for item in deltas:
        alias = item["controller_alias"]
        by_controller[alias].append(float(item["delta_qoe_linear"]))
        if alias not in worst_by_controller or float(item["delta_qoe_linear"]) < float(
            worst_by_controller[alias]["delta_qoe_linear"]
        ):
            worst_by_controller[alias] = item

    comparisons = []
    for alias in sorted(by_controller):
        values = by_controller[alias]
        ci_low, ci_high = bootstrap_ci(values)
        comparisons.append(
            {
                "controller_alias": alias,
                "baseline_alias": baseline_alias,
                "paired_count": len(values),
                "delta_qoe_linear_mean": _mean(values),
                "delta_qoe_linear_ci95_low": ci_low,
                "delta_qoe_linear_ci95_high": ci_high,
                # Peor caso relativo al baseline (cola de las diferencias emparejadas).
                "delta_qoe_linear_p05": _percentile(values, 5.0),
                "delta_qoe_linear_p25": _percentile(values, 25.0),
                "delta_qoe_linear_worst": _min(values),
                "worst_scenario_key": str(worst_by_controller.get(alias, {}).get("scenario_key", "")),
                "sign_test_p_value": sign_test_exact(values),
            }
        )
    pairwise = []
    aliases = sorted({str(row.get("controller_alias")) for row in real})
    for left in aliases:
        for right in aliases:
            if left >= right:
                continue
            values = []
            for rows_by_controller in by_scenario.values():
                if left in rows_by_controller and right in rows_by_controller:
                    values.append(
                        _float(rows_by_controller[left].get("qoe_linear_mean"))
                        - _float(rows_by_controller[right].get("qoe_linear_mean"))
                    )
            if not values:
                continue
            ci_low, ci_high = bootstrap_ci(values)
            pairwise.append(
                {
                    "left_alias": left,
                    "right_alias": right,
                    "paired_count": len(values),
                    "delta_left_minus_right_mean": _mean(values),
                    "delta_left_minus_right_ci95_low": ci_low,
                    "delta_left_minus_right_ci95_high": ci_high,
                    "sign_test_p_value": sign_test_exact(values),
                }
            )

    return {
        "baseline_alias": baseline_alias,
        "scenario_count": len(by_scenario),
        "deltas_vs_baseline": comparisons,
        "pairwise_controller_deltas": pairwise,
    }


def evaluate_gates(
    protocol: Mapping[str, Any],
    sessions: Sequence[Mapping[str, Any]],
    summaries: Sequence[Mapping[str, Any]],
) -> Dict[str, Any]:
    preset = str(protocol.get("preset", ""))
    preset_capable = bool(protocol.get("benchmark_capable")) and preset in {"comparativa", "tfg_final", "equilibrado", "extendido"}
    real_required = [row for row in summaries if not _bool(row.get("synthetic"))]
    synthetic_rows = [row for row in summaries if _bool(row.get("synthetic"))]
    missing_or_bad = [
        str(row.get("session_id"))
        for row in real_required
        if str(row.get("run_status")) != "completed" or not _int(row.get("evaluable"))
    ]
    bad_splits = [str(item.get("session_id")) for item in sessions if not item.get("synthetic") and item.get("source_split") != "eval"]
    bad_media = [
        str(item.get("session_id"))
        for item in sessions
        if not item.get("synthetic") and float(item.get("segment_duration_s", 0.0) or 0.0) != 4.0
    ]
    fallback_violations = [
        str(row.get("session_id"))
        for row in real_required
        if str(row.get("controller_alias", "")).startswith(PROPIOS_PREFIXES)
        and (_int(row.get("fallback_row_count")) > 0 or _int(row.get("diagnostic_only_row_count")) > 0)
    ]
    neural_audit_violations = [
        str(row.get("session_id"))
        for row in real_required
        if str(row.get("controller_alias", "")).startswith(PROPIOS_PREFIXES)
        and (
            _int(row.get("segment_count")) <= 0
            or _int(row.get("neural_audit_missing_row_count")) > 0
            or _int(row.get("neural_success_row_count")) != _int(row.get("segment_count"))
            or _int(row.get("neural_inference_row_count")) != _int(row.get("segment_count"))
        )
    ]
    legacy_violations = [str(row.get("session_id")) for row in summaries if _int(row.get("legacy_artifacts_present"))]

    gate_items = {
        "required_real_sessions_completed": not missing_or_bad,
        "formal_uses_eval_split_only": not bad_splits,
        "formal_uses_only_4s_media_profiles": not bad_media,
        "propios_without_fallback_in_evaluable_rows": not fallback_violations,
        "propios_with_verified_neural_inference": not neural_audit_violations,
        "legacy_artifacts_absent": not legacy_violations,
        "synthetic_reported_separately": bool(synthetic_rows),
        "audit_text_package_available": True,
    }
    all_gates_passed = all(gate_items.values())
    return {
        "gate_items": gate_items,
        "all_gates_passed": all_gates_passed,
        "benchmark_authorized": bool(preset_capable and all_gates_passed),
        "ranking_authorized": bool(preset_capable and all_gates_passed),
        "violations": {
            "missing_or_not_evaluable_real_sessions": missing_or_bad,
            "bad_splits": bad_splits,
            "bad_media_profiles": bad_media,
            "fallback_violations": fallback_violations,
            "neural_audit_violations": neural_audit_violations,
            "legacy_violations": legacy_violations,
        },
    }


def build_ranking(
    aggregates: Sequence[Mapping[str, Any]],
    statistics: Mapping[str, Any],
    gates: Mapping[str, Any],
) -> Dict[str, Any]:
    ranking = [
        {
            "rank": index,
            "controller_alias": str(item.get("controller_alias")),
            "controller_display_name": str(item.get("controller_display_name")),
            "qoe_linear_mean": _float(item.get("qoe_linear_mean")),
        }
        for index, item in enumerate(aggregates, start=1)
    ]
    winner = None
    conclusion = "ranking descriptivo; sin ganador autorizado"
    if _bool(gates.get("ranking_authorized")) and len(ranking) >= 2:
        top = ranking[0]["controller_alias"]
        second = ranking[1]["controller_alias"]
        top_vs_second = _paired_delta_between(statistics, top, second)
        if top_vs_second and top_vs_second["ci95_low"] > 0 and top_vs_second["sign_test_p_value"] < 0.05:
            winner = ranking[0]
            conclusion = "ganador estadisticamente concluyente"
        else:
            conclusion = "sin ganador estadisticamente concluyente"
    return {
        "descriptive_ranking": ranking,
        "winner": winner,
        "conclusion": conclusion,
        "deltas_vs_baseline": list(statistics.get("deltas_vs_baseline", [])),
    }


def generate_phase6_plots(
    raw_chunks: Sequence[Mapping[str, Any]],
    summaries: Sequence[Mapping[str, Any]],
    aggregates: Sequence[Mapping[str, Any]],
    plots_dir: Path,
) -> None:
    plots_dir.mkdir(parents=True, exist_ok=True)
    manifest: List[Dict[str, Any]] = []
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:
        (plots_dir / "graficas_no_generadas.txt").write_text(str(exc), encoding="utf-8")
        (plots_dir / PLOT_MANIFEST_FILENAME).write_text(
            json.dumps(
                {
                    "schema_version": "phase6_plot_manifest_v1",
                    "plots": [
                        {
                            "plot_id": "all",
                            "status": "error",
                            "reason": str(exc),
                            "path": str(plots_dir / "graficas_no_generadas.txt"),
                        }
                    ],
                },
                indent=2,
                sort_keys=True,
            ),
            encoding="utf-8",
        )
        return

    real_summaries = [row for row in summaries if _int(row.get("evaluable")) and not _bool(row.get("synthetic"))]
    synthetic_summaries = [row for row in summaries if _int(row.get("evaluable")) and _bool(row.get("synthetic"))]
    _run_plot(
        manifest,
        plot_id="cdf_qoe_linear",
        output_path=plots_dir / "cdf_qoe_linear.png",
        source_count=len(real_summaries),
        plotter=lambda path: _plot_cdf_by_controller(
            real_summaries,
            metric="qoe_linear_mean",
            title="CDF QoE linear por sesion",
            output_path=path,
            plt=plt,
        ),
    )
    _run_plot(
        manifest,
        plot_id="cdf_qoe_log",
        output_path=plots_dir / "cdf_qoe_log.png",
        source_count=len(real_summaries),
        plotter=lambda path: _plot_cdf_by_controller(
            real_summaries,
            metric="qoe_log_mean",
            title="CDF QoE log por sesion",
            output_path=path,
            plt=plt,
        ),
    )
    _run_plot(
        manifest,
        plot_id="componentes_qoe",
        output_path=plots_dir / "componentes_qoe.png",
        source_count=len(aggregates),
        plotter=lambda path: _plot_components(aggregates, path, plt),
    )
    _run_plot(
        manifest,
        plot_id="calidad_vs_rebuffering",
        output_path=plots_dir / "calidad_vs_rebuffering.png",
        source_count=len(aggregates),
        plotter=lambda path: _plot_quality_rebuffer(aggregates, path, plt),
    )
    _run_plot(
        manifest,
        plot_id="cdf_rebuffering",
        output_path=plots_dir / "cdf_rebuffering.png",
        source_count=len(real_summaries),
        plotter=lambda path: _plot_cdf_by_controller(
            real_summaries,
            metric="total_rebuffer_s",
            title="CDF rebuffering por sesion",
            output_path=path,
            plt=plt,
        ),
    )
    _run_plot(
        manifest,
        plot_id="cdf_smoothness",
        output_path=plots_dir / "cdf_smoothness.png",
        source_count=len(real_summaries),
        plotter=lambda path: _plot_cdf_by_controller(
            real_summaries,
            metric="smoothness_penalty",
            title="CDF smoothness por sesion",
            output_path=path,
            plt=plt,
        ),
    )
    _run_plot(
        manifest,
        plot_id="cdf_bitrate",
        output_path=plots_dir / "cdf_bitrate.png",
        source_count=len(real_summaries),
        plotter=lambda path: _plot_cdf_by_controller(
            real_summaries,
            metric="avg_bitrate_kbps",
            title="CDF bitrate medio por sesion",
            output_path=path,
            plt=plt,
        ),
    )
    _run_plot(
        manifest,
        plot_id="cdf_buffer",
        output_path=plots_dir / "cdf_buffer.png",
        source_count=len(real_summaries),
        plotter=lambda path: _plot_cdf_by_controller(
            real_summaries,
            metric="avg_buffer_s",
            title="CDF buffer medio por sesion",
            output_path=path,
            plt=plt,
        ),
    )
    _run_plot(
        manifest,
        plot_id="qoe_por_dificultad_red",
        output_path=plots_dir / "qoe_por_dificultad_red.png",
        source_count=len(real_summaries),
        plotter=lambda path: _plot_qoe_by_group(real_summaries, "difficulty_bucket", path, plt, title="QoE por dificultad de red"),
    )
    _run_plot(
        manifest,
        plot_id="qoe_por_dataset",
        output_path=plots_dir / "qoe_por_dataset.png",
        source_count=len(real_summaries),
        plotter=lambda path: _plot_qoe_by_group(real_summaries, "dataset_id", path, plt, title="QoE por dataset"),
    )
    _run_plot(
        manifest,
        plot_id="qoe_por_condicion_red",
        output_path=plots_dir / "qoe_por_condicion_red.png",
        source_count=len(real_summaries),
        plotter=lambda path: _plot_qoe_by_group(real_summaries, "network_condition", path, plt, title="QoE por condicion de red"),
    )
    _run_plot(
        manifest,
        plot_id="caso_temporal_bitrate_qoe",
        output_path=plots_dir / "caso_temporal_bitrate_qoe.png",
        source_count=len(raw_chunks),
        plotter=lambda path: _plot_temporal_case(raw_chunks, path, plt),
    )
    _run_plot(
        manifest,
        plot_id="overhead_decision",
        output_path=plots_dir / "overhead_decision.png",
        source_count=len(aggregates),
        plotter=lambda path: _plot_overhead(aggregates, path, plt),
    )
    _run_plot(
        manifest,
        plot_id="sinteticas_diagnostico",
        output_path=plots_dir / "sinteticas_diagnostico.png",
        source_count=len(synthetic_summaries),
        plotter=lambda path: _plot_cdf_by_controller(
            synthetic_summaries,
            metric="qoe_linear_mean",
            title="CDF QoE sinteticas diagnosticas",
            output_path=path,
            plt=plt,
        ),
    )
    _run_plot(
        manifest,
        plot_id="qoe_robustez_peor_caso",
        output_path=plots_dir / "qoe_robustez_peor_caso.png",
        source_count=len(aggregates),
        plotter=lambda path: _plot_qoe_tail(aggregates, path, plt),
    )
    _run_plot(
        manifest,
        plot_id="stalls_por_controller",
        output_path=plots_dir / "stalls_por_controller.png",
        source_count=len(aggregates),
        plotter=lambda path: _plot_stalls(aggregates, path, plt),
    )
    manifest.append(
        {
            "plot_id": "metricas_deferred",
            "status": "deferred",
            "reason": "VMAF, SSIM, P.1203 y fidelidad simulador-real requieren artifacts perceptuales o ejecucion emparejada adicional.",
            "path": "",
            "source_count": 0,
            "bytes": 0,
        }
    )
    (plots_dir / PLOT_MANIFEST_FILENAME).write_text(
        json.dumps({"schema_version": "phase6_plot_manifest_v1", "plots": manifest}, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def _plot_qoe_tail(aggregates: Sequence[Mapping[str, Any]], output_path: Path, plt) -> None:
    rows = list(aggregates)
    if not rows:
        raise ValueError("no aggregates for tail plot")
    labels = [str(row.get("controller_display_name", row.get("controller_alias", ""))) for row in rows]
    mean = [_float(row.get("qoe_linear_mean")) for row in rows]
    median = [_float(row.get("qoe_linear_median")) for row in rows]
    p05 = [_float(row.get("qoe_linear_p05")) for row in rows]
    positions = list(range(len(rows)))
    width = 0.25
    fig, ax = plt.subplots(figsize=(max(6.0, len(rows) * 1.6), 4.0))
    ax.bar([p - width for p in positions], mean, width, label="media")
    ax.bar(list(positions), median, width, label="mediana")
    ax.bar([p + width for p in positions], p05, width, label="P5 (peor caso)")
    ax.set_xticks(list(positions))
    ax.set_xticklabels(labels, rotation=30, ha="right")
    ax.set_ylabel("QoE linear")
    ax.set_title("Robustez / peor caso de QoE por controller")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path, dpi=120)
    plt.close(fig)


def _plot_stalls(aggregates: Sequence[Mapping[str, Any]], output_path: Path, plt) -> None:
    rows = list(aggregates)
    if not rows:
        raise ValueError("no aggregates for stalls plot")
    labels = [str(row.get("controller_display_name", row.get("controller_alias", ""))) for row in rows]
    stalls = [_float(row.get("stall_event_count_mean")) for row in rows]
    gt5 = [100.0 * _float(row.get("session_gt_5s_rebuffer_rate")) for row in rows]
    gt10 = [100.0 * _float(row.get("session_gt_10s_rebuffer_rate")) for row in rows]
    positions = list(range(len(rows)))
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(max(8.0, len(rows) * 1.8), 4.2))
    ax1.bar(positions, stalls, color="#c0392b")
    ax1.set_xticks(positions)
    ax1.set_xticklabels(labels, rotation=30, ha="right")
    ax1.set_ylabel("stalls medios por sesion")
    ax1.set_title("Numero de stalls por controller")
    width = 0.4
    ax2.bar([p - width / 2 for p in positions], gt5, width, label=">5 s", color="#e67e22")
    ax2.bar([p + width / 2 for p in positions], gt10, width, label=">10 s", color="#8e44ad")
    ax2.set_xticks(positions)
    ax2.set_xticklabels(labels, rotation=30, ha="right")
    ax2.set_ylabel("% de sesiones")
    ax2.set_title("Sesiones con rebuffer significativo")
    ax2.legend()
    fig.tight_layout()
    fig.savefig(output_path, dpi=120)
    plt.close(fig)


def render_validation_markdown(package: Mapping[str, Any]) -> str:
    gates = package["gates"]
    protocol = _mapping(package.get("protocol"))
    lines = [
        "# Resultados para validar",
        "",
        "Este archivo resume el experimento en texto plano para auditoria rapida.",
        "",
        "## Estado",
        "",
        "- Benchmark autorizado: {0}".format(_yes_no(gates.get("benchmark_authorized"))),
        "- Ranking autorizado: {0}".format(_yes_no(gates.get("ranking_authorized"))),
        "- Gates superados: {0}".format(_yes_no(gates.get("all_gates_passed"))),
        "- Conclusion de ranking: {0}".format(package["ranking"]["conclusion"]),
        "",
        "## Veredicto tecnico del paquete",
        "",
        "- Estado: pendiente de verificacion automatica de paquete.",
        "",
    ]
    if str(protocol.get("preset", "")) == "diagnostico":
        lines.extend(
            [
                "## Aviso de preset diagnostico",
                "",
                "- Este paquete verifica cableado, metricas, graficas y auditoria.",
                "- No es benchmark, no autoriza ranking y no debe usarse para conclusiones comparativas.",
                "",
            ]
        )
    runtime = _mapping(protocol.get("preset_runtime"))
    if runtime:
        lines.extend(
            [
                "## Configuracion de ejecucion",
                "",
                "- Segmentos maximos por sesion: {0}".format(runtime.get("max_media_segments", "")),
                "- Ventana de replay de red: {0} s".format(runtime.get("network_window_duration_s", "")),
                "- Timeout por sesion: {0} s".format(runtime.get("timeout_seconds", "")),
                "- Duracion total estimada: {0:.1f} s".format(_float(runtime.get("estimated_total_duration_s"))),
                "",
            ]
        )
    lines.extend(
        [
        "## Sesiones",
        "",
        ]
    )
    counts = package["session_counts"]
    for key in ("total", "real", "synthetic", "evaluable", "completed"):
        lines.append("- {0}: {1}".format(key, counts.get(key, 0)))
    lines.extend(["", "## Agregados por controller", ""])
    for row in package["aggregates"]:
        lines.append(
            "- {0}: QoE={1:.4f}, bitrate={2:.1f} kbps, rebuffer={3:.3f}s, smoothness={4:.3f}, switching={5:.3f}".format(
                row.get("controller_display_name"),
                _float(row.get("qoe_linear_mean")),
                _float(row.get("avg_bitrate_kbps")),
                _float(row.get("total_rebuffer_s_mean")),
                _float(row.get("smoothness_penalty_mean")),
                _float(row.get("switching_rate_mean")),
            )
        )
    lines.extend(["", "## Robustez y peor caso (cola de QoE)", ""])
    for row in package["aggregates"]:
        lines.append(
            "- {0}: media={1:.3f}, mediana={2:.3f}, P5={3:.3f}, min={4:.3f}, std={5:.3f}, sesiones_con_stall={6:.0%}, rebuffer_P95={7:.3f}".format(
                row.get("controller_display_name"),
                _float(row.get("qoe_linear_mean")),
                _float(row.get("qoe_linear_median")),
                _float(row.get("qoe_linear_p05")),
                _float(row.get("qoe_linear_min")),
                _float(row.get("qoe_linear_std")),
                _float(row.get("stall_session_rate")),
                _float(row.get("rebuffer_ratio_p95")),
            )
        )
    lines.extend(["", "## Stalls y sesiones catastroficas (cola de rebuffer)", ""])
    for row in package["aggregates"]:
        lines.append(
            "- {0}: stalls/sesion={1:.2f}, rebuffer_P95={2:.2f}s, peor_sesion={3:.2f}s, worst5%_medio={4:.2f}s, sesiones>5s={5:.0%}, sesiones>10s={6:.0%}".format(
                row.get("controller_display_name"),
                _float(row.get("stall_event_count_mean")),
                _float(row.get("total_rebuffer_s_p95")),
                _float(row.get("total_rebuffer_s_max")),
                _float(row.get("worst_5pct_rebuffer_mean_s")),
                _float(row.get("session_gt_5s_rebuffer_rate")),
                _float(row.get("session_gt_10s_rebuffer_rate")),
            )
        )
    tail_deltas = _mapping(package.get("statistics")).get("deltas_vs_baseline", [])
    if tail_deltas:
        lines.extend(["", "## Peor caso vs baseline (robust_mpc)", ""])
        for row in tail_deltas:
            lines.append(
                "- {0}: delta QoE media={1:+.3f}, P5={2:+.3f}, peor={3:+.3f} (peor ventana: {4})".format(
                    row.get("controller_alias"),
                    _float(row.get("delta_qoe_linear_mean")),
                    _float(row.get("delta_qoe_linear_p05")),
                    _float(row.get("delta_qoe_linear_worst")),
                    row.get("worst_scenario_key", ""),
                )
            )
    plot_rows = _plot_manifest_rows(package)
    if plot_rows:
        lines.extend(["", "## Graficas", ""])
        for row in plot_rows:
            lines.append(
                "- {0}: {1} ({2} bytes)".format(
                    row.get("plot_id", ""),
                    row.get("status", ""),
                    row.get("bytes", 0),
                )
            )
    neural_rows = _own_controller_audit_rows(package)
    if neural_rows:
        lines.extend(["", "## Auditoria de inferencia propia", ""])
        for row in neural_rows:
            lines.append(
                "- {0}: auditadas {1}/{2}, inferencias {3}, fallback {4}, modo diagnostico {5}, inferencia media {6:.3f} ms".format(
                    row["controller_display_name"],
                    row["audit_ok_rows"],
                    row["segment_rows"],
                    row["inference_rows"],
                    row["fallback_rows"],
                    row["diagnostic_rows"],
                    row["inference_ms_mean"],
                )
            )
    lines.extend(["", "## Gates", ""])
    for name, ok in gates.get("gate_items", {}).items():
        lines.append("- {0}: {1}".format(name, _yes_no(ok)))
    violations = gates.get("violations", {})
    if any(violations.values()):
        lines.extend(["", "## Incidencias", ""])
        for name, values in violations.items():
            if values:
                lines.append("- {0}: {1}".format(name, ", ".join(values[:20])))
    failure_reasons = _top_failure_reasons(package)
    if failure_reasons:
        lines.extend(["", "## Motivos de fallo detectados", ""])
        for reason, count in failure_reasons:
            lines.append("- {0} sesiones: {1}".format(count, reason))
    return "\n".join(lines) + "\n"


def render_comparative_report(package: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "# Informe comparativo Phase 6",
            "",
            "La comparacion usa `qoe_linear_v1` como metrica primaria y mantiene las trazas sinteticas separadas.",
            "",
            "## Resultado",
            "",
            render_validation_markdown(package),
        ]
    )


def render_technical_conclusions(package: Mapping[str, Any]) -> str:
    ranking = package["ranking"]
    lines = [
        "# Conclusiones tecnicas",
        "",
        "- La metrica primaria es `qoe_linear_mean`.",
        "- Las comparaciones son emparejadas por ventana de traza, media profile y repeticion.",
        "- Las trazas sinteticas son diagnosticas y no sostienen generalizacion real.",
        "- Resultado: {0}.".format(ranking["conclusion"]),
    ]
    winner = ranking.get("winner")
    if winner:
        lines.append("- Controller destacado: {0}.".format(winner["controller_display_name"]))
    return "\n".join(lines) + "\n"


def bootstrap_ci(values: Sequence[float], *, confidence: float = 0.95, iterations: int = 1000, seed: int = 606) -> tuple[float, float]:
    clean = [float(value) for value in values if math.isfinite(float(value))]
    if not clean:
        return 0.0, 0.0
    if len(clean) == 1:
        return clean[0], clean[0]
    rng = random.Random(seed)
    means = []
    for _ in range(iterations):
        sample = [clean[rng.randrange(len(clean))] for _ in clean]
        means.append(sum(sample) / len(sample))
    means.sort()
    lower_idx = int(((1.0 - confidence) / 2.0) * (len(means) - 1))
    upper_idx = int((1.0 - (1.0 - confidence) / 2.0) * (len(means) - 1))
    return float(means[lower_idx]), float(means[upper_idx])


def sign_test_exact(values: Sequence[float]) -> float:
    wins = sum(1 for value in values if float(value) > 0)
    losses = sum(1 for value in values if float(value) < 0)
    n = wins + losses
    if n == 0:
        return 1.0
    tail = min(wins, losses)
    probability = sum(math.comb(n, k) for k in range(tail + 1)) / float(2 ** n)
    return float(min(1.0, 2.0 * probability))


def _base_summary(session: Mapping[str, Any], run_dir: Optional[Path], manifest: Mapping[str, Any]) -> Dict[str, Any]:
    return {
        "session_id": str(session.get("session_id", "")),
        "controller_alias": str(session.get("controller_alias", "")),
        "controller_display_name": str(session.get("controller_display_name", "")),
        "media_profile_id": str(session.get("media_profile_id", "")),
        "trace_window_id": str(session.get("trace_window_id", "")),
        "dataset_id": str(session.get("dataset_id", "")),
        "semantics": str(session.get("semantics", "")),
        "network_condition": str(session.get("network_condition", "")),
        "difficulty_bucket": str(session.get("difficulty_bucket", "")),
        "synthetic": int(bool(session.get("synthetic", False))),
        "source_split": str(session.get("source_split", "")),
        "segment_duration_s": float(session.get("segment_duration_s", 0.0) or 0.0),
        "repetition": int(session.get("repetition", 1) or 1),
        "run_dir": str(run_dir or ""),
        "run_status": str(manifest.get("status", "missing")) if manifest else "missing",
        "failure_reason": "",
        "evaluable": 0,
    }


def _top_failure_reasons(package: Mapping[str, Any]) -> List[tuple[str, int]]:
    summary_path = Path(str(_mapping(package.get("artifacts")).get("session_summary_csv", "")))
    rows = _read_csv_dicts(summary_path)
    counter = Counter(
        str(row.get("failure_reason", "")).strip()
        for row in rows
        if str(row.get("failure_reason", "")).strip()
    )
    return [(reason, count) for reason, count in counter.most_common(8)]


def _plot_manifest_rows(package: Mapping[str, Any]) -> List[Dict[str, Any]]:
    path = Path(str(_mapping(package.get("artifacts")).get("plot_manifest_json", "")))
    data = _read_json(path)
    rows = data.get("plots", []) if isinstance(data, Mapping) else []
    return [dict(row) for row in rows if isinstance(row, Mapping)]


def _own_controller_audit_rows(package: Mapping[str, Any]) -> List[Dict[str, Any]]:
    summary_path = Path(str(_mapping(package.get("artifacts")).get("session_summary_csv", "")))
    rows = [
        row
        for row in _read_csv_dicts(summary_path)
        if str(row.get("controller_alias", "")).startswith(PROPIOS_PREFIXES) and _int(row.get("evaluable"))
    ]
    if not rows:
        return []
    grouped: Dict[str, List[Mapping[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("controller_display_name", row.get("controller_alias", "")))].append(row)
    result = []
    for display_name in sorted(grouped):
        items = grouped[display_name]
        result.append(
            {
                "controller_display_name": display_name,
                "segment_rows": int(sum(_int(row.get("segment_count")) for row in items)),
                "audit_ok_rows": int(sum(_int(row.get("neural_audit_ok_row_count")) for row in items)),
                "inference_rows": int(sum(_int(row.get("neural_inference_row_count")) for row in items)),
                "fallback_rows": int(sum(_int(row.get("fallback_row_count")) for row in items)),
                "diagnostic_rows": int(sum(_int(row.get("diagnostic_only_row_count")) for row in items)),
                "inference_ms_mean": _mean(_values(items, "neural_inference_ms_mean")),
            }
        )
    return result


def _extract_failure_reason(command_log_path: Path) -> str:
    if not command_log_path.is_file():
        return ""
    try:
        lines = command_log_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return ""
    for line in reversed(lines):
        stripped = line.strip()
        if not stripped:
            continue
        if "TraceLoadError:" in stripped:
            return stripped.split("TraceLoadError:", 1)[1].strip() or stripped
        if "TraceReplayError:" in stripped:
            return stripped.split("TraceReplayError:", 1)[1].strip() or stripped
        if "ConfigError:" in stripped:
            return stripped.split("ConfigError:", 1)[1].strip() or stripped
        if stripped.startswith(("TraceLoadError:", "TraceReplayError:", "ConfigError:", "TimeoutExpired")):
            return stripped
    for line in reversed(lines):
        stripped = line.strip()
        if stripped:
            return stripped[:240]
    return ""


def _required_artifacts_present(run_dir: Path) -> bool:
    return all((run_dir / name).is_file() for name in (RUN_MANIFEST_FILENAME, SEGMENT_TELEMETRY_FILENAME, EVALUATION_SEGMENTS_FILENAME))


def _resolve_run_root(session: Mapping[str, Any], package_root: Optional[str | Path]) -> Path:
    configured = Path(str(session.get("run_output_root", "")))
    if configured.is_dir():
        return configured
    if package_root is not None:
        fallback = Path(package_root) / "01_ejecucion" / "runs" / str(session.get("session_id", ""))
        if fallback.is_dir():
            return fallback
    return configured


def _resolve_command_log_path(session: Mapping[str, Any], package_root: Optional[str | Path]) -> Path:
    configured = Path(str(session.get("command_log_path", "")))
    if configured.is_file():
        return configured
    if package_root is not None:
        fallback = Path(package_root) / "01_ejecucion" / "command_logs" / "{0}.log".format(session.get("session_id", ""))
        if fallback.is_file():
            return fallback
    return configured


def _is_evaluable_media_row(row: Mapping[str, Any]) -> bool:
    return _int(row.get("is_init")) == 0 and _int(row.get("use_for_eval")) == 1


def _bitrate_kbps(row: Mapping[str, Any]) -> float:
    return max(0.0, _float(row.get("feedback_cur_bitrate"), _float(row.get("feedback_cur_rate"))) * 8.0 / 1000.0)


def _chunk_size_bytes(row: Mapping[str, Any]) -> int:
    return max(0, _int(row.get("feedback_last_fragment_size"), _int(row.get("last_fragment_size"))))


def _download_time_s(row: Mapping[str, Any]) -> float:
    return max(0.0, _float(row.get("feedback_last_download_time"), _float(row.get("last_download_time"))))


def _measured_throughput_kbps(row: Mapping[str, Any]) -> float:
    size = _chunk_size_bytes(row)
    elapsed = _download_time_s(row)
    if size <= 0 or elapsed <= 0.0:
        return 0.0
    return float(size) * 8.0 / elapsed / 1000.0


def _signed_smoothness(quality_utilities: Sequence[float]) -> tuple[float, float]:
    positive = 0.0
    negative = 0.0
    for previous, current in zip(quality_utilities, quality_utilities[1:]):
        delta = float(current) - float(previous)
        if delta > 0.0:
            positive += delta
        elif delta < 0.0:
            negative += abs(delta)
    return positive, negative


def _neural_audit_counts(rows: Sequence[Mapping[str, Any]]) -> Dict[str, int]:
    counts = {
        "enabled": 0,
        "bundle_loaded": 0,
        "bundle_hash_ok": 0,
        "feature_vector_ok": 0,
        "success": 0,
        "valid_action": 0,
        "audit_ok": 0,
    }
    for row in rows:
        enabled = _int(row.get("feedback_neural_enabled")) > 0
        bundle_loaded = _int(row.get("feedback_neural_bundle_loaded")) > 0
        bundle_hash_ok = _int(row.get("feedback_neural_bundle_hash_ok")) > 0
        feature_vector_ok = _int(row.get("feedback_neural_feature_vector_ok")) > 0
        success = str(row.get("feedback_neural_fallback_reason", "")).strip() == "success_neural"
        valid_action = _int(row.get("feedback_neural_valid_action")) > 0
        no_fallback = _int(row.get("feedback_neural_fallback_used")) == 0
        not_diagnostic = _int(row.get("feedback_neural_diagnostic_only")) == 0
        inference_ms = _float(row.get("feedback_neural_inference_ms")) > 0.0
        counts["enabled"] += int(enabled)
        counts["bundle_loaded"] += int(bundle_loaded)
        counts["bundle_hash_ok"] += int(bundle_hash_ok)
        counts["feature_vector_ok"] += int(feature_vector_ok)
        counts["success"] += int(success)
        counts["valid_action"] += int(valid_action)
        counts["audit_ok"] += int(
            enabled
            and bundle_loaded
            and bundle_hash_ok
            and feature_vector_ok
            and success
            and valid_action
            and no_fallback
            and not_diagnostic
            and inference_ms
        )
    return counts


def _first_nonempty(values: Iterable[Any]) -> str:
    for value in values:
        text = str(value or "").strip()
        if text:
            return text
    return ""


def _session_counts(summaries: Sequence[Mapping[str, Any]]) -> Dict[str, int]:
    return {
        "total": len(summaries),
        "real": sum(1 for row in summaries if not _bool(row.get("synthetic"))),
        "synthetic": sum(1 for row in summaries if _bool(row.get("synthetic"))),
        "evaluable": sum(1 for row in summaries if _int(row.get("evaluable"))),
        "completed": sum(1 for row in summaries if str(row.get("run_status")) == "completed"),
    }


def _public_protocol(protocol: Mapping[str, Any]) -> Dict[str, Any]:
    return {
        "preset": protocol.get("preset"),
        "schema_version": protocol.get("schema_version"),
        "qoe_formula_version": protocol.get("qoe_formula_version"),
        "media_profile_count": len(protocol.get("media_profiles", [])),
        "trace_window_count": len(protocol.get("trace_windows", [])),
        "controller_count": len(protocol.get("controllers", [])),
        "benchmark_capable": bool(protocol.get("benchmark_capable")),
        "ranking_capable": bool(protocol.get("ranking_capable")),
        "preset_runtime": dict(_mapping(protocol.get("preset_runtime"))),
    }


def _evidence_manifest(root: Path, package: Mapping[str, Any]) -> Dict[str, Any]:
    return {
        "schema_version": "phase6_evidence_manifest_v1",
        "package_root": str(root),
        "benchmark_authorized": package["gates"]["benchmark_authorized"],
        "ranking_authorized": package["gates"]["ranking_authorized"],
        "required_files": package["artifacts"],
    }


def _run_plot(
    manifest: List[Dict[str, Any]],
    *,
    plot_id: str,
    output_path: Path,
    source_count: int,
    plotter,
) -> None:
    if int(source_count) <= 0:
        manifest.append(
            {
                "plot_id": plot_id,
                "status": "skipped",
                "reason": "sin datos evaluables",
                "path": str(output_path),
                "source_count": int(source_count),
                "bytes": 0,
            }
        )
        return
    try:
        plotter(output_path)
        size = output_path.stat().st_size if output_path.is_file() else 0
        manifest.append(
            {
                "plot_id": plot_id,
                "status": "generated" if size > 0 else "missing",
                "reason": "" if size > 0 else "archivo ausente o vacio",
                "path": str(output_path),
                "source_count": int(source_count),
                "bytes": int(size),
            }
        )
    except Exception as exc:
        manifest.append(
            {
                "plot_id": plot_id,
                "status": "error",
                "reason": str(exc),
                "path": str(output_path),
                "source_count": int(source_count),
                "bytes": 0,
            }
        )


def _plot_cdf_by_controller(rows, metric, title, output_path, plt) -> None:
    plt.figure(figsize=(8, 5))
    by_controller: Dict[str, List[float]] = defaultdict(list)
    for row in rows:
        by_controller[str(row.get("controller_display_name", row.get("controller_alias")))].append(_float(row.get(metric)))
    for label in sorted(by_controller):
        values = sorted(by_controller[label])
        if not values:
            continue
        y = [(idx + 1) / len(values) for idx in range(len(values))]
        plt.plot(values, y, label=label)
    plt.title(title)
    plt.xlabel(metric)
    plt.ylabel("CDF")
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(output_path, dpi=140)
    plt.close()


def _plot_components(aggregates, output_path, plt) -> None:
    labels = [str(row.get("controller_display_name")) for row in aggregates]
    x = range(len(labels))
    plt.figure(figsize=(10, 5))
    plt.bar(x, [_float(row.get("avg_quality_mbps")) for row in aggregates], label="Calidad Mbps")
    plt.bar(x, [-_float(row.get("total_rebuffer_s_mean")) for row in aggregates], label="-Rebuffer s")
    plt.bar(x, [-_float(row.get("smoothness_penalty_mean")) for row in aggregates], label="-Smoothness")
    plt.xticks(list(x), labels, rotation=35, ha="right")
    plt.title("Componentes QoE")
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(output_path, dpi=140)
    plt.close()


def _plot_quality_rebuffer(aggregates, output_path, plt) -> None:
    plt.figure(figsize=(7, 5))
    for row in aggregates:
        plt.scatter(_float(row.get("rebuffer_ratio_mean")), _float(row.get("avg_quality_mbps")), label=str(row.get("controller_display_name")))
    plt.xlabel("Rebuffering ratio")
    plt.ylabel("Calidad media Mbps")
    plt.title("Calidad vs rebuffering")
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(output_path, dpi=140)
    plt.close()


def _plot_qoe_by_group(rows, group_key, output_path, plt, title="QoE por grupo") -> None:
    grouped: Dict[str, Dict[str, List[float]]] = defaultdict(lambda: defaultdict(list))
    for row in rows:
        grouped[str(row.get(group_key, ""))][str(row.get("controller_display_name"))].append(_float(row.get("qoe_linear_mean")))
    labels = sorted(grouped)
    controllers = sorted({controller for group in grouped.values() for controller in group})
    plt.figure(figsize=(10, 5))
    width = 0.8 / max(1, len(controllers))
    base_x = list(range(len(labels)))
    for idx, controller in enumerate(controllers):
        values = [_mean(grouped[label].get(controller, [])) for label in labels]
        offsets = [x + idx * width for x in base_x]
        plt.bar(offsets, values, width=width, label=controller)
    plt.xticks([x + width * (len(controllers) - 1) / 2.0 for x in base_x], labels, rotation=25, ha="right")
    plt.ylabel("QoE medio")
    plt.title(title)
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(output_path, dpi=140)
    plt.close()


def _plot_temporal_case(raw_chunks, output_path, plt) -> None:
    if not raw_chunks:
        return
    first = raw_chunks[0]
    scenario = (first.get("trace_window_id"), first.get("media_profile_id"), first.get("repetition"))
    selected = [row for row in raw_chunks if (row.get("trace_window_id"), row.get("media_profile_id"), row.get("repetition")) == scenario]
    by_controller: Dict[str, List[Mapping[str, Any]]] = defaultdict(list)
    for row in selected:
        by_controller[str(row.get("controller_display_name"))].append(row)
    fig, axes = plt.subplots(4, 1, figsize=(10, 9), sharex=True)
    for label, rows in sorted(by_controller.items()):
        rows = sorted(rows, key=lambda row: _int(row.get("chunk_index")))
        chunks = [_int(row.get("chunk_index")) for row in rows]
        axes[0].plot(chunks, [_float(row.get("bitrate_kbps")) for row in rows], label=label)
        axes[1].plot(chunks, [_float(row.get("buffer_after_s"), _float(row.get("buffer_s"))) for row in rows], label=label)
        axes[2].plot(chunks, [_float(row.get("rebuffer_s")) for row in rows], label=label)
        axes[3].plot(chunks, [_float(row.get("qoe_linear_reward")) for row in rows], label=label)
    axes[0].set_ylabel("Bitrate kbps")
    axes[1].set_ylabel("Buffer s")
    axes[2].set_ylabel("Rebuffer s")
    axes[3].set_ylabel("QoE chunk")
    axes[3].set_xlabel("Chunk")
    axes[0].set_title("Caso temporal: decisiones y QoE")
    for axis in axes:
        axis.grid(True, alpha=0.3)
    axes[0].legend(fontsize=8, ncol=2)
    fig.tight_layout()
    fig.savefig(output_path, dpi=140)
    plt.close()


def _plot_overhead(aggregates, output_path, plt) -> None:
    labels = [str(row.get("controller_display_name")) for row in aggregates]
    values = [_float(row.get("decision_latency_ms_mean")) for row in aggregates]
    plt.figure(figsize=(9, 5))
    plt.bar(range(len(labels)), values)
    plt.xticks(range(len(labels)), labels, rotation=35, ha="right")
    plt.ylabel("ms por decision")
    plt.title("Overhead de decision")
    plt.tight_layout()
    plt.savefig(output_path, dpi=140)
    plt.close()


def _paired_delta_between(statistics: Mapping[str, Any], top_alias: str, second_alias: str) -> Optional[Dict[str, float]]:
    for row in statistics.get("pairwise_controller_deltas", []):
        left = str(row.get("left_alias"))
        right = str(row.get("right_alias"))
        if left == top_alias and right == second_alias:
            return {
                "mean": _float(row.get("delta_left_minus_right_mean")),
                "ci95_low": _float(row.get("delta_left_minus_right_ci95_low")),
                "ci95_high": _float(row.get("delta_left_minus_right_ci95_high")),
                "sign_test_p_value": _float(row.get("sign_test_p_value"), 1.0),
            }
        if left == second_alias and right == top_alias:
            return {
                "mean": -_float(row.get("delta_left_minus_right_mean")),
                "ci95_low": -_float(row.get("delta_left_minus_right_ci95_high")),
                "ci95_high": -_float(row.get("delta_left_minus_right_ci95_low")),
                "sign_test_p_value": _float(row.get("sign_test_p_value"), 1.0),
            }
    return None


def _values(rows: Sequence[Mapping[str, Any]], key: str) -> List[float]:
    return [_float(row.get(key)) for row in rows]


def _mean(values: Iterable[float]) -> float:
    clean = [float(value) for value in values if math.isfinite(float(value))]
    return sum(clean) / len(clean) if clean else 0.0


def _percentile(values: Sequence[float], percentile: float) -> float:
    clean = sorted(float(value) for value in values if math.isfinite(float(value)))
    if not clean:
        return 0.0
    if len(clean) == 1:
        return clean[0]
    position = (len(clean) - 1) * (float(percentile) / 100.0)
    lower = int(math.floor(position))
    upper = int(math.ceil(position))
    if lower == upper:
        return clean[lower]
    fraction = position - lower
    return clean[lower] * (1.0 - fraction) + clean[upper] * fraction


def _ratio_less_than(values: Sequence[float], threshold: float) -> float:
    clean = [float(value) for value in values if math.isfinite(float(value))]
    return sum(1 for value in clean if value < threshold) / float(len(clean)) if clean else 0.0


def _read_json(path: Path) -> Dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _read_csv_dicts(path: Optional[Path]) -> List[Dict[str, str]]:
    if path is None or not path.is_file():
        return []
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def _latest_run_dir(root: Path) -> Optional[Path]:
    if not root.is_dir():
        return None
    run_dirs = sorted(path for path in root.iterdir() if path.is_dir() and path.name.startswith("run_"))
    return run_dirs[-1] if run_dirs else None


def _float(value: Any, default: float = 0.0) -> float:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return float(default)
    return parsed if math.isfinite(parsed) else float(default)


def _int(value: Any, default: int = 0) -> int:
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return int(default)


def _bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _yes_no(value: Any) -> str:
    return "si" if _bool(value) else "no"

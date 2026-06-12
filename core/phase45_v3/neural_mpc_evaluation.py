from __future__ import annotations

import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Mapping, Sequence

from core.controller.bola import BolaController
from core.controller.rate_based import RateBasedController
from core.controller.robust_mpc import RobustMpcController
from core.neural_abr.artifacts import prepare_output_dir, write_json
from core.phase45_v1.dataset import load_trace_window
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v1.sampling import build_sampling_artifacts
from core.phase45_v3.abr_closed_loop_env import (
    PHASE45_V3_DEFAULT_MAX_BUFFER_S,
    AbrClosedLoopEnv,
    default_phase45_v3_ladder,
    runtime_feedback_from_state,
)
from core.phase45_v3.constants import MEDIA_PROFILE_ID, REWARD_VERSION, VALIDATION_ROLE, no_benchmark_policy
from core.phase45_v3.neural_mpc_controller import (
    NEURAL_MPC_CONTROLLER_KEY,
    NeuralThroughputCalibratedMpcController,
    TorchThroughputQuantilePredictor,
)
from core.phase45_v3.profiles import Phase45V3DatasetProfile
from core.trace_replay.network_model import END_POLICY_LOOP, TraceDrivenNetworkModel


NEURAL_MPC_CLOSED_LOOP_REPORT_SCHEMA_ID = "phase45_v3_neural_mpc_closed_loop_diagnostic_v1"
NEURAL_MPC_CLOSED_LOOP_REPORT_FILENAME = "reporte_phase45_v3_neural_mpc_closedloop.json"


class Phase45V3NeuralMpcEvaluationError(ValueError):
    """Raised when Neural-MPC closed-loop diagnostic evaluation cannot run."""


def evaluate_phase45_v3_neural_mpc_closed_loop(
    phase3_manifest: Mapping[str, object],
    output_dir: object,
    profile: Phase45V3DatasetProfile,
    *,
    predictor_checkpoint: object,
    controllers: Sequence[str] = ("robust_mpc", "bola", "throughput_rule", "neural_mpc"),
    preset: str = "diagnostic",
    source_manifest_path: object | None = None,
    overwrite: bool = False,
    max_validation_windows: int | None = None,
    representation_kbps: Sequence[int] = (300, 750, 1200, 1850, 2850, 4300),
    trace_path_rewrites: Sequence[PathRewriteRule] = (),
    device: str | None = "cpu",
) -> Mapping[str, object]:
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="phase45_v3 neural mpc closed-loop diagnostic")
    controller_keys = tuple(_normalize_controller_name(name) for name in controllers)
    if "neural_mpc" not in controller_keys:
        raise Phase45V3NeuralMpcEvaluationError("controllers must include neural_mpc")
    if "robust_mpc" not in controller_keys:
        raise Phase45V3NeuralMpcEvaluationError("controllers must include robust_mpc baseline")

    sampling = build_sampling_artifacts(phase3_manifest, profile, source_manifest_path=source_manifest_path)
    plan = dict(sampling["plan"])  # type: ignore[arg-type]
    windows = _limited_windows(plan["validation_windows"], _window_limit_for_preset(preset, max_validation_windows))  # type: ignore[index]
    segment_duration_s = float(plan["sampling_policy"]["segment_duration_s"])  # type: ignore[index]
    segment_count = int(plan["segment_count_per_window"])
    ladder = default_phase45_v3_ladder(
        segment_duration_s=segment_duration_s,
        segment_count=segment_count,
        representation_kbps=representation_kbps,
        max_buffer_s=PHASE45_V3_DEFAULT_MAX_BUFFER_S,
    )
    predictor = TorchThroughputQuantilePredictor(predictor_checkpoint, device=device)

    raw_rows = []
    session_rows = []
    skipped_windows = []
    for window in windows:
        try:
            loaded_trace, resolved_trace_path = load_trace_window(window, trace_path_rewrites)
            for controller_key in controller_keys:
                session = _run_session(
                    window=window,
                    resolved_trace_path=str(resolved_trace_path),
                    loaded_trace=loaded_trace,
                    ladder=ladder,
                    controller_key=controller_key,
                    predictor=predictor,
                )
                raw_rows.extend(session["raw_rows"])  # type: ignore[arg-type]
                session_rows.append(session["summary"])  # type: ignore[arg-type]
        except Exception as exc:  # noqa: BLE001 - diagnostic skips are audited.
            skipped_windows.append(
                {
                    "window_id": str(window.get("window_id")),
                    "reason": type(exc).__name__,
                    "message": str(exc),
                }
            )

    if not raw_rows or not session_rows:
        raise Phase45V3NeuralMpcEvaluationError("closed-loop diagnostic produced no rows")

    metrics = _build_metrics(raw_rows, session_rows)
    gates = _evaluate_gates(metrics)
    report = {
        "schema_id": NEURAL_MPC_CLOSED_LOOP_REPORT_SCHEMA_ID,
        "status": "PASS" if not gates["failed"] else "REVIEW",
        "phase": "fase_4_5_v3_neural_mpc_v1",
        "preset": str(preset),
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "output_dir": str(output_path),
        "profile": profile.to_json(),
        "media_profile_id": MEDIA_PROFILE_ID,
        "qoe_formula_version": REWARD_VERSION,
        "controller_keys": list(controller_keys),
        "predictor_checkpoint": str(predictor_checkpoint),
        "predictor_model_sha256": predictor.model_sha256,
        "window_count": len(windows),
        "skipped_windows": skipped_windows,
        "raw_row_count": len(raw_rows),
        "session_count": len(session_rows),
        "metrics": metrics,
        "gates": gates,
        "raw_rows_preview": raw_rows[:100],
        "session_summaries": session_rows,
        "controller_integrated": False,
        "diagnostic_only": True,
        "qoe_claims_authorized": False,
        **no_benchmark_policy(),
    }
    write_json(output_path / NEURAL_MPC_CLOSED_LOOP_REPORT_FILENAME, report)
    return report


def _run_session(
    *,
    window: Mapping[str, object],
    resolved_trace_path: str,
    loaded_trace,
    ladder,
    controller_key: str,
    predictor: TorchThroughputQuantilePredictor,
) -> Mapping[str, object]:
    network_model = TraceDrivenNetworkModel(loaded_trace, end_policy=END_POLICY_LOOP, max_loops=5)
    env = AbrClosedLoopEnv(ladder=ladder, network_model=network_model)
    controller = _make_controller(controller_key, predictor)
    raw_rows = []
    previous_bitrate_kbps = 0.0
    invalid_actions = 0
    while not env.done:
        state = env.state
        action_mask = env.action_mask()
        if controller_key == "neural_mpc":
            decision = controller.select_action(state, ladder, action_mask)  # type: ignore[union-attr]
            action = int(decision.action)
            neural_telemetry = decision.to_json()
        else:
            feedback = _feedback_for_classic(state, ladder)
            controller.setPlayerFeedback(feedback)  # type: ignore[union-attr]
            target_rate_Bps = float(controller.calcControlAction())  # type: ignore[union-attr]
            action = int(controller.quantizeRate(target_rate_Bps))  # type: ignore[union-attr]
            neural_telemetry = {}
        invalid_action_corrected = False
        if action < 0 or action >= ladder.representation_count or not action_mask[action]:
            invalid_actions += 1
            invalid_action_corrected = True
            action = 0
        step = env.step(action)
        bitrate_kbps = float(step.bitrate_kbps)
        smoothness_mbps = abs(bitrate_kbps - previous_bitrate_kbps) / 1000.0 if previous_bitrate_kbps > 0.0 else 0.0
        previous_bitrate_kbps = bitrate_kbps
        raw_rows.append(
            {
                "controller_key": controller_key,
                "window_id": str(window["window_id"]),
                "resolved_trace_path": resolved_trace_path,
                "trace_id": str(window["trace_id"]),
                "dataset_id": str(window["dataset_id"]),
                "semantics": str(window["semantics"]),
                "source_split": str(window["source_split"]),
                "throughput_bucket": str(window.get("throughput_bucket", "")),
                "variability_bucket": str(window.get("variability_bucket", "")),
                "synthetic": bool(window.get("synthetic") is True),
                "segment_index": int(step.segment_index),
                "action": int(action),
                "bitrate_kbps": bitrate_kbps,
                "buffer_s": float(step.buffer_s_before),
                "buffer_after_s": float(step.buffer_s_after),
                "download_time_s": float(step.download_time_s),
                "measured_throughput_kbps": float(step.measured_throughput_bps) / 1000.0,
                "rebuffer_s": float(step.rebuffer_s),
                "qoe_linear_reward": float(step.reward_n),
                "smoothness_mbps": float(smoothness_mbps),
                "invalid_action_corrected": invalid_action_corrected,
                "neural_fallback_used": bool(neural_telemetry.get("fallback_used", False)),
                "neural_fallback_reason": str(neural_telemetry.get("fallback_reason", "")),
                "neural_chosen_quantile": str(neural_telemetry.get("chosen_quantile", "")),
                "neural_best_sequence": list(neural_telemetry.get("best_sequence", [])),
            }
        )
    rewards = [float(row["qoe_linear_reward"]) for row in raw_rows]
    bitrates = [float(row["bitrate_kbps"]) for row in raw_rows]
    summary = {
        "controller_key": controller_key,
        "window_id": str(window["window_id"]),
        "trace_id": str(window["trace_id"]),
        "throughput_bucket": str(window.get("throughput_bucket", "")),
        "synthetic": bool(window.get("synthetic") is True),
        "segment_count": len(raw_rows),
        "qoe_linear_mean": _mean(rewards),
        "qoe_linear_sum": sum(rewards),
        "total_rebuffer_s": sum(float(row["rebuffer_s"]) for row in raw_rows),
        "stall_count": sum(1 for row in raw_rows if float(row["rebuffer_s"]) > 1.0e-9),
        "mean_bitrate_kbps": _mean(bitrates),
        "smoothness_mbps": sum(float(row["smoothness_mbps"]) for row in raw_rows),
        "action0_rate": _ratio(sum(1 for row in raw_rows if int(row["action"]) == 0), len(raw_rows)),
        "invalid_action_count": invalid_actions,
        "fallback_count": sum(1 for row in raw_rows if row["neural_fallback_used"]),
    }
    return {"raw_rows": raw_rows, "summary": summary}


def _make_controller(controller_key: str, predictor: TorchThroughputQuantilePredictor):
    if controller_key == "robust_mpc":
        return RobustMpcController(horizon=5)
    if controller_key == "bola":
        return BolaController()
    if controller_key == "throughput_rule":
        return RateBasedController()
    if controller_key == "neural_mpc":
        return NeuralThroughputCalibratedMpcController(
            predictor,
            quantiles=predictor.quantiles,
            horizon_segments=predictor.horizon_segments,
        )
    raise Phase45V3NeuralMpcEvaluationError("unsupported controller for diagnostic: {0}".format(controller_key))


def _feedback_for_classic(state, ladder) -> Mapping[str, object]:
    feedback = dict(runtime_feedback_from_state(state, ladder))
    feedback["throughput_history_bps"] = [float(value) for value in state.throughput_history_bps]
    feedback["throughput_history_Bps"] = [float(value) / 8.0 for value in state.throughput_history_bps]
    feedback["segment_sizes_B"] = [
        float(ladder.segment_size_bytes(index, min(int(state.segment_index), ladder.segment_count - 1)))
        for index in range(ladder.representation_count)
    ]
    feedback["remaining_segments"] = max(int(ladder.segment_count) - int(state.segment_index), 1)
    return feedback


def _build_metrics(
    raw_rows: Sequence[Mapping[str, object]],
    session_rows: Sequence[Mapping[str, object]],
) -> Mapping[str, object]:
    by_controller = defaultdict(list)
    for row in session_rows:
        by_controller[str(row["controller_key"])].append(row)
    raw_by_controller = defaultdict(list)
    for row in raw_rows:
        raw_by_controller[str(row["controller_key"])].append(row)

    controller_metrics = {}
    for controller, rows in sorted(by_controller.items()):
        raw = raw_by_controller[controller]
        high_capacity_rows = _high_capacity_rows(raw)
        controller_metrics[controller] = {
            "session_count": len(rows),
            "qoe_linear_mean": _mean([float(row["qoe_linear_mean"]) for row in rows]),
            "total_rebuffer_s": sum(float(row["total_rebuffer_s"]) for row in rows),
            "stall_count": sum(int(row["stall_count"]) for row in rows),
            "mean_bitrate_kbps": _mean([float(row["mean_bitrate_kbps"]) for row in rows]),
            "smoothness_mbps": sum(float(row["smoothness_mbps"]) for row in rows),
            "action0_rate": _ratio(sum(1 for row in raw if int(row["action"]) == 0), len(raw)),
            "high_capacity_row_count": len(high_capacity_rows),
            "high_capacity_action0_rate": _high_capacity_action0_rate(high_capacity_rows),
            "fallback_rate": _ratio(sum(1 for row in raw if row.get("neural_fallback_used") is True), len(raw)),
            "invalid_action_count": sum(int(row["invalid_action_count"]) for row in rows),
            "action_histogram": dict(sorted(Counter(str(int(row["action"])) for row in raw).items())),
        }

    paired = _paired_metrics(session_rows, raw_rows)
    neural = controller_metrics.get("neural_mpc", {})
    return {
        "controllers": controller_metrics,
        "paired_vs_robust_mpc": paired,
        "neural_mpc": {
            "high_capacity_neural_row_count": neural.get("high_capacity_row_count", 0),
            "high_capacity_robust_mpc_row_count": paired.get("high_capacity_robust_mpc_row_count", 0),
            "high_capacity_action0_rate": neural.get("high_capacity_action0_rate", 0.0),
            "high_capacity_mean_bitrate_ratio_vs_robust_mpc": paired.get(
                "high_capacity_mean_bitrate_ratio_vs_robust_mpc",
                0.0,
            ),
            "fallback_rate": neural.get("fallback_rate", 0.0),
            "invalid_action_count": neural.get("invalid_action_count", 0),
            "qoe_delta_vs_robust_mpc_mean": paired.get("qoe_delta_vs_robust_mpc_mean", 0.0),
            "rebuffer_delta_vs_robust_mpc_mean": paired.get("rebuffer_delta_vs_robust_mpc_mean", 0.0),
            "bucket_2_5_mbps_qoe_delta_vs_robust_mpc_mean": paired.get(
                "bucket_2_5_mbps_qoe_delta_vs_robust_mpc_mean",
                0.0,
            ),
            "bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean": paired.get(
                "bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean",
                0.0,
            ),
        },
    }


def _paired_metrics(
    session_rows: Sequence[Mapping[str, object]],
    raw_rows: Sequence[Mapping[str, object]],
) -> Mapping[str, object]:
    by_key: dict[tuple[str, str], Mapping[str, object]] = {}
    for row in session_rows:
        by_key[(str(row["window_id"]), str(row["controller_key"]))] = row
    deltas = []
    for (window_id, controller), row in sorted(by_key.items()):
        if controller != "neural_mpc":
            continue
        baseline = by_key.get((window_id, "robust_mpc"))
        if baseline is None:
            continue
        deltas.append(
            {
                "window_id": window_id,
                "throughput_bucket": str(row.get("throughput_bucket", "")),
                "qoe_delta": float(row["qoe_linear_mean"]) - float(baseline["qoe_linear_mean"]),
                "rebuffer_delta_s": float(row["total_rebuffer_s"]) - float(baseline["total_rebuffer_s"]),
                "bitrate_delta_kbps": float(row["mean_bitrate_kbps"]) - float(baseline["mean_bitrate_kbps"]),
            }
        )
    high_neural = _high_capacity_bitrates([row for row in raw_rows if str(row["controller_key"]) == "neural_mpc"])
    high_robust = _high_capacity_bitrates([row for row in raw_rows if str(row["controller_key"]) == "robust_mpc"])
    bucket_2_5 = [row for row in deltas if row["throughput_bucket"] == "2_5_mbps"]
    return {
        "paired_session_count": len(deltas),
        "qoe_delta_vs_robust_mpc_mean": _mean([float(row["qoe_delta"]) for row in deltas]),
        "rebuffer_delta_vs_robust_mpc_mean": _mean([float(row["rebuffer_delta_s"]) for row in deltas]),
        "bitrate_delta_vs_robust_mpc_mean": _mean([float(row["bitrate_delta_kbps"]) for row in deltas]),
        "bucket_2_5_mbps_qoe_delta_vs_robust_mpc_mean": _mean([float(row["qoe_delta"]) for row in bucket_2_5]),
        "bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean": _mean(
            [float(row["rebuffer_delta_s"]) for row in bucket_2_5]
        ),
        "high_capacity_neural_row_count": len(high_neural),
        "high_capacity_robust_mpc_row_count": len(high_robust),
        "high_capacity_mean_bitrate_ratio_vs_robust_mpc": _safe_divide(_mean(high_neural), _mean(high_robust)),
        "paired_deltas": deltas,
    }


def _evaluate_gates(metrics: Mapping[str, object]) -> Mapping[str, object]:
    neural = metrics["neural_mpc"]  # type: ignore[index]
    gates: dict[str, Mapping[str, object]] = {}

    def add(name: str, passed: bool, observed: object, threshold: object) -> None:
        gates[name] = {"passed": bool(passed), "observed": observed, "threshold": threshold}

    high_capacity_neural_rows = int(neural["high_capacity_neural_row_count"])
    high_capacity_robust_rows = int(neural["high_capacity_robust_mpc_row_count"])
    high_capacity_coverage = high_capacity_neural_rows > 0 and high_capacity_robust_rows > 0
    high_capacity_observed = {
        "neural_rows": high_capacity_neural_rows,
        "robust_mpc_rows": high_capacity_robust_rows,
    }
    add("high_capacity_coverage", high_capacity_coverage, high_capacity_observed, "both > 0")
    add(
        "high_capacity_action0_rate",
        high_capacity_neural_rows > 0 and float(neural["high_capacity_action0_rate"]) <= 0.05,
        {
            "row_count": high_capacity_neural_rows,
            "rate": neural["high_capacity_action0_rate"],
        },
        "row_count > 0 and rate <= 0.05",
    )
    add(
        "high_capacity_mean_bitrate_ratio_vs_robust_mpc",
        high_capacity_coverage and float(neural["high_capacity_mean_bitrate_ratio_vs_robust_mpc"]) >= 0.70,
        {
            "row_counts": high_capacity_observed,
            "ratio": neural["high_capacity_mean_bitrate_ratio_vs_robust_mpc"],
        },
        "coverage present and ratio >= 0.70",
    )
    add("fallback_rate", float(neural["fallback_rate"]) == 0.0, neural["fallback_rate"], "== 0")
    add("invalid_action_count", int(neural["invalid_action_count"]) == 0, neural["invalid_action_count"], "== 0")
    add(
        "bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean",
        float(neural["bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean"]) <= 1.0,
        neural["bucket_2_5_mbps_rebuffer_delta_vs_robust_mpc_mean"],
        "<= +1.0 s",
    )
    add(
        "qoe_delta_vs_robust_mpc_mean_not_catastrophic",
        float(neural["qoe_delta_vs_robust_mpc_mean"]) >= -2.0,
        neural["qoe_delta_vs_robust_mpc_mean"],
        ">= -2.0",
    )
    failed = [name for name, row in gates.items() if not row["passed"]]
    return {"failed": failed, "gates": gates}


def _high_capacity_rows(rows: Sequence[Mapping[str, object]]) -> list[Mapping[str, object]]:
    return [row for row in rows if _is_high_capacity_row(row)]


def _high_capacity_action0_rate(rows: Sequence[Mapping[str, object]]) -> float:
    return _ratio(sum(1 for row in rows if int(row["action"]) == 0), len(rows))


def _high_capacity_bitrates(rows: Sequence[Mapping[str, object]]) -> list[float]:
    return [float(row["bitrate_kbps"]) for row in rows if _is_high_capacity_row(row)]


def _is_high_capacity_row(row: Mapping[str, object]) -> bool:
    return (
        float(row.get("measured_throughput_kbps", 0.0)) >= 2.0 * 4300.0
        and float(row.get("buffer_s", 0.0)) >= 8.0
        and float(row.get("rebuffer_s", 0.0)) <= 1.0e-9
    )


def _normalize_controller_name(name: str) -> str:
    key = str(name).strip()
    if key == "rate_based":
        return "throughput_rule"
    return key


def _window_limit_for_preset(preset: str, explicit: int | None) -> int | None:
    if explicit is not None:
        return int(explicit)
    if str(preset).strip().lower() == "diagnostic":
        return 8
    return None


def _limited_windows(raw_windows: object, limit: int | None) -> list[Mapping[str, object]]:
    if not isinstance(raw_windows, list):
        raise Phase45V3NeuralMpcEvaluationError("sampling plan validation_windows must be a list")
    windows = []
    for index, window in enumerate(raw_windows):
        if not isinstance(window, Mapping):
            raise Phase45V3NeuralMpcEvaluationError("validation window {0} must be an object".format(index))
        windows.append(window)
    if limit is not None:
        return windows[: int(limit)]
    return windows


def _mean(values: Sequence[float]) -> float:
    clean = [float(value) for value in values if math.isfinite(float(value))]
    return sum(clean) / float(len(clean)) if clean else 0.0


def _ratio(numerator: int, denominator: int) -> float:
    return float(numerator) / float(denominator) if denominator else 0.0


def _safe_divide(numerator: float, denominator: float) -> float:
    return float(numerator) / float(denominator) if denominator else 0.0

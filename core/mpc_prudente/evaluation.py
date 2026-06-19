"""Diagnóstico closed-loop offline de MPC Prudente sobre el entorno FIEL.

Compara el controller prudente vs `robust_mpc`, `bola` y el Neural-MPC viejo en el
entorno closed-loop con el **ladder fiel** (tamaños reales VBR), sobre ventanas de
VALIDACIÓN (no eval; eval queda para Phase 6).

Lección aprendida: el corpus de validación incluye trazas **impracticables**
(media de pocas kbps) y con **outages** (throughput→0). En ellas ningún controller
puede evitar rebuffer, así que prudente y robust empatan y los números absolutos se
disparan, ahogando la señal. Por eso, como Phase 6, se aplica un **suelo de
servibilidad** (media de throughput) para el titular, y se **estratifica por bucket
de capacidad y variabilidad**, que es donde se ve si la prudencia ayuda (régimen
`2_5_mbps` variable, tipo `real_006`).

No es benchmark ni ranking.
"""

from __future__ import annotations

import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Mapping, Sequence

from core.controller.bola import BolaController
from core.controller.rate_based import RateBasedController
from core.controller.robust_mpc import RobustMpcController
from core.mpc_prudente.media_profile import DEFAULT_MAX_BUFFER_S, MediaProfileSegmentSizes
from core.mpc_prudente.planner import MPC_PRUDENTE_CONTROLLER_KEY, PrudentMpcController
from core.neural_abr.artifacts import prepare_output_dir, write_json
from core.phase45_v1.dataset import load_trace_window
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v1.sampling import build_sampling_artifacts
from core.phase45_v3.abr_closed_loop_env import AbrClosedLoopEnv, runtime_feedback_from_state
from core.phase45_v3.constants import REWARD_VERSION, no_benchmark_policy
from core.phase45_v3.neural_mpc_controller import (
    NeuralThroughputCalibratedMpcController,
    TorchThroughputQuantilePredictor,
)
from core.phase45_v3.profiles import Phase45V3DatasetProfile
from core.trace_replay.network_model import END_POLICY_LOOP, TraceDrivenNetworkModel

MPC_PRUDENTE_CLOSED_LOOP_REPORT_SCHEMA_ID = "mpc_prudente_closed_loop_diagnostic_v2"
MPC_PRUDENTE_CLOSED_LOOP_REPORT_FILENAME = "reporte_mpc_prudente_closedloop.json"

REFERENCE_CONTROLLER = "robust_mpc"
HIGH_CAPACITY_THROUGHPUT_KBPS = 2.0 * 4300.0
# Suelo de servibilidad: bajo esta media de throughput, ni el bitrate más bajo
# (300 kbps) es servible, así que la comparación no es informativa.
DEFAULT_SERVABLE_MEAN_KBPS = 600.0


class MpcPrudenteEvaluationError(ValueError):
    """Raised when the prudent closed-loop diagnostic cannot run."""


def evaluate_mpc_prudente_closed_loop(
    phase3_manifest: Mapping[str, object],
    output_dir: object,
    profile: Phase45V3DatasetProfile,
    *,
    predictor_checkpoint: object,
    media_profile_id: str,
    media_profile_base_dir: str | None = None,
    controllers: Sequence[str] = (MPC_PRUDENTE_CONTROLLER_KEY, "robust_mpc", "bola", "neural_mpc"),
    source_manifest_path: object | None = None,
    overwrite: bool = False,
    max_validation_windows: int | None = None,
    max_buffer_s: float = DEFAULT_MAX_BUFFER_S,
    servable_mean_kbps: float = DEFAULT_SERVABLE_MEAN_KBPS,
    trace_path_rewrites: Sequence[PathRewriteRule] = (),
    device: str | None = "cpu",
) -> Mapping[str, object]:
    output_path = prepare_output_dir(output_dir, overwrite=overwrite, purpose="mpc_prudente closed-loop diagnostic")
    controller_keys = tuple(str(name).strip() for name in controllers)
    if MPC_PRUDENTE_CONTROLLER_KEY not in controller_keys:
        raise MpcPrudenteEvaluationError("controllers must include {0}".format(MPC_PRUDENTE_CONTROLLER_KEY))
    if REFERENCE_CONTROLLER not in controller_keys:
        raise MpcPrudenteEvaluationError("controllers must include robust_mpc reference")

    sampling = build_sampling_artifacts(phase3_manifest, profile, source_manifest_path=source_manifest_path)
    plan = dict(sampling["plan"])  # type: ignore[arg-type]
    windows = _limited(plan["validation_windows"], max_validation_windows)  # type: ignore[index]
    segment_count = int(plan["segment_count_per_window"])
    media_profile = MediaProfileSegmentSizes.load_by_id(media_profile_id, base_dir=media_profile_base_dir)
    ladder = media_profile.to_faithful_ladder(segment_count=segment_count, max_buffer_s=max_buffer_s)
    predictor = TorchThroughputQuantilePredictor(predictor_checkpoint, device=device)

    session_rows: list[Mapping[str, object]] = []
    skipped: list[Mapping[str, object]] = []
    for window in windows:
        try:
            loaded_trace, _resolved = load_trace_window(window, trace_path_rewrites)
            servable = float(loaded_trace.throughput_mean_kbps) >= float(servable_mean_kbps)
            for controller_key in controller_keys:
                session_rows.append(
                    _run_session(window, loaded_trace, ladder, controller_key, predictor, servable)
                )
        except Exception as exc:  # noqa: BLE001 - skips auditados.
            skipped.append(
                {"window_id": str(window.get("window_id")), "reason": type(exc).__name__, "message": str(exc)}
            )

    if not session_rows:
        raise MpcPrudenteEvaluationError("closed-loop diagnostic produced no sessions")

    controller_metrics = _controller_metrics(session_rows)
    paired = _paired_vs_reference(session_rows)
    gates = _gates(controller_metrics, paired)
    servable_window_count = len({str(s["window_id"]) for s in session_rows if s["servable"]})
    report = {
        "schema_id": MPC_PRUDENTE_CLOSED_LOOP_REPORT_SCHEMA_ID,
        "status": "PASS" if not gates["failed"] else "REVIEW",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "output_dir": str(output_path),
        "profile": profile.to_json(),
        "media_profile_id": media_profile_id,
        "segment_size_source": "real_vbr_from_server",
        "qoe_formula_version": REWARD_VERSION,
        "controller_keys": list(controller_keys),
        "predictor_checkpoint": str(predictor_checkpoint),
        "predictor_model_sha256": predictor.model_sha256,
        "servable_mean_kbps_floor": float(servable_mean_kbps),
        "window_count": len(windows),
        "servable_window_count": servable_window_count,
        "session_count": len(session_rows),
        "skipped_windows": skipped,
        "controllers": controller_metrics,
        "paired_vs_robust_mpc": paired,
        "gates": gates,
        "controller_integrated": False,
        "diagnostic_only": True,
        "qoe_claims_authorized": False,
        **no_benchmark_policy(),
    }
    write_json(output_path / MPC_PRUDENTE_CLOSED_LOOP_REPORT_FILENAME, report)
    return report


def _run_session(window, loaded_trace, ladder, controller_key, predictor, servable):
    network_model = TraceDrivenNetworkModel(loaded_trace, end_policy=END_POLICY_LOOP, max_loops=5)
    env = AbrClosedLoopEnv(ladder=ladder, network_model=network_model)
    controller = _make_controller(controller_key, predictor)
    rows = []
    invalid_actions = 0
    fallback_count = 0
    while not env.done:
        state = env.state
        action_mask = env.action_mask()
        if controller_key in (MPC_PRUDENTE_CONTROLLER_KEY, "neural_mpc"):
            decision = controller.select_action(state, ladder, action_mask)
            action = int(decision.action)
            if bool(getattr(decision, "fallback_used", False)):
                fallback_count += 1
        else:
            feedback = _feedback_for_classic(state, ladder)
            controller.setPlayerFeedback(feedback)
            action = int(controller.quantizeRate(float(controller.calcControlAction())))
        if action < 0 or action >= ladder.representation_count or not action_mask[action]:
            invalid_actions += 1
            action = 0
        step = env.step(action)
        rows.append(
            {
                "action": int(action),
                "bitrate_kbps": float(step.bitrate_kbps),
                "buffer_s": float(step.buffer_s_before),
                "measured_throughput_kbps": float(step.measured_throughput_bps) / 1000.0,
                "rebuffer_s": float(step.rebuffer_s),
                "qoe_linear_reward": float(step.reward_n),
            }
        )
    rewards = [float(r["qoe_linear_reward"]) for r in rows]
    high = [r for r in rows if _is_high_capacity(r)]
    return {
        "controller_key": controller_key,
        "window_id": str(window["window_id"]),
        "variability_bucket": str(window.get("variability_bucket", "")),
        "throughput_bucket": str(window.get("throughput_bucket", "")),
        "trace_mean_kbps": float(loaded_trace.throughput_mean_kbps),
        "trace_min_kbps": float(loaded_trace.throughput_min_kbps),
        "servable": bool(servable),
        "qoe_linear_mean": _mean(rewards),
        "total_rebuffer_s": sum(float(r["rebuffer_s"]) for r in rows),
        "stall_count": sum(1 for r in rows if float(r["rebuffer_s"]) > 1.0e-9),
        "mean_bitrate_kbps": _mean([float(r["bitrate_kbps"]) for r in rows]),
        "action0_rate": _ratio(sum(1 for r in rows if int(r["action"]) == 0), len(rows)),
        "high_capacity_row_count": len(high),
        "high_capacity_action0_count": sum(1 for r in high if int(r["action"]) == 0),
        "invalid_action_count": invalid_actions,
        "fallback_count": fallback_count,
        "action_counts": dict(Counter(str(int(r["action"])) for r in rows)),
    }


def _make_controller(controller_key, predictor):
    if controller_key == MPC_PRUDENTE_CONTROLLER_KEY:
        return PrudentMpcController(predictor, quantiles=predictor.quantiles, horizon_segments=predictor.horizon_segments)
    if controller_key == "neural_mpc":
        return NeuralThroughputCalibratedMpcController(
            predictor, quantiles=predictor.quantiles, horizon_segments=predictor.horizon_segments
        )
    if controller_key == "robust_mpc":
        return RobustMpcController(horizon=5)
    if controller_key == "bola":
        return BolaController()
    if controller_key in ("rate_based", "throughput_rule"):
        return RateBasedController()
    raise MpcPrudenteEvaluationError("unsupported controller: {0}".format(controller_key))


def _feedback_for_classic(state, ladder) -> Mapping[str, object]:
    feedback = dict(runtime_feedback_from_state(state, ladder))
    feedback["throughput_history_bps"] = [float(v) for v in state.throughput_history_bps]
    feedback["throughput_history_Bps"] = [float(v) / 8.0 for v in state.throughput_history_bps]
    feedback["segment_sizes_B"] = [
        float(ladder.segment_size_bytes(index, min(int(state.segment_index), ladder.segment_count - 1)))
        for index in range(ladder.representation_count)
    ]
    feedback["remaining_segments"] = max(int(ladder.segment_count) - int(state.segment_index), 1)
    return feedback


def _controller_metrics(session_rows) -> Mapping[str, object]:
    by_controller = defaultdict(list)
    for row in session_rows:
        by_controller[str(row["controller_key"])].append(row)
    out = {}
    for controller, rows in sorted(by_controller.items()):
        servable_rows = [r for r in rows if r["servable"]]
        servable_qoe = [float(r["qoe_linear_mean"]) for r in servable_rows]
        high_rows = sum(int(r["high_capacity_row_count"]) for r in rows)
        high_action0 = sum(int(r["high_capacity_action0_count"]) for r in rows)
        out[controller] = {
            "session_count": len(rows),
            "servable_session_count": len(servable_rows),
            "qoe_linear_mean_all": _mean([float(r["qoe_linear_mean"]) for r in rows]),
            "qoe_linear_mean_servable": _mean(servable_qoe),
            # Cola (peor caso): donde el control consciente del riesgo debe ganar.
            "qoe_servable_p05": _percentile(servable_qoe, 0.05),
            "qoe_servable_p10": _percentile(servable_qoe, 0.10),
            "qoe_servable_p25": _percentile(servable_qoe, 0.25),
            "qoe_servable_min": min(servable_qoe) if servable_qoe else 0.0,
            "total_rebuffer_s_all": sum(float(r["total_rebuffer_s"]) for r in rows),
            "total_rebuffer_s_servable": sum(float(r["total_rebuffer_s"]) for r in servable_rows),
            "stall_session_count_servable": sum(1 for r in servable_rows if int(r["stall_count"]) > 0),
            "mean_bitrate_kbps_servable": _mean([float(r["mean_bitrate_kbps"]) for r in servable_rows]),
            "high_capacity_row_count": high_rows,
            "high_capacity_action0_rate": _ratio(high_action0, high_rows),
            "invalid_action_count": sum(int(r["invalid_action_count"]) for r in rows),
            "fallback_count": sum(int(r["fallback_count"]) for r in rows),
            "by_throughput_bucket": _bucket_breakdown(rows, "throughput_bucket"),
        }
    return out


def _percentile(values, q) -> float:
    clean = sorted(float(v) for v in values if math.isfinite(float(v)))
    if not clean:
        return 0.0
    index = min(max(int(round(float(q) * (len(clean) - 1))), 0), len(clean) - 1)
    return clean[index]


def _bucket_breakdown(rows, key) -> Mapping[str, object]:
    by_bucket = defaultdict(list)
    for row in rows:
        by_bucket[str(row.get(key, ""))].append(row)
    return {
        bucket: {
            "session_count": len(items),
            "qoe_linear_mean": _mean([float(r["qoe_linear_mean"]) for r in items]),
            "total_rebuffer_s": sum(float(r["total_rebuffer_s"]) for r in items),
            "mean_bitrate_kbps": _mean([float(r["mean_bitrate_kbps"]) for r in items]),
        }
        for bucket, items in sorted(by_bucket.items())
    }


def _paired_vs_reference(session_rows) -> Mapping[str, object]:
    by_key = {(str(r["window_id"]), str(r["controller_key"])): r for r in session_rows}
    controllers = sorted({str(r["controller_key"]) for r in session_rows} - {REFERENCE_CONTROLLER})
    out = {}
    for controller in controllers:
        all_deltas = []
        for (window_id, key), row in by_key.items():
            if key != controller:
                continue
            baseline = by_key.get((window_id, REFERENCE_CONTROLLER))
            if baseline is None:
                continue
            all_deltas.append(
                {
                    "servable": bool(row["servable"]),
                    "throughput_bucket": str(row.get("throughput_bucket", "")),
                    "variability_bucket": str(row.get("variability_bucket", "")),
                    "qoe_delta": float(row["qoe_linear_mean"]) - float(baseline["qoe_linear_mean"]),
                    "rebuffer_delta_s": float(row["total_rebuffer_s"]) - float(baseline["total_rebuffer_s"]),
                    "bitrate_delta_kbps": float(row["mean_bitrate_kbps"]) - float(baseline["mean_bitrate_kbps"]),
                }
            )
        servable_deltas = [d for d in all_deltas if d["servable"]]
        out[controller] = {
            "paired_session_count": len(all_deltas),
            "servable_paired_session_count": len(servable_deltas),
            "servable_qoe_delta_mean": _mean([d["qoe_delta"] for d in servable_deltas]),
            "servable_rebuffer_delta_s_mean": _mean([d["rebuffer_delta_s"] for d in servable_deltas]),
            "servable_bitrate_delta_kbps_mean": _mean([d["bitrate_delta_kbps"] for d in servable_deltas]),
            "all_qoe_delta_mean": _mean([d["qoe_delta"] for d in all_deltas]),
            "all_rebuffer_delta_s_mean": _mean([d["rebuffer_delta_s"] for d in all_deltas]),
            "servable_by_throughput_bucket": _delta_bucket(servable_deltas, "throughput_bucket"),
            "servable_by_variability": _delta_bucket(servable_deltas, "variability_bucket"),
        }
    return out


def _delta_bucket(deltas, key) -> Mapping[str, object]:
    by_bucket = defaultdict(list)
    for d in deltas:
        by_bucket[str(d.get(key, ""))].append(d)
    return {
        bucket: {
            "count": len(items),
            "qoe_delta_mean": _mean([d["qoe_delta"] for d in items]),
            "rebuffer_delta_s_mean": _mean([d["rebuffer_delta_s"] for d in items]),
        }
        for bucket, items in sorted(by_bucket.items())
    }


def _gates(controller_metrics, paired) -> Mapping[str, object]:
    prudent = controller_metrics.get(MPC_PRUDENTE_CONTROLLER_KEY, {})
    prudent_paired = paired.get(MPC_PRUDENTE_CONTROLLER_KEY, {})
    gates: dict[str, Mapping[str, object]] = {}

    def add(name, passed, observed, threshold):
        gates[name] = {"passed": bool(passed), "observed": observed, "threshold": threshold}

    add("fallback_count", int(prudent.get("fallback_count", 0)) == 0, prudent.get("fallback_count", 0), "== 0")
    add("invalid_action_count", int(prudent.get("invalid_action_count", 0)) == 0, prudent.get("invalid_action_count", 0), "== 0")
    high_rows = int(prudent.get("high_capacity_row_count", 0))
    add(
        "high_capacity_action0_rate",
        high_rows == 0 or float(prudent.get("high_capacity_action0_rate", 0.0)) <= 0.05,
        {"row_count": high_rows, "rate": prudent.get("high_capacity_action0_rate", 0.0)},
        "rate <= 0.05",
    )
    add(
        "servable_qoe_delta_vs_robust_mpc_not_catastrophic",
        float(prudent_paired.get("servable_qoe_delta_mean", 0.0)) >= -0.5,
        prudent_paired.get("servable_qoe_delta_mean", 0.0),
        ">= -0.5 (servable)",
    )
    add(
        "servable_rebuffer_delta_vs_robust_mpc_bounded",
        float(prudent_paired.get("servable_rebuffer_delta_s_mean", 0.0)) <= 0.5,
        prudent_paired.get("servable_rebuffer_delta_s_mean", 0.0),
        "<= +0.5 s (servable)",
    )
    failed = [name for name, gate in gates.items() if not gate["passed"]]
    return {"failed": failed, "gates": gates}


def _is_high_capacity(row) -> bool:
    return (
        float(row.get("measured_throughput_kbps", 0.0)) >= HIGH_CAPACITY_THROUGHPUT_KBPS
        and float(row.get("buffer_s", 0.0)) >= 8.0
        and float(row.get("rebuffer_s", 0.0)) <= 1.0e-9
    )


def _limited(raw_windows, limit):
    if not isinstance(raw_windows, list):
        raise MpcPrudenteEvaluationError("validation_windows must be a list")
    windows = [w for w in raw_windows if isinstance(w, Mapping)]
    return windows[: int(limit)] if limit is not None else windows


def _mean(values) -> float:
    clean = [float(v) for v in values if math.isfinite(float(v))]
    return sum(clean) / float(len(clean)) if clean else 0.0


def _ratio(numerator, denominator) -> float:
    return float(numerator) / float(denominator) if denominator else 0.0

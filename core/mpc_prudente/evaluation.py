"""Diagnóstico closed-loop offline de MPC Prudente sobre el entorno FIEL.

Compara el controller prudente contra `robust_mpc`, `bola` y el Neural-MPC viejo
(regla buffer→cuantil) en el mismo entorno closed-loop, pero con el **ladder fiel**
(tamaños reales VBR). Reporta QoE/rebuffer por controller, deltas emparejados vs
`robust_mpc` (globales y por bucket de variabilidad) y gates anti-colapso.

Usa ventanas de VALIDACIÓN (no eval; eval queda para Phase 6). No es benchmark ni
ranking: es diagnóstico para decidir si la vía prudente merece ir a Phase 6.
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

MPC_PRUDENTE_CLOSED_LOOP_REPORT_SCHEMA_ID = "mpc_prudente_closed_loop_diagnostic_v1"
MPC_PRUDENTE_CLOSED_LOOP_REPORT_FILENAME = "reporte_mpc_prudente_closedloop.json"

REFERENCE_CONTROLLER = "robust_mpc"
HIGH_CAPACITY_THROUGHPUT_KBPS = 2.0 * 4300.0


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
    raw_rows: list[Mapping[str, object]] = []
    skipped: list[Mapping[str, object]] = []
    for window in windows:
        try:
            loaded_trace, _resolved = load_trace_window(window, trace_path_rewrites)
            for controller_key in controller_keys:
                session, rows = _run_session(window, loaded_trace, ladder, controller_key, predictor)
                session_rows.append(session)
                raw_rows.extend(rows)
        except Exception as exc:  # noqa: BLE001 - skips auditados.
            skipped.append(
                {"window_id": str(window.get("window_id")), "reason": type(exc).__name__, "message": str(exc)}
            )

    if not session_rows:
        raise MpcPrudenteEvaluationError("closed-loop diagnostic produced no sessions")

    controller_metrics = _controller_metrics(session_rows, raw_rows)
    paired = _paired_vs_reference(session_rows)
    gates = _gates(controller_metrics, paired)
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
        "window_count": len(windows),
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


def _run_session(window, loaded_trace, ladder, controller_key, predictor):
    network_model = TraceDrivenNetworkModel(loaded_trace, end_policy=END_POLICY_LOOP, max_loops=5)
    env = AbrClosedLoopEnv(ladder=ladder, network_model=network_model)
    controller = _make_controller(controller_key, predictor)
    rows = []
    invalid_actions = 0
    fallback_count = 0
    previous_bitrate_kbps = 0.0
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
        bitrate_kbps = float(step.bitrate_kbps)
        previous_bitrate_kbps = bitrate_kbps
        rows.append(
            {
                "controller_key": controller_key,
                "window_id": str(window["window_id"]),
                "variability_bucket": str(window.get("variability_bucket", "")),
                "throughput_bucket": str(window.get("throughput_bucket", "")),
                "action": int(action),
                "bitrate_kbps": bitrate_kbps,
                "buffer_s": float(step.buffer_s_before),
                "measured_throughput_kbps": float(step.measured_throughput_bps) / 1000.0,
                "rebuffer_s": float(step.rebuffer_s),
                "qoe_linear_reward": float(step.reward_n),
            }
        )
    rewards = [float(r["qoe_linear_reward"]) for r in rows]
    session = {
        "controller_key": controller_key,
        "window_id": str(window["window_id"]),
        "variability_bucket": str(window.get("variability_bucket", "")),
        "throughput_bucket": str(window.get("throughput_bucket", "")),
        "qoe_linear_mean": _mean(rewards),
        "total_rebuffer_s": sum(float(r["rebuffer_s"]) for r in rows),
        "stall_count": sum(1 for r in rows if float(r["rebuffer_s"]) > 1.0e-9),
        "mean_bitrate_kbps": _mean([float(r["bitrate_kbps"]) for r in rows]),
        "action0_rate": _ratio(sum(1 for r in rows if int(r["action"]) == 0), len(rows)),
        "invalid_action_count": invalid_actions,
        "fallback_count": fallback_count,
    }
    return session, rows


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


def _controller_metrics(session_rows, raw_rows) -> Mapping[str, object]:
    by_controller = defaultdict(list)
    for row in session_rows:
        by_controller[str(row["controller_key"])].append(row)
    raw_by_controller = defaultdict(list)
    for row in raw_rows:
        raw_by_controller[str(row["controller_key"])].append(row)
    out = {}
    for controller, rows in sorted(by_controller.items()):
        raw = raw_by_controller[controller]
        high = [r for r in raw if _is_high_capacity(r)]
        out[controller] = {
            "session_count": len(rows),
            "qoe_linear_mean": _mean([float(r["qoe_linear_mean"]) for r in rows]),
            "total_rebuffer_s": sum(float(r["total_rebuffer_s"]) for r in rows),
            "stall_count": sum(int(r["stall_count"]) for r in rows),
            "mean_bitrate_kbps": _mean([float(r["mean_bitrate_kbps"]) for r in rows]),
            "action0_rate": _ratio(sum(1 for r in raw if int(r["action"]) == 0), len(raw)),
            "high_capacity_row_count": len(high),
            "high_capacity_action0_rate": _ratio(sum(1 for r in high if int(r["action"]) == 0), len(high)),
            "invalid_action_count": sum(int(r["invalid_action_count"]) for r in rows),
            "fallback_count": sum(int(r["fallback_count"]) for r in rows),
            "action_histogram": dict(sorted(Counter(str(int(r["action"])) for r in raw).items())),
        }
    return out


def _paired_vs_reference(session_rows) -> Mapping[str, object]:
    by_key = {(str(r["window_id"]), str(r["controller_key"])): r for r in session_rows}
    controllers = sorted({str(r["controller_key"]) for r in session_rows} - {REFERENCE_CONTROLLER})
    out = {}
    for controller in controllers:
        deltas = []
        for (window_id, key), row in by_key.items():
            if key != controller:
                continue
            baseline = by_key.get((window_id, REFERENCE_CONTROLLER))
            if baseline is None:
                continue
            deltas.append(
                {
                    "variability_bucket": str(row.get("variability_bucket", "")),
                    "qoe_delta": float(row["qoe_linear_mean"]) - float(baseline["qoe_linear_mean"]),
                    "rebuffer_delta_s": float(row["total_rebuffer_s"]) - float(baseline["total_rebuffer_s"]),
                    "bitrate_delta_kbps": float(row["mean_bitrate_kbps"]) - float(baseline["mean_bitrate_kbps"]),
                }
            )
        by_bucket = defaultdict(list)
        for d in deltas:
            by_bucket["variable" if "variable" in d["variability_bucket"] else "estable"].append(d)
        out[controller] = {
            "paired_session_count": len(deltas),
            "qoe_delta_mean": _mean([d["qoe_delta"] for d in deltas]),
            "rebuffer_delta_s_mean": _mean([d["rebuffer_delta_s"] for d in deltas]),
            "bitrate_delta_kbps_mean": _mean([d["bitrate_delta_kbps"] for d in deltas]),
            "by_variability": {
                bucket: {
                    "count": len(items),
                    "qoe_delta_mean": _mean([d["qoe_delta"] for d in items]),
                    "rebuffer_delta_s_mean": _mean([d["rebuffer_delta_s"] for d in items]),
                }
                for bucket, items in sorted(by_bucket.items())
            },
        }
    return out


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
        "qoe_delta_vs_robust_mpc_not_catastrophic",
        float(prudent_paired.get("qoe_delta_mean", 0.0)) >= -2.0,
        prudent_paired.get("qoe_delta_mean", 0.0),
        ">= -2.0",
    )
    add(
        "rebuffer_delta_vs_robust_mpc_bounded",
        float(prudent_paired.get("rebuffer_delta_s_mean", 0.0)) <= 1.0,
        prudent_paired.get("rebuffer_delta_s_mean", 0.0),
        "<= +1.0 s",
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

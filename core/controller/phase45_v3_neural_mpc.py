from __future__ import annotations

import math
import time
from collections.abc import Mapping, Sequence
from numbers import Real
from pathlib import Path

import torch

from core.controller.base import BaseController
from core.controller.contract import quantize_rate_to_level
from core.controller.neural_abr_diagnostics import (
    NeuralAbrDiagnostics,
    augment_feedback_with_neural_diagnostics,
    stable_reason,
)
from core.controller.neural_abr_lite import DEFAULT_MAX_INFERENCE_LATENCY_MS
from core.controller.neural_abr_runtime_features import NeuralAbrRuntimeFeatureBuilder, RuntimeFeatureError
from core.controller.neural_abr_safety import NeuralAbrSafetyError, safe_action_to_rate
from core.controller.robust_mpc import RobustMpcController
from core.neural_abr.artifacts import read_json
from core.neural_abr.content_ladder import ContentLadder, Representation
from core.phase45_v3.abr_closed_loop_env import (
    PHASE45_V3_DEFAULT_MAX_BUFFER_S,
    AbrClosedLoopState,
)
from core.phase45_v3.neural_mpc_bundle import (
    NEURAL_MPC_BUNDLE_INFERENCE_CONTRACT_FILENAME,
    NEURAL_MPC_BUNDLE_MODEL_CARD_FILENAME,
    NEURAL_MPC_BUNDLE_MODEL_CONFIG_FILENAME,
    NEURAL_MPC_BUNDLE_MODEL_FILENAME,
    NEURAL_MPC_BUNDLE_NORMALIZATION_FILENAME,
    validate_phase45_v3_neural_mpc_bundle_dir,
)
from core.phase45_v3.neural_mpc_controller import (
    DEFAULT_NEURAL_MPC_HORIZON,
    NEURAL_MPC_CONTROLLER_KEY,
    NEURAL_MPC_V2_CONTROLLER_KEY,
    plan_neural_mpc_action,
)
from core.phase45_v3.throughput_quantile_dataset import harmonic_mean_bps
from core.phase45_v3.throughput_quantile_model import (
    PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY,
    ThroughputQuantilePredictor,
)


DEFAULT_NEURAL_MPC_BUNDLE_DIR = "/home/daniel/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1"
DEFAULT_NEURAL_MPC_V2_BUNDLE_DIR = "/home/daniel/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v2"
DEFAULT_FALLBACK_CONTROLLER = "robust_mpc"


class Phase45V3NeuralMpcRuntimeError(ValueError):
    def __init__(self, reason: str, message: str) -> None:
        super().__init__(message)
        self.reason = stable_reason(reason)


class Phase45V3NeuralMpcRuntimeBundle:
    def __init__(self, bundle_dir: object, verify_hashes: bool = True) -> None:
        validation = _validate_bundle(bundle_dir, verify_hashes=bool(verify_hashes))
        self.bundle_dir = Path(validation["bundle_dir"])
        self.manifest = dict(validation["manifest"])
        self.model_config = dict(read_json(self.bundle_dir / NEURAL_MPC_BUNDLE_MODEL_CONFIG_FILENAME))
        self.normalization = dict(read_json(self.bundle_dir / NEURAL_MPC_BUNDLE_NORMALIZATION_FILENAME))
        self.inference_contract = read_json(self.bundle_dir / NEURAL_MPC_BUNDLE_INFERENCE_CONTRACT_FILENAME)
        self.model_card = read_json(self.bundle_dir / NEURAL_MPC_BUNDLE_MODEL_CARD_FILENAME)
        self.quantiles = tuple(float(value) for value in self.model_config["quantiles"])
        self.horizon_segments = int(self.model_config.get("horizon_segments", DEFAULT_NEURAL_MPC_HORIZON))
        self.context_mean = tuple(float(value) for value in self.normalization["context_mean"])
        self.context_std = tuple(float(value) for value in self.normalization["context_std"])
        self.model = self._load_model()
        self.model.eval()

    def predict(self, state: AbrClosedLoopState, ladder: ContentLadder) -> tuple[tuple[float, ...], ...]:
        from core.neural_abr.features import build_context_features, flatten_context_features

        context = flatten_context_features(build_context_features(state, ladder))
        if len(context) != len(self.context_mean) or len(context) != len(self.context_std):
            raise Phase45V3NeuralMpcRuntimeError("model_config_invalid", "context normalization width mismatch")
        normalized = [
            (float(value) - float(self.context_mean[index])) / max(float(self.context_std[index]), 1.0e-9)
            for index, value in enumerate(context)
        ]
        started = time.perf_counter()
        tensor = torch.tensor([normalized], dtype=torch.float32)
        try:
            with torch.no_grad():
                prediction_log_ratio = self.model(tensor).detach().cpu()[0]
        except Exception as exc:
            raise Phase45V3NeuralMpcRuntimeError("inference_failed", "model forward failed") from exc
        self.last_latency_ms = (time.perf_counter() - started) * 1000.0
        base_tp = harmonic_mean_bps(state.throughput_history_bps)
        rows = []
        for horizon_index in range(self.horizon_segments):
            row = []
            for quantile_index in range(len(self.quantiles)):
                log_ratio = float(prediction_log_ratio[horizon_index, quantile_index])
                if not math.isfinite(log_ratio):
                    raise Phase45V3NeuralMpcRuntimeError("inference_failed", "non-finite throughput prediction")
                clipped = max(min(log_ratio, math.log(4.0)), math.log(0.15))
                predicted = float(base_tp) * math.exp(clipped)
                row.append(min(max(predicted, 0.15 * float(base_tp)), 4.0 * float(base_tp)))
            rows.append(tuple(sorted(row)))
        return tuple(rows)

    def _load_model(self) -> ThroughputQuantilePredictor:
        checkpoint = _torch_load_weights_only(self.bundle_dir / NEURAL_MPC_BUNDLE_MODEL_FILENAME)
        if not isinstance(checkpoint, Mapping):
            raise Phase45V3NeuralMpcRuntimeError("model_config_invalid", "checkpoint must be a mapping")
        if checkpoint.get("model_key") != PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY:
            raise Phase45V3NeuralMpcRuntimeError("model_config_invalid", "checkpoint model_key is invalid")
        model = ThroughputQuantilePredictor(
            input_dim=int(self.model_config["input_dim"]),
            horizon_segments=self.horizon_segments,
            quantiles=self.quantiles,
            hidden_sizes=tuple(int(value) for value in self.model_config["hidden_sizes"]),
        )
        state_dict = checkpoint.get("model_state_dict")
        if not isinstance(state_dict, Mapping):
            raise Phase45V3NeuralMpcRuntimeError("model_config_invalid", "checkpoint missing model_state_dict")
        try:
            model.load_state_dict(state_dict)
        except Exception as exc:
            raise Phase45V3NeuralMpcRuntimeError("model_config_invalid", "model state_dict incompatible") from exc
        return model


class Phase45V3NeuralMpcController(BaseController):
    name = NEURAL_MPC_CONTROLLER_KEY

    def __init__(
        self,
        bundle_dir: object | None = None,
        fallback_controller: str = DEFAULT_FALLBACK_CONTROLLER,
        verify_hashes: bool = True,
        max_inference_latency_ms: float = DEFAULT_MAX_INFERENCE_LATENCY_MS,
        diagnostic_only: bool = False,
        **_unused,
    ) -> None:
        super().__init__()
        self.name = NEURAL_MPC_CONTROLLER_KEY
        self.controller_key = NEURAL_MPC_CONTROLLER_KEY
        self.bundle_dir = str(bundle_dir or DEFAULT_NEURAL_MPC_BUNDLE_DIR)
        self.verify_hashes = _as_bool(verify_hashes, True)
        self.max_inference_latency_ms = _positive_float(
            max_inference_latency_ms,
            DEFAULT_MAX_INFERENCE_LATENCY_MS,
        )
        self.diagnostic_only = bool(diagnostic_only)
        self.feature_builder = NeuralAbrRuntimeFeatureBuilder()
        self.fallback_controller_key = str(fallback_controller or DEFAULT_FALLBACK_CONTROLLER)
        self.fallback_controller = RobustMpcController()
        self._bundle: Phase45V3NeuralMpcRuntimeBundle | None = None
        self._bundle_load_attempted = False
        self._bundle_load_error_reason = ""
        self._diagnostics = self._base_diagnostics()
        self.last_metrics: dict[str, object] = {}
        self.last_decision = None

    def augment_feedback(self, feedback, context=None):
        return augment_feedback_with_neural_diagnostics(feedback, self._diagnostics)

    def get_neural_diagnostics(self):
        return self._diagnostics.to_feedback_fields()

    def calcControlAction(self):
        feedback = self.feedback or {}
        diagnostics = self._base_diagnostics()
        try:
            payload = self.feature_builder.build(feedback)
            diagnostics.feature_vector_ok = 1
            diagnostics.feature_schema_ok = 1
            diagnostics.action_mask_valid_count = payload.valid_action_count
            ladder = _ladder_from_payload(payload.rates_Bps, feedback)
            state = _state_from_payload(payload.context_features, payload.rates_Bps, feedback)
        except RuntimeFeatureError as exc:
            diagnostics.missing_features = ",".join(exc.missing_features)
            self._diagnostics = diagnostics
            return self._fallback_decision(exc.reason, diagnostics, None)
        except Exception:
            self._diagnostics = diagnostics
            return self._fallback_decision("feature_build_failed", diagnostics, None)

        try:
            bundle = self._ensure_bundle_loaded(diagnostics)
        except Phase45V3NeuralMpcRuntimeError as exc:
            self._diagnostics = diagnostics
            return self._fallback_decision(exc.reason, diagnostics, payload)

        try:
            prediction = bundle.predict(state, ladder)
            decision = plan_neural_mpc_action(
                state=state,
                ladder=ladder,
                predicted_bps_by_horizon_quantile=prediction,
                quantiles=bundle.quantiles,
                horizon_segments=bundle.horizon_segments,
                action_mask=payload.action_mask,
            )
            latency_ms = float(getattr(bundle, "last_latency_ms", 0.0) or 0.0)
            diagnostics.inference_ms = "{0:.6f}".format(latency_ms)
            diagnostics.raw_action = str(int(decision.action))
            diagnostics.raw_rate_Bps = str(float(ladder.bitrate_bps(int(decision.action))) / 8.0)
            if latency_ms > self.max_inference_latency_ms:
                return self._fallback_decision("inference_timeout", diagnostics, payload)
            safe_action, safe_rate = safe_action_to_rate(int(decision.action), payload.action_mask, payload.rates_Bps)
        except Phase45V3NeuralMpcRuntimeError as exc:
            self._diagnostics = diagnostics
            return self._fallback_decision(exc.reason, diagnostics, payload)
        except NeuralAbrSafetyError as exc:
            diagnostics.safety_intervened = 1
            diagnostics.invalid_action_detected = 1 if exc.reason == "selected_masked_action" else 0
            self._diagnostics = diagnostics
            return self._fallback_decision(exc.reason, diagnostics, payload)
        except Exception:
            self._diagnostics = diagnostics
            return self._fallback_decision("inference_failed", diagnostics, payload)

        diagnostics.safe_action = str(safe_action)
        diagnostics.safe_rate_Bps = str(safe_rate)
        diagnostics.selected_representation_index = str(safe_action)
        diagnostics.valid_action = 1
        diagnostics.fallback_reason = "success_neural"
        diagnostics.fallback_used = 0
        self.last_decision = decision
        self._finish_success(float(safe_rate), diagnostics)
        return float(safe_rate)

    def quantizeRate(self, rate):
        rates = _rates_from_feedback(self.feedback or {})
        if rates:
            try:
                return quantize_rate_to_level(rate, rates)
            except ValueError:
                return 0
        return super().quantizeRate(rate)

    def _ensure_bundle_loaded(self, diagnostics: NeuralAbrDiagnostics) -> Phase45V3NeuralMpcRuntimeBundle:
        if self._bundle is not None:
            diagnostics.bundle_loaded = 1
            diagnostics.bundle_schema_ok = 1
            diagnostics.bundle_hash_ok = 1
            diagnostics.feature_schema_ok = 1
            return self._bundle
        if self._bundle_load_attempted and self._bundle_load_error_reason:
            raise Phase45V3NeuralMpcRuntimeError(self._bundle_load_error_reason, "bundle load failed previously")
        try:
            self._bundle = Phase45V3NeuralMpcRuntimeBundle(self.bundle_dir, verify_hashes=self.verify_hashes)
        except Phase45V3NeuralMpcRuntimeError as exc:
            self._bundle_load_attempted = True
            self._bundle_load_error_reason = stable_reason(exc.reason)
            _apply_load_error_diagnostics(diagnostics, exc.reason)
            raise
        self._bundle_load_attempted = True
        diagnostics.bundle_loaded = 1
        diagnostics.bundle_schema_ok = 1
        diagnostics.bundle_hash_ok = 1
        diagnostics.feature_schema_ok = 1
        return self._bundle

    def _fallback_decision(self, reason: str, diagnostics: NeuralAbrDiagnostics, payload) -> float:
        diagnostics.fallback_used = 1
        diagnostics.fallback_reason = stable_reason(reason)
        if payload is not None:
            diagnostics.action_mask_valid_count = payload.valid_action_count
        try:
            self.fallback_controller.setPlayerFeedback(self.feedback or {})
            rate = float(self.fallback_controller.calcControlAction())
            if payload is not None:
                action = quantize_rate_to_level(rate, payload.rates_Bps)
                if action < len(payload.action_mask) and payload.action_mask[action]:
                    rate = float(payload.rates_Bps[action])
                else:
                    action, rate = _lowest_valid_rate(payload)
            else:
                action = self.quantizeRate(rate)
        except Exception:
            action, rate = _lowest_valid_rate(payload)
        diagnostics.safe_action = "" if action is None else str(action)
        diagnostics.safe_rate_Bps = str(float(rate))
        diagnostics.selected_representation_index = diagnostics.safe_action
        diagnostics.valid_action = 1 if action is not None else 0
        self._finish_success(float(rate), diagnostics)
        return float(rate)

    def _finish_success(self, rate: float, diagnostics: NeuralAbrDiagnostics) -> None:
        self.setIdleDuration(0.0)
        self.setControlAction(float(rate))
        self._diagnostics = diagnostics
        self.last_metrics = diagnostics.to_feedback_fields()

    def _base_diagnostics(self) -> NeuralAbrDiagnostics:
        return NeuralAbrDiagnostics(
            controller_key=self.controller_key,
            model_label="Phase45 v3 Neural Throughput-Calibrated MPC",
            bundle_path=self.bundle_dir,
            bundle_configured=1 if self.bundle_dir.strip() else 0,
            diagnostic_only=1 if self.diagnostic_only else 0,
        )


class Phase45V3NeuralMpcV2Controller(Phase45V3NeuralMpcController):
    name = NEURAL_MPC_V2_CONTROLLER_KEY

    def __init__(self, bundle_dir: object | None = None, **kwargs) -> None:
        super().__init__(bundle_dir=bundle_dir or DEFAULT_NEURAL_MPC_V2_BUNDLE_DIR, **kwargs)
        self.name = NEURAL_MPC_V2_CONTROLLER_KEY
        self.controller_key = NEURAL_MPC_V2_CONTROLLER_KEY


def _validate_bundle(bundle_dir: object, verify_hashes: bool) -> Mapping[str, object]:
    if bundle_dir is None or not str(bundle_dir).strip():
        raise Phase45V3NeuralMpcRuntimeError("missing_bundle_dir", "bundle_dir is required")
    try:
        return validate_phase45_v3_neural_mpc_bundle_dir(bundle_dir, verify_hashes=verify_hashes)
    except Exception as exc:
        text = str(exc).lower()
        if "sha256 mismatch" in text or "size mismatch" in text:
            raise Phase45V3NeuralMpcRuntimeError("bundle_hash_invalid", str(exc)) from exc
        if "does not exist" in text or "missing" in text or "must be outside" in text:
            raise Phase45V3NeuralMpcRuntimeError("missing_bundle_dir", str(exc)) from exc
        raise Phase45V3NeuralMpcRuntimeError("bundle_schema_invalid", str(exc)) from exc


def _torch_load_weights_only(path: Path) -> object:
    try:
        return torch.load(path, map_location="cpu", weights_only=True)
    except TypeError as exc:
        raise Phase45V3NeuralMpcRuntimeError("safe_torch_load_unavailable", "torch.load weights_only is unavailable") from exc
    except Exception as exc:
        raise Phase45V3NeuralMpcRuntimeError("bundle_load_failed", "torch.load failed") from exc


def _ladder_from_payload(rates_Bps: Sequence[float], feedback: Mapping[str, object]) -> ContentLadder:
    segment_duration_s = _positive_float(feedback.get("fragment_duration"), 4.0)
    total_segments = _positive_int(feedback.get("total_segments"), 30)
    representations = tuple(
        Representation(representation_index=index, bitrate_bps=max(1, int(round(float(rate) * 8.0))))
        for index, rate in enumerate(rates_Bps)
    )
    return ContentLadder(
        representations=representations,
        segment_duration_s=segment_duration_s,
        segment_count=total_segments,
        max_buffer_s=PHASE45_V3_DEFAULT_MAX_BUFFER_S,
    )


def _state_from_payload(
    context_features: Mapping[str, object],
    rates_Bps: Sequence[float],
    feedback: Mapping[str, object],
) -> AbrClosedLoopState:
    segment_index = min(
        max(_positive_int(feedback.get("segment_index"), 0, allow_zero=True), 0),
        max(_positive_int(feedback.get("total_segments"), 30) - 1, 0),
    )
    level = _positive_int(feedback.get("level"), 0, allow_zero=True)
    last_representation_index = min(max(level, 0), max(len(rates_Bps) - 1, 0))
    return AbrClosedLoopState(
        segment_index=segment_index,
        buffer_s=float(context_features.get("buffer_s", 0.0) or 0.0),
        last_representation_index=last_representation_index,
        throughput_history_bps=_positive_history(context_features.get("throughput_history_bps")),
        download_time_history_s=_positive_history(context_features.get("download_time_history_s")),
        recent_rebuffer_s=float(context_features.get("recent_rebuffer_s", 0.0) or 0.0),
        recent_switch_abs=float(context_features.get("recent_switch_abs", 0.0) or 0.0),
        network_time_s=0.0,
        total_segments=_positive_int(feedback.get("total_segments"), 30),
    )


def _positive_history(value: object) -> tuple[float, ...]:
    if not isinstance(value, (list, tuple)):
        return ()
    parsed = []
    for item in value:
        number = _finite_float(item)
        if number is not None and number > 0.0:
            parsed.append(float(number))
    return tuple(parsed)


def _lowest_valid_rate(payload) -> tuple[int | None, float]:
    if payload is None:
        rates = _rates_from_feedback({})
        return (0, float(rates[0])) if rates else (None, 0.0)
    for index, valid in enumerate(payload.action_mask):
        if valid:
            return int(index), float(payload.rates_Bps[index])
    return None, 0.0


def _rates_from_feedback(feedback: Mapping[str, object]) -> tuple[float, ...]:
    raw_rates = feedback.get("rates", ())
    if isinstance(raw_rates, (str, bytes)):
        return ()
    try:
        values = tuple(raw_rates)  # type: ignore[arg-type]
    except TypeError:
        return ()
    rates = []
    for value in values:
        parsed = _finite_float(value)
        if parsed is None or parsed <= 0.0:
            return ()
        rates.append(float(parsed))
    return tuple(rates)


def _apply_load_error_diagnostics(diagnostics: NeuralAbrDiagnostics, reason: str) -> None:
    stable = stable_reason(reason)
    if stable in {"bundle_load_failed", "safe_torch_load_unavailable", "model_config_invalid"}:
        diagnostics.bundle_schema_ok = 1
        diagnostics.bundle_hash_ok = 1
        diagnostics.feature_schema_ok = 1
    elif stable == "bundle_hash_invalid":
        diagnostics.bundle_schema_ok = 1
        diagnostics.bundle_hash_ok = 0


def _positive_float(value: object, default: float) -> float:
    parsed = _finite_float(value)
    if parsed is None or parsed <= 0.0:
        return float(default)
    return float(parsed)


def _positive_int(value: object, default: int, *, allow_zero: bool = False) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return int(default)
    if parsed < 0 or (parsed == 0 and not allow_zero):
        return int(default)
    return int(parsed)


def _finite_float(value: object) -> float | None:
    if isinstance(value, bool) or not isinstance(value, Real):
        return None
    parsed = float(value)
    if not math.isfinite(parsed):
        return None
    return parsed


def _as_bool(value: object, default: bool) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"true", "yes", "1", "on"}:
            return True
        if lowered in {"false", "no", "0", "off"}:
            return False
    return bool(default)


__all__ = ["Phase45V3NeuralMpcController", "Phase45V3NeuralMpcRuntimeBundle"]

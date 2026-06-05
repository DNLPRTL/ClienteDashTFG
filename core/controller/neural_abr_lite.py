from __future__ import annotations

import math
from collections.abc import Mapping, Sequence
from numbers import Real

from .base import BaseController
from .bba import BbaController
from .bola import BolaController
from .contract import quantize_rate_to_level
from .mpc import MpcController
from .neural_abr_diagnostics import (
    NeuralAbrDiagnostics,
    augment_feedback_with_neural_diagnostics,
    stable_reason,
)
from .neural_abr_loader import NeuralAbrRuntimeBundleError, load_neural_abr_runtime_bundle
from .neural_abr_runtime_features import NeuralAbrRuntimeFeatureBuilder, RuntimeFeatureError, RuntimeFeaturePayload
from .neural_abr_safety import NeuralAbrSafetyError, lowest_valid_action, safe_action_to_rate
from .rate_based import RateBasedController
from .robust_mpc import RobustMpcController
from .sanity_rate import MinRateController


DEFAULT_FALLBACK_CONTROLLER = "robust_mpc"
DEFAULT_MAX_INFERENCE_LATENCY_MS = 50.0


class NeuralAbrLiteController(BaseController):
    name = "neural_abr_lite"

    def __init__(
        self,
        controller_key: str,
        model_label: str,
        expected_teacher: str,
        bundle_dir=None,
        fallback_controller=DEFAULT_FALLBACK_CONTROLLER,
        verify_hashes=True,
        max_inference_latency_ms=DEFAULT_MAX_INFERENCE_LATENCY_MS,
        diagnostic_only=True,
        **_unused,
    ):
        super().__init__()
        self.name = str(controller_key)
        self.controller_key = str(controller_key)
        self.model_label = str(model_label)
        self.expected_teacher = str(expected_teacher)
        self.bundle_dir = "" if bundle_dir is None else str(bundle_dir)
        self.verify_hashes = _as_bool(verify_hashes, True)
        self.max_inference_latency_ms = _positive_float(
            max_inference_latency_ms,
            DEFAULT_MAX_INFERENCE_LATENCY_MS,
        )
        self.diagnostic_only = bool(diagnostic_only)
        self.feature_builder = NeuralAbrRuntimeFeatureBuilder()
        self.fallback_controller_key = str(fallback_controller or DEFAULT_FALLBACK_CONTROLLER)
        self.fallback_controller = _create_classical_fallback(self.fallback_controller_key)
        self._bundle = None
        self._bundle_load_attempted = False
        self._bundle_load_error_reason = ""
        self.last_metrics = {}
        self._diagnostics = self._base_diagnostics()

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
        except RuntimeFeatureError as exc:
            diagnostics.missing_features = ",".join(exc.missing_features)
            self._diagnostics = diagnostics
            return self._fallback_decision(
                reason=exc.reason,
                diagnostics=diagnostics,
                payload=None,
            )

        if payload.valid_action_count == 1:
            action = lowest_valid_action(payload.action_mask)
            if action is None:
                return self._fallback_decision("all_actions_invalid", diagnostics, payload)
            rate = float(payload.rates_Bps[action])
            diagnostics.raw_action = str(action)
            diagnostics.raw_rate_Bps = str(rate)
            diagnostics.safe_action = str(action)
            diagnostics.safe_rate_Bps = str(rate)
            diagnostics.selected_representation_index = str(action)
            diagnostics.valid_action = 1
            diagnostics.fallback_reason = "single_representation"
            self._finish_success(rate, diagnostics)
            return rate

        try:
            bundle = self._ensure_bundle_loaded(diagnostics)
        except NeuralAbrRuntimeBundleError as exc:
            self._diagnostics = diagnostics
            return self._fallback_decision(exc.reason, diagnostics, payload)

        try:
            result = bundle.score(payload.context_features, payload.candidate_features, payload.action_mask)
            latency_ms = float(result.get("latency_ms", 0.0) or 0.0)
            raw_action = int(result["selected_representation_index"])
            diagnostics.inference_ms = "{0:.6f}".format(latency_ms)
            _set_raw_action_diagnostics(diagnostics, raw_action, payload)
            if latency_ms > self.max_inference_latency_ms:
                return self._fallback_decision("inference_timeout", diagnostics, payload)
            safe_action, safe_rate = safe_action_to_rate(raw_action, payload.action_mask, payload.rates_Bps)
        except NeuralAbrRuntimeBundleError as exc:
            if exc.reason == "nan_inf_scores":
                diagnostics.nan_inf_detected = 1
            if exc.reason == "selected_masked_action":
                diagnostics.invalid_action_detected = 1
            self._diagnostics = diagnostics
            return self._fallback_decision(_runtime_inference_reason(exc.reason), diagnostics, payload)
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
        self._finish_success(safe_rate, diagnostics)
        return safe_rate

    def quantizeRate(self, rate):
        rates = _basic_rates(self.feedback or {})
        if rates:
            try:
                return quantize_rate_to_level(rate, rates)
            except ValueError:
                return 0
        return super().quantizeRate(rate)

    def _ensure_bundle_loaded(self, diagnostics: NeuralAbrDiagnostics):
        if self._bundle is not None:
            diagnostics.bundle_loaded = 1
            diagnostics.bundle_schema_ok = 1
            diagnostics.bundle_hash_ok = 1
            diagnostics.feature_schema_ok = 1
            return self._bundle
        if self._bundle_load_attempted and self._bundle_load_error_reason:
            raise NeuralAbrRuntimeBundleError(self._bundle_load_error_reason, "bundle load failed previously")
        try:
            self._bundle = load_neural_abr_runtime_bundle(
                self.bundle_dir,
                expected_teacher=self.expected_teacher,
                verify_hashes=self.verify_hashes,
            )
        except NeuralAbrRuntimeBundleError as exc:
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

    def _fallback_decision(
        self,
        reason: str,
        diagnostics: NeuralAbrDiagnostics,
        payload: RuntimeFeaturePayload | None,
    ):
        fallback_reason = stable_reason(reason)
        diagnostics.fallback_used = 1
        diagnostics.fallback_reason = fallback_reason
        if payload is not None:
            diagnostics.action_mask_valid_count = payload.valid_action_count
        else:
            rates, mask = _basic_rates_and_mask(self.feedback or {})
            payload = _fallback_payload(rates, mask)
            diagnostics.action_mask_valid_count = payload.valid_action_count if payload is not None else 0

        try:
            selected_action, selected_rate = self._classical_fallback_action(payload)
        except Exception:
            fallback_reason = "fallback_controller_failed"
            diagnostics.fallback_reason = fallback_reason
            selected_action, selected_rate = _lowest_rate_from_payload(payload)

        diagnostics.safe_action = "" if selected_action is None else str(selected_action)
        diagnostics.safe_rate_Bps = "" if selected_rate is None else str(float(selected_rate))
        diagnostics.selected_representation_index = diagnostics.safe_action
        diagnostics.valid_action = 1 if selected_action is not None and selected_rate is not None else 0
        rate = float(selected_rate) if selected_rate is not None else 0.0
        self._finish_success(rate, diagnostics)
        return rate

    def _classical_fallback_action(self, payload: RuntimeFeaturePayload | None):
        if payload is None or not payload.rates_Bps or not any(payload.action_mask):
            return None, 0.0
        if self.fallback_controller is not None:
            self.fallback_controller.setPlayerFeedback(self.feedback or {})
            rate = float(self.fallback_controller.calcControlAction())
            action = quantize_rate_to_level(rate, payload.rates_Bps)
            if action < len(payload.action_mask) and payload.action_mask[action]:
                return action, float(payload.rates_Bps[action])
        return _lowest_rate_from_payload(payload)

    def _finish_success(self, rate: float, diagnostics: NeuralAbrDiagnostics) -> None:
        self.setIdleDuration(0.0)
        self.setControlAction(float(rate))
        self._diagnostics = diagnostics
        self.last_metrics = diagnostics.to_feedback_fields()

    def _base_diagnostics(self) -> NeuralAbrDiagnostics:
        return NeuralAbrDiagnostics(
            controller_key=self.controller_key,
            model_label=self.model_label,
            bundle_path=self.bundle_dir,
            bundle_configured=1 if self.bundle_dir.strip() else 0,
            diagnostic_only=1,
        )


class NeuralAbrLiteRobustMpcController(NeuralAbrLiteController):
    def __init__(self, **kwargs):
        super().__init__(
            controller_key="neural_abr_lite_robust_mpc",
            model_label="NeuralABR-Lite robust_mpc",
            expected_teacher="robust_mpc",
            **kwargs,
        )


class NeuralAbrLiteTeacherHibridoController(NeuralAbrLiteController):
    def __init__(self, **kwargs):
        super().__init__(
            controller_key="neural_abr_lite_teacher_hibrido",
            model_label="NeuralABR-Lite teacher_hibrido",
            expected_teacher="teacher_hibrido",
            **kwargs,
        )


def _create_classical_fallback(key: str):
    factories = {
        "min_rate": MinRateController,
        "rate_based": RateBasedController,
        "bba": BbaController,
        "bola": BolaController,
        "mpc": MpcController,
        "robust_mpc": RobustMpcController,
    }
    factory = factories.get(str(key), RobustMpcController)
    return factory()


def _apply_load_error_diagnostics(diagnostics: NeuralAbrDiagnostics, reason: str) -> None:
    stable = stable_reason(reason)
    if stable in {
        "bundle_load_failed",
        "safe_torch_load_unavailable",
        "model_config_invalid",
        "expected_teacher_mismatch",
    }:
        diagnostics.bundle_schema_ok = 1
        diagnostics.bundle_hash_ok = 1
        diagnostics.feature_schema_ok = 1
    elif stable == "feature_schema_invalid":
        diagnostics.bundle_schema_ok = 1
        diagnostics.bundle_hash_ok = 1
        diagnostics.feature_schema_ok = 0
    elif stable == "bundle_hash_invalid":
        diagnostics.bundle_schema_ok = 1
        diagnostics.bundle_hash_ok = 0


def _set_raw_action_diagnostics(
    diagnostics: NeuralAbrDiagnostics,
    raw_action: int,
    payload: RuntimeFeaturePayload,
) -> None:
    diagnostics.raw_action = str(raw_action)
    if 0 <= raw_action < len(payload.rates_Bps):
        diagnostics.raw_rate_Bps = str(float(payload.rates_Bps[raw_action]))


def _runtime_inference_reason(reason: str) -> str:
    if reason == "selected_masked_action":
        return "selected_masked_action"
    return "inference_failed"


def _lowest_rate_from_payload(payload: RuntimeFeaturePayload | None):
    if payload is None:
        return None, 0.0
    action = lowest_valid_action(payload.action_mask)
    if action is None:
        return None, 0.0
    return action, float(payload.rates_Bps[action])


def _fallback_payload(rates: Sequence[float], mask: Sequence[bool]) -> RuntimeFeaturePayload | None:
    if not rates:
        return None
    return RuntimeFeaturePayload(
        context_features={},
        candidate_features=(),
        action_mask=tuple(mask),
        rates_Bps=tuple(rates),
        valid_action_count=sum(1 for valid in mask if valid),
    )


def _basic_rates_and_mask(feedback: Mapping[str, object]) -> tuple[tuple[float, ...], tuple[bool, ...]]:
    rates = _basic_rates(feedback)
    if not rates:
        return (), ()
    max_level = _int_or_default(feedback.get("max_level"), len(rates) - 1)
    max_level = min(max_level, len(rates) - 1)
    mask = tuple(index <= max_level for index in range(len(rates)))
    if not any(mask):
        return rates, tuple(False for _ in rates)
    return rates, mask


def _basic_rates(feedback: Mapping[str, object]) -> tuple[float, ...]:
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


def _positive_float(value: object, default: float) -> float:
    parsed = _finite_float(value)
    if parsed is None or parsed <= 0.0:
        return float(default)
    return float(parsed)


def _finite_float(value: object) -> float | None:
    if isinstance(value, bool) or not isinstance(value, Real):
        return None
    parsed = float(value)
    if not math.isfinite(parsed):
        return None
    return parsed


def _int_or_default(value: object, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return int(default)


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


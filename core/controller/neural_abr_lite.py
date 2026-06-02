"""Guarded NeuralABR-Lite scorer controller."""

from __future__ import annotations

import math
from numbers import Real
from typing import Mapping, Sequence

from core.controller.base import BaseController
from core.controller.contract import quantize_rate_to_level

from .neural_abr_diagnostics import (
    DIAGNOSTIC_KEYS,
    NeuralAbrDecisionTelemetry,
    default_diagnostics,
)
from .neural_abr_loader import NeuralAbrRuntimeError, NeuralAbrRuntimeLoadError, load_runtime_engine
from .neural_abr_runtime_features import (
    RuntimeFeatureError,
    build_action_mask_from_feedback,
    build_runtime_sample,
    feedback_throughput_sample_Bps,
)
from .neural_abr_safety import apply_safety_guard, lowest_valid_action, select_fallback_action


class NeuralAbrLiteController(BaseController):
    name = "neural_abr_lite"

    def __init__(
        self,
        bundle_dir=None,
        enabled=True,
        verify_hashes=True,
        fallback_controller="robust_mpc",
        fallback_params=None,
        safety_buffer_margin_s=1.0,
        safety_throughput_factor=0.85,
        inference_timeout_ms=None,
        diagnostic_telemetry=True,
        fail_closed=True,
        idle_duration=1.0,
        **_unused,
    ):
        super().__init__()
        self.bundle_dir = bundle_dir
        self.requested_enabled = bool(enabled)
        self.verify_hashes = bool(verify_hashes)
        self.fallback_controller = str(fallback_controller or "robust_mpc")
        self.fallback_params = dict(fallback_params or {})
        self.safety_buffer_margin_s = _non_negative_float(safety_buffer_margin_s, 1.0)
        self.safety_throughput_factor = _unit_interval_float(safety_throughput_factor, 0.85)
        self.inference_timeout_ms = _optional_non_negative_float(inference_timeout_ms)
        self.diagnostic_telemetry = bool(diagnostic_telemetry)
        self.fail_closed = bool(fail_closed)
        self.idle_duration = _non_negative_float(idle_duration, 1.0)

        self._engine = None
        self._neural_active = False
        self._load_reason = ""
        self._throughput_history_Bps: list[float] = []
        self._download_time_history_s: list[float] = []
        self._previous_levels: list[int] = []
        self._last_history_sample_key = None
        self.last_metrics = {}

        self._base_telemetry = default_diagnostics()
        self._base_telemetry.update(
            {
                "neural_bundle_configured": 1 if _is_configured(bundle_dir) else 0,
                "neural_diagnostic_only": 1,
            }
        )
        self._last_decision = NeuralAbrDecisionTelemetry.with_base(self._base_telemetry)
        self._configure_engine()

    def calcControlAction(self):
        feedback = self.feedback or {}
        telemetry = NeuralAbrDecisionTelemetry.with_base(self._base_telemetry)
        telemetry.update(
            neural_enabled=1 if self._neural_active else 0,
            neural_fallback_reason=self._load_reason,
        )

        try:
            rates = _rates_from_feedback(feedback)
            action_mask = build_action_mask_from_feedback(feedback)
        except RuntimeFeatureError as exc:
            return self._finish_without_valid_ladder(telemetry, exc.reason)
        except Exception:
            return self._finish_without_valid_ladder(telemetry, "action_mask_invalid")

        if len(rates) == 1:
            telemetry.update(
                neural_action_mask_valid_count=1,
                neural_raw_action=0,
                neural_raw_rate_Bps=rates[0],
                neural_safe_action=0,
                neural_safe_rate_Bps=rates[0],
                neural_fallback_used=0,
                neural_fallback_reason="single_representation",
            )
            return self._finish_selected_rate(rates[0], 0, telemetry)

        if not self.requested_enabled:
            return self._fallback_decision(feedback, rates, action_mask, telemetry, "neural_disabled")
        if not self._neural_active or self._engine is None:
            return self._fallback_decision(feedback, rates, action_mask, telemetry, self._load_reason or "bundle_load_failed")

        effective_throughput, effective_download_times, sample_key = self._effective_histories(feedback)
        try:
            sample = build_runtime_sample(
                feedback,
                effective_throughput,
                effective_download_times,
                previous_levels=self._previous_levels,
                include_feedback_sample=False,
            )
            action_mask = sample.action_mask
            telemetry.update(
                neural_feature_vector_ok=1,
                neural_missing_features="",
                neural_action_mask_valid_count=sum(1 for valid in action_mask if valid),
            )
        except RuntimeFeatureError as exc:
            telemetry.update(
                neural_feature_vector_ok=0,
                neural_missing_features=exc.missing_features,
            )
            return self._fallback_decision(feedback, rates, action_mask, telemetry, exc.reason)
        except Exception:
            telemetry.update(neural_feature_vector_ok=0)
            return self._fallback_decision(feedback, rates, action_mask, telemetry, "feature_build_failed")

        try:
            decision = self._engine.score(sample.context, sample.candidates, sample.action_mask)
            telemetry.update(neural_inference_ms=decision.latency_ms)
            if self.inference_timeout_ms is not None and float(decision.latency_ms) > self.inference_timeout_ms:
                return self._fallback_decision(feedback, rates, action_mask, telemetry, "inference_timeout")
            if not _scores_are_finite(decision.scores):
                telemetry.update(neural_nan_inf_detected=1)
                return self._fallback_decision(feedback, rates, action_mask, telemetry, "non_finite_scores")
            if not _scores_match_action_mask(decision.scores, action_mask):
                return self._fallback_decision(feedback, rates, action_mask, telemetry, "inference_failed")
            raw_action = int(decision.raw_action)
            if raw_action < 0 or raw_action >= len(rates) or not bool(action_mask[raw_action]):
                telemetry.update(neural_invalid_action_detected=1)
                return self._fallback_decision(feedback, rates, action_mask, telemetry, "selected_masked_action")
        except NeuralAbrRuntimeError as exc:
            if exc.reason == "non_finite_scores":
                telemetry.update(neural_nan_inf_detected=1)
            if exc.reason == "selected_masked_action":
                telemetry.update(neural_invalid_action_detected=1)
            return self._fallback_decision(feedback, rates, action_mask, telemetry, exc.reason)
        except Exception:
            return self._fallback_decision(feedback, rates, action_mask, telemetry, "inference_failed")

        telemetry.update(
            neural_raw_action=raw_action,
            neural_raw_rate_Bps=rates[raw_action],
        )
        safety = apply_safety_guard(
            raw_action=raw_action,
            rates_Bps=rates,
            action_mask=action_mask,
            feedback=feedback,
            throughput_history_Bps=effective_throughput,
            safety_buffer_margin_s=self.safety_buffer_margin_s,
            safety_throughput_factor=self.safety_throughput_factor,
        )
        telemetry.update(neural_safety_intervened=1 if safety.intervened else 0)

        if safety.fallback_required or safety.action is None or safety.rate_Bps is None:
            return self._fallback_decision(feedback, rates, action_mask, telemetry, safety.reason)

        fallback_used = 1 if safety.reason == "emergency_lowest_representation" else 0
        telemetry.update(
            neural_safe_action=safety.action,
            neural_safe_rate_Bps=safety.rate_Bps,
            neural_fallback_used=fallback_used,
            neural_fallback_reason=safety.reason,
        )
        self._commit_history_sample(sample_key, effective_throughput, effective_download_times)
        return self._finish_selected_rate(float(safety.rate_Bps), int(safety.action), telemetry)

    def quantizeRate(self, rate):
        try:
            rates = _rates_from_feedback(self.feedback or {})
            level = quantize_rate_to_level(rate, rates)
            max_level = _max_level(self.feedback or {}, len(rates))
            return max(0, min(int(level), max_level))
        except Exception:
            return super().quantizeRate(rate)

    def augment_feedback(self, feedback, context=None):
        if not self.diagnostic_telemetry:
            return dict(feedback)
        augmented = dict(feedback)
        for key, value in self._telemetry_defaults_for_row().items():
            augmented.setdefault(key, value)
        return augmented

    def get_last_decision_telemetry(self):
        return self._last_decision.to_dict()

    def _configure_engine(self) -> None:
        if not self.requested_enabled:
            self._load_reason = "neural_disabled"
            self._base_telemetry.update(neural_enabled=0)
            self._last_decision = NeuralAbrDecisionTelemetry.with_base(self._base_telemetry)
            return
        if not _is_configured(self.bundle_dir):
            self._load_reason = "missing_bundle_dir"
            self._base_telemetry.update(neural_enabled=0)
            self._last_decision = NeuralAbrDecisionTelemetry.with_base(self._base_telemetry)
            return

        try:
            self._engine = load_runtime_engine(self.bundle_dir, verify_hashes=self.verify_hashes)
            self._neural_active = True
            self._load_reason = "success_neural"
            self._base_telemetry.update(
                neural_enabled=1,
                neural_bundle_loaded=1,
                neural_bundle_schema_ok=1,
                neural_bundle_hash_ok=1 if self.verify_hashes else 1,
                neural_feature_schema_ok=1,
                neural_fallback_reason="success_neural",
            )
        except NeuralAbrRuntimeLoadError as exc:
            self._engine = None
            self._neural_active = False
            self._load_reason = exc.reason
            self._base_telemetry.update(
                neural_enabled=0,
                neural_bundle_loaded=0,
                neural_bundle_schema_ok=0 if "schema" in exc.reason or "bundle" in exc.reason else 1,
                neural_bundle_hash_ok=0 if exc.reason == "bundle_hash_invalid" else 1,
                neural_feature_schema_ok=0 if exc.reason == "bundle_schema_invalid" else 1,
                neural_fallback_reason=exc.reason,
            )
        except Exception:
            self._engine = None
            self._neural_active = False
            self._load_reason = "bundle_load_failed"
            self._base_telemetry.update(neural_enabled=0, neural_bundle_loaded=0, neural_fallback_reason=self._load_reason)
        self._last_decision = NeuralAbrDecisionTelemetry.with_base(self._base_telemetry)

    def _fallback_decision(self, feedback, rates, action_mask, telemetry, reason):
        try:
            fallback = select_fallback_action(
                feedback,
                rates,
                action_mask,
                fallback_controller=self.fallback_controller,
                fallback_params=self.fallback_params,
            )
            fallback_reason = "fallback_controller_failed" if fallback.reason == "fallback_controller_failed" else reason
            telemetry.update(
                neural_safe_action=fallback.action,
                neural_safe_rate_Bps=fallback.rate_Bps,
                neural_fallback_used=1,
                neural_fallback_reason=fallback_reason,
            )
            self._commit_history_from_feedback(feedback)
            return self._finish_selected_rate(fallback.rate_Bps, fallback.action, telemetry)
        except Exception:
            try:
                lowest = lowest_valid_action(action_mask)
                selected_rate = float(rates[lowest])
            except Exception:
                lowest = 0
                selected_rate = 0.0
            telemetry.update(
                neural_safe_action=lowest,
                neural_safe_rate_Bps=selected_rate,
                neural_fallback_used=1,
                neural_fallback_reason="emergency_lowest_representation",
            )
            self._commit_history_from_feedback(feedback)
            return self._finish_selected_rate(selected_rate, lowest, telemetry)

    def _finish_without_valid_ladder(self, telemetry, reason):
        telemetry.update(
            neural_fallback_used=1,
            neural_fallback_reason=reason or "all_actions_invalid",
        )
        return self._finish_selected_rate(0.0, None, telemetry)

    def _finish_selected_rate(self, rate_Bps, action, telemetry):
        selected_rate = float(rate_Bps)
        self.setIdleDuration(self.idle_duration)
        self.setControlAction(selected_rate)
        if action is not None:
            self._previous_levels.append(int(action))
            self._previous_levels = self._previous_levels[-8:]
        self._last_decision = telemetry
        self.last_metrics = telemetry.to_dict()
        return selected_rate

    def _effective_histories(self, feedback: Mapping[str, object]):
        throughput = list(self._throughput_history_Bps)
        download_times = list(self._download_time_history_s)
        sample = feedback_throughput_sample_Bps(feedback)
        sample_key = _sample_key(feedback, sample)
        if sample is not None and sample_key != self._last_history_sample_key:
            throughput.append(float(sample[0]))
            download_times.append(float(sample[1]))
        return tuple(throughput[-8:]), tuple(download_times[-8:]), sample_key

    def _commit_history_sample(self, sample_key, throughput, download_times):
        if sample_key is None or sample_key == self._last_history_sample_key:
            return
        self._throughput_history_Bps = [float(value) for value in throughput][-8:]
        self._download_time_history_s = [float(value) for value in download_times][-8:]
        self._last_history_sample_key = sample_key

    def _commit_history_from_feedback(self, feedback):
        throughput, download_times, sample_key = self._effective_histories(feedback)
        self._commit_history_sample(sample_key, throughput, download_times)

    def _telemetry_defaults_for_row(self):
        values = default_diagnostics()
        values.update(
            {
                "neural_enabled": 1 if self._neural_active else 0,
                "neural_bundle_configured": 1 if _is_configured(self.bundle_dir) else 0,
                "neural_bundle_loaded": 1 if self._engine is not None else 0,
                "neural_bundle_schema_ok": self._base_telemetry.get("neural_bundle_schema_ok", 0),
                "neural_bundle_hash_ok": self._base_telemetry.get("neural_bundle_hash_ok", 0),
                "neural_feature_schema_ok": self._base_telemetry.get("neural_feature_schema_ok", 0),
                "neural_fallback_reason": self._load_reason,
                "neural_diagnostic_only": 1,
            }
        )
        return {key: values[key] for key in DIAGNOSTIC_KEYS}


def _is_configured(value: object) -> bool:
    return value is not None and str(value).strip() != ""


def _rates_from_feedback(feedback: Mapping[str, object]) -> tuple[float, ...]:
    raw_rates = feedback.get("rates")
    if raw_rates is None:
        raise RuntimeFeatureError("missing_required_feature", "feedback missing rates", ("rates",))
    try:
        values = tuple(raw_rates)  # type: ignore[arg-type]
    except TypeError as exc:
        raise RuntimeFeatureError("action_mask_invalid", "rates must be iterable") from exc
    if not values:
        raise RuntimeFeatureError("all_actions_invalid", "rates ladder is empty")
    rates = []
    for index, value in enumerate(values):
        if isinstance(value, bool) or not isinstance(value, Real):
            raise RuntimeFeatureError("action_mask_invalid", "rate {0} is not numeric".format(index))
        rate = float(value)
        if not math.isfinite(rate) or rate <= 0.0:
            raise RuntimeFeatureError("action_mask_invalid", "rate {0} is not positive finite".format(index))
        rates.append(rate)
    return tuple(rates)


def _scores_are_finite(scores: Sequence[object]) -> bool:
    try:
        for score in scores:
            if isinstance(score, bool) or not math.isfinite(float(score)):
                return False
    except (TypeError, ValueError):
        return False
    return True


def _scores_match_action_mask(scores: Sequence[object], action_mask: Sequence[object]) -> bool:
    try:
        score_count = len(tuple(scores))
        mask_count = len(tuple(action_mask))
    except TypeError:
        return False
    return score_count > 0 and score_count == mask_count


def _sample_key(feedback: Mapping[str, object], sample):
    if sample is None:
        return None
    return (
        feedback.get("segment_index"),
        feedback.get("last_fragment_size"),
        feedback.get("last_download_time"),
        sample[0],
    )


def _max_level(feedback: Mapping[str, object], count: int) -> int:
    try:
        value = int(feedback.get("max_level", count - 1))
    except (TypeError, ValueError):
        value = count - 1
    return max(0, min(value, count - 1))


def _optional_non_negative_float(value: object) -> float | None:
    if value is None:
        return None
    parsed = _finite_float(value)
    if parsed is None or parsed < 0.0:
        return None
    return parsed


def _non_negative_float(value: object, default: float) -> float:
    parsed = _finite_float(value)
    if parsed is None or parsed < 0.0:
        return float(default)
    return float(parsed)


def _unit_interval_float(value: object, default: float) -> float:
    parsed = _finite_float(value)
    if parsed is None or parsed <= 0.0 or parsed > 1.0:
        return float(default)
    return float(parsed)


def _finite_float(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(parsed):
        return None
    return parsed

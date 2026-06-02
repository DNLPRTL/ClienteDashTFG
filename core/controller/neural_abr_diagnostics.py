"""Diagnostic-only telemetry keys for the NeuralABR-Lite controller."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, MutableMapping


DIAGNOSTIC_KEYS = (
    "neural_enabled",
    "neural_bundle_configured",
    "neural_bundle_loaded",
    "neural_bundle_schema_ok",
    "neural_bundle_hash_ok",
    "neural_feature_schema_ok",
    "neural_feature_vector_ok",
    "neural_missing_features",
    "neural_action_mask_valid_count",
    "neural_raw_action",
    "neural_raw_rate_Bps",
    "neural_safe_action",
    "neural_safe_rate_Bps",
    "neural_safety_intervened",
    "neural_fallback_used",
    "neural_fallback_reason",
    "neural_inference_ms",
    "neural_nan_inf_detected",
    "neural_invalid_action_detected",
    "neural_diagnostic_only",
)


FALLBACK_REASONS = (
    "neural_disabled",
    "missing_bundle_dir",
    "bundle_load_failed",
    "torch_unavailable",
    "safe_torch_load_unavailable",
    "bundle_schema_invalid",
    "bundle_hash_invalid",
    "feature_build_failed",
    "missing_required_feature",
    "action_mask_invalid",
    "all_actions_invalid",
    "inference_failed",
    "inference_timeout",
    "non_finite_scores",
    "selected_masked_action",
    "safety_guard_rejected",
    "fallback_controller_failed",
    "emergency_lowest_representation",
    "single_representation",
    "success_neural",
)


def default_diagnostics() -> dict[str, object]:
    return {
        "neural_enabled": 0,
        "neural_bundle_configured": 0,
        "neural_bundle_loaded": 0,
        "neural_bundle_schema_ok": 0,
        "neural_bundle_hash_ok": 0,
        "neural_feature_schema_ok": 0,
        "neural_feature_vector_ok": 0,
        "neural_missing_features": "",
        "neural_action_mask_valid_count": 0,
        "neural_raw_action": "",
        "neural_raw_rate_Bps": "",
        "neural_safe_action": "",
        "neural_safe_rate_Bps": "",
        "neural_safety_intervened": 0,
        "neural_fallback_used": 0,
        "neural_fallback_reason": "",
        "neural_inference_ms": "",
        "neural_nan_inf_detected": 0,
        "neural_invalid_action_detected": 0,
        "neural_diagnostic_only": 1,
    }


@dataclass
class NeuralAbrDecisionTelemetry:
    values: MutableMapping[str, object] = field(default_factory=default_diagnostics)

    @classmethod
    def with_base(cls, base: Mapping[str, object] | None = None) -> "NeuralAbrDecisionTelemetry":
        values = default_diagnostics()
        if base:
            for key in DIAGNOSTIC_KEYS:
                if key in base:
                    values[key] = csv_safe_value(base[key])
        values["neural_diagnostic_only"] = 1
        return cls(values)

    def update(self, **values: object) -> None:
        for key, value in values.items():
            if key in DIAGNOSTIC_KEYS:
                self.values[key] = csv_safe_value(value)
        self.values["neural_diagnostic_only"] = 1

    def to_dict(self) -> dict[str, object]:
        return {key: csv_safe_value(self.values.get(key, default_diagnostics()[key])) for key in DIAGNOSTIC_KEYS}


def csv_safe_value(value: object) -> object:
    if value is None:
        return ""
    if isinstance(value, bool):
        return 1 if value else 0
    if isinstance(value, (int, float, str)):
        return value
    if isinstance(value, (list, tuple)):
        return ",".join(str(csv_safe_value(item)) for item in value)
    return str(value)


def telemetry_with_overrides(base: Mapping[str, object] | None = None, **overrides: object) -> dict[str, object]:
    telemetry = NeuralAbrDecisionTelemetry.with_base(base)
    telemetry.update(**overrides)
    return telemetry.to_dict()

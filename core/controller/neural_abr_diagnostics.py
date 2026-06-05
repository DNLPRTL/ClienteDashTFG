from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any, Dict


NEURAL_DIAGNOSTIC_KEYS = (
    "neural_enabled",
    "neural_controller_key",
    "neural_model_label",
    "neural_bundle_path",
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
    "neural_selected_representation_index",
    "neural_valid_action",
    "neural_safety_intervened",
    "neural_fallback_used",
    "neural_fallback_reason",
    "neural_inference_ms",
    "neural_nan_inf_detected",
    "neural_invalid_action_detected",
    "neural_diagnostic_only",
)


STABLE_FALLBACK_REASONS = frozenset(
    {
        "",
        "success_neural",
        "single_representation",
        "missing_bundle_dir",
        "bundle_schema_invalid",
        "bundle_hash_invalid",
        "bundle_load_failed",
        "safe_torch_load_unavailable",
        "feature_schema_invalid",
        "expected_teacher_mismatch",
        "model_config_invalid",
        "missing_required_feature",
        "feature_build_failed",
        "action_mask_invalid",
        "all_actions_invalid",
        "inference_failed",
        "inference_timeout",
        "selected_masked_action",
        "safety_guard_rejected",
        "fallback_controller_failed",
    }
)


@dataclass
class NeuralAbrDiagnostics:
    controller_key: str
    model_label: str
    bundle_path: str = ""
    bundle_configured: int = 0
    bundle_loaded: int = 0
    bundle_schema_ok: int = 0
    bundle_hash_ok: int = 0
    feature_schema_ok: int = 0
    feature_vector_ok: int = 0
    missing_features: str = ""
    action_mask_valid_count: int = 0
    raw_action: str = ""
    raw_rate_Bps: str = ""
    safe_action: str = ""
    safe_rate_Bps: str = ""
    selected_representation_index: str = ""
    valid_action: int = 0
    safety_intervened: int = 0
    fallback_used: int = 0
    fallback_reason: str = ""
    inference_ms: str = ""
    nan_inf_detected: int = 0
    invalid_action_detected: int = 0
    diagnostic_only: int = 1
    extra: Dict[str, Any] = field(default_factory=dict)

    def to_feedback_fields(self) -> Dict[str, object]:
        values: Dict[str, object] = {
            "neural_enabled": 1,
            "neural_controller_key": self.controller_key,
            "neural_model_label": self.model_label,
            "neural_bundle_path": self.bundle_path,
            "neural_bundle_configured": int(self.bundle_configured),
            "neural_bundle_loaded": int(self.bundle_loaded),
            "neural_bundle_schema_ok": int(self.bundle_schema_ok),
            "neural_bundle_hash_ok": int(self.bundle_hash_ok),
            "neural_feature_schema_ok": int(self.feature_schema_ok),
            "neural_feature_vector_ok": int(self.feature_vector_ok),
            "neural_missing_features": self.missing_features,
            "neural_action_mask_valid_count": int(self.action_mask_valid_count),
            "neural_raw_action": self.raw_action,
            "neural_raw_rate_Bps": self.raw_rate_Bps,
            "neural_safe_action": self.safe_action,
            "neural_safe_rate_Bps": self.safe_rate_Bps,
            "neural_selected_representation_index": self.selected_representation_index,
            "neural_valid_action": int(self.valid_action),
            "neural_safety_intervened": int(self.safety_intervened),
            "neural_fallback_used": int(self.fallback_used),
            "neural_fallback_reason": stable_reason(self.fallback_reason),
            "neural_inference_ms": self.inference_ms,
            "neural_nan_inf_detected": int(self.nan_inf_detected),
            "neural_invalid_action_detected": int(self.invalid_action_detected),
            "neural_diagnostic_only": int(self.diagnostic_only),
        }
        values.update(self.extra)
        return {key: values.get(key, "") for key in NEURAL_DIAGNOSTIC_KEYS}


def stable_reason(reason: object) -> str:
    text = str(reason or "").strip().lower()
    text = text.replace("-", "_").replace(" ", "_")
    text = "".join(char for char in text if char.isalnum() or char == "_")
    if text in STABLE_FALLBACK_REASONS:
        return text
    return "inference_failed"


def augment_feedback_with_neural_diagnostics(
    feedback: Mapping[str, object],
    diagnostics: NeuralAbrDiagnostics,
) -> Dict[str, object]:
    augmented = dict(feedback)
    augmented.update(diagnostics.to_feedback_fields())
    return augmented


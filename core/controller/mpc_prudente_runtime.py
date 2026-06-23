"""Controller runtime: MPC Neuronal Prudente integrado en el cliente DASH.

Reutiliza la maquinaria guarded de Neural-MPC (feature builder, safety, fallback a
robust_mpc, diagnósticos neurales, verificación de hash), pero:

- planifica sobre la **MediaFaithfulLadder** (tamaños reales VBR del MPD activo),
  no CBR;
- usa el planner prudente CVaR (`plan_prudent_action`) con `risk_alpha` del bundle.

Si el bundle o el perfil de medio fallan, cae a robust_mpc (auditado).
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence

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
from core.controller.phase45_v3_neural_mpc import (
    _as_bool,
    _lowest_valid_rate,
    _positive_float,
    _rates_from_feedback,
    _state_from_payload,
)
from core.controller.robust_mpc import RobustMpcController
from core.mpc_prudente.bundle import MpcPrudenteBundleError, MpcPrudenteRuntimeBundle
from core.mpc_prudente.media_profile import MediaProfileError, MediaProfileSegmentSizes
from core.mpc_prudente.planner import MPC_PRUDENTE_CONTROLLER_KEY, plan_prudent_action

DEFAULT_MPC_PRUDENTE_BUNDLE_DIR = "/home/daniel/TFG/modelos/mpc_prudente/runtime_bundle_v1"
DEFAULT_MEDIA_PROFILE_ID = "paseo_almunecar_10min_30fps_4s"
DEFAULT_FALLBACK_CONTROLLER = "robust_mpc"
DEFAULT_MAX_BUFFER_S = 60.0


class MpcPrudenteRuntimeController(BaseController):
    name = MPC_PRUDENTE_CONTROLLER_KEY

    def __init__(
        self,
        bundle_dir: object | None = None,
        media_profile_id: str = DEFAULT_MEDIA_PROFILE_ID,
        media_profile_dir: object | None = None,
        risk_alpha: float | None = None,
        fallback_controller: str = DEFAULT_FALLBACK_CONTROLLER,
        verify_hashes: bool = True,
        max_inference_latency_ms: float = DEFAULT_MAX_INFERENCE_LATENCY_MS,
        diagnostic_only: bool = False,
        max_buffer_s: float = DEFAULT_MAX_BUFFER_S,
        **_unused,
    ) -> None:
        super().__init__()
        self.name = MPC_PRUDENTE_CONTROLLER_KEY
        self.controller_key = MPC_PRUDENTE_CONTROLLER_KEY
        self.bundle_dir = str(bundle_dir or DEFAULT_MPC_PRUDENTE_BUNDLE_DIR)
        self.media_profile_id = str(media_profile_id or DEFAULT_MEDIA_PROFILE_ID)
        self.media_profile_dir = None if media_profile_dir is None else str(media_profile_dir)
        self.risk_alpha_override = None if risk_alpha is None else float(risk_alpha)
        self.verify_hashes = _as_bool(verify_hashes, True)
        self.max_inference_latency_ms = _positive_float(max_inference_latency_ms, DEFAULT_MAX_INFERENCE_LATENCY_MS)
        self.max_buffer_s = _positive_float(max_buffer_s, DEFAULT_MAX_BUFFER_S)
        self.diagnostic_only = bool(diagnostic_only)
        self.feature_builder = NeuralAbrRuntimeFeatureBuilder()
        self.fallback_controller_key = str(fallback_controller or DEFAULT_FALLBACK_CONTROLLER)
        self.fallback_controller = RobustMpcController()
        self._bundle: MpcPrudenteRuntimeBundle | None = None
        self._ladder = None
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
            ladder = self._ensure_faithful_ladder(payload.rates_Bps)
        except MpcPrudenteBundleError as exc:
            diagnostics.bundle_schema_ok = 0
            self._diagnostics = diagnostics
            return self._fallback_decision("bundle_load_failed", diagnostics, payload)
        except MediaProfileError:
            self._diagnostics = diagnostics
            return self._fallback_decision("media_profile_unavailable", diagnostics, payload)
        except Exception:
            self._diagnostics = diagnostics
            return self._fallback_decision("bundle_load_failed", diagnostics, payload)

        try:
            prediction = bundle.predict(state, ladder)
            risk_alpha = self.risk_alpha_override if self.risk_alpha_override is not None else bundle.risk_alpha
            decision = plan_prudent_action(
                state=state,
                ladder=ladder,
                predicted_bps_by_horizon_quantile=prediction,
                quantiles=bundle.quantiles,
                horizon_segments=bundle.horizon_segments,
                action_mask=payload.action_mask,
                risk_alpha=risk_alpha,
                rebuffer_weight=bundle.rebuffer_weight,
                switch_weight=bundle.switch_weight,
            )
            latency_ms = float(getattr(bundle, "last_latency_ms", 0.0) or 0.0)
            diagnostics.inference_ms = "{0:.6f}".format(latency_ms)
            diagnostics.raw_action = str(int(decision.action))
            diagnostics.raw_rate_Bps = str(float(ladder.bitrate_bps(int(decision.action))) / 8.0)
            if latency_ms > self.max_inference_latency_ms:
                return self._fallback_decision("inference_timeout", diagnostics, payload)
            safe_action, safe_rate = safe_action_to_rate(int(decision.action), payload.action_mask, payload.rates_Bps)
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

    def _ensure_bundle_loaded(self, diagnostics: NeuralAbrDiagnostics) -> MpcPrudenteRuntimeBundle:
        if self._bundle is not None:
            diagnostics.bundle_loaded = 1
            diagnostics.bundle_schema_ok = 1
            diagnostics.bundle_hash_ok = 1
            diagnostics.feature_schema_ok = 1
            return self._bundle
        self._bundle = MpcPrudenteRuntimeBundle(self.bundle_dir, verify_hashes=self.verify_hashes)
        self._bundle_load_attempted = True
        diagnostics.bundle_loaded = 1
        diagnostics.bundle_schema_ok = 1
        diagnostics.bundle_hash_ok = 1
        diagnostics.feature_schema_ok = 1
        return self._bundle

    def _ensure_faithful_ladder(self, rates_Bps: Sequence[float]):
        if self._ladder is None:
            media = MediaProfileSegmentSizes.load_by_id(self.media_profile_id, base_dir=self.media_profile_dir)
            self._ladder = media.to_faithful_ladder(max_buffer_s=self.max_buffer_s)
        if self._ladder.representation_count != len(tuple(rates_Bps)):
            raise MpcPrudenteBundleError(
                "media ladder ({0} reps) does not match client rates ({1})".format(
                    self._ladder.representation_count, len(tuple(rates_Bps))
                )
            )
        return self._ladder

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
            model_label="MPC Neuronal Prudente",
            bundle_path=self.bundle_dir,
            bundle_configured=1 if self.bundle_dir.strip() else 0,
            diagnostic_only=1 if self.diagnostic_only else 0,
        )


__all__ = ["MpcPrudenteRuntimeController", "MpcPrudenteRuntimeBundle"]

from __future__ import annotations

from core.controller.neural_abr_diagnostics import NeuralAbrDiagnostics
from core.controller.neural_abr_lite import NeuralAbrLiteController
from core.controller.neural_abr_loader import NeuralAbrRuntimeBundleError
from core.controller.spbc_abr_v2_dpo_loader import load_spbc_v2_dpo_runtime_bundle
from core.phase45_v1.spbc_v2_dpo_bundle import (
    SPBC_V2_DPO_CONTROLLER_DISPLAY_NAME,
    SPBC_V2_DPO_CONTROLLER_KEY,
)


class SpbcAbrV2DpoAnchorSafeRankController(NeuralAbrLiteController):
    """SPBC v2 DPO anchor-safe-rank runtime controller.

    The inherited controller logic handles runtime feature construction,
    diagnostics, action-mask safety and fallback. This subclass only changes the
    bundle loader/model family.
    """

    def __init__(self, **kwargs):
        super().__init__(
            controller_key=SPBC_V2_DPO_CONTROLLER_KEY,
            model_label=SPBC_V2_DPO_CONTROLLER_DISPLAY_NAME,
            expected_teacher=SPBC_V2_DPO_CONTROLLER_KEY,
            **kwargs,
        )

    def _load_runtime_bundle(self):
        return load_spbc_v2_dpo_runtime_bundle(
            self.bundle_dir,
            verify_hashes=self.verify_hashes,
        )

    def _base_diagnostics(self) -> NeuralAbrDiagnostics:
        diagnostics = super()._base_diagnostics()
        diagnostics.extra["neural_model_family"] = "spbc_abr_v2_dpo"
        return diagnostics


__all__ = [
    "SpbcAbrV2DpoAnchorSafeRankController",
    "NeuralAbrRuntimeBundleError",
]

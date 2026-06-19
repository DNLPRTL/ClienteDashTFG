from __future__ import annotations

import unittest

from core.mpc_prudente.media_profile import (
    MEDIA_PROFILE_SEGMENT_SIZES_SCHEMA_ID,
    MediaProfileSegmentSizes,
)
from core.mpc_prudente.planner import (
    PrudentDecision,
    PrudentMpcController,
    _cvar,
    buffer_risk_alpha,
    plan_prudent_action,
)
from core.phase45_v3.abr_closed_loop_env import AbrClosedLoopState

QUANTILES = (0.10, 0.25, 0.50, 0.75)


def _ladder(segment_count: int = 6):
    bitrates = (300000, 750000, 1200000, 1850000, 2850000, 4300000)
    representations = []
    for bandwidth in bitrates:
        nominal = int(bandwidth * 4.0 / 8.0)
        representations.append({"bandwidth_bps": bandwidth, "segment_bytes": [nominal] * 8})
    profile = MediaProfileSegmentSizes.from_mapping(
        {
            "schema_id": MEDIA_PROFILE_SEGMENT_SIZES_SCHEMA_ID,
            "media_profile_id": "synthetic_test",
            "segment_duration_s": 4.0,
            "segment_count": 8,
            "representations": representations,
        }
    )
    return profile.to_faithful_ladder(segment_count=segment_count, max_buffer_s=60.0)


def _state(buffer_s: float):
    return AbrClosedLoopState(
        segment_index=0,
        buffer_s=float(buffer_s),
        last_representation_index=-1,
        throughput_history_bps=(2_000_000.0,),
        download_time_history_s=(),
        recent_rebuffer_s=0.0,
        recent_switch_abs=0.0,
        network_time_s=0.0,
        total_segments=6,
    )


def _wide_prediction(horizon: int):
    # Spread amplio: q10 bajo (riesgo de stall), q75 alto.
    row = (1_200_000.0, 2_000_000.0, 3_500_000.0, 5_000_000.0)
    return tuple(row for _ in range(horizon))


class CvarTest(unittest.TestCase):
    def test_cvar_levels(self):
        scores = [1.0, 2.0, 3.0, 4.0]
        self.assertEqual(_cvar(scores, 0.25), 1.0)  # peor escenario
        self.assertEqual(_cvar(scores, 0.50), 1.5)  # media de los 2 peores
        self.assertEqual(_cvar(scores, 1.0), 2.5)   # media (neutral)

    def test_buffer_risk_alpha_monotone(self):
        self.assertLess(buffer_risk_alpha(2.0), buffer_risk_alpha(30.0))


class PrudentPlannerTest(unittest.TestCase):
    def test_prudent_picks_safer_action_than_risk_neutral(self):
        ladder = _ladder()
        state = _state(buffer_s=8.0)
        prediction = _wide_prediction(horizon=2)

        prudent = plan_prudent_action(
            state=state, ladder=ladder, predicted_bps_by_horizon_quantile=prediction,
            quantiles=QUANTILES, horizon_segments=2, risk_alpha=0.25,
        )
        neutral = plan_prudent_action(
            state=state, ladder=ladder, predicted_bps_by_horizon_quantile=prediction,
            quantiles=QUANTILES, horizon_segments=2, risk_alpha=1.0,
        )
        # El prudente (mira el peor caso) elige un bitrate más bajo que el neutral.
        self.assertLess(prudent.action, neutral.action)
        self.assertEqual(len(prudent.per_quantile_rebuffer_s), len(QUANTILES))

    def test_decision_respects_action_mask(self):
        ladder = _ladder()
        state = _state(buffer_s=20.0)
        prediction = _wide_prediction(horizon=2)
        mask = (True, True, False, False, False, False)  # solo acciones 0 y 1
        decision = plan_prudent_action(
            state=state, ladder=ladder, predicted_bps_by_horizon_quantile=prediction,
            quantiles=QUANTILES, horizon_segments=2, action_mask=mask, risk_alpha=0.5,
        )
        self.assertIn(decision.action, (0, 1))


class PrudentControllerTest(unittest.TestCase):
    def test_controller_uses_predictor(self):
        ladder = _ladder()
        state = _state(buffer_s=10.0)
        prediction = _wide_prediction(horizon=2)
        controller = PrudentMpcController(
            predictor=lambda s, l: prediction, quantiles=QUANTILES, horizon_segments=2
        )
        decision = controller.select_action(state, ladder)
        self.assertIsInstance(decision, PrudentDecision)
        self.assertFalse(decision.fallback_used)
        self.assertIn(decision.action, range(ladder.representation_count))

    def test_controller_falls_back_on_predictor_error(self):
        ladder = _ladder()
        state = _state(buffer_s=10.0)

        def broken_predictor(s, l):
            raise RuntimeError("predictor down")

        controller = PrudentMpcController(
            predictor=broken_predictor, quantiles=QUANTILES, horizon_segments=2
        )
        decision = controller.select_action(state, ladder)
        self.assertTrue(decision.fallback_used)
        self.assertIn(decision.action, range(ladder.representation_count))


if __name__ == "__main__":
    unittest.main()

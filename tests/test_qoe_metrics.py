from __future__ import annotations

import math
import unittest

from core.evaluation.qoe import (
    LOG_QOE_VERSION,
    SegmentQoEInput,
    QoEWeights,
    compute_linear_qoe,
    compute_log_qoe,
)


class QoEMetricsTest(unittest.TestCase):
    def test_linear_qoe_matches_phase3_5_formula(self):
        result = compute_linear_qoe(
            [
                SegmentQoEInput(1000, 0),
                SegmentQoEInput(2000, 0),
                SegmentQoEInput(1000, 0),
            ]
        )

        self.assertEqual(3, result.segment_count)
        self.assertAlmostEqual(2.0, result.qoe_sum)
        self.assertAlmostEqual(2.0 / 3.0, result.qoe_mean)
        self.assertAlmostEqual(4.0, result.quality_utility_sum)
        self.assertAlmostEqual(2.0, result.smoothness_penalty)
        self.assertEqual((1.0, 1.0, 0.0), result.segment_rewards)
        self.assertEqual(2, result.quality_switch_count)
        self.assertEqual(1, result.up_switch_count)
        self.assertEqual(1, result.down_switch_count)

    def test_rebuffer_penalty_is_applied(self):
        result = compute_linear_qoe(
            [
                SegmentQoEInput(1000, 0),
                SegmentQoEInput(1000, 1.5),
            ]
        )

        self.assertAlmostEqual(2.0 - 4.3 * 1.5, result.qoe_sum)
        self.assertAlmostEqual(1.5, result.total_rebuffer_s)
        self.assertEqual(1, result.stall_event_count)

    def test_custom_weights_validate_and_apply(self):
        result = compute_linear_qoe(
            [
                SegmentQoEInput(1000, 1),
                SegmentQoEInput(2000, 0),
            ],
            weights=QoEWeights(rebuffer_weight=2.0, smoothness_weight=0.5),
        )

        self.assertAlmostEqual(0.5, result.qoe_sum)

    def test_invalid_inputs_are_rejected(self):
        invalid_cases = [
            [],
            [SegmentQoEInput(0, 0)],
            [SegmentQoEInput(-1, 0)],
            [SegmentQoEInput(1000, -0.1)],
            [SegmentQoEInput(math.inf, 0)],
            [SegmentQoEInput(1000, math.nan)],
        ]

        for segments in invalid_cases:
            with self.subTest(segments=segments):
                with self.assertRaises(ValueError):
                    compute_linear_qoe(segments)

    def test_invalid_weights_are_rejected(self):
        for weights in (
            QoEWeights(rebuffer_weight=-1),
            QoEWeights(smoothness_weight=math.inf),
            QoEWeights(startup_penalty_weight=math.nan),
        ):
            with self.subTest(weights=weights):
                with self.assertRaises(ValueError):
                    compute_linear_qoe([SegmentQoEInput(1000, 0)], weights=weights)

    def test_log_qoe_requires_explicit_min_bitrate(self):
        with self.assertRaises(TypeError):
            compute_log_qoe([SegmentQoEInput(1000, 0)])  # type: ignore[call-arg]
        with self.assertRaises(ValueError):
            compute_log_qoe([SegmentQoEInput(1000, 0)], min_bitrate_kbps=0)

        result = compute_log_qoe(
            [
                SegmentQoEInput(1000, 0),
                SegmentQoEInput(2000, 0),
            ],
            min_bitrate_kbps=1000,
        )

        self.assertEqual(LOG_QOE_VERSION, result.formula_version)
        self.assertAlmostEqual(math.log(2.0) - math.log(2.0), result.qoe_sum)


if __name__ == "__main__":
    unittest.main()

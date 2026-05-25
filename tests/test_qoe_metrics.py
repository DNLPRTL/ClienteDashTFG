from __future__ import annotations

import math
import unittest

from core.evaluation import (
    QoEWeights,
    SegmentQoEInput,
    compute_linear_qoe,
    compute_log_qoe,
)


class QoEMetricsTest(unittest.TestCase):
    def test_linear_qoe_three_segments_without_rebuffer(self):
        segments = [
            SegmentQoEInput(1000.0),
            SegmentQoEInput(2000.0),
            SegmentQoEInput(1000.0),
        ]

        result = compute_linear_qoe(segments)

        self.assertEqual("qoe_linear_v1", result.formula_version)
        self.assertEqual(3, result.segment_count)
        self.assertAlmostEqual(4.0, result.quality_utility_sum)
        self.assertAlmostEqual(2.0, result.smoothness_penalty)
        self.assertAlmostEqual(0.0, result.rebuffer_penalty)
        self.assertAlmostEqual(2.0, result.qoe_sum)
        self.assertAlmostEqual(2.0 / 3.0, result.qoe_mean)
        self.assertAlmostEqual(4000.0 / 3.0, result.avg_bitrate_kbps)
        self.assertAlmostEqual(4.0 / 3.0, result.avg_quality_mbps)
        self.assertAlmostEqual(2000.0, result.total_switch_magnitude_kbps)
        self.assertEqual(2, result.quality_switch_count)
        self.assertEqual(1, result.up_switch_count)
        self.assertEqual(1, result.down_switch_count)
        self.assertEqual(0, result.stall_event_count)
        self.assertEqual((1.0, 1.0, 0.0), result.segment_rewards)

    def test_linear_qoe_three_segments_with_rebuffer(self):
        segments = [
            SegmentQoEInput(1000.0),
            SegmentQoEInput(2000.0, rebuffer_s=1.0),
            SegmentQoEInput(1000.0),
        ]

        result = compute_linear_qoe(segments)

        self.assertAlmostEqual(4.0, result.quality_utility_sum)
        self.assertAlmostEqual(2.0, result.smoothness_penalty)
        self.assertAlmostEqual(4.3, result.rebuffer_penalty)
        self.assertAlmostEqual(1.0, result.total_rebuffer_s)
        self.assertEqual(1, result.stall_event_count)
        self.assertAlmostEqual(-2.3, result.qoe_sum)

    def test_single_segment_has_no_smoothness_or_switches(self):
        result = compute_linear_qoe([SegmentQoEInput(2500.0)])

        self.assertAlmostEqual(0.0, result.smoothness_penalty)
        self.assertEqual(0, result.quality_switch_count)
        self.assertAlmostEqual(0.0, result.avg_switch_magnitude_kbps)
        self.assertAlmostEqual(2.5, result.qoe_sum)
        self.assertEqual((2.5,), result.segment_rewards)

    def test_empty_segments_raise_value_error(self):
        with self.assertRaises(ValueError):
            compute_linear_qoe([])

    def test_zero_or_negative_bitrate_raise_value_error(self):
        for bitrate_kbps in (0.0, -1.0):
            with self.subTest(bitrate_kbps=bitrate_kbps):
                with self.assertRaises(ValueError):
                    compute_linear_qoe([SegmentQoEInput(bitrate_kbps)])

    def test_negative_rebuffer_raises_value_error(self):
        with self.assertRaises(ValueError):
            compute_linear_qoe([SegmentQoEInput(1000.0, rebuffer_s=-0.1)])

    def test_nan_and_inf_inputs_raise_value_error(self):
        invalid_values = (float("nan"), float("inf"), float("-inf"))

        for value in invalid_values:
            with self.subTest(field="bitrate", value=value):
                with self.assertRaises(ValueError):
                    compute_linear_qoe([SegmentQoEInput(value)])

            with self.subTest(field="rebuffer", value=value):
                with self.assertRaises(ValueError):
                    compute_linear_qoe([SegmentQoEInput(1000.0, rebuffer_s=value)])

            for field_name in ("rebuffer_weight", "smoothness_weight", "startup_penalty_weight"):
                weights = {
                    "rebuffer_weight": 4.3,
                    "smoothness_weight": 1.0,
                    "startup_penalty_weight": 0.0,
                }
                weights[field_name] = value
                with self.subTest(field=field_name, value=value):
                    with self.assertRaises(ValueError):
                        compute_linear_qoe(
                            [SegmentQoEInput(1000.0)],
                            weights=QoEWeights(**weights),
                        )

    def test_negative_weights_raise_value_error(self):
        for weights in (
            QoEWeights(rebuffer_weight=-1.0),
            QoEWeights(smoothness_weight=-1.0),
            QoEWeights(startup_penalty_weight=-1.0),
        ):
            with self.subTest(weights=weights):
                with self.assertRaises(ValueError):
                    compute_linear_qoe([SegmentQoEInput(1000.0)], weights=weights)

    def test_log_qoe_two_segments_without_rebuffer(self):
        segments = [
            SegmentQoEInput(1000.0),
            SegmentQoEInput(2000.0),
        ]

        result = compute_log_qoe(segments, min_bitrate_kbps=1000.0)

        self.assertEqual("qoe_log_v1", result.formula_version)
        self.assertAlmostEqual(math.log(2.0), result.smoothness_penalty)
        self.assertAlmostEqual(math.log(2.0), result.quality_utility_sum)
        self.assertAlmostEqual(0.0, result.qoe_sum)
        self.assertAlmostEqual(0.0, result.qoe_mean)
        self.assertEqual((0.0, 0.0), result.segment_rewards)

    def test_log_qoe_rejects_non_positive_min_bitrate(self):
        for min_bitrate_kbps in (0.0, -1000.0):
            with self.subTest(min_bitrate_kbps=min_bitrate_kbps):
                with self.assertRaises(ValueError):
                    compute_log_qoe([SegmentQoEInput(1000.0)], min_bitrate_kbps=min_bitrate_kbps)

    def test_log_qoe_rejects_non_finite_min_bitrate(self):
        for min_bitrate_kbps in (float("nan"), float("inf"), float("-inf")):
            with self.subTest(min_bitrate_kbps=min_bitrate_kbps):
                with self.assertRaises(ValueError):
                    compute_log_qoe([SegmentQoEInput(1000.0)], min_bitrate_kbps=min_bitrate_kbps)

    def test_segment_rewards_are_immutable_tuple(self):
        result = compute_linear_qoe([SegmentQoEInput(1000.0)])

        self.assertIsInstance(result.segment_rewards, tuple)


if __name__ == "__main__":
    unittest.main()

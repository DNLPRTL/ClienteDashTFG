from __future__ import annotations

import unittest

import torch

from core.phase45_v3.throughput_quantile_model import (
    pinball_quantile_loss,
    quantile_crossing_penalty,
    temporal_smoothness_penalty,
    throughput_quantile_loss,
)


class Phase45V3ThroughputQuantileLossTest(unittest.TestCase):
    def test_pinball_loss_and_regularizers_are_finite(self):
        prediction = torch.tensor(
            [
                [[-0.5, -0.2, 0.0, 0.2], [-0.4, -0.1, 0.1, 0.3]],
                [[0.0, 0.1, 0.3, 0.4], [0.1, 0.2, 0.4, 0.5]],
            ],
            dtype=torch.float32,
        )
        target = torch.tensor([[0.0, 0.2], [0.2, 0.3]], dtype=torch.float32)
        quantiles = (0.10, 0.25, 0.50, 0.75)

        loss, parts = throughput_quantile_loss(prediction, target, quantiles)

        self.assertTrue(torch.isfinite(loss))
        self.assertGreaterEqual(parts["pinball_loss"], 0.0)
        self.assertEqual(0.0, quantile_crossing_penalty(prediction).item())
        self.assertGreaterEqual(temporal_smoothness_penalty(prediction).item(), 0.0)
        self.assertAlmostEqual(parts["pinball_loss"], pinball_quantile_loss(prediction, target, quantiles).item())

    def test_crossing_penalty_detects_unsorted_quantiles(self):
        prediction = torch.tensor([[[0.5, 0.3, 0.4, 0.6]]], dtype=torch.float32)

        self.assertGreater(quantile_crossing_penalty(prediction).item(), 0.0)


if __name__ == "__main__":
    unittest.main()

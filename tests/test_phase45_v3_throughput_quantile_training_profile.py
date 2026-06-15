from __future__ import annotations

import unittest

from core.phase45_v3.neural_mpc_training import throughput_quantile_training_profile_by_name


class Phase45V3ThroughputQuantileTrainingProfileTest(unittest.TestCase):
    def test_full_v1_profile_is_available_for_neural_mpc_v2(self):
        profile = throughput_quantile_training_profile_by_name("full_v1")

        self.assertEqual("full_v1", profile.name)
        self.assertEqual((0.10, 0.25, 0.50, 0.75), profile.quantiles)
        self.assertEqual(5, profile.horizon_segments)
        self.assertGreater(profile.epochs, throughput_quantile_training_profile_by_name("pilot").epochs)
        self.assertGreaterEqual(profile.batch_size, throughput_quantile_training_profile_by_name("pilot").batch_size)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import unittest

from core.neural_abr.action_mask import ActionMaskError, assert_action_valid, build_action_mask, validate_action_mask
from core.neural_abr.content_ladder import synthetic_smoke_ladder


class NeuralAbrActionMaskTest(unittest.TestCase):
    def test_valid_segment_mask_allows_all_representations(self):
        ladder = synthetic_smoke_ladder(segment_count=2)

        mask = build_action_mask(ladder, 0)

        self.assertEqual((True, True, True, True), mask)

    def test_out_of_range_segment_masks_everything(self):
        ladder = synthetic_smoke_ladder(segment_count=2)

        mask = build_action_mask(ladder, 3)

        self.assertEqual((False, False, False, False), mask)

    def test_action_must_be_inside_true_mask(self):
        mask = validate_action_mask([True, False], 2)

        assert_action_valid(0, mask)
        with self.assertRaises(ActionMaskError):
            assert_action_valid(1, mask)


if __name__ == "__main__":
    unittest.main()

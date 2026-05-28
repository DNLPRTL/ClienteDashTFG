from __future__ import annotations

import unittest

import torch

from core.neural_abr.model import NeuralAbrLiteCandidateScorer, masked_cross_entropy, predict_actions


class NeuralAbrModelTest(unittest.TestCase):
    def test_candidate_scorer_masks_invalid_scores(self):
        model = NeuralAbrLiteCandidateScorer(context_dim=3, candidate_dim=2, hidden_sizes=(4,))
        context = torch.zeros((2, 3), dtype=torch.float32)
        candidates = torch.zeros((2, 3, 2), dtype=torch.float32)
        mask = torch.tensor([[True, False, True], [False, True, False]])

        scores = model(context, candidates, mask)

        self.assertEqual((2, 3), tuple(scores.shape))
        self.assertLess(scores[0, 1].item(), -1.0e8)
        self.assertLess(scores[1, 0].item(), -1.0e8)

    def test_masked_cross_entropy_accepts_valid_teacher_actions(self):
        scores = torch.tensor([[1.0, -1.0e9, 2.0]], dtype=torch.float32)
        mask = torch.tensor([[True, False, True]])
        labels = torch.tensor([2])

        loss = masked_cross_entropy(scores, labels, mask)

        self.assertGreaterEqual(loss.item(), 0.0)
        self.assertEqual([2], predict_actions(scores).tolist())


if __name__ == "__main__":
    unittest.main()

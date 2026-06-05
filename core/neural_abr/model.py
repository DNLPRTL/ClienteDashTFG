from __future__ import annotations

from typing import Mapping, Sequence

import torch
from torch import nn
from torch.nn import functional as F

from core.neural_abr.constants import CANDIDATE_VECTOR_NAMES, CONTEXT_VECTOR_NAMES, PHASE4_MODEL_CONFIG_SCHEMA_ID


class ModelError(ValueError):
    """Raised when candidate scorer inputs are invalid."""


class NeuralAbrLiteCandidateScorer(nn.Module):
    def __init__(
        self,
        context_dim: int | None = None,
        candidate_dim: int | None = None,
        hidden_sizes: Sequence[int] = (32, 16),
    ) -> None:
        super().__init__()
        self.context_dim = int(context_dim or len(CONTEXT_VECTOR_NAMES))
        self.candidate_dim = int(candidate_dim or len(CANDIDATE_VECTOR_NAMES))
        self.hidden_sizes = tuple(int(value) for value in hidden_sizes)
        layers = []
        previous_dim = self.context_dim + self.candidate_dim
        for hidden_size in self.hidden_sizes:
            layers.append(nn.Linear(previous_dim, hidden_size))
            layers.append(nn.ReLU())
            previous_dim = hidden_size
        layers.append(nn.Linear(previous_dim, 1))
        self.scorer = nn.Sequential(*layers)

    def forward(self, context_features: torch.Tensor, candidate_features: torch.Tensor, action_mask: torch.Tensor) -> torch.Tensor:
        if context_features.ndim != 2:
            raise ModelError("context_features must have shape [batch, context_dim]")
        if candidate_features.ndim != 3:
            raise ModelError("candidate_features must have shape [batch, candidates, candidate_dim]")
        if action_mask.ndim != 2:
            raise ModelError("action_mask must have shape [batch, candidates]")
        if context_features.shape[0] != candidate_features.shape[0] or action_mask.shape != candidate_features.shape[:2]:
            raise ModelError("batch or candidate dimensions do not align")
        if context_features.shape[1] != self.context_dim:
            raise ModelError("context feature dimension mismatch")
        if candidate_features.shape[2] != self.candidate_dim:
            raise ModelError("candidate feature dimension mismatch")

        batch_size, candidate_count, _ = candidate_features.shape
        expanded_context = context_features.unsqueeze(1).expand(batch_size, candidate_count, self.context_dim)
        scorer_input = torch.cat([expanded_context, candidate_features], dim=2)
        raw_scores = self.scorer(scorer_input.reshape(batch_size * candidate_count, -1)).reshape(batch_size, candidate_count)
        mask = action_mask.to(dtype=torch.bool, device=raw_scores.device)
        return raw_scores.masked_fill(~mask, -1.0e9)

    def config(self) -> Mapping[str, object]:
        return {
            "schema_id": PHASE4_MODEL_CONFIG_SCHEMA_ID,
            "model_family": "NeuralABR-Lite Candidate Scorer",
            "model_type": "shared_mlp_candidate_scorer",
            "context_dim": self.context_dim,
            "candidate_dim": self.candidate_dim,
            "hidden_sizes": list(self.hidden_sizes),
            "device_default": "cpu",
            "controller_registered": False,
        }


def masked_cross_entropy(masked_scores: torch.Tensor, teacher_actions: torch.Tensor, action_mask: torch.Tensor) -> torch.Tensor:
    if masked_scores.ndim != 2 or action_mask.shape != masked_scores.shape:
        raise ModelError("masked_scores/action_mask shape mismatch")
    actions = teacher_actions.to(dtype=torch.long, device=masked_scores.device)
    mask = action_mask.to(dtype=torch.bool, device=masked_scores.device)
    if actions.ndim != 1 or actions.shape[0] != masked_scores.shape[0]:
        raise ModelError("teacher_actions must have shape [batch]")
    for batch_index, action in enumerate(actions.tolist()):
        if action < 0 or action >= masked_scores.shape[1] or not bool(mask[batch_index, action]):
            raise ModelError("teacher action is invalid under the action mask")
    return F.cross_entropy(masked_scores, actions)


def predict_actions(masked_scores: torch.Tensor) -> torch.Tensor:
    if masked_scores.ndim != 2:
        raise ModelError("masked_scores must have shape [batch, candidates]")
    return torch.argmax(masked_scores, dim=1)


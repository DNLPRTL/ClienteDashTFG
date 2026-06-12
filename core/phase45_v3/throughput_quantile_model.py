from __future__ import annotations

from typing import Mapping, Sequence

import torch
from torch import nn
from torch.nn import functional as F

from core.neural_abr.constants import CONTEXT_VECTOR_NAMES


PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY = "phase45_v3_throughput_quantile_predictor"
THROUGHPUT_QUANTILE_MODEL_CONFIG_SCHEMA_ID = "phase45_v3_throughput_quantile_model_config_v1"


class Phase45V3ThroughputQuantileModelError(ValueError):
    """Raised when throughput-quantile tensors are malformed."""


class ThroughputQuantilePredictor(nn.Module):
    def __init__(
        self,
        *,
        input_dim: int = len(CONTEXT_VECTOR_NAMES),
        horizon_segments: int = 5,
        quantiles: Sequence[float] = (0.10, 0.25, 0.50, 0.75),
        hidden_sizes: Sequence[int] = (256, 128, 64),
    ) -> None:
        super().__init__()
        self.input_dim = int(input_dim)
        self.horizon_segments = int(horizon_segments)
        self.quantiles = tuple(float(value) for value in quantiles)
        self.hidden_sizes = tuple(int(value) for value in hidden_sizes)
        if self.input_dim <= 0:
            raise Phase45V3ThroughputQuantileModelError("input_dim must be positive")
        if self.horizon_segments <= 0:
            raise Phase45V3ThroughputQuantileModelError("horizon_segments must be positive")
        if not self.quantiles:
            raise Phase45V3ThroughputQuantileModelError("quantiles must not be empty")

        width = self.input_dim
        layers: list[nn.Module] = []
        for hidden in self.hidden_sizes:
            if int(hidden) <= 0:
                raise Phase45V3ThroughputQuantileModelError("hidden sizes must be positive")
            layers.append(nn.Linear(width, int(hidden)))
            layers.append(nn.ReLU())
            width = int(hidden)
        layers.append(nn.Linear(width, self.horizon_segments * len(self.quantiles)))
        self.network = nn.Sequential(*layers)

    def forward(self, context: torch.Tensor) -> torch.Tensor:
        if context.ndim != 2 or context.shape[1] != self.input_dim:
            raise Phase45V3ThroughputQuantileModelError("context tensor has invalid shape")
        raw = self.network(context)
        return raw.reshape(context.shape[0], self.horizon_segments, len(self.quantiles))

    def config(self) -> Mapping[str, object]:
        return {
            "schema_id": THROUGHPUT_QUANTILE_MODEL_CONFIG_SCHEMA_ID,
            "model_key": PHASE45_V3_THROUGHPUT_QUANTILE_MODEL_KEY,
            "model_type": "mlp_future_throughput_log_ratio_quantile_predictor",
            "input_dim": self.input_dim,
            "context_feature_names": list(CONTEXT_VECTOR_NAMES),
            "horizon_segments": self.horizon_segments,
            "quantiles": list(self.quantiles),
            "hidden_sizes": list(self.hidden_sizes),
            "controller_registered": False,
        }


def pinball_quantile_loss(
    prediction: torch.Tensor,
    target: torch.Tensor,
    quantiles: Sequence[float],
) -> torch.Tensor:
    _validate_prediction_target(prediction, target, quantiles)
    q = prediction.new_tensor(tuple(float(value) for value in quantiles)).reshape(1, 1, -1)
    error = target.unsqueeze(2) - prediction
    return torch.maximum(q * error, (q - 1.0) * error).mean()


def quantile_crossing_penalty(prediction: torch.Tensor) -> torch.Tensor:
    if prediction.ndim != 3:
        raise Phase45V3ThroughputQuantileModelError("prediction must have shape batch x horizon x quantiles")
    if prediction.shape[2] < 2:
        return prediction.new_tensor(0.0)
    crossing = F.relu(prediction[:, :, :-1] - prediction[:, :, 1:])
    return crossing.mean()


def temporal_smoothness_penalty(prediction: torch.Tensor) -> torch.Tensor:
    if prediction.ndim != 3:
        raise Phase45V3ThroughputQuantileModelError("prediction must have shape batch x horizon x quantiles")
    if prediction.shape[1] < 2:
        return prediction.new_tensor(0.0)
    return torch.abs(prediction[:, 1:, :] - prediction[:, :-1, :]).mean()


def throughput_quantile_loss(
    prediction: torch.Tensor,
    target: torch.Tensor,
    quantiles: Sequence[float],
    *,
    pinball_loss_weight: float = 1.0,
    quantile_crossing_loss_weight: float = 0.10,
    temporal_smoothness_loss_weight: float = 0.05,
) -> tuple[torch.Tensor, Mapping[str, float]]:
    pinball = pinball_quantile_loss(prediction, target, quantiles)
    crossing = quantile_crossing_penalty(prediction)
    smoothness = temporal_smoothness_penalty(prediction)
    total = (
        float(pinball_loss_weight) * pinball
        + float(quantile_crossing_loss_weight) * crossing
        + float(temporal_smoothness_loss_weight) * smoothness
    )
    return total, {
        "pinball_loss": float(pinball.detach().cpu()),
        "quantile_crossing_loss": float(crossing.detach().cpu()),
        "temporal_smoothness_loss": float(smoothness.detach().cpu()),
        "total_loss": float(total.detach().cpu()),
    }


def _validate_prediction_target(prediction: torch.Tensor, target: torch.Tensor, quantiles: Sequence[float]) -> None:
    if prediction.ndim != 3:
        raise Phase45V3ThroughputQuantileModelError("prediction must have shape batch x horizon x quantiles")
    if target.ndim != 2:
        raise Phase45V3ThroughputQuantileModelError("target must have shape batch x horizon")
    if prediction.shape[:2] != target.shape:
        raise Phase45V3ThroughputQuantileModelError("prediction and target horizon dimensions do not align")
    if prediction.shape[2] != len(tuple(quantiles)):
        raise Phase45V3ThroughputQuantileModelError("prediction quantile dimension does not match quantiles")

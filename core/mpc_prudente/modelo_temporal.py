"""Predictor temporal de cuantiles de throughput (GRU) para MPC Prudente.

Frente al MLP: lee la secuencia de red con una GRU (capta tendencias), produce
cuantiles monótonos por construcción (base + incrementos softplus acumulados) y
está pensado para ensemble: la discrepancia entre miembros mide la incertidumbre
epistémica y ensancha la cola inferior en ventanas raras.

Entrada: `seq` [B, L, 2] (throughput, download_time por paso) y `scalar`
[B, F]. Salida: `[B, horizon, n_quantiles]` en espacio log-ratio.
"""

from __future__ import annotations

from typing import Mapping, Sequence

import torch
from torch import nn
from torch.nn import functional as F

CLAVE_MODELO_TEMPORAL = "mpc_prudente_temporal_quantile_predictor"
SCHEMA_ID_CONFIG_TEMPORAL = "mpc_prudente_temporal_model_config_v1"

# Campos escalares del contexto (orden fijo y determinista).
NOMBRES_FEATURES_ESCALARES = (
    "buffer_s",
    "last_representation_index",
    "last_bitrate_bps",
    "recent_rebuffer_s",
    "recent_switch_abs",
    "chunks_remaining_norm",
    "has_chunks_remaining",
)
# Features de secuencia por paso.
NOMBRES_FEATURES_SECUENCIA = ("throughput_history_bps", "download_time_history_s")


class ErrorModeloTemporal(ValueError):
    pass


class PredictorTemporalCuantiles(nn.Module):
    def __init__(
        self,
        *,
        seq_features: int,
        scalar_dim: int,
        horizon_segments: int,
        quantiles: Sequence[float],
        gru_hidden: int = 96,
        gru_layers: int = 1,
        mlp_hidden: Sequence[int] = (96, 64),
        dropout: float = 0.1,
    ) -> None:
        super().__init__()
        self.seq_features = int(seq_features)
        self.scalar_dim = int(scalar_dim)
        self.horizon_segments = int(horizon_segments)
        self.quantiles = tuple(float(q) for q in quantiles)
        self.gru_hidden = int(gru_hidden)
        self.gru_layers = int(gru_layers)
        self.mlp_hidden = tuple(int(h) for h in mlp_hidden)
        self.dropout = float(dropout)
        if self.horizon_segments <= 0 or not self.quantiles:
            raise ErrorModeloTemporal("horizonte o cuantiles invalidos")

        self.gru = nn.GRU(self.seq_features, self.gru_hidden, num_layers=self.gru_layers, batch_first=True)
        width = self.gru_hidden + self.scalar_dim
        layers: list[nn.Module] = []
        for hidden in self.mlp_hidden:
            layers.append(nn.Linear(width, hidden))
            layers.append(nn.ReLU())
            if self.dropout > 0:
                layers.append(nn.Dropout(self.dropout))
            width = hidden
        layers.append(nn.Linear(width, self.horizon_segments * len(self.quantiles)))
        self.head = nn.Sequential(*layers)

    def forward(self, seq: torch.Tensor, scalar: torch.Tensor) -> torch.Tensor:
        if seq.ndim != 3 or seq.shape[2] != self.seq_features:
            raise ErrorModeloTemporal("el tensor de secuencia tiene forma invalida")
        if scalar.ndim != 2 or scalar.shape[1] != self.scalar_dim:
            raise ErrorModeloTemporal("el tensor escalar tiene forma invalida")
        _, hidden = self.gru(seq)  # hidden: [layers, B, gru_hidden]
        feat = torch.cat([hidden[-1], scalar], dim=1)
        raw = self.head(feat).reshape(seq.shape[0], self.horizon_segments, len(self.quantiles))
        # Cuantiles monótonos: base + incrementos positivos acumulados.
        base = raw[:, :, :1]
        increments = F.softplus(raw[:, :, 1:])
        return torch.cat([base, base + torch.cumsum(increments, dim=2)], dim=2)

    def config(self) -> Mapping[str, object]:
        return {
            "schema_id": SCHEMA_ID_CONFIG_TEMPORAL,
            "model_key": CLAVE_MODELO_TEMPORAL,
            "model_type": "gru_monotonic_quantile_predictor",
            "seq_features": self.seq_features,
            "seq_feature_names": list(NOMBRES_FEATURES_SECUENCIA),
            "scalar_dim": self.scalar_dim,
            "scalar_feature_names": list(NOMBRES_FEATURES_ESCALARES),
            "horizon_segments": self.horizon_segments,
            "quantiles": list(self.quantiles),
            "gru_hidden": self.gru_hidden,
            "gru_layers": self.gru_layers,
            "mlp_hidden": list(self.mlp_hidden),
            "dropout": self.dropout,
        }


def combinar_cuantiles_ensemble(
    predictions: torch.Tensor, quantiles: Sequence[float], *, downside_widen: float = 1.0
) -> torch.Tensor:
    """Combina M predicciones [M, B, H, Q] en [B, H, Q].

    Media de los miembros + ensanchado de la cola INFERIOR proporcional a la
    discrepancia epistémica (std entre miembros de la mediana). Re-monotoniza.
    """
    if predictions.ndim != 4:
        raise ErrorModeloTemporal("las predicciones deben tener forma [M, B, H, Q]")
    quants = tuple(float(q) for q in quantiles)
    median_index = min(range(len(quants)), key=lambda i: abs(quants[i] - 0.5))
    mean_q = predictions.mean(dim=0)  # [B, H, Q]
    epistemic_std = predictions[:, :, :, median_index].std(dim=0, unbiased=False)  # [B, H]
    widened = mean_q.clone()
    for k, q in enumerate(quants):
        if q < 0.5:
            scale = float(downside_widen) * (0.5 - q) / 0.5  # más ensanchado cuanto más baja la cola
            widened[:, :, k] = mean_q[:, :, k] - scale * epistemic_std
    # re-monotonizar por seguridad (tras ensanchar la cola)
    return widened.sort(dim=2).values

"""Predictor temporal de cuantiles de throughput (GRU) para MPC Prudente.

Mejora respecto al MLP:
1. Lee la SECUENCIA de red (GRU) en vez de un vector aplanado → capta tendencias.
2. Cuantiles MONÓTONOS por construcción (base + incrementos softplus acumulados):
   imposible que q10 > q25 > ... Sin penalización de crossing, sin postproceso.
3. Pensado para ENSEMBLE profundo: varios modelos con semillas distintas. Su
   discrepancia mide la incertidumbre epistémica; el combinador ensancha la cola
   inferior cuando los modelos no se ponen de acuerdo (ventanas raras/OOD), que es
   justo donde el MLP se pasaba de optimista (caso real_012).

Entrada del modelo: `seq` [B, L, F_seq] (throughput, download_time por paso) y
`scalar` [B, F_scalar] (buffer, último bitrate, rebuffer reciente, etc.).
Salida: `[B, horizon, n_quantiles]` en el mismo espacio log-ratio que el target.
"""

from __future__ import annotations

from typing import Mapping, Sequence

import torch
from torch import nn
from torch.nn import functional as F

MPC_PRUDENTE_TEMPORAL_MODEL_KEY = "mpc_prudente_temporal_quantile_predictor"
TEMPORAL_MODEL_CONFIG_SCHEMA_ID = "mpc_prudente_temporal_model_config_v1"

# Campos escalares del contexto (orden fijo y determinista).
SCALAR_FEATURE_NAMES = (
    "buffer_s",
    "last_representation_index",
    "last_bitrate_bps",
    "recent_rebuffer_s",
    "recent_switch_abs",
    "chunks_remaining_norm",
    "has_chunks_remaining",
)
# Features de secuencia por paso.
SEQ_FEATURE_NAMES = ("throughput_history_bps", "download_time_history_s")


class TemporalQuantileModelError(ValueError):
    pass


class TemporalQuantilePredictor(nn.Module):
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
            raise TemporalQuantileModelError("invalid horizon/quantiles")

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
            raise TemporalQuantileModelError("seq tensor has invalid shape")
        if scalar.ndim != 2 or scalar.shape[1] != self.scalar_dim:
            raise TemporalQuantileModelError("scalar tensor has invalid shape")
        _, hidden = self.gru(seq)  # hidden: [layers, B, gru_hidden]
        feat = torch.cat([hidden[-1], scalar], dim=1)
        raw = self.head(feat).reshape(seq.shape[0], self.horizon_segments, len(self.quantiles))
        # Cuantiles monótonos: base + incrementos positivos acumulados.
        base = raw[:, :, :1]
        increments = F.softplus(raw[:, :, 1:])
        return torch.cat([base, base + torch.cumsum(increments, dim=2)], dim=2)

    def config(self) -> Mapping[str, object]:
        return {
            "schema_id": TEMPORAL_MODEL_CONFIG_SCHEMA_ID,
            "model_key": MPC_PRUDENTE_TEMPORAL_MODEL_KEY,
            "model_type": "gru_monotonic_quantile_predictor",
            "seq_features": self.seq_features,
            "seq_feature_names": list(SEQ_FEATURE_NAMES),
            "scalar_dim": self.scalar_dim,
            "scalar_feature_names": list(SCALAR_FEATURE_NAMES),
            "horizon_segments": self.horizon_segments,
            "quantiles": list(self.quantiles),
            "gru_hidden": self.gru_hidden,
            "gru_layers": self.gru_layers,
            "mlp_hidden": list(self.mlp_hidden),
            "dropout": self.dropout,
        }


def ensemble_quantiles(
    predictions: torch.Tensor, quantiles: Sequence[float], *, downside_widen: float = 1.0
) -> torch.Tensor:
    """Combina M predicciones [M, B, H, Q] en [B, H, Q].

    Media de los miembros + ensanchado de la cola INFERIOR proporcional a la
    discrepancia epistémica (std entre miembros de la mediana). Re-monotoniza.
    """
    if predictions.ndim != 4:
        raise TemporalQuantileModelError("predictions must be [M, B, H, Q]")
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

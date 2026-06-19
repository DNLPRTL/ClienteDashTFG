"""Dataset de entrenamiento FIEL para MPC Neuronal Prudente.

Reutiliza el generador probado de cuantiles de throughput de `phase45_v3`, pero
le inyecta un `ladder_factory` que usa el peso REAL (VBR) de cada segmento del
medio (`media_profiles/segment_sizes/<id>.json`). Así los rollouts que generan el
dataset avanzan el buffer con la física de descarga real del cliente, no con CBR.

El predictor resultante es agnóstico al medio (predice throughput), así que un solo
medio representativo (Paseo) basta para entrenarlo; el planner prudente usará en
runtime los tamaños reales del MPD que esté reproduciendo en cada experimento.
"""

from __future__ import annotations

from typing import Callable, Mapping, Sequence

from core.mpc_prudente.media_profile import DEFAULT_MAX_BUFFER_S, MediaProfileSegmentSizes
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v3.profiles import Phase45V3DatasetProfile
from core.phase45_v3.throughput_quantile_dataset import (
    DEFAULT_THROUGHPUT_QUANTILE_HORIZON,
    DEFAULT_THROUGHPUT_QUANTILES,
    build_phase45_v3_throughput_quantile_dataset,
)

DEFAULT_PILOT_MEDIA_PROFILE_ID = "paseo_almunecar_10min_30fps_4s"


class MpcPrudenteDatasetError(ValueError):
    """Raised when the media-faithful dataset cannot be built."""


def media_faithful_ladder_factory(
    media_profile: MediaProfileSegmentSizes,
    *,
    max_buffer_s: float = DEFAULT_MAX_BUFFER_S,
) -> Callable[[float, int], object]:
    """Devuelve una factoría `(segment_duration_s, segment_count) -> ladder fiel`."""

    def factory(segment_duration_s: float, segment_count: int) -> object:
        if abs(float(media_profile.segment_duration_s) - float(segment_duration_s)) > 1.0e-3:
            raise MpcPrudenteDatasetError(
                "duración de segmento incompatible: medio={0}s plan={1}s".format(
                    media_profile.segment_duration_s, segment_duration_s
                )
            )
        return media_profile.to_faithful_ladder(
            segment_count=int(segment_count), max_buffer_s=float(max_buffer_s)
        )

    return factory


def build_mpc_prudente_dataset(
    phase3_manifest: Mapping[str, object],
    output_dir: object,
    profile: Phase45V3DatasetProfile,
    *,
    media_profile_id: str = DEFAULT_PILOT_MEDIA_PROFILE_ID,
    media_profile_base_dir: str | None = None,
    max_buffer_s: float = DEFAULT_MAX_BUFFER_S,
    source_manifest_path: object | None = None,
    overwrite: bool = False,
    max_training_windows: int | None = None,
    max_validation_windows: int | None = None,
    trace_path_rewrites: Sequence[PathRewriteRule] = (),
    horizon_segments: int = DEFAULT_THROUGHPUT_QUANTILE_HORIZON,
    quantiles: Sequence[float] = DEFAULT_THROUGHPUT_QUANTILES,
) -> Mapping[str, object]:
    media_profile = MediaProfileSegmentSizes.load_by_id(
        media_profile_id, base_dir=media_profile_base_dir
    )
    factory = media_faithful_ladder_factory(media_profile, max_buffer_s=max_buffer_s)
    return build_phase45_v3_throughput_quantile_dataset(
        phase3_manifest,
        output_dir=output_dir,
        profile=profile,
        source_manifest_path=source_manifest_path,
        overwrite=overwrite,
        max_training_windows=max_training_windows,
        max_validation_windows=max_validation_windows,
        trace_path_rewrites=trace_path_rewrites,
        horizon_segments=horizon_segments,
        quantiles=quantiles,
        ladder_factory=factory,
    )

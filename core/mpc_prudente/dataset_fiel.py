"""Dataset de entrenamiento para MPC Prudente con física de descarga real (VBR).

Reutiliza el generador de cuantiles de throughput de `phase45_v3` inyectándole un
`ladder_factory` que usa los tamaños reales de segmento del medio, de forma que los
rollouts avanzan el buffer igual que el cliente y no con la aproximación CBR.
"""

from __future__ import annotations

from typing import Callable, Mapping, Sequence

from core.mpc_prudente.perfil_medio import MAX_BUFFER_S_POR_DEFECTO, PerfilTamanosSegmentos
from core.phase45_v1.paths import PathRewriteRule
from core.phase45_v3.profiles import Phase45V3DatasetProfile
from core.phase45_v3.throughput_quantile_dataset import (
    DEFAULT_THROUGHPUT_QUANTILE_HORIZON,
    DEFAULT_THROUGHPUT_QUANTILES,
    build_phase45_v3_throughput_quantile_dataset,
)

ID_PERFIL_MEDIO_PILOTO = "paseo_almunecar_10min_30fps_4s"


class ErrorDatasetMpcPrudente(ValueError):
    """Error al construir el dataset fiel al medio."""


TOLERANCIA_DURACION_SEGMENTO_S = 0.1  # tolera 4.004s (60fps NTSC) vs 4.0s del plan

# Los 8 perfiles de medio de 4 s (multi-vídeo, sin sesgo a un solo vídeo).
IDS_PERFILES_MULTIMEDIA = (
    "paseo_almunecar_10min_30fps_4s",
    "paseo_almunecar_10min_60fps_4s",
    "paseo_almunecar_1min_30fps_4s",
    "paseo_almunecar_1min_60fps_4s",
    "blender_sunflower_10min_30fps_4s",
    "blender_sunflower_10min_60fps_4s",
    "blender_sunflower_1min_30fps_4s",
    "blender_sunflower_1min_60fps_4s",
)


def _escalera_fiel_desde_perfil(perfil_medio, segment_duration_s, segment_count, max_buffer_s):
    if abs(float(perfil_medio.segment_duration_s) - float(segment_duration_s)) > TOLERANCIA_DURACION_SEGMENTO_S:
        raise ErrorDatasetMpcPrudente(
            "duración de segmento incompatible: medio={0}s plan={1}s".format(
                perfil_medio.segment_duration_s, segment_duration_s
            )
        )
    return perfil_medio.a_escalera_fiel(segment_count=int(segment_count), max_buffer_s=float(max_buffer_s))


def factoria_escalera_fiel(
    perfil_medio: PerfilTamanosSegmentos,
    *,
    max_buffer_s: float = MAX_BUFFER_S_POR_DEFECTO,
) -> Callable[..., object]:
    """Factoría de un solo vídeo: `(segment_duration_s, segment_count, window) -> ladder fiel`."""

    def factory(segment_duration_s: float, segment_count: int, window: object = None) -> object:
        return _escalera_fiel_desde_perfil(perfil_medio, segment_duration_s, segment_count, max_buffer_s)

    return factory


def factoria_escalera_multivideo(
    perfiles_medio: Sequence[PerfilTamanosSegmentos],
    *,
    max_buffer_s: float = MAX_BUFFER_S_POR_DEFECTO,
) -> Callable[..., object]:
    """Factoría multi-vídeo: rota el medio por ventana (determinista por window_id)."""
    import hashlib

    profiles = list(perfiles_medio)
    if not profiles:
        raise ErrorDatasetMpcPrudente("media_profiles vacío")

    def factory(segment_duration_s: float, segment_count: int, window: object = None) -> object:
        if window is None:
            chosen = profiles[0]
        else:
            window_id = str(window.get("window_id", "")) if isinstance(window, Mapping) else str(window)
            index = int(hashlib.sha256(window_id.encode("utf-8")).hexdigest(), 16) % len(profiles)
            chosen = profiles[index]
        return _escalera_fiel_desde_perfil(chosen, segment_duration_s, segment_count, max_buffer_s)

    return factory


def construir_dataset_mpc_prudente(
    phase3_manifest: Mapping[str, object],
    output_dir: object,
    profile: Phase45V3DatasetProfile,
    *,
    media_profile_id: str = ID_PERFIL_MEDIO_PILOTO,
    dir_base_perfiles: str | None = None,
    max_buffer_s: float = MAX_BUFFER_S_POR_DEFECTO,
    source_manifest_path: object | None = None,
    overwrite: bool = False,
    max_training_windows: int | None = None,
    max_validation_windows: int | None = None,
    trace_path_rewrites: Sequence[PathRewriteRule] = (),
    horizon_segments: int = DEFAULT_THROUGHPUT_QUANTILE_HORIZON,
    quantiles: Sequence[float] = DEFAULT_THROUGHPUT_QUANTILES,
) -> Mapping[str, object]:
    perfil_medio = PerfilTamanosSegmentos.cargar_por_id(
        media_profile_id, base_dir=dir_base_perfiles
    )
    factory = factoria_escalera_fiel(perfil_medio, max_buffer_s=max_buffer_s)
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


def construir_dataset_multimedia_mpc_prudente(
    phase3_manifest: Mapping[str, object],
    output_dir: object,
    profile: Phase45V3DatasetProfile,
    *,
    media_profile_ids: Sequence[str] = IDS_PERFILES_MULTIMEDIA,
    dir_base_perfiles: str | None = None,
    max_buffer_s: float = MAX_BUFFER_S_POR_DEFECTO,
    source_manifest_path: object | None = None,
    overwrite: bool = False,
    max_training_windows: int | None = None,
    max_validation_windows: int | None = None,
    trace_path_rewrites: Sequence[PathRewriteRule] = (),
    horizon_segments: int = DEFAULT_THROUGHPUT_QUANTILE_HORIZON,
    quantiles: Sequence[float] = DEFAULT_THROUGHPUT_QUANTILES,
) -> Mapping[str, object]:
    """Dataset multi-vídeo: cada ventana de red rota entre los medios de 4 s,
    para que la dinámica de buffer no quede sesgada a un solo vídeo."""
    perfiles_medio = [
        PerfilTamanosSegmentos.cargar_por_id(str(mid), base_dir=dir_base_perfiles)
        for mid in media_profile_ids
    ]
    factory = factoria_escalera_multivideo(perfiles_medio, max_buffer_s=max_buffer_s)
    result = build_phase45_v3_throughput_quantile_dataset(
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
    return {**result, "media_profile_ids": [str(mid) for mid in media_profile_ids]}

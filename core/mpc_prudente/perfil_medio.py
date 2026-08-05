"""Tamaños reales (VBR) de segmento por representación.

Carga los descriptores de `perfiles_medio/segment_sizes/<id>.json` (extraídos del
servidor con `scripts/extraer_tamanos_reales_segmentos.py`) y construye un ladder
compatible con `ContentLadder` cuyo `segment_size_bytes()` devuelve el peso real
del segmento, no la aproximación CBR `bitrate * duración / 8`.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Mapping, Sequence

from core.neural_abr.content_ladder import ContentLadderError, Representation

SCHEMA_ID_TAMANOS_SEGMENTOS = "media_profile_segment_sizes_v1"
MAX_BUFFER_S_POR_DEFECTO = 60.0

RAIZ_REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIR_TAMANOS_SEGMENTOS = os.path.join(RAIZ_REPO, "media_profiles", "segment_sizes")

# Los ids de media de Phase 6 (cortos) mapean a los ids de descriptor (del MPD real).
MAPA_ID_FASE6_A_DESCRIPTOR = {
    "paseo_10min_30fps_4s": "paseo_almunecar_10min_30fps_4s",
    "paseo_10min_60fps_4s": "paseo_almunecar_10min_60fps_4s",
    "blender_10min_30fps_4s": "blender_sunflower_10min_30fps_4s",
    "blender_10min_60fps_4s": "blender_sunflower_10min_60fps_4s",
    "preflight_paseo_1min_30fps_4s": "paseo_almunecar_1min_30fps_4s",
}


def resolver_id_descriptor_medio(media_profile_id: str, *, base_dir: str | None = None) -> str:
    """Resuelve un id de Phase 6 (corto) al id de descriptor VBR (del MPD real)."""
    directory = base_dir or DIR_TAMANOS_SEGMENTOS
    mid = str(media_profile_id)
    if os.path.isfile(os.path.join(directory, mid + ".json")):
        return mid
    return MAPA_ID_FASE6_A_DESCRIPTOR.get(mid, mid)


class ErrorPerfilMedio(ValueError):
    """Error por descriptor de perfil de medio ausente o malformado."""


@dataclass(frozen=True)
class EscaleraFiel:
    """Ladder con la interfaz de `ContentLadder` pero tamaños reales por segmento."""

    media_profile_id: str
    representations: tuple[Representation, ...]
    segment_duration_s: float
    segment_count: int  # longitud de la ventana (puede diferir del medio real)
    max_buffer_s: float
    # tabla real completa: _segment_bytes[representation_index][segment_real] = bytes
    _segment_bytes: tuple[tuple[int, ...], ...]
    real_segment_count: int
    start_offset: int = 0

    @property
    def representation_count(self) -> int:
        return len(self.representations)

    @property
    def bitrates_bps(self) -> tuple[int, ...]:
        return tuple(rep.bitrate_bps for rep in self.representations)

    @property
    def min_bitrate_bps(self) -> int:
        return min(self.bitrates_bps)

    @property
    def max_bitrate_bps(self) -> int:
        return max(self.bitrates_bps)

    def bitrate_bps(self, representation_index: int) -> int:
        self.validate_representation_index(representation_index)
        return self.representations[representation_index].bitrate_bps

    def validate_representation_index(self, representation_index: int) -> None:
        if isinstance(representation_index, bool) or not isinstance(representation_index, int):
            raise ContentLadderError("representation_index debe ser un entero")
        if representation_index < 0 or representation_index >= self.representation_count:
            raise ContentLadderError("representation_index fuera de la escalera")

    def segment_size_bytes(self, representation_index: int, segment_index: int) -> int:
        self.validate_representation_index(representation_index)
        if isinstance(segment_index, bool) or not isinstance(segment_index, int):
            raise ContentLadderError("segment_index debe ser un entero")
        if segment_index < 0 or segment_index >= self.segment_count:
            raise ContentLadderError("segment_index fuera de la duracion del contenido")
        # Ventanas más largas que el medio real ciclan sobre los segmentos reales.
        indice_real = (self.start_offset + segment_index) % self.real_segment_count
        return int(self._segment_bytes[representation_index][indice_real])

    def cbr_nominal_bytes(self, representation_index: int) -> float:
        return self.bitrate_bps(representation_index) * self.segment_duration_s / 8.0

    def to_manifest(self) -> Mapping[str, object]:
        return {
            "media_profile_id": self.media_profile_id,
            "representation_count": self.representation_count,
            "bitrates_bps": list(self.bitrates_bps),
            "segment_duration_s": self.segment_duration_s,
            "segment_count": self.segment_count,
            "max_buffer_s": self.max_buffer_s,
            "segment_size_source": "real_vbr_from_server",
        }


@dataclass(frozen=True)
class PerfilTamanosSegmentos:
    """Descriptor cargado de `perfiles_medio/segment_sizes/<id>.json`."""

    media_profile_id: str
    mpd_url: str
    segment_duration_s: float
    segment_count: int
    representation_count: int
    bitrates_bps: tuple[int, ...]
    # _segment_bytes[representation_index][segment_index]; index 0 = bitrate más bajo
    _segment_bytes: tuple[tuple[int, ...], ...]
    vbr_cv_max: float

    @classmethod
    def cargar(cls, path: str) -> "PerfilTamanosSegmentos":
        if not os.path.isfile(path):
            raise ErrorPerfilMedio("media profile no encontrado: {0}".format(path))
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
        return cls.desde_dict(data)

    @classmethod
    def cargar_por_id(cls, media_profile_id: str, *, base_dir: str | None = None) -> "PerfilTamanosSegmentos":
        directory = base_dir or DIR_TAMANOS_SEGMENTOS
        resolved = resolver_id_descriptor_medio(media_profile_id, base_dir=directory)
        return cls.cargar(os.path.join(directory, resolved + ".json"))

    @classmethod
    def desde_dict(cls, data: Mapping[str, object]) -> "PerfilTamanosSegmentos":
        if data.get("schema_id") != SCHEMA_ID_TAMANOS_SEGMENTOS:
            raise ErrorPerfilMedio(
                "schema_id inesperado: {0}".format(data.get("schema_id"))
            )
        reps_raw = data.get("representations")
        if not isinstance(reps_raw, Sequence) or not reps_raw:
            raise ErrorPerfilMedio("descriptor sin representations")

        reps_sorted = sorted(reps_raw, key=lambda r: int(r["bandwidth_bps"]))
        bitrates: list[int] = []
        segment_bytes: list[tuple[int, ...]] = []
        seg_counts: set[int] = set()
        for rep in reps_sorted:
            bitrates.append(int(rep["bandwidth_bps"]))
            sizes = tuple(int(v) for v in rep["segment_bytes"])
            if not sizes:
                raise ErrorPerfilMedio("representation sin segment_bytes")
            if any(v <= 0 for v in sizes):
                raise ErrorPerfilMedio("segment_bytes con valores no positivos")
            segment_bytes.append(sizes)
            seg_counts.add(len(sizes))
        if len(seg_counts) != 1:
            raise ErrorPerfilMedio(
                "representations con distinto número de segmentos: {0}".format(sorted(seg_counts))
            )

        return cls(
            media_profile_id=str(data["media_profile_id"]),
            mpd_url=str(data.get("mpd_url", "")),
            segment_duration_s=float(data["segment_duration_s"]),
            segment_count=int(seg_counts.pop()),
            representation_count=len(reps_sorted),
            bitrates_bps=tuple(bitrates),
            _segment_bytes=tuple(segment_bytes),
            vbr_cv_max=float(data.get("vbr_cv_max", 0.0)),
        )

    def segment_size_bytes(self, representation_index: int, segment_index: int) -> int:
        return int(self._segment_bytes[representation_index][segment_index])

    def a_escalera_fiel(
        self,
        *,
        max_buffer_s: float = MAX_BUFFER_S_POR_DEFECTO,
        segment_count: int | None = None,
        start_offset: int = 0,
    ) -> EscaleraFiel:
        count = self.segment_count if segment_count is None else int(segment_count)
        if count <= 0:
            raise ErrorPerfilMedio("segment_count debe ser positivo: {0}".format(count))
        representations = tuple(
            Representation(representation_index=index, bitrate_bps=int(bitrate))
            for index, bitrate in enumerate(self.bitrates_bps)
        )
        return EscaleraFiel(
            media_profile_id=self.media_profile_id,
            representations=representations,
            segment_duration_s=self.segment_duration_s,
            segment_count=count,
            max_buffer_s=float(max_buffer_s),
            _segment_bytes=self._segment_bytes,
            real_segment_count=self.segment_count,
            start_offset=int(start_offset) % self.segment_count,
        )

    def comparacion_cbr(self) -> Mapping[str, object]:
        """Evidencia VBR: real vs CBR nominal por representación (para la memoria)."""
        rows = []
        for index, bitrate in enumerate(self.bitrates_bps):
            sizes = self._segment_bytes[index]
            mean = sum(sizes) / len(sizes)
            cbr = bitrate * self.segment_duration_s / 8.0
            rows.append(
                {
                    "representation_index": index,
                    "bandwidth_bps": bitrate,
                    "real_mean_bytes": mean,
                    "real_max_bytes": float(max(sizes)),
                    "cbr_nominal_bytes": cbr,
                    "real_mean_vs_cbr": (mean / cbr) if cbr > 0 else 0.0,
                    "real_max_vs_cbr": (max(sizes) / cbr) if cbr > 0 else 0.0,
                }
            )
        return {"media_profile_id": self.media_profile_id, "representations": rows}


def perfiles_medio_disponibles(base_dir: str | None = None) -> tuple[str, ...]:
    directory = base_dir or DIR_TAMANOS_SEGMENTOS
    if not os.path.isdir(directory):
        return ()
    ids = [
        name[:-5]
        for name in os.listdir(directory)
        if name.endswith(".json")
    ]
    return tuple(sorted(ids))

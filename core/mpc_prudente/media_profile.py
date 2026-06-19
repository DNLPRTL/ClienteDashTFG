"""Perfil de medio fiel: tamaños reales (VBR) de segmento del servidor DASH.

Carga los descriptores generados por `scripts/extraer_tamanos_reales_segmentos.py`
(`media_profiles/segment_sizes/<id>.json`, schema `media_profile_segment_sizes_v1`)
y expone un "ladder fiel" compatible con el `ContentLadder` clásico, pero cuyo
`segment_size_bytes(representation_index, segment_index)` devuelve el peso REAL del
segmento medido en el servidor, no `bitrate * duración / 8` (CBR).

Ese ladder fiel se usa tal cual en `core.phase45_v3.abr_closed_loop_env` y en
cualquier rollout/planner: el motor llama `ladder.segment_size_bytes(...)` por
duck-typing, así que la física de descarga pasa a ser la real sin tocar el código
congelado de `phase45_v3`.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Mapping, Sequence

from core.neural_abr.content_ladder import ContentLadderError, Representation

MEDIA_PROFILE_SEGMENT_SIZES_SCHEMA_ID = "media_profile_segment_sizes_v1"
DEFAULT_MAX_BUFFER_S = 60.0

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEGMENT_SIZES_DIR = os.path.join(REPO_ROOT, "media_profiles", "segment_sizes")


class MediaProfileError(ValueError):
    """Raised when a media profile descriptor is missing or malformed."""


@dataclass(frozen=True)
class MediaFaithfulLadder:
    """Ladder con tamaños reales de segmento, compatible con `ContentLadder`.

    Implementa la misma interfaz pública que `ContentLadder` (duck-typing) salvo
    que `segment_size_bytes` lee de una tabla real por segmento.
    """

    media_profile_id: str
    representations: tuple[Representation, ...]
    segment_duration_s: float
    segment_count: int
    max_buffer_s: float
    # tabla real: _segment_bytes[representation_index][segment_index] = bytes
    _segment_bytes: tuple[tuple[int, ...], ...]

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
            raise ContentLadderError("representation_index must be an integer")
        if representation_index < 0 or representation_index >= self.representation_count:
            raise ContentLadderError("representation_index is outside the ladder")

    def segment_size_bytes(self, representation_index: int, segment_index: int) -> int:
        self.validate_representation_index(representation_index)
        if isinstance(segment_index, bool) or not isinstance(segment_index, int):
            raise ContentLadderError("segment_index must be an integer")
        if segment_index < 0 or segment_index >= self.segment_count:
            raise ContentLadderError("segment_index is outside the content duration")
        return int(self._segment_bytes[representation_index][segment_index])

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
class MediaProfileSegmentSizes:
    """Descriptor cargado de `media_profiles/segment_sizes/<id>.json`."""

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
    def load(cls, path: str) -> "MediaProfileSegmentSizes":
        if not os.path.isfile(path):
            raise MediaProfileError("media profile no encontrado: {0}".format(path))
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
        return cls.from_mapping(data)

    @classmethod
    def load_by_id(cls, media_profile_id: str, *, base_dir: str | None = None) -> "MediaProfileSegmentSizes":
        directory = base_dir or SEGMENT_SIZES_DIR
        return cls.load(os.path.join(directory, media_profile_id + ".json"))

    @classmethod
    def from_mapping(cls, data: Mapping[str, object]) -> "MediaProfileSegmentSizes":
        if data.get("schema_id") != MEDIA_PROFILE_SEGMENT_SIZES_SCHEMA_ID:
            raise MediaProfileError(
                "schema_id inesperado: {0}".format(data.get("schema_id"))
            )
        reps_raw = data.get("representations")
        if not isinstance(reps_raw, Sequence) or not reps_raw:
            raise MediaProfileError("descriptor sin representations")

        reps_sorted = sorted(reps_raw, key=lambda r: int(r["bandwidth_bps"]))
        bitrates: list[int] = []
        segment_bytes: list[tuple[int, ...]] = []
        seg_counts: set[int] = set()
        for rep in reps_sorted:
            bitrates.append(int(rep["bandwidth_bps"]))
            sizes = tuple(int(v) for v in rep["segment_bytes"])
            if not sizes:
                raise MediaProfileError("representation sin segment_bytes")
            if any(v <= 0 for v in sizes):
                raise MediaProfileError("segment_bytes con valores no positivos")
            segment_bytes.append(sizes)
            seg_counts.add(len(sizes))
        if len(seg_counts) != 1:
            raise MediaProfileError(
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

    def to_faithful_ladder(
        self,
        *,
        max_buffer_s: float = DEFAULT_MAX_BUFFER_S,
        segment_count: int | None = None,
    ) -> MediaFaithfulLadder:
        count = self.segment_count if segment_count is None else int(segment_count)
        if count <= 0 or count > self.segment_count:
            raise MediaProfileError(
                "segment_count fuera de rango (1..{0}): {1}".format(self.segment_count, count)
            )
        representations = tuple(
            Representation(representation_index=index, bitrate_bps=int(bitrate))
            for index, bitrate in enumerate(self.bitrates_bps)
        )
        clipped = tuple(rep_sizes[:count] for rep_sizes in self._segment_bytes)
        return MediaFaithfulLadder(
            media_profile_id=self.media_profile_id,
            representations=representations,
            segment_duration_s=self.segment_duration_s,
            segment_count=count,
            max_buffer_s=float(max_buffer_s),
            _segment_bytes=clipped,
        )

    def cbr_comparison(self) -> Mapping[str, object]:
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


def available_media_profiles(base_dir: str | None = None) -> tuple[str, ...]:
    directory = base_dir or SEGMENT_SIZES_DIR
    if not os.path.isdir(directory):
        return ()
    ids = [
        name[:-5]
        for name in os.listdir(directory)
        if name.endswith(".json")
    ]
    return tuple(sorted(ids))

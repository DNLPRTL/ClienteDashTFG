from __future__ import annotations

from typing import Type

from core.trace_replay.converters.base import BaseTraceConverter
from core.trace_replay.converters.fcc_mba import FccMbaConverter
from core.trace_replay.converters.gavist5g import Gavist5GConverter
from core.trace_replay.converters.interval_logs import Ghent4GLteConverter, NorwayHsdpaConverter
from core.trace_replay.converters.lumos5g import Lumos5GConverter
from core.trace_replay.converters.nyu_mets import NyuMetsConverter
from core.trace_replay.converters.oboe import OboeConverter
from core.trace_replay.converters.puffer import PufferConverter
from core.trace_replay.converters.roma import RomaActiveThroughputConverter
from core.trace_replay.converters.ucc import Ucc4GBeyondThroughputConverter, Ucc5GBeyondThroughputConverter


CONVERTER_CLASSES: tuple[Type[BaseTraceConverter], ...] = (
    NorwayHsdpaConverter,
    Ghent4GLteConverter,
    Ucc4GBeyondThroughputConverter,
    Ucc5GBeyondThroughputConverter,
    OboeConverter,
    NyuMetsConverter,
    Lumos5GConverter,
    FccMbaConverter,
    RomaActiveThroughputConverter,
    Gavist5GConverter,
    PufferConverter,
)


def available_converters() -> tuple[str, ...]:
    return tuple(cls.dataset_id for cls in CONVERTER_CLASSES)


def converter_by_id(dataset_id: str) -> Type[BaseTraceConverter]:
    for cls in CONVERTER_CLASSES:
        if cls.dataset_id == dataset_id:
            return cls
    raise KeyError("unknown dataset converter: {0}".format(dataset_id))

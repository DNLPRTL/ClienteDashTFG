"""Dataset converters for normalized Phase 3 traces."""

from __future__ import annotations

from core.trace_replay.converters.base import ConversionBatchResult, ConvertedTrace, ConversionError
from core.trace_replay.converters.ghent_4g import convert_ghent_4g
from core.trace_replay.converters.hsdpa_norway import convert_hsdpa_norway
from core.trace_replay.converters.lancaster_abr import convert_lancaster_abr


DATASET_CONVERTERS = {
    "hsdpa_norway_mmsys2013": convert_hsdpa_norway,
    "ghent_4g_lte_bandwidth_logs": convert_ghent_4g,
    "lancaster_abr_throughput_traces": convert_lancaster_abr,
}


def convert_dataset(dataset_id, input_dir, output_dir, manifest_dir, max_traces=None, overwrite=False):
    try:
        converter = DATASET_CONVERTERS[dataset_id]
    except KeyError as exc:
        raise ConversionError("unknown dataset_id: {0}".format(dataset_id)) from exc
    return converter(
        input_dir=input_dir,
        output_dir=output_dir,
        manifest_dir=manifest_dir,
        max_traces=max_traces,
        overwrite=overwrite,
    )


__all__ = [
    "ConversionBatchResult",
    "ConvertedTrace",
    "ConversionError",
    "DATASET_CONVERTERS",
    "convert_dataset",
    "convert_ghent_4g",
    "convert_hsdpa_norway",
    "convert_lancaster_abr",
]

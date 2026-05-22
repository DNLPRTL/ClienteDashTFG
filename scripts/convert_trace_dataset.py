"""Convert a raw Phase 3 trace dataset into normalized trace CSVs."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.trace_replay.converters import ConversionError, convert_dataset


def main(argv=None):
    parser = argparse.ArgumentParser(description="Convert raw trace dataset files to normalized_trace_schema_v1.")
    parser.add_argument("--dataset", required=True, choices=[
        "hsdpa_norway_mmsys2013",
        "ghent_4g_lte_bandwidth_logs",
        "lancaster_abr_throughput_traces",
    ])
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--manifest-dir", required=True)
    parser.add_argument("--max-traces", type=int, default=None)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    try:
        result = convert_dataset(
            dataset_id=args.dataset,
            input_dir=args.input_dir,
            output_dir=args.output_dir,
            manifest_dir=args.manifest_dir,
            max_traces=args.max_traces,
            overwrite=args.overwrite,
        )
    except ConversionError as exc:
        print("dataset_id: {0}".format(args.dataset))
        print("input_dir: {0}".format(args.input_dir))
        print("output_dir: {0}".format(args.output_dir))
        print("manifest_dir: {0}".format(args.manifest_dir))
        print("error: {0}".format(exc))
        return 1

    print("dataset_id: {0}".format(result.dataset_id))
    print("input_dir: {0}".format(result.input_dir))
    print("output_dir: {0}".format(result.output_dir))
    print("manifest_dir: {0}".format(result.manifest_dir))
    print("converted trace count: {0}".format(len(result.converted_traces)))
    print("skipped input count: {0}".format(len(result.skipped_inputs)))
    if result.errors:
        print("errors:")
        for error in result.errors:
            print("- {0}".format(error))

    if not result.converted_traces or result.errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

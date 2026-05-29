#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.neural_abr.constants import PHASE4E1_SPLIT_POLICY, PRIMARY_TEACHER
from core.neural_abr.dataset_builder import build_external_trace_dataset, build_synthetic_smoke_dataset


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build an offline NeuralABR-Lite dataset.")
    parser.add_argument("--synthetic-smoke", action="store_true", help="Build the diagnostic synthetic smoke dataset.")
    parser.add_argument("--trace-csv-root", help="Root directory containing normalized external trace CSV files.")
    parser.add_argument("--trace-manifest-root", help="Root directory containing trace manifest JSON files.")
    parser.add_argument("--split-policy", default=PHASE4E1_SPLIT_POLICY)
    parser.add_argument("--representation-kbps", default="300,750,1200,1850,2850")
    parser.add_argument("--segment-duration-s", type=float, default=4.0)
    parser.add_argument("--teacher", default=PRIMARY_TEACHER)
    parser.add_argument("--seed", type=int, default=123)
    parser.add_argument("--diagnostic-only", action="store_true")
    parser.add_argument("--output-dir", required=True, help="Output directory outside the repository.")
    parser.add_argument("--overwrite", action="store_true", help="Replace the output directory if it exists.")
    args = parser.parse_args(argv)

    if args.synthetic_smoke:
        result = build_synthetic_smoke_dataset(args.output_dir, overwrite=args.overwrite)
    else:
        if not args.trace_csv_root:
            parser.error("external trace mode requires --trace-csv-root")
        try:
            representation_kbps = _parse_representation_kbps(args.representation_kbps)
        except argparse.ArgumentTypeError as exc:
            parser.error(str(exc))
        result = build_external_trace_dataset(
            trace_csv_root=args.trace_csv_root,
            trace_manifest_root=args.trace_manifest_root,
            output_dir=args.output_dir,
            split_policy=args.split_policy,
            representation_kbps=representation_kbps,
            segment_duration_s=args.segment_duration_s,
            teacher=args.teacher,
            seed=args.seed,
            diagnostic_only=args.diagnostic_only,
            overwrite=args.overwrite,
        )

    print("NeuralABR-Lite dataset build summary")
    print("dataset_dir: {0}".format(result["dataset_dir"]))
    print("sample_counts: {0}".format(json.dumps(result["sample_counts"], sort_keys=True)))
    print("diagnostic_only: true")
    return 0


def _parse_representation_kbps(value: str) -> tuple[int, ...]:
    parts = [part.strip() for part in str(value).split(",") if part.strip()]
    if not parts:
        raise argparse.ArgumentTypeError("representation-kbps must not be empty")
    try:
        parsed = tuple(int(part) for part in parts)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("representation-kbps must be comma-separated integers") from exc
    if any(part <= 0 for part in parsed):
        raise argparse.ArgumentTypeError("representation-kbps values must be positive")
    return parsed


if __name__ == "__main__":
    raise SystemExit(main())

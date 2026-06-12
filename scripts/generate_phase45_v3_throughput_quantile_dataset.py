#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.phase45_v1.paths import parse_rewrite_rules
from core.phase45_v3.dataset import build_default_phase45_v3_trace_path_rewrites, load_phase3_manifest
from core.phase45_v3.profiles import PROFILES, profile_by_name
from core.phase45_v3.throughput_quantile_dataset import (
    DEFAULT_THROUGHPUT_QUANTILE_HORIZON,
    DEFAULT_THROUGHPUT_QUANTILES,
    build_phase45_v3_throughput_quantile_dataset,
    validate_phase45_v3_throughput_quantile_dataset_dir,
)


TFG_ROOT = REPO_ROOT.parent
DEFAULT_MANIFEST = TFG_ROOT / "manifests_trazas" / "phase3" / "final" / "phase3_trace_manifest_curated.json"
DEFAULT_OUTPUT_ROOT = TFG_ROOT / "datasets_normalizados" / "phase45_v3"
DEFAULT_REPRESENTATION_KBPS = (300, 750, 1200, 1850, 2850, 4300)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Construye el dataset Phase45 v3 de cuantiles de throughput para Neural-MPC."
    )
    parser.add_argument("--profile", choices=sorted(PROFILES), default="smoke")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--tfg-root", type=Path, default=TFG_ROOT)
    parser.add_argument("--max-training-windows", type=int, default=None)
    parser.add_argument("--max-validation-windows", type=int, default=None)
    parser.add_argument("--horizon", type=int, default=DEFAULT_THROUGHPUT_QUANTILE_HORIZON)
    parser.add_argument("--quantiles", default=",".join(str(value) for value in DEFAULT_THROUGHPUT_QUANTILES))
    parser.add_argument("--representation-kbps", default=",".join(str(value) for value in DEFAULT_REPRESENTATION_KBPS))
    parser.add_argument("--trace-path-rewrite", action="append", default=[], metavar="OLD=NEW")
    parser.add_argument("--no-default-trace-path-rewrites", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args(argv)

    output_dir = args.output_dir or DEFAULT_OUTPUT_ROOT / "throughput_quantile_{0}_v1".format(args.profile)
    if args.validate_only:
        validation = validate_phase45_v3_throughput_quantile_dataset_dir(output_dir)
        print(json.dumps(validation, indent=2, sort_keys=True))
        return 0 if validation["status"] == "PASS" else 1

    rewrites = []
    if not args.no_default_trace_path_rewrites:
        rewrites.extend(build_default_phase45_v3_trace_path_rewrites(args.tfg_root))
    rewrites.extend(parse_rewrite_rules(args.trace_path_rewrite))

    result = build_phase45_v3_throughput_quantile_dataset(
        load_phase3_manifest(args.manifest),
        output_dir=output_dir,
        profile=profile_by_name(args.profile),
        source_manifest_path=args.manifest,
        overwrite=args.overwrite,
        max_training_windows=args.max_training_windows,
        max_validation_windows=args.max_validation_windows,
        representation_kbps=_parse_ints(args.representation_kbps, "--representation-kbps"),
        trace_path_rewrites=tuple(rewrites),
        horizon_segments=int(args.horizon),
        quantiles=_parse_floats(args.quantiles, "--quantiles"),
    )
    validation = validate_phase45_v3_throughput_quantile_dataset_dir(output_dir)
    payload = {
        "status": "PASS" if result["status"] == "PASS" and validation["status"] == "PASS" else "FAIL",
        "dataset_generation": result,
        "dataset_validation": validation,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["status"] == "PASS" else 1


def _parse_ints(raw: str, option_name: str) -> tuple[int, ...]:
    values = tuple(int(part.strip()) for part in str(raw).split(",") if part.strip())
    if not values or any(value <= 0 for value in values):
        raise argparse.ArgumentTypeError("{0} must contain positive integers".format(option_name))
    return values


def _parse_floats(raw: str, option_name: str) -> tuple[float, ...]:
    values = tuple(float(part.strip()) for part in str(raw).split(",") if part.strip())
    if not values:
        raise argparse.ArgumentTypeError("{0} must not be empty".format(option_name))
    return values


if __name__ == "__main__":
    raise SystemExit(main())

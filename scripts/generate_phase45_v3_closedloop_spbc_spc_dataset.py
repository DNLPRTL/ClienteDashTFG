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
from core.phase45_v3.closedloop_spbc_spc_dataset import (
    build_default_phase45_v3_closedloop_spbc_spc_trace_path_rewrites,
    build_phase45_v3_closedloop_spbc_spc_dataset,
    load_phase3_manifest,
    validate_phase45_v3_closedloop_spbc_spc_dataset_dir,
)
from core.phase45_v3.profiles import PROFILES, profile_by_name


TFG_ROOT = REPO_ROOT.parent
DEFAULT_MANIFEST = TFG_ROOT / "manifests_trazas" / "phase3" / "final" / "phase3_trace_manifest_curated.json"
DEFAULT_OUTPUT_ROOT = TFG_ROOT / "datasets_normalizados" / "phase45_v3"
DEFAULT_REPRESENTATION_KBPS = (300, 750, 1200, 1850, 2850, 4300)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Construye el dataset Phase45 v3 closed-loop SPBC/SPC con targets policy+critic."
    )
    parser.add_argument("--profile", choices=sorted(PROFILES), default="smoke")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--tfg-root", type=Path, default=TFG_ROOT)
    parser.add_argument("--max-training-windows", type=int, default=None, help="Limite tecnico opcional.")
    parser.add_argument("--max-validation-windows", type=int, default=None, help="Limite tecnico opcional.")
    parser.add_argument("--representation-kbps", default=",".join(str(value) for value in DEFAULT_REPRESENTATION_KBPS))
    parser.add_argument(
        "--trace-path-rewrite",
        action="append",
        default=[],
        metavar="OLD=NEW",
        help="Reescritura de prefijo para normalized_trace_path; puede repetirse.",
    )
    parser.add_argument(
        "--no-default-trace-path-rewrites",
        action="store_true",
        help="Desactiva reescrituras automaticas Windows/WSL para /home/*/TFG y C:/Users/danie/Documents/TFG.",
    )
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--validate-only", action="store_true", help="Valida un output-dir existente y termina.")
    args = parser.parse_args(argv)

    output_dir = args.output_dir or DEFAULT_OUTPUT_ROOT / "closedloop_spbc_spc_{0}_v1".format(args.profile)
    if args.validate_only:
        validation = validate_phase45_v3_closedloop_spbc_spc_dataset_dir(output_dir)
        print(json.dumps(validation, indent=2, sort_keys=True))
        return 0 if validation["status"] == "PASS" else 1

    profile = profile_by_name(args.profile)
    representation_kbps = _parse_representation_kbps(args.representation_kbps)
    rewrites = []
    if not args.no_default_trace_path_rewrites:
        rewrites.extend(build_default_phase45_v3_closedloop_spbc_spc_trace_path_rewrites(args.tfg_root))
    rewrites.extend(parse_rewrite_rules(args.trace_path_rewrite))

    manifest = load_phase3_manifest(args.manifest)
    result = build_phase45_v3_closedloop_spbc_spc_dataset(
        manifest,
        output_dir=output_dir,
        profile=profile,
        source_manifest_path=args.manifest,
        overwrite=args.overwrite,
        max_training_windows=args.max_training_windows,
        max_validation_windows=args.max_validation_windows,
        representation_kbps=representation_kbps,
        trace_path_rewrites=tuple(rewrites),
    )
    validation = validate_phase45_v3_closedloop_spbc_spc_dataset_dir(output_dir)
    payload = {
        "status": "PASS" if result["status"] == "PASS" and validation["status"] == "PASS" else "FAIL",
        "dataset_generation": result,
        "dataset_validation": validation,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["status"] == "PASS" else 1


def _parse_representation_kbps(value: str) -> tuple[int, ...]:
    parts = [part.strip() for part in str(value).split(",") if part.strip()]
    if not parts:
        raise argparse.ArgumentTypeError("representation-kbps must not be empty")
    parsed = tuple(int(part) for part in parts)
    if any(part <= 0 for part in parsed):
        raise argparse.ArgumentTypeError("representation-kbps values must be positive")
    return parsed


if __name__ == "__main__":
    raise SystemExit(main())

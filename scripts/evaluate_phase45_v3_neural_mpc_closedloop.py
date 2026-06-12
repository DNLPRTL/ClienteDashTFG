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
from core.phase45_v3.neural_mpc_evaluation import evaluate_phase45_v3_neural_mpc_closed_loop
from core.phase45_v3.profiles import PROFILES, profile_by_name


TFG_ROOT = REPO_ROOT.parent
DEFAULT_MANIFEST = TFG_ROOT / "manifests_trazas" / "phase3" / "final" / "phase3_trace_manifest_curated.json"
DEFAULT_RUN_ROOT = TFG_ROOT / "runs_phase45_v3"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Evalua Neural-MPC Phase45 v3 en closed-loop offline diagnostico.")
    parser.add_argument("--profile", choices=sorted(PROFILES), default="pilot")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--predictor-checkpoint", type=Path, required=True)
    parser.add_argument("--controllers", default="robust_mpc,bola,throughput_rule,neural_mpc")
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--preset", default="diagnostic")
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--tfg-root", type=Path, default=TFG_ROOT)
    parser.add_argument("--max-validation-windows", type=int, default=None)
    parser.add_argument("--trace-path-rewrite", action="append", default=[], metavar="OLD=NEW")
    parser.add_argument("--no-default-trace-path-rewrites", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--fail-on-collapse", action="store_true")
    args = parser.parse_args(argv)

    rewrites = []
    if not args.no_default_trace_path_rewrites:
        rewrites.extend(build_default_phase45_v3_trace_path_rewrites(args.tfg_root))
    rewrites.extend(parse_rewrite_rules(args.trace_path_rewrite))
    output_dir = args.output_dir or DEFAULT_RUN_ROOT / "neural_mpc_{0}_{1}".format(args.profile, args.preset)
    report = evaluate_phase45_v3_neural_mpc_closed_loop(
        load_phase3_manifest(args.manifest),
        output_dir=output_dir,
        profile=profile_by_name(args.profile),
        predictor_checkpoint=args.predictor_checkpoint,
        controllers=_parse_csv(args.controllers),
        preset=args.preset,
        source_manifest_path=args.manifest,
        overwrite=args.overwrite,
        max_validation_windows=args.max_validation_windows,
        trace_path_rewrites=tuple(rewrites),
        device=args.device,
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    if args.fail_on_collapse and report["status"] != "PASS":
        return 1
    return 0


def _parse_csv(raw: str) -> tuple[str, ...]:
    values = tuple(part.strip() for part in str(raw).split(",") if part.strip())
    if not values:
        raise argparse.ArgumentTypeError("controllers must not be empty")
    return values


if __name__ == "__main__":
    raise SystemExit(main())

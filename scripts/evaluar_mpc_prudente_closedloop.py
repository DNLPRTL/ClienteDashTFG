#!/usr/bin/env python3
"""Diagnóstico closed-loop offline de MPC Prudente (entorno FIEL).

Compara el controller prudente vs robust_mpc/bola/neural_mpc viejo sobre ventanas
de validación. No es benchmark ni ranking.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.mpc_prudente.dataset import DEFAULT_PILOT_MEDIA_PROFILE_ID
from core.mpc_prudente.evaluation import evaluate_mpc_prudente_closed_loop
from core.mpc_prudente.planner import MPC_PRUDENTE_CONTROLLER_KEY
from core.phase45_v1.paths import parse_rewrite_rules
from core.phase45_v3.dataset import build_default_phase45_v3_trace_path_rewrites, load_phase3_manifest
from core.phase45_v3.neural_mpc_training import THROUGHPUT_QUANTILE_MODEL_FILENAME
from core.phase45_v3.profiles import PROFILES, profile_by_name

TFG_ROOT = REPO_ROOT.parent
DEFAULT_MANIFEST = TFG_ROOT / "manifests_trazas" / "phase3" / "final" / "phase3_trace_manifest_curated.json"
DEFAULT_MODEL_ROOT = TFG_ROOT / "modelos" / "mpc_prudente" / "throughput_quantile_predictor"
DEFAULT_OUTPUT_ROOT = TFG_ROOT / "runs_mpc_prudente"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Diagnóstico closed-loop de MPC Prudente.")
    parser.add_argument("--profile", choices=sorted(PROFILES), default="pilot")
    parser.add_argument("--media-profile-id", default=DEFAULT_PILOT_MEDIA_PROFILE_ID)
    parser.add_argument("--predictor-checkpoint", type=Path, default=None)
    parser.add_argument("--train-profile", default="pilot")
    parser.add_argument("--seed", type=int, default=451001)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--tfg-root", type=Path, default=TFG_ROOT)
    parser.add_argument("--controllers", default="{0},robust_mpc,bola,neural_mpc".format(MPC_PRUDENTE_CONTROLLER_KEY))
    parser.add_argument("--max-validation-windows", type=int, default=None)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--trace-path-rewrite", action="append", default=[], metavar="OLD=NEW")
    parser.add_argument("--no-default-trace-path-rewrites", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    checkpoint = args.predictor_checkpoint or (
        DEFAULT_MODEL_ROOT
        / "{0}_{1}_seed{2}".format(args.train_profile, args.media_profile_id, args.seed)
        / THROUGHPUT_QUANTILE_MODEL_FILENAME
    )
    output_dir = args.output_dir or DEFAULT_OUTPUT_ROOT / "diagnostico_{0}_{1}".format(args.profile, args.media_profile_id)

    rewrites = []
    if not args.no_default_trace_path_rewrites:
        rewrites.extend(build_default_phase45_v3_trace_path_rewrites(args.tfg_root))
    rewrites.extend(parse_rewrite_rules(args.trace_path_rewrite))

    report = evaluate_mpc_prudente_closed_loop(
        load_phase3_manifest(args.manifest),
        output_dir=output_dir,
        profile=profile_by_name(args.profile),
        predictor_checkpoint=checkpoint,
        media_profile_id=args.media_profile_id,
        source_manifest_path=args.manifest,
        overwrite=args.overwrite,
        max_validation_windows=args.max_validation_windows,
        controllers=tuple(c.strip() for c in str(args.controllers).split(",") if c.strip()),
        trace_path_rewrites=tuple(rewrites),
        device=args.device,
    )

    print(json.dumps(report, indent=2, sort_keys=True, default=str))
    controllers = report["controllers"]
    prudent = controllers.get(MPC_PRUDENTE_CONTROLLER_KEY, {})
    robust = controllers.get("robust_mpc", {})
    paired = report["paired_vs_robust_mpc"].get(MPC_PRUDENTE_CONTROLLER_KEY, {})
    variable = paired.get("by_variability", {}).get("variable", {})
    print(
        "MPC_PRUDENTE_DIAGNOSTIC status={st} prudent_qoe={pq} robust_qoe={rq} "
        "prudent_rebuffer={pr} robust_rebuffer={rr} qoe_delta={qd} rebuffer_delta={rd} "
        "variable_rebuffer_delta={vrd} fallback={fb} invalid={inv}".format(
            st=report["status"],
            pq=round(float(prudent.get("qoe_linear_mean", 0.0)), 4),
            rq=round(float(robust.get("qoe_linear_mean", 0.0)), 4),
            pr=round(float(prudent.get("total_rebuffer_s", 0.0)), 3),
            rr=round(float(robust.get("total_rebuffer_s", 0.0)), 3),
            qd=round(float(paired.get("qoe_delta_mean", 0.0)), 4),
            rd=round(float(paired.get("rebuffer_delta_s_mean", 0.0)), 4),
            vrd=round(float(variable.get("rebuffer_delta_s_mean", 0.0)), 4),
            fb=prudent.get("fallback_count", 0),
            inv=prudent.get("invalid_action_count", 0),
        )
    )
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

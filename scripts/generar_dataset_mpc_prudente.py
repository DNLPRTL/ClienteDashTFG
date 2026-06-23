#!/usr/bin/env python3
"""Genera el dataset de entrenamiento FIEL (medio VBR real) para MPC Prudente.

Igual que el generador de cuantiles de Neural-MPC, pero usando el peso real de
cada segmento del medio (`--media-profile-id`). No es benchmark ni ranking.
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

from core.mpc_prudente.dataset import (
    DEFAULT_MULTIMEDIA_PROFILE_IDS,
    DEFAULT_PILOT_MEDIA_PROFILE_ID,
    build_mpc_prudente_dataset,
    build_mpc_prudente_multimedia_dataset,
)
from core.phase45_v1.paths import parse_rewrite_rules
from core.phase45_v3.dataset import build_default_phase45_v3_trace_path_rewrites, load_phase3_manifest
from core.phase45_v3.profiles import PROFILES, profile_by_name
from core.phase45_v3.throughput_quantile_dataset import (
    DEFAULT_THROUGHPUT_QUANTILE_HORIZON,
    validate_phase45_v3_throughput_quantile_dataset_dir,
)

TFG_ROOT = REPO_ROOT.parent
DEFAULT_MANIFEST = TFG_ROOT / "manifests_trazas" / "phase3" / "final" / "phase3_trace_manifest_curated.json"
DEFAULT_OUTPUT_ROOT = TFG_ROOT / "datasets_normalizados" / "mpc_prudente"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Dataset fiel (medio VBR real) para MPC Prudente.")
    parser.add_argument("--profile", choices=sorted(PROFILES), default="pilot")
    parser.add_argument("--media-profile-id", default=DEFAULT_PILOT_MEDIA_PROFILE_ID)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--tfg-root", type=Path, default=TFG_ROOT)
    parser.add_argument("--max-training-windows", type=int, default=None)
    parser.add_argument("--max-validation-windows", type=int, default=None)
    parser.add_argument("--horizon", type=int, default=DEFAULT_THROUGHPUT_QUANTILE_HORIZON)
    parser.add_argument("--trace-path-rewrite", action="append", default=[], metavar="OLD=NEW")
    parser.add_argument("--no-default-trace-path-rewrites", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--multimedia", action="store_true", help="rotar los 8 vídeos de 4s por ventana (sin sesgo a uno).")
    args = parser.parse_args(argv)

    media_label = "multimedia" if args.multimedia else args.media_profile_id
    output_dir = args.output_dir or DEFAULT_OUTPUT_ROOT / "throughput_quantile_{0}_{1}".format(
        args.profile, media_label
    )

    if args.validate_only:
        validation = validate_phase45_v3_throughput_quantile_dataset_dir(output_dir)
        print(json.dumps(validation, indent=2, sort_keys=True))
        return 0 if validation["status"] == "PASS" else 1

    rewrites = []
    if not args.no_default_trace_path_rewrites:
        rewrites.extend(build_default_phase45_v3_trace_path_rewrites(args.tfg_root))
    rewrites.extend(parse_rewrite_rules(args.trace_path_rewrite))

    if args.multimedia:
        result = build_mpc_prudente_multimedia_dataset(
            load_phase3_manifest(args.manifest),
            output_dir=output_dir,
            profile=profile_by_name(args.profile),
            media_profile_ids=DEFAULT_MULTIMEDIA_PROFILE_IDS,
            source_manifest_path=args.manifest,
            overwrite=args.overwrite,
            max_training_windows=args.max_training_windows,
            max_validation_windows=args.max_validation_windows,
            trace_path_rewrites=tuple(rewrites),
            horizon_segments=int(args.horizon),
        )
    else:
        result = build_mpc_prudente_dataset(
            load_phase3_manifest(args.manifest),
            output_dir=output_dir,
            profile=profile_by_name(args.profile),
            media_profile_id=args.media_profile_id,
            source_manifest_path=args.manifest,
            overwrite=args.overwrite,
            max_training_windows=args.max_training_windows,
            max_validation_windows=args.max_validation_windows,
            trace_path_rewrites=tuple(rewrites),
            horizon_segments=int(args.horizon),
        )
    validation = validate_phase45_v3_throughput_quantile_dataset_dir(output_dir)
    summary = result["summary"]
    status = "PASS" if result["status"] == "PASS" and validation["status"] == "PASS" else "FAIL"
    payload = {"status": status, "dataset_generation": result, "dataset_validation": validation}
    print(json.dumps(payload, indent=2, sort_keys=True, default=str))

    counts = result["sample_counts"]
    print(
        "MPC_PRUDENTE_DATASET status={st} profile={pr} media={md} "
        "segment_size_source={src} train_samples={tr} val_samples={va} "
        "leakage={lk} skipped_windows={sk} out_dir={od}".format(
            st=status,
            pr=args.profile,
            md=media_label,
            src=summary.get("segment_size_source"),
            tr=counts.get("training"),
            va=counts.get("validation"),
            lk=summary.get("leakage_audit_status"),
            sk=result.get("skipped_window_count"),
            od=output_dir,
        )
    )
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

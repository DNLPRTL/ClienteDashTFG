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

from core.phase45_v1.spc_training import SPC_TRAINING_PROFILES, profile_by_name, train_spc_abr_v1


TFG_ROOT = REPO_ROOT.parent
DEFAULT_DATASET_DIR = TFG_ROOT / "datasets_normalizados" / "phase45_v1" / "phase45v1B_spc_spbc_dataset_v1"
DEFAULT_MODEL_ROOT = TFG_ROOT / "modelos" / "phase45_v1" / "spc_abr_v1"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Entrena offline spc_abr_v1 con el dataset Phase 4-5 v1.")
    parser.add_argument("--profile", choices=sorted(SPC_TRAINING_PROFILES), default="smoke")
    parser.add_argument("--dataset-dir", type=Path, default=DEFAULT_DATASET_DIR)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--device", choices=("auto", "cpu", "cuda"), default="auto")
    parser.add_argument("--epochs", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=None)
    parser.add_argument("--learning-rate", type=float, default=None)
    parser.add_argument("--max-training-samples", type=int, default=None)
    parser.add_argument("--max-validation-samples", type=int, default=None)
    parser.add_argument(
        "--no-profile-sample-limits",
        action="store_true",
        help="Usa todo el dataset aunque el perfil smoke/pilot tenga limites por defecto.",
    )
    parser.add_argument("--skip-dataset-validation", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    profile = profile_by_name(args.profile)
    output_dir = args.output_dir or (DEFAULT_MODEL_ROOT / args.profile)
    max_training_samples = None if args.no_profile_sample_limits else "profile"
    max_validation_samples = None if args.no_profile_sample_limits else "profile"
    if args.max_training_samples is not None:
        max_training_samples = args.max_training_samples
    if args.max_validation_samples is not None:
        max_validation_samples = args.max_validation_samples

    report = train_spc_abr_v1(
        args.dataset_dir,
        output_dir,
        profile=profile,
        overwrite=args.overwrite,
        device=args.device,
        epochs=args.epochs,
        batch_size=args.batch_size,
        learning_rate=args.learning_rate,
        max_training_samples=max_training_samples,
        max_validation_samples=max_validation_samples,
        validate_dataset=not args.skip_dataset_validation,
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

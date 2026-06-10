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

from core.phase45_v1.paths import default_trace_path_rewrites, parse_rewrite_rules
from core.phase45_v1.preference_dataset_v2 import (
    ROLLOUT_SPBC_V2_DPO,
    V2_DAGGER2_DATASET_SCHEMA_ID,
    Phase45V2DatasetBuildError,
    build_phase45_v2_dataset,
    load_phase3_manifest,
    validate_phase45_v2_dataset_dir,
)
from core.phase45_v1.profiles import PROFILES, profile_by_name


TFG_ROOT = REPO_ROOT.parent
DEFAULT_MANIFEST = TFG_ROOT / "manifests_trazas" / "phase3" / "final" / "phase3_trace_manifest_curated.json"
DEFAULT_OUTPUT_DIR = TFG_ROOT / "datasets_normalizados" / "phase45_v1" / "phase45v2_preference_onpolicy_dagger2_dataset_v1"
DEFAULT_SPBC_CHECKPOINT = TFG_ROOT / "modelos" / "phase45_v1" / "spbc_abr_v1" / "full_v1" / "modelo_spbc_abr_v1.pt"
DEFAULT_POLICY_ROLLOUT_CHECKPOINT = (
    TFG_ROOT
    / "modelos"
    / "phase45_v1"
    / "spbc_abr_v2_dpo"
    / "full_v1_utility_risk_v1"
    / "modelo_spbc_abr_v2_dpo.pt"
)
DEFAULT_REPRESENTATION_KBPS = (300, 750, 1200, 1850, 2850, 4300)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Construye un dataset Phase 4-5 v2 DAgger-2 con rollout oracle, "
            "spbc_v1_on_policy y spbc_v2_dpo_on_policy."
        )
    )
    parser.add_argument("--profile", choices=sorted(PROFILES), default="smoke")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--spbc-checkpoint", type=Path, default=DEFAULT_SPBC_CHECKPOINT)
    parser.add_argument("--policy-rollout-checkpoint", type=Path, default=DEFAULT_POLICY_ROLLOUT_CHECKPOINT)
    parser.add_argument(
        "--allow-oracle-only-full",
        action="store_true",
        help="Permite generar full_v1 sin spbc_v1_on_policy; usar solo como diagnostico explicito.",
    )
    parser.add_argument(
        "--allow-no-v2-policy-rollout",
        action="store_true",
        help="Permite omitir spbc_v2_dpo_on_policy; solo diagnostico, no usar para cerrar 7B.",
    )
    parser.add_argument("--device", choices=("auto", "cpu", "cuda"), default="auto")
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
        help="Desactiva reescrituras automaticas Windows/WSL para /home/*/TFG.",
    )
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--validate-only", action="store_true", help="Valida un output-dir existente y termina.")
    args = parser.parse_args(argv)

    if args.validate_only:
        validation = validate_phase45_v2_dataset_dir(args.output_dir)
        print(json.dumps(validation, indent=2, sort_keys=True))
        return 0

    policy_rollout_checkpoint: Path | None = args.policy_rollout_checkpoint
    if not args.allow_no_v2_policy_rollout:
        if policy_rollout_checkpoint is None or not policy_rollout_checkpoint.expanduser().is_file():
            raise Phase45V2DatasetBuildError(
                "DAgger-2 requires an existing --policy-rollout-checkpoint; missing: {0}".format(
                    policy_rollout_checkpoint
                )
            )
    elif policy_rollout_checkpoint is not None and not policy_rollout_checkpoint.expanduser().is_file():
        policy_rollout_checkpoint = None

    profile = profile_by_name(args.profile)
    representation_kbps = _parse_representation_kbps(args.representation_kbps)
    rewrites = []
    if not args.no_default_trace_path_rewrites:
        rewrites.extend(default_trace_path_rewrites(TFG_ROOT))
    rewrites.extend(parse_rewrite_rules(args.trace_path_rewrite))
    manifest = load_phase3_manifest(args.manifest)
    result = build_phase45_v2_dataset(
        manifest,
        output_dir=args.output_dir,
        profile=profile,
        source_manifest_path=args.manifest,
        overwrite=args.overwrite,
        max_training_windows=args.max_training_windows,
        max_validation_windows=args.max_validation_windows,
        representation_kbps=representation_kbps,
        trace_path_rewrites=tuple(rewrites),
        spbc_checkpoint=args.spbc_checkpoint,
        extra_policy_rollout_checkpoint=policy_rollout_checkpoint,
        extra_policy_rollout_source=ROLLOUT_SPBC_V2_DPO,
        dataset_schema_id=V2_DAGGER2_DATASET_SCHEMA_ID,
        allow_oracle_only_full=args.allow_oracle_only_full,
        device=args.device,
    )
    validation = validate_phase45_v2_dataset_dir(args.output_dir)
    print(
        json.dumps(
            {
                "status": "PASS",
                "dataset_generation": result,
                "dataset_validation": validation,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


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

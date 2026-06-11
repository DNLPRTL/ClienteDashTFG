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

from core.phase45_v1.spbc_v2_dpo_bundle import export_spbc_v2_dpo_inference_bundle
from core.phase45_v1.spbc_v2_dpo_training import SPBC_V2_DPO_MODEL_FILENAME, SPBC_V2_DPO_TRAINING_REPORT_FILENAME


TFG_ROOT = REPO_ROOT.parent
DEFAULT_RUN_DIR = TFG_ROOT / "modelos" / "phase45_v1" / "spbc_abr_v2_dpo" / "full_v2_anchor_safe_rank_v1"
DEFAULT_CHECKPOINT = DEFAULT_RUN_DIR / SPBC_V2_DPO_MODEL_FILENAME
DEFAULT_TRAINING_REPORT = DEFAULT_RUN_DIR / SPBC_V2_DPO_TRAINING_REPORT_FILENAME
DEFAULT_OUTPUT_DIR = (
    TFG_ROOT
    / "modelos"
    / "phase45_v1"
    / "spbc_abr_v2_dpo"
    / "full_v2_anchor_safe_rank_v1_bundle"
)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Exporta el checkpoint SPBC ABR v2 DPO anchor-safe-rank a un bundle de inferencia Phase 6."
    )
    parser.add_argument("--checkpoint", type=Path, default=DEFAULT_CHECKPOINT)
    parser.add_argument("--training-report", type=Path, default=DEFAULT_TRAINING_REPORT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--expected-checkpoint-sha256", default=None)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    report = export_spbc_v2_dpo_inference_bundle(
        checkpoint_path=args.checkpoint,
        training_report_path=args.training_report,
        output_dir=args.output_dir,
        expected_checkpoint_sha256=args.expected_checkpoint_sha256,
        overwrite=bool(args.overwrite),
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

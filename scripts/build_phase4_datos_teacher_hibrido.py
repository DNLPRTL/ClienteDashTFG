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

from core.neural_abr.hybrid_training_data import build_phase4_hybrid_teacher_data_from_plan_file


TFG_ROOT = REPO_ROOT.parent
DEFAULT_PLAN = (
    TFG_ROOT
    / "manifests_trazas"
    / "phase4"
    / "phase4A_plan_de_trazas_para_entrenamiento"
    / "phase4_plan_de_trazas_para_entrenamiento.json"
)
DEFAULT_OUTPUT_DIR = TFG_ROOT / "datasets_normalizados" / "phase4" / "phase4H_datos_teacher_hibrido_sin_vmaf"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Construye datos de entrenamiento Phase 4H con teacher hibrido sin VMAF."
    )
    parser.add_argument("--plan", type=Path, default=DEFAULT_PLAN)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--max-training-windows", type=int, default=None)
    parser.add_argument("--max-validation-windows", type=int, default=None)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    report = build_phase4_hybrid_teacher_data_from_plan_file(
        args.plan,
        output_dir=args.output_dir,
        overwrite=args.overwrite,
        max_training_windows=args.max_training_windows,
        max_validation_windows=args.max_validation_windows,
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

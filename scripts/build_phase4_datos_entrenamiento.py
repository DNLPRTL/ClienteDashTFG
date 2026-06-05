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

from core.neural_abr.constants import DEFAULT_REPRESENTATION_KBPS
from core.neural_abr.training_data import build_phase4_training_data_from_plan_file


TFG_ROOT = REPO_ROOT.parent
DEFAULT_PLAN = (
    TFG_ROOT
    / "manifests_trazas"
    / "phase4"
    / "phase4A_plan_de_trazas_para_entrenamiento"
    / "phase4_plan_de_trazas_para_entrenamiento.json"
)
DEFAULT_OUTPUT_DIR = TFG_ROOT / "datasets_normalizados" / "phase4" / "phase4B_datos_para_entrenamiento"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Construye los datos offline de Phase 4 para entrenar NeuralABR-Lite mas adelante."
    )
    parser.add_argument("--plan", type=Path, default=DEFAULT_PLAN, help="Plan de trazas generado en Phase 4A.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Directorio externo de salida.")
    parser.add_argument("--max-training-windows", type=int, default=None, help="Limite opcional para prueba rapida.")
    parser.add_argument("--max-validation-windows", type=int, default=None, help="Limite opcional para prueba rapida.")
    parser.add_argument("--representation-kbps", default=",".join(str(value) for value in DEFAULT_REPRESENTATION_KBPS))
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    representation_kbps = _parse_representation_kbps(args.representation_kbps)
    result = build_phase4_training_data_from_plan_file(
        args.plan,
        output_dir=args.output_dir,
        overwrite=args.overwrite,
        max_training_windows=args.max_training_windows,
        max_validation_windows=args.max_validation_windows,
        representation_kbps=representation_kbps,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
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


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

from core.neural_abr.training_smoke import run_phase4_training_smoke


TFG_ROOT = REPO_ROOT.parent
DEFAULT_DATA_DIR = TFG_ROOT / "datasets_normalizados" / "phase4" / "phase4B_datos_para_entrenamiento"
DEFAULT_OUTPUT_DIR = TFG_ROOT / "runs_trazas" / "phase4" / "phase4D_prueba_rapida_entrenamiento"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Ejecuta una prueba rapida diagnostica de entrenamiento NeuralABR-Lite en CPU."
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--max-samples", type=int, default=128)
    parser.add_argument("--seed", type=int, default=123)
    parser.add_argument("--device", default="cpu")
    args = parser.parse_args(argv)
    report = run_phase4_training_smoke(
        training_data_dir=args.data_dir,
        output_dir=args.output_dir,
        epochs=args.epochs,
        batch_size=args.batch_size,
        max_samples=args.max_samples,
        seed=args.seed,
        device=args.device,
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


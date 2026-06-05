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

from core.neural_abr.model_training import train_phase4_candidate_model


TFG_ROOT = REPO_ROOT.parent
DEFAULT_DATA_DIR = TFG_ROOT / "datasets_normalizados" / "phase4" / "phase4B_datos_para_entrenamiento"
DEFAULT_OUTPUT_DIR = TFG_ROOT / "modelos" / "phase4" / "phase4E_modelo_candidato_neural_abr_lite"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Entrena en CPU el modelo candidato offline NeuralABR-Lite con labels robust_mpc."
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=1e-3)
    parser.add_argument("--seed", type=int, default=40403)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--max-training-samples", type=int, default=None)
    parser.add_argument("--max-validation-samples", type=int, default=None)
    parser.add_argument("--hidden-sizes", default="32,16")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    report = train_phase4_candidate_model(
        training_data_dir=args.data_dir,
        output_dir=args.output_dir,
        overwrite=args.overwrite,
        epochs=args.epochs,
        batch_size=args.batch_size,
        learning_rate=args.learning_rate,
        seed=args.seed,
        device=args.device,
        max_training_samples=args.max_training_samples,
        max_validation_samples=args.max_validation_samples,
        hidden_sizes=_parse_hidden_sizes(args.hidden_sizes),
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


def _parse_hidden_sizes(value: str) -> tuple[int, ...]:
    parts = [part.strip() for part in str(value).split(",") if part.strip()]
    if not parts:
        raise argparse.ArgumentTypeError("hidden-sizes must not be empty")
    parsed = tuple(int(part) for part in parts)
    if any(part <= 0 for part in parsed):
        raise argparse.ArgumentTypeError("hidden-sizes values must be positive")
    return parsed


if __name__ == "__main__":
    raise SystemExit(main())

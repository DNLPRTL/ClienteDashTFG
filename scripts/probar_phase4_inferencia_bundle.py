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

from core.neural_abr.inference import run_phase4_inference_smoke


TFG_ROOT = REPO_ROOT.parent
DEFAULT_BUNDLE_DIR = TFG_ROOT / "modelos" / "phase4" / "phase4F_bundle_para_inferencia_neural_abr_lite"
DEFAULT_DATA_DIR = TFG_ROOT / "datasets_normalizados" / "phase4" / "phase4B_datos_para_entrenamiento"
DEFAULT_OUTPUT_DIR = TFG_ROOT / "runs_trazas" / "phase4" / "phase4F_prueba_inferencia_bundle"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Ejecuta solo la prueba offline de inferencia del bundle NeuralABR-Lite.")
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE_DIR)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--max-samples", type=int, default=512)
    args = parser.parse_args(argv)

    report = run_phase4_inference_smoke(
        bundle_dir=args.bundle_dir,
        data_dir=args.data_dir,
        output_dir=args.output_dir,
        max_samples=args.max_samples,
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

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

from core.neural_abr.export_bundle import export_phase4_inference_bundle


TFG_ROOT = REPO_ROOT.parent
DEFAULT_MODEL_DIR = TFG_ROOT / "modelos" / "phase4" / "phase4H_modelo_teacher_hibrido_neural_abr_lite"
DEFAULT_DATA_DIR = TFG_ROOT / "datasets_normalizados" / "phase4" / "phase4H_datos_teacher_hibrido_sin_vmaf"
DEFAULT_OUTPUT_DIR = TFG_ROOT / "modelos" / "phase4" / "phase4H_bundle_para_inferencia_teacher_hibrido_neural_abr_lite"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Exporta el segundo modelo NeuralABR-Lite con teacher hibrido a bundle local de inferencia."
    )
    parser.add_argument("--model-dir", type=Path, default=DEFAULT_MODEL_DIR)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    report = export_phase4_inference_bundle(
        model_dir=args.model_dir,
        data_dir=args.data_dir,
        output_dir=args.output_dir,
        overwrite=args.overwrite,
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

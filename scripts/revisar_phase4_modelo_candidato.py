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

from core.neural_abr.candidate_readiness import assess_phase4_candidate_model


TFG_ROOT = REPO_ROOT.parent
DEFAULT_DATA_DIR = TFG_ROOT / "datasets_normalizados" / "phase4" / "phase4B_datos_para_entrenamiento"
DEFAULT_MODEL_DIR = TFG_ROOT / "modelos" / "phase4" / "phase4E_modelo_candidato_neural_abr_lite"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Revisa si el modelo candidato NeuralABR-Lite queda listo para export en Phase 4F."
    )
    parser.add_argument("--model-dir", type=Path, default=DEFAULT_MODEL_DIR)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--min-training-samples", type=int, default=1000)
    parser.add_argument("--min-validation-samples", type=int, default=250)
    parser.add_argument("--min-training-teacher-agreement", type=float, default=0.85)
    parser.add_argument("--min-validation-teacher-agreement", type=float, default=0.80)
    args = parser.parse_args(argv)

    report = assess_phase4_candidate_model(
        model_dir=args.model_dir,
        data_dir=args.data_dir,
        output_dir=args.output_dir,
        min_training_samples=args.min_training_samples,
        min_validation_samples=args.min_validation_samples,
        min_training_teacher_agreement=args.min_training_teacher_agreement,
        min_validation_teacher_agreement=args.min_validation_teacher_agreement,
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if report["status"] == "BLOCKED_NEEDS_FIX" else 0


if __name__ == "__main__":
    raise SystemExit(main())

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

from core.neural_abr.bundle_validation import validate_phase4_inference_bundle


TFG_ROOT = REPO_ROOT.parent
DEFAULT_BUNDLE_DIR = TFG_ROOT / "modelos" / "phase4" / "phase4H_bundle_para_inferencia_teacher_hibrido_neural_abr_lite"
DEFAULT_DATA_DIR = TFG_ROOT / "datasets_normalizados" / "phase4" / "phase4H_datos_teacher_hibrido_sin_vmaf"
DEFAULT_OUTPUT_DIR = TFG_ROOT / "runs_trazas" / "phase4" / "phase4H_validacion_bundle_teacher_hibrido"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Valida el bundle del modelo NeuralABR-Lite con teacher hibrido."
    )
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE_DIR)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--max-samples", type=int, default=512)
    parser.add_argument("--latency-p95-limit-ms", type=float, default=10.0)
    args = parser.parse_args(argv)

    report = validate_phase4_inference_bundle(
        bundle_dir=args.bundle_dir,
        data_dir=args.data_dir,
        output_dir=args.output_dir,
        max_samples=args.max_samples,
        latency_p95_limit_ms=args.latency_p95_limit_ms,
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if report["status"] == "BLOCKED_NEEDS_FIX" else 0


if __name__ == "__main__":
    raise SystemExit(main())

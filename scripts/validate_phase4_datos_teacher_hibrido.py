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

from core.neural_abr.hybrid_training_data import validate_phase4_hybrid_teacher_data_dir


TFG_ROOT = REPO_ROOT.parent
DEFAULT_DATA_DIR = TFG_ROOT / "datasets_normalizados" / "phase4" / "phase4H_datos_teacher_hibrido_sin_vmaf"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Valida los datos Phase 4H de teacher hibrido sin VMAF."
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    args = parser.parse_args(argv)

    report = validate_phase4_hybrid_teacher_data_dir(args.data_dir)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

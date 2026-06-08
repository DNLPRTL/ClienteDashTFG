#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.phase6.analysis import analyze_phase6_run


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Analiza una ejecucion Phase 6 ya materializada.")
    parser.add_argument("package_root", help="Carpeta externa de validacion comparativa.")
    parser.add_argument("--no-plots", action="store_true", help="Calcula CSV/JSON/MD sin generar graficas.")
    args = parser.parse_args(argv)

    package = analyze_phase6_run(args.package_root, generate_plots=not args.no_plots)
    print(json.dumps(package["gates"], indent=2, sort_keys=True))
    print("Resultados para validar: {0}".format(package["artifacts"]["resultados_para_validar_md"]))
    return 0 if package["gates"]["all_gates_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

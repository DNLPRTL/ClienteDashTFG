#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Optional, Sequence


RAIZ_REPO = Path(__file__).resolve().parents[1]
if str(RAIZ_REPO) not in sys.path:
    sys.path.insert(0, str(RAIZ_REPO))

from core.phase6.analisis import analizar_paquete_phase6
from core.phase6.verificacion import verificar_paquete_phase6


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Analiza una ejecucion Phase 6 ya materializada.")
    parser.add_argument("package_root", help="Carpeta externa de validacion comparativa.")
    parser.add_argument("--no-plots", action="store_true", help="Calcula CSV/JSON/MD sin generar graficas.")
    args = parser.parse_args(argv)

    package = analizar_paquete_phase6(args.package_root, generate_plots=not args.no_plots)
    verification = verificar_paquete_phase6(args.package_root, require_plots=not args.no_plots, write_artifacts=True)
    print(json.dumps(package["gates"], indent=2, sort_keys=True))
    print("Resultados para validar: {0}".format(package["artifacts"]["resultados_para_validar_md"]))
    print("Verificacion paquete: {0}".format(verification["artifacts"]["verification_md"]))
    return 0 if package["gates"]["all_gates_passed"] and verification["all_checks_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

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

from core.fase6.verificacion import verificar_paquete_fase6


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Verifica un paquete Phase 6 de validacion comparativa.")
    parser.add_argument("package_root", help="Carpeta externa Phase 6.")
    parser.add_argument("--no-plots-required", action="store_true", help="No falla si no hay graficas generadas.")
    args = parser.parse_args(argv)

    package = verificar_paquete_fase6(
        args.package_root,
        require_plots=not args.no_plots_required,
        write_artifacts=True,
    )
    print(json.dumps({"all_checks_passed": package["all_checks_passed"], "counts": package["counts"]}, indent=2, sort_keys=True))
    print("Verificacion paquete: {0}".format(package["artifacts"]["verification_md"]))
    return 0 if package["all_checks_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

"""Genera en Windows los ficheros de comprobacion del kit de la VM cliente (fase de blindaje).

- hashes_codigo.sha256: huellas del codigo entregado (TFG Material), sin __pycache__ ni .idea;
- hashes_bundle.sha256, hashes_catalogo.sha256 y hashes_cuantiles_fijos.sha256;
- cuantiles_fijos.json: copia para instalar en ~/TFG/modelos/cuantiles_fijos/;
- ventanas_esperadas_previa.txt y ventanas_esperadas_final.txt: las ventanas que deben salir en
  el plan en seco de la VM (la seleccion solo usa estadisticas de las trazas, no resultados).

Uso (desde cualquier carpeta): python generar_kit.py
"""
from __future__ import annotations

import csv
import glob
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

KIT = os.path.dirname(os.path.abspath(__file__))
MATERIAL = r"C:\Users\danie\Documents\TFG Material"
CODIGO = os.path.join(MATERIAL, "01_codigo", "ClienteDashTFG")
BUNDLE = os.path.join(MATERIAL, "03_modelos", "modelo_propio", "bundle")
CUANTILES = os.path.join(MATERIAL, "03_modelos", "cuantiles_fijos", "cuantiles_fijos.json")
CATALOGO = os.path.join(MATERIAL, "02_corpus_red", "catalogo_trazas.json")
TRAZAS = os.path.join(MATERIAL, "02_corpus_red", "datasets_normalizados").replace("\\", "/")


def sha256(ruta: str) -> str:
    h = hashlib.sha256()
    with open(ruta, "rb") as fichero:
        for bloque in iter(lambda: fichero.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def huellas(raiz: str, salida: str) -> int:
    lineas = []
    for directorio, subdirs, ficheros in os.walk(raiz):
        subdirs[:] = sorted(d for d in subdirs if d not in ("__pycache__", ".idea", ".ruff_cache", ".pytest_cache"))
        for nombre in sorted(ficheros):
            ruta = os.path.join(directorio, nombre)
            relativa = "./" + os.path.relpath(ruta, raiz).replace("\\", "/")
            lineas.append("{0}  {1}".format(sha256(ruta), relativa))
    with open(salida, "w", encoding="utf-8", newline="\n") as fichero:
        fichero.write("\n".join(lineas) + "\n")
    return len(lineas)


def ventanas_plan(preset: str) -> list:
    config = json.load(open(os.path.join(CODIGO, "config", "evaluacion.local.json"), encoding="utf-8"))
    config["rutas"]["ruta_catalogo"] = CATALOGO
    config["rutas"]["raiz_salida"] = tempfile.mkdtemp(prefix="plan_seco_")
    config["rutas"]["reescrituras_rutas_trazas"] = [{"from": "/home/daniel/TFG/datasets_normalizados", "to": TRAZAS}]
    ruta_cfg = os.path.join(config["rutas"]["raiz_salida"], "config.json")
    json.dump(config, open(ruta_cfg, "w", encoding="utf-8"))
    entorno = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1", MSYS_NO_PATHCONV="1")
    subprocess.run([sys.executable, os.path.join(CODIGO, "scripts", "3_evaluacion", "ejecutar_evaluacion.py"),
                    "--config", ruta_cfg, "--preset", preset, "--solo-plan"], check=True, env=entorno,
                   stdout=subprocess.DEVNULL)
    plan = glob.glob(os.path.join(config["rutas"]["raiz_salida"], "*_" + preset, "00_protocolo", "ventanas_trazas.csv"))[0]
    return [fila["id_ventana_traza"] for fila in csv.DictReader(open(plan, encoding="utf-8"))]


def main() -> int:
    print("codigo:", huellas(CODIGO, os.path.join(KIT, "hashes_codigo.sha256")), "ficheros")
    print("bundle:", huellas(BUNDLE, os.path.join(KIT, "hashes_bundle.sha256")), "ficheros")
    with open(os.path.join(KIT, "hashes_catalogo.sha256"), "w", encoding="utf-8", newline="\n") as fichero:
        fichero.write("{0}  ./catalogo_trazas.json\n".format(sha256(CATALOGO)))
    shutil.copyfile(CUANTILES, os.path.join(KIT, "cuantiles_fijos.json"))
    with open(os.path.join(KIT, "hashes_cuantiles_fijos.sha256"), "w", encoding="utf-8", newline="\n") as fichero:
        fichero.write("{0}  ./cuantiles_fijos.json\n".format(sha256(CUANTILES)))
    for preset, nombre in (("previa_vm", "ventanas_esperadas_previa.txt"), ("final_blindaje", "ventanas_esperadas_final.txt")):
        ventanas = ventanas_plan(preset)
        with open(os.path.join(KIT, nombre), "w", encoding="utf-8", newline="\n") as fichero:
            fichero.write("\n".join(ventanas) + "\n")
        print(preset, len(ventanas), "ventanas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

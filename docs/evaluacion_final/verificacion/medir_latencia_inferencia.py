"""Latencia de la inferencia del conjunto con y sin carga de CPU, con los hilos de PyTorch por
defecto o con uno solo. Cada condicion se mide en un proceso nuevo.

Uso: python medir_latencia_inferencia.py <codigo> <bundle>
"""
from __future__ import annotations

import multiprocessing
import statistics
import subprocess
import sys
import time

MEDIDA = r"""
import sys, time, statistics
sys.dont_write_bytecode = True
sys.path.insert(0, sys.argv[1])
import torch
if sys.argv[3] == "1":
    torch.set_num_threads(1)
from core.modelo_propio.bundle import BundleModelo
from core.modelo_propio.estado_sesion import EstadoSesion
from core.modelo_propio.perfil_video import PerfilTamanosSegmentos
bundle = BundleModelo(sys.argv[2])
escalera = PerfilTamanosSegmentos.cargar_por_id("paseo_almunecar_10min_30fps_4s").a_escalera_fiel(num_segmentos=30)
estado = EstadoSesion(10, 16.6, 3, (2.0e6, 2.0e6, 2.0e6, 2.0e6, 1.7e6), (2.4, 2.4, 2.4, 2.4, 2.8), 0.0, 0.0, 0.0, 30)
latencias = []
for _ in range(1500):
    bundle.predecir(estado, escalera)
    latencias.append(bundle.ultima_latencia_ms)
latencias.sort()
print("hilos={0} media={1:.2f} p99={2:.2f} max={3:.2f} >50ms={4}".format(
    torch.get_num_threads(), statistics.mean(latencias), latencias[int(0.99 * len(latencias))],
    latencias[-1], sum(1 for x in latencias if x > 50.0)))
"""


def _quemar(fin: float) -> None:
    x = 0
    while time.time() < fin:
        x += 1


def medir(codigo: str, bundle: str, un_hilo: bool) -> str:
    salida = subprocess.run(
        [sys.executable, "-c", MEDIDA, codigo, bundle, "1" if un_hilo else "0"],
        capture_output=True, text=True, check=True,
    )
    return salida.stdout.strip()


def main() -> int:
    codigo, bundle = sys.argv[1], sys.argv[2]
    for carga in (False, True):
        procesos = []
        if carga:
            fin = time.time() + 120.0
            procesos = [multiprocessing.Process(target=_quemar, args=(fin,)) for _ in range(multiprocessing.cpu_count())]
            for p in procesos:
                p.start()
        for un_hilo in (False, True):
            print("carga={0} {1}".format("si" if carga else "no", medir(codigo, bundle, un_hilo)), flush=True)
        for p in procesos:
            p.terminate()
    return 0


if __name__ == "__main__":
    sys.exit(main())

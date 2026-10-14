"""Comprueba que el controlador final construye sus entradas exactamente como el entrenamiento.

Reinyecta, fila a fila y en orden, la realimentacion registrada en las sesiones del controlador
propio (como hace el reproductor: todas las filas, y decision desde la segunda de video) en un
ControladorPropio de la version final. En cada decision compara las entradas que recibe el
modelo con las que construye el entrenamiento a partir de las mismas observaciones:

- sesion de segmentos_totales - 1 segmentos de video e indice = siguiente segmento a descargar;
- historial con todas las descargas de video (las cinco ultimas);
- rebuffering reciente = max(tiempo de la ultima descarga - buffer previo, 0), como en
  simular_paso_bucle_cerrado.

Cuenta tambien cuantas decisiones cambian respecto a las registradas por la version anterior.

Uso: python verificar_entradas.py <codigo> <bundle> <paquete> [<paquete> ...]
"""
from __future__ import annotations

import ast
import csv
import json
import sys
from pathlib import Path


def parsear(valor: str):
    texto = (valor or "").strip()
    if texto == "":
        return None
    if texto.startswith("["):
        return ast.literal_eval(texto)
    for tipo in (int, float):
        try:
            return tipo(texto)
        except ValueError:
            pass
    return texto


def main() -> int:
    codigo, bundle = Path(sys.argv[1]), Path(sys.argv[2])
    paquetes = [Path(p) for p in sys.argv[3:]]
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(codigo))
    from core.controladores.contrato import CLAVES_REALIMENTACION
    from core.controladores.controlador_propio import ControladorPropio
    from core.controladores.entradas_contexto import construir_entradas_contexto
    from core.modelo_propio import bundle as modulo_bundle
    from core.modelo_propio.estado_sesion import EstadoSesion
    from core.modelo_propio.perfil_video import PerfilTamanosSegmentos

    captura = {}
    predecir_original = modulo_bundle.BundleModelo.predecir

    def predecir_capturando(self, estado, escalera):
        captura.update(estado=estado, escalera=escalera)
        return predecir_original(self, estado, escalera)

    modulo_bundle.BundleModelo.predecir = predecir_capturando

    comparadas = iguales = finales = 0
    cambios = {"real": [0, 0, 0], "sintetica": [0, 0, 0]}
    respaldos = 0
    diferencias = []
    for paquete in paquetes:
        ejecuciones = paquete / "01_ejecucion" / "ejecuciones"
        for dir_sesion in sorted(p for p in ejecuciones.iterdir() if "controlador_propio" in p.name):
            config = paquete / "00_protocolo" / "configs_cliente" / "{0}.yaml".format(dir_sesion.name)
            parametros = dict(json.loads(config.read_text(encoding="utf-8"))["controlador"]["parametros"])
            perfil = parametros["id_perfil_video"]
            parametros["dir_bundle"] = str(bundle)
            ctrl = ControladorPropio(**parametros)
            escalera_entrenamiento = None
            filas = list(csv.DictReader((next(dir_sesion.iterdir()) / "telemetria_segmentos.csv").open(encoding="utf-8")))
            descargas = []
            buffer_previo = 0.0
            nivel_previo = None
            tipo = "real" if "_real_" in dir_sesion.name else "sintetica"
            for fila in filas:
                fb = {clave: parsear(fila["feedback_" + clave]) for clave in CLAVES_REALIMENTACION}
                ctrl.fijarFeedbackReproductor(fb)
                k = int(fb["indice_segmento"])
                rebuffering = 0.0
                if k >= 1 and (fb.get("tamano_ultimo_fragmento") or 0) > 0:
                    t = float(fb["tiempo_ultima_descarga"])
                    descargas.append((8.0 * float(fb["tamano_ultimo_fragmento"]) / t, t))
                    rebuffering = max(t - buffer_previo, 0.0)
                cambio = 0.0 if nivel_previo is None or k <= 2 else float(abs(int(fb["nivel"]) - nivel_previo))
                if (fila.get("tasa_objetivo_politica") or "").strip():
                    captura.clear()
                    tasa = ctrl.calcularAccionControl()
                    nivel_nuevo = min(ctrl.cuantizarTasa(tasa), int(fb["nivel_max"]))
                    respaldos += int(ctrl._diagnosticos.respaldo_usado)
                    segmentos_video = int(fb["segmentos_totales"]) - 1
                    if k <= segmentos_video - 1:
                        if escalera_entrenamiento is None:
                            escalera_entrenamiento = PerfilTamanosSegmentos.cargar_por_id(perfil).a_escalera_fiel(
                                buffer_maximo_s=60.0, num_segmentos=segmentos_video
                            )
                        estado_entrenamiento = EstadoSesion(
                            indice_segmento=k,
                            buffer_s=max(float(fb["tiempo_en_cola"]), 0.0),
                            indice_ultima_representacion=int(fb["nivel"]),
                            historial_throughput_bps=tuple(tp for tp, _ in descargas[-5:]),
                            historial_tiempo_descarga_s=tuple(t for _, t in descargas[-5:]),
                            rebuffering_reciente_s=rebuffering,
                            cambio_reciente_abs=cambio,
                            tiempo_red_s=0.0,
                            segmentos_totales=segmentos_video,
                        )
                        esperado = construir_entradas_contexto(estado_entrenamiento, escalera_entrenamiento)
                        obtenido = construir_entradas_contexto(captura["estado"], captura["escalera"])
                        comparadas += 1
                        if dict(esperado) == dict(obtenido):
                            iguales += 1
                        elif len(diferencias) < 5:
                            claves = [c for c in esperado if esperado[c] != obtenido[c]]
                            diferencias.append((dir_sesion.name[:30], k, {c: (esperado[c], obtenido[c]) for c in claves}))
                    else:
                        finales += 1
                    registrado = int(parsear(fila["nivel_elegido_politica"]))
                    cambios[tipo][0] += 1
                    cambios[tipo][1] += int(nivel_nuevo < registrado)
                    cambios[tipo][2] += int(nivel_nuevo > registrado)
                if (fb.get("tamano_ultimo_fragmento") or 0) > 0 or k == 0:
                    buffer_previo = max(float(fb["tiempo_en_cola"]), 0.0)
                if k >= 1:
                    nivel_previo = int(fb["nivel"])
    print("decisiones comparadas (k = 2..29): {0}; entradas identicas a las del entrenamiento: {1}".format(
        comparadas, iguales))
    print("decisiones finales sin segmento siguiente (k = 30): {0}".format(finales))
    print("decisiones de la version final que recurrieron al respaldo: {0}".format(respaldos))
    for tipo, (n, bajo, alto) in cambios.items():
        if n:
            print("{0}: {1} decisiones; distinto nivel que la version anterior en {2} ({3:.1f} %): {4} mas bajo, {5} mas alto".format(
                tipo, n, bajo + alto, 100.0 * (bajo + alto) / n, bajo, alto))
    for d in diferencias:
        print("   DIFERENCIA:", d)
    return 0 if comparadas == iguales and respaldos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

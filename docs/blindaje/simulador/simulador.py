"""Simulador en tiempo virtual de una sesion del cliente DASH (fase de blindaje).

Reproduce, sin esperas reales, lo que hace reproductor.py con el motor simulado y la
emulacion por traza, usando las clases reales del codigo entregado:

- los controladores reales (registro.crear_controlador) con la misma realimentacion
  (construir_realimentacion_controlador) en los mismos momentos;
- el mismo modelo de red (ModeloRedPorTraza) sobre la ventana compactada y recortada, con el
  reloj de la traza contando desde que se crea el descargador, como en la VM;
- el mismo buffer: arranque con 0,1 s en cola, parada al bajar a 0,01 s, espera en pasos de
  0,01 s cuando hay mas de 60 s, 1 s de inactividad tras el init y tras el calentamiento;
- la misma QoE de analisis.py: filas 2..30, el rebuffering de cada parada en la fila del
  ultimo segmento encolado y sin contar el vaciado final.

Solo sirve para las pruebas previas sobre la particion de validacion y para estimar varianzas.
No va a la memoria.
"""
from __future__ import annotations

import json
import os
import sys
import time
import zlib
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Any, Dict, List, Mapping, Optional, Sequence

RAIZ_CODIGO = os.environ.get(
    "TFG_CODIGO", r"C:\Users\danie\Documents\TFG Material\01_codigo\ClienteDashTFG"
)
if RAIZ_CODIGO not in sys.path:
    sys.path.insert(0, RAIZ_CODIGO)

from core.controladores.registro import crear_controlador  # noqa: E402
from core.evaluacion.qoe import EntradaQoESegmento, calcular_qoe_lineal, calcular_qoe_log  # noqa: E402
from core.feedback_reproductor import construir_realimentacion_controlador  # noqa: E402
from core.modelo_propio.perfil_video import DIR_TAMANOS_SEGMENTOS, resolver_id_descriptor_video  # noqa: E402
from core.reproduccion_trazas.cargador import cargar_traza_normalizada  # noqa: E402
from core.reproduccion_trazas.descargador_controlado import (  # noqa: E402
    compactar_tiempos_traza,
    recortar_ventana_traza,
)
from core.reproduccion_trazas.modelo_red import ModeloRedPorTraza  # noqa: E402

RAIZ_TRAZAS_WINDOWS = r"C:\Users\danie\Documents\TFG Material\02_corpus_red\datasets_normalizados"
PREFIJO_TRAZAS_LINUX = "/home/daniel/TFG/datasets_normalizados/"
DIR_BUNDLE_WINDOWS = r"C:\Users\danie\Documents\TFG Material\03_modelos\modelo_propio\bundle"

UMBRAL_PAUSA_S = 0.01
TIEMPO_MIN_COLA_S = 0.1


@dataclass
class ConfigSesion:
    clave_controlador: str
    parametros: Dict[str, Any]
    id_perfil_video: str
    ruta_traza: str
    inicio_ventana_s: float
    duracion_ventana_s: float
    politica_fin: str = "fail"
    max_bucles: int = 0
    max_segmentos: int = 30
    calidad_inicial: int = 0
    buffer_maximo_s: float = 60.0
    paso_vaciado_s: float = 0.01
    # Tiempos de la VM que no dependen del controlador, calibrados con los paquetes reales:
    # cada descarga dura ~6 ms mas que la traza (peticion HTTP y exceso del sleep), cada
    # sleep(1) dura ~1,007 s y la espera con el buffer lleno casi no se desvia.
    t_hasta_init_s: float = 0.03
    exceso_descarga_s: float = 0.006
    exceso_inactividad_s: float = 0.007
    exceso_sueno_s: float = 0.00002
    # A que fila va cada parada: "cabeza" = como el reproductor actual (la del ultimo segmento
    # encolado; la espera del ultimo segmento se pierde a veces); "esperado" = la del segmento
    # que se esperaba (correccion C2).
    regla_paradas: str = "cabeza"
    latencias_s: Optional[Dict[str, float]] = None
    latencia_medida: bool = False
    # Para validar contra la VM: latencia registrada de cada decision, en orden.
    latencias_registradas_s: Optional[List[float]] = None
    etiqueta: str = ""
    extra: Dict[str, Any] = field(default_factory=dict)


@dataclass
class FilaSegmento:
    indice: int
    nivel: int
    bitrate_kbps: float
    bytes: int
    t_inicio_s: float
    t_fin_s: float
    tiempo_descarga_s: float
    buffer_tras_encolar_s: float
    espera_buffer_lleno_s: float = 0.0
    rebuffering_s: float = 0.0


@dataclass
class ResultadoSesion:
    etiqueta: str
    clave_controlador: str
    filas: List[FilaSegmento]
    resumen: Dict[str, float]
    t_ultima_descarga_s: float = 0.0
    excede_ventana: bool = False
    error: str = ""
    extra: Dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Datos (con cache por proceso)


def ruta_traza_local(ruta: str) -> str:
    if ruta.startswith(PREFIJO_TRAZAS_LINUX):
        return os.path.join(RAIZ_TRAZAS_WINDOWS, *ruta[len(PREFIJO_TRAZAS_LINUX):].split("/"))
    return ruta


@lru_cache(maxsize=4096)
def _traza_completa(ruta: str):
    return compactar_tiempos_traza(cargar_traza_normalizada(ruta_traza_local(ruta)))


@lru_cache(maxsize=4096)
def traza_ventana(ruta: str, inicio_s: float, duracion_s: float):
    return recortar_ventana_traza(_traza_completa(ruta), inicio_ventana_s=inicio_s, duracion_ventana_s=duracion_s)


@lru_cache(maxsize=64)
def descriptor_video(id_perfil_video: str) -> Mapping[str, Any]:
    resuelto = resolver_id_descriptor_video(id_perfil_video, dir_base=DIR_TAMANOS_SEGMENTOS)
    with open(os.path.join(DIR_TAMANOS_SEGMENTOS, resuelto + ".json"), encoding="utf-8") as fichero:
        datos = json.load(fichero)
    reps = sorted(datos["representations"], key=lambda r: int(r["bandwidth_bps"]))
    return {
        "id": resuelto,
        "tasas_Bps": tuple(int(r["bandwidth_bps"]) / 8.0 for r in reps),
        "bytes": tuple(tuple(int(v) for v in r["segment_bytes"]) for r in reps),
        "init_bytes": tuple(int(r.get("init_bytes") or 0) for r in reps),
        "duracion_segmento_s": float(datos["duracion_segmento_s"]),
    }


def instalar_cache_bundle() -> None:
    # El bundle se carga una vez por proceso: no guarda estado entre decisiones.
    import core.controladores.controlador_propio as modulo_propio

    if getattr(modulo_propio, "_cache_bundle_simulador", False):
        return
    original = modulo_propio.cargar_bundle
    cache: Dict[tuple, Any] = {}

    def cargar_bundle_cacheado(dir_bundle, verificar_hashes=True):
        clave = (str(dir_bundle), bool(verificar_hashes))
        if clave not in cache:
            cache[clave] = original(dir_bundle, verificar_hashes=verificar_hashes)
        return cache[clave]

    modulo_propio.cargar_bundle = cargar_bundle_cacheado
    modulo_propio._cache_bundle_simulador = True


# ---------------------------------------------------------------------------
# Motor de reproduccion en tiempo virtual (equivale a core/motores/simulado.py)


class MotorVirtual:
    """Buffer del motor simulado en tiempo continuo.

    El motor real consume en tics de ~10 ms y entra en parada en el primer tic en que quedan
    <= 0,01 s. Segun la fase del tic, el ultimo segmento queda con un resto de (0; 0,01] s
    o se consume entero (en los paquetes reales, ~21 % de las paradas). Eso decide la fila
    a la que el reproductor actual asigna la parada y si el buffer tras la siguiente descarga
    es 4,0x s o exactamente 4,0 s, que es el umbral de respaldo de BOLA. Aqui se sortea con la
    misma probabilidad y una semilla por sesion.
    """

    def __init__(self, prob_consumo_entero: float = 0.21, semilla: int = 0) -> None:
        import random

        self.cola: List[list] = []  # [indice, restante_s, bytes, duracion_s]
        self.reproduciendo = False
        self.arrancado = False
        self.t = 0.0
        self.inicio_parada: Optional[float] = None
        self.parada_consumio_entero = False
        self.prob_consumo_entero = float(prob_consumo_entero)
        self.aleatorio = random.Random(semilla)
        # Duracion de cada parada, por el indice del segmento cuya llegada la termina, y si en
        # esa parada el ultimo segmento se consumio entero. El vaciado final no termina con
        # ninguna llegada y no queda registrado.
        self.paradas: Dict[int, float] = {}
        self.consumo_entero: Dict[int, bool] = {}

    def total_s(self) -> float:
        return sum(seg[1] for seg in self.cola)

    def bytes_en_cola(self) -> int:
        return int(sum(seg[2] * (seg[1] / seg[3]) for seg in self.cola if seg[3] > 0))

    def avanzar(self, t_nuevo: float) -> None:
        if t_nuevo <= self.t:
            return
        if self.reproduciendo:
            dt = t_nuevo - self.t
            if dt < self.total_s() - UMBRAL_PAUSA_S:
                self._consumir(dt)
            else:
                # La cola baja al umbral: empieza una parada, con el resto que deje el tic.
                if self.aleatorio.random() < self.prob_consumo_entero:
                    resto, entero = 0.0, True
                else:
                    resto, entero = self.aleatorio.uniform(1e-4, UMBRAL_PAUSA_S), False
                consumible = min(max(self.total_s() - resto, 0.0), dt)
                self._consumir(consumible)
                if entero:
                    self.cola = [seg for seg in self.cola if seg[1] > 1e-12]
                self.reproduciendo = False
                self.inicio_parada = self.t + consumible
                self.parada_consumio_entero = entero
        self.t = t_nuevo

    def _consumir(self, dt: float) -> None:
        while dt > 0 and self.cola:
            cabeza = self.cola[0]
            usado = min(dt, cabeza[1])
            cabeza[1] -= usado
            dt -= usado
            if cabeza[1] <= 1e-12:
                self.cola.pop(0)

    def encolar(self, indice: int, duracion_s: float, num_bytes: int) -> None:
        self.cola.append([indice, float(duracion_s), int(num_bytes), float(duracion_s)])
        if not self.reproduciendo and self.total_s() >= TIEMPO_MIN_COLA_S:
            self.reproduciendo = True
            if self.arrancado and self.inicio_parada is not None:
                self.paradas[indice] = self.paradas.get(indice, 0.0) + (self.t - self.inicio_parada)
                self.consumo_entero[indice] = self.parada_consumio_entero
            self.arrancado = True
            self.inicio_parada = None


# ---------------------------------------------------------------------------
# Sesion


def _latencia(cfg: ConfigSesion, num_decision: int, medida_s: float) -> float:
    if cfg.latencias_registradas_s is not None and num_decision < len(cfg.latencias_registradas_s):
        return cfg.latencias_registradas_s[num_decision]
    if cfg.latencia_medida:
        return medida_s
    tabla = cfg.latencias_s or {}
    if cfg.clave_controlador.startswith(("controlador_propio", "propio")):
        # Desde el pulido F8 (15/10) el modelo se carga al crear el controlador: la primera decision
        # ya no paga la carga (antes, 0.05 s; medido en la VM: 53-98 ms).
        return tabla.get("propio_primera", 0.006) if num_decision == 0 else tabla.get("propio", 0.003)
    return tabla.get("clasico", 0.0003)


def _tiempo_http_s(num_bytes: int) -> float:
    # Peticion real a la VM servidor por la red local; si dura mas que la traza, manda ella.
    return 0.003 + num_bytes / 60.0e6


def simular_sesion(cfg: ConfigSesion, controlador: Any = None) -> ResultadoSesion:
    instalar_cache_bundle()
    video = descriptor_video(cfg.id_perfil_video)
    tasas = list(video["tasas_Bps"])
    nivel_max = len(tasas) - 1
    duracion_seg = video["duracion_segmento_s"]
    num_elementos = int(cfg.max_segmentos) + 1  # init + medias
    red = ModeloRedPorTraza(
        traza_ventana(cfg.ruta_traza, float(cfg.inicio_ventana_s), float(cfg.duracion_ventana_s)),
        politica_fin=cfg.politica_fin,
        max_bucles=int(cfg.max_bucles),
    )
    if controlador is None:
        controlador = crear_controlador(cfg.clave_controlador, dict(cfg.parametros))
    motor = MotorVirtual(semilla=zlib.crc32((cfg.etiqueta or "sesion").encode("utf-8")))
    estado = {"t": float(cfg.t_hasta_init_s), "nivel": max(0, min(int(cfg.calidad_inicial), nivel_max))}
    bytes_descargados = 0
    peticion = {"inicio": None, "fin": None}
    filas: List[FilaSegmento] = []

    def realimentacion(indice: int, ultimo_tamano: int, ultimo_tiempo: float, duracion: Optional[float]):
        motor.avanzar(estado["t"])
        fb = construir_realimentacion_controlador(
            bytes_en_cola=motor.bytes_en_cola(),
            tiempo_en_cola=motor.total_s(),
            tasas=tasas,
            duraciones_fragmentos=[duracion_seg] * len(tasas),
            nivel_actual=estado["nivel"],
            nivel_max=nivel_max,
            bytes_descargados=bytes_descargados,
            indice_segmento=indice,
            inicio_peticion_segmento=peticion["inicio"],
            fin_peticion_segmento=peticion["fin"],
            ultimo_tamano=ultimo_tamano,
            ultimo_tiempo=ultimo_tiempo,
            duracion_fragmento=duracion,
            segmentos_totales=num_elementos,
        )
        if hasattr(controlador, "ampliar_realimentacion"):
            try:
                fb = controlador.ampliar_realimentacion(fb, contexto={"fase": "fila"})
            except Exception:
                pass
        return fb

    controlador.fijarFeedbackReproductor(realimentacion(0, 0, 0.0, None))
    calentamiento = True
    num_decision = 0
    try:
        for indice in range(num_elementos):
            es_init = indice == 0
            espera = 0.0
            if not es_init:
                motor.avanzar(estado["t"])
                pasos = 0
                while motor.total_s() > cfg.buffer_maximo_s:
                    pasos += 1
                    estado["t"] += cfg.paso_vaciado_s + cfg.exceso_sueno_s
                    motor.avanzar(estado["t"])
                espera = pasos * (cfg.paso_vaciado_s + cfg.exceso_sueno_s)
            nivel = estado["nivel"]
            num_bytes = video["init_bytes"][nivel] if es_init else video["bytes"][nivel][indice - 1]
            num_bytes = max(int(num_bytes), 1)
            peticion["inicio"] = estado["t"]
            descarga = red.descarga(num_bytes, tiempo_inicio_s=estado["t"])
            estado["t"] += max(descarga.duracion_s, _tiempo_http_s(num_bytes)) + cfg.exceso_descarga_s
            peticion["fin"] = estado["t"]
            motor.avanzar(estado["t"])
            if es_init:
                controlador.fijarFeedbackReproductor(realimentacion(indice, 0, descarga.duracion_s, 0.0))
            else:
                motor.encolar(indice, duracion_seg, num_bytes)
                bytes_descargados += num_bytes
                fb = realimentacion(indice, num_bytes, descarga.duracion_s, duracion_seg)
                controlador.fijarFeedbackReproductor(fb)
                filas.append(
                    FilaSegmento(
                        indice=indice,
                        nivel=nivel,
                        bitrate_kbps=tasas[nivel] * 8.0 / 1000.0,
                        bytes=num_bytes,
                        t_inicio_s=peticion["inicio"],
                        t_fin_s=peticion["fin"],
                        tiempo_descarga_s=descarga.duracion_s,
                        buffer_tras_encolar_s=float(fb["tiempo_en_cola"]),
                        espera_buffer_lleno_s=espera,
                    )
                )
                if calentamiento:
                    calentamiento = False
                else:
                    antes = time.perf_counter()
                    tasa = controlador.calcularAccionControl()
                    medida = time.perf_counter() - antes
                    estado["nivel"] = min(controlador.cuantizarTasa(tasa), nivel_max)
                    estado["t"] += _latencia(cfg, num_decision, medida)
                    num_decision += 1
            inactividad = float(controlador.obtenerDuracionInactividad())
            if inactividad > 0:
                estado["t"] += inactividad + cfg.exceso_inactividad_s
    except Exception as exc:  # traza agotada u otro fallo: se informa, no se oculta
        return ResultadoSesion(
            etiqueta=cfg.etiqueta,
            clave_controlador=cfg.clave_controlador,
            filas=filas,
            resumen={},
            error="{0}: {1}".format(type(exc).__name__, exc),
            extra=dict(cfg.extra),
        )

    motor.avanzar(estado["t"])
    por_indice = {fila.indice: fila for fila in filas}
    for indice_llegada, duracion in motor.paradas.items():
        if cfg.regla_paradas == "cabeza":
            # Reproductor actual: la fila en cabeza de la cola de reproduccion, que es la del
            # segmento esperado solo si el anterior se consumio entero.
            indice_fila = indice_llegada if motor.consumo_entero.get(indice_llegada) else indice_llegada - 1
        else:
            indice_fila = indice_llegada
        if indice_fila in por_indice:
            por_indice[indice_fila].rebuffering_s += duracion
    if cfg.regla_paradas == "cabeza" and filas:
        filas[-1].rebuffering_s = 0.0  # el reproductor actual anula la fila del ultimo segmento
    t_ultima = filas[-1].t_fin_s if filas else 0.0
    return ResultadoSesion(
        etiqueta=cfg.etiqueta,
        clave_controlador=cfg.clave_controlador,
        filas=filas,
        resumen=resumir(filas),
        t_ultima_descarga_s=t_ultima,
        excede_ventana=t_ultima > float(cfg.duracion_ventana_s),
        extra=dict(cfg.extra),
    )


def resumir(filas: Sequence[FilaSegmento]) -> Dict[str, float]:
    # Mismas filas y misma QoE que core/evaluacion/analisis.py (la fila 1 es el calentamiento).
    evaluables = [fila for fila in filas if fila.indice >= 2 and fila.bitrate_kbps > 0]
    if not evaluables:
        return {}
    entradas = [EntradaQoESegmento(bitrate_kbps=f.bitrate_kbps, rebuffering_s=f.rebuffering_s) for f in evaluables]
    lineal = calcular_qoe_lineal(entradas)
    log = calcular_qoe_log(entradas, min_bitrate_kbps=max(1.0, min(e.bitrate_kbps for e in entradas)))
    return {
        "qoe_lineal_media": float(lineal.qoe_media),
        "qoe_log_media": float(log.qoe_media),
        "bitrate_medio_kbps": float(lineal.bitrate_medio_kbps),
        "rebuffering_total_s": float(lineal.rebuffering_total_s),
        "num_stalls": int(lineal.num_stalls),
        "num_cambios_calidad": int(lineal.num_cambios_calidad),
        "penalizacion_suavidad": float(lineal.penalizacion_suavidad),
        "buffer_medio_s": sum(f.buffer_tras_encolar_s for f in evaluables) / len(evaluables),
        "num_segmentos": len(evaluables),
    }


def simular_lote(configs: Sequence[ConfigSesion], procesos: int = 1) -> List[ResultadoSesion]:
    if procesos <= 1:
        return [simular_sesion(cfg) for cfg in configs]
    from concurrent.futures import ProcessPoolExecutor

    with ProcessPoolExecutor(max_workers=procesos) as ejecutor:
        return list(ejecutor.map(simular_sesion, configs, chunksize=4))

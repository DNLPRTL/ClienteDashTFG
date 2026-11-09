# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/anexos.docx: los tres anexos anunciados en el apartado 1.6.

  Anexo A. Reproduccion del experimento a partir del material entregado.
  Anexo B. Manual de uso del cliente.
  Anexo C. Documentacion complementaria (corpus, contenido, ficheros del paquete, columnas).

Regla cero: todo lo que se afirma se lee o se cuenta en TFG Material (codigo entregado, paquete de evidencia,
corpus, modelos, contenido, dataset, informes de entorno). Las tablas de claves de configuracion, controladores y
opciones de linea de comandos se construyen importando o analizando el codigo entregado, no a mano. Ninguna cifra de
resultados: para eso el texto remite al capitulo 6.

Ejecutar desde la raiz del repo (necesita el Python con torch, porque importa el registro de controladores):
  py -3.12 docs/memoria/apoyo/generar_anexos.py
"""
from __future__ import annotations

import csv
import dataclasses
import inspect
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from docx import Document

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla  # noqa: E402

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
CODIGO = TFG_MATERIAL / "01_codigo" / "ClienteDashTFG"
CORPUS = TFG_MATERIAL / "02_corpus_red"
MODELOS = TFG_MATERIAL / "03_modelos"
EVIDENCIA = TFG_MATERIAL / "04_evidencia_final"
PAQUETE = EVIDENCIA / "20261015_031741_final_blindaje"
VERIFICACION = EVIDENCIA / "verificacion_windows_20261016"
CONTENIDO = TFG_MATERIAL / "05_contenido_dash"
DATASET = TFG_MATERIAL / "06_dataset_entrenamiento" / "dataset_entrenamiento"
INFO_ENTORNO = TFG_MATERIAL / "00_info_entorno"

PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
BORRADORES = RAIZ_REPO / "docs" / "memoria" / "borradores_docx"
BIB = RAIZ_REPO / "docs" / "memoria" / "bibliografia.bib"
SALIDA = BORRADORES / "anexos.docx"

sys.path.insert(0, str(CODIGO))  # para importar el codigo entregado (core.*)

PROHIBIDOS = ["SPBC", "Q_H", "mpc_prudente", "Phase", "Fase 6", "v1", "v2", "Neural", "tfg_final",
              "benchmark_autorizado", "ensemble temporal", "Codex", "DashClientModular"]
CITAS = ["apacheHttpd", "gstreamerDocs", "pytorchDocs", "mao2017pensieve", "blenderTearsOfSteel"]

SESION_EJEMPLO = "s00008_controlador_propio_paseo_10min_30fps_4s_real_001_e5ffa59001_r1"

NOMBRES_BLOQUES = {
    "00_info_entorno": "Informes de hardware y software de las máquinas cliente, servidor y de entrenamiento",
    "01_codigo": "Código entregado: cliente, controladores, modelo, evaluación, entrenamiento, scripts y pruebas",
    "02_corpus_red": "Catálogo de trazas y los ficheros CSV de red que reproduce el cliente",
    "03_modelos": "Modelo del controlador propio (pesos, configuración, normalización, planificador, manifiesto) "
                  "y cuantiles fijos de la variante sin red",
    "04_evidencia_final": "Paquete de evidencia del experimento final y su verificación fuera de línea",
    "05_contenido_dash": "Contenido DASH tal como lo sirve el servidor: manifiestos, inicializaciones y segmentos",
    "06_dataset_entrenamiento": "Conjunto de datos con el que se entrenó el modelo propio",
}

# Significado de cada clave de la configuracion de una sesion (se cruza con los campos de las clases de datos).
SIGNIFICADO_SESION = {
    "mpd_url": "dirección HTTP del manifiesto del vídeo",
    "motor_video.nombre": "motor de reproducción: simulado o gst (GStreamer)",
    "motor_video.tiempo_min_cola": "segundos de vídeo en cola que exige el motor para salir de pausa, al "
                                   "arrancar y tras una parada",
    "motor_video.decodificar_video": "con GStreamer, decodifica el vídeo y lo muestra; si no, lo descarta sin "
                                     "decodificar",
    "motor_video.nombre_sink": "elemento de salida de GStreamer; vacío elige uno según la clave anterior",
    "controlador.nombre": "clave del controlador en el registro (Tabla B.2)",
    "controlador.parametros": "diccionario de parámetros que recibe el constructor del controlador",
    "reproduccion.calidad_inicial": "índice del nivel con el que se descarga el primer segmento",
    "reproduccion.decision_inicial_controlador": "si es verdadero, el controlador decide también el primer segmento",
    "reproduccion.headless": "indicador de ejecución sin pantalla, archivado en el manifiesto de la sesión",
    "reproduccion.buffer_maximo_s": "tope del buffer; por encima, el descargador espera",
    "reproduccion.espera_vaciado_buffer_s": "paso de espera mientras el buffer está lleno",
    "reproduccion.preroll_s": "segundos iniciales de la sesión cuyas filas se marcan como arranque en la telemetría",
    "reproduccion.max_segmentos_video": "segmentos que se reproducen; vacío reproduce el vídeo entero",
    "descargador.max_reintentos": "reintentos de cada petición HTTP antes de dar el segmento por fallido",
    "descargador.detallado": "registro detallado de cada petición",
    "reproduccion_red.activada": "activa la emulación de red por traza",
    "reproduccion_red.ruta_csv_traza": "fichero CSV de la traza (tiempo, duración y throughput de cada muestra)",
    "reproduccion_red.inicio_ventana_s": "segundo de la traza en que empieza la ventana",
    "reproduccion_red.duracion_ventana_s": "duración de la ventana; vacío usa la traza hasta el final",
    "reproduccion_red.politica_fin": "qué hacer al agotar la ventana: fail detiene la sesión y loop la repite",
    "reproduccion_red.max_bucles": "vueltas adicionales permitidas con la política loop",
    "reproduccion_red.tiempos_compactos": "reconstruye el eje de tiempos de la traza encadenando las muestras sin "
                                          "huecos",
    "reproduccion_red.con_esperas": "espera de verdad el tiempo de descarga que dicta la traza; si es falso, "
                                    "solo lo calcula",
    "salida.dir_raiz": "carpeta bajo la que se crea el directorio de la sesión",
    "salida.fichero_telemetria_segmentos": "nombre del fichero de telemetría por segmento",
    "salida.fichero_segmentos_evaluacion": "nombre del fichero de segmentos de evaluación",
    "registro.activada": "activa el registro de la sesión en consola y en fichero",
    "registro.nivel": "nivel del registro (INFO, DEBUG, …)",
    "analisis.activada": "reservada; el cliente entregado no la usa",
    "analisis.raiz_salida": "reservada; el cliente entregado no la usa",
}

# Significado de cada clave de la configuracion de la evaluacion (se cruza con los valores por defecto del codigo).
SIGNIFICADO_EVALUACION = {
    "rutas.ruta_catalogo": "catálogo de trazas",
    "rutas.raiz_salida": "carpeta donde se crea cada paquete de evidencia (fecha, hora y preset en el nombre)",
    "rutas.raiz_repo": "carpeta del código, desde la que se lanza cada sesión",
    "rutas.python": "intérprete con el que se lanza cada sesión",
    "rutas.reescrituras_rutas_trazas": "pares de ruta vieja y nueva para reubicar los CSV del catálogo en otra "
                                       "máquina",
    "experimento.preset": "nombre del preset: tamaño, partición, filtro de ventanas y reglas del experimento",
    "experimento.semilla": "semilla del sorteo de ventanas y del orden de los controladores",
    "experimento.motor": "motor de reproducción de todas las sesiones",
    "experimento.controladores": "claves de los controladores que se comparan; vacío toma todos los comparables",
    "experimento.ids_perfiles_video": "vídeos del experimento; vacío toma los del preset",
    "experimento.incluir_diagnostico_sintetico": "añade las ventanas sintéticas de diagnóstico",
    "experimento.repeticiones": "repeticiones de cada escenario",
    "experimento.grupos_fuga_excluidos": "grupos de captura que no pueden salir en el sorteo",
    "reproduccion_red.duracion_ventana_s": "duración de la ventana de traza (el preset la fija)",
    "reproduccion_red.decision_interval_s": "duración del segmento con que se estima la duración de cada sesión",
    "reproduccion_red.politica_fin": "como en la sesión; común a todas (el preset puede fijarla)",
    "reproduccion_red.max_bucles": "como en la sesión; común a todas (el preset puede fijarlo)",
    "reproduccion_red.tiempos_compactos": "como en la sesión; común a todas",
    "reproduccion_red.min_media_throughput_kbps_for_formal": "throughput medio mínimo de una traza para entrar en "
                                                             "un preset formal",
    "reproduccion_red.min_max_throughput_kbps_for_formal": "throughput máximo mínimo de una traza para entrar en "
                                                           "un preset formal",
    "reproduccion_red.con_esperas": "como en la sesión; común a todas",
    "reproduccion.max_segmentos_video": "como en la sesión (el preset lo fija)",
    "reproduccion.calidad_inicial": "como en la sesión",
    "reproduccion.decision_inicial_controlador": "como en la sesión",
    "reproduccion.buffer_maximo_s": "como en la sesión",
    "reproduccion.espera_vaciado_buffer_s": "como en la sesión",
    "reproduccion.preroll_s": "como en la sesión",
    "ejecucion.tiempo_limite_s": "tiempo límite por sesión; superado, la sesión se da por fallida",
    "ejecucion.reanudar": "al relanzar sobre un paquete existente, salta las sesiones ya completadas",
    "ejecucion.ejecutar_sesiones": "si es falso, solo planifica",
    "ejecucion.ejecutar_analisis": "si es falso, no analiza al terminar",
    "ejecucion.max_sesiones": "límite técnico de sesiones para pruebas del ejecutor",
    "parametros_controladores.<clave>": "parámetros del constructor de cada controlador (Tabla B.2); en el "
                                        "controlador propio y sus variantes: carpeta del modelo, respaldo, "
                                        "comprobación de huellas, latencia máxima de inferencia y modo",
}

OPCIONES_EJECUTOR = {
    "--config": "fichero local de configuración; por defecto config/evaluacion.local.json si existe",
    "--preset": "preset del experimento; sobrescribe el de la configuración",
    "--raiz-salida": "carpeta externa donde crear el paquete",
    "--raiz-paquete": "paquete existente sobre el que reanudar o analizar",
    "--ensayo": "genera el protocolo y las configuraciones de sesión sin ejecutar nada",
    "--solo-plan": "genera solo el protocolo y el plan de sesiones",
    "--sin-analisis": "no recalcula los resultados al terminar",
    "--reanudar": "reanuda un paquete existente saltando las sesiones completadas",
    "--no-reanudar": "no reanuda: vuelve a ejecutar todas las sesiones",
    "--max-sesiones": "límite técnico de sesiones para pruebas",
    "--paralelo": "sesiones simultáneas; por defecto una, como en el experimento",
    "--escribir-config-ejemplo": "escribe config/evaluacion.local.example.json y termina",
}

SCRIPTS = [
    ("1_contenido/herramienta_video.sh", "prepara los vídeos de origen: recorte, cambio de fotogramas y "
                                         "normalización a H.264", "servidor; interactivo"),
    ("1_contenido/generar_dash_lote.sh", "codifica los seis niveles y empaqueta los segmentos de 2 s y 4 s con "
                                         "sus manifiestos", "servidor; ffmpeg y GPAC"),
    ("1_contenido/extraer_tamanos_reales_segmentos.py", "lee los manifiestos servidos y escribe el descriptor "
                                                        "de tamaños reales por segmento de cada vídeo",
     "cualquiera con acceso al servidor"),
    ("2_entrenamiento/generar_dataset.py", "construye el conjunto de datos fiel al medio a partir del catálogo "
                                           "(apartado 5.7)", "entrenamiento"),
    ("2_entrenamiento/entrenar_modelo.py", "entrena el conjunto de redes de cuantiles", "entrenamiento; GPU"),
    ("2_entrenamiento/exportar_bundle.py", "exporta el modelo entrenado al formato que carga el cliente, con el "
                                           "manifiesto de huellas", "entrenamiento"),
    ("2_entrenamiento/calcular_cuantiles_fijos.py", "calcula los cuantiles fijos de la variante sin red a partir "
                                                    "del conjunto de entrenamiento", "entrenamiento"),
    ("2_entrenamiento/wsl_generar_dataset.sh", "envoltorio de generar_dataset.py con las rutas del proyecto",
     "entrenamiento"),
    ("2_entrenamiento/wsl_entrenar_modelo.sh", "envoltorio de entrenar_modelo.py con las rutas del proyecto",
     "entrenamiento"),
    ("2_entrenamiento/wsl_exportar_bundle.sh", "envoltorio de exportar_bundle.py; empaqueta el modelo para "
                                               "llevarlo al cliente", "entrenamiento"),
    ("3_evaluacion/ejecutar_evaluacion.py", "planifica y ejecuta la evaluación comparativa y construye el "
                                            "paquete de evidencia (Tabla B.4)", "cliente"),
    ("3_evaluacion/gui_evaluacion.py", "interfaz gráfica mínima que elige preset y controladores y lanza el "
                                       "ejecutor", "cliente"),
    ("3_evaluacion/analizar_resultados.py", "vuelve a analizar un paquete ya ejecutado: resultados, contrastes, "
                                            "compuertas y gráficas", "cualquiera"),
    ("3_evaluacion/verificar_paquete.py", "verifica la estructura y los conteos de un paquete", "cualquiera"),
]

# Columnas de segmentos.csv (una fila por decision evaluable) y de las principales de sesiones.csv.
COLUMNAS_SEGMENTOS = {
    "id_sesion": "identificador de la sesión en el plan",
    "alias_controlador": "clave del controlador",
    "nombre_visible_controlador": "nombre legible del controlador",
    "id_ventana_traza": "identificador de la ventana de red",
    "id_perfil_video": "identificador del vídeo",
    "id_dataset": "conjunto de trazas de origen",
    "semantica": "tipo de medida de la traza según el catálogo",
    "condicion_red": "etiqueta de calidad de la traza según el catálogo",
    "tramo_dificultad": "estrato de capacidad y variabilidad de la ventana (baja, media, alta; con o sin "
                        "variabilidad)",
    "sintetica": "1 si la ventana es sintética de diagnóstico",
    "repeticion": "número de repetición del escenario",
    "indice_segmento": "índice del segmento dentro del vídeo",
    "indice_segmento_media": "posición de la decisión dentro de la sesión",
    "bitrate_kbps": "tasa nominal del nivel elegido (kbit/s)",
    "calidad_mbps": "término de calidad de la QoE: la tasa nominal en Mbit/s",
    "tamano_segmento_bytes": "bytes reales descargados del segmento",
    "tiempo_descarga_s": "tiempo de descarga que dictó la traza (s)",
    "throughput_medido_kbps": "throughput medido en esa descarga (kbit/s)",
    "buffer_s": "buffer en el momento de la decisión (s)",
    "buffer_despues_s": "mismo valor que la anterior; se conserva por compatibilidad del esquema",
    "rebuffering_s": "parada atribuida al segmento (s)",
    "suavidad_mbps": "cambio de calidad respecto al segmento anterior, en valor absoluto (Mbit/s)",
    "recompensa_qoe_lineal": "término de QoE del segmento: calidad menos 4,3 veces la parada menos el cambio",
    "latencia_decision_ms": "tiempo de la decisión medido en el cliente (ms)",
    "red_activada": "1 si la decisión usó la red de cuantiles",
    "red_solo_diagnostico": "1 si la red corrió solo en modo diagnóstico, sin decidir",
    "etiqueta_modelo_red": "identificador del modelo cargado",
    "bundle_cargado": "1 si el modelo se cargó",
    "hash_bundle_ok": "1 si las huellas de los ficheros del modelo coincidieron con el manifiesto",
    "vector_features_ok": "1 si el vector de entrada de la red se construyó completo",
    "ms_inferencia_red": "tiempo de la inferencia de la red (ms)",
    "accion_bruta_red": "nivel propuesto por el planificador antes de la máscara de seguridad",
    "accion_segura_red": "nivel tras la máscara de seguridad",
    "accion_valida_red": "1 si la acción pasó la validación",
    "respaldo_usado": "1 si decidió el controlador de respaldo",
    "motivo_respaldo_red": "motivo del respaldo, si lo hubo",
}

COLUMNAS_SESIONES = {
    "id_sesion, alias_controlador, id_ventana_traza, id_perfil_video, sintetica, repeticion":
        "identificación de la sesión, como en segmentos.csv",
    "estado_ejecucion, evaluables, motivo_no_evaluable": "estado final (completado o fallido), si la sesión entra "
                                                        "en el análisis y, si no, por qué",
    "num_segmentos": "decisiones evaluables de la sesión",
    "qoe_lineal_media, qoe_lineal_suma": "QoE lineal media por segmento (la métrica primaria) y su suma",
    "qoe_log_media": "QoE con utilidad logarítmica, media por segmento (secundaria)",
    "bitrate_medio_kbps, calidad_media_mbps": "tasa nominal media de los segmentos descargados",
    "rebuffering_total_s, num_stalls, proporcion_rebuffering": "parada total (s), número de paradas y fracción "
                                                               "del tiempo de sesión parado",
    "penalizacion_suavidad, suavidad_positiva_mbps, suavidad_negativa_mbps": "penalización por cambios de "
                                                                            "calidad, total y separada en "
                                                                            "subidas y bajadas",
    "num_cambios_calidad, num_subidas, num_bajadas, tasa_cambios, magnitud_media_cambio_kbps": "cambios de nivel: "
                                                                                              "cuántos, de qué "
                                                                                              "signo y de qué "
                                                                                              "tamaño medio",
    "buffer_medio_s, proporcion_buffer_bajo": "buffer medio en las decisiones y fracción de decisiones con menos "
                                              "de 5 s",
    "latencia_decision_ms_media, latencia_decision_ms_p95": "latencia de decisión, media y percentil 95 (ms)",
    "ms_inferencia_red_media, ms_inferencia_red_p95": "tiempo de inferencia de la red, media y percentil 95 (ms)",
    "num_filas_respaldo, proporcion_filas_respaldo": "decisiones tomadas por el respaldo y su fracción",
    "num_filas_red_activada, num_filas_inferencia_red, num_filas_auditoria_red_ok": "decisiones con la red "
                                                                                   "activa, inferencias "
                                                                                   "registradas y filas de "
                                                                                   "auditoría válidas",
    "tramo_dificultad, condicion_red, semantica, id_dataset, particion_origen": "estratos y procedencia de la "
                                                                               "ventana, como en segmentos.csv",
}


# ---------------------------------------------------------------------------------------------------------
def texto_docx(ruta):
    d = Document(str(ruta))
    t = "\n".join(p.text for p in d.paragraphs)
    for tabla in d.tables:
        for fila in tabla.rows:
            for celda in fila.cells:
                t += "\n" + celda.text
    return t


def fmt_num(n):
    """Enteros con espacio de miles a partir de cinco cifras (biblia §5)."""
    n = int(n)
    s = str(n)
    if n < 10000:
        return s
    grupos = []
    while s:
        grupos.insert(0, s[-3:])
        s = s[:-3]
    return " ".join(grupos)


def fmt_dec(x, dec=1):
    return ("{0:." + str(dec) + "f}").format(x).replace(".", ",")


def fmt_bytes(n):
    if n >= 1e9:
        return fmt_dec(n / 1e9, 1) + " GB"
    if n >= 1e6:
        return fmt_dec(n / 1e6, 1) + " MB"
    return fmt_dec(n / 1e3, 0) + " kB"


def tamano_y_ficheros(carpeta, excluir_dirs=(".idea",)):
    n = 0
    bytes_ = 0
    for raiz, dirs, ficheros in os.walk(carpeta):
        dirs[:] = [d for d in dirs if d not in excluir_dirs]
        for f in ficheros:
            n += 1
            bytes_ += (Path(raiz) / f).stat().st_size
    return n, bytes_


def leer_csv(ruta):
    with open(ruta, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def datos_verificados():
    d = {}
    # --- Inventario -----------------------------------------------------------------------------------
    inventario = []
    for bloque in sorted(NOMBRES_BLOQUES):
        n, b = tamano_y_ficheros(TFG_MATERIAL / bloque)
        inventario.append((bloque, n, b))
    d["inventario"] = inventario
    inv = {b: (n, s) for b, n, s in inventario}
    assert inv["01_codigo"][0] == 103, inv["01_codigo"]
    assert inv["03_modelos"][0] == 6 and inv["00_info_entorno"][0] >= 3
    assert (INFO_ENTORNO / "info_entorno_cliente.txt").exists() and (INFO_ENTORNO / "info_entorno_servidor.txt").exists()
    assert (INFO_ENTORNO / "info_entorno_wsl.txt").exists()
    d["total_ficheros"] = sum(n for _, n, _ in inventario)
    d["total_bytes"] = sum(b for _, _, b in inventario)

    # --- Codigo entregado ------------------------------------------------------------------------------
    modulos_py = [p for p in CODIGO.rglob("*.py") if ".idea" not in p.parts]
    d["n_modulos_py"] = len(modulos_py)
    n_tests = sum(len(re.findall(r"^\s*def test_", p.read_text(encoding="utf-8"), re.M))
                  for p in (CODIGO / "pruebas").glob("test_*.py"))
    assert n_tests == 18, n_tests
    d["n_tests"] = n_tests
    for rel, _, _ in SCRIPTS:
        assert (CODIGO / "scripts" / rel).exists(), rel
    assert len(SCRIPTS) == len(list((CODIGO / "scripts").rglob("*.py")) + list((CODIGO / "scripts").rglob("*.sh")))
    main_src = (CODIGO / "main.py").read_text(encoding="utf-8")
    assert 'nombre_motor == "simulado"' in main_src and 'nombre_motor == "gst"' in main_src
    assert "--config" in main_src
    req = (CODIGO / "requirements.txt").read_text(encoding="utf-8")
    assert "requests" in req and "numpy" in req and "matplotlib" in req and "PyTorch" in req and "GStreamer" in req
    d["requisitos"] = [l.strip() for l in req.splitlines() if l.strip() and not l.startswith("#")]

    from core.configuracion_cliente import ConfigCliente  # noqa: E402
    from core.controladores.registro import REGISTRO_CONTROLADORES  # noqa: E402
    from core.evaluacion.catalogo import ESPECIFICACIONES_PRESET, NOMBRES_PRESET  # noqa: E402
    from core.evaluacion.configuracion import CONFIG_EVALUACION_POR_DEFECTO  # noqa: E402
    from core.artefactos_salida import (  # noqa: E402
        FICHERO_CONFIG_RESUELTA, FICHERO_ENTORNO, FICHERO_LOG_EJECUCION, FICHERO_MANIFIESTO_EJECUCION,
        FICHERO_SEGMENTOS_EVALUACION, FICHERO_TELEMETRIA_SEGMENTOS)

    # Claves de la sesion, desde las clases de datos.
    filas_sesion = []
    for campo in dataclasses.fields(ConfigCliente):
        if campo.name == "ruta_origen":
            continue
        if dataclasses.is_dataclass(campo.type) or (campo.default_factory is not dataclasses.MISSING
                                                     and dataclasses.is_dataclass(campo.default_factory)):
            sub = campo.default_factory()
            for sc in dataclasses.fields(sub):
                clave = "{0}.{1}".format(campo.name, sc.name)
                filas_sesion.append((clave, getattr(sub, sc.name)))
        else:
            filas_sesion.append((campo.name, campo.default if campo.default is not dataclasses.MISSING else ""))
    claves = [c for c, _ in filas_sesion]
    assert set(claves) == set(SIGNIFICADO_SESION), set(claves) ^ set(SIGNIFICADO_SESION)
    d["claves_sesion"] = filas_sesion

    # Controladores, desde el registro.
    controladores = []
    for clave, ficha in REGISTRO_CONTROLADORES.items():
        firma = inspect.signature(ficha.fabrica)
        params = [p for p in firma.parameters if not p.startswith("_") and p not in ("args", "kwargs")]
        if isinstance(ficha.fabrica, __import__("functools").partial):
            params = [p for p in params if p not in ficha.fabrica.keywords]
        if "parametros" in params:  # el MPC robusto hereda del MPC basico y le pasa el resto de parametros
            base = next(p for c, _, p in controladores if c == "mpc")
            params = [p for p in params if p != "parametros"] + list(base)
        controladores.append((clave, ficha.etiqueta, params))
    assert [c for c, _, _ in controladores] == ["basado_en_tasa", "bba", "bola", "mpc", "mpc_robusto",
                                                 "controlador_propio", "propio_mediana", "propio_cuantiles_fijos",
                                                 "propio_cuantiles_recientes"]
    d["controladores"] = controladores

    # Configuracion de la evaluacion, desde los valores por defecto del codigo.
    filas_eval = []
    for seccion, valor in CONFIG_EVALUACION_POR_DEFECTO.items():
        if seccion == "version_esquema":
            continue
        if seccion == "parametros_controladores":
            filas_eval.append(("parametros_controladores.<clave>", "por controlador"))
            continue
        for k, v in valor.items():
            filas_eval.append(("{0}.{1}".format(seccion, k), v))
    assert set(c for c, _ in filas_eval) == set(SIGNIFICADO_EVALUACION), \
        set(c for c, _ in filas_eval) ^ set(SIGNIFICADO_EVALUACION)
    d["claves_eval"] = filas_eval
    assert "final_blindaje" in NOMBRES_PRESET
    pf = ESPECIFICACIONES_PRESET["final_blindaje"]
    assert pf["ventanas_reales"] == "todas" and pf["ventanas_sinteticas"] == 3 and pf["particion"] == "eval"
    assert pf["duracion_ventana_red_s"] == 160.0 and pf["max_segmentos_video"] == 30 and pf["tiempo_limite_s"] == 900.0
    assert pf["filtro_ventanas"] == "pensieve" and pf["politica_fin"] == "loop" and pf["max_bucles"] == 1
    d["n_presets"] = len(NOMBRES_PRESET)

    # Opciones del ejecutor, desde su codigo fuente.
    src = (CODIGO / "scripts" / "3_evaluacion" / "ejecutar_evaluacion.py").read_text(encoding="utf-8")
    opciones = re.findall(r'add_argument\(\s*"(--[a-z-]+)"', src)
    assert set(opciones) == set(OPCIONES_EJECUTOR), set(opciones) ^ set(OPCIONES_EJECUTOR)
    d["opciones"] = opciones
    for s in ("analizar_resultados.py", "verificar_paquete.py"):
        t = (CODIGO / "scripts" / "3_evaluacion" / s).read_text(encoding="utf-8")
        assert '"raiz_paquete"' in t
    assert "--sin-graficas" in (CODIGO / "scripts" / "3_evaluacion" / "analizar_resultados.py").read_text(encoding="utf-8")
    assert "--sin-graficas-obligatorias" in (CODIGO / "scripts" / "3_evaluacion" / "verificar_paquete.py").read_text(encoding="utf-8")
    assert "import tkinter" in (CODIGO / "scripts" / "3_evaluacion" / "gui_evaluacion.py").read_text(encoding="utf-8")
    d["ficheros_sesion"] = [FICHERO_CONFIG_RESUELTA, FICHERO_LOG_EJECUCION, FICHERO_ENTORNO,
                            FICHERO_MANIFIESTO_EJECUCION, FICHERO_SEGMENTOS_EVALUACION, FICHERO_TELEMETRIA_SEGMENTOS]

    # Configuracion local real de la evaluacion final.
    cfg = json.load(open(CODIGO / "config" / "evaluacion.local.json", encoding="utf-8"))
    assert len(cfg["experimento"]["controladores"]) == 8 and cfg["experimento"]["preset"] == "final_blindaje"
    assert cfg["experimento"]["semilla"] == 606 and len(cfg["experimento"]["grupos_fuga_excluidos"]) == 42
    assert cfg["rutas"]["ruta_catalogo"].endswith("catalogo_trazas.json")
    assert cfg["parametros_controladores"]["controlador_propio"]["verificar_hashes"] is True
    d["cfg_local"] = cfg

    # --- Paquete de evidencia -------------------------------------------------------------------------
    protocolo = json.load(open(PAQUETE / "00_protocolo" / "protocolo_validacion.json", encoding="utf-8"))
    assert protocolo["num_sesiones"] == 1208 and protocolo["preset"] == "final_blindaje"
    assert len(protocolo["controladores"]) == 8 and len(protocolo["perfiles_video"]) == 5
    assert len(protocolo["ventanas_trazas"]) == 77 and len(protocolo["grupos_fuga_excluidos"]) == 42
    assert len(protocolo["hipotesis"]["principales"]) == 5
    d["n_ventanas"] = len(protocolo["ventanas_trazas"])
    plan = leer_csv(PAQUETE / "00_protocolo" / "plan_sesiones.csv")
    assert len(plan) == 1208
    ventanas = leer_csv(PAQUETE / "00_protocolo" / "ventanas_trazas.csv")
    assert len(ventanas) == 77 and sum(1 for v in ventanas if v["sintetica"] == "True") == 3
    configs = sorted((PAQUETE / "00_protocolo" / "configs_cliente").glob("*.yaml"))
    logs = sorted((PAQUETE / "01_ejecucion" / "logs_comandos").glob("*.log"))
    ejecuciones = sorted(p for p in (PAQUETE / "01_ejecucion" / "ejecuciones").iterdir() if p.is_dir())
    assert len(configs) == 1208 and len(logs) == 1208 and len(ejecuciones) == 1208
    for carpeta in ejecuciones:
        subs = [p for p in carpeta.iterdir() if p.is_dir()]
        assert len(subs) == 1 and sorted(p.name for p in subs[0].iterdir()) == sorted(d["ficheros_sesion"]), carpeta
    n_seg = sum(1 for _ in open(PAQUETE / "02_resultados" / "segmentos.csv", encoding="utf-8")) - 1
    n_ses = sum(1 for _ in open(PAQUETE / "02_resultados" / "sesiones.csv", encoding="utf-8")) - 1
    assert n_seg == 35032 and n_ses == 1208
    d["n_decisiones"] = n_seg
    cab_seg = next(csv.reader(open(PAQUETE / "02_resultados" / "segmentos.csv", encoding="utf-8")))
    assert set(cab_seg) == set(COLUMNAS_SEGMENTOS), set(cab_seg) ^ set(COLUMNAS_SEGMENTOS)
    d["columnas_segmentos"] = cab_seg
    cab_ses = next(csv.reader(open(PAQUETE / "02_resultados" / "sesiones.csv", encoding="utf-8")))
    for grupo in COLUMNAS_SESIONES:
        for col in grupo.split(", "):
            assert col in cab_ses, col
    d["n_columnas_sesiones"] = len(cab_ses)
    verif = (PAQUETE / "02_resultados" / "verificacion_paquete.md").read_text(encoding="utf-8")
    assert "Veredicto tecnico: OK" in verif and "segmentos_brutos: 35032" in verif
    graficas = json.load(open(PAQUETE / "03_graficas" / "graficas.json", encoding="utf-8"))
    pngs = sorted((PAQUETE / "03_graficas").glob("*.png"))
    d["n_graficas"] = len(pngs)
    assert d["n_graficas"] == 16, d["n_graficas"]
    resultados = sorted(p.name for p in (PAQUETE / "02_resultados").iterdir())
    for f in ("agregados_por_controlador.json", "contrastes_prerregistrados.json", "contrastes_prerregistrados.md",
              "estadistica.json", "resumen_resultados.json", "resumen_resultados.md", "segmentos.csv",
              "sesiones.csv", "verificacion_paquete.json", "verificacion_paquete.md"):
        assert f in resultados, f
    assert (PAQUETE / "04_informe" / "conclusiones_tecnicas.md").exists()
    assert (PAQUETE / "04_informe" / "contenido_paquete.json").exists()
    for f in ("controladores.csv", "perfiles_video.csv", "plan_sesiones.json"):
        assert (PAQUETE / "00_protocolo" / f).exists(), f
    n_paq, _ = tamano_y_ficheros(PAQUETE)
    d["n_ficheros_paquete"] = n_paq
    # Sesion de ejemplo (la primera del plan con el controlador propio, como en los capitulos 5 y 6).
    primera_propio = next(s for s in plan if s["clave_controlador"] == "controlador_propio")
    assert primera_propio["id_sesion"] == SESION_EJEMPLO, primera_propio["id_sesion"]
    cfg_ejemplo = (PAQUETE / "00_protocolo" / "configs_cliente" / (SESION_EJEMPLO + ".yaml")).read_text(encoding="utf-8")
    ce = json.loads(cfg_ejemplo)  # el fichero lleva extension .yaml y contenido JSON, que el cargador acepta
    assert ce["controlador"]["nombre"] == "controlador_propio" and ce["motor_video"]["nombre"] == "simulado"
    assert ce["motor_video"]["tiempo_min_cola"] == 0.1 and ce["reproduccion"]["max_segmentos_video"] == 30
    assert ce["reproduccion"]["buffer_maximo_s"] == 60.0 and ce["reproduccion_red"]["activada"] is True
    assert ce["reproduccion_red"]["inicio_ventana_s"] == 296.0 and ce["reproduccion_red"]["duracion_ventana_s"] == 160.0
    assert ce["reproduccion_red"]["politica_fin"] == "loop" and ce["reproduccion_red"]["max_bucles"] == 1
    assert "fcc_measuring_broadband_america" in ce["reproduccion_red"]["ruta_csv_traza"]
    assert ce["controlador"]["parametros"]["verificar_hashes"] is True
    assert ce["controlador"]["parametros"]["controlador_respaldo"] == "mpc_robusto"
    d["cfg_ejemplo"] = cfg_ejemplo.rstrip("\n").splitlines()
    assert len(d["cfg_ejemplo"]) <= 60

    # Verificacion fuera de linea.
    huellas = (VERIFICACION / "huellas_paquete.sha256").read_text(encoding="utf-8").splitlines()
    assert len(huellas) == n_paq == 9699, (len(huellas), n_paq)
    leeme = (VERIFICACION / "LEEME.md").read_text(encoding="utf-8")
    m = re.search(r"Huella de la propia lista: `([0-9a-f]{64})`", leeme)
    assert m
    d["huella_lista"] = m.group(1)
    assert d["huella_lista"][:8] in texto_docx(BORRADORES / "cap6_3_integridad_verificacion.docx")
    aud = json.load(open(VERIFICACION / "auditoria_decisiones.json", encoding="utf-8"))
    assert sum(v["decisiones"] for v in aud["por_controlador"].values()) == 35032
    assert all(v["distintas"] == 0 and v["respaldos"] == 0 for v in aud["por_controlador"].values())
    sim = json.load(open(VERIFICACION / "validacion_simulador.json", encoding="utf-8"))
    assert sim["forzado"]["sesiones"] == 1184 and sim["forzado"]["niveles_identicos"] == 1184
    d["scripts_verificacion"] = sorted(p.name for p in VERIFICACION.glob("*.py"))

    # --- Corpus ---------------------------------------------------------------------------------------
    cat = json.load(open(CORPUS / "catalogo_trazas.json", encoding="utf-8"))
    assert cat["num_trazas"] == 6768 and len(cat["trazas"]) == 6768
    assert cat["politica_particion"] == "by_leakage_group"
    por = defaultdict(lambda: {"n": 0, "dur": 0.0, "part": Counter(), "sem": Counter(), "grupos": set()})
    for t in cat["trazas"]:
        x = por[t["id_dataset"]]
        x["n"] += 1
        x["dur"] += float(t.get("duracion_s") or 0.0)
        x["part"][t["particion"]] += 1
        x["sem"][t["semantica"]] += 1
        x["grupos"].add(t["grupo_fuga"])
    assert len(por) == 12
    d["corpus"] = {k: v for k, v in sorted(por.items())}
    d["corpus_particiones"] = cat["conteo_particiones"]
    d["corpus_excluidas"] = (cat["num_excluidas_calidad"], cat["num_duplicadas_excluidas"],
                             cat["num_trazas_manifiesto_origen"])
    assert d["corpus_excluidas"] == (213, 11, 6981)
    n_csv = sum(1 for _ in (CORPUS / "datasets_normalizados").rglob("*.csv"))
    d["n_csv_corpus"] = n_csv
    assert n_csv == 6992, n_csv
    d["esquema_csv"] = next(csv.reader(open(next((CORPUS / "datasets_normalizados").rglob("*.csv")), encoding="utf-8")))
    assert d["esquema_csv"] == ["tiempo_s", "duracion_s", "throughput_kbps"], d["esquema_csv"]

    # --- Modelos --------------------------------------------------------------------------------------
    man = json.load(open(MODELOS / "modelo_propio" / "bundle" / "manifiesto.json", encoding="utf-8"))
    assert len(man["ficheros"]) == 4 and man["tamano_ensemble"] == 5 and man["alfa_riesgo"] == 0.75
    assert sorted(man["ficheros_requeridos"]) == sorted(p.name for p in (MODELOS / "modelo_propio" / "bundle").iterdir())
    d["ficheros_bundle"] = man["ficheros_requeridos"]
    cf = json.load(open(MODELOS / "cuantiles_fijos" / "cuantiles_fijos.json", encoding="utf-8"))
    assert cf["horizonte_segmentos"] == 5 and len(cf["cuantiles"]) == 4

    # --- Contenido ------------------------------------------------------------------------------------
    videos = []
    for f in sorted((CODIGO / "perfiles_video" / "tamanos_segmentos").glob("*.json")):
        x = json.load(open(f, encoding="utf-8"))
        reps = x["representations"]
        assert [r["bandwidth_bps"] for r in reps] == [300000, 750000, 1200000, 1850000, 2850000, 4300000]
        alto = reps[-1]["segment_bytes"]
        total = sum(sum(r["segment_bytes"]) for r in reps)
        fps = "60" if reps[0]["frame_rate"].startswith("60") else "30"
        carpeta = x["mpd_url"].split("/dash/")[1].split("/")[0]
        assert (CONTENIDO / carpeta / "4sec").is_dir(), carpeta
        mpd = x["mpd_url"].rsplit("/", 1)[1]
        assert (CONTENIDO / carpeta / "4sec" / mpd).exists(), mpd
        videos.append({
            "carpeta": carpeta, "fps": fps, "segmentos": x["num_segmentos"], "total": total,
            "ratio_real_nominal": sum(alto) / len(alto) / reps[-1]["cbr_nominal_bytes"],
            "max_min": max(alto) / min(alto),
        })
    assert len(videos) == 9
    d["videos"] = videos
    d["n_contenido_carpetas"] = sum(1 for p in CONTENIDO.iterdir() if p.is_dir())
    assert d["n_contenido_carpetas"] == 9

    # --- Dataset de entrenamiento ----------------------------------------------------------------------
    rd = json.load(open(DATASET / "resumen_dataset.json", encoding="utf-8"))
    d["dataset"] = (rd["conteo_muestras"]["entrenamiento"], rd["conteo_muestras"]["validacion"],
                    rd["conteo_ventanas_generacion"]["entrenamiento"], rd["conteo_ventanas_generacion"]["validacion"])
    assert rd["cuantiles"] == [0.1, 0.25, 0.5, 0.75]

    # --- Remisiones a capitulos ya escritos -------------------------------------------------------------
    assert "Tabla 6.3" in texto_docx(BORRADORES / "cap6_1_diseno_experimento.docx")
    assert "Tabla 5.5" in texto_docx(BORRADORES / "cap5_4_ejecutor_configuracion.docx")
    cap1 = texto_docx(BORRADORES / "cap1_introduccion.docx")
    assert "la reproducción del experimento a partir del paquete de evidencia, el manual de uso del cliente" in cap1
    claves_bib = set(re.findall(r"^@\w+\{([^,]+),", BIB.read_text(encoding="utf-8"), re.M))
    for c in CITAS:
        assert c in claves_bib, c
    return d


# ---------------------------------------------------------------------------------------------------------
def anexo(b, letra, titulo):
    b.doc.add_paragraph("Anexo {0}".format(letra), style="Capitulo numero")
    b.doc.add_paragraph(titulo, style="Heading 1")


def valor_texto(v):
    if v is None or v == "":
        return "vacío"
    if isinstance(v, bool):
        return "verdadero" if v else "falso"
    if isinstance(v, float):
        return fmt_dec(v, 2).rstrip("0").rstrip(",") if v != int(v) else str(int(v))
    if isinstance(v, (list, dict)):
        return "vacío" if not v else str(v)
    return str(v)


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    d = datos_verificados()
    b = Borrador(PLANTILLA)

    # ===================================================================================================
    anexo(b, "A", "Reproducción del experimento a partir del material entregado")
    b.parrafo(
        "Este anexo describe cómo se repite el experimento del capítulo 6 con el material que acompaña a la memoria. "
        "Primero inventaría ese material, después recorre los pasos en el orden en que se ejecutaron en el proyecto, "
        "preparar la máquina cliente, servir el contenido, comprobar el código, lanzar la evaluación y analizar el "
        "paquete, y termina con las comprobaciones que no requieren volver a ejecutar nada: repetir el análisis "
        "sobre el paquete entregado y verificar su integridad. Los comandos se dan para una máquina Linux, que es "
        "donde corrió el experimento; el análisis y la verificación se han ejecutado también en Windows "
        "(apartado 6.3). Los nombres de ficheros y claves son los del código entregado.")

    b.h2("A.1. Material entregado")
    b.parrafo(
        "El material se organiza en siete bloques numerados, resumidos en la Tabla A.1. Los tamaños y el número de "
        "ficheros se han contado sobre la copia entregada. El bloque más pesado es el contenido DASH, porque "
        "contiene los segmentos de los nueve vídeos en los seis niveles; el paquete de evidencia, en cambio, ocupa "
        "poco porque guarda telemetría y no vídeo. Solo el código, el corpus, los modelos y el contenido hacen "
        "falta para repetir la evaluación; el conjunto de datos de entrenamiento solo se necesita para volver a "
        "entrenar el modelo.")
    filas = []
    for bloque, n, bytes_ in d["inventario"]:
        filas.append((bloque, NOMBRES_BLOQUES[bloque], fmt_num(n), fmt_bytes(bytes_)))
    filas.append(("Total", "", fmt_num(d["total_ficheros"]), fmt_bytes(d["total_bytes"])))
    b.tabla(["Bloque", "Contenido", "Ficheros", "Tamaño"], filas,
            "Tabla A.1: Bloques del material entregado, con el número de ficheros y el tamaño de cada uno.",
            anchos_cm=[3.2, 8.2, 2.2, 2.4], alineaciones=["l", "l", "r", "r"])
    b.parrafo(
        "El código son {0} ficheros, de los que {1} son módulos de Python; el resto son los descriptores de tamaños "
        "de los nueve vídeos, la configuración de la evaluación, los scripts de shell y el fichero de requisitos. "
        "El corpus contiene el catálogo y los {2} ficheros CSV de trazas, uno por traza, con tres columnas: "
        "tiempo, duración de la muestra y throughput en kbit/s. El modelo son los {3} ficheros que carga el "
        "cliente, con un manifiesto que lleva la huella SHA-256 de los otros cuatro. El paquete de evidencia tiene "
        "{4} ficheros y la verificación fuera de línea añade la lista de sus huellas y los informes de la "
        "auditoría de decisiones y de la validación del simulador descritos en el apartado 6.3."
        .format(fmt_num(d["inventario"][1][1]), d["n_modulos_py"], fmt_num(d["n_csv_corpus"]),
                len(d["ficheros_bundle"]), fmt_num(d["n_ficheros_paquete"])))

    b.h2("A.2. Preparación de la máquina cliente")
    b.parrafo(
        "El cliente necesita Python 3 y tres paquetes: //requests// para las descargas, //NumPy// para el "
        "planificador y //matplotlib// para las gráficas del análisis. El controlador propio y sus variantes con "
        "red necesitan además //PyTorch// [pytorchDocs], que se instala aparte en su variante de CPU: la "
        "inferencia tarda milisegundos y no requiere GPU. El motor de reproducción real necesita GStreamer y sus "
        "enlaces de Python, pero el experimento usa el motor simulado y no los requiere. En la máquina virtual del "
        "experimento el intérprete fue Python 3.8.10 (Tabla 6.3); las pruebas automáticas del código se han "
        "ejecutado también con Python 3.12 en Windows.")
    b.parrafo(
        "El código espera el corpus y los modelos bajo una carpeta //TFG// en el directorio del usuario, con los "
        "nombres que fija la configuración de la evaluación: el catálogo en //TFG/catalogo_trazas.json//, los CSV "
        "en //TFG/datasets_normalizados/<conjunto>/// y los modelos en //TFG/modelos/modelo_propio/bundle/// y "
        "//TFG/modelos/cuantiles_fijos///. Las rutas de los CSV que lista el catálogo son absolutas y empiezan por "
        "///home/daniel/TFG//; en otra máquina basta con usar la misma ruta o con declarar en la configuración "
        "de la evaluación la regla de reescritura que convierte esa raíz en la nueva (clave "
        "//rutas.reescrituras_rutas_trazas//, Tabla B.3). El Listado A.1 recoge los comandos de este paso.")
    b.codigo([
        "cd ~/TFG/ClienteDashTFG",
        "pip install -r requirements.txt",
        "pip install torch --index-url https://download.pytorch.org/whl/cpu",
        "python3 -m unittest discover -s pruebas",
    ], "Listado A.1: Instalación de las dependencias y pruebas automáticas del código entregado.")
    b.parrafo(
        "La última línea ejecuta las {0} pruebas automáticas del código: carga del modelo con comprobación de "
        "huellas y paso al respaldo si falla, equivalencia del MPC robusto con su implementación de referencia, "
        "atribución de las paradas al segmento correcto, las tres variantes de ablación y el módulo de contrastes "
        "prerregistrados. Todas deben terminar sin error antes de seguir.".format(d["n_tests"]))

    b.h2("A.3. Servidor de contenido")
    b.parrafo(
        "El contenido se sirve con un servidor web estático; en el proyecto fue Apache [apacheHttpd] en una segunda "
        "máquina virtual (Tabla 6.3). Basta con copiar el bloque de contenido a la raíz publicada de forma que cada "
        "vídeo quede en una carpeta con su nombre y, dentro, la carpeta //4sec// con el manifiesto y los seis "
        "directorios de segmentos. Las direcciones que espera cada vídeo están en el catálogo de vídeos del código "
        "(//core/evaluacion/catalogo.py//), todas por HTTP y con la forma "
        "//192.168.1.132/dash/<vídeo>/4sec/<vídeo>_simple_4s.mpd//; si el servidor tiene otra dirección se "
        "cambian ahí. Antes de lanzar nada conviene pedir un manifiesto y un segmento con un navegador o con "
        "//curl// y comprobar que el servidor devuelve los bytes completos: el cliente no corrige errores del "
        "servidor, los registra y da la sesión por fallida.")

    b.h2("A.4. Comprobaciones previas y plan en seco")
    b.parrafo(
        "El fichero //config/evaluacion.local.json// del código entregado es la configuración exacta de la "
        "evaluación final: los ocho controladores, el preset del experimento, la semilla {0}, las rutas y los "
        "parámetros del controlador propio y de sus tres variantes, con la comprobación de huellas del modelo "
        "activada, y la lista de los {1} grupos de captura excluidos del sorteo. Solo hay que ajustar las rutas si "
        "la máquina no replica la del proyecto. Con esa configuración, el ejecutor puede generar el protocolo y el "
        "plan sin ejecutar ninguna sesión (Listado A.2, primera línea). La selección de ventanas es determinista "
        "(apartado 5.4.3): el plan generado debe listar las mismas {2} sesiones, en el mismo orden y con las mismas "
        "ventanas e inicios, que el fichero //00_protocolo/plan_sesiones.csv// del paquete entregado. Esa "
        "comparación, columna a columna salvo las rutas absolutas, es la primera prueba de que la máquina está "
        "bien preparada.".format(d["cfg_local"]["experimento"]["semilla"],
                                len(d["cfg_local"]["experimento"]["grupos_fuga_excluidos"]), fmt_num(1208)))
    b.codigo([
        "python3 scripts/3_evaluacion/ejecutar_evaluacion.py \\",
        "    --preset final_blindaje --solo-plan",
        "python3 scripts/3_evaluacion/ejecutar_evaluacion.py --preset final_blindaje",
        "python3 scripts/3_evaluacion/ejecutar_evaluacion.py --preset final_blindaje \\",
        "    --raiz-paquete ~/TFG/validacion_comparativa/<paquete> --reanudar",
    ], "Listado A.2: Plan en seco, ejecución completa y reanudación de la evaluación final.")

    b.h2("A.5. Ejecución")
    b.parrafo(
        "La segunda línea del Listado A.2 lanza la evaluación completa. El ejecutor crea el paquete, escribe el "
        "protocolo, el plan y una configuración por sesión, y ejecuta las {0} sesiones en serie, cada una como un "
        "proceso independiente del cliente con su configuración; al terminar analiza el paquete, aplica las "
        "compuertas y lo verifica. En la máquina virtual del proyecto tardó 41,3 h (apartado 6.1.4). Si la "
        "ejecución se interrumpe, la tercera línea la reanuda sobre el mismo paquete saltando las sesiones "
        "completadas; en el experimento final no hizo falta. La Tabla A.2 resume qué debe coincidir con el paquete "
        "entregado y qué no.".format(fmt_num(1208)))
    b.tabla(["Elemento", "Qué se espera al repetir la ejecución"], [
        ("Protocolo y plan", "idénticos: mismas ventanas, inicios, vídeos, orden de controladores e "
                             "identificadores de sesión, porque dependen solo del catálogo, la configuración y la "
                             "semilla"),
        ("Decisiones", "idénticas a las del paquete si la realimentación que recibe cada controlador es la misma; "
                       "las decisiones son deterministas dada la realimentación (apartado 6.3.3)"),
        ("Tiempos de descarga", "los dicta la traza, pero la traza se aplica sobre la descarga real; un servidor "
                                "más lento que la traza o una espera del sistema cambian la temporización"),
        ("Paradas y QoE", "iguales salvo las diferencias de temporización anteriores; en el proyecto, la física "
                          "reproducida en tiempo virtual coincidió con la máquina virtual en la mediana y difirió "
                          "en la cola (apartado 6.3.3)"),
        ("Resultados de las hipótesis", "deben reproducir el sentido y la aceptación de P1 a P5 del apartado 6.4; "
                                        "las cifras exactas solo coinciden si coinciden las sesiones"),
        ("Duración", "depende de la máquina; la estimación del protocolo es de 144 s por sesión"),
    ], "Tabla A.2: Qué debe coincidir con el paquete entregado al repetir la ejecución y qué puede variar.",
        anchos_cm=[3.6, 12.4])

    b.h2("A.6. Análisis, verificación e integridad del paquete")
    b.parrafo(
        "El análisis y la verificación existen como herramientas independientes (Listado A.3). La primera recalcula "
        "desde la telemetría todos los ficheros de //02_resultados// y las gráficas de //03_graficas//, aplica las "
        "compuertas y escribe el informe; la segunda comprueba la estructura y los conteos del paquete y escribe "
        "//verificacion_paquete.md//. Aplicadas a una copia del paquete entregado, sin ejecutar ninguna sesión, "
        "deben devolver los mismos ficheros de resultados: así se reprodujo en otra máquina el análisis del "
        "capítulo 6, incluidos los intervalos bootstrap gracias a la semilla fija del protocolo (apartado 6.3.3). "
        "Se trabaja sobre una copia porque el análisis reescribe las carpetas de resultados y gráficas.")
    b.codigo([
        "python3 scripts/3_evaluacion/analizar_resultados.py <copia_del_paquete>",
        "python3 scripts/3_evaluacion/verificar_paquete.py <copia_del_paquete>",
        "cd <paquete_original>",
        "find . -type f | LC_ALL=C sort | xargs -d '\\n' sha256sum \\",
        "    | sed 's/ \\*\\./  ./' | sha256sum",
    ], "Listado A.3: Repetición del análisis y de la verificación sobre una copia del paquete, y huella del paquete "
       "original.")
    b.parrafo(
        "La integridad del paquete entregado se comprueba con las dos últimas líneas: la huella SHA-256 de la lista "
        "ordenada de huellas de sus {0} ficheros debe ser {1}…{2}, la misma que figura en la carpeta de "
        "verificación fuera de línea y en el apartado 6.3. Esa carpeta contiene la lista completa de huellas, el "
        "informe de la auditoría que repitió las {3} decisiones con el código congelado y el informe de la "
        "validación del simulador en tiempo virtual, los dos en JSON con el detalle por sesión y por controlador. "
        .format(fmt_num(d["n_ficheros_paquete"]), d["huella_lista"][:8], d["huella_lista"][-4:],
                fmt_num(d["n_decisiones"]))
        + ("Junto a los informes van los dos programas que los generaron, que se ejecutan desde el código "
           "entregado con la ruta del paquete como argumento." if d["scripts_verificacion"] else
           "Los dos informes se generaron con programas de auditoría que leen la telemetría del paquete y crean "
           "los controladores con el código entregado; el apartado 6.3 describe su procedimiento."))

    # ===================================================================================================
    anexo(b, "B", "Manual de uso del cliente")
    b.parrafo(
        "Este anexo es la guía de uso del código entregado: cómo instalarlo, cómo ejecutar una sesión suelta y "
        "qué produce, qué controladores admite, cómo lanzar una evaluación comparativa y cómo regenerar el "
        "contenido y el modelo. Las tablas de claves y opciones se han generado leyendo el código, de modo que "
        "coinciden con él. El diseño de cada pieza está en los capítulos 4 y 5; aquí solo se explica cómo usarla.")

    b.h2("B.1. Instalación")
    b.parrafo(
        "El código no se instala como paquete: se copia la carpeta y se ejecuta desde ella. Los requisitos son los "
        "del apartado A.2 (Listado A.1): Python 3, //requests//, //NumPy// y //matplotlib// desde el fichero de "
        "requisitos, PyTorch de CPU para el controlador propio y, solo para la reproducción real, GStreamer con sus "
        "enlaces de Python [gstreamerDocs]. Las {0} pruebas automáticas de la carpeta //pruebas// comprueban la "
        "instalación en alrededor de un minuto.".format(d["n_tests"]))

    b.h2("B.2. Una sesión")
    b.parrafo(
        "Una sesión es una reproducción de un vídeo con un controlador. Se lanza con //main.py// y un fichero de "
        "configuración (Listado B.1). El fichero puede ser YAML o JSON: el cargador prueba primero JSON y, si no, "
        "YAML con la biblioteca PyYAML si está instalada o, en su defecto, con un lector propio de YAML simple. Las "
        "claves que no aparecen toman el valor "
        "por defecto de las clases de datos del módulo //core/configuracion_cliente.py//, y la configuración "
        "resultante, con todos los valores ya resueltos, se archiva en el directorio de la sesión. La Tabla B.1 "
        "lista todas las claves con su valor por defecto y su significado.")
    b.codigo(["python3 main.py --config mi_sesion.yaml"],
             "Listado B.1: Lanzamiento de una sesión del cliente con un fichero de configuración.")
    filas = [(c, valor_texto(v), SIGNIFICADO_SESION[c]) for c, v in d["claves_sesion"]]
    b.tabla(["Clave", "Por defecto", "Significado"], filas,
            "Tabla B.1: Claves de la configuración de una sesión, leídas de las clases de datos del código "
            "entregado, con su valor por defecto.", anchos_cm=[5.0, 3.0, 8.0])
    b.parrafo(
        "El Listado B.2 reproduce la configuración de la sesión {0} del experimento final, la primera del plan en "
        "que corre el controlador propio y el ejemplo de los capítulos 5 y 6, tal como la escribió el ejecutor en "
        "el paquete de evidencia. Es un fichero JSON con extensión //.yaml//, que el cargador acepta. Se ve la "
        "emulación de red activada sobre una traza de la FCC con ventana de 160 s desde el segundo 296 y una "
        "vuelta de seguridad, el motor simulado con cola mínima de 0,1 s, 30 segmentos, buffer de 60 s y el "
        "controlador propio con la carpeta del modelo, el respaldo y la comprobación de huellas. Para una sesión "
        "sin emulación basta con poner //reproduccion_red.activada// a falso: el cliente descarga entonces a la "
        "velocidad real de la red.".format(SESION_EJEMPLO.split("_")[0].lstrip("s0")))
    b.codigo(d["cfg_ejemplo"],
             "Listado B.2: Configuración de la sesión {0} del experimento final, copiada del paquete de evidencia."
             .format(SESION_EJEMPLO.split("_")[0].lstrip("s0")))

    b.h2("B.3. Controladores")
    b.parrafo(
        "El controlador se elige por su clave en el registro (//core/controladores/registro.py//) y recibe el "
        "diccionario de //controlador.parametros// en su constructor. La Tabla B.2 lista las nueve claves "
        "registradas con los parámetros que admite cada una; los valores por defecto son los publicados en los "
        "artículos de origen (apartado 5.5) y los del apartado 5.6 para el controlador propio. Las tres variantes de "
        "ablación son el mismo controlador propio con el modo de predicción fijado; el MPC básico existe en el "
        "registro como paso intermedio hacia su variante robusta y no corre en la evaluación. Los parámetros "
        "comunes al controlador propio y sus variantes son la carpeta del modelo (//dir_bundle//), el "
        "identificador del vídeo (//id_perfil_video//), el peso del riesgo (//alfa_riesgo//), el controlador de "
        "respaldo, la comprobación de huellas del modelo, la latencia máxima de inferencia antes de pasar al "
        "respaldo y el modo solo diagnóstico, en que la red calcula pero no decide.")
    etiquetas = {
        "basado_en_tasa": "basado en tasa (media armónica del throughput)",
        "bba": "BBA, basado en la ocupación del buffer",
        "bola": "BOLA, optimización de Lyapunov sobre el buffer",
        "mpc": "MPC básico, forma de referencia; no se evalúa",
        "mpc_robusto": "MPC robusto canónico",
        "controlador_propio": "controlador propio: predictor de cuantiles y planificador con riesgo",
        "propio_mediana": "variante sin riesgo: solo la mediana de la red",
        "propio_cuantiles_fijos": "variante sin red: cuantiles fijos del error de la media armónica",
        "propio_cuantiles_recientes": "variante sin red: cuantiles de las últimas descargas",
    }
    filas = [(clave, etiquetas[clave], ", ".join(params)) for clave, _, params in d["controladores"]]
    b.tabla(["Clave", "Controlador", "Parámetros que admite"], filas,
            "Tabla B.2: Controladores registrados en el código entregado y parámetros de su constructor, leídos "
            "del registro.", anchos_cm=[4.7, 4.9, 6.4])

    b.h2("B.4. Salidas de una sesión")
    b.parrafo(
        "Cada sesión crea bajo //salida.dir_raiz// un directorio con la fecha y la hora y escribe en él los seis "
        "ficheros del apartado 4.6: la configuración resuelta, el registro de la ejecución, la instantánea del "
        "entorno (intérprete, plataforma y versiones de los paquetes), el manifiesto de la ejecución con el estado "
        "final (creado, en marcha, completado o fallido), el fichero de segmentos de evaluación y la telemetría "
        "por segmento. La telemetría tiene una fila por segmento descargado, incluida la inicialización, con el "
        "índice y el tiempo, el diccionario completo de realimentación que recibió el controlador (columnas con "
        "prefijo //feedback_//), los tiempos de la descarga, las medidas derivadas (throughput actual, suavizado, "
        "mínimo y desviación de las cinco últimas descargas, fase de la sesión, decisión del controlador y su "
        "latencia) y las paradas. Esa telemetría es la que repite la auditoría del apartado 6.3 y la que resume el "
        "análisis en las tablas del Anexo C.")

    b.h2("B.5. Evaluación comparativa")
    b.parrafo(
        "El ejecutor (//scripts/3_evaluacion/ejecutar_evaluacion.py//) planifica y ejecuta muchas sesiones y "
        "construye el paquete de evidencia (apartado 5.4). Lee los valores por defecto del código y, encima, el "
        "fichero //config/evaluacion.local.json//, clave a clave. La Tabla B.3 lista las claves con su valor por "
        "defecto; un fichero de ejemplo se escribe con la opción correspondiente de la Tabla B.4. El preset fija "
        "el tamaño y las reglas del experimento: partición del catálogo, número o criterio de ventanas, vídeos, "
        "duración de la ventana y segmentos por sesión; el código entregado define {0} presets, del de "
        "diagnóstico con dos ventanas al del experimento final.".format(d["n_presets"]))
    filas = [(c, valor_texto(v) if c != "parametros_controladores.<clave>" else "", SIGNIFICADO_EVALUACION[c])
             for c, v in d["claves_eval"]]
    b.tabla(["Clave", "Por defecto", "Significado"], filas,
            "Tabla B.3: Claves de la configuración de la evaluación, leídas de los valores por defecto del código "
            "entregado.", anchos_cm=[5.6, 3.4, 7.0])
    b.tabla(["Opción", "Efecto"], [(o, OPCIONES_EJECUTOR[o]) for o in d["opciones"]],
            "Tabla B.4: Opciones de línea de comandos del ejecutor de la evaluación.", anchos_cm=[4.6, 11.4])
    b.parrafo(
        "El ejecutor devuelve código de salida cero solo si ninguna sesión falló y la verificación del paquete se "
        "superó. Las herramientas //analizar_resultados.py// y //verificar_paquete.py// de la misma carpeta "
        "repiten el análisis y la verificación de un paquete ya ejecutado (Listado A.3); la primera admite "
        "//--sin-graficas// y la segunda //--sin-graficas-obligatorias//. Para pruebas interactivas existe "
        "//gui_evaluacion.py//, una ventana mínima con Tkinter que elige el preset y los controladores, escribe "
        "una configuración temporal y lanza el ejecutor mostrando su progreso.")

    b.h2("B.6. Reproducción real con GStreamer")
    b.parrafo(
        "Con //motor_video.nombre// igual a //gst//, el cliente empuja los segmentos a una tubería de GStreamer en "
        "lugar de al motor simulado. Si //decodificar_video// es verdadero, la tubería decodifica el H.264 y lo "
        "muestra en pantalla con el elemento de salida por defecto del sistema; si es falso, lo descarta sin "
        "decodificar, lo que permite medir el comportamiento del demultiplexado y del buffer real sin coste de "
        "decodificación. La clave //nombre_sink// fuerza un elemento de salida concreto. El resto de la "
        "configuración, el controlador y la emulación de red son los mismos que con el motor simulado, así que "
        "una sesión real se lanza con el mismo comando del Listado B.1. El capítulo 4 compara los dos motores.")

    b.h2("B.7. Contenido y entrenamiento")
    b.parrafo(
        "Los scripts de la carpeta //scripts// se agrupan por etapa (Tabla B.5): preparar el contenido en el "
        "servidor, generar el conjunto de datos y entrenar el modelo en la máquina de entrenamiento, y evaluar en "
        "el cliente. Ninguno de los de contenido y entrenamiento hace falta para repetir la evaluación, porque el "
        "contenido servido, el modelo exportado y los cuantiles fijos forman parte del material entregado. El "
        "Listado B.3 recoge el orden de los de entrenamiento, con los envoltorios de shell que fijan las rutas del "
        "proyecto; cada script de Python acepta //--help// y lista sus opciones.")
    b.tabla(["Script", "Qué hace", "Dónde se ejecuta"], [(s, q, m) for s, q, m in SCRIPTS],
            "Tabla B.5: Scripts del código entregado, por etapa.", anchos_cm=[5.6, 7.4, 3.0])
    b.codigo([
        "bash scripts/2_entrenamiento/wsl_generar_dataset.sh",
        "bash scripts/2_entrenamiento/wsl_entrenar_modelo.sh",
        "bash scripts/2_entrenamiento/wsl_exportar_bundle.sh",
        "D=~/TFG/datasets_normalizados/modelo_propio/dataset_entrenamiento",
        "python3 scripts/2_entrenamiento/calcular_cuantiles_fijos.py \\",
        "    --dataset $D/datos_entrenamiento.jsonl \\",
        "    --salida ~/TFG/modelos/cuantiles_fijos/cuantiles_fijos.json",
    ], "Listado B.3: Orden de los scripts de entrenamiento: conjunto de datos, entrenamiento, exportación del modelo "
       "y cuantiles fijos.")
    b.parrafo(
        "El conjunto de datos entregado tiene {0} muestras de entrenamiento y {1} de validación, generadas a "
        "partir de {2} y {3} ventanas del catálogo respectivamente (apartado 5.7). El contenido se regenera con los "
        "dos scripts de shell de la primera etapa, que usan ffmpeg para codificar y GPAC para segmentar, y el "
        "descriptor de tamaños reales de cada vídeo se extrae después del servidor con el tercero.".format(
            fmt_num(d["dataset"][0]), fmt_num(d["dataset"][1]), fmt_num(d["dataset"][2]), fmt_num(d["dataset"][3])))

    # ===================================================================================================
    anexo(b, "C", "Documentación complementaria")
    b.parrafo(
        "Este anexo reúne las tablas largas a las que remite el texto: el corpus de trazas por conjunto, el "
        "contenido DASH servido, los ficheros del paquete de evidencia y el significado de las columnas de los dos "
        "ficheros de resultados sobre los que se calcula todo el capítulo 6. Todas las cifras se han contado sobre "
        "el material entregado al generar este anexo.")

    b.h2("C.1. Corpus de trazas por conjunto")
    b.parrafo(
        "El catálogo contiene {0} trazas de {1} conjuntos, once públicos y uno sintético de diagnóstico, repartidas "
        "en las particiones de entrenamiento, prueba y evaluación por grupo de captura, de modo que las trazas de "
        "un mismo dispositivo, usuario o campaña caen en la misma partición (apartado 4.7). La Tabla C.1 da, para "
        "cada conjunto, el número de trazas, las horas acumuladas, el reparto por particiones, el número de grupos "
        "de captura y el tipo de medida que contiene. Del manifiesto de conversión original, con {2} trazas, se "
        "excluyeron {3} por calidad (pocas muestras, poca duración o throughput siempre nulo) y {4} duplicadas. En "
        "el experimento final solo intervienen las ventanas de la partición de evaluación que pasan el filtro de "
        "relevancia de Pensieve [mao2017pensieve], 74 de dos conjuntos (apartado 6.1.2); el resto del catálogo "
        "sirvió para entrenar y para las pruebas previas.".format(
            fmt_num(sum(v["n"] for v in d["corpus"].values())), len(d["corpus"]),
            fmt_num(d["corpus_excluidas"][2]), d["corpus_excluidas"][0], d["corpus_excluidas"][1]))
    semanticas = {
        "active_fixed_broadband_download_test": "pruebas de descarga en acceso fijo",
        "active_mobile_speedtest": "pruebas de velocidad en móvil",
        "available_bandwidth": "ancho de banda disponible medido",
        "observed_application_traffic": "tráfico de aplicación observado",
        "real_streaming_delivery_rate": "tasa de entrega de streaming real",
        "synthetic_available_bandwidth": "ancho de banda sintético controlado",
    }
    nombres = {
        "fcc_measuring_broadband_america": "FCC Measuring Broadband America",
        "gavist5g": "GaVist 5G", "ghent_4g_lte": "Gante 4G LTE", "lumos5g": "Lumos5G",
        "norway_hsdpa_umass": "Noruega HSDPA", "nyu_mets": "NYU METS", "oboe": "Oboe",
        "puffer_stanford": "Puffer", "roma_4g_nbiot_5g_nsa": "Roma 4G, NB-IoT y 5G NSA",
        "synthetic_controlled_network": "Sintético controlado",
        "ucc_4g_lte_beyond_throughput": "UCC 4G LTE", "ucc_5g_beyond_throughput": "UCC 5G",
    }
    filas = []
    tot = Counter()
    for k, v in d["corpus"].items():
        sem = ", ".join(semanticas[s] for s in v["sem"])
        filas.append((nombres[k], fmt_num(v["n"]), fmt_dec(v["dur"] / 3600, 1),
                      "{0} / {1} / {2}".format(v["part"]["train"], v["part"]["test"], v["part"]["eval"]),
                      fmt_num(len(v["grupos"])), sem))
        tot["n"] += v["n"]
        tot["dur"] += v["dur"]
        tot["g"] += len(v["grupos"])
        for p in ("train", "test", "eval"):
            tot[p] += v["part"][p]
    assert (tot["train"], tot["test"], tot["eval"]) == tuple(d["corpus_particiones"][p] for p in ("train", "test", "eval"))
    filas.append(("Total", fmt_num(tot["n"]), fmt_dec(tot["dur"] / 3600, 1),
                  "{0} / {1} / {2}".format(tot["train"], tot["test"], tot["eval"]), fmt_num(tot["g"]), ""))
    b.tabla(["Conjunto", "Trazas", "Horas", "Entren. / prueba / eval.", "Grupos", "Tipo de medida"], filas,
            "Tabla C.1: Los doce conjuntos del catálogo de trazas: número de trazas, horas acumuladas, reparto por "
            "particiones, grupos de captura y tipo de medida. Contado sobre el catálogo entregado.",
            anchos_cm=[3.4, 1.4, 1.6, 2.9, 1.7, 5.0], alineaciones=["l", "r", "r", "c", "r", "l"])

    b.h2("C.2. Contenido DASH servido")
    b.parrafo(
        "El servidor publica nueve vídeos (Tabla C.2), cada uno codificado en los seis niveles de la escalera de "
        "300 a 4300 kbit/s y segmentado a 2 s y a 4 s; el experimento usa los de 4 s de los cuatro vídeos de 10 min "
        "vistos en el entrenamiento y del vídeo nuevo, Tears of Steel [blenderTearsOfSteel]. Los descriptores de "
        "tamaños reales que acompañan al código dan, para cada vídeo y nivel, los bytes de cada segmento. La tabla "
        "muestra dos medidas de la variabilidad del nivel más alto que importan al planificador: el cociente entre "
        "el tamaño medio real y el nominal de la tasa declarada, y el cociente entre el segmento mayor y el menor. "
        "Las dos codificaciones de Paseo de Almuñécar a 60 fps y las de 1 min son casi constantes; las de Blender "
        "y, sobre todo, Tears of Steel varían mucho de un segmento a otro, que es la situación del apartado 1.2.")
    filas = []
    for v in d["videos"]:
        filas.append((v["carpeta"].replace("_", " "), v["fps"], str(v["segmentos"]), fmt_dec(v["total"] / 1e6, 0),
                      fmt_dec(v["ratio_real_nominal"], 2), fmt_dec(v["max_min"], 1)))
    b.tabla(["Vídeo", "fps", "Segmentos", "Tamaño total (MB)", "Nivel alto: media real / nominal",
             "Nivel alto: mayor / menor"], filas,
            "Tabla C.2: Los nueve vídeos servidos, con sus segmentos de 4 s y la variabilidad de tamaño de su nivel "
            "más alto, según los descriptores de tamaños reales del código entregado.",
            anchos_cm=[4.4, 1.0, 2.2, 2.4, 3.0, 3.0], alineaciones=["l", "c", "r", "r", "r", "r"])

    b.h2("C.3. Ficheros del paquete de evidencia")
    b.parrafo(
        "El paquete del experimento final tiene cinco carpetas numeradas (Tabla C.3) y {0} ficheros. Las carpetas "
        "de protocolo y ejecución se escriben antes y durante el experimento y no se tocan después; las de "
        "resultados, gráficas e informe las recalcula el análisis a partir de las dos primeras. Junto al paquete, "
        "y fuera de él para no alterar sus huellas, va la carpeta de verificación fuera de línea del apartado A.6."
        .format(fmt_num(d["n_ficheros_paquete"])))
    filas = [
        ("00_protocolo/protocolo_validacion.json", "protocolo congelado: preset, hipótesis P1 a P5 con margen, "
                                                   "pruebas y corrección, controladores, vídeos, ventanas y grupos "
                                                   "excluidos"),
        ("00_protocolo/plan_sesiones.csv y .json", "las {0} sesiones en el orden de ejecución, con controlador, "
                                                   "ventana, vídeo y rutas".format(fmt_num(1208))),
        ("00_protocolo/ventanas_trazas.csv", "las {0} ventanas de red con traza, inicio, duración, estadísticos y "
                                             "estrato".format(d["n_ventanas"])),
        ("00_protocolo/controladores.csv, perfiles_video.csv", "controladores y vídeos del experimento con sus "
                                                               "nombres visibles"),
        ("00_protocolo/configs_cliente/", "la configuración de cada una de las {0} sesiones (Listado B.2)"
                                          .format(fmt_num(1208))),
        ("01_ejecucion/ejecuciones/<sesión>/", "el directorio de cada sesión con sus seis ficheros (apartado B.4)"),
        ("01_ejecucion/logs_comandos/", "la salida del proceso de cada sesión"),
        ("02_resultados/sesiones.csv", "una fila por sesión con sus métricas (Tabla C.5)"),
        ("02_resultados/segmentos.csv", "una fila por decisión evaluable, {0} en total (Tabla C.4)"
                                        .format(fmt_num(d["n_decisiones"]))),
        ("02_resultados/agregados_por_controlador.json", "medias, percentiles e intervalos por controlador sobre las "
                                                         "sesiones reales"),
        ("02_resultados/estadistica.json", "diferencias pareadas entre controladores y pruebas de signos"),
        ("02_resultados/contrastes_prerregistrados.json y .md", "las cinco hipótesis y las secundarias con sus "
                                                                "intervalos, valores p, corrección y decisión"),
        ("02_resultados/resumen_resultados.json y .md", "resumen legible del experimento: estado, compuertas, "
                                                        "sesiones y agregados"),
        ("02_resultados/verificacion_paquete.json y .md", "veredicto de la verificación automática y sus conteos"),
        ("03_graficas/", "{0} gráficas descriptivas y su manifiesto".format(d["n_graficas"])),
        ("04_informe/", "conclusiones técnicas automáticas y manifiesto del contenido del paquete"),
    ]
    b.tabla(["Fichero o carpeta", "Contenido"], filas,
            "Tabla C.3: Ficheros y carpetas del paquete de evidencia del experimento final.", anchos_cm=[6.4, 9.6])

    b.h2("C.4. Columnas del fichero de decisiones")
    b.parrafo(
        "El fichero //segmentos.csv// tiene una fila por decisión evaluable, {0} en total, y {1} columnas "
        "(Tabla C.4). Las construye el análisis a partir de la telemetría de cada sesión: identifica la sesión y su "
        "escenario, recoge lo que se descargó y cuánto tardó, calcula los tres términos de la QoE del segmento y "
        "copia los campos de auditoría de la red que el controlador propio y sus variantes escriben en la "
        "realimentación. En los controladores clásicos las columnas de auditoría van vacías o a cero.".format(
            fmt_num(d["n_decisiones"]), len(d["columnas_segmentos"])))
    filas = [(c, COLUMNAS_SEGMENTOS[c]) for c in COLUMNAS_SEGMENTOS]
    b.tabla(["Columna", "Significado"], filas,
            "Tabla C.4: Columnas del fichero de decisiones del paquete de evidencia.", anchos_cm=[5.4, 10.6])

    b.h2("C.5. Columnas principales del fichero de sesiones")
    b.parrafo(
        "El fichero //sesiones.csv// tiene una fila por sesión y {0} columnas. La Tabla C.5 agrupa las que usa el "
        "capítulo 6; el resto son conteos de auditoría de la red, rutas y réplicas de los identificadores del plan. "
        "Las métricas de QoE se calculan sobre las decisiones evaluables de la sesión con la fórmula del "
        "apartado 6.2.".format(d["n_columnas_sesiones"]))
    filas = [(c, COLUMNAS_SESIONES[c]) for c in COLUMNAS_SESIONES]
    b.tabla(["Columnas", "Significado"], filas,
            "Tabla C.5: Columnas principales del fichero de sesiones del paquete de evidencia.",
            anchos_cm=[7.0, 9.0])

    # Comprobaciones finales -------------------------------------------------------------------------------
    texto = "\n".join(p.text for p in b.doc.paragraphs)
    for tabla in b.doc.tables:
        for fila in tabla.rows:
            for celda in fila.cells:
                texto += "\n" + celda.text
    for nombre in PROHIBIDOS:
        assert not re.search(r"\b" + re.escape(nombre) + r"\b", texto), nombre
    claves_bib = set(re.findall(r"^@\w+\{([^,]+),", BIB.read_text(encoding="utf-8"), re.M))
    for c in set(re.findall(r"\[([A-Za-z]\w*\d{4}\w*|\w+Docs?|\w+Httpd|blender\w+)\]", texto)):
        assert c in claves_bib, c
    b.guardar(SALIDA)
    print("Guardado:", SALIDA)
    print("palabras del cuerpo:", b.palabras_cuerpo, "| tablas:", len(b.doc.tables))


if __name__ == "__main__":
    main()

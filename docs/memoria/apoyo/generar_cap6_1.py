# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap6_1_diseno_experimento.docx (apertura del capitulo 6 y 6.1).

Todo recuento sale de un programa: plan de sesiones, ventanas y protocolo del paquete final
(00_protocolo), manifiestos de las 1208 ejecuciones (fechas), configuracion y preset del codigo
entregado, huellas del kit de la VM, descriptores de tamanos de los videos, informes de entorno de
las maquinas (00_info_entorno) y entorno.json de las sesiones. Si algo no cuadra con el protocolo
o con 07_RESULTADO_FINAL.md, el script falla.

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap6_1.py
"""
from __future__ import annotations

import csv
import ctypes
import hashlib
import json
import os
import platform
import re
import statistics
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla  # noqa: E402

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
CODIGO = TFG_MATERIAL / "01_codigo" / "ClienteDashTFG"
PAQUETE = TFG_MATERIAL / "04_evidencia_final" / "20261015_031741_final_blindaje"
VERIF_WIN = TFG_MATERIAL / "04_evidencia_final" / "verificacion_windows_20261016"
INFO_ENTORNO = TFG_MATERIAL / "00_info_entorno"
CONTENIDO = TFG_MATERIAL / "05_contenido_dash"
BUNDLE = TFG_MATERIAL / "03_modelos" / "modelo_propio" / "bundle"
KIT_VM = RAIZ_REPO / "docs" / "blindaje" / "kit_vm"
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
FIG = RAIZ_REPO / "docs" / "memoria" / "figuras" / "fig_6_1_diseno_experimento.png"
SALIDA = RAIZ_REPO / "docs" / "memoria" / "borradores_docx" / "cap6_1_diseno_experimento.docx"
sys.path.insert(0, str(CODIGO))

NOMBRE_VIDEO = {
    "paseo_10min_30fps_4s": "Paseo de Almuñécar a 30 fps", "paseo_10min_60fps_4s": "Paseo de Almuñécar a 60 fps",
    "blender_10min_30fps_4s": "Blender Sunflower a 30 fps", "blender_10min_60fps_4s": "Blender Sunflower a 60 fps",
    "tears_10min_30fps_4s": "Tears of Steel a 30 fps",
}
DESCRIPTOR = {
    "paseo_10min_30fps_4s": "paseo_almunecar_10min_30fps_4s", "paseo_10min_60fps_4s": "paseo_almunecar_10min_60fps_4s",
    "blender_10min_30fps_4s": "blender_sunflower_10min_30fps_4s", "blender_10min_60fps_4s": "blender_sunflower_10min_60fps_4s",
    "tears_10min_30fps_4s": "tears_of_steel_10min_30fps_4s",
}
EN_FRASE = {
    "basado_en_tasa": "el basado en tasa", "bba": "BBA", "bola": "BOLA", "mpc_robusto": "el MPC robusto",
    "controlador_propio": "el controlador propio", "propio_mediana": "la variante de la mediana sola",
    "propio_cuantiles_recientes": "la variante de cuantiles recientes", "propio_cuantiles_fijos": "la variante de cuantiles fijos",
}
NOMBRE_ARTEFACTO = {
    "config_resuelta.json": "configuración resuelta", "ejecucion.log": "registro", "entorno.json": "entorno",
    "manifiesto_ejecucion.json": "manifiesto de la ejecución", "segmentos_evaluacion.csv": "segmentos de evaluación",
    "telemetria_segmentos.csv": "telemetría de segmentos",
}
NOMBRE_CTRL = {
    "basado_en_tasa": "Basado en tasa", "bba": "BBA", "bola": "BOLA", "mpc_robusto": "MPC robusto",
    "controlador_propio": "Controlador propio", "propio_mediana": "Propio, solo la mediana",
    "propio_cuantiles_recientes": "Propio, cuantiles recientes", "propio_cuantiles_fijos": "Propio, cuantiles fijos",
}


def coma(x, dec=2):
    return ("{0:.%df}" % dec).format(x).replace(".", ",")


def miles(n):
    # Separador de miles solo a partir de cinco cifras ("1208 sesiones", "35 032"), como la biblia.
    return "{0:,}".format(int(n)).replace(",", " ") if int(n) >= 10000 else str(int(n))


def leer_csv(ruta):
    with open(ruta, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def es_true(v):
    return str(v).strip().lower() in ("true", "1", "si", "sí")


def sha256_fichero(ruta):
    return hashlib.sha256(Path(ruta).read_bytes()).hexdigest()


def campo_info(texto, patron, grupo=1):
    m = re.search(patron, texto, re.M)
    return m.group(grupo).strip() if m else None


def maquina(nombre):
    t = (INFO_ENTORNO / "info_entorno_{0}.txt".format(nombre)).read_text(encoding="utf-8", errors="replace")
    return {
        "so": campo_info(t, r"^Description:\s*(.+)$"),
        "kernel": campo_info(t, r"^Linux \S+ (\S+)"),
        "virt": campo_info(t, r"^virtualizacion:\s*(\S+)"),
        "cpu": campo_info(t, r"^CPU:\s*(.+)$"),
        "nucleos": campo_info(t, r"^nucleos visibles:\s*(\d+)"),
        "ram": campo_info(t, r"^Mem(?:oria|):?\s+(\S+)"),
        "python": campo_info(t, r"^Python (\d+\.\d+\.\d+)"),
        "torch": campo_info(t, r"^torch:\s*(\S+)"),
        "gpu": campo_info(t, r"^gpu:\s*(.+)$"),
        "apache": campo_info(t, r"^apache2\s+(\S+)"),
        "gstreamer": campo_info(t, r"^GStreamer (\S+)"),
    }


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    from core.evaluacion.catalogo import ESPECIFICACIONES_PRESET, IDS_VIDEOS_VISTOS, ID_VIDEO_NUEVO
    from core.evaluacion.contrastes import HIPOTESIS_PRINCIPALES, MARGEN_EQUIVALENCIA_QOE, VERSION_HIPOTESIS

    # ---- Paquete: protocolo, plan, ventanas --------------------------------------------------
    protocolo = json.load(open(PAQUETE / "00_protocolo" / "protocolo_validacion.json", encoding="utf-8"))
    plan = leer_csv(PAQUETE / "00_protocolo" / "plan_sesiones.csv")
    ventanas = leer_csv(PAQUETE / "00_protocolo" / "ventanas_trazas.csv")
    config = json.load(open(CODIGO / "config" / "evaluacion.local.json", encoding="utf-8"))
    preset = ESPECIFICACIONES_PRESET["final_blindaje"]
    pe = protocolo["preset_efectivo"]

    reales = [v for v in ventanas if not es_true(v["sintetica"])]
    sinteticas = [v for v in ventanas if es_true(v["sintetica"])]
    por_dataset = Counter(v["id_dataset"] for v in reales)
    medias = [float(v["throughput_medio_ventana_kbps"]) for v in reales]
    minimos = [float(v["throughput_min_ventana_kbps"]) for v in reales]
    assert len(reales) == 74 and len(sinteticas) == 3 and por_dataset == {"oboe": 56, "fcc_measuring_broadband_america": 18}
    assert max(medias) < 6000 and min(minimos) > 200, "el filtro de relevancia no se cumple en alguna ventana"
    assert protocolo["num_sesiones"] == len(plan) == 1208 and protocolo["particion"] == "eval"
    assert protocolo["filtro_ventanas"] == "pensieve" and protocolo["orden_controladores"] == "aleatorio_por_escenario"
    assert protocolo["asignacion_videos"] == "visto_rotado_mas_nuevo" and protocolo["motor"] == "simulado"
    assert pe["duracion_ventana_red_s"] == 160.0 and pe["max_segmentos_video"] == 30 and pe["tiempo_limite_s"] == 900.0
    assert preset["politica_fin"] == "loop" and preset["max_bucles"] == 1 and preset["ventanas_reales"] == "todas"
    assert config["experimento"]["semilla"] == 606 and len(config["experimento"]["controladores"]) == 8
    grupos = config["experimento"]["grupos_fuga_excluidos"]
    grupos_sint = [g for g in grupos if g.startswith("synthetic_controlled_network:")]
    assert len(grupos) == 42 and len(grupos_sint) == 3 and protocolo["grupos_fuga_excluidos"] == sorted(grupos)
    assert protocolo["hipotesis"]["version"] == VERSION_HIPOTESIS == "hipotesis_blindaje_v1"
    assert protocolo["hipotesis"]["margen_equivalencia_qoe"] == MARGEN_EQUIVALENCIA_QOE == 0.15
    assert len(protocolo["hipotesis"]["principales"]) == len(HIPOTESIS_PRINCIPALES) == 5
    assert protocolo["version_formula_qoe"] == "qoe_lineal_v1"

    n_reales = sum(1 for s in plan if not es_true(s["sintetica"]))
    n_sint = len(plan) - n_reales
    assert n_reales == 74 * 2 * 8 == 1184 and n_sint == 3 * 1 * 8 == 24
    por_video = Counter(s["id_perfil_video"] for s in plan)
    assert por_video[ID_VIDEO_NUEVO] == 74 * 8 == 592
    # Rotacion del video visto: ventana i (en el orden del plan) lleva vistos[i % 4]; las sinteticas tambien.
    orden_ventanas = []
    for s in plan:
        if s["id_ventana_traza"] not in orden_ventanas:
            orden_ventanas.append(s["id_ventana_traza"])
    ventanas_por_visto = Counter()
    reales_por_visto = Counter()
    ids_reales = {v["id_ventana_traza"] for v in reales}
    for i, idv in enumerate(orden_ventanas):
        vistos_en_ventana = {s["id_perfil_video"] for s in plan if s["id_ventana_traza"] == idv} - {ID_VIDEO_NUEVO}
        assert vistos_en_ventana == {IDS_VIDEOS_VISTOS[i % 4]}, idv
        ventanas_por_visto[IDS_VIDEOS_VISTOS[i % 4]] += 1
        if idv in ids_reales:
            reales_por_visto[IDS_VIDEOS_VISTOS[i % 4]] += 1
    assert all(por_video[v] == ventanas_por_visto[v] * 8 for v in IDS_VIDEOS_VISTOS)
    controladores = [c["alias"] for c in protocolo["controladores"]]
    assert len(controladores) == 8 and set(controladores) == set(config["experimento"]["controladores"])
    # Parametros de los controladores: los clasicos y el MPC robusto solo reciben el video.
    params = config["parametros_controladores"]
    assert set(params) == {"controlador_propio", "propio_mediana", "propio_cuantiles_recientes", "propio_cuantiles_fijos"}
    for clave, p in params.items():
        assert p["alfa_riesgo"] == 0.75 and p["controlador_respaldo"] == "mpc_robusto" and p["latencia_max_inferencia_ms"] == 50.0
        assert p["verificar_hashes"] is True and p["solo_diagnostico"] is False
    assert "ruta_cuantiles_fijos" in params["propio_cuantiles_fijos"]
    # Los ordenes del sorteo difieren entre escenarios.
    ordenes = {}
    for s in plan:
        ordenes.setdefault((s["id_ventana_traza"], s["id_perfil_video"]), []).append(s["alias_controlador"])
    assert len(ordenes) == 74 * 2 + 3 == 151 and all(len(o) == 8 for o in ordenes.values())
    assert len(set(tuple(o) for o in ordenes.values())) > 100, "el sorteo no esta variando el orden"

    # ---- Fechas de las 1208 ejecuciones ------------------------------------------------------
    inicios = {}
    for s in plan:
        carpetas = sorted((PAQUETE / "01_ejecucion" / "ejecuciones" / s["id_sesion"]).glob("ejecucion_*"))
        assert len(carpetas) == 1, s["id_sesion"]  # una sola ejecucion por sesion (sin reanudaciones)
        m = json.load(open(carpetas[0] / "manifiesto_ejecucion.json", encoding="utf-8"))
        assert m["estado"] == "completado"
        inicios[s["id_sesion"]] = datetime.fromisoformat(m["creado_utc"].replace("Z", "+00:00"))
    ejemplo_entorno = json.load(open(sorted((PAQUETE / "01_ejecucion" / "ejecuciones" / plan[0]["id_sesion"]).glob("ejecucion_*"))[0] / "entorno.json", encoding="utf-8"))
    primero, ultimo_inicio = min(inicios.values()), max(inicios.values())
    # El fin de la ultima sesion: 07_RESULTADO da 16/10 18:34 UTC; aqui se toma el inicio de la ultima
    # sesion mas la duracion media de las 1207 anteriores.
    ordenados = sorted(inicios.values())
    duraciones = [(b - a).total_seconds() for a, b in zip(ordenados, ordenados[1:])]
    dur_media = statistics.mean(duraciones)
    fin_estimado = ultimo_inicio.timestamp() + dur_media
    horas = (fin_estimado - primero.timestamp()) / 3600
    assert 41.0 < horas < 41.6, horas
    assert max(duraciones) < 300, "hay huecos de mas de 5 minutos entre sesiones"

    # ---- Ejemplo real: la primera sesion del plan en la que corre el controlador propio -----
    ejemplo = next(s for s in plan if s["alias_controlador"] == "controlador_propio")
    num_ejemplo = int(ejemplo["id_sesion"][1:6])
    ventana_ej = next(v for v in ventanas if v["id_ventana_traza"] == ejemplo["id_ventana_traza"])
    num_ventana_ej = orden_ventanas.index(ejemplo["id_ventana_traza"]) + 1
    orden_ej = ordenes[(ejemplo["id_ventana_traza"], ejemplo["id_perfil_video"])]
    posicion_ej = orden_ej.index("controlador_propio") + 1
    carpeta_ej = sorted((PAQUETE / "01_ejecucion" / "ejecuciones" / ejemplo["id_sesion"]).glob("ejecucion_*"))[0]
    ficheros_ej = sorted(p.name for p in carpeta_ej.iterdir())
    assert len(ficheros_ej) == 6
    telemetria_ej = leer_csv(carpeta_ej / "telemetria_segmentos.csv")
    fases = Counter(f["fase_eval"] for f in telemetria_ej)
    assert fases == {"init": 1, "calentamiento": 1, "regimen_estable": 29}
    cfg_ej = json.load(open(carpeta_ej / "config_resuelta.json", encoding="utf-8"))
    rep = cfg_ej["reproduccion"]
    assert rep["calidad_inicial"] == 0 and rep["decision_inicial_controlador"] is False and rep["buffer_maximo_s"] == 60.0
    assert rep["max_segmentos_video"] == 30 and rep["espera_vaciado_buffer_s"] == 0.01 and rep["preroll_s"] == 0.0
    assert cfg_ej["motor_video"]["tiempo_min_cola"] == 0.1 and cfg_ej["reproduccion_red"]["max_bucles"] == 1
    siguiente = plan[num_ejemplo]  # la sesion num_ejemplo + 1 (indice num_ejemplo porque plan es 0-based)
    dur_ej = (inicios[siguiente["id_sesion"]] - inicios[ejemplo["id_sesion"]]).total_seconds()
    minutos_desde_inicio = (inicios[ejemplo["id_sesion"]] - primero).total_seconds() / 60

    # ---- Lo que se congela: huellas del kit, bundle, codigo --------------------------------
    lineas_codigo = [l.split(None, 1) for l in (KIT_VM / "hashes_codigo.sha256").read_text(encoding="utf-8").splitlines() if l.strip()]
    ficheros_codigo = [l[1].lstrip("*") for l in lineas_codigo]
    n_py = sum(1 for f in ficheros_codigo if f.endswith(".py"))
    assert len(ficheros_codigo) == 103 and n_py == 86
    for h, f in lineas_codigo:  # el codigo de TFG Material es el que se congelo
        assert sha256_fichero(CODIGO / f.lstrip("*")) == h, f
    huella_lista_codigo = sha256_fichero(KIT_VM / "hashes_codigo.sha256")
    assert huella_lista_codigo.startswith("a65e77e3") and huella_lista_codigo.endswith("22448")
    manifiesto = json.load(open(BUNDLE / "manifiesto.json", encoding="utf-8"))
    assert len(manifiesto["ficheros_requeridos"]) == 5 and manifiesto["tamano_ensemble"] == 5
    for nombre, info in manifiesto["ficheros"].items():
        assert sha256_fichero(BUNDLE / nombre) == info["sha256"], nombre
    assert sha256_fichero(BUNDLE / "manifiesto.json").startswith("7341c89c")
    ventanas_esperadas = [l for l in (KIT_VM / "ventanas_esperadas_final.txt").read_text(encoding="utf-8").splitlines() if l.strip()]
    assert len(ventanas_esperadas) == 77
    huella_ventanas = sha256_fichero(KIT_VM / "ventanas_esperadas_final.txt")
    assert huella_ventanas.startswith("a3445cc6")
    huella_cfg = sha256_fichero(CODIGO / "config" / "evaluacion.local.json")
    assert huella_cfg.startswith("700da716")
    n_pruebas = sum(len(re.findall(r"^\s*def test_", p.read_text(encoding="utf-8"), re.M)) for p in (CODIGO / "pruebas").glob("test_*.py"))
    assert n_pruebas == 18
    catalogo = json.load(open(TFG_MATERIAL / "02_corpus_red" / "catalogo_trazas.json", encoding="utf-8"))
    n_trazas = len(catalogo["trazas"])
    assert n_trazas == 6768
    pasos_guion = len(re.findall(r'echo "\d/9 ', (KIT_VM / "blindaje_vm.sh").read_text(encoding="utf-8")))
    assert pasos_guion == 9

    # ---- Contenido: Tears of Steel y los vistos -----------------------------------------------
    cv30 = {}
    primeros = {}
    for idv, nombre_desc in DESCRIPTOR.items():
        d = json.load(open(CODIGO / "perfiles_video" / "tamanos_segmentos" / "{0}.json".format(nombre_desc), encoding="utf-8"))
        assert d["representation_count"] == 6 and d["duracion_segmento_s"] == 4.0
        cvs, fr = [], []
        for r in d["representations"]:
            b = r["segment_bytes"][:30]
            cvs.append(statistics.pstdev(b) / statistics.mean(b))
            fr.append(sum(r["segment_bytes"][:2]) / (2 * r["cbr_nominal_bytes"]))
        cv30[idv] = (min(cvs), max(cvs))
        primeros[idv] = (min(fr), max(fr))
        if idv == ID_VIDEO_NUEVO:
            n_seg_tears, dur_tears = d["num_segmentos"], d["media_presentation_duration_s"]
            escalera = [r["bandwidth_bps"] // 1000 for r in d["representations"]]
    assert escalera == [300, 750, 1200, 1850, 2850, 4300] and n_seg_tears == 150 and dur_tears == 600.0
    mpd_tears = (CONTENIDO / "Tears_of_Steel_10min_30fps" / "4sec" / "Tears_of_Steel_10min_30fps_simple_4s.mpd").read_text(encoding="utf-8")
    assert 'frameRate="30"' in mpd_tears and 'width="1920" height="1080"' in mpd_tears
    gpac = re.search(r"GPAC version ([\d.]+)-", mpd_tears).group(1)  # 2.5 (version de desarrollo)
    cv_vistos = (min(cv30[v][0] for v in IDS_VIDEOS_VISTOS), max(cv30[v][1] for v in IDS_VIDEOS_VISTOS))
    assert 0.27 < cv30[ID_VIDEO_NUEVO][0] and cv30[ID_VIDEO_NUEVO][1] < 0.32 and cv_vistos[1] < 0.2
    assert primeros[ID_VIDEO_NUEVO][1] < 0.07 and primeros[ID_VIDEO_NUEVO][0] > 0.01

    # ---- Maquinas ---------------------------------------------------------------------------
    cliente, servidor, wsl = maquina("cliente"), maquina("servidor"), maquina("wsl")
    assert cliente["python"] == ejemplo_entorno["python"]["version"] == "3.8.10"
    assert ejemplo_entorno["versiones_paquetes"]["requests"] == "2.32.4"
    numpy_v = ejemplo_entorno["analisis_opcional"]["numpy"]["version"]
    mpl_v = ejemplo_entorno["analisis_opcional"]["matplotlib"]["version"]
    assert numpy_v == "1.24.4" and mpl_v == "3.7.5" and cliente["torch"].startswith("2.4.1")
    assert "7800" in wsl["gpu"] and wsl["torch"].startswith("2.9.1+rocm7.2.1")
    ram_total = ctypes.c_ulonglong(0)

    class MemStatus(ctypes.Structure):
        _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong), ("ullTotalPhys", ctypes.c_ulonglong),
                    ("ullAvailPhys", ctypes.c_ulonglong), ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                    ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong), ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]

    ms = MemStatus()
    ms.dwLength = ctypes.sizeof(MemStatus)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(ms))
    ram_win_gib = ms.ullTotalPhys / 2 ** 30
    win_release = platform.win32_ver()[0]
    py_win = os.popen("python --version").read().strip().replace("Python ", "")

    # ---- Documento ---------------------------------------------------------------------------
    b = Borrador(PLANTILLA)
    b.capitulo(6, "Evaluación")
    b.parrafo(
        "El capítulo 5 ha dejado el sistema implementado: el cliente, el ejecutor de experimentos, los cuatro "
        "controladores clásicos, el controlador propio con sus variantes y el entorno que entrena su modelo. "
        "Este capítulo lo evalúa con un único experimento, cuyo diseño se fijó y se congeló antes de ejecutar "
        "la primera sesión. El apartado 6.1 describe ese diseño: la pregunta, lo que se congela, la red, el "
        "contenido, los controladores y la ejecución. El 6.2 define las métricas y las cinco hipótesis "
        "prerregistradas con su método estadístico. El 6.3 comprueba la integridad de la ejecución y del "
        "paquete de evidencia. Los apartados 6.4 a 6.6 presentan los resultados: las hipótesis, los "
        "descriptivos por controlador y un análisis secundario exploratorio. El 6.7 interpreta lo que se "
        "puede afirmar y declara las limitaciones."
    )

    b.h2("6.1. Diseño del experimento final")
    b.parrafo(
        "El experimento responde a dos preguntas. La primera es si el controlador propio iguala en calidad "
        "de experiencia al MPC robusto canónico y lo mejora en seguridad, es decir, en paradas de la "
        "reproducción. La segunda es qué aporta cada pieza del controlador: la red de cuantiles frente a "
        "estimadores sin red y la agregación de riesgo frente a la mediana, con el mismo planificador. El "
        "principio de diseño es que todo lo que puede influir en la respuesta se fija antes de ejecutar y se "
        "comprueba después: las ventanas de red, los vídeos, los controladores con sus parámetros, el orden "
        "de ejecución, las métricas, las hipótesis y el análisis. La Figura 6.1 resume el diseño: tres "
        "factores (red, contenido y controladores) que se cruzan en {0} sesiones, lo que se congela antes y "
        "el paquete de evidencia que sale después. Las condiciones de red y el perfil del contenido se "
        "diseñaron en el apartado 4.7, la separación entre ejecución y evaluación en el 4.8 y el ejecutor "
        "con su preset en el 5.4; aquí se añade solo lo específico de este experimento.".format(miles(len(plan)))
    )
    b.figura(
        FIG,
        "Figura 6.1: Diseño del experimento final. A la izquierda, lo que se congela y se comprueba en la "
        "máquina virtual antes de lanzar; en el centro, los tres factores que se cruzan (red, contenido y "
        "controladores); a la derecha, las {0} sesiones y su ejecución. En amarillo, el contenido; en azul, "
        "el resultado del cruce.".format(miles(len(plan))),
        ancho_cm=16.0,
    )

    b.h3("6.1.1. Lo que se congela antes de ejecutar")
    b.parrafo(
        "El experimento se ejecuta una sola vez y con una sola versión de cada pieza. Antes de lanzarlo se "
        "calculó la huella SHA-256 del código entregado ({0} ficheros, {1} de ellos módulos de Python), de "
        "la configuración de la evaluación, de los {2} ficheros del paquete del modelo, de los cuantiles fijos "
        "de la variante sin red, del catálogo de trazas y del descriptor de tamaños del vídeo nuevo, y se "
        "guardó la lista de las {3} ventanas de red que debía producir el plan. Las hipótesis y su método "
        "estadístico están escritos en el código y el ejecutor los copia al protocolo del paquete al "
        "planificar, antes de la primera sesión, de modo que el análisis no se elige a la vista de los "
        "resultados. La Tabla 6.2 recoge cada pieza congelada y cómo se comprobó.".format(
            len(ficheros_codigo), n_py, len(manifiesto["ficheros_requeridos"]), len(ventanas_esperadas))
    )
    b.tabla(
        ["Pieza", "Contenido", "Comprobación antes de lanzar"],
        [
            ("Código entregado", "{0} ficheros ({1} módulos de Python)".format(len(ficheros_codigo), n_py),
             "huella SHA-256 de cada fichero y de la lista ({0}…); ningún fichero sobrante".format(huella_lista_codigo[:8])),
            ("Configuración de la evaluación", "8 controladores y sus parámetros, preset, semilla {0}, {1} grupos excluidos".format(
                config["experimento"]["semilla"], len(grupos)), "huella SHA-256 ({0}…)".format(huella_cfg[:8])),
            ("Modelo del controlador propio", "{0} ficheros: pesos, configuración del modelo, normalización, configuración del planificador y manifiesto".format(
                len(manifiesto["ficheros_requeridos"])), "huella de cada fichero contra el manifiesto; el controlador la vuelve a comprobar al cargarlo"),
            ("Cuantiles fijos", "cuantiles del error de la media armónica en el entrenamiento (variante sin red)", "huella SHA-256"),
            ("Catálogo de trazas", "{0} trazas con sus particiones y grupos de captura".format(miles(n_trazas)), "huella SHA-256"),
            ("Descriptor del vídeo nuevo", "tamaños reales de los {0} segmentos de Tears of Steel en los 6 niveles".format(n_seg_tears),
             "huella SHA-256 (incluido en el código)"),
            ("Ventanas esperadas", "{0} ventanas: {1} reales y {2} sintéticas".format(len(ventanas_esperadas), len(reales), len(sinteticas)),
             "plan en seco en la máquina virtual, cotejado con la lista ({0}…)".format(huella_ventanas[:8])),
            ("Hipótesis y análisis", "P1 a P5, margen de equivalencia, pruebas, bootstrap y corrección (versión {0})".format(VERSION_HIPOTESIS.replace("_", " ")),
             "copiadas al protocolo del paquete al planificar"),
            ("Código en funcionamiento", "{0} pruebas automáticas; los {1} controladores deciden con los 5 vídeos; el servidor sirve los 5 manifiestos".format(
                n_pruebas, len(controladores)), "ejecutadas en la máquina virtual antes de lanzar"),
        ],
        "Tabla 6.2: Lo que se congela antes de ejecutar el experimento y cómo se comprobó en la máquina "
        "virtual cliente. Las huellas se abrevian a sus ocho primeros caracteres hexadecimales. Los "
        "parámetros del preset están en la Tabla 5.5.",
        anchos_cm=[3.6, 6.4, 6.0],
    )
    b.parrafo(
        "El guion que lanzó el experimento hizo estas comprobaciones en {0} pasos, en orden, y se detenía al primer "
        "fallo. Se fijaron también dos reglas de validez antes de ejecutar: si una sesión no se completaba "
        "tras reanudar, su escenario saldría de los pares de ese controlador y se informaría; y ninguna "
        "sesión completada se repetiría ni se descartaría por su resultado. La alternativa, repetir sesiones "
        "con resultados anómalos, se descartó porque permite elegir el resultado. Ninguna de las dos reglas "
        "llegó a aplicarse (apartado 6.3).".format(pasos_guion)
    )

    b.h3("6.1.2. Red y contenido")
    b.parrafo(
        "La red de cada sesión es una ventana de {0} s de una traza real de la partición de evaluación del "
        "catálogo, reproducida con la emulación del apartado 4.7. Se toman todas las ventanas relevantes de "
        "esa partición según el criterio de Pensieve [mao2017pensieve], aplicado a la propia ventana y no a "
        "la traza entera: throughput medio menor de 6 Mbit/s y mínimo mayor de 0,2 Mbit/s, de modo que la "
        "escalera de 300 a 4300 kbit/s obligue a decidir. Quedan fuera los {1} grupos de captura utilizados "
        "durante el desarrollo ({2} reales y {3} sintéticos), así que ninguna ventana del experimento se había "
        "ejecutado antes con ningún controlador. El embudo completo, de {4} trazas de la partición a {5} "
        "ventanas, está en la Tabla 5.6. Las {5} ventanas proceden de dos conjuntos de datos: {6} de Oboe "
        "[akhtar2018oboe], trazas de sesiones de vídeo sobre redes de acceso fijas y móviles, y {7} de la "
        "campaña de banda ancha fija de la FCC [fccMeasuringBroadbandAmerica]. Sus medias van de {8} a {9} "
        "Mbit/s y el mínimo más bajo es {10} Mbit/s. El inicio de cada ventana se sortea con la semilla {11} "
        "(ecuación 5.2) y la traza da una sola vuelta de seguridad si la sesión agota los {0} s, cosa que no "
        "hace falta en condiciones normales porque una sesión de 30 segmentos consume como mucho unos 145 s "
        "de red.".format(
            coma(pe["duracion_ventana_red_s"], 0), len(grupos), len(grupos) - len(grupos_sint), len(grupos_sint), 873, len(reales),
            por_dataset["oboe"], por_dataset["fcc_measuring_broadband_america"], coma(min(medias) / 1000, 2),
            coma(max(medias) / 1000, 2), coma(min(minimos) / 1000, 2), config["experimento"]["semilla"])
    )
    b.parrafo(
        "Se eligieron ventanas de {0} s en lugar de las de 300 s de los presets de desarrollo por dos "
        "motivos: cubren con margen lo que consume una sesión y permiten que el filtro de relevancia se "
        "evalúe sobre el tramo de traza que de verdad se reproduce, y no sobre una media de cinco minutos "
        "que puede ocultar un tramo de baja capacidad. Las {1} ventanas sintéticas ({2}) sirven solo de "
        "diagnóstico: comprueban que los controladores se comportan como se espera en redes de forma "
        "conocida, se informan aparte y no entran en ningún contraste.".format(
            coma(pe["duracion_ventana_red_s"], 0), len(sinteticas),
            ", ".join({"synthetic_stable_low": "estable y baja", "synthetic_perfect_high": "perfecta y alta",
                       "synthetic_periodic_oscillation": "oscilación periódica"}[v["escenario_sintetico"]] for v in sinteticas))
    )
    b.parrafo(
        "El contenido cruza dos vídeos con cada ventana real. El primero es uno de los cuatro vídeos "
        "vistos por el modelo en el entrenamiento (Paseo de Almuñécar y Blender Sunflower, a 30 y 60 fps), "
        "asignado por rotación en el orden de las ventanas, de modo que cada uno aparece en {0} o {1} "
        "ventanas reales. El segundo es Tears of Steel, un cortometraje de la Blender Foundation publicado con "
        "licencia Creative Commons Atribución 3.0 [blenderTearsOfSteel], del que se tomaron los primeros {2} s a 30 fps y se "
        "empaquetaron con GPAC {3} con la misma escalera de seis niveles, segmentos de 4 s y resolución "
        "máxima de 1920 por 1080. Es contenido nuevo para el modelo: no intervino en el entrenamiento ni en "
        "ninguna decisión de diseño. Su interés está en que el predictor no ve el contenido pero el "
        "planificador sí usa su tabla de tamaños, y Tears of Steel tiene un perfil de tamaños mucho más "
        "variable que los vídeos vistos: en los 30 segmentos de una sesión, el coeficiente de variación del "
        "tamaño dentro de cada nivel está entre {4} y {5}, frente a valores entre {6} y {7} en los vistos, y "
        "sus dos primeros segmentos son casi negros, con entre un {8} y un {11} % del tamaño nominal según el nivel. Se descartó añadir más "
        "contenidos nuevos porque cada vídeo adicional por ventana suma {9} sesiones y unas {10} h de "
        "máquina. Las ventanas sintéticas llevan solo el vídeo visto que les toca en la rotación.".format(
            min(reales_por_visto.values()), max(reales_por_visto.values()),
            coma(dur_tears, 0), gpac, coma(cv30[ID_VIDEO_NUEVO][0], 2), coma(cv30[ID_VIDEO_NUEVO][1], 2),
            coma(cv_vistos[0], 2), coma(cv_vistos[1], 2), coma(100 * primeros[ID_VIDEO_NUEVO][0], 0),
            74 * 8, coma(74 * 8 * dur_media / 3600, 0), coma(100 * primeros[ID_VIDEO_NUEVO][1], 0))
    )

    b.h3("6.1.3. Controladores y sus parámetros")
    b.parrafo(
        "Corren los ocho controladores de la Tabla 6.1, cada uno con un único juego de parámetros, el mismo "
        "en las {0} sesiones. Los tres clásicos y el MPC robusto usan los valores por defecto de su "
        "implementación (Tabla 5.7) y reciben solo el identificador del vídeo, con el que el MPC robusto "
        "carga la tabla de tamaños reales. El controlador propio y sus tres variantes comparten α = {1}, el "
        "MPC robusto como respaldo, un límite de {2} ms para la inferencia y la comprobación de huellas del "
        "paquete del modelo al cargarlo; la variante de cuantiles fijos recibe además su fichero de "
        "cuantiles. El MPC básico existe en el registro pero no corre, porque su variante robusta es la "
        "referencia fuerte (apartado 5.5). Cada controlador interviene en las hipótesis que indica la "
        "tabla: el MPC robusto es el rival de la pregunta principal y las tres variantes aíslan cada pieza "
        "del propio; los tres clásicos sitúan el resultado en la escala habitual de la literatura y solo "
        "entran en el análisis descriptivo.".format(miles(len(plan)), coma(0.75, 2), coma(50, 0))
    )
    filas_ctrl = [
        ("Basado en tasa", "clásico, decide con el throughput estimado", "descriptivo"),
        ("BBA", "clásico, decide con la ocupación del buffer", "descriptivo"),
        ("BOLA", "clásico, optimización en línea sobre el buffer", "descriptivo"),
        ("MPC robusto", "referencia fuerte: control predictivo canónico con tamaños reales", "P1 (equivalencia en QoE) y P2 (paradas)"),
        ("Controlador propio", "cuantiles de la red, ensanchados, y agregación de riesgo con α = 0,75", "referencia de P1 a P5"),
        ("Propio, solo la mediana", "mismo planificador; un solo escenario, el cuantil 0,50 de la red", "P5 (aporte de la agregación de riesgo)"),
        ("Propio, cuantiles recientes", "mismo planificador; cuantiles de las cinco últimas descargas, sin red", "P3 (aporte de la red frente a una distribución local)"),
        ("Propio, cuantiles fijos", "mismo planificador; cuantiles fijos del error de la media armónica, sin red", "P4 (aporte de la red frente a una distribución fija)"),
    ]
    assert [NOMBRE_CTRL[c] for c in config["experimento"]["controladores"]] == [f[0] for f in filas_ctrl]
    b.tabla(
        ["Controlador", "Papel en el experimento", "Hipótesis en la que interviene"],
        filas_ctrl,
        "Tabla 6.1: Los ocho controladores del experimento final, su papel y la hipótesis prerregistrada en "
        "la que intervienen. Las cuatro versiones del propio comparten planificador, tamaños reales, α y "
        "respaldo (Tabla 5.11).",
        anchos_cm=[4.0, 6.6, 5.4],
    )

    b.h3("6.1.4. Ejecución y entorno")
    b.parrafo(
        "El plan cruza las {0} ventanas reales con sus dos vídeos y las {1} sintéticas con uno, y cada "
        "escenario con los ocho controladores: {0} × 2 × 8 + {1} × 1 × 8 = {2} sesiones (ecuación 5.3), "
        "con una sola repetición. Dentro de cada escenario el orden de los ocho controladores se sortea con "
        "una semilla derivada de la ventana y del vídeo, de modo que la posición en la serie no favorece a "
        "ninguno; los {3} escenarios dieron más de cien órdenes distintos. Las sesiones corren en serie, una "
        "detrás de otra, en la máquina virtual cliente, descargando del servidor DASH de la otra máquina "
        "virtual. Cada sesión reproduce 30 segmentos de 4 s: el primero se descarga en el nivel más bajo "
        "como calentamiento, sin consultar al controlador, y los 29 siguientes son las decisiones que se "
        "evalúan. El buffer máximo es de 60 s, el motor es el simulado con cola mínima de {4} s, y el paso "
        "de espera con el buffer lleno es de {5} s. El experimento arrancó el {6} a las {7} UTC y la última "
        "sesión terminó el {8} hacia las {9} UTC: {10} h en total, unos {11} s por sesión, sin huecos de "
        "más de cinco minutos.".format(
            len(reales), len(sinteticas), miles(len(plan)), len(ordenes), coma(0.1, 1), coma(0.01, 2),
            primero.strftime("%d/%m/%Y"), primero.strftime("%H:%M"), ultimo_inicio.strftime("%d/%m/%Y"),
            datetime.fromtimestamp(fin_estimado, tz=timezone.utc).strftime("%H:%M"), coma(horas, 1), coma(dur_media, 0))
    )
    b.parrafo(
        "El proyecto usa cuatro máquinas, resumidas en la Tabla 6.3. Las dos máquinas virtuales, cliente y "
        "servidor, corren en el mismo equipo físico bajo VirtualBox y se comunican por la red local; el "
        "cliente es la que ejecutó las {0} sesiones, con el mismo intérprete y las mismas versiones en "
        "todas ellas, registradas por cada sesión en su fichero de entorno. El modelo se entrenó en un "
        "subsistema Linux para Windows con una GPU de AMD y la variante ROCm de PyTorch; el cliente lo "
        "ejecuta en CPU con la variante estándar. El desarrollo, las pruebas rápidas y el análisis "
        "reproducido del apartado 6.3 se hicieron en el equipo anfitrión con Windows.".format(miles(len(plan)))
    )
    b.tabla(
        ["Máquina", "Sistema y hardware", "Software que intervino"],
        [
            ("Cliente (máquina virtual, ejecuta las sesiones)",
             "{0}, núcleo Linux {1}; {2} núcleos de {3} y {4} de memoria".format(cliente["so"], cliente["kernel"].split("-generic")[0],
                                                                               cliente["nucleos"], cliente["cpu"].replace("(R)", "").replace("(TM)", ""), cliente["ram"].replace("Gi", " GiB")),
             "Python {0}; requests {1}, NumPy {2}, PyTorch {3} en CPU; matplotlib {4} para el análisis".format(
                 cliente["python"], ejemplo_entorno["versiones_paquetes"]["requests"], numpy_v, cliente["torch"].split("+")[0], mpl_v)),
            ("Servidor (máquina virtual, sirve el contenido)",
             "{0}, núcleo Linux {1}; {2} núcleos y {3} de memoria".format(servidor["so"], servidor["kernel"].split("-generic")[0],
                                                                       servidor["nucleos"], servidor["ram"].replace("Gi", " GiB")),
             "Apache {0}; contenido empaquetado con GPAC {1}".format(servidor["apache"].split("-")[0], gpac)),
            ("Entrenamiento (WSL2)",
             "{0} sobre WSL2; {1} núcleos, {2} de memoria y GPU {3}".format(wsl["so"], wsl["nucleos"], wsl["ram"].replace("Gi", " GiB"),
                                                                           wsl["gpu"].replace("AMD ", "")),
             "Python {0}; PyTorch {1} con ROCm 7.2.1".format(wsl["python"], wsl["torch"].split("+")[0])),
            ("Desarrollo (anfitrión)",
             "Windows {0}; {1} de memoria; el mismo procesador".format(win_release, coma(ram_win_gib, 0) + " GiB"),
             "Python {0}; desarrollo, pruebas rápidas y reproducción del análisis".format(py_win)),
        ],
        "Tabla 6.3: Las cuatro máquinas del proyecto. Las versiones de la máquina cliente son las que "
        "registró cada una de las {0} sesiones en su fichero de entorno.".format(miles(len(plan))),
        anchos_cm=[3.8, 6.4, 5.8],
    )

    b.parrafo(
        "Un ejemplo concreto fija las ideas. La regla para elegirlo se declaró antes de mirar: la primera "
        "sesión del plan en la que corre el controlador propio. Es la sesión {0} del plan, en la ventana {1} "
        "(una traza de la FCC de acceso fijo con inicio en el segundo {2} de la traza, media de {3} Mbit/s y "
        "mínimo de {4} Mbit/s en la ventana) con el vídeo {5}; el sorteo colocó al propio en la posición {6} "
        "de los ocho, detrás de {7}. Su configuración resuelta es la de la Tabla 5.5: nivel inicial 0 sin "
        "decisión inicial, 30 segmentos, buffer de 60 s, ventana de {8} s con una vuelta. Empezó {9} min "
        "después de la primera sesión del experimento y la siguiente arrancó {10} s más tarde. Su carpeta "
        "contiene los seis artefactos del apartado 4.6 ({11}) y su telemetría tiene 31 filas: la "
        "inicialización, el segmento de calentamiento y las 29 decisiones evaluables. Las cifras de esa "
        "sesión y de las demás se presentan a partir del apartado 6.4; el 6.2 define antes qué se mide y "
        "qué se contrasta.".format(
            num_ejemplo, num_ventana_ej, coma(float(ventana_ej["inicio_ventana_s"]), 0),
            coma(float(ventana_ej["throughput_medio_ventana_kbps"]) / 1000, 2), coma(float(ventana_ej["throughput_min_ventana_kbps"]) / 1000, 2),
            NOMBRE_VIDEO[ejemplo["id_perfil_video"]], posicion_ej,
            ", ".join(EN_FRASE[c] for c in orden_ej[:posicion_ej - 1]),
            coma(pe["duracion_ventana_red_s"], 0), coma(minutos_desde_inicio, 1), coma(dur_ej, 0),
            ", ".join(NOMBRE_ARTEFACTO[f] for f in ficheros_ej))
    )

    b.guardar(SALIDA)
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("fechas:", primero.isoformat(), ultimo_inicio.isoformat(), "horas", round(horas, 2), "dur media", round(dur_media, 1))
    print("ejemplo:", ejemplo["id_sesion"], "ventana", num_ventana_ej, "posicion", posicion_ej, "dur", round(dur_ej, 1), "min desde inicio", round(minutos_desde_inicio, 1))
    print("ventanas por visto:", dict(ventanas_por_visto), "| cv tears", cv30[ID_VIDEO_NUEVO], "vistos", cv_vistos, "primeros", primeros[ID_VIDEO_NUEVO])
    print("maquinas:", cliente, servidor, wsl, win_release, round(ram_win_gib, 1), py_win)
    print("gpac", gpac, "| medias ventana", min(medias), max(medias), "min", min(minimos))


if __name__ == "__main__":
    main()

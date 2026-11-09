# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap5_4_ejecutor_configuracion.docx.

Reproduce la seleccion de ventanas del experimento final con el codigo del entregable
(core/evaluacion/seleccion.py) sobre el catalogo y el corpus de TFG Material, la compara con las
ventanas del paquete final y calcula el embudo de candidatas (Tabla 5.6). La Tabla 5.5 sale del
protocolo del paquete y de la configuracion real.

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap5_4.py
"""
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla, m_d, m_f, m_r, m_sub  # noqa: E402

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
CODIGO = TFG_MATERIAL / "01_codigo" / "ClienteDashTFG"
PAQUETE = TFG_MATERIAL / "04_evidencia_final" / "20261015_031741_final_blindaje"
CATALOGO = TFG_MATERIAL / "02_corpus_red" / "catalogo_trazas.json"
CORPUS = TFG_MATERIAL / "02_corpus_red" / "datasets_normalizados"
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
FIGURA = RAIZ_REPO / "docs" / "memoria" / "figuras" / "fig_5_2_ejecutor_evaluacion.png"
SALIDA = RAIZ_REPO / "docs" / "memoria" / "borradores_docx" / "cap5_4_ejecutor_configuracion.docx"


def coma(x, dec=0):
    return ("{0:.%df}" % dec).format(x).replace(".", ",")


def reproducir_seleccion():
    sys.path.insert(0, str(CODIGO))
    from core.evaluacion.configuracion import cargar_config_evaluacion  # noqa: E402
    from core.evaluacion.seleccion import (  # noqa: E402
        cargar_catalogo_trazas,
        es_traza_sintetica,
        grupos_fuga_excluidos,
        seleccionar_ventanas_trazas,
    )
    from scripts_eval import aplicar_overrides_preset  # type: ignore  # noqa: E402

    config = cargar_config_evaluacion(CODIGO / "config" / "evaluacion.local.json")
    config["rutas"]["ruta_catalogo"] = str(CATALOGO)
    config["rutas"]["reescrituras_rutas_trazas"] = [
        {"from": "/home/daniel/TFG/datasets_normalizados/", "to": str(CORPUS).replace("\\", "/") + "/"}
    ]
    preset = config["experimento"]["preset"]
    config = aplicar_overrides_preset(config, preset)
    catalogo = cargar_catalogo_trazas(CATALOGO)
    trazas = catalogo["trazas"]
    excluidos = grupos_fuga_excluidos(config)
    duracion = float(config["reproduccion_red"]["duracion_ventana_s"])

    reales_eval = [t for t in trazas if t.get("particion") == "eval" and not es_traza_sintetica(t)]
    con_duracion = [t for t in reales_eval if t.get("usable_en_eval", True) is not False and float(t["duracion_s"]) >= duracion]
    sin_excluidos = [t for t in con_duracion if str(t.get("grupo_fuga", "")) not in excluidos]
    ventanas = seleccionar_ventanas_trazas(catalogo, preset, config)
    reales = [v for v in ventanas if not v["sintetica"]]
    sinteticas = [v for v in ventanas if v["sintetica"]]

    # Comparacion con el paquete final.
    paquete = list(csv.DictReader(open(PAQUETE / "00_protocolo" / "ventanas_trazas.csv", encoding="utf-8")))
    clave = lambda d: (str(d["id_traza"]), float(d["inicio_ventana_s"]))  # noqa: E731
    iguales = sorted(clave(v) for v in ventanas) == sorted(clave(v) for v in paquete)
    assert iguales, "la seleccion reproducida no coincide con la del paquete final"
    assert len(reales) == 74 and len(sinteticas) == 3

    embudo = [
        ("Trazas reales de la partición de evaluación", len(reales_eval)),
        ("Con al menos 160 s de duración y aptas para evaluación", len(con_duracion)),
        ("Fuera de los 42 grupos de captura usados en el desarrollo", len(sin_excluidos)),
        ("Ventana relevante: media < 6 Mbit/s y mínimo > 0,2 Mbit/s", len(reales)),
    ]
    por_dataset = Counter(v["id_dataset"] for v in reales)
    primera = reales[0]
    return {
        "embudo": embudo,
        "por_dataset": por_dataset,
        "primera": primera,
        "excluidos": len(excluidos),
        "semilla": int(config["experimento"]["semilla"]),
        "config": config,
    }


def datos_protocolo():
    protocolo = json.load(open(PAQUETE / "00_protocolo" / "protocolo_validacion.json", encoding="utf-8"))
    plan = json.load(open(PAQUETE / "00_protocolo" / "plan_sesiones.json", encoding="utf-8"))["sesiones"]
    primera_cfg = json.load(
        open(next((PAQUETE / "00_protocolo" / "configs_cliente").glob("s00001_*")), encoding="utf-8")
    )
    return protocolo, plan, primera_cfg


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    # El ejecutor vive en scripts/3_evaluacion; se importa como modulo con un alias.
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "scripts_eval", CODIGO / "scripts" / "3_evaluacion" / "ejecutar_evaluacion.py"
    )
    sys.path.insert(0, str(CODIGO))
    modulo = importlib.util.module_from_spec(spec)
    sys.modules["scripts_eval"] = modulo
    spec.loader.exec_module(modulo)

    sel = reproducir_seleccion()
    protocolo, plan, cfg1 = datos_protocolo()
    pe = protocolo["preset_efectivo"]
    assert protocolo["num_sesiones"] == len(plan) == 1208
    assert pe["duracion_ventana_red_s"] == 160.0 and pe["max_segmentos_video"] == 30 and pe["tiempo_limite_s"] == 900.0
    assert cfg1["reproduccion"]["espera_vaciado_buffer_s"] == 0.01 and cfg1["reproduccion"]["preroll_s"] == 0.0
    assert cfg1["motor_video"]["tiempo_min_cola"] == 0.1 and cfg1["reproduccion_red"]["max_bucles"] == 1
    assert cfg1["reproduccion_red"]["politica_fin"] == "loop" and cfg1["reproduccion"]["calidad_inicial"] == 0
    assert cfg1["reproduccion"]["decision_inicial_controlador"] is False
    controladores = [c["alias"] for c in protocolo["controladores"]]
    assert len(controladores) == 8
    orden_1 = [s["alias_controlador"] for s in plan[:8]]
    orden_2 = [s["alias_controlador"] for s in plan[8:16]]
    assert orden_1 != orden_2
    videos = Counter(s["id_perfil_video"] for s in plan)
    assert videos["tears_10min_30fps_4s"] == 592
    p1 = sel["primera"]
    assert p1["id_ventana_traza"] == plan[0]["id_ventana_traza"]
    nombres = {
        "basado_en_tasa": "basado en tasa", "bba": "BBA", "bola": "BOLA", "mpc_robusto": "MPC robusto",
        "controlador_propio": "propio", "propio_mediana": "propio (solo mediana)",
        "propio_cuantiles_fijos": "propio (cuantiles fijos)", "propio_cuantiles_recientes": "propio (cuantiles recientes)",
    }

    b = Borrador(PLANTILLA)
    b.h2("5.4. Ejecutor de experimentos y configuración")
    b.parrafo(
        "El apartado 4.8 fijó el diseño del experimento: ventanas de red, escenarios, controladores, "
        "compuertas y análisis separados de la ejecución. Este apartado describe el software que lo lleva a la "
        "práctica: los dos niveles de configuración, la selección determinista de ventanas, la construcción "
        "del protocolo y del plan de sesiones, la ejecución sesión a sesión y el paquete de evidencia que "
        "resulta. La Figura 5.2 resume el flujo completo con los números del experimento final."
    )
    b.figura(
        FIGURA,
        "Figura 5.2: Flujo del ejecutor de experimentos, desde las entradas hasta el paquete de evidencia, "
        "con los valores del experimento final. En amarillo, el proceso independiente que ejecuta cada "
        "sesión; en rojo, la regla de tratamiento de las sesiones fallidas.",
        ancho_cm=16.0,
    )

    b.h3("5.4.1. Dos niveles de configuración")
    b.parrafo(
        "El sistema distingue la configuración de una sesión de la configuración de un experimento. La "
        "primera es la que consume el cliente (//main.py//): un fichero con ocho secciones (dirección del "
        "manifiesto, motor de reproducción, controlador y sus parámetros, reproducción, descargador, "
        "reproducción de trazas, salida y registro) que se convierte en un objeto inmutable de clases de "
        "datos. La conversión valida cada campo y cada regla cruzada con un mensaje que nombra la clave "
        "afectada: la ruta de la traza es obligatoria si la emulación está activada, la política de fin solo "
        "admite dos valores, el paso de espera debe ser positivo. Un error de configuración se detecta "
        "antes de tocar la red. La configuración resuelta, con los valores por defecto ya aplicados, se "
        "archiva en el directorio de cada sesión (apartado 4.6): queda documentado lo que se ejecutó."
    )
    b.parrafo(
        "La segunda es la configuración de la evaluación, que consume el ejecutor. Sus valores por defecto "
        "viven en el código y un fichero local los sobrescribe clave a clave. Sus secciones fijan las rutas "
        "(catálogo de trazas, raíz de salida, repositorio e intérprete, y reglas de reescritura para mover el "
        "corpus entre máquinas), el experimento (preset, semilla, motor, controladores, vídeos, inclusión de "
        "ventanas sintéticas, repeticiones y grupos de captura excluidos), los parámetros de reproducción y de "
        "emulación comunes a todas las sesiones, las opciones de ejecución (tiempo límite por sesión, "
        "reanudación, sesiones en paralelo) y los parámetros de cada controlador. El fichero de la evaluación "
        "final declara los ocho controladores, el preset, la semilla, las rutas, los parámetros del controlador "
        "propio y de sus tres variantes y la lista de {0} grupos de captura excluidos; lo demás son valores "
        "por defecto.".format(sel["excluidos"])
    )

    b.h3("5.4.2. El preset del experimento")
    b.parrafo(
        "Un preset es una especificación cerrada de las condiciones de un experimento: partición del "
        "catálogo, número de ventanas reales y sintéticas, filtro de relevancia, vídeos y forma de "
        "asignarlos, orden de los controladores, segmentos por sesión, duración y política de fin de la "
        "ventana de traza y tiempo límite por sesión. El preset sobrescribe los parámetros de reproducción y "
        "de emulación que le corresponden y su especificación efectiva se escribe en el protocolo del "
        "paquete. Existen presets reducidos para pruebas de humo y diagnóstico, que no habilitan ninguna "
        "comparación. La Tabla 5.5 recoge los parámetros que fijaron el preset y la configuración de la "
        "evaluación final, tal como quedaron escritos en el protocolo y en la configuración de cada sesión."
    )
    b.tabla(
        ["Parámetro", "Valor en la evaluación final", "Dónde se fija"],
        [
            ("Partición del catálogo", "evaluación", "preset"),
            ("Ventanas reales", "todas las relevantes de la partición (74)", "preset"),
            ("Filtro de relevancia", "media < 6 Mbit/s y mínimo > 0,2 Mbit/s en la ventana", "preset"),
            ("Ventanas sintéticas", "3, informadas aparte", "preset"),
            ("Duración de la ventana de traza", "160 s, con una vuelta de seguridad", "preset"),
            ("Vídeos por ventana real", "uno visto, en rotación entre cuatro, y el nuevo", "preset"),
            ("Orden de los controladores", "sorteado en cada escenario", "preset y semilla"),
            ("Segmentos por sesión", "30 (29 decisiones)", "preset"),
            ("Tiempo límite por sesión", "900 s", "preset"),
            ("Semilla", str(sel["semilla"]), "configuración"),
            ("Grupos de captura excluidos", str(sel["excluidos"]), "configuración"),
            ("Controladores", "8", "configuración"),
            ("Motor y cola mínima", "simulado, 0,1 s", "ejecutor"),
            ("Nivel inicial", "el más bajo, sin decisión inicial del controlador", "ejecutor"),
            ("Buffer y paso de espera", "60 s y 0,01 s", "ejecutor"),
            ("Ventana de arranque", "0 s", "ejecutor"),
            ("Sesiones", "1208, en serie", "resultado del plan"),
        ],
        "Tabla 5.5: Parámetros del experimento final y dónde se fija cada uno: en la especificación del "
        "preset, en el fichero de configuración de la evaluación o en la configuración que el ejecutor "
        "escribe para cada sesión.",
        anchos_cm=[5.2, 7.4, 3.4],
    )

    b.h3("5.4.3. Selección determinista de las ventanas de red")
    b.parrafo(
        "La selección parte del catálogo de trazas y aplica cuatro filtros en orden. Primero, la traza debe "
        "pertenecer a la partición de evaluación y estar marcada como apta. Segundo, debe durar al menos lo "
        "que la ventana. Tercero, su grupo de captura no puede estar en la lista de excluidos, que en la "
        "evaluación final contiene todos los grupos usados durante el desarrollo, de modo que ninguna ventana "
        "del experimento se había ejecutado antes. Cuarto, la ventana concreta que se va a reproducir debe "
        "ser relevante: su throughput medio tiene que quedar por debajo de 6 Mbit/s y su mínimo por encima de "
        "0,2 Mbit/s. Este último criterio es el que usa Pensieve para descartar las trazas en que elegir "
        "siempre la calidad máxima es trivial y aquellas en que la red no sostiene ningún nivel "
        "[mao2017pensieve]; aquí se calcula sobre la propia ventana, con las muestras ya compactadas y "
        "recortadas, igual que las reproduce la emulación."
    )
    b.parrafo(
        "El inicio de cada ventana dentro de su traza no se sortea con un generador de números aleatorios, "
        "sino con un resumen criptográfico de la semilla y del identificador de la traza. Si T es la duración "
        "de la traza en segundos, W la de la ventana y P el número de inicios posibles en pasos de 4 s, el "
        "inicio es:"
    )
    b.ecuacion(
        m_sub(m_r("t"), m_r("0")) + m_r("=", cursiva=False)
        + m_d(m_r("SHA256", cursiva=False) + m_d(m_r("semilla", cursiva=False) + m_r(",", cursiva=False) + m_r("id", cursiva=False))
              + m_r(" mod ", cursiva=False) + m_r("P"))
        + m_r("·", cursiva=False) + m_r("4", cursiva=False) + m_r(" s", cursiva=False)
        + m_r(",   ", cursiva=False) + m_r("P") + m_r("=", cursiva=False)
        + m_d(m_f(m_r("T") + m_r("−", cursiva=False) + m_r("W"), m_r("4", cursiva=False)), abre="⌊", cierra="⌋")
        + m_r("+", cursiva=False) + m_r("1", cursiva=False),
        "5.2",
    )
    b.parrafo(
        "donde SHA256(semilla, id) es el resumen de la cadena formada por la semilla y el identificador de la "
        "traza, interpretado como entero. Con la misma semilla y el mismo catálogo, dos ejecuciones producen "
        "exactamente las mismas ventanas, y cambiar la semilla las cambia todas. Las ventanas sintéticas se "
        "seleccionan aparte, con una semilla derivada, y quedan etiquetadas como diagnóstico."
    )
    e = sel["embudo"]
    pd = sel["por_dataset"]
    b.parrafo(
        "La Tabla 5.6 muestra el embudo de la evaluación final, reproducido para esta memoria con el mismo "
        "código y el mismo catálogo: de las {0} trazas reales de la partición de evaluación quedan {1} "
        "ventanas relevantes, {2} del conjunto Oboe y {3} del programa de medición de banda ancha de la "
        "FCC. La primera de ellas ilustra la ecuación (5.2): una traza de la FCC de {4} s de duración admite "
        "{5} inicios posibles y el resumen de la semilla con su identificador cae en el desplazamiento {6}, "
        "de modo que la ventana empieza en el segundo {7}; su throughput medio es de {8} Mbit/s y su mínimo "
        "de {9} Mbit/s.".format(
            e[0][1], e[3][1], pd["oboe"], pd["fcc_measuring_broadband_america"],
            coma(_duracion_traza(p1["id_traza"]), 1), _posibles(p1["id_traza"]),
            int(float(p1["inicio_ventana_s"]) // 4), coma(float(p1["inicio_ventana_s"]), 0),
            coma(float(p1["throughput_medio_ventana_kbps"]) / 1000.0, 2),
            coma(float(p1["throughput_min_ventana_kbps"]) / 1000.0, 2),
        )
    )
    b.tabla(
        ["Filtro aplicado en orden", "Trazas que quedan"],
        [(nombre, str(n)) for nombre, n in e],
        "Tabla 5.6: Embudo de selección de las ventanas reales de la evaluación final, reproducido con el "
        "código del entregable sobre el catálogo de trazas. Cada fila aplica un filtro más sobre la anterior.",
        anchos_cm=[11.5, 4.5],
        alineaciones=["l", "c"],
    )

    b.h3("5.4.4. Protocolo y plan de sesiones")
    b.parrafo(
        "Con las ventanas elegidas, el ejecutor construye el protocolo y el plan. El protocolo recoge la "
        "versión del esquema y de la fórmula de calidad, el preset efectivo, los perfiles de vídeo, los "
        "controladores, las ventanas con sus estadísticas, los grupos excluidos y la definición de las "
        "hipótesis que se contrastarán (referencia, rivales, métricas, margen de equivalencia y métodos), "
        "copiada del módulo de contrastes antes de ejecutar ninguna sesión. El plan asigna a cada ventana "
        "real un vídeo visto en el entrenamiento, en rotación entre los cuatro, y el contenido nuevo; a las "
        "sintéticas, solo el visto. En cada escenario los controladores se ejecutan en un orden sorteado con "
        "una semilla derivada de la semilla global, la ventana y el vídeo, para que la posición en la serie "
        "no favorezca a ninguno. El número de sesiones resulta de:"
    )
    b.ecuacion(
        m_r("S") + m_r("=", cursiva=False)
        + m_d(m_sub(m_r("V"), m_r("r")) + m_r("·", cursiva=False) + m_r("2", cursiva=False)
              + m_r("+", cursiva=False) + m_sub(m_r("V"), m_r("s")))
        + m_r("·", cursiva=False) + m_r("C") + m_r("·", cursiva=False) + m_r("R")
        + m_r("=", cursiva=False) + m_d(m_r("74", cursiva=False) + m_r("·", cursiva=False) + m_r("2", cursiva=False)
                                        + m_r("+", cursiva=False) + m_r("3", cursiva=False))
        + m_r("·", cursiva=False) + m_r("8", cursiva=False) + m_r("·", cursiva=False) + m_r("1", cursiva=False)
        + m_r("=", cursiva=False) + m_r("1208", cursiva=False),
        "5.3",
    )
    b.parrafo(
        "donde V~r~ y V~s~ son las ventanas reales y sintéticas, C los controladores y R las repeticiones. "
        "Protocolo y plan se escriben en JSON y en CSV antes de ejecutar nada, así que el experimento es "
        "inspeccionable antes de empezar. Cada sesión recibe un identificador legible que concatena su "
        "índice, el controlador, el vídeo, la ventana y la repetición; la primera del experimento final fue "
        "//{0}//, y en esa ventana el orden sorteado fue: {1}.".format(
            plan[0]["id_sesion"], ", ".join(nombres[a] for a in orden_1)
        )
    )

    b.h3("5.4.5. Ejecución, reanudación y paquete de evidencia")
    b.parrafo(
        "El ejecutor recorre el plan una sesión detrás de otra. Para cada una escribe la configuración "
        "completa del cliente en JSON: el manifiesto del vídeo, la traza con su inicio y duración de "
        "ventana y la política de bucle con una vuelta, el controlador con sus parámetros y el identificador "
        "del perfil de tamaños del vídeo, el motor simulado con cola mínima de 0,1 s, el arranque en el nivel "
        "más bajo sin decisión inicial, treinta segmentos, buffer de 60 s con paso de espera de 0,01 s y sin "
        "ventana de arranque. Después lanza el cliente como un proceso independiente, con un tiempo límite de "
        "900 s, y guarda toda su salida en un registro de comando con el instante de inicio, la orden exacta "
        "y el código de retorno. Ejecutar cada sesión en su propio proceso aísla los fallos, libera la "
        "memoria entre sesiones, garantiza que el estado del cliente nace limpio y permite repetir cualquier "
        "sesión aislada con su fichero de configuración y la misma orden. Todos los controladores reciben el "
        "identificador del vídeo de la sesión; el propio, sus variantes y el MPC robusto planifican con sus "
        "tamaños reales y los demás lo ignoran."
    )
    b.parrafo(
        "Antes de lanzar una sesión, el ejecutor comprueba si ya existe para ella una ejecución cuyo "
        "manifiesto esté en estado completado y, si es así, la omite. Un experimento interrumpido se reanuda "
        "sobre el mismo paquete sin repetir trabajo, y las sesiones incompletas o fallidas se repiten; ninguna "
        "sesión completada se repite ni se descarta por su resultado. Tras cada sesión se imprime una línea "
        "de progreso con las ejecutadas, fallidas y omitidas, el tiempo transcurrido y una estimación del "
        "restante. El ejecutor admite varias sesiones a la vez, pero la evaluación final se ejecutó en serie "
        "para que ninguna sesión compartiera la máquina con otra."
    )
    b.parrafo(
        "Al terminar, el ejecutor invoca el análisis del paquete (QoE por sesión, contrastes prerregistrados "
        "y compuertas) y su verificación (apartado 4.8), y devuelve un código de salida que solo es cero si "
        "ninguna sesión falló y la verificación se superó. Análisis y verificación existen también como "
        "herramientas independientes, para volver a analizar o verificar un paquete sin ejecutar nada; así "
        "se reprodujeron en otra máquina los resultados del capítulo 6. El paquete tiene cinco bloques: "
        "protocolo (con la configuración de cada sesión), ejecución (artefactos y registros de comando de cada "
        "sesión), resultados, gráficas e informe."
    )
    b.parrafo(
        "El ejecutor tiene además una interfaz gráfica mínima, construida con //tkinter//, con el preset, "
        "una casilla por controlador, los botones de ejecutar y detener y una barra de progreso que lee las "
        "líneas de progreso del ejecutor; muestra la orden exacta que va a lanzar y no hace nada que no pueda "
        "hacerse desde la línea de órdenes. La evaluación final se lanzó desde la línea de órdenes en segundo "
        "plano, mediante un guion de operación que antes comprobó las huellas del código, del modelo y del "
        "catálogo, ejecutó las pruebas automáticas y generó el plan en seco para cotejar las 77 ventanas "
        "esperadas; el capítulo 6 recoge ese procedimiento. El apartado 5.5 desciende a la implementación de "
        "los controladores clásicos."
    )

    b.guardar(SALIDA)
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("embudo:", e, "| por dataset:", dict(pd))


_CATALOGO_CACHE = {}


def _traza(id_traza):
    if not _CATALOGO_CACHE:
        for t in json.load(open(CATALOGO, encoding="utf-8"))["trazas"]:
            _CATALOGO_CACHE[t["id_traza"]] = t
    return _CATALOGO_CACHE[id_traza]


def _duracion_traza(id_traza):
    return float(_traza(id_traza)["duracion_s"])


def _posibles(id_traza):
    return int(max(0.0, _duracion_traza(id_traza) - 160.0) // 4.0) + 1


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Genera docs/memoria/borradores_docx/cap5_7_entorno_entrenamiento.docx.

Datos: plan_muestreo.json, resumen_dataset.json y auditoria_no_contaminacion.json del dataset
entregado (06_dataset_entrenamiento), configuracion del bundle (03_modelos), perfiles del codigo
(entrenamiento/*.py) y calibracion_validacion.json (producido por calibracion_validacion.py sobre
el material entregado).

Ejecutar desde la raiz del repo:  py -3.12 docs/memoria/apoyo/generar_cap5_7.py
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

RAIZ_REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from memoria_docx import Borrador, crear_plantilla, m_d, m_f, m_r, m_sub  # noqa: E402

TFG_MATERIAL = Path(r"C:\Users\danie\Documents\TFG Material")
CODIGO = TFG_MATERIAL / "01_codigo" / "ClienteDashTFG"
DATASET = TFG_MATERIAL / "06_dataset_entrenamiento" / "dataset_entrenamiento"
BUNDLE = TFG_MATERIAL / "03_modelos" / "modelo_propio" / "bundle"
CALIB = Path(__file__).resolve().parent / "calibracion_validacion.json"
PLANTILLA = RAIZ_REPO / "docs" / "memoria" / "plantilla" / "plantilla_memoria_ugr.docx"
FIG = RAIZ_REPO / "docs" / "memoria" / "figuras" / "fig_5_6_entorno_entrenamiento.png"
SALIDA = RAIZ_REPO / "docs" / "memoria" / "borradores_docx" / "cap5_7_entorno_entrenamiento.docx"
sys.path.insert(0, str(CODIGO))

NOMBRES_DATASET = {
    "fcc_measuring_broadband_america": "FCC (banda ancha fija)", "synthetic_controlled_network": "sintéticas controladas",
    "gavist5g": "GaVist5G", "norway_hsdpa_umass": "Norway HSDPA", "oboe": "Oboe", "ucc_4g_lte_beyond_throughput": "UCC 4G",
    "lumos5g": "Lumos5G", "ucc_5g_beyond_throughput": "UCC 5G", "puffer_stanford": "Puffer", "roma_4g_nbiot_5g_nsa": "Roma 4G/5G",
    "nyu_mets": "NYU-METS", "ghent_4g_lte": "Ghent 4G",
}


def coma(x, dec=2):
    return ("{0:.%df}" % dec).format(x).replace(".", ",")


def miles(n):
    # Separador de miles solo a partir de cinco cifras ("4096 ventanas", "111 630"), como la biblia.
    return "{0:,}".format(int(n)).replace(",", " ") if int(n) >= 10000 else str(int(n))


def m_sum(sub, sup, cuerpo):
    return ('<m:nary><m:naryPr><m:chr m:val="∑"/></m:naryPr><m:sub>{0}</m:sub><m:sup>{1}</m:sup><m:e>{2}</m:e></m:nary>'
            .format(sub, sup, cuerpo))


def main():
    if not PLANTILLA.exists():
        crear_plantilla(PLANTILLA)
    from entrenamiento.entrenamiento_modelo import PERFILES_ENTRENAMIENTO
    from entrenamiento.perfiles_dataset import PERFILES
    from entrenamiento.dataset_fiel import IDS_PERFILES_VIDEO

    plan = json.load(open(DATASET / "plan_muestreo.json", encoding="utf-8"))
    resumen = json.load(open(DATASET / "resumen_dataset.json", encoding="utf-8"))
    audit = json.load(open(DATASET / "auditoria_no_contaminacion.json", encoding="utf-8"))
    audit_m = json.load(open(DATASET / "auditoria_muestreo.json", encoding="utf-8"))
    cfg_mod = json.load(open(BUNDLE / "configuracion_modelo.json", encoding="utf-8"))
    cfg_plan = json.load(open(BUNDLE / "configuracion_planificador.json", encoding="utf-8"))
    cal = json.load(open(CALIB, encoding="utf-8"))
    pd = PERFILES["completo_v1"]
    pe = PERFILES_ENTRENAMIENTO["full"]
    pol = plan["politica_muestreo"]

    vt, vv = plan["ventanas_entrenamiento"], plan["ventanas_validacion"]
    assert len(vt) == 4096 and len(vv) == 935 and plan["segmentos_por_ventana"] == 30
    assert resumen["conteo_muestras"]["entrenamiento"] == 490500 and resumen["conteo_muestras"]["validacion"] == 111630
    assert audit["estado"] == "PASS" and audit["eval_usado"] is False and audit_m["comprobacion_fuga"]["estado"] == "PASS"
    assert set(x["particion_origen"] for x in vt) == {"train"} and set(x["particion_origen"] for x in vv) == {"test"}
    assert resumen["origen_tamanos_segmentos"] == "vbr_real_del_servidor" and len(IDS_PERFILES_VIDEO) == 8
    assert cfg_mod["tamano_ensemble"] == pe.tamano_ensemble == 5 and cfg_plan["alfa_riesgo"] == 0.75
    assert cal["num_muestras_validacion"] == 111630
    catalogo = json.load(open(TFG_MATERIAL / "02_corpus_red" / "catalogo_trazas.json", encoding="utf-8"))
    cat_tramos = Counter(
        ("lte_1" if m <= 1000 else "1_2" if m <= 2000 else "2_5" if m <= 5000 else "5_20" if m <= 20000 else "gt_20")
        for m in (float(t["throughput_medio_kbps"]) for t in catalogo["trazas"] if t["particion"] == "train")
    )
    por_ds_t = Counter(x["id_dataset"] for x in vt)
    por_ds_v = Counter(x["id_dataset"] for x in vv)
    sint_t = sum(1 for x in vt if x.get("sintetica"))
    sint_v = sum(1 for x in vv if x.get("sintetica"))
    trazas_t = len(set(x["id_traza"] for x in vt))
    trazas_v = len(set(x["id_traza"] for x in vv))
    grupos_t = len(set(x["grupo_fuga"] for x in vt))
    grupos_v = len(set(x["grupo_fuga"] for x in vv))
    tramo_t = Counter(x.get("tramo_throughput") for x in vt)
    omitidas = len(resumen["ventanas_omitidas"])
    cov = cal["cobertura_con_ensanchado"]["global"]
    cov_sin = cal["cobertura_sin_ensanchado"]["global"]
    cov_h = cal["cobertura_con_ensanchado"]["por_horizonte"]

    b = Borrador(PLANTILLA)
    b.h2("5.7. Entorno de entrenamiento fiel al medio")
    b.parrafo(
        "El predictor del apartado 5.6 aprende de datos que no proceden del experimento, sino de un entorno "
        "de entrenamiento construido para parecerse al cliente real en lo que importa: la red se reproduce "
        "con trazas reales y el contenido con los tamaños reales de los segmentos. Este apartado describe "
        "ese entorno en cuatro pasos (Figura 5.6): el muestreo de ventanas del catálogo de trazas, el "
        "simulador de sesiones que genera las muestras, el entrenamiento del conjunto de redes con su "
        "comprobación de calibración y la exportación del paquete que carga el cliente. Cierra con la "
        "calibración del modelo entregado sobre el conjunto de validación."
    )
    b.figura(
        FIG,
        "Figura 5.6: Entorno de entrenamiento del predictor: muestreo de ventanas, simulador de sesiones fiel "
        "al medio, entrenamiento del conjunto de redes y paquete del modelo. En amarillo, el contenido real; "
        "en azul, lo que sale de cada paso.",
        ancho_cm=16.0,
    )

    b.h3("5.7.1. Por qué un entorno fiel al medio")
    b.parrafo(
        "La primera versión del entorno de entrenamiento suponía segmentos de tasa constante: el tamaño de "
        "cada segmento era su tasa nominal por su duración. El cliente real descarga segmentos de tamaño "
        "variable (apartado 4.7), de modo que el tiempo de descarga, el buffer y el rebuffering que el modelo "
        "veía en el entrenamiento no eran los que vería después en el cliente. Esa diferencia se identificó "
        "como causa de que versiones anteriores del controlador no superaran a los clásicos (apartado 7.5), "
        "y motivó rehacer el entorno con una regla: la física de la sesión simulada tiene que ser la del "
        "cliente. La red la pone una traza real reproducida con el mismo modelo de red del apartado 5.2, y "
        "el contenido lo pone la tabla de tamaños reales de un vídeo, la misma que lee el planificador. Se "
        "descartó la alternativa de entrenar directamente con sesiones del cliente real: cada sesión de 30 "
        "segmentos dura dos minutos de reloj y el dataset exigía más de cinco mil ventanas, un coste de "
        "cientos de horas que el simulador reduce a minutos con la misma física."
    )

    b.h3("5.7.2. Muestreo de ventanas del catálogo")
    b.parrafo(
        "El catálogo de trazas (apartado 4.7) tiene tres particiones por grupo de captura. El dataset toma "
        "sus ventanas de entrenamiento de la partición de entrenamiento y las de validación de la partición "
        "de validación; la partición de evaluación está prohibida en el código del muestreo y la auditoría "
        "del dataset lo comprueba a posteriori sobre cada muestra. Cada ventana dura {0} s, que son 30 "
        "segmentos de 4 s, y de una traza se toman como mucho {1} ventanas consecutivas. La selección no es "
        "un sorteo uniforme: las ventanas candidatas se agrupan por conjunto de datos, semántica, tramo de "
        "throughput medio y variabilidad, y se recorren los grupos por turnos con un peso mayor para las "
        "redes lentas (de 5 para medias de hasta 1 Mbit/s a 1 para medias de más de 20 Mbit/s) y un punto "
        "más para las trazas variables o con cortes. Unas cuotas impiden que un origen domine: ningún "
        "conjunto de datos aporta más del {2} % de las ventanas, ninguna semántica más del {3} % y las "
        "sintéticas no pasan del {4} %. La semilla del sorteo es fija, así que el plan de muestreo se "
        "regenera idéntico.".format(
            coma(pol["duracion_ventana_s"], 0), pol["max_ventanas_por_traza"],
            coma(100 * pol["fraccion_max_dataset"], 0), coma(100 * pol["fraccion_max_semantica"], 0),
            coma(100 * pol["fraccion_max_sinteticas"], 0),
        )
    )
    b.parrafo(
        "El perfil usado pidió {0} ventanas de entrenamiento y {1} de validación; las cuotas dejaron {2} de "
        "validación. La Tabla 5.13 muestra su composición por origen. Las {3} ventanas de entrenamiento "
        "proceden de {4} trazas y {5} grupos de captura distintos; las de validación, de {6} trazas y {7} "
        "grupos, sin ningún grupo en común con las de entrenamiento. El sesgo hacia redes lentas es "
        "deliberado: en el entrenamiento, {8} ventanas tienen una media de hasta 2 Mbit/s y {9} más de "
        "20 Mbit/s, aunque estas últimas abundan mucho más en el catálogo ({10} de las {11} trazas de la partición de "
        "entrenamiento superan los 20 Mbit/s de media).".format(
            miles(pd.num_ventanas_train), miles(pd.num_ventanas_validacion), len(vv), miles(len(vt)), miles(trazas_t), miles(grupos_t),
            miles(trazas_v), grupos_v, miles(tramo_t["lte_1_mbps"] + tramo_t["1_2_mbps"]), miles(tramo_t["gt_20_mbps"]),
            miles(cat_tramos["gt_20"]), miles(sum(cat_tramos.values())),
        )
    )
    filas = []
    for ds, n in por_ds_t.most_common():
        filas.append((NOMBRES_DATASET.get(ds, ds), str(n), str(por_ds_v.get(ds, 0))))
    filas.append(("Total", str(len(vt)), str(len(vv))))
    b.tabla(
        ["Origen de las trazas", "Ventanas de entrenamiento", "Ventanas de validación"],
        filas,
        "Tabla 5.13: Ventanas del dataset de entrenamiento por conjunto de datos de origen. Las sintéticas "
        "({0} y {1}) quedan por debajo del {2} % que fija la cuota.".format(sint_t, sint_v, coma(100 * pol["fraccion_max_sinteticas"], 0)),
        anchos_cm=[7.0, 4.5, 4.5],
        alineaciones=["l", "c", "c"],
    )

    b.h3("5.7.3. Simulador de sesiones y construcción de las muestras")
    b.parrafo(
        "Cada ventana se convierte en sesiones simuladas de 30 segmentos. El simulador reproduce la ventana "
        "con el modelo de red del apartado 5.2, con política de bucle por si una sesión lenta consume la "
        "ventana, y avanza el buffer con la misma dinámica del planificador: el tiempo de descarga es el "
        "tamaño real del segmento dividido por el throughput que entrega la traza, el rebuffering es el "
        "exceso de ese tiempo sobre el buffer y el buffer se recarga con los 4 s del segmento hasta el tope "
        "de 60 s. El contenido se rota: a cada ventana se le asigna, por un resumen de su identificador, uno "
        "de los ocho descriptores de tamaños reales de 4 s (Paseo y Blender, de 10 y 1 min, a 30 y 60 fps), "
        "de modo que el modelo ve descargas con los patrones de tamaño de ambos contenidos. Los vídeos de "
        "1 min tienen 15 segmentos y se recorren cíclicamente para completar los 30."
    )
    b.parrafo(
        "Para que el dataset cubra estados variados sin aprender ninguna política concreta, cada ventana se "
        "recorre cuatro veces con cuatro reglas de decisión heurísticas: elegir el nivel que cabe bajo 0,85 "
        "veces la media armónica, subir un nivel sobre ese cuando el buffer pasa de 8 s, bajar al mínimo con "
        "el buffer por debajo de 4 s, y recorrer los niveles cíclicamente. La acción de la regla no es la "
        "etiqueta de nada: solo sirve para visitar estados con buffers altos y bajos, niveles distintos y "
        "descargas de tamaños distintos. En cada paso se guarda una muestra con lo que vería el controlador "
        "en el cliente (las mismas doce entradas de la Tabla 5.10, construidas con la misma función) y, como "
        "etiqueta, el futuro de la traza:"
    )
    b.ecuacion(
        m_sub(m_r("y"), m_r("k,h")) + m_r("=", cursiva=False)
        + "<m:func><m:fName>" + m_r("ln", cursiva=False) + "</m:fName><m:e>"
        + m_f(m_sub(m_r("B"), m_r("k+h")) + m_r("+", cursiva=False) + m_r("ε"),
              m_sub(m_r("C̄"), m_r("k")) + m_r("+", cursiva=False) + m_r("ε"))
        + "</m:e></m:func>"
        + m_r(",   ", cursiva=False) + m_r("h") + m_r("=", cursiva=False) + m_r("1, …, 5", cursiva=False),
        "5.13",
    )
    b.parrafo(
        "donde B~k+h~ es el ancho de banda medio que ofrece la traza, ponderado por tiempo, durante los 4 s "
        "del horizonte h contados desde el instante de red actual, C̄~k~ la media armónica de las descargas "
        "del historial en ese momento y ε = 1 bit/s evita el logaritmo de cero. La etiqueta es, por tanto, "
        "lo que la red daría en cada segmento futuro relativo a lo que el controlador acaba de medir, que es "
        "exactamente lo que el planificador necesita para simular las descargas de los cinco segmentos "
        "siguientes. El throughput futuro entra en la muestra solo como objetivo y la auditoría del dataset "
        "comprueba que no aparece entre las entradas."
    )
    b.parrafo(
        "El resultado son {0} muestras de entrenamiento y {1} de validación, un cuarto por cada regla de "
        "recorrido. {2} ventanas se omitieron porque su traza no entregaba caudal en ningún tramo. La "
        "auditoría de no contaminación comprueba que ninguna traza ni ningún grupo de captura aparece en los "
        "dos conjuntos, que ninguna muestra procede de la partición de evaluación y que los metadatos de la "
        "muestra (identidad de la traza, origen, partición, regla de recorrido) nunca son entradas del "
        "modelo. El dataset se entrega con su plan de muestreo y sus dos auditorías.".format(
            miles(resumen["conteo_muestras"]["entrenamiento"]), miles(resumen["conteo_muestras"]["validacion"]), omitidas
        )
    )

    b.h3("5.7.4. Entrenamiento del conjunto y calibración")
    b.parrafo(
        "El entrenamiento corre en la máquina con GPU del proyecto (WSL2 con ROCm y una Radeon RX 7800 XT, "
        "apartado 6.2) y produce los cinco miembros del conjunto uno tras otro, cada uno con su semilla. La "
        "normalización de las entradas se ajusta solo con las muestras de entrenamiento. Cada miembro se "
        "entrena {0} épocas con lotes de {1} muestras y el optimizador AdamW con tasa de aprendizaje "
        "{2}, decaimiento de pesos de 10⁻⁵ y recorte de la norma del gradiente a 5. La pérdida es la pinball "
        "de la ecuación (5.9) sobre los cuatro cuantiles y los cinco horizontes, más un término que "
        "penaliza los saltos entre horizontes consecutivos:".format(pe.epocas, miles(pe.tamano_lote), "3·10⁻⁴")
    )
    b.ecuacion(
        m_r("L") + m_r("=", cursiva=False)
        + m_f(m_r("1", cursiva=False), m_r("5·4", cursiva=False))
        + m_sum(m_r("h,τ"), "", m_sub(m_r("ρ"), m_r("τ")) + m_d(m_sub(m_r("y"), m_r("h")) + m_r("−", cursiva=False) + "<m:sSubSup><m:e>" + m_r("ŷ") + "</m:e><m:sub>" + m_r("h") + "</m:sub><m:sup>" + m_d(m_r("τ")) + "</m:sup></m:sSubSup>"))
        + m_r("+", cursiva=False) + m_r("λ") + m_r("·", cursiva=False)
        + m_f(m_r("1", cursiva=False), m_r("4·4", cursiva=False))
        + m_sum(m_r("h,τ"), "", m_d("<m:sSubSup><m:e>" + m_r("ŷ") + "</m:e><m:sub>" + m_r("h+1") + "</m:sub><m:sup>" + m_d(m_r("τ")) + "</m:sup></m:sSubSup>"
                                    + m_r("−", cursiva=False) + "<m:sSubSup><m:e>" + m_r("ŷ") + "</m:e><m:sub>" + m_r("h") + "</m:sub><m:sup>" + m_d(m_r("τ")) + "</m:sup></m:sSubSup>", abre="|", cierra="|")),
        "5.14",
    )
    b.parrafo(
        "donde λ = {0} es el peso de la suavidad temporal, que evita predicciones que oscilen de un horizonte "
        "al siguiente sin motivo. Tras cada época se evalúa la pinball sobre el conjunto de validación y se "
        "conserva el estado de la mejor época, que es la forma de parada temprana que emplea el entrenador. "
        "Al terminar, el conjunto se somete a una comprobación de calibración: la cobertura empírica de cada "
        "cuantil, es decir, la fracción de etiquetas de validación que quedan por debajo del cuantil predicho, "
        "debe acercarse a su nivel nominal con un error absoluto máximo de {1}; además, la pérdida de todos "
        "los miembros debe ser finita. El paquete del modelo (apartado 5.6) se exporta después con α = 0,75, "
        "los pesos de la QoE y el manifiesto de huellas.".format(coma(pe.peso_suavidad, 2), coma(0.08, 2))
    )
    b.parrafo(
        "La Tabla 5.14 recoge la calibración del modelo entregado, recalculada para esta memoria sobre las "
        "{0} muestras de validación con el mismo paquete que ejecutó el experimento. La cobertura global de "
        "los cuantiles 0,10, 0,25, 0,50 y 0,75 es {1}, {2}, {3} y {4}; el error máximo es {5}, dentro de "
        "la tolerancia. El sesgo es sistemático y va en el sentido prudente: los tres cuantiles inferiores "
        "cubren menos de lo nominal, de modo que el escenario pesimista del planificador es algo más "
        "pesimista de lo que anuncia, y el superior cubre más. El ensanchado epistémico apenas mueve la "
        "cobertura ({6} frente a {7} en el cuantil 0,10 sin él), porque en validación los cinco miembros "
        "discrepan poco; su pinball media es {8} y la de cada miembro por separado queda entre {9} y "
        "{10}.".format(
            miles(cal["num_muestras_validacion"]), coma(cov[0], 3), coma(cov[1], 3), coma(cov[2], 3), coma(cov[3], 3),
            coma(cal["error_abs_max_cobertura"], 3), coma(cov[0], 3), coma(cov_sin[0], 3), coma(cal["pinball_media"], 3),
            coma(min(cal["pinball_por_miembro"]), 3), coma(max(cal["pinball_por_miembro"]), 3),
        )
    )
    b.tabla(
        ["Horizonte", "Cuantil 0,10", "Cuantil 0,25", "Cuantil 0,50", "Cuantil 0,75"],
        [("segmento {0}".format(h + 1), coma(cov_h[h][0], 3), coma(cov_h[h][1], 3), coma(cov_h[h][2], 3), coma(cov_h[h][3], 3)) for h in range(5)]
        + [("global", coma(cov[0], 3), coma(cov[1], 3), coma(cov[2], 3), coma(cov[3], 3))],
        "Tabla 5.14: Cobertura empírica de los cuantiles predichos por el modelo entregado sobre el conjunto de "
        "validación ({0} muestras), por horizonte y global. El valor nominal es el del cuantil; un valor menor "
        "indica una predicción más pesimista que su nivel.".format(miles(cal["num_muestras_validacion"])),
        anchos_cm=[3.2, 3.2, 3.2, 3.2, 3.2],
        alineaciones=["l", "c", "c", "c", "c"],
    )
    b.parrafo(
        "La calibración por horizonte muestra el patrón esperable: el primer segmento es el más pesimista en "
        "la cola inferior ({0} en el cuantil 0,10) y el quinto el más ajustado ({1}), porque a mayor "
        "distancia la etiqueta se parece más a una media y la red dispersa menos sus cuantiles. La Tabla 5.15 "
        "reúne los parámetros del dataset y del entrenamiento.".format(coma(cov_h[0][0], 3), coma(cov_h[4][0], 3))
    )
    b.tabla(
        ["Bloque", "Parámetro", "Valor"],
        [
            ("Muestreo", "ventana", "{0} s, 30 segmentos de 4 s; hasta {1} por traza".format(coma(pol["duracion_ventana_s"], 0), pol["max_ventanas_por_traza"])),
            ("", "cuotas", "≤ {0} % por conjunto de datos, ≤ {1} % por semántica, ≤ {2} % sintéticas".format(
                coma(100 * pol["fraccion_max_dataset"], 0), coma(100 * pol["fraccion_max_semantica"], 0), coma(100 * pol["fraccion_max_sinteticas"], 0))),
            ("", "ventanas", "{0} de entrenamiento, {1} de validación".format(miles(len(vt)), len(vv))),
            ("Simulador", "contenido", "8 descriptores de tamaños reales, rotados por ventana; buffer máximo 60 s"),
            ("", "recorridos", "4 reglas heurísticas por ventana; {0} y {1} muestras".format(
                miles(resumen["conteo_muestras"]["entrenamiento"]), miles(resumen["conteo_muestras"]["validacion"]))),
            ("", "etiqueta", "ln del cociente entre el ancho de banda futuro de la traza y la media armónica, 5 horizontes"),
            ("Entrenamiento", "conjunto", "{0} GRU de {1} unidades, MLP {2}, dropout {3}".format(
                pe.tamano_ensemble, pe.tamano_oculto_gru, " y ".join(str(c) for c in pe.capas_ocultas_mlp), coma(pe.dropout, 1))),
            ("", "optimización", "AdamW, tasa 3·10⁻⁴, {0} épocas, lotes de {1}, mejor época por validación".format(pe.epocas, miles(pe.tamano_lote))),
            ("", "pérdida", "pinball (0,10; 0,25; 0,50; 0,75) + {0} · suavidad temporal".format(coma(pe.peso_suavidad, 2))),
            ("", "calibración", "error máximo de cobertura ≤ {0}; obtenido {1}".format(coma(0.08, 2), coma(cal["error_abs_max_cobertura"], 3))),
            ("Paquete", "exportación", "α = {0}, pesos 4,3 y 1,0, ensanchado {1}, SHA-256 de 4 ficheros".format(coma(cfg_plan["alfa_riesgo"], 2), coma(cfg_plan["ensanchado_cola"], 1))),
        ],
        "Tabla 5.15: Parámetros del dataset, del simulador y del entrenamiento del modelo entregado.",
        anchos_cm=[2.8, 3.0, 10.2],
    )
    b.parrafo(
        "Los límites del entorno son los de su fidelidad. El simulador reproduce la temporalidad de la red y "
        "los bytes reales, pero no la latencia de la petición ni el paso de espera del buffer, que en el "
        "cliente añaden decenas de milisegundos por segmento. Las etiquetas describen el ancho de banda que "
        "ofrece la traza, no el throughput que mediría una descarga concreta, que depende de su tamaño y de "
        "si la traza cambia durante ella. El conjunto de validación procede de la partición de validación del "
        "catálogo, con la que también se eligió α (apartado 5.6), así que la calibración de la Tabla 5.14 no "
        "es una medida sobre datos nunca vistos: esa medida es el experimento del capítulo 6."
    )
    # El cierre del capitulo (tres parrafos que recapitulan 5.1 a 5.7 y enlazan con el 6) va aparte:
    # docs/memoria/apoyo/generar_cap5_resumen.py -> borradores_docx/cap5_8_resumen_capitulo5.docx.

    b.guardar(SALIDA)
    print("palabras del cuerpo:", b.palabras_cuerpo)
    print("salida:", SALIDA)
    print("trazas/grupos:", trazas_t, grupos_t, trazas_v, grupos_v, "| tramos:", dict(tramo_t))


if __name__ == "__main__":
    main()

# Notas del 6.1 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap6_1_diseno_experimento.docx` (≈1890 palabras de cuerpo, 6 páginas:
apertura del capítulo 6 sin epígrafe + 6.1 con cuatro subapartados, Figura 6.1, Tablas 6.1 a 6.3, 3 citas, sin
ecuaciones). Generado por `docs/memoria/apoyo/generar_cap6_1.py`. Comprobador sin avisos (tras dos ajustes del
comprobador: el título de capítulo, estilo Heading 1, va sin número por diseño; «Ubuntu 20.04» no es un decimal).
Render con Word revisado página a página.

## Qué hace el script (todo por programa; falla si algo no cuadra)

- Lee `protocolo_validacion.json`, `plan_sesiones.csv` y `ventanas_trazas.csv` del paquete: 1208 sesiones, 1184
  reales (74 × 2 × 8) y 24 sintéticas (3 × 1 × 8); 74 ventanas = Oboe 56 + FCC 18; filtro «pensieve», orden
  «aleatorio_por_escenario», asignación «visto_rotado_mas_nuevo», partición eval; preset efectivo 160 s / 30
  segmentos / 900 s; hipótesis `hipotesis_blindaje_v1` con margen 0,15; fórmula `qoe_lineal_v1`.
- Comprueba el filtro de relevancia sobre las 74 ventanas (media máx 5,93 Mbit/s < 6; mínimo mín 0,26 > 0,2).
- Comprueba la rotación del vídeo visto: la ventana i (orden del plan) lleva `IDS_VIDEOS_VISTOS[i % 4]`; en las 74
  reales: Paseo 30 fps 19, Blender 30 fps 19, Paseo 60 fps 18, Blender 60 fps 18 (las 3 sintéticas suman 1 a
  Paseo 60, Blender 60 y Paseo 30 → 20/19/19/19 ventanas; 160/152/152/152 sesiones; Tears 592).
- Comprueba que los 151 escenarios tienen 8 sesiones y que el sorteo da más de cien órdenes distintos.
- Lee los 1208 `manifiesto_ejecucion.json`: una sola carpeta de ejecución por sesión (sin reanudaciones), estado
  completado; primera sesión 15/10/2026 01:17:43 UTC, última 16/10 18:34:39 UTC; duración media entre inicios 123,1
  s; fin estimado de la última = 18:36; total 41,32 h; ningún hueco > 5 min.
- Huellas: recalcula el SHA-256 de los 103 ficheros del código de TFG Material contra `kit_vm/hashes_codigo.sha256`
  (86 son `.py`; los otros 17: requirements, 2 configs, 9 descriptores de tamaños, 5 scripts .sh); la huella de la
  lista empieza por a65e77e3 y acaba en 22448 (= 06_PROTOCOLO §2); bundle: 5 ficheros, huellas = manifiesto;
  `manifiesto.json` 7341c89c…; configuración 700da716…; ventanas esperadas 77, a3445cc6…; 18 `def test_` en
  `pruebas/`; catálogo 6768 trazas; 9 pasos en `blindaje_vm.sh comprobar`.
- Contenido: de los descriptores de tamaños del código, CV de los 30 primeros segmentos por nivel: Tears 0,28–0,31,
  vistos 0,05–0,19; dos primeros segmentos de Tears entre 2 % (nivel 4300) y 6 % (nivel 300) del nominal. Del MPD
  de Tears en `05_contenido_dash`: 600 s, 30 fps, 1920×1080, GPAC 2.5-DEV, escalera 300…4300.
- Máquinas: `00_info_entorno/*.txt` (SO, núcleo, CPU, núcleos, RAM, Python, torch, GPU, Apache) + `entorno.json` de
  la sesión 1 (requests 2.32.4, numpy 1.24.4, matplotlib 3.7.5). Windows: medido en la propia máquina al generar
  (Windows 11, 31,8 GiB, Python 3.11.9).

## Fuente de cada número del texto

| Dato | Fuente |
|---|---|
| 1208, 1184, 24, 74, 56/18, 151 escenarios, 592 sesiones de Tears | `plan_sesiones.csv`, `ventanas_trazas.csv` |
| 103 ficheros / 86 .py, 5 ficheros del bundle, 77 ventanas, 18 pruebas, 9 pasos | kit de la VM + código de TFG Material (recalculado) |
| 42 grupos excluidos (39 reales + 3 sintéticos), semilla 606 | `config/evaluacion.local.json` = `protocolo_validacion.json` |
| 873 trazas de la partición | Tabla 5.6 (5.4; reproducido allí) |
| medias de ventana 0,35–5,93 Mbit/s, mínimo 0,26 | `ventanas_trazas.csv` (columnas `*_ventana_kbps`) |
| ~145 s de red por sesión | `06_PROTOCOLO_FINAL.md` §3 (30 segmentos × 4 s + arranque; con buffer de 60 s) |
| Tears: 600 s, 30 fps, 1920×1080, 150 segmentos, GPAC 2.5 | MPD y descriptor en TFG Material |
| CV 0,28–0,31 / 0,05–0,19; 2–6 % | descriptores (recalculado) |
| 592 sesiones y ~20 h por vídeo adicional | 74 × 8 × 123,1 s |
| α 0,75, respaldo MPC robusto, 50 ms, verificar_hashes | `config/evaluacion.local.json` |
| fechas y 41,3 h, 123 s/sesión | manifiestos (recalculado); 07_RESULTADO dice «01:17 → 18:34 UTC, 41,3 h» |
| ejemplo: sesión 8, ventana 1 (FCC, inicio 296 s, 5,04 / 4,38 Mbit/s), Paseo 30 fps, posición 8, 14,3 min, 122 s, 31 filas | plan, ventanas, manifiestos y telemetría de `s00008_…` |
| Tabla 6.3 | `info_entorno_*.txt`, `entorno.json`, máquina Windows |

## Regla del ejemplo real

Declarada antes de mirar: «la primera sesión del plan en la que corre el controlador propio». Salió la sesión 8
(ventana 1, FCC de alta capacidad, Paseo 30 fps, octavo del sorteo). No es un caso degenerado para lo que ilustra
(identificadores, configuración, artefactos); sus resultados NO se citan en el 6.1 (van del 6.4 en adelante).
Dato para la defensa: esa sesión dio QoE 3,97, 0 paradas, 29 inferencias de la red, 0 respaldos, inferencia media
1,2 ms (`sesiones.csv`); no se dice en el 6.1 a propósito.

## Citas

- `mao2017pensieve` p. 7 (§5.1 «Trace datasets»: «average throughput is less than 6 Mbps, and whose minimum
  throughput is above 0.2 Mbps»): verificada (ya en 5.4).
- `akhtar2018oboe` p. 7 («We use throughput traces from real user sessions collected over a three month period»)
  y p. 10 (FCC y HSDPA como conjuntos públicos): verificadas en el PDF. Se cita como origen de las trazas Oboe.
- `fccMeasuringBroadbandAmerica`: web oficial (misc), sin PDF; se cita como origen de los datos.
- `blenderTearsOfSteel` (alta 09/11 con permiso de Daniel): páginas index y Sharing de mango.blender.org guardadas
  en `biblioteca_final/11_estadistica/`; la página Sharing dice «licensed under the Creative Commons Attribution 3.0
  license». La cita va en la frase del cortometraje. Origen del
  fichero usado: `https://download.blender.org/demo/movies/ToS/tears_of_steel_1080p.mov.zip` (583 774 281 bytes,
  `kit_servidor/preparar_video_nuevo.sh`).

## Decisiones de redacción

- La Tabla 6.2 NO repite los parámetros del preset (ya en la Tabla 5.5): recoge lo que se congela y cómo se
  comprobó. El prompt pedía «parámetros del preset»; se cambia por este motivo y se remite a la 5.5.
- Tabla 6.3 (máquinas) añadida porque el 5.1 de Daniel remite «la topología completa de máquinas» al capítulo 6 y
  el cap 4 no la describe (comprobado por programa sobre su Word: 0 menciones a VirtualBox, Apache o WSL).
- La ecuación de la QoE NO va en el 6.1 sino en el 6.2 (el cap 4 tampoco la escribe: 0 apariciones de «4,3»).
- «160 s en lugar de 300 s»: se justifica por cobertura de la sesión y por evaluar el filtro sobre el tramo que se
  reproduce; NO se citan las cifras de desarrollo (cuántas ventanas quedaban con 300 s).
- Los tramos de dificultad internos (`alta_capacidad`…) no se nombran; se da el rango de medias.
- «Una repetición» se justifica en 6.3 (determinismo auditado), no aquí.

## Preguntas probables del tribunal

1. **¿Por qué solo Oboe y FCC?** Son los conjuntos que, en la partición de evaluación y fuera de los 42 grupos del
   desarrollo, tienen ventanas de 160 s con media < 6 Mbit/s y mínimo > 0,2 Mbit/s; los conjuntos 4G/5G modernos
   quedan casi siempre por encima de 6 Mbit/s. Limitación declarada en 6.7.
2. **¿El filtro no sesga hacia redes lentas?** Sí, a propósito: donde la escalera obliga a decidir. Es el criterio
   de Pensieve, aplicado a la ventana.
3. **¿Por qué una sola repetición?** El cliente es determinista en sus decisiones dada la realimentación (auditoría
   35 032/35 032 en 6.3); la variabilidad temporal de la VM es pequeña (fidelidad del simulador, 6.3).
4. **¿Por qué el orden sorteado?** Para que la posición en la serie (y cualquier deriva del servidor o de la VM) no
   favorezca a un controlador.
5. **¿Qué pasa si el modelo falla en una sesión?** Respaldo MPC robusto; en el experimento no ocurrió (0 respaldos,
   6.3).
6. **¿Tears of Steel es «nuevo» de verdad?** No intervino en el entrenamiento ni en ninguna decisión de diseño; el
   descriptor se extrajo el 14/10 y se congeló con el código.

## Avisos (no van a la memoria)

- `benchmark_autorizado = false` en el paquete (lista de presets antigua); no se menciona.
- El `info_entorno_cliente.txt` lista el `pip freeze` del Python 3.10 del sistema (requests 2.22.0, numpy 2.2.6):
  las versiones que valen son las de `entorno.json` (Python 3.8.10, requests 2.32.4, numpy 1.24.4).
- La Tabla 6.3 da el fin de la última sesión como estimación (inicio + duración media): 18:36 UTC; 07_RESULTADO
  da el inicio de la última (18:34).

## Qué se puede recortar

El párrafo de «160 s frente a 300 s» (fundirlo en una frase del anterior) y la mitad del párrafo de las máquinas si
la Tabla 6.3 basta. Mantener la Figura 6.1, las tres tablas y el ejemplo.

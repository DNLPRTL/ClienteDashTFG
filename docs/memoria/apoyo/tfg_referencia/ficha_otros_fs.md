# Ficha de formato y estilo — TFG_FS.pdf (Francisco Sánchez Martínez, ETSIIT-UGR, septiembre de 2025)

Ficha elaborada a partir de la lectura íntegra del texto extraído con `pdftotext` (flujo y maquetación) del fichero `docs/memoria/DE OTROS TUTORES PERO RECIENTES DE MI FACULTAD/TFG_FS.pdf` (155 páginas físicas, 36 621 palabras). Las páginas se indican entre paréntesis y corresponden a la **página física del PDF**; cuando la numeración impresa difiere se avisa. Las citas literales van entre comillas angulares « ». Todo lo que no se puede saber desde el texto (negritas, cursivas, colores, tipografía) se marca como «no determinable desde el texto», y las inferencias se señalan como tales con su evidencia.

> Peso de este patrón: ALTO. Es un TFG de otro tutor (Joaquín T. Valderrama, TSTC), defendido en septiembre de 2025 en el mismo grado (Ingeniería de Tecnologías de Telecomunicación) y la misma escuela. Refleja la práctica más reciente de la ETSIIT (declaración de uso de IA generativa según las recomendaciones UGR 2024, gestión de datos, comité de ética, capítulo de «Resultados de aprendizaje»).

---

## A. Identificación

| Campo | Valor (literal cuando procede) | Página |
|---|---|---|
| Título completo | «Exploración neurofisiológica de mecanismos neuronales de adaptación al ruido» | 1, 3, 4 |
| Título en inglés | «Neurophysiological Exploration of Neural Mechanisms of Adaptation to Noise» | 6 |
| Autor | «Autor / Francisco Sánchez Martínez» (la portada usa la etiqueta «Autor») | 1 |
| Tutor | «Director / Joaquín Tomás Valderrama Valenzuela» (la portada usa la etiqueta **«Director»**, no «Tutor»). En el informe: «D. Joaquín Tomás Valderrama Valenzuela, profesor del Área de Teoría de la señal y Comunicaciones del Departamento Teoría de la Señal, Telemática y Comunicaciones de la Universidad de Granada» | 1, 9 |
| Departamento | Teoría de la Señal, Telemática y Comunicaciones (TSTC). **No aparece en la portada**; solo en el informe del director (9) y en los agradecimientos (11) | 9, 11 |
| Titulación literal | «TRABAJO FIN DE GRADO» (línea 1) / «INGENIERÍA DE TECNOLOGÍAS DE TELECOMUNICACIÓN» (línea 2, mayúsculas) | 1 |
| Centro literal | «Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación» seguida de una línea que solo contiene «—» (raya; probablemente hueco de una línea vacía de plantilla o logotipo; inferencia) | 1 |
| Universidad | «Universidad de Granada» (solo en texto corrido del informe y agradecimientos; en portada no hay texto «Universidad de Granada», lo que sugiere que el escudo es imagen; inferencia) | 9 |
| Fecha / curso | «Granada, septiembre de 2025» (portada). Informe firmado «en Granada a 5 de septiembre de 2025 .» | 1, 9 |
| Número de páginas | 155 físicas (154 saltos de página). Última página impresa: 154 (la física 153). | — |
| Herramienta de maquetación | **LaTeX** (certeza alta). Evidencia: (a) el propio autor lo declara en 6.2: «Uso de LaTeX: la elaboración de un documento complejo, como esta memoria de TFG, me ha permitido desarrollar habilidades en el manejo de esta herramienta.» (105); (b) «Capítulo 1» en una línea y el título en otra (25); (c) numeración de epígrafes con punto final «1.1.», «2.2.3.1.» (estilo babel-spanish); (d) índices con puntos conductores; (e) pies «Figura 2.3:» y «Tabla 2.1:» con dos puntos; (f) ecuaciones numeradas a la derecha «(2.1)»; (g) bibliografía autor-año estilo `apalike`/natbib con «and»; (h) listados con «Listing D.1:» y numeración de líneas (paquete `listings`, con los acentos de los comentarios rotos, típico de `listings` sin `extendedchars`); (i) cabeceras alternas par/impar y páginas en blanco antes de cada capítulo (clase `book`, dos caras); (j) partición silábica («adap-/tación», «provo-/can», «po-/tenciales»); (k) porcentaje con espacio «50 %» (171 casos) y comillas tipográficas “ ”. | 25, 31, 105, 131 |

---

## B. Estructura completa en orden (páginas físicas)

| Bloque | Páginas | Observaciones |
|---|---|---|
| Portada | 1 | Ver literal en L |
| Verso de portada | 2 | Solo contiene el carácter «3» (número de página impreso suelto; defecto de numeración de preliminares) |
| Segunda portada | 3 | Título, «Autor», nombre, «Director», nombre. Sin escuela ni fecha |
| Resumen + palabras clave (español) | 4–5 | Orden: título, autor, **«Palabras clave:» antes del «Resumen»** |
| Abstract + keywords (inglés) | 6–7 | Mismo orden: «Keywords:» antes de «Abstract» |
| Página en blanco | 8 | |
| Informe / autorización del director | 9 | Único documento oficial. Ver literal abajo |
| Página en blanco | 10 | |
| Dedicatoria | — | **No hay** (la familia se menciona dentro de los agradecimientos) |
| Agradecimientos | 11–12 | 517 palabras, 7 párrafos |
| Índice general | 13–15 | Cabecera «ÍNDICE GENERAL» en mayúsculas en páginas interiores |
| Página en blanco | 16 | |
| Índice de figuras | 17–21 | 79 entradas |
| Página en blanco | 22 | |
| Índice de tablas | 23 | 9 entradas |
| Página en blanco | 24 | |
| Glosario / lista de acrónimos | — | **No hay**. Las siglas se definen al primer uso (ver J) |
| Capítulo 1. Introducción | 25–30 | |
| Capítulo 2. Estado del arte | 31–68 | |
| Capítulo 3. Medidas psicoacústicas | 69–77 | p. 78 en blanco |
| Capítulo 4. Medidas neurofisiológicas | 79–98 | |
| Capítulo 5. Discusión científica | 99–101 | p. 102 en blanco |
| Capítulo 6. Resultados de aprendizaje | 103–105 | p. 106 en blanco |
| Bibliografía | 107–110 | 39 entradas (el índice la sitúa en la 105: error de índice) |
| Apéndice A. Aprobación del comité de ética | 111 | **Solo portadilla**. La página impresa 112 no existe en el PDF (la física 112 ya lleva impreso «113»): el documento de aprobación no está en el fichero (eliminado o nunca incluido; inferencia a partir del salto de numeración) |
| Apéndice B. Poster IERASG | 112–113 | Portadilla + póster científico a página completa (en inglés) |
| Apéndice C. Respuestas ABR y Full-Range | 114–129 | Portadilla + 26 figuras (dos por página) |
| Apéndice D. Códigos de programación | 130–153 | Portadilla + 14 listados MATLAB |
| Páginas en blanco finales | 154–155 | |

**Faltan** respecto a un TFG «completo» de la escuela: declaración de originalidad / autorización del alumno para la biblioteca, dedicatoria, glosario de acrónimos, lista de listados, capítulo de planificación/presupuesto, apartado de requisitos. **Sobran/son singulares**: declaración de uso de IA generativa (1.5), gestión de datos (1.4), aprobación del comité de ética (1.6 + apéndice A), publicaciones asociadas (1.7), capítulo «Resultados de aprendizaje» (6).

### B.1 Informe/autorización del director — texto literal (p. 9)

> «D. Joaquín Tomás Valderrama Valenzuela, profesor del Área de Teoría de la señal y Comunicaciones del Departamento Teoría de la Señal, Telemática y Comunicaciones de la Universidad de Granada.
>
> Informa:
>
> Que el presente trabajo, titulado Exploración neurofisiológica de mecanismos neuronales de adaptación al ruido, ha sido realizado bajo su supervisión por Francisco Sánchez Martínez, y autorizo la defensa de dicho trabajo ante el tribunal que corresponda.
>
> Y para que conste, expide y firma el presente informe en Granada a 5 de septiembre de 2025 .
>
> El director:
>
> Joaquín Tomás Valderrama Valenzuela»

Notas: no hay DNI de nadie; el título va, por el flujo del texto, en el mismo párrafo (probablemente en cursiva o negrita; no determinable); hay un espacio sobrante antes del punto final de la fecha («2025 .»); no existe declaración firmada por el alumno.

### B.2 Resumen y palabras clave — texto literal (pp. 4–5)

> «Exploración neurofisiológica de mecanismos neuronales de adaptación al ruido
>
> Francisco Sánchez Martínez
>
> Palabras clave: adaptación neuronal al ruido, SRT-50, medidas psicoacústicas, potenciales evocados auditivos, ABR, MLR, CAEP, EEG, neurofisiología, comprensión en ruido.
>
> Resumen
>
> Este trabajo de fin de grado propone y evalúa un marco experimental para caracterizar de forma objetiva la adaptación neuronal al ruido mediante medidas psicoacústicas y neurofisiológicas no invasivas.
>
> En el estudio psicoacústico se diseñó un test que estimó el umbral de audición correspondiente al 50 % de inteligibilidad (SRT-50, por sus siglas en inglés: speech reception threshold) con tres escenarios en los que difiere el retardo entre el inicio del ruido y la palabra (50, 800 y 1600 ms). Se emplearon palabras vocodificadas y ruido con espectro similar a la voz (SSN, por sus siglas en inglés: speech-shaped noise), ambos calibrados acústicamente. Se analizaron estadísticamente los valores SRT-50 obtenidos en las diferentes condiciones experimentales. Los resultados mostraron una mejora significativa de la inteligibilidad cuando el estímulo verbal se presenta con retraso respecto al inicio del enmascarador, evidenciando adaptación al ruido a nivel perceptivo.
>
> En el estudio neurofisiológico se registraron señales de electroencefalografía (EEG, por sus siglas en inglés: electroencephalography) para la estimación de diferentes potenciales evocados auditivos (AEPs, por sus siglas en inglés: auditory evoked potentials) en dos escenarios con condiciones análogas a las del test psicoacústico: presentación temprana del estímulo (50 ms) y tardía (800 ms) respecto al inicio del ruido. El estímulo acústico consistió en ráfagas de clics presentadas con una relación señal-ruido (SNR, por sus siglas en inglés: signal-to-noise ratio) de 5 dB. La señal EEG registrada se procesó siguiendo dos metodologías: (1) estimación de los potenciales evocados auditivos del tronco cerebral (ABR, por sus siglas en inglés: auditory brainstem response); y (2) estimación del potencial evocado auditivo de la vía completa (full-range AEP), el cual permite representar de manera integral todas las componentes de la vía auditiva, incluyendo componentes ABR, componentes de latencia media (MLR, por sus siglas en inglés: middle-latency response) y componentes corticales (CAEP, por sus siglas en inglés: cortical auditory evoked potentials). El procesado de la señal EEG incluyó técnicas de mejora de la calidad tales como filtrado digital, rechazo de trama y atenuación del artefacto del pestañeo. Para la estimación de las respuestas ABR y full-range AEP se utilizaron técnicas basadas en deconvolución (las cuales permiten estimar respuestas neurofisiológicas que solapan entre sí, proporcionando un alto grado de flexibilidad en el diseño experimental) y en filtrado dependiente de la latencia en el caso del full-range AEP, permitiendo una representación adecuada de todas las componentes de la vía auditiva en el eje logarítmico de la frecuencia. A nivel de grupo, no se observaron cambios significativos y robustos en la morfología de las respuestas entre condiciones, lo que indica que el estímulo acústico empleado posiblemente no sea adecuado para evidenciar la adaptación mediante medidas neurofisiológicas.
>
> En conjunto, el trabajo realizado confirma la evidencia conductual de adaptación al ruido y plantea nuevas líneas de investigación orientadas a su estudio mediante medidas neurofisiológicas.»

Estructura del resumen (≈430 palabras, 4 párrafos): (1) una frase de encuadre («propone y evalúa un marco experimental...»), (2) estudio 1 con método + resultado, (3) estudio 2 con método + resultado (negativo, dicho sin rodeos), (4) frase de cierre con la aportación y las líneas futuras. Define cada sigla al primer uso también dentro del resumen.

### B.3 Abstract y keywords — texto literal (pp. 6–7)

> «Neurophysiological Exploration of Neural Mechanisms of Adaptation to Noise
>
> Francisco Sánchez Martínez
>
> Keywords: neural adaptation to noise, SRT-50, psychoacoustic measures, auditory evoked potentials, ABR, MLR, CAEP, EEG, neurophysiology, speech-in-noise perception.
>
> Abstract
>
> This bachelor thesis proposes and evaluates an experimental framework to objectively characterize neural adaptation to noise using non-invasive psychoacoustic and neurophysiological measurements.
>
> In the psychoacoustic study, a test was designed to estimate the speech reception threshold corresponding to 50 % intelligibility (SRT-50) under three scenarios that differed in the delay between noise onset and word presentation (50, 800, and 1600 ms). Vocoded words and speech-shaped noise (SSN), both acoustically calibrated, were employed. The SRT-50 values obtained across the different experimental conditions were analyzed statistically. The results revealed a significant improvement in intelligibility when the speech stimulus was presented with a delay relative to the onset of the masker, providing evidence of perceptual-level adaptation to noise.
>
> In the neurophysiological study, electroencephalography (EEG) signals were recorded to estimate different auditory evoked potentials (AEPs) under two scenarios analogous to the psychoacoustic test: early stimulus presentation (50 ms) and late presentation (800 ms) relative to noise onset. The acoustic stimulus consisted of click trains presented at a signal-to-noise ratio (SNR) of +5 dB. The EEG recordings were processed using two approaches: (1) estimation of auditory brainstem responses (ABR); and (2) estimation of full-range auditory evoked potentials (AEPs), which provide an integrated representation of the entire auditory pathway, including ABR, middle-latency responses (MLR), and cortical auditory evoked potentials (CAEP). EEG preprocessing included quality-enhancement techniques such as digital filtering, epoch rejection, and blink-artifact suppression. For the estimation of ABR and full-range AEPs, deconvolution-based methods were applied—allowing the separation of overlapping neurophysiological responses and providing high flexibility in experimental design—as well as latency-dependent filtering in the case of full-range AEPs, enabling an appropriate representation of all auditory pathway components along the logarithmic frequency axis. At the group level, no significant or consistent morphological differences were observed between conditions, suggesting that the acoustic stimulus employed may not have been optimal for demonstrating adaptation through neurophysiological measures.
>
> Overall, the findings confirm behavioral evidence of noise adaptation and point to new lines of research aimed at studying this phenomenon through neurophysiological approaches.»

### B.4 Agradecimientos (pp. 11–12) — rasgos

Título «Agradecimientos» sin numerar. Primera persona del singular. Orden: tutor → colaboradores externos (Universidad de Salamanca) → cesión de equipos (empresa) → departamento y centro (TSTC, CITIC, cámara anecoica) → financiación («beca Ramón y Cajal (Ref: RYC2022-037875-I) de la Agencia Estatal de Investigación») → participantes («los 27 participantes») → familia y amigos (lista nominal larga). Cierre con guiño al tema: «por enseñarme a afrontar la vida con menos ruido.» (12).

---

## C. Índice general — copia literal (pp. 13–15, números de página impresos)

```
Índice general

1. Introducción                                                              25
   1.1. Objetivo del trabajo . . . . . . . . . . . . . . . . . . . . . . . . 25
   1.2. Motivación . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
   1.3. Estructura de la memoria . . . . . . . . . . . . . . . . . . . . . . 26
   1.4. Gestión de datos . . . . . . . . . . . . . . . . . . . . . . . . . . 27
   1.5. Declaración sobre el uso de tecnologías de IA generativa y de asistencia
        en el proceso de redacción . . . . . . . . . . . . . . . . . . . . . 29
   1.6. Aprobación del comité de ética . . . . . . . . . . . . . . . . . . . 29
   1.7. Publicaciones asociadas . . . . . . . . . . . . . . . . . . . . . . . 29

2. Estado del arte                                                           31
   2.1. Onda de presión sonora . . . . . . . . . . . . . . . . . . . . . . . 31
   2.2. Proceso de audición . . . . . . . . . . . . . . . . . . . . . . . . . 33
        2.2.1. Oído externo . . . . . . . . . . . . . . . . . . . . . . . . . 33
        2.2.2. Oído medio . . . . . . . . . . . . . . . . . . . . . . . . . . 33
        2.2.3. Oído interno . . . . . . . . . . . . . . . . . . . . . . . . . 34
               2.2.3.1. La cóclea . . . . . . . . . . . . . . . . . . . . . . 34
               2.2.3.2. Órgano de Corti y células ciliadas . . . . . . . . . 36
               2.2.3.3. Inervación coclear . . . . . . . . . . . . . . . . . 37
               2.2.3.4. Sistema de realimentación . . . . . . . . . . . . . . 39
               2.2.3.5. Transducción mecanoeléctrica . . . . . . . . . . . . 39
        2.2.4. Nervio coclear . . . . . . . . . . . . . . . . . . . . . . . . 39
   2.3. Mecanismos fisiológicos de adaptación neuronal . . . . . . . . . . . 41
        2.3.1. Sistema olivococlear . . . . . . . . . . . . . . . . . . . . . 42
               2.3.1.1. Efectos del sistema olivococlear en entornos ruidosos 44
               2.3.1.2. Influencia en el reconocimiento del habla en ruido . 45
        2.3.2. Adaptación del rango dinámico hacia el nivel de ruido . . . . 46
        2.3.3. Tasa de descarga neuronal . . . . . . . . . . . . . . . . . . 47
   2.4. Potenciales evocados auditivos . . . . . . . . . . . . . . . . . . . 48
        2.4.1. Principales tipos de potenciales . . . . . . . . . . . . . . . 49
               2.4.1.1. ABR . . . . . . . . . . . . . . . . . . . . . . . . . 49
               2.4.1.2. MLR . . . . . . . . . . . . . . . . . . . . . . . . . 51
               2.4.1.3. CAEP . . . . . . . . . . . . . . . . . . . . . . . . 51
        2.4.2. Técnicas de registro . . . . . . . . . . . . . . . . . . . . . 52
               2.4.2.1. Estímulo acústico . . . . . . . . . . . . . . . . . . 54
               2.4.2.2. Transductor . . . . . . . . . . . . . . . . . . . . . 57
               2.4.2.3. Electrodos . . . . . . . . . . . . . . . . . . . . . 59
               2.4.2.4. Amplificación . . . . . . . . . . . . . . . . . . . . 60
        2.4.3. Técnicas de análisis . . . . . . . . . . . . . . . . . . . . . 61
               2.4.3.1. Promediado . . . . . . . . . . . . . . . . . . . . . 61
               2.4.3.2. Rechazo de tramas . . . . . . . . . . . . . . . . . . 63
               2.4.3.3. Reducción de artefactos . . . . . . . . . . . . . . . 64
               2.4.3.4. Deconvolución . . . . . . . . . . . . . . . . . . . . 65
               2.4.3.5. Filtrado digital . . . . . . . . . . . . . . . . . . 66
               2.4.3.6. Análisis de latencias y amplitudes . . . . . . . . . 68

3. Medidas psicoacústicas                                                    69
   3.1. Hipótesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
   3.2. Métodos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
        3.2.1. Participantes . . . . . . . . . . . . . . . . . . . . . . . . 70
        3.2.2. Diseño del experimento . . . . . . . . . . . . . . . . . . . . 71
        3.2.3. Calibración acústica . . . . . . . . . . . . . . . . . . . . . 74
        3.2.4. Análisis de datos . . . . . . . . . . . . . . . . . . . . . . 75
   3.3. Resultados . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76

4. Medidas neurofisiológicas                                                 79
   4.1. Hipótesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
   4.2. Métodos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
        4.2.1. Diseño del experimento . . . . . . . . . . . . . . . . . . . . 80
               4.2.1.1. Estímulo . . . . . . . . . . . . . . . . . . . . . . 81
               4.2.1.2. Escenarios . . . . . . . . . . . . . . . . . . . . . 82
               4.2.1.3. Registro . . . . . . . . . . . . . . . . . . . . . . 84
               4.2.1.4. Procesado . . . . . . . . . . . . . . . . . . . . . . 85
        4.2.2. Calibración acústica . . . . . . . . . . . . . . . . . . . . . 86
        4.2.3. Análisis de datos . . . . . . . . . . . . . . . . . . . . . . 87
               4.2.3.1. Análisis de potenciales ABR . . . . . . . . . . . . . 88
               4.2.3.2. Análisis de potenciales MLR-CAEP . . . . . . . . . . 88
   4.3. Resultados . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
        4.3.1. ABR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
        4.3.2. MLR-CAEP . . . . . . . . . . . . . . . . . . . . . . . . . . . 94

5. Discusión científica                                                      99
   5.1. Discusión de resultados . . . . . . . . . . . . . . . . . . . . . . . 99
   5.2. Conclusión . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
   5.3. Trabajo futuro . . . . . . . . . . . . . . . . . . . . . . . . . . . 101

6. Resultados de aprendizaje                                                103
   6.1. Conocimientos . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
   6.2. Competencias . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
   6.3. Relación del aprendizaje con la carrera profesional . . . . . . . . 105

Bibliografía                                                                105

A. Aprobación del comité de ética                                           111

B. Poster IERASG                                                            113

C. Respuestas ABR y Full-Range                                              115

D. Códigos de programación                                                  131
   D.1. Códigos empleados en el test psicoacústico . . . . . . . . . . . . 132
   D.2. Códigos empleados en el test neurofisiológico . . . . . . . . . . . 137
```

Observaciones del índice: cuatro niveles (capítulo, sección, subsección, subsubsección), todos con número y punto final; el índice general **no** lista los índices de figuras/tablas ni los agradecimientos; «Bibliografía 105» es un error (empieza en la 107); «Poster» sin tilde; los apéndices se numeran con letras A–D y el D tiene subsecciones.

---

## D. Títulos y numeración

- **Capítulos**: dos líneas, «Capítulo 1» y debajo «Introducción» (25); «Capítulo 2» / «Estado del arte» (31); ... Apéndices: «Apéndice A» / «Aprobación del comité de ética» (111). En el índice los capítulos van como «1. Introducción». Cada capítulo empieza en página impar (recto); las páginas pares sobrantes quedan en blanco (78, 102, 106).
- **Nivel 2**: «1.1. Objetivo del trabajo», «3.2. Métodos» — número con punto final y título en caja de frase (solo mayúscula inicial).
- **Nivel 3**: «2.2.1. Oído externo», «4.2.3. Análisis de datos».
- **Nivel 4** (profundidad máxima usada, muy frecuente en el cap. 2 y 4): «2.2.3.1. La cóclea», «2.4.3.6. Análisis de latencias y amplitudes», «4.2.1.4. Procesado».
- **Epígrafes sin numerar** (tipo `\paragraph`/`\subsubsection*`): «Duración», «Intensidad», «Tasa», «Polaridad» dentro de 2.4.2.1 (54–56); «Filtrado dependiente de la latencia» dentro de 2.4.3.5 (67); «Procedimiento 1:» / «Procedimiento 2:» dentro de 4.2.1.4 (85). También títulos de bloque en los preliminares sin numerar: «Resumen», «Abstract», «Agradecimientos», «Índice general», «Índice de figuras», «Índice de tablas», «Bibliografía».
- **Cabeceras de página**: pares «26  1.3. Estructura de la memoria» (número + sección actual), impares «Introducción  27» (título del capítulo + número); páginas de apertura de capítulo con número centrado abajo («25» al pie de la p. 25); en índices y bibliografía la cabecera va en mayúsculas («ÍNDICE GENERAL», «BIBLIOGRAFÍA»).
- **Párrafo introductorio de capítulo: NO existe en ningún capítulo.** Los seis capítulos pasan directamente del título a la primera sección numerada (1.1, 2.1, 3.1, 4.1, 5.1, 6.1). Como sustituto, los dos «arranques» literales (primer párrafo tras el primer epígrafe):
  - Cap. 1, bajo «1.1. Objetivo del trabajo» (25): «La detección de estímulos y el reconocimiento del habla mejora a medida que los estímulos se retrasan con respecto al inicio del ruido. Este fenómeno se conoce como “adaptación al ruido”. Comprender los mecanismos fisiológicos que subyacen a esta adaptación resulta esencial y para ello son necesarias metodologías neurofisiológicas capaces de caracterizarlos.»
  - Cap. 3, bajo «3.1. Hipótesis» (69): «Un estudio previo [López, 2024] ha demostrado que existe una mejora en la inteligibilidad de palabras vocodificadas cuando estas se presentan con un retraso respecto al inicio del ruido. Este hallazgo respalda la existencia de mecanismos de adaptación que favorecen la comprensión en entornos ruidosos. El presente estudio tiene como objetivo (1) evaluar si los resultados son consistentes con los del estudio López [2024] bajo condiciones similares (escenario 1 y 2) y (2) evaluar una nueva condición aumentando la duración del tiempo de ruido precedente al estímulo. Se plantea la hipótesis de que la inteligibilidad de palabras vocodificadas aumentará cuando su presentación sea más tardía con respecto al inicio del ruido (escenario 3), lo que se reflejaría en un valor SRT-50 más bajo, es decir, una mejor inteligibilidad.»
- **Cierre de capítulo**: ningún capítulo termina con resumen o conclusión parcial; acaban en el último párrafo de contenido. Ejemplos: cap. 3 (77): «Los umbrales mejoraron en 2.38 y 2.92 dB en las condiciones media y tardía, respectivamente, en comparación con la condición temprana. El análisis estadístico entre la condición intermedia y la condición tardía no mostró diferencias estadísticamente significativas.»; cap. 4 (98): «Los resultados estadísticos son coherentes con las observaciones previas y muestran que no existen diferencias significativas ni en amplitud, ni en latencia ni en energía entre las dos condiciones. En consecuencia, la morfología de las respuestas en ambos escenarios puede considerarse estadísticamente compatible.» La conclusión global es la sección 5.2 (un solo párrafo) y el trabajo futuro la 5.3.
- Los capítulos experimentales (3 y 4) siguen el esquema de artículo científico: **Hipótesis → Métodos (Participantes, Diseño, Calibración, Análisis de datos) → Resultados**, y la discusión va aparte (cap. 5).

---

## E. Figuras

- **Número total: 79** (53 en el cuerpo: cap. 1 = 2, cap. 2 = 28, cap. 3 = 7, cap. 4 = 15, cap. 5 = 1; apéndice C = 26). Numeración **por capítulo** («Figura 2.10») y por apéndice («Figura C.3»).
- **Formato literal del pie**: «Figura 2.3: Estructura coclear simplificada [Valderrama, 2014].» (35) — «Figura» + número + **dos puntos** + texto en caja de frase + **punto final**. Excepciones/erratas: «Figura 2.4: Diagrama de sección coclear [Valderrama, 2014]» sin punto (35); «Figura 3.5: Aplicación del vocodificador tipo Shannon a palabra Hotel .» con espacio antes del punto (73). Pies largos de varias frases cuando describen paneles: «Figura 2.5: (A) Desplazamiento de la membrana basilar en función de la frecuencia del estímulo. (B) Frecuencias características asociadas a diferentes secciones de la cóclea [Valderrama, 2014].» (36); el más largo es el de la Figura 1.1 (4 frases, 28).
- **Posición del pie: debajo de la figura.** Evidencia (modo `-lineprinter`): en la p. 35 hay 19 líneas en blanco (imagen) antes de «Figura 2.3:» y otras 20 antes de «Figura 2.4:»; en la p. 73, 19 blancas antes de «Figura 3.4:» y 18 antes de «Figura 3.5:». Las figuras van centradas (pie centrado cuando cabe en una línea).
- **Referencia en el texto** (41 menciones; forma dominante el paréntesis «véase»): «(véase Figura 2.3)» ×13 variantes; «ver Figura» ×3; «La Figura X muestra» ×7; «En la Figura X» ×7. Tres frases literales:
  - «La Figura 3.6 muestra los umbrales promedio SRT-50 para cada participante en las tres condiciones experimentales.» (76)
  - «En la Figura 4.8 las componentes de interés presentan amplitudes muy similares, sin diferencias notables en la morfología entre las condiciones temprana y tardía.» (89)
  - «En la respuesta del sujeto P27 (Figura 4.10) se observa la presencia del artefacto PAM (ver 2.4.1.2), asociado a la actividad del músculo postauricular.» (91)
  - Otras: «(véase Figura 2.9 B)» (40), «(véase Figura 4.5 y 4.6)» (82), «Al observar el promedio de todas las respuestas (Figura 4.11), se aprecian diferencias en la morfología entre ambas condiciones.» (92). Algunas figuras se anuncian sin número: «A continuación, se mostrarán algunos ejemplos.» (89), «se representaron de forma conjunta en la siguiente figura» (97).
- **Fuente**: nunca «Fuente: elaboración propia» (la palabra «Fuente» solo aparece como cabecera de la Tabla 2.1, «Fuente sonora»). Las figuras ajenas llevan la cita autor-año al final del pie: «[Valderrama, 2014]» (20 figuras, todas de la tesis del tutor), «Figura de Rüttiger et al. [2017].» (38), «Figura de [López-Poveda, 2018].» (43), «Figura adaptada de [Nieder and Nieder, 1970a] por [López-Poveda, 2018].» (44), «Figura de Jennings and Domínguez [2022].» (48), «[Pujol and Lenoir, 2024]» (37). Las figuras propias no indican nada.
- **Tipos**: diagramas anatómicos y esquemas reproducidos de la bibliografía (cap. 2, mayoría), fotografías de equipos (auriculares Etymotic ER-2, p. 57–58; electrodos 10/20, p. 59), esquemas de montaje (configuración de electrodos, p. 60; registro EEG, p. 53), capturas de pantalla (REDCap p. 28; run del test p. 72; `ginput` p. 87), logotipo (p. 30), diagramas de tiempo de los escenarios (p. 71, 81, 83), formas de onda (clic, ráfaga, p. 81–82), gráficas de resultados (SRT-50 por participante p. 76–77; respuestas ABR y full-range p. 89–97; audiogramas p. 70, 80; señal EEG cruda p. 100). El capítulo 2 es muy denso en figuras (28 en 38 páginas, casi una por página).

---

## F. Tablas

- **Número: 9** (cap. 2: 2.1–2.3; cap. 4: 4.1–4.6). Ninguna en los capítulos 1, 3, 5, 6 ni en apéndices.
- **Pie debajo de la tabla** (evidencia: en la p. 32 el contenido «Fuente sonora ... Turbina de avión 130 dB» precede a «Tabla 2.1: ...»; igual en la p. 93 con las tablas 4.1 y 4.2).
- **Formato literal**: «Tabla 2.1: Niveles promedio SPL de diferentes fuentes a una distiancia reducida.» (32) [sic «distiancia»]; «Tabla 4.2: Resultados de análisis t-test pareado de latencias y energía de respuestas ABR.» (93). Mismo patrón que las figuras: «Tabla» + número + dos puntos + frase + punto.
- **Referencia en el texto**: las tablas **no se citan por número**; se anuncian de forma genérica:
  - «Las siguientes tablas muestran las medidas de latencia, amplitud y energía obtenidas en las condiciones temprana y tardía. Los valores presentados corresponden al promedio calculado a partir de las mediciones de todos los participantes en cada condición.» (93)
  - «Los valores que se presentan en las siguientes tablas corresponden al promedio de todas las medidas individuales obtenidas a partir de los potenciales de cada condición experimental.» (97)
  - Las tablas 2.1–2.3 no se mencionan en el texto (no hay ninguna aparición de «Tabla 2.x» fuera de los pies).
- **Contenido**: valores de referencia de la literatura (niveles SPL de fuentes; tasas máximas e ISI por técnica; ventana de promediación por potencial) y resultados estadísticos (columna «Medida», «P-valor», «Cond. temprana», «Cond. tardía», con unidades en la cabecera «(µV)» o en cada celda «3.5490 ms»). Tablas pequeñas: 2–4 columnas, 2–4 filas de datos; valores con 4 decimales. Tras cada bloque de tablas sigue una frase de interpretación: «En los análisis morfológicos realizados, los p-valores obtenidos no fueron estadísticamente significativos.» (93).

---

## G. Ecuaciones

- **Hay 20 ecuaciones numeradas**, a la derecha y por capítulo: (2.1)–(2.8), (3.1)–(3.5), (4.1)–(4.7). Más una expresión en display sin numerar: «Modelo = fitlme(T, SRT ∼ Cond + Run + (1|Participante))» (75). Ninguna en los capítulos 1, 5 y 6.
- **Introducción**: frase que termina en dos puntos. Ejemplos: «Ecuación de un tono senoidal:» (31); «El ISI se calcula como la inversa de la tasa de estimulación:» (55); «La SNR de la señal después de promediar K respuesta presenta la siguiente expresión:» (63); «La señal de salida del amplificador se expresa como:» (60).
- **Definición de variables**: con «donde» a continuación o con lista «símbolo: significado». Ejemplo literal (31):
  > «p SPL (dB) = 20 · log10 p0   (2.2)
  > donde p es la presión efectiva (en pascales) del sonido medido y p0 = 20 µPa es la presión de referencia en el aire, correspondiente al umbral de audición para una persona joven con audición normal a 1 kHz.»
  Otro (65): «y(t) = s(t) ∗ x(t) + n(t) (2.7) / y(t) : señal EEG. s(t) : secuencia de estimulación. x(t): potencial evocado auditivo. n(t): ruido.» Y en (2.6) la definición va dentro del propio bloque: «xi: es el valor de la muestra i ésima dentro de la trama. N : es el número total de muestras de la trama.» (64).
- **Rasgo singular**: ecuaciones «de cálculo» numeradas con los números sustituidos, p. ej. (4.2): «Tseq1 ≈ (50 + 50 + 50 + 500) ms · 10000/6 ≈ 1083 s ≈ 18 mins» (84), y ecuaciones de calibración con subíndices textuales largos: «SSN60 dB nHL = SSNnorm · 10^(−83/20) · 10^(60/20) (3.3)» (74), «Palabracalibrada = Palabranorm · std(SSN60 dB nHL) · 10^(SNR/20) (3.5)» (75). Es un estilo de estudiante: nombres de variable en palabras («Palabra», «Ruido», «Clic»), no símbolos griegos.
- **Símbolos en línea**: «J = 15 ms», «Fc = [200 2000] Hz», «Q = 30», «(V+ − V−)», ganancias «Ad» y «Ac», «p0 = 20 µPa», «K», «ISI[6, 12] ms», «SNR de +5 dB». Las magnitudes llevan unidad con espacio («65 dB nHL», «20 kHz», «10 ms»); hay 63 casos «N ms» frente a 1 «Nms» y 19 «dB nHL» frente a 0 «dBnHL» (consistente, salvo «25ms» y «60-70dB nHL» en la p. 51).
- Decimales: **punto** en 327 casos frente a 5 con coma (las cinco en la p. 76: «-3,76 dB», «-6,14 dB», «-6,68 dB» — inconsistencia a evitar). Miles: «10.000 respuestas» (80) con punto, pero «44100 Hz» (72) sin separador.

---

## H. Código y comandos

- **Listados**: 14, todos en el apéndice D (131–153), MATLAB. Pie **encima** del código con la etiqueta inglesa sin traducir: «Listing D.1: Script que calibra en dBA y dB nHL ruido SSN.» (131), «Listing D.3: Script que implementa el test SRT-50.» (132), «Listing D.11: Función que procesa la señal EEG para estimar potenciales MLR y CAEP.» (145). Bloque monoespaciado con **numeración de líneas** reiniciada en cada listado. Longitudes: 14, 22, 24, 34, 34, 49, 75, 86, 93, 95, 115, 143, 143 y 153 líneas (≈1080 líneas en 23 páginas). Los listados se parten entre páginas sin aviso. No hay índice de listados.
- **Referencia desde el cuerpo**: una sola, al final de 3.2.2: «En el apéndice D.1 se incluye el códgo de programación que implementa el test psicoacústico.» (73) [sic «códgo»]. El apéndice D.2 no se referencia desde el capítulo 4.
- **Comandos en línea**: no hay (no es un trabajo de sistemas). Las funciones se citan por su nombre en texto corrido con aposición: «utilizando la función fitlme de Matlab» (75); «se empleó la función ginput (graphical input) de MATLAB, que permite seleccionar de manera interactiva puntos directamente sobre la representación gráfica de la señal» (87); «La Figura 4.7 muestra la implementación utilizada para las medidas.» (87). Nombres de fichero: «varios segundos del archivo SSN.wav» (74), «Dado que estaban en formato .wav» (74). Software con fabricante y sede al primer uso: «MATLAB (The Mathworks Inc. Natick, Massachusetts)» (27), «equipo Duet (Intelligent Hearing Systems, Miami, Florida)» (70), «ChatGPT (OpenAI, San Francisco, EEUU)» (29), «SmartEP-CAM (software propietario del sistema de registro Duet)» (84). Si los nombres de función/fichero van en monoespaciado o cursiva: **no determinable desde el texto**.
- **Defectos del código impreso**: acentos rotos en comentarios («Tap ó n en o í do izquierdo», «Calibraci ó n del ruido», «Inicializaci ó n», p. 131–153) por usar `listings` sin soporte UTF-8; identificadores partidos por el justificado («ind icesAleatori os», «Nois elevel _0dBnH L», «R SLSD_ S C L S _ N r e s p o n s e s»); mezcla de comentarios en español e inglés; datos personales en el código («Participante = 'Francisco Sanchez Martinez'», D.5, p. 136); rutas absolutas de Windows y líneas `%save(...)` comentadas; el listado D.14 ocupa 2,5 páginas de código de análisis repetitivo.

---

## I. Citas y bibliografía

- **Estilo en el texto: autor-año entre corchetes** (natbib con corchetes, estilo `apalike`/`plainnat`). Formas: parentética «[Valderrama, 2014]»; múltiple «[Terreros and Delano, 2015; Saldaña, 2015]» (43); mismo autor varios años «[Lopez-Poveda et al., 2016, 2017]» (46); letras «[Nieder and Nieder, 1970a,b]» (44); textual «propuesta de Jewett and Williston [1971]» (49), «Figura de Rüttiger et al. [2017].» (38), «de acuerdo con lo establecido en el capítulo 16 de Majumder et al. [2018]» (70), «Como documento de guía se empleó Batuecas Caletrío et al. [2022].» (104). El conector es el inglés «and» (bibliografía en inglés). Nunca numéricas [1].
- **Dónde se concentran** (recuento por mi expresión regular; parentéticas + textuales): cap. 1 = 3 + 0; **cap. 2 = 36 + 3 (de ellas 19 en pies de figura)**; cap. 3 = 2 + 2; cap. 4 = 3 + 1; cap. 5 = 2 + 3; cap. 6 = 0 + 1. Total ≈ 56 llamadas para 39 referencias. El estado del arte acumula ~70 % de las citas; la referencia más citada es la tesis del tutor [Valderrama, 2014] (20 veces, casi todas en pies de figura). Los capítulos experimentales citan muy poco (solo la metodología que replican y los algoritmos usados).
- **Orden de la bibliografía: alfabético** por primer apellido (p. 107–110), sin numerar. Formato `apalike`: «Apellido, I. N. and Apellido, I. (año). Título. *Revista*, vol(núm):páginas. doi:...». Tres entradas literales:
  - Artículo (107): «Dean, I., Harper, N. S., and McAlpine, D. (2005). Neural population coding of sound level adapts to stimulus statistics. Nature Neuroscience, 8(12):1684–1689. doi:10.1038/nn1541.»
  - Libro (107): «Dallos, P. (1973). The Auditory Periphery. Biophysics and Physiology. Number 548. Academic Press, New York.» — y tesis (109): «Valderrama, J. T. (2014). Desarrollo e implementación de un sistema avanzado de registro de potenciales evocados auditivos. Nuevas estrategias de estimulación a alta tasa. PhD thesis, Universidad de Granada. http://hdl.handle.net/10481/50945.»
  - Web/documento institucional (109): «Universidad de Granada (2024). Recomendaciones para el uso de la inteligencia artificial en la universidad de granada. pages 1–74. https://ceprud.ugr.es.» — **sin fecha de acceso** (ninguna web la lleva).
- **Total: 39 referencias.** Reparto: 29 artículos de revista (74 %), 3 tesis (Valderrama 2014, López 2024, Kearney 2018), 3 libros/capítulos (Dallos 1973, Evans 1974, Cárdenas y Marrero 1994), 3 documentos web (Elsevier 2025, Universidad de Granada 2024, Pujol y Lenoir 2024 «Cochlea.eu»), 1 comunicación a congreso (Valderrama et al. 2025, el póster del propio trabajo). Proporción web/documentación frente a artículos ≈ 1:10. Antigüedad: desde 1954 (Dawson) hasta 2025; muchas referencias clásicas de fisiología (1970–1985).
- **Defectos a evitar**: títulos en minúscula por BibTeX («universidad de granada», «Generative ai policies»); DOIs con formato variable («doi:10...», «doi: 10...», «10.1016/...» a secas, «https://doi.org/...»); misma persona con dos grafías («López-Poveda, E. A.» y «Lopez-Poveda, E. A.», y «MarrufoPérez» sin guion en un pie); cita parentética usada como sujeto: «[Jennings and Domínguez, 2022] mostraron que...» (47) frente a la forma correcta «Jewett and Williston [1971]»; la Jennings & Domínguez (2022) aparece en «Hearing Research, 23(3)» con un DOI de otra revista; entrada «Bibliografía 105» en el índice.

---

## J. Registro y redacción

- **Persona y voz**: capítulos 1–5 en **impersonal con «se»** («se diseñó», «se emplearon», «se registraron», «se observa», «se presenta»; 0 marcas de primera persona del singular) con alguna primera persona del plural muy ocasional (5 casos: «Tal y como hemos visto en la sección 2.2.4» (54), «podemos observar» (36), «podemos estimar» (66), «nos indican» (52), «nos queda» (86)). Los preliminares (agradecimientos) y el **capítulo 6 van en primera persona del singular** (30 marcas: «descubrí», «adquirí», «He aprendido», «considero haber desarrollado», «he tenido el privilegio»). La portada y el informe hablan en tercera persona.
- **Tiempos verbales**: cap. 1 presente («se propone», «se describe», «El capítulo 2 presenta») y pretérito perfecto («se ha desarrollado»); cap. 2 presente atemporal («La cóclea ... se encuentra dividida»); caps. 3–4 métodos en pretérito indefinido («Se diseñó un procedimiento», «Un total de 15 sujetos ... participaron», «Se registraron potenciales») y resultados en presente («La Figura 3.6 muestra», «Se observa que», «presentan») con apoyo de indefinido para lo estadístico («no mostró diferencias»); cap. 5 presente + condicional para lo futuro («Sería por tanto interesante», «podría comprobarse», «consistiría en emplear»); cap. 6 pretérito perfecto («he adquirido», «he aprendido»).
- **Longitud**: 275 párrafos de cuerpo analizados; **media 2,5 frases por párrafo (mediana 2), ≈60 palabras por párrafo**; **frases de 24 palabras de media (mediana 22; p10 = 11, p90 = 40)**. Párrafos cortos, frases medias-largas con subordinadas de gerundio («..., evidenciando adaptación», «..., permitiendo una representación adecuada»).
- **Listas**: unas 12 en 81 páginas, casi todas en el cap. 2 y el cap. 6. Tres tipos: (a) viñetas con **etiqueta + dos puntos** (el glifo de viñeta no se extrae; se deduce por la sangría uniforme en el modo maquetación): «Frecuencia: número de ciclos por segundo...», «Amplitud: ...», «Fase: ...» (31–32); «Aferentes: ...», «Eferentes: ...» (38); «Tasa baja: ...», «Tasa media: ...», «Tasa alta: ...» (39–40); «Condensación: ...», «Rarefacción: ...», «Alternante: ...» (56); «Amplificación diferencial: ...», «Filtrado: ...», «Amplificación: ...» (60–61); «Condición temprana: ...», «Condición tardía: ...» (80); y todas las competencias del 6.2 («Realización de otoscopia: he aprendido a ...»). (b) **Listas numeradas «1. 2. 3. 4.»** para los pasos de procesado («Procedimiento 1:» / «Procedimiento 2:», 85). (c) **Enumeraciones en línea «(1) ... y (2) ...»** para objetivos e hipótesis (25, 64, 69) y «(1)», «(2)», «(3)» como pasos de calibración dentro de párrafos (74–75). Las viñetas sin etiqueta son raras (ventajas del EEG, 52: «El sistema de registro puede ser portátil.»).
- **Negrita/cursiva en el cuerpo**: **no determinable desde el texto**. Inferencias: las etiquetas de las listas («Frecuencia:», «Realización de otoscopia:») van probablemente en negrita (patrón `\item \textbf{...}`); los anglicismos («speech-shaped noise», «fade-in», «run», «eartip», «grand-average», «full-range») y el título del TFG dentro del informe irían en cursiva. No hay indicios de negritas en frases del cuerpo.
- **Anglicismos y siglas**: fórmula fija al primer uso, en el cuerpo 14 veces y también en el resumen: «(SRT-50, por sus siglas en inglés: speech reception threshold)», «(OHCs, por sus siglas en inglés: outer hair cells)» (36), «(ISI, por sus siglas en inglés: inter-stimulus interval)» (55), «(DRA, por sus siglas en inglés: Dynamic Range Adaptation)» (46). Otras siglas se definen solo con paréntesis «(PVCN)», «(GND)». No hay glosario; varias siglas del cuerpo dependen de la definición del resumen (ABR, MLR, CAEP, AEP, EEG, SNR). Anglicismos sin traducir muy frecuentes: «run», «runs», «fade-in y fade-out», «eartip», «trigger», «grand-average», «full-range», «one-down, one-up», «delay», «setup», «software propietario». Siglas en plural a la inglesa: «OHCs», «IHCs», «AEPs», «EEGs».
- **Nivel de detalle técnico**: alto y concreto en métodos (modelos de equipos con fabricante y ciudad, niveles «60 dB nHL (63.7 dBA SPL)», filtros «Butterworth paso banda de orden 4 con Fc = [200 2000] Hz», «muestreada a 20 kHz», umbrales «90 %», «J = 15 ms y resolución de 40 filtros por década»), didáctico en el estado del arte (explica desde qué es una onda sonora).
- **Objetivos**: un párrafo con enumeración en línea, no lista: «En este Trabajo Fin de Grado se propone los siguientes objetivos específicos: (1) diseñar e implementar un estudio subjetivo basado en psicoacústica que replique los resultados obtenidos en un estudio previo y (2) un estudio objetivo basado en señales EEG que permita caracterizar los mecanismos neurofisiológicos que participan en el proceso de adaptación neuronal al ruido. La hipótesis de partida es que la representación neuronal de estímulos acústicos se verá potenciada en escenarios donde los mecanismos de adaptación estén activos.» (25). Cada estudio reformula su objetivo como «Hipótesis» (3.1, 4.1).
- **Requisitos**: no se formulan como tales (no hay apartado de requisitos ni de especificaciones).
- **Resultados**: número + interpretación inmediata: «Además, se indica el valor medio general por escenario, con resultados de -3,76 dB para la condición temprana, -6,14 dB para la condición intermedia y -6,68 dB para la condición tardía.» → «Las diferencias entre la condición temprana y cada una de las condiciones retrasadas son estadísticamente significativas.» (76). En el cap. 4: descripción cualitativa por sujeto (Figuras 4.8–4.10) → promedio (4.11) → tablas con p-valores → frase de síntesis. Los resultados negativos se dicen sin eufemismos: «Los resultados no son reproducibles, las componentes MLR no son identificables» (95).
- **Limitaciones**: en la discusión, como párrafos con causa y efecto, sin epígrafe propio: «Las condiciones de registro para las medidas neurofisiológicas no fueron las más óptimas. Los registros no se realizaron en un espacio específicamente acondicionado para el registro de EEG, sino en aulas universitarias y viviendas particulares. Como consecuencia, las señales EEG obtenidas presentaron un nivel considerable de ruido...» (100).
- **Frases típicas de apertura y cierre** (literales):
  1. «Este documento está estructurado en 6 capítulos.» (26)
  2. «El capítulo 2 presenta literatura fundamental que permite poner en contexto y comprender los estudios realizados.» (26)
  3. «El capítulo 3 presenta los métodos y resultados de un estudio orientado a caracterizar mecanismos de adaptación al ruido mediante técnicas subjetivas basadas en psicoacústica, replicando un estudio previo.» (26)
  4. «Este estudio se centra en el registro y análisis de potenciales evocados auditivos ABR, MLR y CAEP en diferentes condiciones de ruido.» (79)
  5. «A continuación, se presentan algunas de las técnicas empleadas en la estimación y análisis de los potenciales evocados auditivos.» (61)
  6. «Los potenciales evocados obtenidos presentan una alta variabilidad en la morfología de la respuesta y en su mayoría son poco reproducibles. Sin embargo, en algunos casos es posible identificar las componentes I, III y V. A continuación, se mostrarán algunos ejemplos.» (89)
  7. «En conjunto, estos hallazgos apoyan la conclusión de que la morfología de los ABR en ambas condiciones es estadísticamente equivalente.» (92)
  8. «Finalmente, cabe señalar la intención de difundir los resultados de esta nueva campaña de medidas tanto en forma de artículo científico como mediante su presentación en el 49th Annual Midwinter Meeting of the Association for Research in Otorhinolaryngology (ARO), que tendrá lugar en San Juan (Puerto Rico, EEUU) en febrero de 2026.» (101)
- **Conectores frecuentes** (recuento en el cuerpo): Además (14), Sin embargo (10), De esta forma (7), De este modo (6), Posteriormente (5), Finalmente (5), Asimismo (5), A continuación (4), En general (4), En cambio (4), En primer lugar (3), Por último (3), En consecuencia (3), Dado que (3), Por ejemplo (3), Seguidamente (2), Por lo tanto (2), Inicialmente (2), En este contexto (2), Cabe destacar (1), Aun así (1). Marcadores de secuencia en la descripción de la estructura: «En primer lugar, ... A continuación, ... Seguidamente, ... Finalmente, ...» (26–27).
- **Otros rasgos**: «véase» mucho más que «ver» (16 frente a 5); referencias cruzadas a secciones por número solo «(véase 2.3.2)», «(ver 2.4.1.2)», «descrito en 2.4.3.3»; comillas tipográficas para acuñar términos: “adaptación al ruido” (25), “efecto de antienmascaramiento” (44), “hipoacusia oculta” (105); «TFG» como abreviatura en el cuerpo (8 veces: «este TFG») junto a «este trabajo» (6), «este proyecto» (5), «esta memoria» (3); notas al pie con superíndices numéricos solo en 1.7 para las afiliaciones de los coautores (29–30).

### J.1 Tres párrafos representativos completos

**Diseño / arquitectura** (4.2.1.2 Escenarios, 82):
> «Se diseñaron dos secuencias de estimulación con el objetivo de implementar los escenarios experimentales. El ruido empleado fue ruido blanco gaussiano, considerado el más adecuado para enmascarar los clics, y se presentó a un nivel de 60 dB nHL. Dado que los clics se presentaron a 65 dB nHL, la SNR en la que se registraron los potenciales fue de +5 dB.»
>
> «Ambas secuencias incluyeron intervalos de silencio entre los periodos de ruido-ráfaga, cuya duración seguía una distribución uniforme entre 450 y 550 ms (véase Figura 4.5 y 4.6). Para evitar transiciones abruptas, el ruido fue suavizado mediante ventanas de fade-in y fade-out de 10 ms de duración. Además, el ruido se prolongó 50 ms tras el último clic de cada ráfaga, para mantener la continuidad temporal del estímulo.»

**Resultados / evaluación** (4.3.1 ABR, 92):
> «En general, los efectos observados a nivel individual en las señales ABR no fueron sistemáticos entre los participantes. En algunos casos las amplitudes fueron menores, en otros mayores y, en ciertos participantes, las latencias resultaron inferiores en la condición tardía. Los resultados estadísticos son coherentes con estas observaciones y muestran que no existen diferencias significativas ni en amplitud, ni en latencia ni en energía entre las dos condiciones. En conjunto, estos hallazgos apoyan la conclusión de que la morfología de los ABR en ambas condiciones es estadísticamente equivalente.»

**Conclusiones** (5.2 Conclusión, 101 — es la sección completa):
> «Los resultados sugieren que el paradigma utilizado en el test SRT-50 es adecuado para evaluar la adaptación conductual en la inteligibilidad de palabras vocodificadas en presencia de ruido. Por su parte, el test neurofisiológico indica que los clics podrían no ser el estímulo acústico más eficaz para caracterizar los mecanismos neuronales de adaptación al ruido. Estos hallazgos abren la posibilidad de implementar cambios metodológicos que permitan evidenciar efectos neurofisiológicos consistentes que reflejen adaptación neuronal.»

---

## K. Capítulo a capítulo

| Cap. | Páginas (físicas) | Palabras | Figuras / tablas / ecuaciones | Propósito y contenido | Valoración |
|---|---|---|---|---|---|
| 1. Introducción | 25–30 (6) | 1 922 | 2 fig. / 0 / 0 | 1.1 objetivo e hipótesis (3 párrafos); 1.2 motivación (1 párrafo); 1.3 estructura de la memoria (un párrafo por capítulo, patrón «El capítulo N presenta...»); 1.4 gestión de datos (REDCap, principios FAIR); 1.5 declaración de uso de IA generativa (ChatGPT «para mejorar la redacción», revisado por autor y supervisor, cita las recomendaciones UGR 2024 y la política de Elsevier); 1.6 comité de ética (Helsinki, CEIH-UGR, consentimiento informado); 1.7 publicaciones asociadas (póster IERASG 2025 con los coautores y sus afiliaciones en notas al pie) | Bien: la declaración de IA y la ética son fórmulas reutilizables y muy actuales en la UGR. Mal: la motivación es muy corta (1 párrafo) y va después del objetivo; erratas («valorar la si el marco propuesto para sirve», «presenta presenta», «en en el»); la introducción mezcla aspectos administrativos (REDCap, póster) con lo científico |
| 2. Estado del arte | 31–68 (38) | 10 171 (53 % del cuerpo) | 28 fig. / 3 tab. / 8 ec. | De lo básico (onda sonora, dB SPL) a lo específico: anatomía del oído, mecanismos de adaptación (sistema olivococlear, DRA, tasa de descarga), potenciales evocados (tipos, registro, análisis: promediado, rechazo de tramas, ITMS, deconvolución RSLSD, filtrado dependiente de latencia). Profundidad hasta nivel 4 | Bien: progresión didáctica, figura por concepto, ecuaciones con variables definidas, estadística justificada al final (t-test vs Wilcoxon). Mal: desproporcionado (38 de 81 páginas), 20 figuras copiadas de la tesis del tutor, erratas (intesidad, polardidad, principalemnte, acohol, proximo, vectibular), lista de niveles SPL sin fuente, texto de apoyo en algunos epígrafes muy breve («Duración», un párrafo) |
| 3. Medidas psicoacústicas | 69–77 (9) | 1 744 | 7 fig. / 0 / 5 ec. | Hipótesis; Métodos (participantes n=15 con audiometría, diseño del test SRT-50 adaptativo one-down one-up, vocoder tipo Shannon con parámetros en lista, calibración con ecuaciones paso a paso, análisis con modelo lineal mixto `fitlme`); Resultados (medias por condición, significación, mejora de 2.38 y 2.92 dB) | Bien: formato de artículo, reproducible (equipos, niveles, fórmula del modelo). Mal: los resultados ocupan solo 2 páginas y no se dan los estadísticos del modelo (p-valores, IC) salvo «estadísticamente significativas»; decimales con coma solo aquí; figura 3.5 con pie defectuoso |
| 4. Medidas neurofisiológicas | 79–98 (20) | 3 600 | 15 fig. / 6 tab. / 7 ec. | Hipótesis; Métodos (n=12, estímulo clic en rarefacción, ráfagas de 6 clics con ISI uniforme 6–12 ms, dos escenarios 50/800 ms, cálculo del tiempo de registro, registro con Duet a 20 kHz, dos procedimientos de procesado en listas numeradas, calibración, análisis con `ginput` ciego); Resultados ABR (3 sujetos ejemplo + grand-average + 2 tablas) y MLR-CAEP (3 sujetos + promedio + 4 tablas) | Bien: la parte más «ingenieril»; procedimientos numerados, tablas con p-valores, honestidad con los resultados negativos y los artefactos (PAM). Mal: algunas frases incompletas («utilizando el cursor del para señalar»); las tablas no se citan por número; figuras de respuestas individuales consumen mucho espacio (una por página) |
| 5. Discusión científica | 99–101 (3) | 966 | 1 fig. / 0 / 0 | 5.1 discusión (coherencia con López 2024 y con la literatura de DRA; por qué no se vio adaptación con clics: constante de 30 ms de Jennings & Domínguez; limitaciones de las condiciones de registro con figura de EEG crudo); 5.2 conclusión (un párrafo); 5.3 trabajo futuro (5 párrafos: estímulos tipo voz, ráfagas más largas, niveles variables, nueva base de datos con retardo ≈30 ms, difusión en ARO 2026) | Bien: discusión con hipótesis explicativas y propuestas concretas; conclusiones breves y prudentes («sugieren», «podrían»). Mal: la conclusión global es un solo párrafo; no hay recapitulación de objetivos cumplidos ni lista de aportaciones |
| 6. Resultados de aprendizaje | 103–105 (3) | 940 | 0 / 0 / 0 | 6.1 conocimientos (4 párrafos en 1.ª persona); 6.2 competencias (lista de 11 ítems «Etiqueta: he...»: otoscopia, audiometría, REDCap, registro AEP, trato con participantes, redacción científica, MATLAB, Scopus, calibración, bases de datos, LaTeX); 6.3 relación con la carrera profesional (máster en acústica, contrato en proyecto EarlyDiag-HLOSS) | Bien: capítulo reflexivo poco habitual que el tribunal valora (competencias del grado). Mal: salto de registro (impersonal → yo) sin transición; información personal (referencia del contrato) |
| **Planificación / presupuesto / costes** | — | — | — | **No existe.** No hay fases, diagrama de Gantt, horas, costes de personal, hardware, software ni total. Lo más parecido: el cálculo de la duración de las secuencias de registro (ec. 4.2–4.3: «≈ 18 mins», «≈ 39 mins») y la mención de la financiación (beca Ramón y Cajal) en los agradecimientos y de la cesión del equipo Duet | Es un TFG de corte investigador; si la memoria nueva necesita planificación/costes, no puede tomarse de aquí |
| Bibliografía | 107–110 (4) | 951 | — | 39 entradas alfabéticas, estilo apalike | Ver I |
| Apéndice A | 111 (1) | 8 | — | Solo la portadilla «Apéndice A / Aprobación del comité de ética» | Documento no incluido en el PDF |
| Apéndice B | 112–113 (2) | 451 | — | Portadilla + póster IERASG completo (inglés; autores, afiliaciones, Motivation/Methods/Results/Conclusions, referencias, agradecimientos a la financiación) | Modelo de cómo adjuntar una publicación derivada |
| Apéndice C | 114–129 (16) | 274 | 26 fig. | Respuestas ABR y full-range de los 12 sujetos (dos figuras por página) y los dos promedios (repiten las Figuras 4.11 y 4.15) | Material suplementario sin texto |
| Apéndice D | 130–153 (24) | ≈8 800 tokens | 14 listados | D.1 código del test psicoacústico (4 listados); D.2 código del test neurofisiológico (10 listados) | Ver H; útil como patrón de «código al final, nunca en el cuerpo» |

---

## L. Particularidades UGR/ETSIIT

- **Portada literal (p. 1)**, en este orden vertical: «TRABAJO FIN DE GRADO» / «INGENIERÍA DE TECNOLOGÍAS DE TELECOMUNICACIÓN» / título en tres líneas centradas («Exploración neurofisiológica de / mecanismos neuronales de / adaptación al ruido») / «Autor» / «Francisco Sánchez Martínez» / «Director» / «Joaquín Tomás Valderrama Valenzuela» / «Escuela Técnica Superior de Ingenierías Informática y de / Telecomunicación» / «—» / «Granada, septiembre de 2025». No hay texto «Universidad de Granada» ni departamento en la portada (el escudo, si lo hay, es imagen).
- **Segunda portada (p. 3)**: repite título, «Autor» y «Director» sin escuela ni fecha.
- **Orden de preliminares**: portada → verso → segunda portada → resumen (con palabras clave delante) → abstract (con keywords delante) → informe del director → agradecimientos → índice general → índice de figuras → índice de tablas. **No hay** dedicatoria, ni declaración del alumno (originalidad, autorización de depósito en biblioteca), ni glosario.
- **Fórmula oficial del director** (p. 9), con las piezas: identificación («D. ..., profesor del Área de ... del Departamento ... de la Universidad de Granada.»), verbo «Informa:», objeto («Que el presente trabajo, titulado ..., ha sido realizado bajo su supervisión por ..., y autorizo la defensa de dicho trabajo ante el tribunal que corresponda.»), cláusula de constancia («Y para que conste, expide y firma el presente informe en Granada a 5 de septiembre de 2025 .»), pie de firma («El director:» + nombre completo). Hay un cambio de persona dentro de la fórmula («ha sido realizado bajo su supervisión ... y autorizo»).
- **Mención al tribunal**: solo en el informe («ante el tribunal que corresponda»).
- **«Granada, mes de año»**: portada «Granada, septiembre de 2025»; informe con día «Granada a 5 de septiembre de 2025».
- **Firma**: el espacio de firma se deduce de la línea «El director:» seguida del nombre; no hay firma textual del alumno.
- **DNI**: no aparece en ningún sitio.
- **Nombre del tutor**: «Director» en portada; «D. Joaquín Tomás Valderrama Valenzuela» en el informe; «el Dr. Joaquín T. Valderrama» en agradecimientos; «Dr. Joaquín T. Valderrama» en 6.3. **Departamento**: «Departamento Teoría de la Señal, Telemática y Comunicaciones» (informe) y «Departamento de Teoría de la Señal, Telemática y Comunicaciones (TSTC)» (agradecimientos).
- **Elementos UGR recientes que conviene imitar**: la sección «1.5. Declaración sobre el uso de tecnologías de IA generativa y de asistencia en el proceso de redacción» con cita a [Universidad de Granada, 2024] («Recomendaciones para el uso de la inteligencia artificial en la universidad de granada», ceprud.ugr.es) — texto literal (29): «Durante la preparación de este documento, el autor utilizó ChatGPT (OpenAI, San Francisco, EEUU) para mejorar la redacción. Tras el uso de esta herramienta, tanto el autor como su supervisor revisaron y editaron el contenido según fue necesario y asumen plena responsabilidad sobre el contenido final de esta memoria. El uso de esta herramienta en este TFG se adhiere a las recomendaciones de la Universidad de Granada con respecto al uso de herramientas de inteligencia artificial [Universidad de Granada, 2024] y a las políticas de uso de inteligencia artificial generativa promovidas por editoriales de literatura científica, tales como Elsevier (Ámsterdam, Países Bajos) [Elsevier, 2025].»
- **Numeración de preliminares defectuosa**: números impresos «3» en la p. física 2, «4» en la 5, «6» en la 7, «12» en la 12 (a partir de ahí coinciden hasta la 111); de la 112 en adelante la impresa va una por delante de la física (falta la página impresa 112). Indica ensamblado de PDF externos (informe, póster, aprobación) y conviene evitarlo.

---

## M. Cifras globales

| Magnitud | Valor |
|---|---|
| Páginas físicas totales | 155 (última impresa 154) |
| Preliminares (portada → índices) | 24 (1–24), de ellas 7 en blanco o casi (2, 8, 10, 16, 22, 24) |
| Cuerpo (caps. 1–6) | 81 (25–105), con 3 páginas en blanco intercaladas (78, 102, 106) |
| Bibliografía | 4 (107–110) |
| Anexos | 43 (111–153) + 2 blancas finales (154–155) |
| Figuras | 79 (53 cuerpo + 26 apéndice C) |
| Tablas | 9 |
| Ecuaciones numeradas | 20 (+1 display sin numerar) |
| Listados de código | 14 (≈1 080 líneas MATLAB) |
| Referencias | 39 (≈56 llamadas en el texto) |
| Siglas definidas con «por sus siglas en inglés» | 14 en el cuerpo (+8 en el resumen) |
| Palabras totales | 36 621 |
| Palabras del cuerpo (caps. 1–6) | 19 343 |
| Palabras por capítulo | 1: 1 922 · 2: 10 171 · 3: 1 744 · 4: 3 600 · 5: 966 · 6: 940 |
| Resumen / abstract / palabras clave | ≈430 / ≈380 / 10 términos cada uno |
| Agradecimientos | 517 |
| Índices (texto) | 5 274 (incluye los puntos conductores) |
| Bibliografía (texto) | 951 |
| Apéndice D (código) | ≈8 800 tokens |
| Frases por párrafo / palabras por frase | 2,5 (mediana 2) / 24 (mediana 22) |
| Densidad de figuras en el cuerpo | 0,65 figuras/página (cap. 2: 0,74; cap. 4: 0,75) |

---

## N. Lecciones transferibles

### N.1 Reglas concretas para una memoria «a la ETSIIT 2025» como esta

1. **Portada y preliminares en este orden**: «TRABAJO FIN DE GRADO» / titulación en mayúsculas / título / «Autor» + nombre / «Director» (o «Tutor») + nombre / escuela / «Granada, mes de año»; después segunda portada, resumen con palabras clave, abstract con keywords, informe del tutor con la fórmula «Informa: Que el presente trabajo, titulado ..., ha sido realizado bajo su supervisión por ..., y autorizo la defensa de dicho trabajo ante el tribunal que corresponda. Y para que conste, expide y firma el presente informe en Granada a D de mes de año.», agradecimientos, índice general, de figuras y de tablas. Añadir la declaración del alumno si la escuela la exige (aquí falta).
2. **Resumen en 4 párrafos** (encuadre de una frase; método y resultado de cada bloque de trabajo; cierre con aportación y líneas futuras), ≈400 palabras, con todas las siglas definidas al primer uso también dentro del resumen, y abstract equivalente en inglés.
3. **LaTeX clase libro a dos caras**: «Capítulo N» en línea propia + título; epígrafes «N.M.» con punto final hasta nivel 4; capítulo siempre en página impar; cabeceras alternas (par: número + sección; impar: capítulo + número); índices con puntos conductores.
4. **Sin párrafo introductorio de capítulo**: entrar directamente en la sección N.1; tampoco resumen al final de capítulo. La función «hoja de ruta» la cumple 1.3 «Estructura de la memoria» con un párrafo por capítulo que empieza «El capítulo N presenta...».
5. **Capítulos experimentales con esquema de artículo**: Hipótesis → Métodos (Participantes / Diseño del experimento / Calibración / Análisis de datos) → Resultados; y una «Discusión» aparte que termina en «Conclusión» (un párrafo) y «Trabajo futuro».
6. **Figuras**: pie debajo, «Figura N.M: Texto con mayúscula inicial y punto final.»; numeración por capítulo; referencia en texto con «(véase Figura N.M)» o «La Figura N.M muestra ...»; fuente ajena como cita autor-año al final del pie («Figura de Autor et al. [año].», «Figura adaptada de ... por ...»); las propias sin nota de fuente. Tablas igual, pie debajo, pequeñas, con unidades en cabecera y p-valores a 4 decimales; mejor citarlas por número (aquí no se hace).
7. **Ecuaciones numeradas por capítulo a la derecha**, introducidas por frase con dos puntos y seguidas de «donde ...» o de lista «símbolo: significado»; unidades con espacio («65 dB nHL», «10 ms», «50 %»), punto decimal en todo el documento.
8. **Siglas con la fórmula «(SIGLA, por sus siglas en inglés: término inglés)» al primer uso** y anglicismos admitidos sin traducir cuando son términos de la disciplina; coherencia de grafía en todo el texto.
9. **Registro**: impersonal con «se» en todo el cuerpo técnico; métodos en indefinido, resultados en presente, futuro en condicional; párrafos de 2–3 frases (~60 palabras) y frases de ~22–24 palabras; conectores de secuencia («En primer lugar», «A continuación», «Posteriormente», «Finalmente») y de contraste («Sin embargo», «En cambio»). La primera persona del singular queda reservada a agradecimientos y al capítulo de aprendizaje.
10. **Citas autor-año entre corchetes con natbib**: «[Apellido, año]» parentética y «Apellido et al. [año]» cuando el autor es sujeto; bibliografía alfabética sin numerar con DOI; el estado del arte concentra las citas y los capítulos propios citan solo lo que replican o usan.
11. **Código fuera del cuerpo**: apéndice propio con listados numerados, pie encima, líneas numeradas, y una sola frase en el cuerpo que remita al apéndice («En el apéndice D.1 se incluye el código ...»). Si se usa `listings`, traducir la etiqueta a «Listado» y activar UTF-8 para que no se rompan los acentos.
12. **Secciones «institucionales» que la UGR valora en 2025**: declaración de uso de IA generativa (texto y cita a las recomendaciones UGR 2024), gestión de datos/ética cuando hay personas, publicaciones o difusión derivadas (con el póster/artículo en apéndice) y un capítulo final de «Resultados de aprendizaje» (conocimientos, competencias, relación con la carrera).

### N.2 Cosas que NO aparecen en este TFG

- Emojis, iconos, colores en texto, markdown, enlaces en el cuerpo.
- Negritas en frases del cuerpo (no hay indicios; solo, inferiblemente, en etiquetas de lista).
- Viñetas en exceso: ~12 listas en 81 páginas, siempre con ítems de una o varias frases completas, nunca telegráficos; ninguna lista de una sola palabra.
- Citas numéricas [1], superíndices de cita, notas al pie de contenido (solo afiliaciones en 1.7).
- «Fuente: elaboración propia» en pies.
- Tablas de código, código en el cuerpo, comandos de terminal, pantallazos de consola.
- Capítulo de planificación temporal, Gantt, presupuesto, costes, análisis de requisitos, casos de uso, diagramas UML.
- Glosario/acrónimos, lista de listados, lista de ecuaciones, dedicatoria, declaración de originalidad del alumno, DNI.
- Resúmenes al principio o al final de cada capítulo; tablas-resumen de objetivos cumplidos; «aportaciones» enumeradas.
- Primera persona en el cuerpo técnico; juicios de valor sobre el propio trabajo («excelente», «novedoso»).
- Tablas grandes o apaisadas, figuras a sangre, páginas de figuras en el cuerpo (van al apéndice C).

### N.3 Errores detectados que conviene evitar

- Erratas sin corregir: «distiancia» (32), «intesidad» (45), «vectibular» (34), «proximo» (36), «principalemnte» (51), «polardidad» (56), «acohol» (52), «códgo» (73), «Cassic» (86), «Inicalización»/«aletorio» (código), «bioteconología» (29); frases rotas: «valorar la si el marco propuesto para sirve para detectar» (25), «El capítulo 4 presenta presenta» (26), «en en el congreso» (26), «utilizando el cursor del para señalar» (87), «realizar el estudio de sin correr riesgos» (104); «mas» sin tilde, «25ms», «60-70dB nHL» (51).
- Pies de figura sin punto final o con espacio antes del punto (2.4, 3.5); pie de la Figura 3.5 con texto de cuerpo pegado detrás.
- Índice con la bibliografía en la página equivocada (105 vs 107); «Poster» sin tilde.
- Numeración impresa incoherente en preliminares y una página impresa ausente (112) por ensamblar PDF externos; apéndice A reducido a una portadilla sin el documento.
- Decimales con coma en una sola página (76) frente al punto en el resto; miles con punto («10.000») y sin separador («44100 Hz»).
- Tablas nunca citadas por número; tablas 2.1–2.3 sin mención en el texto.
- Mezcla de grafías de un mismo autor en la bibliografía (López-Poveda / Lopez-Poveda), títulos en minúscula por BibTeX («universidad de granada»), DOIs con cuatro formatos, cita parentética usada como sujeto («[Jennings and Domínguez, 2022] mostraron»), webs sin fecha de acceso.
- Etiqueta «Listing» en inglés y acentos rotos en los comentarios del código; identificadores partidos por el justificado; datos personales dentro del código.
- Cambio de persona dentro del informe del director («bajo su supervisión ... y autorizo») y espacio antes del punto en la fecha.
- Desproporción: estado del arte = 53 % del cuerpo; discusión + conclusión = 5 %; conclusión global de un solo párrafo sin recapitular objetivos.
- Salto de registro brusco entre el cap. 5 (impersonal) y el cap. 6 (primera persona), sin frase puente.

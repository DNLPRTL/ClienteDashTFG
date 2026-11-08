# Ficha de formato y estilo — TFG Juan Rafael Sánchez Martínez (ETSIIT, UGR, junio 2024)

Fichero analizado: `docs/memoria/DE OTROS TUTORES PERO RECIENTES DE MI FACULTAD/JuanRafaelSanchezMartinez_TFG_MPE_CMJ.pdf`
Método: texto extraído con `pdftotext` (flujo y `-layout`), leído entero (150 páginas PDF, 44 819 palabras según `wc`). Las páginas se citan como **páginas del PDF** salvo que se diga «pág. impresa». Regla de conversión en el cuerpo: pág. impresa = PDF − 24 (la pág. impresa 3 es la PDF 27).
Nota sobre las citas literales: el PDF usa fuentes Computer Modern con codificación OT1, por lo que `pdftotext` separa los acentos («S´anchez», «sen˜ales»). En las citas literales de esta ficha se han recompuesto los acentos; el resto del texto (erratas incluidas) se reproduce tal cual.
Peso del patrón: ALTO (TFG reciente de la misma escuela, otros tutores; formato de plantilla LaTeX de la ETSIIT).

---

## A. Identificación

- **Título completo (portada, PDF 1):** «Desarrollo de Sistemas Espaciotemporales basados en antenas a Giga Hercios» (título) + subtítulo «Estudio de las características de no reciprocidad en circuitos modulados temporalmente con señales no sinusoidales». En el resumen (PDF 5) se unen con dos puntos: «Desarrollo de Sistemas Espaciotemporales basados en antenas a Giga Hercios: Estudio de las características…». OJO: en el informe de los directores (PDF 9) y en 1.4 (PDF 33) el título aparece como «…Giga Hertzios…» (inconsistencia portada/informe).
- **Autor:** Juan Rafael Sánchez Martínez (firma los agradecimientos como «Rafa», PDF 11).
- **Directores (la portada dice «Directores», no «Tutor»):** Carlos Molero Jiménez («tutor1») y Mario Pérez Escribano («tutor2»). Presentados en el informe (PDF 9) como «Profesor del Área de Teoría de la Señal y Comunicaciones del Departamento Teoría de la Señal, Telemática y Comunicaciones de la Universidad de Granada».
- **Departamento:** Teoría de la Señal, Telemática y Comunicaciones (TSTC), Área de Teoría de la Señal y Comunicaciones.
- **Titulación literal (portada):** «TRABAJO FIN DE GRADO» / «INGENIERÍA DE TECNOLOGÍAS DE TELECOMUNICACIÓN». Confirmado en 6.3 («carrera de Ingeniería de Tecnologías de Telecomunicación», PDF 137) y 7.1 («Grado en Ingeniería de Tecnologías de Telecomunicación», PDF 139). Desliz en 1.1 (PDF 27): «constituye el último paso para la obtención del título de Graduado en Ingeniería de Sistemas de Telecomunicación por la Universidad de Granada» (error heredado, probablemente de otra memoria).
- **Centro literal (portada):** «Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación» seguido de una raya «—» sola en la línea siguiente (hueco de plantilla sin rellenar o logo).
- **Universidad:** Universidad de Granada (no aparece como texto en la portada; sí en el informe de los directores y en el cuerpo).
- **Fecha literal:** «Granada, Junio de 2024» (portada). Informe de los directores firmado «en Granada a 24 de Junio de 2024» (PDF 9). Gantt: febrero–junio 2024.
- **Número de páginas:** 150 páginas PDF, de las cuales 16 en blanco (4, 6, 8, 10, 12, 14, 22, 24, 26, 66, 124, 132, 144, 148, 149, 150). Paginación impresa: romana en preliminares (Acrónimos = i, Índice general = iii–iv, Índice de figuras = v–ix, Índice de códigos = xi), arábiga desde «Parte I» (pág. 1 = PDF 25) hasta la bibliografía (pág. 123 = PDF 147).
- **Herramienta de maquetación:** LaTeX, con certeza casi total (clase tipo `book`/`memoir` a doble cara). Evidencias: (1) 7.2 (PDF 140) cita «Overleaf. Este último es un editor de textos en formato LaTeX que es gratuito»; (2) páginas en blanco al verso para que cada capítulo abra en impar (`openright`); (3) acentos extraídos como glifos separados = codificación OT1 de Computer Modern; (4) las tablas se llaman «Cuadro» (nombre por defecto de `babel` español); (5) caja «Contenido» al inicio de cada capítulo (`minitoc`); (6) listados con pie «Código X.Y:» e «Índice de códigos» (paquete `listings` con nombre personalizado); (7) ecuaciones numeradas «(2.11)» alineadas a la derecha; (8) cabeceras alternas: páginas pares «12  2.1. Análisis de filtros paso-banda pasivos», impares «Marco Teórico  13» (PDF 36–37); (9) 375 de 3472 líneas del cuerpo terminan en guion de partición (≈11 %), texto justificado; (10) bibliografía BibTeX estilo `plain`/`unsrt` («[1] David M. Pozar. Microwave Engineering. John Wiley & Sons, Inc., Hoboken, NJ, fourth edition, 2012.»); (11) errores típicos de comillas LaTeX («”estudio…”», «.El éxito…deseas..»).

## B. Estructura completa, en orden, con páginas PDF

| Bloque | Páginas PDF | Pág. impresa | Observaciones |
|---|---|---|---|
| Portada | 1 | — | Ver texto literal abajo |
| Página casi vacía con solo un «3» | 2 | — | Artefacto de maquetación |
| Segunda portada (título, subtítulo, Autor, Directores; sin cabecera ni fecha) | 3 | — | PDF 4 en blanco |
| Resumen y palabras clave (español) | 5 | — | PDF 6 en blanco |
| Abstract y keywords (inglés) | 7 | — | PDF 8 en blanco |
| Informe/autorización de los directores | 9 | — | PDF 10 en blanco |
| Agradecimientos (incluye la dedicatoria) | 11 | — | PDF 12 en blanco |
| Acrónimos | 13 | i | PDF 14 en blanco |
| Índice general | 15–16 | iii–iv | |
| Índice de figuras | 17–21 | v–ix | PDF 22 en blanco |
| Índice de códigos | 23 | xi | PDF 24 en blanco. No hay índice de tablas |
| Portadilla «Parte I. Desarrollo del trabajo» | 25 | 1 | PDF 26 en blanco |
| Capítulo 1. Introducción y visión general | 27–34 | 3–10 | |
| Capítulo 2. Marco Teórico | 35–65 | 11–41 | PDF 66 en blanco |
| Capítulo 3. Implementación de circuitos en MATLAB y ADS | 67–92 | 43–68 | |
| Capítulo 4. Simulación de circuitos en MATLAB y ADS | 93–123 | 69–99 | PDF 124 en blanco |
| Capítulo 5. Diseño e implementación real | 125–131 | 101–107 | PDF 132 en blanco |
| Capítulo 6. Conclusión | 133–138 | 109–114 | |
| Capítulo 7. Recursos, costes y planificación | 139–142 | 115–118 | PDF 142 casi vacía (solo cabecera) |
| Portadilla «Parte II. Bibliografía» | 143 | 119 | PDF 144 en blanco |
| Bibliografía | 145–147 | 121–123 | PDF 148–150 en blanco |

**Faltan:** declaración de originalidad del alumno; autorización de depósito/biblioteca; página de firma del alumno; DNI; dedicatoria separada (va dentro de los agradecimientos); índice de tablas (hay dos cuadros sin índice); glosario (solo lista de 10 acrónimos); anexos; notas al pie (ninguna en todo el documento).

**Portada literal (PDF 1):**
> TRABAJO FIN DE GRADO
> INGENIERÍA DE TECNOLOGÍAS DE TELECOMUNICACIÓN
> Desarrollo de Sistemas Espaciotemporales basados en antenas a Giga Hercios
> Estudio de las características de no reciprocidad en circuitos modulados temporalmente con señales no sinusoidales
> Autor
> Juan Rafael Sánchez Martínez
> Directores
> Carlos Molero Jiménez
> Mario Pérez Escribano
> Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación
> —
> Granada, Junio de 2024

**Informe/autorización de los directores, literal (PDF 9):**
> D. Carlos Molero Jiménez (tutor1), Profesor del Área de Teoría de la Señal y Comunicaciones del Departamento Teoría de la Señal, Telemática y Comunicaciones de la Universidad de Granada.
>
> D. Mario Pérez Escribano (tutor2), Profesor del Área de Teoría de la Señal y Comunicaciones del Departamento Teoría de la Señal, Telemática y Comunicaciones de la Universidad de Granada.
>
> Informan:
> Que el presente trabajo, titulado Desarrollo de Sistemas Espaciotemporales basados en antenas a Giga Hertzios, Estudio de las características de no reciprocidad en circuitos modulados temporalmente con señales no sinusoidales, ha sido realizado bajo su supervisión por Juan Rafael Sánchez Martínez (alumno), y autorizamos la defensa de dicho trabajo ante el tribunal que corresponda.
> Y para que conste, expiden y firman el presente informe en Granada a 24 de Junio de 2024.
>
> Los directores:
>
> Carlos Molero Jiménez (tutor1)   Mario Pérez Escribano (tutor2)

Nota: «(tutor1)», «(tutor2)» y «(alumno)» son marcadores de la plantilla que no se eliminaron. No hay firma visible en el texto (no determinable si hay firma manuscrita/imagen). No existe declaración del alumno.

**Resumen y palabras clave, literal (PDF 5):**
> Desarrollo de Sistemas Espaciotemporales basados en antenas a Giga Hercios: Estudio de las características de no reciprocidad en circuitos modulados temporalmente con señales no sinusoidales
> Juan Rafael Sánchez Martínez
>
> Palabras clave: ADS, aislamiento inverso, circuitos lineales variables en el tiempo (LTV), filtros paso-banda (BPF) aislantes, matriz ABCD, matriz de admitancia compleja, modulación especiotemporal (STM), no reciprocidad, parámetros S, pérdida de inserción.
>
> Resumen
>
> En este proyecto se demuestra un filtro de paso de banda aislante con bajas pérdidas de inserción y alto aislamiento inverso mediante la modulación de sus resonadores constituyentes. El trabajo consiste en el estudio y análisis del comportamiento del filtro cuando es modulado temporalmente mediante señales periódicas con diferentes formas de onda. La idea desarrollada constituye una base de trabajo para los circuitos modulados espaciotemporalmente, ofreciendo infinidad de oportunidades en este campo.
>
> Para entender el principio de funcionamiento de estos dispositivos, se ha desarrollado un método de análisis en el dominio espectral. Se demuestra que la no reciprocidad en la misma frecuencia es el resultado de la conversión no recíproca de frecuencias a las frecuencias de intermodulación (IM) por los resonadores variables en el tiempo. Mediante una frecuencia de modulación, profundidad de modulación y retardo de fase específicos, la potencia de la señal en las frecuencias IM se convierte nuevamente a la frecuencia RF y se suma constructivamente para formar una banda pasante de bajas pérdidas de inserción, mientras que en la dirección inversa se suman destructivamente para crear el aislamiento.
>
> Para demostrar la teoría, se realizaron numerosas simulaciones en MATLAB, las cuales fueron validadas mediante ADS (Advanced Design System). Adicionalmente, se diseñó un prototipo de filtro con una única etapa resonante. De esta forma, se ha verificado el correcto funcionamiento de los filtros paso banda aislantes, los cuales pueden encontrar aplicaciones en sistemas de transmisión y recepción simultánea de señales radio de banda ancha.

**Abstract y keywords, literal (PDF 7):**
> Development of spatio-temporal systems based on Giga Hertz antennas: Study of non-reciprocity characteristics in temporally modulated circuits with non-sinusoidal signals.
> Juan Rafael Sánchez Martínez
>
> Keywords: ABCD matrix, ADS, complex admittance matrix, insertion loss, inverse isolation, isolating bandpass filters (BPFs), linear time-varying circuits (LTV) circuits, non-reciprocity, S-parameters, spatiotemporal modulation (STM).
>
> Abstract
>
> This work demonstrates an isolating bandpass filter with low insertion losses and high reverse isolation by modulating its constituent resonators. This project consists of the study and analysis of the behavior of a filter when it is temporally modulated using periodic signals with different waveforms. The idea developed constitutes a working basis for spatiotemporally modulated circuits, offering endless opportunities in this field.
>
> To understand the principle of operation of these devices, a method of analysis in the spectral domain has been developed. It is shown that non-reciprocity at the same frequency results from the non-reciprocal conversion of frequencies to intermodulation (IM) frequencies by the time-varying resonators. Using a specific modulation frequency, modulation depth, and phase delay, the signal power at the IM frequencies is converted back to the RF frequency and constructively summed to form a low-loss passband. In contrast, in the reverse direction, it is destructively summed to create isolation.
>
> Numerous simulations were performed in MATLAB to demonstrate the theory, and they were validated using ADS (Advanced Design System). A prototype filter with a single resonant stage was also designed and manufactured. In this way, the correct operation of the isolating bandpass filters has been verified, which can find applications in broadband radio transmission and simultaneous reception systems.

Observación: resumen y abstract tienen la misma estructura de tres párrafos (qué se demuestra / cómo funciona / qué se hizo y para qué sirve), ~230 palabras cada uno; las palabras clave van ordenadas alfabéticamente, separadas por comas y con punto final. El abstract dice «designed and manufactured» mientras el resumen solo dice «se diseñó».

**Agradecimientos, literal (PDF 11):**
> Agradecimientos
>
> Quisiera expresar mi más sincero agradecimiento a mis tutores, Carlos Molero Jiménez y Mario Pérez Escribano, por su inestimable ayuda y amabilidad durante la realización de este trabajo. Su guía no solo me ha proporcionado valiosos conocimientos técnicos, sino también importantes lecciones de vida. Me han acogido y tratado como si fuese uno más de ellos, lo cual valoro profundamente.
>
> Asimismo, quiero agradecer a Sergio Ortiz Ruiz, cuya colaboración ha sido esencial para el diseño del prototipo real. Sin su inigualable asistencia, este proyecto no habría sido posible.
>
> A mis padres, mi hermana y Elena, / por su fe inquebrantable en mí y su apoyo constante, / siempre brindándome fuerza y aliento en cada paso.
> A mis amigos y compañeros de vida, / por ser faros en mi trayecto, iluminando el camino / y compartiendo alegrías y desafíos.
> Con profundo agradecimiento, / Rafa

(La dedicatoria va alineada a la derecha dentro de la misma página, según el layout.)

**Acrónimos (PDF 13, pág. i), literal, formato «SIGLA  Desarrollo» en dos columnas sin puntuación:** ADS Advanced Design System; BPF Band-Pass Filter; CI Circuitos integrados; EM Electromagnetic; IM Intermodulation; LT Línea de Transmisión; LTV Linear Time-Varying; PDN Power Distribution Network; RF Radiofrecuencia; STM Spatio-Temporal Modulationl [sic]. Diez entradas, mezcla de desarrollos en inglés y español.

## C. Índice general, copiado literalmente (PDF 15–16)

```
Índice general

I   Desarrollo del trabajo                                          1

1. Introducción y visión general                                    3
   1.1. Descripción del trabajo . . . . . . . . . . . . . . . . .   3
   1.2. Estado del arte  . . . . . . . . . . . . . . . . . . . . .   4
   1.3. Objetivos y fases del trabajo  . . . . . . . . . . . . . .   7
        1.3.1. Objetivos . . . . . . . . . . . . . . . . . . . . .   7
        1.3.2. Fases del trabajo . . . . . . . . . . . . . . . . .   8
        1.3.3. Herramientas de desarrollo  . . . . . . . . . . . .   8
   1.4. Descripción de la memoria  . . . . . . . . . . . . . . . .   9

2. Marco Teórico                                                   11
   2.1. Análisis de filtros paso-banda pasivos  . . . . . . . . .  12
   2.2. Análisis de circuitos variables en el tiempo . . . . . . .  15
        2.2.1. Método del dominio espectral  . . . . . . . . . . .  16
        2.2.2. Parámetros S: Transmisión y reflexión . . . . . . .  21
   2.3. Señales periódicas a tener en cuenta . . . . . . . . . . .  25
        2.3.1. Señal moduladora cosenoidal . . . . . . . . . . . .  25
        2.3.2. Señal moduladora triangular . . . . . . . . . . . .  28
        2.3.3. Señal moduladora cuadrada . . . . . . . . . . . . .  30
   2.4. Resonadores y filtros variables en el tiempo . . . . . . .  32
        2.4.1. Resonador modulado en el tiempo . . . . . . . . . .  33
        2.4.2. Filtros: Introducción de la modulación espacial . .  34
        2.4.3. Filtro paso banda tripolar aislante . . . . . . . .  38
        2.4.4. Convergencia numérica . . . . . . . . . . . . . . .  40

3. Implementación de circuitos en MATLAB y ADS                     43
   3.1. Desarrollo de códigos en MATLAB  . . . . . . . . . . . . .  44
        3.1.1. Condensador variable en el tiempo . . . . . . . . .  45
        3.1.2. Resonador modulado en el tiempo . . . . . . . . . .  53
        3.1.3. Filtro paso banda aislante con n etapas . . . . . .  54
   3.2. Implementación de circuitos en ADS . . . . . . . . . . . .  57
        3.2.1. Componentes utilizados en los modelos circuitales .  59
        3.2.2. Modelos circuitales de las diferentes configuraciones 66

4. Simulación de circuitos en MATLAB y ADS                         69
   4.1. Resultados para la señal cosenoidal  . . . . . . . . . . .  69
   4.2. Resultados para la señal triangular  . . . . . . . . . . .  82
   4.3. Resultados para la señal cuadrada  . . . . . . . . . . . .  91

5. Diseño e implementación real                                   101
   5.1. Prototipado y simulación en ADS  . . . . . . . . . . . . . 101
   5.2. Montaje real del circuito  . . . . . . . . . . . . . . . . 103
   5.3. Experimento para la medición de no reciprocidad  . . . . . 104

6. Conclusión                                                     109
   6.1. Conclusiones y seguimiento del trabajo . . . . . . . . . . 109
        6.1.1. Conclusiones  . . . . . . . . . . . . . . . . . . . 109
        6.1.2. Seguimiento del trabajo . . . . . . . . . . . . . . 110
   6.2. Líneas futuras . . . . . . . . . . . . . . . . . . . . . . 112
   6.3. Conclusiones finales . . . . . . . . . . . . . . . . . . . 113

7. Recursos, costes y planificación                               115
   7.1. Recursos humanos . . . . . . . . . . . . . . . . . . . . . 115
   7.2. Recursos hardware y software . . . . . . . . . . . . . . . 116
   7.3. Recursos hardware y software . . . . . . . . . . . . . . . 116
   7.4. Costes . . . . . . . . . . . . . . . . . . . . . . . . . . 116
   7.5. Planificación  . . . . . . . . . . . . . . . . . . . . . . 116

II  Bibliografía                                                  119

Bibliografía                                                      123
```

Notas: el índice general solo baja al nivel 3 (X.Y.Z); el nivel 4 (1.3.3.1 «Herramientas software», 1.3.3.2 «Herramientas hardware», 3.1.1.1 «Implementación de otras señales moduladoras», 3.2.1.1 «Puertos» … 3.2.1.6 «Simuladores de parámetros S y transitorio») solo aparece en la caja «Contenido» de cada capítulo. Error: 7.3 repite el título de 7.2 (debería ser «Fabricación y medidas»). La entrada «Bibliografía 123» apunta a la última página de la bibliografía y no a la primera (121): otro error.

## D. Títulos y numeración

- **Capítulos:** «Capítulo 1» en una línea y el título en la siguiente («Introducción y visión general»). Debajo, una caja titulada **«Contenido»** con el mini-índice del capítulo (hasta nivel 4, con puntos conductores y páginas). Después, **siempre un párrafo introductorio sin epígrafe** antes del primer X.1 (los siete capítulos lo tienen).
- **Partes:** portadillas «Parte I / Desarrollo del trabajo» (PDF 25) y «Parte II / Bibliografía» (PDF 143), a página propia con verso en blanco.
- **Nivel 2:** «2.1. Análisis de filtros paso-banda pasivos» (número con punto final, espacio, título). **Nivel 3:** «2.2.1. Método del dominio espectral». **Nivel 4:** «3.2.1.1. Puertos», «1.3.3.1. Herramientas software» (numerado, con punto, en línea propia). **Profundidad máxima:** 4 (X.Y.Z.W), usada en los capítulos 1 y 3.
- **Mayúsculas:** títulos de capítulo con mayúsculas tipo título solo a veces («Marco Teórico», pero «Diseño e implementación real»); epígrafes en minúscula salvo nombres («Parámetros S: Transmisión y reflexión», «Capacitancia Variable»). No hay regla uniforme.
- **Epígrafes sin numerar:** solo en preliminares (Resumen, Abstract, Agradecimientos, Acrónimos, índices) y «Bibliografía». En el cuerpo todo va numerado; no hay «Resumen del capítulo» como epígrafe.
- **Párrafo introductorio, 2 casos literales:**
  - Cap. 1 (PDF 27): «El propósito principal del presente capítulo es proporcionar una visión genérica de los aspectos más relevantes de este trabajo de fin de grado. Asimismo, se pretende realizar una descripción que permita al lector familiarizarse con los apartados que conforman este documento.»
  - Cap. 3 (PDF 67): «En este capítulo se describirá el proceso de implementación y análisis de los circuitos utilizando MATLAB y ADS, destacando las características y metodologías empleadas en cada plataforma para el desarrollo y simulación de los mismos. El uso combinado de MATLAB y ADS proporciona una metodología robusta para el diseño y análisis de circuitos modulados temporalmente. MATLAB se utiliza para el desarrollo inicial y el análisis teórico, mientras que ADS permite validar estos resultados en un entorno de simulación más cercano a la realidad física. Esta integración asegura una comprensión completa y detallada del comportamiento de los circuitos, optimizando su diseño y facilitando su implementación práctica.»
  - (Otros: cap. 2 PDF 35 «El principal objetivo del presente capítulo es proporcionar una visión específica y concreta acerca del fundamento teórico…»; cap. 6 PDF 133 «Tras haber expuesto los aspectos más relevantes del trabajo, en este apartado se presentan las conclusiones obtenidas durante su desarrollo…»; cap. 7 PDF 139 «Este último capítulo de la memoria está destinado a exponer la planificación y los recursos esenciales utilizados en el proyecto.»)
- **Cierres de capítulo/apartado:** no hay epígrafe de resumen, pero sí párrafos de cierre marcados con fórmula:
  - Fin de 2.2.2 (PDF 48): «En resumen, el análisis de circuitos variables en el tiempo mediante el método del dominio espectral y la derivación de parámetros S multimodo proporciona una base sólida para diseñar y optimizar filtros no recíprocos.»
  - Fin del cap. 2 (PDF 65): «Como resumen del apartado 2.4, podemos concluir que es necesario utilizar más de un componente de circuito de variación temporal para alcanzar la no reciprocidad en la frecuencia central. […] Por ejemplo, un filtro aislante de tres polos puede ofrecer un rendimiento de RF significativamente superior en comparación con el filtro de dos polos.»
  - Fin del cap. 4 (PDF 121–123): párrafo «En el presente capítulo se ha llevado a cabo un estudio exhaustivo…», lista de ventajas/inconvenientes por señal, «En resumen, el estudio realizado ha permitido observar…», anuncio del siguiente capítulo («El siguiente paso será la fabricación de un prototipo…») y remate: «A modo de conclusión, el presente capítulo ha subrayado la importancia de explorar modulaciones alternativas y su impacto en el rendimiento de los filtros BPF aislante, ofreciendo una guía valiosa para futuras investigaciones y desarrollos tecnológicos en este campo.»
  - Fin del cap. 3 (PDF 91): «Para conluir el apartado, se va a realizar la misma simulación que en el apartado de MATLAB pero mediante ADS, con el objetivo de validar los resultados (ver figura 3.11). De este modo, se ha podido corrobar la validex de los resultados, tras la coincidencia obtenida entre MATLAB y ADS.» [sic]
  - Fin del cap. 5 (PDF 131): anuncio de trabajo futuro («Se espera que en unos meses se pueda llevar a cabo un diseño más complejo que incluya tres etapas resonadoras…»). El cap. 7 termina en el cuadro del Gantt, sin cierre.

## E. Figuras

- **Total:** 43 (cap. 1: 1; cap. 2: 10; cap. 3: 11; cap. 4: 15; cap. 5: 6; caps. 6–7: 0). Numeración **por capítulo** («Figura 4.6»).
- **Pie literal:** «Figura 2.3: (a) Circuito LTV con un único condensador en derivación modulado sinusoidalmente. (b) Circuito espectral equivalente con puertos para todas las frecuencias IM.» → «Figura N.M:» con **dos puntos**, texto con mayúscula inicial y **punto final** (excepción: «Figura 5.2: Disposición física del circuito, (a) 2-D, (b) 3-D», sin punto). Pies cortos descriptivos en caps. 2–3 y 5; pies larguísimos (10–15 líneas) en los estudios paramétricos del cap. 4, que listan todos los parámetros y los 16 paneles: «Figura 4.6: Estudios paramétricos del filtro de tres polos (JS1 = J3L = 0.0119 Ω−1, J12 = J23 = 0.0062 Ω−1, RS = RL = 50 Ω, L0 = 4 nH, y valor del condensador estático C0 = 6.37 pF). (a) Modulación de |S21,(0,0)| con fm variable. (b) … (o) Síntesis de |S11,(0,0)| con fm = 0.15f0, ξ = 0.27, y φ = 45◦.» (PDF 107).
- **Posición del pie:** debajo de la figura (las etiquetas de subfigura «(a) (b) (c)…» preceden al pie en la extracción). Subfiguras etiquetadas (a)…(o) **incluyendo la «(ñ)»** entre (n) y (o) (PDF 99, 107, 112, 113, 118, 119): detalle del paquete `subcaption` con alfabeto español.
- **Cómo se referencian (3 frases literales):**
  - «La modulación temporal de estos componentes induce una no reciprocidad efectiva, lo que permite que la señal viaje en una sola dirección a través del dispositivo (ver figura 1.1).» (PDF 29)
  - «En la Figura 2.2 se presenta un esquema de un circuito LTV elemental que consta de un único condensador C(t) en derivación, cuya capacitancia varía con el tiempo.» (PDF 41)
  - «En las figuras 4.1a y 4.1d se presenta la transmisión entre la frecuencia portadora de RF ω en el puerto 1 y ω en el puerto 2, representada por S21,(0,0) y S12,(0,0).» (PDF 94)
  - (Otras: «tal y como se puede ver en la figura 3.1» PDF 68; «En la figura 4.2(b)-(f), se observa la transmisión…» PDF 95; «Los resultados … se muestran en la figura 5.3» PDF 126.) 114 referencias a figuras en total; inconsistencia: «figura» en minúscula 60 veces, «Figura» 50 veces; subfiguras unas veces «4.1a», otras «4.8(b)-(f)».
- **Fuente:** nunca se escribe «Fuente: elaboración propia». Solo la figura 1.1 (tomada del artículo base) termina el pie con la cita «[17]». El resto se da por propio sin indicarlo.
- **Tipos:** esquemas de topología/circuito (1.1, 2.2, 2.3, 2.7–2.10); gráfico conceptual de un BPF (2.1); espectros de Fourier (2.4–2.6); diagrama de flujo (3.1); capturas de componentes y simuladores de ADS (3.2–3.9); gráficas de resultados MATLAB/ADS (3.10, 3.11, 4.1–4.3, 4.5, 4.7, 4.8, 4.11–4.13); mapas paramétricos 4×4 a página completa (4.4, 4.6, 4.9, 4.10, 4.14, 4.15); layout 2D/3D de ADS (5.2); fotografías del circuito y del banco de medida (5.4, 5.5); captura del analizador de espectros (5.6).
- **Colocación:** flotantes de LaTeX; las figuras 3.10 y 3.11 se desplazan al final del capítulo en una página sin cabecera (PDF 92) y el texto lo reconoce: «ver figura 3.10, situada al final del capítulo» (PDF 81). Seis figuras ocupan página completa.

## F. Tablas

- **Número:** 2, ambas en el capítulo 7, llamadas **«Cuadro»**: «Cuadro 7.1: Resumen de costes» y «Cuadro 7.2: Diagrama de Gantt» (dos puntos, sin punto final). No existe índice de tablas.
- **Pie:** debajo de la tabla (en la extracción el contenido precede al pie). El cuadro 7.1 lleva encima una cabecera propia «Presupuesto» y el 7.2 «Diagrama de Gantt». Ambos comparten la página PDF 141 (página de flotantes sin cabecera ni número), lo que deja la PDF 142 casi vacía con solo la cabecera «118  7.5. Planificación».
- **Referencias literales:** «El cuadro 7.1 recoge un breve resumen de los costes asociados al proyecto considerando todo tipo de recursos, así como el coste total al que este asciende.» (PDF 140) y «Utilizando el diagrama de Gantt mostrado en la tabla 7.2, se pueden observar las diversas tareas que componen el proyecto y la duración de cada una.» (PDF 140) → inconsistencia «cuadro»/«tabla».
- **Contenido:** 7.1 = presupuesto con filas agrupadas (Recursos Humanos: Ing. Técnico 25 €/h × 500 h = 12500 €, Ing. Superior 55 €/h × 200 h = 11000 €; Recursos Software y Hardware: ADS 20000 €, MATLAB 900 €, PC 2100 €; Fabricación y Medidas: Fabricación 10 €, Medida en cámara 240 €; TOTAL 46750 €). 7.2 = Gantt como tabla: 10 tareas en filas («Revisión bibliográfica de artículos», «Familiarización con el entorno en ADS», «Diseño de funciones y scripts en Matlab», «Análisis y simulaciones en MATLAB», «Desarrollo de esquemáticos en el entorno de ADS», «Validación de resultados con ADS», «Diseño y medición del prototipo», «Redacción de la memoria», «Revisión de la memoria», «Preparación defensa Trabajo Fin de Grado») × columnas Feb–Jun 2024 divididas en «1°» y «2°» (quincenas). No hay tablas de resultados ni de componentes: todos los resultados numéricos del cap. 4 van en prosa.

## G. Ecuaciones

- **Sí, muchas:** 64 numeradas, (2.1)–(2.60) en el marco teórico y (3.1)–(3.4) en implementación. Numeración por capítulo, número entre paréntesis alineado a la derecha, en línea aparte (`equation`), incluidas matrices espectrales de página entera (2.11, 2.44, 2.48, 2.58, 2.60) y sistemas con dos números en una línea («(2.28) (2.29)», «(2.37) (2.38)», `subequations`/`align`).
- **Cómo se introducen:** frase que termina sin dos puntos (o con ellos) y la ecuación lleva su propia puntuación (coma o punto): «El comportamiento temporal del condensador se modela con la expresión» → «C(t) = C0 + ∆C cos(ωmt + ϕ),» (2.2).
- **Definición de variables, ejemplo literal (PDF 41):** «donde C0 es la capacitancia nominal (en ausencia de modulación), ∆C es la profundidad de la modulación (indica el máximo cambio en la capacitancia debido a la modulación), ωm es la frecuencia angular de modulación y ϕ s el desfase inicial de la modulación.» [sic «s»]. Variante en lista: «donde:» seguido de viñetas (PDF 44: «Los elementos diagonales corresponden a la admitancia en cada frecuencia de intermodulación (IM). / Los elementos fuera de la diagonal corresponden a la transconductancia entre diferentes frecuencias de intermodulación.»; PDF 50: «A es la amplitud de la onda. ω = 2πf es la frecuencia angular. ϕ es la fase inicial.»).
- **Referencias a ecuaciones:** «ecuación 2.2», «(ecuación 2.10)», «según ecuación 2.53», «vista en 2.11», «conforme a lo descrito en 2.50» — número sin paréntesis, 27 referencias explícitas con la palabra «ecuación».
- **Símbolos en línea:** abundantes en el cuerpo (S21, |S21,(0,0)|, S12,(0,−1), ξ, fm, ∆ϕ, φ, D(0, 0), RS, RL, QL, ω ± nωm, 1/jωC(t)), en modo matemático (cursiva). Mezcla ϕ/φ para la misma fase entre capítulos (2 y 4). Unidades pegadas en algunos casos («1GHz», «200MHz», «25dB», «10ns») y separadas en otros («50 Ω», «6.37 pF», «4 nH»); decimales con punto (no coma).
- Las derivaciones se hacen completas (de la ley de Kirchhoff a los parámetros S multimodo, 2.14–2.32), siguiendo el artículo [17].

## H. Código y comandos

- **Listados:** 8, todos MATLAB, todos en el cap. 3, con **índice propio** («Índice de códigos», PDF 23). Pie **debajo** del bloque: «Código 3.1: Código de Matlab de definición de parámetros iniciales.» / «Código 3.3: Código de Matlab para el cáculo de los parámetros de dispersión en cada frecuencia.» [sic] / «Código 3.8: Código de Matlab para la implementación del filtro BPF aislante con 2 etapas.» (dos puntos, punto final).
- **Presentación:** bloque monoespaciado (paquete `listings`), comentarios en español («% Parámetros iniciales a ajustar», «N = 7; % Tamaño de la matriz»), sin números de línea detectables. Los acentes de los comentarios salen rotos en el PDF («Par ´a metros», «se ~n al», «Conversi o´ n», «Tama n~ o»): `listings` sin configurar para UTF-8. Longitud: de 7 líneas (3.2) a ~45 líneas (3.8, que ocupa PDF 79–81, cruzando dos saltos de página). Fragmentos, no programas completos: cada listado es un bloque funcional (parámetros, inicialización, bucle, representación, variantes de relleno de matriz, resonador, filtro de dos etapas).
- **Prosa alrededor del código:** cada listado va precedido de un anuncio («…tal y como se puede ver en el código 3.2.», «El código 3.8 implementa esto que estamos comentando.») y seguido/precedido de párrafos que explican línea a línea cada variable: «El parámetro N define el tamaño de la matriz, el cual se encuentra relacionado con el número de armónicos… El vector de frecuencias fRf = linspace(finicial, ffinal, numero puntos) crea un conjunto de n puntos… La fase de la señal moduladora se define con theta grados. Este valor en grados se convierte a radianes mediante theta = deg2rad(theta grados)…» (PDF 70, párrafo de ~330 palabras).
- **Nombres de variables/funciones/componentes en el texto:** aparecen sin comillas; probablemente en monoespaciada (inferencia: los guiones bajos desaparecen en la extracción, «theta grados», «S matrices», «P 1Tone», «Term G», «Vf Triangle», «Z1P Eqn», lo que es coherente con `\texttt{}`; no determinable con certeza desde el texto). Funciones citadas por nombre: «La función squeeze se utiliza para…», «utilizando la función angle», «usando la función rad2deg», «se utiliza la función plot» (PDF 73–74). Parámetros de ADS en línea: «Num=1», «Z=50 Ohm», «P=polar(dbmtow(-20),0)», «Freq=fRf», «Vpeak=2*ampm», «Harmonics=16», «LSSP FreqAtPort[2]=fRf+fm», «StopTime=500.0 nsec» (PDF 83–89). Fórmulas de hoja de datos como ecuaciones numeradas: «cap = Coeff[0] + Coeff[1] · v + …» (3.1), «Coeff = list(Coeff[0], …)» (3.2).
- No hay comandos de terminal ni rutas de ficheros; no hay pseudocódigo; el diagrama de flujo (figura 3.1) sustituye al pseudocódigo.

## I. Citas y bibliografía

- **Estilo en el texto:** numérico entre corchetes «[17]», con rangos «[1–5]», «[6–10]», «[12–15]» y cita en pie de figura («…se refiere a la carga [17].»). Casi siempre al final de la frase antes del punto; a veces «Según [18], …», «como se describe en [19]», «consultar [24]».
- **Orden de la bibliografía:** por orden de aparición (unsrt): [1]–[17] se citan en el cap. 1 en ese orden; [18]–[23] en el cap. 2; [24] en el cap. 5.
- **Formato literal de entradas (BibTeX plain/unsrt, autores con «and», sin DOI ni URL):**
  - Artículo: «[17] Xiaohu Wu, Xiaoguang Liu, Mark D. Hickle, Dimitrios Peroulis, Juan Sebastián Gómez-Díaz, and Alejandro Álvarez Melcón. Isolating bandpass filters using time-modulated resonators. IEEE Transactions on Microwave Theory and Techniques, 67(6):2331–2345, 2019.»
  - Libro: «[1] David M. Pozar. Microwave Engineering. John Wiley & Sons, Inc., Hoboken, NJ, fourth edition, 2012.»
  - Web/hoja de datos con fecha de acceso: «[24] Skyworks Solutions, Inc. Smv1234-079lf: Hyperabrupt junction tuning varactor diode, 2024. Accessed: 2024-06-22.»
  - Tesis: «[16] M. D. Hickle. Synthesis, design, and fabrication techniques for reconfigurable microwave and millimeter-wave filters. Ph.d. dissertation, School Elect. Comput. Eng., Purdue Univ., West Lafayette, IN, USA, 2016.»
- **Total:** 24 referencias: 20 artículos de revista/congreso (IEEE casi todos, Nature Photonics, PRL, ACM SIGCOMM), 2 libros ([1] Pozar, [23] Steer), 1 tesis doctoral, 1 hoja de datos web. Proporción webs/documentación: 1/24 (4 %). Sin normas, sin manuales de software citados (ADS y MATLAB se describen sin referencia).
- **Concentración:** 22 llamadas en el cuerpo: cap. 1 = 8 (estado del arte, cubre [1]–[17]), cap. 2 = 12 ([17] ×5, [18] ×2, [19], [20], [21], [22], [23]), cap. 5 = 1 ([24]), caps. 3, 4, 6 y 7 = 0. Todo el trabajo gira en torno al artículo [17] (citado ≥8 veces, base de los objetivos: «tomando como referencia los datos y resultados del artículo [17]»).
- Defectos: meses inconsistentes («Aug 2013», «04 2017», «02 1965»), guiones de páginas con espacios («15 – 27»), entrada [4] sin revista, acentos de autores españoles desiguales («Melcón» vs «Gomez-Diaz»).

## J. Registro y redacción

- **Persona y voz:** base impersonal con «se» («se ha desarrollado», «se muestra», «se observa»; 42 «se ha» + 14 «se han» en el cuerpo), **mezclada sin pudor con la primera persona del plural**: «hemos» 23 veces, «vamos a» 11, «nuestro/a(s)» 37, «podemos» 15 («vamos a sentar la base», «Tal y como ya hemos comentado», «nuestro filtro aislante propuesto», «Hemos conseguido lograr una muy alta directividad»). Tercera persona «el autor» 3 veces, solo en el cap. 6 («cuyo autor valora como muy satisfactorio», «el autor define que el éxito…»). Primera persona del singular únicamente en Agradecimientos y en 6.3 («deseo resaltar», «me siento muy orgulloso»). Nunca «yo».
- **Tiempos por capítulo:** cap. 1 presente + futuro de planificación («El trabajo se llevará a cabo en las siguientes fases», «Se desarrollarán códigos»), descripción de la memoria en presente («se presenta», «aborda», «cubre»); cap. 2 presente atemporal («se define», «se obtiene», «permite»); cap. 3 presente y futuro de anuncio («se describirá», «comenzaremos», «pasamos a») + perfecto compuesto para lo construido («hemos creado un nuevo componente en ADS», «nos hemos basado en el esquemático»); cap. 4 presente de lectura de figuras («se observa», «muestra», «revela») + perfecto compuesto para logros («se ha logrado», «hemos mejorado»); cap. 5 pretérito indefinido para la sesión de medida («se generó una señal cosenoidal de 2 Vpp», «se observó cierta reciprocidad», «El experimento constó de una serie de pasos»); cap. 6 perfecto compuesto («Este trabajo ha demostrado», «se ha validado»); cap. 7 perfecto y presente.
- **Longitud:** 391 párrafos de cuerpo (>200 caracteres); media 81 palabras y mediana 69 por párrafo; 5,3 frases por párrafo de media (mediana 3): conviven párrafos de 3 frases con bloques de 300+ palabras (explicaciones de código en el cap. 3, PDF 70). Frases de ~15 palabras de media, pero con mucha subordinación («…, lo que indica que…», «…, es decir, …»).
- **Listas:** ≈15 en 116 páginas de cuerpo; viñetas (itemize, sangría ancha, cada ítem es una o varias frases completas con punto final) para objetivos específicos (3 ítems, PDF 31), características de un BPF (8 ítems con etiqueta y dos puntos, PDF 36–37), parámetros S (4, PDF 45), definiciones «donde:» (PDF 44, 50), partes de la sección 2.4 (4, PDF 56–57), pasos del flujo MATLAB (7 con etiqueta, PDF 68–69), variables del bucle (PDF 71–72), funcionalidades de ADS (4, PDF 82), puertos (2, PDF 83), valores del prototipo (PDF 125), ventajas/inconvenientes por señal (6, PDF 121–122) y líneas futuras (7 con etiqueta, PDF 136). Listas **numeradas** (enumerate) solo para secuencias: fases del trabajo (4, PDF 32) y pasos del experimento (4, PDF 128–129). Nunca listas anidadas; nunca listas para argumentar; la descripción de la memoria (1.4) va en prosa, no en lista.
- **Negrita/cursiva:** no determinable con certeza desde el texto. Inferencias: las etiquetas de ítem seguidas de dos puntos («Frecuencia central (f0):», «Parámetros iniciales a ajustar:», «Ampliación de las modulaciones temporales estudiadas:») y el título dentro del informe van probablemente en negrita; los nombres de variables en monoespaciada; no hay indicios de negrita en el cuerpo de los párrafos.
- **Anglicismos y siglas:** siglas definidas al primer uso con desarrollo (casi siempre en inglés entre paréntesis o a la inversa): «filtro de paso de banda (BPF)», «Advanced Design System (ADS)», «circuitos LTV (Linear Time-Varying)», «modulación espacio-temporal (STM)», «filtro pasa banda (BPF, por sus siglas en inglés)», y lista de acrónimos al principio; varias siglas se redefinen más de una vez (ADS, BPF, LTV). Anglicismos sin marcar ni traducir: «full-duplex», «layout», «setup», «delay», «scripts», «software», «maximally flat», «ripple» (este con traducción: «ondulación en la banda de paso (Ripple)»). Terminología técnica en español («pérdida de inserción», «aislamiento inverso», «directividad», «inversor de admitancia»), con americanismos («capacitor», «voltaje» alternando con «condensador», «tensión»).
- **Nivel de detalle técnico:** alto; marco teórico con derivaciones completas; implementación explicada parámetro a parámetro; resultados con cifras concretas (IL, ancho de banda, aislamiento, directividad) para cada configuración.
- **Objetivos:** objetivo principal en un párrafo («El propósito principal es analizar diversas técnicas de modulación, extendiendo así el rango de señales consideradas más allá de las formas de onda sinusoidales convencionales…») + «Adicionalmente, se han establecido una serie de objetivos específicos que deben cumplirse para la realización exitosa del proyecto:» + 3 viñetas en infinitivo («Establecer una base confiable…», «Modificar tanto el programa como el esquemático…», «Implementar un circuito real y evaluar su comportamiento…») (PDF 31). **Fases:** lista numerada 1–4 con etiqueta + descripción de 3–6 líneas (PDF 32). **Requisitos:** no hay apartado de requisitos (no es un TFG de software).
- **Resultados:** cifra + interpretación en la misma frase: «El filtro muestra una frecuencia central de 1GHz y una pérdida mínima de inserción de 1dB, lo que indica una transmisión eficiente de la señal a través del filtro con muy poca atenuación. Además, el ancho de banda de 3dB es de aproximadamente 200MHz, lo que proporciona una capacidad significativa para transmitir señales dentro de esta banda. El aislamiento invserso del filtro es mejor que 25dB, lo que significa que…» (PDF 105). Siempre se cierra con la coincidencia MATLAB/ADS como validación.
- **Limitaciones:** explícitas y honestas, en el propio capítulo y repetidas en conclusiones: «Debido a esta alta variabilidad, estos resultados no pueden considerarse válidos.» (PDF 129); «aunque se ha intentado medir el correcto funcionamiento del circuito, la falta de tiempo y recursos impidió realizar una validación exhaustiva» (PDF 130); «la falta de recursos y tiempo ha provocado que la medición de resultados no pueda considerarse como válida» (PDF 135); también limitaciones de herramienta: «ADS no es capaz de simular el circuito correspondiente bajo estas condiciones, debido a la complejidad y la riqueza espectral de la señal» (PDF 115).
- **Frases típicas de apertura y cierre (literales):**
  1. «El propósito principal del presente capítulo es proporcionar una visión genérica de los aspectos más relevantes de este trabajo de fin de grado.» (PDF 27)
  2. «Antes de comenzar con el análisis de circuitos variables en el tiempo, que es el tema que nos ocupa en el presente trabajo, vamos a sentar la base de la teoría y práctica moderna de los filtros BPF (Band Pass Filter) cotidianos.» (PDF 36)
  3. «En la presente sección, se profundiza en el estudio y análisis de los resonadores y filtros que varían en el tiempo, extendiendo y aplicando los conceptos y técnicas desarrolladas previamente en el análisis de circuitos LTV (Linear Time-Varying).» (PDF 56)
  4. «En este apartado se detallarán cada uno de los componentes utilizados para el diseño y simulación de los diferentes circuitos a implementar.» (PDF 83)
  5. «En esta sección se presentarán y compararán los resultados de las simulaciones realizadas utilizando MATLAB y ADS…» (PDF 93)
  6. «Para concluir con el estudio de las señales no senoidales propuestas, es necesario analizar las numerosas aplicaciones que se encuentran al utilizar una señal moduladora cuadrada.» (PDF 115)
  7. «A modo de conclusión, el presente capítulo ha subrayado la importancia de explorar modulaciones alternativas y su impacto en el rendimiento de los filtros BPF aislante…» (PDF 123)
  8. «Tras haber expuesto los aspectos más relevantes del trabajo, en este apartado se presentan las conclusiones obtenidas durante su desarrollo.» (PDF 133)
- **Conectores frecuentes:** «Tal y como (ya) hemos comentado», «Cabe destacar que», «Es importante destacar/resaltar/señalar que», «Como podemos ver/observar», «A continuación,», «Posteriormente,», «Por último,», «Asimismo,», «Además,», «Sin embargo,», «En cambio,», «De esta forma,», «En resumen,», «Por lo tanto,», «Es decir,», «En otras palabras,», «En este contexto,», «Una vez [participio]…», «Llegados a este punto,», «Pasamos ahora a…», «Destacar por último que…» (infinitivo suelto como conector, uso coloquial).

**Tres párrafos representativos, literales:**

*Diseño/arquitectura (3.2.1.5, PDF 87):*
> «Para asignar los valores adecuados a los elementos reactivos, se ha utilizado la relación J = 1/K, donde J es la admitancia característica del inversor. Esta relación permite definir de manera precisa las propiedades de inversión del componente. Los valores de los elementos reactivos se han configurado para que las impedancias en las ramas del circuito sean ±j/J, asegurando así el comportamiento deseado del inversor. Esto ya fue comentado en el apartado teórico correspondiente, pero es conveniente recordarlo.
> La implementación en ADS se ha llevado a cabo utilizando componentes de ecuaciones de parámetros Z (Z1P Eqn). Estos componentes permiten definir las impedancias en las ramas del circuito mediante ecuaciones específicas. Para las ramas laterales, se ha configurado la ecuación Z[1, 1] = −j/J, mientras que para la rama central se ha utilizado Z[1, 1] = j/J.»

*Resultados/evaluación (4.1, PDF 105):*
> «Tras realizar los estudios numéricos detallados, se han identificado los valores óptimos para los parámetros de modulación del filtro STM de tres polos. Estos valores son fm = 0.15f0, ξ = 0.27, y φ = 45◦. Estos parámetros han sido seleccionados para maximizar la aislación y garantizar un rendimiento óptimo del filtro, equilibrando la pérdida de inserción y la calidad de la señal. Las gráficas en la cuarta columna de la figura 4.6 presentan las respuestas del filtro STM de tres polos con los parámetros de modulación óptimos. El filtro muestra una frecuencia central de 1GHz y una pérdida mínima de inserción de 1dB, lo que indica una transmisión eficiente de la señal a través del filtro con muy poca atenuación. Además, el ancho de banda de 3dB es de aproximadamente 200MHz, lo que proporciona una capacidad significativa para transmitir señales dentro de esta banda. El aislamiento invserso del filtro es mejor que 25dB, lo que significa que el filtro es muy eficaz para evitar que las señales no deseadas se reflejen de vuelta al sistema. Esto es crucial para aplicaciones donde la interferencia y el ruido deben minimizarse para mantener la calidad de la señal. Además, la pérdida de retorno a lo largo de la banda de paso es mejor que 15dB, lo que indica que el filtro refleja muy poca señal hacia la fuente, permitiendo una transmisión limpia y eficiente.»

*Conclusiones (6.1.1, PDF 133):*
> «Este trabajo ha demostrado la no reciprocidad en la frecuencia portadora, obteniendo excelentes características de baja pérdida de inserción y alto aislamiento inverso. Por primera vez, se ha validado esta teoría utilizando señales periódicas que no son sinusoidales, específicamente ondas triangulares y cuadradas. Estas señales no solo confirmaron la teoría, sino que también mejoraron las prestaciones obtenidas con ondas sinusoidales. Este avance es de gran importancia ya que abre nuevas posibilidades en el diseño y aplicación de estos circuitos, permitiendo explorar modulaciones que ofrecen mejores resultados.»

## K. Capítulo a capítulo

**Cap. 1. Introducción y visión general (PDF 27–34; págs. 3–10; ≈3000 palabras; 1 figura; 0 tablas).** Propósito: contexto, estado del arte, objetivos, fases, herramientas y mapa de la memoria. 1.1 describe el trabajo y sitúa la «modalidad»; 1.2 estado del arte histórico (ferritas → dispositivos activos → modulación temporal → «filtros aisladores» [16], [17]) y aplicaciones (full-duplex, radar/defensa, IRM), cerrando con «En conclusión, la no-reciprocidad… es un campo de investigación activo»; 1.3.1 objetivo general + 3 específicos en viñetas; 1.3.2 cuatro fases numeradas; 1.3.3 herramientas software (MSI, Windows 11, Matlab 2024a, ADS de Keysight) y hardware (varactores, VNA Rohde&Schwarz ZNH26, generador GF-657 Promax, osciloscopio Promax, analizador R&S FSH20); 1.4 descripción de la memoria capítulo a capítulo en prosa, con párrafo final de «contribución significativa». Bien: estado del arte con citas agrupadas y progresión histórica clara; fases y herramientas concretas. Mal: desliz de titulación («Ingeniería de Sistemas de Telecomunicación»), comillas incorrectas, autoelogio en el cierre, repetición de las mismas ideas de 1.1 en 1.4.

**Cap. 2. Marco Teórico (PDF 35–65; págs. 11–41; ≈11 200 palabras; 10 figuras; 60 ecuaciones; 0 tablas).** 2.1 BPF pasivos: definición, lista de 8 características (f0, BW, 3 dB, rizado, IL, selectividad, Q con la ecuación (2.1), rechazo), simetría/reciprocidad, repaso histórico con [18]–[21]. 2.2 circuitos LTV: método del dominio espectral (condensador modulado, índice ξ, matriz de frecuencias, matriz de admitancia espectral YC, asimetría YC(−1,0) ≠ YC(0,−1) → base de la no reciprocidad) y parámetros S multimodo (derivación completa 2.14–2.32). 2.3 señales periódicas: cosenoidal (Fourier, Euler, estructura de la matriz), triangular (2.41–2.44) y cuadrada (2.45–2.48), con espectros en figuras 2.4–2.6. 2.4 resonador LC modulado, inversores de admitancia (red en T), filtro de dos polos (cascada ABCD, 2.54–2.58), filtro tripolar (2.59–2.60), convergencia numérica (truncado (2n+1)×(2n+1)). Cada subapartado cierra con «En resumen». Bien: ecuaciones numeradas, referenciadas y con símbolos definidos; figuras de topología junto a la teoría; la extensión a señales no sinusoidales es aportación propia bien delimitada. Mal: muy largo y redundante (frases de relleno «Esta sección proporciona una visión integral…»), matrices gigantes de página entera, dependencia casi total de [17] para 2.2 y 2.4, erratas («repsectivamente», «funadamental», «moduladon»).

**Cap. 3. Implementación de circuitos en MATLAB y ADS (PDF 67–92; págs. 43–68; ≈8500 palabras incl. código; 11 figuras; 8 códigos; 4 ecuaciones).** 3.1 flujo de trabajo (figura 3.1 + 7 pasos en viñetas con etiqueta) y código por bloques: parámetros (3.1), inicialización (3.2), bucle de parámetros S (3.3), representación (3.4), rellenos triangular/cuadrada (3.5, 3.6), resonador (3.7), filtro de dos etapas (3.8); cada bloque explicado en prosa variable a variable. 3.2 ADS: funcionalidades (viñetas), componentes uno a uno (puertos P_1Tone/Term_G, fuentes V_1Tone/Vf_Triangle/Vf_Square, NonlinC con polinomio de coeficientes, inductor L, inversor de admitancia creado ad hoc con Z1P_Eqn, simuladores LSSP y TRAN con sus parámetros), modelos circuitales, conversión desfase→retardo con las ecuaciones (3.3)–(3.4), y validación MATLAB vs ADS (figuras 3.10–3.11 al final del capítulo). Bien: reproducible, explica cada parámetro de ADS (cosa que el texto presume que no estaba documentada); figuras de componentes. Mal: prosa que parafrasea el código línea a línea (párrafos de 300+ palabras), acentos rotos en los comentarios de los listados, figuras expulsadas al final, autoelogio («subraya la originalidad y la innovación de nuestro trabajo», PDF 82), erratas («conluir», «validex», «corrobar»).

**Cap. 4. Simulación de circuitos en MATLAB y ADS (PDF 93–123; págs. 69–99; ≈11 100 palabras; 15 figuras; 0 tablas).** Es el capítulo de resultados. Misma plantilla para cada señal (4.1 cosenoidal, 4.2 triangular, 4.3 cuadrada): (i) condensador único → no reciprocidad entre armónicos (figuras tituladas «Resultados de las mediciones», aunque son simulaciones); (ii) resonador frente a RS/RL; (iii) filtro de dos polos: respuesta estática (Chebyshev 0.043 dB, 150 MHz) + estudio paramétrico fm, ξ, ∆ϕ en mapa 4×4 + valores nominales; (iv) filtro tripolar: estática + paramétrico + prestaciones (IL, BW 3 dB, aislamiento, retorno); (v) coincidencia MATLAB/ADS como validación. Cierre con lista de ventajas/inconvenientes por señal, «En resumen», anuncio del cap. 5 y «A modo de conclusión». Bien: resultados cuantificados e interpretados, comparación sistemática entre señales con la misma base estática, reconocimiento de límites de ADS. Mal: ni una tabla resumen (cifras dispersas en prosa), pies de figura de 15 líneas, títulos de figura equívocos («mediciones»), inconsistencias numéricas (ξ = 0.15 en el texto PDF 98 frente a 0.25 en el pie), repetición de explicaciones cualitativas ya dadas en el cap. 2.

**Cap. 5. Diseño e implementación real (PDF 125–131; págs. 101–107; ≈1750 palabras; 6 figuras; 0 tablas).** Prototipo de una sola etapa (50 Ω, 0.6 nF, 2.2 nH, varactor SMV1234 [24], decenas de MHz por falta de generadores), esquemático ADS (5.1), layout 2D/3D (5.2), simulación (5.3), foto del circuito fabricado (5.4), banco de medida (5.5), protocolo en lista numerada de 4 pasos, medidas (cosenoidal 2 Vpp a 5 MHz, RF a 15 MHz; armónicos en torno a −90 dBm con diferencias de 1–2 dBm), diagnóstico (generador en barrido, piezas desoldadas) y conclusión honesta de que los resultados no son válidos, más propuesta de prototipo de tres etapas. Bien: honestidad, fotos, protocolo paso a paso. Mal: corto, sin tabla de componentes ni valores medidos, sin figura comparativa medida/simulación.

**Cap. 6. Conclusión (PDF 133–138; págs. 109–114; ≈2400 palabras; 0 figuras).** 6.1.1 conclusiones técnicas en tres párrafos (logro principal, ADS como validación «sin información documentada», aplicaciones); 6.1.2 «Seguimiento del trabajo»: recorrido capítulo a capítulo con valoración («El quinto capítulo ha servido como broche final…») y reconocimiento de la limitación del cap. 5; 6.2 líneas futuras: 7 viñetas con etiqueta («Ampliación de las modulaciones temporales estudiadas:», «Materiales y tecnología de fabricación:», …); 6.3 «Conclusiones finales» personales: tutores, carrera, redacción de la memoria, reflexión sobre el éxito y la felicidad, cita de Albert Schweitzer. Bien: líneas futuras concretas; seguimiento útil para el tribunal. Mal: afirmaciones no probadas («Por primera vez», «en internet no existe ninguna información documentada»), 6.3 demasiado emocional y largo para una memoria técnica, comillas rotas en la cita.

**Cap. 7. Recursos, costes y planificación (PDF 139–142; págs. 115–118; ≈875 palabras; 2 cuadros).** Existe y va **después** de las conclusiones, como último capítulo antes de la bibliografía. Contenido: 7.1 recursos humanos (alumno 500 h a 25 €/h; dos tutores ≈100 h cada uno a 55 €/h; «El coste total asciende a unos 19100€»); 7.2 hardware (MSI Pulse GL66, Windows 11, i7-12700U, 32 GB RAM, 1 TB, 2100 €) y software (MATLAB 900 €/año, ADS 20000 €/año, Overleaf gratuito; licencias gratuitas para estudiantes UGR); 7.3 [título erróneo] fabricación (10 €, material del grupo) y medida en laboratorio (240 € = 80 €/h × 3 h); 7.4 remite al cuadro 7.1 (TOTAL 46750 €); 7.5 Gantt (cuadro 7.2, 10 tareas, quincenas, febrero–junio 2024). Errores: epígrafe 7.3 duplicado, incoherencia texto/cuadro (19100 € frente a 12500 + 11000 = 23500 €), página 142 casi vacía. Patrón útil: justificar el capítulo («la realización de un Trabajo de Fin de Grado generalmente no implica gastos directos. Sin embargo, … es útil estimar el coste total que implicaría llevar a cabo un proyecto similar en un entorno profesional»).

## L. Particularidades UGR/ETSIIT observadas

- Portada con la secuencia «TRABAJO FIN DE GRADO» (sin «de») → titulación en mayúsculas → título → subtítulo → «Autor» → nombre → «Directores» → nombres → nombre completo de la Escuela → «Granada, Junio de 2024» (mes con mayúscula inicial). No figura «Universidad de Granada» como texto en portada (probablemente logo). Segunda portada idéntica sin cabecera ni fecha.
- Orden de preliminares: portada, segunda portada, resumen/palabras clave (ES), abstract/keywords (EN), informe de los directores, agradecimientos, acrónimos, índice general, índice de figuras, índice de códigos, portadilla de Parte I. Cada bloque en página impar con verso en blanco.
- Fórmula oficial del informe de los directores: «D. [Nombre] (tutor1), Profesor del Área de … del Departamento … de la Universidad de Granada. […] Informan: Que el presente trabajo, titulado …, ha sido realizado bajo su supervisión por [alumno] (alumno), y autorizamos la defensa de dicho trabajo ante el tribunal que corresponda. Y para que conste, expiden y firman el presente informe en Granada a 24 de Junio de 2024. Los directores:». Única mención al tribunal en todo el documento. Marcadores de plantilla sin borrar.
- Tutores nombrados como «Directores» en portada, «tutor1/tutor2» en el informe, «tutores» en agradecimientos y «tutor del proyecto»/«cotutor» en 6.3 (PDF 137: «El Dr. Carlos Molero Jiménez, tutor del proyecto, y el Dr. Mario Pérez Escribano, cotutor del mismo»).
- Departamento escrito como «Departamento Teoría de la Señal, Telemática y Comunicaciones» (sin «de»).
- No aparecen: DNI, declaración de originalidad, autorización de depósito en biblioteca, firma del alumno, fecha de defensa, convocatoria.
- El resumen va precedido del título completo y del nombre del autor, y las palabras clave van **antes** del resumen (igual en el abstract).
- El texto menciona la «modalidad» del trabajo (PDF 27) y los medios del grupo de investigación (material de fabricación, laboratorio a 80 €/h).

## M. Cifras globales

- Páginas PDF: 150 (16 en blanco). Preliminares: PDF 1–26 (26 págs., 9 en blanco). Cuerpo: PDF 27–142 (116 págs., 3 en blanco + 1 casi vacía). Parte II + bibliografía: PDF 143–147 (5 págs., 1 en blanco). Finales en blanco: 148–150.
- Páginas impresas: i–xi (preliminares numerados), 1–118 (cuerpo), 119–123 (Parte II y bibliografía).
- Figuras: 43. Cuadros: 2. Ecuaciones numeradas: 64. Listados: 8. Referencias: 24. Llamadas a cita en el cuerpo: 22 (+1 en pie de figura). Acrónimos: 10. Notas al pie: 0. Anexos: 0.
- Palabras (pdftotext, `wc -w`; incluyen cabeceras, pies e índices): total ≈ 44 800. Preliminares ≈ 5400 (unas 3000 son el índice de figuras por sus pies kilométricos). Cap. 1 ≈ 3000; cap. 2 ≈ 11 200; cap. 3 ≈ 8500 (con código); cap. 4 ≈ 11 100; cap. 5 ≈ 1750; cap. 6 ≈ 2400; cap. 7 ≈ 875; Parte II + bibliografía ≈ 570. Cuerpo ≈ 38 800. Reparto: teoría (cap. 2) 29 %, implementación (cap. 3) 22 %, resultados (cap. 4) 29 %, prototipo 4,5 %, conclusiones 6 %, costes 2 %, introducción 8 %.
- Párrafos: 391 párrafos de cuerpo; 81 palabras de media (mediana 69); 5,3 frases/párrafo (mediana 3); ≈15 palabras/frase.
- Partición de palabras: 375 de 3472 líneas del cuerpo acaban en guion (≈11 %).

## N. Lecciones transferibles

**Reglas para parecerse a esta memoria (formato, estructura y redacción):**

1. **Maquetación de libro LaTeX a doble cara** (plantilla ETSIIT): capítulos que abren en página impar con verso en blanco, cabecera par «nº  X.Y. Título de sección» e impar «Título del capítulo  nº», paginación romana en preliminares y arábiga desde la portadilla «Parte I. Desarrollo del trabajo»; la bibliografía va en su propia «Parte II».
2. **Preliminares en este orden exacto:** portada (TRABAJO FIN DE GRADO / titulación en mayúsculas / título / subtítulo / Autor / Directores / Escuela / Granada, Mes de Año) → segunda portada → resumen con título, autor, «Palabras clave:» alfabéticas y tres párrafos → abstract con la misma estructura → informe de los directores con la fórmula «Informan: Que el presente trabajo, titulado …, ha sido realizado bajo su supervisión por …, y autorizamos la defensa de dicho trabajo ante el tribunal que corresponda. Y para que conste, expiden y firman el presente informe en Granada a DD de Mes de AAAA. Los directores:» → agradecimientos (con la dedicatoria dentro) → acrónimos → índice general → índice de figuras → índice de códigos/tablas.
3. **Cada capítulo abre con «Capítulo N» + título en línea aparte, caja «Contenido» con su mini-índice y un párrafo introductorio sin epígrafe** (3–6 líneas: qué se va a hacer y por qué), y cierra con un párrafo marcado («En resumen,», «Como resumen del apartado X,», «A modo de conclusión,») que anuncia además el siguiente capítulo.
4. **Capítulo 1 con cuatro bloques fijos:** descripción del trabajo; estado del arte con citas agrupadas por rangos ([1–5]) y progresión histórica; objetivos (general en párrafo + específicos en viñetas con infinitivo) y fases (lista numerada con etiqueta) y herramientas software/hardware con modelos concretos; descripción de la memoria en prosa capítulo a capítulo.
5. **Numeración homogénea por capítulo:** epígrafes «X.Y.» / «X.Y.Z.» con punto tras el número (cuarto nivel solo en el mini-índice); pies «Figura X.Y: Texto.» y «Código X.Y: Texto.» con dos puntos y punto final debajo del objeto; «Cuadro X.Y: Texto» debajo de la tabla; ecuaciones con «(X.Y)» a la derecha y numeradas todas, incluidas las triviales; subfiguras (a)…(ñ)…(o).
6. **Todo objeto se cita en el texto en minúscula y sin paréntesis en el número** («figura 4.4», «ecuación 2.2», «código 3.3», «cuadro 7.1», «sección 3.2.2», «apartado 2.4»), antes o justo después de aparecer; nunca se deja una figura sin llamada. Los pies de las figuras de resultados incluyen todos los parámetros del experimento para que la figura sea autocontenida.
7. **Ecuaciones con ritual fijo:** frase de entrada («se modela con la expresión», «viene dada por»), ecuación con su puntuación, y «donde …» definiendo cada símbolo (en frase o en lista «donde:»); derivaciones completas en el marco teórico, no solo el resultado.
8. **Registro:** impersonal con «se» como columna vertebral, admitiendo la primera persona del plural de acompañamiento («vamos a», «hemos comentado», «nuestro filtro»), nunca el singular en el cuerpo; presente para teoría y lectura de figuras, pretérito perfecto compuesto para lo realizado, indefinido para la sesión experimental; párrafos de 60–90 palabras y 3–5 frases; conectores de hilo («Tal y como hemos comentado», «Cabe destacar que», «A continuación», «Por último», «En resumen»).
9. **Resultados = cifra + lectura en la misma frase** («una pérdida mínima de inserción de 1dB, lo que indica…»), misma plantilla de análisis para cada caso comparado (estático → paramétrico → nominal → validación), y cada bloque de resultados remata con la validación cruzada (MATLAB frente a ADS) y una lista de ventajas/inconvenientes.
10. **Limitaciones explícitas y sin maquillaje** en el capítulo donde surgen («estos resultados no pueden considerarse válidos debido a…»), repetidas en el «seguimiento del trabajo» de las conclusiones, con causa y remedio propuesto.
11. **Conclusiones en tres piezas:** conclusiones técnicas (3–4 párrafos), «seguimiento del trabajo» (recorrido capítulo a capítulo), «líneas futuras» en viñetas con etiqueta en negrita; cierre personal opcional y breve.
12. **Capítulo final «Recursos, costes y planificación»** (después de conclusiones, antes de la bibliografía): recursos humanos (horas × €/h del alumno como ingeniero técnico y de los tutores como ingeniero superior), hardware y software con precios de licencia reales aunque la UGR los ceda, fabricación/medida, un cuadro resumen con TOTAL y el Gantt como cuadro por quincenas con ~10 tareas; justificar el capítulo con la frase de que un TFG no tiene gastos directos pero se estima el coste profesional.
13. **Bibliografía numérica por orden de aparición** (BibTeX `unsrt`), revistas con nombre completo, «volumen(número):páginas, año», webs con «Accessed: AAAA-MM-DD»; citas concentradas en introducción y marco teórico, y en implementación/resultados solo hojas de datos.

**Cosas que NO aparecen en este TFG (y por tanto no hay que meter):**
- Emojis, markdown, viñetas anidadas, listas para argumentar, cuadros-resumen por capítulo, títulos en forma de pregunta.
- Negritas dentro de los párrafos (a lo sumo etiquetas de ítem), cursivas marcando anglicismos (los anglicismos van sin marcar), comillas para nombres de variables.
- Notas al pie, URLs en el cuerpo, «Fuente: elaboración propia», índice de tablas, glosario extenso, anexos, listado de requisitos, capturas de terminal, tablas de código largas, números de línea en listados.
- Tablas de resultados en el capítulo de resultados (todo en prosa + figuras), comparativas con otros trabajos en tabla.
- Primera persona del singular en el cuerpo; «yo» nunca.
- Declaración de originalidad, DNI, firma del alumno, fecha de defensa.

**Errores detectados que conviene evitar:**
- Marcadores de plantilla sin eliminar: «(tutor1)», «(tutor2)», «(alumno)», raya «—» suelta en la portada, página 2 con solo un «3».
- Título distinto en portada («Giga Hercios») e informe/1.4 («Giga Hertzios»); titulación errónea en 1.1 («Ingeniería de Sistemas de Telecomunicación»).
- Epígrafe 7.3 con el mismo título que 7.2; índice que manda «Bibliografía» a la pág. 123 en vez de 121; cifras incoherentes entre texto (19100 €) y cuadro (23500 € de personal).
- Pies de figura equívocos («Resultados de las mediciones» para simulaciones); valores del texto que no coinciden con los del pie (ξ = 0.15 frente a 0.25).
- Comillas LaTeX mal compuestas («”estudio…”», «¨ınstantánea”», «.El éxito … deseas..»); acentos rotos en comentarios de código.
- Erratas abundantes («conluir», «validex», «corrobar», «refelxión», «repsectivamente», «especiotemporal», «Modulationl», «eperimental», «aislación», «invserso», «casp»); mezcla «figura/Figura», «cuadro/tabla», «ϕ/φ», «condensador/capacitor», «tensión/voltaje»; unidades pegadas («1GHz») y separadas («50 Ω») sin criterio.
- Página casi vacía con cabecera (PDF 142) y figuras empujadas al final del capítulo (PDF 92): controlar los flotantes.
- Autoelogio sin prueba («contribución significativa», «Por primera vez», «no existe ninguna información documentada», «las características de no reciprocidad logradas son impresionantes») y cierre emocional con cita motivacional.
- Párrafos de 300+ palabras que parafrasean el código línea a línea; redefinir siglas (ADS, BPF, LTV) varias veces; repetir en el cap. 4 explicaciones cualitativas ya dadas en el cap. 2.

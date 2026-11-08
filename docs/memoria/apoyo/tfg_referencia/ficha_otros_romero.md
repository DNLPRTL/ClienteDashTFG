# Ficha de formato y estilo — TFG Antonio Romero Espigares (ETSIIT-UGR, septiembre 2025)

Fichero analizado: `docs/memoria/DE OTROS TUTORES PERO RECIENTES DE MI FACULTAD/TFG Antonio Romero Espigares.pdf`
(187 páginas en el PDF, 67 311 palabras según `pdftotext`, 268 MB por las imágenes).

Método: texto extraído entero con `pdftotext -enc UTF-8` (flujo y `-layout`), leído de principio a fin;
páginas concretas comprobadas en layout (portada, licencia, resumen, índices, pies, ecuaciones,
bibliografía, anexos). Los metadatos del PDF (Producer/Creator) no se pudieron leer (sin `pdfinfo`/`pdffonts`
ni pypdf en el entorno), así que la herramienta de maquetación se infiere del texto.

**Convención de páginas.** Se cita la página del PDF. La numeración impresa va 5 por delante
(PDF p. 22 = impresa 27; PDF p. 134 = impresa 139) porque al PDF le faltan 5 páginas de los
preliminares (las dos autorizaciones y sus blancos, ver B). Cuando importa, se da también la impresa.

---

## A. Identificación

| Campo | Dato (literal cuando se indica) | Dónde |
|---|---|---|
| Título | «Diseño e implementación de un contador Geiger-Müller para la detección de radiación ionizante» | portada (PDF p. 1) |
| Variante del título en pies de página impares | «Diseño e implementación de un contador Geiger-Müller **portátil** para la detección de radiación ionizante» | p. 24, 28, 31… (incoherencia: el pie de las páginas impares añade «portátil»; el de las páginas de apertura de capítulo y preliminares no) |
| Autor | «Autor / Antonio Romero Espigares» | p. 1 |
| Tutor | «Director / D. Andrés María Roldán Aranda» | p. 1. En la licencia: «Prof. Andrés Roldán Aranda» (p. 2). En los cajetines de esquemáticos: «SUPERVISED BY: PhD. Andrés M. Roldán Aranda» (p. 101) y «Sr. Andrés Roldán Aranda Ternured Professor University of Granada» (pp. 102–112; «Ternured» es errata de Tenured) |
| Departamento | No figura en portada ni en el cuerpo. **Inferencia:** Departamento de Electrónica y Tecnología de Computadores, por el cajetín del esquemático «DEPARTMENT: Electronics and Computer Technology» (p. 101) y por el laboratorio GranaSAT (agradecimientos p. 5, motivación p. 23) |
| Titulación literal | «TRABAJO FIN DE GRADO» / «INGENIERÍA DE TECNOLOGÍAS DE TELECOMUNICACIÓN» (sin la palabra «Grado en») | p. 1. Cajetín: «BACHELOR'S DEGREE IN TELECOMMUNICATION ENGINEERING / ACADEMIC COURSE 2024/2025» (p. 101) |
| Centro literal | «Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación» | p. 1 |
| Universidad | «Universidad de Granada» **no aparece como texto** en la portada (presumiblemente va en logotipo gráfico). Solo «University of Granada» en los cajetines de esquemáticos (11 veces) | p. 102–112 |
| Fecha / curso | «Granada, Septiembre de 2025» (con mayúscula en el mes) | p. 1 |
| Páginas | 187 en el PDF; la numeración impresa llega a 191 + 1 blanca final (192). Faltan 5 páginas de preliminares | — |
| Licencia | Página 2 entera dedicada a «© 2025 by Antonio Romero Espigares y Prof. Andrés Roldán Aranda» + resumen humano de la licencia CC BY-SA 4.0 en inglés | p. 2 |
| Herramienta de maquetación | **LaTeX (inferencia fuerte)** | ver evidencias |

Evidencias de LaTeX: cabecera de capítulo en dos líneas «Capítulo 1» / «INTRODUCCIÓN» (p. 22); puntos
conductores en los índices; pies «Figura 3.5 – …» con guion largo (paquete *caption* con `labelsep=endash`);
pies «Listado F.1 – …» (paquete *listings* con babel español, que traduce «Listing» por «Listado»);
identificadores del código extraídos con letras espaciadas («i ni tP ow er», «d ra wF as tH L in e»), típico
de *listings* con `columns=flexible`; referencia rota «Librería spi1.c ??» (p. 72); términos del glosario
insertados automáticamente con mayúscula en mitad de frase («detección de Radiación ionizante mediante
Tubo Geiger-Müller», p. 26) y huecos de `\gls` indefinidos («compatibilidad directa con la mediante formato
Arduino Shield», p. 45; «se sigue el estándar -315», p. 31; «GPIO, , SPI», p. 24) = paquete *glossaries*;
puntos dobles al final de cada entrada del glosario («…conmutación rápida..», p. 17) = descripción con punto
+ punto automático; numeración de párrafos «3.2.8.0.1» (p. 58) = `\paragraph` bajo una `\subsection` sin
`\subsubsection`; bibliografía con «url:» en minúscula y orden alfabético = *biblatex*; dígitos sueltos
«1», «2», «3»… en el margen de cada página = pestañas laterales (thumb index) del número de capítulo;
vídeos embebidos «(Para reproducir video hacer doble click sobre el simbolo superior)» = paquete *media9*
o similar. Es, con toda probabilidad, la plantilla LaTeX del grupo GranaSAT del tutor.

---

## B. Estructura completa en orden

| Bloque | PDF | Impresa | Observaciones |
|---|---|---|---|
| Portada | 1 | 1 | Ver L |
| Página de copyright + licencia CC BY-SA 4.0 (en inglés) | 2 | 2–3 | Hace de «segunda portada» |
| Autorización de defensa (informe del tutor) | **ausente** | 4 | El índice la lista: «Autorización de defensa 4». No está en el PDF |
| Autorización de depósito en biblioteca | **ausente** | 6 | El índice la lista: «Autorización de depósito en biblioteca 6». No está en el PDF |
| Resumen + palabras clave (español) | 3 | 8 | Una página |
| Abstract + keywords (inglés) | 4 | 9 | Una página |
| Dedicatoria | — | — | **No hay** |
| Agradecimientos | 5 | 10 | Una página |
| Índice general | 6–12 | 11–17 | 7 páginas (profundidad hasta 5 niveles) |
| Lista de figuras («Ĺista de figuras», inicial decorada) | 13–15 | 18–20 | |
| Lista de tablas («Ĺista de Tablas») | 16 | 21 | |
| Índice de listados | — | — | **No hay**, pese a 18 listados en el anexo F |
| Glosario | 17–20 | 22–25 | 56 términos con definición larga |
| Siglas | 21 | 26 | 9 siglas |
| Capítulo 1. INTRODUCCIÓN | 22–25 | 27–30 | |
| Capítulo 2. ESTADO DEL ARTE | 26–29 | 31–34 | |
| Capítulo 3. DISEÑO DEL SISTEMA | 30–79 | 35–84 | 50 páginas: 69 % del cuerpo |
| Capítulo 4. FABRICACIÓN Y ENSAMBLAJE | 80–91 | 85–96 | |
| Capítulo 5. CONCLUSIONES | 92–93 | 97–98 | |
| Bibliografía | 94–97 | 99–102 | 69 entradas |
| Apéndice A. Coste del proyecto | 98–99 | 103–104 | |
| Apéndice B. Esquemáticos | 100–123 | 105–128 | 12 hojas Altium propias + 6 hojas EVAL-ADICUP3029 + 3 hojas CN0536 (PDF incrustados, apaisados) |
| Apéndice C. PCB | 124–126 | 129–131 | Vistas top/bottom |
| Apéndice D. Módelos 3D (sic) | 127–130 | 132–135 | 6 renders |
| Apéndice E. Simulaciones | 131–133 | 136–138 | LTspice |
| Apéndice F. Códigos | 134–186 | 139–191 | 53 páginas de código |
| Página en blanco final | 187 | 192 | |

Faltan respecto a lo habitual en la UGR: dedicatoria, índice de listados, las dos autorizaciones (en
este fichero), y no hay página de «Declaración de originalidad» separada. No hay capítulo de
«Presupuesto»/«Planificación» como tal: el cronograma va en 1.5 y los costes en el apéndice A.

### Textos literales de páginas oficiales

**Autorizaciones (defensa y depósito):** no reproducibles: las páginas 4 y 6 impresas no están en el
PDF. Solo consta su título en el índice general (PDF p. 6): «Autorización de defensa» y «Autorización de
depósito en biblioteca».

**Página de licencia (PDF p. 2), literal:**

> Antonio Romero Espigares, 2025
> © 2025 by Antonio Romero Espigares y Prof. Andrés Roldán Aranda: "Diseño e implementación de un contador Geiger-Müller para la detección de radiación ionizante" This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license.
> This is a human-readable summary of (and not a substitute for) the license: You are free to:
> Share — copy and redistribute the material in any medium or format. Adapt — remix, transform, and build upon the material for any purpose, even commercially.
> The licensor cannot revoke these freedoms as long as you follow the license terms.
> Under the following terms:
> Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
> ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original. No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.
> To view a complete copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/

**Resumen y palabras clave (PDF p. 3), literal:**

> "Diseño e implementación de un contador Geiger-Müller para la detección de radiación ionizante"
> Antonio Romero Espigares
> PALABRAS CLAVE:
> Contador Geiger-Müller, Radiación ionizante, SI-29BG, CrossCore Embedded Studio, Altium Designer, SolidWorks, SquareLine Studio, Electronica, Diseño PCB, LVGL, ILI9488, XPT2046, SPI, EVAL-ADICUP3029, CN0536.
> RESUMEN:
> El presente Trabajo Fin de Grado consiste en el diseño e implementación de un contador Geiger-Müller para la detección de radiación ionizante. El dispositivo integra tanto el hardware de medida como una interfaz de usuario gráfica que permite la visualización en tiempo real de las magnitudes de radiación registradas.
> Para el desarrollo del firmware se ha empleado la placa de desarrollo EVAL-ADICUP3029 de Analog Devices, basada en el microcontrolador ADuCM3029, y el entorno de programación CrossCore Embedded Studio. Durante el proyecto se han realizado múltiples miniproyectos de prueba, con el fin de comprender y controlar los distintos periféricos del microcontrolador (GPIO, SPI, UART, temporizadores, interrupciones, etc.), desarrollando así las librerías necesarias para la construcción del sistema final.
> La interfaz gráfica se ha implementado utilizando la librería de código abierto LVGL, en combinación con la Pantalla TFT ILI9488 y el controlador táctil XPT2046. El diseño de la UI se ha realizado con la herramienta SquareLine Studio, lo que ha permitido crear diferentes ventanas, indicadores y elementos gráficos adaptados al proyecto, posteriormente exportados e integrados en el firmware del sistema.
> En paralelo, se ha trabajado en el diseño electrónico, elaborando un circuito impreso en Altium Designer, el cual no se ha podido fabricar, que integra el módulo de alto voltaje para el Tubo Geiger-Müller, la gestión de alimentación mediante batería recargable y la protección de los diferentes buses de comunicación.
> Asimismo, se ha desarrollado un importante trabajo de diseño mecánico, fabricando en SolidWorks las diferentes piezas del sistema. Dichas piezas se han prototipado en varias iteraciones mediante impresión 3D, ajustando tolerancias, mecanismos de fijación y accesibilidad hasta obtener una versión final optimizada. El montaje completo integra la electrónica, la pantalla, la caja y conectores GX16, garantizando un dispositivo robusto y funcional.
> En definitiva, el proyecto combina diseño electrónico, programación embebida, desarrollo de interfaces gráficas y diseño mecánico, abordando todas las etapas de un ciclo de desarrollo multidisciplinar. El resultado es un prototipo plenamente operativo que permite medir radiación ionizante, visualizar los resultados en tiempo real en una pantalla táctil.

**Abstract y keywords (PDF p. 4), literal:**

> Design and implementation of a Geiger-Müller counter for the detection of ionising radiation
> Antonio Romero Espigares
> KEYWORDS:
> Contador Geiger-Müller, Radiación ionizante, SI-29BG, CrossCore Embedded Studio, Altium Designer, SolidWorks, SquareLine Studio, Electronics,PCB desing, LVGL, ILI9488, XPT2046, SPI, EVAL-ADICUP3029, CN0536.
> ABSTRACT:
> This Final Degree Project consists of the design and implementation of a Geiger-Müller counter for the detection of ionising radiation. The device integrates both the measurement hardware and a graphical user interface that allows real-time visualisation of the recorded radiation levels.
> The firmware was developed using the EVAL-ADICUP3029 development board from Analog Devices, based on the ADuCM3029 microcontroller, and the CrossCore Embedded Studio programming environment. During the project, multiple mini-test projects were carried out in order to understand and control the different peripherals of the microcontroller (GPIO, SPI, UART, timers, interrupts, etc.), thus developing the necessary libraries for the construction of the final system.
> The graphical interface was implemented using the open source library LVGL, in combination with the Pantalla TFT ILI9488 and the touch controller XPT2046. The UI design was created using the SquareLine Studio tool, which allowed us to create different windows, indicators and graphic elements adapted to the project, which were then exported and integrated into the system firmware.
> At the same time, work has been carried out on the electronic design, creating a printed circuit in Altium, which has not yet been manufactured, integrating the high-voltage module for the Geiger tube, rechargeable battery power management and protection for the different communication buses.
> Likewise, significant work has been done on the mechanical design, manufacturing the different parts of the system in Solidworks. These parts have been prototyped in several iterations using 3D printing, adjusting tolerances, fastening mechanisms and accessibility until an optimised final version was obtained. The complete assembly integrates the electronics, screen, box and GX16 connectors, ensuring a robust and functional device.
> In short, the project combines electronic design, embedded programming, graphical interface development and mechanical design, addressing all stages of a multidisciplinary development cycle. The result is a fully operational prototype that allows ionising radiation to be measured and the results to be viewed in real time on a touch screen.

Nota: las keywords inglesas están casi todas en español (copia sin traducir) y «Pantalla TFT» aparece
en español dentro del abstract: rastro del glosario automático. Errores a evitar.

**Agradecimientos (PDF p. 5):** encabezado «Agradecimientos:» (con dos puntos); cinco párrafos cortos
(padres y hermana, novia, amigos de la carrera y «Los del aguante», grupo GranaSAT, cierre «A todos
ellos, gracias por haber contribuido a que este proyecto sea posible.»). Registro personal, primera
persona del singular («quiero expresar mi más profundo agradecimiento»): es el único lugar del documento
con «yo».

---

## C. Índice general copiado literalmente (PDF pp. 6–12; impresas 11–17)

Se reproducen todas las entradas y niveles con su número de página impresa (los puntos conductores
se abrevian con «…»). Se conservan los defectos tal cual («Ĺista», «Módelos», «F.10.Librería» sin espacio,
el 3.2.13 duplicado).

```
Índice general
Autorización de defensa                 4
Autorización de depósito en biblioteca  6
Resumen                                 8
Agradecimientos                         10
Índice general                          11
Ĺista de figuras                        18
Ĺista de Tablas                         21
Glosario                                22
Siglas                                  26
1. INTRODUCCIÓN                         27
1.1. Motivación … 27
1.2. Alcance del TFG … 28
1.3. Metodología de diseño … 28
1.4. Estructura del documento … 29
1.5. Cronograma del proyecto … 30
2. ESTADO DEL ARTE                      31
2.1. Principio de funcionamiento del Tubo Geiger-Müller … 31
2.1.1. Estructura básica … 31
2.1.2. Proceso de detección … 31
2.1.3. Zona de operación … 32
2.1.4. Limitaciones … 32
2.1.5. Aplicaciones … 32
2.2. Soluciones de Analog Devices: CN0536 … 33
2.3. Soluciones comerciales: MadExp HV … 33
2.4. Comparativa y motivación del diseño propio … 33
3. DISEÑO DEL SISTEMA                   35
3.1. Diseño electrónico … 35
3.1.1. Software EDA utilizado … 35
3.1.2. Esquemáticos de circuito … 36
3.1.2.1. Símbolos y nomenclatura … 36
3.1.2.2. Símbolos de circuitos integrados … 36
3.1.2.2.1. Designadores de referencia … 38
3.1.2.3. Redes y nombres de red … 38
3.1.2.4. Diagrama estructural de bloques … 38
3.1.2.5. Sistema de suministro de energía … 39
3.1.2.5.1. Estructura del sistema de suministro de energía … 39
3.1.2.5.2. Power rails … 40
3.1.2.5.3. Monitoreo de batería y corriente … 40
3.1.2.5.4. Carga de baterías de Litio-Ion y Litio-Polímero … 41
3.1.2.5.5. Estimación del consumo energético y autonomía de la batería … 42
3.1.2.6. Comunicación … 43
3.1.2.6.1. Comunicación UART … 43
3.1.2.6.2. Pantalla TFT e interfaz táctil … 44
3.1.2.7. Circuito de encendido con pulsador … 45
3.1.2.8. Almacenamiento … 46
3.1.2.9. Generación de alto voltaje para el tubo Geiger-Müller … 46
3.1.2.10. Circuito de detección de partículas … 47
3.1.3. Diseño de la placa de circuito impreso (PCB) … 48
3.1.3.1. Características generales de la PCB … 48
3.1.3.1.1. Dimensiones, forma y estructura … 48
3.1.3.1.2. Montaje mecánico … 49
3.1.3.1.3. Herramienta de diseño … 49
3.1.3.1.4. Tecnología de montaje y componentes … 49
3.1.3.1.5. Distribución funcional y conectividad … 49
3.1.3.1.6. Vistas de la placa … 49
3.1.4. Uso de la placa CN0536 como solución provisional … 49
3.1.4.1. Descripción funcional de la CN0536 … 50
3.1.4.2. Principio de funcionamiento de la muestra usada … 51
3.2. Diseño firmware … 52
3.2.1. Entorno de desarrollo: CrossCore Embedded Studio … 52
3.2.1.1. Configuración de CrossCore Embedded Studio para trabajar con la EVAL-ADICUP3029 … 52
3.2.1.1.1. Instalación del IDE … 53
3.2.1.2. Preparación del entorno para el ADuCM3029 … 53
3.2.2. Prueba inicial con diseño de referencia … 53
3.2.3. Primer proyecto creado: control de LEDs … 54
3.2.3.1. Creación del proyecto … 54
3.2.3.1.1. Configuración de rutas de inclusión … 55
3.2.3.2. Compilación y depuración … 55
3.2.3.3. Código implementado … 55
3.2.3.4. Conclusión de la prueba … 55
3.2.4. Proyecto de control de GPIO con interrupciones … 55
3.2.5. Proyecto de control de LED con retardo programable … 56
3.2.5.1. Estructura general … 56
3.2.5.2. Inicialización de hardware … 57
3.2.5.3. Funcionamiento de la librería delay.c … 57
3.2.5.4. Bucle principal … 57
3.2.5.5. Temporizador SysTick … 57
3.2.5.6. Resultados … 57
3.2.6. Primeras Detecciones … 58
3.2.6.1. Arquitectura y librerías empleadas … 58
3.2.6.2. Módulo de detección: geiger.c … 58
3.2.6.3. Flujo de funcionamiento … 59
3.2.6.4. Visualización de resultados mediante UART … 59
3.2.6.5. Programa principal de detección … 60
3.2.6.5.1. Inicialización … 60
3.2.6.5.2. Bucle principal … 60
3.2.6.5.3. Resumen … 60
3.2.6.6. Resultados del proyecto de detección … 60
3.2.6.6.1. Comparativa de conteos … 61
3.2.6.6.2. Forma de onda del pulso detectado … 61
3.2.7. Pantalla TFT ILI9488 con módulo táctil XPT2046 … 62
3.2.7.1. Comunicación SPI … 62
3.2.7.1.1. Ventajas del SPI en este proyecto … 63
3.2.8. Librería spi_1 … 63
3.2.8.0.1. Flujo de funcionamiento … 63
3.2.8.0.2. Asignación de pines … 63
3.2.8.0.3. Inicialización … 64
3.2.8.0.4. Control de líneas … 64
3.2.8.0.5. Transmisión de datos … 64
3.2.8.0.6. Resumen … 64
3.2.8.1. Adaptación de la librería para pantalla ILI9488 … 64
3.2.8.1.1. Ficheros principales … 64
3.2.8.1.2. Funciones destacadas … 65
3.2.8.1.3. Integración con SPI … 65
3.2.8.2. Controlador táctil XPT2046 … 66
3.2.8.2.1. Conexiones y pines … 66
3.2.8.2.2. Funcionamiento interno … 66
3.2.8.2.3. Adaptaciones frente a la librería original … 67
3.2.8.3. Calibración del panel táctil XPT2046 … 67
3.2.8.3.1. Objetivo … 67
3.2.8.3.2. Descripción del funcionamiento … 67
3.2.8.3.3. Adaptaciones para el ADuCM3029 … 68
3.2.9. Integración de LVGL en el proyecto … 69
3.2.9.1. ¿Qué es LVGL? … 69
3.2.9.2. Versión utilizada … 69
3.2.10. Configuración en CrossCore … 69
3.2.10.1. Estructura de directorios y rutas de inclusión … 69
3.2.10.2. Archivo de configuración lv_conf.h … 69
3.2.11. Integración del temporizador de LVGL con SysTick … 70
3.2.12. Resumen de pasos para integrar LVGL … 70
3.2.13. Resumen de pasos para integrar LVGL … 70
3.2.13.1. Cambios realizados en lv_conf.h respecto al template oficial … 70
3.2.13.2. Pruebas gráficas básicas con LVGL … 71
3.2.14. Diseño de interfaces gráficas con SquareLine Studio … 73
3.2.14.1. Flujo de trabajo con SquareLine Studio … 74
3.2.14.2. Integración con CrossCore … 75
3.2.15. Proyecto final … 75
3.2.15.1. Integración de la detección con la interfaz … 75
3.2.16. Visualización en pantalla … 76
3.2.17. Interfaz final … 76
3.3. Diseño mecánico … 77
3.3.1. Prototipado e iteraciones del diseño del manípulo … 77
3.3.1.1. Primer prototipo … 78
3.3.1.2. Segundo prototipo: rediseño alargado … 79
3.3.1.3. Tercer prototipo: manípulos dedicados … 80
3.3.2. Diseño de la caja del producto … 81
3.3.2.1. Estructura general … 81
3.3.2.2. Problemas del primer prototipo … 82
3.3.2.3. Sujeción entre piezas … 83
3.3.2.4. Prototipo final y validación … 84
4. FABRICACIÓN Y ENSAMBLAJE             85
4.1. Montaje de la pantalla y la placa de control … 85
4.2. Fabricación de los cables de conexión entre caja y manípulos … 88
4.3. Proceso de impresión y validación del manipulo … 89
4.3.1. Validación práctica del primer prototipo … 89
4.3.2. Validación práctica del segundo prototipo … 90
4.3.3. Validación práctica del tercer prototipo … 91
4.4. Fabricación de la caja … 93
4.4.1. Montaje de la caja … 93
4.5. Montaje final y conexión del sistema … 96
5. CONCLUSIONES                         97
5.1. Limitaciones y dificultades encontradas … 97
5.2. Líneas de mejora y trabajos futuros … 98
5.3. Conclusión final … 98
A. Coste del proyecto                   103
B. Esquemáticos                         105
B.1. Geiger shield … 105
B.2. EVAL-ADICUP3029 … 118
B.3. cn0536 … 125
C. PCB                                  129
D. Módelos 3D                           132
D.1. Geiger shield … 132
D.2. Primer prototipo de manipulo … 133
D.3. Segundo prototipo de manipulo … 133
D.4. Segundo prototipo de manipulo y abrazadera … 134
D.5. Manipulo final … 134
D.6. Caja Final … 135
E. Simulaciones                         136
E.1. Simulación del circuito de alto voltaje en LTspice … 136
E.1.1. Modelado de los componentes … 136
E.1.2. Esquema de simulación … 137
E.1.3. Resultados … 137
F. Códigos                              139
F.1. Control de LEDs en EVAL-ADICUP3029 … 139
F.2. Control de interrupciones GPIO EVAL-ADICUP3029 … 142
F.3. Control de interrupciones GPIO EVAL-ADICUP3029 … 145
F.4. Libreria Delay.c … 147
F.5. Libreria pwr.c … 149
F.6. Libreria gpio.c … 150
F.7. Libreria geiger.h … 150
F.8. Libreria geiger.c … 152
F.9. Código Detección … 155
F.10.Librería spi1.c … 157
F.11.Librería ili9488.h … 160
F.12.Librería ili9488.c … 163
F.13.Librería xpt2046.h … 169
F.14.Librería xpt2046.c … 171
F.15.Código de calibración de xpt2046 … 176
F.16.Código de seguimiento táctil … 179
F.17.Aplicación de LVGL … 181
F.18.Proyecto final … 185
```

Observación: la bibliografía (impresa 99–102) **no aparece en el índice general**.

---

## D. Títulos y numeración

- **Capítulos:** página de apertura con «Capítulo N» en una línea y el título **en mayúsculas** en la
  siguiente («Capítulo 3» / «DISEÑO DEL SISTEMA», PDF p. 30). Sin resumen/abstract de capítulo, sin
  epígrafe «Introducción» interno: el texto empieza directamente bajo el título. En el índice los
  capítulos van como «3. DISEÑO DEL SISTEMA».
- **Apéndices:** «Apéndice A» / «Coste del proyecto» (p. 98), mismo esquema; letras A–F; subsecciones
  «B.1. Geiger shield», «E.1.1. Modelado de los componentes».
- **Nivel 2:** «3.1. Diseño electrónico» (número con punto final, espacio, título en minúsculas salvo
  nombres propios). **Nivel 3:** «3.1.2. Esquemáticos de circuito». **Nivel 4:** «3.1.2.5. Sistema de
  suministro de energía». **Nivel 5:** «3.1.2.5.1. Estructura del sistema de suministro de energía».
  Todos numerados y todos en el índice. Profundidad máxima usada: **5 niveles** (p. ej. 3.1.2.2.1,
  3.1.3.1.6, 3.2.6.5.3). Existen niveles 5 huérfanos con «.0.» («3.2.8.0.1. Flujo de funcionamiento»,
  p. 58) por saltarse el nivel 4.
- **Epígrafes sin numerar:** en el cuerpo, ninguno. En el apéndice A hay un título sin numerar «Coste
  del shield (placa propia)» (p. 98). En listas se usan etiquetas en negrita-descriptiva («Etapa de
  entrada:», «Inductor y conmutación:») que hacen de pseudo-epígrafes.
- **Cabeceras y pies:** páginas pares: cabecera «NN   Capítulo X. TÍTULO», pie «Antonio Romero
  Espigares» (derecha). Páginas impares: cabecera «X.Y. Sección   NN», pie con el título largo (versión
  con «portátil»). Páginas de apertura de capítulo y preliminares: sin cabecera; pie con título + número.
  Pestaña lateral con el número de capítulo en el margen exterior.
- **Párrafo introductorio de capítulo:** sí, siempre. Dos casos literales:

  Capítulo 2 (PDF p. 26): «En este capítulo se revisan las tecnologías y soluciones existentes
  relacionadas con la detección de Radiación ionizante mediante Tubo Geiger-Müller y el diseño de
  sistemas electrónicos asociados. Se incluyen tanto desarrollos de referencia como módulos de
  alimentación de alto voltaje diseñados específicamente para este tipo de aplicaciones. El objetivo es
  establecer un marco de comparación para el prototipo desarrollado en este Trabajo Fin de Grado.»

  Capítulo 3 (PDF p. 30): «Este capítulo presenta el diseño completo del sistema desarrollado,
  incluyendo los bloques electrónicos, firmware y mecánicos. Se describe en detalle la estructura
  modular del proyecto, la gestión de tareas, el control de la interfaz gráfica y la integración del
  hardware final. Además, se incluyen esquemas, simulaciones y modelos mecánicos asociados al
  desarrollo.»

  Capítulo 4 (PDF p. 80) abre igual: «En este capítulo se describe el proceso de fabricación y
  ensamblaje del dispositivo desarrollado. …» y añade «El objetivo de este apartado es dejar
  documentado de manera clara el flujo de trabajo desde la fabricación de las piezas hasta la
  integración completa del dispositivo,.» (coma + punto: errata).

- **Cierre de capítulo:** no hay sección «Resumen del capítulo». Los capítulos terminan con un párrafo
  de remate o de enlace al siguiente. Literal, cierre del capítulo 2 (p. 28–29): «Por ello, este Trabajo
  Fin de Grado aborda el desarrollo de un sistema propio, adaptado a los requisitos planteados:
  integración con una interfaz gráfica táctil, modularidad mecánica, y un diseño reproducible..».
  Cierre del capítulo 3 (p. 79): «El proceso completo de fabricación de las piezas descritas, así como
  su ensamblaje final junto con los componentes electrónicos, se detalla en el Capitulo 4, donde se
  aborda tanto la impresión 3D como el montaje del sistema completo.» Dentro del capítulo 3 sí hay
  mini-epígrafes «Resumen» (3.2.6.5.3, 3.2.8.0.6) y un «Conclusión de la prueba» (3.2.3.4).

---

## E. Figuras

- **Total:** 75 figuras con pie numerado según la lista de figuras: cap. 1: 1; cap. 2: 1; cap. 3: 46;
  cap. 4: 19; apéndice D: 6; apéndice E: 2. Además: dos grupos de subfiguras **sin pie ni número**
  («(a) Base del manipulo. … (f) Soldadura del detector», PDF pp. 87–88, y «(a) Base con la placa … (f)
  Ensamblaje final.», pp. 90–91) y **8 vídeos embebidos** señalados con la frase «(Para reproducir video
  hacer doble click sobre el simbolo superior)» (pp. 50, 51, 52, 63, 64, 68, 70, 91), sin pie ni
  numeración.
- **Formato literal del pie:** «Figura 3.5 – Módulo INA219 utilizado para la medida de corriente
  mediante resistencia shunt.» Etiqueta «Figura», número capítulo.secuencia, espacio, **guion largo
  (–)**, espacio, texto con mayúscula inicial y **punto final** (excepciones sin punto: «Figura 3.3 –
  Salida 3.3 V», «Figura 3.4 – Salida 5 V», «Figura 3.6 – Circuito de carga», «Figura 3.7 – Circuito
  de protección de carga»). Nunca «Figura 4.3:» ni «Figura 4.3.».
- **Posición:** debajo de la imagen (inferido: en todas las páginas el pie va tras el hueco de la
  imagen e inmediatamente antes del texto siguiente o del pie de página, p. ej. Gantt p. 25). Cuando hay
  subfiguras, las letras «(a) …», «(b) …» van bajo cada imagen y el pie general debajo: «(a) Vista
  isométrica (b) Vista superior de la PCB (Top Layer) (c) Vista inferior de la PCB (Bottom Layer) /
  Figura 3.13 – Fotografías del prototipo desde diferentes ángulos.» (p. 45). Un caso usa las letras de
  subfigura dentro de pies independientes: «Figura 4.14 – (a) Manipulo sobre el tripode.» y «Figura
  4.15 – (b) Abrazadera y manipulo sobre el tripode.» (p. 86).
- **Referencia en el texto** (3 frases literales):
  - «En la Figura 1.1 se muestra el diagrama de Gantt con las fases principales del desarrollo del proyecto, desde la etapa inicial de lecturas y familiarización con herramientas hasta el ensamblaje final y la redacción de la memoria.» (p. 25)
  - «La Figura 3.11 muestra el esquemático completo del generador HV, cuyo principio de funcionamiento se detalla a continuación:» (p. 41)
  - «En la Figura 4.12 se muestra el resultado de esta primera validación, donde puede observarse el fallo de cierre y la falta de espacio para los componentes internos.» (p. 85)
  También hay referencias informales sin número («En las siguientes imagenes se puede ver el resultado de utilizar la funcion fillScreen con dos colores diferentes:», p. 60; «El las siguientes imagenes se muestran los resultados del primer prototipo.», p. 73) y una referencia desnuda «( 3.16)» (p. 56). A los renders del anexo se les llama «Figura 3D D.2» (p. 74).
  Solo 7 referencias explícitas «Figura N.N» en todo el cuerpo para 67 figuras: la mayoría de figuras
  no se citan por número.
- **Fuente:** no se usa «Fuente: elaboración propia». Solo se indica procedencia en logotipos («Figura
  3.1 – Altium Designer logotipo, extraído de: [5].», también 3.15, 3.26, 3.28), en «Figura 3.11 –
  Circuito generador de alto voltaje basado en PWM, inspirado en [47].» y en «Figura 2.1 – Módulo
  MadExp HV: convertidor 5V-900V para tubos Geiger. [47]» (cita suelta tras el punto). El resto se
  entiende propio sin decirlo.
- **Tipos:** fotografías de hardware, soldaduras y prototipos impresos (≈35, dominan en caps. 3.3 y
  4); recortes de esquemáticos Altium (≈10); capturas de terminal/Tera Term (3); capturas de
  osciloscopio (2); capturas de la UI (3 en una figura); renders 3D SolidWorks/Altium (6+2); diagrama
  de bloques (1); diagrama de Gantt (1); logotipos de herramientas (4); esquema y gráfica LTspice (2).
  Ninguna gráfica de resultados con ejes.
- **Numeración:** por capítulo (3.1…3.46) y por apéndice (D.1, E.1). Las figuras de los anexos van en la
  lista de figuras.

---

## F. Tablas

- **Número:** 5 (Tabla 3.1, 3.2, 3.3, A.1, A.2). Ninguna en caps. 1, 2, 4, 5.
- **Pie:** mixto. Tabla 3.1 lleva el título **encima** («Tabla 3.1 – Leyenda de componentes comunes
  utilizados en los esquemáticos del proyecto.» precede a la cabecera «Símbolo / Descripción», p. 32, y
  la tabla continúa en p. 33). Las otras cuatro lo llevan **debajo** (3.2 p. 33, 3.3 p. 37, A.1 p. 98,
  A.2 p. 99).
- **Formato literal:** «Tabla 3.3 – Consumo estimado de los principales componentes del sistema.»;
  «Tabla A.2 – Coste estimado de materiales para el shield (una unidad) y pedido de PCB.» Misma
  puntuación que las figuras (guion largo, punto final).
- **Referencia en el texto** (2 literales): «En la Tabla 3.1 se muestra una recopilación de los
  principales símbolos utilizados en este proyecto.» (p. 31); «La Tabla A.1 recoge los principales
  elementos con su coste unitario, cantidad empleada y coste total.» (p. 98). También parentética:
  «presenta un consumo reducido (del orden de 12 mA en operación activa) (Tabla 3.3)» (p. 39).
- **Contenido:** leyenda de símbolos con imagen en la celda + descripción (3.1); símbolos de red
  (3.2); consumo por componente con columnas Componente / Descripción / Consumo típico / Fuente, con citas
  [n] dentro de la tabla (3.3); costes con Componente / Referencia / Coste unitario / Cantidad / Coste
  total y fila TOTAL (A.1); lista de materiales del shield con Subtotal y Total (A.2). Con decimales en
  coma en A.1 («60,51 €») y en punto en A.2 («0.99»): inconsistente. En layout, la tabla 3.3 y la A.1
  tienen celdas desalineadas (descripciones largas que desbordan).

---

## G. Ecuaciones

- **Hay** unas 11 expresiones en display, **ninguna numerada**. No existe «(3.1)». Aparecen en 3.1.2.5.3
  (I_max, P_d,max, P_d, ΔI; p. 36), 3.1.2.5.5 (E, Duración típica; p. 38), 3.2.6.2 (CPM; p. 54),
  3.2.8.3.2 (x_mín, x_máx, y_mín, y_máx; p. 63) y una «reacción» en 2.1.2: «Radiación + Gas −→ Ion
  positivo + Electrón libre» (p. 26).
- **Cómo se introducen:** frase con dos puntos y la fórmula a continuación, con los valores
  numéricos sustituidos en la misma línea. Ejemplo literal (p. 36): «El valor máximo de corriente
  medible se calcula como: / Imax = Vmax / Rsense = 320 mV / 200 mΩ = 1,6 A». Y después: «La potencia
  máxima disipada por la resistencia shunt sería: / Pd,max = I²max · Rsense = (1,6 A)² · 0,2 Ω =
  0,512 W / Este valor excede ligeramente el límite típico de una resistencia 1206 estándar (0.5 W).»
- **Definición de variables:** no hay «donde …»: las variables se explican en la frase anterior
  (resistencia shunt de 200 mΩ, ganancia PGA 8, 320 mV) o se sobreentienden. En la fórmula del CPM se
  mezclan identificadores de código con matemáticas: «CPM = delta × 60 / SAMPLE_PERIOD_SECONDS» (p. 54).
- **Símbolos en línea:** escasos: «VSG > Vth» (p. 40), «Vt = 400 V», «Ron = 1 kΩ», «Roff = 1e12 Ω»
  (p. 131). Decimales con coma dentro de las fórmulas («1,6 A») y con punto en el texto («3.3 V»,
  «0.5 W», «42.6 µA»): incoherente; a evitar.

---

## H. Código y comandos

- **Listados completos:** todos en el **Apéndice F** (53 páginas, PDF 134–186): 18 listados, cada uno
  bajo una sección «F.N. Título» y con pie **debajo** del bloque: «Listado F.1 – Control de LEDs en la
  usando librerías NO-OS» (hueco de glosario), «Listado F.8 – Libreria geiger.c», «Listado F.18 –
  Proyecto final». Bloque monoespaciado con **números de línea** desde 1, comentarios Doxygen
  (`@file`, `@brief`, `@param`, `@return`) y comentarios de sección «// 1. Inclusión de librerías».
  Longitud: de 25 líneas (gpio.c, 1 página) a 331 líneas (ili9488.c, 6 páginas) y 319 (Proyecto final,
  7 páginas). No hay índice de listados.
- **Fragmentos en el cuerpo:** sí, cortos (1–8 líneas), sin numerar ni pie, en 3.2.11 («while (1) {
  lv_tick_inc(1); lv_timer_handler(); delay_ms(5); }», p. 65), 3.2.13.1 («#define LV_MEM_CUSTOM 1»,
  «#define LV_BUILD_EXAMPLES 0», p. 66), 3.2.13.2 (tres bloques LVGL, pp. 67–68) y 3.2.14.1 («#include
  "ui.h" ui_init();», p. 69).
- **Nombres de ficheros/funciones en el texto:** escritos tal cual, sin comillas, con paréntesis en
  las funciones: «la función delay_ms() que bloquea la ejecución», «el archivo de configuración
  lv_conf.h», «Las funciones gráficas (drawPixel(), fillScreen()) pertenecen a la librería…» (p. 63),
  «writecommand(uint8_t cmd): transmite un byte de comando» (p. 59). En el PDF extraído no se
  distingue la fuente; **inferencia:** monoespaciado (`\texttt`), por la convención LaTeX y porque nunca
  llevan comillas. Macros en mayúsculas («LV_USE_CALENDAR pasa de 1 a 0»).
- **Comandos y rutas de menú:** «se accedió a File → New → CrossCore Project» (p. 49), «Nivel de
  optimización: -Og» (p. 64), «Desde la opción Import Existing Pack, importar los ficheros .pack» (p.
  48). No hay comandos de shell. Se listan paquetes con nombre de fichero literal
  («AnalogDevices.ADuCM302x_DFP.3.2.0.pack [8]»).
- **Asignación de pines como lista:** «MISO: GPIO24 (P1.8) → Pin 30 del uC.» (p. 58), con flechas.
- Nota: el apéndice F incluye un número de serie de software («El número de serie válido para todas
  las placas EVAL-ADICUP3029 es: EZK-CCES-…», p. 48): no recomendable.

---

## I. Citas y bibliografía

- **Estilo en texto:** numérico entre corchetes: «disponible en GitHub [1]», «Según la hoja de datos
  del TP4056 [64]», múltiples sin ordenar «[24, 23, 9]» (p. 52). También citas tras el punto («…de
  Analog Devices. [16]», p. 53; «[11]» suelto al final de párrafo, p. 28) y dentro de pies de figura y
  de celdas de tabla («Datasheet ADuCM3029 [7]», «Mouser [32]»).
- **Orden de la bibliografía:** alfabético por autor o, si no hay autor, por título («[26] BSP300
  MOSFET», «[30] Condensador aluminio 25V THT»), no por aparición (la primera cita del texto es [1] por
  casualidad alfabética: «@issus»). Estilo biblatex numérico: «Autor. *Título*. Año. url: …».
- **Tres entradas literales:**
  - Libro: «[43] Glenn F. Knoll. Radiation Detection and Measurement. Wiley, 1979.»
  - Documentación técnica/datasheet: «[60] Texas Instruments. INA219 - Zero-Drift, Bidirectional Current/Power Monitor With I2C Interface. 2024. url: https://www.ti.com/product/INA219.»
  - Web: «[45] LVGL. Light and Versatile Graphics Library - Sitio oficial. 2025. url: https://lvgl.io/.»
  - (Tienda, muy frecuente) «[4] AliExpress. PLA Filament 1kg Spool for 3D Printing. url: https://es.aliexpress.com/item/1005005221657533.html.»
  - (Artículo divulgativo) «[17] Analog Devices. Introduction to SPI Interface. 2020. url: https://www.analog.com/en/resources/analog-dialogue/articles/introduction-to-spi-interface.html.»
  **No hay fecha de acceso** en ninguna web; algunas llevan año, otras no.
- **Total:** 69 referencias. 67 con URL (97 %). Composición aproximada: 0 artículos de revista, 2
  libros (Chen 1974 y Knoll 1979, que **no se citan en ningún punto del texto**), ≈20 datasheets/manuales
  (alldatasheet, analog.com, ARM), ≈20 páginas de tienda (AliExpress, Mouser, Digikey, RS, LCSC,
  Thomann) usadas como referencia de precio en el apéndice A, ≈4 logotipos «logotype extracted from
  webpage», el resto wikis, repositorios GitHub y webs oficiales de software.
- **Concentración:** capítulo 3: ≈49 líneas con citas (casi todas en 3.1 electrónica y 3.2 firmware);
  capítulo 2: 2 citas ([11], [47]); capítulos 1, 4 y 5: **ninguna**; apéndice A: 25 (precios);
  apéndice E: 4. El estado del arte está prácticamente sin citar.
- Defecto de codificación: «3.5ÏLI9488» por «3.5" ILI9488» (entradas [2] y [55]).

---

## J. Registro y redacción

- **Persona y voz:** impersonal con «se» de forma dominante («se ha empleado», «se diseñó», «se optó
  por»: 49 apariciones de «se ha/se han» en el cuerpo). Primera persona del plural **residual** y
  seguramente involuntaria: «podemos saber la corriente» (p. 34), «En nuestro proyecto se ha
  establecido» (p. 66), «tambien recibimos la información» (p. 63), «Usaremos SPI1» (comentario de
  código). Nunca «yo» ni «hemos» en el cuerpo; «quiero» solo en agradecimientos. El inglés del
  abstract sí usa «allowed us».
- **Tiempos verbales:** presente para describir el sistema y la teoría (cap. 2, 3.1: «El sistema
  utiliza una batería», «La CN0536 integra»); pretérito perfecto compuesto para lo hecho en el TFG en
  resumen, cap. 1 y cap. 5 («se ha desarrollado», «se han obtenido los siguientes logros»); pretérito
  indefinido para narrar el proceso (3.2.2–3.2.6, 3.3, cap. 4: «se empleó el reference design», «se
  diseñó un segundo manípulo», «se realizaron pruebas»). Deslices al futuro en la intro de 3.2: «El
  desarrollo del firmware se llevará a cabo…», «se implementarán las rutinas» (p. 47), inconsistentes
  con el resto.
- **Párrafos y frases:** medidos sobre el cuerpo: 298 párrafos ≥25 palabras, media 49 palabras y
  **2,3 frases por párrafo**; frase media **21 palabras**. Párrafos cortos (2–3 frases), frecuentes
  párrafos de una sola frase que introducen una lista («La metodología seguida se puede resumir en las
  siguientes fases:»). Sangría de primera línea, sin espacio entre párrafos (layout).
- **Listas:** uso **muy intenso**, casi en cada sección: 56 ítems numerados y decenas de viñetas (los
  marcadores no se extraen, pero el layout muestra ítems sangrados), más viñetas anidadas «•». Tipos: (a)
  enumeraciones de pasos de procedimiento (instalación, calibración, fabricación de cables, montaje);
  (b) viñetas de características, áreas de trabajo, limitaciones y trabajos futuros; (c) listas
  descriptivas «Etiqueta: explicación» que sustituyen a subapartados («Etapa de entrada: La tensión de
  alimentación de 5 V…», «Inductor y conmutación: …», «Etapa multiplicadora y filtrado: …», p. 41). Las
  secciones 1.2, 1.3, 2.1.3, 2.1.4, 2.2, 2.3, 2.4, 5 (logros), 5.1, 5.2 son esencialmente listas.
- **Negrita / cursiva:** no determinable desde el texto. Inferencia: las etiquetas de las listas
  descriptivas van en negrita (patrón `\item[\textbf{…}]`); los anglicismos no llevan marca (aparecen
  lisos: «shield», «footprint», «drag-and-drop», «Power rails», «Include Paths», «reference design»,
  «template», «callback»). Comillas tipográficas solo para cadenas y títulos: «“HOLA DESDE LVGL!!!!”»,
  «“Graphic Symbols for Electrical and Electronics Diagrams”».
- **Anglicismos y siglas:** glosario de 56 términos (incluye «Firmware», «Software», «Shield»,
  «Prototipo», «Puerto serie») y lista de 9 siglas (ADC, CPM, ESD, I2C, PCB, SPI, UART, UI, USB). En el
  cuerpo la definición al primer uso solo se hace una vez explícitamente («footprint de la Printed
  Circuit Board (PCB)», p. 31); el resto se delega al glosario (UART, SPI, GPIO, PWM se usan sin
  expandir). Mayúscula sistemática en «Tubo Geiger-Müller», «Radiación ionizante», «Pantalla TFT»,
  «Convertidor Boost» en mitad de frase (artefacto del glosario).
- **Nivel de detalle:** muy alto en firmware (pin a pin, función a función, macros), alto en
  electrónica (valores de componentes, cálculos de corriente, potencia y autonomía), descriptivo y
  narrativo en mecánica y fabricación (iteraciones, problemas, soluciones). Teoría (cap. 2) breve y sin
  citas.
- **Objetivos:** **no hay sección «Objetivos»**. Se formulan como lista de viñetas de «áreas
  principales» en la introducción y en «1.2. Alcance del TFG» («Implementación de librerías de bajo
  nivel…», «Desarrollo del firmware principal…», 6 ítems), y el capítulo 5 los recoge en espejo como
  «logros principales» (7 ítems). La metodología (1.3) es una lista numerada de 8 fases.
- **Requisitos:** no se formalizan (ni tabla ni lista RF/RNF); los requisitos aparecen embebidos en
  la justificación de cada bloque («requiere una tensión de polarización elevada, habitualmente entre
  300 y 400 V»).
- **Resultados:** cualitativos y breves, número + interpretación solo en consumo/autonomía («Consumo
  total típico estimado: ∼ 114 mA», «Duración típica = 13,15 h», seguido de «Estas estimaciones asumen
  un consumo constante y lineal, lo cual no es del todo exacto.», p. 38) y en la simulación («del orden
  de 42.6 µA», p. 132). La validación funcional se despacha sin cifras: «Los resultados muestran una
  concordancia elevada entre ambos sistemas.» (p. 56). No hay tabla de resultados ni gráficas de
  medida.
- **Limitaciones:** lista de 4 viñetas en 5.1 (PCB no fabricada, fuentes de baja actividad, memoria
  del micro, iteraciones mecánicas), seguida de la frase atenuante «A pesar de estas limitaciones, el
  proyecto cumple con los objetivos planteados inicialmente…» (p. 93).
- **Frases típicas de apertura** (literales):
  1. «En este capítulo se revisan las tecnologías y soluciones existentes…» (p. 26)
  2. «Este capítulo presenta el diseño completo del sistema desarrollado…» (p. 30)
  3. «Esta sección detalla todos los aspectos relacionados con el diseño electrónico…» (p. 30)
  4. «Este apartado describe el sistema de alimentación del dispositivo, encargado de…» (p. 34)
  5. «A continuación se describe su operación paso a paso:» (p. 40)
  6. «El presente Trabajo Fin de Grado tiene como alcance el diseño, implementación y validación de…» (p. 23)
  7. «Este proyecto tiene como objetivo entender el uso combinado de pines GPIO…» (p. 50)
  **Frases típicas de cierre** (literales):
  8. «En resumen, el Tubo Geiger-Müller actúa como un amplificador gaseoso de ionizaciones individuales…» (p. 27)
  9. «De este modo, el dispositivo combina las capacidades de detección hardware del contador Geiger con una experiencia de usuario moderna e intuitiva…» (p. 72)
  10. «Con este procedimiento se obtuvieron dos cables robustos y fácilmente intercambiables…» (p. 84)
  11. «Este enfoque iterativo basado en impresión y validación física resultó esencial para alcanzar un diseño final funcional y robusto…» (p. 86)
  12. «En definitiva, la motivación de este trabajo reside en unir la teoría aprendida durante la carrera con un caso práctico real y multidisciplinar…» (p. 23)
  13. «En conclusión, el presente TFG ha permitido materializar un prototipo funcional…» (p. 93)
- **Conectores frecuentes:** «Además», «Asimismo», «Sin embargo», «No obstante», «Por otro lado»,
  «Por ello», «Para ello», «De este modo», «De esta forma», «De esta manera», «Cabe destacar que», «A
  continuación», «Posteriormente», «Finalmente», «En resumen», «En definitiva», «Gracias a», «Con el
  objetivo de», «Con el fin de».

### Tres párrafos representativos completos (literales)

**Diseño/arquitectura (3.1.3.1.1, PDF p. 43):**

> Se trata de una placa de dos capas, una capa superior (Top Layer) y una capa inferior (Bottom Layer). La distribución de pistas ha sido cuidadosamente planificada para garantizar un enrutado eficiente de señales digitales y analógicas, respetando las zonas críticas como la generación de alto voltaje y la detección de partículas. El plano de masa se encuentra ubicado en la capa superior, proporcionando una referencia estable para todo el sistema y mejorando el comportamiento electromagnético del conjunto.

**Resultados/evaluación (3.2.6.6.1, PDF p. 56):**

> Las mediciones se realizaron en idénticas condiciones ambientales, situando la fuente a una distancia constante del tubo Geiger SI-29BG. Se registraron los CPM medios durante intervalos de 60 s, tanto con el sistema desarrollado como con el firmware original de Analog Devices ( 3.16). […] Los resultados muestran una concordancia elevada entre ambos sistemas. Esto valida la correcta captura y procesamiento de pulsos en el firmware diseñado.

**Conclusiones (5.3, PDF p. 93):**

> En conclusión, el presente TFG ha permitido materializar un prototipo funcional de contador GeigerMüller que integra en un solo dispositivo la electrónica de detección, el firmware de gestión, una interfaz gráfica táctil y un diseño mecánico optimizado. El resultado es un sistema portátil, robusto y didáctico, capaz de medir radiación ionizante y mostrarla en tiempo real, constituyendo una plataforma versátil tanto para fines educativos como para investigación básica.

---

## K. Capítulo a capítulo

**Capítulo 1. INTRODUCCIÓN (PDF 22–25, 4 págs., ≈1 400 palabras, 1 figura, 0 tablas).**
Contexto (3 párrafos), lista de 4 áreas, 1.1 Motivación (4 párrafos, GranaSAT), 1.2 Alcance (lista de
6), 1.3 Metodología (lista numerada de 8 fases: revisión, librerías incrementales, integración, UI,
shield, mecánica iterativa, ensamblaje, validación), 1.4 Estructura del documento (un párrafo por
capítulo + viñetas por apéndice), 1.5 Cronograma: una frase y la Figura 1.1 Gantt (sin fechas legibles
en texto, sin tabla de horas). Bien: metodología clara y espejo con el cap. 5. Mal: sin sección de
objetivos, sin cita alguna, el 1.4 promete «los objetivos» que no existen como apartado; «Capítulo 4.
Fabricación y ensamblaje: Se explica el diseño mecánico…» describe mal el capítulo.

**Capítulo 2. ESTADO DEL ARTE (PDF 26–29, 4 págs., ≈1 100 palabras, 1 figura).**
Principio del tubo GM (estructura, detección, zonas de operación, limitaciones, aplicaciones), CN0536 de
Analog Devices, MadExp HV, comparativa y motivación del diseño propio. Casi todo en listas. Bien: breve
y orientado a justificar el diseño. Mal: solo 2 citas ([11], [47]); los dos libros de física de la
bibliografía no se citan; sin figuras de la curva característica; cierra con «..».

**Capítulo 3. DISEÑO DEL SISTEMA (PDF 30–79, 50 págs., ≈17 100 palabras, 46 figuras, 3 tablas).**
Tres grandes bloques: 3.1 electrónico (pp. 30–46: convenciones de esquemáticos, diagrama de bloques,
alimentación con cálculos, UART, pantalla, encendido por pulsador, HV, detección, PCB, uso provisional
de la CN0536, fuente NIS-07), 3.2 firmware (pp. 47–72: IDE, miniproyectos LED/GPIO/delay/detección,
SPI, ILI9488, XPT2046, calibración, LVGL, SquareLine, proyecto final, UI), 3.3 mecánico (pp. 72–79:
tres prototipos de manípulo, caja en tres piezas, problemas y validación). Bien: trazabilidad código ↔
anexo F («En el Apéndice F.15 se puede consuntar…»), cálculos justificados, narración honesta de la PCB
no fabricada, mini-resúmenes. Mal: es un capítulo-monstruo que mezcla diseño, implementación, pruebas y
resultados; profundidad de 5 niveles con huérfanos «.0.»; sección 3.2.12 duplicada en 3.2.13; vídeos
embebidos como única evidencia en 8 puntos; referencia rota «??»; miniproyectos que son tutorial más
que diseño.

**Capítulo 4. FABRICACIÓN Y ENSAMBLAJE (PDF 80–91, 12 págs., ≈2 800 palabras, 19 figuras +
12 subfiguras sin pie).** Montaje pantalla+placa sobre metacrilato, cables GX16 (procedimiento en 5
pasos), impresión y validación de los tres prototipos, fabricación y montaje de la caja, montaje final y
vídeo. Bien: procedimiento paso a paso reproducible, fotos del proceso, honestidad sobre fallos de
tolerancia. Mal: dos grupos de fotos (a)–(f) sin pie ni numeración; pie «Figura 4.13 – Problemas con el
primer prototipo.» repetido para el segundo; muchas erratas («manipulo», «tripode», «Esta pieza» con
pie partido «pantal la»).

**Capítulo 5. CONCLUSIONES (PDF 92–93, 2 págs., ≈730 palabras, 0 figuras).** Párrafo de síntesis,
lista de 7 logros, 5.1 limitaciones (4 viñetas), 5.2 líneas futuras (6 viñetas), 5.3 conclusión final (2
párrafos). Bien: espejo del alcance. Mal: ninguna cifra, ninguna referencia a resultados concretos.

**Bibliografía (PDF 94–97).** Ver I.

**Planificación / presupuesto / costes.** No hay capítulo dedicado. Planificación: solo el Gantt
(1.5) sin desglose de horas por fase. Costes: **Apéndice A** (PDF 98–99) con dos tablas: Tabla A.1
«Coste estimado del proyecto sin fabricación de shield propia» con filas EVAL-ADICUP3029 (60,51 €),
Módulo CN0536 (111,85 €), Pantalla TFT ILI9488 (9,29 €), Conectores GX16 (2 × 1,23 €), Cable multipar
(2 m × 6,70 €/m = 13,40 €), Filamento PLA (549 g, 10,98 €), «Coste de mano de obra / Ingeniero junior
(12 €/h) / 800 h / 9600 €» y «TOTAL 9808,49 €». Tabla A.2: materiales del shield (22 líneas con precio
unitario y referencia a tienda) «Subtotal componentes 33.79», «PCB 2 capas (5 uds., pedido) 25.00»,
«Total estimado (materiales + PCB) 58.14». No hay costes de software ni licencias (Altium, SolidWorks,
SquareLine), ni amortización de equipos, ni IVA («no incluyen IVA ni gastos de envío salvo donde se
indique»). Las referencias de precio son páginas de tienda citadas en la bibliografía.

**Apéndices B–F.** B: 12 hojas propias con cajetín en inglés (título, autor, supervisor, fecha,
«Sheet n of 12», revisión 4) más esquemáticos de fabricante incrustados; introducido por un párrafo que
dice que «los esquemas son autónomos y se pueden entender por sí mismos». C: vistas top/bottom sin
pies. D: 6 renders con pie («Figura D.6 – Figura 3D del manipulo final» aplicado a la caja: error). E:
simulación LTspice con modelos SPICE pegados como texto y resultado «42.6 µA» reutilizado en la Tabla
3.3. F: 18 listados completos (ver H).

---

## L. Particularidades UGR/ETSIIT

- **Portada (PDF p. 1), orden literal:** «TRABAJO FIN DE GRADO» / «INGENIERÍA DE TECNOLOGÍAS DE
  TELECOMUNICACIÓN» / título en tres líneas / «Autor» / «Antonio Romero Espigares» / «Director» / «D.
  Andrés María Roldán Aranda» / «Escuela Técnica Superior de Ingenierías Informática y de
  Telecomunicación» / «—» / «Granada, Septiembre de 2025». El tutor se llama **«Director»** y lleva
  tratamiento «D.». No aparece el departamento, ni «Universidad de Granada» como texto, ni «Grado en».
- **Orden de preliminares (según índice):** portada (1) → licencia (2–3) → autorización de defensa
  (4) → autorización de depósito en biblioteca (6) → resumen (8) → abstract (9) → agradecimientos (10)
  → índice general (11) → lista de figuras (18) → lista de tablas (21) → glosario (22) → siglas (26) →
  capítulo 1 (27). Cada bloque empieza en página impar (recto), con blancos intermedios.
- **Fórmulas oficiales:** las dos páginas de autorización (defensa/depósito) existen en el original
  pero **han sido retiradas de este PDF**, así que no se puede reproducir su redacción. En lo que queda
  no hay menciones a «tribunal», ni DNI (las 16 apariciones de «DNI» son «Do Not Install» en los
  esquemáticos de Analog Devices), ni firma, ni declaración de originalidad.
- **Elementos propios de la plantilla del tutor (GranaSAT):** página de licencia CC BY-SA con
  copyright compartido alumno + tutor; pestañas laterales con número de capítulo; pie alterno título/
  autor; glosario + siglas separados; apéndices de esquemáticos con cajetín bilingüe; vídeos
  embebidos; apéndice de costes con mano de obra a 12 €/h.
- **Idioma:** castellano en todo el cuerpo; cajetines de esquemáticos, comentarios de algunos códigos y
  licencia en inglés; título del abstract traducido.

---

## M. Cifras globales

| Magnitud | Valor |
|---|---|
| Páginas PDF / impresas | 187 / 192 (5 preliminares ausentes) |
| Preliminares (portada → siglas) | 21 págs. PDF (26 impresas) |
| Cuerpo (caps. 1–5) | 72 págs. (PDF 22–93) |
| Bibliografía | 4 págs. |
| Apéndices | 89 págs. (PDF 98–186) + 1 blanca; de ellas 53 de código y 24 de esquemáticos |
| Figuras con pie | 75 (1 + 1 + 46 + 19 + 6 + 2) + 2 grupos de subfiguras sin pie + 8 vídeos |
| Tablas | 5 |
| Ecuaciones | ≈11 en display, 0 numeradas |
| Listados | 18 (todos en el anexo F) + ≈6 fragmentos sin pie en el cuerpo |
| Referencias | 69 (67 con URL, 2 libros no citados) |
| Términos de glosario / siglas | 56 / 9 |
| Palabras totales (pdftotext) | ≈67 300 (incluye código y esquemáticos) |
| Palabras por bloque (sin puntos conductores) | preliminares ≈5 750 (glosario incluido); cap. 1 ≈1 390; cap. 2 ≈1 090; cap. 3 ≈17 100; cap. 4 ≈2 770; cap. 5 ≈730; bibliografía ≈1 330; ap. A ≈560; ap. B ≈6 150 (etiquetas de esquemático); ap. C ≈780; ap. D ≈240; ap. E ≈720; ap. F ≈16 600 (código) |
| Cuerpo redactado real (caps. 1–5) | ≈23 100 palabras |
| Media por párrafo / por frase | 49 palabras y 2,3 frases / 21 palabras |
| Niveles de numeración | 5 |
| Referencias cruzadas en el cuerpo | «Capítulo» 47, «Apéndice/Apendice» 22, «Figura N.N» 7, «Sección» 5, «Apartado F.n» 5, «Tabla» 3 |

---

## N. Lecciones transferibles

### Reglas para parecerse a esta memoria (formato, estructura, redacción)

1. **Portada ETSIIT sobria y en este orden:** «TRABAJO FIN DE GRADO», titulación en mayúsculas,
   título, «Autor / Nombre», «Director / D. Nombre», nombre completo de la Escuela, «Granada, Mes de
   Año». Detrás, una página de copyright/licencia, las dos autorizaciones (defensa y depósito), resumen
   + palabras clave, abstract + keywords, agradecimientos, índice general, lista de figuras, lista de
   tablas, glosario y siglas. Cada bloque en página impar.
2. **Capítulos en dos líneas** («Capítulo N» / TÍTULO EN MAYÚSCULAS), epígrafes numerados con punto
   final («3.1.», «3.1.2.») y párrafo introductorio obligatorio de 2–4 frases que diga qué contiene el
   capítulo. Sin epígrafe «Introducción» ni «Resumen» por capítulo; se cierra con un párrafo de remate o
   de enlace al capítulo siguiente.
3. **Pies con guion largo y punto final:** «Figura 3.5 – Texto.» y «Tabla 3.3 – Texto.», debajo del
   objeto, numerados por capítulo, con subfiguras «(a) …» bajo cada imagen y pie común debajo. Las
   figuras de anexos se numeran «D.1», «E.1» y van en la lista de figuras. Fuente solo cuando no es
   propia («extraído de: [n]», «inspirado en [n]»).
4. **Citas numéricas [n]** y bibliografía biblatex ordenada alfabéticamente con formato «Autor.
   Título. Año. url: …»; datasheets, manuales y webs oficiales como fuentes mayoritarias; precios de
   componentes referenciados a la tienda. (Corregir respecto al modelo: añadir fecha de acceso y citar
   todo lo que esté en la bibliografía.)
5. **Registro impersonal con «se»**, sin «yo» ni «nosotros»: presente para describir el sistema,
   pretérito perfecto compuesto para lo logrado, indefinido para narrar iteraciones. Párrafos de 2–3
   frases (≈50 palabras) y frases de ≈20 palabras.
6. **Listas como herramienta principal de exposición:** viñetas para alcance, características,
   limitaciones y trabajos futuros; numeradas para procedimientos paso a paso; descriptivas
   «Etiqueta: explicación» para desglosar un circuito o un flujo. Casi cada sección tiene una.
7. **Introducción con metodología explícita** (lista numerada de fases) y **estructura del documento**
   (una frase por capítulo y viñetas por apéndice), más un **cronograma Gantt** como figura. Alcance y
   logros del capítulo 5 en espejo, ítem por ítem.
8. **Cálculos de diseño justificados en display** con valores sustituidos en la misma línea y el
   resultado comentado en la frase siguiente («Este valor excede ligeramente…»), sin numerar la ecuación
   si no se va a referenciar.
9. **Código fuera del cuerpo:** en el cuerpo solo fragmentos de 1–8 líneas; el código íntegro en un
   apéndice con «Listado X.N – título» debajo, líneas numeradas, comentarios Doxygen, y referencias
   cruzadas desde el texto («se puede consultar en el Apéndice F.10»). Nombres de funciones con
   paréntesis «delay_ms()» y ficheros «lv_conf.h» tal cual, sin comillas.
10. **Glosario largo + lista corta de siglas** generados con *glossaries*, definiendo cada término una
    vez; en el cuerpo se expande la sigla al primer uso solo en los casos clave.
11. **Costes en apéndice** con dos tablas (prototipo real y alternativa) con columnas Componente /
    Referencia / Coste unitario / Cantidad / Coste total, fila de mano de obra con €/h y horas, y TOTAL.
12. **Anexos técnicos voluminosos como evidencia:** esquemáticos completos con cajetín, vistas de PCB,
    renders 3D, simulación con parámetros, código entero. Aquí casi la mitad del documento.

### Cosas que NO aparecen en este TFG (y conviene seguir evitando)

- Emojis, iconos, markdown visible, texto en color, cajas destacadas, notas al margen.
- Negritas en el cuerpo del texto corrido (solo, inferido, en etiquetas de listas).
- Cursiva para anglicismos (van lisos).
- Ecuaciones numeradas y «donde:» con lista de variables.
- Tablas de resultados numéricos, gráficas con ejes, estadísticas, intervalos de confianza.
- Sección de «Objetivos» separada, requisitos numerados (RF/RNF), casos de uso, diagramas UML.
- Pie «Fuente: elaboración propia».
- Fecha de acceso en las URL; artículos científicos de revista.
- Notas a pie de página.
- Frases en primera persona del singular fuera de los agradecimientos.
- Preguntas retóricas (solo una en un título: «¿Qué es LVGL?»), metáforas, adjetivos vacíos.
- Citas en los capítulos 1, 4 y 5.
- Índice de listados, lista de ecuaciones, dedicatoria.

### Errores detectados que conviene evitar

- Ortografía y tildes inconsistentes en la misma palabra: «manipulo» (41) / «manípulo» (41),
  «tripode» (6) / «trípode» (8), «Apendice» (4) / «Apéndice» (57), «Libreria» / «Librería», «esquematico»
  (13), «imagenes», «Módelos 3D», «consuntar» (×4 por «consultar»), «Transitor», «fooprint»,
  «saleccionado», «dispositovo», «alimenatción», «palca», «procedieminto», «funcionamineto», «El las
  siguientes imagenes» (×2), «Electronica», «PCB desing», «Ternured Professor».
- Puntuación: «..» al final de todas las entradas del glosario y del cierre del cap. 2; «,.» en la
  intro del cap. 4; pies sin punto final (3.3, 3.4, 3.6, 3.7); decimales con coma y con punto mezclados.
- Automatismos del glosario sin revisar: términos con mayúscula en mitad de frase, «la mediante
  formato», «estándar -315», «GPIO, , SPI», «refresco de :», «generados por .»; «glsanalogdevices» impreso
  tal cual (p. 61).
- Estructura: sección 3.2.12 y 3.2.13 con el mismo título y contenido; F.2 y F.3 con el mismo título;
  numeración «3.2.8.0.1» por saltarse un nivel; 5 niveles de profundidad; capítulo 3 con el 69 % del
  cuerpo; bibliografía fuera del índice; «Figura 3D D.2» como forma de referencia.
- Figuras: dos grupos de fotos sin pie; pie repetido (4.13); pie equivocado (D.6); subfiguras
  convertidas en figuras independientes (4.14, 4.15); referencia rota «??»; referencia desnuda «( 3.16)»;
  solo 7 referencias explícitas a 67 figuras.
- Pie de página con una versión del título («portátil») distinta de la portada.
- Keywords del abstract en español y «Pantalla TFT» dentro del inglés.
- Vídeos embebidos como única evidencia de funcionamiento (no se ven en la mayoría de visores ni en
  papel); publicar un número de serie de software.
- Libros en la bibliografía que no se citan; webs sin fecha de acceso; entradas con codificación rota
  («3.5ÏLI9488»).
- Resultados sin cifras («concordancia elevada») y sin tabla comparativa cuando se afirma haber
  comparado CPM durante 60 s.
- Tablas con celdas desbordadas (3.3, A.1) y unidades mezcladas en una misma columna («2m», «549 g»,
  «800 h» en Cantidad).

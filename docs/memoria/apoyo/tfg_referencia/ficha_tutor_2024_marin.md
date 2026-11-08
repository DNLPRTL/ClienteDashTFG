# Ficha de formato y estilo — TFG del tutor, 2024 (Ángel Marín Munuera)

**Fuente analizada:** `docs/memoria/DE MI TUTOR JUAN JOSE RAMOS MUNOZ/2024_TFG_AngelMarinMunuera.pdf`
**Método:** texto extraído con `pdftotext` (xpdf 4.00) en modo flujo y en modo `-layout`; lectura íntegra de las 143 páginas (preliminares, 7 capítulos, capítulo de apéndices con 15 volcados de ficheros y bibliografía). Recuentos hechos por programa sobre el texto extraído.
**Convención de páginas:** «(p. N)» = página del PDF. La numeración impresa va cuatro por detrás a partir del índice (impresa = PDF − 4; p. ej., el Capítulo 1 empieza en la p. 19 impresa = p. 23 del PDF).
**Avisos sobre la extracción:** el PDF compone los acentos como glifo separado (fuente OT1 de LaTeX); se han recompuesto por programa. Los guiones bajos de los identificadores del cuerpo se pierden en la extracción (`control manual.py` = `control_manual.py`, `set manual mode()` = `set_manual_mode()`); en las citas literales se dejan tal cual salen y se avisa. Donde algo no se puede saber desde el texto (negritas, cursivas, logotipos) se dice expresamente.
**Aviso de autoría:** el TFG tiene DOS directores: Jorge Navarro Ortiz (figura como «director del proyecto», 20 h, y es el único que firma el informe) y Juan J. Ramos Muñoz («co-director», 10 h). Varios rasgos pueden ser preferencia de Navarro tanto como de Ramos; se señala cuando procede.

---

## A. Identificación

- **Título completo:** «Experimentación en 5G mediante UGVs» (pp. 1, 5, 7, 13).
- **Autor:** Ángel Marín Munuera (pp. 1, 5, 7, 11).
- **Directores (literal de portada: «Directores»):** «Jorge Navarro Ortiz» y «Juan J. Ramos Muñoz» (pp. 1, 5). En el informe (p. 13) ambos aparecen como «Profesor Titular de Universidad del Área de Ingeniería Telemática del Departamento Teoría de la Señal, Telemática y Comunicaciones de la Universidad de Granada». En el capítulo de costes (p. 34): «Juan José Ramos Muñoz, co-director del proyecto» y «Jorge Navarro Ortiz, director del proyecto».
- **Departamento:** Teoría de la Señal, Telemática y Comunicaciones; Área de Ingeniería Telemática (p. 13).
- **Titulación literal:** portada: «TRABAJO FIN DE GRADO» / «INGENIERÍA DE TECNOLOGÍAS DE TELECOMUNICACIÓN» (p. 1). Autorización: «alumno de la titulación Grado de Ingenierías en Tecnologías de Telecomunicación» (p. 11; sic, «Ingenierías»).
- **Centro literal:** «Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación» (pp. 1, 11).
- **Universidad:** «Universidad de Granada» (pp. 11, 13). En la portada el nombre de la universidad no aparece como texto (probablemente va en el logotipo; no determinable desde el texto).
- **Fecha/curso (literal de portada):** «Granada, junio de 2024» (p. 1). Autorización del alumno: «Granada a día 20 de junio de 2024.» (p. 11). Informe: «en Granada en junio de 2024» (p. 13). Último acceso de las referencias: 20/06/2024 (y 24/06/2024 en la [38]).
- **Número de páginas:** 143 según `pdftotext` (el encargo indica 144; la diferencia probablemente es una página en blanco final que la herramienta no emite). Páginas en blanco: 2, 4, 6, 8, 10, 12, 14, 22, 30, 36, 40, 70, 142, 143. La p. 3 solo contiene el carácter «3» (probablemente un folio en una página de cortesía; no determinable).
- **Herramienta de maquetación inferida: LaTeX** (clase tipo `book`, plantilla de la ETSIIT). Evidencias: (1) acentos extraídos como glifo separado («Experimentaci´on», «Mun˜oz») = fuentes Computer Modern con codificación OT1; (2) páginas pares en blanco tras portada, portadilla, resumen, abstract, autorización e informe, y antes de cada capítulo que caería en par (`openright`); (3) 169 guiones de partición de palabra a final de línea solo en pp. 23–73; (4) «Capítulo N» en una línea y el título en la siguiente; cabeceras corridas distintas en pares («28  2.2. Costes») e impares («Planificación y Costes  31»); (5) tablas llamadas «Cuadro» e «Índice de cuadros» (valor por defecto de `babel` spanish); (6) pie «Listing 1:» sin traducir (paquete `listings`) y listados con numeración de líneas; (7) bibliografía con los rasgos de BibTeX estilo `unsrt`/`plain` (títulos pasados a minúsculas: «Aws deepracer pricing», «5g key performance indicators», «Uavs for 5g networks»); (8) restos de la plantilla sin rellenar en la página del abstract: «Project Title: Project Subtitle» y «First name, Family name (student)» (p. 9); (9) comillas tipográficas ‘ ’ y signos × ≈ − compuestos por el motor matemático.

## B. Estructura completa, en orden (páginas del PDF)

1. **Portada (p. 1).** Texto, de arriba abajo: «TRABAJO FIN DE GRADO» / «INGENIERÍA DE TECNOLOGÍAS DE TELECOMUNICACIÓN» / «Experimentación en 5G mediante UGVs» / «Autor» / «Ángel Marín Munuera» / «Directores» / «Jorge Navarro Ortiz» / «Juan J. Ramos Muñoz» / «Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación» / «—» / «Granada, junio de 2024». p. 2 en blanco; p. 3 solo «3»; p. 4 en blanco.
2. **Segunda portada / portadilla (p. 5):** «Experimentación en 5G / mediante UGVs» / «Autor» / «Ángel Marín Munuera» / «Directores» / «Jorge Navarro Ortiz» / «Juan J. Ramos Muñoz». Sin centro ni fecha. p. 6 en blanco.
3. **Resumen y palabras clave en español (p. 7).** Cabecera: título y autor. Luego «Palabras clave: …», «Resumen» y cinco párrafos. p. 8 en blanco.
4. **Abstract y keywords (p. 9).** Cabecera con los marcadores de la plantilla SIN rellenar: «Project Title: Project Subtitle» / «First name, Family name (student)». Luego «Keywords: …», «Abstract», cinco párrafos. p. 10 en blanco.
5. **Autorización del alumno (depósito en biblioteca) (p. 11).** Con DNI, «Fdo:» y fecha. p. 12 en blanco.
6. **Informe/autorización de los directores (p. 13).** «Informan: …», «El director:» y el nombre de Jorge Navarro Ortiz (un solo firmante aunque hay dos directores). p. 14 en blanco.
7. **Agradecimientos (p. 15, mitad superior).** Cuatro párrafos breves en primera persona. **Comparten página con el inicio del Índice general.**
8. **Índice general (pp. 15–17; impresas 11–13).** Empieza en la misma p. 15, debajo de los agradecimientos.
9. **Índice de figuras (p. 18; impresa 14)** seguido, en la misma página, del **Índice de cuadros**.
10. **«Abreviaciones y notaciones utilizadas» (pp. 19–21; impresas 15–17):** unas 60 siglas en orden alfabético, formato «SIGLA Expansión en español (Expansión en inglés)», la expansión inglesa en cursiva (inferido por el espacio antes del paréntesis de cierre: «(Three Dimensional )»). Ejemplo literal: «API Interfaz de Programación de Aplicaciones (Application Programming Interface)». Glitch: la cabecera corrida de estas páginas sigue diciendo «ÍNDICE DE CUADROS». p. 22 en blanco.
11. **Capítulos (pp. 23–74; impresas 19–70):** 1 Introducción (23–29), 2 Planificación y Costes (31–35), 3 Estado del arte (37–39), 4 Tecnologías implicadas (41–46), 5 Diseño e implementación (47–64), 6 Experimentación (65–69), 7 Conclusión (71–74).
12. **«Capítulo 8 Apéndices» (pp. 75–138; impresas 71–134):** quince apéndices, letras A–O incluida la «Ñ», cada uno un volcado íntegro de un fichero (README, YAML, INI, scripts sh, scripts Python, JSON).
13. **Bibliografía (pp. 139–141; impresas 135–137):** 38 entradas numeradas. NO aparece en el índice general.
14. pp. 142–143 en blanco.

**Bloques que faltan:** dedicatoria; declaración de originalidad explícita (solo hay autorización de biblioteca e informe de los directores); glosario de términos (solo siglas); índice de listados; anexos como parte separada (van como «Capítulo 8»); capítulo propio de objetivos, requisitos, metodología o trabajo futuro (los objetivos van dentro de la introducción y el trabajo futuro dentro de «Conclusión»); notas al pie (cero en todo el documento).

### B.1 Texto literal de la autorización del alumno (p. 11)

> Yo, Ángel Marín Munuera, alumno de la titulación Grado de Ingenierías en Tecnologías de Telecomunicación de la Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación de la Universidad de Granada, con DNI [DNI], autorizo la ubicación de la siguiente copia de mi Trabajo Fin de Grado en la biblioteca del centro para que pueda ser consultada por las personas que lo deseen.
>
> Fdo: Ángel Marín Munuera
>
> Granada a día 20 de junio de 2024.

(En el original figura el DNI completo, con letra; aquí se omite por ser dato personal. En el PDF, nombre, titulación, centro y universidad van probablemente en negrita: no determinable desde el texto.)

### B.2 Texto literal del informe de los directores (p. 13)

> D. Jorge Navarro Ortiz, Profesor Titular de Universidad del Área de Ingeniería Telemática del Departamento Teoría de la Señal, Telemática y Comunicaciones de la Universidad de Granada.
>
> D. Juan J. Ramos Muñoz, Profesor Titular de Universidad del Área de Ingeniería Telemática del Departamento Teoría de la Señal, Telemática y Comunicaciones de la Universidad de Granada.
>
> Informan:
>
> Que el presente trabajo, titulado Experimentación en 5G mediante UGVs, ha sido realizado bajo su supervisión por Ángel Marín Munuera, y autorizamos la defensa de dicho trabajo ante el tribunal que corresponda.
>
> Y para que conste, expiden y firman el presente informe en Granada en junio de 2024.
>
> El director:
>
> Jorge Navarro Ortiz

(Incoherencia: «Informan» y «expiden y firman» en plural, «autorizamos» en primera persona, y una única línea de firma «El director:».)

### B.3 Resumen y palabras clave (p. 7), literal

> Palabras clave: Redes 5G, Quinta Generación, medidas experimentales, vehículo automatizado, redes móviles, UGV, AWS DeepRacer EVO
>
> Resumen
>
> La Quinta Generación (5G) de redes móviles ha significado una oportunidad sin precedentes para el surgimiento e implementación de diversas tecnologías avanzadas, que requieren escenarios con conexiones de alta velocidad y fiabilidad. Este proyecto se centra en la medición experimental de las redes 5G empleando UGVs, con el objetivo de determinar la viabilidad y evaluar el rendimiento de la conectividad de estas redes en diferentes escenarios utilizando estos dispositivos.
>
> En este documento se detalla la configuración de un sistema de mediciones experimentales 5G utilizando un UGV, concretamente, un AWS DeepRacer EVO. Se han realizado múltiples pruebas de campo en diferentes entornos, tanto de interior como de exterior.
>
> Las estadísticas de la red se recogieron y monitorizaron en tiempo real, principalmente utilizando dos plataformas de software: Prometheus y Grafana. Además, todo este proceso se automatizó mediante el uso de scripts y archivos de rutas, de forma que los experimentos sean reproducibles. Se puso a prueba la capacidad de este UGV para ser automatizado, permitiendo la realización de estos experimentos de manera eficiente.
>
> Los resultados obtenidos demuestran la capacidad de estos vehículos para realizar experimentos automatizados, medir redes 5G y comprobar su funcionamiento. Se incluye también una pequeña guía para la ejecucion [sic] de experimentos similares a los que se han realizado, sin necesidad de conocimientos avanzados.
>
> Finalmente, este proyecto ofrece recomendaciones para la realización de estos experimentos y sugiere líneas futuras de investigación para mejorar aún más la integración de estas tecnologías.

(≈ 230 palabras, cinco párrafos: contexto → qué se hace → cómo → resultados → recomendaciones/futuro. Las palabras clave van ANTES del resumen.)

### B.4 Abstract y keywords (p. 9), literal

> Keywords: 5G Networks, Fifth Generation, Experimental Measurements, Automated Vehicle, Mobile Networks, UGV, AWS DeepRacer EVO
>
> Abstract
>
> The Fifth Generation (5G) of mobile networks has presented an unprecedented opportunity for the emergence and implementation of various advanced technologies that require scenarios with high-speed and reliable connections. This project focuses on the experimental measurement of 5G networks using UGVs, aiming to determine the feasibility and evaluate the performance of network connectivity in different scenarios using these devices.
>
> This document details the configuration of a 5G experimental measurement system using a UGV, specifically an AWS DeepRacer EVO. Multiple field tests have been conducted in various environments, both indoors and outdoors.
>
> Network statistics were collected and monitored in real-time, primarily using two software platforms: Prometheus and Grafana. Additionally, this entire process was automated using scripts and route files to ensure the experiments are reproducible. The capability of this UGV to be automated was tested, allowing the efficient execution of these experiments.
>
> The results obtained demonstrate the ability of these vehicles to perform automated experiments, measure 5G networks, and verify their functionality. A small guide is also included for conducting similar experiments to those performed, without the need for advanced knowledge.
>
> Finally, this project offers recommendations for conducting these experiments and suggests future research lines to further improve the integration of these technologies.

### B.5 Agradecimientos (p. 15), literal

> Agradecimientos a mi familia, por haber estado apoyándome durante todos estos años de forma incondicional, anteponiendo mi bienestar al suyo.
> Agradecimientos a mis amigos, por todos los buenos momentos durante esta etapa. Con especial mención a los Primos, Pornais, el Grupo del Kanketilla, y Moisés.
> Agradecimientos a Wendy, por su gran importancia durante la última recta de la carrera.
> Y agradecimientos a Jorge Navarro, por haber dedicado una gran cantidad de esfuerzo, tiempo y paciencia en que este proyecto fuera completado.

## C. Índice general copiado literalmente (pp. 15–17; números = páginas impresas)

```
1 Introducción                                   19
2 Planificación y Costes                         27
  2.1 Planificación                              27
  2.2 Costes                                     28
    2.2.1 Costes hardware                        29
    2.2.2 Costes software                        29
    2.2.3 Costes humanos                         30
    2.2.4 Estimación del coste total             31
3 Estado del arte                                33
4 Tecnologías implicadas                         37
  4.1 AWS DeepRacer Evo                          37
    4.1.1 Hardware                               37
    4.1.2 Software                               38
    4.1.3 ROS                                    39
    4.1.4 Consolas y APIs                        40
  4.2 Plataformas destinadas a las métricas 5G   40
    4.2.1 Prometheus                             40
    4.2.2 Grafana                                40
  4.3 Lenguajes                                  41
    4.3.1 Python                                 41
    4.3.2 JSON                                   41
    4.3.3 Shell                                  41
    4.3.4 YAML                                   41
  4.4 Otras                                      42
    4.4.1 Git                                    42
    4.4.2 USB-tethering                          42
5 Diseño e implementación                        43
  5.1 Diseño                                     43
    5.1.1 Archivo de ruta                        44
  5.2 Implementación del control del coche       47
  5.3 Implementación de las plataformas de medición  51
    5.3.1 Configuración de Prometheus            52
    5.3.2 Configuración de Grafana               52
    5.3.3 Importación de dashboards y datasources  53
  5.4 Realización de las mediciones              54
  5.5 Ejecución de la plataforma                 55
    5.5.1 Preparación de entorno                 55
    5.5.2 Operación                              57
    5.5.3 Depuración de errores                  59
6 Experimentación                                61
  6.1 Experimento en interior                    63
  6.2 Experimento en exterior                    65
7 Conclusión                                     67
8 Apéndices                                      71
  Apéndice A. README.md                          71
  Apéndice B. prometheusOriginal.yml             72
  Apéndice C. grafanaOriginal.ini                72
  Apéndice D. importdatasourcesOriginal.sh       103
  Apéndice E. importdashboardsOriginal.sh        104
  Apéndice F. startstatsOriginal                 104
  Apéndice G. ss exporterOriginal                104   [ss_exporterOriginal]
  Apéndice H. control manual.py                  107   [control_manual.py]
  Apéndice I. ruta.json                          108
  Apéndice J. prometheusModificado.yml           110
  Apéndice K. ss exporterModificado.py           111   [ss_exporterModificado.py]
  Apéndice L. start statsModificado.sh           114   [start_statsModificado.sh]
  Apéndice M. stop statsModificado               114   [stop_statsModificado]
  Apéndice N. AWS DeepRacer 5G + WIFI-1716887935477.json  114
  Apéndice Ñ. aaModificado                       133
  Apéndice O. camara.py                          133
```

Observaciones: en el índice los números de sección van SIN punto final («2.1 Planificación»), mientras que en los epígrafes del cuerpo van CON punto («2.1. Planificación»). El índice no incluye el Índice de figuras, el Índice de cuadros, las Abreviaciones ni la Bibliografía. Los apéndices se listan como entradas no numeradas dentro del «8 Apéndices». Índice de figuras (p. 18): 14 entradas con pie corto («5.3 Solicitud set manual mode() … 48», «6.1 Montaje del coche. … 61»). Índice de cuadros (p. 18): una sola entrada («2.1 Estimación del coste total del proyecto. … 31»).

## D. Títulos y numeración

- **Capítulos:** «Capítulo N» en una línea y el título en la siguiente, sin punto final (p. ej. p. 31: «Capítulo 2» / «Planificación y Costes»; p. 75: «Capítulo 8» / «Apéndices»). La página de apertura de capítulo no lleva cabecera corrida y lleva el folio centrado abajo. Las páginas interiores llevan cabecera corrida: en pares «folio + N.M. Título de sección» («28  2.2. Costes»), en impares «Título del capítulo + folio» («Diseño e implementación  49»). Uso de mayúsculas en títulos: solo inicial, salvo nombres propios («Planificación y Costes» lleva «Costes» en mayúscula, incoherente con «Diseño e implementación»).
- **Nivel 2:** «N.M. Título» con punto tras el número (p. 31: «2.1. Planificación»; p. 47: «5.1. Diseño»). **Nivel 3:** «N.M.K. Título» (p. 33: «2.2.1. Costes hardware»; p. 59: «5.5.1. Preparación de entorno»). **Profundidad máxima: 3.** No hay nivel 4 ni párrafos titulados.
- **Epígrafes sin numerar:** los de los preliminares («Resumen», «Abstract», «Agradecimientos», «Índice general», «Índice de figuras», «Índice de cuadros», «Abreviaciones y notaciones utilizadas»), las entradas «Apéndice X. nombre_de_fichero» dentro del capítulo 8, y «Bibliografía».
- **Capítulos que abren con párrafo introductorio:** los siete. Siempre 1–3 frases, en futuro, que anuncian el contenido. Dos literales:
  - Capítulo 2 (p. 31): «En esta sección se incluirá la planificación temporal de este proyecto, que se ha seguido de forma aproximada. Además, se incluirán los costes de los elementos software y hardware para realizar una estimación de los mismos. También se añadirá al cómputo total el coste de los recursos humanos involucrados en este trabajo.»
  - Capítulo 4 (p. 41): «Este capítulo describirá de la forma más breve posible las diferentes tecnologías utilizadas. Se entrará en detalle, con su aplicación específica en este proyecto, en el siguiente capítulo.»
  - Otros: Capítulo 3 (p. 37): «Esta sección repasará los estudios actuales de medidas de redes de datos con vehículos automatizados y otra bibliografía que relaciona los conceptos de 5G y vehículos automatizados. De esta forma, se podrá tener una contextualización de la sinergia entre 5G y los vehículos automatizados, así como la identificación de vacíos, como la experimentación en la medición de estas señales con el uso de vehículos automatizados.» Capítulo 6 (p. 65): «En esta sección se explicarán los dos experimentos realizados, haciendo uso de la implementación y diseño descritos anteriormente. Se comienza mostrando el montaje (setup) utilizado para ellos, en la Figura 6.1.» Capítulo 7 (p. 71): «Esta sección recapitulará el cumplimiento de los objetivos planteados en la Sección 1 gracias a las tecnologías usadas, así como la relevancia de los vehículos automatizados en la experimentación 5G y posibles mejoras para el proyecto.»
  - Las secciones también suelen abrir con una frase-anuncio: «Se describen a continuación los diferentes componentes de hardware con los que cuenta AWS DeepRacer EVO [8]:» (p. 41); «Se explica a continuación la configuración de Prometheus que se realiza mediante la copia del archivo prometheus.yml (…)» (p. 56); «Este apartado explicará los pasos a seguir para la reproducibilidad del experimento, otro de los objetivos clave de este proyecto.» (p. 59).
- **Cierre de capítulos:** ningún capítulo cierra con resumen o conclusión parcial propiamente dicha; terminan con el último contenido. Excepciones parciales: el Capítulo 1 cierra con el mapa del documento (pp. 27–29); la sección 5.4 cierra con un párrafo de recapitulación: «Como recopilación de lo explicado anteriormente, el repositorio hace uso de las herramientas de Grafana y Prometheus. Una vez se instalan, el archivo grafana.ini configura la base de Grafana, y se gestiona importando los datasources y el dashboard a utilizar con import dashboard.sh e import datasources.sh. Grafana visualizará los contenidos que se recojan con Prometheus. (…) Mientras se realizan las mediciones, el coche estará en movimiento con el archivo de ruta seleccionado.» (pp. 58–59); el Capítulo 6 cierra con una frase valorativa (p. 69, véase J).
- **Cómo se nombran los capítulos en el texto:** casi siempre «Sección N» (17 veces: «la Sección 2 explica la Planificación temporal y Costes del proyecto», «como ya se ha explicado en la Sección 4», «como se ha detallado en la Sección 6»); «Capítulo» solo en los encabezados y en «en el siguiente capítulo» (p. 41). Además «la subsección 5.5.» (p. 48), «Este apartado» (p. 59), «el apartado Installation» (p. 59). A los apéndices: «en Apéndice I», «en el Apéndice I» (19 referencias).

## E. Figuras

- **Número total: 14.** Numeración **por capítulo**: 2.1; 5.1–5.8; 6.1–6.5. Ninguna en los capítulos 1, 3, 4 y 7.
- **Formato literal del pie:** «Figura N.N: Texto» — dos puntos tras el número, inicial mayúscula. Punto final INCOHERENTE: con punto en 5.3, 5.4, 5.5, 5.6, 6.1, 6.2, 6.3, 6.4, 6.5; sin punto en 2.1, 5.1, 5.2, 5.7, 5.8. Ejemplos: «Figura 2.1: Diagrama de Gantt del Proyecto» (p. 32); «Figura 5.1: Diseño propuesto para el proyecto» (p. 47); «Figura 5.3: Payload de la trama solicitud a la API cuando se ejecuta set manual mode().» (p. 52); «Figura 6.4: Tráfico acumulativo recibido del servidor.» (p. 69).
- **Pie corto para el índice** (`\caption[corto]{largo}`): índice «6.1 Montaje del coche.» frente a pie «Figura 6.1: La imagen izquierda muestra una vista superior, mientras que la derecha muestra una vista lateral.» (p. 65); índice «6.3 Gráficos del experimento de interior.» frente a pie «Figura 6.3: Provenientes de los paneles de los dashboards configurados en Grafana, que representan el tráfico de red de una conexión 5G NR y WiFi.» (p. 67); índice «5.3 Solicitud set manual mode()» frente a «Figura 5.3: Payload de la trama solicitud a la API cuando se ejecuta set manual mode().».
- **Posición del pie: DEBAJO de la figura** (p. 32: la figura va tras la lista de tareas y el pie justo antes de «2.2. Costes»; p. 49: pie en la parte superior de la página inmediatamente tras la imagen y antes del texto; p. 52: dos figuras apiladas, cada una con su pie debajo). Las figuras 6.4 y 6.5 van **una junto a otra en dos columnas**, cada una con su propio pie (p. 69).
- **Cómo se referencian en el texto** (literales):
  1. «La planificación temporal se presenta como Diagrama de Gantt en la Figura 2.1.» (p. 31)
  2. «Se comienza mostrando el montaje (setup) utilizado para ellos, en la Figura 6.1.» (p. 65)
  3. «La Figura 6.3 muestra dos gráficos provenientes de los paneles de los dashboards configurados en Grafana, que representan el tráfico de red de una conexión 5G NR y WiFi.» (p. 68)
  4. «En la Figura 6.4, se muestra el tráfico acumulativo recibido del servidor durante el experimento en exterior.» (p. 69)
  5. Fórmula repetida en el capítulo 5: «El contenido de la solicitud se muestra en la Figura 4.3.» (p. 51), «La solicitud se muestra en la Figura 4.6.» (p. 53), «como se muestra en la Figura 4.7» (p. 60), «Se muestra un extracto en la Figura 4.8, a modo de ejemplo» (p. 61).
  - **ERROR sistemático:** las ocho referencias del capítulo 5 apuntan a «Figura 4.x» cuando las figuras son 5.x (números escritos a mano, no con `\ref`); además «la figura 4.2» en minúscula (p. 48) y «Este se muestre [sic] en la Figura 4.1» (p. 47).
- **Fuente:** no se indica nunca («Fuente:», «elaboración propia», «extraída de [n]» no aparecen). Todo el material gráfico es propio (capturas y fotos del autor).
- **Tipos de figura (inferidos de pies y texto):** diagrama de Gantt (2.1); diagrama de bloques del diseño (5.1); diagrama de flujo (5.2); capturas de JSON de las peticiones a la API (5.3–5.6); captura de pantalla de Grafana (5.7); extracto del fichero de ruta como imagen (5.8); fotografías del montaje del coche, dos vistas (6.1); composición de capturas (cámara + consola + Grafana) (6.2); gráficas de Grafana (6.3, 6.4, 6.5). No hay gráficas generadas por el autor con herramienta propia (matplotlib, etc.): los resultados son capturas de paneles.
- **Descripción de las figuras:** tras la figura, el texto la describe elemento a elemento: «La imagen izquierda muestra una vista superior. (…) La imagen derecha muestra una vista lateral.» (pp. 65–66); «El gráfico izquierdo muestra, como indica el título, el tráfico recibido del servidor (…) El gráfico derecho muestra por su parte el tráfico enviado al servidor» (p. 68); «Como se indica en la leyenda, el tráfico de 5G NR está representado en color rojo y el WiFi en color azul.» (p. 68).

## F. Tablas

- **Número: 1.** «Cuadro 2.1: Estimación del coste total del proyecto.» (p. 35). Denominación **«Cuadro»** (no «Tabla») e **«Índice de cuadros»**.
- **Pie: DEBAJO de la tabla**, formato «Cuadro N.N: Texto.» con punto final.
- **Referencia en el texto** (única, literal): «Como se observa en el Cuadro 2.1., el total ha sido de ocho mil seiscientos cuarenta euros con ochenta y siete céntimos.» (p. 35). Nótese la doble puntuación «2.1.,» y que la cifra se escribe en letras en el texto y en número en la tabla.
- **Contenido:** tres columnas «Concepto | Cantidad | Coste (EUR)», con filas agrupadas por bloques «Costes hardware» (AWS DeepRacer EVO, 6 meses (amortización), 91.33; Teléfono móvil Xiaomi 12, 133.17; ASUS ExpertCenter D7 SFF, 747.00; Monitor Xiaomi A27i, 41.50; Total hardware 1013.00), «Costes software» (Suscripción a AWS, 6 meses, 97.87; Contrato operador móvil O2, 1 mes, 30.00; Herramientas de Ubuntu, 0.00; Total software 127.87), «Costes humanos» (Ángel Marín Munuera, 300 horas, 6000.00; Juan José Ramos Muñoz, 10 horas, 500.00; Jorge Navarro Ortiz, 20 horas, 1000.00; Total costes humanos 7500.00) y «Coste total del proyecto 8640.87». Decimales con **punto**, dos decimales.
- No hay tablas de resultados, de requisitos, de comparación del estado del arte ni de especificaciones (las especificaciones hardware se dan como lista, pp. 41–42).

## G. Ecuaciones

- **No hay ecuaciones numeradas** (ninguna «(N.N)»). Hay **fórmulas expuestas sin numerar**, solo en el capítulo de costes: tres fórmulas de amortización (p. 33) y líneas de cálculo (p. 34). Se introducen con una frase que termina en punto y la fórmula va centrada debajo. Ejemplo literal (p. 33): «El Amazon DeepRacer EVO cuesta aproximadamente 548 euros, considerando el precio de venta en dólares (598 USD) y aplicando una tasa de conversión aproximada de 1 USD = 0.92 EUR [9]. Estimando una vida útil de 3 años, como es común en la mayoría de equipos electrónicos, se imputa un costo amortizado.» y debajo: «Costo amortizado 6 meses = (548 EUR / 3 años) × (6 meses / 12 meses/año) = 91.33 EUR».
- **Definición de variables:** no hay símbolos; las magnitudes se escriben en palabras con unidades dentro de la propia fórmula («Tarifa = 20 EUR/hora   Tiempo dedicado = 12 créditos × 25 horas/crédito = 300 horas», «Costo total = 300 horas × 20 EUR/hora = 6000 EUR», p. 34; «Total en EUR = 106.38 USD × 0.92 EUR/USD ≈ 97.87 EUR», p. 34).
- **Símbolos en línea:** «×», «≈», signo menos tipográfico «−» en los valores de calibración («Dirección central: −1», «Giro máximo a la derecha: −12», p. 66). Unidades pegadas al número sin espacio («7.4V», «1000mAh», «13600mAh», p. 41–42) frente a «75 Mb/s», «4 Mb/s», «30 kb/s» con espacio (pp. 68–69). Decimales con punto en todo el documento («595.73 billones», «0.6», «1.0»).

## H. Código y comandos

- **Listados en el cuerpo:** ninguno en bloque largo. Comandos de una línea se muestran como línea aparte (sin pie ni numeración): «pip3 install awsdeepracer control» (p. 59; en el original `awsdeepracer_control`), «client = awsdeepracer control.Client(password="XXX", ip="localhost")» (p. 59), «[dashboards] min refresh interval = 1s» (p. 56; original `min_refresh_interval`), «jq . ruta.json» (p. 64), «sudo su / cd /root/.ros/logs / rm *» (tres líneas, p. 63).
- **Comandos en línea dentro de la frase:** «En el caso de ping -c 4 192.168.222.1 | tee -a ping.log envía 4 paquetes de solicitud de eco a la dirección IP 192.168.222.1.» (p. 50); «En el script de ruta, se ejecuta iperf3 -c 192.168.222.1 -t 10, que ejecuta una prueba de rendimiento (…) durante 10 segundos.» (p. 50); «se comienza la ruta con el vehículo mediante python3 ./control manual.py -r ruta.json» (p. 58); «se ejecuta ss -i -t» (p. 58); «se puede comprobar la memoria que ocupan si, dentro del directorio, se ejecuta du -hs.» (p. 63). Los comandos se explican luego **opción por opción** en viñetas anidadas: «• ping: ejecuta la herramienta ping. • -c 4: esta opción le indica que se envíen 4 paquetes de solicitud de eco. (…) • 192.168.222.1: es la dirección IP del dispositivo de destino» (p. 50), y los operadores en lista: «|: operador de tubería (…) tee: comando de Unix (…) -a: indica que se agregue la salida al final (…) ping.log: nombre del archivo» (p. 50).
- **Nombres de ficheros, métodos y campos en el texto:** se escriben tal cual, con paréntesis en los métodos: «set manual mode()», «start car()», «move(angle, throttle, max speed)», «stop car()», «run command thread(command)», «main»; ficheros «prometheus.yml», «grafana.ini», «ss exporter.py», «start stats.sh», «README.md», «ruta.json»; campos JSON «steps», «description», «action», «duration», «params», «command», «message», «steering angle», «throttle», «max speed». La pérdida de guiones bajos en la extracción indica que se compusieron con `\_` en la fuente de texto (redonda o cursiva), no en monoespaciada; si van en cursiva o monoespaciada **no es determinable** desde el texto. Hay indicios de cursiva para algún término («Iperf :» con el espacio típico de la corrección itálica, p. 50) y para las expansiones inglesas de las siglas. Comillas simples tipográficas para citar literales de interfaz: «mediante la herramienta ‘Inspeccionar elemento’» (p. 51), «se ha excluido ‘ip netns exec MPTCPns’» (p. 59), «Con ’relativa’ se quiere decir» (p. 52).
- **Apéndices (listados completos, paquete `listings`, numeración de líneas, monoespaciada):** 15 ficheros volcados íntegros. Longitudes: README 29 líneas (p. 75); prometheusOriginal.yml 37 (p. 76); **grafanaOriginal.ini 975 líneas = 31 páginas (pp. 77–107), casi todo comentarios del fichero por defecto**; importdatasources 8 líneas; importdashboards 3; startstats 16; ss_exporterOriginal 102 (pp. 108–110); control_manual.py 71 (pp. 111–112); ruta.json 87 (pp. 112–114); prometheusModificado 37; ss_exporterModificado 102; start_statsModificado 16; stop_statsModificado 21; **dashboard JSON 866 líneas = 19 páginas (pp. 118–137)**; aaModificado 1 línea; camara.py 27. Cada uno va precedido de la misma frase: «A continuación se muestra el contenido del archivo X:» / «…del script X:». **Solo uno lleva pie: «Listing 1: Script para el control manual del AWS DeepRacer» (p. 111)**, en inglés (valor por defecto del paquete). El listado de `control_manual.py` contiene la contraseña real de la consola del coche (contraseña en claro en el código, p. 111; aquí se omite) mientras el cuerpo dice sustituir «XXX» (p. 59).
- **URL en el cuerpo:** una sola, como parte de una explicación de código: «http://localhost:8080/stream?topic=/camera_pkg/display_mjpeg» (p. 62). El resto de URL van solo en la bibliografía.

## I. Citas y bibliografía

- **Estilo en el texto:** numérico entre corchetes **[n]**, un número por corchete (no hay «[1, 2]» ni rangos), por **orden de aparición** (estilo `unsrt`): capítulo 1 usa [1]–[8], capítulo 2 [9]–[13], capítulo 3 [14]–[20], capítulo 4 [21]–[28], capítulo 5 [29]–[37], capítulos 6 y 7 [38]. Posición: al final de la frase antes del punto («…con un tamaño de mercado de 50.63 billones de dólares [4].», p. 23) o tras el sintagma al que afecta («Presenta mejoras sustanciales en la velocidad, latencia y eficiencia [1], pudiendo…», p. 23). En el estado del arte la cita funciona como sujeto o complemento: «[14] presenta un método para evaluar la cobertura de redes 5G mediante el uso de UAVs.» (p. 37), «En [15], se explica cómo 5G brinda…» (p. 37), «En el TFG [18], se expone el funcionamiento de DeepRacer…» (p. 39), «Se hará uso del repositorio [29]. El repositorio en cuestión es una edición de [30], cuyo funcionamiento se explica en [31].» (p. 51). Sin autor-año, sin superíndices, sin notas al pie.
- **Recuento:** 38 referencias; 43 citas en el cuerpo (cap. 1: 8; cap. 2: 6; cap. 3: 7; cap. 4: 10; cap. 5: 10; cap. 6: 1; cap. 7: 1). Repetidas: [8], [9], [23], [29], [38]. Ninguna cita en los apéndices ni en resumen/abstract. **Concentración:** la mayor densidad relativa está en el estado del arte (7 citas en ~1150 palabras), pero el mayor número absoluto está en los capítulos 4 (una referencia por tecnología) y 5 (repositorios, documentación, foros de soporte); el capítulo 2 cita páginas de precios para cada coste.
- **Orden de la bibliografía:** por orden de aparición (coincide con el numérico).
- **Formato literal de tres entradas** (pp. 139–141):
  - Artículo: «[1] J.K. Verma D.S. Duhan, U. Shrivastava. A study on 5g technology and its applications in telecommunications. IEEE Access, 2022. Disponible en https://ieeexplore.ieee.org/document/9752402 (último acceso el 20/06/2024).»
  - Revista/entidad (no hay libros ni normas): «[6] IEEE. Service level agreement. IEEE Communications Magazine, 2022. Disponible en https://ieeexplore.ieee.org (último acceso el 20/06/2024).»
  - Web con fecha de acceso: «[23] Prometheus. Prometheus concepts, 2023. Disponible en https://prometheus.io (último acceso el 20/06/2024).»
  - Autorreferencia a material propio: «[38] Ángel Marín Munuera. Vídeo demostración del experimento en interior, 2024. Disponible en https://drive.google.com/file/d/… (último acceso el 24/06/2024).»
- **Patrón de entrada:** «[n] Autor o Entidad. Título con solo la inicial en mayúscula (BibTeX). Revista (si la hay), año. Disponible en URL (último acceso el dd/mm/aaaa).». Nombre de revista probablemente en cursiva (no determinable). Encabezado «Bibliografía» sin numerar (p. 139), cabecera corrida «BIBLIOGRAFÍA».
- **Proporción webs/documentación frente a artículos:** las 38 entradas (100 %) llevan «Disponible en URL (último acceso …)». Por tipo: ~5 artículos o revistas citados a través de la web ([1], [6], [14]–[17]), 2 TFG ajenos ([18], [19]), 1 publicación en LinkedIn citada como TFG ([20]) y otra como tutorial ([31]), 3 repositorios GitHub ([29], [30], [32]), 5 páginas de precios ([9]–[13]), 4 páginas de mercado/consultoras ([2]–[5], [7]), ~12 páginas de documentación oficial (AWS, ROS, Prometheus, Grafana, Python, Oracle/JSON, Git, GitHub, repost.aws, Baeldung) y 1 vídeo propio. Hay un duplicado exacto ([23] = [33]). Varias entradas tienen como «autor» el portal («IEEE», «ScienceDirect», «LinkedIn», «MediaMarkt») y el orden de autores de [1] está desordenado. Es la parte más débil del documento.

## J. Registro y redacción

- **Persona y voz:** impersonal con **«se»** de forma casi exclusiva («se ha» 45 veces, «se han» 14, «se puede» 20, «se debe» 17, «se realiza/realizó/realizan» 14 en pp. 23–73). El trabajo se nombra en tercera persona: «este proyecto», «este TFG», «este trabajo», «este documento». Primera persona del plural casi inexistente: «algo de lo que se hará uso en nuestro proyecto» (p. 58), «Aplicado al caso limitado en el que nos encontramos» (p. 43), «porque estamos en interior y estamos conectados a la red de un operador real» (p. 68). Cero «hemos», «realizamos», «podemos». Primera persona del singular solo en la autorización («Yo, …, autorizo») y en los agradecimientos («mi familia»).
- **Tiempos verbales dominantes:** Introducción y Tecnologías: presente («5G es la denominación…», «Prometheus [23] es una plataforma…»). Planificación: pretérito perfecto y pasado simple («El proyecto ha tenido una duración total de seis meses», «se hizo uso de una gran cantidad de recursos multimedia», «se tuvo que invertir»). Estado del arte: presente para lo que dice cada trabajo y perfecto/futuro para posicionar el propio («Este proyecto ha contemplado las medidas de redes 5G.», «En este proyecto, las medidas realizadas serán de redes 5G»). **Diseño e implementación: FUTURO y presente** —rasgo muy marcado—: «Se medirán las estadísticas», «se hará uso de dos herramientas», «ambas enviarán», «Esta recolección estará automatizada», «será necesario crear una clase cliente», «El bucle (…) continúa hasta que se completen todos los pasos» (unas 125 formas en -rá/-rán en pp. 23–73 frente a unas pocas decenas de pasados). Experimentación: pasado simple y perfecto («tuvo lugar en la ETSIIT», «se utilizó uno de los equipos del despacho 2.19», «se pudo visualizar en tiempo real», «Se ha medido el bitrate»). Conclusión: perfecto y presente («ha quedado demostrado», «el experimento en su conjunto está automatizado», «han sido satisfactorios»).
- **Párrafos y frases (pp. 23–73, medidos sobre el layout):** 222 párrafos de cuerpo; **2,8 frases por párrafo de media (mediana 2)**; 63 palabras por párrafo de media (mediana 48; mínimo 15, máximo 333 —la lista de modificaciones de la p. 60—). Frases de **21,6 palabras de media** (mediana 20); solo el 4 % supera las 40 palabras; la más larga, 63 palabras (p. 38). Sintaxis académica con subordinadas y gerundios encadenados: «Se demuestra que los drones pueden realizar mediciones de forma precisa, pero existen grandes desafíos con la precisión de los sistemas de posicionamiento y la estabilidad de las mediciones debido a la naturaleza del vehículo.» (p. 37); «…debiendo ser sistemático, automatizado y repetible», «necesitando mayores garantías…», «remarcando la casi inexistencia de trabajos…» (pp. 37–38).
- **Listas:** muy frecuentes, unas 14 en 51 páginas, SIEMPRE del tipo «**Término de entrada:** explicación en uno o varios párrafos» (estilo `description`; el término va probablemente en negrita, no determinable). Dónde y para qué: aplicaciones de los vehículos (p. 24, 3 ítems); **objetivos (p. 26, 7 ítems)**; tareas de la planificación (pp. 31–32, 8); costes hardware (p. 33, 4), software (p. 34, 3) y humanos (p. 34, 3); componentes hardware (pp. 41–42, 11) y software (pp. 42–43, 2 con 4 viñetas «•» anidadas: Amazon S3, CloudWatch, IoT Core, Kinesis); herramientas del fichero de ruta (pp. 49–50, Ping e Iperf con sub-viñetas «•» por opción); métodos de la API (pp. 51–53, 4); modificaciones de ficheros (pp. 59–60, 7); pasos de operación (pp. 61–62, 3); errores comunes (pp. 63–64, 4); **conclusiones por objetivo (pp. 71–72, los mismos 7 ítems que los objetivos)**. **No hay ninguna lista numerada.** Las viñetas «•» solo aparecen en segundo nivel (10 en total).
- **Negrita/cursiva en el cuerpo:** no determinables desde el texto, salvo indicios de cursiva para las expansiones inglesas de las siglas y para algún término («Iperf»). Lo que sí se ve: anglicismos SIN comillas ni marca visible en la extracción: «setup», «scraping», «dashboards», «datasources», «stream», «fading», «handover», «downlink», «uplink», «logs», «scripts», «refresh», «targets», «joystick», «smartphone», «bitrate», «namespaces», «hebras» (castellano para threads). Patrón habitual: término español seguido del inglés entre paréntesis la primera vez: «el montaje (setup)», «espacios de nombres (namespaces)», «proceso denominado scraping», «los paneles, dashboards, son…».
- **Siglas:** lista de «Abreviaciones y notaciones utilizadas» (pp. 19–21) con expansión español + inglés. En el texto muchas se usan sin expandir (UGV, UAV, 5G, QoS, KPI, SLA, MEC, RSRP, LTE) y algunas se expanden al primer uso («el Internet de las cosas, también conocido como IoT», p. 23; «parámetros que caracterizan a la red, denominados KPIs [5]», p. 25; «LiDAR: siglas de Light Detection and Ranging», p. 42; «Robot Operating System [22]», p. 43). Plural con «s» pegada: «SLAs», «UAVs», «APIs», «KPIs», «TFG» invariable («Estos TFG no profundizan»).
- **Nivel de detalle técnico:** alto en el capítulo 5 (puertos concretos 9090/9100/8080/18080/3000, nombres de ficheros, campos JSON, explicación línea a línea de una expresión PromQL: «Sigue la sintaxis rate(vector[Interval]). En este caso, el vector es node network device bytes total…», p. 57); medio-enciclopédico en el 4; bajo en cifras en el 6 (cuatro valores en total: ~75 Mb/s y 4 Mb/s en interior; 30 kb/s y 4 Mb/s en exterior), sin tablas de resultados ni estadística.
- **Cómo se formulan los objetivos:** introducidos por «Una vez introducidas las dos tecnologías en las que se va a basar este TFG, se expondrán los objetivos del mismo:» (pp. 25–26) y una lista de 7 entradas con término + dos puntos: «Mediciones experimentales de 5G: objetivo principal, se pretende poder realizar medidas experimentales de rendimiento de redes 5G de forma automatizada con un vehículo terrestre en el que se puede configurar una ruta.» / «Automatización: …» / «Enfocado al usuario: …» / «Reproducibilidad: …» / «Tiempo real: …» / «Conexión en local: …» / «Bajo costo: …». Cierre: «Expuestos estos objetivos, se introduce el vehículo automatizado que ejecutará la medición de redes 5G: AWS DeepRacer EVO.» (p. 27). **Requisitos:** no se formalizan; lo más parecido son los pasos de «5.5.1. Preparación de entorno». **Resultados:** número + interpretación causal en la misma frase o la siguiente: «El tráfico de 5G, en rojo, muestra una velocidad constante alrededor de 75 Mb/s, ya que el tráfico generado por iperf se enviaba desde el servidor hacia el coche.» (p. 68); «Las velocidades obtenidas son considerablemente más bajas de lo esperado. Esto se debe, primordialmente, al entorno interior en el que se ha realizado el experimento y a la propia naturaleza de la estación utilizada.» (p. 68). **Limitaciones:** repartidas entre el propio capítulo de experimentos («Es cierto que en ese momento el coche no estaba bien calibrado dado que era algo con lo que no se había contado», p. 67; «esta vez se tuvo que conectar mediante punto de acceso inalámbrico en lugar de USB-tethering, debido a dificultades técnicas», p. 69), la subsección «Depuración de errores» (pp. 63–64) y los «factores a tener en cuenta» de la conclusión (p. 72).
- **Frases típicas de apertura y cierre (literales):**
  1. «Para dar por concluida esta introducción, se termina detallando la estructura que sigue este TFG.» (p. 27)
  2. «Seguidamente, la Sección 2 explica la Planificación temporal y Costes del proyecto.» (p. 27)
  3. «Se comenzará la sección explicando con gran nivel de abstracción el diseño propuesto para la realización de las mediciones, de forma que se cumplan los objetivos propuestos en la Sección 1.» (p. 47)
  4. «Se pasa a la explicación del archivo de ruta que se le pasa al script de control mencionado (véase el archivo ejemplo de ruta en Apéndice I).» (p. 48)
  5. «Se continúa explicando la implementación de las mediciones 5G.» (p. 55)
  6. «Una vez preparado el entorno, se puede proceder a la operación con el vehículo.» (p. 61)
  7. «De esta forma, queda demostrada la posibilidad de realizar experimentos de mediciones de diferentes métricas 5G con vehículos automatizados.» (p. 68)
  8. «A pesar de las dificultades técnicas encontradas, los resultados obtenidos son representativos y satisfactorios, ya que se cumple el objetivo de realizar mediciones experimentales de estas redes, mostrando en este caso un mal comportamiento de la red en esta zona.» (p. 69)
- **Conectores frecuentes (recuento en pp. 23–73):** «Además» (45), «De esta forma» (14), «Es decir» (11), «Una vez …» (12: «Una vez hecho esto», «Una vez identificados los métodos a usar», «Una vez finalizada»), «Por último» (10), «Cabe destacar/mencionar/señalar» (8), «Por tanto» (5), «A continuación» (5), «Por una parte / Por otra parte» (4/3), «Sin embargo» (3), «En primer lugar / En segundo lugar», «Paralelamente», «Seguidamente», «Como aclaración», «A modo de ejemplo / aclaración / añadido», «Bien es cierto que», «He aquí», «Como es lógico», «Tal y como», «Sin entrar en detalle», «Como recopilación de lo explicado anteriormente». Referencias hacia delante: «véase … en Apéndice X» (16, siempre entre paréntesis), «como se verá más adelante», «que se explicará de forma más detallada a continuación», «Este método se detalla posteriormente». Nunca «Finalmente» ni «Por lo tanto» ni «Nótese».

### J.1 Tres párrafos representativos completos

**Diseño/arquitectura (pp. 47–48):**
> Para esta medición, se hará uso de dos herramientas de Prometheus, tecnología que, como ya se ha explicado en la Sección 4, permite la recolección de este tipo de datos. Estas dos herramientas son Node Exporter y ss, y ambas enviarán a la plataforma principal las métricas recolectadas en cada caso por diferentes puertos TCP. Esta recolección estará automatizada, iniciando y deteniendo el proceso mediante el uso de scripts.

**Resultados/evaluación (p. 68):**
> El gráfico izquierdo muestra, como indica el título, el tráfico recibido del servidor, es decir, el tráfico en sentido downlink. El eje vertical representa la velocidad de descarga en Mb/s. En el eje horizontal se representa la marca de tiempo de cada medición en formato HH:MM:SS. Se distinguen perfectamente los instantes en los que inicia el comando ping. El tráfico de 5G, en rojo, muestra una velocidad constante alrededor de 75 Mb/s, ya que el tráfico generado por iperf se enviaba desde el servidor hacia el coche.

**Conclusiones (p. 72):**
> Los resultados, además, como se ha detallado en la Sección 6, han sido satisfactorios. Aun así, es importante tener en cuenta una serie de factores en los experimentos realizados, como ya se ha mencionado en la Sección 1. Aunque se debe hacer especial énfasis en el peso que presenta el vehículo en cada experimento, pues determinará la velocidad. Y por otra parte, el nivel de batería, especialmente la del motor. Esto es debido a que a menor nivel de batería puede esperarse menor potencia en el motor, así como incluso no poder llegar a finalizar el experimento. Las condiciones meteorológicas en el caso en interior no han influido de forma lógica, y en el caso en exterior han sido favorables. Además, el terreno en ambos experimentos ha sido totalmente liso; en otro tipo de áreas, como zonas rurales, el desempeño de los experimentos podría variar. Y en general, cualquier escenario que presente dificultades para el movimiento del mismo.

## K. Capítulo a capítulo

**Capítulo 1. Introducción (pp. 23–29; ≈2360 palabras; 0 figuras, 0 cuadros; 8 citas).** Propósito: contexto y motivación, objetivos y estructura. Contenido: qué es 5G con cifras de mercado ([2]–[4]), sectores (salud, transporte, educación), tecnologías 5G (ondas milimétricas, celdas, MIMO, beamforming); vehículos automatizados y lista de aplicaciones; «sinergia bidireccional» entre ambos; medición de redes con vehículos (KPI, SLA, reproducibilidad, visión de negocio); UAV frente a UGV; lista de 7 objetivos; presentación de AWS DeepRacer EVO; mapa del documento sección a sección (pp. 27–29). Bien: objetivos explícitos y recuperables en la conclusión; mapa claro; motivación de negocio. Mal: afirmaciones de mercado con fuentes débiles; «billones» por «billions»; erratas («irrefrutable», «experienciará», «vehículos automatizado»); el mapa anuncia «Sección 7, Conclusiones» pero el capítulo se titula «Conclusión».

**Capítulo 2. Planificación y Costes (pp. 31–35; ≈1240 palabras; 1 figura, 1 cuadro; 6 citas).** Es el capítulo de planificación/presupuesto. 2.1 Planificación: duración «seis meses, desde enero hasta junio»; lista de 8 tareas (Estudio de AWS DeepRacer EVO; Estudio de AWS; Pruebas manuales; Investigación sobre el control del vehículo en local; Automatización del movimiento en local; Visualización de la cámara; Experimentación; Redacción de la memoria) y **Diagrama de Gantt como Figura 2.1** (imagen; las fechas no se dan en el texto). 2.2 Costes: hardware con **amortización a 3 años imputando 6 meses** (DeepRacer 548 EUR → 91.33; Xiaomi 12 799 EUR → 133.17; monitor 249 EUR → 41.50; el PC ASUS 747 EUR se imputa íntegro, sin amortizar —incoherencia—), software (suscripción AWS 30 h × 3.50 USD + 10 GB × 0.023 USD/GB-mes × 6 ≈ 97.87 EUR; contrato O2 30 EUR; herramientas Ubuntu 0), humanos (**alumno: 12 créditos × 25 horas/crédito = 300 horas a 20 EUR/hora = 6000 EUR; co-director 10 h y director 20 h a 50 EUR/hora**), Cuadro 2.1 con total **8640.87 EUR**. Cada precio lleva su cita a la web del vendedor. Bien: cálculo explícito y trazable. Mal: alterna «costo/coste»; reconoce que la planificación «se ha seguido de forma aproximada»; el Gantt sin descripción.

**Capítulo 3. Estado del arte (pp. 37–39; ≈1150 palabras; 0 figuras; 7 citas).** Siete trabajos, un párrafo largo por trabajo ([14]–[17] artículos; [18], [19] TFG; [20] publicación), en presente, y **cada párrafo termina posicionando el TFG frente al trabajo**: «La experimentación se realiza, sin embargo, en 4G (…). Este proyecto ha contemplado las medidas de redes 5G.»; «En ambos se goza de automatización; no obstante, las mediciones realizadas son en frecuencias LTE, además de no contar con mediciones en tiempo real. En este proyecto, las medidas realizadas serán de redes 5G, con monitorización en tiempo real.»; «Estos TFG no profundizan en las posibles aplicaciones de estos vehículos para la medición automatizada de redes 5G.». Bien: hueco identificado trabajo a trabajo. Mal: muy corto; sin tabla comparativa; referencias de baja calidad (entradas «IEEE», «ScienceDirect» genéricas).

**Capítulo 4. Tecnologías implicadas (pp. 41–46; ≈1950 palabras; 0 figuras; 10 citas).** Catálogo: 4.1 AWS DeepRacer Evo (hardware como lista de 11 componentes con cifras; software: Ubuntu 20.04, servicios AWS en viñetas, ROS, consola y API), 4.2 Prometheus y Grafana, 4.3 Python, JSON, Shell, YAML, 4.4 Git y USB-tethering. Cada tecnología: definición en un párrafo con cita a su documentación + frase de enlace «En este trabajo, el uso de Python estará enfocado a la automatización y creación de scripts.» / «En este trabajo, JSON servirá principalmente para la automatización de rutas.». Bien: cada tecnología ligada a su uso. Mal: enciclopédico (describir Python, JSON o Git aporta poco); promete que la estación base se describe aquí (p. 28) y no aparece.

**Capítulo 5. Diseño e implementación (pp. 47–64; ≈5760 palabras, el 39 % del cuerpo; 8 figuras; 10 citas).** Núcleo técnico. 5.1 Diseño: diagrama de bloques (Fig. 5.1), flujo del fichero de movimiento (Fig. 5.2), 5.1.1 estructura del fichero de ruta (campos JSON) y explicación de ping/iperf opción a opción. 5.2 Control del coche: repositorio [29], cuatro métodos de la API con captura de cada payload (Figs. 5.3–5.6), recorrido método a método del script (`run_command`, `run_command_thread`, `main`, acciones move/stop/start). 5.3 Plataformas de medición: repositorio del tutor Jorge Navarro [32], instalación según README (Apéndice A), configuración de Prometheus (puerto 8080 → conflicto con ROS), de Grafana (única línea cambiada: `min_refresh_interval = 1s`, con justificación), scripts de importación y explicación de la expresión PromQL. 5.4 Realización de las mediciones (start/stop stats, ss_exporter, métricas Gauge) con párrafo de recapitulación. 5.5 Ejecución de la plataforma: preparación del entorno, lista de 7 ficheros modificados con «Véase … en Apéndice X» cada uno, operación en 3 pasos, depuración de 4 errores con su solución y comandos. Bien: reproducibilidad real, justificación de cada cambio, enlace sistemático a apéndices. Mal: **todas las referencias a figuras con número equivocado («Figura 4.x»)**; un bloque de texto duplicado literalmente (p. 60: «y se ha añadido también mlan0 … USB-tethering. Esta es la interfaz de la cual se medirán las prestaciones de las redes 5G» aparece dos veces seguidas); mezcla de diseño, implementación y manual de usuario; «hebras» explicadas dos veces.

**Capítulo 6. Experimentación (pp. 65–69; ≈1260 palabras; 5 figuras; 1 cita).** Montaje (fotos, Fig. 6.1) con valores de calibración en lista; vista del usuario (Fig. 6.2); 6.1 interior (pasillo de la segunda planta de la ETSIIT, despacho 2.19, Xiaomi 12 + O2 por USB-tethering; Fig. 6.3: ~75 Mb/s de bajada, 4 Mb/s de subida «debido a que se trata únicamente del tráfico generado por las confirmaciones de TCP»; causa de la baja velocidad: interior y operador real); 6.2 exterior (Villa de Otura, punto de acceso Wi-Fi por «dificultades técnicas»; Figs. 6.4–6.5: picos de 30 kb/s y 4 Mb/s; explicación: mala cobertura). Vídeo demostración [38]. Bien: describe ejes, unidades, colores y marcas temporales; reconoce fallos (calibración, cambio de conexión). Mal: una sola ejecución por escenario, sin tabla de resultados, sin estadística ni repetición, cifras del exterior poco interpretadas («30 kb/s»), valoración («representativos y satisfactorios») no respaldada.

**Capítulo 7. Conclusión (pp. 71–74; ≈1170 palabras; 0 figuras; 1 cita).** Estructura espejo de los objetivos: los 7 términos de la lista de objetivos, cada uno con el veredicto («ha quedado demostrado que…», «el experimento en su conjunto está automatizado», «los experimentos son plenamente reproducibles»); párrafo de factores/limitaciones (peso, batería, meteorología, terreno); párrafo sobre la sinergia; **mejoras y trabajo futuro sin epígrafe propio**: más cómputo (Raspberry Pi), Secure Boot y kernel personalizado, generación de rutas (planos interiores, Open Source Routing Machine), navegación autónoma con OpenCV (HoughLinesP, readNet/DNN), combinación UGV + UAV. Bien: correspondencia uno a uno con los objetivos, futuro concreto. Mal: título en singular; sin separar «Trabajo futuro»; varias afirmaciones fuertes para dos experimentos.

**Capítulo 8. Apéndices (pp. 75–138; ≈20 300 palabras de código, 64 páginas).** Quince volcados íntegros (véase H), con la frase «A continuación se muestra el contenido del archivo X:». Incluye 31 páginas del `grafana.ini` por defecto (casi todo comentado) y 19 páginas de JSON del dashboard. Mal: hinchazón evidente (el apéndice pesa más que el cuerpo), ficheros «Original» y «Modificado» completos en vez de diferencias, contraseña real en el código, un solo pie «Listing 1».

**Bibliografía (pp. 139–141).** 38 entradas; véase I.

## L. Particularidades UGR/ETSIIT y del tutor

- **Orden de las páginas iniciales:** portada → portadilla → resumen + palabras clave → abstract + keywords → autorización del alumno para la biblioteca (con DNI, «Fdo:», «Granada a día 20 de junio de 2024.») → informe de los directores → agradecimientos → índice general → índice de figuras + índice de cuadros → abreviaturas → capítulos.
- **Fórmulas oficiales:** autorización del alumno («Yo, …, alumno de la titulación …, con DNI …, autorizo la ubicación de la siguiente copia de mi Trabajo Fin de Grado en la biblioteca del centro para que pueda ser consultada por las personas que lo deseen.») e informe («Informan: Que el presente trabajo, titulado …, ha sido realizado bajo su supervisión por …, y autorizamos la defensa de dicho trabajo ante el tribunal que corresponda. Y para que conste, expiden y firman el presente informe en Granada en junio de 2024.»). **Mención al tribunal:** «ante el tribunal que corresponda» (p. 13). **Firma:** líneas «Fdo: Ángel Marín Munuera» y «El director:» + «Jorge Navarro Ortiz» (si hay firma manuscrita escaneada no es determinable). **DNI:** presente en la autorización (p. 11). **«Granada, mes de año»:** sí, en portada («Granada, junio de 2024») y en el informe («en Granada en junio de 2024»).
- **Nombre del tutor:** «Juan J. Ramos Muñoz» en portada, portadilla e informe; «Juan José Ramos Muñoz» en el capítulo de costes y en el cuadro. Tratamiento «D.». Cargo «Profesor Titular de Universidad». Rol «Directores» en portada (no «Tutores»); «co-director del proyecto» en costes. **Departamento:** «Departamento Teoría de la Señal, Telemática y Comunicaciones» (sin «de»), «Área de Ingeniería Telemática».
- **Rasgos que parecen preferencia del tutor/escuela (inferencias con su evidencia):**
  1. **Capítulo 2 «Planificación y Costes» inmediatamente tras la introducción**, con Gantt, costes hardware amortizados (vida útil 3 años), software, humanos (alumno 12 ECTS × 25 h = 300 h a 20 EUR/h; directores a 50 EUR/h) y cuadro total. Es el único cuadro del TFG, lo que sugiere que es un bloque exigido más que una elección del alumno.
  2. **«Estado del arte» como capítulo breve independiente** en el que cada trabajo acaba con el hueco que este TFG cubre.
  3. **«Tecnologías implicadas» como capítulo propio**, previo al diseño.
  4. **Objetivos en lista dentro de la introducción y conclusión que los repasa uno a uno** con el mismo encabezado de cada ítem.
  5. **Reproducibilidad como objetivo explícito** y guía de ejecución dentro del capítulo técnico (5.5) con depuración de errores.
  6. **Uso del repositorio y la plataforma de monitorización del propio grupo** (repositorio de Jorge Navarro [32]: Prometheus + Grafana + ss_exporter): en el TFG de Daniel es análogo reutilizar infraestructura/herramientas del grupo citándolas.
  7. **Extensión:** cuerpo de ~51 páginas (~14 900 palabras) + apéndices (64 páginas); la longitud total la dan los apéndices.
  8. **Estilo de conclusiones:** sin autocrítica estadística, veredicto por objetivo, factores de influencia y mejoras concretas; tono afirmativo («ha quedado demostrado», «plenamente reproducibles»).
  9. **Mapa del documento al final de la introducción** describiendo cada «Sección».
  10. **Lista de abreviaturas** con expansión español/inglés al principio.
- **Sello de la plantilla ETSIIT:** cabeceras corridas, «Cuadro», folio centrado en aperturas, páginas pares en blanco, índice de figuras y de cuadros en la misma página, apéndices como capítulo 8, y los marcadores sin rellenar en la página del abstract.

## M. Cifras globales

- **Páginas (PDF):** 143 en total. Preliminares pp. 1–22 (22 páginas, 8 de ellas en blanco: 2, 4, 6, 8, 10, 12, 14, 22; la p. 3 casi en blanco). Cuerpo pp. 23–74 (52 páginas, 4 en blanco: 30, 36, 40, 70; 48 con texto). Apéndices pp. 75–138 (64 páginas). Bibliografía pp. 139–141 (3 páginas). Blancas finales 142–143. Páginas impresas: el cuerpo va de la 19 a la 70; la bibliografía de la 135 a la 137.
- **Figuras:** 14 (cap. 2: 1; cap. 5: 8; cap. 6: 5). **Cuadros:** 1. **Ecuaciones numeradas:** 0 (fórmulas expuestas sin numerar: 3, más ~8 líneas de cálculo). **Listados:** 15 ficheros volcados en apéndices (1 con pie «Listing 1»); 0 en el cuerpo (solo comandos de una línea). **Referencias:** 38; **citas en el texto:** 43. **Siglas en la lista:** ≈ 60. **Notas al pie:** 0. **Viñetas «•»:** 10 (todas de segundo nivel). **Listas numeradas:** 0.
- **Palabras (según `wc` sobre el texto extraído; incluyen cabeceras corridas y folios, error ≈ ±3 %):** total 38 968. Preliminares (portada–abreviaturas) 2 946. **Cuerpo (caps. 1–7) 14 892.** Apéndices 20 329 (código). Bibliografía 666. Por capítulo: 1 Introducción 2 361; 2 Planificación y Costes 1 243; 3 Estado del arte 1 154; 4 Tecnologías implicadas 1 947; 5 Diseño e implementación 5 757; 6 Experimentación 1 262; 7 Conclusión 1 168. Resumen ≈ 230 palabras; abstract ≈ 215.
- **Densidad:** ≈ 310 palabras por página de cuerpo con texto; 1 figura cada 3,4 páginas de cuerpo; 1 cita cada ≈ 350 palabras de cuerpo.

## N. Lecciones transferibles

### N.1 Reglas concretas para que una memoria nueva se parezca a esta

1. **Maquetar en LaTeX con la plantilla de la ETSIIT (clase tipo `book`, doble cara):** portada con «TRABAJO FIN DE GRADO», titulación en mayúsculas, título, «Autor», «Director/Directores», centro y «Granada, mes de año»; portadilla; página de resumen con «Palabras clave:» ANTES del «Resumen» (5 párrafos: contexto, qué se hace, cómo, resultados, futuro) y su gemela en inglés; autorización del alumno para la biblioteca con DNI, «Fdo:» y «Granada a día D de mes de año.»; informe del tutor con la fórmula «Informa(n): Que el presente trabajo, titulado …, ha sido realizado bajo su supervisión por …, y autoriza(mos) la defensa de dicho trabajo ante el tribunal que corresponda. Y para que conste, expide(n) y firma(n) el presente informe en Granada en mes de año.»; agradecimientos; índice general; índice de figuras e índice de tablas; lista de abreviaturas con expansión en español y en inglés (cursiva).
2. **Jerarquía de títulos:** «Capítulo N» + título en línea aparte; secciones «N.M. Título» y subsecciones «N.M.K. Título» (con punto tras el número en el epígrafe, sin punto en el índice); como máximo tres niveles; nada de epígrafes de cuarto nivel ni párrafos titulados.
3. **Cada capítulo abre con un párrafo-anuncio de 1–3 frases** («En esta sección se explicarán…», «Este capítulo describirá…») y la introducción termina con un mapa del documento capítulo a capítulo; los capítulos no llevan resumen final (como mucho un párrafo «Como recopilación de lo explicado anteriormente, …» al cerrar una sección larga).
4. **Capítulo 2 «Planificación y Costes» justo después de la introducción:** lista de tareas con término + dos puntos, diagrama de Gantt como Figura 2.1, costes hardware amortizados (vida útil 3 años, meses del proyecto), costes software (suscripciones, contratos), costes humanos (alumno 12 ECTS × 25 h = 300 h a 20 EUR/h; tutor a 50 EUR/h), fórmulas expuestas sin numerar con las magnitudes en palabras y unidades, y un cuadro resumen con el total referenciado con «Como se observa en el Cuadro N.N».
5. **Estado del arte corto, un párrafo por trabajo, en presente, con la cita numérica como sujeto («En [15], se explica…», «[14] presenta…»)** y cerrando cada párrafo con la diferencia respecto al propio TFG; capítulo de «Tecnologías implicadas» con una frase de enlace por tecnología («En este trabajo, X servirá para…»).
6. **Registro impersonal con «se» sin excepciones** (nada de «hemos», «nuestro», «yo»); presente para describir, pretérito perfecto para lo realizado («se ha hecho uso», «se han obtenido»), pasado simple para los hechos de los experimentos («tuvo lugar», «se utilizó»); el futuro solo si se decide imitar el rasgo del autor en el diseño (no recomendable en exceso). Conectores sobrios y repetidos: «Además», «De esta forma», «Es decir», «Por último», «Una vez …», «Cabe destacar», «Por una parte / Por otra parte».
7. **Párrafos de 2–3 frases (≈ 50–65 palabras) y frases de ≈ 20 palabras;** anglicismos sin comillas (cursiva si acaso), término español seguido del inglés entre paréntesis la primera vez («el montaje (setup)»); siglas en la lista inicial y, para las menos comunes, expansión al primer uso.
8. **Listas descriptivas «Término: explicación» (sin numeración)** para objetivos, tareas, componentes, modificaciones, pasos y conclusiones; viñetas «•» solo en segundo nivel; la conclusión repite la lista de objetivos ítem por ítem con el veredicto.
9. **Figuras:** pie DEBAJO, «Figura N.N: Texto.» (inicial mayúscula; decidir y mantener el punto final), numeración por capítulo, pie corto para el índice; cada figura se anuncia antes («se muestra en la Figura N.N», «La Figura N.N muestra…») y se describe después elemento a elemento (ejes, unidades, leyenda, colores, valor característico); sin «Fuente:» si el material es propio. Figuras pequeñas emparejadas en dos columnas con pies independientes.
10. **Tablas:** «Cuadro/Tabla N.N: Texto.» con el pie debajo (elegir «Tabla» si se traduce `\tablename`, pero ser coherente en todo el documento y en el índice); referencia «Como se observa en el Cuadro N.N».
11. **Citas numéricas [n] por orden de aparición, antes del punto**, un número por corchete; bibliografía con «Disponible en URL (último acceso el dd/mm/aaaa).» para webs; 35–40 referencias para un cuerpo de ~15 000 palabras; proteger mayúsculas en BibTeX y no duplicar entradas.
12. **Código fuera del cuerpo:** en el texto solo comandos de una línea (como línea aparte) y nombres de ficheros/métodos/campos; ficheros completos a apéndices con numeración de líneas, cada uno introducido por «A continuación se muestra el contenido del archivo X:»; en el cuerpo, «(véase … en Apéndice X)» entre paréntesis cada vez que se cite uno.
13. **Resultados:** número + causa en la misma frase («alrededor de 75 Mb/s, ya que…», «Esto se debe, primordialmente, a…»); admitir incidencias en el propio capítulo; frase final valorativa que enlace con los objetivos; en la conclusión, párrafo de «factores a tener en cuenta» y mejoras concretas con tecnologías nombradas.

### N.2 Cosas que NO aparecen en este TFG (y por tanto conviene evitar)

- Emojis, markdown, símbolos decorativos, títulos en mayúsculas dentro del cuerpo.
- Listas numeradas (ninguna); viñetas «•» en primer nivel; listas de una sola línea por ítem.
- Negritas de énfasis en el cuerpo (no detectables; en todo caso solo en los términos de entrada de las listas).
- Notas al pie (cero), ecuaciones numeradas, tablas de resultados, gráficas propias generadas por el autor, estadística (medias, intervalos, repeticiones).
- Epígrafes «Objetivos», «Metodología», «Requisitos», «Trabajo futuro» como capítulos o secciones propias.
- «Fuente: elaboración propia» en los pies; citas con autor-año; superíndices; URL en el cuerpo (salvo una técnica).
- Dedicatoria, declaración de originalidad explícita, glosario de términos, índice de listados, resumen ejecutivo.
- Primera persona («hemos», «nuestro»), preguntas retóricas, exclamaciones, frases de relleno tipo «es importante señalar que es importante».
- Tablas de código o listados largos dentro del cuerpo; capturas de código salvo la Fig. 5.8.

### N.3 Errores detectados que conviene no repetir

- Marcadores de la plantilla sin rellenar en la página del abstract («Project Title: Project Subtitle», «First name, Family name (student)»).
- **Referencias cruzadas escritas a mano:** las ocho referencias a figuras del capítulo 5 apuntan a «Figura 4.x» en vez de «5.x»; «la figura 4.2» en minúscula; «Este se muestre en la Figura 4.1». Usar siempre `\ref`/`\autoref` y «Figura» con mayúscula.
- Puntuación incoherente en los pies (unos con punto final y otros sin él) y «Cuadro 2.1.,» con doble signo.
- «Listing 1» en inglés y un solo listado con pie entre quince; cabecera corrida «ÍNDICE DE CUADROS» en las páginas de abreviaturas; Bibliografía ausente del índice general; «Índice de cuadros» si en el texto se prefiere «Tabla».
- Apéndices hinchados: 31 páginas de un fichero `.ini` por defecto casi todo comentado y 19 páginas de JSON exportado; ficheros «Original» y «Modificado» completos en vez de diferencias; **contraseña real** en un listado.
- Texto duplicado literalmente (p. 60) y erratas («irrefrutable», «experienciará», «ejecucion», «Ingenierías en Tecnologías», «billones» por «miles de millones»); alternancia «costo/coste»; «Conclusión» en el título frente a «Conclusiones» en el mapa; PC no amortizado cuando el resto del hardware sí.
- Informe con dos directores y una sola línea de firma «El director:»; nombre del tutor con dos formas («Juan J.» / «Juan José»).
- Resultados con una sola ejecución por escenario, sin tabla, sin repetición ni estadística, y valoración «representativos y satisfactorios» sin respaldo; cifras sin interpretar («30 kb/s»).
- Llamar «Sección N» a los capítulos en el texto mientras los encabezados dicen «Capítulo N»; prometer contenido que luego no aparece (la estación base en el capítulo 4).
- Descripciones enciclopédicas de herramientas de uso común (Python, JSON, Git) que no aportan al TFG.

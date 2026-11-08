# Ficha de formato y estilo — TFG 2017 Rafael González Callejas (tutor: Juan José Ramos Muñoz, codirector Jorge Navarro Ortiz)

Fuente: `docs/memoria/DE MI TUTOR JUAN JOSE RAMOS MUNOZ/2017_TFG_RafaelGonzalezCallejas.pdf` (150 páginas PDF, 35 235 palabras según `wc`).
Peso: MEDIO (tutor correcto, pero año 2017; sirve para ver qué pide el tutor de forma estable, no para copiar el formato antiguo tal cual).
Método: extracción con `pdftotext` (flujo y `-layout`), lectura íntegra del texto, metadatos y fuentes del PDF leídos del binario. Las páginas que se citan son páginas del PDF salvo que se indique "pág. impresa". Equivalencia: pág. impresa = pág. PDF − 28 (Capítulo 1 empieza en PDF 29 = impresa 1).
Convención: lo que se afirma a partir del texto se da como hecho; lo que se deduce se marca como **inferencia** con su evidencia. Cuando no se puede saber, se dice "no determinable desde el texto".

---

## A. Identificación

- **Título completo (portada, p. 1):** «Implementación de movilidad en redes 5G» con subtítulo «Simulación de movilidad con Software Defined Networking». En la segunda portada (p. 5) el subtítulo cambia a «Simulación de movilidad mediante Software Defined Networking.» (con puntos finales y «mediante» en vez de «con»). En la cabecera del resumen (p. 7) aparece unido con dos puntos: «Implementación de movilidad en redes 5G: Simulación de movilidad con Software Defined Networking». En el informe de los directores (p. 13): «Implementación de movilidad en redes 5G, Simulación de movilidad con Software Defined Networking» (con coma). Cuatro variantes del mismo título: descuido a evitar.
- **Autor:** Rafael González Callejas (en el abstract, p. 9, solo «Rafael González»).
- **Directores (literal «Directores», no «Tutor»):** Jorge Navarro Ortiz y Juan José Ramos Muñoz. El codirector principal de facto es Navarro Ortiz (Cap. 3 solo contabiliza su tutorización; agradecimientos: «A Juanjo, y en especial a Jorge»).
- **Departamento (p. 13, literal):** «Área de Ingeniería Telemática del Departamento de Teoría de la Señal, Telemática y Comunicaciones de la Universidad de Granada». No aparece en la portada.
- **Titulación literal:** portada (p. 1): «GRADO EN INGENIERÍA EN TECNOLOGÍAS DE LAS TELECOMUNICACIONES»; autorización (p. 11): «Grado en Ingeniería de Tecnologías de Telecomunicación»; Cap. 3 (p. 51): «Grado en Ingeniería de Tecnologías de las Telecomunicación». Tres grafías distintas; la oficial es la de la autorización.
- **Centro literal (p. 1):** «Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación».
- **Universidad:** «Universidad de Granada» aparece solo en las páginas de autorización (p. 11 y 13). En la portada no hay texto «Universidad de Granada»: **inferencia** de que el escudo/logo va como imagen (el PDF contiene imágenes en portada y pdftotext no las lee).
- **Fecha/curso:** portada: «Granada, Septiembre de 2017»; autorizaciones: «Granada a 12 de Septiembre de 2017.» No se indica curso académico.
- **Número de páginas:** 150 páginas PDF. Numeración impresa: preliminares en romanos (i–xi: acrónimos i–iii, índice general v–vii, figuras ix–x, cuadros xi); cuerpo 1–111; Anexo A 113–115; Bibliografía 117–119. Las páginas de resumen/abstract llevan folio arábigo propio (se ve un «4» en p. 8 y un «6» en p. 10): numeración de preliminares incoherente.
- **Herramienta de maquetación:** LaTeX, **confirmado** por metadatos del PDF: `Producer: pdflatex`, `Creator: LaTeX con el paquete ....` (hyperref en español). Evidencias adicionales: fuentes Computer Modern (CMR10 cuerpo, CMBX12 títulos, CMTI10 cursiva, CMTT10 monoespaciada, CMCSC10 versalitas); pies «Cuadro X.Y:» (nombre por defecto de babel-spanish); cabecera «Apéndice A»; líneas de puntos en los índices; partición silábica («referen-cia», «ana-lizar»); ligaduras «fi/fl»; acentos como glifos separados (codificación OT1, sin `fontenc T1`); listados con números de línea y espaciado por caracteres (paquete `listings`); páginas en blanco en el verso antes de cada capítulo (clase `book`, `openright`); bibliografía estilo IEEEtran («vol.», «no.», «pp.», «[Online]. Available:») con restos «URL{...}» de una macro `\url` no resuelta.

## B. Estructura completa en orden (páginas PDF)

| Bloque | Páginas PDF | Observaciones |
|---|---|---|
| Portada | 1 | «TRABAJO FIN DE GRADO», titulación, título, subtítulo, «Autor», «Directores», centro, «—», «Granada, Septiembre de 2017» |
| Blanco | 2 | |
| Página casi vacía | 3 | Solo contiene el número «3». Probable hoja con folio e imagen no extraíble; no determinable desde el texto |
| Blanco | 4 | |
| Segunda portada | 5 | Título, subtítulo, Autor, Directores. Sin fecha ni centro |
| Blanco | 6 | |
| Resumen + palabras clave (español) | 7–8 | Cabecera: título completo + autor; luego «Palabras clave:»; luego «Resumen» |
| Abstract + keywords (inglés) | 9–10 | Misma disposición |
| Autorización del alumno (biblioteca) | 11 | Fórmula oficial, DNI sin rellenar («XXX») |
| Blanco | 12 | |
| Informe/autorización de los directores | 13 | «Informan: … autorizamos la defensa … ante el tribunal que corresponda» |
| Blanco | 14 | |
| Agradecimientos | 15 | Sin dedicatoria separada |
| Blanco | 16 | |
| Índice de Acrónimos | 17–19 (i–iii) | 58 acrónimos, sin numerar, orden alfabético |
| Blanco | 20 | |
| Índice general | 21–23 (v–vii) | Hasta nivel 3 (subsección) |
| Blanco | 24 | |
| Índice de figuras | 25–26 (ix–x) | Títulos cortos distintos de los pies reales |
| Índice de cuadros | 27 (xi) | Título «Índice de cuadros» pero el índice general lo llama «Lista de tablas» |
| Blanco | 28 | |
| Capítulo 1 Introducción | 29–35 (1–7) | |
| Blanco | 36 | |
| Capítulo 2 Estado del arte | 37–45 (9–17) | |
| Blanco | 46 | |
| Capítulo 3 Planificación temporal y presupuesto | 47–56 (19–28) | |
| Capítulo 4 Requisitos de funcionalidad y decisiones de diseño | 57–60 (29–32) | |
| Capítulo 5 Tecnologias aplicadas | 61–79 (33–51) | |
| Blanco | 80 | |
| Capítulo 6 Herramientas utilizadas | 81–104 (53–76) | |
| Capítulo 7 Diseño e implementación de un escenario de movilidad | 105–124 (77–96) | |
| Capítulo 8 Fase de pruebas y evaluación | 125–135 (97–107) | |
| Blanco | 136 | |
| Capítulo 9 Conclusiones y vías futuras | 137–139 (109–111) | |
| Blanco | 140 | |
| Apéndice A / Anexo A: Topología en Mininet | 141–143 (113–115) | Script Python completo |
| Blanco | 144 | |
| Bibliografía | 145–147 (117–119) | 27 entradas |
| Blanco | 148–150 | |

**Faltan:** dedicatoria (no hay página propia), declaración de originalidad del alumno (solo hay autorización de depósito en biblioteca), glosario de términos (solo acrónimos), índice de listados/código, lista de símbolos, página de «Capítulo 10: Bibliografía» (el apartado 1.5.10 la anuncia como capítulo, pero la bibliografía va sin numerar).

### Texto literal de las páginas oficiales

**Autorización del alumno (p. 11):**

> Yo, Rafael González Callejas, alumno del Grado en Ingeniería de Tecnologías de Telecomunicación de la Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación de la Universidad de Granada, con DNI XXX, autorizo la ubicación de la siguiente copia de mi Trabajo Fin de Grado en la biblioteca del centro para que pueda ser consultada por las personas que lo deseen.
>
> Fdo: Rafael González Callejas
>
> Granada a 12 de Septiembre de 2017.

(En la maquetación, el nombre, la titulación, el centro y la universidad van resaltados —**inferencia**: negrita—, el «Fdo:» a la izquierda y la fecha alineada a la derecha.)

**Informe de los directores (p. 13):**

> D. Jorge Navarro Ortiz, Profesor del Área de Ingeniería Telemática del Departamento de Teoría de la Señal, Telemática y Comunicaciones de la Universidad de Granada.
>
> D. Juan José Ramos Muñoz, Profesor del Área de Ingeniería Telemática del Departamento Teoría de la señal, Telemática y Comunicaciones de la Universidad de Granada.
>
> Informan:
>
> Que el presente trabajo, titulado Implementación de movilidad en redes 5G, Simulación de movilidad con Software Defined Networking, ha sido realizado bajo su supervisión por Rafael González Callejas, y autorizamos la defensa de dicho trabajo ante el tribunal que corresponda.
>
> Y para que conste, expiden y firman el presente informe en Granada a 12 de Septiembre de 2017.
>
> Los directores:
>
> Jorge Navarro Ortiz          Juan José Ramos Muñoz

**Palabras clave (p. 7):** «Palabras clave: (Software Defined Network) SDN, Movilidad, Handover, OpenDayLight, Mininet, Framework, OpenFlow, 5G, Controlador, Java.»

**Resumen (p. 7–8), íntegro:**

> En un mundo marcado por el enorme crecimiento de los dispositivos con conexión a Internet, donde cada vez estamos más conectados y usamos los recursos de la red en la realización de las tareas más cotidianas, las futuras redes de comunicaciones deben tender hacia una mayor simplicación y flexibilidad, utilizando un hardware más sencillo e interoperable y menos costoso, invirtiendo en sistemas de gestión más sofisticados y eficientes que gestionen dicha demanda de recursos de la forma más inteligente posible.
>
> En este sentido, tecnologías como las redes definidas por software se postulan como una alternativa en vías de desarrollo para satisfacer las nuevas necesidades y requerimientos del ecosistema de red. La filosofía detrás de las redes definidas por software es la de separar el plano de control del plano de datos de las redes de comunicaciones, de forma que toda la inteligencia de la red se centralice y se gestione a nivel software mientras los dispositivos de red se vuelven más simples y compatibles.
>
> De la mano de esta centralización y gestión de los recursos de red a nivel software, OpenDayLight surge como un framework altamente mantenido y soportado por un consorcio de importantes fabricantes y operadoras de red, con las herramientas necesarias para gestionar todo el flujo de red, obtener estadísticas y facilitar el desarrollo de la inteligencia de red a través de aplicaciones y plugins específicamente diseñados para consumir los datos generados por los dispositivos de red y aplicar las reglas necesarias para generar el comportamiento que se desee conseguir.
>
> Al hilo del desarrollo de estas tecnologías, OpenFlow aparece de la mano de la (Open Networking Foundation) ONF como un protocolo pensado para establecer la comunicación entre el plano de control y el plano de datos de una red, facilitando la instalación y borrado de flujos y la gestión de las tablas de flujo de los switches compatibles con esta tecnología.
>
> En este contexto, este proyecto de fin de grado está destinado a estudiar y emular la gestión de movilidad en la que será la quinta generación de redes móviles. Trataremos de emular el proceso de movilidad completo, desde el proceso de señalización, a través de aplicaciones Java, hasta la generación de un escenario usando elementos simulados con la herramienta Mininet, que nos permite utilizar switches compatibles con el protocolo OpenFlow y que está fuertemente integrada con OpenDayLight.
>
> Por supuesto, desarrollaremos un controlador integrado en OpenDayLight que se encargará del descubrimiento e instalación de las rutas de encaminamiento de los paquetes intercambiados por nuestra red, a través de la instalación de flujos por medio del protocolo OpenFlow. Trabajaremos principalmente con Java como lenguaje de programación, si bien, la generación de la topología de red se realizará en Python, y utilizaremos scripts bash para la gestión de las tarjetas de red que actuarán como puntos de acceso.

Estructura del resumen: 4 párrafos de contexto (red actual → SDN → OpenDayLight → OpenFlow) + 2 párrafos de «este proyecto» en futuro. ~520 palabras. No contiene resultados ni cifras. Es la pauta a NO copiar literalmente en lo que toca a ausencia de resultados, pero sí en estructura «contexto → tecnología → qué se hace».

**Keywords (p. 9):** «Keywords: SDN (Software Defined Network), Mobility, Handover, OpenDayLight, Framework, OpenFlow, 5G, Controller, Java.»

**Abstract (p. 9–10), íntegro (se conservan sus erratas en inglés):**

> Nowadays, with the exponential growth of devices consumming network resources, even for the most quotidian tasks, where the network claims for a more flexible and adaptative paradigm, which allows a reduction on hardware investment and pushes for a more centralized network management, the future fith generation of mobile communications is intended to develop a new philosophy of network management in order to deal with this requirements.
>
> Given this scenario, technologies such as SDN (Sofware Defined Network) are being considered as an alternative to reach the goals represented by this new network requirements. SDN philosophy is based on the division between data plane and control plane, so that, network devices can be simpler, more interopeable and cheaper since network intelligence is centralized in software based applications.
>
> According to this new paradigm, OpenDayLight arises as a versatile framework for network management, highly supported and mantained by a wide group of network manufacturers and operators. This technology is expected to be an alternative for network management, provided its capacity to extract network information so that an external application can be aware of network devices and topology and can also be able to install, delete and modify data flows depending on the desired network behaviour.
>
> Since OpenDayLight is a very useful tool for network management, a protocol that allows OpenDayLight to communicate with network devices is required. OpenFlow is the first protocol developed for this purpose by the (ONF) Open Networking Foundation. OpenFlow is responsible for the communication between the controller application, where the business inteligence is implemented, and network devices where the actions ordered by the controller are applied.
>
> Considering this evolution of network communications, this project will try to study and emulate a mobility scenario based on those new network paradigms. We will use Mininet as a tool for simulating a network topology that allows us to test the handover procedure in a 5G network, which will be controlled by an application running over OpenDayLight.
>
> During the project we will work mainly with Java, for developing all the applications and controller that take part on the simulation. We will also use Python to simulate our network topology, and bash scripts to configure network components such as wireless network interface cards.

**Agradecimientos (p. 15):** cuatro párrafos breves, tono personal («A mi familia y amigos…», «A mi madre…», «A Juanjo, y en especial a Jorge, por su dedicación, ayuda constante y predisposición, gracias a él este proyecto puede ver la luz.», «A todos, gracias.»).

## C. Índice general copiado literalmente (p. 21–23)

```
Índice general

Índice de Acrónimos                                              I
Lista de figuras                                                IX
Lista de tablas                                                 XI
1. Introducción                                                  1
   1.1. Motivación                                               1
   1.2. Objetivos                                                2
   1.3. Contexto                                                 3
        1.3.1. Introducción a la movilidad en redes 5G           3
   1.4. Importancia del modelo SDN                               4
   1.5. Estructura de la memoria                                 5
        1.5.1. Capítulo 1: Introducción                          5
        1.5.2. Capítulo 2: Estado del arte                       5
        1.5.3. Capítulo 3: Planificación y estimación de costes  5
        1.5.4. Capítulo 4: Requisitos de funcionalidad y decisiones de diseño   5
        1.5.5. Capítulo 5: Tecnologías aplicadas                 6
        1.5.6. Capítulo 6: Herramientas utilizadas               6
        1.5.7. Capítulo 7: Diseño e implementación de un escenario de movilidad 6
        1.5.8. Capítulo 8: Fase de pruebas y evaluacion          6
        1.5.9. Capítulo 9: Conclusión y vías futuras             6
        1.5.10. Capítulo 10: Bibliografía                        7
2. Estado del arte                                               9
   2.1. Comparación con otros modelos                            9
        2.1.1. Mininet-WiFi: Emulating Software-Defined Wireless Networks       9
        2.1.2. Handover Management in SDN-based Mobile Networks 12
        2.1.3. Link-level Access Cloud Architecture Design Based on SDN for 5G Networks 15
3. Planificación temporal y presupuesto                         19
   3.1. Planificación temporal                                  19
        3.1.1. División del trabajo                             20
        3.1.2. Planificación económica                          23
   3.2. Estimación de costes                                    25
        3.2.1. Coste en recursos humanos                        25
        3.2.2. Coste en recursos hardware                       26
        3.2.3. Coste en recursos software                       26
   3.3. Análisis final de planificación y costes                27
4. Requisitos de funcionalidad y decisiones de diseño           29
   4.1. Requisitos de funcionalidad                             30
        4.1.1. Decisiones de diseño                             31
5. Tecnologias aplicadas                                        33
   5.1. Redes Definidas por Software                            33
        5.1.1. Arquitectura SDN                                 34
        5.1.2. Beneficios del uso de SDN                        36
   5.2. Protocolo OpenFlow                                      37
        5.2.1. Tablas OpenFlow                                  39
        5.2.2. Canal OpenFlow                                   47
6. Herramientas utilizadas                                      53
   6.1. Mininet                                                 53
        6.1.1. ¿Por qué usar Mininet?                           53
        6.1.2. Usando Mininet                                   54
        6.1.3. Comparacion con GNS3                             57
   6.2. OpenDayLight                                            58
        6.2.1. ¿Qué es OpenDayLight?                            59
        6.2.2. Distribuciones de OpenDayLight                   60
        6.2.3. Arquitectura de OpenDayLight                     67
        6.2.4. RESTCONF y REST API                              71
7. Diseño e implementación de un escenario de movilidad         77
   7.1. Diseño e implementación de la topología de red          77
   7.2. Diseño e implementación del proceso de señalización     83
        7.2.1. Implementación en JAVA                           85
        7.2.2. Servidores para el source AP y el target AP      88
        7.2.3. Controlador integrado en OpenDayLight            90
        7.2.4. Instalador de flujos                             93
   7.3. Funciones auxiliares                                    94
8. Fase de pruebas y evaluación                                 97
   8.1. Prueba de funcionalidad: señalización y topología       97
   8.2. Pruebas de rendimiento y funcionalidad                 101
   8.3. Ping entre User Equipment (UE) y hosts                 101
   8.4. FTP entre UE y hosts                                   103
   8.5. Evaluación de resultados                               106
9. Conclusiones y vías futuras                                 109
   9.1. Conclusiones                                           109
   9.2. Vías futuras                                           110
   9.3. Valoración personal                                    111
A. Anexo A: Topología en Mininet                               113
Bibliografía                                                   119
```

Notas sobre el índice: los números de sección llevan punto final («1.1.», «1.3.1.»); los números de página van con líneas de puntos; el índice se detiene en el nivel 3 aunque el texto llega al nivel 5; la bibliografía real empieza en la pág. impresa 117, no 119 (índice desactualizado); «Lista de figuras / Lista de tablas» en el índice frente a «Índice de figuras / Índice de cuadros» en las páginas reales; el apartado 8.3 contiene la expansión automática de un acrónimo en el propio título.

## D. Títulos y numeración

- **Capítulos:** dos líneas: «Capítulo 1» en una línea y el título en la siguiente («Capítulo 1 / Introducción», p. 29). El anexo sigue la convención LaTeX: «Apéndice A / Anexo A: Topología en Mininet» (p. 141), con la palabra «Anexo» duplicando la de «Apéndice».
- **Nivel 2 y 3:** «1.1. Motivación», «1.3.1. Introducción a la movilidad en redes 5G» (número con punto final, título con mayúscula inicial solamente, salvo nombres propios y títulos de artículos en inglés que conservan sus mayúsculas: «2.1.1. Mininet-WiFi: Emulating Software-Defined Wireless Networks»). Dos títulos interrogativos: «6.1.1. ¿Por qué usar Mininet?», «6.2.1. ¿Qué es OpenDayLight?».
- **Nivel 4 (no aparece en el índice):** «2.1.2.1. SDN centralizado», «3.1.2.1. Recursos humanos», «5.2.1.1. Pipeline processing», «5.2.2.1. Mensajes del protocolo OpenFlow», «6.2.2.1. Alternativas de instalación».
- **Nivel 5:** «5.2.2.1.1 Mensajes Controlador-switch», «5.2.2.1.2 Mensajes asíncronos», «5.2.2.1.3 Mensajes simétricos» (sin punto final tras el número). Profundidad máxima usada: 5 niveles. Excesivo para un TFG; es lo que ocurre al volcar la especificación OpenFlow.
- **Epígrafes sin numerar:** sí, como títulos de párrafo en línea o en negrita: «Acción Output», «Acción Set-Queue», «Acción Drop», «Acción Group», «Acción Pop-Tag/Push-Tag», «Acción Set-Field» (p. 73–75); «Proceso de adición de flujos.» y «Proceso de borrado de flujos.» (p. 102–103); «Instalación desde ZIP:», «Instalación desde RPM:», «Imagen virtualizable:» (p. 88–89); la lista de módulos de Hydrogen («Clustering Manager :», «Container Manager :», …, p. 90) y las características de Karaf (p. 91–92) van como listas descriptivas con el término resaltado.
- **Párrafo introductorio al abrir capítulo:** sí en los capítulos 2 a 9 (texto entre el título del capítulo y el primer epígrafe numerado). El capítulo 1 es la excepción: pasa directamente a «1.1. Motivación». Dos ejemplos literales:
  - Capítulo 2 (p. 37): «El objetivo de este capítulo es dotar al lector de una amplia perspectiva sobre los estudios que se están realizando o se han realizado recientemente en el campo de la gestión de movilidad en redes 5G.» (sigue un segundo párrafo que anuncia el método y un tercero que anuncia el cierre: «Esta sección finalizará con una breve conclusión sobre las aportaciones originales que este proyecto supone en el campo de la gestión de movilidad en las futuras redes 5G.»)
  - Capítulo 7 (p. 105): «En el capítulo que nos ocupa, vamos a abordar el diseño de todas las piezas que forman el puzle de la simulación de un handover entre dos puntos de acceso de la que podría ser la futura estructura de red sobre la que se implemente la quinta generación de redes móviles.» (…) «Sin más dilaciones vamos a comenzar a analizar la topología de la red escogida y los diferentes elementos que van a formar parte de ella.»
- **Cierre con resumen/transición:** sí en los capítulos 2, 5, 6 y 7; el 8 cierra con un apartado propio «8.5. Evaluación de resultados»; los capítulos 1, 3 y 4 terminan sin cierre (el 4 acaba en una lista de viñetas). Citas literales:
  - Cap. 2 (p. 45): «Concluye de esta forma el apartado de estado del arte, donde hemos tratado de llevar a cabo una amplia visión de los estudios más interesantes que se están llevando a cabo en este campo actualmente.»
  - Cap. 5 (p. 79): «Con esto concluye el apartado destinado a la comprensión del funcionamiento de las tecnologías que van a suponer la base de nuestro proyecto, las redes definidas por software y el protocolo OpenFlow para la gestión de la comunicación entre los elementos de red y el controlador.» seguido de «En el siguiente capítulo analizaremos las herramientas utilizadas para hacer uso de estas tecnologías, Mininet, para la virtualización de redes, y OpenDayLight para gestionar las operaciones relacionadas con el controlador.»
  - Cap. 6 (p. 104): «Con esto concluye el apartado de herramientas, en el que hemos hecho un análisis de las principales funcionalidades y arquitectura de las dos piezas basicas en la implementacion de nuestro escenario de movilidad.»
  - Cap. 7 (p. 124): «Con todo ello, ya tenemos todos los componentes necesarios para realizar una emulación completa de un handover. En el siguiente apartado analizaremos el funcionamiento de las soluciones implementadas y realizaremos una pequeña comparación entre ambas, tanto en rendimiento como en escalabilidad.»
- **Cabeceras de página (p. 30–31):** páginas pares: número de página a la izquierda + «1.2. Objetivos» (sección actual); páginas impares: «Introducción» (título del capítulo) + número a la derecha. Primera página de cada capítulo sin cabecera y con folio centrado abajo.

## E. Figuras

- **Número total:** 54 (1.1; 2.1–2.6; 3.1–3.3; 5.1–5.5; 6.1–6.15; 7.1–7.11; 8.1–8.13). Capítulos 4 y 9 sin figuras. El PDF contiene 107 objetos imagen (varias figuras compuestas de más de una imagen, más el escudo de portada).
- **Numeración:** por capítulo («Figura 6.14»).
- **Formato literal del pie:** «Figura 1.1: Simulación de movilidad a realizar. Figura realizada con draw.io.» — palabra «Figura» completa, número, dos puntos, texto con mayúscula inicial. El punto final es inconsistente: con punto en «Figura 1.1: …draw.io.», «Figura 2.1: Componentes para una topología básica con interfaces Wi-Fi [6].», «Figura 8.7: Instalador de flujos: Resultados de ping.»; sin punto en «Figura 7.1: Diseño de topología de la red», «Figura 5.2: Arquitectura OpenFlow. Imagen obtenida de [8]», «Figura 8.11: FTP sin handover». Mayúsculas internas tipo inglés en algunos pies: «Criterios de Matching en OpenFlow», «Flujo de un paquete a través del Processing Pipeline».
- **Posición del pie:** debajo de la figura (**inferencia** fuerte: en el flujo de texto el pie aparece siempre después del hueco de la imagen y antes del párrafo que la comenta, p. ej. p. 56 y p. 63; es el comportamiento estándar de `\caption` tras `\includegraphics`).
- **Fuente de la figura:** se indica dentro del pie de tres maneras: cita entre corchetes al final («… Wi-Fi [6].», «Arquitectura AD-SAL [21].»), frase explícita («Imagen obtenida de [8]», «Figura tomada de [4].», «Imagen obtenida de [9]») o herramienta propia («Figura realizada con draw.io.», «Diagrama realizado con Draw.io»). No existe la fórmula «Fuente: elaboración propia». Las capturas propias no indican fuente.
- **Índice de figuras con título corto distinto del pie:** p. ej. índice «1.1. Proceso de Handover» frente a pie «Figura 1.1: Simulación de movilidad a realizar…»; índice «6.11. ODL Framework Overview» frente a pie «Visión general del framework OpenDayLight [20]». **Inferencia:** uso de `\caption[corto]{largo}`. Varios títulos cortos con erratas («Distritucion de costes», «ArquitecturaHellium», «Topologia basica»).
- **Cómo se referencian en el texto (105 menciones, 102 con «Figura» en mayúscula, 3 en minúscula: «figura 6.2», «figura 6.11», «figura 6.15»):**
  - «La Figura 1.1 ejemplifica el proceso descrito en el párrafo anterior. En ella vemos con más detalle la topología que se pretende implementar, y el cambio entre puntos de acceso a realizar.» (p. 30)
  - «Como puede verse en la Figura 2.1, tanto en el AP como en las Station (STA) se ha añadido una interfaz Wi-Fi.» (p. 38)
  - «La Figura 7.2 muestra cómo se ve la distribución de puertos en cada switch a través de la consola de Mininet:» (p. 107; la figura se introduce con dos puntos)
  - «Los resultados se reflejan en las Figuras 8.7 y 8.8» (p. 130; sin punto final).
  - Otras fórmulas: «El esquema de esta aproximación es el que puede verse en la Figura 2.2», «En la Figura 3.2 vemos el porcentaje…», «Echando un vistazo a la figura podemos apreciar que…».
- **Tipos:** (a) diagramas de arquitectura/bloques tomados de artículos y documentación (cap. 2, 5 y 6: unas 20); (b) diagramas propios con draw.io: topología (1.1, 7.1), Gantt (3.1), diagramas de flujo de las aplicaciones (7.8, 7.9, 7.10, 7.11), reparto de roles en la señalización (7.7); (c) gráficos de tarta (3.2, 3.3); (d) capturas de pantalla de terminal, Mininet, GNS3, consola de las aplicaciones Java y gráficas de E/S de Wireshark (6.1, 6.3–6.5, 7.2–7.5, 8.1–8.13). No hay fotografías. Tres figuras ocupan página entera (3.1 Gantt, p. 50; 5.4, p. 70; 7.10, p. 120).
- **Errores detectados:** referencias rotas «la Figura 32» (p. 71) y «la Figura 44» (p. 126) —números de una numeración anterior—; «Figura 8.5» y «Figura 8.6» con el mismo pie («Eventos recibidos en el instalador») cuando la 8.6 muestra el UE; el texto dice «como vemos en la Figura 8.3» (p. 128) donde corresponde la 8.6; «Figura 6.11 y 6.12» citadas (p. 97) para las arquitecturas AD-SAL/MD-SAL que son 6.12 y 6.13. Los resultados del capítulo 8 se presentan solo como capturas (sin tablas ni gráficas propias).

## F. Tablas

- **Número:** 10 («Cuadro» 3.1–3.4, 5.1–5.3, 6.1–6.2, 7.1). Capítulos 1, 2, 4, 8 y 9 sin tablas.
- **Pie:** debajo de la tabla (p. 51: cuerpo de la tabla y a continuación «Cuadro 3.1: Tiempo empleado en la realización del proyecto.»; igual en p. 54 y p. 108).
- **Formato literal:** «Cuadro 3.1: Tiempo empleado en la realización del proyecto.» La etiqueta es «Cuadro» (por defecto de babel) aunque el texto siempre dice «tabla». Punto final presente en 3.1–3.4 y 5.1, ausente en 5.2, 5.3, 6.1, 6.2 y 7.1.
- **Cómo se referencian (5 menciones numéricas, en minúscula salvo una):**
  - «Una división del trabajo, en función del tiempo empleado en cada parte del mismo, sería la que puede verse en las tablas 3.1 y 3.2.» (p. 49)
  - «Existen otras pequeñas diferencias entre MD-SAL y AD-SAL, aparte de las ya mencionadas, y que recogemos en la Tabla 6.2 a modo de resumen.» (p. 99)
  - También: «podemos resumir el total de gastos humanos en la tabla 3.3» (p. 54, sin punto). Las tablas 5.1, 5.2, 5.3 y 7.1 no se citan por número: se introducen con dos puntos («…suelen tener la siguiente estructura:», «Las tablas siguientes muestran, por switch, los flujos que se deben instalar…:»).
- **Contenido:** horas por tarea (alumno y tutor), costes en euros (mano de obra, hardware), estructuras de una entrada OpenFlow (tablas de una sola fila con nombres de campos), orden de cabeceras, comandos de Mininet (tres columnas: Funcionalidad / Comandos / Funciones específicas, con texto largo), comparación MD-SAL frente a AD-SAL (dos columnas de prosa, ocupa una página), flujos por switch (match / prioridad / acción). Las tablas de prosa larga (6.1, 6.2) se leen mal; las numéricas (3.x) son sencillas de dos columnas.
- **Error aritmético:** Cuadro 3.1 suma «Total 430» horas, pero 50+70+40+100+40+100+20 = 420; el coste del Cuadro 3.3 (11 900 €) sí cuadra con 420 h × 25 € + 28 h × 50 €.

## G. Ecuaciones

- No hay ninguna ecuación, ni numerada ni en línea. No hay símbolos matemáticos. La única notación cuantitativa son cifras con unidad pegada o separada de forma irregular: «1.2Gbps», «100km/h», «50Mbps», «300Mbps», «2,8 GHz», «entre los 80KBytes y los 500KBytes», «102,43 segundos», «322.92», «847.92», «el 48 %» (espacio fino antes del % propio de babel-spanish). Separador decimal mezclado (coma y punto). Valores hexadecimales en el cuerpo: «dl type=0x0806».
- Por tanto «no determinable desde el texto» cómo introduciría el tutor una ecuación; esta memoria es puramente cualitativa.

## H. Código y comandos

- **Listados de código:** sí, 9 en total, 8 en el capítulo 7 y 1 en el Anexo A. Presentación: bloque monoespaciado (fuente CMTT10) con **números de línea** a la izquierda, sin marco visible, sin pie ni numeración (no existe «Listado X.Y» ni «Código X.Y») y sin índice de listados. **Inferencia:** paquete `listings` (el espaciado letra a letra en la extracción «S t r i n g» es su artefacto típico). Se introducen con una frase que termina en dos puntos:
  - «Estas funciones, que son bastante sencillas y comunes para todas las aplicaciones, tienen la siguiente forma:» (p. 114) → tres funciones Java (6, 5 y 18 líneas).
  - «Estos flujos se pueden instalar con los siguientes comandos:» (p. 118) → 6 líneas `ovs-ofctl`.
  - «Basta con ejecutar el comando:» (p. 122) → 2 líneas (`cd …`, `sudo ./bin/karaf`).
  - «cada interfaz tiene asociado un script bash y un fichero de configuración como los siguientes:» (p. 122–123) → script de 7 líneas y fichero `hostapd` de 6 líneas, seguidos de un párrafo que explica línea a línea qué hace el script.
  - Dos scripts bash del UE (9 y 39 líneas, p. 123–124).
  - Anexo A: script Python de la topología (82 líneas, p. 141–143), precedido de cinco párrafos de explicación.
- Longitud típica: 5–20 líneas en el cuerpo; el listado largo (39 líneas) y el script completo (82) se colocan al final del capítulo y en anexo respectivamente. Comentarios del Java en inglés («// Function that converts Byte codified information to String :»), comentarios de bash en castellano («#Script para configurar la interfaz wifi»), mensajes de consola en castellano («CONTROLLER:: Ejecutando comandos...»).
- **Comandos y nombres en línea:** entre comillas tipográficas, sin monoespaciado perceptible: «ejecutar el comando “net”», «la función auxiliar “executeCommand()”», «el comando “sudo apt-get install yum”», «“sudo rpm -Uvh opendaylight-release-0.1.0-2.fc19.noarch.rpm”», «bajo el directorio “/opendaylight”», «un RPC de tipo “AddFlow”», «“fail secure mode” ó “fail standalone mode”». Nombres de fichero en listas descriptivas (run.sh, run.bat, version.properties, configuration, lib, plugins) con el término resaltado (**inferencia**: negrita por la fuente CMBX10 presente). Nombres de clases/mensajes sin marcar: «mainClass de JAVA», «Handover Request», «Flow Programmer Service», «OFPP IN PORT». Las opciones de Mininet van como en el manual: «-custom ((topologia.py))».
- **Nombres de tecnología:** «JAVA» en mayúsculas en gran parte del texto (también «Java»), «OpenDayLight» (grafía propia del autor; la oficial es OpenDaylight), «karaf/Karaf», «mininet/Mininet»: sin criterio fijo.

## I. Citas y bibliografía

- **Estilo en el texto:** numérico entre corchetes «[4]», ordenado por aparición. Se usa tanto como apoyo («…utilizar Software Defined Network (SDN) [1] para…») como sustantivo («en [7] se analiza…», «puede consultarse de forma íntegra en [6]», «de acuerdo lo recogido en [2]», «si el lector así lo desea» tras remitir a [4]). No hay citas de autor-año ni superíndices. Una URL se pone directamente en el texto (p. 39: «https://github.com/intrig-unicamp/mininet-wifi»; p. 60: «http://sdnhub.org/») en vez de referenciarla.
- **Orden de la bibliografía:** por orden de aparición (las 21 primeras siguen exactamente el orden de cita: cap. 1 → [1]–[5], cap. 2 → [6]–[7], cap. 5 → [8]–[9], cap. 6 → [10]–[21]). Las entradas [22]–[27] no se citan en ningún punto del cuerpo (restos de una sección eliminada sobre historia de la telefonía móvil, coherente con acrónimos sin usar como GSM, TDMA, D-AMPS, PHS, WWWW).
- **Número total:** 27 referencias; 21 citadas. Reparto: 8 artículos/congresos (IEEE, ACM), 1 tesis de máster, 1 informe técnico, 1 artículo de revista divulgativa, 1 documento universitario, 15 páginas web/documentación (56 %). Dos referencias son del propio grupo del tutor: [2] Cattoni, Mogensen, …, Ameigeiras, Ramos-Munoz (CloudNet 2014) y [4] Ameigeiras, Ramos-Munoz, Schumacher, Prados-Garzon, Navarro-Ortiz, Lopez-Soler (IEEE Network 2015), que es la base del protocolo implementado.
- **Dónde se concentran las citas (52 citas en el cuerpo):** cap. 6 (19), cap. 2 (17), cap. 1 (6), cap. 5 (5), cap. 7 (3), cap. 4 (2); capítulos 3, 8 y 9 sin ninguna cita.
- **Formato literal de tres entradas (estilo IEEEtran):**
  - Artículo: «[4] P. Ameigeiras, J. J. Ramos-munoz, L. Schumacher, J. Prados-Garzon, J. Navarro-Ortiz, and J. M. Lopez-soler, “Link-level access cloud architecture design based on sdn for 5g networks,” IEEE Network, vol. 29, no. 2, pp. 24–31, March 2015.»
  - Congreso: «[6] R. R. Fontes, S. Afzal, S. H. B. Brito, M. A. S. Santos, and C. E. Rothenberg, “Mininet-wifi: Emulating software-defined wireless networks,” in Network and Service Management (CNSM), 2015 11th International Conference on, Nov 2015, pp. 384–389.»
  - Web con fecha de acceso: «[10] “Mininet walkthrough,” accedido 23-05-2017. [Online]. Available: URL{http://mininet.org/walkthrough}»
  - Tesis/informe: «[3] J. Vehanen, “Handover between lte and 3g radio access technologies: Test measurement challenges and field environment test planning,” G2 Pro gradu, diplomityö, 2011. [Online]. Available: http://urn.fi/URN:NBN:fi:aalto-201207022686»
- **Defectos de la bibliografía:** mezcla de idiomas en una misma entrada («accedido …» + «[Online]. Available:»); «URL{…}» sin resolver en todas las webs; títulos en minúscula por BibTeX («sdn», «5g», «lte», «Gns3»); entradas web sin autor ni organización («“Netvirt project,”» repetida en [12], [20] y [27] con títulos genéricos que no describen el contenido); [9] sin nombre de revista («vol. 17, pp. 1–1, 01 2015»); [19] duplicada de [18]; URLs partidas con espacios.

## J. Registro y redacción

- **Persona y voz:** primera persona del plural dominante, muy marcada: «vamos a» (35), «hemos» (34), «podemos» (36), «nuestro/nuestra» (97), «nosotros» (6), «analizaremos» (7), «veremos» (6). Se combina con impersonal con «se» («se pretende emular», «se utilizarán puntos de acceso», «se puede consultar»). Primera persona del singular solo en dos puntos: cap. 4 («la propia experiencia de los profesores del departamento, en este caso D. Jorge Navarro Ortiz, o la mía propia») y 9.3 («En mi caso personal…», «Recordaré este proyecto…»). Segunda persona genérica en las conclusiones («siempre que necesitas realizar algún cambio…», «no es hasta llegado el momento de la implementación cuando de verdad eres consciente»). Apelación explícita al lector: «aportar al lector», «dotar al lector», «si el lector así lo desea», «para facilitar al lector el seguimiento», «sirviendo así de guía para el lector».
- **Tiempos verbales por capítulo:** caps. 1–4 en **futuro** de planificación («será necesario crear», «se simulará», «analizaremos», «esta estimación puede variar»): la memoria conserva la voz de un plan previo y no la actualiza. Caps. 5–6 presente descriptivo (texto de manual). Cap. 7 mezcla futuro de intención («vamos utilizar JAVA», «crearemos una aplicación servidora») con presente. Cap. 8 presente + pretérito perfecto («se ha usado», «hemos podido comprobar») y aún algún futuro («Realizaremos una serie de tres simulaciones»). Cap. 9 pretérito perfecto y pasado («ha resultado muy costosa», «se ha planteado»). Lección: la incoherencia temporal es el defecto de redacción más visible de la memoria.
- **Párrafos y frases (cuerpo, 372 párrafos de más de 25 palabras):** media de 1,7 frases por párrafo (mediana 2), 55 palabras por párrafo; frases largas: media 33 palabras (mediana 30), 92 de 623 frases superan las 50 palabras y 184 las 40. Abundan los párrafos de una sola frase larga con subordinadas encadenadas y gerundios («…pudiendo configurarlos y gestionarlos…», «…permitiéndonos además elegir…»). Casi nunca hay párrafos de 4 o más frases.
- **Listas:** viñetas «•» en 107 líneas, concentradas en cap. 5 (54), cap. 6 (26), cap. 3 (20), cap. 4 (5), cap. 7 (2); ninguna en caps. 1, 2, 8 y 9. Subviñetas «·» (acciones y mensajes OpenFlow, cap. 5) y «◦» (variantes de instalación, cap. 6). Patrón constante: **término resaltado + dos puntos + explicación de 2–5 líneas** («• Framework para el Controlador : …», «• Paso 1 : …», «• Requisitos de funcionalidad : …»). Se usan para: tareas del plan, recursos hardware/software, elementos y beneficios de SDN, tipos de grupo, instrucciones y acciones OpenFlow, mensajes del protocolo, ficheros de la distribución, pasos de un proceso (10 «Paso n»), decisiones de diseño, elementos físicos de la red. No hay listas numeradas (los pasos son viñetas con «Paso n»). El espacio antes de los dos puntos («USB :», «Controlador :») delata un `\textbf{…} :` descuidado.
- **Negrita/cursiva (inferencias):** cursiva (CMTI10) para anglicismos destacados —la secuencia «(handover )» con espacio antes del paréntesis es la corrección de cursiva de LaTeX—; negrita (CMBX10/CMBX9) en los términos de las listas descriptivas, en los datos de las autorizaciones y en los títulos. En el cuerpo corrido no se aprecian negritas de énfasis. No determinable con total certeza desde el texto.
- **Anglicismos y siglas:** anglicismos masivos sin traducir ni marcar de forma consistente: «switch» (165 apariciones), «handover» (49), «plugin» (36), «host» (27), «framework» (25), «pipeline» (13), «script», «sniffer», «matching», «datastore», «learning-switch», «open source», «data centers», «parsea», «customizada», «testeo». Siglas: se definen al primer uso con la expansión inglesa seguida de la sigla entre paréntesis: «Software Defined Network (SDN)», «User Equipment (UE)», «File Transfer Protocol (FTP)», «Network Adress Translation (NAT)». **Inferencia:** paquete de acrónimos automático, porque la expansión se repite en capítulos posteriores («Media Access Control (MAC)» de nuevo en p. 121; «Internet Protocol (IP)» dos veces en la misma frase, p. 115) y se cuela en un título («8.3. Ping entre User Equipment (UE) y hosts») y en el índice de figuras («2.2. Aproximacion Centralized Software Defined Network (SDN)»). Hay un «Índice de Acrónimos» de 58 entradas al principio, con 8 acrónimos no usados en el texto (CDMA, D-AMPS, DAWN, GSM, OWA, PHS, TDMA, WWWW).
- **Nivel de detalle técnico:** alto y enciclopédico en caps. 5–6 (reproduce la especificación OpenFlow: tipos de mensajes, acciones, instrucciones; distribuciones de OpenDaylight), medio en cap. 7 (explica la lógica de cada aplicación y muestra código auxiliar, pero no el código del controlador), bajo en rigor cuantitativo en cap. 8 (los resultados son capturas de Wireshark y de consola; las cifras se dan en prosa aproximada: «del orden de 3 veces superior», «en torno a 15 segundos», «102,43 segundos»; media de 3 repeticiones; sin tabla de resultados ni medidas de dispersión).
- **Formulación de los objetivos:** un párrafo, no una lista: «El objetivo final de este proyecto es emular de la forma más exacta y efectiva posible un escenario de movilidad en una red móvil 5G. Para ello será necesario crear el escenario apropiado en un emulador de redes, configurar un controlador que gestione el envío de paquetes y la instalación de flujos de datos, y simular el comportamiento de una estación móvil…» (p. 30). El segundo párrafo concreta medios: «se utilizarán puntos de acceso o Access Point (AP) Wi-Fi para emular dicho traspaso. Así, se simulará la señalización que aparece en [4] para forzar que un PC cambie su conexión de un AP a otro.»
- **Formulación de los requisitos (cap. 4):** primero se define la diferencia entre «requisito de funcionalidad» y «decisión de diseño» en dos viñetas; luego prosa argumentativa (coste, hardware disponible, Linux, Java) y tres viñetas de decisiones (framework del controlador, herramienta de simulación, configuración de puntos de acceso), cada una con justificación de 5–8 líneas. No hay tabla ni codificación de requisitos (RF-01…).
- **Formulación de los resultados:** captura + párrafo interpretativo con cifra aproximada y comparación con el «caso ideal» (instalador manual de flujos): «Como vemos, en el caso de la solución basada en el controlador integrado con OpenDayLight, se añade un retardo del orden de 3 veces superior al caso ideal, representado por los resultados obtenidos para el caso de instalador de flujos. Si bien la pérdida de paquetes es bastante similar, aumentando en uno sólamente.» (p. 130). Cierre del capítulo con «Evaluación de resultados» en tres ejes: eficiencia, transparencia para el usuario, escalabilidad.
- **Formulación de las limitaciones:** nunca en un apartado propio; aparecen como atenuaciones dentro del texto: «Es dificil determinar cuánta incidencia tiene en ello el proceso de señalización y cuánta es debida a las limitaciones hardware de nuestro escenario.» (p. 130); «plantear una implementación real de este escenario queda fuera del objetivo de este proyecto, puesto que no contamos con todo el hardware necesario» (p. 58); «con los recursos limitados de los que disponemos» (p. 138).
- **Frases típicas de apertura y cierre (literales):**
  1. «En este apartado vamos a tratar de aportar al lector un marco de referencia contextualizado sobre la situación actual de las redes de comunicaciones móviles.» (p. 29)
  2. «En este apartado vamos a realizar una planificación temporal y económica del proyecto.» (p. 47)
  3. «Una vez analizados los requisitos de nuestro proyecto, dedicaremos los capítulos quinto y sexto al análisis y comprensión de las principales tecnologías y herramientas implicadas en el desarrollo del mismo.» (p. 61)
  4. «Vamos a empezar haciendo un pequeño análisis de cuáles son los fundamentos de las redes definidas por software.» (p. 61)
  5. «Una vez introducida la herramienta que se usará para la simulación de topologías de nuestro proyecto, estamos listos para hablar del controlador…» (p. 86)
  6. «Una vez implementado el escenario, es la hora de comprobar su funcionalidad y eficiencia.» (p. 125)
  7. «Tras la realización de las pruebas mostradas en el apartado anterior, se pueden obtener varias conclusiones interesantes, que vamos a recoger en este apartado.» (p. 134)
  8. «Realizado el trabajo, tras mucho estudio, muchas pruebas, muchos fallos, y muchos quebraderos de cabeza, este apartado está destinado a analizar el desarrollo del proyecto…» (p. 137)
  9. «En el siguiente apartado veremos cómo se ha diseñado e implementado cada uno de los componentes necesarios para emular un escenario de movilidad.» (p. 104)
- **Conectores frecuentes (recuento en el cuerpo):** «Por tanto» (19), «Finalmente» (11), «Sin embargo» (10), «Como vemos» (9), «Como ya hemos comentado» (9), «De igual forma» (9), «De igual manera» (8), «A continuación» (6), «No obstante» (4), «Por otro lado» (3), «Por otra parte» (2). Muletillas propias: «a saber:», «Es por ello que», «Es por este motivo por el cuál», «Con todo ello», «Una vez + participio», «Por su parte», «En primer lugar / En segundo lugar», «a grandes rasgos», «en pro de», «al hilo de», «en este sentido», «de cara a». Latinismos «e.g.» y «i.e.» una vez cada uno.
- **Tres párrafos representativos completos:**
  - Diseño/arquitectura (p. 119): «Esta solución, unida a una pequeña modificación en la aplicación que gestiona el target AP, permitirá realizar un cambio de celda de forma transparente. La clave en este caso reside en, conocida la MAC origen del UE que va a realizar el cambio de celda, realizar un borrado de los flujos relativos a ese equipo en todos los switches, de forma que cuando se quiera conectar de nuevo con el UE en su nueva celda, el target AP no tendrá flujo definido para la MAC asociada al UE y tendrá que intercambiar mensajes con el controlador, que detectará diferencias entre los flujos almacenados para dicha MAC con respecto a los recibidos ahora, de forma que modificará los flujos y los volverá a instalar creando la nueva ruta hacia el UE.»
  - Resultados/evaluación (p. 134): «En primer lugar, en términos de eficiencia, los resultados obtenidos para las diferentes pruebas realizadas indican que el rendimiento obtenido cuando se utiliza un controlador con una solución basada en OpenDayLight son muy similares a los obtenidos para el caso ideal. En un principio podría pensarse que el procesamiento de paquetes realizador por el controlador podría percibirse de forma negativa en el rendimiento del escenario, pero los resultados demuestran que su utilización es prácticamente imperceptible y se ve enmascarada por el resto de elementos hardware y de red que afectan al rendimiento del sistema.»
  - Conclusiones (p. 138): «Podemos concluir con que este proyecto es una primera aproximación a un escenario de simulación real, con los recursos limitados de los que disponemos, y teniendo en cuenta que son nuestros primeros pasos con una tecnología que tiene una complejidad notable y un potencial mucho mayor. Encontramos a lo largo de la memoria un equilibrio entre carga práctica y teórica, pues son muchos los detalles de implementación que se debían explicar, de igual forma que muchos los conceptos que se consideran necesarios para facilitar al lector el acercamiento a los conceptos sobre los que se levanta este proyecto.»

## K. Capítulo a capítulo

**Capítulo 1. Introducción** (PDF 29–35, impresas 1–7; ~2 000 palabras; 1 figura, 0 tablas; 6 citas).
Apartados: Motivación, Objetivos, Contexto (1.3.1 Introducción a la movilidad en redes 5G), Importancia del modelo SDN, Estructura de la memoria (un subapartado numerado por capítulo, 1.5.1–1.5.10). Propósito: situar al lector y justificar SDN. Bien: objetivos concretos con topología (Figura 1.1) y método de medida («un sniffer (wireshark en nuestro caso) medirá la pérdida de paquetes»); cada capítulo descrito en 3–4 líneas. Mal: todo en futuro; sin párrafo introductorio de capítulo; «Capítulo 10: Bibliografía» no existe como capítulo; cifras de contexto con una sola cita.

**Capítulo 2. Estado del arte** (PDF 37–45, impresas 9–17; ~2 360 palabras; 6 figuras; 17 citas).
Un solo apartado numerado (2.1 Comparación con otros modelos) con tres trabajos analizados como subapartados titulados con el título original en inglés del artículo: Mininet-WiFi [6], Handover Management in SDN-based Mobile Networks [7] (con tres variantes en nivel 4: centralizado, semi-centralizado, jerárquico) y el artículo del grupo [4], del que se toma el protocolo de handover a implementar. Cierra con tres párrafos de conclusión que posicionan la aportación propia («una alternativa aún no contemplada, la interacción del entorno simulado con elementos reales»). Bien: cada trabajo se compara explícitamente con el propio (puntos fuertes/débiles) y el capítulo cierra con la contribución. Mal: solo tres referencias; figuras copiadas de los artículos; URL directa en el texto.

**Capítulo 3. Planificación temporal y presupuesto** (PDF 47–56, impresas 19–28; ~2 400 palabras; 3 figuras; 4 tablas; 0 citas).
Contiene: diagrama de Gantt (Figura 3.1, página entera, hecho con draw.io, tareas solapadas a lo largo de «un curso universitario»); división del trabajo en 7 tareas descritas en viñetas (Búsqueda de información y documentación; Familiarización con el entorno; Fase de diseño físico y lógico; Implementación del escenario; Fase de pruebas; Redacción del proyecto; Preparación de defensa y exposición); Cuadro 3.1 horas del alumno por tarea (50, 70, 40, 100, 40, 100, 20; total impreso 430, suma real 420); Cuadro 3.2 horas del tutor por tarea (2, 4, 4, 6, 4, 6, 2; total 28); Planificación económica con recursos humanos (tutor «Profesor Contratado Doctor», 50 €/h; alumno 25 €/h), hardware (MacBook Pro 2010, Toshiba Satellite A660, conexión de 50 Mbps, 3 adaptadores Wi-Fi USB Tenda N, hub USB) y software (Ubuntu 14.04, Eclipse Neon, Java, Python, OpenDayLight, Mininet, Maven, Wireshark; todo libre, coste 0); Estimación de costes: Cuadro 3.3 mano de obra por tarea (1350, 1950, 1200, 2800, 1200, 2800, 600; total 11 900 €), Cuadro 3.4 hardware (322.92 prorrateado, 200, 300, 30, 5; total 847.92 €); software 0 €; Análisis final con dos gráficos de tarta (tiempo: «el 48 % del tiempo total … se destina a … la implementación del proyecto y su redacción»; coste: «la práctica totalidad de los costes son debidos a la mano de obra»). Bien: cubre horas, tarifas, hardware prorrateado por vida útil, software, tutor incluido como coste. Mal: no se da el coste total del proyecto en una cifra (sería 12 747,92 €); error de suma; referencia cruzada errónea («paquetes de trabajo definidos en el apartado 4.1.1» cuando es 3.1.1); «Elemeto», «temporazalización», «Gant»; sin citas; redactado en futuro como plan a priori.

**Capítulo 4. Requisitos de funcionalidad y decisiones de diseño** (PDF 57–60, impresas 29–32; ~1 500 palabras; 0 figuras; 0 tablas; 2 citas).
Distingue requisito (impuesto por la naturaleza del proyecto: implementar la señalización de [4]) de decisión (elegida por el autor: herramientas, lenguajes, topología). Requisitos: software libre, hardware disponible, Linux, Java/UDP. Decisiones: OpenDayLight (frente a POX), Mininet (frente a Packet Tracer y GNS3), puntos de acceso tradicionales con hostapd (frente a ad hoc). Bien: cada elección justificada con alternativa descartada. Mal: el único subapartado (4.1.1) depende de 4.1 de forma ilógica (debería ser 4.2); termina sin cierre; frases muy largas; mezcla de motivos técnicos y personales («ya ha sido utilizado por profesores del departamento»).

**Capítulo 5. Tecnologias aplicadas** (PDF 61–79, impresas 33–51; ~5 740 palabras; 5 figuras; 3 tablas; 5 citas).
Fundamento teórico: SDN (arquitectura ONF, beneficios) y OpenFlow (tablas de flujo, pipeline, group tables, matching, instrucciones y acciones, canal, tipos de mensajes, establecimiento/interrupción de conexión, cifrado, gestión de mensajes). Bien: párrafo de apertura que enlaza con el capítulo 6; cierre con transición; tablas simples para estructuras. Mal: es un resumen de la especificación OpenFlow con 5 niveles de epígrafe, 54 líneas de viñetas y casi sin relación con el proyecto; título sin tilde («Tecnologias»); referencia rota «Figura 32».

**Capítulo 6. Herramientas utilizadas** (PDF 81–104, impresas 53–76; ~5 690 palabras; 15 figuras; 2 tablas; 19 citas).
Mininet (por qué, uso con tabla de comandos y capturas, comparación con GNS3) y OpenDayLight (qué es, formas de instalación, distribuciones Hydrogen/Hellium/Lithium/Beryllium con sus diagramas, arquitectura SAL, MD-SAL frente a AD-SAL con tabla comparativa, RESTCONF, procesos de adición y borrado de flujos en 10 y 6 pasos). Bien: justifica la elección de cada herramienta frente a alternativas; capturas propias de uso. Mal: capítulo de manual (historial de distribuciones irrelevante para el proyecto); 15 figuras, casi todas copiadas de documentación web; «Hellium», «distrución»; Figura 6.8 con el título del subapartado pegado en la misma línea.

**Capítulo 7. Diseño e implementación de un escenario de movilidad** (PDF 105–124, impresas 77–96; ~6 090 palabras incluido código; 11 figuras; 1 tabla; 3 citas).
Topología (elementos físicos: UE portátil y dos tarjetas Wi-Fi; resto en Mininet; tabla de flujos por switch; pruebas de conectividad con capturas); proceso de señalización (figura del protocolo de [4] y su mapeo a la topología; cliente UE, servidores source/target AP, mensajes Handover Request/Acknowledge/Confirmation/Context Information descritos en lista; funciones auxiliares Java listadas); controlador en OpenDayLight (learning-switch con mapa switch→MAC→puerto; borrado de flujos del UE al recibir la confirmación); instalador de flujos manual como «caso ideal» de referencia; funciones auxiliares (arranque de Karaf, scripts hostapd y scripts del UE). Bien: es el capítulo propio más extenso; explica cada pieza con diagrama de flujo propio; justifica la doble implementación para aislar el retardo del hardware. Mal: no muestra el código del controlador ni de las aplicaciones principales (solo utilidades); listados sin numerar ni referenciar; algunas figuras de capturas sin explicación de ejes; sigue usando futuro.

**Capítulo 8. Fase de pruebas y evaluación** (PDF 125–135, impresas 97–107; ~2 340 palabras; 13 figuras; 0 tablas; 0 citas).
Prueba funcional de señalización (traza Wireshark y consolas de cada aplicación), pruebas de rendimiento: ping UE↔hosts con y sin handover para las dos soluciones (3 repeticiones, RTT medio, paquetes perdidos) y FTP con y sin handover (interrupciones de ~6 s frente a ~15 s; transferencia de 102,43 s). Evaluación de resultados en prosa (eficiencia, transparencia, escalabilidad). Bien: diseño experimental con línea base explícita y dos tipos de tráfico; cierre interpretativo. Mal: resultados solo en capturas, sin tabla numérica ni gráfica propia ni dispersión; n = 3; cifras aproximadas en prosa; pie duplicado 8.5/8.6; referencias rotas («Figura 44», «Figura 8.3»); frase inacabada «Si bien la pérdida de paquetes es bastante similar, aumentando en uno sólamente.».

**Capítulo 9. Conclusiones y vías futuras** (PDF 137–139, impresas 109–111; ~980 palabras; 0 figuras; 0 tablas; 0 citas).
Conclusiones (recapitulación del objetivo, dificultad de las herramientas, satisfacción por cumplir el objetivo, aportación: definir el contenido de los mensajes del protocolo de [4]), Vías futuras (implementación real multi-alumno; integración con el TFG de Bárbara Valera sobre filtrado de inundaciones en OpenDaylight), Valoración personal (reflexión sobre el ingeniero, frustración y aprendizaje, solapamiento con el trabajo). Bien: tres apartados claros; vías futuras concretas y ligadas al departamento. Mal: muy corto (3 páginas); sin cifras de resultados; tono coloquial («quebraderos de cabeza», «esta aventura»); no repasa los objetivos uno a uno.

**Anexo A. Topología en Mininet** (PDF 141–143, impresas 113–115; ~1 240 palabras, casi todo código). Cinco párrafos explicativos y el script Python de 82 líneas con números de línea. Único anexo; no hay anexos de manual de usuario, instalación ni código del controlador.

**Bibliografía** (PDF 145–147, impresas 117–119): 27 entradas, IEEEtran, defectos ya descritos.

## L. Particularidades UGR/ETSIIT y del tutor

- **Fórmulas oficiales (literales en B):** la autorización del alumno es la fórmula ETSIIT de depósito en biblioteca («autorizo la ubicación de la siguiente copia de mi Trabajo Fin de Grado en la biblioteca del centro para que pueda ser consultada por las personas que lo deseen»), con «Fdo:» y lugar/fecha «Granada a 12 de Septiembre de 2017.». La de los directores es la fórmula de informe («Informan: Que el presente trabajo, titulado …, ha sido realizado bajo su supervisión por …, y autorizamos la defensa de dicho trabajo ante el tribunal que corresponda. Y para que conste, expiden y firman el presente informe en Granada a …», firmado «Los directores:»). Incoherencia de persona dentro de la fórmula («Informan … autorizamos»).
- **Orden de las páginas iniciales:** portada → (blanco) → segunda portada → resumen/palabras clave → abstract/keywords → autorización alumno → informe directores → agradecimientos → acrónimos → índice general → índice de figuras → índice de cuadros. Resumen y abstract van ANTES de las autorizaciones (orden poco habitual; en memorias UGR más recientes las autorizaciones suelen ir antes del resumen). Cada bloque empieza en página impar con verso en blanco.
- **Mención al tribunal:** solo en el informe de los directores («ante el tribunal que corresponda») y en el plan de trabajo («preparar tanto la exposición para la defensa ante el tribunal»).
- **«Granada, mes de año»:** portada «Granada, Septiembre de 2017» (mes con mayúscula, uso antiguo); autorizaciones con día completo.
- **Firma:** espacio para firma implícito tras «Fdo:» y bajo «Los directores:» con los dos nombres en la misma línea. **DNI** presente como campo pero sin rellenar («XXX») en la copia depositada.
- **Nombre del tutor:** en portada «Directores / Jorge Navarro Ortiz / Juan José Ramos Muñoz»; en el informe «D. Juan José Ramos Muñoz, Profesor del Área de Ingeniería Telemática del Departamento Teoría de la señal, Telemática y Comunicaciones de la Universidad de Granada.» (sin categoría docente; el codirector Navarro sí se identifica en cap. 3 como «Profesor Contratado Doctor»). En la bibliografía aparece como coautor «J. J. Ramos-Munoz» ([2], [4]).
- **Rasgos que parecen preferencia del tutor / del grupo (inferencias, un solo TFG no basta para generalizar):**
  1. Capítulo de **planificación y presupuesto** completo (Gantt, horas alumno y tutor, tarifas €/h, hardware prorrateado, software, análisis con gráficos) situado al principio (cap. 3), antes de requisitos y tecnología.
  2. Capítulo propio de **requisitos y decisiones de diseño**, separado de la tecnología.
  3. Separación **Tecnologías aplicadas** (conceptos/protocolos) / **Herramientas utilizadas** (software concreto).
  4. **Estado del arte comparativo** (cada trabajo frente al propio) que termina posicionando la aportación, y que incluye los artículos del grupo (Ameigeiras, Ramos-Muñoz, Navarro-Ortiz) como base del diseño.
  5. **Pruebas con línea base explícita** («caso ideal» frente a solución propuesta) y dos tipos de tráfico; evaluación final en tres ejes.
  6. **Conclusiones + Vías futuras + Valoración personal** como tres apartados del último capítulo; vías futuras que conectan con otros TFG del departamento.
  7. **Anexo con el código** de la topología; bibliografía IEEE numérica por aparición; «Índice de Acrónimos» al principio.
  8. Extensión: ~29 000 palabras de cuerpo, 111 páginas impresas, 54 figuras, 10 tablas.

## M. Cifras globales

- Páginas PDF: 150. Preliminares: 28 (PDF 1–28, de las cuales 11 en blanco). Cuerpo: 111 páginas impresas (PDF 29–139), con 4 versos en blanco (36, 46, 80, 136). Anexo: 3 (+1 blanco). Bibliografía: 3. Blancos finales: 3.
- Figuras: 54. Tablas: 10. Ecuaciones: 0. Listados de código: 9 (sin numerar). Referencias: 27 (21 citadas; 52 citas en el cuerpo).
- Palabras (wc sobre el texto extraído): total 35 235. Preliminares 4 437 (resumen ~520, abstract ~400, resto índices y acrónimos). Cap. 1: 2 010. Cap. 2: 2 358. Cap. 3: 2 396. Cap. 4: 1 494. Cap. 5: 5 743. Cap. 6: 5 690. Cap. 7: 6 086 (incluye ~400 de código). Cap. 8: 2 339. Cap. 9: 983. Cuerpo (caps. 1–9): ≈ 29 100. Anexo A: 1 239 (casi todo código). Bibliografía: 466.
- Reparto del cuerpo: fundamento/manual (caps. 5–6) 39 %; trabajo propio (caps. 7–8) 29 %; introducción + estado del arte + planificación + requisitos 28 %; conclusiones 3 %.

## N. Lecciones transferibles

### Reglas para que una memoria nueva se parezca a esta (formato, estructura, redacción)

1. **Páginas iniciales en este orden y con estas fórmulas:** portada («TRABAJO FIN DE GRADO», titulación en mayúsculas, título y subtítulo, «Autor», «Directores»/«Tutor», centro, «Granada, mes de año»), segunda portada, resumen con «Palabras clave:» y abstract con «Keywords:», autorización del alumno para la biblioteca (fórmula literal de B, con DNI real), informe del tutor («Informa: Que el presente trabajo, titulado …, ha sido realizado bajo su supervisión por …, y autoriza la defensa de dicho trabajo ante el tribunal que corresponda. Y para que conste, expide y firma el presente informe en Granada a …»), agradecimientos, índice de acrónimos, índice general, índice de figuras, índice de tablas. Cada bloque en página impar.
2. **Esqueleto de capítulos:** 1 Introducción (motivación, objetivos, contexto, estructura de la memoria con un párrafo por capítulo) · 2 Estado del arte comparativo que acabe en la aportación propia · 3 Planificación temporal y presupuesto (Gantt, tareas, horas alumno y tutor, €/h, hardware prorrateado, software, total y gráficos) · 4 Requisitos y decisiones de diseño justificadas frente a alternativas · 5 Fundamentos/tecnologías · 6 Herramientas · 7 Diseño e implementación · 8 Pruebas y evaluación con línea base y apartado final «Evaluación de resultados» · 9 Conclusiones, vías futuras y valoración personal · Anexos con código · Bibliografía numérica.
3. **Numeración LaTeX-book:** «Capítulo N» en una línea y título en la siguiente; epígrafes «N.M.» y «N.M.K.» con punto final en el número; índice hasta nivel 3; nunca bajar de nivel 4 en el texto (esta memoria llega a 5 y se nota).
4. **Cada capítulo abre con 1–3 párrafos que dicen qué se va a tratar y cierra con un párrafo de síntesis + transición** («Con esto concluye el apartado … En el siguiente capítulo analizaremos …»). Aplicarlo también a los capítulos 1, 3 y 4, que aquí no lo hacen.
5. **Figuras:** pie debajo, «Figura N.M: Texto.» con punto final siempre; fuente dentro del pie cuando no es propia («Imagen obtenida de [n]» o «[n]» al final); en el texto siempre «la Figura N.M» con mayúscula y mencionada antes de que aparezca; numeración por capítulo; diagramas propios homogéneos (aquí draw.io).
6. **Tablas:** etiqueta «Tabla N.M:» (configurar babel para no dejar «Cuadro»), pie debajo, referenciadas por número y no con «la tabla siguiente:»; las tablas numéricas, cortas y de pocas columnas; evitar tablas de prosa larga.
7. **Listas descriptivas «término en negrita + dos puntos + explicación»** para tareas, recursos, requisitos, elementos y pasos; viñetas solo en los capítulos de planificación, requisitos, tecnología e implementación; nada de viñetas en introducción, estado del arte, resultados y conclusiones (así lo hace esta memoria).
8. **Siglas:** expansión inglesa + sigla entre paréntesis en el primer uso y después solo la sigla; índice de acrónimos al principio con solo los que se usan; no dejar que la expansión entre en títulos ni en pies.
9. **Código:** bloques monoespaciados con números de línea, introducidos por una frase con dos puntos y seguidos de un párrafo que explica qué hace; solo utilidades cortas (5–20 líneas) en el cuerpo y los scripts completos en anexo; comandos y nombres de función en el texto marcados (aquí entre comillas tipográficas; mejor monoespaciado).
10. **Citas numéricas [n] por orden de aparición, estilo IEEE,** con fecha de acceso en las webs; concentrar las citas en introducción, estado del arte y fundamentos; que todas las entradas de la bibliografía estén citadas y todas las webs lleven autor u organización y título descriptivo.
11. **Registro:** primera persona del plural («vamos a», «hemos», «nuestro») combinada con impersonal; apelación ocasional «al lector»; conectores sobrios («Por tanto», «Sin embargo», «De igual forma», «Finalmente», «Como vemos»); tiempos coherentes: presente para describir, pasado para lo hecho, futuro solo en vías futuras (esta memoria falla en esto).
12. **Resultados = cifra + interpretación + comparación con la referencia;** terminar el capítulo con una evaluación en ejes (eficiencia, transparencia, escalabilidad) y las conclusiones retomando esos ejes. Mejorar respecto al original añadiendo tablas numéricas, repeticiones y dispersión.

### Lo que NO aparece en este TFG (y por tanto no debe aparecer en la nueva memoria)

- Emojis, iconos, colores en el texto, markdown visible, cajas de «nota/aviso».
- Negrita de énfasis en el cuerpo del párrafo (solo en términos de lista y títulos).
- Listas numeradas ni listas anidadas de más de dos niveles; viñetas en introducción, estado del arte, resultados y conclusiones.
- Ecuaciones, símbolos matemáticos, notación estadística.
- Tablas de código, listados numerados tipo «Listado 7.1», índice de listados.
- «Fuente: elaboración propia».
- Códigos de requisito (RF-01), matrices de trazabilidad, casos de uso UML, historias de usuario.
- Apartado de «Limitaciones» separado; apartado de «Metodología» separado; cronograma real frente al planificado.
- Hipervínculos visibles en el cuerpo (salvo dos URL sueltas, que son un descuido).
- Primera persona del singular fuera de la valoración personal.
- Preguntas retóricas en el cuerpo (solo en dos títulos de sección).
- Capítulo de instalación/manual de usuario; anexos de datos crudos.

### Errores detectados que conviene evitar

- Incoherencias de título (4 variantes), titulación (3 grafías) y nombres («Hellium», «OpenDayLight» por OpenDaylight, «JAVA»/«Java», «Gant»).
- Referencias cruzadas rotas o erróneas («Figura 32», «Figura 44», «Figura 8.3» por 8.6, «Figuras 6.11 y 6.12» por 6.12 y 6.13, «apartado 4.1.1» por 3.1.1) y pies duplicados (8.5/8.6): regenerar siempre con `\ref`/`\label` y revisar la última compilación.
- Índice desactualizado (bibliografía en 119 frente a 117 real), «Lista de figuras/tablas» frente a «Índice de figuras/cuadros», «Cuadro» frente a «tabla», DNI «XXX» sin rellenar, página 3 vacía con folio.
- Error aritmético en la tabla de horas (430 frente a 420) y ausencia de la cifra total del presupuesto.
- Bibliografía con «URL{…}» sin resolver, títulos en minúscula por BibTeX («sdn», «5g»), entrada duplicada ([18]/[19]), 6 entradas no citadas, 8 acrónimos no usados: restos de secciones eliminadas.
- Expansión automática de acrónimos repetida (dos veces en una frase) y dentro de títulos/índices.
- Resultados sin tabla numérica, con n = 3 y cifras aproximadas en prosa; frase inacabada en la interpretación del ping.
- Memoria en futuro en los capítulos 1–4 y 7 (voz de plan no actualizada); frases de 50+ palabras con gerundios encadenados; párrafos de una sola frase.
- Abstract en inglés con erratas («consumming», «fith», «interopeable», «mantained», «inteligence»).
- Dos capítulos de fundamento (5 y 6) que suman el 39 % del cuerpo y copian documentación; mejor acortarlos y dedicar ese espacio al trabajo propio.
- Tono coloquial en conclusiones («quebraderos de cabeza», «esta aventura», «Sin más dilaciones»).

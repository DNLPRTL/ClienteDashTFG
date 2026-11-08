# Biblia de formato y estilo de la memoria (TFG ETSIIT-UGR) — v2, 09/11/2026

Guía obligatoria para redactar cualquier apartado de la memoria desde el 5.3.
Sale de siete TFG aprobados en la ETSIIT (tres del tutor Juan José Ramos
Muñoz, 2017, 2024 y 2025, y cuatro recientes de otros tutores), leídos
enteros y medidos. Las fichas completas están en
`docs/memoria/apoyo/tfg_referencia/` (una por TFG, con citas literales y
páginas) y las medidas de maquetación en `maquetacion_medida.md`. Pesa más lo
del tutor, y dentro de lo suyo, lo más reciente (2025 y 2024). Esta biblia fija
el FORMATO y el REGISTRO; el contenido lo fijan el plan maestro
(`00_PLAN_MAESTRO_MEMORIA.md`) y el estándar v2 (memoria
`estandar-redaccion-memoria-v2`). Si hay conflicto de formato, manda esta
biblia; si hay conflicto de contenido, manda el plan.

## 1. El corpus

| TFG | Año | Tutor | Herramienta | Páginas | Cuerpo (palabras) | Fig. / Tab. / Refs. | Peso |
|---|---|---|---|---|---|---|---|
| Cañizares Cancho | 2025 | Ramos Muñoz y Navarro Ortiz | Word, plantilla oficial ETSIIT, Arial 12 | 108 | ~15 000 | 57 / 13 / 34 | máximo |
| Marín Munuera | 2024 | Navarro Ortiz (director) y Ramos Muñoz (codirector) | LaTeX, plantilla ETSIIT, 11 pt | 143 | ~14 900 | 14 / 1 / 38 | alto (firma Navarro: algunos rasgos pueden ser suyos) |
| González Callejas | 2017 | Ramos Muñoz | LaTeX, plantilla ETSIIT | 150 | ~29 000 | 54 / 10 / 27 | medio |
| Sánchez Martínez | 2024 | Molero y Pérez Escribano | LaTeX, plantilla ETSIIT | 150 | ~39 000 | 43 / 2 / 24 | alto |
| Hernández Manrique | 2024 | Peinado y Gómez | LaTeX, plantilla ETSIIT | 110 | ~24 000 | 15+ / 15 / 28 | alto |
| Sánchez Martínez (FS) | 2025 | Valderrama | LaTeX, plantilla ETSIIT | 155 | ~30 000 | 79 / 9 / 39 | alto |
| Romero Espigares | 2025 | Roldán Aranda (GranaSAT) | LaTeX, plantilla propia del grupo | 187 | ~28 000 | 75 / 5 / 69 | alto (estructura), bajo (formato) |

Seis de siete usan la plantilla LaTeX de la escuela (clase libro a dos caras,
A4, 11 pt, Computer Modern o Latin Modern). El del tutor de 2025 usa la
plantilla oficial de Word de la escuela (Arial 12). Las dos rutas son
válidas: la estructura y los textos oficiales son idénticos.

## 2. Ruta elegida y maquetación

Ruta de trabajo: **Word con la plantilla oficial de la ETSIIT** (la del
tutor 2025), porque el capítulo 4 y el 5.1–5.2 ya están en Word con figuras
en JPG. La ruta LaTeX (Prism, `unsrt`) queda como alternativa para el PDF
final; cambiar de una a otra solo cambia la tipografía, no el texto.

Parámetros medidos en el TFG del tutor de 2025 (Word), que son los de la
plantilla `.docx` de Claude (`docs/memoria/plantilla/plantilla_memoria_ugr.docx`,
se crea en el primer turno del 5.3):

| Elemento | Valor |
|---|---|
| Papel y márgenes | A4; márgenes de 2,5 cm (los 3 cm laterales del Word actual de Daniel también valen; uniformes en todo el documento) |
| Cuerpo | Arial 12 pt, justificado, sangría de primera línea, interlineado 1,15–1,5 (el actual de Daniel, 1,16, vale) |
| Capítulo | dos líneas: «Capítulo N» en Arial regular 24 pt y el título en Arial negrita 26 pt; cada capítulo empieza en página nueva |
| Nivel 2 | «N.M. Título» en Arial negrita 18 pt, número con punto final |
| Nivel 3 | «N.M.K. Título» en Arial negrita 12 pt, en línea propia |
| Nivel 4 | sin numerar, rótulo en negrita; evitarlo |
| Pies de figura y tabla | debajo, centrados, Arial 9 pt: «Figura 4.3: Texto.» / «Tabla 4.1: Texto.» (dos puntos tras el número, mayúscula inicial, punto final) |
| Tablas | tablas nativas de Word, cabecera en negrita, unidades entre paréntesis en la cabecera, fila «Total» cuando toca, 10–12 pt, no más de 6 columnas |
| Ecuaciones | editor de ecuaciones de Word, centradas, número «(N.M)» a la derecha (la plantilla LaTeX lo hace sola) |
| Código | fragmentos de 10 líneas como mucho, en Consolas 10 pt con pie «Listado N.M: Texto.» debajo; nunca capturas de pantalla de código |
| Páginas | número centrado al pie; sin cabeceras en Word (en LaTeX las pone la plantilla) |
| Listas | viñetas con entradilla en negrita y dos puntos: «**Duty cycle:** explicación»; numeradas solo para pasos o bloques ordenados |
| Énfasis | cursiva para anglicismos, nombres comerciales, identificadores, ficheros y elementos de menú; comillas dobles rectas para literales; nunca negrita de énfasis dentro de un párrafo |

En LaTeX: `\tablename` a «Tabla» (la plantilla dice «Cuadro»), «Índice de
tablas» en lugar de «Índice de cuadros», y borrar los marcadores de la plantilla
(«Project Title: Project Subtitle», «First name, Family name (student)»): el
TFG del tutor de 2024 los dejó impresos.

## 3. Páginas iniciales (orden y textos oficiales)

Orden, igual en los dos TFG recientes del tutor; cada bloque empieza en página
impar y los versos quedan en blanco:

1. Portada: logotipos de la UGR y de la ETSIIT; «TRABAJO FIN DE GRADO»;
   «INGENIERÍA DE TECNOLOGÍAS DE TELECOMUNICACIÓN»; título (y subtítulo);
   «Autor» y nombre; «Director» y nombre; «Escuela Técnica Superior de
   Ingenierías Informática y de Telecomunicación»; «Granada, junio de 2026»
   (mes en minúscula).
2. Segunda portada: título, «Autor», «Director», sin fecha.
3. Resumen: título, autor, «Palabras clave:» (6–8, separadas por comas),
   «Resumen» en 3–4 párrafos (300–400 palabras: encuadre, qué se construyó,
   qué se evaluó y qué salió, aportación y límites). Siglas definidas también
   aquí.
4. Abstract: lo mismo en inglés («Keywords:», «Abstract»).
5. Autorización del alumno, literal de la plantilla:
   «Yo, NOMBRE APELLIDOS, alumno de la titulación Grado en Ingeniería de
   Tecnologías de Telecomunicación de la Escuela Técnica Superior de
   Ingenierías Informática y de Telecomunicación de la Universidad de
   Granada, con DNI NÚMERO, autorizo la ubicación de la siguiente copia de mi
   Trabajo Fin de Grado en la biblioteca del centro para que pueda ser
   consultada por las personas que lo deseen.» Debajo: «Fdo: NOMBRE
   APELLIDOS» y «Granada a día D de junio de 2026.»
6. Informe del director, literal (adaptado a un solo director; la
   categoría del tutor hay que confirmarla con él; en 2024 figura como
   «Profesor Titular de Universidad»):
   «D. Juan José Ramos Muñoz, Profesor Titular de Universidad del Área de
   Ingeniería Telemática del Departamento de Teoría de la Señal, Telemática y
   Comunicaciones de la Universidad de Granada.
   Informa:
   Que el presente trabajo, titulado TÍTULO, ha sido realizado bajo su
   supervisión por NOMBRE APELLIDOS, y autoriza la defensa de dicho trabajo
   ante el tribunal que corresponda.
   Y para que conste, expide y firma el presente informe en Granada a D de
   junio de 2026.
   El director:
   Juan José Ramos Muñoz»
7. Agradecimientos (opcional, sobrio, sin cierre emotivo).
8. Índice general (hasta el nivel 3), índice de figuras, índice de tablas.
9. Lista de acrónimos («Acrónimos»): sigla en negrita, expansión inglesa en
   cursiva y traducción entre paréntesis; solo las siglas que se usan (ABR,
   DASH, MPD, HTTP, QoE, MPC, CVaR, GRU, VBR, CBR, HAS, CDN, URL, JSON,
   CSV, SVG…).

Un solo índice, generado por Word, actualizado al final (los índices sin
actualizar son el error más repetido del corpus).

## 4. Esqueleto del cuerpo y qué lleva cada parte

El esqueleto del tutor (2017, 2024, 2025) coincide con el que fijó el
profesor para esta memoria: siete capítulos, bibliografía y anexos. Lo que
el corpus añade a cada uno:

- **Capítulo 1. Introducción (8–10 páginas).** Motivación y contexto;
  problema; objetivos en lista de viñetas con infinitivo («Diseñar…»,
  «Evaluar…»), numerables para que el capítulo 7 los responda uno a uno;
  alcance; «Estructura de la memoria» con una frase por capítulo (los siete
  TFG lo llevan). Sin resultados.
- **Capítulo 2. Estado del arte (12–16 páginas).** Donde se concentran las
  citas (en el corpus, del 50 al 70 % de las llamadas). Tabla comparativa
  de familias ABR. Cierra con las lagunas que justifican el enfoque.
- **Capítulo 3. Planificación y costes (8–10 páginas).** Lo piden los tres
  TFG del tutor (en 2017 va justo aquí, después del estado del arte): fases
  en viñetas con entradilla en negrita; diagrama de Gantt como figura;
  tabla de horas por fase con total; costes de hardware con amortización
  («vida útil de 3–4 años, N meses de proyecto»), software (libre: 0 €, se
  dice), recursos humanos con tarifa del alumno (20–25 €/h) y del tutor
  (50 €/h) y horas; tabla final de totales. Todo en pasado: las fases ya
  se hicieron. Las cuatro máquinas (Windows, WSL2 con GPU, VM cliente, VM
  servidor) entran como hardware amortizado.
- **Capítulo 4. Diseño (de Daniel, en Word).** Solo revisión de contenido.
- **Capítulo 5. Implementación (25–30 páginas).** Decisiones como
  alternativas → criterio → elección; código solo como fragmentos cortos que
  justifican una decisión (regla del plan), con el código completo remitido
  al material entregado; tablas para parámetros, mapas fórmula → código y
  componentes; figuras propias (arquitectura, bucle de decisión).
- **Capítulo 6. Evaluación (15–20 páginas).** Patrón del tutor:
  experimentos o preguntas numeradas, cada una con su tabla, la cifra, la
  interpretación física y la limitación reconocida en el mismo bloque. Aquí
  además: protocolo fijado antes (06_PROTOCOLO_FINAL), P1–P5 en una tabla
  con media, intervalos, ventanas +/−/= y p de Holm; descriptivos por
  controlador; secundario marcado como exploratorio. Cada número con su
  interpretación, sin «gana a todos».
- **Capítulo 7. Conclusiones y trabajo futuro (4–6 páginas).** Objetivo a
  objetivo; resultados principales sin números nuevos; limitaciones;
  trabajo futuro en viñetas con entradilla en negrita; resultados negativos
  como aportación. Sin valoraciones personales («en mi humilde opinión»).
- **Bibliografía.** Numérica por orden de aparición (IEEE, `unsrt`), solo lo
  citado; webs con «[En línea]. Disponible en: URL. [Último acceso: mes de
  año]»; títulos de artículos en inglés; sin parámetros de seguimiento en las
  URL; meses en español.
- **Anexos.** Configuración, comandos de reproducción, entorno, tablas
  largas, fragmentos extensos. El código entero no va en el cuerpo.

Extensión: cuerpos de 15 000 a 39 000 palabras en el corpus; para esta
memoria, 30 000–35 000 palabras de cuerpo (unas 100 páginas con figuras) y
lo largo a los anexos.

## 5. Objetos: figuras, tablas, ecuaciones, código, siglas, citas

- Toda figura y tabla se anuncia antes en el texto, se numera por capítulo y
  se comenta después. Mención en el texto con una sola convención en toda la
  memoria: el capítulo 4 de Daniel usa «Figura 4.3» y «figura 4.3» a partes
  iguales; se unifica a **«Figura 4.3» y «Tabla 4.1» con mayúscula** (la
  plantilla LaTeX y el TFG del tutor de 2024 lo hacen así), nunca «Fig.».
- Pie: «Figura N.M: Texto.»; si la figura es ajena, la cita al final del
  pie «… [n].»; nada de «Fuente: elaboración propia».
- Figuras propias en SVG (grises más azul `#1971c2` para la decisión,
  amarillo `#fff9db` para lo asíncrono o el medio, rojo `#c92a2a` para
  alertas) y PNG para Word; las de datos, generadas por script desde el
  paquete final. Sin figuras decorativas, sin capturas de código.
- Ecuaciones: frase de entrada terminada en dos puntos, ecuación centrada y
  numerada «(N.M)», y «donde …» definiendo cada símbolo con sus unidades en
  la frase siguiente. Solo para los mecanismos centrales.
- Siglas: «Expansión (SIGLA)» en el primer uso de cada capítulo si hace
  falta, y en la lista de acrónimos; anglicismos en cursiva y, si existe
  término en español, el español (pasarela, segmento, parada, rebuffering
  se mantiene como término técnico definido).
- Citas: «[n]» antes del punto; varias seguidas «[3], [7]». En los
  borradores de Claude la cita va como la clave del `.bib` entre corchetes
  («[yin2015mpc]») y Daniel la convierte al número al maquetar.
- Números: coma decimal en todo el documento; espacio entre cifra y unidad
  («4,1 %», «160 s», «2,5 Mbit/s»); la misma precisión en texto y tabla; los
  miles con espacio fino o sin separador («1208 sesiones», «35 032»).

## 6. Registro y redacción

Lo que hacen los TFG del tutor, filtrado por las reglas del profesor:

1. Impersonal con «se» en todo el cuerpo («se implementa», «se evaluó»).
   Nunca primera persona del singular; el plural de modestia («hemos») se
   evita aunque el corpus lo tolere.
2. Tiempos: presente para describir el sistema y la teoría; pretérito
   perfecto para lo hecho («se ha implementado»); indefinido para la sesión
   experimental («se ejecutó»); condicional para el trabajo futuro. Nunca
   futuro para lo ya realizado (defecto en tres de los siete TFG).
3. Cada capítulo abre con un párrafo que anuncia qué contiene y qué venía
   antes, y cierra con un resumen de dos o tres frases que enlaza con el
   siguiente (regla del profesor; el tutor lo hace en 2017). Cada apartado
   abre con una frase de anuncio.
4. Párrafos de 2–4 frases y 50–90 palabras; frases de 15–25 palabras; una
   idea por frase. Los párrafos de más de 120 palabras se parten.
5. Listas solo con entradilla en negrita y dos puntos, y solo para
   objetivos, requisitos, fases, componentes, limitaciones, logros y trabajo
   futuro; la argumentación y la discusión de resultados van en prosa.
6. Conectores sobrios: «Por tanto», «Sin embargo», «Además», «Por último»,
   «En primer lugar», «A continuación». Prohibidos los tics (rayas para
   incisos, «cabe destacar», «conviene subrayar», «dicho de otro modo», «en
   definitiva», «no es X sino Y» en serie, tríadas, «clave» y «robusto»
   como adjetivos de bombo, cierres efectistas).
7. Resultados: cifra con unidad, interpretación en la misma frase o la
   siguiente, comparación con la referencia y la limitación que toque.
   Resultados negativos dichos sin maquillar.
8. Cada decisión de diseño con la alternativa descartada y el motivo; cada
   afirmación con cita verificada en el PDF; cada recuento verificado por
   programa.
9. Terminología del entregado (`04_CORRESPONDENCIAS_NOMENCLATURA.md`):
   «controlador propio», «MPC robusto», «variante sin red», nunca nombres
   internos de desarrollo.

## 7. Reglas de salida para los borradores de Claude

1. Cero markdown en el texto del borrador: ni «#», ni «*», ni «|», ni acentos
   graves, ni emojis, ni viñetas por sistema, ni negritas de énfasis.
2. Entregable: un `.docx` por apartado en `docs/memoria/borradores_docx/`
   (`cap5_3_analizador_mpd.docx`…), hecho con la plantilla del § 2, con los
   títulos numerados escritos y en estilo de título para que Word genere los
   índices, los pies de figura y tabla en su estilo, y las citas como
   «[clave_bib]». En el chat, solo el resumen de lo que trae el paquete.
3. Figuras en `docs/memoria/figuras/` (SVG más PNG) y tablas dentro del
   `.docx`; notas «no van a la memoria» y chuletas de defensa en
   `docs/memoria/notas/` (ahí sí vale markdown).
4. Antes de entregar, pasar la lista: títulos numerados y en orden; toda
   figura y tabla referenciada antes y comentada después; pies con el
   formato del § 2; siglas definidas; coma decimal y unidades; impersonal;
   sin tics; sin cifras de desarrollo; sin claves internas; citas solo del
   `.bib` y verificadas; recuentos comprobados por programa; longitud dentro
   del presupuesto del apartado.

## 8. Lo que no debe aparecer y errores vistos en el corpus

No aparece en ningún TFG aprobado del corpus, y no aparecerá aquí: emojis,
colores de texto, subrayados, markdown, negrita o mayúsculas de énfasis,
notas al pie como muletilla, preguntas retóricas, lenguaje coloquial,
«Fuente: elaboración propia», capturas de código, listados largos en el
cuerpo, cinco niveles de numeración, capítulos de más del 40 % del cuerpo,
primera persona del singular en el texto técnico.

Errores repetidos que hay que evitar: índices sin actualizar; marcadores de
la plantilla sin borrar; «Cuadro» en los pies y «tabla» en el texto; pies sin
punto final o duplicados; fases y procedimientos ya hechos narrados en
futuro; entradas de la bibliografía nunca citadas; URL con parámetros de
seguimiento y meses en inglés; coma y punto decimal mezclados; cifras
distintas en texto y tabla; expansión de siglas repetida en cada uso o
metida en títulos; conclusiones sin cifras o con valoración personal.

## 9. Rasgos del tutor que conviene respetar

De sus tres TFG: planificación y presupuesto completos con Gantt, horas y
tarifas; introducción con «Estructura de la memoria»; evaluación con
experimentos numerados, tablas y discusión honesta de lo que no salió;
conclusiones breves ligadas a los objetivos; anexos prácticos (manual de uso,
reproducción); lista de acrónimos; citas a especificaciones y documentación
oficial además de a artículos; su grupo publica sobre redes y telemática
(carpeta `02_trabajos_locales_ugr` de la biblioteca: citar lo pertinente).

## 10. Lo que añade el TFG del tutor de 2024 (ficha `ficha_tutor_2024_marin.md`)

Confirma lo anterior: capítulo 2 «Planificación y Costes» justo tras la
introducción (Gantt, hardware amortizado a 3 años, software, personal con
12 ECTS × 25 h a 20 €/h y tutores a 50 €/h, cuadro con el total); objetivos
en lista en la introducción y conclusión que los repasa uno a uno con su
veredicto; estado del arte breve, un párrafo por trabajo que acaba diciendo
en qué se diferencia de este; capítulo de tecnologías con una frase de enlace
por herramienta («En este trabajo, X sirve para…»); figuras anunciadas antes
y descritas después (ejes, unidades, colores); cada resultado con su número
y su causa en la misma frase; código en apéndices remitido con «(véase el
Apéndice X)».

Errores suyos que no se copian: referencias cruzadas rotas («Figura 4.x»
para figuras del capítulo 5), plantilla del abstract sin rellenar, apéndices
más largos que el cuerpo con ficheros de configuración volcados enteros,
diseño narrado en futuro, resultados de una sola ejecución sin estadística.

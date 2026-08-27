# Borrador 4.8 — Separación entre ejecución y evaluación (+ cierre del capítulo)

> BORRADOR para masticar y reescribir (27/08/2026). Impersonal, frases cortas.
> Numeración de figuras/tablas provisional. Citas = claves de `bibliografia.bib`.
> Fuente técnica: `core/evaluacion/` del entregable (qoe.py y seleccion.py
> leídos; verificacion.py revisado) + paquete canónico (protocolo, gates,
> verificación).

---

### 4.8. Separación entre ejecución y evaluación

Los apartados anteriores describen el sistema que ejecuta sesiones. Queda la
última frontera del diseño: la evaluación es un sistema aparte, que decide
qué sesiones se ejecutan, qué significan sus resultados y cuándo es legítimo
compararlos. Esta separación no es una comodidad de organización, sino una
salvaguarda metodológica: el código que compite no participa en su propia
calificación. Cuatro piezas la componen: el plan de experimento, la métrica
congelada, las compuertas de validez y la verificación del paquete.

**El plan de experimento.** Un experimento se define por una configuración y
un preset que fija su tamaño. A partir del catálogo de trazas, el sistema
selecciona de forma determinista las ventanas de red del experimento: solo
considera trazas de la partición de evaluación, marcadas como utilizables y
con criterios mínimos de servibilidad, y las elige balanceando su
procedencia, con una semilla fija que hace la selección repetible. Las
trazas sintéticas se seleccionan aparte y quedan etiquetadas como
diagnóstico. Con las ventanas elegidas, el plan de sesiones es el producto
de tres factores: controladores, ventanas de red y perfiles de vídeo (más
las repeticiones configuradas). El punto metodológico central es el
emparejamiento por diseño: cada combinación de ventana y vídeo se ejecuta
con todos los controladores, de modo que las comparaciones posteriores son
siempre entre sesiones que afrontaron exactamente las mismas condiciones.
Para cada sesión planificada se genera su fichero de configuración completo,
que queda archivado: el protocolo del experimento es inspeccionable antes de
ejecutarlo y auditable después.

**La métrica congelada.** La calidad de experiencia se calcula en un módulo
puro e independiente, definido y fijado antes de ejecutar los experimentos,
que sigue la formulación compuesta clásica de la literatura
\cite{yin2015mpc}: recompensa por calidad, penalización por rebuffering y
penalización por inestabilidad entre segmentos consecutivos. Existen dos
variantes, una lineal (la métrica primaria) y una logarítmica (secundaria,
como análisis de sensibilidad), y ambas se computan únicamente sobre los
segmentos de régimen estable que marca la telemetría (apartado 4.6). La
definición formal y los pesos se detallan en el capítulo 6. Lo relevante
aquí es el principio: la métrica no se eligió a la vista de los resultados,
y su cálculo no comparte código con ningún controlador.

**Las compuertas de validez.** Antes de autorizar cualquier comparación, el
análisis evalúa un conjunto de condiciones objetivas sobre el paquete de
resultados, las compuertas de validez (Tabla 4.7). Si todas se superan, el
paquete queda habilitado para comparar y ordenar controladores; si alguna
falla, el paquete se degrada a material de diagnóstico y sus números no
sustentan conclusiones. La decisión, por tanto, no la toma el autor caso a
caso: la toma una regla fijada de antemano, y el resultado queda escrito en
el propio paquete. Este mecanismo demostró su utilidad durante el proyecto:
ejecuciones técnicamente completas quedaron descartadas como evidencia por
una compuerta caída, y se repitieron tras corregir la causa.

**[TABLA 4.7 — Compuertas de validez del experimento]**

| Compuerta | Qué garantiza |
|---|---|
| Sesiones reales completadas | Ninguna sesión real quedó a medias o fallida |
| Solo partición de evaluación | Ninguna traza de entrenamiento o prueba contaminó el experimento |
| Solo perfiles congelados (4 s) | Todo el contenido pertenece al formato experimental fijado |
| Sin respaldo en sesiones evaluables | El controlador con modelo decidió siempre por sí mismo |
| Inferencia verificada | Cada decisión del modelo dejó su rastro de auditoría completo |
| Sin artefactos antiguos | El paquete no mezcla restos de ejecuciones anteriores |
| Sintéticas informadas aparte | Lo sintético no se agrega con lo real en ninguna cifra |
| Resumen textual disponible | El paquete incluye su propio resumen legible |

*Pie: Tabla 4.7: Compuertas de validez que deben superarse para que un
paquete de resultados habilite comparaciones entre controladores.*

**La verificación del paquete.** Tras el análisis, una verificación
automática comprueba la integridad del paquete de evidencia: que están todos
los artefactos, que los conteos cuadran, que las gráficas declaradas
existen, que no hay sesiones fallidas sin justificar. El veredicto se
escribe junto a los resultados. El paquete final es autocontenido y sigue
una estructura fija (protocolo, ejecución, resultados, gráficas e informe),
de modo que un tercero puede auditar el experimento completo, desde el plan
hasta cada fichero de telemetría, sin acceso al entorno original.

Sobre esta base, el análisis estadístico se apoya en el emparejamiento del
plan: las comparaciones entre controladores se hacen por deltas pareados por
escenario, con intervalos de confianza e inferencia no paramétrica, y los
resultados se examinan también por distribuciones y colas, no solo por
medias, siguiendo las buenas prácticas señaladas en la literatura de
evaluación de QoE \cite{peroni2024qoePitfalls}. Su aplicación concreta y los
resultados se presentan en el capítulo 6.

**Resumen del capítulo.** *(cierre obligatorio del capítulo 4)* Este
capítulo ha descrito el diseño de la plataforma: una arquitectura de módulos
con responsabilidades separadas (4.1); el analizador del manifiesto, que
aísla al cliente del XML del MPD (4.2); la descarga con conexión persistente
y el buffer con tope que iguala el compromiso de todos los controladores
(4.3); dos motores de reproducción intercambiables, uno simulado para medir
sin ruido y uno real para verificar (4.4); una interfaz común de
controladores con un contrato de realimentación cerrado y salvaguardas para
los controladores con modelo (4.5); una telemetría que registra lo observado,
lo decidido y sus consecuencias, y que constituye el único puente hacia la
evaluación (4.6); unas condiciones experimentales fijadas en dos ejes
independientes, la red emulada por trazas reales y el contenido
caracterizado por sus tamaños reales (4.7); y una evaluación separada de la
ejecución, con protocolo emparejado, métrica congelada, compuertas de
validez y verificación automática (4.8). El capítulo siguiente desciende a
la implementación de estas piezas.

---

### Notas para Daniel (no van a la memoria)

- Citas usadas (2): `\cite{yin2015mpc}` (formulación compuesta de la QoE) y
  `\cite{peroni2024qoePitfalls}` (evaluar por distribuciones/colas, no solo
  medias). El resto es diseño propio.
- Verificado en código: qoe.py = módulo PURO (dataclasses congeladas,
  validación estricta, sin dependencias del cliente); pesos lineal 4.3 /
  suavidad 1.0, log 2.66, utilidad en Mbps, suavidad |Δ| con primera delta 0
  — los NÚMEROS van en 6.5, aquí solo el principio. seleccion.py: solo
  particion=="eval" + usable_en_eval + suelo de throughput para formal +
  selección balanceada determinista (semilla 606; sintéticas semilla+17,
  etiquetadas aparte). verificacion.py: checks nombrados + render markdown +
  detección de artefactos antiguos. Los 8 gates de la tabla son los del
  paquete canónico (resumen_resultados.md, gates 8/8 en sí).
- La frase "ejecuciones técnicamente completas quedaron descartadas por una
  compuerta caída y se repitieron" es la historia REAL del paquete del 06/08
  (gate de inferencia verificada caído por el desfase del reproductor →
  relanzado el 10/08). En la memoria va SIN fechas internas ni detalles; en
  la defensa, si preguntan "¿los gates sirven de algo?", esta es la prueba:
  el sistema descartó un resultado FAVORABLE por un defecto de auditoría.
  Eso es integridad metodológica demostrada con hechos.
- El preset del experimento final (12 ventanas reales + 3 sintéticas × 4
  vídeos × 5 controladores = 300 sesiones, ventana 300 s, 30 segmentos) va
  en 6.1/6.3 — aquí no se dan números para no duplicar.
- El resumen del capítulo cumple la regla del profesor (cierre con resumen).
  Cuando pases el capítulo a limpio, revisa que cada apartado tenga su
  referencia de figura/tabla correcta con la numeración final de LaTeX.
- Longitud: ~950 palabras con el resumen del capítulo incluido.

# Protocolo de los estudios complementarios de la evaluación final

Fijado el 14/10/2026, con el experimento final en marcha y ANTES de conocer
ninguno de sus resultados. Completa `PROTOCOLO_EVALUACION_FINAL.md`: mismo
sistema (versión final del controlador), mismas 15 ventanas, mismo banco de
pruebas, mismas métricas y misma estadística. Cada estudio se ejecuta una sola
vez y se informa tal cual salga.

## Estudio A. Ablación: qué aporta cada pieza del controlador propio

Pregunta: cuánto de la calidad del controlador propio se debe a la red
neuronal, cuánto al criterio de riesgo y cuánto a que su planificador optimiza
la misma métrica que se evalúa, con tamaños reales y horizonte de 5.

Controladores (los cinco en la misma ejecución, 300 sesiones, unas 10,5 h):

| Clave | Qué es | Qué aísla |
|---|---|---|
| `controlador_propio` | El controlador final, sin cambios | Referencia |
| `propio_mediana` | La misma red, pero el planificador decide solo con el escenario central (mediana) | El criterio de riesgo (CVaR) |
| `planificador_cuantiles_fijos` | El mismo planificador con CVaR, pero los cuatro escenarios salen de cuantiles fijos: la media armónica multiplicada por los cuantiles empíricos de la etiqueta de entrenamiento (ln C/C̄, por horizonte), calculados una sola vez sobre la partición de entrenamiento. Sin red | La predicción condicionada de la red |
| `planificador_robusto` | El mismo planificador (objetivo lineal, tamaños reales, horizonte 5) con un único escenario: la predicción del MPC robusto (media armónica / (1 + error máximo reciente)). Sin red ni riesgo | Alinear objetivo, tamaños y horizonte con la métrica |
| `mpc_robusto` | El MPC robusto clásico, sin cambios | Referencia clásica |

Comparaciones fijadas (pareadas por escenario, sesiones reales, mismo análisis
que la comparativa principal: diferencia media de QoE lineal, IC95 por
bootstrap, prueba exacta del signo y escenarios ganados, perdidos y
empatados):

1. `controlador_propio` frente a `planificador_cuantiles_fijos`: ¿aporta la red?
2. `controlador_propio` frente a `propio_mediana`: ¿aporta el criterio de riesgo?
3. `planificador_robusto` frente a `mpc_robusto`: ¿cuánto se debe a alinear
   objetivo, tamaños y horizonte?
4. `controlador_propio` frente a `planificador_robusto`: el controlador propio
   frente al clásico mejor alineado.

Para estas cuatro comparaciones, la significación se declara con la corrección
de Holm al 5 %; se informan también los valores p sin corregir.

Repetibilidad: `controlador_propio` y `mpc_robusto` aparecen también en la
comparativa principal con las mismas ventanas y vídeos; se informa, escenario a
escenario, la fracción de trayectorias idénticas y la diferencia absoluta media
de QoE entre las dos ejecuciones (ruido del banco de pruebas).

## Estudio B. Contenido que el modelo no ha visto

Pregunta: ¿funciona el controlador propio, sin reentrenar, con un vídeo que no
forma parte de los ocho del entrenamiento?

- Vídeo nuevo de 10 min a 30 fps, de contenido distinto a los del
  entrenamiento (cortometraje abierto con licencia CC-BY), codificado en la VM
  servidor con la misma herramienta, la misma escalera de seis niveles
  (300–4300 kbit/s) y segmentos de 4 s; su descriptor de tamaños reales se
  extrae igual que los demás. Se informa su variabilidad de tamaños (si supera
  el 16 % del entrenamiento, el estudio es además de extrapolación).
- Los cinco controladores de la comparativa principal, las mismas 15 ventanas
  y solo ese vídeo: 75 sesiones, unas 2,6 h.
- Se informa: auditoría del controlador propio (respaldos), la misma tabla y
  las mismas comparaciones pareadas que en la comparativa principal, y si el
  orden de los controladores coincide con el de los vídeos de la evaluación.

## Estudio C. Calidad del predictor (sin ejecutar sesiones)

- Sobre la partición de validación (111 630 muestras): pérdida de cuantiles
  por horizonte y cuantil del predictor frente a dos referencias sin
  aprendizaje (la media armónica como valor único y los cuantiles fijos del
  estudio A), y cobertura empírica de cada cuantil.
- En la comparativa principal y en el estudio B: cobertura en lazo cerrado
  (fracción del throughput medido después por debajo de cada cuantil predicho
  para el segmento siguiente) y error de la mediana frente a la media armónica.

## Orden y salvaguardas

1. Se implementan las variantes en el código de entrega como controladores
   nuevos, sin cambiar los existentes. Antes de ejecutar nada se comprueba,
   reproduciendo fuera de línea las 1740 decisiones del paquete final, que el
   controlador propio decide exactamente igual con el código ampliado.
2. Los cuantiles fijos se calculan una vez sobre la partición de
   entrenamiento y quedan en un fichero versionado.
3. Prueba de humo de las variantes en la VM; después, el estudio B y el
   estudio A, cada uno una sola vez.
4. Se informa todo, favorable o no. Ningún estudio se repite ni se modifica a
   la vista de sus resultados.

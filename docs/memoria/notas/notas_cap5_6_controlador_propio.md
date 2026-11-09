# Notas del 5.6 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap5_6_controlador_propio.docx` (≈3250 palabras de cuerpo,
9 páginas, 6 subapartados, Figuras 5.4 y 5.5, Tablas 5.9 a 5.12, ecuaciones 5.7 a 5.12, 7 citas).
Generado por `docs/memoria/apoyo/generar_cap5_6.py` a partir de `apoyo/resumen_propio_final.json`,
que produce `apoyo/reproducir_propio_final.py` (reproducción de las 4379 decisiones del propio del
paquete final, 86 s en CPU). Sustituye al borrador v2 del 13/10 (`borradores/cap5_6_controlador_propio.md`,
hecho con el paquete de agosto, que queda como histórico).

## Qué cambia respecto al borrador v2 de octubre

- El comparador es el MPC robusto canónico (horizonte 5, QoE lineal, tamaños reales): la antigua
  Tabla 5.6 de «tres diferencias» pierde sentido. Ahora la Tabla 5.9 dice que planificador, tamaños y
  objetivo son los mismos y que solo cambian la predicción (4 cuantiles frente a 1 valor rebajado) y la
  agregación (3 peores frente a 1). Es la frase de la defensa: «frente al MPC robusto, lo único que cambia
  es cómo se predice».
- Desaparece el párrafo de las dos discrepancias entrenamiento/ejecución (rebuffering reciente a cero,
  progreso sobre el vídeo completo): el código final las calcula como en el entrenamiento
  (`constructor_entradas.py`, `entradas_planificador.py`). Comprobado en el código.
- La carga del bundle es al crear el controlador (C8), no en la primera decisión.
- CVaR descrito como ⌈α·K⌉ peores de K = 4 (07_RESULTADO §8): α = 0,75 → 3; saltos de 0,25.
- Nuevo 5.6.5: las tres variantes de ablación como diseño del experimento (C4), con el mapa a P3–P5.
- Todos los números salen del paquete final; ninguno del de agosto.

## Reproducción que hace el script (regla del ejemplo real)

- `reproducir_propio_final.py`: 151 sesiones del propio (148 reales + 3 sintéticas), 4379 decisiones
  reinyectadas con el bundle de `03_modelos` (torch 2.6.0 CPU en Windows; la VM usó 2.4.1):
  4379/4379 idénticas en nivel y tasa, 0 respaldos. Variantes sobre el mismo estado solo en las 4292
  reales. Guarda un JSONL por decisión fuera del repo (`TFG\apoyo_memoria\final\`).
- Regla del ejemplo (fijada antes de mirar): sesión del propio con la misma ventana (real_004 de Oboe)
  y vídeo (Blender 60 fps) que el ejemplo del 5.5, y el mismo segmento (6). Resultado: `s00054`,
  buffer 15,21 s, nivel previo 0. Coincidencia útil: el cuantil 0,10 del propio (0,497 Mbit/s) casi
  iguala la predicción robusta del MPC en su sesión gemela (0,499), y ambos eligen 0 1 1 1 1. Decirlo
  en la defensa: dos caminos distintos a la misma prudencia en ese estado.
- Propiedad de orden (puntuaciones no decrecientes con el cuantil, todas las secuencias): 4292/4292.

## Fuente de cada número

| Dato | Fuente |
|---|---|
| 29 claves prohibidas, 25 campos de diagnóstico, 20 motivos | `constantes_entradas.py`, `diagnosticos_red.py` (contados) |
| GRU 96, MLP 96/64, dropout 0,1, 5 miembros, cuantiles, horizonte 5 | `03_modelos/.../configuracion_modelo.json` |
| α 0,75, ensanchado 1,0, pesos 4,3 y 1 | `configuracion_planificador.json` |
| 46 292 parámetros por miembro, 231 460 | contados con PyTorch en el script |
| acotación 0,15–4 veces la base | `bundle.py` (`RATIO_LOG_MIN/MAX` y `filas_log_ratio_a_bps`) |
| ensanchado: mediana 1,0 %, p90 2,4 %, máx 7 % (descenso del q10 del primer horizonte) | `resumen_propio_final.json` (σ de las medianas de los 5 miembros, exp(−0,8σ)) |
| inferencia 1,2 ms mediana, 3,3 ms máx | `feedback_ms_inferencia_red` de las 4379 decisiones |
| decisión completa 2,9 ms mediana, p99 5,9 ms, máx 22,4 ms | `ms_decision_politica` de las 4379 filas (el máximo es una primera decisión; 07_RESULTADO: solo 4 de 35 032 pasan de 20 ms) |
| Tabla 5.12 (1279 / 200 / 81 / 363 / 174 de 4292) | `resumen_propio_final.json` |
| 474 150 muestras de los cuantiles fijos | `cuantiles_fijos.json` |
| ejemplo: cuantiles 0,497/0,716/0,899/1,091; secuencias 0 2 3 3 3 (−102,68, −28,53, 5,50, 5,50; CVaR −41,91) y 0 1 1 1 1 (2,85 ×4); medido después 0,93 Mbit/s | `resumen_propio_final.json`, ejemplo |

## Citas

- `yan2020puffer` (p. 2–3: predictor probabilístico de tiempos de transmisión que informa a un MPC;
  Fugu), `kan2021bayesmpc` (p. 2: BNN, incertidumbre aleatoria y epistémica, región de confianza, peor
  caso), `yin2015mpc` (horizonte deslizante): verificadas en PDF.
- `cho2014gru`, `koenker1978quantiles`, `lakshminarayanan2017ensembles`, `rockafellar2000cvar`: en el
  .bib, verificadas por Crossref en agosto, SIN PDF en `biblioteca_final`. Se citan por lo que son
  (GRU, regresión cuantílica, deep ensembles, CVaR), sin atribuirles frases. **Pedir permiso a Daniel
  para descargar los cuatro**: Cho 2014 (arXiv 1406.1078, ~0,6 MB), Lakshminarayanan 2017 (arXiv
  1612.01474, ~1,5 MB), Rockafellar y Uryasev 2000 (Journal of Risk; PDF libre en la web del autor,
  ~0,3 MB), Koenker y Bassett 1978 (Econometrica, JSTOR: acceso UGR).

## Preguntas probables del tribunal

1. **¿Qué hace exactamente tu planificador?** Ecuación (5.12): calidad menos cambios menos 4,3 veces el
   rebuffering medio simulado en los tres escenarios no optimistas, con el tamaño real de cada segmento.
2. **¿Por qué α = 0,75?** Barrido en validación con el predictor anterior (junio); el valor exacto
   importa poco: cambiar a peor caso o a media de los cuatro mueve el 4,7 % y el 1,9 % de las
   decisiones (Tabla 5.12). Con K = 4 solo hay cuatro α distintos.
3. **¿Es un CVaR de verdad?** Es un CVaR discreto sobre cuatro escenarios de cuantil no equiprobables:
   aproximación prudente, declarada como tal.
4. **¿Para qué el ensemble?** Desconfianza del modelo: en el final el desacuerdo fue pequeño (mediana
   1 %, máx 7 % de rebaja del q10) y cambió el 4,1 % de las decisiones, casi siempre a la baja.
5. **¿El tamaño real importa?** Cambia el 8,5 % de las decisiones, en los dos sentidos (130 abajo, 233
   arriba): hace al controlador más preciso, no más conservador.
6. **¿Cómo sé que decidió tu modelo?** 4379 decisiones auditadas sin respaldo y reproducidas fuera de
   línea con el paquete archivado (35 032 en total con la auditoría de 07_RESULTADO).
7. **¿Elegiste el ejemplo que mejor queda?** No: misma ventana, vídeo y segmento que la Figura 5.3,
   decidido antes de mirar.
8. **¿Por qué la mediana sola no sirve?** En el ejemplo elige 0 2 3 3 3: 5,50 en el escenario central
   y −102,68 en el pesimista. Es exactamente el fallo de P5 en el capítulo 6 (0,83 paradas por sesión).
9. **¿Qué pasa con un vídeo nuevo?** Se mide en el capítulo 6 con Tears of Steel (exploratorio); el
   predictor no ve el contenido, el planificador lee su tabla.

## Detalles que el texto no cuenta

- `alfa_riesgo_por_buffer` sigue en `planificador.py` (0,25/0,50/0,75/1 por tramos de buffer) y solo
  actúa si no se pasa α; la configuración pasa 0,75.
- El controlador acepta `alfa_riesgo` por configuración y lo prioriza sobre el del bundle (ambos 0,75).
- `torch.set_num_threads(1)` y tres pasadas de calentamiento del modelo al cargar (C8).
- La máscara de acciones es siempre completa en el experimento (6 acciones válidas).
- El motivo `perfil_video_no_disponible` no está en el vocabulario cerrado y se registraría como
  `fallo_inferencia`; nunca ocurrió.
- Las «entradas candidatas» que el constructor calcula y audita no las usa el predictor (resto).

## Qué se puede recortar (≈ 600 palabras sin perder contenido)

Párrafo de precedentes (si el cap 2 presenta Fugu y el MPC bayesiano), el párrafo del paquete del modelo
(repite el 5.1), la analogía del radioenlace y la mitad del párrafo de límites. Mantener (5.11), (5.12),
la Figura 5.5 y la Tabla 5.12.

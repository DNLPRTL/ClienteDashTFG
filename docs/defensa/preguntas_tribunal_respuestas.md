# Posibles preguntas del tribunal — con respuestas preparadas

Fecha: 2026-08-05. Estudiar junto a `apropiacion_codigo_mpc_prudente.md`.

## A. Diseño del controller

**1. ¿Por qué predictor + planner y no RL end-to-end (tipo Pensieve)?**
Porque separa lo aprendible de lo verificable: la red aprende SOLO a predecir
throughput (problema supervisado, medible con calibración), y la decisión la toma
un optimizador determinista e inspeccionable. RL end-to-end lo intentamos en
líneas previas (SPBC, imitación) y no superó a los clásicos: quedó documentado
como resultado negativo. Además es el paradigma validado en producción por
Fugu/Puffer (Stanford).

**2. ¿Por qué predecir cuantiles y no la media?**
La media esconde el riesgo: dos redes con la misma media pueden tener colas muy
distintas, y el stall vive en la cola. Los cuantiles dan una distribución
predictiva; el planner puede ser conservador cuando la cola inferior es mala.
La calidad se audita con calibración (cobertura empírica ≈ nivel nominal).

**3. ¿Qué es exactamente el CVaR que usáis?**
Evaluamos cada secuencia de acciones bajo los K=4 escenarios de cuantil y
promediamos los `ceil(α·K)` peores. Con α=0.75 (el valor del experimento final):
media de los 3 peores escenarios (q10, q25, q50), descartando el optimista.
Es una aproximación discreta y conservadora del CVaR clásico.

**4. En el código hay una regla adaptativa buffer→alpha, ¿se usó?**
En los diagnósticos offline sí; en la evaluación final se fijó α=0.75 para todos
los estados (así el resultado mide UNA política de riesgo bien definida, sin
acoplar dos mecanismos). La regla adaptativa queda como trabajo futuro evaluado
solo preliminarmente.

**5. ¿Los cuantiles no son equiprobables y los tratáis como escenarios iguales?**
Cierto: (0.10, 0.25, 0.50, 0.75) no reparten la probabilidad uniformemente.
Tratarlos como equiprobables sobrepondera la cola inferior → sesgo conservador
DELIBERADO, coherente con el objetivo (evitar stalls). No afecta a la validez de
la comparación porque es parte fija del controller evaluado.

**6. ¿Por qué GRU y no LSTM/Transformer en v2?**
El historial es corto (últimos pasos de descarga); una GRU pequeña capta la
tendencia con menos parámetros y menos latencia. Un Transformer está
sobredimensionado para secuencias de esta longitud y este presupuesto de datos.

**7. ¿Qué aporta el ensemble frente a un solo GRU?**
Incertidumbre EPISTÉMICA: 5 modelos con semillas distintas discrepan más en
ventanas raras (fuera de distribución). Esa discrepancia ensancha la cola
inferior de la predicción combinada → prudencia automática donde el modelo sabe
menos. La ablación lo respalda: v2 mejora a v1 con CI pareado [+0.020, +0.168].

**8. ¿Cómo garantizáis que los cuantiles no se crucen?**
v2: por construcción (base + incrementos softplus acumulados). v1 (MLP): gate de
crossing en entrenamiento (≤2%) y re-ordenado defensivo en runtime.

## B. Fidelidad al medio (VBR)

**9. ¿Por qué importa el VBR si el MPD declara bitrates?**
Porque el tiempo de descarga real depende de los BYTES reales del segmento, no
del nominal. Medimos los tamaños en el servidor: hay segmentos bastante por
encima del nominal (vbr_cv_max hasta ~0.16 en Blender 60fps). Un planner CBR
subestima sistemáticamente el riesgo justo en los picos. Fue la causa raíz del
fracaso del Neural-MPC anterior.

**10. ¿El controller "hace trampa" al conocer los tamaños reales?**
No: el cliente DASH real también los conoce (el MPD/las cabeceras permiten
conocer el tamaño del siguiente segmento; players como dash.js exponen esa
información, y MPC clásico ya la usa en la literatura, Yin 2015). Lo que NUNCA ve
es el futuro de la red ni metadatos de la traza (contrato de features con lista
de campos prohibidos y auditoría).

**11. ¿Y si cambia el vídeo? ¿Está ajustado a un contenido?**
El dataset de entrenamiento rota 8 perfiles de medio y en Phase 6 cada sesión
inyecta el perfil del vídeo que reproduce (4 vídeos distintos, 30 y 60 fps, dos
contenidos). El predictor además es agnóstico al medio: predice red.

## C. Validez experimental

**12. ¿Por qué debemos creer que la comparación es justa?**
Los 6 controllers corren en el MISMO cliente, mismas 60 ventanas de traza
(pareadas escenario a escenario), mismos 4 vídeos, misma QoE congelada de
antemano (`qoe_linear_v1`), misma semilla. Los baselines están implementados
fieles a sus papers (con paper_card y evidencia por baseline). Y robust_mpc casi
empata con nuestro v2: si hubiéramos amañado algo, no habría quedado tan fuerte.

**13. ¿Qué significa exactamente el "empate" con robust_mpc?**
ΔQoE pareado +0.060 con CI95 [−0.05, +0.21] y sign test p=0.54 → no hay evidencia
de superioridad en QoE media. El claim es: misma QoE estadísticamente, con MENOS
rebuffering (stalls/sesión 0.29 vs 0.44; sesiones >5 s 12% vs 23%). No decimos
"ganamos a todos"; decimos "frontera calidad-riesgo mejor en la parte de riesgo".

**14. ¿Por qué hay 24 empates exactos de 48 escenarios contra robust?**
Son ventanas fáciles: ambos controllers saturan la escalera sin stalls y toman
decisiones idénticas → sesiones idénticas segmento a segmento. La diferencia
entre controllers solo puede aparecer en ventanas difíciles, y ahí es donde se
mide.

**15. ¿n=48 no es pequeño?**
Por eso reportamos CI bootstrap + sign test exacto y NO reclamamos victoria
(el CI incluye 0). 48 escenarios pareados (12 ventanas × 4 vídeos) es lo que el
presupuesto de cómputo permitió con 6 controllers (360 sesiones); la dirección
de los resultados es consistente entre vídeos y buckets.

**16. ¿Las trazas sintéticas contaminan el resultado?**
No: están en sesiones separadas (72), se reportan aparte y los agregados y la
estadística usan SOLO las 288 reales. Las sintéticas son diagnóstico controlado.

**17. ¿Hay fuga de información entrenamiento→evaluación?**
Splits por `leakage_group` (nunca por filas), eval reservado desde Phase 3 y
nunca usado para entrenar ni calibrar; en Phase 6 la selección exige
`split=eval`. El modelo no ve identificadores ni futuro (lista de campos
prohibidos verificada en código y tests).

**18. ¿Por qué la métrica lineal de Yin/MPC y no VMAF?**
`qoe_linear_v1` se congeló ANTES de evaluar (contrato del proyecto) y es la
métrica estándar de la línea MPC/Pensieve, comparable con la literatura. VMAF
requiere artefactos perceptuales por segmento que quedaron explícitamente fuera
de alcance (deferred y documentado). qoe_log se reporta como sensibilidad.

**19. Los MPC clásicos optimizan otra utilidad interna, ¿no les perjudica?**
Optimizan log-rate-ratio internamente y se evalúan con QoE lineal; esa decisión
va EN CONTRA de nuestro controller (que sí optimiza la métrica de eval) y aun
así robust_mpc empata → refuerza que no hay amaño. Documentado como sutileza.

**20. ¿El peor caso de v2 (P5 = −3.7)?**
Concentrado en la traza real con outage (real_012) + el vídeo más pesado
(Blender 60fps): con caída total de red, cualquier política que haya comprado
calidad sufre. rate_based es más seguro en esa cola a costa de mucho menos
bitrate el resto del tiempo. Es el trade-off que la memoria discute; mitigarlo
(p.ej. α adaptativo) es trabajo futuro.

**21. ¿Latencia de decisión?**
~190 ms de media (enumeración 6^5 en Python puro), p95 < 300 ms, frente a
segmentos de 4 s → sobra margen. No se optimizó (poda/beam/vectorización) porque
no era cuello de botella; sería trivial reducirla.

**22. ¿Cómo sé que la IA decidió de verdad en todas las sesiones (y no el fallback)?**
Telemetría por segmento: 1740/1740 filas de cada controller propio auditadas
(bundle cargado, hash OK, features OK, acción válida, inferencia > 0 ms,
fallback=0, diagnostic=0). El gate `propios_with_verified_neural_inference`
falla el paquete entero si una sola fila no cumple.

**23. ¿Puedo reproducir el experimento?**
Sí: protocolo determinista (semilla 606 → mismas ventanas), configs de cliente
por sesión guardadas en el paquete, bundles con sha256, receta en
`docs/defensa/material_reproducibilidad.md`. El análisis se puede re-derivar del
paquete sin re-ejecutar sesiones.

## D. Proceso / honestidad

**24. ¿Qué NO funcionó por el camino?**
SPBC/SPC (RL con preferencias), el scorer Q_H, y Neural-MPC v2 (más agresivo →
más rebuffer, peor que robust). Todos documentados como resultados negativos, y
"más datos" tampoco mejoró por sí solo: la palanca fue fidelidad al medio +
objetivo con riesgo. Contarlo así demuestra método, no debilidad.

**25. ¿Qué mejorarías con más tiempo?**
(a) α adaptativo evaluado formalmente; (b) afinar la cola extrema (outages);
(c) VMAF/P.1203 como métricas perceptuales; (d) más ventanas eval para estrechar
el CI; (e) red real (no emulada) tipo despliegue Puffer.

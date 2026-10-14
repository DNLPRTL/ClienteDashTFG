# Protocolo de la evaluación final

Fijado el 14/10/2026, antes de ejecutarla. Esta es la evaluación que presenta la
memoria: se ejecuta una sola vez y sus resultados se informan tal cual, sean
favorables o no.

## 1. Sistema evaluado: versión final del controlador propio

Código: `TFG Material\01_codigo\ClienteDashTFG` (huellas en
`hashes_codigo_final.sha256`). La versión anterior está archivada en
`TFG\legacy\codigo_entrega_20261014_antes_version_final\`.

Cambios respecto a la versión anterior. Ninguno se eligió a la vista de
resultados de calidad: cada uno corrige un defecto concreto y se verificó
antes de ejecutar (scripts en `verificacion/`).

| Cambio | Defecto que corrige | Verificación |
|---|---|---|
| Planificador vectorizado (`core/modelo_propio/planificador.py`) | 7776 secuencias en Python puro: 174 ms por decisión, dependiente de la velocidad de la máquina | Misma acción, secuencia, CVaR y rebuffering en 3480/3480 decisiones registradas, bit a bit con la suma de Python 3.8 de la VM; ≈4 ms por decisión frente a 280 ms en Windows |
| Inferencia con un hilo (`core/modelo_propio/bundle.py`) | Con varios hilos, la latencia de una red tan pequeña se dispara si la CPU está ocupada (origen de los respaldos por latencia) | Predicciones idénticas bit a bit con 1 y 14 hilos en 3480 estados; media 0,87 ms frente a 1,97 ms; máximo con la CPU saturada 10,8 ms frente a 38,5 ms |
| Calentamiento del modelo al cargarlo (`bundle.py`) | La primera inferencia de cada proceso es lenta | Sin efecto en las predicciones (el modelo no tiene estado) |
| Entradas calculadas como en el entrenamiento (`core/controladores/constructor_entradas.py`, `controlador_propio.py`) | El progreso usaba los 151 segmentos del vídeo en vez de los 30 de la sesión; el rebuffering reciente valía siempre 0; el historial no incluía la descarga del segmento de calentamiento | Entradas idénticas a las del entrenamiento, construidas a partir de las mismas observaciones, en 3360/3360 decisiones (k = 2..29); 0 respaldos al reinyectar las 3480 decisiones registradas |

No cambian: el modelo (bundle de `03_modelos`, mismas huellas), el dataset,
α = 0,75, los pesos del objetivo, las salvaguardas (latencia máxima 50 ms,
respaldo MPC robusto), los controladores clásicos, el preset `tfg_final`, la
semilla 606, la métrica y el código de análisis.

Efecto en las decisiones, medido sobre los estados registrados de las
ejecuciones anteriores: cambia el nivel en el 6,8 % de las decisiones de
sesiones reales (98 a un nivel más bajo, 92 a uno más alto).

## 2. Ventanas de red

Mismo algoritmo y misma semilla (606), con la nueva opción
`experimento.grupos_fuga_excluidos` de `config/evaluacion.local.json`: los 27
grupos de captura de todas las ventanas reales que han aparecido en cualquier
ejecución anterior (las 15 copiadas en Windows; las 8 que solo estaban en la VM
son diagnósticos y humos cuyas ventanas están incluidas, porque la selección es
determinista). Resultado: 12 ventanas reales que nunca se han ejecutado, de 12
grupos distintos, con la misma mezcla de dificultad que el sorteo sin
exclusiones (baja 4, alta 1, alta variable 2, media 1, media variable 1, muy
alta 3), y las 3 sintéticas de diagnóstico. Lista exacta en
`ventanas_esperadas_final.txt`.

## 3. Ejecución

Una sola vez, en la VM cliente, lanzada desde la interfaz gráfica con el preset
`tfg_final` y los cinco controladores: 300 sesiones (240 reales y 60
sintéticas). Antes: comprobaciones de `evaluacion_final.sh comprobar` (código,
modelo, catálogo, servidor, ventanas esperadas y velocidad del planificador) y
la prueba de humo de 5 sesiones. En el anfitrión: sin limitación de energía
para VirtualBox, ventana de la VM visible y sin otras cargas pesadas.

## 4. Análisis (fijado de antemano)

1. Compuertas y verificación del propio paquete.
2. Comparación pareada del controlador propio con cada clásico, con el análisis
   del paquete: diferencia media de QoE lineal por escenario, IC95 por
   bootstrap, prueba exacta del signo y escenarios ganados, perdidos y
   empatados. Una diferencia se declara significativa si p < 0,05 en la prueba
   del signo; su sentido lo dan los escenarios ganados frente a los perdidos.
3. Descriptivos por controlador: QoE media y mediana, colas, bitrate,
   rebuffering, paradas por sesión y sesiones con más de 5 s y de 10 s de
   parada.
4. Mecanismo del controlador: reproducción fuera de línea de sus decisiones y
   efecto de cada componente (Tabla 5.7), con los scripts de
   `docs/memoria/apoyo/`.
5. Predictor: calibración en lazo cerrado (fracción del throughput medido
   después por debajo de cada cuantil predicho) y error de su mediana frente a
   la media armónica.

Se informa todo, favorable o no.

## 5. Si algo falla

- Una compuerta no superada: se diagnostica leyendo solo compuertas,
  verificación y registros. Un defecto del banco de pruebas ajeno a las
  decisiones se corrige y se repite, declarándolo; un comportamiento del
  sistema es un resultado y el paquete solo se usa si se demuestra, antes de
  abrir métricas de calidad, que no alteró ninguna decisión.
- Una interrupción (apagón, reinicio): se reanuda el mismo paquete; las
  sesiones completadas no se repiten.
- Nada se repite ni se cambia por motivos de resultados.

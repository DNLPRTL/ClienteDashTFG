# Resultado de la réplica (segunda evaluación)

Analizado el 14/10/2026 siguiendo `AFIRMACIONES_A_COMPROBAR.md`, que se fijó y
commiteó antes de abrir ningún resultado de calidad. Paquete:
`20261013_233745_tfg_final` (VM cliente, 13/10 23:37 a 14/10 ≈ 10:03).

## 1. Validez del paquete

- 300/300 sesiones completadas, 0 fallidas, verificación técnica OK (15/15
  comprobaciones), las 15 ventanas exactas de `ventanas_esperadas.txt`, las 60
  configuraciones del controlador propio con los mismos parámetros que en
  agosto y el mismo entorno registrado (Python 3.8.10, kernel 5.15.0-139).
- **Compuertas: 6/8.** Fallan `propios_sin_respaldo_en_evaluables` y
  `propios_con_inferencia_verificada` por una única decisión: la primera de la
  sesión `s00005` (primera sesión del controlador propio), cuya inferencia
  tardó 149,6 ms (límite 50 ms) y se delegó en el respaldo. El modelo había
  planificado el nivel 0 y el respaldo eligió el nivel 0.
- **Reproducción fuera de línea: 1740/1740** acciones del planificador y
  1740/1740 niveles finales coinciden con los registrados (torch 2.6.0 en
  Windows). Se cumple el criterio fijado: el paquete se usa con la salvedad
  declarada. El veredicto automático del paquete no se ha modificado.
- **Sensibilidad sin el escenario afectado** (`real_001_0eabc04a0b` con
  Paseo 30 fps, 5 sesiones): ninguna conclusión cambia.

## 2. Diferencia del banco de pruebas: VM más lenta

Durante toda la réplica la VM fue ≈1,8 veces más lenta que en agosto: el
controlador propio tardó 315 ms de media por decisión (agosto: 174 ms,
estable toda la noche) y 2,18 ms por inferencia (agosto: 1,25 ms). Código,
modelo y software de la VM son idénticos; la causa probable está en el
anfitrión (estado de energía o prioridad de la VM), no verificable desde el
paquete. Solo afecta de forma apreciable al controlador propio, el único que
tarda más de 1 ms en decidir: mientras decide, no descarga.

Medido con las 60 sesiones sintéticas, idénticas en las dos evaluaciones
(`repetibilidad_sinteticas.py`):

| Controlador | Trayectoria idéntica | dQoE medio (réplica − agosto) |
|---|---|---|
| BBA | 11/12 | +0,007 |
| MPC robusto | 9/12 | −0,003 |
| Basado en tasa | 7/12 | −0,019 |
| BOLA | 8/12 | −0,066 |
| Controlador propio | 0/12 | −0,060 |

La segunda evaluación es, por tanto, en todo caso desfavorable al controlador
propio. Las ventanas nuevas son además más fáciles (el basado en tasa no tuvo
ninguna parada).

## 3. Afirmaciones (solo trazas reales, 48 escenarios por evaluación)

| # | Afirmación | Agosto | Réplica | Veredicto |
|---|---|---|---|---|
| 1 | QoE media más alta de los cinco | Sí: 2,010 (2.º basado en tasa 1,970; robusto 1,947) | No: robusto 2,831, propio 2,822 | **No confirmada** |
| 2 | Sin diferencia significativa con el MPC robusto | Δ +0,063 [−0,043; +0,209], p = 0,15, G8/P16/E24 | Δ −0,009 [−0,077; +0,066], p = 0,064, G7/P17/E24 | **Confirmada** |
| 3 | Mejor que BBA y BOLA con significación | BBA +0,222, p = 3,3e-6, G40/P8; BOLA +0,766, p = 1,0e-7, G42/P6 | BBA +0,207, p = 1,4e-8, G43/P5; BOLA +0,762, p = 1,6e-11, G45/P2 | **Confirmada** |
| 4 | Mejor que el basado en tasa (prueba del signo) | +0,040 [−0,149; +0,229], p = 2,2e-4, G37/P11 | +0,323 [+0,156; +0,475], p = 1,5e-9, G44/P4 | **Confirmada** |
| 5 | Menos paradas y menos sesiones > 5 s que el robusto | 0,33 frente a 0,46; 12,5 % frente a 25 % | 0,15 frente a 0,21; 8,3 % frente a 8,3 % | **No confirmada** (la parte de sesiones > 5 s) |
| 6 | Sin respaldo y todo auditado | 0 respaldos | 1 respaldo (sin cambio de acción) | **No confirmada** tal como se formuló |

Δ = propio − rival en QoE lineal media por escenario, IC95 por bootstrap del
análisis de entrega, p = prueba exacta del signo; G/P/E = escenarios ganados,
perdidos y empatados por el propio.

**Observaciones descriptivas coherentes en las dos evaluaciones** (no
estaban en la lista previa; se presentan como descriptivas, sin contraste):
frente al MPC robusto, el propio tiene menos rebuffering medio (3,04 frente a
3,85 s; 0,79 frente a 0,96 s), menos paradas por sesión, menos sesiones con
más de 10 s de parada (10,4 % frente a 12,5 %; 4,2 % frente a 8,3 %), algo
menos de bitrate (2636 frente a 2685 kbit/s; 3088 frente a 3151) y la mediana
de QoE más alta de los cinco. En la comparación escenario a escenario, el
robusto gana más escenarios que el propio en las dos (16 frente a 8; 17 frente
a 7, con 24 empates), sin significación.

## 4. Mecanismo del controlador (segunda columna de la Tabla 5.7)

1392 decisiones reales por evaluación; reproducción exacta y puntuaciones
ordenadas por cuantil en el 100 % de las 3480 decisiones de las dos.

| Variante | Agosto | Réplica |
|---|---|---|
| Solo mediana | 329 (23,6 %), CVaR más bajo en 307 (93 %) | 233 (16,7 %), CVaR más bajo en 212 (91 %) |
| Solo cuantil 0,10 | 20 (1,4 %) | 22 (1,6 %) |
| Media de los cuatro (α = 1) | 16 (1,1 %) | 8 (0,6 %) |
| Tamaños nominales | 68 (4,9 %), 32 más bajo / 36 más alto | 41 (2,9 %), 21 / 20 |
| Sin ensanchado epistémico | 61 (4,4 %), 43 más prudente (70 %) | 37 (2,7 %), 24 (65 %) |
| Progreso como en el entrenamiento (discrepancia B) | 95 (6,8 %), 73 hacia más bajo | 48 (3,4 %), 35 hacia más bajo |

Ensanchado del cuantil 0,10: mediana 2,2 % / 2,2 %, p90 7,4 % / 7,3 %, máximo
31,8 % / 33,0 %.

## 5. Conclusión para la memoria

Confirmado en las dos evaluaciones, la segunda con ventanas que nunca se
habían ejecutado: el controlador propio no se distingue estadísticamente del
MPC robusto en calidad media y supera con significación a BBA, BOLA y al
controlador basado en tasa. No se confirman la QoE media más alta ni la
reducción de sesiones con paradas largas frente al MPC robusto. Se declaran la
única decisión delegada (sin efecto en las acciones) y la VM más lenta en la
segunda evaluación, desfavorable al controlador propio.

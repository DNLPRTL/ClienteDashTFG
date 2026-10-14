# Validación del simulador en tiempo virtual (14/10/2026, noche)

Es desarrollo y no va a la memoria. Como mucho entra una frase metodológica.

- **Qué es:** `simulador.py` reproduce sin esperas una sesión del cliente
  (`reproductor.py` con el motor simulado y la emulación por traza). Usa las
  clases reales del código entregado.
- **Cómo se valida:** `validar_simulador.py` compara contra paquetes reales de
  la VM cliente: `20260810_133520`, `20261013_233745` y `20261014_161901` (el
  detenido), todos en `TFG\legacy\evidencia_desarrollo`.

## Calibración (de los paquetes reales, no de los resultados)

| Constante | Valor | Medida en los paquetes |
|---|---|---|
| Exceso de cada descarga sobre el tiempo de la traza (petición HTTP + sueño) | 6 ms | mediana 4,7–7,2 ms |
| Duración real de `sleep(1)` tras el init y tras el calentamiento | 1,007 s | mediana 1,0072 s |
| Exceso por paso de 0,01 s en la espera con buffer lleno | 0,02 ms | mediana 0,01–0,03 ms |
| Paradas en las que el último segmento se consume entero en el tic | 21 % | 49/223 y 30/143 |

El último dato sale del tic de ~10 ms del motor real (`core/motores/simulado.py`).
Según su fase, la parada empieza con un resto de (0; 0,01] s o con el segmento
consumido entero. Eso decide dos cosas:

- a qué fila asigna la parada el reproductor actual;
- si el buffer tras la siguiente descarga es 4,0x s o exactamente 4,0 s, que
  es el umbral de respaldo de BOLA.

El simulador lo sortea con esa probabilidad y una semilla por sesión.

## Resultados

Sesiones reales; las sintéticas no entran. ΔQoE = simulador − VM, en QoE
lineal media por sesión.

| Modo | Sesiones | Mediana \|ΔQoE\| | p90 \|ΔQoE\| | Sesgo medio | Trayectoria idéntica |
|---|---|---|---|---|---|
| Forzado (mismos niveles que la VM): valida red, buffer y paradas | 415 clásicos + 103 propio | 0,000 | 0,007 | −0,003 | — |
| Cerrado (decide el controlador real), clásicos | 415 | 0,000 | 0,043 | −0,012 | 347 (84 %) |
| Cerrado, propio final (paquete detenido) | 7 | 0,000 | — | +0,000 | 6 de 7 |

**Por controlador, en lazo cerrado:**

| Controlador | Sesgo | Trayectoria idéntica |
|---|---|---|
| Basado en tasa | −0,002 | 99/104 |
| BBA | −0,003 | 85/104 |
| BOLA | −0,041 | 74/104 |
| MPC robusto | −0,004 | 89/103 |

En la propia VM, ejecutar dos veces la misma sesión sintética repetía la
trayectoria en 7–11 de 12 casos según el controlador (`RESULTADO_REPLICA.md`).
El simulador se parece a la VM tanto como la VM a sí misma.

**Diferencias pareadas por escenario, en lazo cerrado:**

| Par | n | Media en la VM | Media en el simulador | r |
|---|---|---|---|---|
| MPC robusto − BBA | 103 | +0,210 | +0,210 | 0,973 |
| MPC robusto − basado en tasa | 103 | +0,152 | +0,150 | 0,992 |
| Basado en tasa − BBA | 104 | +0,057 | +0,058 | 0,996 |
| MPC robusto − BOLA | 103 | +0,940 | +0,978 | 0,975 |
| BOLA − BBA | 104 | −0,730 | −0,768 | 0,972 |
| Propio − MPC robusto (solo paquete detenido) | 7 | +0,077 | +0,053 | 0,84 |

Criterio fijado en el plan: mediana de \|ΔQoE\| ≤ 0,05, r ≥ 0,9 y media de las
diferencias a ≤ 0,03.
- **Se cumple en todo**, salvo en los pares con BOLA, que quedan a 0,04.
- **Propio − MPC robusto:** el par con el código final solo tiene 7
  escenarios. Se completa en el semáforo 2, con las sesiones cortas en la VM
  sobre validación.

## Desviaciones explicadas

1. **Paradas que la VM no cuenta.** El reproductor anula la fila del último
   segmento para no contar el vaciado final. Cuando la parada que se espera
   ese segmento cae en esa fila (~21 % de las veces), también se pierde.
   - En el paquete de octubre hubo tres casos (BBA y BOLA, hasta 9,48 s).
   - En el detenido, otros tres.
   - Al revés, la parada antes del segundo segmento a veces cuenta y a veces
     no.

   Con el modo forzado, la diferencia de esas sesiones es exactamente la
   parada perdida. Por ejemplo, BOLA: VM 8,02 s = simulador 17,46 − 9,48. Se
   corrige en el reproductor (cambio C2): cada parada se asigna al segmento que
   se esperaba, y el vaciado final se excluye por estado y no por fila.
2. **Ventanas con cortes (throughput 0).** Por ejemplo, la HSDPA de Noruega
   del paquete de agosto empieza con 71 s a 0 kbit/s. Un desfase de 0,06 s
   hace que una descarga caiga a un lado u otro del corte (1,3 s frente a
   8 s): es sensibilidad caótica. El filtro de Pensieve (mínimo > 0,2 Mbit/s)
   excluye estas ventanas del experimento final.
3. **El propio antiguo** (paquetes de agosto y octubre) tardaba 174–315 ms por
   decisión. Con la latencia registrada de cada decisión, el modo forzado
   queda en sesgo +0,006.

## Uso

```bash
cd docs/blindaje/simulador
python validar_simulador.py <paquete> [<paquete> ...] --modo ambos --procesos 12 --salida informe.json
```

Variable `TFG_CODIGO`: ruta del código entregado. Por defecto,
`TFG Material\01_codigo\ClienteDashTFG`.

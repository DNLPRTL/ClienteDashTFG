# Semáforo 1: prueba previa en el simulador sobre validación (14/10/2026, noche)

Es desarrollo y no va a la memoria. Como mucho entra una frase metodológica:
"las decisiones de diseño se tomaron sobre la partición de validación".

## Banco

- **Ventanas:** las 100 ventanas relevantes de la partición de validación
  (catálogo `test`), con el filtro de Pensieve calculado sobre la ventana de
  160 s y bucle de seguridad de 1. Son Oboe 61, FCC 37, NYU 1 y UCC 1.
  Ninguna se usa en eval.
- **Vídeos:** los 4 vistos. Tears of Steel aún no está codificado.
- **Controladores:**
  - el código final, con el MPC robusto canónico;
  - las tres variantes de ablación;
  - la regla de paradas corregida (C2).
- **Tamaño:** 3200 sesiones, que el simulador corre en 15 s. Su validación
  contra la VM está en `simulador/VALIDACION_SIMULADOR.md`.

## Resultados

| Controlador | QoE | Bitrate (kbit/s) | Rebuffering (s/sesión) | Paradas/sesión | Sesiones > 5 s |
|---|---|---|---|---|---|
| MPC robusto canónico | 2,390 | 2630 | 0,16 | 0,15 | 1,2 % |
| **Propio** | 2,388 | 2578 | **0,05** | **0,03** | **0,2 %** |
| Propio sin red, cuantiles de las 5 últimas descargas | 2,374 | 2679 | 0,56 | 0,58 | 2,5 % |
| Propio solo con la mediana (sin CVaR) | 2,328 | 2716 | 0,95 | 0,95 | 6,8 % |
| Propio sin red, cuantiles fijos | 2,234 | 2368 | 0,04 | 0,03 | 0,2 % |
| BBA | 2,074 | 2498 | 0,07 | 0,06 | 0,2 % |
| Basado en tasa | 1,661 | 1802 | 0,00 | 0,00 | 0,0 % |
| BOLA | 1,505 | 1886 | 1,41 | 0,80 | 5,8 % |

**Diferencias pareadas propio − otro.** Escenario = ventana × vídeo
(n = 400). IC por bootstrap de ventanas.

| Frente a | ΔQoE [IC95] | ΔRebuffering s [IC95] |
|---|---|---|
| MPC robusto canónico | −0,002 [−0,023; +0,021] | −0,10 [−0,22; −0,02] |
| Sin red, recientes | +0,014 [−0,024; +0,057] | −0,51 [−0,73; −0,31] |
| Solo mediana | +0,060 [+0,013; +0,114] | −0,89 [−1,26; −0,57] |
| Sin red, fijos | +0,154 [+0,114; +0,195] | +0,01 [−0,04; +0,08] |
| BBA | +0,314 [+0,275; +0,356] | −0,01 [−0,09; +0,06] |

- **Lectura:** el propio domina a los dos estimadores sin red. Tiene la QoE
  de los cuantiles recientes con la seguridad de los fijos.
- **Sin red, el cuantil elegido para el experimento final** (regla D2: el más
  fuerte en QoE de validación) es el de las **últimas descargas**.

**Calidad del predictor en el dataset de validación** (107 909 muestras con
historial):

| Predictor | Pinball medio | Cobertura del cuantil 0,10 por horizonte |
|---|---|---|
| Red, como decide | 0,1468 | 3,3–9,0 % |
| Red sin ensanchado | 0,1465 | 3,5–9,3 % |
| Cuantiles fijos | 0,1630 | 6,0–8,2 % |
| Cuantiles recientes | 0,1600 | 30,5–40,0 % |

R¹ de Koenker y Machado frente a los fijos: 0,09–0,13; frente a los recientes:
0,06–0,09.

## Ajuste D7 (mitad A elige, mitad B confirma; partición por grupo de captura)

| Opción | Mitad A | Mitad B | ¿Se adopta? (≥ +0,03 en B sin más rebuffering) |
|---|---|---|---|
| α = 1 (propio) | 2,565 frente a 2,556 | 2,234 frente a 2,227 | No (+0,007) |
| α = 1 (cuantiles fijos) | 2,381 frente a 2,366 | 2,112 frente a 2,107 | No |
| α (cuantiles recientes) | mejor: 0,75, la actual | — | No hay cambio |
| Recalibración conformal + α = 1 | 2,597 | 2,249 (rebuffering 0,18 frente a 0,01) | No |
| Recalibración conformal + α = 0,75 | 2,585 | 2,250 (rebuffering 0,09 frente a 0,01) | No |

La frontera en α es plana, como en junio. La recalibración lleva las
coberturas a ±4 puntos del nominal y la pinball apenas cambia (0,1532 →
0,1528). En lazo cerrado sube la QoE en +0,02, a costa de más paradas. El
controlador queda como está: α = 0,75, con ensanchado y sin recalibrar.

## Criterios fijados en el plan

| Condición | Resultado | |
|---|---|---|
| (a) Propio − MPC ≥ −0,05 y cota inferior del IC90 > −0,15 | −0,002; IC90 [−0,019; +0,018] | ✔ |
| (b) Rebuffering medio del propio ≤ MPC | 0,05 frente a 0,16 s | ✔ |
| (c) Propio − sin red > 0 en QoE con IC95 que excluye 0 | +0,014 [−0,024; +0,057] | ✘ (sigue tras D7) |
| (d) Potencia del TOST ≥ 80 % con el N previsto | ~100 % (sd por ventana 0,11) | ✔ |

**Ámbar persistente.**
- No llega al rojo del plan ("propio ≤ sin red tras el ajuste"): la
  estimación es positiva, pero no significativa.
- La aportación de la red sale en seguridad, no en QoE media: a igual QoE,
  10 veces menos rebuffering que los cuantiles recientes.

## Potencia del diseño final (74 ventanas × 2 vídeos)

Remuestreando los resultados de validación.

| Comparación | Métrica | Diferencia esperada | P(significativa) |
|---|---|---|---|
| Propio − MPC | QoE | −0,002 | 0,07 (equivalencia: ~1) |
| Propio − MPC | paradas/sesión | −0,12 | 0,95 |
| Propio − MPC | rebuffering s | −0,10 | 0,31 |
| Propio − recientes | QoE / paradas / rebuffering | +0,013 / −0,55 / −0,50 | 0,07 / 1,00 / 1,00 |
| Propio − mediana | QoE / paradas / rebuffering | +0,06 / −0,93 / −0,90 | 0,46 / 1,00 / 1,00 |

## Pendiente de decisión de Daniel

Recomendación: **adelante con el experimento final.**
1. **Prerregistrar las métricas.** En el protocolo, antes de ejecutar, las
   **paradas por sesión** y el **rebuffering** pasan a ser medidas
   co-principales de seguridad para H1 y H3, con Holm. La QoE sigue siendo la
   principal, con TOST.
2. **Añadir cuantiles fijos como octavo controlador**, para mostrar que la red
   domina a los dos estimadores sin red. Cuesta unas 3 h más de VM en paralelo.

Antes falta confirmar en la VM (semáforo 2) que el simulador acierta también
con el MPC canónico y las variantes.

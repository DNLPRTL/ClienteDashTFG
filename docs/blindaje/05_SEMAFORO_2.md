# Semáforo 2: prueba corta en la VM (15/10/2026)

Es **desarrollo**: no va a la memoria como resultado. Sirve para decidir si se
lanza el experimento final.

## Qué se ejecutó

| Dato | Valor |
|---|---|
| Paquete | `TFG\legacy\evidencia_desarrollo\20261014_202407_previa_vm` |
| Código | `TFG\legacy\codigo_previa_vm_20261014\ClienteDashTFG` (huellas = kit con el que la VM pasó `comprobar`) |
| Preset | `previa_vm`: 10 ventanas de **validación** (FCC 5, Oboe 4, NYU 1) × 2 vídeos (uno visto en rotación + Tears of Steel) × 8 controladores = 160 sesiones, en serie |
| Duración | 18:24 → 23:51 UTC, 5,5 h; **123,5 s por sesión** (mediana 122,4) |

No gasta ninguna ventana del experimento final, que sale de `eval`.

## Criterios (fijados en el plan, § 4, antes de mirar)

| Criterio | Resultado | ¿Cumple? |
|---|---|---|
| Todas las sesiones completas (el plan decía 84/84; con el diseño actual son 160) | 160/160, 0 fallidas | Sí |
| 0 respaldos | 0 en las 160 | Sí |
| Latencia de decisión p99 < 20 ms | Clásicos ≤ 0,1 ms y MPC 2,8 ms. **Propio y variantes: 66–72 ms**, por la carga del modelo en la primera decisión (53–98 ms); sin ella, p99 = 2,1–3,5 ms | **No** (corregible) |
| VM ≈ simulador: mediana de \|ΔQoE\| por sesión ≤ 0,05 | 0,000 en modo forzado y en bucle cerrado | Sí |
| VM ≈ simulador: diferencias propio − MPC con r ≥ 0,9 | **r = 0,894** (n = 20 escenarios) | **No**, por 0,006 |
| VM ≈ simulador: media de esas diferencias a ≤ 0,03 de la VM | VM −0,060; simulador −0,049 (a 0,010) | Sí |
| Paralelo ≈ serie | No aplica: el final va en serie (decidido el 15/10) | — |
| Vídeo nuevo correcto | 80/80 sesiones con Tears of Steel; modo forzado: 80/80 trayectorias idénticas, \|ΔQoE\| máx. 0,036 | Sí |

## VM frente al simulador

Validación con `simulador/validar_simulador.py --regla esperado` (reproductor
corregido en C2).

- **Modo forzado** (el simulador sigue los niveles que eligió la VM; valida
  red, buffer, paradas y QoE):
  - 160/160 trayectorias idénticas;
  - \|ΔQoE\| máximo 0,036 y sesgo medio −0,0007;
  - por controlador, QoE media a ≤ 0,004 y rebuffering a ≤ 0,02 s;
  - mismas sesiones con parada, salvo una de los cuantiles recientes (9 frente
    a 10).
- **Bucle cerrado** (decide el controlador real):
  - 123/160 trayectorias idénticas;
  - QoE media por controlador a ≤ 0,03, salvo BOLA (+0,09) y BBA (+0,03). Las
    dos diferencias salen de una sola ventana extrema (`real_007`, BOLA con 54 s
    de rebuffering).

Diferencias pareadas por escenario, en bucle cerrado:

| Propio − … | Media VM | Media simulador | r |
|---|---|---|---|
| MPC robusto | −0,060 | −0,049 | 0,894 |
| Solo la mediana | +0,030 | +0,006 | 0,973 |
| Cuantiles fijos | +0,051 | +0,056 | 0,980 |
| Cuantiles recientes | −0,023 | −0,003 | 0,989 |
| (BOLA − BBA) | −0,939 | −0,873 | 0,999 |

### Por qué r = 0,894

1. La física del simulador es exacta: en modo forzado coincide en todo.
2. La diferencia en bucle cerrado viene de 6 sesiones del propio o del MPC con
   decisiones que se separan por milisegundos (\|ΔQoE\| ≤ 0,16, sin
   rebuffering).
3. Las diferencias propio − MPC tienen poca dispersión, y con 20 pares la
   correlación es muy sensible: su IC95 aproximado va de 0,75 a 0,96.
4. Con 8 semillas distintas, el simulador da trayectorias idénticas para estos
   controladores. No sirve, por tanto, para estimar el ruido de repetición de la
   VM.

## Corrección (C8 en `03_CAMBIOS_CODIGO_BLINDAJE.md`)

- El modelo se carga al crear el controlador, antes de arrancar el reproductor.
- Primera decisión en Windows: 1,8–3,4 ms (antes, 17 ms).
- Regresión: 4000 sesiones de validación idénticas con el simulador.
- En la VM, el humo del experimento final lo comprueba automáticamente: p99 de
  las decisiones < 20 ms y primera decisión del propio < 20 ms.

## Veredicto: ámbar → adelante

Por la letra del plan es **ámbar**: un fallo técnico corregible (la latencia) y
r a 0,006 del umbral. La acción del plan es "corregir y repetir la parte
afectada".

- **Latencia:** corregida en C8. La parte afectada, la primera decisión, se
  repite en el humo del final, con criterio automático.
- **r:** no hay nada que corregir. La memoria solo usa datos de la VM. El
  simulador sirvió para dimensionar el experimento, y su estimación de la
  diferencia media se confirma en la VM (−0,049 frente a −0,060).

No es rojo. El plan reserva el rojo para "VM distinta del simulador", y aquí
coinciden la física (forzado), las medias y las paradas.

**Decisión:** fijar el protocolo y lanzar el experimento final si el humo sale
correcto.

## Resultados de la prueba corta (desarrollo, 10 ventanas: no citar)

| Controlador | QoE media | Rebuffering (s/sesión) | Sesiones con parada |
|---|---|---|---|
| MPC robusto | 2,054 | 0,22 | 2/20 |
| Cuantiles recientes | 2,018 | 0,75 | 9/20 |
| **Propio** | 1,995 | 0,26 | 2/20 |
| Solo la mediana | 1,964 | 1,26 | 11/20 |
| Cuantiles fijos | 1,943 | 0,49 | 2/20 |
| BBA | 1,776 | 0,27 | 2/20 |
| Basado en tasa | 1,443 | 0,00 | 0/20 |
| BOLA | 0,837 | 4,86 | 2/20 |

El análisis completo de la VM (`02_resultados/contrastes_prerregistrados.md`)
funciona de punta a punta. Con solo 10 ventanas:
- se aceptan P1 (equivalencia con el MPC), P3 y P5;
- no se aceptan P2 (las mismas paradas que el MPC) ni P4 (falta potencia).

**Expectativa honesta para el final:**
- P1 y P3–P5 tienen buena potencia.
- P2 depende de que el MPC pare más que el propio en las ventanas de eval. En
  el simulador, sobre 100 ventanas de validación, paraba 5 veces más; en estas
  10, igual.
- No se cambia nada del controlador por esta prueba, para no ajustar a la
  validación.

## Duración prevista del final

1208 sesiones × 123,5 s ≈ **41,5 h**, con algo de margen por las ventanas
difíciles: unas 42–44 h.

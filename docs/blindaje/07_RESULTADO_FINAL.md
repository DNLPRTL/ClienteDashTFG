# Resultado del experimento final (F7, 16/10/2026)

Es el **único experimento que va a la memoria**. Todas las cifras de este
documento salen del paquete
`TFG Material\04_evidencia_final\20261015_031741_final_blindaje` y se pueden
citar. El protocolo, fijado antes de ejecutar, está en `06_PROTOCOLO_FINAL.md`.

## 1. Integridad y verificación

| Comprobación | Resultado |
|---|---|
| Ejecución | 1208/1208 sesiones completadas, 0 fallidas, una sola ejecución por sesión (sin reanudaciones). Del 15/10 01:17 al 16/10 18:34 UTC: **41,3 h**, sin huecos de más de 5 min |
| Compuertas (`verificar_paquete`) | Veredicto OK: las 15 comprobaciones superadas, sintéticas aparte |
| Fidelidad al protocolo | Las 77 ventanas = `ventanas_esperadas_final.txt`; un solo conjunto de parámetros por controlador, el del protocolo (α = 0,75, respaldo MPC robusto, bundle y cuantiles fijos de `~/TFG/modelos`); hipótesis `hipotesis_blindaje_v1` copiadas al protocolo antes de ejecutar |
| Respaldos | 0 en las 604 sesiones de las variantes del propio (17 516 decisiones) |
| Latencia de decisión | p99 global 4,4 ms. Por controlador: p99 ≤ 5,9 ms; propio p50 2,9 ms. Primera decisión del propio: mediana 5,6 ms (en la prueba corta, 63 ms, antes de C8). Solo 4 de 35 032 decisiones pasan de 20 ms, todas primeras decisiones (máx. 23,4 ms). Inferencia máx. 5,6 ms (límite 50) |
| Entorno | El mismo en las 1208 sesiones: Python 3.8.10, Linux 5.15 (VM cliente) |
| **Auditoría de decisiones** (`simulador/auditar_decisiones.py`) | Se da al código congelado, en Windows, la realimentación que registró la VM, y se repite cada decisión: **35 032/35 032 idénticas** (tasa y nivel), 0 respaldos. Contraprueba: con α = 0,5 cambian 96 decisiones del propio, y con el MPC no robusto, 876 |
| **Física** (`simulador/validar_simulador.py`, modo forzado) | El simulador reproduce las 1184 sesiones reales con los niveles de la VM: mediana \|ΔQoE\| = 0, p90 0,006, sesgo +0,003. 22 sesiones (1,9 %) pasan de 0,05, casi todas con algo más de rebuffering en la VM (desfases de temporización del sistema) |
| **Análisis reproducido en Windows** | `contrastes_prerregistrados.json` idéntico (diferencias ≤ 1e-9). Resto, solo rutas y redondeo ≤ 1e-14, porque Python 3.12 suma en coma flotante con compensación y 3.8 no |
| Huellas del paquete | 9699 ficheros en `04_evidencia_final\verificacion_windows_20261016\huellas_paquete.sha256`; huella de la lista `e5dc724b…3126` |

Nota sobre `02_resultados/estadistica.json`: es el módulo descriptivo heredado.
Su prueba del signo es por escenario y cuenta como empate solo la igualdad
exacta, así que cuatro de sus p cambian entre la VM y Windows por ese redondeo.
**No se usa para inferencia**: la inferencia es la prerregistrada, idéntica en
las dos máquinas.

## 2. Hipótesis prerregistradas (74 ventanas reales, 148 escenarios)

Diferencia = propio − rival. Ventanas +/−/= según la diferencia media de cada
ventana. Holm sobre P1–P5, α = 0,05.

| Id | Hipótesis | Media | IC95 | IC90 | Ventanas +/−/= | p | p Holm | Se acepta |
|---|---|---|---|---|---|---|---|---|
| P1 | QoE equivalente al MPC robusto (±0,15) | −0,001 | [−0,022; +0,021] | **[−0,018; +0,017]** | 31/39/4 | < 1e-10 | < 1e-10 | **Sí** |
| P2 | Menos paradas que el MPC robusto | −0,122 | [−0,196; −0,054] | [−0,189; −0,061] | 1/12/61 | 0,0017 | 0,0017 | **Sí** |
| P3 | Menos paradas que los cuantiles recientes | −0,439 | [−0,595; −0,297] | | 1/35/38 | 5,4e-10 | 1,6e-9 | **Sí** |
| P4 | Más QoE que los cuantiles fijos | +0,149 | [+0,107; +0,190] | | 59/15/0 | 1,3e-7 | 2,6e-7 | **Sí** |
| P5 | Menos paradas que solo la mediana | −0,791 | [−1,027; −0,581] | | 1/43/30 | 2,6e-12 | 1,0e-11 | **Sí** |

**Las cinco se aceptan.**

En P1, el IC90 cabe holgadamente en ±0,15: sería equivalente incluso con un
margen de ±0,02, unos 0,13 s de rebuffering por sesión.

En P2, en 61 de las 74 ventanas empatan (casi siempre a 0 paradas los dos). De
las 13 en que difieren, el propio para menos en 12.

## 3. Tabla descriptiva (148 sesiones reales por controlador)

| Controlador | QoE lineal | QoE log | Bitrate (kbit/s) | Rebuffering (s/sesión) | Paradas/sesión | Sesiones con parada | Cambios |
|---|---|---|---|---|---|---|---|
| Cuantiles recientes (sin red) | 2,583 | 1,873 | 2846 | 0,36 | 0,480 | 33,1 % | 4,76 |
| Solo la mediana (sin CVaR) | 2,571 | 1,866 | 2891 | 0,56 | 0,831 | 46,6 % | 5,45 |
| MPC robusto | 2,548 | 1,850 | 2786 | 0,11 | 0,162 | 14,9 % | 4,99 |
| **Propio** | **2,547** | 1,849 | 2727 | **0,03** | **0,041** | **4,1 %** | 4,41 |
| Cuantiles fijos (sin red) | 2,398 | 1,804 | 2533 | 0,03 | 0,027 | 2,7 % | 3,72 |
| BBA | 2,232 | 1,694 | 2664 | 0,20 | 0,182 | 6,1 % | 11,17 |
| Basado en tasa | 1,751 | 1,515 | 1895 | 0,01 | 0,020 | 2,0 % | 5,68 |
| BOLA | 1,194 | 1,179 | 1981 | 4,05 | 1,216 | 6,1 % | 6,55 |

Lectura:
- El propio **no tiene la QoE media más alta**. Las dos variantes más
  arriesgadas la superan por 0,02–0,04, porque la QoE lineal castiga poco una
  parada repartida en 29 segmentos.
- Lo que muestra es que **iguala al MPC canónico con 4 veces menos paradas**
  (0,041 frente a 0,162; 4,1 % frente a 14,9 % de sesiones con parada).
- Es, de los controladores con QoE alta, el que menos para.

### De dónde sale la QoE (propio − rival, por segmento)

| Rival | ΔQoE | Bitrate | Rebuffering | Suavidad |
|---|---|---|---|---|
| MPC robusto | −0,001 | −0,059 | +0,012 | +0,046 |
| Cuantiles recientes | −0,036 | −0,119 | +0,048 | +0,035 |
| Solo la mediana | −0,024 | −0,164 | +0,078 | +0,062 |
| Cuantiles fijos | +0,149 | +0,194 | +0,000 | −0,046 |
| BBA | +0,315 | +0,064 | +0,025 | +0,226 |

- **Frente al MPC**, el propio cede 59 kbit/s de bitrate (−2,1 %) y lo
  recupera con menos rebuffering y cambios más suaves.
- **Frente a los cuantiles fijos**, ganan la red y el contexto: casi 200
  kbit/s más con la misma seguridad.

## 4. Lo que aporta cada pieza

Las variantes usan el mismo planificador y cambian solo la predicción.

- **La red frente a estimadores sin red:**
  - con los **cuantiles recientes** pierde 0,036 de QoE y para 12 veces menos
    (0,041 frente a 0,480);
  - con los **cuantiles fijos** gana 0,149 de QoE con la misma seguridad
    (0,041 frente a 0,027 paradas; diferencia +0,014, IC95 [−0,027; +0,047],
    no significativa).
  - Resumen: la red da casi la QoE de la opción arriesgada con la seguridad de
    la prudente.
- **La agregación de riesgo frente a la mediana sola:** −0,024 de QoE (IC95
  [−0,071; +0,023], no significativo) y 20 veces menos paradas (0,041 frente a
  0,831).

## 5. Análisis secundario (exploratorio, sin claims confirmatorios)

**Estratos, propio − MPC robusto:**

| Estrato | Ventanas | ΔQoE (IC95) | ΔParadas (IC95) |
|---|---|---|---|
| FCC | 18 | +0,038 [+0,005; +0,076] | −0,194 [−0,361; −0,056] |
| Oboe | 56 | −0,013 [−0,038; +0,011] | −0,098 [−0,188; −0,027] |
| Vídeos vistos | 74 | +0,021 [−0,007; +0,051] | −0,176 [−0,297; −0,081] |
| Vídeo nuevo (Tears of Steel) | 74 | −0,023 [−0,046; −0,000] | −0,068 [−0,135; +0,000] |

**Interacción con el contenido.** (propio − MPC) con Tears of Steel menos
(propio − MPC) con el vídeo visto da −0,045, IC95 [−0,077; −0,014]; la prueba
del signo da p = 0,34 (40 ventanas negativas, 31 positivas, 3 empates).
- Con el contenido nuevo, la ventaja en paradas se reduce y la QoE queda un
  poco por debajo de la del MPC.
- Es un resultado exploratorio, y se informa tal cual.
- Hipótesis de trabajo, no comprobadas: el VBR de Tears of Steel es mucho mayor
  (CV 0,28–0,31 frente a 0,05–0,19), y sus dos primeros segmentos son casi
  negros (2 % del tamaño nominal), lo que da medidas de throughput poco fiables
  al inicio.

**Sintéticas** (3 ventanas, diagnóstico):
- el propio, 2,448 de QoE y 0 paradas;
- el MPC, 2,416 y 0,33 paradas por sesión.

Con n = 3 no se concluye nada.

**Frente a los clásicos:** el propio supera en QoE a BBA (+0,315), al basado en
tasa (+0,796) y a BOLA (+1,353). BOLA sufre en ventanas de baja capacidad
(4,05 s de rebuffering por sesión).

## 6. Qué se puede afirmar en la memoria y qué no

**Sí:**
- En 74 ventanas reales de red emulada (Oboe y FCC) y con dos contenidos (uno
  visto y uno nuevo), el controlador propio da una QoE lineal **equivalente** a
  la del MPC robusto canónico. El margen prerregistrado era ±0,15 y el IC90
  observado cabe en ±0,02.
- Con **menos paradas y menos rebuffering** que el MPC canónico.
- La red aporta frente a estimadores sin red con el mismo planificador (P3 y
  P4), y la agregación de riesgo aporta frente a la mediana (P5).
- Todo con contrastes prerregistrados y corrección de Holm.

**No:**
- Que el propio tenga la mejor QoE: no la tiene, y no se planteó así.
- Que mejore la QoE del MPC.
- Que generalice a redes reales con TCP y tráfico competidor (D5), a otros
  tipos de contenido más allá de los tres usados (dos vistos y uno nuevo), o a
  métricas perceptuales (VMAF).
- Nada sobre Tears of Steel por separado más allá de lo exploratorio del § 5.

## 7. Desviaciones del protocolo

Ninguna:
- sin sesiones repetidas ni descartadas;
- sin cambios de código ni de parámetros durante la ejecución;
- el análisis es el prerregistrado, reproducido en dos máquinas.

## 8. Notas para la redacción

- **Definición exacta de la agregación de riesgo**
  (`planificador._cvar`): para cada secuencia candidata se promedian las
  puntuaciones de los ⌈α·K⌉ peores de los K = 4 escenarios de cuantil (0,1,
  0,25, 0,5 y 0,75).
  - Con α = 0,75 son los 3 peores. Como la puntuación crece con el throughput,
    en la práctica son los escenarios de q0,1, q0,25 y q0,5.
  - α solo cambia la decisión en saltos de 0,25: 0,70 y 0,75 deciden igual.
  - Hay que describirlo así, como CVaR discreto sobre escenarios de cuantil (no
    son muestras equiprobables), sin atribuirle más de lo que es.
- **El texto automático `04_informe/conclusiones_tecnicas.md`** del paquete
  conserva el nombre antiguo `qoe_linear_mean`. No se cita; las cifras salen de
  `02_resultados`.
- **Referencias nuevas** para los métodos estadísticos: TOST (Schuirmann,
  1987), Holm (1979) y bootstrap (Efron y Tibshirani, 1993), más la ficha de
  Tears of Steel (Blender Foundation, CC-BY 3.0). Requieren permiso para
  descargar los PDF.

# Protocolo del experimento final (fase de blindaje)

Fijado y commiteado el 15/10/2026, **antes de ejecutar ninguna sesión**.

- Es el único experimento que va a la memoria. Todo lo anterior es desarrollo:
  prueba corta, semáforos y paquetes de agosto y octubre.
- Se ejecuta tal como está escrito. Cualquier desviación se documenta en la
  memoria con su motivo.

## 1. Pregunta

¿El controlador propio (predictor neuronal de cuantiles + planificador MPC con
CVaR) iguala en QoE al MPC robusto canónico y lo mejora en seguridad (menos
paradas)? ¿Qué aporta la red frente a estimadores sin red con el mismo
planificador?

## 2. Lo que se congela

| Pieza | Huella SHA-256 |
|---|---|
| Código entregado (103 ficheros) | lista en `kit_vm/hashes_codigo.sha256`; huella de la lista: `a65e77e3…22448` |
| `config/evaluacion.local.json` | `700da716…19b3` |
| Modelo (bundle, 5 ficheros) | `kit_vm/hashes_bundle.sha256`; `pesos_modelo.pt` = `54d686f8…abbaad9`; `manifiesto.json` = `7341c89c…c31d` |
| Cuantiles fijos | `a3a5ceb2…dc89` |
| Catálogo de trazas | `1ac4675d…ed4d` |
| Descriptor de Tears of Steel | `81e76dc7…aa49c` |
| Ventanas esperadas (77) | `kit_vm/ventanas_esperadas_final.txt`, `a3445cc6…a727` |

La VM comprueba todo esto antes de empezar (`blindaje_vm.sh comprobar`):
- huellas del código, el modelo, el catálogo y los cuantiles;
- que no sobra ningún fichero;
- que las 18 pruebas pasan en la VM;
- que el plan en seco da las 77 ventanas esperadas.

## 3. Diseño

### Red (emulación)

- **Corpus:** partición `eval` del catálogo curado. La validación no se toca.
- **Ventanas reales:** todas las relevantes de `eval`, ventanas de 160 s.
  - **Filtro de Pensieve** sobre la propia ventana: media < 6 Mbit/s y mínimo
    > 0,2 Mbit/s.
  - **Grupos excluidos:** los 42 ya usados en desarrollo (39 reales y 3
    sintéticos).
  - **Resultado: 74 ventanas** (Oboe 56, FCC 18).
  - Inicio de cada ventana determinista, con semilla 606.
- **Ventanas sintéticas:** 3, solo como diagnóstico. Se informan aparte y no
  entran en los contrastes.
- **Bucle de seguridad:** como máximo 1 vuelta (`politica_fin = loop`,
  `max_bucles = 1`). Una sesión consume como mucho unos 145 s de traza.

### Contenido

- En cada ventana real, **2 vídeos**:
  - uno visto, en rotación entre Paseo 30/60 fps y Blender 30/60 fps;
  - **Tears of Steel**, contenido nuevo para el modelo (CC-BY 3.0).
- Las sintéticas usan un vídeo visto.
- 30 segmentos de 4 s por sesión (29 decisiones), buffer máximo de 60 s y
  tamaños VBR reales.

### Controladores (8)

| Clave | Qué es |
|---|---|
| `basado_en_tasa` | Clásico |
| `bba` | Clásico |
| `bola` | Clásico |
| `mpc_robusto` | MPC robusto canónico (Yin 2015, § 7.1; código de Pensieve): horizonte 5, QoE lineal y tamaños reales |
| `controlador_propio` | Ensemble GRU de cuantiles + CVaR α = 0,75 |
| `propio_mediana` | Mismo planificador; solo la mediana de la red (sin CVaR) |
| `propio_cuantiles_recientes` | Mismo planificador; cuantiles de las 5 últimas descargas (sin red) |
| `propio_cuantiles_fijos` | Mismo planificador; cuantiles fijos del error de la media armónica en el entrenamiento (sin red) |

### Ejecución

- **1208 sesiones:** 74 × 2 × 8 reales + 3 × 1 × 8 sintéticas. Una
  repetición.
- **Orden:** los controladores se sortean en cada escenario con la semilla
  `"606|ventana|vídeo|1"`.
- **En serie:** una sesión detrás de otra, en la VM cliente (192.168.1.160)
  contra la VM servidor (192.168.1.132).
- **Duración prevista:** 42–44 h. En la prueba corta, 123,5 s por sesión.

## 4. Métricas

Por sesión, sobre los 29 segmentos evaluables:
- **Principal:** `qoe_lineal_media` = bitrate (Mbit/s) − 4,3 · rebuffering (s)
  − |Δ bitrate| (Mbit/s).
- **Co-principal de seguridad:** `num_stalls`.
- **Secundarias:** rebuffering total, bitrate medio, cambios de calidad y
  `qoe_log_media`.
- **Solo informativa:** el retardo de arranque.

## 5. Hipótesis principales (versión `hipotesis_blindaje_v1`)

Referencia: `controlador_propio`. Están definidas en
`core/evaluacion/contrastes.py` y se copian al protocolo del paquete al
planificar.

| Id | Hipótesis | Rival | Métrica | Prueba |
|---|---|---|---|---|
| P1 | QoE equivalente | MPC robusto | QoE lineal | TOST con margen ±0,15 |
| P2 | Menos paradas | MPC robusto | paradas | signo, unilateral |
| P3 | Menos paradas (aporte de la red) | cuantiles recientes | paradas | signo, unilateral |
| P4 | Más QoE (aporte de la red) | cuantiles fijos | QoE lineal | signo, unilateral |
| P5 | Menos paradas (aporte del CVaR) | solo la mediana | paradas | signo, unilateral |

- **Margen de P1:** 0,15 equivale a 1 s de rebuffering en una sesión de 29
  segmentos (4,3/29).
- **Unidad de análisis:** el escenario (ventana × vídeo). **Bloque:** la
  ventana, porque sus dos escenarios comparten red.
  - Las pruebas del signo usan la diferencia media de cada ventana.
  - Los intervalos remuestrean ventanas: bootstrap por bloques, 10 000
    remuestreos, semilla 2026.
- **TOST:** p = máximo de los dos unilaterales, con aproximación normal sobre
  las medias por ventana. Se informa además si el IC90 bootstrap queda dentro
  de ±0,15.
- **Multiplicidad:** Holm sobre P1–P5, α = 0,05.

  Cada hipótesis se acepta si su p ajustado por Holm es ≤ 0,05.
- **Empates:** las ventanas con diferencia media exactamente 0 no cuentan en la
  prueba del signo. Se informa cuántas hay.

## 6. Análisis secundario (descriptivo, sin claims confirmatorios)

- Todas las métricas frente a cada rival: media, IC95 por bootstrap de
  ventanas y prueba del signo bilateral.
- **Estratos:** Oboe y FCC; vídeo nuevo y vídeos vistos (propio frente a MPC y
  frente a los cuantiles recientes).
- **Interacción de contenido:** (propio − MPC) con Tears of Steel menos
  (propio − MPC) con el vídeo visto, por ventana.
- Las 3 ventanas sintéticas, aparte.
- Todo lo calcula `analisis.py`, que lo escribe en
  `02_resultados/contrastes_prerregistrados.{json,md}`, junto con el resumen,
  las gráficas y la verificación del paquete.

## 7. Validez y sesiones fallidas

- **Compuertas** (`verificar_paquete.py`): todas las sesiones completas;
  ninguna fallida en los segmentos; respaldos auditados; inferencia auditada en
  las variantes con red; sintéticas aparte.
- **Si la ejecución se corta** (apagón, cuelgue), se reanuda el mismo paquete
  (`blindaje_vm.sh reanudar`). Las sesiones completadas se conservan y las
  incompletas o fallidas se repiten.
- **Si una sesión no se puede completar** tras reanudar, su escenario sale de
  los pares de ese controlador. Se informa en la memoria.
- **Ninguna sesión completada se repite ni se descarta** por su resultado.

## 8. Qué se informará, salga lo que salga

- P1–P5 con media, IC95, IC90 (P1), ventanas +/−/=, p y p de Holm, también las
  que no se acepten.
- Si P2 no se acepta, se dice tal cual: la seguridad frente al MPC no queda
  demostrada.
- Las diferencias del análisis secundario se presentan como exploratorias.
- Limitaciones declaradas:
  - emulación de red sin TCP ni tráfico competidor (D5);
  - ventanas concentradas en Oboe y FCC;
  - un solo contenido nuevo;
  - el bitrate como proxy de calidad (sin VMAF).

## 9. Operación

1. Humo previo de 8 sesiones sobre validación (`blindaje_vm.sh humo`), con
   criterio automático:
   - 8/8 completadas y 0 respaldos;
   - p99 de la latencia de decisión < 20 ms;
   - primera decisión del propio < 20 ms.
2. Lanzamiento con `blindaje_vm.sh final`: `nohup`, sobrevive al cierre de la
   terminal.
3. Durante la ejecución:
   - el PC sin suspenderse y la VM sin otras cargas;
   - nada de copias desde el servidor ni WSL.
4. Al terminar, el paquete se copia a `TFG Material\04_evidencia_final\` y se
   verifica con `verificar_paquete.py`.

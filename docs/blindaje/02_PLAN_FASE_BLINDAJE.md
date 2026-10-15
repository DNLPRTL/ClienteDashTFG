# Fase de blindaje: plan de pasos (propuesta del 14/10/2026, noche)

Propuesta de Claude tras leer `00_HANDOFF_FASE_BLINDAJE.md` y comprobarlo
contra el código de `TFG Material\01_codigo\ClienteDashTFG` y los datos.

> **Estado (15/10/2026):**
> - Hechos F0–F5 y F8 (el pulido se adelantó: el código se congela antes del
>   final).
> - Semáforo 1 en ámbar → adelante (`04_SEMAFORO_1.md`). Semáforo 2 en ámbar
>   → adelante (`05_SEMAFORO_2.md`): la latencia se corrigió en C8 y r = 0,894
>   no afecta al final.
> - Protocolo del final fijado en `06_PROTOCOLO_FINAL.md`.
> - Siguiente: F6, el experimento final en la VM con el kit
>   (`kit_vm/LEEME.md`), por script con `nohup` en lugar de la interfaz,
>   porque sobrevive al cierre de la ventana.

**Daniel confirmó D1–D8 tal como se recomiendan el 14/10 por la noche,**
incluido el permiso para descargar `tears_of_steel_1080p.mov.zip` en la VM
servidor. Falta el tope de horas de VM para el experimento final, que da él
aparte. Nada de este documento va a la memoria. El registro de cambios del
código está en `03_CAMBIOS_CODIGO_BLINDAJE.md`.

---

## 1. Lo comprobado hoy

| Hecho | Resultado | Fuente |
|---|---|---|
| MPC robusto del cliente | H = 3, q = ln(R/Rmin), tamaños nominales (como dice el traspaso) | `core/controladores/mpc.py:10,346-352` |
| Error del MPC robusto | Se mide contra la predicción **ya rebajada**; al arrancar aplica ×0,85 | `robust_mpc.py:223-248,304-305` |
| Historial del MPC | No incluye la descarga de calentamiento (el propio sí) | `mpc.py:94,173-192`; `reproductor.py:639-643` |
| RobustMPC canónico (Yin 2015 §7.1, PDF p. 9-10) | Ĉ/(1+err), Ĉ = media armónica de 5, err = error porcentual absoluto máximo de los 5 últimos; FastMPC con h = 5 | `biblioteca_final/04_abr_clasicos/yin2015mpc.pdf` |
| Pensieve, artículo (PDF p. 3) | robustMPC con horizonte de 5 chunks y error máximo de 5 | `mao2017pensieve.pdf` |
| Pensieve, código `test/mpc.py` | Error contra la **media armónica** (`past_bandwidth_ests.append(harmonic_bandwidth)`), error inicial 0, horizonte truncado al final, tamaños reales, recompensa lineal en Mbit/s | github.com/hongzimao/pensieve |
| Filtro de trazas | Pensieve p. 7: media < 6 Mbit/s y mínimo > 0,2 Mbit/s, "para evitar selección trivial"; Yin p. 9: FCC con media entre 0 y 3 Mbit/s, misma razón | PDFs |
| Las 12 ventanas del experimento detenido | Coinciden con `ventanas_esperadas_final.txt` (recalculadas con `seleccion.py`) | catálogo + config |
| Ventanas relevantes (160 s, sin los 39 grupos usados) | Filtro de Pensieve **sobre la propia ventana**: **74 en eval** (Oboe 56, FCC 18; 74 grupos distintos), **100 en validación**. Sobre la traza entera: 65 / 84 | 6992 trazas normalizadas |
| Potencia (paquetes de desarrollo) | 24/48 empates; sd de las diferencias 0,528 / 0,304; N80(Δ = 0,10) = 220 / 73 | `legacy/evidencia_desarrollo` |
| Tiempo real por sesión | 122 s en ventanas fáciles; 130–145 s de media en baja capacidad (p90 hasta 197 s). Se presupuesta 2,4 min | manifiestos de ejecución |
| Entradas del predictor | La red predice log(throughput futuro / media armónica) por horizonte y cuantil; el contenido no entra | `bundle.py:182-215`, dataset |
| Contenido evaluado | Las sesiones reproducen siempre los 30 primeros segmentos; el entrenamiento usó esos mismos 30 de los mismos vídeos (desplazamiento 0) | `dataset_fiel.py:36-48`, `controlador_propio.py:282-291` |

### Hallazgos nuevos

1. **Tres fallos de traducción (NameError) en el código entregado.**
   - `scripts/1_contenido/extraer_tamanos_reales_segmentos.py:194`
     (`number`, `start_numero`, `hard_tope`): rompe la extracción de tamaños,
     que hace falta para el vídeo nuevo.
   - `entrenamiento/dataset_cuantiles.py:222` (`limpio_quantiles`) y
     `entrenamiento/dataset_fiel.py:108` (`mid`): rompen la regeneración del
     dataset.
   - Más el Q_H muerto de `politicas_rollout.py:119-131`, ya conocido.
2. El MPC robusto se aparta del canónico en dos puntos más que los del
   traspaso: la referencia del error y el ×0,85 de arranque.
3. El reproductor duerme 1 s tras el init y tras el segmento de calentamiento
   (valor inicial de `ControladorBase.duracion_inactividad`). Es igual para
   todos los controladores; el simulador debe replicarlo.
4. La desventaja de latencia del propio en desarrollo (174–315 ms por
   decisión, tiempo en que no descarga) queda resuelta con el planificador
   vectorizado.
5. La atribución del rebuffering a filas está desplazada un segmento (la
   espera antes de k+1 cae en la fila k en 174 de 223 casos). La suma por
   sesión no cambia; lo excluido por la fila de calentamiento fue 0,01 s en
   600 sesiones. No se toca.
6. Los enlaces de Tears of Steel del traspaso dan 404. El fichero vigente:
   `https://download.blender.org/demo/movies/ToS/tears_of_steel_1080p.mov.zip`,
   583 774 281 bytes.

---

## 2. Decisiones para Daniel (recomendación primero)

| # | Decisión | Recomendación |
|---|---|---|
| D1 | MPC robusto | **Canónico**: H = 5; calidad lineal en Mbit/s; 4,3 y 1; tamaños reales del vídeo activo; media armónica de 5; /(1 + error máximo de 5) medido contra la media armónica; sin ×0,85; mismo historial que el propio. Implementado sobre el mismo planificador con un solo escenario. Sustituye al actual, también como respaldo del propio |
| D2 | Variantes de ablación dentro del experimento final | `propio_mediana` (aísla el CVaR) y `propio_sin_red` (aísla la red). Para el segundo, el estimador sin red más fuerte en validación entre: (a) cuantiles fijos del error de la media armónica, sacados del dataset de entrenamiento; (b) cuantiles empíricos de las 5 últimas descargas |
| D3 | Vídeo nuevo | **Tears of Steel** (imagen real con efectos; contenido de prueba habitual en DASH), CC-BY 3.0, "(CC) Blender Foundation \| mango.blender.org". Primeros 10 min, 30 fps, mismos scripts, sin audio (la banda sonora es BY-ND y no se usa). **Permiso de descarga**: `tears_of_steel_1080p.mov.zip`, 583 774 281 B (≈ 557 MiB), de download.blender.org, en la VM servidor |
| D4 | Ventanas | Todas las de eval que pasan el filtro de Pensieve sobre la ventana de 160 s, con bucle de seguridad de 1, sin los 39 grupos usados: **74, sin sorteo**. Más 3 sintéticas nuevas como diagnóstico |
| D5 | Tamaño | Diseño A (2 vídeos por ventana). N definitivo en el semáforo 1 con la potencia del simulador. Falta el tope de horas de VM |
| D6 | Dos sesiones en paralelo en la VM | Probarlo en F4; adoptarlo solo si pasa el criterio |
| D7 | Ajuste en validación | Se mide siempre: α ∈ {0,5; 0,75; 1; según buffer} × recalibración conformal sí/no. Se adopta solo si mejora ≥ 0,03 la QoE media en la mitad B de validación sin más rebuffering |
| D8 | Margen de equivalencia | δ = 0,15 de QoE media por segmento (= 1 s de rebuffering por sesión: 4,3 × 1 / 29 ≈ 0,148) |

---

## 3. Pasos

| Paso | Quién | Qué | Duración |
|---|---|---|---|
| F0 | Daniel | Responder D1–D8 y copiar el paquete detenido a Windows | 15 min |
| F1a | Claude | Copia previa a `legacy`; los tres NameError; script del vídeo nuevo | ~2 h |
| F3 | Daniel | En la VM servidor, un script: descarga, recorte, 30 fps y DASH | 1–2 h desatendido |
| F2a | Claude | Simulador en tiempo virtual que mueve las clases reales; validación contra los tres paquetes de desarrollo | ~½ día |
| F1b | Claude | MPC canónico, las dos variantes, cuantiles sin red versionados, tests; las 1740 decisiones del propio deben repetirse idénticas | ~½ día |
| F2b | Claude | Prueba previa en el simulador: 100 ventanas de validación × 5 vídeos × todos; barrido D7 → **semáforo 1** con informe | ~2 h |
| F1c | Claude | Selección, ejecución en paralelo, análisis (TOST, Holm, clúster, estratos) y kit de F4 | ~1 día |
| F4 | Daniel | En la VM cliente: 6 ventanas de validación × 2 vídeos × 7 controladores, en serie y luego en paralelo | ~5 h (noche) |
| S2 | Claude | **Semáforo 2** | 1 h |
| F5 | Claude | Protocolo final y kit commiteados antes de ejecutar | ~3 h |
| F6 | Daniel | Experimento final, por la interfaz | ~21 h en paralelo / ~42 h en serie |
| F7 | Claude | Verificación, reproducción fuera de línea, análisis según el protocolo, copia a `04_evidencia_final` | ~½ día |
| F8 | Claude | Pulido: `.idea`, Q_H, LEEME, `requirements`, convergencia | ~2 h |
| F9 | Ambos | Memoria | después |

Calendario: alrededor de una semana hasta el paquete final si no sale ámbar
ni rojo.

---

## 4. Semáforos (criterio fijado antes de mirar)

### Semáforo 1: simulador sobre validación

Precondición: simulador validado contra la VM con los paquetes de desarrollo.
Por sesión, mediana de |ΔQoE| ≤ 0,05. Diferencias pareadas propio − MPC con
r ≥ 0,9. Media de esas diferencias a ≤ 0,03 de la de la VM.

| Luz | Criterio (ventanas relevantes de validación) | Acción |
|---|---|---|
| Verde | Propio − MPC canónico: Δ ≥ −0,05 y cota inferior del IC90 > −0,15; rebuffering medio del propio ≤ el del MPC; propio − sin red > 0 con IC95 que excluye 0; potencia del TOST ≥ 80 % con el N previsto | Adelante |
| Ámbar | Falla alguna condición sin llegar a rojo | Ajuste D7 en la mitad A; confirmación en la mitad B; si queda en verde, adelante |
| Rojo | Δ < −0,15 sin ventaja en rebuffering; o propio ≤ sin red tras el ajuste; o simulador no validable | Parar y decidir con Daniel antes de gastar VM |

### Semáforo 2: ejecución corta en la VM

| Luz | Criterio | Acción |
|---|---|---|
| Verde | 84/84 sesiones; 0 respaldos; latencia de decisión p99 < 20 ms; VM ≈ simulador con el criterio de arriba; paralelo ≈ serie (media de las diferencias ≤ 0,02 y mediana de \|dif\| no mayor que el ruido de repetición); vídeo nuevo correcto | Fijar el protocolo y lanzar |
| Ámbar | Fallo técnico corregible | Corregir y repetir la parte afectada |
| Rojo | VM distinta del simulador | No lanzar; investigar |

---

## 5. Experimento final propuesto (diseño A)

- **Controladores (7):** basado en tasa, BBA, BOLA, MPC robusto canónico,
  propio, propio_mediana y propio_sin_red.
- **Ventanas:** 74 reales (todas las relevantes de eval) y 3 sintéticas
  nuevas, como diagnóstico, con un vídeo.
- **Vídeos por ventana:** uno visto (rotando entre los 4) y Tears of Steel.
- **Ejecución:** orden de controladores aleatorio con semilla dentro de cada
  escenario y una sesión de calentamiento inicial que no se analiza.
- **Análisis prerregistrado:**
  - Unidad: el escenario (ventana × vídeo); clúster: la ventana.
  - H1: propio frente a MPC (TOST con δ = 0,15 y superioridad).
  - H2: frente a la mediana (efecto del CVaR).
  - H3: frente a sin red (efecto de la red).
  - Holm sobre H1–H3.
  - H4: contenido nuevo frente a visto, por interacción pareada por ventana.
  - Secundarias: rebuffering (total, paradas, % > 5 s), bitrate, cambios,
    arranque, P5 y mínimo.
  - Estratos: Oboe/FCC y tramo de dificultad.
  - Mecanismo: decisiones que cambian sin cada componente; cobertura en lazo
    cerrado.

| Diseño | Sesiones | Serie (2,4 min) | Paralelo ×2 | TOST(0,15) / Δ superioridad detectable* |
|---|---|---|---|---|
| A: 2 vídeos por ventana | 1036 + 21 = 1057 | ~42 h | ~21 h | ≈ 82 % / ≈ 0,14 |
| B: 1 vídeo (rotan los 5) | 518 + 21 = 539 | ~22 h | ~11 h | ≈ 65 % / ≈ 0,16 |
| C: 3 vídeos por ventana | 1554 + 21 = 1575 | ~63 h | ~32 h | ≈ 87 % / ≈ 0,13 |

\* Con sd = 0,5 por escenario y correlación de 0,5 entre vídeos de la misma
ventana. Con sd = 0,4, A llega a ≈ 96 % y B a ≈ 89 %. Se recalcula en el
semáforo 1 con la sd real de validación.

---

## 6. Cambios de código y su verificación

Todos en `TFG Material`, con copia previa a `legacy` y con el diff y las
huellas SHA-256 en el repo.

| Cambio | Verificación |
|---|---|
| 1. Los tres NameError y el Q_H | `ruff` F821 a 0; humo de `generar_dataset` con 2 ventanas; volver a extraer el descriptor de Paseo y que salga idéntico al guardado |
| 2. MPC canónico | Tests contra un port literal del bucle de Pensieve; error contra la media armónica; historial con el calentamiento |
| 3. Variantes | Tests; los cuantiles sin red, en un JSON con huella |
| 4. El propio no cambia | Las 1740 decisiones de desarrollo y las del paquete detenido, idénticas |
| 5. Selección y ejecución en paralelo | Tests; lista esperada 74 + 3 en el kit |
| 6. Análisis | Tests con datos sintéticos de resultado conocido |
| 7. Vídeo nuevo | Catálogo, mapa de descriptores y comprobación de 5 MPD en el kit |
| 8. Simulador (`docs/blindaje/simulador/`, fuera del material) | Validado contra los tres paquetes |

---

## 7. Riesgos

1. El MPC canónico es mucho más fuerte, así que es probable que el propio no
   gane en QoE media. Relato si pasa: equivalencia (TOST) con menos
   rebuffering y menos colas, es decir, el compromiso riesgo-calidad, con la
   ablación mostrando de dónde sale. Si tampoco hay eso, rojo antes de gastar
   VM.
2. Lo más peligroso: que `propio_sin_red` empate con el propio. La red
   aportaría en la predicción (pinball), pero no en las decisiones. Se sabe en
   el semáforo 1.
3. Que el simulador no coincida con la VM. Se mitiga con la validación y el
   semáforo 2.
4. Pocas ventanas difíciles y concentradas: Oboe 56 y FCC 18, ninguna móvil
   con cortes (las excluye el mínimo de 0,2 Mbit/s). Validez externa
   limitada; se informa por conjunto.
5. Solo son demostrables diferencias a partir de ≈ 0,14.
6. Reutilizar la validación (α de junio, parada temprana, D7) puede
   sobreajustar. Se mitiga con la mitad B.
7. 21–42 h de VM. Se mitiga con la reanudación, el orden aleatorio, la sesión
   de calentamiento y `powercfg`.
8. Tears of Steel: el original es 1920×800 y queda con bandas negras; el paso
   de 24 a 30 fps duplica fotogramas. Se informa su VBR.
9. D5 no se toca: ni TCP ni tráfico competidor. Se declara.
10. Calendario: una semana si no sale ámbar ni rojo.

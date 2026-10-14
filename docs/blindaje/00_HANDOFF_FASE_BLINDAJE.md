# Fase de blindaje: documento de traspaso

Escrito el 14/10/2026 por la noche, al cerrar el hilo anterior. Lo lee primero
el hilo nuevo. Separa lo **verificado** (con fichero, línea o cifra) de lo
**propuesto** (a verificar y decidir con Daniel). Nada de aquí va a la memoria
tal cual.

---

## 0. Qué pide Daniel

Daniel ha **detenido** el experimento final que estaba en marcha. Quiere:

1. Aplicar todas las mejoras que eliminen o acoten las deficiencias técnicas del
   trabajo, sin rebajarlas. La emulación de red no se toca.
2. Saber **antes** de lanzar si el resultado puede ser bueno, con pruebas que
   cuesten minutos u horas, como se hacía con los presets `diagnostico` y
   `rapido` en junio.
3. Lanzar **un único experimento final**. Es lo único que irá a la memoria.
4. Rigor académico: bibliografía, papers, Google Scholar y PDFs disponibles.

La primera respuesta del hilo nuevo debe ser el **plan de pasos** (ver §9).

---

## 1. Reglas de Daniel (no negociables)

1. **Memoria = solo el experimento final.** Nada de "dos evaluaciones",
   "réplica", "estudio complementario" ni historia de desarrollo. Si el
   experimento final incluye variantes de ablación o un vídeo no visto, son
   partes de LA evaluación final: una ejecución, un paquete, un protocolo. Las
   pruebas previas (humo, simulador, comprobaciones) son desarrollo y no van a
   la memoria. Como mucho entra una frase metodológica, por ejemplo: "las
   decisiones de diseño se tomaron sobre la partición de validación".
   Ver la memoria persistente `memoria-solo-experimento-final`.
2. **Borradores.** Daniel tiene escritos en Word el capítulo 4 completo y el 5
   hasta el 5.3. Durante el blindaje no se tocan, ni se proponen cambios. Al
   acabar la parte técnica, él pasa los Word y Claude le dice qué cambia, en
   texto y en figuras. Del 5.4 en adelante, Claude rehace los borradores enteros
   con el estado final. Durante el blindaje no se hace trabajo de memoria; solo
   se apunta en §8 qué apartados quedarán afectados.
3. Lo ocurrido entre el remake del 5.6 (13/10) y el "vale adelante" (14/10
   tarde) **no existe** para la memoria.
4. **Excelencia.** Cada deficiencia se resuelve o se mide. Lo que no se pueda,
   se declara con datos.
   - **Citas:** solo claves de `docs/memoria/bibliografia.bib`, verificadas
     contra el PDF de `C:\Users\danie\Documents\TFG\literatura\biblioteca_final\`
     (los `.md` de `docs/todos los estudios pdf convertidos a md/` son solo
     índice de búsqueda).
   - **Referencias nuevas:** se proponen a Daniel. Descargarlas exige su permiso
     explícito, indicando fichero, origen y tamaño.
5. **Contrato de trabajo.**
   - Claude desarrolla y verifica en Windows. Daniel ejecuta en las VM y en WSL
     y pega las salidas.
   - Comandos cortos y scripts versionados.
   - Commits con rutas explícitas, nunca `git add .`.
   - Nunca revertir cambios de Daniel.
   - Cualquier descarga, con su permiso explícito.
6. **Respuestas** en español, densas pero entendibles. Pasos concretos.

---

## 2. Estado a 14/10 por la noche

- **Código que se entrega y que corre en la VM.**
  - Ruta: `C:\Users\danie\Documents\TFG Material\01_codigo\ClienteDashTFG`
    (80 `.py`, en castellano).
  - **No tiene git.** Cada cambio se documenta así:
    1. Copia previa en `TFG\legacy\`.
    2. Diff y huellas SHA-256 commiteados en el repo, como en
       `docs/evaluacion_final/cambios_codigo_version_final.diff`.
  - El repo `DashClientModular4` (rama `rebuild/phase3-from-phase2`) contiene
    documentos, kits y bibliografía. Su código es el antiguo en inglés: no se
    usa.
- **Versión final del controlador** (14/10, commit `5da131d`):
  - planificador vectorizado con numpy (idéntico bit a bit);
  - `torch.set_num_threads(1)` y calentamiento del modelo;
  - entradas alineadas con el entrenamiento (progreso sobre los 30 segmentos de
    la sesión, rebuffering reciente, historial con la descarga de
    calentamiento);
  - opción `experimento.grupos_fuga_excluidos`.

  El código anterior está archivado en
  `TFG\legacy\codigo_entrega_20261014_antes_version_final\`.
- **Experimento detenido.** El experimento final del 14/10 (`tfg_final`, 5
  controladores, 15 ventanas, 300 sesiones) se lanzó por la tarde y Daniel lo
  paró por la noche.
  - El paquete parcial está en la VM cliente, en
    `~/TFG/validacion_comparativa/<sello>_tfg_final`. **No se ha analizado.**
  - Hay que archivarlo como desarrollo, sin borrarlo. Sus 12 ventanas reales
    pasan a contar como **usadas**.
  - Es el único conjunto de sesiones con el código final del controlador, así
    que sirve para validar el simulador (§4.8).
- **Protocolos superados.** `docs/evaluacion_final/PROTOCOLO_EVALUACION_FINAL.md`
  y `PROTOCOLO_ESTUDIOS_COMPLEMENTARIOS.md` (commit `6c42423`) quedan
  **superados**. Sirven de base. El protocolo nuevo se fija y se commitea antes
  del experimento final nuevo.
- **Ejecuciones de desarrollo archivadas.** Están en
  `TFG\legacy\evidencia_desarrollo\`: `20260810_133520_tfg_final` y
  `20261013_233745_tfg_final`.
  - Cada una tiene 300 sesiones, con el código anterior al 14/10.
  - Sirven como datos de desarrollo: varianzas, validación del simulador.
- `TFG Material\04_evidencia_final\` está **vacía**.

---

## 3. Infraestructura y flujo

### Máquinas

| Máquina | Datos | Papel |
|---|---|---|
| Windows | i5-14600KF híbrido (6P + 8E), Python 3.12 | Desarrollo y verificación. Ejecutar con `PYTHONUTF8=1 PYTHONIOENCODING=utf-8` si algo imprime emojis (cp1252). |
| VM cliente "TFGv1" | 192.168.1.160, usuario `daniel`, VirtualBox 7.0.14, 6 vCPU, 8 GB, Python 3.8.10, torch 2.4.1, numpy 1.24.4 | Ejecuta los experimentos |
| VM servidor | 192.168.1.132 | Apache en `/var/www/html/dash`. Contenido creado con `scripts/1_contenido/generar_dash_lote.sh` (ffmpeg + Docker `jjlin/gpac`). Escalera 1080p/4300 … 144p/300 kbps. |
| WSL Ubuntu-24.04 | `~/TFG`, GPU AMD con ROCm | Solo si hay que reentrenar (no previsto) |

Windows llega al servidor DASH por HTTP.

### Cómo llega el código a la VM

Se copia con `scp` desde `TFG Material` (no con `git pull`). El kit de
comprobación vive en el repo, en `docs/evaluacion_final/`, y también se copia
por `scp`. `evaluacion_final.sh` tiene tres órdenes: `comprobar` (7
comprobaciones), `humo` (5 sesiones en `/tmp`) y `estado`. El paso a paso está
en `docs/evaluacion_final/LEEME.md`. Ese kit hay que regenerarlo para el
experimento nuevo.

### Cómo se lanza el experimento

- **Por interfaz:** `python3 scripts/3_evaluacion/gui_evaluacion.py` (preset y
  controladores).
- **Para reanudar:** `ejecutar_evaluacion.py --raiz-paquete <paquete>` omite las
  sesiones completadas.
- **Rendimiento:** antes de una ejecución larga, en PowerShell como
  administrador:
  `powercfg /powerthrottling disable /path "C:\Program Files\Oracle\VirtualBox\VirtualBoxVM.exe"`.
  Con la ventana de la VM en segundo plano, Windows la relegaba a los núcleos E.
  Además: el PC sin suspenderse, sin WSL ni otras cargas, y pausar Windows
  Update.

### Datos disponibles en Windows

Todo lo necesario para un simulador o un análisis está en Windows:

| Qué | Dónde | Tamaño |
|---|---|---|
| Catálogo | `TFG Material\02_corpus_red\catalogo_trazas.json` | 6768 trazas |
| Trazas normalizadas | `02_corpus_red\datasets_normalizados\` | 6992 ficheros |
| Dataset de entrenamiento | `06_dataset_entrenamiento\dataset_entrenamiento\datos_entrenamiento.jsonl` | 1,2 GB |
| Dataset de validación | `06_dataset_entrenamiento\dataset_entrenamiento\datos_validacion.jsonl` | 275 MB |
| Bundle del modelo | `03_modelos\modelo_propio\bundle\` | — |
| Descriptores de tamaños de los 8 vídeos | `01_codigo\ClienteDashTFG\perfiles_video\tamanos_segmentos\` | — |

### Tiempo por sesión

Las sesiones corren en **tiempo real**. 300 sesiones duran unas 10,5 h, es
decir, unos **2,1 min por sesión** con la sobrecarga incluida.

---

## 4. Hechos verificados hoy (cifras y fuente)

### 4.1 Particiones del catálogo

| Partición del catálogo | Trazas | Uso real | Fuente |
|---|---|---|---|
| `train` | 4725 | Entrenamiento | — |
| `test` | 1018 | **Validación de la red**: rol `validacion`, parada temprana y barrido de α en junio | `entrenamiento/corpus_trazas/muestreo.py:171` |
| `eval` | 1025 | Evaluación. El código la prohíbe para el dataset | `muestreo.py:169-170`, `ventanas.py:197` |

En la memoria, `test` se llama **validación**.

### 4.2 Ventanas reales disponibles en `eval`

Calculado con `core/evaluacion/seleccion.py` sobre el catálogo. "No trivial"
significa que no es de muy alta capacidad (≥ 20 Mbit/s de media), donde todos
los controladores eligen el máximo.

| Conjunto | Ventanas | No triviales |
|---|---|---|
| Reales en `eval` | 873 | — |
| Duración ≥ 300 s y suelo 450/300 kbps (filtro actual) | 736 | 163 |
| … sin los 27 grupos usados en desarrollo | 636 | 81 |
| … sin esos 27 ni los 12 del experimento detenido (39 grupos) | 618 | **66** (FCC: alta 50, media 11, baja 5; sin redes móviles) |
| Filtro tipo Pensieve¹ con duración ≥ 160 s, sin los 39 grupos | **65** | Oboe 56, FCC 9 |
| Ídem sin el filtro del mínimo (media 0,45–6 Mbit/s) | 82 | Oboe 56, FCC 19, Roma 7 |
| Partición de validación (`test`), filtro tipo Pensieve, ≥ 160 s | **84** | Oboe 61, FCC 23 |

¹ Media < 6 Mbit/s y mínimo > 0,2 Mbit/s.

Con ventanas de 300 s, las ventanas difíciles sin usar están casi agotadas. Las
de Oboe duran 158–216 s y la exigencia actual de 300 s las deja fuera.

### 4.3 La selección es de prefijo

Con la misma semilla y las mismas exclusiones, un preset pequeño elige las
**primeras** ventanas del grande. Por ejemplo, las 8 de `rapido` son las 8
primeras de `tfg_final`.

Por eso **las pruebas previas no pueden sortear de `eval` con la configuración
final**: quemarían ventanas del experimento final. Las pruebas previas deben
salir de la partición de validación (o de los grupos ya usados en desarrollo).
`seleccion.py` solo filtra `particion == "eval"`, así que hay que añadir una
opción de partición.

### 4.4 Empates y potencia estadística

Datos de desarrollo: los dos paquetes archivados, 48 escenarios reales cada uno.

**Propio frente al MPC robusto actual:**

| | Agosto | Octubre |
|---|---|---|
| Escenarios con empate exacto | 24 de 48 | 24 de 48 |
| Δ QoE media | +0,063 | −0,009 |
| Desviación de las diferencias pareadas (sin ventanas de muy alta capacidad) | 0,528 | 0,304 |

**Escenarios necesarios** para detectar una diferencia con potencia del 80 %
(α = 0,05, bilateral, aproximación normal):

| Diferencia a detectar | Escenarios necesarios |
|---|---|
| Δ = 0,10 | 73–219 |
| Δ = 0,15 | 33–98 |

Con 48 escenarios, de los cuales la mitad empatan, no se puede demostrar una
mejora pequeña frente al MPC robusto.

Alternativa rigurosa: una **prueba de equivalencia (TOST)** con un margen fijado
de antemano, más superioridad en las métricas de rebuffering. Para equivalencia
con ±0,15 y σ ≈ 0,4 hacen falta unos 60 escenarios no triviales. Hay que
recalcular con los datos del simulador.

### 4.5 El MPC robusto del cliente no es el canónico

Estado actual del código, en `core/controladores/mpc.py` (`robust_mpc.py`
hereda de él):

| Parámetro | Valor actual | Fuente |
|---|---|---|
| Horizonte | `HORIZONTE_POR_DEFECTO = 3` | línea 10 |
| Límite de secuencias | `MAX_SECUENCIAS_ENUMERADAS = 4096` (un horizonte de 5 necesita 7776; con 4096 se recortaría a 4) | línea 15 |
| Calidad | q(R) = ln(R/Rmin) | `_calidades_log_ratio_tasas`, líneas 346-348 |
| Pesos | rebuffering 4,3 y cambios 1 | — |
| Tamaños | **nominales**: tasa × duración | `_tamanos_candidatos_B`, líneas 351-352 |
| Predicción | Media armónica de 5 | — |
| Robusto | base / (1 + error máximo de 5), arranque ×0,85 | — |

En las ejecuciones de desarrollo corrió con `parametros: {}`, es decir, con
estos valores por defecto. Comprobado en `00_protocolo/configs_cliente/*mpc_robusto*.yaml`
del paquete `20261013_233745_tfg_final`.

**Literatura** (verificada hoy):

- **Yin et al. 2015**, `yin2015mpc`, §7.1: q(·) identidad (lineal), horizonte 5,
  media armónica de 5. Está en el `.md` de `docs/todos los estudios...`, líneas
  ~903-935.
- **Pensieve**, `mao2017pensieve`, §5.1: el MPC y el robustMPC maximizan la
  métrica de QoE evaluada con un horizonte de 5 chunks. Usa la misma escalera
  300…4300 kbps y la QoE_lin con 4,3.
- **Código de referencia de Pensieve**
  (`github.com/hongzimao/pensieve/blob/master/test/mpc.py`, consultado hoy):
  - `MPC_FUTURE_CHUNK_COUNT = 5`
  - `REBUF_PENALTY = 4.3`, `SMOOTH_PENALTY = 1`
  - recompensa **lineal** en Mbit/s (la logarítmica está comentada)
  - tiempo de descarga con **tamaños reales** de chunk (`get_chunk_size`)
  - media armónica de los 5 últimos
  - robusto: `/(1 + max_error)`

**Conclusión.** El MPC robusto actual está en desventaja frente a su forma
canónica: horizonte 3, utilidad logarítmica y tamaños nominales. Un tribunal que
conozca Pensieve puede decir que se comparó con una línea base debilitada.

En agosto Daniel eligió tamaños nominales como "convención DASH estándar". Con la
evidencia del código de Pensieve, conviene revisar esa decisión con él (§5, D2).

### 4.6 Filtro de trazas de Pensieve

Pensieve §5.1 (párrafo de trazas; en el `.md`, líneas ~575-582) solo usa trazas
con throughput medio menor que 6 Mbit/s y mínimo mayor que 0,2 Mbit/s. Su razón:
evitar los casos donde elegir siempre la máxima calidad es lo óptimo y aquellos
donde la red no sostiene ningún nivel. Yin 2015 también filtra las trazas FCC
por throughput medio (verificar la cifra exacta en el PDF).

Es la referencia para un **filtro de ventanas relevantes**, fijado antes y
declarado.

### 4.7 Ventana de traza necesaria

Estimación: suma de las descargas más las esperas con el buffer lleno, sobre las
sesiones reales de desarrollo.

| Paquete | Mediana | P95 | Máximo | Dónde se da el máximo |
|---|---|---|---|---|
| Agosto | 68 s | 131 s | 145 s | Baja capacidad |
| Octubre | 60 s | 116 s | 134 s | Baja capacidad |

Una ventana de 160 s, con `politica_fin = "loop"` y `max_bucles = 1` como red de
seguridad (`core/reproduccion_trazas/modelo_red.py` ya lo admite), bastaría y
abre Oboe. Antes hay que verificarlo con las columnas `replay_tiempo_traza_fin_s`
de la telemetría de sesión.

### 4.8 Piezas para un simulador rápido

Hoy la emulación duerme lo que dicta la traza
(`core/reproduccion_trazas/descargador_controlado.py`, `con_esperas`) y el motor
simulado consume en tiempo real con un hilo (`core/motores/simulado.py`). Por
eso cada sesión dura lo mismo que en la realidad.

Lo que ya existe:

- **`entrenamiento/simulador_sesiones.py`**: `EntornoSesion` con
  `ModeloRedPorTraza` y una escalera con tamaños reales. Es un simulador por
  segmento en tiempo virtual. No modela la espera con el buffer lleno: recorta
  el buffer a 60 s y la traza no avanza durante la espera. Hay que corregirlo si
  se usa.
- **`docs/memoria/apoyo/reproducir_decisiones_propio.py`**: alimenta al
  controlador real con filas de realimentación de un paquete. Reproduce
  1740/1740 decisiones.
- Contrato de realimentación: `core/feedback_reproductor.py`.

**Propuesta.** Un arnés en tiempo virtual que conduzca las clases **reales** de
los controladores con realimentación idéntica a la del reproductor.

- **Validación sin VM:**
  - los clásicos, sobre los dos paquetes de desarrollo, porque su código no ha
    cambiado;
  - el propio, sobre el paquete detenido, que lleva el código final.
- **Usos:** prueba previa en minutos sobre la validación, estimación de varianza
  y potencia, y decisiones de diseño sobre la validación.

### 4.9 El predictor no ve el contenido

Entradas del predictor:

- **Secuencia:** 2 features (throughput y tiempo de descarga) de las 5 últimas
  descargas.
- **Escalares (7):** buffer, último índice, último bitrate, rebuffering
  reciente, cambio reciente, segmentos restantes normalizados y si quedan
  segmentos (`03_modelos\modelo_propio\bundle\configuracion_modelo.json`).

Ningún tamaño de segmento entra en el predictor. El contenido entra solo por los
tamaños reales que usa el planificador, leídos del descriptor del vídeo activo.

### 4.10 Vídeos

- **Evaluación:** 4 vídeos de 10 min en
  `core/evaluacion/catalogo.py:PERFILES_VIDEO` = 2 contenidos × 30/60 fps.
  - Paseo Almuñécar: grabación real.
  - Blender Sunflower: muy probablemente la edición "sunflower" de Big Buck
    Bunny (dura 10:34,6). Confírmalo con Daniel.
- **Entrenamiento:** rotó 8 descriptores, los 2 contenidos × {10 min, 1 min} ×
  {30, 60 fps}.
- **Consecuencia:** el contenido evaluado son 2 contenidos, ambos vistos. Un
  vídeo nuevo debe ser **otro contenido** (no Big Buck Bunny), con licencia
  abierta (por ejemplo Tears of Steel o Sintel, CC-BY) y codificado con la misma
  herramienta y la misma escalera.
- **Para añadir un vídeo:**
  1. codificarlo en la VM servidor;
  2. extraer su descriptor con `scripts/1_contenido/extraer_tamanos_reales_segmentos.py`;
  3. añadirlo a `PERFILES_VIDEO`;
  4. añadirlo a `MAPA_ID_CORTO_A_DESCRIPTOR` (`core/modelo_propio/perfil_video.py`);
  5. añadirlo a la comprobación del kit.

### 4.11 Código muerto con un fallo

En `entrenamiento/politicas_rollout.py:119-131`, `evaluar_acciones_qh` usa
nombres inexistentes (`values`, `viables`). Es el oráculo Q_H abandonado. Solo
lo alcanza `utilidades_rollout._muestras_de_rollout_ventana`.
`dataset_cuantiles.py` define su propia función, así que el dataset real no pasa
por ahí.

`generar_dataset.py` importa dos utilidades de `utilidades_rollout`. En el
pulido final hay que moverlas y quitar el código Q_H muerto.

### 4.12 Datos del modelo

**Dataset y entrenamiento:**

- 490 500 muestras de entrenamiento y 111 630 de validación, de 5031 ventanas;
  4 políticas de exploración. Auditoría de no contaminación superada.
- AdamW, 80 épocas, mejor época por validación entre 66 y 80 (dos miembros en
  78 y 80); pinball más suavidad temporal 0,05.

**Calidad del predictor:**

| Medida | Resultado |
|---|---|
| Cobertura en validación con ensanchado (nominal 10/25/50/75) | 7,0 / 18,3 / 43,9 / 79,0 %; desviación máxima 6,7 puntos, en q25 |
| Error log de la mediana en lazo cerrado (desarrollo, h = 1) | 18–21 % menor que la media armónica |
| Cobertura en lazo cerrado | 5,1 / 24,7 / 53,6 / 75,8 % |

**Cuánto cambian las decisiones** sin cada componente (Tabla 5.7 de desarrollo,
1392 decisiones):

| Variante | Decisiones que cambian |
|---|---|
| Decidir solo con la mediana | 23,6 % |
| Peor caso | 1,4 % |
| Media de los 4 cuantiles | 1,1 % |
| Tamaños nominales | 4,9 % |
| Sin ensanchado | 4,4 % |

α = 0,75 se fijó en junio con un barrido sobre 27 ventanas de **validación**; la
frontera salió plana.

---

## 5. Deficiencias y propuesta

Lista de Daniel, más las que han salido hoy.

| Deficiencia | Pregunta del tribunal | Propuesta | Coste |
|---|---|---|---|
| **D1.** No está aislado qué aporta la red | "¿Y con cuantiles fijos en vez de la red?" | Variantes **dentro del experimento final**: `propio_mediana` (misma red, decide con la mediana: aísla el CVaR) y `propio_cuantiles_fijos` (mismo planificador con CVaR; escenarios = media armónica × exp(cuantiles empíricos de la etiqueta de entrenamiento por horizonte), calculados una vez y versionados con huella: aísla el condicionamiento de la red). Con D2, el propio frente al MPC robusto aísla predictor más riesgo | Implementar 2 controladores; +2/7 de sesiones |
| **D2.** Objetivo no igualado (y MPC debilitado, §4.5) | "¿Su MPC optimiza otra cosa, con horizonte 3?" | MPC robusto **canónico**: horizonte 5, q lineal en Mbit/s, μ = 4,3, λ = 1, tamaños reales del descriptor del vídeo activo, media armónica 5, /(1 + error máximo de 5). Implementarlo con el **mismo** planificador vectorizado y un solo escenario: igual semántica, solo cambia la predicción. Citas: Yin 2015 y Pensieve (artículo y código). Decide Daniel (en agosto eligió tamaños nominales) | Pocas horas; riesgo: el MPC se vuelve más fuerte |
| **D3.** Calibración imperfecta | "¿Sus cuantiles son fiables?" | (a) **Medir siempre**: fiabilidad por h/τ en validación, pinball frente a la media armónica y frente a cuantiles fijos, cobertura en lazo cerrado en el paquete final. (b) **Opcional**: recalibración conformal por (h, τ) con una mitad de la validación, separada por grupo; se adopta solo si en la prueba previa sobre validación no empeora QoE ni rebuffering (criterio fijado antes). Referencias nuevas (CQR de Romano 2019, Kuleshov 2018), a descargar con permiso. (c) Si no se adopta, declarar con números que la cola baja es prudente a propósito | (a) horas; (b) un día |
| **D4.** Banco pequeño, ventanas fáciles, sin potencia | "¿48 escenarios y la mitad empatan?" | 1. **Filtro de ventanas relevantes** tipo Pensieve, fijado y citado, quizá calculado sobre la ventana y no sobre la traza. 2. **Ventanas de 160 s** con bucle de seguridad, que abren Oboe. 3. **Más ventanas y menos vídeos por ventana**: la diversidad de redes vale más que repetir vídeo. 4. **Estadística:** pareada, IC95 por bootstrap **por ventana** (clúster), signo exacto, G/P/E, Holm en la familia, **TOST** frente al MPC robusto con margen fijado antes, resultados por tramo, métricas secundarias (rebuffering, paradas, sesiones > 5 s, P5 y mínimo). 5. **N** fijado con la potencia estimada con el simulador | Código de selección y análisis; horas de VM según N |
| **D5.** Emulación, no red real | "¿Y TCP o el tráfico competidor?" | No se toca. Se declara: bytes reales, servidor real, cliente real; lo emulado es la temporalidad. Citas: `netravali2015mahimahi`, `sentosa2025cellreplay`, `alomar2023causalsim`, `yan2020puffer`, `hoffman2025intoTheWildABR` | Nada |
| **D6.** Contenido ya visto | "¿Y con otro vídeo?" | Un **vídeo nuevo** (CC-BY, otro contenido) dentro del experimento final; se informa su variabilidad VBR. Como el predictor no ve el contenido (§4.9), se mide sobre todo el planificador leyendo un descriptor nuevo. Diseño posible: cada ventana con un vídeo visto (en rotación) más el nuevo, para comparar contenido visto y nuevo en las mismas redes | Descarga con permiso; ~1 h de preparación |
| **E1.** Pruebas previas que queman ventanas (§4.3) | — | Pruebas previas solo sobre la validación (opción de partición) | Pequeño |
| **E2.** Sesiones de 30 segmentos (2 min) | "¿Sesiones cortas?" | Se mantienen: el progreso del predictor se entrenó con 30. Se declara | Nada |
| **E3.** Ventanas sintéticas ya ejecutadas en desarrollo | — | Nueva semilla o exclusión de las ya usadas. Son diagnóstico y se informan aparte | Pequeño |
| **E4.** Código muerto con fallo (§4.11) | Lectura del código | Quitarlo en el pulido | Pequeño |

**Convergencia** (dos miembros con mejor época en 78 y 80): no reentrenar. Se
documenta con la meseta de validación. Antes de afirmarlo, comprobar la pérdida
de validación por época en el informe de entrenamiento de WSL
(`~/TFG/legacy/antes_castellano_20260806_2111/modelos/modelo_propio/entrenamiento/reporte_entrenamiento_temporal.json`).

**Riesgo honesto.** Con el MPC canónico, el propio puede empatar o perder en QoE
media. La prueba previa lo dirá antes del experimento final. Si pierde en media
pero gana en rebuffering y cola, el relato es el compromiso riesgo-calidad, el
mismo eje que BayesMPC o SafeSABR.

Solo se puede ajustar algo sobre la **validación**, por ejemplo α o la
recalibración, con un criterio escrito antes. Nunca sobre `eval`.

---

## 6. Proceso propuesto, con semáforo antes del experimento final

Es una propuesta. El hilo nuevo la verifica y la concreta.

| Fase | Quién | Qué |
|---|---|---|
| F0 | Daniel | Decide D2, las variantes, el vídeo nuevo, el tamaño del experimento y la recalibración |
| F1 | Claude | Implementa los cambios en `TFG Material` (con copia previa a legacy) y los verifica (detalle debajo) |
| F2 | Claude | Simulador en tiempo virtual: lo valida contra los paquetes de desarrollo y lo ejecuta sobre la validación con todos los controladores. Salen efectos, empates, varianzas, potencia y N. **Semáforo 1** con un criterio escrito antes |
| F3 | Daniel | Codifica el vídeo nuevo en la VM servidor |
| F4 | Daniel | Ejecución corta en la VM sobre ventanas de validación (~2–3 h), con todos los controladores y el vídeo nuevo. Confirma que simulador y banco coinciden, 0 respaldos y latencias. **Semáforo 2** |
| F5 | Claude | Fija el **protocolo final** y lo commitea, junto con el kit nuevo (huellas, ventanas esperadas, comprobaciones de 5 vídeos), **antes** de ejecutar |
| F6 | Daniel | Ejecuta el experimento final, una sola vez, por la interfaz |
| F7 | Claude | Verificación, reproducción fuera de línea, análisis según el protocolo y copia a `04_evidencia_final` |
| F8 | Claude | Pulido neutro del material: `.idea`, código muerto, LEEME, `requirements` |
| F9 | Ambos | Memoria: revisión de los Word de Daniel (cap 4 y 5.1–5.3) y remake desde el 5.4 |

**Detalle de F1.** Cambios en `TFG Material`:

- MPC canónico y las dos variantes;
- opción de partición, y de duración y bucle de ventana;
- asignación de vídeo por ventana;
- análisis: TOST, Holm, bootstrap por clúster y resultados por tramo;
- cuantiles fijos versionados.

Verificación: el propio decide igual que antes en las 1740 decisiones de
desarrollo, o en las del paquete detenido.

**Tamaño del experimento final**, con 7 controladores (`basado_en_tasa`, `bba`,
`bola`, `mpc_robusto` canónico, `controlador_propio`, `propio_mediana`,
`propio_cuantiles_fijos`), 48 ventanas reales, 3 sintéticas y 2,1 min por
sesión:

| Diseño | Escenarios | Sesiones | Horas de VM |
|---|---|---|---|
| (a) 1 vídeo por ventana (rotación de 5) | 51 | 357 | ~12,5 |
| (b) 2 vídeos por ventana (uno visto + el nuevo) | 102 | 714 | ~25 |
| (c) 5 vídeos por ventana | 255 | 1785 | ~62 |

No se recomiendan sesiones en paralelo en la VM: la temporización es real y
habría que validarlas aparte.

---

## 7. Lo que no se hace

- Red real, `tc` o tráfico competidor.
- Reentrenar, salvo que la prueba previa muestre un fallo que lo exija.
- Lanzar el preset `extendido` a ciegas.
- Tocar `eval` en las pruebas.
- Mirar resultados del final antes de fijar el análisis.
- Comparar con Pensieve: no hay entrenamiento ni puerto; el trabajo propio ya
  cubre esa vía.
- Trabajar en la memoria antes de cerrar lo técnico.

---

## 8. Apartados de la memoria que quedarán afectados

Solo como apunte; no se trabajan ahora.

- **Word de Daniel:**
  - 4.3 (paso de espera de 0,01 s en la evaluación)
  - 4.4 (cola mínima de 0,1 s en la evaluación)
  - 4.5 (registro con más controladores)
  - 4.7 (duración y bucle de la ventana, filtro de ventanas, "validación", frase
    del empate)
  - 4.8 (estadística: TOST, Holm, clúster; compuertas)
  - 5.2 (política de fin en bucle)
- **Remake de Claude:**
  - 5.4 (selección, partición, asignación de vídeo, presets)
  - 5.5 (MPC canónico)
  - 5.6 (propio y variantes; cuantiles fijos)
  - 5.7
  - capítulo 6 entero
  - 7

---

## 9. Primera respuesta del hilo nuevo

1. Verificar contra el código y los datos lo que vaya a usar de §4. No repetir
   la lectura en voz alta: un resumen corto.
2. Dar el **plan de pasos**:
   - quién hace cada paso (Claude o Daniel);
   - orden y duración;
   - comandos cortos para Daniel;
   - cada decisión de F0 con la recomendación primero.
3. Definir los **semáforos**: qué resultado de la prueba previa significa
   "adelante", cuál "ajustar en validación" y cuál "replantear".
4. Proponer el diseño del experimento final con horas de VM, y la lista de
   cambios de código con su verificación.
5. Señalar los riesgos con honestidad, incluido que el propio pierda frente al
   MPC canónico, y cómo se contaría.
6. No preguntar nada que no bloquee. Lo opinable va como recomendación para que
   Daniel confirme.

---

## 10. Ficheros clave

| Qué | Dónde |
|---|---|
| Este traspaso y el prompt | `docs/blindaje/` |
| Kit y protocolos del 14/10 (base, superados) | `docs/evaluacion_final/` |
| Configuración de la evaluación | `TFG Material\01_codigo\ClienteDashTFG\config\evaluacion.local.json` (27 grupos excluidos) |
| Presets, vídeos y selección | `core/evaluacion/catalogo.py`, `seleccion.py`, `configuracion.py` |
| Análisis y verificación | `core/evaluacion/analisis.py` (bootstrap y signo; sin TOST, Holm ni clúster), `verificacion.py` |
| Controladores | `core/controladores/` (`registro.py`, `mpc.py`, `robust_mpc.py`, `controlador_propio.py`, `constructor_entradas.py`) |
| Modelo propio | `core/modelo_propio/` (`planificador.py` vectorizado, `bundle.py`, `perfil_video.py`) |
| Emulación | `core/reproduccion_trazas/` (`modelo_red.py` con loop, `descargador_controlado.py`) |
| Simulador de entrenamiento | `entrenamiento/simulador_sesiones.py` |
| Reproducción y análisis de decisiones | `docs/memoria/apoyo/` |
| Paquetes de desarrollo | `TFG\legacy\evidencia_desarrollo\` |
| Plan de la memoria | `docs/memoria/00_PLAN_MAESTRO_MEMORIA.md`; estándar de redacción en la memoria persistente |

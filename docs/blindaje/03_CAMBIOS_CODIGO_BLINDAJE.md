# Fase de blindaje: registro de cambios del código entregado

El código que se entrega y que corre en la VM está en
`TFG Material\01_codigo\ClienteDashTFG` y no tiene git. Cada cambio se
documenta aquí, con su verificación.

- **Copia previa a todos los cambios de esta fase:**
  `TFG\legacy\codigo_entrega_20261014_antes_blindaje\ClienteDashTFG`, con las
  huellas SHA-256 de sus 96 ficheros en `huellas_antes_blindaje.sha256`
  (`__pycache__` y `.idea` excluidos).
- **Diff acumulado frente a esa copia:** `cambios_codigo_blindaje.diff`, que
  se regenera con cada cambio. Desde `C:\Users\danie\Documents`:
  ```bash
  diff -ruN --exclude=__pycache__ --exclude=.idea "TFG/legacy/codigo_entrega_20261014_antes_blindaje/ClienteDashTFG" "TFG Material/01_codigo/ClienteDashTFG" > "TFG/DashClientModular4/docs/blindaje/cambios_codigo_blindaje.diff"
  ```

---

## C1. Tres fallos de traducción (NameError), 14/10 noche

Al traducir el código al castellano quedaron nombres sin definir. Los detecta
`ruff check --isolated --select F821`.

| Fichero | Antes | Después | Qué rompía |
|---|---|---|---|
| `scripts/1_contenido/extraer_tamanos_reales_segmentos.py:194` | `while number < start_numero + hard_tope:` | `while numero < numero_inicial + tope_duro:` | La extracción de tamaños de cualquier vídeo (hace falta para el vídeo nuevo) |
| `entrenamiento/dataset_cuantiles.py:222` | `limpio_quantiles` | `cuantiles_limpios` | La regeneración del dataset, al final, ya escrito el `.jsonl` |
| `entrenamiento/dataset_fiel.py:108` | `str(mid)` | `str(id_perfil)` | El retorno de `construir_dataset` |

Además, en el mismo script de extracción, las claves de metadatos del JSON se
habían traducido (`frame_tasa`, `start_numero`, `segmento_bytes_media`…). Se
devuelven a las del esquema `tamanos_segmentos_perfil_v1` con el que se
generaron los 8 descriptores guardados. El volcado vuelve a `sort_keys=True`
con salto de línea final, como los guardados. Así el descriptor del vídeo nuevo
tiene el mismo formato que los otros 8. El cargador
(`core/modelo_propio/perfil_video.py`) solo lee las claves comunes, que no
cambian.

Queda el fallo del oráculo Q_H en `entrenamiento/politicas_rollout.py:119-131`.
Es código muerto y se quita en el pulido final (F8), junto con sus constantes y
utilidades.

### Verificación

1. `ruff check --isolated --select F821` solo marca el Q_H muerto.
2. **Re-extracción de los 8 descriptores** desde el servidor DASH, con el
   script corregido y a una carpeta temporal. Los 8 coinciden con los
   guardados: mismas claves, en el mismo orden, y los mismos
   `segment_bytes`, `bandwidth_bps` e `init_bytes`. Solo cambian la marca
   `generado` y el último decimal de algún coeficiente de variación
   (redondeo de coma flotante, tolerancia relativa 1e-12).
3. **Humo de la generación del dataset.** Se ejecutó
   `scripts/2_entrenamiento/generar_dataset.py --perfil piloto` con 2 ventanas
   de entrenamiento y 2 de validación, a una carpeta temporal:
   - `estado=PASS`, 240 + 240 muestras, fuga `PASS` y 0 ventanas omitidas;
   - `--solo-validar` da `PASS`;
   - las claves de las muestras son las que lee
     `entrenamiento/entrenamiento_modelo.py`.

   En Git Bash hay que poner `MSYS_NO_PATHCONV=1`: si no, convierte el
   `/home/...` de `--reescritura-ruta-traza`.
4. **Nota para el pulido:** el `esquema_targets.json` del dataset entregado
   (`06_dataset_entrenamiento`) conserva los nombres de campo en inglés,
   mientras que las muestras `.jsonl` y el código los usan en castellano. Se
   regenera o se traduce en F8.

---

## C2. Asignación de paradas en el reproductor, 14/10 noche

Problema, medido en los paquetes reales: el reproductor apuntaba cada parada a
la fila en cabeza de la cola de reproducción y anulaba la fila del último
segmento para no contar el vaciado final.

- Según la fase del tic de 10 ms del motor, la cabeza era el segmento anterior
  (~79 %) o el que se esperaba (~21 %).
- Así, la parada antes del último segmento **se perdía a veces**. En octubre,
  tres casos de BBA y BOLA de hasta 9,48 s, que cambian la QoE de la sesión en
  1,4 puntos.
- Y la parada antes del segundo segmento **contaba a veces**.

Corrección en `reproductor.py`:
- la parada se apunta al segmento que se está esperando (`indice_actual`);
- las paradas que empiezan con todas las descargas hechas (el vaciado final)
  se ignoran por estado (`_descargas_terminadas`);
- ya no se anula la fila del último segmento.

La suma de paradas de la sesión es la misma, salvo los dos bordes que antes
dependían del azar.

Verificación: `pruebas/test_paradas_y_variantes.py` y una sesión real en
Windows contra el servidor, con la parada en la fila del segmento esperado.

## C3. MPC robusto canónico, 14/10 noche

Reescritos `core/controladores/mpc.py` y `robust_mpc.py` en la forma de
referencia de Yin et al. (2015, sec. 7.1) y del código de Pensieve
(`test/mpc.py`):

- **horizonte** de 5;
- **QoE lineal** en Mbit/s, con 4,3 por segundo de rebuffering y 1 por Mbit/s
  de cambio;
- **tamaños reales** del vídeo activo;
- **predicción** con la media armónica de las 5 últimas descargas, incluidas
  las de calentamiento;
- **parte robusta:** se divide entre (1 + error porcentual máximo de esa media
  armónica en las 5 últimas descargas). Sin factor de arranque.

Decide con el planificador del controlador propio con un solo escenario, así
que frente al propio solo cambia la predicción. El descriptor del vídeo se lee
al crear el controlador: si falta, la sesión falla al empezar.

Se van las desviaciones del MPC anterior:
- horizonte 3;
- ln(R/Rmin);
- tamaños nominales;
- error medido contra la predicción ya rebajada;
- ×0,85 al arrancar;
- historial sin la descarga de calentamiento.

Verificación: `pruebas/test_mpc_canonico.py`.
- En 400 estados aleatorios con tamaños reales, la secuencia elegida tiene la
  recompensa máxima de una copia literal del bucle de Pensieve. La acción
  coincide en ≥ 390; el resto son empates exactos.
- Comprueba el error contra la media armónica, la ausencia de factor de
  arranque, el historial con calentamiento y el fallo si falta el descriptor.

## C4. Variantes de ablación del controlador propio, 14/10 noche

- `core/controladores/entradas_planificador.py`, nuevo: estado de la sesión y
  escalera, movidos sin cambios desde `controlador_propio.py` para
  compartirlos con el MPC.
- `controlador_propio.py`:
  - parámetro `modo_prediccion`: `red` (el propio), `mediana`,
    `cuantiles_fijos` o `cuantiles_recientes`, con claves de registro
    `propio_mediana`, `propio_cuantiles_fijos` y `propio_cuantiles_recientes`;
  - `alfa_riesgo="buffer"` y `ruta_recalibracion`, opcionales, para el ajuste
    D7 (no adoptados);
  - el respaldo es el MPC robusto canónico del mismo vídeo y recibe todas las
    descargas.
- `constructor_entradas.py`: `registrar_realimentacion` devuelve si entró una
  descarga nueva, y hay una propiedad `historial_throughput_bps`. No cambia
  nada de lo que calcula.
- `core/modelo_propio/bundle.py`: `predecir` acepta desplazamientos opcionales
  de recalibración (no adoptados).
- `scripts/2_entrenamiento/calcular_cuantiles_fijos.py`, nuevo. Genera
  `TFG Material\03_modelos\cuantiles_fijos\cuantiles_fijos.json`:
  - 474 150 muestras con historial del dataset de entrenamiento;
  - SHA-256 del fichero: `a3a5ceb2d086bd3f5832c71245a89f7c418dc4947360fda9a3f330eeb230dc89`;
  - SHA-256 del dataset de origen: `eccc5f0c…1bb`.

Verificación:
- **regresión con el simulador sobre 2000 sesiones de validación:** el propio
  repite 400/400 trayectorias bit a bit, y los clásicos también;
- `pruebas/test_paradas_y_variantes.py` (variantes);
- sesión real en Windows de `propio_cuantiles_recientes`, con 0 respaldos.

## C5. Ejecución y análisis, 14/10 noche

- `scripts/3_evaluacion/ejecutar_evaluacion.py`: el `id_perfil_video` de la
  sesión llega a todos los controladores. El propio y el MPC planifican con sus
  tamaños; los demás lo ignoran.
- `core/evaluacion/catalogo.py`: alias y nombres visibles de las variantes.
- `core/evaluacion/analisis.py`: la compuerta de inferencia auditada solo
  exige inferencia a las variantes con red (`controlador_propio`,
  `propio_mediana`). La de respaldo sigue para todas.

## C6. Selección, plan, ejecución y análisis del experimento final, 14/10 noche

- **`core/evaluacion/catalogo.py`:**
  - vídeo nuevo `tears_10min_30fps_4s` (Tears of Steel, CC-BY 3.0);
  - presets `previa_vm` y `final_blindaje`. La prueba corta usa 10 ventanas de
    validación. El final usa todas las ventanas relevantes de eval, más 3
    sintéticas.

  En los dos:
  - ventanas de 160 s con bucle de seguridad (`politica_fin = loop`,
    `max_bucles = 1`);
  - filtro de Pensieve sobre la ventana;
  - un vídeo visto en rotación más el nuevo en cada ventana;
  - orden de los controladores sorteado en cada escenario.
- **`core/evaluacion/seleccion.py`:**
  - partición configurable por preset;
  - filtro de Pensieve calculado sobre la ventana (media < 6 Mbit/s y mínimo
    > 0,2 Mbit/s), con las mismas funciones de carga que la emulación;
  - opción "todas";
  - estadísticas de cada ventana en el protocolo;
  - las exclusiones también se aplican a las sintéticas.

  Los presets antiguos no cambian.
- **`scripts/3_evaluacion/ejecutar_evaluacion.py`:**
  - política de fin del preset;
  - asignación de vídeos por ventana;
  - orden sorteado con semilla;
  - hipótesis copiadas al protocolo antes de ejecutar;
  - opción `--paralelo` / `sesiones_en_paralelo`. Por defecto 1, como siempre;
    **no se usa**, porque el final va en serie.
- **`core/evaluacion/contrastes.py`, nuevo.** Contrastes prerregistrados:
  - **P1:** QoE equivalente al MPC robusto, TOST con margen ±0,15;
  - **P2:** menos paradas que el MPC;
  - **P3:** menos paradas que los cuantiles recientes;
  - **P4:** más QoE que los cuantiles fijos;
  - **P5:** menos paradas que la mediana.

  Métodos:
  - prueba del signo exacta sobre las medias por ventana;
  - IC por bootstrap de ventanas (10 000 remuestreos);
  - Holm sobre P1–P5.

  Secundarias:
  - todas las métricas frente a cada rival;
  - estratos Oboe/FCC y visto/nuevo;
  - interacción de contenido.

  `analisis.py` escribe `contrastes_prerregistrados.json` y `.md`.
- **`config/evaluacion.local.json`:**
  - los 8 controladores, con los parámetros de las variantes;
  - preset `final_blindaje`;
  - los 42 grupos ya usados en desarrollo, excluidos: 39 reales y las 3
    sintéticas.

Verificación:
- **planes en seco:**
  - `previa_vm` da 10 ventanas: FCC 5, Oboe 4, NYU 1;
  - `final_blindaje` da 74 + 3 ventanas y 1208 sesiones;
- **tests:** `pruebas/test_contrastes.py`, con datos sintéticos de resultado
  conocido;
- **análisis completo** sobre una copia del paquete de octubre;
- **`kit_vm/comprobar_controladores.py`:** los 8 controladores deciden con los
  vídeos vistos.

## C7. Vídeo nuevo (Tears of Steel), 15/10

- **En el servidor**, con `kit_servidor/preparar_video_nuevo.sh`, salida
  correcta:
  - zip oficial con SHA-256 `d87a41de…57a5`;
  - original 1920×800 a 24 fps;
  - master de los primeros 600 s a 30 fps;
  - empaquetado con GPAC 2.5-DEV, la misma versión que los otros MPD;
  - 150 segmentos de 4 s en cada uno de los 6 niveles.
- **`perfiles_video/tamanos_segmentos/tears_of_steel_10min_30fps_4s.json`**,
  extraído desde Windows con el script del material. En los 30 segmentos de una
  sesión, el coeficiente de variación es 0,28–0,31, frente a 0,05 en Paseo y
  0,13–0,19 en Blender. Los dos primeros segmentos son casi negros: 2 % del
  tamaño nominal.
- **`core/modelo_propio/perfil_video.py`:** se añade `tears_10min_30fps_4s` al
  mapa de descriptores.
- **`scripts/1_contenido/extraer_tamanos_reales_segmentos.py`:** la carpeta de
  salida por defecto subía un nivel menos de la cuenta, tras moverse el script
  a `scripts/1_contenido`, y escribía en `scripts/perfiles_video`. Corregido.

Verificación:
- los 8 controladores deciden con los 5 vídeos (`kit_vm/comprobar_controladores.py`);
- 3 sesiones reales en Windows contra el servidor con Tears of Steel, con 0
  respaldos; la trayectoria del propio es idéntica a la del simulador;
- simulador sobre las 100 ventanas de validación: propio − MPC = −0,017
  [−0,045; +0,013], con 0,01 frente a 0,12 paradas por sesión.

## C8. Pulido antes de congelar (F8), 15/10

Copia exacta del código que ejecutó la prueba corta, antes de este pulido:
`TFG\legacy\codigo_previa_vm_20261014\ClienteDashTFG`. Sus huellas son las del
kit con el que la VM pasó `comprobar` (`hashes_codigo.sha256`, 100 ficheros).

- **Carga del modelo al crear el controlador.**
  - Problema: el propio y sus 3 variantes cargaban el bundle en la primera
    decisión (comprobación de huellas incluida). En la prueba corta, esa
    decisión tardó 53–98 ms; el resto, 1,5–2,9 ms de mediana (p99 de todas las
    decisiones: 66–72 ms). Incumplía el criterio del semáforo 2 (p99 < 20 ms).
  - Cambio en `controlador_propio.py`: `_cargar_modelo()` se llama en
    `__init__`. El controlador se crea antes de arrancar el reproductor
    (`main.py`), así que la carga queda fuera de la sesión, como en un
    reproductor real al arrancar. Si la carga falla, se reintenta en cada
    decisión y decide el respaldo con motivo `fallo_carga_bundle`, como antes.
    Los cuantiles fijos se cargan en el mismo sitio.
  - Medido en Windows: crear el controlador, 10–12 ms; primera decisión,
    1,8–3,4 ms. El MPC robusto, 2,6 ms en su primera decisión.
- **Fuera los ganchos de D7 no adoptados:** `alfa_riesgo="buffer"`,
  `ruta_recalibracion`, `cargar_desplazamientos` y los desplazamientos de
  `bundle.predecir`. `bundle.py` vuelve a ser idéntico al anterior al blindaje.
- **Fuera el código muerto de Q_H:** `entrenamiento/politicas_rollout.py` y
  `entrenamiento/utilidades_rollout.py` (guardados en
  `TFG\legacy\qh_retirado_20261015`).
  - Las dos funciones que usaba `generar_dataset.py` pasan a sus sitios:
    `reescrituras_rutas_por_defecto` a `corpus_trazas/rutas.py`, y
    `cargar_catalogo_trazas` ya existía en `corpus_trazas/ventanas.py`.
  - `entrenamiento/constantes.py` se queda con las 5 constantes que se usan.
    `FASE_DATASET_QH` conserva su valor porque está escrito en los metadatos del
    dataset entregado.
- **Pruebas dentro del código entregado:** `pruebas/` con las de C2–C6 y una
  nueva, `test_carga_modelo.py`. `pruebas/artefactos.py` encuentra el bundle y
  los cuantiles fijos en Windows y en la VM. 18 pruebas, todas correctas.
- **`.idea`** sale de la carpeta del código (a `TFG\legacy\idea_ClienteDashTFG_20261015`).
- **Fuera del código (datos):** el `esquema_targets.json` de
  `06_dataset_entrenamiento` tenía los 4 nombres de campo en inglés, mientras
  que las muestras `.jsonl` los usan en castellano
  (`objetivos_cuantiles_throughput.throughput_base_bps`…). Se sustituye por el
  que escribe el código actual, idéntico salvo esos 4 nombres. Ningún manifiesto
  guarda su huella. El original está en
  `TFG\legacy\dataset_esquema_targets_ingles`.

Verificación:
- **regresión con el simulador:** 4000 sesiones de validación (100 ventanas ×
  5 vídeos × 8 controladores), con la misma latencia simulada antes y después.
  Las 4000 filas, idénticas;
- **dataset piloto** (2 + 2 ventanas) regenerado antes y después: muestras,
  esquema y auditorías idénticos byte a byte; solo cambian las marcas de tiempo;
- `ruff check --select F` sin avisos, salvo un `f-string` sin variables en
  `reproductor.py:496`, anterior y sin efecto;
- `python -m unittest discover -s pruebas`: 18 pruebas correctas;
- `kit_vm/comprobar_controladores.py` en Windows: los 8 controladores deciden
  con los 5 vídeos.

El kit de la VM se regenera con 103 ficheros de código. `comprobar` ahora:
- ejecuta las pruebas en la VM;
- falla si sobra algún fichero de una versión anterior.

El humo comprueba la latencia: p99 < 20 ms y primera decisión del propio
< 20 ms.

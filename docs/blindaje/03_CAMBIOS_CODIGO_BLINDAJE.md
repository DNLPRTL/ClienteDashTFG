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

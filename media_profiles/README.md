# media_profiles/

Descriptores **versionados** del medio DASH real servido en `192.168.1.132`.

A diferencia de los datasets/trazas pesados (que viven fuera de Git), estos
descriptores son pequenos (unos KB por perfil) y son la **fuente de verdad del
medio** para entrenar y planificar con fidelidad VBR. Por eso se commitean: asi
viajan por GitHub a WSL (entrenamiento) y a Ubuntu cliente (runtime) sin copiar a
mano.

## `segment_sizes/<media_profile_id>.json`

Tabla real `segmento N -> bytes` por representacion, extraida con
`scripts/extraer_tamanos_reales_segmentos.py` (lee `Content-Length` de cada
`.m4s`). Schema `media_profile_segment_sizes_v1`. Contenido por perfil:

- metadatos del MPD: `mpd_url`, `segment_duration_s`, `segment_count`,
  `media_presentation_duration_s`;
- por representacion (ordenadas ascendente; `representation_index=0` = bitrate mas
  bajo = accion 0): `bandwidth_bps`, resolucion, `frame_rate`, `codecs`,
  `init_bytes`, `segment_bytes` (lista real), y evidencia VBR
  (`segment_bytes_cv`, `real_mean_vs_cbr_ratio`).

Perfiles cubiertos (solo versiones de **4 s**; las de 2 s se obvian):
`Paseo`/`Blender` x `10min`/`1min` x `30fps`/`60fps`.

> Generar/actualizar (en Ubuntu cliente):
> `bash scripts/extraer_tamanos_reales_segmentos_ubuntu_cliente.sh`

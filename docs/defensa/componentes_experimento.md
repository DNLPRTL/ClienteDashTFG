# Componentes del experimento — hardware, software, red, herramientas y formatos

Fecha: 2026-08-05. Sección de referencia para la memoria y la defensa: QUÉ
máquinas, QUÉ software con QUÉ versiones exactas, CÓMO se generó el contenido y
CÓMO se conecta todo. Fuentes: informes de entorno recogidos en cada máquina el
05/08/2026 (`TFG Material/00_info_entorno/`) + los propios artefactos (MPD,
scripts del servidor, repo).

---

## 1. Topología general

Un único PC físico (Windows) aloja TODO el experimento: dos máquinas virtuales
VirtualBox en red puente con el router doméstico (cliente y servidor, clones de
una misma VM base — mismo hostname `TFGv1`) y un WSL2 para el entrenamiento GPU.
No hay red real en las mediciones: las condiciones de red se EMULAN reproduciendo
trazas (replay determinista en el cliente); el HTTP cliente↔servidor solo
transporta los bytes del vídeo.

```text
PC físico (Windows 11)
├── VirtualBox 7.0.14 (red puente)
│   ├── VM Ubuntu CLIENTE  (192.168.1.160) — cliente DASH + Phase 6
│   └── VM Ubuntu SERVIDOR (192.168.1.132) — Apache sirve el contenido DASH
├── WSL2 2.7.3 · Ubuntu 24.04 — entrenamiento IA (GPU AMD por /dev/dxg)
└── Windows nativo — desarrollo (PyCharm), git, tests rápidos, memoria
        └── GitHub (DNLPRTL/ClienteDashTFG) = puente de código entre máquinas
```

## 2. Host físico (Windows)

| Componente | Valor |
|---|---|
| SO | Windows 11 Home 10.0.26200 |
| CPU | Intel Core i5-14600KF (14 núcleos / 20 hilos) |
| RAM | 32 GB |
| GPU | AMD Radeon RX 7800 XT (entrenamiento vía WSL2/ROCm) |
| Placa base | ASUS ROG STRIX Z690-A GAMING WIFI |
| Python | 3.12.8 |
| VirtualBox | 7.0.14 |
| WSL | 2.7.3.0 (kernel 6.6.114.1-1) |
| IDE | PyCharm Community Edition |
| Control de versiones | git + GitHub (repo `DNLPRTL/ClienteDashTFG`) |

## 3. VM Ubuntu CLIENTE (192.168.1.160) — el banco de pruebas

Único entorno donde se ejecuta lo que cuenta: el cliente DASH, los 6 controllers
y la evaluación formal Phase 6 (las 360 sesiones del resultado final).

| Componente | Valor (informe 05/08/2026) |
|---|---|
| SO | Ubuntu 20.04.6 LTS (focal), kernel 5.15.0-139-generic |
| Virtualización | VirtualBox ("oracle"); 8 vCPU, 8 GB RAM, disco 151 GB |
| Python | 3.8.10 (del sistema) |
| PyTorch | 2.4.1+cu121 (build CUDA ejecutando en CPU — la VM no tiene GPU; la inferencia de los bundles es CPU) |
| requests | 2.22.0 (descargas HTTP del cliente) |
| GStreamer | 1.16.3 + PyGObject 3.36.0 (motor de reproducción real; Phase 6 usa el motor `fake`) |
| numpy / pandas | 2.2.6 / 2.3.1 (análisis y gráficas de Phase 6) |
| matplotlib | (dependencia de análisis, requirements-analysis.txt) |
| openssh-server | 8.2p1 (transferencias scp con el host) |
| Otros presentes | ffmpeg 4.2.7, gpac 0.5.2, apache2 2.4.41 (instalados en la VM base clonada; no intervienen en el experimento) |

Qué habría que instalar en un PC nuevo para REPLICAR el rol de cliente:
`python3` + `pip install -r requirements.txt` (requests) + PyTorch CPU +
`pip install -r requirements-analysis.txt` (numpy/pandas/matplotlib) y, solo si
se quiere el motor de reproducción real, GStreamer 1.x con PyGObject del sistema.

## 4. VM Ubuntu SERVIDOR (192.168.1.132) — el reparto de vídeo

| Componente | Valor (informe 05/08/2026) |
|---|---|
| SO | Ubuntu 20.04.6 LTS, kernel 5.15.0-139 (clon de la misma VM base que el cliente) |
| Recursos | 6 vCPU, 8 GB RAM, disco 99 GB (78 GB usados) |
| Servidor web | **Apache 2.4.41 (Ubuntu)**, activo como servicio, sirviendo estáticos desde `/var/www/html/dash` (13 GB) |
| Herramientas de generación | **ffmpeg 4.2.7** (codificación) + **MP4Box de GPAC 2.5-DEV vía Docker** (imagen `jjlin/gpac`; por eso MP4Box no está instalado nativo) |

### 4.1 Contenido alojado (verificado en el servidor)

- 2 contenidos × 2 duraciones × 2 framerates = **8 vídeos**: Paseo de Almuñécar
  (grabación propia 1080p; fuentes de 637 MB/728 MB) y Blender Sunflower
  (película abierta) en 10 min y 1 min, a 30 y 60 fps.
- Cada vídeo tiene: el `.mp4` fuente, la carpeta `_reps_<video>/` con las 6
  representaciones codificadas (`<video>_<res>_<bitrate>k.mp4`), y los
  empaquetados `2sec/` y `4sec/` (el experimento usa **4 s**).
- Escalera de 6 representaciones (del MPD, exacta):

| id | Resolución | Codec (perfil H.264) | Bitrate |
|---|---|---|---|
| 6 | 256×144 | avc1.64000C | 300 kbps |
| 5 | 426×240 | avc1.640015 | 750 kbps |
| 4 | 640×360 | avc1.64001E | 1200 kbps |
| 3 | 854×480 | avc1.64001F | 1850 kbps |
| 2 | 1280×720 | avc1.64001F | 2850 kbps |
| 1 | 1920×1080 | avc1.640032 | 4300 kbps |

### 4.2 Cómo se generó el contenido (proceso real, scripts en `scripts/servidor/` del repo)

Proceso en tres pasos con dos scripts bash propios (versionados en el repo:
`scripts/servidor/herramienta_video.sh` y `scripts/servidor/generar_dash_lote.sh`):

**Paso 0 — Preparación de los másteres (`herramienta_video.sh`, interactivo,
ffmpeg):** a partir de las fuentes (grabación propia de Paseo de Almuñécar y la
película abierta Blender Sunflower): recorte a 10 min / 1 min
(`ffmpeg -ss INICIO -t DURACION`), conversión a 30 fps de las variantes
(`ffmpeg -r 30`, las versiones 30fps salen del máster 60fps) y normalización a
MP4 H.264 limpio (libx264, `-pix_fmt yuv420p`, `+faststart`). Resultado: los 8
másteres `<video>.mp4`, uno por carpeta.

**Paso 1 — Codificación de las 6 representaciones (`generar_dash_lote.sh`,
ffmpeg/libx264):** el script recorre carpeta por carpeta, detecta los FPS con
`ffprobe` y genera la escalera en orden mayor→menor (por eso los ids del MPD son
1=1080p … 6=144p):

```bash
ffmpeg -y -i MASTER.mp4 \
  -vf "scale=W:H:force_original_aspect_ratio=decrease,pad=W:H:(ow-iw)/2:(oh-ih)/2,setsar=1,setdar=16/9" \
  -c:v libx264 -preset slow -profile:v high -pix_fmt yuv420p \
  -b:v BRk -maxrate BRk -bufsize $((2*BR))k \
  -x264-params keyint=$((FPS*2)):min-keyint=$((FPS*2)):scenecut=0 \
  -movflags +faststart -an \
  _reps_<video>/<video>_<H>p_<BR>k.mp4
```

Claves: sin audio (`-an`); control de tasa VBR con tope
(`-b:v`+`-maxrate`+`-bufsize 2×`) — por eso los segmentos tienen tamaños VBR
reales y no CBR exacto, el hecho que explota el controller; GOP fijo de 2 s
(`keyint=2×FPS`, `scenecut=0`) para que cada corte de segmento (2 s y 4 s)
caiga en keyframe; preset `slow` (calidad de codificación).

**Paso 2 — Empaquetado DASH (mismo script, MP4Box/GPAC 2.5-DEV vía Docker
`jjlin/gpac`), con el bandwidth FORZADO por entrada** — así el MPD anuncia
exactamente 300000…4300000 bps:

```bash
sudo docker run --rm -u "$(id -u)":"$(id -g)" -v "$(pwd)":/data jjlin/gpac:latest MP4Box \
  -dash 4000 -frag 4000 -rap \
  -profile live -bs-switching no -segment-ext m4s \
  -segment-name 'chunk_$Bandwidth$bps/<video>_4s' \
  -init-seg     'chunk_$Bandwidth$bps/<video>_4s_init.mp4' \
  -out /data/4sec/<video>_simple_4s.mpd \
  /data/_reps_<video>/<video>_1080p_4300k.mp4#video:bandwidth=4300000 \
  ... (las 6 reps, cada una con su #video:bandwidth=...)
```

Resultado: MPD **estático**, perfil `urn:mpeg:dash:profile:isoff-live:2011`,
`SegmentTemplate` con `$Bandwidth$` y `$Number$` (timescale 15360, duration
61440 = 4.000 s exactos), un directorio `chunk_<bps>bps/` por representación con
su init `.mp4` y sus segmentos `.m4s`. El atributo generator del MPD confirma la
herramienta: *"MPD file Generated with GPAC version 2.5-DEV"* (17/02/2026). Se
generó también la variante de 2 s (no usada en el resultado final).

**Publicación:** mover a `/var/www/html/dash/<video>/` — Apache lo sirve como
estático sin configuración especial. Comprobación desde el cliente:
`curl -I http://192.168.1.132/dash/<video>/4sec/<video>_simple_4s.mpd`.

**Medición de los tamaños reales:** `scripts/extraer_tamanos_reales_segmentos.py`
(repo, se ejecuta en el cliente) descarga el MPD, recorre todos los segmentos por
HTTP y escribe `media_profiles/segment_sizes/<video>.json` (bytes reales por
segmento y representación, `vbr_cv_max` hasta ~0.16) — la tabla que usan el
dataset y el planner.

## 5. WSL2 — el banco de entrenamiento GPU

| Componente | Valor (informe 05/08/2026) |
|---|---|
| Distribución | Ubuntu 24.04.4 LTS (noble), kernel 6.6.114.1-microsoft-standard-WSL2 |
| Recursos | 20 hilos visibles, 15 GB RAM, disco virtual 1 TB |
| GPU | AMD Radeon RX 7800 XT expuesta vía `/dev/dxg` |
| Stack GPU | ROCm 7.2.1 (en `/opt/rocm-7.2.1`, con `amdsmi`) |
| Python | 3.12.3 |
| Entorno virtual | `~/venvs/rocm721` |
| PyTorch | **2.9.1+rocm7.2.1** (wheels locales de `~/wheels/rocm721`, con sha256) + torchvision 0.24.0 + torchaudio 2.9.0 + triton 3.5.1 |
| numpy | 1.26.4 |
| Comprobación | `torch.cuda.is_available()` → True; device = "AMD Radeon RX 7800 XT" |

Rol: generar el dataset de entrenamiento (rollouts closed-loop con física VBR
real) y entrenar los predictores (MLP v1; ensemble de 5 GRUs v2, ~80 épocas,
pinball loss). Exporta los bundles con sha256 que luego carga el cliente.

## 6. El software del experimento (el repo)

- **Lenguaje:** Python puro; sin frameworks. Tests: `unittest` (489). IDE de
  desarrollo: PyCharm Community (Windows).
- **Dependencias de ejecución mínimas:** `requests`; PyTorch solo para los
  controllers IA; GStreamer opcional (motor real).
- **Dependencias de análisis:** numpy, pandas, matplotlib (gráficas Phase 6).
- **Motores de reproducción:** `fake` (avance de tiempo de media controlado,
  sin decodificar; el usado en TODA la evaluación formal — hace el experimento
  independiente del rendimiento gráfico de la VM) y GStreamer (reproducción
  real, usada en smokes de verificación).
- **Emulación de red:** `core/trace_replay/` reproduce una ventana de 300 s de
  una traza normalizada limitando el ancho de banda por intervalos; política de
  fin `fail`; decisión ABR cada segmento (4 s).
- **GUI de experimentos:** `scripts/gui_fase6.py` (tkinter, sin dependencias).

## 7. Formatos y contratos de datos (exactos)

| Dato | Formato |
|---|---|
| Traza de red normalizada | CSV `timestamp_s,duration_s,throughput_kbps` |
| Manifest del corpus | JSON `phase3_trace_manifest_curated.json`: 6768 trazas (1024 sintéticas), split por `leakage_group`, eval reservado |
| Contenido DASH | MPD estático perfil isoff-live + `SegmentTemplate`; inits `.mp4` y segmentos `.m4s` de 4 s en `chunk_<bps>bps/`; vídeo H.264 (libx264, perfil high), sin audio |
| Tamaños VBR | JSON `media_profile_segment_sizes_v1` (bytes reales por segmento × representación) |
| Bundle de modelo | Carpeta con checkpoint torch (`weights_only`), config del modelo, normalización, config del planner y `manifest.json` con sha256 de cada fichero |
| Telemetría de sesión | `segment_telemetry.csv` (fila por segmento: bitrate, buffer, stall, tiempos de descarga, auditoría de inferencia neural) |
| Paquete de evidencia | `00_protocolo / 01_ejecucion / 02_resultados / 03_graficas / 04_informe` |
| QoE | `qoe_linear_v1`: `bitrate_mbps − 4.3·rebuffer_s − |Δbitrate_mbps|`, media por sesión |

## 8. Flujo completo (quién produce qué)

```text
[Servidor]  máster .mp4 → ffmpeg/libx264 (6 reps VBR) → MP4Box/GPAC en Docker
            (segmentos 4s + MPD) → Apache /var/www/html/dash
[Cliente]   extraer_tamanos_reales_segmentos.py → media_profiles/*.json (repo)
[WSL]       manifest + trazas phase3 → dataset multimedia (rollouts VBR)
            → entrenar v1 (MLP) y v2 (ensemble 5×GRU) → bundles con sha256
[Cliente]   bundles + trazas eval + MPDs → Phase 6 tfg_final (360 sesiones)
            → paquete de evidencia → números y gráficas de la memoria
[Windows]   desarrollo (PyCharm + git), tests (489), memoria del TFG
```

## 9. Herramientas usadas — lista completa

| Herramienta | Versión | Para qué |
|---|---|---|
| Python | 3.8.10 (cliente/servidor) · 3.12.3 (WSL) · 3.12.8 (Windows) | Todo el software del proyecto |
| PyTorch | 2.4.1 (cliente, inferencia CPU) · 2.9.1+rocm7.2.1 (WSL, entrenamiento GPU) | Modelos IA |
| ROCm | 7.2.1 | GPU AMD en WSL |
| ffmpeg / libx264 | 4.2.7 | Codificar las 6 representaciones VBR |
| GPAC / MP4Box | 2.5-DEV (Docker `jjlin/gpac`) | Empaquetado DASH (segmentos + MPD) |
| Docker | (en el servidor) | Ejecutar el MP4Box moderno sin instalarlo |
| Apache | 2.4.41 | Servir MPD y segmentos por HTTP |
| GStreamer + PyGObject | 1.16.3 / 3.36.0 | Motor de reproducción real (opcional) |
| requests | 2.22.0 | Descargas HTTP del cliente |
| numpy / pandas / matplotlib | 2.2.6 / 2.3.1 / (analysis) | Análisis y 16 gráficas de Phase 6 |
| unittest (stdlib) | — | Suite de 489 tests |
| tkinter (stdlib) | — | GUI de lanzamiento de experimentos |
| VirtualBox | 7.0.14 | VMs cliente y servidor (red puente) |
| WSL2 | 2.7.3 | Ubuntu con GPU para entrenar |
| git + GitHub | — | Versionado y puente entre máquinas |
| OpenSSH (scp) | 8.2p1 | Transferencia de artefactos entre máquinas |
| PyCharm Community | — | IDE de desarrollo en Windows |

Trazabilidad: los dos scripts de generación reales están versionados en
`scripts/servidor/` del repo. Su salida cuadra con lo observado en el servidor:
el naming de las representaciones (`<video>_<H>p_<BR>k.mp4` en las carpetas
`_reps_*`), los bandwidth exactos del MPD (forzados por entrada), el generator
GPAC 2.5-DEV y la estructura `chunk_<bps>bps/` + `2sec/`/`4sec/`. Los scripts
del Escritorio del servidor (`generate_dash.sh`, `auto_dash_resume.sh`,
`pack_walk_docker.sh`, escalera de 20 niveles "tipo Bunny") son iteraciones
previas, legacy.

# Componentes del experimento — hardware, software, red y formatos (todo, exacto)

Fecha: 2026-08-05. Propósito: sección de referencia para la memoria y la defensa:
QUÉ máquinas, QUÉ software con QUÉ versiones, QUÉ formatos y CÓMO se conecta todo.
Los huecos marcados `[PENDIENTE: informe <máquina>]` se completan con la salida de
`scripts/recopilar_info_entorno.sh` ejecutado en cada máquina (no se inventa nada).

---

## 1. Topología general

Un único PC físico (Windows) aloja TODO el experimento: dos máquinas virtuales
VirtualBox (cliente y servidor, en red puente con el router doméstico) y un WSL2
para el entrenamiento GPU. No hay red real en las mediciones: las condiciones de
red se EMULAN reproduciendo trazas (replay determinista); el HTTP entre cliente y
servidor solo transporta los bytes del vídeo.

```text
PC físico (Windows 11)
├── VirtualBox 7.0.14
│   ├── VM Ubuntu CLIENTE  (192.168.1.160) — ejecuta el cliente DASH y Phase 6
│   └── VM Ubuntu SERVIDOR (192.168.1.132) — sirve MPD + segmentos por HTTP
├── WSL2 (2.7.3) Ubuntu 24.04 — entrenamiento IA con GPU AMD (ROCm)
└── Windows nativo — desarrollo, tests rápidos, git, memoria del TFG
        └── GitHub (DNLPRTL/ClienteDashTFG) = puente de código entre todos
```

## 2. Host físico (Windows) — verificado

| Componente | Valor |
|---|---|
| SO | Windows 11 Home 10.0.26200 |
| CPU | Intel Core i5-14600KF (14 núcleos / 20 hilos) |
| RAM | 32 GB |
| GPU | AMD Radeon RX 7800 XT (la usa WSL2/ROCm para entrenar) |
| Placa | ASUS ROG STRIX Z690-A GAMING WIFI |
| Python (Windows) | 3.12.8 |
| VirtualBox | 7.0.14 |
| WSL | 2.7.3.0 (kernel 6.6.114.1-1) |

## 3. VM Ubuntu CLIENTE (192.168.1.160) — el banco de pruebas

- **Rol:** único entorno donde se ejecuta lo que cuenta: el cliente DASH real,
  los 6 controllers y la evaluación formal Phase 6 (las 360 sesiones del
  resultado final salieron de aquí).
- **SO / hardware asignado:** `[PENDIENTE: informe cliente]` (SO, CPU/RAM/disco
  asignados por VirtualBox, versión de Python; nota conocida: su Python es 3.8.x,
  lo que motivó el arreglo de compatibilidad del 05/08/2026).
- **Software necesario para replicar (lo que hubo que instalar):**
  - Python 3 + `pip install -r requirements.txt` del repo (mínimo: `requests`).
  - PyTorch (CPU) — para cargar los bundles y ejecutar la inferencia de v1/v2.
  - GStreamer + PyGObject (paquetes del sistema) — SOLO para el motor de
    reproducción real; **Phase 6 usa el motor `fake`** (sin decodificar vídeo),
    así que para replicar el experimento formal no es imprescindible.
  - Versiones exactas instaladas: `[PENDIENTE: informe cliente — pip freeze + dpkg]`.
- **Material local:** `~/TFG/ClienteDashTFG` (repo) + `~/TFG/manifests_trazas`,
  `~/TFG/datasets_normalizados/phase3`, `~/TFG/modelos/mpc_prudente`,
  `~/TFG/runs_trazas/phase6/...` (evidencia). Config local:
  `config/phase6.local.json` (rutas + URLs del servidor).

## 4. VM Ubuntu SERVIDOR (192.168.1.132) — el reparto de vídeo

- **Rol:** servir por HTTP el contenido DASH desde `/var/www/html/dash`. NO
  ejecuta nada del experimento ni define la red (eso lo hace el replay de trazas
  en el cliente).
- **Servidor web y SO:** `[PENDIENTE: informe servidor — apache/nginx + versión, SO]`.
- **Contenido alojado** (verificado desde el cliente y las tablas VBR del repo):
  2 contenidos (Paseo de Almuñécar — grabación propia— y Blender Sunflower) ×
  2 duraciones (10 min y 1 min) × 2 framerates (30 y 60 fps) = 8 perfiles, cada
  uno con MPD estático (`*_simple_4s.mpd`), 1 init por representación y
  segmentos `.m4s` de 4 s. Escalera de 6 representaciones:
  **300 / 750 / 1200 / 1850 / 2850 / 4300 kbps, codificación VBR** (los tamaños
  reales por segmento están extraídos en `media_profiles/segment_sizes/*.json`;
  variabilidad medida `vbr_cv_max` hasta ~0.16 en Blender 60fps).
  Conteos de segmentos (10 min): Paseo 30fps = 151, Paseo 60fps = 150,
  Blender 30fps = 151, Blender 60fps = 159.
- **Cómo se generaron los MPD y segmentos:** `[PENDIENTE: informe servidor —
  el script recoge las versiones de ffmpeg/MP4Box, el MPD completo (su atributo
  generator delata la herramienta) y los scripts de generación que haya en la
  máquina; con eso se documentan aquí los comandos exactos]`.
- **Extracción de tamaños reales:** `scripts/extraer_tamanos_reales_segmentos.py`
  (del repo) recorre el servidor por HTTP y escribe las tablas VBR versionadas.

## 5. WSL2 — el banco de entrenamiento GPU

| Componente | Valor (verificado en docs del proyecto) |
|---|---|
| Distribución | Ubuntu 24.04.4 LTS en WSL2 |
| GPU | AMD Radeon RX 7800 XT vía `/dev/dxg` |
| Stack GPU | ROCm (rocminfo detecta la GPU) |
| PyTorch | 2.9.1+rocm7.2.1 |
| Entorno virtual | `~/venvs/rocm721` |
| Comprobación | `torch.cuda.is_available()` → True, device = RX 7800 XT |
| pip freeze completo | `[PENDIENTE: informe wsl]` |

- **Rol:** generar el dataset de entrenamiento (rollouts closed-loop sobre las
  trazas, con física VBR real) y entrenar los predictores (MLP v1; ensemble de
  5 GRUs v2). Exporta los bundles con sha256 que luego carga el cliente.
- **Material local:** repo + `~/TFG/datasets_normalizados/phase3` (trazas) +
  `~/TFG/datasets_normalizados/mpc_prudente/throughput_quantile_full_v1_multimedia`
  (dataset final) + `~/TFG/modelos/mpc_prudente` (entrenamientos y bundles).

## 6. El software del experimento (el repo)

- **Lenguaje:** Python puro (sin frameworks web); tests con `unittest` (489).
- **Dependencias de ejecución:** mínimas a propósito — `requests` (descargas
  HTTP); PyTorch solo para los controllers IA; GStreamer opcional (motor real).
- **Dependencias de análisis** (`requirements-analysis.txt`): numpy, pandas,
  matplotlib (gráficas de Phase 6).
- **Motores de reproducción:** `fake` (avanza el tiempo de media de forma
  controlada; el usado en TODA la evaluación formal) y GStreamer (reproducción
  real, usada solo en smokes de verificación).
- **Emulación de red:** `core/trace_replay/` reproduce una ventana de 300 s de
  una traza normalizada, limitando el ancho de banda por intervalos; política de
  fin `fail`, timestamps compactados, decisión cada segmento (4 s).

## 7. Formatos y contratos de datos (exactos)

| Dato | Formato |
|---|---|
| Traza de red normalizada | CSV con cabecera `timestamp_s,duration_s,throughput_kbps` |
| Manifest del corpus | JSON (`phase3_trace_manifest_curated.json`): 6768 trazas, campos de split/leakage_group/buckets; eval reservado |
| Contenido DASH | MPD estático (perfil "simple", plantilla de segmentos), inits `.mp4`, segmentos `.m4s` de 4 s |
| Tamaños VBR | JSON `media_profile_segment_sizes_v1` (bytes reales por segmento y representación) |
| Bundle de modelo | Carpeta con checkpoint torch (`weights_only`), config, normalización, config del planner y `manifest.json` con sha256 de cada fichero |
| Telemetría de sesión | `segment_telemetry.csv` (una fila por segmento: bitrate, buffer, stall, tiempos, auditoría neural) |
| Paquete de evidencia | `00_protocolo / 01_ejecucion / 02_resultados / 03_graficas / 04_informe` |
| QoE | `qoe_linear_v1`: `bitrate_mbps − 4.3·rebuffer_s − |Δbitrate_mbps|`, media por sesión |

## 8. Flujo completo (quién produce qué)

```text
[Servidor] vídeos fuente → (herramienta [PENDIENTE]) → MPD + inits + .m4s (VBR, 4s)
[Repo]     extraer_tamanos_reales_segmentos.py → media_profiles/segment_sizes/*.json
[WSL]      trazas phase3 + manifest → dataset multimedia → entrenar v1/v2 → bundles (sha256)
[Cliente]  bundles + trazas eval + MPDs del servidor → Phase 6 tfg_final (360 sesiones)
           → paquete de evidencia → números y gráficas de la memoria
```

---

**Cómo completar los `[PENDIENTE]`:** ejecutar en cada máquina
`bash scripts/recopilar_info_entorno.sh <cliente|servidor|wsl>` y volcar aquí las
salidas (`~/info_entorno_<etiqueta>.txt`).

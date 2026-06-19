# Decisión — "MPC Neuronal Prudente": paso 0 (fidelidad al medio real)

| Campo | Valor |
|---|---|
| Fecha | 2026-06-19 |
| Autor | Claude (Claude Code) |
| Rama | `rebuild/phase3-from-phase2` |
| Plan padre | `plan_maestro_controller_ia_claude_20260619.md` |
| Estado | Paso 0 implementado (extractor). Pendiente: ejecución en Ubuntu cliente. |

## Nombre humano de la línea (sustituye al técnico `phase45_v4`)

- **Controller: "MPC Neuronal Prudente".** Es un planificador MPC (decide el
  bitrate mirando el futuro) cuyo cerebro de predicción es una red neuronal que
  estima el ancho de banda futuro **con incertidumbre**, y que decide de forma
  **prudente** (evita lanzarse a calidades altas si hay riesgo de corte),
  planificando con el **peso real (VBR)** de cada segmento de vídeo.
- **Clave corta para código:** `mpc_prudente`.
- Dos innovaciones que lo hacen defendible: (1) **fiel-al-vídeo** (entrena y
  planifica con los tamaños reales del MPD, no CBR); (2) **prudente** (objetivo
  consciente del riesgo sobre la cola mala del throughput).

> Nombre provisional: Daniel puede renombrar. No bloquea el paso 0 (que es
> name-neutral: solo extrae datos del medio).

## Decisiones acordadas con Daniel

1. **Reconstrucción fiel directa.** No se hace la "foto antes" de v2; se deja
   anotado como pendiente para la memoria. Prioridad: cerrar el TFG.
2. **Cobertura de medio: los 8 perfiles de 4 s** (`Paseo`/`Blender` ×
   `10min`/`1min` × `30fps`/`60fps`). Las versiones de 2 s se obvian. Meta: que el
   controller funcione apuntando a cualquiera de esos MPD (distintos contenidos,
   fps y pesos VBR reales), como en la realidad.
3. **Tabla de medio commiteada** como descriptor versionado (pequeña).
4. Nombres humanos (arriba).

## Paso 0 implementado

- `scripts/extraer_tamanos_reales_segmentos.py`: parsea cada MPD (representations,
  SegmentTemplate, duración) y lee el `Content-Length` real de cada `.m4s` →
  tabla `segmento N → bytes` por representación + evidencia VBR
  (`segment_bytes_cv`, `real_mean_vs_cbr_ratio`). Salida JSON en
  `media_profiles/segment_sizes/<perfil>.json`. Solo HTTP, sin descargar el vídeo
  salvo respaldo si falta `Content-Length`.
- `scripts/extraer_tamanos_reales_segmentos_ubuntu_cliente.sh`: runbook que
  sincroniza, comprueba acceso al servidor, ejecuta el extractor y sube los
  descriptores por git.
- `media_profiles/README.md`: documenta el formato y por qué se versiona.

## Cómo ejecutar (Daniel, Ubuntu cliente)

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/extraer_tamanos_reales_segmentos_ubuntu_cliente.sh
```

Pegar la línea final `SEGMENT_SIZE_EXTRACTION status=...` y una o dos líneas
`media_profile=...`.

## Siguiente paso (cuando lleguen los datos)

Diseñar el contrato del **dataset de entrenamiento fiel** que consume estas
tablas (medio VBR real) + el corpus de trazas curado (red), para `mpc_prudente`.

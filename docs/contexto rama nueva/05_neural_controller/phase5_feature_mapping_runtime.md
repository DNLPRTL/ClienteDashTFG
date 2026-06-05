# Phase 5 - Feature mapping runtime

## Regla principal

El feature builder runtime solo usa informacion disponible antes de pedir el
siguiente segmento. No usa metadata de traza, split, labels, QoE futuro ni
throughput futuro.

## Mapping de feedback a context features

| Feature Phase 4 | Fuente runtime | Regla |
|---|---|---|
| `throughput_history_bps` | descargas completadas | `8 * last_fragment_size / last_download_time`, con padding a 5 |
| `download_time_history_s` | descargas completadas | historial pasado, con padding a 5 |
| `buffer_s` | `queued_time` | buffer actual pre-decision |
| `last_representation_index` | `level` | clamp a la ladder actual |
| `last_bitrate_bps` | `rates[level] * 8` | conversion B/s a bps |
| `recent_rebuffer_s` | no disponible en feedback actual | `0.0`, limitacion documentada |
| `recent_switch_abs` | niveles observados | cambio absoluto reciente |
| `chunks_remaining_norm` | no disponible por defecto | `0.0` salvo exposicion segura futura |
| `has_chunks_remaining` | no disponible por defecto | `0.0` salvo exposicion segura futura |

## Candidate features

Para cada rate actual del MPD:

- `candidate_representation_index`: posicion de la representacion.
- `candidate_bitrate_bps`: `rate_Bps * 8`.
- `candidate_ladder_position_norm`: posicion normalizada en la ladder.
- `candidate_bitrate_norm_ladder`: bitrate normalizado dentro de la ladder.
- `candidate_delta_from_last_bitrate_norm`: diferencia frente al ultimo bitrate.
- `candidate_chunk_size_bytes`: `rate_Bps * fragment_duration_s`.
- `candidate_chunk_size_available`: `1.0`, porque replica la estimacion
  bitrate-duracion usada por el ladder sintetico de Phase 4.

## Campos prohibidos

Si el feedback contiene alguno de los campos prohibidos por Phase 4, el builder
falla cerrado antes de construir el vector.

Ejemplos:

```text
trace_id
dataset_id
split
leakage_group
future_throughput
future_qoe
teacher_action
benchmark_rank
```


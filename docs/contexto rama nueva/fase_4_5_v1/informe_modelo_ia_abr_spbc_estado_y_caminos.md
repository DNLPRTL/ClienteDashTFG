# Informe de estado para construir el controller IA ABR

Fecha: 2026-06-11.

Estado de uso: documento tecnico previo a integrar controller. Este informe no
es un benchmark, no contiene ranking formal y no autoriza afirmar mejora de QoE
frente a baselines. Su funcion es congelar lo que sabemos antes de decidir el
siguiente movimiento de Fase 4-5 v1 y Phase 6.

## 1. Resumen ejecutivo

Tenemos una base bastante mas solida que al inicio: corpus curado, contrato QoE
cerrado, replay tecnico, datasets de preferencias on-policy, oracle offline,
modelo SPBC v2 con DPO y cabezas auxiliares, gates de seguridad y un candidato
aceptado offline. Lo que no tenemos todavia es una validacion comparativa formal
ejecutada como Phase 6 ni un controller IA integrado que haya pasado el cliente
real bajo protocolo congelado.

El modelo aceptado actualmente es:

```text
model_key=spbc_abr_v2_dpo
run=full_v2_anchor_safe_rank_v1
checkpoint=/home/danie/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt
sha256=43b4d012448e12885fac8cbfec914aab6450e0c1b146a4bb8534e8b90b61c227
```

Su significado correcto es: mejor candidato offline disponible para pasar a
integracion controlada. No significa que ya gane, ni que generalice, ni que sea
el controller final del TFG.

La evidencia acumulada dice una cosa importante: cuando intentamos mejorar el
SPBC empujando agresividad, PPO o ventaja segura, el entrenamiento encuentra
formas de bajar unas metricas internas pero rompe utilidad, rebuffer u
over-aggressive en los buckets criticos. El problema no parece ser solo "falta
entrenar mas"; parece ser un problema de decision bajo distribucion, trade-off
de seguridad/utilidad y desalineacion entre surrogate offline y lo que luego
queremos defender en Phase 6.

Mi lectura tecnica es:

- No conviene seguir gastando horas en variantes ciegas de loss antes de ver el
  controller integrado.
- El camino mas defendible ahora es integrar el anchor SPBC v2, ejecutar Phase 6
  con protocolo formal y usar los resultados reales para decidir si hace falta
  un segundo ciclo: especialista por regimen, hibrido SPBC+SPC o predictor mas
  planificador.
- SPC no queda "descartado para siempre"; queda descartado como reemplazo
  directo no probado del SPBC. Puede tener sentido como critico/copiloto o como
  predictor en un sistema hibrido, pero no debe desplazar el anchor sin evidencia
  nueva.

## 2. Separacion de fases y prohibiciones

El proyecto esta en la rama:

```text
rebuild/phase3-from-phase2
```

Las fases cerradas no deben reinterpretarse:

- Phase 1 y Phase 2 estan cerradas.
- Phase 3 Rebuild esta cerrada con corpus externo, auditoria de calidad, replay
  tecnico y manifest curado.
- Phase 3.5 Rebuild esta cerrada con contrato `qoe_linear_v1`, calculadora QoE
  pura, postprocesador QoE, gates y smokes sinteticos controlados.
- Phase 4 Rebuild esta cerrada con dos bundles offline `NeuralABR-Lite`, uno
  entrenado con `robust_mpc` real y otro con `teacher_hibrido`.
- Phase 5 esta cerrada con dos controllers IA integrados.
- La verificacion de cliente y controllers clasicos esta cerrada.
- Phase 6 esta preparada para evaluacion comparativa formal, pero sus smokes,
  preflights y diagnosticos no son benchmark si el preset no lo autoriza.

Fase 4-5 v1 es una iteracion nueva e independiente para crear controllers IA
nuevos. No sustituye automaticamente a Phase 4 ni Phase 5 cerradas y no hereda
sin debate las decisiones de `NeuralABR-Lite`.

Prohibiciones relevantes:

- No llamar benchmark a smoke tests, dry-runs, conversiones ni auditorias.
- No declarar mejora de QoE, ranking, ganador ni generalizacion antes de Phase 6
  formal.
- No entrenar ni evaluar usando columnas prohibidas como `trace_id`, `dataset_id`,
  `split`, `source_id`, `group_id`, `leakage_group`, etiquetas OOD, throughput
  futuro o resultados de oracle como input del modelo.
- No mezclar dataset, trazas, modelos, logs, runs y bundles pesados dentro del
  repositorio.

## 3. Maquinas, rutas y hardware disponible

### 3.1 Windows

Windows es el entorno de desarrollo, test rapido, documentacion, commits y push.
El repositorio local esta en:

```text
C:\Users\danie\Documents\TFG\DashClientModular4
```

Las rutas externas pesadas en Windows son:

```text
C:\Users\danie\Documents\TFG\dataset en bruto
C:\Users\danie\Documents\TFG\datasets_normalizados
C:\Users\danie\Documents\TFG\manifests_trazas
C:\Users\danie\Documents\TFG\runs_trazas
C:\Users\danie\Documents\TFG\auditorias_trazas
C:\Users\danie\Documents\TFG\modelos
```

### 3.2 WSL2 / ROCm

El entrenamiento pesado IA se hace en WSL2 Ubuntu con ROCm:

```text
Distribucion: Ubuntu-24.04 en WSL2
Venv GPU: ~/venvs/rocm721
Torch observado: 2.9.1+rocm7.2.1
GPU observada: AMD Radeon RX 7800 XT
Repo recomendado: ~/TFG/DashClientModular4
Raiz pesada recomendada: ~/TFG
```

La GPU AMD Radeon RX 7800 XT es el recurso que permite entrenamientos de varias
horas con PyTorch ROCm. En este proyecto ya se ha observado que una ejecucion
multi-seed puede costar aproximadamente una hora por seed, asi que cualquier
experimento nuevo tiene que estar justificado por evidencia y no por intuicion.

Regla operativa importante: no usar `/mnt/c/Users/danie/Documents/TFG/...` como
ruta principal de entrenamiento. Datasets, checkpoints, modelos, logs y runs
deben vivir bajo rutas Linux en `~/TFG`.

### 3.3 Ubuntu cliente

La VM Ubuntu cliente ejecuta validaciones relevantes y Phase 6. Windows y WSL2
no sustituyen la validacion formal del cliente.

### 3.4 Ubuntu servidor

El servidor solo sirve MPD, inicializaciones y segmentos DASH. No define la red
experimental ni decide el benchmark.

## 4. Servidor DASH, MPD, videos y fragmentos

El servidor DASH observado en la documentacion tecnica es:

```text
IP servidor: 192.168.1.132
Base URL: http://192.168.1.132/dash/
Raiz servidor: /var/www/html/dash
```

Inventario relevante:

- 16 MPDs.
- 6 representaciones por MPD.
- Segmentacion principal de 4 segundos.
- Escalera comun:

```text
300000 bps
750000 bps
1200000 bps
1850000 bps
2850000 bps
4300000 bps
```

Equivalente en kbps:

```text
300, 750, 1200, 1850, 2850, 4300
```

Videos/directorios disponibles:

```text
Blender_Sunflower_10min_30fps
Blender_Sunflower_10min_60fps
Blender_Sunflower_1min_30fps
Blender_Sunflower_1min_60fps
Paseo_Almunecar_10min_30fps
Paseo_Almunecar_10min_60fps
Paseo_Almunecar_1min_30fps
Paseo_Almunecar_1min_60fps
```

Tamanos de videos fuente documentados:

```text
Blender 10min 30fps: 263.34 MiB
Blender 10min 60fps: 339.37 MiB
Blender 1min 30fps: 25.57 MiB
Blender 1min 60fps: 29.33 MiB
Paseo 10min 30fps: 607.21 MiB
Paseo 10min 60fps: 693.87 MiB
Paseo 1min 30fps: 52.61 MiB
Paseo 1min 60fps: 59.46 MiB
```

MPD principal usado por el perfil base de entrenamiento/evaluacion:

```text
http://192.168.1.132/dash/Paseo_Almunecar_10min_30fps/4sec/Paseo_Almunecar_10min_30fps_simple_4s.mpd
```

Ese perfil representa:

```text
media_profile_id=paseo_10min_30fps_4s
duracion ~= PT0H10M0.100S
segment_duration_s=4.0
fps=30
diagnostic_only=false
```

El perfil de entrenamiento offline usa una escalera sintetizada desde bitrate y
duracion de segmento. La formula de tamano de segmento es:

```text
segment_size_bytes = round(bitrate_bps * segment_duration_s / 8.0)
```

Con 4 segundos, los tamanos aproximados por representacion son:

```text
300 kbps  -> 150000 bytes
750 kbps  -> 375000 bytes
1200 kbps -> 600000 bytes
1850 kbps -> 925000 bytes
2850 kbps -> 1425000 bytes
4300 kbps -> 2150000 bytes
```

Esto importa porque el modelo no esta aprendiendo sobre un video abstracto:
aprende a decidir entre seis acciones con tamanos de segmento coherentes con los
MPD reales de 4 segundos.

## 5. Corpus de trazas Phase 3

La unidad canonica de throughput normalizado es:

```text
throughput_kbps
```

El schema de traza normalizada es:

```csv
timestamp_s,duration_s,throughput_kbps
```

Manifest curado canonico:

```text
C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\phase3_trace_manifest_curated.json
/home/danie/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json
```

Resumen observado del manifest curado:

```text
schema_id=phase3_trace_manifest_final_v1
artifact_set=final_with_synthetic_controlled_quality_curated
trace_count=6768
train=4725
eval=1025
test=1018
synthetic_trace_count=1024
synthetic_split_counts=train:720,test:152,eval:152
duration_min_s~=30.801
duration_max_s~=32962.955
```

Distribucion por `dataset_id`:

```text
fcc_measuring_broadband_america: 4174
synthetic_controlled_network: 1024
roma_4g_nbiot_5g_nsa: 438
oboe: 427
ucc_4g_lte_beyond_throughput: 135
gavist5g: 122
lumos5g: 118
puffer_stanford: 93
norway_hsdpa_umass: 86
ucc_5g_beyond_throughput: 83
ghent_4g_lte: 40
nyu_mets: 28
```

Distribucion por semantica:

```text
active_fixed_broadband_download_test: 4174
synthetic_available_bandwidth: 1024
available_bandwidth: 917
active_mobile_speedtest: 438
observed_application_traffic: 122
real_streaming_delivery_rate: 93
```

Distribucion por condicion:

```text
usable_network_trace: 6324
low_bandwidth_network: 297
high_or_extreme_throughput_network: 107
severe_or_intermittent_network: 40
```

Lectura importante: hay muchas trazas, pero no todas significan exactamente lo
mismo. FCC, Puffer y GAViST no deben tratarse sin control como equivalentes a
ancho de banda disponible puro. Por eso el sampler y las auditorias conservan
semanticas, buckets y restricciones de cuota.

## 6. Splits y contaminacion

Los splits `train`, `test` y `eval` se hacen por `leakage_group` o grupo
semantico, no por filas. Esto evita que ventanas casi equivalentes caigan en
train y validacion.

El modelo no puede ver:

```text
trace_id
dataset_id
source_id
split
group_id
leakage_group
OOD label
futuro throughput
metadata del manifest
acciones/resultados del oracle como input
resultados per-action como input
```

El uso autorizado de futuro/oracle queda limitado a construir etiquetas,
preferencias y auditorias. No entra al forward del modelo.

## 7. Dataset Fase 4-5 v1/v2

La iteracion nueva Fase 4-5 v1 parte del corpus operativo en:

```text
docs/contexto rama nueva/fase_4_5_v1/abr ia md/
```

Los datasets relevantes creados para SPBC v2 son:

```text
phase45v2_preference_onpolicy_dataset_v1
phase45v2_preference_onpolicy_dagger2_dataset_v1
```

Ruta externa WSL del dataset DAgger-2:

```text
/home/danie/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dagger2_dataset_v1
```

Inputs externos:

```text
/home/danie/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json
/home/danie/TFG/datasets_normalizados/phase3/final/
```

Archivos esperados en el dataset v2:

```text
datos_entrenamiento_preference_onpolicy_v2.jsonl
datos_validacion_preference_onpolicy_v2.jsonl
resumen_dataset_phase45_v2.json
plan_muestreo_phase45_v2.json
auditoria_muestreo_phase45_v2.json
esquema_model_inputs_phase45_v2.json
esquema_targets_phase45_v2.json
auditoria_no_contaminacion_phase45_v2.json
estadisticas_normalizacion_train_only_phase45_v2.json
auditoria_preferencias_phase45_v2.json
```

El dataset contiene estados por segmento, candidatos de accion, mascara de
acciones validas, accion de oracle, resultados por accion y pares de preferencia.

Fuentes de rollout relevantes:

```text
oracle_rollout
spbc_v1_on_policy
spbc_v2_dpo_on_policy
```

DAgger-2 anade rollout del modelo:

```text
spbc_abr_v2_dpo/full_v1_utility_risk_v1
```

Ese rollout se relabela con:

```text
oracle_qoe_beam_v1
```

La idea es combatir el problema clasico de compounding error: no entrenar solo
en estados perfectos de oracle, sino tambien en estados a los que llega la
politica aprendida.

## 8. Perfil de muestreo

Perfiles de dataset:

```text
smoke:
  train_window_count=24
  validation_window_count=8
  oracle_horizon_segments=3
  oracle_beam_width=4
  future_horizon_segments=3
  max_windows_per_trace=1
  synthetic_max_fraction=0.15
  dataset_max_fraction=0.50
  semantics_max_fraction=0.70
  seed=phase45_v1_smoke_dataset_seed

pilot:
  train_window_count=512
  validation_window_count=128
  oracle_horizon_segments=4
  oracle_beam_width=5
  future_horizon_segments=4
  max_windows_per_trace=3
  synthetic_max_fraction=0.15
  dataset_max_fraction=0.40
  semantics_max_fraction=0.55
  seed=phase45_v1_pilot_dataset_seed

full_v1:
  train_window_count=8192
  validation_window_count=2048
  oracle_horizon_segments=5
  oracle_beam_width=6
  future_horizon_segments=5
  max_windows_per_trace=4
  synthetic_max_fraction=0.15
  dataset_max_fraction=0.35
  semantics_max_fraction=0.50
  seed=phase45_v1_full_dataset_seed
```

Configuracion del sampler:

```text
segment_duration_s=4.0
window_duration_s=120.0
segment_count_per_window=30
media_profile_id=paseo_10min_30fps_4s
synthetic_max_fraction=0.15
```

Prioridad por bucket:

```text
lte_1_mbps: 5
1_2_mbps: 4
2_5_mbps: 3
5_20_mbps: 2
gt_20_mbps: 1
variable_trace_bonus=1
```

En ejecuciones full-samples de los runbooks se ha observado una escala del orden
de cientos de miles de muestras por source. Un dato observado y usado como
referencia operativa fue:

```text
training=557460
validation=128970
```

No debe confundirse ese numero con una constante del contrato: depende de
cuantos rollouts/estados/candidatos se materializan en el dataset concreto.

## 9. Contrato de input del modelo

El modelo solo consume:

```text
model_inputs.context
model_inputs.candidates
action_mask
```

Features secuenciales:

```text
throughput_history_bps
download_time_history_s
```

Features escalares:

```text
buffer_s
last_representation_index
last_bitrate_bps
recent_rebuffer_s
recent_switch_abs
chunks_remaining_norm
has_chunks_remaining
```

Features por candidato:

```text
candidate_representation_index
candidate_ladder_position_norm
candidate_bitrate_bps
candidate_bitrate_norm_ladder
candidate_delta_from_last_bitrate_norm
candidate_chunk_size_bytes
candidate_chunk_size_available
```

Longitud de historia por defecto:

```text
DEFAULT_CONTEXT_HISTORY_LENGTH=5
```

Campos presentes pero no autorizados como input:

```text
metadata
rollout_policy_action
rollout_policy_model_key
per_action_outcomes
reward_n
qoe_gap
rollout_source
preference_pairs
```

## 10. QoE, reward y oracle

La formula cerrada de la rama es:

```text
qoe_formula_version=qoe_linear_v1
reward_n = bitrate_mbps - 4.3 * rebuffer_s - smoothness_mbps
primary_session_metric=qoe_linear_mean
```

`qoe_log_v1` queda como metrica secundaria de sensibilidad.
`startup_delay_s` queda report-only.
VMAF queda aplazado por dependencia de artefactos.

Oracle:

```text
oracle_qoe_beam_v1
```

El oracle usa futuro solo para etiqueta. Su beam search prioriza:

1. mayor reward,
2. menor rebuffer,
3. menos cambios,
4. menor primera accion si persiste el empate.

Si algo falla, el fallback es la accion valida mas baja. Esto es deliberadamente
conservador.

La simulacion por paso usa:

```text
download_time_s = segment_size_bits / throughput_bps
rebuffer_s = max(download_time_s - buffer_s, 0)
buffer_after_s = min(max(buffer_s - download_time_s, 0) + segment_duration_s, max_buffer_s)
```

Con `max_buffer_s=20.0` en la ladder offline de entrenamiento.

## 11. Arquitectura SPBC v1

El SPBC v1 es una politica candidata con GRU:

```text
model_key=spbc_abr_v1
model_type=gru_candidate_policy
```

Bloques:

- GRU de historia con `sequence_dim=2`.
- Encoder de estado sobre 7 escalares.
- Encoder de candidato sobre 7 features por representacion.
- Tower compartida.
- Head de politica que produce un logit por candidato.
- Mascara de acciones invalidas con logit `-1e9`.

Forma conceptual:

```text
history_sequence -> GRU -> history_vector
scalar_context -> MLP -> state_vector
[history_vector,state_vector] -> shared MLP -> shared_state
candidate_features -> candidate MLP -> candidate_vector
[shared_state,candidate_vector] -> policy_head -> action_logit
```

El objetivo era imitar accion de oracle de forma segura, sin usar metadata ni
futuro como input.

## 12. Arquitectura SPBC v2 DPO

El modelo actual extiende SPBC v1:

```text
model_key=spbc_abr_v2_dpo
schema_id=phase45_v2_spbc_dpo_checkpoint_v1
model_type=gru_candidate_policy_with_auxiliary_utility_risk_heads
```

Ficheros canonicos:

```text
modelo_spbc_abr_v2_dpo.pt
reporte_entrenamiento_spbc_abr_v2_dpo.json
```

Bloques heredados:

- GRU de historia.
- Encoder de estado.
- Encoder de candidato.
- Tower compartida.
- Head de logits base.

Bloques nuevos:

- `reward_head`: predice reward normalizado por accion.
- `rebuffer_head`: predice rebuffer por accion, con sigmoid y cap.
- `risk_head`: predice riesgo objetivo por accion.

Las cabezas auxiliares se inicializan con peso final cero para no romper de
golpe el comportamiento inicial del SPBC base.

Fusion de decision:

```text
centered_reward = predicted_reward - mean_reward_valid_actions
fusion =
  decision_reward_fusion_weight * centered_reward
  - decision_rebuffer_fusion_weight * predicted_rebuffer_norm
  - decision_risk_fusion_weight * predicted_risk_probability

action_logits = base_action_logits + fusion
```

Pesos por defecto del perfil full:

```text
decision_reward_fusion_weight=0.12
decision_rebuffer_fusion_weight=0.30
decision_risk_fusion_weight=0.18
rebuffer_prediction_cap_s=4.0
```

Algunas variantes los sobrescribieron con pesos mas altos, por ejemplo
`decision_rebuffer_fusion_weight=0.52` y `decision_risk_fusion_weight=0.40`, pero
eso no convierte esas variantes en modelo aceptado.

Arquitectura full:

```text
sequence_dim=2
scalar_dim=7
candidate_dim=7
history_hidden_size=128
state_hidden_size=96
candidate_hidden_size=48
shared_hidden_size=192
dropout=0.10
```

Perfil de entrenamiento `full_v1`:

```text
epochs=32
batch_size=1024
learning_rate=4.0e-4
max_training_samples=None
max_validation_samples=None
seed=450731
```

Pesos base de loss del perfil:

```text
label_smoothing=0.02
ce_loss_weight=0.45
dpo_loss_weight=0.85
ranking_loss_weight=0.35
utility_loss_weight=0.55
rebuffer_loss_weight=0.45
dpo_beta=0.20
ranking_margin_scale=0.15
utility_temperature=0.55
rebuffer_loss_cap_s=4.0
aux_reward_loss_weight=0.08
aux_rebuffer_loss_weight=0.10
aux_risk_loss_weight=0.08
```

Pesos opcionales anadidos durante exploracion, por defecto a cero si no se
activan:

```text
reference_kl_loss_weight
over_aggressive_probability_loss_weight
over_aggressive_margin_loss_weight
over_aggressive_reference_excess_loss_weight
safe_utility_rank_loss_weight
safe_improvement_rank_loss_weight
copy_baseline_loss_weight
residual_logit_l2_loss_weight
ppo_clip_loss_weight
safe_advantage_policy_loss_weight
```

Fuentes y pesos de pares de preferencia:

```text
oracle_vs_spbc_policy: 1.30
oracle_vs_rollout_policy: 1.35
best_reward_vs_worst_valid: 1.00
safe_vs_rebuffer: 1.45
best_reward_vs_over_aggressive: 1.55
smoothness_tiebreak_when_reward_close: 1.15
fallback_valid_distinction: 0.60
```

Nombres de metricas/loss registradas:

```text
loss
ce_loss
dpo_loss
ranking_loss
utility_loss
rebuffer_loss
aux_reward_loss
aux_rebuffer_loss
aux_risk_loss
reference_kl_loss
over_aggressive_probability_loss
over_aggressive_margin_loss
over_aggressive_reference_excess_loss
safe_utility_rank_loss
safe_improvement_rank_loss
copy_baseline_loss
residual_logit_l2_loss
ppo_clip_loss
safe_advantage_policy_loss
```

## 13. Modelo actual aceptado offline

El mejor candidato actual es:

```text
run=full_v2_anchor_safe_rank_v1
checkpoint=/home/danie/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt
reporte=/home/danie/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/reporte_entrenamiento_spbc_abr_v2_dpo.json
sha256=43b4d012448e12885fac8cbfec914aab6450e0c1b146a4bb8534e8b90b61c227
best_epoch=8
gate=true
```

Metricas offline observadas:

```text
global_over=0.009878
focus_over=0.026312
spbc2_over=0.005187
global_u=0.053229
focus_u=0.062015
spbc2_u=0.044244
safe_rank=0.018196476
```

Deltas frente a `full_v1_utility_risk_v1`:

```text
global utility_regret: -0.015430
global rebuffer_regret: -0.003992
global over_aggressive: -0.005777
global predicted_rebuffer_s_mean: -0.004228
global predicted_bitrate_kbps_mean: -127.600217
global under_aggressive: +0.059409

2_5_mbps utility_regret: -0.026998
2_5_mbps rebuffer_regret: -0.007969
2_5_mbps over_aggressive: -0.018583
2_5_mbps predicted_rebuffer_s_mean: -0.008934
2_5_mbps predicted_bitrate_kbps_mean: -340.249597
2_5_mbps under_aggressive: +0.163059
```

Interpretacion correcta:

- Mejora seguridad offline frente al modelo de referencia usado para DAgger.
- Baja bitrate medio y sube under-aggressive.
- Es un modelo conservador.
- Es defendible como candidato de integracion porque paso gates offline.
- No es todavia resultado formal de TFG.

## 14. Rutas probadas para mejorar y que paso

### 14.1 CE + DPO inicial sobre v2

Objetivo: convertir BC simple en aprendizaje por preferencias con pares
oracle/politica y DPO.

Resultado: tecnicamente viable, pero insuficiente en buckets criticos. Movia
loss y preferencias, pero no cerraba de forma robusta utilidad, rebuffer y
over-aggressive donde mas importaba.

Diagnostico probable:

- El modelo aprendia preferencias locales, pero no resolvia bien estados
  on-policy.
- El surrogate offline podia favorecer pequenos cambios de ranking sin garantizar
  comportamiento estable en 2-5 Mbps.
- Faltaba anclaje mas fuerte a seguridad y no regresion.

### 14.2 `full_v1_utility_risk_v1`

Objetivo: anadir prediccion auxiliar de reward, rebuffer y riesgo, con fusion en
decision.

Resultado: util como referencia y como generador de estados DAgger-2, pero no
como modelo final aceptado.

Diagnostico probable:

- Las cabezas auxiliares aportan senal, pero si la fusion no esta muy controlada
  pueden cambiar agresividad sin mejorar QoE real.
- Sirvio para revelar el problema: al modelo se le puede ensenar "riesgo", pero
  no basta con una cabeza de riesgo para obtener politica robusta.

### 14.3 `safe_margin_v1`

Objetivo: endurecer margen de seguridad y no regresion.

Resultado: una ejecucion full-samples parecio prometedora, pero la confirmacion
multi-seed no fue robusta. En seeds 450741, 450742 y 450743 el mejor epoch fue
fallback a referencia (`best_epoch=0`) en 3/3.

Fallo dominante: no fue solo over-aggressive; aparecieron regresiones de utilidad
en `2_5_mbps` y/o frente al source `spbc_v2_dpo_on_policy`.

Diagnostico probable:

- El margen de seguridad protegia un lado del trade-off, pero empujaba demasiado
  hacia conservadurismo o no encontraba mejora neta respecto al anchor.
- Multi-seed fue imprescindible: sin repetir, habriamos confundido una ejecucion
  buena con una decision estable.

### 14.4 `anchor_safe_rank_v1`

Objetivo: anclar al mejor SPBC v2 disponible y usar ranking seguro para mejorar
sin romper gates.

Resultado: aceptado offline. Es el candidato actual.

Por que funciono mejor:

- No intentaba reinventar la politica desde cero.
- Penalizaba regresiones contra referencia.
- Trataba seguridad y ranking como restricciones practicas, no solo como
  objetivos blandos.

Coste:

- Sube under-aggressive.
- Baja bitrate esperado.
- Puede ser demasiado prudente en Phase 6.

### 14.5 Residual safe-rank v1

Objetivo: entrenar un residual sobre el anchor en vez de mover toda la politica.

Seeds probadas:

```text
450861
450862
450863
```

Resultado resumido de las tres:

```text
status=PASS
best_epoch=0
fallback_to_reference=true
global_over=0.009878
focus_over=0.026312
spbc2_over=0.005187
global_u=0.053229
focus_u=0.062015
spbc2_u=0.044244
safe_rank=0.018196476
safe_improve=1.509928053
copy_base=0.0
residual_l2=0.0
```

Interpretacion: no fallo por romper todo; fallo porque no encontro mejora
aceptable sobre el anchor. El gate salvo el modelo y devolvio la referencia.

Diagnostico probable:

- El espacio de mejora local alrededor del anchor es estrecho bajo esos gates.
- El residual se quedo bloqueado: cualquier movimiento util rompia alguna no
  regresion, y cualquier movimiento seguro no mejoraba suficiente.

### 14.6 SPC reward-risk

Objetivo: entrenar un SPC como modelo de recompensa/riesgo para elegir accion,
potencialmente mas analitico que una politica directa.

Resultado del primer reward-risk anchor:

```text
best_epoch: 9 / 12 / 5 segun seed
global utility regret ~= 0.068708..0.071663
global rebuffer regret ~= 0.004038..0.004795
global over ~= 0.010500..0.013833
focus over ~= 0.031790..0.041975
risk_fn ~= 0.001289..0.001978
```

Deltas frente al SPBC:

```text
rebuffer: mejora ligera (-0.001214 / -0.000692 / -0.000457)
utility: empeora (+0.006017 / +0.003062 / +0.003898)
over: empeora (+0.000833 / +0.004166 / +0.001500)
```

Interpretacion: SPC aprendio algo de riesgo/rebuffer, pero como conductor directo
no supero el balance del SPBC.

Diagnostico probable:

- Estimar consecuencias por accion no equivale a tomar la mejor decision global.
- La seleccion por score puede amplificar errores pequenos de calibracion.
- El modelo puede parecer util como critico/copiloto, pero no como piloto final
  sin validacion adicional.

### 14.7 SPC safe-rank v2

Objetivo: corregir SPC con ranking seguro.

Resultado: rechazado. Dos seeds tuvieron explosion de calibracion de riesgo:

```text
seed_450851 risk_brier=0.152982 risk_fn=0.034779
seed_450852 risk_brier=0.011859 risk_fn=0.002133
seed_450853 risk_brier=0.147532 risk_fn=0.035576
```

Ademas empeoraban utilidad, rebuffer, over y focus frente a SPBC.

Diagnostico probable:

- El score-pushing deformo la calibracion.
- El objetivo de ranking seguro no basto para mantener prediccion de riesgo
  fiable.
- Como evaluador, un SPC mal calibrado es peligroso: puede dar falsa seguridad.

### 14.8 SPC critic/copilot

Objetivo conceptual: no usar SPC como conductor directo, sino como critico o
copiloto de un SPBC.

Estado: no hay SPC aceptado que deba integrarse ya como copilot. La idea sigue
siendo cientificamente razonable, pero requiere evaluador offline especifico,
calibracion y gates propios.

Diagnostico:

- SPC no debe bloquear el avance del anchor.
- Si se retoma, debe evaluarse como filtro/alarma/estimador de riesgo, no como
  sustituto directo del piloto SPBC.

### 14.9 PPO-safe v1

Objetivo: aplicar una actualizacion tipo PPO controlada para mejorar sin alejarse
demasiado de la referencia.

Resultado final:

```text
run=pilot_dagger2_ppo_safe_seed_450881_v1
decision=REVIEW
status=PASS
best_epoch=0
fallback_to_reference=true
gate=true
```

Metricas finales: iguales al anchor porque el gate devolvio la referencia.

Epochs entrenados:

```text
epoch=1 gate=false global_over=0.009801 focus_over=0.025829 spbc2_over=0.004955 global_u=0.053657 focus_u=0.064339 spbc2_u=0.043125 kl=0.003376544 failed=2_5_mbps_utility_regret_non_regression
epoch=2 gate=false global_over=0.009545 focus_over=0.025926 spbc2_over=0.004792 global_u=0.053569 focus_u=0.064564 spbc2_u=0.043034 kl=0.003683310 failed=2_5_mbps_utility_regret_non_regression
epoch=3 gate=false global_over=0.009630 focus_over=0.025733 spbc2_over=0.004838 global_u=0.053888 focus_u=0.065646 spbc2_u=0.043159 kl=0.003376247 failed=global_utility_regret_non_regression,2_5_mbps_utility_regret_non_regression
epoch=4 gate=false global_over=0.009359 focus_over=0.025314 spbc2_over=0.004536 global_u=0.053382 focus_u=0.065328 spbc2_u=0.042510 kl=0.003067797 failed=2_5_mbps_utility_regret_non_regression
```

Lectura: bajo over-aggressive y mantuvo KL bajo, pero empeoro utilidad en el
bucket critico `2_5_mbps`. No es un camino muerto para siempre, pero si queda
claro que PPO sobre este surrogate y estos gates no fue la mejora brillante que
buscabamos.

Diagnostico probable:

- PPO optimizo una senal que no captura bien el trade-off local de 2-5 Mbps.
- Con anchor ya conservador, seguir empujando seguridad puede quitar utilidad.
- Falta evaluacion real de controller antes de saber si el problema offline
  importa igual en Phase 6.

### 14.10 Safe-advantage probe v1

Objetivo: usar una senal de ventaja segura para mover la politica hacia acciones
con mayor retorno esperado.

Resultado final:

```text
run=pilot_dagger2_safe_advantage_probe_seed_450891_v1
decision=REVIEW
status=PASS
best_epoch=0
fallback_to_reference=true
gate=true
```

Metricas finales: iguales al anchor porque el gate devolvio la referencia.

Epochs entrenados:

```text
epoch=1 selection=13.46961085 global_over=0.024533 focus_over=0.052915 spbc2_over=0.021424 global_u=1.541909 focus_u=0.920844 spbc2_u=1.528167 kl=0.088098042 failed=over,utility,rebuffer en global/focus/spbc2
epoch=2 selection=13.71868205 global_over=0.025882 focus_over=0.054783 spbc2_over=0.022470 global_u=1.557478 focus_u=0.942769 spbc2_u=1.545893 kl=0.094122512 failed=over,utility,rebuffer en global/focus/spbc2
epoch=3 selection=13.70458330 global_over=0.025471 focus_over=0.054138 spbc2_over=0.022005 global_u=1.561487 focus_u=0.969361 spbc2_u=1.541756 kl=0.095217449 failed=over,utility,rebuffer en global/focus/spbc2
```

Lectura: esta variante se movio demasiado. Subio bitrate, pero exploto
over-aggressive, rebuffer y regret. Fue rechazo claro, no un empate dudoso.

Diagnostico probable:

- La ventaja segura no estaba suficientemente acotada.
- El modelo encontro una via facil: elegir mas alto.
- La senal de ventaja no estaba alineada con seguridad en estados dificiles.

## 15. Que tenemos que los papers tambien tienen

De la lectura de trabajos tipo Comyco, SafeSABR, SABR, Fugu/Puffer, Gelato,
Plume, Oboe, ANT, BETA, A2BR, SODA y CausalSim se extrae una idea comun: los
controllers IA defendibles no nacen solo de "entrenar una red". Tienen pipeline,
contrato experimental, datos, simulador, safety, ablations y validacion.

Ya tenemos varias piezas comparables:

- Dataset curado y documentado.
- Separacion de train/test/eval por grupo.
- DAgger/on-policy para reducir compounding error.
- Oracle offline con QoE explicita.
- Ladder y fragmentos coherentes con MPD real.
- Gates de no contaminacion.
- Gates de seguridad/no regresion.
- Modelo con mascara de acciones y contrato de input limpio.
- Integracion Phase 6 preparada para evaluacion formal.

## 16. Que nos falta frente a esos trabajos

Lo que aun falta no es glamour, es cierre experimental:

- Integrar el modelo aceptado como controller real.
- Ejecutar preflight/diagnostico sin llamarlo benchmark.
- Ejecutar Phase 6 con preset capaz de benchmark cuando el protocolo este
  congelado.
- Comparar contra baselines clasicos solo en Phase 6 y con analisis emparejado.
- Analizar fallos por regimen: `lte_1_mbps`, `1_2_mbps`, `2_5_mbps`,
  `5_20_mbps`, `gt_20_mbps`, sinteticas y reales por separado.
- Medir latencia de inferencia, fallback, errores de bundle y limpieza de CSV.
- Separar claramente resultados reales y sinteticos.
- Hacer ablations si el anchor no pelea: sin cabezas auxiliares, sin fusion,
  especialista por bucket, SPC como critico, planner sobre predictor.

## 17. Riesgos tecnicos actuales

### 17.1 Conservadurismo

El anchor reduce over-aggressive y rebuffer offline, pero sube under-aggressive y
baja bitrate medio. En Phase 6 puede quedar como controller seguro pero poco
competitivo si los baselines clasicos aprovechan mejor el ancho de banda.

### 17.2 Desalineacion offline/online

Los gates offline no son el cliente real. La dinamica de buffer, temporizacion,
descargas, MPD y media engine pueden introducir diferencias.

### 17.3 Escasez relativa de casos extremos

Aunque hay 6768 trazas, las condiciones severas/intermitentes son pocas:

```text
severe_or_intermittent_network=40
low_bandwidth_network=297
```

El sampler las prioriza, pero la cola dificil sigue siendo pequena.

### 17.4 Semanticas heterogeneas

No todas las trazas son ancho de banda disponible directo. Algunas son
speedtests, otras trafico observado, otras delivery rate real. Esto puede sesgar
lo que el modelo cree que significa throughput.

### 17.5 SPC como falsa seguridad

SPC puede parecer atractivo porque predice reward/riesgo, pero si no esta
calibrado puede empeorar decisiones. Las seeds de safe-rank v2 lo demostraron.

### 17.6 Coste computacional

Con la AMD Radeon RX 7800 XT podemos entrenar, pero cada experimento multi-seed
cuesta horas. Ya no estamos en fase de tirar ideas a la pared; cada ejecucion
debe contestar una pregunta concreta.

## 18. Lo que el modelo actual sabe y lo que no sabe

Sabe:

- Historial corto de throughput y download time.
- Buffer actual.
- Ultima representacion y bitrate.
- Rebuffer reciente.
- Suavidad/cambios recientes.
- Chunks restantes normalizados.
- Seis candidatos con bitrate, posicion en ladder, delta frente al ultimo bitrate
  y tamano estimado de chunk.
- Mascara de acciones validas.

No sabe:

- Identidad de traza.
- Dataset de origen.
- Si la traza es sintetica.
- Split.
- Semantica de red como input.
- Futuro real de throughput.
- Calidad perceptual VMAF.
- Complejidad visual de cada escena.
- Estado del servidor mas alla de lo observado por descarga.
- Nombre del MPD.

Esto es bueno para evitar contaminacion, pero limita el techo: si dos situaciones
tienen features iguales pero semantica distinta, el modelo no puede distinguirlas.

## 19. Que significa "brillante" en este contexto

Un controller IA brillante para este TFG no tiene por que ganar a todos los
baselines clasicos en todos los escenarios. Tiene que ser defendible:

- Entrenado con datos trazables.
- Sin leakage.
- Con objetivo QoE explicito.
- Con safety gates.
- Con fallos documentados.
- Integrado en el cliente real.
- Evaluado con Phase 6, no con smokes.
- Capaz de pelear en algun regimen o aportar un comportamiento interesante:
  menos rebuffer, menos agresividad peligrosa, o adaptacion estable en buckets
  dificiles.

Si el resultado es "no gana siempre, pero es estable, seguro y muestra una
estrategia aprendida defendible", eso puede ser cientificamente valioso. Si
intentamos forzar que gane todo antes de medir, corremos el riesgo de destruir lo
que ya tenemos.

## 20. Caminos claros a partir de ahora

### Camino A: integrar el anchor SPBC v2 y pasar a Phase 6

Accion:

```text
Integrar full_v2_anchor_safe_rank_v1 como controller IA.
Exportar bundle si falta.
Validar inferencia y fallback.
Ejecutar Phase 6 diagnostico/rapido.
Si todo esta limpio, ejecutar equilibrado o extendido cuando proceda.
```

Ventajas:

- Es el unico camino apoyado por un modelo que ya paso gates offline.
- Convierte trabajo de entrenamiento en evidencia real.
- Permite saber si el conservadurismo offline es problema real o ventaja.
- Evita seguir gastando horas sin feedback del cliente.

Riesgos:

- Puede no ganar.
- Puede ser demasiado prudente.
- Puede revelar problemas de integracion.

Lectura: es el camino recomendado ahora.

### Camino B: SPBC piloto + SPC critico/copiloto

Accion:

```text
Mantener SPBC como piloto.
Entrenar o calibrar SPC solo como estimador de riesgo/rebuffer.
Crear evaluador offline de veto o ajuste.
No integrarlo como conductor hasta pasar gates propios.
```

Ventajas:

- Aprovecha la intuicion de SPC sin darle el volante entero.
- Es defendible como arquitectura hibrida.
- Permite explicar decisiones: policy + critic.

Riesgos:

- SPC ya mostro problemas de calibracion.
- Puede anadir complejidad sin mejora.
- Necesita evaluador especifico y ablations.

Lectura: buen segundo ciclo si Phase 6 muestra que el SPBC necesita un filtro o
una correccion puntual.

### Camino C: especialista por regimen

Accion:

```text
Entrenar/fine-tunear especialista para 2_5_mbps o low-bandwidth.
Usar gating simple basado en features permitidas, no metadata.
Comparar contra anchor en offline y despues Phase 6.
```

Ventajas:

- Ataca justo donde fallaron PPO y safe-advantage.
- Conecta con literatura de especializacion por condiciones.
- Puede mejorar sin romper todo el espacio de estados.

Riesgos:

- El gating puede oscilar.
- Puede sobreajustar buckets.
- Hay que evitar usar etiquetas prohibidas.

Lectura: cientificamente prometedor, pero posterior a integrar y medir el anchor.

### Camino D: predictor de consecuencias + planner

Accion:

```text
Entrenar un predictor calibrado de rebuffer/reward/riesgo por accion.
No seleccionar por score crudo.
Usarlo dentro de un mini-planner/MPC con restricciones de seguridad.
```

Ventajas:

- Se parece mas a Fugu/Puffer: modelo predictivo + control explicito.
- Mas interpretable que una politica pura.
- Puede hacer mejor uso de la ladder y del buffer.

Riesgos:

- Es una arquitectura nueva.
- Necesita calibracion seria.
- El SPC anterior demuestra que el predictor puede fallar si se fuerza.

Lectura: camino fuerte si queremos una segunda gran contribucion, pero no debe
bloquear la primera integracion.

### Camino E: PPO/RL despues de integracion

Accion:

```text
No seguir PPO ahora.
Retomarlo solo si Phase 6 identifica una metrica concreta que optimizar.
Usar KL, early stopping y gates por regimen.
```

Ventajas:

- Puede pulir una politica ya razonable.
- Encaja con literatura RL si se controla.

Riesgos:

- Ya vimos que PPO-safe no mejoro el bucket critico.
- Safe-advantage exploto.
- Muy caro computacionalmente.

Lectura: no recomendado como siguiente paso inmediato.

### Camino F: VMAF/contenido/perceptual

Accion:

```text
Incluir VMAF o complejidad de contenido cuando los artefactos esten disponibles.
```

Ventajas:

- Mejor alineacion con calidad perceptual.
- Podria diferenciar Blender/Paseo y 30/60 fps.

Riesgos:

- Esta deferred por dependencia de artefactos.
- Cambia el contrato QoE y la comparabilidad.

Lectura: futuro, no ahora.

## 21. Pregunta final: que camino exacto debemos tomar

Con todo lo anterior, la pregunta honesta no es "como entrenamos otra red mas".
La pregunta exacta es:

```text
Queremos demostrar primero que el mejor SPBC entrenado puede vivir como controller
real en Phase 6, o queremos abrir otra ronda de investigacion antes de tener
ninguna evidencia de cliente?
```

Mi respuesta tecnica es:

1. Tomar el camino A ahora: integrar `full_v2_anchor_safe_rank_v1`.
2. No tocar mas losses hasta verlo como controller.
3. Ejecutar diagnostico y rapido sin llamarlos benchmark.
4. Si el pipeline esta limpio, ejecutar preset formal de Phase 6.
5. Usar resultados reales para elegir entre:
   - B: SPBC + SPC critico/copiloto,
   - C: especialista por regimen,
   - D: predictor + planner.

La razon es simple: ya tenemos demasiada evidencia de que los intentos de mejora
offline pueden parecer inteligentes y acabar devolviendo fallback. El siguiente
dato que falta no es otro loss; es comportamiento real del controller bajo el
cliente y el protocolo formal.

## 22. Decision recomendada antes de integrar

Decision recomendada:

```text
Integrar como primer controller IA nuevo:
spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1
```

Condiciones:

- Registrar claramente que es candidato offline, no ganador.
- Exportar bundle versionado.
- Mantener fallback seguro.
- Anadir auditoria de inferencia.
- No mezclar sus resultados con smokes antiguos.
- Phase 6 decide, no el entrenamiento.

Si Phase 6 muestra que pelea pero es conservador, el siguiente experimento
deberia ser especialista por regimen o hibrido SPBC+SPC critico, no otra
variante PPO general.

Si Phase 6 muestra que ni pelea ni aporta estabilidad, entonces el camino mas
honesto seria replantear a predictor + planner, porque la familia de politicas
directas SPBC/DPO habria alcanzado su techo con este dataset y este surrogate.

## 23. Incertidumbres que no se deben esconder

Este informe usa evidencia versionada del repositorio, documentos operativos y
salidas de WSL pegadas durante la ejecucion. Algunos artefactos pesados viven
fuera del repo y no estan commiteados:

```text
/home/danie/TFG/datasets_normalizados/phase45_v1/...
/home/danie/TFG/modelos/phase45_v1/...
/tmp/phase45_*.log
```

Por tanto:

- Los checkpoints no estan versionados en git.
- Los logs temporales de entrenamiento no son fuente permanente si no se copian a
  un reporte estable.
- Phase 6 formal todavia no se ha ejecutado para este controller.
- Cualquier afirmacion de mejora queda prohibida hasta esa ejecucion.

Esta honestidad no debilita el TFG; lo fortalece. Un trabajo defendible sabe
donde esta el suelo firme y donde empieza la hipotesis.

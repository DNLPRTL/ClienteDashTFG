# Informe objetivo de bloqueo para ayuda externa - Phase45 v3 Q_H scorer pilot

Fecha: 2026-06-12

Estado del documento: informe objetivo para pedir ayuda externa. No contiene
propuestas de solucion, recomendaciones de siguiente experimento, ranking,
benchmark ni afirmaciones de mejora de QoE.

## Solicitud a ChatGPT u otra IA

Analizar objetivamente el bloqueo descrito en este informe. Identificar, a
partir de los hechos documentados, causas tecnicas compatibles con los datos,
riesgos de interpretacion y datos adicionales que convendria revisar. No asumir
que hay benchmark final, ganador, ranking ni mejora de QoE autorizada.

No proponer un plan de accion. La respuesta solicitada debe limitarse a
diagnostico objetivo, dudas tecnicas, comprobaciones faltantes y explicacion de
los patrones observados.

## Objetivo general del trabajo

Proyecto: `DashClientModular4`.

Tema: cliente MPEG-DASH modular con controladores ABR clasicos y un controlador
IA propio defendible para un TFG.

Objetivo tecnico de esta linea concreta: construir un modelo IA ABR nuevo
adaptado al cliente real, evitando los errores detectados en SPBC v1/v2. El
modelo actual de esta linea es un `phase45_v3_qh_scorer`: un scorer neural que
recibe estado ABR visible por el controller y candidatos de bitrate, y debe
ordenar acciones segun targets `Q_H(s,a)` generados en un entorno cerrado
equivalente a la dinamica ABR del cliente.

## Arquitectura operativa

Rama Git:

```text
rebuild/phase3-from-phase2
```

Commits relevantes recientes:

```text
ddd3d8a chore(phase45): add QH scorer error analysis
94f75b2 feat(phase45): add temporal GRU QH scorer profile
d9510cb chore(phase45): require GPU for adv regret runbook
4c5a217 feat(phase45): add advantage regret QH scorer profile
c3396fd docs(phase45): document QH scorer pilot blockage
e8d07b6 chore(phase45): add QH scorer pilot rank WSL runbook
```

Repositorio Windows:

```text
C:\Users\danie\Documents\TFG\DashClientModular4
```

Repositorio WSL2:

```text
/home/danie/TFG/DashClientModular4
```

Raiz de artefactos pesados en WSL2:

```text
/home/danie/TFG
```

Entorno WSL2/ROCm observado por Daniel:

```text
Distribucion: Ubuntu-24.04 en WSL2
Venv: /home/danie/venvs/rocm721
Torch: 2.9.1+rocm7.2.1.gitff65f5bc
torch.cuda.is_available(): True
GPU: AMD Radeon RX 7800 XT
```

Regla metodologica del proyecto: Windows desarrolla, testea rapido, commitea y
pushea; WSL2 entrena IA pesada; Ubuntu cliente valida ejecuciones relevantes; el
servidor Ubuntu solo sirve MPD/segmentos.

## Restricciones metodologicas

Estas ejecuciones son entrenamiento/validacion offline de modelo candidato.

No autorizan:

```text
benchmark_performed
ranking_performed
winner
QoE improvement claim
generalizacion real-world
```

El modelo `phase45_v3_qh_scorer` no esta integrado como controller final ni
evaluado en Phase6 formal.

## Contexto previo: SPBC rechazado por colapso runtime

Antes de Phase45 v3 se habia integrado/probado un controller SPBC v2. En una
ejecucion rapida Phase6 se detecto colapso de politica:

```text
controller=propio_spbc_v2_anchor
status=FAIL
collapse_detected=True
high_capacity_action0_rate=0.6623376623376623
max_consecutive_action0_after_startup=26
fallback_row_count=5
fallback_reasons={"inference_timeout": 5}
qoe_delta_vs_baseline_mean=-1.7679512342365435
baseline_alias=base_robust_mpc
mean_measured_throughput_kbps=100153.01954068724
mean_selected_bitrate_kbps=656.2068965517242
median_selected_bitrate_kbps=300.0
```

Diagnostico factual asociado: los datasets/modelos SPBC v1/v2 se habian
construido con una dinamica offline que no reproducia completamente la dinamica
del cliente final. En particular se encontro una diferencia relevante de buffer:
entrenamiento antiguo con `max_buffer_s=20.0` frente a cliente/Phase6 con
`max_buffer_s=60.0`.

## Entorno cerrado Phase45 v3

Phase45 v3 se creo para generar targets en un entorno cerrado con paridad de
dinamica ABR respecto al cliente/Phase6, sin usar informacion futura como input
del modelo.

Contrato de paridad documentado por el codigo y el dataset pilot:

```text
parity_scope=ABR decision dynamics used by the client and Phase 6 trace replay
qoe_formula_version=qoe_linear_v1
reward=bitrate_mbps - 4.3 * rebuffer_s - smoothness_mbps
segment_duration_s=4.0
segment_count=30
max_buffer_s=60.0
representation_bitrates_kbps=[300,750,1200,1850,2850,4300]
network_source=TraceDrivenNetworkModel over normalized throughput_kbps windows
controller_visible_inputs_match_runtime_feature_builder=True
```

Elementos no reproducidos por el entorno cerrado:

```text
HTTP server process
GStreamer media pipeline
OS scheduling jitter
```

Archivos principales de esta linea:

```text
core/phase45_v3/abr_closed_loop_env.py
core/phase45_v3/dataset.py
core/phase45_v3/qh_oracle.py
core/phase45_v3/qh_scorer_training.py
core/phase45_v3/validation.py
scripts/generate_phase45_v3_qh_dataset.py
scripts/train_phase45_v3_qh_scorer.py
scripts/analyze_phase45_v3_qh_scorer_errors.py
tests/test_phase45_v3_state_builder_parity.py
tests/test_phase45_v3_dataset.py
tests/test_phase45_v3_qh_scorer_losses.py
```

## Dataset usado en los pilots

Ruta:

```text
/home/danie/TFG/datasets_normalizados/phase45_v3/qh_closed_loop_pilot
```

Archivos principales:

```text
datos_entrenamiento_phase45_v3_qh.jsonl
datos_validacion_phase45_v3_qh.jsonl
resumen_dataset_phase45_v3_qh.json
plan_muestreo_phase45_v3_qh.json
auditoria_muestreo_phase45_v3_qh.json
auditoria_no_contaminacion_phase45_v3.json
auditoria_qh_oracle_phase45_v3.json
estadisticas_normalizacion_train_only_phase45_v3.json
esquema_model_inputs_phase45_v3.json
esquema_targets_phase45_v3_qh.json
```

Perfil dataset pilot:

```text
name=pilot
train_window_count=256
validation_window_count=64
qh_horizon_segments=4
qh_beam_width=18
max_windows_per_trace=3
synthetic_max_fraction=0.15
dataset_max_fraction=0.4
semantics_max_fraction=0.55
rollouts_per_window=4
seed=phase45_v3_pilot_qh_dataset_seed
```

Plan de muestreo:

```text
media_profile_id=paseo_10min_30fps_4s
segment_count_per_window=30
segment_duration_s=4.0
window_duration_s=120.0
source_manifest_path=/home/danie/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json
source_trace_count=6768
source_manifest_artifact_set=final_with_synthetic_controlled_quality_curated
```

Conteo de muestras:

```text
training=30600
validation=7440
```

Rollouts presentes:

```text
qh_minus_one=9510
qh_oracle=9510
qh_plus_one=9510
startup_conservative=9510
```

Auditoria Q_H:

```text
status=PASS
errors=[]
future_information_is_target_only=true
high_capacity_safe_state_count=7783
high_capacity_safe_target_action0_rate=0.01529
target_action_distribution={'0': 6081, '1': 4998, '2': 4667, '3': 4308, '4': 3446, '5': 14540}
```

Auditoria de no contaminacion:

```text
status=PASS
errors=[]
skipped_window_count=3
metadata_fields_are_model_features=false
eval_split_used=false
```

Este dataset no es benchmark. Sus salidas mantienen:

```text
benchmark_performed=false
outputs_are_benchmark_results=false
ranking_performed=false
no_final_ranking=true
qoe_claims_authorized=false
```

## Modelo entrenado

Modelo:

```text
model_key=phase45_v3_qh_scorer
```

Arquitecturas probadas:

```text
shared_mlp_qh_candidate_scorer
gru_candidate_qh_scorer
```

Entrada conceptual:

```text
contexto ABR visible por controller + features de cada candidato de bitrate
```

Salida conceptual:

```text
score por accion/candidato; se elige argmax entre acciones validas
```

Targets:

```text
Q_H(s,a) por accion generados por oracle cerrado
future_information_is_target_only=true
```

Gates de entrenamiento aplicados:

```text
top1_accuracy_floor >= 0.55
mean_regret_q_h <= 0.35
high_capacity_predicted_action0_rate <= 0.05
```

El gate bloqueante en todos los pilots ha sido:

```text
mean_regret_q_h
```

## Intentos ejecutados

### Tabla compacta

```text
run                                                   status  arch        top1      mean_regret  p95       high_cap_a0  pred_a0   failed
qh_scorer_pilot_dataset_pilot_seed450921_v1          REVIEW  mlp         0.792473  0.594340     1.650000  0.001179     0.177016  mean_regret_q_h
qh_scorer_pilot_plus_dataset_pilot_seed450922_v1     REVIEW  mlp         0.802285  0.550857     1.549999  0.001179     0.181989  mean_regret_q_h
qh_scorer_pilot_rank_dataset_pilot_seed450923_v1     REVIEW  mlp         0.792070  0.476182     1.599998  0.001179     0.183065  mean_regret_q_h
qh_scorer_pilot_adv_regret_dataset_pilot_seed450924_v1 REVIEW mlp         0.788844  0.395739     1.450001  0.002946     0.221505  mean_regret_q_h
qh_scorer_pilot_adv_regret_gru_dataset_pilot_seed450925_v1 REVIEW gru     0.764516  0.442516     1.650000  0.007661     0.226747  mean_regret_q_h
```

### 1. `pilot`

Ruta:

```text
/home/danie/TFG/modelos/phase45_v3/qh_scorer/qh_scorer_pilot_dataset_pilot_seed450921_v1
```

Checkpoint:

```text
sha256=36fda2478f96e33f3ef72789b89d8d5c19304451ba0daab7e3bbb8cb1c196eb0
device=cuda
elapsed_s=7.219
```

Perfil:

```text
epochs=12
batch_size=512
learning_rate=0.0005
hidden_sizes=[192,96,48]
ce_loss_weight=0.45
q_value_loss_weight=1.0
seed=450921
```

Resultado:

```text
status=REVIEW
failed=['mean_regret_q_h']
top1_accuracy=0.792473
mean_regret_q_h=0.594340
p95_regret_q_h=1.650000
high_capacity_predicted_action0_rate=0.001179
predicted_action0_rate=0.177016
```

### 2. `pilot_plus`

Ruta:

```text
/home/danie/TFG/modelos/phase45_v3/qh_scorer/qh_scorer_pilot_plus_dataset_pilot_seed450922_v1
```

Checkpoint:

```text
sha256=f3b2b6147ef011e8cdc4d784bca90aa28fe20a72d6c11a8d9f7beedef4aa99d5
device=cuda
elapsed_s=14.183
```

Perfil:

```text
epochs=28
batch_size=512
learning_rate=0.00025
hidden_sizes=[256,128,64]
ce_loss_weight=0.35
q_value_loss_weight=1.35
seed=450922
```

Resultado:

```text
status=REVIEW
failed=['mean_regret_q_h']
top1_accuracy=0.802285
mean_regret_q_h=0.550857
p95_regret_q_h=1.549999
high_capacity_predicted_action0_rate=0.001179
predicted_action0_rate=0.181989
```

### 3. `pilot_rank`

Ruta:

```text
/home/danie/TFG/modelos/phase45_v3/qh_scorer/qh_scorer_pilot_rank_dataset_pilot_seed450923_v1
```

Checkpoint:

```text
sha256=8ade3c2bd411ff66329bd308a69d00b973e9393f2db2e8cfc8fcbb1d34510b10
device=cuda
elapsed_s=16.115
```

Perfil:

```text
epochs=28
batch_size=512
learning_rate=0.00025
hidden_sizes=[256,128,64]
ce_loss_weight=0.25
q_value_loss_weight=0.8
pairwise_rank_loss_weight=1.1
pairwise_margin_scale=1.0
pairwise_q_gap_cap=4.0
seed=450923
```

Resultado:

```text
status=REVIEW
failed=['mean_regret_q_h']
top1_accuracy=0.792070
mean_regret_q_h=0.476182
p95_regret_q_h=1.599998
high_capacity_predicted_action0_rate=0.001179
predicted_action0_rate=0.183065
```

### 4. `pilot_adv_regret_v1`

Ruta:

```text
/home/danie/TFG/modelos/phase45_v3/qh_scorer/qh_scorer_pilot_adv_regret_dataset_pilot_seed450924_v1
```

Checkpoint:

```text
/home/danie/TFG/modelos/phase45_v3/qh_scorer/qh_scorer_pilot_adv_regret_dataset_pilot_seed450924_v1/modelo_phase45_v3_qh_scorer.pt
sha256=fd51320dbbddcec0c8cd55aa619422d87dcec452ab6915f7bbf50d16ae5fa078
device=cuda
elapsed_s=26.653
```

Perfil:

```text
epochs=40
batch_size=512
learning_rate=0.00018
hidden_sizes=[384,192,96]
ce_loss_weight=0.08
q_value_loss_weight=0.0
pairwise_rank_loss_weight=0.7
pairwise_margin_scale=0.6
pairwise_q_gap_cap=5.0
pairwise_use_denormalized_q_gap=true
soft_q_kl_loss_weight=1.2
q_softmax_temperature=0.35
expected_regret_loss_weight=1.6
tail_regret_loss_weight=0.9
tail_regret_fraction=0.25
advantage_huber_loss_weight=0.45
top_vs_bad_margin_loss_weight=1.2
top_vs_bad_regret_threshold=0.5
top_vs_bad_margin_scale=0.45
top_vs_bad_gap_cap=5.0
seed=450924
```

Resultado:

```text
status=REVIEW
failed=['mean_regret_q_h']
top1_accuracy=0.788844
mean_regret_q_h=0.395739
p95_regret_q_h=1.450001
high_capacity_predicted_action0_rate=0.002946
predicted_action0_rate=0.221505
regret_gt_0_5_rate=0.139247
regret_gt_1_0_rate=0.089382
regret_gt_2_0_rate=0.037769
```

Distribuciones finales:

```text
predicted_action_distribution={'0': 1648, '1': 812, '2': 706, '3': 648, '4': 522, '5': 3104}
target_action_distribution={'0': 1131, '1': 899, '2': 831, '3': 724, '4': 609, '5': 3246}
```

### 5. `pilot_adv_regret_gru_v1`

Ruta:

```text
/home/danie/TFG/modelos/phase45_v3/qh_scorer/qh_scorer_pilot_adv_regret_gru_dataset_pilot_seed450925_v1
```

Checkpoint:

```text
/home/danie/TFG/modelos/phase45_v3/qh_scorer/qh_scorer_pilot_adv_regret_gru_dataset_pilot_seed450925_v1/modelo_phase45_v3_qh_scorer.pt
sha256=bcc26ec2b4bebbfe2065c29770ff0e140552c59ca1c4c3f3358a531c08e942e2
device=cuda
elapsed_s=32.928
```

Perfil:

```text
model_architecture=gru_candidate_qh_scorer
history_gru_hidden_size=96
epochs=44
batch_size=512
learning_rate=0.00015
hidden_sizes=[384,192,96]
losses=same objective family as pilot_adv_regret_v1
seed=450925
```

Resultado:

```text
status=REVIEW
failed=['mean_regret_q_h']
top1_accuracy=0.764516
mean_regret_q_h=0.442516
p95_regret_q_h=1.650000
high_capacity_predicted_action0_rate=0.007661
predicted_action0_rate=0.226747
regret_gt_0_5_rate=0.162769
regret_gt_1_0_rate=0.099194
regret_gt_2_0_rate=0.044086
```

## Comparacion factual entre los ultimos dos intentos

`pilot_adv_regret_v1` frente a `pilot_adv_regret_gru_v1`:

```text
mean_regret_q_h: 0.395739 -> 0.442516
p95_regret_q_h: 1.450001 -> 1.650000
top1_accuracy: 0.788844 -> 0.764516
high_capacity_predicted_action0_rate: 0.002946 -> 0.007661
regret_gt_0_5_rate: 0.139247 -> 0.162769
regret_gt_1_0_rate: 0.089382 -> 0.099194
regret_gt_2_0_rate: 0.037769 -> 0.044086
```

Hecho observado: en este pilot, el GRU temporal no mejora el MLP
`pilot_adv_regret_v1`; empeora las metricas principales de validacion offline.

## Analisis de errores generado

Script:

```text
scripts/analyze_phase45_v3_qh_scorer_errors.py
```

Comando ejecutado para MLP:

```bash
python3 scripts/analyze_phase45_v3_qh_scorer_errors.py \
  --run-name qh_scorer_pilot_adv_regret_dataset_pilot_seed450924_v1 \
  --dataset-dir ~/TFG/datasets_normalizados/phase45_v3/qh_closed_loop_pilot \
  --top-n 25
```

Salida:

```text
/home/danie/TFG/modelos/phase45_v3/qh_scorer/qh_scorer_pilot_adv_regret_dataset_pilot_seed450924_v1/analisis_errores_phase45_v3_qh_scorer.json
```

Comando ejecutado para GRU:

```bash
python3 scripts/analyze_phase45_v3_qh_scorer_errors.py \
  --run-name qh_scorer_pilot_adv_regret_gru_dataset_pilot_seed450925_v1 \
  --dataset-dir ~/TFG/datasets_normalizados/phase45_v3/qh_closed_loop_pilot \
  --top-n 0
```

Salida:

```text
/home/danie/TFG/modelos/phase45_v3/qh_scorer/qh_scorer_pilot_adv_regret_gru_dataset_pilot_seed450925_v1/analisis_errores_phase45_v3_qh_scorer.json
```

### Resumen de error - mejor MLP

Overall:

```text
count=7440
mean_regret_q_h=0.395739
p50_regret_q_h=0.0
p95_regret_q_h=1.450001
max_regret_q_h=127.994537
regret_gt_0_5_rate=0.139247
regret_gt_1_0_rate=0.089382
regret_gt_2_0_rate=0.037769
```

Por estado de alta capacidad:

```text
high_capacity_state=false count=5743 mean=0.495922 p95=1.905354 gt2=0.047362
high_capacity_state=true  count=1697 mean=0.056697 p95=0.000000 gt2=0.005303
```

Por bucket de buffer:

```text
00_04s   count=248  mean=0.760336 p95=5.810799 gt2=0.145161
04_08s   count=3167 mean=0.499127 p95=2.550001 gt2=0.058731
08_16s   count=1676 mean=0.437616 p95=1.450001 gt2=0.028043
16_32s   count=914  mean=0.428122 p95=1.000000 gt2=0.008753
32s_plus count=1435 mean=0.035017 p95=0.000000 gt2=0.002787
```

Por bucket de throughput:

```text
lte_1_mbps count=1680 mean=0.234303 p95=1.350000 gt2=0.003571
1_2_mbps   count=1080 mean=0.238106 p95=1.151220 gt2=0.007407
2_5_mbps   count=2280 mean=0.593478 p95=3.000000 gt2=0.075000
5_20_mbps  count=1560 mean=0.401270 p95=1.449999 gt2=0.039744
gt_20_mbps count=840  mean=0.374287 p95=0.000000 gt2=0.040476
```

Por rollout policy:

```text
qh_minus_one         count=1860 mean=0.279358 p95=1.449999 gt2=0.019355
qh_oracle            count=1860 mean=0.318185 p95=1.350000 gt2=0.030645
qh_plus_one          count=1860 mean=0.623309 p95=2.474163 gt2=0.056989
startup_conservative count=1860 mean=0.362103 p95=1.550003 gt2=0.044086
```

Por accion predicha:

```text
pred=0 count=1648 mean=0.509874 p95=3.461220 gt2=0.066748
pred=1 count=812  mean=0.568637 p95=1.350000 gt2=0.030788
pred=2 count=706  mean=0.468674 p95=1.950001 gt2=0.046742
pred=3 count=648  mean=0.643990 p95=2.550001 gt2=0.075617
pred=4 count=522  mean=0.835449 p95=3.682091 gt2=0.078544
pred=5 count=3104 mean=0.147551 p95=0.000000 gt2=0.007410
```

Por accion objetivo:

```text
target=0 count=1131 mean=0.384782 p95=0.000000 gt2=0.016799
target=1 count=899  mean=0.556664 p95=1.350002 gt2=0.011123
target=2 count=831  mean=0.498138 p95=1.350000 gt2=0.024067
target=3 count=724  mean=0.652040 p95=1.950001 gt2=0.048343
target=4 count=609  mean=0.528062 p95=2.550001 gt2=0.065681
target=5 count=3246 mean=0.246780 p95=1.892227 gt2=0.048367
```

Matriz de confusion target -> predicted:

```text
target 0: pred0=1105 pred1=17 pred2=6 pred3=3
target 1: pred0=288 pred1=540 pred2=63 pred3=5 pred4=2 pred5=1
target 2: pred0=94 pred1=205 pred2=471 pred3=53 pred4=5 pred5=3
target 3: pred0=43 pred1=28 pred2=118 pred3=448 pred4=77 pred5=10
target 4: pred0=9 pred1=10 pred2=26 pred3=123 pred4=328 pred5=113
target 5: pred0=109 pred1=12 pred2=22 pred3=16 pred4=110 pred5=2977
```

Regret buckets:

```text
regret=0       count=5972
regret=0_0.5   count=432
regret=0.5_1.0 count=371
regret=1.0_2.0 count=384
regret=2.0_plus count=281
```

Patrones factuales del top de errores severos del MLP:

```text
dataset_id frecuente=roma_4g_nbiot_5g_nsa
otros dataset_id presentes=puffer_stanford
semantics frecuente=active_mobile_speedtest
variability_bucket frecuente=high_variability
rollout_policy frecuente=qh_plus_one, qh_oracle, startup_conservative
throughput_bucket frecuente=2_5_mbps, 5_20_mbps, gt_20_mbps
buffer_bucket frecuente=04_08s, 08_16s, 16_32s
```

Ejemplos top de error del MLP:

```text
sample=trace_roma_4g_nbiot_5g_nsa...startup_conservative...segment_0013
regret=127.994537 target_action=3 predicted_action=5 buffer=15.857s throughput_bucket=5_20_mbps

sample=trace_roma_4g_nbiot_5g_nsa...qh_oracle...segment_0014
regret=119.064621 target_action=1 predicted_action=5 buffer=31.379s throughput_bucket=2_5_mbps

sample=trace_roma_4g_nbiot_5g_nsa...qh_plus_one...segment_0002
regret=105.919609 target_action=0 predicted_action=1 buffer=4.956s throughput_bucket=gt_20_mbps

sample=trace_roma_4g_nbiot_5g_nsa...qh_plus_one...segment_0013
regret=76.777740 target_action=1 predicted_action=3 buffer=24.286s throughput_bucket=2_5_mbps

sample=trace_roma_4g_nbiot_5g_nsa...qh_oracle...segment_0016
regret=56.044533 target_action=0 predicted_action=1 buffer=12.142s throughput_bucket=5_20_mbps
```

### Resumen de error - GRU

Overall:

```text
count=7440
mean_regret_q_h=0.442516
p50_regret_q_h=0.0
p95_regret_q_h=1.650000
max_regret_q_h=127.994537
regret_gt_0_5_rate=0.162769
regret_gt_1_0_rate=0.099194
regret_gt_2_0_rate=0.044086
```

Por estado de alta capacidad:

```text
high_capacity_state=false count=5743 mean=0.548625 p95=2.449999 gt2=0.054153
high_capacity_state=true  count=1697 mean=0.083420 p95=0.000000 gt2=0.010018
```

Por bucket de buffer:

```text
00_04s   count=248  mean=0.760336 p95=5.810799 gt2=0.145161
04_08s   count=3167 mean=0.537310 p95=3.000002 gt2=0.064730
08_16s   count=1676 mean=0.507899 p95=1.549999 gt2=0.040573
16_32s   count=914  mean=0.542241 p95=1.200001 gt2=0.014223
32s_plus count=1435 mean=0.038498 p95=0.000000 gt2=0.004181
```

Por bucket de throughput:

```text
lte_1_mbps count=1680 mean=0.260544 p95=1.350002 gt2=0.004167
1_2_mbps   count=1080 mean=0.264171 p95=1.150000 gt2=0.004630
2_5_mbps   count=2280 mean=0.681876 p95=3.100000 gt2=0.088596
5_20_mbps  count=1560 mean=0.444883 p95=2.000000 gt2=0.050000
gt_20_mbps count=840  mean=0.381668 p95=0.450001 gt2=0.042857
```

Por rollout policy:

```text
qh_minus_one         count=1860 mean=0.368953 p95=1.450001 gt2=0.030645
qh_oracle            count=1860 mean=0.357390 p95=1.350000 gt2=0.033333
qh_plus_one          count=1860 mean=0.657293 p95=2.886339 gt2=0.059140
startup_conservative count=1860 mean=0.386426 p95=2.471927 gt2=0.053226
```

Hecho observado: el GRU empeora respecto al MLP precisamente en varios buckets
que ya eran problematicos en el MLP.

## Estado actual del bloqueo

No hay PASS del scorer pilot v3. El mejor resultado actual es:

```text
run=qh_scorer_pilot_adv_regret_dataset_pilot_seed450924_v1
profile=pilot_adv_regret_v1
architecture=shared_mlp_qh_candidate_scorer
status=REVIEW
mean_regret_q_h=0.395739
gate_mean_regret_q_h=0.35
exceso_absoluto=0.045739
```

Gates del mejor intento:

```text
top1_accuracy=0.788844 >= 0.55 PASS
high_capacity_predicted_action0_rate=0.002946 <= 0.05 PASS
mean_regret_q_h=0.395739 <= 0.35 FAIL
```

El bloqueo concreto es:

```text
El modelo pasa top1_accuracy y anti-colapso en alta capacidad, pero no alcanza
mean_regret_q_h <= 0.35 en validacion del dataset pilot.
```

El avance numerico existe, pero no hay avance de paso:

```text
El pipeline no deberia avanzar a full/integracion bajo el gate actual porque el
mejor mean_regret_q_h observado es 0.395739.
```

## Observaciones factuales del bloqueo

1. Alta capacidad ya no reproduce el colapso SPBC.

```text
MLP high_capacity_state=true mean_regret_q_h=0.056697 p95=0.000000
MLP high_capacity_predicted_action0_rate=0.002946
```

2. El peso principal del regret esta en estados que no son high-capacity-safe.

```text
MLP high_capacity_state=false mean_regret_q_h=0.495922
MLP high_capacity_state=true  mean_regret_q_h=0.056697
```

3. El bucket `2_5_mbps` es el bucket grande con peor media.

```text
MLP 2_5_mbps count=2280 mean_regret_q_h=0.593478 p95=3.000000
```

4. `qh_plus_one` es el rollout con peor media.

```text
MLP qh_plus_one count=1860 mean_regret_q_h=0.623309 p95=2.474163
```

5. Los buckets de buffer mas bajos o medios concentran mucho regret.

```text
MLP 00_04s mean=0.760336
MLP 04_08s mean=0.499127
MLP 08_16s mean=0.437616
MLP 32s_plus mean=0.035017
```

6. Las acciones predichas 3 y 4 tienen media de regret alta.

```text
MLP pred=3 mean=0.643990
MLP pred=4 mean=0.835449
```

7. Tambien existen errores severos con `predicted_action=5`, pero la media de
esa accion predicha es baja porque muchos casos de accion 5 son correctos.

```text
MLP pred=5 count=3104 mean=0.147551 max=127.994537
```

8. El GRU no reduce el bloqueo en este pilot.

```text
MLP mean_regret_q_h=0.395739
GRU mean_regret_q_h=0.442516
```

## Comandos de reproduccion usados

Generacion/validacion dataset pilot:

```bash
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate
python3 scripts/generate_phase45_v3_qh_dataset.py --profile pilot --overwrite
python3 scripts/summarize_phase45_v3_qh_dataset.py --profile pilot
```

Entrenamiento `pilot_adv_regret_v1`:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/run_phase45_v3_qh_scorer_pilot_adv_regret_wsl.sh
```

Entrenamiento `pilot_adv_regret_gru_v1`:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/run_phase45_v3_qh_scorer_pilot_adv_regret_gru_wsl.sh
```

Analisis de errores:

```bash
cd ~/TFG/DashClientModular4
source ~/venvs/rocm721/bin/activate
python3 scripts/analyze_phase45_v3_qh_scorer_errors.py \
  --run-name qh_scorer_pilot_adv_regret_dataset_pilot_seed450924_v1 \
  --dataset-dir ~/TFG/datasets_normalizados/phase45_v3/qh_closed_loop_pilot \
  --top-n 25
python3 scripts/analyze_phase45_v3_qh_scorer_errors.py \
  --run-name qh_scorer_pilot_adv_regret_gru_dataset_pilot_seed450925_v1 \
  --dataset-dir ~/TFG/datasets_normalizados/phase45_v3/qh_closed_loop_pilot \
  --top-n 0
```

## Validaciones locales de codigo

Validaciones realizadas tras anadir el analizador de errores:

```text
git diff --check: PASS
python -m unittest tests.test_phase45_v3_qh_scorer_losses tests.test_phase45_v3_dataset: PASS
python -m unittest discover: 429 tests OK
python scripts/check_client_readiness.py --strict: PASS
```

## Preguntas objetivas para ayuda externa

1. Que causas tecnicas son compatibles con que el modelo tenga buena top1
accuracy y buen anti-colapso en alta capacidad, pero siga fallando
`mean_regret_q_h <= 0.35`?

2. Que lectura objetiva debe hacerse de que el regret se concentre en
`2_5_mbps`, `qh_plus_one`, buffers `00_04s` a `16_32s`, y predicciones 3/4?

3. Que riesgos de interpretacion hay al mirar solo `top1_accuracy` en este
problema de ABR con targets `Q_H(s,a)`?

4. Que datos adicionales deberian inspeccionarse antes de afirmar que el
bloqueo es de arquitectura, de objetivo de entrenamiento, de dataset, de target
oracle o de distribucion de trazas?

5. Que inconsistencias potenciales deberian descartarse entre dataset,
normalizacion, features visibles, mask de acciones, target `Q_H`, reward
`qoe_linear_v1` y dinamica runtime antes de continuar?

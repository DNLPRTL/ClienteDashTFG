# Informe objetivo de bloqueo para ayuda externa - Phase45 v3 Q_H scorer pilot

Fecha: 2026-06-12

Estado del documento: informe objetivo para pedir ayuda externa. No contiene
propuestas de solucion, recomendaciones de siguiente experimento, ranking,
benchmark ni afirmaciones de mejora de QoE.

## Solicitud a ChatGPT u otra IA

Analizar objetivamente el bloqueo descrito en este informe. Identificar, a
partir de los hechos documentados, posibles causas tecnicas, riesgos de
interpretacion y datos adicionales que convendria revisar. No asumir que hay
benchmark final ni que existe mejora de QoE autorizada.

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

Repositorio Windows:

```text
C:\Users\danie\Documents\TFG\DashClientModular4
```

Repositorio WSL2 recomendado:

```text
/home/danie/TFG/DashClientModular4
```

Raiz de artefactos pesados en WSL2:

```text
/home/danie/TFG
```

Entorno WSL2/ROCm observado:

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

Contrato de paridad documentado por el dataset pilot:

```text
parity_scope=ABR decision dynamics used by the client and Phase 6 trace replay
qoe_formula_version=qoe_linear_v1
reward=bitrate_mbps - 4.3 * rebuffer_s - smoothness_mbps
segment_duration_s=4.0
segment_count=30
max_buffer_s=60.0
representation_bitrates_bps=[300000,750000,1200000,1850000,2850000,4300000]
network_source=TraceDrivenNetworkModel over normalized throughput_kbps windows
controller_visible_inputs_match_runtime_feature_builder=True
```

Elementos no reproducidos por el entorno cerrado:

```text
HTTP server process
GStreamer media pipeline
OS scheduling jitter
```

## Dataset usado en los pilots

Ruta:

```text
/home/danie/TFG/datasets_normalizados/phase45_v3/qh_closed_loop_pilot
```

Comando de resumen ejecutado:

```bash
cd ~/TFG/DashClientModular4
python3 scripts/summarize_phase45_v3_qh_dataset.py --profile pilot
```

Salida compacta:

```text
phase45_v3_qh_dataset status=PASS profile=pilot samples={'training': 30600, 'validation': 7440} max_buffer_s=60.0 qh=PASS leakage=PASS fallback_count=0 target_action0_rate=0.159858 high_capacity_safe_state_count=7783 high_capacity_safe_target_action0_rate=0.01529 target_actions={'0': 6081, '1': 4998, '2': 4667, '3': 4308, '4': 3446, '5': 14540} rollouts={'qh_minus_one': 9510, 'qh_oracle': 9510, 'qh_plus_one': 9510, 'startup_conservative': 9510} q_h_reward_mean=-16.552883
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

Auditoria Q_H:

```text
status=PASS
errors=[]
high_capacity_safe_state_count=7783
high_capacity_safe_target_action0_rate=0.01529
target_action_distribution={'0': 6081, '1': 4998, '2': 4667, '3': 4308, '4': 3446, '5': 14540}
```

Auditoria de no contaminacion:

```text
status=PASS
errors=[]
skipped_window_count=3
```

Este dataset no es benchmark. Sus salidas mantienen:

```text
benchmark_performed=false
outputs_are_benchmark_results=false
ranking_performed=false
no_final_ranking=true
```

## Modelo entrenado

Modelo:

```text
model_key=phase45_v3_qh_scorer
model_type=shared_mlp_qh_candidate_scorer
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

El gate bloqueante en los tres pilots fue:

```text
mean_regret_q_h
```

## Intentos ejecutados

### 1. `pilot`

Ruta:

```text
/home/danie/TFG/modelos/phase45_v3/qh_scorer/qh_scorer_pilot_dataset_pilot_seed450921_v1
```

Modelo:

```text
/home/danie/TFG/modelos/phase45_v3/qh_scorer/qh_scorer_pilot_dataset_pilot_seed450921_v1/modelo_phase45_v3_qh_scorer.pt
sha256=36fda2478f96e33f3ef72789b89d8d5c19304451ba0daab7e3bbb8cb1c196eb0
```

Resultado:

```text
status=REVIEW
failed=['mean_regret_q_h']
train_sample_count=30600
validation_sample_count=7440
elapsed_s=7.219
top1_accuracy=0.792473
mean_regret_q_h=0.59434
p95_regret_q_h=1.65
high_capacity_predicted_action0_rate=0.001179
predicted_action_distribution={'0': 1317, '1': 970, '2': 835, '3': 626, '4': 506, '5': 3186}
target_action_distribution={'0': 1131, '1': 899, '2': 831, '3': 724, '4': 609, '5': 3246}
```

### 2. `pilot_plus`

Ruta:

```text
/home/danie/TFG/modelos/phase45_v3/qh_scorer/qh_scorer_pilot_plus_dataset_pilot_seed450922_v1
```

Modelo:

```text
/home/danie/TFG/modelos/phase45_v3/qh_scorer/qh_scorer_pilot_plus_dataset_pilot_seed450922_v1/modelo_phase45_v3_qh_scorer.pt
sha256=f3b2b6147ef011e8cdc4d784bca90aa28fe20a72d6c11a8d9f7beedef4aa99d5
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
train_sample_count=30600
validation_sample_count=7440
elapsed_s=14.183
top1_accuracy=0.802285
mean_regret_q_h=0.550857
p95_regret_q_h=1.549999
high_capacity_predicted_action0_rate=0.001179
predicted_action_distribution={'0': 1354, '1': 851, '2': 917, '3': 625, '4': 546, '5': 3147}
target_action_distribution={'0': 1131, '1': 899, '2': 831, '3': 724, '4': 609, '5': 3246}
```

### 3. `pilot_rank`

Ruta:

```text
/home/danie/TFG/modelos/phase45_v3/qh_scorer/qh_scorer_pilot_rank_dataset_pilot_seed450923_v1
```

Modelo:

```text
/home/danie/TFG/modelos/phase45_v3/qh_scorer/qh_scorer_pilot_rank_dataset_pilot_seed450923_v1/modelo_phase45_v3_qh_scorer.pt
sha256=8ade3c2bd411ff66329bd308a69d00b973e9393f2db2e8cfc8fcbb1d34510b10
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
train_sample_count=30600
validation_sample_count=7440
elapsed_s=16.115
top1_accuracy=0.79207
mean_regret_q_h=0.476182
p95_regret_q_h=1.599998
high_capacity_predicted_action0_rate=0.001179
predicted_action_distribution={'0': 1362, '1': 973, '2': 847, '3': 657, '4': 540, '5': 3061}
target_action_distribution={'0': 1131, '1': 899, '2': 831, '3': 724, '4': 609, '5': 3246}
```

Ultimas epocas observadas en `pilot_rank`:

```text
epoch=24 mean_regret_q_h=0.672477 top1_accuracy=0.815591 p95_regret_q_h=1.450001
epoch=25 mean_regret_q_h=0.593206 top1_accuracy=0.813978 p95_regret_q_h=1.471334
epoch=26 mean_regret_q_h=0.687947 top1_accuracy=0.817876 p95_regret_q_h=1.489798
epoch=27 mean_regret_q_h=0.672319 top1_accuracy=0.815323 p95_regret_q_h=1.450001
epoch=28 mean_regret_q_h=0.539624 top1_accuracy=0.817204 p95_regret_q_h=1.450001
best_state_final mean_regret_q_h=0.476182
```

## Comparacion factual entre intentos

```text
pilot      mean_regret_q_h=0.59434   top1=0.792473 high_capacity_action0=0.001179 status=REVIEW
pilot_plus mean_regret_q_h=0.550857  top1=0.802285 high_capacity_action0=0.001179 status=REVIEW
pilot_rank mean_regret_q_h=0.476182  top1=0.79207  high_capacity_action0=0.001179 status=REVIEW
```

Reduccion de `mean_regret_q_h`:

```text
pilot -> pilot_plus: 0.043483 absoluta
pilot_plus -> pilot_rank: 0.074675 absoluta
pilot -> pilot_rank: 0.118158 absoluta
```

El mejor intento sigue por encima del gate:

```text
mejor_mean_regret_q_h=0.476182
gate_mean_regret_q_h=0.35
exceso_absoluto=0.126182
```

Los gates no bloqueantes pasan en el mejor intento:

```text
top1_accuracy=0.79207 >= 0.55
high_capacity_predicted_action0_rate=0.001179 <= 0.05
```

## Cambios de codigo relacionados

Commits relevantes recientes:

```text
c81911a feat(phase45): add regret-aware QH scorer profile
e8d07b6 chore(phase45): add QH scorer pilot rank WSL runbook
```

Archivos principales:

```text
core/phase45_v3/qh_scorer_training.py
scripts/train_phase45_v3_qh_scorer.py
scripts/run_phase45_v3_qh_scorer_pilot_rank_wsl.sh
tests/test_phase45_v3_dataset.py
```

`pilot_rank` anadio una perdida pairwise de ranking sobre `Q_H`:

```text
pairwise_rank_loss_weight=1.1
pairwise_margin_scale=1.0
pairwise_q_gap_cap=4.0
```

Validaciones Windows tras anadir `pilot_rank`:

```text
git diff --check: PASS
python -m unittest discover: 424 tests OK
python scripts/check_client_readiness.py --strict: PASS
```

## Estado actual del bloqueo

No hay PASS del scorer pilot v3. El mejor resultado actual es `pilot_rank`, con
`status=REVIEW`.

El bloqueo concreto es:

```text
El modelo pasa top1_accuracy y anti-colapso en alta capacidad, pero no alcanza
mean_regret_q_h <= 0.35 en validacion del dataset pilot.
```

El avance numerico existe, pero no hay avance de paso:

```text
El pipeline no deberia avanzar a full/integracion bajo el gate actual porque el
mejor mean_regret_q_h observado es 0.476182.
```

## Limites de interpretacion

Estas ejecuciones son entrenamiento/validacion offline de modelo candidato.

No autorizan:

```text
benchmark_performed
ranking_performed
winner
QoE improvement claim
generalizacion real-world
```

El modelo `phase45_v3_qh_scorer` aun no esta integrado como controller final ni
evaluado en Phase6 formal.

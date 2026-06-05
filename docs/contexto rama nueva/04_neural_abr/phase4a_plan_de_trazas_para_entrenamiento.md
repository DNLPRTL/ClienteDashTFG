# Phase 4A - Plan de trazas para entrenamiento

Status: implemented_on_windows_pending_ubuntu_validation.

## Proposito

Phase 4A prepara el plan de trazas que se usara mas adelante para entrenar
NeuralABR-Lite offline. Esta fase no entrena IA, no genera labels de teacher y
no declara resultados.

Entrada canonica:

```text
C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\phase3_trace_manifest_curated.json
```

Salidas externas esperadas:

```text
C:\Users\danie\Documents\TFG\manifests_trazas\phase4\phase4A_plan_de_trazas_para_entrenamiento\phase4_indice_de_ventanas_de_traza.json
C:\Users\danie\Documents\TFG\manifests_trazas\phase4\phase4A_plan_de_trazas_para_entrenamiento\phase4_plan_de_trazas_para_entrenamiento.json
C:\Users\danie\Documents\TFG\manifests_trazas\phase4\phase4A_plan_de_trazas_para_entrenamiento\phase4_auditoria_de_seleccion_de_trazas.json
```

En Ubuntu cliente, las mismas salidas deben quedar bajo:

```text
$HOME/TFG/manifests_trazas/phase4/phase4A_plan_de_trazas_para_entrenamiento
```

## Decisiones cerradas

- Segmento primario: `4s`.
- Segmento `2s`: diagnostico posterior, no objetivo primario de Phase 4A.
- Ventana temporal: `120s`.
- Cada ventana contiene 30 decisiones teoricas de 4s.
- `split=train` alimenta el plan de entrenamiento.
- `split=test` alimenta validacion interna offline.
- `split=eval` queda reservado para evaluacion posterior y no se selecciona.
- Trazas sinteticas: cuota maxima por defecto `15%`.
- Dataset dominante, incluido FCC: cuota maxima por defecto `30%`.
- Semantica dominante: cuota maxima por defecto `35%`.
- Dificultad dominante: cuota maxima por defecto `45%`.
- Maximo por traza: 3 ventanas seleccionadas por rol.
- Si las cuotas estrictas impiden llenar el objetivo solicitado, el sampler no
  relaja los caps automaticamente. El audit reporta `unfilled_target_count`.

## Politica de no contaminacion

El plan puede contener metadatos para auditoria, como `trace_id`, `dataset_id`,
`semantics`, `leakage_group` y `source_split`. Esos campos no son features del
modelo.

Quedan prohibidos como features:

```text
trace_id
dataset_id
source_id
split
source_split
training_plan_role
group_id
leakage_group
semantics
network_condition
synthetic
synthetic_scenario
future_throughput_kbps
future_reward
future_qoe
final_qoe
teacher_action
benchmark_rank
```

## Comando Windows

```powershell
python scripts/build_phase4_training_trace_plan.py --manifest "C:\Users\danie\Documents\TFG\manifests_trazas\phase3\final\phase3_trace_manifest_curated.json" --output-root "C:\Users\danie\Documents\TFG\manifests_trazas\phase4\phase4A_plan_de_trazas_para_entrenamiento" --segment-duration-s 4 --window-duration-s 120 --synthetic-max-fraction 0.15 --seed phase4a_training_trace_sampler_v1
```

## Comando Ubuntu cliente

```bash
cd ~/TFG/DashClientModular4
git pull --ff-only origin rebuild/phase3-from-phase2
python -m unittest discover
python scripts/check_client_readiness.py --strict
python scripts/validate_phase3_trace_manifest.py --manifest "$HOME/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json"
python scripts/build_phase4_training_trace_plan.py \
  --manifest "$HOME/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json" \
  --output-root "$HOME/TFG/manifests_trazas/phase4/phase4A_plan_de_trazas_para_entrenamiento" \
  --segment-duration-s 4 \
  --window-duration-s 120 \
  --synthetic-max-fraction 0.15 \
  --seed phase4a_training_trace_sampler_v1
```

Resultado esperado:

```text
status=PASS
benchmark_performed=false
ia_training_performed=false
ranking_performed=false
```

## Limites

Phase 4A no produce datos finales para entrenar. Produce un plan de ventanas y
una auditoria. Los datos con muestras, labels de `robust_mpc`, normalizacion y
prueba rapida de entrenamiento pertenecen a Phase 4B/C/D.

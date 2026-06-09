# Runbook Phase 4-5 v2 - Dataset enriquecido preference/on-policy

## Objetivo

Generar el dataset externo `phase45v2_preference_onpolicy_dataset_v1` para el
Bloque 7A. Este dataset conserva el contrato v1 intacto y anade:

- superficie QoE inmediata por accion;
- gaps QoE;
- pares de preferencia multiples;
- rollout `oracle_rollout`;
- rollout `spbc_v1_on_policy` si existe checkpoint `spbc_abr_v1/full_v1`.

Este bloque no entrena modelos, no exporta bundles, no registra controllers, no
ejecuta Phase 6 y no autoriza benchmark, ranking ni mejora QoE.

## Entradas

Manifest y trazas normalizadas bajo WSL2:

```bash
~/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json
~/TFG/datasets_normalizados/phase3/final/
```

Checkpoint on-policy recomendado:

```bash
~/TFG/modelos/phase45_v1/spbc_abr_v1/full_v1/modelo_spbc_abr_v1.pt
```

## Salida externa

```bash
~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dataset_v1/
```

No commitear esta carpeta.

## Sincronizacion WSL2

```bash
cd ~/TFG/DashClientModular4
git status --short --branch
git pull

source ~/venvs/rocm721/bin/activate
python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

La salida esperada es `True` y la GPU AMD expuesta por ROCm.

## Smoke

```bash
python3 scripts/build_phase45_v2_dataset.py \
  --profile smoke \
  --overwrite \
  --trace-path-rewrite /home/daniel/TFG=$HOME/TFG \
  --trace-path-rewrite /home/danie/TFG=$HOME/TFG
```

Si el checkpoint `spbc_abr_v1/full_v1` no existe, `smoke` puede generar solo
`oracle_rollout` para validar rutas y contrato.

## Pilot

```bash
python3 scripts/build_phase45_v2_dataset.py \
  --profile pilot \
  --overwrite \
  --trace-path-rewrite /home/daniel/TFG=$HOME/TFG \
  --trace-path-rewrite /home/danie/TFG=$HOME/TFG
```

## Full recomendado

```bash
python3 scripts/build_phase45_v2_dataset.py \
  --profile full_v1 \
  --overwrite \
  --device auto \
  --trace-path-rewrite /home/daniel/TFG=$HOME/TFG \
  --trace-path-rewrite /home/danie/TFG=$HOME/TFG
```

`full_v1` falla si no encuentra el checkpoint `spbc_abr_v1/full_v1`. Esto evita
generar por accidente un dataset v2 sin la parte on-policy.

Solo para diagnostico explicito sin on-policy:

```bash
python3 scripts/build_phase45_v2_dataset.py \
  --profile full_v1 \
  --overwrite \
  --allow-oracle-only-full \
  --trace-path-rewrite /home/daniel/TFG=$HOME/TFG \
  --trace-path-rewrite /home/danie/TFG=$HOME/TFG
```

## Validacion de un dataset existente

```bash
python3 scripts/build_phase45_v2_dataset.py \
  --validate-only \
  --output-dir ~/TFG/datasets_normalizados/phase45_v1/phase45v2_preference_onpolicy_dataset_v1
```

La salida esperada incluye:

```json
{
  "status": "PASS",
  "sample_counts": {
    "training": 0,
    "validation": 0
  }
}
```

Los conteos reales no seran cero; este bloque solo muestra la forma del JSON.

## Contrato

- `eval` queda excluido.
- Los splits se respetan por `leakage_group`.
- `metadata`, futuro throughput, oracle y accion spbc no son inputs del modelo.
- `per_action_outcomes` contiene `reward_n`, `qoe_gap`,
  `estimated_rebuffer_s`, `smoothness_mbps`, `bitrate_kbps` y `valid_action`.
- `preference_pairs` es una lista y puede contener varias fuentes por muestra.
- Las salidas mantienen `benchmark_performed=false`,
  `ranking_performed=false`, `no_final_ranking=true` e
  `ia_training_performed=false`.

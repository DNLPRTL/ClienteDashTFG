# Runbook SPBC v2 DPO controller en Phase 6

Fecha: 2026-06-11.

Este runbook integra el candidato:

```text
controller_key=spbc_abr_v2_dpo_anchor_safe_rank
alias_phase6=propio_spbc_v2_anchor
modelo_fuente_wsl=/home/danie/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1/modelo_spbc_abr_v2_dpo.pt
bundle_wsl=/home/danie/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1_bundle
bundle_ubuntu_cliente=/home/daniel/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1_bundle
```

No es benchmark. No autoriza ranking ni mejora de QoE antes de Phase 6 formal.

## 1. Exportar bundle en WSL

```bash
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate
python3 scripts/export_phase45_v2_spbc_dpo_bundle.py \
  --expected-checkpoint-sha256 43b4d012448e12885fac8cbfec914aab6450e0c1b146a4bb8534e8b90b61c227 \
  --overwrite
python3 scripts/validate_phase45_v2_spbc_dpo_bundle.py
```

## 2. Copiar bundle a Ubuntu cliente

Sustituir `<IP_UBUNTU_CLIENTE>` por la IP real de la VM cliente.

```bash
tar -C ~/TFG/modelos/phase45_v1/spbc_abr_v2_dpo \
  -czf /tmp/full_v2_anchor_safe_rank_v1_bundle.tgz \
  full_v2_anchor_safe_rank_v1_bundle
scp /tmp/full_v2_anchor_safe_rank_v1_bundle.tgz daniel@<IP_UBUNTU_CLIENTE>:/tmp/
```

En Ubuntu cliente:

```bash
mkdir -p /home/daniel/TFG/modelos/phase45_v1/spbc_abr_v2_dpo
tar -C /home/daniel/TFG/modelos/phase45_v1/spbc_abr_v2_dpo \
  -xzf /tmp/full_v2_anchor_safe_rank_v1_bundle.tgz
cd /home/daniel/TFG/DashClientModular4
git pull
python3 scripts/validate_phase45_v2_spbc_dpo_bundle.py \
  --bundle-dir /home/daniel/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1_bundle
```

## 3. Carpetas hermanas esperadas en Ubuntu cliente

Necesarias para Phase 6:

```text
/home/daniel/TFG/DashClientModular4
/home/daniel/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json
/home/daniel/TFG/datasets_normalizados/phase3/final/
/home/daniel/TFG/modelos/phase45_v1/spbc_abr_v2_dpo/full_v2_anchor_safe_rank_v1_bundle/
/home/daniel/TFG/runs_trazas/phase6/validacion_comparativa/
```

Solo si se comparan tambien los dos IA antiguos:

```text
/home/daniel/TFG/modelos/phase4/phase4F_bundle_para_inferencia_neural_abr_lite/
/home/daniel/TFG/modelos/phase4/phase4H_bundle_para_inferencia_teacher_hibrido_neural_abr_lite/
```

Si manifest/trazas no estan ya en Ubuntu cliente, copiarlas desde WSL:

```bash
rsync -a ~/TFG/manifests_trazas/phase3/final/ \
  daniel@<IP_UBUNTU_CLIENTE>:/home/daniel/TFG/manifests_trazas/phase3/final/
rsync -a ~/TFG/datasets_normalizados/phase3/final/ \
  daniel@<IP_UBUNTU_CLIENTE>:/home/daniel/TFG/datasets_normalizados/phase3/final/
```

## 4. Opciones recomendadas en GUI Phase 6

Primer preflight:

```text
Preset: diagnostico
Motor: fake
Reanudar: activado
Dry run: desactivado
Solo plan: desactivado
Sin analisis: desactivado
Controllers: Robust MPC + Propio SPBC v2 Anchor
```

Si el preflight sale limpio:

```text
Preset: rapido
Motor: fake
Controllers: Rate Based, BBA, BOLA, MPC, Robust MPC, Propio SPBC v2 Anchor
```

Si se quiere comparar tambien contra los dos IA antiguos y sus bundles existen:

```text
Anadir: Propio RMP, Propio TH
```

Primer preset con capacidad formal de benchmark si los gates pasan:

```text
Preset: equilibrado
Motor: fake
Controllers: Rate Based, BBA, BOLA, MPC, Robust MPC, Propio SPBC v2 Anchor
```

## 5. Comandos CLI equivalentes

Diagnostico con config por defecto:

```bash
cd /home/daniel/TFG/DashClientModular4
git pull
python3 scripts/run_phase6_validacion_comparativa.py --preset diagnostico --resume
```

Rapido:

```bash
python3 scripts/run_phase6_validacion_comparativa.py --preset rapido --resume
```

Equilibrado:

```bash
python3 scripts/run_phase6_validacion_comparativa.py --preset equilibrado --resume
```

La GUI genera una config temporal si se seleccionan controllers manualmente.
Para comparar un subconjunto fijo por CLI, crear una config local con
`experiment.controllers`.

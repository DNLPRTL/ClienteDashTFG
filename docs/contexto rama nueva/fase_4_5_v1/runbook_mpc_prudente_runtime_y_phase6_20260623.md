# Runbook — MPC Prudente: runtime + bundle + Phase 6 (cierre opción A)

| Campo | Valor |
|---|---|
| Fecha | 2026-06-23 |
| Autor | Claude (Claude Code) |
| Rama | `rebuild/phase3-from-phase2` |
| Estado | Controller runtime + bundle + registro + Phase 6 config listos y probados en Windows. Pendiente: ejecutar el pipeline en WSL/Ubuntu. |

## Qué se montó (opción A)

- `core/controller/mpc_prudente_runtime.py`: controller `mpc_prudente_v1` integrado
  en el cliente. Carga el bundle, reconstruye la **MediaFaithfulLadder** (tamaños
  reales VBR), planifica con CVaR (`risk_alpha=0.75`), con fallback a robust_mpc,
  safety guard, verificación de hash y diagnósticos neurales.
- `core/mpc_prudente/bundle.py`: export/validate del bundle (predictor + config del
  planner + hashes sha256; carga `weights_only=True`).
- Registrado en `core/controller/registry.py` (`mpc_prudente_v1`) y alias Phase 6
  `propio_mpc_prudente` (para que los gates auditen la inferencia neural).
- `config/phase6.mpc_prudente.local.example.json`: compara `rate_based, bola,
  robust_mpc, mpc_prudente_v1` en preset `diagnostico`.
- Probado en Windows: 480 tests OK, readiness PASS, export+validate del bundle PASS
  con el modelo real (risk_alpha=0.75, quantiles, horizon=5).

## Pipeline ordenado (lo que ejecuta Daniel)

### 1. (WSL) Entrenar el predictor final (si no está ya)
```bash
wsl -d Ubuntu-24.04
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate
bash scripts/run_mpc_prudente_pilot_training_wsl.sh
```
(Ya entrenado seed 451001 = PASS. Reusar ese sirve.)

### 2. (WSL) Exportar el bundle runtime
```bash
bash scripts/export_mpc_prudente_bundle_wsl.sh
# -> MPC_PRUDENTE_BUNDLE status=PASS  (bundle en ~/TFG/modelos/mpc_prudente/runtime_bundle_v1)
```

### 3. (WSL) Empaquetar el bundle para mover a Ubuntu cliente
```bash
bash scripts/package_mpc_prudente_bundle_transfer_wsl.sh
# -> tar en ~/TFG/paquetes_transfer/mpc_prudente_runtime_bundle_v1.tar.gz
```

### 4. (Daniel) Mover el tar a la VM cliente Ubuntu y descomprimir
```bash
# en Ubuntu cliente:
mkdir -p ~/TFG/modelos/mpc_prudente
tar -xzf <ruta>/mpc_prudente_runtime_bundle_v1.tar.gz -C ~/TFG/modelos/mpc_prudente/
```

### 5. (Ubuntu cliente) Sincronizar repo y validar el bundle
```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/validate_mpc_prudente_bundle_ubuntu_cliente.sh
# -> MPC_PRUDENTE_BUNDLE_VALIDATION status=PASS
```

### 6. (Ubuntu cliente) Phase 6 DIAGNOSTICO (smoke real + auditoría de inferencia)
```bash
cp config/phase6.mpc_prudente.local.example.json config/phase6.local.json
# Revisar que bundle_dir y output_root usan tu usuario real (daniel vs danie).
python3 scripts/run_phase6_validacion_comparativa.py --config config/phase6.local.json --preset diagnostico
python3 scripts/verificar_paquete_phase6.py --package-root <paquete_generado>
```

### 7. (Ubuntu cliente) Phase 6 COMPARATIVA — el resultado formal (recomendado)
Preset nuevo `comparativa`: 12 ventanas reales (balanceadas por capacidad/
variabilidad) + 3 sintéticas, 30 segmentos, 300 s, **autorizado para ranking**.
Solo `robust_mpc` + `mpc_prudente_v1` (cara a cara eficiente, ~1 h).
```bash
python3 scripts/run_phase6_validacion_comparativa.py --config config/phase6.local.json --preset comparativa
python3 scripts/verificar_paquete_phase6.py --package-root <paquete>
```
(El config de ejemplo ya trae `preset=comparativa` y `controllers=[robust_mpc, mpc_prudente_v1]`.)
En la GUI: el preset `comparativa` aparece solo en el desplegable y `Propio MPC
Prudente` en los checkboxes (la interfaz es data-driven; no hubo que tocarla).

## Qué mirar en los resultados (la vara correcta, ya nativa en Phase 6)

- `qoe_linear_mean` + CI95 + sign-test (media).
- **Cola/robustez**: `qoe_linear_min/p05`, `qoe_linear_std`, `delta_qoe_linear_worst`
  vs robust_mpc, `total_rebuffer_s_p95/max`, `session_gt_5s/10s_rebuffer_rate`,
  `worst_scenario_key`.
- Auditoría neural del propio: 0 fallback, inferencias auditadas, 0 acciones inválidas.
- Gráfica `qoe_robustez_peor_caso`.

## Importante (gestión de expectativas)

El diagnóstico interno (validación, simulación) NO es idéntico a Phase 6 (eval,
cliente real). La ventaja en la **cola** debería transferir; los números absolutos
diferirán. Phase 6 es el juez. Si convence → cerrada la parte técnica; si quieres
más, opción B (predictor temporal mejor) como mejora/ablación.

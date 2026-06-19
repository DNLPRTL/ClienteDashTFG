# Decisión — MPC Prudente: planner consciente del riesgo + diagnóstico closed-loop

| Campo | Valor |
|---|---|
| Fecha | 2026-06-19 |
| Autor | Claude (Claude Code) |
| Rama | `rebuild/phase3-from-phase2` |
| Plan padre | `plan_maestro_controller_ia_claude_20260619.md` |
| Estado | Implementado y previsualizado en Windows CPU. Pendiente: diagnóstico canónico en WSL (Daniel). |

## El planner prudente (el cerebro del controller)

`core/mpc_prudente/planner.py`. Arregla las dos debilidades del planner Neural-MPC:

1. **Fidelidad**: el planner viejo estimaba el tiempo de descarga con CBR
   (`bitrate*duración`). El prudente usa el **peso real (VBR)** del segmento
   (`ladder.segment_size_bytes`), igual que el cliente.
2. **Prudencia (riesgo)**: el viejo elegía UN cuantil de throughput con una regla
   fija buffer→cuantil. El prudente evalúa cada acción bajo **todos** los cuantiles
   predichos y agrega con **CVaR_alpha** (media de los peores escenarios). El nivel
   `alpha` baja con el buffer: poco buffer → mira el peor caso (q10), mucho buffer →
   expectativa neutral. Esto generaliza la regla a un objetivo de riesgo
   principiado (BayesMPC / control sensible al riesgo) y evita el `real_006`.

Demostrado en test: ante la misma situación con cola predictiva amplia, el planner
prudente (alpha bajo) elige un bitrate **más seguro** que el neutral (alpha=1).
Tiene fallback a `robust_mpc`, action mask y 0 acciones inválidas.

## Diagnóstico closed-loop (entorno FIEL)

`core/mpc_prudente/evaluation.py`. Corre prudente vs robust_mpc/bola/neural_mpc
viejo en el entorno closed-loop con el **ladder fiel**, sobre ventanas de
validación. Reporta QoE/rebuffer por controller, deltas emparejados vs robust_mpc
(globales y por bucket de variabilidad) y gates anti-colapso (fallback=0,
invalid=0, high_capacity_action0≤0.05, QoE no catastrófica, rebuffer acotado).

## Preview en Windows CPU (6 ventanas de validación, modelo pilot)

```
status=PASS
prudent_qoe=2.3816   robust_qoe=2.4147   (qoe_delta=-0.033)
prudent_rebuffer=4.049   robust_rebuffer=4.049   (rebuffer_delta=0.0)
fallback=0   invalid=0
```

Lectura honesta:
- **Competitivo y seguro**: prudente empata a robust_mpc (QoE -0.03, sin rebuffer
  extra), sin fallback ni acciones inválidas. Contrasta con el Neural-MPC v2 viejo
  (-0.40 vs robust y desastre en `real_006`).
- Muestra pequeña (6 ventanas); el valor de la prudencia se ve en ventanas
  **variables** duras, que pueden no estar en estas 6. El diagnóstico canónico con
  más ventanas (incluyendo variables) dirá el delta real.

## Cómo ejecutar el diagnóstico canónico (Daniel, WSL — CPU)

```bash
wsl -d Ubuntu-24.04
cd ~/TFG/DashClientModular4
git pull
source ~/venvs/rocm721/bin/activate
bash scripts/run_mpc_prudente_pilot_diagnostic_wsl.sh
```

Pegar la línea `MPC_PRUDENTE_DIAGNOSTIC status=...`. Nos fijamos en `qoe_delta`,
`rebuffer_delta`, `variable_rebuffer_delta`, `fallback` e `invalid`.

## Siguiente paso

Según el diagnóstico: si prudente es competitivo/seguro (esperado), integrar el
**controller runtime** en el cliente (bundle + registro + safety guard + hash) y
llevarlo a **Phase 6** diagnóstico/rápido contra robust_mpc/bola/rate_based. Es
donde se autoriza (con gates) la comparación formal.

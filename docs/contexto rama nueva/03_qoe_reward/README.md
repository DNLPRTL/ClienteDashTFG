# Phase 3.5 Rebuild - QoE, reward y gates

Status: closed_phase3_5_rebuild_after_validation.

Phase 3.5 Rebuild define como se calcula QoE y que artifacts pueden considerarse evaluables en fases posteriores. Esta fase no ejecuta benchmark, no entrena IA, no compara controllers y no declara ganadores.

## Decision principal

```text
qoe_formula_version = qoe_linear_v1
primary_session_metric = qoe_linear_mean
segment_reward_candidate = reward_n
secondary_metric = qoe_log_v1
startup_delay_s = report_only
VMAF = deferred_artifact_dependent
```

Formula por segmento:

```text
bitrate_mbps = representation_bitrate_kbps / 1000.0
smoothness_mbps = 0.0 if first segment else abs(bitrate_mbps_n - bitrate_mbps_n-1)
reward_n = bitrate_mbps - 4.3 * rebuffer_s - smoothness_mbps
```

QoE de sesion:

```text
qoe_linear_sum = sum(reward_n)
qoe_linear_mean = qoe_linear_sum / segment_count
```

## Relacion con Phase 3 nueva

Phase 3 aporta trazas normalizadas y manifest curado. Phase 3.5 no consume esas trazas directamente; define el calculo que se aplicara a runs futuros. Los smokes de esta fase son sinteticos y controlados.

## Archivos clave

```text
qoe_selection.md
reward_definition.md
secondary_metrics.md
evaluation_gate_policy.md
qoe_artifact_computation_spec.md
no_ranking_policy.md
phase3_5_results_boundary.md
phase3_5_closure_report.md
phase3_5_transition_to_phase4.md
```

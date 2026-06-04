# Secondary metrics

Status: closed_phase3_5_rebuild_contract.

Metricas secundarias:

```text
qoe_log_v1
avg_bitrate_kbps
total_rebuffer_s
stall_event_count
quality_switch_count
up_switch_count
down_switch_count
total_switch_magnitude_kbps
avg_switch_magnitude_kbps
startup_delay_s report_only
```

`qoe_log_v1` usa utilidad logaritmica y requiere `min_bitrate_kbps` explicito. No se infiere desde la propia sesion porque eso haria que sesiones distintas no fueran comparables.

`startup_delay_s` se reporta si existe, pero no se penaliza en `qoe_linear_v1`.

VMAF queda diferido hasta que existan artifacts perceptuales reproducibles.

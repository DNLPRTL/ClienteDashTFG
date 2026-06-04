# Reward definition

Status: closed_phase3_5_rebuild_contract.

## Formula version

```text
qoe_formula_version = qoe_linear_v1
```

## Segment reward

Para cada segmento `n`:

```text
bitrate_mbps_n = representation_bitrate_kbps_n / 1000.0
smoothness_mbps_n = 0.0 if n == 0 else abs(bitrate_mbps_n - bitrate_mbps_n-1)
reward_n = bitrate_mbps_n - 4.3 * rebuffer_s_n - smoothness_mbps_n
```

Unidades:

```text
representation_bitrate_kbps: kbps
bitrate_mbps: Mbps utility
rebuffer_s: seconds
smoothness_mbps: Mbps delta
reward_n: QoE utility units
```

## Session QoE

```text
qoe_linear_sum = sum(reward_n)
qoe_linear_mean = qoe_linear_sum / segment_count
```

`qoe_linear_mean` sera la metrica primaria futura para resumen de sesion cuando exista protocolo de evaluacion formal.

## IA boundary

`reward_n` es candidato para Phase 4, pero Phase 3.5 no entrena ningun modelo ni selecciona algoritmo IA.

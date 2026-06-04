# Phase 6 Threats To Validity

Status: final Phase 6A2 protocol decision plus Phase 6B readiness hardening. Expanded from `threats_matrix.md`.

## Internal Validity

- Trace leakage from Phase 4 can invalidate fair `neural_abr_lite` comparison. Mitigation: block by `trace_id`, `leakage_group`, `checksum_sha256` and `canonical_content_fingerprint`.
- Ghent aggregate/per-mobility duplicates can create hidden split leakage. Mitigation: use `logs_all` OR per-mobility folders unless deduplicated by checksum/fingerprint before split.
- Controller configuration drift can break comparability. Mitigation: freeze configs and include them in the evidence package.

## Construct Validity

- `qoe_linear_v1` is an objective reproducible QoE proxy, not subjective MOS. Mitigation: report QoE components and avoid MOS/VMAF claims without artifacts.
- Startup delay is report-only unless measured homogeneously.
- Segment rows are not independent statistical units. Mitigation: compare sessions/traces.

## External Validity

- HSDPA/Ghent same-family traces do not prove modern cellular or global Internet behavior.
- Raca 4G, Raca 5G and Lumos5G improve OOD coverage only after access/license/format and eligibility checks.
- Lancaster is not authorized for primary final evaluation until a source card/source note and clean audit exist.
- Small TFG-scale samples may make results underpowered. Mitigation: report uncertainty, effect sizes and limits.

## Ecological Validity

- Python trace-driven evaluation is reproducible but is not a live Internet deployment.
- VM server/content/demo work is not benchmark network evidence.
- Media-profile limitations may affect conclusions. Mitigation: freeze and report `media_profile_phase6_v1`.

## Reporting Validity

- No final winner should be declared from small or noisy samples.
- No `neural_abr_lite` QoE improvement claim is allowed unless the frozen protocol and evidence package support it.
- In Phase 6C, materialization and external manifest freeze are not `ready_for_benchmark` and `benchmark_authorized` remains false.
- Mixed, negative or inconclusive results must be reported without narrative pressure.

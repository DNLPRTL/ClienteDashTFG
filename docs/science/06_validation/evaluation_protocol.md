# Phase 6 Evaluation Protocol

Status: final Phase 6A2 protocol decision with Phase 6B readiness hardening. This protocol authorizes readiness work, not benchmark execution.

## Objective

Phase 6 will compare technical controls, academic baselines and the guarded `neural_abr_lite` controller under a frozen Python trace-driven protocol, using eligible traces and a shared deterministic media profile.

## Primary Path

The primary evaluation path remains Python trace-driven.

VM/content/demo infrastructure may support media_profile/content work, but VM bridge networking is not benchmark evidence.

## Controllers

Controllers in scope:

- `min_rate`;
- `fixed_rate`;
- `max_rate`;
- `rate_based`;
- `bba`;
- `bola`;
- `mpc`;
- `robust_mpc`;
- `neural_abr_lite`.

Controller classes and interpretation boundaries are frozen in `controller_matrix.md`.

## Trace Policy

Final trace IDs are not defined in this document. They must be frozen only by:

```text
phase6_trace_manifest_final.json
```

The final manifest must pass schema validation and eligibility audit. It must block overlap with Phase 4 by `trace_id`, `leakage_group`, `checksum_sha256` and `canonical_content_fingerprint`.

Recommended groups:

- `same_family_clean`;
- `OOD_final`;
- Lancaster excluded or `diagnostic_only` unless a source card/source note and clean audit exist.

## Media Profile

The primary media profile is `media_profile_phase6_v1`.

It must be deterministic, shared by all controllers and use an identical representation ladder. `segment_duration_s = 2.0` unless a real extracted MPD profile is frozen before execution.

## Metrics

Primary metric:

```text
qoe_linear_mean using qoe_linear_v1
```

Secondary metrics and gates are frozen in `metrics_schema.md`.

## Statistics

Statistical comparison uses session/trace as the unit. Future reports must include descriptive distributions, bootstrap 95% CI and paired comparisons by `trace_id` when sample size permits.

## Evidence Package

Future execution must produce an external evidence package aligned with `ubuntu_evidence_package_spec.md` and `reproducibility_checklist.md`.

## Non-Authorization

This protocol does not run a benchmark, produce plots, generate CSV result outputs, rank controllers, declare a winner, or claim that `neural_abr_lite` improves QoE.

In Phase 6C, materialization and external manifest freeze are not `ready_for_benchmark`; `benchmark_authorized` remains false.

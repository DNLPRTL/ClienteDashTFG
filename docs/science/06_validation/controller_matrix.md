# Phase 6 Controller Matrix

Status: final Phase 6A2 protocol decision. This matrix authorizes the next technical readiness phase, not benchmark execution.

## Controllers In Scope

| Controller key | Class | Role in Phase 6 | Interpretation boundary |
| --- | --- | --- | --- |
| `min_rate` | Technical control | Lower-bound deterministic control | Sanity/control only; not an academic ABR claim. |
| `fixed_rate` | Technical control | Fixed representation/rate behavior for stability checks | Sanity/control only; configuration must be frozen before runs. |
| `max_rate` | Technical control | Upper-bound stress/control behavior | Sanity/control only; expected to expose rebuffer risk under poor traces. |
| `rate_based` | Academic baseline | Throughput/rate-driven baseline | Baseline family comparator; no SOTA claim. |
| `bba` | Academic baseline | Buffer-based baseline | Serious academic baseline and stability reference. |
| `bola` | Academic baseline | Buffer/objective-based baseline | Serious academic baseline. |
| `mpc` | Academic baseline | Predictive/horizon baseline | Serious academic baseline. |
| `robust_mpc` | Academic baseline | Robust predictive baseline | Primary strong classical comparator for pairwise tables. |
| `neural_abr_lite` | Guarded neural scorer controller | Phase 5 integrated guarded neural scorer | Evaluated only if trace eligibility and artifact gates pass; no retraining or QoE-improvement presumption. |

## Inclusion Rules

- Every controller must run on the same frozen trace manifest, media profile, representation ladder and gate policy.
- Controller configuration must be captured in the future evidence package.
- `neural_abr_lite` must remain guarded by its Phase 5 action mask, safety guard and fallback behavior.
- Neural fallback/safety telemetry must be reported separately from primary QoE metrics.
- Technical controls are included to interpret behavior, not to declare academic winners.

## Non-Authorization

This matrix does not execute any controller, produce a ranking, or declare a winner.

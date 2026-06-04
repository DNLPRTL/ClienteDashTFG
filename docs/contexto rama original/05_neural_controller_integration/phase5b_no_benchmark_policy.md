# Phase 5B no benchmark policy

## Policy

Phase 5 structural smokes are not benchmarks.

## Allowed Phase 5 validation

Future Phase 5 implementation may validate:

- controller can load or fail closed;
- feature builder uses online-only data;
- action mask prevents invalid actions;
- safety guard can intervene;
- fallback does not crash;
- diagnostic telemetry is populated;
- fake engine smoke can execute the controller path.

## Forbidden Phase 5 output

Phase 5 must not produce:

- ranking;
- winner;
- improvement claim;
- formal QoE comparison;
- statistical significance;
- SOTA claim;
- real-world claim.

## Phase 6 requirement

Formal comparative validation belongs to Phase 6. Phase 6 must define traces, metrics, baselines, statistical handling and reporting rules before any ranking.

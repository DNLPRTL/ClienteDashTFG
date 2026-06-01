# Source card 09: CausalSim trace bias and contamination

## Title

CausalSim: A Causal Framework for Unbiased Trace-Driven Simulation.

## Authors

Abdullah Alomar, Pouya Hamadanian, Arash Nasr-Esfahany, Anish Agarwal, Mohammad Alizadeh, Devavrat Shah.

## Year

2023.

## Venue/type

USENIX NSDI; evaluation methodology source.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

CausalSim warns that trace-driven simulation can be biased because controller actions affect observed traces.

## Runtime integration pattern

The source is not a controller pattern. It is an evaluation and contamination warning.

## Runtime inputs

Observed traces and action-dependent outcomes. Phase 5 should not treat such logs as neutral training labels.

## Runtime action/output

Not applicable for controller action. The output is evaluation caution.

## Safety/fallback/action mask

No direct action mask transfer. The important transfer is diagnostic separation: telemetry is not automatically benchmark or training data.

## Latency/compute/deployment assumptions

Not a runtime compute source for Phase 5.

## What transfers to DashClientModular4

- Runtime neural telemetry is diagnostic-only.
- Logs are not automatically training data.
- Dry-run legacy labels must not be used as model labels.
- Phase 5 smoke is not a benchmark.

## What must not be copied

- CausalSim modeling algorithm.

## Phase 5 docs affected

- `phase5a1_telemetry_contamination_matrix.md`
- `phase5b_telemetry_contract.md`
- `phase5b_no_benchmark_policy.md`

## Memory/defense usage

Use this source in the evaluation and threats-to-validity chapters.

## Final decision

Transfer the contamination warning. Do not implement CausalSim.

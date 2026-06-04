# Phase 4E.1 External Trace Split Plan

## Split unit

The split unit is the trace, identified by `trace_id` and protected by `leakage_group`.

Rows from the same trace must never be split across train, validation and OOD diagnostic.

## Initial split policy

Use `phase4e1_trace_level_regime_v1`:

1. Load all normalized CSVs and matching manifests.
2. Group by `leakage_group` if present; otherwise by `trace_id`.
3. Compute simple trace descriptors:
   - sample count;
   - duration sum;
   - mean throughput;
   - p05/p50/p95 throughput;
   - coefficient of variation;
   - zero-throughput ratio;
   - mobility tags;
   - network tags;
   - dataset id.
4. Produce train, validation and OOD diagnostic splits.
5. Preserve at least one trace per visible dataset in validation where feasible.
6. Hold difficult or distribution-shift traces in OOD diagnostic.

## OOD meaning in Phase 4E.1

OOD is diagnostic-only. It is not a benchmark and not a ranking.

With the current small Phase 3 converted subset, OOD is a smoke-level stress check, not a real-world generalization proof.

## Forbidden split practices

Forbidden:

- random row-level split;
- using validation or OOD statistics to normalize train;
- tuning model choices on OOD;
- mixing dry-run result rows with network traces;
- using controller outputs as if they were exogenous traces.

## Acceptance markers

- SPLIT_UNIT: trace_or_leakage_group
- ROW_LEVEL_RANDOM_SPLIT: forbidden
- OOD_DIAGNOSTIC_ONLY: true

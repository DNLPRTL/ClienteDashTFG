# Phase 3.5 Results Boundary

Phase 3.5D validates the QoE artifact path with controlled smoke scenarios. It does not create experimental results.

## Boundaries

- A smoke run is not a benchmark.
- A `qoe_run_summary.json` file is not a benchmark aggregate.
- Scenario order is not ranking.
- The synthetic controller name is not a real controller result.
- Generated smoke outputs are external artifacts and are not versioned in Git.
- Phase 6, or another later formal evaluation phase, must close the comparison protocol before controller results can be ranked.

## Allowed Interpretation

Phase 3.5D can support statements such as:

- the post-processor can consume dry-run-like artifacts;
- QoE summaries preserve non-benchmark flags;
- gates prevent legacy, incomplete or conflicting sources from being promoted;
- a smoke report can validate the artifact contract.

## Forbidden Interpretation

Phase 3.5D must not be used to claim:

- controller performance;
- controller ranking;
- benchmark results;
- IA/RL training readiness beyond the documented future reward candidate;
- superiority of any ABR method.

## Validation markers

- PHASE_3_5D_RESULTS_BOUNDARY: smoke_not_benchmark
- outputs_are_benchmark_results=false
- no_final_ranking=true

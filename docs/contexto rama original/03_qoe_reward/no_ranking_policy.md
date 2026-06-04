# No-Ranking Policy For Phase 3.5D

Phase 3.5D is a controlled smoke-validation phase. It must preserve the no-ranking boundary from Phase 3.5A2 and Phase 3.5C.

## Prohibited

- Sorting controllers by QoE.
- Naming a best controller.
- Naming a winner.
- Comparing real controllers.
- Treating smoke scenarios as benchmark results.
- Promoting synthetic scenario values to thesis performance claims.

## Permitted

- Validating gates.
- Validating schemas.
- Validating deterministic QoE calculation on synthetic inputs.
- Reviewing scenarios by fixed scenario name.
- Checking that all outputs keep `outputs_are_benchmark_results=false`.
- Checking that all outputs keep `no_final_ranking=true`.

## Scenario Naming Rule

Scenarios are referenced by fixed names such as `complete_use_for_eval` or `incomplete_session`. They are not ordered by score and do not represent controller alternatives.

## Validation markers

- PHASE_3_5D_NO_RANKING_POLICY: active
- no ranking
- no benchmark
- no best controller
- no winner

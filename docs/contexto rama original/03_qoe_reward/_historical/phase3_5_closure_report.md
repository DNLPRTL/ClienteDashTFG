# Phase 3.5 Closure Report

Phase 3.5 closes the QoE/reward/methodology block for DashClientModular4 before any IA/RL work, formal benchmark or controller ranking.

## Initial HEAD

Expected initial HEAD: `e540ac3 test(qoe): add controlled Phase 3.5 smoke scenarios`.

## Subphase Closure Table

| subphase | role | main deliverables | closure status |
| --- | --- | --- | --- |
| A0 | literature intake/scaffold | source inventory, triage scaffold, search protocol | closed |
| A1 | source cards/evidence matrix | distilled cards, QoE evidence matrix, terms crosswalk, candidates | closed |
| A2 | QoE/reward/gates/schema decision | `qoe_linear_v1`, reward candidate, secondary metrics, gate policy, schema boundary | closed |
| A2.1 | schema marker hotfix | literal schema markers for validation | closed |
| B | pure QoE calculator | `core/evaluation/qoe.py`, `tests/test_qoe_metrics.py` | closed |
| C | dry-run artifact QoE post-processor | `core/evaluation/artifacts.py`, `scripts/compute_qoe_from_dry_run.py`, `tests/test_qoe_artifacts.py` | closed |
| D | controlled smoke scenarios | `scripts/run_qoe_smoke_scenarios.py`, `tests/test_qoe_smoke_scenarios.py`, external smoke report | closed |
| E | closure, memory integration and transition gate | closure docs, limitation docs, handoff docs, memory updates | closed by this document set |

## Main Deliverables By Subphase

- A0 created the Phase 3.5 evidence intake structure.
- A1 distilled the QoE/reward source cards and completed the evidence matrix.
- A2 closed the documented QoE/reward formula and artifact contract.
- A2.1 corrected a documentation marker validation issue.
- B implemented the pure deterministic calculator for `qoe_linear_v1` and `qoe_log_v1`.
- C implemented isolated computation from dry-run artifacts to QoE artifacts.
- D implemented controlled synthetic smoke scenarios outside the repository.
- E consolidates closure, limitations, validation summary and Phase 4 transition.

## Decisions Closed

- Primary formula version: `qoe_linear_v1`.
- Primary session metric for future evaluation: `qoe_linear_mean`.
- Segment reward: `reward_n` from `qoe_linear_v1`, documented as future IA candidate only.
- Sensitivity formula: `qoe_log_v1`.
- Startup delay: report-only with no penalty in `qoe_linear_v1`.
- VMAF/perceptual quality: deferred and artifact-dependent.
- Gates: `use_for_eval`, `diagnostic_only`, `do_not_use_for_eval`.
- Legacy dry-runs: not benchmark material and not promoted automatically.
- Controlled smoke scenarios: validation artifacts only, not benchmark and not ranking.

## Final Validation Set

The closure validation set is:

- `python -m py_compile core\evaluation\__init__.py core\evaluation\qoe.py core\evaluation\artifacts.py scripts\compute_qoe_from_dry_run.py scripts\run_qoe_smoke_scenarios.py tests\test_qoe_metrics.py tests\test_qoe_artifacts.py tests\test_qoe_smoke_scenarios.py`
- `python -m unittest tests.test_qoe_metrics`
- `python -m unittest tests.test_qoe_artifacts`
- `python -m unittest tests.test_qoe_smoke_scenarios`
- `python -m unittest discover`
- `python scripts\check_client_readiness.py --strict`
- `git diff --check`
- forbidden-file check through `git status --porcelain`.

## Confirmations

- No IA/RL is trained in Phase 3.5.
- No controller ranking is produced in Phase 3.5.
- No formal benchmark is executed or claimed in Phase 3.5.
- No generated datasets, CSV/log artifacts, PDFs, ZIPs or media are committed to Git.
- No controller, player, runtime or media-engine changes are part of Phase 3.5E.

## Validation markers

- HEAD_EXPECTED: e540ac3
- PHASE_3_5E_STATUS: closure_ready
- PHASE_3_5_CLOSED_BY_THIS_DOC: true
- qoe_linear_v1
- qoe_linear_mean
- qoe_log_v1
- use_for_eval
- diagnostic_only
- do_not_use_for_eval
- no IA
- no ranking
- no benchmark

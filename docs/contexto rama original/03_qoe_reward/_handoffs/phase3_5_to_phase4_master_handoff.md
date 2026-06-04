# Phase 3.5 To Phase 4 Master Handoff

This handoff summarizes the real project state after Phase 3.5 and before Phase 4 IA/RL work.

## Real Project State

DashClientModular4 has implemented baseline controllers, trace/replay infrastructure, final QoE metric semantics, pure QoE calculation, isolated QoE artifact computation and controlled QoE smoke validation. It has not run a formal benchmark, has not ranked controllers and has not trained IA/RL.

## Phase 3.5 History

| subphase | commit | summary |
| --- | --- | --- |
| A0 | `0a43675` | evidence intake scaffold |
| A1 | `475c2b2` | source cards and evidence matrix |
| A2 | `8970fd4` | QoE/reward/gates/schema decision |
| A2.1 | `02c0695` | schema marker hotfix |
| B | `b4636ab` | pure QoE calculator |
| C | `50dd3aa` | dry-run artifact QoE post-processor |
| D | `e540ac3` | controlled smoke scenarios |
| E | `TO_BE_FILLED_AFTER_COMMIT` | closure, memory integration and transition gate |

## Technical Deliverables

- `core/evaluation/qoe.py`
- `core/evaluation/artifacts.py`
- `scripts/compute_qoe_from_dry_run.py`
- `scripts/run_qoe_smoke_scenarios.py`
- `tests/test_qoe_metrics.py`
- `tests/test_qoe_artifacts.py`
- `tests/test_qoe_smoke_scenarios.py`

## Scientific Deliverables

- QoE source cards.
- QoE evidence matrix.
- QoE terms crosswalk.
- Formula candidates and final selection.
- Reward definition.
- Secondary metrics.
- Gate policy.
- Benchmark/result schema boundary.
- Limitations and defense talking points.

## Validations

- Pure QoE tests.
- QoE artifact tests.
- Controlled smoke scenario tests.
- Full `unittest discover`.
- Client readiness strict.
- `git diff --check`.
- Forbidden-file check.
- External smoke report outside Git.

## Risks Passed To IA

- Reward hacking.
- Overfitting to traces.
- Train/evaluation leakage.
- Treating smoke as benchmark evidence.
- Comparing IA against baselines without a formal protocol.
- Failing to distinguish training reward from evaluation metric.

## Phase 4A0 Must Do

- Search IA/RL ABR papers.
- Create IA source cards.
- List algorithm candidates.
- Define state/action/reward design.
- Define training data contract.
- Define acceptance tests.
- Define reproducibility and artifact-storage policy.

## Recommended Prompt For New Chat

Start Phase 4A0 as a literature intake and algorithm triage block. Do not implement IA, train, benchmark or rank until the scientific cards and decision documents are closed.

## Validation markers

- PHASE_3_5_TO_PHASE_4_MASTER_HANDOFF: ready
- A0=0a43675
- A1=475c2b2
- A2=8970fd4
- A2_1=02c0695
- B=b4636ab
- C=50dd3aa
- D=e540ac3
- E=TO_BE_FILLED_AFTER_COMMIT
- no benchmark
- no ranking
- no IA training yet

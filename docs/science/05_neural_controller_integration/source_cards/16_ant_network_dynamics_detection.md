# Source card 16: ANT network dynamics detection

## Title

Learning Accurate Network Dynamics for Enhanced Adaptive Video Streaming.

## Authors

Jiaoyang Yin, Hao Chen, Yiling Xu, Zhan Ma, Xiaozhong Xu.

## Year

2024.

## Venue/type

IEEE Transactions on Broadcasting; research source.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

ANT warns that mean and standard deviation of throughput may be insufficient to characterize network dynamics.

## Runtime integration pattern

The source uses richer dynamics detection and multiple dedicated models.

## Runtime inputs

Network dynamics features beyond simple averages. Phase 5 does not add a neural condition detector.

## Runtime action/output

Model or decision adapted to detected network dynamics.

## Safety/fallback/action mask

No direct action-mask transfer. It supports careful telemetry and no overclaiming from simple averages.

## Latency/compute/deployment assumptions

Dedicated model switching is deferred to future work.

## What transfers to DashClientModular4

- Do not rely only on simple average throughput for claims.
- Keep telemetry useful for later dynamics analysis.

## What must not be copied

- Dynamic model switching.
- Neural condition detector.

## Phase 5 docs affected

- `phase5a1_runtime_feature_availability_matrix.md`
- `phase5b_telemetry_contract.md`
- `notes_for_memory.md`

## Memory/defense usage

Use this source to justify limitations around network characterization.

## Final decision

Transfer diagnostics caution. Defer ANT-style detection.

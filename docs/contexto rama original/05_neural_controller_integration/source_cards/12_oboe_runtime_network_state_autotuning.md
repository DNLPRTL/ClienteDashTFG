﻿# Source card 12: Oboe runtime network state autotuning

## Title

Oboe: Auto-tuning Video ABR Algorithms to Network Conditions.

## Authors

Zahaib Akhtar, Yun Seong Nam, Ramesh Govindan, Sanjay Rao, Jessica Chen, Ethan Katz-Bassett, Bruno Ribeiro, Jibin Zhan, Hui Zhang.

## Year

2018.

## Venue/type

ACM SIGCOMM; ABR autotuning research source.

## Phase 5 triage

ACCEPTED_FOR_SOURCE_CARD.

## Why this source matters for integration

Oboe shows that runtime network regime awareness can matter. It uses online change-point detection and throughput mean/variability to update ABR configuration.

## Runtime integration pattern

Offline best configurations are precomputed per network state, then online network changes update the selected ABR configuration.

## Runtime inputs

Throughput mean, variability and change-point signals.

## Runtime action/output

ABR parameter configuration rather than a direct neural representation score.

## Safety/fallback/action mask

No direct action mask transfer. It supports richer future diagnostics and possibly safety/fallback analysis.

## Latency/compute/deployment assumptions

The autotuning engine and change-point implementation are not part of Phase 5.

## What transfers to DashClientModular4

- Telemetry can later include network regime diagnostics.
- Fallback/safety can consider recent throughput variability.

## What must not be copied

- Parameter autotuning engine.
- Change-point implementation in Phase 5.

## Phase 5 docs affected

- `phase5a1_runtime_feature_availability_matrix.md`
- `phase5b_telemetry_contract.md`
- `_historical/notes_for_memory.md`

## Memory/defense usage

Use this source to explain why the project records diagnostics but does not overclaim based on simple throughput averages.

## Final decision

Transfer regime-awareness as future diagnostic context. Do not implement Oboe.

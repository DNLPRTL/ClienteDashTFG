# Source Card: CellReplay

## Identity

- Source ID: `2025_sentosa_cellreplay_record_replay_cellular`
- Title: CellReplay: Towards accurate record-and-replay for cellular networks
- Authors: William Sentosa, Balakrishnan Chandrasekaran, P. Brighten Godfrey, Haitham Hassanieh
- Year/venue: 2025, USENIX NSDI
- Intake origin: `wave2_guardrails_secondary/2025_sentosa_cellreplay_record_replay_cellular.md`
- Phase 6A0 triage: `ACCEPTED_GUARDRAIL_SECONDARY`

## Why It Matters

CellReplay updates the emulation boundary for cellular networks. It documents that replay accuracy can be workload-dependent and that reproducibility does not guarantee perfect fidelity.

## Phase 6 Protocol Transfers

- Keep cellular emulation as secondary/diagnostic.
- Label Ubuntu demos as `diagnostic_only` when appropriate.
- Do not mix Python trace-driven and emulation outputs as equivalent evidence.
- Add cellular-emulation limitations to threats.

## What Does Not Transfer

- No CellReplay implementation.
- No hardware requirement.
- No move of the primary benchmark to emulation.

## Current Decision

Use as cellular replay limitation evidence.

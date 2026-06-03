# Source Card: Mahimahi

## Identity

- Source ID: `2015_netravali_mahimahi_record_replay_http`
- Title: Mahimahi: Accurate Record-and-Replay for HTTP
- Authors: Ravi Netravali, Anirudh Sivaraman, Somak Das, Ameesh Goyal, Keith Winstein, James Mickens, Hari Balakrishnan
- Year/venue: 2015, USENIX ATC
- Intake origin: `wave2_guardrails_secondary/2015_netravali_mahimahi_record_replay_http.md`
- Phase 6A0 triage: `ACCEPTED_GUARDRAIL_SECONDARY`

## Why It Matters

Mahimahi is the classic HTTP record-and-replay reference. It is useful for Ubuntu/demo context and for explaining what emulation can and cannot prove.

## Phase 6 Protocol Transfers

- Keep Mahimahi-style work as secondary validation or demo.
- Do not require Mahimahi for final Phase 6 results.
- Label any emulation artifacts separately from Python trace-driven evidence.
- Pair with CellReplay to document cellular replay limitations.

## What Does Not Transfer

- No replacement of the Python trace-driven runner.
- No primary QoE result path.
- No Windows readiness requirement.

## Current Decision

Use as secondary emulation reference only.

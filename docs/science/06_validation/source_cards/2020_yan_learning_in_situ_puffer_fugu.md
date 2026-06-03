# Source Card: Puffer/Fugu Learning In Situ

## Identity

- Source ID: `2020_yan_learning_in_situ_puffer_fugu`
- Title: Learning in situ: a randomized experiment in video streaming
- Authors: Francis Y. Yan, Hudson Ayers, Chenzhi Zhu, Sadjad Fouladi, James Hong, Keyi Zhang, Philip Levis, Keith Winstein
- Year/venue: 2020, USENIX NSDI
- Intake origin: `wave1_mandatory_methodology/2020_yan_learning_in_situ_puffer_fugu.md`
- Phase 6A0 triage: `ACCEPTED_MANDATORY_METHODOLOGY`

## Why It Matters

Puffer/Fugu is the mandatory reference for careful ABR comparison. It shows that even real randomized ABR experiments face heavy-tailed variability, uncertainty and cases where sophisticated methods do not clearly beat simple buffer-based control.

## Phase 6 Protocol Transfers

- Report uncertainty, sample counts, medians and percentiles when future runs exist.
- Do not reduce results to a single global mean.
- Keep BBA/BOLA/MPC/RobustMPC as serious baselines.
- Treat mixed or non-winning results as scientifically valid if the protocol is clean.

## What Does Not Transfer

- No Fugu implementation.
- No RCT requirement for the TFG.
- No replacement of `qoe_linear_v1`.
- No Phase 6A0 benchmark or QoE improvement claim.

## Current Decision

Use as claims-discipline and reporting methodology evidence only.

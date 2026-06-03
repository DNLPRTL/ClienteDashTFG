# Source Card: Taraghi Heuristic ABR QoE

## Identity

- Source ID: `2021_taraghi_understanding_qoe_heuristic_abr`
- Title: Understanding Quality of Experience of Heuristic-based HTTP Adaptive Bitrate Algorithms
- Authors: Babak Taraghi, Abdelhak Bentaleb, Christian Timmerer, Roger Zimmermann, Hermann Hellwagner
- Year/venue: 2021, ACM NOSSDAV
- Intake origin: `phase6a0_wave3_4_md/wave4_qoe_metric_sources/2021_taraghi_understanding_qoe_heuristic_abr.md`
- Phase 6A0 triage: `ACCEPTED_QOE_REPORTING`

## Why It Matters

Taraghi et al. reinforces that selected bitrate, stall events, bitrate switches and startup delay should be interpreted separately. It also exposes the gap between objective and subjective QoE evaluation.

## Phase 6 Protocol Transfers

- Report QoE components, not only `qoe_linear_mean`.
- Keep startup as report-only unless measured homogeneously.
- Use component summaries for interpretability in future results.
- Add small media-profile/video diversity as a threat.

## What Does Not Transfer

- No P.1203 replacement for Phase 3.5 metrics.
- No new BOLA/Shaka/FastMPC implementations from this paper.
- No adoption of its results as DashClientModular4 results.

## Current Decision

Use as component-reporting and objective/subjective-gap evidence.

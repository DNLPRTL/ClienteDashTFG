# Source Card: SODA

## Identity

- Source ID: `2024_chen_soda_consistent_high_quality_video_streaming`
- Title: SODA: An Adaptive Bitrate Controller for Consistent High-Quality Video Streaming
- Authors: Tianyu Chen, Yiheng Lin, Nicolas Christianson, Zahaib Akhtar, Sharath Dharmaji, Mohammad Hajiesmaili, Adam Wierman, Ramesh K. Sitaraman
- Year/venue: 2024, ACM SIGCOMM
- Intake origin: `wave1_mandatory_methodology/2024_chen_soda_consistent_high_quality_video_streaming.md`
- Phase 6A0 triage: `ACCEPTED_MANDATORY_METHODOLOGY`

## Why It Matters

SODA prevents a simplistic AI-versus-old-heuristics framing. It represents modern non-neural ABR work with production/deployability concerns and strong attention to quality, rebuffering and switching.

## Phase 6 Protocol Transfers

- Do not present AI as automatically superior.
- Report switching count/rate/magnitude as secondary metrics.
- Treat SODA as contextual evidence, not an implemented baseline.
- Include causal-bias cautions that align with CausalSim and Veritas.

## What Does Not Transfer

- No SODA implementation in Phase 6A0.
- No comparison against SODA unless a real controller exists.
- No import of SODA production claims as TFG results.
- No replacement of `qoe_linear_v1`.

## Current Decision

Use as modern non-neural ABR context and switching/smoothness reporting support.

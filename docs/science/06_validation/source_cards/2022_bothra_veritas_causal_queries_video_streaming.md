# Source Card: Veritas

## Identity

- Source ID: `2022_bothra_veritas_causal_queries_video_streaming`
- Title: Veritas: Answering Causal Queries from Video Streaming Traces
- Authors: Chandan Bothra, Jianfei Gao, Sanjay Rao, Bruno Ribeiro
- Year/status: 2022, arXiv/preprint intake
- Intake origin: `wave2_guardrails_secondary/2022_bothra_veritas_causal_queries_video_streaming.md`
- Phase 6A0 triage: `ACCEPTED_GUARDRAIL_SECONDARY`

## Why It Matters

Veritas reinforces that "what would have happened under another ABR" is a causal question, not a simple association. A bitrate change can alter buffer, download timing and future decisions.

## Phase 6 Protocol Transfers

- Do not reuse run logs as neutral network traces.
- Add causal-threat language next to CausalSim.
- Keep metrics/gates distinct from strong counterfactual claims.
- Describe Phase 6 as controlled comparison under a protocol, not a complete Internet counterfactual.

## What Does Not Transfer

- No Veritas implementation.
- No reopening of NeuralABR-Lite training.
- No production counterfactual claim.

## Current Decision

Use as causal-query and counterfactual-caution evidence.

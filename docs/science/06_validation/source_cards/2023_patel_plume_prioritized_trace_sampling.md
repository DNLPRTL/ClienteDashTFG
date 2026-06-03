# Source Card: Plume

## Identity

- Source ID: `2023_patel_plume_prioritized_trace_sampling`
- Title: Plume: A Framework for High Performance Deep RL Network Controllers via Prioritized Trace Sampling
- Authors: Sagar Patel, Junyang Zhang, Sangeetha Abdu Jyothi, Nina Narodytska
- Year/status: 2023, arXiv intake
- Intake origin: `wave2_guardrails_secondary/2023_patel_plume_prioritized_trace_sampling.md`
- Phase 6A0 triage: `ACCEPTED_GUARDRAIL_SECONDARY`

## Why It Matters

Plume adds a trace-distribution skew guardrail. Small or skewed trace sets can hide failures on difficult tail traces, especially for learned controllers.

## Phase 6 Protocol Transfers

- Characterize traces by dataset family, mobility, throughput and variability when possible.
- Report by dataset/split as well as aggregate.
- Use percentiles/CDF-style summaries in future reporting.
- Avoid letting easy traces dominate conclusions.

## What Does Not Transfer

- No Plume/Gelato implementation.
- No NeuralABR-Lite retraining.
- No TraceBench adoption without a later decision.

## Current Decision

Use as trace skew and tail-reporting evidence.

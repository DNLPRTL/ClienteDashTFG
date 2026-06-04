# Phase 5A0 literature delta plan

Phase 5A0 is mandatory before implementation.

## Why another search is needed

Phase 4 literature selected and trained the model. Phase 5 changes the problem to runtime integration:

- safe controller design;
- bundle loading;
- action masking;
- fallback;
- runtime feature availability;
- inference latency in a real Python client;
- telemetry without benchmark contamination.

## Google Scholar Labs prompts

### Prompt 1 — learned ABR controller integration

```text
Find papers from 2020 to 2026 about deploying or integrating machine-learning adaptive bitrate controllers into HTTP adaptive streaming clients. Focus on hybrid designs where a neural model provides scoring, guidance, caps, or recommendations, while a classical ABR controller or safety layer enforces valid actions, fallback, buffer constraints, and robustness. Extract title, authors, year, venue, method, runtime architecture, fallback strategy, state/action/reward, feature availability at runtime, latency, deployment assumptions, limitations, and relevance to a Python CPU-first DASH client.
```

### Prompt 2 — safety/fallback/action masking

```text
Find papers and engineering reports on safety mechanisms for learned controllers in networking or adaptive video streaming, especially action masking, fallback controllers, rule-based safety layers, invalid-action prevention, confidence/risk gates, runtime error handling, and safe deployment. Prioritize sources that discuss ML-based ABR, HAS/DASH/HLS, or network control. Extract what safety mechanism is used, what failure modes it prevents, whether it was evaluated in real deployment or simulation, and how it could apply to a small Python DASH client.
```

### Prompt 3 — CPU inference and model loading

```text
Find sources from 2020 to 2026 about low-latency CPU inference for small neural models in Python applications, especially PyTorch or ONNX Runtime. Focus on model loading, CPU-only inference, latency measurement, deterministic inference, model bundle schemas, security of model loading, and avoiding GPU-only dependencies. Extract practical constraints for Windows CPU-first deployment and what is appropriate for an undergraduate thesis.
```

### Prompt 4 — runtime feature availability and leakage

```text
Find papers about online feature availability, future-information leakage, trace-driven evaluation pitfalls, and sim-to-real gaps in adaptive bitrate streaming. Focus on what information is actually available to an ABR controller before requesting the next segment, and what features are invalid because they use future throughput, future QoE, final reward, or benchmark labels. Extract concrete rules for preventing leakage in controller integration.
```

### Prompt 5 — modular DASH/HAS controller APIs

```text
Find papers or technical reports about the software architecture of ABR controllers in modular DASH/HAS clients, including controller APIs, telemetry, runtime state, MPD representation ladders, model-assisted decisions, and fallback mechanisms. Extract design patterns that support reproducible evaluation without contaminating benchmark artifacts.
```

### Prompt 6 — 2025/2026 neural ABR deployment delta

```text
Find 2025 and 2026 papers on neural adaptive bitrate streaming, learned ABR deployment, ML-based ABR real-world testing, and client-side learned ABR integration. Prioritize sources that go beyond offline training and discuss how the model is actually used by a player/controller. Extract whether the paper changes the Phase 4 decision or only reinforces existing constraints.
```

## Information to copy

For each relevant result:

```text
title:
authors:
year:
venue:
DOI/stable URL:
method family:
runtime integration pattern:
fallback/safety mechanism:
action mask / invalid action handling:
feature availability at runtime:
latency / compute assumptions:
client-side or server-side:
code availability:
limitations:
relevance to DashClientModular4:
changes required to Phase 5 plan:
```

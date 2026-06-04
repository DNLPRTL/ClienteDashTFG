# Phase 5A0 search protocol

## Purpose

Phase 5A0 changes the research question from model selection to controller integration. Phase 4 already selected and exported NeuralABR-Lite as a Candidate Scorer. Phase 5A0 asks how to integrate that scorer safely into a Python DASH client without creating implementation debt, leakage, benchmark contamination or unsafe runtime behavior.

## Adapted Google Scholar Labs process

The search protocol was adapted from a Google Scholar Labs-style workflow:

1. Define structured research prompts.
2. Search for integration, safety, fallback, feature-availability and deployment evidence.
3. Distill each source into a source card.
4. Convert evidence into contracts before any implementation.

Google Scholar did not support the full structured prompts as executable queries. The results were therefore adapted manually: search themes were broken into smaller keyword searches, candidate sources were triaged, and the final Phase 5 documentation uses the provided source distillation rather than copying long paper excerpts.

## Search themes

The targeted search themes were:

- learned ABR integration;
- safety, fallback and action masking;
- runtime feature availability and leakage;
- CPU inference and model loading;
- hybrid ML plus classical controller boundaries;
- recent 2025/2026 deployment delta.

## Extraction fields

Each accepted source is reduced to integration evidence:

```text
title
authors
year
venue/type
Phase 5 triage
runtime integration pattern
runtime inputs
runtime action/output
safety/fallback/action mask
latency/compute/deployment assumptions
what transfers to DashClientModular4
what must not be copied
contracts affected
memory/defense usage
final decision
```

## Boundary

This protocol produces documentation only. It does not authorize controller code, registry changes, playback changes, media engine changes, config activation, retraining, benchmark runs, rankings or model artifacts in Git.

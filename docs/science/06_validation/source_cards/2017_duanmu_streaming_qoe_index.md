# Source Card: Streaming QoE Index

## Identity

- Source ID: `2017_duanmu_streaming_qoe_index`
- Title: A Quality-of-Experience Index for Streaming Video
- Authors: Zhengfang Duanmu, Kai Zeng, Kede Ma, Abdul Rehman, Zhou Wang
- Year/venue: 2017, IEEE Journal of Selected Topics in Signal Processing
- Intake origin: `phase6a0_wave3_4_md/wave4_qoe_metric_sources/2017_duanmu_streaming_qoe_index.md`
- Phase 6A0 triage: `ACCEPTED_QOE_REPORTING`

## Why It Matters

This source documents the limits of bitrate-only or simple objective QoE models and highlights perceptual quality, initial buffering, stalling and their interactions.

## Phase 6 Protocol Transfers

- Keep `qoe_linear_v1` as reproducible objective QoE, while acknowledging limitations.
- Keep startup report-only unless measured homogeneously.
- Keep VMAF/perceptual claims deferred and artifact-dependent.
- Do not equate bitrate alone with perceived quality.

## What Does Not Transfer

- No replacement of `qoe_linear_v1` with SQI.
- No MOS claim.
- No subjective dataset as direct client benchmark.

## Current Decision

Use as QoE limitation and perceptual-artifact boundary evidence.

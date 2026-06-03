# Phase 6A0 Search Protocol

Status: Phase 6A0 open, documentation/protocol intake only.

## Intake Source

The local intake used for this scaffold is:

```text
C:\Users\danie\Downloads\md fase 6
```

The preferred literature workspace path did not exist locally during this block:

```text
C:\Users\danie\Documents\TFG\_literature\phase6_validation\md_phase6_waves_20260603
```

The intake pack is treated as Markdown source-card/source-note material. Raw PDFs are not used as implementation inputs, and no PDF is added to Git.

## Intake Waves

| Wave | Role | Local folder |
| --- | --- | --- |
| Wave 1 | mandatory methodology | `wave1_mandatory_methodology/` |
| Wave 2 | guardrails and secondary sources | `wave2_guardrails_secondary/` |
| Wave 3 | trace and dataset sources | `phase6a0_wave3_4_md/wave3_trace_dataset_sources/` |
| Wave 4 | QoE and reporting sources | `phase6a0_wave3_4_md/wave4_qoe_metric_sources/` |
| Wave 3/4 notes | cross-cutting consolidation notes | `phase6a0_wave3_4_md/wave3_4_crosscutting_notes/` |

## Search And Handling Rules

- Use generated Markdown cards, source notes, indexes and manifests before opening historical Markdown.
- Do not ask Codex to implement from raw PDFs.
- Do not copy long paper passages, figures, datasets, PDFs or archives into the repository.
- Treat source cards as protocol evidence, not benchmark evidence.
- Keep datasets, models, runs, logs, CSVs, JSONL, zips and media outside Git.
- Consolidate duplicate logical sources before creating canonical cards.

## Phase 6A0 Scope

Phase 6A0 may:

- create validation documentation;
- classify sources and datasets;
- define evidence-package expectations;
- record threats to validity;
- record open Phase 6B/C hardening tasks.

Phase 6A0 must not:

- execute benchmarks;
- generate plots;
- create rankings or winners;
- retrain NeuralABR-Lite;
- change `qoe_linear_v1` or `reward_n`;
- change `player.py`, controllers, `core/trace_replay`, `core/evaluation` or benchmark scripts.

## Protocol Questions Opened

- Which datasets become Phase 6C materialized inputs after format/license checks?
- How will future manifests encode `canonical_content_fingerprint` in addition to `checksum_sha256`, `trace_id` and `leakage_group`?
- What minimum sample size is acceptable for reporting uncertainty?
- Which media_profile set is available without making VM bridge networking the benchmark?
- Which future evidence artifacts are sufficient to support VMAF or MOS-like claims, if any?

## Current Decision

Phase 6A0 opens the validation documentation path and consolidates evidence. It does not open the benchmark.

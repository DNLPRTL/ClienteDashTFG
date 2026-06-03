# Ubuntu Evidence Package Spec

Status: future evidence package contract. This document does not authorize running a benchmark.

## Package Name

Future Phase 6 runs should produce an auditable ZIP named:

```text
phase6_ubuntu_evidence_<timestamp>.zip
```

The ZIP must be created outside the repository and only referenced by manifest/checksum in documentation if needed.

## Required Contents

```text
00_README_EXECUTION.md
commands_used.sh
terminal_transcript.txt
git_status_before_after.txt
git_head.txt
environment.txt
phase6_config_resolved_snapshot.json
artifact_manifest.json
trace_manifest_audit_report.json
controller_matrix_summary.md
per_controller_trace_summary.csv
qoe_summaries/
run_logs/
selected_segment_samples/
exclusions_and_gates.md
```

## Reviewability Requirements

The package must allow independent review of:

- controller;
- trace_id;
- split;
- media_profile;
- representation selected by segment;
- bitrate;
- buffer before/after;
- download time;
- rebuffer;
- switching;
- QoE segment/session;
- gates/exclusions;
- exact commands;
- exact commit;
- exact environment.

## Required Metadata Fields

The evidence package should expose or link to fields for:

- `controller`;
- `trace_id`;
- `leakage_group`;
- `checksum_sha256`;
- `canonical_content_fingerprint` when future manifests include it;
- `split`;
- `dataset_family`;
- `media_profile`;
- `segment_index`;
- `selected_representation_index`;
- `selected_bitrate_bps`;
- `buffer_before_s`;
- `buffer_after_s`;
- `download_time_s`;
- `rebuffer_s`;
- `switch_count` or segment-level switch flag;
- `qoe_linear_v1_segment`;
- `qoe_linear_mean_session`;
- `qoe_log_v1_session` if computed as sensitivity;
- `startup_delay_s` if measured, otherwise explicit report-only/deferred status;
- `use_for_eval`;
- `diagnostic_only`;
- `do_not_use_for_eval`;
- exclusion reason.

## Non-Equivalence Rules

- Smoke artifacts are not benchmark artifacts.
- Legacy dry-run artifacts are not benchmark artifacts.
- VM server/content/demo artifacts are not benchmark network evidence.
- Diagnostic or secondary emulation artifacts must be labeled separately from primary Python trace-driven evidence.

## Git Boundary

The evidence ZIP, run logs, CSVs, JSONL files, plots, datasets, media and generated benchmark outputs must not be committed to Git.

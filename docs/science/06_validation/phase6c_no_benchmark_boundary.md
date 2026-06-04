# Phase 6C No-Benchmark Boundary

Status: mandatory Phase 6C boundary.

Phase 6C automates trace acquisition and materialization only. It does not authorize benchmark execution.

Phase 6C-H1 hardens live materialization progress, source selection, idempotency, resume and timeouts. These changes make acquisition and normalization safer; they do not change the benchmark boundary.

Forbidden in Phase 6C:

- running the client over real Phase 6 traces;
- running dry-runs over real Phase 6 traces;
- computing QoE over real Phase 6 outputs;
- generating result CSVs;
- generating plots;
- ranking controllers;
- declaring a winner;
- claiming `neural_abr_lite` improves QoE;
- committing datasets, normalized CSVs, receipts, local manifests, logs, zips, media or model bundles.

The only committed Phase 6C artifacts are source/config metadata, automation scripts, synthetic tests and documentation.

Per-step logs, receipts, normalized CSVs, local manifests, audit outputs and frozen manifests remain under the external root and are not committed. A successful primary-source freeze still records materialization readiness only.

Every Phase 6C report and frozen manifest must keep:

```json
{
  "ready_for_benchmark": false,
  "benchmark_authorized": false
}
```

`ready_for_phase6c` and a successful materialization freeze mean the trace identities are prepared for future evaluation planning. They do not mean the benchmark is ready or approved.

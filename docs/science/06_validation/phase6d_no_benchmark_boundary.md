# Phase 6D No-Benchmark Boundary

Status: mandatory Phase 6D boundary.

Phase 6D freezes a media profile from a real MPD. It does not authorize benchmark execution.

Allowed in Phase 6D:

- parse a real MPEG-DASH MPD;
- inspect local or HTTP-accessible segment sizes;
- freeze `media_profile_phase6_v1` outside the repository;
- validate media-profile structure;
- check controller/media-profile compatibility;
- inspect NeuralABR-Lite JSON metadata for action-count compatibility.

Forbidden in Phase 6D:

- running the client over Phase 6 traces;
- running controllers;
- running trace replay;
- computing QoE;
- generating result CSVs;
- generating plots;
- ranking controllers;
- declaring a winner;
- claiming `neural_abr_lite` improves QoE;
- retraining `neural_abr_lite`;
- changing `qoe_linear_v1` or `reward_n`;
- committing real MPDs, `.m4s`, `.mp4`, media, logs, receipts, model bundles, normalized traces, result CSVs or generated reports.

The server/VM is a media-profile source and demo/integration support surface. It is not the benchmark network.

Future benchmark network conditions remain trace-driven:

```text
normalized traces -> TraceDrivenNetworkModel -> Python execution
```

Every Phase 6D report and frozen profile must keep:

```json
{
  "ready_for_benchmark": false,
  "benchmark_authorized": false
}
```

The external Phase 6C trace manifest plus the external Phase 6D media profile are required inputs for later Phase 6E planning. They still do not mean `ready_for_benchmark=true`.

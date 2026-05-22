# Phase 3.4D Environment Probe Policy

Environment probes for Mahimahi and `tc/netem` are local/audit-only checks. They do not install tools, run emulation or create benchmark evidence.

## Allowed Probe Scope

Allowed probes are limited to command availability and version/help output:

- Mahimahi command presence: `mm-link`, `mm-delay`, `mm-webrecord`, `mm-webreplay`;
- Linux traffic-control command presence: `tc`, `ip`;
- version/help text when the command exists.

No qdisc changes, namespace changes, packet shaping, HTTP replay or network emulation are authorized in Phase 3.4D.

## Artifact Storage

Probe artifacts must live outside the repository. They may be placed in a local audit folder such as:

```text
C:\Users\danie\Documents\TFG\_datasets\phase3_traces_replay\_audit\phase3_4d_environment_probes
```

Do not commit probe logs, screenshots, command dumps, CSVs, ZIPs, PDFs or generated summaries. Authored Markdown summaries may be committed only when they are manually written documentation, not raw command output.

## Benchmark Boundary

Probe artifacts are not:

- benchmark artifacts;
- dry-run artifacts;
- final QoE/reward evidence;
- controller-ranking evidence;
- IA/RL training data.

Probe failures do not block Phase 3.5 because the primary path is the custom Python trace-driven pipeline.

## Memory Use

Probe output may inform Chapter 6 threats-to-validity notes, especially platform dependency, operational complexity and reproducibility limitations.

Any thesis wording must say "available in local environment" or "not available in local environment" rather than implying that Mahimahi or `tc/netem` was used for benchmark results.

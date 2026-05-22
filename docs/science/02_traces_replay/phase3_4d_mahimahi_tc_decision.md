# Phase 3.4D Mahimahi/tc Decision

Phase 3.4D closes the replay/emulation method decision for the current project stage. It is documentation only: no Mahimahi wrapper, no `tc/netem` wrapper, no installation, no network emulation and no benchmark execution are implemented here.

## Verdict

The custom Python trace-driven pipeline remains the primary reproducible path for Phase 3.5 and future IA work.

Mahimahi is retained as a secondary Ubuntu-only validation/runbook candidate. Linux `tc/netem` is retained as a Linux fallback/sanity/runbook candidate. Neither tool is required to proceed to Phase 3.5.

Mahimahi/tc outputs must not be mixed with Python dry-run outputs as equivalent benchmark results. If either external method is used later, its artifacts need separate method labels, separate limitations and explicit non-equivalence notes until a later benchmark protocol authorizes comparison.

## Why Python Remains Primary

The project already has a deterministic Python trace-driven path:

```text
raw dataset outside repo
  -> converter
  -> normalized_trace_schema_v1 CSV
  -> schema validator
  -> TraceLoader
  -> TraceDrivenNetworkModel
  -> TraceDrivenFakeReplayAdapter
  -> controlled dry-run harness
```

This path is primary because it is:

- deterministic and inspectable;
- covered by `unittest` synthetic tests;
- usable on Windows and Ubuntu;
- independent of privileged qdisc or namespace manipulation;
- aligned with future IA/reward-loop needs;
- already isolated from controller future-sample leakage;
- explicit about non-benchmark dry-run artifact semantics.

## Why Mahimahi Is Useful But Secondary

Mahimahi is scientifically useful because it is a known framework for HTTP record-and-replay and network emulation. It can help validate later whether selected behavior survives a shell-based external emulation setup.

It remains secondary because it is Ubuntu/Linux-oriented, adds operational dependency risk, may not match the current fake dry-run path, and is not needed for deterministic Phase 3.5 metric definition. Its HTTP record/replay model is also not automatically equivalent to the current synthetic segment dry-run harness.

## Why tc/netem Is Fallback/Sanity Only

Linux `tc/netem` can emulate delay, loss and related network effects through kernel traffic control. It is useful as a low-level sanity or fallback tool when a future runbook needs controlled impairment.

It is not primary because real qdisc changes require privileges, cleanup can contaminate the host network if mishandled, kernel timer granularity may affect timing, and `tc/netem` is not trace-driven by itself without additional shaping logic.

## Decision Table

| method | role | platform | reproducibility | privilege requirements | integration risk | benchmark status | Phase 3.5 status | future use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Custom Python trace-driven pipeline | Primary path | Windows and Ubuntu | High: deterministic local model and synthetic tests | None for normal use | Low: already integrated in `core.trace_replay` boundaries | Not benchmark until Phase 3.5 defines metrics | Required and sufficient path | Phase 3.5 metrics/QoE design and future IA environment basis |
| Mahimahi | Secondary validation/runbook candidate | Ubuntu/Linux | Medium to high when environment is controlled | Depends on installation and namespace assumptions | Medium: external HTTP/emulation workflow can diverge from fake dry-run | Not benchmark in Phase 3.4D | Optional, not blocking | Later external validation if separately authorized |
| Linux `tc/netem` | Fallback/sanity/runbook candidate | Linux | Medium: host/kernel settings must be controlled | Real qdisc changes require privileges | High if not isolated; cleanup and host contamination risks | Not benchmark in Phase 3.4D | Optional, not blocking | Later impairment sanity checks in isolated namespace if separately authorized |

## Phase 3.5 Gate

Phase 3.5 can proceed without Mahimahi or `tc/netem` being operational. The next necessary work is final metric/QoE boundary definition over the existing Python trace-driven path.

External emulation can add later validation context, but it cannot replace the Python trace-driven pipeline for Phase 3.5 and cannot produce final controller rankings unless a later benchmark protocol explicitly authorizes it.

## Non-Goals

Phase 3.4D does not:

- implement Mahimahi;
- implement `tc/netem`;
- install tools;
- execute network emulation;
- change qdisc or network namespaces;
- define final QoE/reward;
- rank controllers;
- change runtime, player, controller, media-engine, metric or IA code.

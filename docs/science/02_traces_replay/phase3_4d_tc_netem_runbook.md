# Phase 3.4D tc/netem Runbook

This is an Ubuntu/Linux-only optional runbook for future environment probing. It does not authorize qdisc modification, network namespace creation or real network emulation in Phase 3.4D.

## Scope

Linux `tc/netem` can emulate delay, loss and related network effects. It can be useful as a fallback or sanity tool, but it is not trace-driven by itself and does not replace the custom Python trace-driven pipeline.

## Probe Commands Only

The default Phase 3.4D probes are command-availability and version checks:

```bash
command -v tc
command -v ip
tc -V
ip -V
```

Do not run `tc qdisc add`, `tc qdisc change`, `tc qdisc del`, `ip netns add`, or any command that modifies host networking in Phase 3.4D.

## Future Use Conditions

If future `tc/netem` use is separately authorized, it must:

- use an isolated namespace or an equivalently documented isolation boundary;
- document every interface touched;
- document setup and cleanup commands before execution;
- capture environment details outside the repository;
- state kernel, timer and privilege limitations;
- label outputs as `tc_netem_validation` or equivalent, not as Python dry-run outputs;
- avoid controller ranking unless a later final benchmark protocol explicitly permits it.

## Risks

| risk | implication |
| --- | --- |
| Privileged qdisc changes | Real impairment usually requires elevated privileges. |
| Kernel timer granularity | Delay and rate behavior may differ across kernels and hosts. |
| Cleanup risk | A failed cleanup can contaminate host networking. |
| Host/network contamination | Non-isolated qdisc changes can affect unrelated traffic. |
| Not trace-driven by itself | Additional shaping logic would be needed to replay throughput traces. |
| Comparability risk | `tc/netem` outputs cannot be treated as equivalent to Python dry-run outputs without a later protocol. |

## Interpretation

`tc/netem` remains a Linux fallback/sanity candidate. Missing `tc` or `ip` commands do not block Phase 3.5 because the primary path is the Python trace-driven pipeline.

# Phase 6A0 Threats Matrix

Status: threats-to-validity scaffold. No benchmark result is recorded here.

| Threat | Why it matters | Current mitigation | Future gate |
| --- | --- | --- | --- |
| Trace-driven exogeneity assumption | A trace may not be independent from the ABR/controller that produced the measured throughput | Documented via CausalSim and Veritas; classify trace origin | Phase 6B/C protocol must state assumptions per dataset |
| Phase 4 checksum leakage | Phase 4 candidate data had checksum duplicates and cannot be strong generalization evidence | Phase 6 must block overlap by `trace_id`, `leakage_group` and `checksum_sha256` | Eligibility audit before any evaluation |
| Missing canonical content fingerprint parsing | Future manifests may include `canonical_content_fingerprint`, but current audit script appears focused on checksum/trace/leakage fields | Recorded as hardening gap; code not changed in this block | Phase 6B/C must harden `scripts/audit_phase6_trace_eligibility.py` if fingerprints are adopted |
| Dataset skew | Common/easy traces can dominate small benchmark conclusions | Plume-driven reporting: dataset family, split, percentiles and tail summaries | Future result plan must include distribution/component reporting |
| OOD undercoverage | HSDPA/Ghent alone do not prove modern/global generalization | Raca 4G, Raca 5G and Lumos5G listed as future OOD candidates | OOD dataset cards, manifests and split rules before OOD claims |
| QoE metric limitations | `qoe_linear_v1` is objective/reproducible but not full subjective QoE | Keep QoE components and secondary/sensitivity metrics documented | No MOS/VMAF claim without artifacts and metric decision |
| Simulation vs real-world gap | Trace-driven comparison is reproducible but not equivalent to live Internet deployment | Into the Wild and Puffer/Fugu claims discipline | Future thesis text must state real-world deployment is out of scope |
| Media profile limitations | A small media_profile set may not represent all content/ladders/codecs | VM/content path is media/demo support, not network benchmark | Evidence package must record media_profile and representation decisions |
| No VMAF/perceptual artifacts | Without video/perceptual artifacts, perceptual-quality claims are unsupported | VMAF/P.1203/MOS deferred | Artifact-dependent metric gate required |
| Small TFG-scale sample limits | Limited traces/sessions can make effect sizes uncertain | Report sample counts and uncertainty when runs exist | Statistical comparison plan required before claims |
| Dependency on local external workspaces | Datasets/models/runs live outside Git and may drift | Evidence package spec requires commands, commit, environment and artifact manifest | Phase 6C must produce auditable ZIP with hashes |
| Emulation/demo fidelity | Mahimahi/tc/CellReplay-style demos may not match cellular reality | Keep secondary/diagnostic labels | Do not mix diagnostic demos with primary benchmark tables |
| Ghent duplicate archives | `logs_all` plus per-mobility archives can duplicate traces under different paths | Hard dataset-card rule | Deduplicate by checksum/fingerprint before split |

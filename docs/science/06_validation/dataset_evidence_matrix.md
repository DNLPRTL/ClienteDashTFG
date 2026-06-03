# Dataset Evidence Matrix

Status: dataset-readiness matrix only. No dataset has been added to Git and no benchmark has been run.

| Dataset | Role | Split candidate | OOD suitability | Format/license status | Leakage risk | Checksum/fingerprint requirement | Phase 6C readiness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| HSDPA Norway / MMSys 2013 | First materialization candidate | Candidate train/test split after checks | Limited; legacy 3G/HSDPA domain | Unknown/TBD; inspect outside Git | Phase 4 overlap must be blocked | Required: `trace_id`, `leakage_group`, `checksum_sha256`; add `canonical_content_fingerprint` if available | Not ready; needs local download, parser, manifest and audit |
| Ghent 4G/LTE | First materialization candidate with duplicate guardrail | Candidate LTE split after deduplication | Moderate LTE/mobile domain | Unknown/TBD; inspect outside Git | High if `logs_all` and per-mobility folders are both used without deduplication | Required before split; fingerprints must deduplicate aggregate/per-mobility content | Not ready; needs duplicate plan, parser, manifest and audit |
| Raca 4G LTE | Future modern OOD candidate | Candidate test/OOD after first materialization | Strong 4G/mobile OOD candidate | Unknown/TBD; access/license/format checks required | Synthetic and real traces must be separated | Required before split; include production/synthetic labels | Future candidate; not required for initial closure |
| Raca 5G | Future 5G OOD candidate | Candidate OOD after checks | Strong 5G candidate if trace format fits | Unknown/TBD; access/license/format checks required | Synthetic/ns-3 and production must be separated | Required before split; include app pattern labels if used | Future candidate; not required for initial closure |
| Lumos5G | Future 5G/mmWave OOD candidate | Candidate OOD after checks | Strong high-variance mmWave candidate | Unknown/TBD; access/license/format checks required | Must not mix with other 5G families as identical domain | Required before split; include dataset family and mobility/context labels where possible | Future candidate; not required for initial closure |
| Lancaster | Gap, not authorized | Intended Phase 6C candidate only after source card | Unknown until card exists | No source card in current wave pack | Unknown | Not authorized until a source note/card exists | Not ready; source card required |

## Dataset Rules

- HSDPA Norway and Ghent are the first materialization candidates.
- Ghent must use `logs_all` OR per-mobility folders, not both unless deduplicated by checksum/fingerprint before split.
- Raca 4G, Raca 5G and Lumos5G are recommended/future OOD candidates, subject to access/license/format checks.
- Lancaster is a gap and is not authorized for use until a source note/card exists.
- No raw dataset, normalized CSV, run output or archive belongs in Git.

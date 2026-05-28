# Simulator determinism contract

## Deterministic replay requirement

For a fixed set of manifests, trace files, seed, teacher config and environment parameters, repeated dataset generation must produce the same:

```text
sample count
split assignment
teacher labels
normalization stats
sanity metrics
manifest hashes
```

## Seeds

Every future training/dataset command must record:

```text
python hash seed if applicable
random seed
numpy seed if used
torch seed if used
teacher seed if applicable
environment seed
```

## Hashes

Phase 4D should hash important inputs:

```text
trace manifest
split manifest
teacher config
feature schema
normalization stats
sample files
```

## Allowed nondeterminism

If any component has unavoidable nondeterminism, it must be documented and bounded. CPU-first deterministic settings are preferred.

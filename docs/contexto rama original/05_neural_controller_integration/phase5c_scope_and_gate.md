# Phase 5C scope and gate

## Scope

Phase 5C is documentation/specification finalization only. It translates the Phase 5B contracts into an implementation-ready Phase 5D plan and prompt.

Phase 5D is the first implementation block. Controller code, registry changes, player hooks, config examples and tests are still prohibited in Phase 5C.

## Required starting state

The required starting commit is:

```text
8c9ca3b docs(neural-abr): document Phase 5 integration evidence and contracts
```

A later starting commit is acceptable only if it is documentation-only and already validated.

## Phase 5C prohibited work

Phase 5C must not:

- create or modify runtime Python code;
- create neural controller files;
- modify `core/controller/registry.py`;
- modify `player.py`;
- modify `main.py`;
- modify `core/client_config.py`;
- modify `core/dataset_schema.py`;
- modify `config/client.example.yaml`;
- create tests;
- add model artifacts, PDFs, logs, CSVs, datasets, zips or checkpoints;
- benchmark, rank controllers, retrain or claim improvement.

## Closure criteria

Phase 5C can close only when:

- all Phase 5C docs are created;
- no code is touched;
- `python -m unittest discover` is OK;
- `python scripts/check_client_readiness.py --strict` is PASS;
- Ubuntu validation is done;
- the future Phase 5D Codex implementation prompt is ready;
- the block remains diagnostic-only and not benchmark evidence.

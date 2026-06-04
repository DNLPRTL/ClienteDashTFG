# Action space decision

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## Decision

The action space is closed as:

```text
action = representation_index
```

The action must be an integer index into the valid MPD representation ladder for the current segment.

## Forbidden actions

The model must not output:

```text
raw bitrate not present in the MPD
quality label disconnected from the MPD
target throughput
download rate
buffer target
controller name
continuous action requiring post-hoc discretization
```

## Validity requirements

Every selected action must satisfy:

```text
0 <= representation_index < number_of_representations
action_mask[representation_index] == 1
representation exists in the current MPD
representation is valid for the current segment
```

## Variable ladders

Because ladders can differ between media assets, the model must not depend on a fixed number of output neurons for a fixed ladder unless the dataset contract explicitly locks one ladder for a smoke-only experiment.

The selected base design is candidate scoring, which supports variable ladders.

## Phase boundaries

Phase 4B defines the action contract only. Implementation of action mapping, action masks, and fallback behavior is deferred to later specs and Codex after Phase 4C.

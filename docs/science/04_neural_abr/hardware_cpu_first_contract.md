# Hardware CPU-first contract

Project: DashClientModular4 — Phase 4 IA/RL ABR
Phase block: Phase 4B — state/action/reward/training-data contracts
Status: repo-ready contract draft generated after Phase 4A0/A1/A2.

## User hardware baseline

The design targets:

```text
Windows 11
i5-14600KF
32 GB RAM
AMD RX 7800 XT 16 GB
Python 3.12.8
PyTorch 2.6.0+cpu
CUDA unavailable
torch_directml not installed
WSL not installed
```

## Base requirement

The base NeuralABR-Lite path must work on CPU.

Allowed:

```text
PyTorch CPU
NumPy/Pandas style preprocessing if needed later
small MLP/candidate scorer
small training smokes
manifest-backed artifacts outside repo
```

Not allowed as a gate:

```text
CUDA
ROCm
DirectML
WSL
Ray/RLlib
TensorFlow 1.x legacy stack
large MoE/transformer training
multi-GPU training
long DRL training as a mandatory path
```

## GPU/DirectML policy

AMD GPU acceleration may be explored later only as optional acceleration. It must not be required for reproducibility or for closing the thesis.

## Model scale policy

The base model must be small enough that:

```text
inference per decision is negligible relative to segment duration
training smoke can run on CPU
architecture can be explained in the defense
model files stay outside Git
```

## Phase 4B decision

CPU-first is a hard gate. Any method that requires a large GPU stack is not selected as base implementation.

# Evaluation gate policy

Status: closed_phase3_5_rebuild_contract.

Los gates separan calculo tecnico de uso evaluable. No son castigos numericos.

Valores permitidos:

```text
use_for_eval
diagnostic_only
do_not_use_for_eval
```

Reglas:

- Si una sesion esta incompleta, queda `do_not_use_for_eval`.
- Si el artifact fuente es legacy o anterior al contrato QoE, queda `do_not_use_for_eval`.
- Si el artifact fuente intenta declararse benchmark, el postprocesador fuerza salida no benchmark y queda `do_not_use_for_eval`.
- Si falta una columna requerida, el postprocesador falla en vez de inventar valores.
- Startup y VMAF se registran como limitaciones, no como penalizaciones ocultas.

Campos de salida obligatorios:

```text
session_eval_gate
gate_reasons
outputs_are_benchmark_results=false
benchmark_performed=false
ranking_performed=false
no_final_ranking=true
ia_training_performed=false
```

# Runbook Phase45 v3 Neural-MPC Bundle en Ubuntu Cliente - 2026-06-15

## Proposito

Validar en Ubuntu cliente el bundle experimental externo:

```text
phase45_v3_neural_throughput_calibrated_mpc_v1
```

Esta validacion solo comprueba contrato, manifiesto, hashes y presencia del
bundle. No integra el controller en runtime, no ejecuta Phase 6, no es benchmark
y no autoriza ranking ni afirmaciones de mejora QoE.

## Por que este paso existe

WSL2/ROCm ha entrenado y empaquetado el candidato. Ubuntu cliente es el entorno
que manda para validar funcionamiento real del proyecto. Antes de tocar runtime
o Phase 6, el bundle debe existir tambien en la estructura externa de Ubuntu
cliente.

## Estado de entrada

Bundle generado en WSL2:

```text
~/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1
```

Destino esperado en Ubuntu cliente:

```text
~/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1
```

Repositorio esperado en Ubuntu cliente:

```text
~/TFG/DashClientModular4
```

## Opcion A - Si el bundle ya esta copiado en Ubuntu cliente

En Ubuntu cliente:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/validate_phase45_v3_neural_mpc_experimental_bundle_ubuntu_cliente.sh
```

Despues pegar en el chat el JSON final impreso por:

```bash
bash scripts/print_phase45_v3_neural_mpc_experimental_bundle_summary_ubuntu_cliente.sh
```

## Opcion B - Copiar desde WSL2 a Ubuntu cliente

En WSL2:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/package_phase45_v3_neural_mpc_experimental_bundle_transfer_wsl.sh
```

Esto crea:

```text
~/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1.tar.gz
```

Copiar el `.tar.gz` a Ubuntu cliente. Si hay SSH:

```bash
scp ~/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1.tar.gz danie@<IP_UBUNTU_CLIENTE>:/tmp/
```

Si no hay SSH, mover ese `.tar.gz` por el metodo disponible y dejarlo en:

```text
/tmp/neural_mpc_experimental_candidate_v1.tar.gz
```

En Ubuntu cliente:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/unpack_phase45_v3_neural_mpc_experimental_bundle_ubuntu_cliente.sh /tmp/neural_mpc_experimental_candidate_v1.tar.gz
```

El script desempaqueta en:

```text
~/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1
```

y despues valida el bundle.

## Salida esperada

La salida final debe contener:

```text
status=PASS
bundle_created=true
controller_integrated=false
benchmark_performed=false
ranking_performed=false
phase6_formal_evaluation_performed=false
qoe_claims_authorized=false
```

## Si falla

No avanzar a integracion. Pegar el JSON o el error en el chat.

Fallos tipicos:

- el bundle no esta en `~/TFG/modelos/phase45_v3/...`;
- el `.tar.gz` se descomprimio en un nivel de carpeta incorrecto;
- el repo de Ubuntu cliente no hizo `git pull`;
- algun hash no coincide, senal de copia incompleta o bundle modificado.

## Que carpetas haran falta mas adelante para Phase 6

Este paso actual no necesita Phase 6. Cuando se autorice Phase 6 formal, Ubuntu
cliente debera tener, como minimo:

```text
~/TFG/DashClientModular4
~/TFG/modelos/phase45_v3/neural_mpc_experimental_candidate_v1
~/TFG/manifests_trazas/phase3/final/phase3_trace_manifest_curated.json
~/TFG/datasets_normalizados/phase3/final/schema_v1
```

Ademas, la VM servidor Ubuntu debe servir el contenido DASH por HTTP desde:

```text
/var/www/html/dash
```

La ruta exacta de runs/evidencia de Phase 6 se definira en el runbook formal de
integracion/evaluacion. Hasta entonces no se debe ejecutar benchmark ni ranking
con este candidato.

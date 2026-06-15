# Proceso estandar de desarrollo IA ABR - Fase 4-5 v1

Estado: guia operativa obligatoria para nuevas lineas IA ABR.

Este documento define el embudo de desarrollo que debe seguir cualquier
controller IA nuevo del proyecto. Su objetivo es evitar repetir errores
historicos: entrenar fuera de la dinamica real del cliente, escalar demasiado
pronto, integrar un controller por entusiasmo offline o llamar benchmark a una
ejecucion diagnostica.

## Principio central

Toda linea IA ABR debe avanzar por etapas pequenas, auditables y reversibles.
No se pasa a la etapa siguiente porque un numero aislado parezca bueno. Se pasa
solo si el paquete de evidencias de la etapa anterior es coherente y no viola
los gates de seguridad, paridad, no contaminacion y no benchmark.

La secuencia canonica es:

```text
decision documentada
-> dataset pilot
-> auditoria dataset pilot
-> entrenamiento pilot 1 seed
-> resumen y analisis de errores
-> pilot multi-seed
-> diagnostico closed-loop offline
-> bundle experimental externo
-> smoke/runtime load
-> Phase 6 diagnostico en Ubuntu cliente
-> Phase 6 rapido si procede
-> iteracion controlada
-> full dataset/full training solo si la evidencia lo justifica
```

## Etapa 0 - Decision de linea

Antes de crear codigo o dataset, debe existir una decision tecnica en:

```text
docs/contexto rama nueva/fase_4_5_v1/
```

Debe contener:

- nombre estable de la linea;
- hipotesis tecnica;
- que reutiliza del proyecto y que no reutiliza;
- que linea existente no debe tocar;
- contrato de inputs visibles;
- targets offline;
- gates minimos;
- rutas externas previstas;
- criterios de parada;
- restricciones de no benchmark/no ranking/no claims.

Si la decision no separa explicitamente entrenamiento, runtime, evaluacion y
benchmark, esta incompleta.

## Etapa 1 - Dataset pilot

El primer dataset debe ser pilot y barato. Sirve para validar contrato,
paridad, schema, leakage, targets y coste computacional. No sirve para declarar
modelo candidato.

Debe vivir fuera de Git, normalmente bajo:

```text
~/TFG/datasets_normalizados/phase45_v3/<linea>_pilot_v1
```

Debe usar:

- manifest curado Phase 3;
- splits por grupo semantico/leakage, nunca por filas;
- dinamica cerrada compatible con el cliente cuando la linea sea closed-loop;
- `qoe_linear_v1` si el target depende de QoE;
- fragmentos de 4 s si usa el perfil `paseo_10min_30fps_4s`;
- escalera real `[300, 750, 1200, 1850, 2850, 4300]` kbps;
- `max_buffer_s=60.0` cuando simule dinamica del cliente/Phase 6;
- futuro solo como target, nunca como input.

Debe producir resumen y auditorias con flags:

```text
benchmark_performed=false
outputs_are_benchmark_results=false
ranking_performed=false
no_final_ranking=true
qoe_claims_authorized=false
```

## Etapa 2 - Entrenamiento pilot 1 seed

El primer entrenamiento debe ser una sola seed. Su objetivo es probar que el
contrato aprende algo sin fallos obvios.

No se acepta avanzar si:

- selecciona `best_epoch=0` por fallback;
- pasa solo copiando una referencia sin aprendizaje real;
- rompe gates anti-colapso;
- produce acciones invalidas;
- requiere relajar gates;
- usa artefactos fuera de rutas Linux en WSL;
- necesita comandos manuales largos no versionados.

Daniel debe ejecutar solo comandos cortos, por ejemplo:

```bash
cd ~/TFG/DashClientModular4
git pull
bash scripts/<runbook>.sh
```

## Etapa 3 - Analisis de errores

Todo pilot debe tener resumen y, si falla o queda en `REVIEW`, analisis de
errores por:

- bucket de throughput;
- bucket de buffer;
- rollout/source/politica si aplica;
- accion objetivo;
- accion predicha;
- alta capacidad;
- fallback;
- invalid actions;
- rebuffer;
- utilidad/QoE;
- colas severas.

No se lanza otra variante si no se entiende que fallo en la anterior.

## Etapa 4 - Pilot multi-seed

Solo se pasa a multi-seed si el pilot 1 seed muestra avance real. Multi-seed no
debe usarse para buscar una seed afortunada.

La lectura debe reportar:

- estado por seed;
- gates fallidos;
- metricas max/min/mean;
- hashes de modelos;
- estabilidad entre seeds;
- si alguna seed cae a fallback;
- si el coste computacional justifica escalar.

Si mas de dos ejecuciones consecutivas no avanzan de paso, se activa la regla de
informe de bloqueo autosuficiente.

## Etapa 5 - Diagnostico closed-loop offline

Antes de bundle/runtime, el modelo debe probarse en closed-loop offline dentro
del entorno que replica el cliente.

Gates minimos:

- `fallback_rate == 0` salvo que la linea declare fallback como comportamiento
  experimental y aun asi quede auditado;
- `invalid_action_count == 0`;
- no colapso a accion baja en alta capacidad;
- no rebuffer explosivo en `2_5_mbps`;
- no comprar utilidad media rompiendo colas;
- no comprar bitrate subiendo mucho rebuffer;
- no copiar un baseline sin aportar comportamiento interpretable.

Este diagnostico no es benchmark.

## Etapa 6 - Bundle experimental externo

Solo si el diagnostico closed-loop offline es estable se prepara bundle. El
bundle vive fuera de Git, normalmente bajo:

```text
~/TFG/modelos/phase45_v3/<linea>_experimental_candidate_v1
```

Git solo versiona:

- exportador;
- validador;
- contrato de bundle;
- tests;
- runbooks.

El bundle debe incluir manifiesto, hashes, config, normalizacion, tarjeta de
modelo, contrato de inferencia, politica de fallback y reporte de export.

## Etapa 7 - Smoke/runtime load

Antes de usar GUI o Phase 6, el controller debe pasar un smoke de carga y
decision en Ubuntu cliente.

Debe verificar:

- bundle carga;
- hashes validos;
- schema valido;
- features runtime disponibles;
- accion valida;
- fallback no usado en caso nominal;
- telemetria neural presente.

## Etapa 8 - Phase 6 diagnostico

Primer uso en el cliente real:

```text
Preset: diagnostico
Motor: fake
Controllers: baselines clasicos necesarios + nuevo controller
```

No se usa para ranking ni claims. Sirve para detectar:

- colapso runtime;
- latencia;
- fallback;
- telemetria rota;
- discrepancias entre WSL closed-loop y Ubuntu cliente;
- comportamiento por bucket.

## Etapa 9 - Phase 6 rapido

Si `diagnostico` no muestra fallos estructurales, se puede ejecutar `rapido`.
Sigue sin ser benchmark final ni ranking autorizado. Su funcion es ampliar
cobertura y revelar fallos de estabilidad.

Si falla, se vuelve a analisis. No se relajan gates por prisa.

## Etapa 10 - Iteracion controlada

Las mejoras deben tener hipotesis concreta:

- predictor;
- dataset;
- target;
- planner;
- loss;
- calibracion;
- fallback;
- feature contract.

Cada cambio debe aislarse. No mezclar varias causas en una ejecucion si luego
no se puede explicar que arreglo el problema.

## Etapa 11 - Full dataset/full training

Solo se escala a full cuando:

- pilot 1 seed tuvo sentido;
- pilot multi-seed fue estable;
- diagnostico closed-loop offline fue estable;
- bundle/smoke no fallaron;
- Phase 6 diagnostico no mostro colapso;
- Phase 6 rapido no revelo fallo estructural;
- el coste GPU esta justificado.

Full no convierte el resultado en ganador. Solo genera un candidato mas serio.

## Criterios de parada obligatorios

Parar y documentar bloqueo si:

- tres ejecuciones no avanzan de paso;
- los fallos cambian de forma incoherente sin explicacion;
- el modelo solo pasa por fallback;
- el modelo repite colapso de politica;
- aparecen discrepancias entre entorno cerrado y cliente;
- un gate critico se quiere relajar para poder avanzar;
- no se sabe que pregunta contesta la siguiente ejecucion.

## Relacion con lineas actuales

`phase45_v3_neural_throughput_calibrated_mpc_v1` es la linea viva
predictor+planner. No debe modificarse por abrir nuevas lineas.

`phase45_v3_qh_scorer` queda como experimento bloqueado y fuente de aprendizaje.

SPBC/SPC historicos quedan como evidencia negativa y fuente conceptual. No se
reutilizan sus datasets antiguos para afirmar validez de nuevos controllers.

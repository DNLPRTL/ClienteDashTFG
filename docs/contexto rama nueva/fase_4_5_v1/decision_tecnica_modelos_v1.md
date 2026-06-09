# Fase 4-5 v1 - Decision tecnica de modelos/controllers IA

Status: decision_inicial_lista_para_specs.

Fecha: 2026-06-09.

Esta decision abre Fase 4-5 v1 como iteracion nueva. No sustituye a Phase 4 ni
Phase 5 cerradas y no hereda el diseno de `NeuralABR-Lite`. Los controllers IA
anteriores quedan solo como comparadores historicos dentro de Phase 6.

## 1. Guardrails de la decision

- No se declara ganador, mejora QoE ni ranking.
- No se usa `eval` para entrenar, ajustar hiperparametros ni seleccionar modelo.
- No se usan smokes, dry-runs ni logs de runtime como benchmark ni como trazas
  causales de entrenamiento.
- El controller no puede ver `trace_id`, `dataset_id`, `source_id`, `split`,
  `group_id`, `leakage_group`, etiquetas OOD ni throughput futuro.
- Las trazas sinteticas pueden ayudar al entrenamiento/diagnostico, pero deben
  tener cuota limitada y reportarse separadas.
- WSL2/ROCm entrena y genera artefactos externos bajo `~/TFG`; Windows versiona
  codigo/docs; Ubuntu cliente valida Phase 6.

## 2. Lectura paper por paper

| # | Paper | Aporte util para v1 | Decision |
|---:|---|---|---|
| 01 | Comyco | Imitation learning con solver experto, DAgger/rollouts y eficiencia muestral. | Usar como base para oracle + BC, no copiar VMAF ni claims. |
| 02 | Puffer/Fugu | Predictor supervisado de TTP + MPC y validacion real in situ; advierte que ML no gana por ser ML. | Usar predictor + planner como candidato seguro y mantener humildad experimental. |
| 03 | SABR | BC/DPO pretraining + PPO fine-tuning, evaluacion OOD y trazas amplias. | Adoptar pipeline en dos etapas: BC fuerte primero, PPO solo despues de gates. |
| 04 | PLL-ABR | PPO con LSTM/atencion local para dinamica temporal. | Tomar encoder recurrente/atencion ligera como opcion, no como primer riesgo obligatorio. |
| 05 | GreenABR | DRL con energia y VMAF/potencia. | Trabajo futuro; energia no es metrica Phase 6. |
| 06 | ALVS | Live streaming con accion conjunta calidad + playback speed. | Fuera del primer controller; Phase 6 actual es VOD/fake playback. |
| 07 | Edge RL | Edge-assisted, multi-cliente, fairness, VMAF. | Futuro/memoria; requiere infraestructura no disponible en Phase 6. |
| 08 | PCA/GWO/BP | Clasificacion/seleccion hibrida con framing de imagen. | No usar como base; alineacion y trazabilidad ABR debiles frente al resto. |
| 09 | A2BR | Meta-RL, priors de dominio, adaptacion por condiciones heterogeneas. | Inspirar especializacion por regimen; meta-RL completo no es primer paso. |
| 10 | ANT | Detector de dinamica de red + modelos dedicados y switching. | Usar como patron para Mixture/selector posterior. |
| 11 | Souane DRL DASH | Formulacion state/action/reward DASH y simulacion. | Referencia secundaria para contrato RL. |
| 12 | BETA | Under-generalization, deteccion de sesiones pobres, modelos especializados. | Usar para validacion por escenarios y posible specialist controller. |
| 13 | Visual sensitivity | DRL perceptual con HVS/VMAF/content features. | Futuro; VMAF/content artifacts siguen deferred. |
| 14 | Incendio | MARL con expert guidance e inicializacion por experto para short video. | Tomar idea de guidance; descartar MARL/short-video como primer controller. |
| 15 | HAS review | Taxonomia, QoE, energia, retos. | Usar en memoria y justificacion de estado del arte. |
| 16 | Learning-based HAS review | Taxonomia learning-based y riesgos de despliegue. | Usar en memoria y criterios de deployability. |
| 17 | BPA | BiLSTM bandwidth prediction + actor-critic bitrate selection. | Candidato fuerte: predictor de ancho de banda + decision ABR segura. |
| 18 | Fortuna | Offline RL + meta-learning en redes diversas/heavy-tailed. | Futuro GPU largo; demasiado complejo para primer controller integrado. |
| 19 | Gelato/Plume | Skew de trazas, clustering/balanceo y validacion Puffer. | Obligatorio para sampler balanceado por regimen y colas raras. |
| 20 | KAKEN fairness | Fairness/multiusuario y estabilidad. | Futuro; Phase 6 es single-client. |
| 21 | A2BR extendido | Priors, IMDP, actor-critic y adaptacion heterogenea. | Igual que 09: especializacion si el global falla. |
| 22 | Ahaggar | IA como guidance hibrido, CMCD/CMSD, servidor-cliente. | Adoptar filosofia de modelo + decision segura; CMCD/CMSD futuro. |
| 23 | CausalSim | Sesgo causal en simulacion trace-driven. | Guardrail metodologico obligatorio: no logs sesgados como verdad. |
| 24 | EAStream | Meta-RL con latente de entorno/VAE sin fine-tuning online. | Futuro; posible latente de regimen si v1 necesita MoE. |
| 25 | PPO-ABR | PPO aplicado a ABR y comparacion con A3C. | PPO como fine-tuning controlado, no como inicio desde cero. |
| 26 | SODA | No neural, consistente, deployable, robusto ante volatilidad. | Borrow de safety/smoothness/deployability y criterios de aceptacion. |
| 27 | DQNReg | DQN segment-wise para DASH. | No usar como base primaria; util como familia simple de referencia. |
| 28 | MamBRA | SSM/Mamba para prediccion de bandwidth de sesion. | Futuro/predictor avanzado; v1 debe evitar dependencias exoticas. |
| 29 | MERINA | Meta-RL con contexto latente para generalizacion. | Futuro; aporta idea de contexto latente/OOD. |
| 30 | MetaABR | Meta-learning ABR, task split y testbed. | Futuro/regimen; no primer controller. |
| 31 | Oboe | Auto-tuning por estado de red y cambio de parametros. | Usar para selector/regimen y perfiles conservadores. |
| 32 | Pensieve | Formulacion seminal state/action/reward y simulador rapido. | Base historica; no clonar A3C. |

## 3. Sintesis por familias

### 3.1. Imitation learning + experto

Comyco y SABR son los mas importantes para arrancar. La idea defendible no es
"la red aprende de robust_mpc", sino:

1. generar estados en un simulador trace-driven;
2. consultar un experto offline que si puede usar futuro solo para crear labels;
3. entrenar una politica que en runtime solo ve pasado y presente;
4. mitigar compounding error con rollouts tipo DAgger;
5. si el BC pasa gates, hacer fine-tuning PPO con KL/safety.

Esto encaja con DashClientModular4 porque ya existe replay offline, QoE
`qoe_linear_v1`, action mask y Phase 6 trace-driven.

### 3.2. Predictor + decision ABR

Puffer/Fugu, BPA y MamBRA apuntan a que el predictor de ancho de banda puede ser
un modulo separable. Para nuestro problema inmediato, reducir rebuffer en redes
bajas/variables, esto es mas seguro que una politica caja negra pura:

- el predictor aprende capacidad futura/conservadora;
- el planner ABR sigue siendo auditable;
- se pueden registrar cuantiles, riesgo y limites de seguridad por chunk;
- si el predictor duda, el controller puede degradar de forma explicable.

La arquitectura inicial debe usar GRU/LSTM/atencion ligera en PyTorch estandar.
Mamba queda como futuro por coste de dependencia e inferencia.

### 3.3. Especializacion por regimen de red

A2BR, ANT, BETA, Oboe, Gelato/Plume, MERINA, MetaABR y EAStream coinciden en que
un modelo unico puede subgeneralizar. La lectura practica para v1:

- balancear el sampler por throughput medio, variabilidad, drops y cola baja;
- evaluar siempre por buckets, no solo promedio global;
- si un modelo global falla, entrenar especialistas por regimen;
- el selector runtime solo puede usar estadisticas online recientes, nunca
  metadata de traza.

### 3.4. Seguridad, consistencia y deployability

SODA, Oboe, Puffer/Fugu y CausalSim son el ancla de sobriedad. Para presumir de
un controller IA en un TFG, no basta con "red neuronal". Debe ser:

- auditable por chunk;
- calibrado o al menos diagnosticable;
- robusto ante throughput bajo y volatilidad;
- con fallback implementado pero fallback usado igual a 0 en evaluacion;
- con latencia de inferencia acotada;
- evaluado sin mezclar sinteticas con reales.

## 4. Decision de modelos candidatos

Se proponen tres candidatos, ordenados por prioridad.

### Candidato A - `spc_abr_v1`

Nombre academico: Safe Predictive Control ABR v1.

Tipo: predictor neural de throughput/capacidad + planner ABR determinista
risk-aware.

Arquitectura:

- encoder GRU/LSTM sobre historial de throughput, download time, buffer, ultima
  calidad, switch reciente y rebuffer reciente;
- cabeza de prediccion de cuantiles de throughput/capacidad para horizonte
  corto: p10, p25, p50 sobre 1, 3 y 5 chunks;
- planner que simula acciones candidatas con `qoe_linear_v1`, pero usa cuantiles
  conservadores segun estado de buffer;
- guardrail que limita la accion si el buffer es bajo o el p10 no soporta el
  chunk.

Por que construirlo primero:

- ataca directamente el fallo observado: rebuffer por agresividad en redes
  bajas/variables;
- es mas auditable que una politica pura;
- puede competir descriptivamente sin depender de magia RL;
- cada decision puede explicarse por cuantiles, buffer y riesgo.

### Candidato B - `spbc_abr_v1`

Nombre academico: Safe Predictive Behavioral Cloning ABR v1.

Tipo: politica neural con predictor auxiliar, entrenada por behavioral cloning
desde un experto offline `oracle_qoe_beam_v1`.

Arquitectura:

- mismo encoder temporal que `spc_abr_v1`;
- cabeza de policy logits sobre representaciones con action mask;
- cabeza auxiliar de throughput/riesgo para regularizar;
- opcional ranking/DPO step-wise: accion experta preferida frente a acciones
  alternativas de mayor riesgo.

Entrenamiento:

- experto offline por beam search/MPC con futuro solo para labels;
- reward label basado en `qoe_linear_v1`;
- tie-break conservador: menor rebuffer, menor switch, menor bitrate si hay
  empate;
- DAgger-style rollouts para reducir compounding error.

Por que construirlo:

- es el controller IA "de politica" mas defendible a corto plazo;
- aprovecha Comyco/SABR sin depender de los modelos antiguos;
- permite comparar contra `spc_abr_v1` y saber si aprender la politica aporta
  algo sobre planner+predictor.

### Candidato C - `spbc_ppo_abr_v1`

Nombre academico: Safe Predictive BC + PPO ABR v1.

Tipo: fine-tuning RL de `spbc_abr_v1`.

Condicion de entrada:

- solo se entrena si `spbc_abr_v1` pasa gates offline;
- debe mantener KL/regularizacion hacia la politica BC;
- debe usar penalizacion fuerte de rebuffer y CVaR/tail-risk en redes bajas.

Por que no empezar aqui:

- PPO desde cero es menos estable;
- puede subir calidad a costa de rebuffer;
- necesita mas instrumentacion para demostrar que no se salio de la zona segura.

## 5. Opciones descartadas como primer controller

- DQN puro: menos estable y menos alineado con policy masking/Phase 6.
- A3C/Pensieve clonado: historicamente importante, pero no brilla como decision
  nueva.
- Meta-RL completo/MAML/VAE: defendible como futuro, demasiado grande para el
  primer ciclo integrado.
- Mamba/SSM: interesante para predictor, pero introduce riesgo de dependencia;
  GRU/LSTM/atencion ligera bastan para v1.
- Energia, edge, multiusuario, live playback speed, short-video MARL y VMAF:
  buenos para memoria/futuro, fuera del contrato Phase 6 actual.

## 6. Dataset derivado recomendado

Nombre propuesto: `phase45_v1_training_corpus`.

Entradas:

- manifest curado Phase 3;
- solo split `train` para entrenamiento;
- split `test` para validacion offline y seleccion de hiperparametros;
- split `eval` reservado intacto para Phase 6;
- sinteticas con cuota maxima documentada y reporte separado.

Sampler:

- balance por throughput medio: `<=1`, `1-2`, `2-5`, `5-20`, `>20` Mbps;
- balance por variabilidad: baja/media/alta usando CV e indicadores de drops;
- cap por `leakage_group`;
- cap por dataset/semantica para que Puffer/FCC/GAViST/sinteticas no dominen;
- ventanas de 30 segmentos de 4 s como Phase 6, con variantes de arranque.

Features visibles por modelo:

- historial de throughput medido;
- historial de download time;
- buffer actual;
- ultima representacion y bitrate;
- rebuffer reciente;
- switch reciente;
- segmento actual normalizado/restante;
- ladder y chunk size por candidato;
- mascara de acciones validas.

Labels permitidos solo en entrenamiento:

- accion experta `oracle_qoe_beam_v1`;
- reward por segmento `qoe_linear_v1`;
- targets de throughput futuro para predictor, derivados del replay;
- diagnosticos de regimen para auditoria, no como input runtime.

## 7. Entrenamiento y barridos

Primer barrido recomendado:

- encoder: GRU, LSTM, GRU + atencion ligera;
- history length: 5, 8, 12;
- hidden size: 64, 128;
- dropout: 0.0, 0.1;
- optimizer: AdamW;
- losses: CE/DPO para policy, pinball loss para cuantiles, risk BCE si se
  etiqueta rebuffer posible;
- safety factor inicial: 0.80, 0.90, 1.00 segun buffer;
- synthetic quota: 0%, 10%, 15%.

Promocion offline minima:

- dataset validation OK y leakage audit OK;
- inferencia CPU < 50 ms por decision en Windows y Ubuntu cliente;
- action mask siempre respetada;
- fallback usado = 0 en smokes con bundle valido;
- sin NaN/Inf;
- reporte por buckets reales y sinteticas separadas;
- no empeorar de forma catastrofica el rebuffer en buckets `<=1` y `1-2` Mbps
  durante validacion offline. Esto no es claim de mejora ni ranking.

## 8. Bundle e integracion

Crear paquete nuevo, independiente del bundle antiguo:

```text
~/TFG/modelos/phase45_v1/<controller_key>/<timestamp>/
  bundle_manifest.json
  model.pt
  normalizacion_train_only.json
  feature_schema.json
  model_card.json
  inference_contract.json
  training_report.json
  leakage_audit.json
```

Schema IDs propuestos:

- `phase45_v1_training_corpus_v1`
- `phase45_v1_spc_abr_bundle_v1`
- `phase45_v1_spbc_abr_bundle_v1`
- `phase45_v1_controller_telemetry_v1`

Controllers registrados:

- `spc_abr_v1`
- `spbc_abr_v1`
- `spbc_ppo_abr_v1` solo si supera gates previos

Phase 6 los descubrira automaticamente al estar en `CONTROLLER_REGISTRY`, salvo
que se excluyan explicitamente por config.

## 9. Telemetria obligatoria por chunk

Campos minimos para controllers v1:

- `feedback_neural_controller_key`
- `feedback_neural_model_label`
- `feedback_neural_bundle_loaded`
- `feedback_neural_bundle_hash_ok`
- `feedback_neural_feature_vector_ok`
- `feedback_neural_inference_ms`
- `feedback_neural_raw_action`
- `feedback_neural_safe_action`
- `feedback_neural_fallback_used`
- `feedback_neural_fallback_reason`
- `feedback_neural_prediction_p10_bps`
- `feedback_neural_prediction_p25_bps`
- `feedback_neural_prediction_p50_bps`
- `feedback_neural_rebuffer_risk`
- `feedback_neural_safety_intervened`

Para Phase 6 evaluable, se espera:

```text
bundle_loaded=1
bundle_hash_ok=1
fallback_used=0
fallback_reason=success_neural
```

## 10. Roadmap inmediato

1. Escribir specs implementables de dataset, oracle, modelo, bundle,
   controller y tests.
2. Implementar scripts de dataset y oracle offline sin tocar `player.py`.
3. Entrenar en WSL2 `spc_abr_v1` y `spbc_abr_v1`.
4. Exportar bundles externos y validar inferencia.
5. Integrar controllers plug-and-play.
6. Ejecutar en Ubuntu cliente Phase 6 `diagnostico` y `rapido`.
7. Solo si prometen, pasar a `equilibrado`.

Decision final de arranque:

```text
Construir primero `spc_abr_v1` y `spbc_abr_v1`.
Reservar `spbc_ppo_abr_v1` para fine-tuning posterior condicionado por gates.
No empezar por meta-RL/Mamba/MARL/edge/energia/VMAF.
```


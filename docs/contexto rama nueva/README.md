# Contexto rama nueva

Esta carpeta contiene el contexto canonico de la rama `rebuild/phase3-from-phase2`.

La rama se reinicia desde el cierre real de Phase 2. Por tanto, las fases anteriores a Phase 3 pueden apoyarse en `docs/contexto rama original`, pero Phase 3 y posteriores deben documentarse aqui con las decisiones nuevas.

## Indice

```text
02_traces_replay     Phase 3 Rebuild: trazas, normalizacion, manifests y replay tecnico.
03_qoe_reward        Phase 3.5 Rebuild: QoE, reward, gates y no-ranking.
04_neural_abr        Phase 4 Rebuild: modelo offline, sampler y entrenamiento.
05_neural_controller Phase 5 Rebuild: integracion de dos controllers IA.
fase_verificacion_cliente_y_controllers_clasicos
                     Verificacion del cliente DASH y controllers clasicos.
06_validation        Phase 6 futura: validacion formal y protocolo.
07_memoria_defensa   Material futuro para memoria y defensa.
```

## Reglas

- No meter artifacts generados en Git.
- No llamar benchmark a smokes.
- No usar dry-runs legacy como datos de entrenamiento.
- No declarar ranking, ganador ni mejora de QoE hasta que una fase de evaluacion formal lo autorice.
- Usar siempre los documentos obligatorios de arquitectura y procedimiento antes de cambios relevantes.

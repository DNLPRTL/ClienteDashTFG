# Apoyo de la memoria — reproducción de las decisiones del controlador propio

Scripts que respaldan los números del apartado 5.6.4 (Tabla 5.7) y la
Figura 5.3. Todos leen el material de entrega (`TFG Material\`), no el repo.

| Script | Qué hace | Salida |
|---|---|---|
| `reproducir_decisiones_propio.py` | Reinyecta, decisión a decisión, la realimentación registrada en la telemetría de las 60 sesiones del controlador propio (paquete `20260810_133520_tfg_final`) en un `ControladorPropio` nuevo con el bundle de `03_modelos`. Comprueba que la acción coincide con la registrada y evalúa variantes sobre el mismo estado (solo mediana, solo q10, media de los 4, tamaños nominales, sin ensanchado epistémico, progreso medido como en el entrenamiento). Unos 5 minutos en CPU. | `TFG\apoyo_memoria\decisiones_propio.jsonl` y `resumen_reproduccion.json` |
| `analizar_decisiones_propio.py` | Resume las decisiones (reales y sintéticas por separado) y elige el ejemplo de la Figura 5.3 con la regla fijada de antemano (ver su cabecera). | `resumen_decisiones_propio.json` (aquí) y `TFG\apoyo_memoria\ejemplo_decision.json` |
| `generar_fig_5_3.py` | Dibuja la Figura 5.3 a partir del ejemplo. | `docs/memoria/figuras/fig_5_3_decision_real.svg` |

Orden de ejecución (Windows, Python con torch y numpy):

```bash
python docs/memoria/apoyo/reproducir_decisiones_propio.py
python docs/memoria/apoyo/analizar_decisiones_propio.py
python docs/memoria/apoyo/generar_fig_5_3.py
```

Resultado de referencia (13/10/2026, torch 2.6.0 CPU en Windows; el experimento
corrió con torch 2.4.1 en la VM): 1740/1740 decisiones reproducidas exactamente.
Los datos pesados (JSONL de 3,6 MB) viven fuera del repo, en `TFG\apoyo_memoria\`.

**Segunda evaluación (réplica con ventanas nuevas, 14/10/2026).** Los dos
primeros scripts aceptan otro paquete y otra carpeta, sin tocar los datos de
agosto:

```bash
python docs/memoria/apoyo/reproducir_decisiones_propio.py --paquete "<TFG>\validacion_comparativa_replica\20261013_233745_tfg_final" --salida "<TFG>\apoyo_memoria\replica"
python docs/memoria/apoyo/analizar_decisiones_propio.py --datos "<TFG>\apoyo_memoria\replica" --salida docs/memoria/apoyo/resumen_decisiones_propio_replica.json --fuente "telemetria del paquete 20261013_233745_tfg_final reproducida con el bundle de 03_modelos"
```

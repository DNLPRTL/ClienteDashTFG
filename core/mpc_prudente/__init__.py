"""MPC Neuronal Prudente — línea de controller IA ABR fiel-al-vídeo y prudente.

Reconstrucción rigurosa del controller IA del TFG. Reutiliza primitivas probadas
(predictor de cuantiles, action mask, QoE) pero corrige las dos causas raíz del
bajo QoE de las líneas previas:

1. Fidelidad al medio real: entrenar y planificar con el peso real (VBR) de cada
   segmento del MPD del cliente, no con la aproximación CBR (bitrate x duración).
2. Prudencia: objetivo de planificación consciente del riesgo sobre la cola mala
   del throughput, en vez de una regla fija buffer -> cuantil.

No hereda ni modifica los controllers congelados de `phase45_v3` (v1/v2).
"""

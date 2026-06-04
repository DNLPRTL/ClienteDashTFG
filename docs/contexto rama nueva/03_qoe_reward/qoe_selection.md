# QoE selection

Status: closed_phase3_5_rebuild_contract.

La metrica primaria futura queda fijada como `qoe_linear_mean`, derivada de `qoe_linear_v1`.

La decision se conserva de la rama anterior porque sigue siendo adecuada para esta rama reconstruida:

- calidad positiva por bitrate
- penalizacion fuerte por rebuffering
- penalizacion por cambios bruscos de calidad
- calculable desde telemetria de segmentos
- compatible con baselines ABR y con un reward candidato para IA futura

No se adopta VMAF en esta fase porque requiere artifacts perceptuales y una pipeline adicional. No se penaliza startup en la metrica primaria porque todavia no esta medido de forma homogenea en todos los modos.

`qoe_log_v1` queda como metrica secundaria de sensibilidad, no como metrica primaria.

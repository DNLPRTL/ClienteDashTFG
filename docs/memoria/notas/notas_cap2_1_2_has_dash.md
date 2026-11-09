# Notas de la apertura del capítulo 2 y de 2.1–2.2 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap2_1_2_has_dash.docx` (≈1520 palabras de cuerpo, 4 páginas: apertura del
capítulo + 2.1 Streaming adaptativo sobre HTTP (4 párrafos, incl. antecedentes locales) + 2.2 MPEG-DASH (4 párrafos);
9 citas, sin figuras ni tablas). Generado por `docs/memoria/apoyo/generar_cap2_1_2.py` (lee la escalera y la duración
de segmento del MPD entregado para no escribirlas a mano). Comprobador sin avisos.

## Por qué 2.1 y 2.2 juntos

Son contexto corto (la biblia da 12–16 páginas al capítulo entero, ~2 por apartado) y comparten fuentes. Los
apartados 2.3–2.7 irán uno por turno: el 2.4 (familias, tabla estrella) es el más largo.

## Citas verificadas (página del PDF en `biblioteca_final/`)

| Clave | Afirmación | Dónde |
|---|---|---|
| `seufert2015hasQoeSurvey` | vídeo = 57 % del tráfico de consumo en 2012 | p. 1 (469), introducción |
| ídem | MSS 2008, HLS 2009, HDS 2010, incompatibles; 3GPP TS 26.234 Rel. 9 (2009); DASH por MPEG en 2012 | p. 5 (§III-A) |
| ídem | compromiso del tamaño de segmento (cortos: muchos ficheros; largos: no se adaptan a fluctuaciones rápidas → más paradas; buffer mayor compensa) | p. 13–14 (Tabla III y texto) |
| `timmerer2025hasReview` | «more than half of global Internet traffic» | p. 2 |
| ídem | CMAF armoniza HLS/DASH sobre ISO BMFF y habilita baja latencia; MSE/EME y ABR en JavaScript | p. 4 |
| ídem | per-title encoding | p. 2 y §3.2 (p. 8) |
| `stockhammer2011dash` | HTTP sin estado; descarga progresiva como antecedente; principios 1–7 (NAT/firewall, servidores y cachés estándar, CDN, control en el cliente) | p. 1–2 (§2 Design Principles) |
| `peroni2025pipelineSurvey` | cadena de mejor esfuerzo CP → CDN → cliente, con ABR como eslabón | p. 1 (resumen) |
| `ameigeiras2012youtubeTraffic` | ráfaga inicial de 40 s y throttling a un múltiplo de la tasa de codificación (factor 1,25); reducción del ancho de banda → interrupciones | p. 1–2 (resumen y §2), Tabla p. 5 («burst … 40 s», «throttle-factor») |
| `ramosMunoz2014mobileYoutube` | Android gama alta: doble umbral que interrumpe/reanuda según el buffer; iOS: descarga no interrumpida | p. 1 (resumen) |
| `iso23009_1_2022` | modelo de datos jerárquico Period → Adaptation Set → Representation → Segment; representaciones perceptualmente equivalentes, cambio sin interrupción; segmento de inicialización; plantillas (SegmentTemplate); perfil isoff-live | p. 21 del PDF (§5.3.1, pág. 13 del estándar); SegmentTemplate p. 44–45; isoff-live p. 190, 266 |
| `timmerer2012dashCreationConsumption` | cadena creación → consumo (tutorial MM'12) | p. 1 (resumen) |
| `dashIfIop` | puntos de interoperabilidad, v4.1 (2017) | p. 1 y 3 |

Datos del proyecto en el texto: 6 representaciones de 300 a 4300 kbit/s y segmentos de 4 s (leídos del MPD de Paseo
30 fps; `timescale 15360 / duration 61440`); perfil `urn:mpeg:dash:profile:isoff-live:2011`; plantilla `$Number$`.
«4 s, la duración de los conjuntos de referencia con los que se compara»: Pensieve usa segmentos de ≈4 s (p. 8).

## Decisiones de redacción

- Apertura del capítulo con el mapa 2.1–2.7 (biblia §6.3).
- Antecedentes locales dentro del 2.1 (no como subapartado): dos trabajos del grupo del tutor (Ramos-Muñoz es el
  primer autor del de 2014). Párrafo sugerido en `local_streaming_source_evidence.md` reescrito; sin figuras copiadas.
- No se usan siglas sin expansión: HAS, MPD, CMAF se expanden; «MSE/EME» no se nombran como siglas.
- El 2.2 anticipa las dos decisiones de empaquetado que importan al resto (duración de segmento y tasa nominal
  frente a tamaño real, «central en este trabajo») y remite a 2.4 y 4.7, sin adelantar resultados.
- El perfil isoff-live «aunque el nombre alude al directo, es el habitual para VoD empaquetado por herramientas de
  código abierto»: es lo que produce GPAC con `-profile live`; se dice sin cita porque es constatación del propio
  contenido (MPD entregado).

## Preguntas probables del tribunal

1. **¿Por qué HTTP y no un protocolo de streaming?** Principios de Stockhammer: sin estado, NAT/firewall, cachés y CDN
   existentes, control en el cliente.
2. **¿Qué normaliza DASH y qué no?** MPD y segmentos sí; la decisión del cliente no. Por eso existe este trabajo.
3. **¿Por qué 4 s de segmento?** Compromiso de Seufert; valor de Pensieve y de los conjuntos de referencia.
4. **¿Qué tienen que ver los papers de YouTube del tutor?** Muestran el problema previo al HAS (ráfaga + throttling,
   umbrales fijos de buffer en el terminal) que la adaptación en el cliente resuelve.

## Qué se puede recortar

El párrafo de evolución (CMAF, per-title) a dos frases, y el último párrafo del 2.2 a la mitad si el 4.7 ya cuenta la
diferencia nominal/real. Mantener los principios de Stockhammer y el modelo de datos del MPD.

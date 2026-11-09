# Notas del capítulo 3 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap3_planificacion_costes.docx` (≈1390 palabras de cuerpo, 6 páginas:
apertura, 3.1 metodología y fases (lista con entradilla), 3.2 cronograma e hitos (Figura 3.1 Gantt), 3.3 horas
(Tabla 3.2), 3.4 costes (ecuación 3.1, Tablas 3.3 y 3.4), cierre sin epígrafe; Tabla 3.1 fases → tareas → entregable;
sin citas). Generado por `docs/memoria/apoyo/generar_cap3.py`. Comprobador sin avisos.

## CÓMO EDITARLO (lo que pidió Daniel: «todo montado y que yo pueda modificarlo»)

**Única fuente de datos: `docs/memoria/apoyo/planificacion_cap3.json`.** Ahí están las fases (id, nombre, fechas
inicio/fin, horas, tipo, descripción, tareas, entregable), los hitos, los supuestos (tarifas, horas del tutor, vida
útil, meses) y las listas de hardware y software. Cambias lo que quieras y ejecutas:

```bash
py -3.12 docs/memoria/apoyo/generar_cap3.py
```

Se regeneran el Gantt (`figuras/fig_3_1_gantt.svg/png`), las cuatro tablas y el texto (los totales, porcentajes,
fechas en letra y recuentos se recalculan solos). El script comprueba que el primer commit (2026-05-06) sigue siendo
el del repositorio y que las fechas del proyecto cuadran con `meses_proyecto`.

Lo que **debes revisar** porque son hipótesis mías (marcadas en el JSON como `supuestos` y en el texto como
«hipótesis habituales en los trabajos de la escuela»):
- **Fechas de F1** (estudio previo, 20/04–15/05): anteriores al primer commit; pon las tuyas.
- **Horas por fase**: 30/50/40/25/70/45/40 = 300 h (12 ECTS × 25 h, como el TFG del tutor de 2024). Si quieres reflejar
  las horas reales, cámbialas; el texto dice «que corresponde a los 12 créditos…» solo si el total es 300. Si no es 300,
  avísame y cambio esa frase (o quítala tú del generador).
- **Tarifas**: alumno 20 €/h, tutor 50 €/h, 25 h de tutor. Corpus: 20–25 €/h y 50 €/h.
- **Hardware**: 1800 € el equipo (i5-14600KF, 32 GiB, RX 7800 XT) y 300 € periféricos; vida útil 4 años; 7 meses →
  262,50 + 43,75 = 306,25 €. Pon los precios reales de tus facturas.
- **Total**: 6000 + 1250 + 306,25 + 0 = 7556,25 € (96 % recursos humanos).

## Por qué estas fases y fechas (criterio, no caos)

- Siete fases con nombre funcional, fechas redondeadas a la semana y solapes explícitos (dicho en el texto). Anclas
  reales del git: primer commit 06/05; 118 commits en junio (cliente+infraestructura+clásicos); julio SIN commits
  (entrenamiento en WSL, por eso F5 cubre julio); 10/08 paquete de agosto y arranque de `docs/memoria`; 14/10 blindaje;
  15–16/10 experimento final; noviembre redacción. Los nombres internos (Phase 1–7, phase45, Q_H, SPBC) NO aparecen:
  se describen funcionalmente (04_CORRESPONDENCIAS §5).
- Las «dos desviaciones» (iteraciones descartadas del controlador; fase de blindaje con parada del experimento del
  14/10) se cuentan como replanificación honesta, sin cifras de desarrollo (regla del experimento único).
- Gantt con la paleta sobria: estudio gris claro, desarrollo gris, validación azul, redacción amarillo; hitos en
  líneas punteadas y el experimento final en rojo.
- Ecuación (3.1) de amortización expuesta y numerada (el tutor 2024 las pone sin numerar; la biblia pide numerar).

## Preguntas probables del tribunal

1. **¿300 h para todo esto?** Es la carga nominal del TFG; se declara que no incluye las 41,3 h de máquina del
   experimento ni el entrenamiento en GPU. (Si Daniel pone sus horas reales, la respuesta cambia.)
2. **¿Por qué no hay coste de nube?** Todo corrió en un equipo propio: dos VM y WSL en el mismo PC.
3. **¿Qué pasó en octubre?** La evaluación de agosto destapó deficiencias; se detuvo el experimento en marcha, se
   blindó el código y se ejecutó una sola vez el final. Replanificación consciente, no retraso.

## Qué se puede recortar

El párrafo de software a dos frases; la Tabla 3.1 si el índice de la memoria va justo (las tareas están en 3.1).
Mantener el Gantt, la Tabla 3.2 y la Tabla 3.4.

# Notas del 6.5 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap6_5_descriptivos.docx` (≈1140 palabras de cuerpo, 4 páginas, Tablas 6.8 y
6.9, Figuras 6.3 y 6.4, sin ecuaciones, sin citas nuevas). Generado por `docs/memoria/apoyo/generar_cap6_5.py`,
que dibuja las dos figuras con matplotlib (`figuras/fig_6_3_cdf_qoe.svg/png`, `fig_6_4_paradas_bitrate.svg/png`).
Comprobador sin avisos; render con Word revisado.

## Cambio en la clase Borrador

`memoria_docx.Borrador.tabla` fija ahora la disposición de tabla (`tblLayout fixed`, `autofit = False`) y el ancho
de cada columna: Word ya no estrecha las columnas numéricas al contenido (la Tabla 6.8, de 8 columnas, salía con
«2,58/3» partido). Los `.docx` anteriores no cambian hasta que se regeneren; si se regeneran, solo cambia el ajuste.

## Qué hace el script (todo por programa)

- Tabla 6.8: recalcula desde `sesiones.csv` (148 reales por controlador) QoE lineal, QoE log, bitrate, rebuffering,
  paradas, fracción con parada, cambios, mínimo y máximo de rebuffering, y exige igualdad con
  `agregados_por_controlador.json`; el percentil 5 de la QoE se toma del paquete (`qoe_lineal_p05`).
- Comprueba que el orden por QoE lineal es recientes > mediana > MPC robusto > propio > fijos > BBA > tasa > BOLA,
  que la QoE log ordena igual, y que el propio es el 4.º (NO el primero).
- Tabla 6.9: verifica la identidad QoE = calidad_media − 4,3·rebuf/29 − suavidad/29 en las 1184 sesiones, forma los
  148 escenarios y descompone propio − rival; la suma de componentes iguala la ΔQoE de las secundarias del JSON.
- Figura 6.3: CDF empírica por controlador; eje cortado en −1 (BOLA tiene 8 sesiones por debajo, mínimo −17,26).
- Figura 6.4: paradas/sesión frente a bitrate medio, 8 puntos con la QoE entre paréntesis.
- Ejemplo (regla fijada antes de mirar: el escenario con mayor diferencia de QoE a favor del MPC robusto): ventana 7
  (Oboe), Tears of Steel: propio 2,610 frente a 2,957 (−0,347); 0 paradas ambos; bitrate −0,247, suavidad −0,100.
  (Coincide con la «peor ventana» del propio frente al MPC que lista `resumen_resultados.md`: real_007, tears.)

## Fuente de cada número

| Dato | Fuente |
|---|---|
| Tabla 6.8 | `sesiones.csv` = `agregados_por_controlador.json` |
| «12 y 20 veces más paradas» | 0,480/0,041 = 11,7; 0,831/0,041 = 20,3 |
| 0,149 y 0,796 menos que el propio (fijos, tasa) | 2,547 − 2,398; 2,547 − 1,751 |
| BBA 11,2 cambios; BOLA 4,05 s y 1,22 paradas; tasa 1895 kbit/s | Tabla 6.8 |
| p05: propio 0,625, MPC 0,512, mediana 0,479 | `qoe_lineal_p05` del paquete |
| BOLA 8 sesiones con QoE < 0 (y 8 < −1), mínimo −17,26, 120,6 s | `sesiones.csv` |
| «ningún otro baja de −0,59» | mínimo de BBA (−0,588) |
| Tabla 6.9 | descomposición desde `sesiones.csv`; IC95 de `contrastes_prerregistrados.json → secundarias` |
| −59 kbit/s = −2,1 % | 2727,0 − 2785,6 |
| aportes de cada pieza (−0,036 [−0,071; −0,003], +0,014 [−0,027; +0,047], −0,024 [−0,071; +0,023]) | secundarias del JSON |

## Decisiones de redacción

- Primera frase de lectura: «el controlador propio no tiene la QoE lineal media más alta» (regla de 07_RESULTADO §6).
- Las dos figuras del paquete equivalentes (`cdf_qoe_lineal.png`, `calidad_vs_rebuffering.png`) NO se pegan: estilo
  distinto (colores por defecto de matplotlib, nombres internos). Se rehacen con la paleta sobria desde `sesiones.csv`.
- La QoE log se menciona solo para decir que ordena igual; no se concluye nada (referencia por sesión, 6.2).
- «En paradas no se distingue del basado en tasa ni de BBA»: IC95 de Δparadas incluyen 0 (tasa [+0,000; +0,047];
  BBA [−0,338; +0,007]). Correcto decirlo así.

## Preguntas probables del tribunal

1. **Si las variantes arriesgadas tienen más QoE, ¿por qué no usarlas?** Porque paran 12 y 20 veces más; la QoE
   lineal diluye la parada entre 29 segmentos. El criterio de seguridad estaba prerregistrado (P2–P5).
2. **¿Dónde pierde el propio?** En las sesiones fáciles, cediendo ~59 kbit/s de bitrate (2,1 %); lo recupera en
   rebuffering y suavidad. Ejemplo de la ventana 7 con Tears of Steel (−0,347).
3. **¿Por qué BOLA tan mal?** Tamaños nominales y buffer: en redes de baja capacidad pide niveles que no sostiene;
   una sesión con 120,6 s de rebuffering. Es el BOLA del artículo, sin calibrar (5.5).
4. **¿Qué significa el percentil 5 más alto?** Que las peores sesiones del propio son menos malas que las de
   cualquier otro: es donde se nota la agregación de riesgo.

## Qué se puede recortar

El párrafo de los clásicos (fundir en dos frases) y la Figura 6.4 si sobra espacio (la Tabla 6.8 ya lo dice).
Mantener la Tabla 6.9 y la Figura 6.3.

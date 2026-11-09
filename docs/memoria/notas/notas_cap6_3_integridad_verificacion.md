# Notas del 6.3 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap6_3_integridad_verificacion.docx` (≈1340 palabras de cuerpo, 4 páginas,
3 subapartados, Tabla 6.6, sin figura, sin ecuaciones, sin citas nuevas). Generado por
`docs/memoria/apoyo/generar_cap6_3.py` (≈1 min la primera vez). Comprobador sin avisos; render con Word revisado.

## Qué hace el script (todo por programa; falla si algo no cuadra)

- Manifiestos y `entorno.json` de las 1208 ejecuciones: una sola carpeta de ejecución por sesión, estado completado,
  un único entorno (Python 3.8.10, Linux 5.15.0-139, requests 2.32.4, numpy 1.24.4, matplotlib 3.7.5, pandas 2.0.3);
  inicios 15/10 01:17:43 → 16/10 18:34:39 UTC; hueco máximo entre inicios 246 s; 41,32 h.
- `ventanas_trazas.csv` = `kit_vm/ventanas_esperadas_final.txt` (77 ids, mismo orden).
- `sesiones.csv`: 604 sesiones del propio y variantes, 17 516 decisiones, 0 respaldos, 17 516 filas de auditoría ok,
  8758 inferencias (2 × 4379). `segmentos.csv`: 35 032 filas, respaldo_usado = 0 en todas.
- Latencias (`latencia_decision_ms`): p99 global 4,42 ms; p99 por controlador 0,04–0,05 (clásicos), 2,89 (MPC
  robusto), 4,11–4,66 (variantes), 5,94 (propio); mediana del propio 2,88; 4 decisiones > 20 ms, todas con
  `indice_segmento = 2` (primera decisión): s00192 propio 22,4; s00325 cuantiles recientes 21,3; s01093 MPC robusto
  20,3; s01119 cuantiles recientes 23,4 ms. Primera decisión del propio: mediana 5,60 ms. Inferencia máx 5,60 ms.
- Compuertas: 8/8 (`resumen_resultados.json → gates.detalle_gates`), violaciones vacías; verificación 15/15
  (`verificacion_paquete.json`), preset final_blindaje; 24 sesiones sintéticas.
- Huellas: recalcula el SHA-256 de los 9699 ficheros del paquete y los compara con `huellas_paquete.sha256`; la huella
  de la lista es e5dc724b…3126 (= 07_RESULTADO).
- Auditoría (`auditoria_decisiones.json`): 35 032 decisiones, 0 distintas, 0 respaldos; 4379 por controlador.
- Validación del simulador (`validacion_simulador.json`): forzado 1184 sesiones, niveles idénticos 1184, mediana |ΔQoE|
  0,000, p90 0,0055, máx 0,208, sesgo +0,0029 (sim − VM); 22 sesiones > 0,05, las 22 con rebuf_vm > rebuf_sim.
  Cerrado: pareadas propio − MPC robusto, n 148, media VM −0,0008, sim +0,0020, correlación 0,866.
- Repite `contrastes_prerregistrados(sesiones.csv, hipotesis_del_paquete)` con el módulo del entregable y compara
  número a número con `contrastes_prerregistrados.json`: 0 diferencias > 1e-9 (principales, secundarias, estratos,
  interacción). Resultado guardado en `apoyo/contrastes_reproducidos.json` (caché; borrar para repetir).
- Ejemplo sesión 8: 29 decisiones idénticas, 0 respaldos; inferencia media 1,20 ms; latencia mediana 2,81 ms,
  primera 5,4 ms; forzado: qoe_sim = qoe_vm = 3,974; error mediano del buffer 0,034 s.

## Lo que NO se dice y por qué

- **Contraprueba de la auditoría** (07_RESULTADO: con α = 0,5 cambian 96 decisiones del propio y con el MPC no
  robusto 876): NO está en `auditoria_decisiones.json` ni en ningún fichero de TFG Material, así que no se cita.
  Se puede regenerar con `docs/blindaje/simulador/auditar_decisiones.py` si se quiere incluir.
- **Indicador `benchmark_autorizado = false`**: no se menciona (lista de presets antigua en `evaluar_gates`).
- **Cifras de las pareadas en lazo cerrado** (−0,001 / +0,002): se dice «difiere en menos de 0,003» para no
  adelantar el valor de P1 antes del 6.4.
- El módulo heredado `estadistica.json` (signo por escenario, empates exactos): no se usa ni se cita.

## Avisos (no van a la memoria)

- Los scripts de auditoría y de validación del simulador viven en el REPO (`docs/blindaje/simulador/`), no en el
  código entregado de TFG Material; sus salidas sí están en TFG Material (`verificacion_windows_20261016/`, con
  LEEME que indica cómo repetirlos). El texto los llama «programa de auditoría» y «simulador en tiempo virtual
  construido con las clases del propio cliente», sin nombrar ficheros. Si Daniel quiere que estén en el entregable,
  copiar `docs/blindaje/simulador/{simulador,auditar_decisiones,validar_simulador}.py` a una carpeta
  `herramientas_verificacion/` del código y recalcular las huellas del kit (OJO: cambiaría la huella del código
  congelado, así que mejor como carpeta aparte en `04_evidencia_final`).
- La «primera decisión» de una sesión es la del segmento 2 (el 1 es calentamiento). Las 4 latencias > 20 ms son
  todas de ese segmento: carga del planificador vectorizado y calentamiento de hilos; no afectan a la QoE porque la
  decisión se toma mientras se reproduce el segmento anterior.
- El hueco máximo de 246 s entre inicios es una sesión larga (BOLA con 120 s de rebuffering), no una pausa.

## Preguntas probables del tribunal

1. **¿Cómo sé que las decisiones las tomó tu modelo y no el respaldo?** 0 respaldos en 17 516 decisiones, filas de
   auditoría completas y 35 032 decisiones repetidas fuera de línea con el código congelado.
2. **¿Por qué una sola repetición?** Las decisiones son deterministas dada la realimentación (auditoría), y la física
   se reproduce (simulador forzado, mediana |ΔQoE| = 0). Repetir las 41 h habría medido el ruido de la VM, no el
   controlador.
3. **¿Qué son las 22 sesiones con |ΔQoE| > 0,05?** Más rebuffering en la VM que en el simulador: esperas del SO
   durante la parada; reparto neutral entre controladores (orden sorteado).
4. **¿El simulador es independiente?** No: comparte modelo de red y dinámica del buffer con el cliente. Valida
   coherencia interna, no fidelidad frente a una red real (6.7).
5. **¿Qué pasaría si el bootstrap cambiara de semilla?** Los intervalos moverían en la tercera cifra; la semilla fija
   permite reproducir exactamente los JSON (hecho: diferencias < 1e-9 en otra máquina y otro Python).

## Qué se puede recortar

El párrafo de latencias a la mitad (dejar p99, las 4 primeras decisiones y la inferencia máxima) y la frase del
lazo cerrado del simulador. Mantener la Tabla 6.6 y el párrafo de la auditoría.

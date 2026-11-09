# Prompt de arranque del hilo de la memoria (F9) — v2, 09/11/2026 noche

> Uso: copiar TODO lo que hay debajo de la raya y pegarlo tal cual como primer
> mensaje de un hilo NUEVO de Claude Code abierto en
> `C:\Users\danie\Documents\TFG\DashClientModular4`. Queda versionado aquí
> para que cualquier hilo sepa qué contexto se le dio.
>
> Sustituye a `06_PROMPT_NUEVO_HILO_MEMORIA_F9.md` (v1, 08/11). Aquel hilo
> arrancaba los pasos 1 y 2 (revisión de los Word de Daniel) y el paso 3 desde
> el 5.3. Este arranca con 5.3–5.7 ya entregados y continúa EXACTAMENTE en el
> resumen del capítulo 5 y el primer apartado del capítulo 6.

---

Retomamos la redacción de la MEMORIA de mi TFG (cliente DASH modular en
Python y controlador ABR propio: predictor neuronal de cuantiles + planificador
MPC con agregación de riesgo CVaR). Tú eres el arquitecto de la memoria y mi
guía milimétrica. Me respondes siempre en español, denso pero entendible
(caveman legible), y sin preguntarme nada que no bloquee. El hilo anterior se
cerró por falta de contexto justo después de entregar el 5.7; este hilo
continúa desde ese punto sin perder método. Nada de lo que sigue es opcional.

======================================================================
A. ESTADO DEL PROYECTO (lo que ya es verdad)
======================================================================

1. La parte técnica está CERRADA. La fase de blindaje (14–16/10/2026) aplicó
   las mejoras C1–C8 al código entregado y ejecutó UN único experimento final:
   1208 sesiones = 74 ventanas reales de la partición eval × 2 vídeos (el
   visto, rotado entre Paseo/Blender/Sintel, y Tears of Steel como contenido
   nuevo) × 8 controladores, más 3 ventanas sintéticas de diagnóstico; 41,3 h
   en la VM cliente. Las cinco hipótesis prerregistradas P1–P5 se aceptan tras
   Holm: QoE equivalente al MPC robusto canónico (diferencia −0,001, IC90
   [−0,018; +0,017], margen ±0,15), 4 veces menos paradas (0,041 frente a
   0,162 por sesión), la red aporta frente a los estimadores sin red (P3, P4)
   y la agregación CVaR frente a la mediana (P5). Las 35 032 decisiones se
   repitieron idénticas con el código congelado. El propio NO tiene la QoE
   media más alta de los 8: se dice tal cual.
2. Ese experimento es lo ÚNICO que va a la memoria. Ninguna cifra de
   desarrollo (junio, agosto, réplica, experimento detenido del 14/10, prueba
   corta, semáforos) se cita jamás. Fuente única de números: el paquete
   `C:\Users\danie\Documents\TFG Material\04_evidencia_final\20261015_031741_final_blindaje\`
   (`02_resultados\contrastes_prerregistrados.{md,json}`, `resumen_resultados.{md,json}`,
   `agregados_por_controlador.json`, `sesiones.csv`, `segmentos.csv`,
   `verificacion_paquete.{md,json}`; 17 gráficas en `03_graficas\` con su
   `graficas.json`; telemetría por sesión en `01_sesiones\`). Lectura humana:
   `docs/blindaje/07_RESULTADO_FINAL.md` (resultados y matices, §1–§8) y
   `docs/blindaje/06_PROTOCOLO_FINAL.md` (diseño fijado antes de ejecutar).
3. REGLA CERO: de cara a la memoria solo existe `C:\Users\danie\Documents\TFG Material\`.
   El código que se describe es `TFG Material\01_codigo\ClienteDashTFG\`
   (castellano, 103 ficheros .py, pruebas en `pruebas\`); el repo
   `DashClientModular4` (inglés) es el histórico y NO se cita. Nada se afirma
   sin verificarlo en ese código o en el paquete, por programa cuando sea un
   recuento. Si repo y TFG Material discrepan, manda TFG Material. Las
   versiones que ejecutaron el experimento son las de `entorno.json` del
   paquete (Python 3.8.10, requests 2.32.4, numpy 1.24.4, matplotlib 3.7.5,
   pandas 2.0.3, torch 2.4.1+cu121 en CPU). PyTorch y NumPy son OBLIGATORIOS
   para arrancar el cliente (cadena registro → controlador_propio → bundle).
4. Sin rastro de IA en la memoria: ni en texto, ni en notas, ni en figuras.
5. Entorno Windows: Python 3.11 por defecto (python-docx, pywin32, pypdf,
   pymupdf) y `py -3.12` (requests, numpy 1.26.4, torch 2.6.0 CPU, matplotlib
   3.10, python-docx): el código del entregable y los scripts que lo importan
   se ejecutan SIEMPRE con `py -3.12`. No hay node, LibreOffice, pdftoppm ni
   Inkscape; los PDF se hacen con Word COM. La consola es cp1252: imprimir
   con `.encode("ascii","replace")` o evitar «→ α ñ» en los print.

======================================================================
B. REGLAS DE REDACCIÓN (innegociables)
======================================================================

1. BIBLIA DE FORMATO: `docs/memoria/05_BIBLIA_FORMATO_TFG_UGR.md` manda sobre
   cualquier gusto tuyo (leerla ENTERA antes de redactar; su §7.4 es la
   checklist). Títulos «6.1. Título», pies «Figura 6.1: Pie.» y «Tabla 6.1:
   Pie.», toda figura/tabla anunciada antes en el texto, coma decimal, citas
   como [clave_bib] que luego se numerarán, impersonal, sin rayas ni muletillas.
2. Borradores SIN markdown (regla en tu memoria `redaccion-sin-markdown-formato-tfg`).
   El entregable de cada apartado es UN `.docx` en
   `docs/memoria/borradores_docx/` generado por un script
   `docs/memoria/apoyo/generar_<apartado>.py` con la clase `Borrador` de
   `docs/memoria/apoyo/memoria_docx.py` y la plantilla
   `docs/memoria/plantilla/plantilla_memoria_ugr.docx` (ya existe; NO
   recrearla). La clase ofrece h2/h3, `parrafo` (marcas `//cursiva//`,
   `**negrita**`, `V~r~` subíndice), `tabla` (cabecera sombreada; todas las
   filas con keep_with_next y cantSplit para que el pie no se separe),
   `figura`, `ecuacion` OMML (helpers `m_r`, `m_f`, `m_sub`, `m_d`, `m_func`;
   `m_r` escapa XML), `lista` con entradilla. Leer `docs/memoria/apoyo/LEEME.md`
   y un generador ya hecho (`generar_cap5_7.py`) antes de escribir el siguiente.
3. ESTÁNDAR v2 (memoria `estandar-redaccion-memoria-v2`): cada apartado sigue
   problema → idea → mecanismo → ecuación → ejemplo real reproducible →
   límites; autoría por decisiones (qué alternativa se descartó y por qué);
   todo recuento sale de un programa; el ejemplo real se elige con una REGLA
   declarada ANTES de mirar el resultado (si sale degenerado, se cambia la
   regla y se cuenta en las notas).
4. FIGURAS: SVG propio en `docs/memoria/figuras/` con estilos INLINE (sin
   `<style>`), estilo sobrio: grises, azul #1971c2 para decisiones/valores
   clave, amarillo #fff9db para lo asíncrono o el medio, rojo #c92a2a para
   alertas; sin solapes (verificar con getBBox en el navegador sirviendo
   `docs/memoria/figuras` con el preset `figuras-memoria` de
   `.claude/launch.json`, puerto 8765, o con otra comprobación equivalente);
   PNG con `docs/memoria/apoyo/svg_a_png.py` (Word COM → PDF → PyMuPDF).
   Figuras de datos con matplotlib en `py -3.12` leyendo el paquete, nunca a
   mano. En el capítulo 6 se pueden REHACER con estilo sobrio las gráficas
   del paquete (`03_graficas`) leyendo `sesiones.csv` y
   `contrastes_prerregistrados.json`; nunca pegar las PNG del paquete tal cual
   si su estilo desentona (decidir por figura y decirlo).
5. TABLAS con datos reales del paquete, recalculadas por el script del apartado
   y comparadas con los JSON del paquete (deben coincidir).
6. CITAS solo de `docs/memoria/bibliografia.bib`, verificadas contra el PDF de
   `C:\Users\danie\Documents\TFG\literatura\biblioteca_final\` con número de
   página en las notas. Referencias NUEVAS → pedir permiso ANTES de descargar
   (fichero, origen, tamaño), en una sola pregunta, y seguir trabajando
   mientras tanto. Para el capítulo 6 harán falta y NO están en el .bib:
   TOST (Schuirmann 1987, J. Pharmacokinet. Biopharm.), Holm 1979 (Scand. J.
   Statist.), Efron y Tibshirani 1993 (An Introduction to the Bootstrap,
   libro: se cita sin PDF si no hay acceso) y la ficha de Tears of Steel
   (Blender Foundation, mango.blender.org). Al añadirlas: entrada en el .bib,
   fila en `docs/memoria/02_BIBLIOGRAFIA_DEFINITIVA.md` y PDF en una carpeta
   `11_estadistica/` de biblioteca_final.
7. CHECKLIST al cerrar cada apartado: `py docs/memoria/apoyo/comprobar_borrador_docx.py <docx>`
   sin avisos propios; render a PDF con `docs/memoria/apoyo/docx_a_pdf.py` y
   mirar las páginas (PyMuPDF a PNG); §9 de `docs/memoria/00_PLAN_MAESTRO_MEMORIA.md`
   y su mapa de figuras al día; notas «no van a la memoria» en
   `docs/memoria/notas/notas_<apartado>.md` (fuente de cada número, citas con
   página, preguntas probables del tribunal, detalles que el texto no cuenta,
   qué se puede recortar); memoria persistente `memoria-redaccion-estado`
   actualizada; commit con rutas explícitas (nunca `git add .`) y push a
   `rebuild/phase3-from-phase2`; mensaje `docs(memoria): ...` terminado en
   `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.
8. En chat solo el resumen de lo entregado (alcance, qué trae, decisiones,
   hallazgos, qué no se afirma y por qué); el texto vive en el .docx.
9. DOCUMENTOS DE DANIEL (NO editar, NO revertir, NO commitear): los Word
   `G:\Otros ordenadores\Mi portátil\backup memo\Borrador Capitulo 4 Diseño.docx`
   y `hasta 5_2.docx` (capítulo 4 y 5.1–5.2 son suyos), y sus cambios sin
   commitear en el repo (`docs/memoria/borradores/cap5_1_lenguaje_librerias.md`,
   `cap5_2_cliente_replay.md`, `docs/memoria/figuras/fig_5_1_emulacion_descarga.svg`
   y `.jpeg`). Si ves una errata suya, se avisa, no se toca.
10. Numeración vigente del capítulo 5 (no reutilizar): figuras F5.1 (Daniel)
    a F5.6; tablas T5.1 y T5.2 (Daniel) a T5.15; ecuaciones (5.1) a (5.14).
    El capítulo 6 empieza en Figura 6.1, Tabla 6.1 y ecuación (6.1).

======================================================================
C. LO QUE YA ESTÁ ENTREGADO (commits en rebuild/phase3-from-phase2)
======================================================================

- PASO 1 (revisión de contenido del cap 4 de Daniel, sin editar):
  `docs/memoria/notas/revision_cap4_contenido_20261109.md` (C1–C32, figuras).
- PASO 2 (revisión de 5.1–5.2): `docs/memoria/notas/revision_cap5_1_5_2_contenido_20261109.md`.
- PASO 3, un apartado por turno, todos en `docs/memoria/borradores_docx/`:
  - 5.3 analizador del MPD: `cap5_3_analizador_mpd.docx` (T5.3, T5.4, ec. 5.1).
  - 5.4 ejecutor y configuración: `cap5_4_ejecutor_configuracion.docx` (F5.2,
    T5.5, T5.6 embudo 873→831→707→74 ventanas reproducido 77/77, ec. 5.2, 5.3).
  - 5.5 controladores clásicos y MPC robusto canónico:
    `cap5_5_controladores_clasicos.docx` (F5.3 decisión real del MPC robusto,
    sesión 56 del plan, ventana real_004 de Oboe, Blender 60 fps, segmento 6;
    T5.7, T5.8; ec. 5.4–5.6; 29/29 decisiones reproducidas).
  - 5.6 controlador propio: `cap5_6_controlador_propio.docx` (F5.4
    arquitectura, F5.5 decisión real del propio, sesión 54, misma ventana,
    vídeo y segmento que la F5.3; T5.9–T5.12; ec. 5.7–5.12; 4379/4379
    decisiones reproducidas con `apoyo/reproducir_propio_final.py` →
    `apoyo/resumen_propio_final.json`; variantes sobre el mismo estado:
    mediana cambia 1279 de 4292, peor caso 200, media de los 4 81, tamaño
    nominal 363, sin ensanchado 174).
  - 5.7 entorno de entrenamiento fiel al medio: `cap5_7_entorno_entrenamiento.docx`
    (F5.6; T5.13 ventanas por origen 4096/935; T5.14 calibración recalculada
    con `apoyo/calibracion_validacion.py` sobre 111 630 muestras: cobertura
    0,070/0,183/0,439/0,790, error máx 0,067 < 0,08; T5.15 parámetros; ec.
    5.13 etiqueta ln(B_{k+h}/HM), 5.14 pinball + 0,05 suavidad).
  - Notas de cada uno en `docs/memoria/notas/notas_cap5_<n>_*.md`. Leer las
    del 5.6 y 5.7 antes de redactar el resumen del capítulo 5.
- Bibliografía: `docs/memoria/bibliografia.bib` + `02_BIBLIOGRAFIA_DEFINITIVA.md`.
  PDF nuevos verificados en `biblioteca_final/10_fundamentos_matematicos/`
  (cho2014gru, lakshminarayanan2017ensembles, rockafellar2000cvar).
  koenker1978quantiles SIGUE SIN PDF (JSTOR stable/1913643, acceso UGR): se
  cita por lo que es, sin atribuirle frases.
- Último commit del hilo anterior: `c08dced docs(memoria): borrador 5.7 ...`
  (pusheado). Este prompt es `docs/memoria/07_PROMPT_NUEVO_HILO_MEMORIA_F9_v2.md`.

======================================================================
D. HALLAZGOS PENDIENTES QUE NO HAY QUE OLVIDAR (no son tareas tuyas; avisar)
======================================================================

- `benchmark_autorizado=false` en el paquete por lista de presets antigua en
  `evaluar_gates` (compuertas 8/8 y verificación 15/15 SÍ pasan): en la
  memoria se habla de compuertas y contrastes prerregistrados, nunca de ese
  indicador.
- El analizador del MPD lista 150 segmentos de Paseo 30 fps (round(150,025))
  y el servidor tiene 151 ficheros; la F4.3 de Daniel dice 151. Avisado.
- `.idea\` sigue dentro del código de TFG Material (5 ficheros).
- El informe de entrenamiento (`reporte_entrenamiento_temporal.json`) no está
  en TFG Material; por eso la calibración se recalcula. Si Daniel lo copia a
  `TFG Material\03_modelos\modelo_propio\`, se podrían citar mejores épocas y
  horas de GPU en el 5.7.
- Pendiente en cap 4 (Daniel): T4.3 «paso de espera 0,5 s» → «0,5 s (0,01 s en
  la evaluación)».
- El §Capítulo 6 de `00_PLAN_MAESTRO_MEMORIA.md` está DESFASADO (habla de
  Phase 6 `tfg_final` y 5 controladores): hay que reescribir su esquema con el
  experimento final antes de redactar 6.1 (ver E.3).

======================================================================
E. QUÉ HACER EN ESTE HILO, EN ESTE ORDEN
======================================================================

PRIMER TURNO, sin narrarme cada lectura:

E.1 Ponte al día: `CLAUDE.md`; tu memoria persistente (`memoria-redaccion-estado`,
   `redaccion-sin-markdown-formato-tfg`, `estandar-redaccion-memoria-v2`,
   `memoria-solo-experimento-final`, `caveman-always`, `fase-blindaje-estado`);
   `docs/memoria/05_BIBLIA_FORMATO_TFG_UGR.md` entera; `docs/memoria/apoyo/LEEME.md`
   y `memoria_docx.py`; `docs/memoria/apoyo/generar_cap5_7.py` como patrón;
   `docs/blindaje/06_PROTOCOLO_FINAL.md` y `07_RESULTADO_FINAL.md` enteros;
   `docs/memoria/00_PLAN_MAESTRO_MEMORIA.md` (§9 y §Capítulo 6); las notas
   `notas_cap5_6_*` y `notas_cap5_7_*`; y los ficheros `02_resultados\*.md` del
   paquete. Confírmame en cuatro líneas que estás al día y entra DIRECTAMENTE
   en E.2 sin esperar respuesta.

E.2 RESUMEN DEL CAPÍTULO 5 (lo que pide la biblia §6.3 para cerrar cada
   capítulo): dos o tres párrafos corridos, sin título numerado propio (va bajo
   el epígrafe «Resumen» o como cierre, según diga la biblia; comprobarlo), que
   recapitulen 5.1–5.7 (lenguaje y librerías, cliente y reproducción de trazas,
   analizador del MPD, ejecutor y configuración, controladores clásicos y MPC
   robusto canónico, controlador propio, entorno de entrenamiento) y enlacen
   con el capítulo 6 (qué se va a medir y con qué protocolo). Sin cifras nuevas;
   solo las ya dichas en el capítulo. Entregable: `borradores_docx/cap5_8_resumen_capitulo5.docx`
   generado por `apoyo/generar_cap5_resumen.py`; notas `notas/notas_cap5_resumen.md`
   (qué se recapitula de cada apartado y qué se deja fuera); §9 al día; commit y push.

E.3 ESQUEMA DEL CAPÍTULO 6 (mismo turno que E.2 o el siguiente, sin
   preguntarme): reescribir el §Capítulo 6 del plan maestro con el experimento
   final. Propuesta de partida, ajústala si el protocolo lo pide y dime qué
   cambiaste: 6.1 Diseño del experimento final (pregunta, lo que se congela,
   red: 74 ventanas eval de 160 s con bucle de 1 vuelta y filtro media < 6
   Mbit/s y mínimo > 0,2 Mbit/s, 42 grupos excluidos, semilla 606; contenido:
   vídeo visto rotado y Tears of Steel; 8 controladores con sus parámetros
   únicos; ejecución en la VM, orden sorteado, 30 segmentos y 29 evaluables,
   nivel inicial 0 sin decisión inicial); 6.2 Métricas e hipótesis
   prerregistradas (QoE lineal 4,3/1 con ecuación, paradas, secundarias;
   P1–P5 con TOST ±0,15, signo unilateral, bootstrap por bloques de ventanas
   10 000 remuestreos semilla 2026, Holm; margen = 1 s de rebuffering en 29
   segmentos); 6.3 Integridad de la ejecución y verificación (1208/1208,
   compuertas, 35 032 decisiones repetidas idénticas, fidelidad del
   simulador, latencias, huellas); 6.4 Resultados de las hipótesis P1–P5
   (tabla principal con media, IC95, IC90, ventanas +/−/=, p y p Holm;
   figura); 6.5 Resultados descriptivos por controlador (tabla de
   `agregados_por_controlador.json`: QoE, paradas, rebuffering, bitrate,
   cambios, QoE log; lo que aporta cada pieza; figuras CDF/dispersión
   rehechas); 6.6 Análisis secundario exploratorio (estratos Oboe/FCC, vídeo
   nuevo frente a visto, interacción de contenido, sintéticas aparte; sin
   claims); 6.7 Interpretación y limitaciones (el propio no tiene la QoE
   media más alta; emulación sin TCP ni tráfico competidor; ventanas
   concentradas en Oboe y FCC; un solo contenido nuevo; bitrate como proxy sin
   VMAF; desviaciones del protocolo de 07_RESULTADO §7); resumen del capítulo.
   Comprobar contra la revisión del cap 4 (`revision_cap4_contenido_20261109.md`)
   qué cuenta ya Daniel (entornos, vídeos, trazas, métrica) para no repetirlo:
   en el 6 se remite al 4 y solo se añade lo específico del experimento.

E.4 CAPÍTULO 6, APARTADO 6.1 (empezar en cuanto E.2 y E.3 estén
   commiteados, en el mismo hilo, sin esperar mi «listo» salvo para las
   descargas): protocolo completo de la sección B. Antes de redactar, una sola
   pregunta pidiendo permiso para descargar las referencias nuevas de B.6
   (con fichero, origen y tamaño aproximado), y mientras tanto seguir con la
   parte del 6.1 que no las necesita. Figura 6.1 candidata: diseño del
   experimento (ventanas × vídeos × controladores → 1208 sesiones, con lo que
   se congela), SVG propio. Tabla 6.1: los 8 controladores con su papel
   (referencias clásicas, MPC robusto canónico, propio, tres variantes de
   ablación) y la hipótesis en la que intervienen. Tabla 6.2: parámetros del
   preset `final_blindaje` (verificados en el código y en `protocolo.json`
   del paquete). Ejemplo real: una sesión del plan, descrita con sus
   identificadores legibles (sesión n del plan, ventana, vídeo), no con el id
   largo. Después, 6.2 … 6.7 y resumen, UNO POR TURNO, esperando mi «sigue».

E.5 Después del capítulo 6, por orden: capítulos 2, 3, 1 y 7, resumen y
   abstract, anexos y bibliografía. Cada uno con el mismo protocolo.

Recordatorio final: mide todo por programa, no afirmes nada que no hayas
visto en TFG Material, deja el método intacto y no me preguntes lo que no
bloquea. Empieza.

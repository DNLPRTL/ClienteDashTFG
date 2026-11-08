# Prompt de arranque del hilo de la memoria (F9) — v1, 08/11/2026

> Uso: copiar TODO lo que hay debajo de la raya y pegarlo tal cual como primer
> mensaje de un hilo NUEVO de Claude Code abierto en
> `C:\Users\danie\Documents\TFG\DashClientModular4`. Queda versionado aquí
> para que cualquier hilo sepa qué contexto se le dio.
>
> Sustituye a `03_PROMPT_REENTRADA_MEMORIA.md` (v3, agosto): aquel hilo
> arrancaba el capítulo 5 con el experimento antiguo. Este arranca tras el
> experimento final del blindaje (16/10/2026) y con la biblia de formato.

---

Retomamos la redacción de la MEMORIA de mi TFG (cliente DASH modular en
Python y controlador ABR propio: predictor neuronal de cuantiles + planificador
MPC con agregación de riesgo). Tú eres el arquitecto de la memoria y mi guía
milimétrica. Me respondes siempre en español, denso pero entendible, y sin
preguntarme nada que no bloquee.

QUÉ HA PASADO DESDE EL ÚLTIMO HILO DE REDACCIÓN

1. La parte técnica está CERRADA. La fase de blindaje (14–16/10/2026) aplicó
   las mejoras C1–C8 al código entregado, hizo una prueba corta y ejecutó UN
   único experimento final: 1208 sesiones, 74 ventanas reales de la partición
   eval × 2 vídeos × 8 controladores, más 3 ventanas sintéticas de
   diagnóstico; 41,3 h en la VM cliente. Las cinco hipótesis prerregistradas
   P1–P5 se aceptan tras Holm: QoE equivalente al MPC robusto canónico
   (diferencia −0,001, IC90 [−0,018; +0,017], margen ±0,15) con 4 veces menos
   paradas (0,041 frente a 0,162 por sesión); la red aporta frente a los
   estimadores sin red (P3, P4) y la agregación de riesgo frente a la mediana
   (P5). Las 35 032 decisiones se repitieron idénticas con el código
   congelado. Todo está en `docs/blindaje/07_RESULTADO_FINAL.md` (resultados
   y matices), `06_PROTOCOLO_FINAL.md` (diseño fijado antes de ejecutar) y
   `03_CAMBIOS_CODIGO_BLINDAJE.md` (qué cambió en el código, C1–C8).
2. Ese experimento es lo ÚNICO que va a la memoria. Ninguna cifra de
   desarrollo (junio, agosto, réplica, experimento detenido del 14/10, prueba
   corta, semáforos) se cita. Fuente única de números: el paquete
   `C:\Users\danie\Documents\TFG Material\04_evidencia_final\20261015_031741_final_blindaje\`
   (`02_resultados\contrastes_prerregistrados.md`, `resumen_resultados.md`,
   `agregados_por_controlador.json`, `sesiones.csv`; gráficas en
   `03_graficas\`).
3. Tengo una BIBLIA DE FORMATO nueva, sacada de siete TFG aprobados de mi
   escuela (tres del tutor Juan José Ramos Muñoz, 2017/2024/2025, y cuatro
   recientes de otros tutores): `docs/memoria/05_BIBLIA_FORMATO_TFG_UGR.md`.
   Las fichas de cada TFG están en `docs/memoria/apoyo/tfg_referencia/`. La
   biblia manda sobre cualquier gusto tuyo de formato.
4. Regla nueva de redacción (está en tu memoria como
   `redaccion-sin-markdown-formato-tfg`): los borradores NO llevan markdown
   (ni almohadillas, ni asteriscos, ni tablas con barras, ni acentos graves,
   ni emojis, ni viñetas por sistema). Salen como texto de memoria definitiva
   con el formato de un TFG de la UGR, listos para pegar en Word: títulos
   numerados «5.3. Título», párrafos corridos, «Figura 5.2: Pie.» y
   «Tabla 5.1: Pie.», citas numéricas [n]. El entregable de cada apartado es
   un `.docx` con los estilos de la biblia (apartado «Reglas de salida»).

PONTE AL DÍA EN ESTE ORDEN (sin narrarme cada lectura; al final, «al día» y
cuatro líneas de confirmación):

1. `CLAUDE.md` y tu memoria persistente: `redaccion-sin-markdown-formato-tfg`,
   `memoria-redaccion-estado`, `estandar-redaccion-memoria-v2`,
   `memoria-solo-experimento-final`, `memoria-tooling-y-no-rastro-ia`,
   `fase-blindaje-estado`, `bibliografia-tfg-estado`, `caveman-always`.
2. `docs/memoria/05_BIBLIA_FORMATO_TFG_UGR.md` entera.
3. `docs/blindaje/07_RESULTADO_FINAL.md`, `06_PROTOCOLO_FINAL.md` y
   `03_CAMBIOS_CODIGO_BLINDAJE.md`.
4. `docs/memoria/00_PLAN_MAESTRO_MEMORIA.md` (índice expandido; su §9 es el
   checklist) y `04_CORRESPONDENCIAS_NOMENCLATURA.md` (el plan usa nombres
   viejos de junio; se traducen SIEMPRE). `02_BIBLIOGRAFIA_DEFINITIVA.md` y
   `bibliografia.bib`: las únicas citas válidas, verificadas contra el PDF de
   `C:\Users\danie\Documents\TFG\literatura\biblioteca_final\` antes de
   entrar en la memoria.
5. El código real que se describe: `C:\Users\danie\Documents\TFG Material\01_codigo\ClienteDashTFG`
   (castellano, 103 ficheros, con `pruebas\`). El repo donde trabajas es el
   bruto (contexto, planes, bibliografía); si repo y TFG Material discrepan,
   manda TFG Material. Antes de afirmar algo del sistema, léelo en ese código
   o en el paquete final.

REGLA CERO. De cara a la memoria SOLO EXISTE `C:\Users\danie\Documents\TFG Material\`
(su `LEEME.md` está al día a 16/10). Nada se afirma sin verificarlo en código
o datos. La memoria no deja NINGÚN rastro de que se usó IA para redactarla.

MIS DOCUMENTOS (son míos: no los edites, no los reviertas; si ves una errata
mía, avísame sin tocarla):

- `G:\Otros ordenadores\Mi portátil\backup memo\Borrador Capitulo 4 Diseño.docx`
  (954 KB): capítulo 4 completo, apartados 4.1–4.8, 10 850 palabras, 12
  imágenes (F4.1–F4.6 pasadas a JPG/PNG), tablas T4.1–T4.7, pies «Figura 4.x:»
  y «Tabla 4.x:». Lo escribí yo con mis palabras a partir de tus borradores
  de agosto (`docs/memoria/borradores/cap4_*.md`).
- `G:\Otros ordenadores\Mi portátil\backup memo\hasta 5_2.docx` (43 KB):
  capítulo 5, apartados 5.1 (lenguaje y bibliotecas, con T5.1) y 5.2 (el
  cliente: sesión, viaje de los datos y reproducción de trazas, con T5.2 y
  F5.1), 4280 palabras.

Léelos con Python (`zipfile` + `word/document.xml`) o con la skill de docx.

EL ENCARGO, EN TRES PASOS Y EN ESTE ORDEN

PASO 1. Revisión SOLO DE CONTENIDO del capítulo 4. Cotejas cada afirmación
del Word contra el código final de TFG Material y contra el protocolo y
resultados del experimento final, y me devuelves la lista exacta de cambios:
apartado, frase actual entre comillas, frase propuesta, y por qué (qué cambio
C1–C8 o qué dato final lo obliga). Nada de estilo ni de formato: eso lo
adapto yo después al método nuevo. Con las figuras, máxima prudencia: están en
JPG y rehacerlas me cuesta mucho; solo marcas «cambiar» si la información que
muestran es falsa con el sistema final, y dices qué cambiaría; si la figura
sigue siendo cierta, «se mantiene». Pistas de lo que puede haber cambiado
(compruébalo, no lo des por hecho):

- 4.3 / T4.3: el paso de espera del bucle de descarga es 0,5 s por defecto
  y 0,01 s en la evaluación (pendiente desde octubre).
- 4.4 / 4.6: corrección C2 del reproductor: la parada se apunta al segmento
  que se está esperando (`indice_actual`), el vaciado final se ignora por
  estado (`_descargas_terminadas`) y ya no se anula la fila del último
  segmento. Si el texto describe la contabilidad antigua de paradas (cabeza
  de la cola, fila anulada), cambia.
- 4.5: el registro tiene ahora el MPC robusto canónico y las tres variantes
  de ablación del propio (`propio_mediana`, `propio_cuantiles_fijos`,
  `propio_cuantiles_recientes`); todos los controladores reciben
  `id_perfil_video`; el MPC lee el descriptor del vídeo al crearse; el propio
  carga el modelo al crearse (ya no en la primera decisión) y su respaldo es
  el MPC robusto canónico, que ve todas las descargas. Límite de inferencia
  50 ms, sin cambios.
- 4.7: la ventana de red del experimento final es de 160 s con bucle de
  seguridad (`politica_fin = loop`, `max_bucles = 1`), filtro de Pensieve
  sobre la propia ventana (media < 6 Mbit/s y mínimo > 0,2 Mbit/s), partición
  eval y 42 grupos de captura excluidos; cinco vídeos, con Tears of Steel como
  contenido nuevo (150 segmentos, CV de tamaños 0,28–0,31 frente a 0,05–0,19
  de los vistos). Cualquier frase sobre «empate» o resultados se quita o se
  deja neutra: los resultados van al capítulo 6.
- 4.8: compuertas del paquete (15 comprobaciones de `verificar_paquete`,
  sintéticas aparte, auditoría de inferencia solo a las variantes con red,
  0 respaldos), hipótesis prerregistradas copiadas al protocolo antes de
  ejecutar (`core/evaluacion/contrastes.py`), orden de controladores sorteado
  por escenario con semilla, asignación «visto rotado más nuevo».
- 4.1 / T4.1: módulos nuevos `core/evaluacion/contrastes.py`,
  `core/controladores/entradas_planificador.py`, `robust_mpc.py` reescrito y
  carpeta `pruebas/` (18 pruebas); fuera `entrenamiento/politicas_rollout.py`
  y `utilidades_rollout.py`.
- En ningún sitio puede quedar que el MPC clásico «optimiza la utilidad
  logarítmica» ni «horizonte 3» ni «tamaños nominales»: el MPC robusto es
  ahora el canónico (Yin 2015 § 7.1 y el código de Pensieve): horizonte 5,
  QoE lineal, tamaños reales y error medido contra la media armónica.
- Aviso de forma que sí me interesa (una línea, no es contenido): en el Word
  los títulos de nivel 2 salen como «Capítulo 4.2. …» por la numeración
  automática; en la biblia el formato es «4.2. Título».

PASO 2. Lo mismo, solo contenido, con `hasta 5_2.docx` (5.1 y 5.2). Pistas:
versiones reales (requests, numpy, matplotlib del `requirements.txt`; Python
3.8.10 y las versiones de `entorno.json` de las sesiones del paquete final;
PyTorch solo para el propio), las dependencias reales (la configuración es
JSON; comprueba si se usa PyYAML antes de dejarlo), la carpeta `pruebas/` con
`unittest`, la corrección C2, la ventana de 160 s con bucle, el paso de espera
de 0,01 s en la evaluación, y la T5.2 de verificación de trazas contra
`core/reproduccion_trazas/`.

PASO 3. Cuando yo diga «listo, vamos al 5.3», empieza la redacción desde cero
del resto de la memoria con el método nuevo, UN apartado por turno:
5.3 analizador del MPD, 5.4 ejecutor y configuración, 5.5 controladores
clásicos (con el MPC robusto canónico y el planificador compartido), 5.6
controlador propio (predictor de cuantiles con ensemble de 5 GRU y
ensanchado de la cola; planificador con agregación de riesgo que promedia los
⌈α·K⌉ peores de los K = 4 escenarios de cuantil, α = 0,75, es decir los tres
peores; salvaguardas; las tres variantes de ablación como diseño del
experimento), 5.7 entorno de entrenamiento fiel al medio, resumen del
capítulo 5; capítulo 6 según `06_PROTOCOLO_FINAL.md` y `07_RESULTADO_FINAL.md`
(diseño, métricas, P1–P5 con sus tablas, descriptivos, secundario
exploratorio, limitaciones: el propio NO tiene la QoE media más alta, la
interacción con el contenido nuevo es exploratoria, la red es emulada sin
TCP); después capítulos 2, 3, 1 y 7, resumen y abstract, anexos y
bibliografía. Antes del 5.3, una sola vez: crea la plantilla
`docs/memoria/plantilla/plantilla_memoria_ugr.docx` con los estilos que fija
la biblia y úsala para todos los entregables.

PROTOCOLO POR APARTADO (innegociable), cada turno el paquete completo:
(a) alcance: qué cuenta y qué no, para no pisar otros apartados;
(b) BORRADOR COMPLETO en español, impersonal, frases cortas, nivel de TFG de
    grado de Teleco de la ETSIIT, con el estándar v2 (problema → idea →
    mecanismo → ecuación → ejemplo real → límites; autoría por decisiones; sin
    rayas ni muletillas; recuentos verificados por programa) y el formato de
    la biblia; entregado como `.docx` en `docs/memoria/borradores_docx/` y,
    en el chat, solo el resumen de lo que trae;
(c) figuras que toquen: SVG editable hecho por ti con el contenido técnico
    exacto del entregable, verificado renderizándolo (sin solapes), más su
    PNG para Word, estilo sobrio de siempre (grises, azul #1971c2 para la
    decisión, amarillo #fff9db para lo asíncrono o el medio, rojo #c92a2a
    para alertas), pie numerado y referencia en el texto; las de datos,
    generadas por script desde el paquete final;
(d) tablas con contenido real del entregable o del paquete final;
(e) citas: solo claves del `.bib`, verificadas contra el PDF original; si hace
    falta una referencia nueva (TOST de Schuirmann 1987, Holm 1979, Efron y
    Tibshirani 1993, ficha de Tears of Steel), me pides permiso para
    descargar diciendo fichero, origen y tamaño;
(f) checklist de cierre, §9 del plan maestro al día, commit y push con rutas
    explícitas (nunca `git add .`), y notas «no van a la memoria» con las
    preguntas probables del tribunal y la fuente de cada número.
Cuando yo diga «listo, X terminado, vamos con Y», conservas mis versiones y
sigues.

PRIMER TURNO DE ESTE HILO: ponte al día con las lecturas de arriba, confirma
en cuatro líneas, y entra DIRECTAMENTE en el PASO 1 con la lista de cambios
del capítulo 4.

# Notas del 5.5 (no van a la memoria) — 09/11/2026

Entregable: `docs/memoria/borradores_docx/cap5_5_controladores_clasicos.docx` (1747 palabras de cuerpo,
5 páginas, 4 subapartados, Figura 5.3, Tablas 5.7 y 5.8, ecuaciones 5.4 a 5.6, 6 citas). Generado por
`docs/memoria/apoyo/generar_cap5_5.py`, que también produce la figura (matplotlib, SVG y PNG).

## Reproducción que hace el script (regla del ejemplo real)

- Regla fijada antes de mirar el resultado: primera sesión del MPC robusto en el orden del plan cuya
  ventana es de Oboe (variabilidad: la corrección robusta tiene algo que corregir) y cuyo vídeo es
  visto; dentro de ella, la primera decisión con historial de 5 descargas y 5 errores medidos.
  Primera regla probada y descartada (y por qué): «primera sesión del MPC robusto y primera decisión
  con cambio de nivel» caía en una ventana de la FCC de throughput casi constante (5,06 Mbit/s), con
  dos muestras idénticas y error ≈ 1e-15: no ilustraba nada. Se cambió la regla ANTES de ver la
  decisión de la sesión de Oboe. Decirlo así si el tribunal pregunta.
- Sesión elegida: `s00056_mpc_robusto_blender_10min_60fps_4s_real_004_33c3424595_r1` (sesión 56 del
  plan, ventana real 004 de Oboe, Blender 60 fps). Las 29 decisiones reproducidas con el código del
  entregable a partir de `telemetria_segmentos.csv` coinciden con las de la VM (nivel y tasa).
- Decisión ilustrada: segmento 6, buffer 15,14 s, nivel anterior 0. Historial 0,48, 0,80, 1,24,
  0,98, 0,88 Mbit/s; media armónica 0,791 Mbit/s; errores 15, 45, 59, 38, 25 %; máximo 58,5 %;
  predicción robusta 0,499 Mbit/s; mejor secuencia 0 1 1 1 1 (puntuación 2,85) → nivel 0 (300
  kbit/s). Con la media armónica sin rebajar: 2 2 2 2 2 (puntuación 5,10). Fuente: salida del script.

## Fuente de cada número

| Dato | Fuente |
|---|---|
| Parámetros por defecto (0,85, α 0,5, 2 s; 5 s y 10 s; V 5, γ 0,2; horizonte 5, ventana 5, 4,3 y 1) | constantes de `basado_en_tasa.py`, `bba.py`, `bola.py`, `mpc.py`, `robust_mpc.py` |
| «los cuatro corrieron con sus parámetros por defecto; solo reciben id_perfil_video» | `configs_cliente/*.yaml` del paquete (parámetros = {id_perfil_video}) |
| 6⁵ = 7776 secuencias | `planificador._secuencias` con 6 niveles y horizonte 5 (mascara completa) |
| 400 estados, ≥ 390 acciones iguales | `pruebas/test_mpc_canonico.py` |
| «el MPC básico existe en el registro pero no corre» | `registro.py` (clave `mpc`) y `config/evaluacion.local.json` (8 controladores sin `mpc`) |
| «respaldo del propio, creado para el mismo vídeo, recibe toda la realimentación» | `controlador_propio.py` |

## Citas verificadas contra el PDF (páginas del fichero)

- `liu2011rateAdaptation`: p. 1 (step-wise increase / aggressive decrease; sin RTT ni pérdidas),
  p. 2-3 (segment fetch time frente a media segment duration).
- `huang2014bba`: p. 4 (reservoir, cushion), p. 5 (BBA-0, Fig. 5), p. 4 supuesto «Videos are
  encoded at a constant bit-rate (CBR)»: munición para el argumento «reactivo frente al VBR».
- `spiteri2020bola`: p. 5 (estructura de la solución de (11), no-download, υm = ln(Sm/S1), ejemplo
  γ = 5/p y V = 0,93), p. 6 (BOLA-BASIC «directly from (11)»; «any utility function satisfying (1)»).
- `yin2015mpc`: p. 7 (Teorema 1), p. 9 (RB con media armónica de 5; BB con r = 5 s y c = 10 s;
  FastMPC h = 5; q identidad; λ = 1, µ = 3000 kbps), p. 10 (RobustMPC: Ĉ/(1 + err), err máximo
  error porcentual absoluto de los 5 últimos chunks).
- `mao2017pensieve`: p. 3 (robustMPC con horizonte 5 y estimación conservadora), p. 8 (Tabla 1:
  QoE_lin con q(R) = R y penalización 4,3; MPC «over a horizon of 5 future chunks»; robustMPC
  normaliza por los errores). El uso de los tamaños reales de cada segmento está en el código de
  referencia publicado con Pensieve (`test/mpc.py`, `get_chunk_size`), no en el artículo: por eso la
  Tabla 5.8 dice «código de referencia» en esas filas. Si el tribunal pide la fuente exacta: el
  repositorio público de Pensieve (hongzimao/pensieve), fichero `test/mpc.py`.
- `spiteri2019dashjs`: p. 1 y 7 (BOLA-E con placeholder e insufficient buffer rule; DYNAMIC;
  FAST SWITCHING; «part of the official DASH reference player dash.js»).

## Preguntas probables del tribunal

1. **¿Por qué el MPC robusto usa tamaños reales y BOLA no?** Fidelidad a la referencia de cada uno:
   el código de Pensieve planifica con el tamaño real de cada chunk; el artículo de BOLA usa S_m
   nominal. Cambiar BOLA sería una variante propia. Además, con tamaños reales el MPC es el
   comparador más exigente para el propio: solo cambia la predicción.
2. **¿Por qué no BOLA-E o DYNAMIC (los de dash.js)?** Son mejoras de producción (arranque, buffers
   pequeños, live); el experimento aísla el mecanismo de BOLA y no evalúa arranque (4.6).
3. **¿BOLA no calibrado perjudica la comparación?** Se declara. Con V = 5 y γp = 0,8 el buffer
   objetivo implícito V(υ_M + γp) ≈ 5·(2,66 + 0,8) ≈ 17 segmentos ≈ 69 s supera el tope de 60 s:
   BOLA tiende a llenar y a elegir alto; plausible explicación de su rebuffering en 6 (hipótesis).
4. **¿El MPC robusto es el de Yin o el de Pensieve?** La regla es la de Yin (sec. RobustMPC de la
   evaluación, Teorema 1); los valores (horizonte 5, QoE lineal con 4,3, tamaños reales, sin factor
   de arranque) son los del código de referencia de Pensieve, que es lo que la literatura posterior
   compara. Yin evaluó con q identidad y µ = 3 s por segundo de rebuffering; Pensieve con 4,3.
5. **¿Determinismo?** Ningún clásico usa aleatoriedad; la auditoría reproduce las 35 032 decisiones
   del paquete (07_RESULTADO), y este script reproduce las 29 de una sesión como ejemplo.
6. **¿Por qué el error se mide contra la media armónica y no contra la predicción rebajada?** Es lo
   que hace el código de referencia; medirlo contra la rebajada realimenta la rebaja (el error
   crece porque la predicción ya era baja) y hunde la predicción. Se corrigió en el blindaje (C3).

## Detalles que el texto no cuenta

- `basado_en_tasa` lee primero `bwe` del contrato (tamaño/tiempo que calcula el reproductor) y solo
  si falta recalcula el cociente; es la misma cifra.
- BBA redondea hacia abajo `floor(x·(n−1))` con n = 6 niveles; con buffer inválido pide el mínimo.
- BOLA: respaldo al mínimo si buffer ≤ una duración de segmento (`buffer_bajo_respaldo_s = p`).
- El MPC básico (`mpc`) comparte código con el robusto: la clase robusta solo redefine la
  predicción y el registro del error.
- La media armónica usa 300 kbit/s por defecto si el historial está vacío (nunca ocurre en sesión:
  la descarga de calentamiento entra antes de la primera decisión).
- El planificador acorta el horizonte al final del vídeo (`restantes`), como Pensieve.
- El CVaR con un solo cuantil y α = 1 es la media de un solo valor: el MPC robusto no usa CVaR
  aunque pase por la misma función.

## Qué se puede recortar

El párrafo de principios comunes (a la mitad) y la lista de mejoras de dash.js. Mantener la
Tabla 5.8, la ecuación (5.6) y el ejemplo real: son la defensa del comparador.

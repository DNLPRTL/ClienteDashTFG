# Prompt para abrir el hilo de la fase de blindaje

Uso: copiar todo lo que hay debajo de la raya y pegarlo como primer mensaje del
hilo nuevo, abierto en la carpeta del proyecto `DashClientModular4`. Se versiona
aquí para saber qué contexto se le dio.

---

Retomamos mi TFG (cliente DASH modular en Python y controlador ABR propio:
predictor de cuantiles con un ensemble de GRU y planificador MPC con CVaR).
Empezamos la FASE DE BLINDAJE.

Antes de responder, lee entero `docs/blindaje/00_HANDOFF_FASE_BLINDAJE.md` y tu
memoria persistente (sobre todo `fase-blindaje-estado`,
`memoria-solo-experimento-final` y `workflow-claude-daniel`). Lo que vayas a
usar, compruébalo contra el código real de
`C:\Users\danie\Documents\TFG Material\01_codigo\ClienteDashTFG` (es lo que se
entrega y lo que corre en la VM) y contra los datos. No me narres cada lectura.

Qué quiero:

- He detenido el experimento final que estaba en marcha. Quiero aplicar TODAS
  las mejoras que eliminen o acoten las deficiencias de abajo, sin rebajarlas.
  La emulación de red no se toca. Todo lo demás se puede solucionar, explicar o
  detallar, sin límite. Después, lanzar UN ÚNICO experimento final: es lo único
  que irá a la memoria.
- Antes de lanzarlo quiero saber si el resultado puede ser bueno, con pruebas
  que cuesten minutos u horas (como hacíamos con `diagnostico` y `rapido`), sin
  gastar ventanas del experimento final.
- Rigor académico: la bibliografía del proyecto (`bibliografia.bib` y los PDF
  de `biblioteca_final`), papers recientes y Google Scholar. Si hay que
  descargar algo, pídeme permiso indicando fichero, origen y tamaño.
- El resultado más brillante posible, aprovechando el tiempo al máximo.

Mis deficiencias, sin rebajarlas:

1. **No está aislado qué aporta la red.** Mi controlador se diferencia del MPC
   robusto en cinco cosas a la vez: predictor neuronal, CVaR, tamaños reales,
   horizonte 5 frente a 3 y objetivo lineal frente a logarítmico. Si sale
   mejor, no se puede decir cuánto se debe a la IA. La pregunta más peligrosa
   del tribunal: "¿y si en vez de la red usas cuantiles calculados de las
   últimas descargas?". Hoy la respuesta honesta es "no está medido". La Tabla
   5.7 muestra que el criterio de riesgo pesa mucho más en las decisiones
   (17–24 %) que el ensanchado o los tamaños (3–5 %).
2. **La comparación no está del todo igualada en el objetivo.** Mi planificador
   optimiza la misma QoE lineal con la que se evalúa; los MPC clásicos
   optimizan una logarítmica. Está declarado, pero no está claro en qué sentido
   pesa.
3. **La calibración en validación no es perfecta.** Se desvía hasta 6,7 puntos
   y la mediana está algo sesgada a la baja. No se recalibró, y el ensanchado
   hace la cola baja deliberadamente prudente.
4. **El banco de pruebas es pequeño.**
   - Son 12 ventanas reales y 48 escenarios pareados, con sesiones de 2 minutos.
   - En muchas ventanas fáciles todos eligen el nivel máximo y empatan.
   - Con ese tamaño, una mejora pequeña frente al MPC robusto es casi imposible
     de demostrar estadísticamente.
5. **Es emulación, no red real.** No hay efectos de TCP ni tráfico competidor.
   Es justo el tipo de hueco que Puffer y CausalSim señalan.
6. **El contenido no es nuevo.** Los cuatro vídeos de la evaluación también
   estaban en el entrenamiento. La generalización a contenido nuevo es una
   propiedad del diseño, no un resultado medido.

Reglas:

- En la memoria va solo el experimento final; nada de dos evaluaciones ni de
  estudios aparte.
- Ahora NO trabajamos la memoria. Tengo el capítulo 4 y el 5 hasta el 5.3
  escritos en Word: no los toques. Cuando acabe lo técnico te los paso y me
  dices qué cambia (texto y figuras). Desde el 5.4 rehaces tú los borradores
  enteros con el resultado final.
- Tú desarrollas y verificas en Windows; yo ejecuto en las VM o en WSL y te
  pego las salidas. Comandos cortos, scripts versionados y commits con rutas
  explícitas.

En tu primera respuesta dame el plan de pasos de esta fase, directo (§9 del
traspaso):

- qué haces tú y qué hago yo, en qué orden y cuánto dura cada cosa, con los
  comandos que me tocan;
- las decisiones que necesitas de mí, con tu recomendación primero;
- los semáforos de la prueba previa: adelante, ajustar en validación o
  replantear;
- el diseño del experimento final, con las horas de VM;
- los riesgos, con honestidad.

No me preguntes nada que no bloquee.

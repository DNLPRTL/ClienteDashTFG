# 03 - Puffer / Fugu

PDF: `2020_yan_puffer_learning_in_situ_nsdi.pdf`

Titulo: Learning in situ: a randomized experiment in video streaming.

## Que hace

Puffer es una plataforma real de streaming que permite probar algoritmos ABR en
usuarios reales mediante experimentos aleatorizados. Fugu usa aprendizaje para
predecir tiempo de transmision y tomar decisiones ABR.

## Tecnica

- Evaluacion real en produccion, no solo simulacion.
- Aleatorizacion ciega entre algoritmos.
- Fugu aprende un Transmission Time Predictor.
- La decision ABR se apoya en prediccion de tiempo/descarga, SSIM/calidad y
  estado del player.

## Evaluacion del paper

Reporta anos de streaming acumulado, miles de usuarios y comparacion in situ.
El foco es que los resultados de simulador pueden diferir de produccion.

## Relevancia para el proyecto

Muy importante metodologicamente:

- Phase 6 debe tratar resultados como evidencia formal solo bajo gates;
- los controllers nuevos deben auditar decision por chunk, no solo media final;
- predictor + decision segura es una ruta valida para un controller propio.

Limitacion:

- no tenemos plataforma de usuarios reales;
- Puffer/Fugu dependen de SSIM y datos de servicio que no forman parte de
  nuestro runtime.

## Decision

Usar como justificacion de evaluacion rigurosa y como inspiracion para
`neural_abr_predictive_mpc_v1`, no como implementacion directa.

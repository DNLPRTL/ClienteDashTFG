# 28 - KPCA / GWO / LSSVM bit rate selection

PDF: `1-s2.0-S1687850724002206-main.pdf`

Titulo: Bit rate selection technology of image processing based on artificial
intelligence in MPEG-DASH adaptive streaming media.

## Que hace

Propone un metodo hibrido de IA para seleccion de bitrate usando reduccion de
dimension y optimizacion bio-inspirada.

## Tecnica

- Kernel PCA para transformar/reducir features.
- Grey Wolf Optimization para optimizar parametros.
- Least Squares SVM / BP-style predictor segun la descripcion del PDF.
- Enfoque mas de regresion/clasificacion que de control ABR secuencial.

## Evaluacion del paper

Reporta accuracy/error de seleccion o prediccion. El foco esta menos alineado
con QoE ABR por chunks y mas con tecnologia de seleccion de bitrate.

## Relevancia para el proyecto

Baja para v1:

- no modela buffer dynamics de forma central;
- no ataca rebuffer ni incertidumbre secuencial;
- dificil de defender frente a papers ABR IA mas especificos.

## Decision

No usar como base de controller. Puede citarse como ejemplo de AI no-RL, pero no
aporta la robustez que buscamos.

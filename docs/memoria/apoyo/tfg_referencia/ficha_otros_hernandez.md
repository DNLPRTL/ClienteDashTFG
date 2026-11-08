# Ficha de formato y estilo — TFG de Pablo Hernández Manrique (ETSIIT-UGR, junio 2024)

Fuente analizada: `docs/memoria/DE OTROS TUTORES PERO RECIENTES DE MI FACULTAD/TFG_PabloHernandezManrique.pdf`.
Método: extracción íntegra con `pdftotext` (flujo y `-layout`), lectura completa del texto
(110 páginas detectadas, 28 555 palabras) y comprobación página a página con el layout.
Las páginas se citan como **páginas del PDF** entre paréntesis. La numeración impresa en
el documento va una unidad por detrás a partir de la dedicatoria (PDF 20 = impresa 19).

Nota técnica: las fuentes del PDF no exportan los acentos (pdftotext los devuelve como glifo
suelto, p. ej. `Cap?itulo`), así que en todas las citas literales de esta ficha los acentos
se han **restituido**; el resto de la grafía (mayúsculas, puntuación, erratas) se respeta tal
cual aparece. Lo que no se puede saber solo desde el texto (negritas, cursivas, color,
tipografía exacta) se marca como «inferencia» o como «no determinable desde el texto».

---

## A. Identificación

- **Título completo:** «Implementación y evaluación de robustez de una técnica de watermarking para detección de deepfakes de voz» (p. 1, 3, 5, 10). Título en inglés en el abstract: «Implementation and robustness evaluation of a watermarking technique for voice deepfake detection» (p. 7).
- **Autor:** Pablo Hernández Manrique (p. 1).
- **Tutores («Directores»):** Antonio Miguel Peinado Herreros y Ángel Manuel Gómez García (p. 1, 3, 10). En el informe constan como «Profesor del Área de Teoría de la Señal» (p. 10).
- **Departamento:** «Departamento de Teoría de la Señal, Telemática y Comunicaciones de la Universidad de Granada» (p. 10). No figura en la portada, solo en el informe de los directores.
- **Titulación (literal de portada):** «TRABAJO FIN DE GRADO» / «INGENIERÍA DE TECNOLOGÍAS DE TELECOMUNICACIÓN» (p. 1). Es por tanto el Grado en Ingeniería de Tecnologías de Telecomunicación: comprobado.
- **Centro (literal):** «Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación» (p. 1). Debajo aparece una raya «--» que probablemente es un separador o el hueco de un logo (inferencia; el layout muestra solo «--»).
- **Universidad:** «Universidad de Granada» aparece escrito solo en el informe de los directores (p. 10). En la portada no se escribe el nombre de la universidad (presumiblemente va en el escudo, no extraíble).
- **Fecha (literal):** «Granada, Junio de 2024» (p. 1). El informe está fechado «en Granada a 24 de Junio de 2024 .» (p. 10; obsérvese el espacio antes del punto).
- **Número de páginas:** 110 páginas según la extracción (el encargo indicaba 111; la diferencia puede ser una página final en blanco no detectada). Páginas totalmente vacías: 4, 8, 9, 25, 35, 53, 101, 109. Página 2 contiene solo el carácter «3» (probablemente escudo/logo no extraíble; no determinable).
- **Herramienta de maquetación inferida:** **LaTeX** (certeza alta). Evidencias:
  1. Explícita: «La memoria fue escrita en la plataforma Overleaf, también gratuita y sin límite de uso.» (p. 104).
  2. Cabeceras de capítulo en dos líneas «Capítulo 1» / «Introducción» (p. 20) y títulos de índices «Índice general», «Índice de figuras», «Índice de cuadros» (p. 14, 16, 18): nombres por defecto de `babel` español. Las tablas se llaman «Cuadro» (p. 33, 41…), que es el `\tablename` por defecto de babel-spanish.
  3. Ecuaciones numeradas a la derecha «(2.1)», «(3.14)» (p. 29, 49), funciones por partes con llave (p. 44).
  4. Bibliografía con estilo BibTeX `plain/unsrt` en inglés («and», «pages 234–241», «In Proceedings…», «Master's thesis», «PhD thesis», «B.S. thesis») (p. 106–108).
  5. Acentos como glifo separado y sin ligaduras ni caracteres precompuestos en la extracción: huella de codificación de fuente OT1 (sin `fontenc T1`).
  6. Espacio fino antes del símbolo de porcentaje («30 %», «70 %») en todo el texto: comportamiento de babel-spanish.
  7. Cabeceras corrientes tipo clase `book`: página par = número + «1.2. Motivación» (p. 21); página impar = título del capítulo + número (p. 22). Los capítulos abren siempre en página impar y dejan versos en blanco (p. 25, 35, 53, 101).
  8. Diagrama de Gantt con etiquetas «100 % complete», «0 % complete», «TODAY» (p. 105): salida por defecto del paquete `pgfgantt`.
  9. Subfiguras «(a)…», «(b)…» con pie común (p. 27, 38, 92–94): paquete `subcaption`/`subfigure`.
  10. El orden de la bibliografía coincide con el orden de primera cita **incluyendo las citas dentro de los pies del índice de figuras** ([1]–[4] antes que [5], que es la primera cita del cuerpo, p. 23): típico de `unsrt`.
  11. Artefactos de corrección de cursiva: «(salida del Embedder )», «BCE para el Detector )», «Embedding :» (p. 42, 45, 28): espacio antes del paréntesis/dos puntos, propio de `\textit{...}`.

## B. Estructura completa en orden (con páginas del PDF)

| # | Bloque | Páginas | Observaciones |
|---|---|---|---|
| 1 | Portada | 1 | «TRABAJO FIN DE GRADO», titulación, título, «Autor», «Directores», Escuela, «Granada, Junio de 2024». |
| 2 | Página casi vacía | 2 | Solo «3» extraíble; probablemente escudo/imagen. No determinable. |
| 3 | Segunda portada (portadilla) | 3 | Solo título, «Autor» + nombre, «Directores» + nombres. Sin fecha ni escuela. |
| 4 | Blanco | 4 | |
| 5 | Resumen y palabras clave (español) | 5–6 | Orden: título, autor, «Palabras clave:», encabezado «Resumen», tres párrafos. |
| 6 | Abstract y keywords (inglés) | 7 | Orden: «Project Title:», autor, «Keywords:», encabezado «Abstract», tres párrafos. |
| 7 | Blancos | 8–9 | |
| 8 | Informe/autorización de los directores | 10 | Fórmula oficial (copiada abajo). |
| 9 | Dedicatoria | 11 | Cuatro líneas alineadas a la derecha. |
| 10 | Agradecimientos | 12–13 | Dos páginas, en primera persona del singular; cierran con dos citas de canciones (Drexler, Sabina). |
| 11 | Índice general | 14–15 | |
| 12 | Índice de figuras | 16–17 | |
| 13 | Índice de cuadros | 18–19 | |
| 14 | Capítulo 1. Introducción | 20–24 (25 blanco) | |
| 15 | Capítulo 2. Watermarking. Antecendentes, dominios y métodos | 26–34 (35 blanco) | |
| 16 | Capítulo 3. Arquitectura de las Redes Neuronales… | 36–52 (53 blanco) | |
| 17 | Capítulo 4. Ataques implementados en el sistema. | 54–59 | |
| 18 | Capítulo 5. Marco y Resultados Experimentales | 60–95 | p. 92–94 son láminas de figuras a página completa; p. 95 solo cabecera (casi vacía). |
| 19 | Capítulo 6. Conclusiones y Trabajo Futuro | 96–100 (101 blanco) | |
| 20 | Capítulo 7. Presupuesto y Cronograma de Trabajo | 102–105 | |
| 21 | Bibliografía | 106–108 (109 blanco) | 28 referencias numéricas. |
| 22 | Acrónimos | 110 | Lista de 20 siglas, al final del documento. |

**Bloques que FALTAN:** declaración de originalidad del alumno; autorización del alumno a la biblioteca (depósito/difusión); mención a la licencia; glosario de términos (solo hay lista de acrónimos, y va al final, no al principio); anexos; índice de ecuaciones; página de tribunal; DNI; firmas visibles (solo nombres).

### B.1 Texto literal del informe/autorización de los directores (p. 10)

> D. Antonio Miguel Peinado Herreros, Profesor del Área de Teoría de la Señal del Departamento de Teoría de la Señal, Telemática y Comunicaciones de la Universidad de Granada.
>
> D. Ángel Manuel Gómez García, Profesor del Área de Teoría de la Señal del Departamento Teoría de la Señal, Telemática y Comunicaciones de la Universidad de Granada.
>
> Informan:
>
> Que el presente trabajo, titulado *Implementación y evaluación de robustez de una técnica de watermarking para detección de deepfakes de voz*, ha sido realizado bajo su supervisión por Pablo Hernández Manrique, y autorizamos la defensa de dicho trabajo ante el tribunal que corresponda.
>
> Y para que conste, expiden y firman el presente informe en Granada a 24 de Junio de 2024 .
>
> Los directores:
>
> Antonio Miguel Peinado Herreros          Ángel Manuel Gómez García

(La cursiva del título es inferencia: el layout lo muestra partido en líneas más cortas, como un bloque destacado; el texto no permite confirmar el estilo. En el segundo párrafo falta «de» antes de «Teoría», tal cual en el original.)

### B.2 Dedicatoria literal (p. 11)

> A mis padres y hermanas, por acompañarme en el camino.
> A mis amigos, por la comprensión y la paciencia que tienen conmigo.
> A mi abuela Antonia, por enseñarme lo que es el valor y la valentía.
> ... y a Elena.
> Muchas gracias a todos por limarme las aristas.

### B.3 Resumen y palabras clave literales (p. 5–6)

> **Palabras clave:** Marca de agua, Deepfake, Derechos de Autor, Propiedad Intelectual, Imperceptibilidad, Robustez, SNR, PESQ, BER, STOI, Accuracy, Error Medio Absoluto, Entropía Binaria Cruzada.
>
> **Resumen**
>
> En esta era, los datos, la autenticidad y la protección de los mismos han adquirido un protagonismo y una gran relevancia como consecuencia de la aparición de técnicas avanzadas de manipulación y edición de datos a través del uso inmoral de las tecnologías de inteligencia artifical emergentes, como los deepfakes. Estas técnicas, que son capaces de crear contenido hiperrealista y de mucha similitud con el original a partir del cual se generó, han puesto contra la espada y la pared a nuestro juicio para diferenciar entre lo verdadero y lo generado mediante inteligencia artificial.
>
> Con este trabajo pretendemos hacer frente a esta situación haciendo uso de técnicas de marcado de agua basado en redes neuronales y aprendizaje profundo. Las marcas de agua nos permiten firmar el contenido de tal forma que podamos conocer la legitimidad de su procedencia en el receptor. Con este enfoque somos capaces de determinar qué contenido ha sido generado de manera fraudulenta. Se presentarán dos redes neuronales, cada una de ellas con una tarea conceptualmente opuesta, denominadas Embedder y Detector. El Embedder, basado en una arquitectura U-Net, se encargará de realizar una incrustación imperceptible de la marca de agua minimizando las diferencias entre las señales de voz originales y las señales de voz que contienen la marca de agua. El Detector, por su parte, trata de detectar la marca de agua sin errores. Dado que la tarea de cada red neuronal es opuesta, se propone una optimización conjunta para alcanzar el equilibrio entre los requisitos de cada una de ellas. Por último, con el fin de garantizar una reconstrucción de la señal de voz por parte del Embedder sin poner en compromiso la detección de la marca de agua por parte del Detector, se añade una función de coste complementaria al Embedder basada en el PESQ de las señales originales y con marca de agua.
>
> Los resultados del estudio indican que el enfoque propuesto es efectivo, ofreciendo un nuevo mecanismo para proteger la integridad de las comunicaciones multimedia y combatir la propagación de informaciones falsas mediante deepfakes. Este trabajo contribuye a los esfuerzos de garantizar la confiabilidad y seguridad de la información en la era digital, abordando directamente los desafíos emergentes asociados con las tecnologías de inteligencia artificial.

(«artifical» es errata del original. El resumen ocupa 417 palabras y desborda a la p. 6.)

### B.4 Abstract y keywords literales (p. 7)

> **Project Title:** Implementation and robustness evaluation of a watermarking technique for voice deepfake detection
>
> Pablo Hernández Manrique
>
> **Keywords:** Watermark, Deepfake, Copyright, Intellectual Property, Imperceptibility, Robustness, SNR, PESQ, BER, STOI, Accuracy, Mean Absolute Error, Binary Cross Entropy.
>
> **Abstract**
>
> In this era, data, authenticity, and their protection have taken on disproportionate prominence and critical relevance due to the emergence of advanced data manipulation and editing techniques through the unethical use of emerging artificial intelligence technologies, such as deepfakes. These techniques, capable of creating hyper-realistic content that closely resembles the original from which it was generated, have cornered our judgment in discerning between what is true and what is generated by artificial intelligence.
>
> With this work, we aim to address this situation by using watermarking techniques based on neural networks and deep learning. Watermarking allows us to sign the content in such a way that we can know the legitimacy of its provenance at the recipient. With this approach we are able to determine which content has been fraudulently generated.Two neural networks will be presented, each with a conceptually opposite task, named Embedder and Detector. The Embedder, based on a U-Net architecture, will handle the imperceptible embedding of the watermark, minimizing the differences between the original voice signals and the signals that contain the watermark. The Detector, on the other hand, attempts to detect the watermark without errors. Since the task of each neural network is opposite, a joint optimization is proposed to balance the requirements of each. Finally, to ensure a reconstruction of the voice signal by the Embedder without compromising the watermark detection by the Detector, a complementary cost function based on the PESQ of the original and watermarked signals is added to the Embedder.
>
> The results of the study indicate that the proposed approach is effective, offering a new mechanism to protect the integrity of multimedia communications and combat the spread of false information through deepfakes. This work contributes to efforts to ensure the reliability and security of information in the digital age, directly addressing the emerging challenges associated with artificial intelligence technologies.

(«generated.Two» sin espacio es errata del original. 343 palabras.)

## C. Índice general copiado literalmente (p. 14–15)

Los números son los impresos en el índice (página impresa = PDF − 1). Los puntos de relleno se abrevian con «…».

```
Índice general

1. Introducción                                                        19
   1.1. Descripción del problema …………………………………………………………… 19
   1.2. Motivación …………………………………………………………………………… 20
   1.3. Objetivos de este trabajo …………………………………………………………… 21
   1.4. Delimitaciones ……………………………………………………………………… 22
   1.5. Organización de la memoria ………………………………………………………… 22

2. Watermarking. Antecendentes, dominios y métodos                     25
   2.1. Antecedentes ……………………………………………………………………… 25
   2.2. Watermarking mediante Redes Neuronales ………………………………………… 27
        2.2.1. STFT: Short Time Fourier Transform ………………………………… 29
   2.3. Elección del Dominio ……………………………………………………………… 31
   2.4. Tipos de ataques …………………………………………………………………… 31

3. Arquitectura de las Redes Neuronales. Implementación del
   Sistema de Watermarking basado en U-Net.                           35
   3.1. Redes neuronales propuestas ……………………………………………………… 35
   3.2. Arquitectura del Embedder ………………………………………………………… 36
        3.2.1. Modelo propuesto para el Embedder …………………………………… 38
   3.3. Arquitectura del Detector ………………………………………………………… 40
        3.3.1. Modelo propuesto para el Detector …………………………………… 41
   3.4. Entrenamiento de los modelos ……………………………………………………… 42
   3.5. Función de pérdida basada en el PESQ …………………………………………… 44
        3.5.1. Transformación al Dominio Perceptual ……………………………… 45
        3.5.2. Cálculo de las Perturbaciones Simétrica y Asimétrica ……… 46
        3.5.3. Preprocesado Espectral y Ecualización ……………………………… 47
        3.5.4. Implementación de la Función de Pérdida Basada en
               el PESQ al Entrenamiento del Sistema ……………………………… 48

4. Ataques implementados en el sistema.                                53
   4.1. Ataque de filtrado paso-baja ……………………………………………………… 54
   4.2. Ataque de adición de ruido aleatorio ……………………………………………… 56
   4.3. Ataque de supresión aleatoria de muestras ……………………………………… 57

5. Marco y Resultados Experimentales                                   59
   5.1. Dataset ……………………………………………………………………………… 59
   5.2. Métricas de Evaluación …………………………………………………………… 61
   5.3. Rendimiento del sistema en la fase de entrenamiento ………………………… 62
        5.3.1. Fase de Entrenamiento del Sistema Original ………………………… 62
        5.3.2. Fase de Entrenamieto del Sistema Propio con Ponde-
               ración Tardía ……………………………………………………………… 65
        5.3.3. Fase de Entrenamiento del Sistema Propio con Pon-
               deración Temprana ……………………………………………………… 68
   5.4. Rendimiento del sistema en la fase de validación …………………………… 70
        5.4.1. Fase de Validación del Sistema Original …………………………… 71
        5.4.2. Fase de Validación del Sistema Propio con Pondera-
               ción Tardía ……………………………………………………………… 73
        5.4.3. Fase de Validación del Sistema Propio con Pondera-
               ción Temprana …………………………………………………………… 76
   5.5. Rendimiento del sistema en la fase de Evaluación …………………………… 79
        5.5.1. Fase de Evaluación del Sistema Original …………………………… 79
        5.5.2. Fase de Evaluación del Sistema Propio con Pondera-
               ción Tardía ……………………………………………………………… 82
        5.5.3. Fase de Evaluación del Sistema Propio con Pondera-
               ción Temprana …………………………………………………………… 85
        5.5.4. Análisis General de los Resultados obtenidos en la Fa-
               se de Evaluación ……………………………………………………… 87

6. Conclusiones y Trabajo Futuro                                       95
   6.1. Conclusión ………………………………………………………………………… 95
   6.2. Trabajo Futuro …………………………………………………………………… 98

7. Presupuesto y Cronograma de Trabajo                                101
   7.1. Presupuesto del Trabajo …………………………………………………………… 101
        7.1.1. Costes de Recursos Humanos …………………………………………… 101
        7.1.2. Coste del Material ……………………………………………………… 103
   7.2. Cronograma de Trabajo …………………………………………………………… 103

Bibliografía                                                          107

Lista de Acrónimos                                                    109
```

Observaciones: el índice conserva las erratas de los títulos («Antecendentes», «Entrenamieto»); los capítulos 3 y 4 llevan punto final en el título y los demás no; «Bibliografía 107» no cuadra con la página impresa real (105, PDF 106): el índice está desfasado dos páginas en esa entrada. El índice de figuras (p. 16–17) y el de cuadros (p. 18–19) repiten los pies completos, incluidas las citas «[1]», «[2]» dentro del pie.

## D. Títulos y numeración

- **Capítulos:** «Capítulo N» en una línea y el título en la(s) línea(s) siguiente(s), sin punto tras el número (p. 20: «Capítulo 1» / «Introducción»). Los títulos largos se parten en hasta cuatro líneas (p. 36: «Arquitectura de las Redes / Neuronales. Implementación / del Sistema de Watermarking / basado en U-Net.»). Mayúscula inicial en casi todas las palabras importantes de algunos títulos («Marco y Resultados Experimentales», «Conclusiones y Trabajo Futuro») y minúscula en otros («Tipos de ataques», «Ataque de filtrado paso-baja»): capitalización inconsistente.
- **Nivel 2:** «1.1. Descripción del problema» — número con punto final tras el último dígito y título a continuación (p. 20, 21, 22…).
- **Nivel 3:** «2.2.1. STFT: Short Time Fourier Transform» (p. 30), «3.5.4. Implementación de la Función de Pérdida Basada en el PESQ al Entrenamiento del Sistema» (p. 49). Mismo formato con punto tras el número.
- **Profundidad máxima:** 3 niveles numerados (x.y.z). No hay x.y.z.w.
- **Epígrafes sin numerar:** sí, de dos tipos. (a) Mini-encabezados que introducen cada tabla del capítulo 5: «Resultados de evaluación para la SNR», «Resultados de evaluación para la SDR», …, y en 5.5.3 «Resultados de test para la SNR» (p. 80–87; nótese la inconsistencia evaluación/test). (b) Sub-epígrafes del análisis general: «Comparativa de los modelos con 0 % de Ataques», «… con 10 % …», «… con 20 % …», «… con 30 % …» (p. 88–90). Inferencia: son `\paragraph` o `\subsubsection*` (aparecen en línea propia, sin numeración y sin entrada en el índice).
- **Párrafo introductorio al abrir capítulo:** los capítulos 1, 2, 3 y 5 **no** lo tienen: tras el título va directamente «1.1.», «2.1.», «3.1.», «5.1.» (p. 20, 26, 36, 60). Los capítulos 4, 6 y 7 **sí** abren con uno o varios párrafos sin numerar antes del primer epígrafe. Dos casos literales:
  - Capítulo 4 (p. 54): «En este capítulo nos centraremos en una de las facetas fundamentales de los sistemas de watermarking: la robustez. Nuestro sistema de watermarking no solo sirve para incrustar el mensaje en la señal portadora con propósitos de autenticación y protección de los derechos de autor del contenido multimedia, sino que debe de ser capaz de resistir y recuperarse de ataques malitencionados que tienen como propósito poner en entredicho el funcionamiento de nuestro sistema y eliminar la marca de agua. La integridad del sistema de watermarking se evalúa a través de la robustez del mismo ante estos ataques. Por este motivo, el entrenamiento de las redes neuronales incluyendo estos ataques es primordial para garantizar la solidez del sistema propuesto [1].»
  - Capítulo 7 (p. 102): «En este capítulo abordaremos dos aspectos fundamentales para la planificación y desarrollo exitoso del trabajo expuesto en la presente memoria: el presupuesto y el cronograma de trabajo. La elaboración de cualquier proyecto requiere de un análisis presupuestario que dé una aproximación del valor económico del mismo. En la descripción del presupuesto especificaremos los recursos económicos necesarios, así como su justificación y distribución. El cronograma de trabajo también es una parte esencial ya que nos permite desglosar las etapas del proyecto, los plazos que se han de cumplir y los hitos alcanzados a lo largo del desarrollo del proyecto.»
  - También el capítulo 6 (p. 96): «En este capítulo final, se procederá a realizar una evaluación exhaustiva del grado de cumplimiento de los objetivos inicialmente establecidos para este proyecto. Adicionalmente, se discutirán las conclusiones derivadas tanto de estos objetivos como de los resultados obtenidos por el sistema, proporcionando una visión integral y detallada del desempeño y las implicaciones del proyecto en su conjunto.»
- **Cierre de capítulo:** ningún capítulo tiene un apartado «Resumen» o «Conclusiones parciales». Los capítulos terminan con el último párrafo del último epígrafe; a veces ese párrafo es una remisión hacia delante: capítulo 2 (p. 34): «Los ataques que implementaremos probarán la robustez de nuestro sistema y su eficacia para reconstruir la marca de agua en situaciones desfavorables. Los ataques implementados son: adición de ruido, filtrado paso-baja y supresión de muestras. El fundamento matemático de estos ataques se desarrollará con detalle en capítulos posteriores.» El capítulo 5 cierra con un sub-apartado de síntesis (5.5.4) cuyo último párrafo hace de conclusión parcial (p. 91): «Por tanto, dado que el sistema con ponderación temprana es el que mejor reconstruye la señal de voz con mucha diferencia y proporciona una robustez sobresaliente en la detección de la marca de agua, este será sistema el que mejor se adapta a un escenario real y el que mejor cumple las premisas de imperceptibilidad y robustez esenciales en los sistemas de marcado de agua.»

## E. Figuras

- **Número total:** 29 figuras numeradas (1.1; 2.1–2.5; 3.1–3.6; 4.1–4.2; 5.1–5.15), de las cuales 5 están compuestas por dos subfiguras «(a)» y «(b)» (2.1, 3.1, 5.13, 5.14, 5.15): 10 subfiguras.
- **Numeración:** por capítulo (capítulo.ordinal).
- **Formato literal del pie:** «Figura N.M: Texto» — palabra «Figura» con mayúscula, número, **dos puntos**, espacio, texto con mayúscula inicial. El punto final es inconsistente: con punto («Figura 2.4: Obtención de la forma de onda a través de la ISTFT [3].», p. 31; «Figura 5.1: Curva de las pérdidas del Embedder en el proceso de entrenamiento.», p. 64) y sin punto («Figura 3.4: Pesos del Embedder y del Detector», p. 45; «Figura 2.2: Sistema Completo de Watermarking sin DNNs [2]», p. 28). Caso anómalo: «Figura 1.1: Arquitectura del Sistema.[1]» (p. 23), con la cita pegada tras el punto. Pies de subfigura: «(a) Primera aproximación Embedder basada en [2].» / «(b) Primera aproximación Detector basada en [2].» (p. 27); «(a) Señales Reconstruida (azul), Original (roja) y Distorsión (negra).» / «(b) Zoom de las señales.» (p. 92).
- **Posición del pie:** **debajo** de la figura (p. 23: hueco de imagen y después «Figura 1.1: …»; p. 27 y 92: subpies «(a)», «(b)» y a continuación el pie general). Centrado (inferencia por el layout).
- **Cómo se referencian en el texto:** con «figura» en minúscula + número, dentro de la frase o entre paréntesis. Tres frases literales:
  1. «La figura 1.1 muestra un diagrama general del sistema implementado.» (p. 22)
  2. «Comúnmente el hop length suele ser de una menor longitud que el tamaño de la ventana para que las ventanas se solapen entre sí.» precedido de «…viene dada por la longitud de salto o hop length (veáse la figura 2.3).» (p. 31; «veáse» con tilde mal puesta es del original)
  3. «En la curva mostrada en la figura 5.1, calculada a partir del MAE entre la entrada y la salida del Embedder podemos observar una tendencia a la baja a medida que avanzamos en las épocas del entrenamiento…» (p. 64)
  También: «Podemos visualizar gráficamente la evolución de los pesos durante el entrenamiento en la figura 3.4.» (p. 44); a veces solo el número sin la palabra: «…vienen recogidos en la tabla 2.1 y su clasificación en 2.5.» (p. 33), «(véase 3.1b)» (p. 37), «como puede verse en 3.4» (p. 45). Frecuencia: 39 menciones «figura N.M» en el cuerpo.
- **Indicación de fuente:** no se usa «Fuente:» ni «elaboración propia». Las figuras tomadas de otros trabajos llevan la cita bibliográfica dentro del pie: «[1]» (1.1, 3.2, 3.3), «[2]» (2.1, 2.2), «[3]» (2.3, 2.4), «[4]» (2.5). Las figuras propias no llevan indicación alguna.
- **Tipos:** diagramas de bloques/arquitectura (1.1, 2.1, 2.2, 3.1, 3.2, 3.3); ilustraciones conceptuales de la STFT tomadas de una tesis (2.3, 2.4); taxonomía/esquema de ataques (2.5); gráficas de curvas (pesos de entrenamiento 3.4, 3.5; pérdidas 3.6; respuesta en frecuencia y al impulso del filtro 4.1, 4.2; curvas de pérdida y BER por época 5.1–5.12); formas de onda con zoom (5.13–5.15). No hay capturas de pantalla ni fotografías.
- **Colocación:** flotantes en la parte superior o inferior de la página; tres láminas a página completa sin cabecera (p. 92–94); la p. 95 queda prácticamente vacía por el arrastre de flotantes. Las figuras 4.1 y 4.2 quedan lejos de su mención (p. 56–57 frente a la mención en p. 55).

## F. Tablas

- **Número:** 20 tablas, llamadas **«Cuadro»** en el pie y en el índice («Índice de cuadros», p. 18): 2.1; 3.1, 3.2, 3.3; 5.1–5.15; 7.1. Numeración por capítulo.
- **Posición del pie:** **encima** de la tabla en 19 de 20 casos (p. 33, 41, 43, 44, 81–87). Excepción: «Cuadro 7.1: Desglose de los costes de recursos humanos.» va **debajo** (p. 103). Inconsistencia a evitar.
- **Formato literal:** «Cuadro 5.1: SNR (dB) para diferentes niveles de degradación en modelos entrenados» (sin punto final, p. 81); «Cuadro 2.1: Ataques descritos en [4].» (con punto, p. 33); «Cuadro 3.1: Especificaciones del Embedder. Dimensiones de la señal a lo largo de la Red.» (p. 41); «Cuadro 3.3: Valores de los parámetros utilizados para los pesos del modelo» (p. 44).
- **Cómo se referencian (literal):**
  1. «Los ataques descritos en [4] vienen recogidos en la tabla 2.1 y su clasificación en 2.5.» (p. 33) — usa «tabla» aunque el pie diga «Cuadro».
  2. «En el cuadro 7.1 podemos ver un desglose del coste que ha supuesto la confección de este trabajo.» (p. 103).
  Otras: «En la siguiente tabla vienen recogidos los valores numéricos de los parámetros utilizados:» (p. 44, sin número); «Observando las tablas podemos concluir que el modelo que mejor reconstruye la señal de voz…» (p. 82, genérico). Las 15 tablas del capítulo 5 **no se citan por número** en el texto: se introducen con el mini-encabezado «Resultados de evaluación para la SNR» y se comentan en bloque.
- **Contenido:** taxonomía de ataques con abreviaturas (2.1, en inglés, copiada de [4]); especificaciones capa a capa de las redes (tipo de capa, filtros, tamaño/paso, salida: 3.1 y 3.2); hiperparámetros (3.3); matrices 4×4 de evaluación cruzada (filas = modelo entrenado con 0/10/20/30 % de ataques; columnas = probabilidad de ataque en test) para SNR, SDR, PESQ, STOI y BER en tres sistemas (5.1–5.15); desglose de costes de personal con filas Concepto / Ingeniero / Tiempo invertido (h) / Precio unitario (€/h) / Total sin IVA (€) y fila TOTAL (7.1).
- **Estilo de rejilla:** no determinable desde el texto (el layout sugiere tablas sencillas con cabecera de dos niveles «Modelos entrenados» / «Probabilidad de Ataque»).
- **Problemas detectados:** en 12 de las 15 tablas del capítulo 5 cada fila repite el mismo valor en las cuatro columnas (p. ej. «7.12 7.12 7.12 7.12», p. 81), de modo que la dimensión «probabilidad de ataque» no aporta información para SNR/SDR/PESQ/STOI; el «Cuadro 5.12» está titulado «SNR (dB)» cuando contiene la SDR (p. 86); decimales con punto en las tablas («0.9335») pero con coma en el presupuesto («27.590,0 euros», «69,9 €», p. 103–104).

## G. Ecuaciones

- **Hay 32 ecuaciones numeradas**, numeradas por capítulo y alineadas a la derecha entre paréntesis: (2.1)–(2.4), (3.1)–(3.15), (4.1)–(4.13). Solo en los capítulos 2, 3 y 4. El capítulo 5 incluye además ~5 ecuaciones centradas **sin numerar** (definiciones de SNR, SDR y sus términos auxiliares, p. 62) dentro de una lista.
- **Cómo se introducen:** una frase que termina en dos puntos o en «como:», seguida de la ecuación centrada y de un párrafo que empieza por «donde» definiendo cada símbolo en orden de aparición. Ejemplo literal (p. 29):
  > «La fórmula genérica para una señal de voz con marca de agua en el dominio del tiempo (DT) puede ser expresada como en [1]:
  > y(n) = x(n) + αw(n)        (2.1)
  > donde y(n) representa la señal de voz con marca de agua, mientras que x(n) y w(n) representa la señal de voz original y la marca de agua respectivamente. El parámetro α determina la fuerza de la marca de agua incrustada, teniendo un gran impacto en la perceptibilidad y detectabilidad de la marca de agua.»
  (El símbolo α se restituye por el contexto; la extracción lo pierde.)
  Otro patrón (p. 45): «La función de pérdida total, fruto de la combinación de las funciones de pérdida del Embedder y del Detector, se rige a través de la siguiente expresión: L_Total = W_Embedder · L_Embedder + W_Detector · L_Detector (3.5) donde W_Embedder es el peso asignado a la pérdida del Embedder, L_Embedder es la pérdida asociciada al Embedder, definida como el MAE, …».
- **Referencias a ecuaciones en el texto:** «En las ecuaciones 3.3 y 3.4 los parámetros we, wd, Δwe y Δwd son parámetros de diseño y M es el número total de épocas.» (p. 44); «considerando la aproximación dada por la ecuación 3.14» (p. 51). Siempre «ecuación» en minúscula y sin paréntesis.
- **Tipos:** definiciones de señal (2.1, 2.2), STFT y espectrograma con sumatorio (2.3, 2.4), funciones de pérdida (3.1 MAE, 3.2 BCE), pesos definidos por partes con llave y condiciones «si i ≤ 1 / si 1 < i ≤ M» (3.3, 3.4), transformaciones perceptuales con vectores y normas (3.6–3.13), pérdidas combinadas y normalizadas (3.14, 3.15), respuesta de filtro de Butterworth, convolución y derivadas parciales para la retropropagación (4.1–4.13).
- **Símbolos en línea:** uso abundante en el cuerpo: «x», «x̂», «r», «ε» («El objetivo final es que x̂ − x = ε con ε lo más pequeño posible», p. 37), dimensiones «512 × 64 × 2» (p. 39), parámetros «α está fijado a 0.2» (p. 39), «fc = 4 kHz» incluso dentro de pies de figura (p. 56). Subíndices textuales largos en modo matemático («W_Embedder», «L_PESQmax»).

## H. Código y comandos

- **No hay listados de código**, ni pseudocódigo, ni algoritmos numerados, ni comandos, ni nombres de ficheros o funciones. Cero apariciones de «Listado», «Código», «Algoritmo» con número.
- Las herramientas se citan solo en prosa, en el capítulo 7 y de pasada en el 5–6: «…se realizaron unos cursos introductorios al lenguaje de programación Pytorch sobre el que se desarrolla el código del trabajo realizado.» (p. 104; llamar «lenguaje de programación» a PyTorch es impreciso); «El presente proyecto ha sido desarrollado en la plataforma de programación colaborativa Google Colab.» (p. 104); «…no se logra la convergencia total de los modelos debido a las limitaciones de cómputo que la plataforma Google Colab presenta.» (p. 69).
- **Terminología técnica inglesa en el cuerpo:** se escribe tal cual, acompañada de su traducción la primera vez: «capa de normalización (batch normalization)», «capa de dropout», «función de activación Leaky ReLU», «capa fully conected» (sic), «Mean Absolute Error (MAE)» (p. 38–42). Inferencia: «Embedder», «Detector», «Embedding», «carrier», «key», «hop length», «frame-by-frame», «trade-off» van en cursiva (artefactos «Embedder )», «Embedding :» con espacio de corrección de cursiva, p. 28, 42, 45, 61).
- No hay anexo de código ni enlace a repositorio.

## I. Citas y bibliografía

- **Estilo en el texto:** numérico entre corchetes «[n]», colocado antes del punto («…en el mundo digital [2].», p. 26), al inicio de frase como sujeto («En [1], la arquitectura propuesta es capaz de cubrir dos modelos.», p. 36) o en medio («como en [1] y en [3]», p. 29). Citas múltiples separadas con «y» en corchetes independientes («[16] y [17]», p. 38), nunca «[16, 17]». También dentro de pies de figura y de tabla.
- **Orden de la bibliografía:** por orden de aparición (`unsrt`). Prueba: [1]–[4] se numeran según su primera aparición en los pies del índice de figuras (p. 16) y [5] es la primera cita del cuerpo (p. 23). La entrada [28] no se cita en ningún capítulo (incluida vía `\nocite`, inferencia).
- **Número total:** 28 referencias (p. 106–108).
- **Formato literal de entradas:**
  - Artículo: «[1] Kosta Pavlović, Slavko Kovacević, Igor Djurović, and Adam Wojciechowski. Robust speech watermarking by a jointly trained embedder and detector using a dnn. *Digital Signal Processing*, 122:103381, 2022.» (p. 106; cursiva del nombre de revista inferida por el estilo `plain`).
  - Libro: «[2] Michael Arnold, Martin Schmucker, and Stephen D Wolthusen. *Techniques and applications of digital watermarking and content protection*. Artech House, 2002.» (p. 106).
  - Norma: «[20] ITU-T Recommendation. Perceptual evaluation of speech quality (pesq): An objective method for end-to-end speech quality assessment of narrow-band telephone networks and speech codecs. Rec. ITU-T P. 862, 2001.» (p. 107).
  - Congreso: «[24] Jonathan Le Roux, Scott Wisdom, Hakan Erdogan, and John R. Hershey. Sdr – half-baked or well done? In *ICASSP 2019 - 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, pages 626–630, 2019.» (p. 108).
  - Tesis: «[13] Miguel Zamorano Castaño. Análisis de señales mediante stft y wavelet: aplicación a defectología en rodamientos. Master's thesis, 2010.» (p. 107).
  - **Web con fecha de acceso: no hay ninguna.** Cero URLs, cero «Disponible en», cero «consultado el».
- **Proporción por tipo:** 12 artículos de revista (1, 4, 7, 8, 10, 11, 15, 16, 19, 21, 23, 28); 7 comunicaciones a congreso (6, 9, 12, 14, 22, 24, 27); 5 tesis/TFG/TFM (3, 13, 18, 25, 26); 1 libro (2); 1 norma ITU-T (20); 1 corpus/dataset (5); 1 preprint arXiv (17); 0 webs/documentación. Es decir, ~68 % literatura revisada por pares, 0 % documentación de software o páginas web.
- **Dónde se concentran las citas:** 92 citas en el cuerpo: cap. 2 = 30 (12 referencias distintas), cap. 3 = 35 (9 distintas), cap. 5 = 12, cap. 4 = 7, cap. 6 = 6, cap. 1 = 2, cap. 7 = 0. Los capítulos 2 y 3 acumulan el 70 %. La referencia [1] (trabajo que se replica y amplía) se cita en los seis capítulos técnicos, unas 40 veces.
- **Defectos:** estilo BibTeX en inglés («and», «pages», «In», «Master's thesis») en una memoria en castellano; títulos con mayúsculas aplastadas por BibTeX («dnn», «pesq», «stft», «Timit acousticphonetic»); autores desordenados en [5]; [3] y [18] sin indicación de tipo ni institución; «Sdr – half-baked» con guion corto; nombres de revista a veces en minúscula («Signal processing»).

## J. Registro y redacción

- **Persona y voz:** mezcla de **primera persona del plural** («podemos» ×35, «nuestro/a» ×26, «hemos» ×6, «nosotros» ×3; verbos «utilizamos», «presentamos», «implementaremos», «consideraremos», «realizaremos pruebas cruzadas») con **impersonal con «se»** («se procede a la exposición», «se exponen los resultados», «se ha presentado un sistema», «se opta por»). El plural de modestia domina en explicaciones y análisis; el «se» domina en aperturas de apartado y en el capítulo 7. **Nunca** primera persona del singular en el cuerpo (solo en los agradecimientos, p. 12–13). Ejemplos: «Nosotros las hemos adaptado a nuestra conveniencia.» (p. 44); «En esta sección se procede a la descripción de las métricas de evaluación…» (p. 62).
- **Tiempos verbales dominantes:** presente en los capítulos 1–4 (descripción teórica y de diseño), con futuro para anticipar («se desarrollará con detalle en capítulos posteriores», p. 34; «presentaremos y describiremos», p. 54); presente de observación en el capítulo 5 («podemos observar», «se observa», «presenta») con pretérito perfecto ocasional («ha sido esencial»); pretérito indefinido y perfecto en el capítulo 6 («fueron entrenadas conjuntamente», «se le incorporó», «se exploraron», «permitió evaluar») y en el 7 («se desarrolló entre los meses de…», «se realizó un estudio exhaustivo»).
- **Longitud de párrafos y frases:** párrafos largos: media 81 palabras, mediana 70, máximo 268 (p. 39); 2–3 frases por párrafo (media 2,8). Frases largas y subordinadas: media 30 palabras, mediana 27, el 10 % supera las 51. Hay párrafos de una sola frase de 60+ palabras.
- **Listas:** escasas y siempre con etiqueta inicial destacada (inferencia: negrita). Una lista numerada (p. 28: «1. Embedding: … 2. Detección: …»). Listas con viñeta: «Organización de la memoria» (7 ítems «Capítulo N. Título: descripción», p. 23–24); métricas (5 ítems «SNR:», «SDR:», «PESQ:», «STOI:», «BER:», con ecuaciones dentro, p. 62–63); conclusiones particulares (dos bloques de 3 viñetas, p. 97–99); trabajo futuro (4 ítems con título en negrita: «Implementación de nuevos ataques y evaluación de la robustez del sistema ante estos:», «Optimización y eficiencia:», «Aplicaciones en tiempo real:», «Generalización a otros tipos de medio:», p. 100); etapas del cronograma (5 ítems «Primera Etapa:» … «Quinta Etapa:», p. 104–105). Todo lo demás es prosa continua; no hay listas en el diseño ni en el análisis de resultados.
- **Negrita/cursiva en el cuerpo:** no determinable con certeza. Inferencias: negrita solo en etiquetas de ítems de lista; cursiva en anglicismos (Embedder, Detector, carrier, key, hop length, trade-off, frame-by-frame) y en el título del trabajo dentro del informe. Sin negritas de énfasis en los párrafos.
- **Anglicismos y siglas:** anglicismo + equivalente español en la primera aparición, en cualquier orden: «A esta técnica se le conoce como Marca de Agua o Watermark.» (p. 20); «longitud de salto o hop length» (p. 31); «junto a una clave o key» (p. 27); «portadores o carriers» (p. 28). Siglas definidas al primer uso con el desarrollo entre paréntesis («modelo JND (Just Noticeable Difference)», p. 26; «error medio absoluto o Mean Absolute Error (MAE)», p. 38; «Binary Cross Entropy (BCE)», p. 41) y recogidas en la lista «Acrónimos» final (p. 110), que mezcla desarrollos en inglés y en español («DT Dominio del Tiempo»). Se usan «watermarking»/«marcado de agua»/«marca de agua» indistintamente en todo el texto; «deepfake» sin cursiva aparente ni traducción.
- **Nivel de detalle técnico:** alto en la arquitectura (dimensiones tensoriales capa a capa, tamaño de ventana 1024, salto 512, 5 bloques, Leaky ReLU 0.2, dropout 50 %, mensaje de 512 bits repetido 16×2, p. 39–42) y en la derivación matemática de la pérdida PESQ y de los ataques (p. 46–59). Medio-bajo en lo experimental: no se indican tamaños exactos de train/val/test, semillas, número de épocas por fase ni desviaciones típicas; los resultados son medias sin incertidumbre.
- **Cómo se formulan los objetivos:** en **párrafos**, no en lista (1.3, p. 22): «El objetivo de este trabajo es desarrollar un sistema de watermarking robusto haciendo uso de técnicas de aprendizaje profundo. Por robustez entenderemos que la marca de agua pueda ser extraída del audio codificado tras haber sido transmitido por un canal…»; «El reto principal es la construcción de un Embedder y un Detector.»
- **Requisitos:** como principios, en prosa: «El sistema debe de obedecer a dos principios fundamentales: robustez e imperceptibilidad.» (p. 22). Umbral cuantitativo introducido tarde y sin cita: «Este BER no es el adecuado para un sistema de marcado de agua, que debería de mantenerse siempre por debajo del 1 %.» (p. 89).
- **Resultados:** tabla + párrafo con número e interpretación: «…el modelo entrenado con un 30 % de nivel de degradación, proporcionando un BER de 0.05 % en promedio, una SNR de 7.24 dB en promedio, una SDR de 6.63 dB en promedio, un PESQ de 2.23 en promedio y un STOI de 0.9335 en promedio.» (p. 82). La interpretación recurre con frecuencia a la aleatoriedad del entrenamiento para explicar resultados contraintuitivos («Esto se debe nuevamente a la estocasticidad en la generación de ataques.», p. 73; «resulta algo contraintuitivo…», p. 65).
- **Limitaciones:** dentro de la conclusión, en un párrafo (p. 99): «Aunque los rendimientos obtenidos en los tres sistemas evaluados son técnicamente aceptables, existe un considerable margen de mejora. Este potencial está limitado por el tamaño de nuestra base de datos, que contiene únicamente tres horas de audio, en comparación con la extensa base de datos de más de 800 horas utilizada en la referencia principal [1]. Además, las restricciones computacionales impuestas por la plataforma Google Colab han condicionado las fases de entrenamiento, validación y evaluación…». También en 1.4 «Delimitaciones» (p. 23) como supuestos de partida.
- **Frases típicas de apertura y cierre (literales):**
  1. «En este capítulo nos centraremos en una de las facetas fundamentales de los sistemas de watermarking: la robustez.» (apertura cap. 4, p. 54)
  2. «En esta sección se exponen los resultados obtenidos en el proceso de validación del sistema original propuesto en [1].» (apertura 5.4.1, p. 72)
  3. «En este apartado se procede a la exposición de los resultados obtenidos durante el proceso de entrenamiento del sistema propuesto en [1].» (apertura 5.3.1, p. 63)
  4. «Como ya se mencionaba en la sección anterior, una marca de agua se trata de un mensaje que se incrusta en diversos contenidos multimedia…» (apertura 2.2, p. 28)
  5. «Haciendo eco de lo previamente dicho en secciones anteriores, el proceso de entrenamiento de ambas redes neuronales ha de realizarse de manera conjunta…» (apertura 3.4, p. 43)
  6. «Por último, y de igual forma que en los dos apartados anteriores, en esta sección se realizará un análisis cuantitativo de los diferentes escenarios propuestos…» (apertura 5.5.3, p. 86)
  7. «Los resultados obtenidos respecto al BER y la calidad de la señal reconstruida se estudiarán en el capítulo 5.» (cierre de párrafo/anticipación, p. 51)
  8. «Con este trabajo presentamos una base rígida para las posibles investigaciones futuras y nos permite establecer un marco referencial para explorar y expandir los hallazgos en el campo del watermarking basado en redes neuronales.» (cierre cap. 6, p. 100)
- **Conectores frecuentes (recuento en el cuerpo):** «A su vez» (15), «Sin embargo» (15), «Por último» (7), «es decir» (7), «Por otro lado/Por otra parte» (6), «en consecuencia» (6), «Como ya se mencionaba/dijo» (6), «de cara a» (6), «Por tanto» (5), «de suma importancia» (5), «Observando…» (5), «Como podemos ver/Como vemos» (5), «Cabe destacar/mencionar» (4), «trade-off» (4), «dejar en claro» (4), «contraintuitivo» (3). Muletillas a evitar: «debe de» + infinitivo (reiterado), «de la misma» como pronombre («la percepción de la misma»), «el mismo/la misma» anafóricos.
- **Tres párrafos representativos completos (literales):**
  - *Diseño/arquitectura* (p. 39): «La parte de la arquitectura que realiza el downsampling consta de 5 bloques que realizan la convolución bidimensional de la señal de entrada, reduciendo las dimensiones espaciales de la misma y aumentando el número de filtros. Tras la convolución bidimensional, la señal pasa por una capa de normalización (batch normalization) y por una función de activación Leaky ReLU cuyo parámetro α está fijado a 0.2. Tras los 5 bloques que componen la parte de downsampling de la arquitectura la representación de la señal de entrada en el espacio latente adopta unas dimensiones de 16 × 2 × 256, donde, siguiendo la misma estructura que antes, 16 representa el número de puntos de frecuencia, 2 el número de tramas temporales y 256 el número de canales. En este punto, la marca de agua es incrustada en la señal mediante la concatenación al final de la dimensión de los canales. La marca de agua se trata de una señal binaria generada a partir de un conjunto de mensajes escogidos aleatoriamente, dando lugar a un vector unidimensional de 512 bits. Dado que la marca de agua es un vector de una dimensión, esta es repetida 16 × 2 veces antes de ser incrustada con el fin de incrementar la probabilidad de que sea preservada. El tensor resultante tras la concatenación de la marca de agua con la representación de la señal de entrada en el espacio latente rompe la simetría de la arquitectura de la U-Net, lo que afecta a la parte de upsampling y reconstrucción del Embedder. Este problema queda resuelto en [1] añadiendo otra capa de convolución bidimensional que reduce el número de canales y restaura la simetría.»
  - *Resultados/evaluación* (p. 82): «Observando las tablas podemos concluir que el modelo que mejor reconstruye la señal de voz y detecta la marca de agua en todos los escenarios posibles es el modelo entrenado con un 30 % de nivel de degradación, proporcionando un BER de 0.05 % en promedio, una SNR de 7.24 dB en promedio, una SDR de 6.63 dB en promedio, un PESQ de 2.23 en promedio y un STOI de 0.9335 en promedio. Aunque el PESQ obtenido es ligeramente mejor para el modelo entrenado con un 20 % de ataques, la diferencia en la robustez que existe entre estos dos sistemas hace que el modelo entrenado con un 30 % de ataques sea mejor opción.»
  - *Conclusiones* (p. 98): «Podemos afirmar que el sistema cumple satisfactoriamente con los requisitos de imperceptibilidad y robustez en mayor o menor medida. Los resultados obtenidos en el capítulo anterior muestran la efectividad del sistema en preservar la calidad de la marca de agua incrustada en el Embedder a pesar de las degradaciones introducidas antes de llegar al Detector y, a su vez, garantiza que la distorsión provocada por la marca de agua sobre la señal reconstruida sea prácticamente imperceptible para el usuario final.»

## K. Capítulo a capítulo

**Capítulo 1. Introducción (p. 20–24; ~1 700 palabras; 1 figura, 0 tablas).** Propósito: contexto, motivación, objetivos, delimitaciones y organización. Contenido: 1.1 problema (deepfakes y biometría), 1.2 motivación, 1.3 objetivos (en prosa; dos principios: robustez e imperceptibilidad; figura 1.1 con el diagrama general tomado de [1]), 1.4 delimitaciones (señales limpias, corpus TIMIT), 1.5 organización por capítulos en lista. Bien: la organización de la memoria es clara y específica; define «robustez» operativamente. Mal: los objetivos no son una lista verificable ni se retoman uno a uno en las conclusiones; 1.1 y 1.2 repiten ideas; la figura 1.1 es ajena; 1.4 describe TIMIT y luego 5.1 lo vuelve a describir.

**Capítulo 2. Watermarking. Antecendentes, dominios y métodos (p. 26–34; ~2 500 palabras; 5 figuras, 1 tabla; 30 citas).** Estado del arte: historia y sistemas clásicos (2.1), watermarking con redes neuronales y STFT (2.2, 2.2.1 con ecuaciones 2.1–2.4), elección del dominio (2.3), tipos de ataques con taxonomía de [4] (2.4). Bien: concentra la revisión bibliográfica; termina anunciando los tres ataques implementados. Mal: todas las figuras son prestadas; tabla 2.1 en inglés; errata en el título del capítulo; 2.3 arranca con «Para abordar esta pregunta…» sin que haya pregunta formulada.

**Capítulo 3. Arquitectura de las Redes Neuronales. Implementación del Sistema de Watermarking basado en U-Net. (p. 36–52; ~5 400 palabras; 6 figuras, 3 tablas; 15 ecuaciones; 35 citas).** Núcleo del diseño: redes propuestas (3.1), Embedder U-Net con MAE (3.2, 3.2.1, cuadro 3.1), Detector con BCE (3.3, 3.3.1, cuadro 3.2), entrenamiento conjunto con pesos por época (3.4, ecuaciones 3.3–3.5, cuadro 3.3), función de pérdida PESQ y su integración con dos esquemas de ponderación, temprana y tardía (3.5.x, ecuaciones 3.6–3.15). Bien: es el capítulo más sólido; cada bloque de red se describe con dimensiones y justificación («potencia de dos para conservar la simetría de la U-Net»); se explicita qué se cambia respecto a [1]. Mal: el título es largo y lleva punto; la figura 3.2 (diagrama con dimensiones) se pierde al extraer pero su contenido se duplica en el cuadro 3.1; el capítulo ya adelanta resultados («superando así las prestaciones del sistema original», p. 50) antes del capítulo de resultados; mezcla aportación propia y resumen de [19] sin separarlos tipográficamente.

**Capítulo 4. Ataques implementados en el sistema. (p. 54–59; ~1 500 palabras; 2 figuras, 0 tablas; 13 ecuaciones; 7 citas).** Tres ataques como capas no entrenables: filtro paso-baja de Butterworth orden 16 y fc = 4 kHz (4.1), ruido aditivo con cálculo del nivel para 30 dB (4.2), supresión aleatoria del 3 % de muestras (4.3); para cada uno, modelo, derivada parcial y regla de la cadena. Bien: estructura paralela y previsible; justifica cada parámetro (por qué 4 kHz, por qué 1000 muestras de 32768). Mal: la figura 4.1 queda alejada de su mención; las derivaciones de la retropropagación son redundantes entre sí.

**Capítulo 5. Marco y Resultados Experimentales (p. 60–95; ~9 400 palabras, un tercio del cuerpo; 15 figuras, 15 tablas; 12 citas).** Dataset TIMIT y segmentación en 32768 muestras (5.1), métricas SNR/SDR/PESQ/STOI/BER (5.2), y después una matriz 3 fases × 3 sistemas: entrenamiento (5.3.1–5.3.3), validación (5.4.1–5.4.3) y evaluación (5.5.1–5.5.3) para el sistema original, con ponderación tardía y con ponderación temprana, cada uno con 4 niveles de probabilidad de ataque (0/10/20/30 %); 5.5.4 análisis general por nivel de ataque. Bien: la estructura es sistemática y exhaustiva; cada tabla va seguida de interpretación con cifras; el 5.5.4 compara y elige («el sistema con ponderación temprana es el que mejor se adapta a un escenario real»). Mal: altísima repetición (los mismos párrafos sobre «el aumento de la pérdida no implica peor reconstrucción» aparecen en 3.5.4, 5.3.2, 5.3.3, 5.4.2, 5.4.3); las curvas de entrenamiento y validación ocupan 12 figuras de página casi completa; doce tablas con columnas idénticas; sin medidas de dispersión ni tests; explicación recurrente de resultados contraintuitivos por «la naturaleza estocástica» sin contraste; mini-encabezados inconsistentes («evaluación» vs «test»); p. 95 casi vacía.

**Capítulo 6. Conclusiones y Trabajo Futuro (p. 96–100; ~1 750 palabras; 0 figuras, 0 tablas; 6 citas).** Párrafo introductorio, 6.1 Conclusión (recapitulación del sistema, dos bloques de conclusiones particulares en viñetas con cifras de BER por sistema, párrafo de limitaciones), 6.2 Trabajo futuro (4 líneas con cita). Bien: cuantifica las conclusiones («El BER varía de un 0 % con un 0 % de ataques a un 0.81 % con un 30 % de ataques»); reconoce limitaciones con cifras (3 h frente a 800 h). Mal: no comprueba objetivo por objetivo pese a anunciarlo («evaluación exhaustiva del grado de cumplimiento de los objetivos»); un bloque de 6.1 aparece sangrado como si fuera parte de una lista (p. 96–97: error de maquetación); dos líneas con un punto suelto (p. 100); «base rígida» por «base sólida».

**Capítulo 7. Presupuesto y Cronograma de Trabajo (p. 102–105; ~950 palabras; 1 figura no numerada (Gantt), 1 tabla; 0 citas).** Sí existe capítulo de planificación/costes y contiene: 7.1.1 costes de recursos humanos: ingeniero senior 65 €/h, junior 50 €/h; conceptos «Formación y documentación 100 h», «Diseño e implementación de los sistemas de watermarking 230 h», «Análisis de los resultados 25 h», «Redacción de la memoria 50 h», «Revisión de la memoria 20 h», «Revisión y dirección del trabajo (tutor 1) 68 h», «(tutor 2) 68 h»; TOTAL 561 h y 27.590 € sin IVA (cuadro 7.1). 7.1.2 coste del material: suscripción Google Colab 11,65 €/mes × 6 meses = 69,9 €; dataset cedido por los tutores (coste nulo); Overleaf gratuito; portátil HP 15-fc0091ns (Ryzen 5, 16 GB, 1 TB) con amortización de 181,74 €; **total del proyecto 27.841,64 €**. 7.2 cronograma: cinco etapas en lista (oct–dic 2023 estudio; dic 2023–ene 2024 cursos de PyTorch y Colab; feb–may 2024 diseño, entrenamiento y resultados; may–jun 2024 redacción; últimas semanas de junio revisión) y diagrama de Gantt pgfgantt de octubre 2023 a julio 2024 con filas «Proyecto Completo», «Etapa 1»–«Etapa 5», «Defensa TFG» y porcentajes de avance. Bien: va al final, es breve, da horas, tarifas, hardware, software y total. Mal: el Gantt no tiene pie ni numeración; no se desglosan licencias ni costes indirectos; no se justifica la amortización; el símbolo € se pierde en la extracción («65,»), lo que sugiere un problema de codificación de la fuente.

## L. Particularidades UGR/ETSIIT

- **Portada (p. 1), orden exacto de elementos:** «TRABAJO FIN DE GRADO» → titulación en mayúsculas → título → «Autor» + nombre → «Directores» + dos nombres → nombre completo de la Escuela → «Granada, Junio de 2024». No aparece la palabra «Universidad de Granada» en texto (se supone en el escudo). No hay DNI, ni departamento, ni curso académico en la portada.
- **Portadilla (p. 3):** repite título, autor y directores sin fecha.
- **Orden de páginas iniciales:** portada → portadilla → resumen/palabras clave (ES) → abstract/keywords (EN) → informe de los directores → dedicatoria → agradecimientos → índice general → índice de figuras → índice de cuadros. Es decir, el resumen va **antes** del informe de los tutores y la dedicatoria/agradecimientos después del informe.
- **Fórmula oficial del tutor:** «D. [Nombre], Profesor del Área de [área] del Departamento de [departamento] de la Universidad de Granada. […] Informan: Que el presente trabajo, titulado […], ha sido realizado bajo su supervisión por [alumno], y autorizamos la defensa de dicho trabajo ante el tribunal que corresponda. Y para que conste, expiden y firman el presente informe en Granada a [día] de [Mes] de [año]. Los directores: [nombres]» (p. 10). Es la única mención al **tribunal** en toda la memoria.
- **Firma:** solo los nombres bajo «Los directores:»; no hay rúbrica visible ni línea de firma en la extracción (no determinable si el PDF lleva firma gráfica).
- **DNI:** no aparece en ninguna página.
- **Nombre del tutor y departamento:** tutores como «Directores» en portada y portadilla; en el informe con tratamiento «D.» y la fórmula «Profesor del Área de Teoría de la Señal del Departamento de Teoría de la Señal, Telemática y Comunicaciones de la Universidad de Granada».
- **No hay** declaración de originalidad firmada por el alumno ni autorización de depósito en biblioteca; **no hay** hoja con la composición del tribunal ni calificación.
- La «Lista de Acrónimos» va al final, tras la bibliografía (p. 110), y así figura en el índice.

## M. Cifras globales

- **Páginas (PDF):** preliminares 1–19 (19 páginas, de ellas 5 en blanco/casi vacías); cuerpo 20–105 (86 páginas, de ellas 4 en blanco de cambio de capítulo y 1 casi vacía); bibliografía 106–108 (3 páginas) + 1 blanco; acrónimos 110 (1 página); anexos: 0. Total 110.
- **Figuras:** 29 numeradas (+10 subfiguras). **Tablas:** 20. **Ecuaciones numeradas:** 32 (+ ~5 sin numerar). **Listados de código:** 0. **Referencias:** 28 (27 citadas en el cuerpo, 92 citas en total).
- **Palabras (aprox., por recuento de la extracción):** resumen 417; abstract 343; agradecimientos + dedicatoria ≈ 800; índices ≈ 2 900 tokens (incluidos puntos de relleno); cap. 1 ≈ 1 700; cap. 2 ≈ 2 500; cap. 3 ≈ 5 400; cap. 4 ≈ 1 500; cap. 5 ≈ 9 400; cap. 6 ≈ 1 750; cap. 7 ≈ 950; bibliografía ≈ 780; acrónimos ≈ 90. Cuerpo (cap. 1–7) ≈ 23 200 palabras; total documento ≈ 28 500.
- **Densidad:** ≈ 300–420 palabras por página de texto corrido (p. ej. p. 14–16: 576, 583, 552 tokens por los índices; p. 39: 504; páginas con figura: 120–250).
- **Párrafos de más de 25 palabras:** 241; frases: ≈ 760; media de 30 palabras por frase.

## N. Lecciones transferibles

### N.1 Reglas concretas para que una memoria nueva se parezca a esta

1. **Maquetar en LaTeX con clase tipo `book` a dos caras y babel español**: «Capítulo N» en línea propia y el título debajo; capítulos siempre en página impar; cabecera par «número + sección», impar «capítulo + número»; índices titulados «Índice general», «Índice de figuras», «Índice de cuadros»; tablas llamadas «Cuadro» (o, si se prefiere «Tabla», redefinir `\tablename` y ser coherente en texto e índice).
2. **Epígrafes numerados con punto tras el número** («1.1.», «2.2.1.») y profundidad máxima de tres niveles; epígrafes sin numerar solo para mini-encabezados que introducen tablas o comparativas dentro de resultados. Títulos de capítulo sin punto final y con una sola convención de mayúsculas.
3. **Páginas iniciales en este orden**: portada (TRABAJO FIN DE GRADO / titulación / título / Autor / Directores / Escuela / «Granada, Mes de Año»), portadilla, resumen + «Palabras clave:» (ES), «Project Title:» + «Keywords:» + «Abstract» (EN), informe de los directores con la fórmula «Informan: Que el presente trabajo, titulado …, ha sido realizado bajo su supervisión por …, y autorizamos la defensa de dicho trabajo ante el tribunal que corresponda. Y para que conste, expiden y firman el presente informe en Granada a … .», dedicatoria, agradecimientos, tres índices. Resumen de 3 párrafos (~400 palabras): contexto, qué se hace y cómo, qué se obtiene.
4. **Capítulo 1 con cinco apartados fijos**: descripción del problema, motivación, objetivos, delimitaciones y organización de la memoria (lista de ítems «Capítulo N. Título: qué contiene», un párrafo por capítulo).
5. **Figuras: pie debajo, «Figura N.M: Texto.»** con dos puntos; referencias en minúscula («la figura 5.1», «(véase la figura 2.3)»); si la figura es ajena, la cita «[n]» va dentro del pie; si es propia, nada. Numeración por capítulo. **Tablas: pie encima, «Cuadro N.M: Texto»**, referidas por número en el texto (esta memoria no lo hace en el cap. 5: corregirlo).
6. **Ecuaciones centradas y numeradas por capítulo «(N.M)»**, introducidas por una frase que acaba en dos puntos y seguidas de «donde …» definiendo cada símbolo en orden; referidas como «la ecuación 3.14» o «las ecuaciones 3.3 y 3.4».
7. **Citas numéricas «[n]» por orden de aparición** (BibTeX `unsrt`), antes del punto, también en pies de figura/tabla; la referencia principal se cita cada vez que se toma algo de ella («como en [1]», «siguiendo la línea de trabajo presentada en [1]»). Mejor que esta memoria: usar un estilo en español y referencias con URL y fecha de acceso para webs, que aquí no existen.
8. **Voz: plural de modestia + impersonal con «se»**, nunca «yo» en el cuerpo. Aperturas de apartado con fórmula fija («En esta sección se exponen…», «En este apartado se procede a…», «En este capítulo nos centraremos en…»), presente en diseño, presente de observación en resultados, pasado en conclusiones y cronograma.
9. **Párrafos de 2–3 frases y 60–90 palabras**, prosa continua, listas solo para: organización de la memoria, métricas, conclusiones particulares, trabajo futuro y etapas del cronograma, siempre con etiqueta inicial destacada seguida de dos puntos.
10. **Anglicismo + equivalente español en la primera aparición** («marcado de agua o watermarking», «longitud de salto o hop length») y sigla con desarrollo entre paréntesis al primer uso; lista de acrónimos al final (o al principio, pero una sola).
11. **Resultados: tabla, después párrafo que repite las cifras clave con unidad y las interpreta**, y un sub-apartado final de «Análisis general» que compara y elige explícitamente la mejor variante; las conclusiones repiten las cifras decisivas (BER, SNR…) y un párrafo de limitaciones con números (horas de audio, cómputo).
12. **Capítulo final de «Presupuesto y Cronograma»** con: tarifa senior/junior, tabla concepto × ingeniero × horas × €/h × total, total de horas y euros sin IVA, costes de material (suscripciones, hardware con amortización, software gratuito), total del proyecto, etapas con meses y Gantt (pgfgantt) de todo el curso, incluida la defensa.

### N.2 Cosas que NO aparecen en este TFG (y conviene no introducir)

- Emojis, iconos, colores en el texto, markdown, cajas o «callouts».
- Negritas de énfasis en el cuerpo de los párrafos (solo etiquetas de lista, inferido).
- Listas con viñetas en el diseño o en el análisis de resultados; listas anidadas de más de un nivel (salvo las viñetas dentro de 6.1).
- Listados de código, pseudocódigo, comandos, nombres de ficheros/funciones, capturas de pantalla, enlaces a repositorios.
- Referencias web con URL y fecha de consulta; documentación de software citada.
- Notas al pie (ninguna detectada), glosario inicial, anexos, índice de ecuaciones.
- Primera persona del singular en el cuerpo; preguntas retóricas (solo una implícita en 2.3).
- Tests estadísticos, intervalos de confianza, desviaciones típicas, semillas, tiempos de cómputo.
- Declaración de originalidad, autorización de biblioteca, DNI, hoja de tribunal.
- Resúmenes o conclusiones parciales al final de cada capítulo.

### N.3 Errores detectados que conviene evitar

- Erratas en títulos que se propagan al índice: «Antecendentes» (cap. 2), «Entrenamieto» (5.3.2), «frencuencia» (fig. 4.1); y en el cuerpo: «artifical», «otrográficas», «recosntrucción», «decaeimiento», «referecia», «inlcuyendo», «percpetual evaluation of speech quiality», «aleatoridad», «impercetibilidad», «asociciada», «malitencionados», «Ziwcker» (Zwicker), «fully conected», «para para», «parar garantizar», «a el MAE», «veáse», «generated.Two».
- Acrónimos mal desarrollados: «LSB Lateral Single Band» (es Least Significant Bit), «QIM Quantified Index Modulation» (Quantization) (p. 110).
- «Cuadro 5.12: SNR (dB)» cuando la tabla es de SDR (p. 86); doce tablas con las cuatro columnas idénticas; valores con distinto número de decimales en la misma tabla («0.93», «0.935», «0.9335»).
- Pie de tabla encima en todas menos en el cuadro 7.1 (debajo); punto final inconsistente en pies de figura y tabla; cita pegada al punto («Sistema.[1]»).
- Mezcla «tabla»/«cuadro» en el texto frente a «Cuadro» en pies; «evaluación»/«test» en los mini-encabezados; decimales con punto en tablas y con coma en el presupuesto.
- Índice desfasado en la entrada «Bibliografía 107» (real 105); espacio antes del punto en la fecha del informe; «Departamento Teoría» sin «de».
- Página casi vacía por arrastre de flotantes (p. 95); figuras alejadas de su mención (4.1, 4.2); bloque de texto sangrado por error como ítem de lista (p. 96–97); puntos sueltos en líneas propias (p. 100).
- Repetición casi literal del mismo razonamiento en cinco apartados distintos (el aumento de la pérdida al añadir el término PESQ).
- Anticipar resultados en el capítulo de diseño («superando así las prestaciones del sistema original», p. 50).
- Estilo bibliográfico en inglés para una memoria en castellano, con mayúsculas aplastadas en siglas («dnn», «pesq», «stft») y una referencia no citada ([28]).
- Enunciar la comprobación de objetivos en la apertura del capítulo 6 y no hacerla uno a uno.
- Llamar a PyTorch «lenguaje de programación»; «base rígida» por «base sólida»; «recursos humanitarios» por «recursos humanos» (p. 24, 104).

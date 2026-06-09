# Bit rate selection technology of image processing based on artificial intelligence in MPEG-DASH adaptive streaming media
**Archivo PDF:** `1-s2.0-S1687850724002206-main.pdf`
**Identificador:** `08_pca_gwo_bp_mpeg_dash_ai_bitrate_selection`
**Páginas:** 9
**Foco para Fase 4-5 v1:** Hybrid AI bitrate selection with PCA/GWO/BP and image-processing framing.

> Documento Codex-ready generado para diseño de nuevos modelos/controllers IA ABR. No es una source card corta. Contiene extracción técnica cruda y organizada. El PDF original sigue siendo la fuente de verdad para fórmulas, tablas y figuras si la extracción textual pierde layout.

## 1. Cómo usar este `.md`
- Leer primero las secciones 2-4 para ubicar método, datos y evaluación.
- Usar los extractos crudos por categoría como material base para diseño/contratos/Codex.
- Para ecuaciones, tablas o figuras críticas, comprobar la página indicada en el PDF original.
- No tratar los resultados del paper como promesa directa para DashClientModular4; convertirlos en hipótesis/guardrails y verificar en Phase 6.

## 2. Índice de secciones detectadas
- p.2: P. Yang et al.
- p.3: P. Yang et al.
- p.4: P. Yang et al.
- p.5: P. Yang et al.
- p.6: 1080 Ti
- p.6: 16 GB DDR4 RAM
- p.6: 512 GB SSD
- p.6: P. Yang et al.
- p.7: P. Yang et al.
- p.8: P. Yang et al.
- p.9: P. Yang et al.

## 3. Índice de páginas con palabras clave
- p.1: training, PPO
- p.2: throughput, training, OOD
- p.3: training
- p.5: training
- p.6: dataset, training, PPO, generalization
- p.7: dataset, training, PPO
- p.8: state, dataset, training
- p.9: state, action

## 4. Extracción técnica cruda por categorías

### 4.x Modelo / arquitectura / algoritmo

**[Modelo / arquitectura / algoritmo | extracto 1 | p.1]**

Bit rate selection technology of image processing based on artificial intelligence in MPEG-DASH adaptive streaming media Ping Yang *, Jinyi Qiao , Minxiu Chen School of Media and Design, Hangzhou Dianzi University, Hangzhou, 310018, China A R T I C L E I N F O Keywords: AI MPEG-DASH Streaming media product Bit rate selection technique PCA-GWO-BP A B S T R A C T Aiming at the bit rate selection problem of MPEG-DASH adaptive streaming media in image processing, a hybrid method combining multiple artificial intelligence algorithms is proposed. Firstly, kernel principal component analysis, Grey Wolf optimization algorithm and least squares support vector machine are integrated to construct an efficient hybrid algorithm model. This model aims to optimize the image processing effect in streaming media transmission, especially in the dynamic network environment. The experimental results show that the accuracy of the hybrid algorithm reaches 0.945 in the training process, and the absolute error is only 0.0005, which is significantly better than other comparison algorithms. Further empirical analysis shows that the accuracy of the proposed rate selection technique in image processing is as high as 92.3%, which is far higher than the existing technique. This research not only improves the image quality of streaming media transmission, but also greatly improves the user experience. The research provides a new perspective for image processing technology in the field of digital media, and is of great significance for promoting the innovation and development of streaming media technology. 1. Introduction In the digital era, streaming media technology has become a popular way of multimedia transmission, widely used in online video, audio live broadcast, distance education and many oth

**[Modelo / arquitectura / algoritmo | extracto 2 | p.2]**

changes of network conditions to ensure smooth playback. This research provides a new bit rate selection strategy for the streaming media field, which effectively improves the efficiency and user experience of streaming media transmission. The paper mainly consists of four parts to discuss, the first part of the content is mainly to describe the BP algorithm, GWO algorithm and the related research on intelligent algorithms in the field of streaming media; the second part of the content is mainly to analyze the bit rate selection technology for MPEG-DASH adaptive streaming media products based on PCA-GWO-BP algorithm; the third part is mainly to compare and contrast the performance and research to propose a new bit rate selection strategy for streaming media products. performance comparison and the comparative analysis of the research proposed streaming media product bit rate selection techniques; the fourth part is mainly the summary of the whole paper. 2. Literature review As various optimization methods of BP algorithm are gradually developed, BP algorithm and its improved algorithms are applied in many fields. Lu’s team proposed a novel algorithm based on adaptive cloning genetic algorithm and BP algorithm to address the problem of low recognition accuracy of traditional intrusion detection system. The model is applied in simulation experiments, and the outcomes demonstrate that the detection accuracy exceeds the traditional intrusion detection system, and it has good global searchability (Lu et al., 2021). Safavi et al. introduces and compares the BP algorithm and radial basis function NN in order to make a better estimation of the minimum deviation of the nuclear boiling ratio, and the results of the comparison of the two networks show that the training of the radi

**[Modelo / arquitectura / algoritmo | extracto 3 | p.3]**

combination of BP neural network and MPEG-DASH can greatly improve the intelligence and user experience of streaming media transmission. Therefore, this paper proposes a bit rate selection technology for streaming media products based on improved BP neural network, hoping that it can provide an efficient selection scheme and promote the user’s experience. In this selection technology, BP neural network is mainly composed of three modules: input layer, hidden layer and output layer. The constitutive model of BP neural network is shown in Fig. 1. The main module HL in the BP NN can be categorized according to the number of layers, divided into single HL and multi-HL. In the prediction network bandwidth mapping relationships are not complex, so the single HL BP NN with shorter training time can be used. In the BP NN, the output value net1 expression transmitted from the IL to the HL is shown in Equation (1). net1 = w1x + b1, h = g1(net1) (1) In Equation (1), x denotes the initial value of neuron; b1 denotes the intercept term, and the weight value of interlayer connection is denoted by w1. The result net2 expression transmitted from the HL to the OL is shown in Equation (2). net2 = ω2 + b2, y = g2(net2) (2) In Equation (2), b2 denotes the intercept term and ω2 denotes the weight value of the connection between the HL and the OL. The specific sigmoid function expression is shown in Equation (3). y ⌢= g2(net2) = g2 ( vTg1(net1) + b2 ) = g2 ( vTg1 ( wTx + b1 ) + b2 ) (3) In Equation (3), y ⌢is the NN output value. During the operation of the BP NN, errors are always generated, and the total error generated during the operation E(θ) is expressed in Equation (4). E(θ) = 1 2 ∑ 2 i=1 (yi −̂yi)2 (4) In Equation (4), y denotes the actual value. Although the BP algorithm has a bette

**[Modelo / arquitectura / algoritmo | extracto 4 | p.4]**

F = 1 A ∑ A s=1 ̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ∑ A k=1 ( y s k −o s k )2 √ √ √ √ (6) In Equation (6), A represents the number of grey wolves. Then the three GWs with the highest values in the wolf population are selected and recorded as, δ . The parameters r→ 1 , r→ 2 , a→in the GWO are updated to determine the location of the new wolf individuals and utilized as the initial parameters of the BP NN. Based on the updated fitness value of the wolf individuals, the newest, δ are re-informed. Finally, check whether the quantity of iterations set by the algorithm is reached. If it is not done, the parameters r→ 1 , r→ 2 , a→in the GWO are re-updated, and if it is done, the BP NN is given the optimal initial parameters. PCA is a preprocessing method that transforms the original multiple variables into several with comprehensive indicators (Diab et al., 2022b). For better enhancing the efficiency and prediction accuracy of the GWO-BP algorithm, this study adopts PCA to downsize the evaluation index data and constructs a GWO-BP prediction model based on PCA.The flowchart of the PCA-GWO-BP model is shown in Fig. 3. As can be seen from Fig. 3, the specific steps for solving the GWO-BP algorithm incorporating the PCA algorithm are as follows: firstly, determine the position and speed of the GWs of the initialized population, and count the fitness of each GW. Perform the advantage and disadvantage ranking of GWs, and update the position and speed of GWs. On the grounds of the updated GW positions, the positions are downscaled using the PCA algorithm. Based on the dimensionality reduction, train the network using the BP algorithm and calculate the fitness of the network. According to the size of the fitness, update the Fig. 3. PCA-GWO-BP model flow. Fig. 4. Bit rate selection

**[Modelo / arquitectura / algoritmo | extracto 5 | p.5]**

position and speed of the GW population. Repeat initializing the GW position and velocity of the population until the stopping condition is reached. The GW position update formula in the GWO-BP algorithm incorporating PCA algorithm is shown in Equation (7). x(i, t + 1) = x(i, t) + Aʹ ∗D (7) In Equation (7), Aʹ is the control parameter, D is the position difference of the GW, and the GW velocity update formula is showcased in Equation (8). v(i, t + 1) = r ∗v(i, t) + C ∗P − x(i, t) (8) In Equation (8), C serves as the control parameter, r is the random number, and P serves as the position of the current optimal solution, respectively. The selection of the control parameters A and C has a great influence on the convergence speed and the quality of the solution of the algorithm, and the optimal values are usually determined experimentally and empirically. The GW fitness calculation formula is shown in Equation (9). fitness(i) = 1 (1 + error(i)) (9) In Equation (9), P is the training error of the BP algorithm. The GWOBP algorithm incorporating PCA algorithm is able to find the optimal solution of the optimization problem faster by combining PCA algorithm and GWO-BP algorithm, using the dimensionality reduction ability of PCA algorithm and the optimization ability of GWO-BP algorithm. Meanwhile, by flexibly adjusting the parameters, it can achieve better performance in the prediction problem. 3.2. Streaming media product bit rate selection technique based on PCAGWO-BP algorithm MPEG-DASH adaptive streaming product bitrate selection technology is a technology that dynamically adjusts the video bitrate based on the network environment, aiming to provide users with a smooth, highquality video experience (Khalaf et al., 2020). This technology utilizes the MPEG-DASH standard to ad

**[Modelo / arquitectura / algoritmo | extracto 6 | p.6]**

media product; α and β are the adjustment coefficients, which can be set according to the actual situation. Finally, the bitrate selection strategy is continuously optimized through real-time monitoring and feedback mechanism. This process needs to be adjusted according to user feedback and network conditions to improve user experience and service quality. In the above process, the prediction of network bandwidth using the network bandwidth prediction model constructed based on PCAGWO-BP algorithm is the most important part of it, and the specific flow of this prediction model is shown in Fig. 5. Fig. 5 showcases the process of the network bandwidth prediction model based on the improved BP algorithm can be mainly divided into the following eight processes. First, historical data on network bandwidth is collected, including information on network traffic and bandwidth utilization. These data will be utilized as inputs to the model for training and predicting network bandwidth. After that, the collected raw data are preprocessed, including data cleaning, normalization and other operations to eliminate the effects of outliers and magnitude differences on the prediction model. The pre-processed data is then subjected to dimensionality reduction using the PCA algorithm to extract key features and remove noise. This reduces the dimensionality of the data, reduces computational complexity, and improves the generalization ability of the model. The fourth step is to construct a BP NN with a suitable number of HL nodes based on the features of the dimensionality reduced data. This network will be used to learn and predict the change law of network bandwidth. Then the GWO algorithm is applied to optimize the weights and thresholds of the BP NN. By simulating the hunting behavior

**[Modelo / arquitectura / algoritmo | extracto 7 | p.7]**

curve of 0.857; it exceeds the GWO-BP algorithm’s 0.763, the SSA-BP algorithm’s 0.756, and the GWO-SVM algorithm’s 0.747. The above results illustrate that, in terms of the dimension of the ROC curve, the research proposed PCA-SWO-BP algorithm’s performance is better than the comparison algorithms. The training error data of the four algorithms during model training are compared and the outcomes are showcased in Fig. 8. Fig. 8 showcases that among the four algorithms, the PCA-GWO-BP algorithm has the most obvious downward trend of training error and reaches the desired accuracy at 566 iterations; the GWO-BP algorithm has a slightly slower downward trend of training error and reaches the desired accuracy at 855 iterations; and the SSA-BP algorithm has a relatively gentle downward trend of training error and reaches the desired accuracy at 955 iterations; The GWO-BP algorithm has the smoothest decline in training error and reaches the desired accuracy in 1032 iterations. This result indicates that the proposed PCA-GWO-BP algorithm performs better in training, has the fastest convergence speed and has better performance. Fig. 9 gives the comparison results of the absolute errors of the four algorithm models during the prediction process. From Fig. 9, the PCA-GWO-BP algorithm has the lowest overall level of absolute error, with an average absolute error value of 0.0005; which is below the GWO-BP algorithm’s 0.0012; the SSA-BP algorithm’s 0.0021; and the GWO-SVM algorithm’s 0.0057. From this result, it can be concluded that in terms of the absolute error dimension, the PCAGWO-BP algorithm’s overall performance is also better than the comparison algorithms. Comparing the above dimensions, it showcases that the overall prediction performance of the proposed PCA-GWO-BP algorith

**[Modelo / arquitectura / algoritmo | extracto 8 | p.8]**

media products proposed in the study (Technology 1) and the code rate selection technology for streaming media products based on SSA-BP algorithm (Technology 2) and the code rate selection technology for streaming media products based on GWO-BP algorithm (Technology 3) are compared and experimented, and the accuracy, real-time, and impact on the user experience of the code rate selection are used as the comparison indexes. The accuracy and real-time comparison results of the three techniques in different datasets are shown in Fig. 10. From Fig. 10(a), the selection accuracy of technique 1 in the video dataset is 92.3%, which is significantly higher than that of technique 2 (80.1%) and that of technique 3 (79.5%); moreover, it can be found that the selection accuracy of technique 1 in the network state dataset is 91.8%, which is significantly higher than that of technique 2 (78.3%) and that of technique 3 (79.9%). From Fig. 10(b), it can be obtained that the response time of technology 1 in both data sets is less than 5 s, which is much lower than that of technology 2 and technology 3. Therefore, from the above results, it can be concluded that the accuracy and realtime performance of the proposed streaming media product bit rate selection technology is better than the comparison technology. For comparing the actual application effect of the three technologies, the study selected a number of different groups of users to score their experience and statistics, the scoring statistics are shown in Fig. 11. The full score is 10 points, the higher the score, the higher the recognition. Fig. 11showcases that the average score of technique 1 among the eight groups of users is 9.67; much higher than that of technique 2, which is 8.43, and that of technique 3, which is 7.88. This

### 4.x Estado / inputs / features observables

**[Estado / inputs / features observables | extracto 1 | p.1]**

Bit rate selection technology of image processing based on artificial intelligence in MPEG-DASH adaptive streaming media Ping Yang *, Jinyi Qiao , Minxiu Chen School of Media and Design, Hangzhou Dianzi University, Hangzhou, 310018, China A R T I C L E I N F O Keywords: AI MPEG-DASH Streaming media product Bit rate selection technique PCA-GWO-BP A B S T R A C T Aiming at the bit rate selection problem of MPEG-DASH adaptive streaming media in image processing, a hybrid method combining multiple artificial intelligence algorithms is proposed. Firstly, kernel principal component analysis, Grey Wolf optimization algorithm and least squares support vector machine are integrated to construct an efficient hybrid algorithm model. This model aims to optimize the image processing effect in streaming media transmission, especially in the dynamic network environment. The experimental results show that the accuracy of the hybrid algorithm reaches 0.945 in the training process, and the absolute error is only 0.0005, which is significantly better than other comparison algorithms. Further empirical analysis shows that the accuracy of the proposed rate selection technique in image processing is as high as 92.3%, which is far higher than the existing technique. This research not only improves the image quality of streaming media transmission, but also greatly improves the user experience. The research provides a new perspective for image processing technology in the field of digital media, and is of great significance for promoting the innovation and development of streaming media technology. 1. Introduction In the digital era, streaming media technology has become a popular way of multimedia transmission, widely used in online video, audio live broadcast, distance education and many oth

**[Estado / inputs / features observables | extracto 2 | p.2]**

changes of network conditions to ensure smooth playback. This research provides a new bit rate selection strategy for the streaming media field, which effectively improves the efficiency and user experience of streaming media transmission. The paper mainly consists of four parts to discuss, the first part of the content is mainly to describe the BP algorithm, GWO algorithm and the related research on intelligent algorithms in the field of streaming media; the second part of the content is mainly to analyze the bit rate selection technology for MPEG-DASH adaptive streaming media products based on PCA-GWO-BP algorithm; the third part is mainly to compare and contrast the performance and research to propose a new bit rate selection strategy for streaming media products. performance comparison and the comparative analysis of the research proposed streaming media product bit rate selection techniques; the fourth part is mainly the summary of the whole paper. 2. Literature review As various optimization methods of BP algorithm are gradually developed, BP algorithm and its improved algorithms are applied in many fields. Lu’s team proposed a novel algorithm based on adaptive cloning genetic algorithm and BP algorithm to address the problem of low recognition accuracy of traditional intrusion detection system. The model is applied in simulation experiments, and the outcomes demonstrate that the detection accuracy exceeds the traditional intrusion detection system, and it has good global searchability (Lu et al., 2021). Safavi et al. introduces and compares the BP algorithm and radial basis function NN in order to make a better estimation of the minimum deviation of the nuclear boiling ratio, and the results of the comparison of the two networks show that the training of the radi

**[Estado / inputs / features observables | extracto 3 | p.3]**

combination of BP neural network and MPEG-DASH can greatly improve the intelligence and user experience of streaming media transmission. Therefore, this paper proposes a bit rate selection technology for streaming media products based on improved BP neural network, hoping that it can provide an efficient selection scheme and promote the user’s experience. In this selection technology, BP neural network is mainly composed of three modules: input layer, hidden layer and output layer. The constitutive model of BP neural network is shown in Fig. 1. The main module HL in the BP NN can be categorized according to the number of layers, divided into single HL and multi-HL. In the prediction network bandwidth mapping relationships are not complex, so the single HL BP NN with shorter training time can be used. In the BP NN, the output value net1 expression transmitted from the IL to the HL is shown in Equation (1). net1 = w1x + b1, h = g1(net1) (1) In Equation (1), x denotes the initial value of neuron; b1 denotes the intercept term, and the weight value of interlayer connection is denoted by w1. The result net2 expression transmitted from the HL to the OL is shown in Equation (2). net2 = ω2 + b2, y = g2(net2) (2) In Equation (2), b2 denotes the intercept term and ω2 denotes the weight value of the connection between the HL and the OL. The specific sigmoid function expression is shown in Equation (3). y ⌢= g2(net2) = g2 ( vTg1(net1) + b2 ) = g2 ( vTg1 ( wTx + b1 ) + b2 ) (3) In Equation (3), y ⌢is the NN output value. During the operation of the BP NN, errors are always generated, and the total error generated during the operation E(θ) is expressed in Equation (4). E(θ) = 1 2 ∑ 2 i=1 (yi −̂yi)2 (4) In Equation (4), y denotes the actual value. Although the BP algorithm has a bette

**[Estado / inputs / features observables | extracto 4 | p.5]**

position and speed of the GW population. Repeat initializing the GW position and velocity of the population until the stopping condition is reached. The GW position update formula in the GWO-BP algorithm incorporating PCA algorithm is shown in Equation (7). x(i, t + 1) = x(i, t) + Aʹ ∗D (7) In Equation (7), Aʹ is the control parameter, D is the position difference of the GW, and the GW velocity update formula is showcased in Equation (8). v(i, t + 1) = r ∗v(i, t) + C ∗P − x(i, t) (8) In Equation (8), C serves as the control parameter, r is the random number, and P serves as the position of the current optimal solution, respectively. The selection of the control parameters A and C has a great influence on the convergence speed and the quality of the solution of the algorithm, and the optimal values are usually determined experimentally and empirically. The GW fitness calculation formula is shown in Equation (9). fitness(i) = 1 (1 + error(i)) (9) In Equation (9), P is the training error of the BP algorithm. The GWOBP algorithm incorporating PCA algorithm is able to find the optimal solution of the optimization problem faster by combining PCA algorithm and GWO-BP algorithm, using the dimensionality reduction ability of PCA algorithm and the optimization ability of GWO-BP algorithm. Meanwhile, by flexibly adjusting the parameters, it can achieve better performance in the prediction problem. 3.2. Streaming media product bit rate selection technique based on PCAGWO-BP algorithm MPEG-DASH adaptive streaming product bitrate selection technology is a technology that dynamically adjusts the video bitrate based on the network environment, aiming to provide users with a smooth, highquality video experience (Khalaf et al., 2020). This technology utilizes the MPEG-DASH standard to ad

**[Estado / inputs / features observables | extracto 5 | p.6]**

media product; α and β are the adjustment coefficients, which can be set according to the actual situation. Finally, the bitrate selection strategy is continuously optimized through real-time monitoring and feedback mechanism. This process needs to be adjusted according to user feedback and network conditions to improve user experience and service quality. In the above process, the prediction of network bandwidth using the network bandwidth prediction model constructed based on PCAGWO-BP algorithm is the most important part of it, and the specific flow of this prediction model is shown in Fig. 5. Fig. 5 showcases the process of the network bandwidth prediction model based on the improved BP algorithm can be mainly divided into the following eight processes. First, historical data on network bandwidth is collected, including information on network traffic and bandwidth utilization. These data will be utilized as inputs to the model for training and predicting network bandwidth. After that, the collected raw data are preprocessed, including data cleaning, normalization and other operations to eliminate the effects of outliers and magnitude differences on the prediction model. The pre-processed data is then subjected to dimensionality reduction using the PCA algorithm to extract key features and remove noise. This reduces the dimensionality of the data, reduces computational complexity, and improves the generalization ability of the model. The fourth step is to construct a BP NN with a suitable number of HL nodes based on the features of the dimensionality reduced data. This network will be used to learn and predict the change law of network bandwidth. Then the GWO algorithm is applied to optimize the weights and thresholds of the BP NN. By simulating the hunting behavior

**[Estado / inputs / features observables | extracto 6 | p.7]**

curve of 0.857; it exceeds the GWO-BP algorithm’s 0.763, the SSA-BP algorithm’s 0.756, and the GWO-SVM algorithm’s 0.747. The above results illustrate that, in terms of the dimension of the ROC curve, the research proposed PCA-SWO-BP algorithm’s performance is better than the comparison algorithms. The training error data of the four algorithms during model training are compared and the outcomes are showcased in Fig. 8. Fig. 8 showcases that among the four algorithms, the PCA-GWO-BP algorithm has the most obvious downward trend of training error and reaches the desired accuracy at 566 iterations; the GWO-BP algorithm has a slightly slower downward trend of training error and reaches the desired accuracy at 855 iterations; and the SSA-BP algorithm has a relatively gentle downward trend of training error and reaches the desired accuracy at 955 iterations; The GWO-BP algorithm has the smoothest decline in training error and reaches the desired accuracy in 1032 iterations. This result indicates that the proposed PCA-GWO-BP algorithm performs better in training, has the fastest convergence speed and has better performance. Fig. 9 gives the comparison results of the absolute errors of the four algorithm models during the prediction process. From Fig. 9, the PCA-GWO-BP algorithm has the lowest overall level of absolute error, with an average absolute error value of 0.0005; which is below the GWO-BP algorithm’s 0.0012; the SSA-BP algorithm’s 0.0021; and the GWO-SVM algorithm’s 0.0057. From this result, it can be concluded that in terms of the absolute error dimension, the PCAGWO-BP algorithm’s overall performance is also better than the comparison algorithms. Comparing the above dimensions, it showcases that the overall prediction performance of the proposed PCA-GWO-BP algorith

**[Estado / inputs / features observables | extracto 7 | p.8]**

media products proposed in the study (Technology 1) and the code rate selection technology for streaming media products based on SSA-BP algorithm (Technology 2) and the code rate selection technology for streaming media products based on GWO-BP algorithm (Technology 3) are compared and experimented, and the accuracy, real-time, and impact on the user experience of the code rate selection are used as the comparison indexes. The accuracy and real-time comparison results of the three techniques in different datasets are shown in Fig. 10. From Fig. 10(a), the selection accuracy of technique 1 in the video dataset is 92.3%, which is significantly higher than that of technique 2 (80.1%) and that of technique 3 (79.5%); moreover, it can be found that the selection accuracy of technique 1 in the network state dataset is 91.8%, which is significantly higher than that of technique 2 (78.3%) and that of technique 3 (79.9%). From Fig. 10(b), it can be obtained that the response time of technology 1 in both data sets is less than 5 s, which is much lower than that of technology 2 and technology 3. Therefore, from the above results, it can be concluded that the accuracy and realtime performance of the proposed streaming media product bit rate selection technology is better than the comparison technology. For comparing the actual application effect of the three technologies, the study selected a number of different groups of users to score their experience and statistics, the scoring statistics are shown in Fig. 11. The full score is 10 points, the higher the score, the higher the recognition. Fig. 11showcases that the average score of technique 1 among the eight groups of users is 9.67; much higher than that of technique 2, which is 8.43, and that of technique 3, which is 7.88. This

### 4.x Acción / decisión ABR

**[Acción / decisión ABR | extracto 1 | p.1]**

Bit rate selection technology of image processing based on artificial intelligence in MPEG-DASH adaptive streaming media Ping Yang *, Jinyi Qiao , Minxiu Chen School of Media and Design, Hangzhou Dianzi University, Hangzhou, 310018, China A R T I C L E I N F O Keywords: AI MPEG-DASH Streaming media product Bit rate selection technique PCA-GWO-BP A B S T R A C T Aiming at the bit rate selection problem of MPEG-DASH adaptive streaming media in image processing, a hybrid method combining multiple artificial intelligence algorithms is proposed. Firstly, kernel principal component analysis, Grey Wolf optimization algorithm and least squares support vector machine are integrated to construct an efficient hybrid algorithm model. This model aims to optimize the image processing effect in streaming media transmission, especially in the dynamic network environment. The experimental results show that the accuracy of the hybrid algorithm reaches 0.945 in the training process, and the absolute error is only 0.0005, which is significantly better than other comparison algorithms. Further empirical analysis shows that the accuracy of the proposed rate selection technique in image processing is as high as 92.3%, which is far higher than the existing technique. This research not only improves the image quality of streaming media transmission, but also greatly improves the user experience. The research provides a new perspective for image processing technology in the field of digital media, and is of great significance for promoting the innovation and development of streaming media technology. 1. Introduction In the digital era, streaming media technology has become a popular way of multimedia transmission, widely used in online video, audio live broadcast, distance education and many oth

**[Acción / decisión ABR | extracto 2 | p.2]**

changes of network conditions to ensure smooth playback. This research provides a new bit rate selection strategy for the streaming media field, which effectively improves the efficiency and user experience of streaming media transmission. The paper mainly consists of four parts to discuss, the first part of the content is mainly to describe the BP algorithm, GWO algorithm and the related research on intelligent algorithms in the field of streaming media; the second part of the content is mainly to analyze the bit rate selection technology for MPEG-DASH adaptive streaming media products based on PCA-GWO-BP algorithm; the third part is mainly to compare and contrast the performance and research to propose a new bit rate selection strategy for streaming media products. performance comparison and the comparative analysis of the research proposed streaming media product bit rate selection techniques; the fourth part is mainly the summary of the whole paper. 2. Literature review As various optimization methods of BP algorithm are gradually developed, BP algorithm and its improved algorithms are applied in many fields. Lu’s team proposed a novel algorithm based on adaptive cloning genetic algorithm and BP algorithm to address the problem of low recognition accuracy of traditional intrusion detection system. The model is applied in simulation experiments, and the outcomes demonstrate that the detection accuracy exceeds the traditional intrusion detection system, and it has good global searchability (Lu et al., 2021). Safavi et al. introduces and compares the BP algorithm and radial basis function NN in order to make a better estimation of the minimum deviation of the nuclear boiling ratio, and the results of the comparison of the two networks show that the training of the radi

**[Acción / decisión ABR | extracto 3 | p.3]**

combination of BP neural network and MPEG-DASH can greatly improve the intelligence and user experience of streaming media transmission. Therefore, this paper proposes a bit rate selection technology for streaming media products based on improved BP neural network, hoping that it can provide an efficient selection scheme and promote the user’s experience. In this selection technology, BP neural network is mainly composed of three modules: input layer, hidden layer and output layer. The constitutive model of BP neural network is shown in Fig. 1. The main module HL in the BP NN can be categorized according to the number of layers, divided into single HL and multi-HL. In the prediction network bandwidth mapping relationships are not complex, so the single HL BP NN with shorter training time can be used. In the BP NN, the output value net1 expression transmitted from the IL to the HL is shown in Equation (1). net1 = w1x + b1, h = g1(net1) (1) In Equation (1), x denotes the initial value of neuron; b1 denotes the intercept term, and the weight value of interlayer connection is denoted by w1. The result net2 expression transmitted from the HL to the OL is shown in Equation (2). net2 = ω2 + b2, y = g2(net2) (2) In Equation (2), b2 denotes the intercept term and ω2 denotes the weight value of the connection between the HL and the OL. The specific sigmoid function expression is shown in Equation (3). y ⌢= g2(net2) = g2 ( vTg1(net1) + b2 ) = g2 ( vTg1 ( wTx + b1 ) + b2 ) (3) In Equation (3), y ⌢is the NN output value. During the operation of the BP NN, errors are always generated, and the total error generated during the operation E(θ) is expressed in Equation (4). E(θ) = 1 2 ∑ 2 i=1 (yi −̂yi)2 (4) In Equation (4), y denotes the actual value. Although the BP algorithm has a bette

**[Acción / decisión ABR | extracto 4 | p.4]**

F = 1 A ∑ A s=1 ̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ∑ A k=1 ( y s k −o s k )2 √ √ √ √ (6) In Equation (6), A represents the number of grey wolves. Then the three GWs with the highest values in the wolf population are selected and recorded as, δ . The parameters r→ 1 , r→ 2 , a→in the GWO are updated to determine the location of the new wolf individuals and utilized as the initial parameters of the BP NN. Based on the updated fitness value of the wolf individuals, the newest, δ are re-informed. Finally, check whether the quantity of iterations set by the algorithm is reached. If it is not done, the parameters r→ 1 , r→ 2 , a→in the GWO are re-updated, and if it is done, the BP NN is given the optimal initial parameters. PCA is a preprocessing method that transforms the original multiple variables into several with comprehensive indicators (Diab et al., 2022b). For better enhancing the efficiency and prediction accuracy of the GWO-BP algorithm, this study adopts PCA to downsize the evaluation index data and constructs a GWO-BP prediction model based on PCA.The flowchart of the PCA-GWO-BP model is shown in Fig. 3. As can be seen from Fig. 3, the specific steps for solving the GWO-BP algorithm incorporating the PCA algorithm are as follows: firstly, determine the position and speed of the GWs of the initialized population, and count the fitness of each GW. Perform the advantage and disadvantage ranking of GWs, and update the position and speed of GWs. On the grounds of the updated GW positions, the positions are downscaled using the PCA algorithm. Based on the dimensionality reduction, train the network using the BP algorithm and calculate the fitness of the network. According to the size of the fitness, update the Fig. 3. PCA-GWO-BP model flow. Fig. 4. Bit rate selection

**[Acción / decisión ABR | extracto 5 | p.5]**

position and speed of the GW population. Repeat initializing the GW position and velocity of the population until the stopping condition is reached. The GW position update formula in the GWO-BP algorithm incorporating PCA algorithm is shown in Equation (7). x(i, t + 1) = x(i, t) + Aʹ ∗D (7) In Equation (7), Aʹ is the control parameter, D is the position difference of the GW, and the GW velocity update formula is showcased in Equation (8). v(i, t + 1) = r ∗v(i, t) + C ∗P − x(i, t) (8) In Equation (8), C serves as the control parameter, r is the random number, and P serves as the position of the current optimal solution, respectively. The selection of the control parameters A and C has a great influence on the convergence speed and the quality of the solution of the algorithm, and the optimal values are usually determined experimentally and empirically. The GW fitness calculation formula is shown in Equation (9). fitness(i) = 1 (1 + error(i)) (9) In Equation (9), P is the training error of the BP algorithm. The GWOBP algorithm incorporating PCA algorithm is able to find the optimal solution of the optimization problem faster by combining PCA algorithm and GWO-BP algorithm, using the dimensionality reduction ability of PCA algorithm and the optimization ability of GWO-BP algorithm. Meanwhile, by flexibly adjusting the parameters, it can achieve better performance in the prediction problem. 3.2. Streaming media product bit rate selection technique based on PCAGWO-BP algorithm MPEG-DASH adaptive streaming product bitrate selection technology is a technology that dynamically adjusts the video bitrate based on the network environment, aiming to provide users with a smooth, highquality video experience (Khalaf et al., 2020). This technology utilizes the MPEG-DASH standard to ad

**[Acción / decisión ABR | extracto 6 | p.6]**

media product; α and β are the adjustment coefficients, which can be set according to the actual situation. Finally, the bitrate selection strategy is continuously optimized through real-time monitoring and feedback mechanism. This process needs to be adjusted according to user feedback and network conditions to improve user experience and service quality. In the above process, the prediction of network bandwidth using the network bandwidth prediction model constructed based on PCAGWO-BP algorithm is the most important part of it, and the specific flow of this prediction model is shown in Fig. 5. Fig. 5 showcases the process of the network bandwidth prediction model based on the improved BP algorithm can be mainly divided into the following eight processes. First, historical data on network bandwidth is collected, including information on network traffic and bandwidth utilization. These data will be utilized as inputs to the model for training and predicting network bandwidth. After that, the collected raw data are preprocessed, including data cleaning, normalization and other operations to eliminate the effects of outliers and magnitude differences on the prediction model. The pre-processed data is then subjected to dimensionality reduction using the PCA algorithm to extract key features and remove noise. This reduces the dimensionality of the data, reduces computational complexity, and improves the generalization ability of the model. The fourth step is to construct a BP NN with a suitable number of HL nodes based on the features of the dimensionality reduced data. This network will be used to learn and predict the change law of network bandwidth. Then the GWO algorithm is applied to optimize the weights and thresholds of the BP NN. By simulating the hunting behavior

**[Acción / decisión ABR | extracto 7 | p.7]**

curve of 0.857; it exceeds the GWO-BP algorithm’s 0.763, the SSA-BP algorithm’s 0.756, and the GWO-SVM algorithm’s 0.747. The above results illustrate that, in terms of the dimension of the ROC curve, the research proposed PCA-SWO-BP algorithm’s performance is better than the comparison algorithms. The training error data of the four algorithms during model training are compared and the outcomes are showcased in Fig. 8. Fig. 8 showcases that among the four algorithms, the PCA-GWO-BP algorithm has the most obvious downward trend of training error and reaches the desired accuracy at 566 iterations; the GWO-BP algorithm has a slightly slower downward trend of training error and reaches the desired accuracy at 855 iterations; and the SSA-BP algorithm has a relatively gentle downward trend of training error and reaches the desired accuracy at 955 iterations; The GWO-BP algorithm has the smoothest decline in training error and reaches the desired accuracy in 1032 iterations. This result indicates that the proposed PCA-GWO-BP algorithm performs better in training, has the fastest convergence speed and has better performance. Fig. 9 gives the comparison results of the absolute errors of the four algorithm models during the prediction process. From Fig. 9, the PCA-GWO-BP algorithm has the lowest overall level of absolute error, with an average absolute error value of 0.0005; which is below the GWO-BP algorithm’s 0.0012; the SSA-BP algorithm’s 0.0021; and the GWO-SVM algorithm’s 0.0057. From this result, it can be concluded that in terms of the absolute error dimension, the PCAGWO-BP algorithm’s overall performance is also better than the comparison algorithms. Comparing the above dimensions, it showcases that the overall prediction performance of the proposed PCA-GWO-BP algorith

**[Acción / decisión ABR | extracto 8 | p.8]**

media products proposed in the study (Technology 1) and the code rate selection technology for streaming media products based on SSA-BP algorithm (Technology 2) and the code rate selection technology for streaming media products based on GWO-BP algorithm (Technology 3) are compared and experimented, and the accuracy, real-time, and impact on the user experience of the code rate selection are used as the comparison indexes. The accuracy and real-time comparison results of the three techniques in different datasets are shown in Fig. 10. From Fig. 10(a), the selection accuracy of technique 1 in the video dataset is 92.3%, which is significantly higher than that of technique 2 (80.1%) and that of technique 3 (79.5%); moreover, it can be found that the selection accuracy of technique 1 in the network state dataset is 91.8%, which is significantly higher than that of technique 2 (78.3%) and that of technique 3 (79.9%). From Fig. 10(b), it can be obtained that the response time of technology 1 in both data sets is less than 5 s, which is much lower than that of technology 2 and technology 3. Therefore, from the above results, it can be concluded that the accuracy and realtime performance of the proposed streaming media product bit rate selection technology is better than the comparison technology. For comparing the actual application effect of the three technologies, the study selected a number of different groups of users to score their experience and statistics, the scoring statistics are shown in Fig. 11. The full score is 10 points, the higher the score, the higher the recognition. Fig. 11showcases that the average score of technique 1 among the eight groups of users is 9.67; much higher than that of technique 2, which is 8.43, and that of technique 3, which is 7.88. This

### 4.x Reward / QoE / función objetivo

**[Reward / QoE / función objetivo | extracto 1 | p.1]**

Bit rate selection technology of image processing based on artificial intelligence in MPEG-DASH adaptive streaming media Ping Yang *, Jinyi Qiao , Minxiu Chen School of Media and Design, Hangzhou Dianzi University, Hangzhou, 310018, China A R T I C L E I N F O Keywords: AI MPEG-DASH Streaming media product Bit rate selection technique PCA-GWO-BP A B S T R A C T Aiming at the bit rate selection problem of MPEG-DASH adaptive streaming media in image processing, a hybrid method combining multiple artificial intelligence algorithms is proposed. Firstly, kernel principal component analysis, Grey Wolf optimization algorithm and least squares support vector machine are integrated to construct an efficient hybrid algorithm model. This model aims to optimize the image processing effect in streaming media transmission, especially in the dynamic network environment. The experimental results show that the accuracy of the hybrid algorithm reaches 0.945 in the training process, and the absolute error is only 0.0005, which is significantly better than other comparison algorithms. Further empirical analysis shows that the accuracy of the proposed rate selection technique in image processing is as high as 92.3%, which is far higher than the existing technique. This research not only improves the image quality of streaming media transmission, but also greatly improves the user experience. The research provides a new perspective for image processing technology in the field of digital media, and is of great significance for promoting the innovation and development of streaming media technology. 1. Introduction In the digital era, streaming media technology has become a popular way of multimedia transmission, widely used in online video, audio live broadcast, distance education and many oth

**[Reward / QoE / función objetivo | extracto 2 | p.2]**

changes of network conditions to ensure smooth playback. This research provides a new bit rate selection strategy for the streaming media field, which effectively improves the efficiency and user experience of streaming media transmission. The paper mainly consists of four parts to discuss, the first part of the content is mainly to describe the BP algorithm, GWO algorithm and the related research on intelligent algorithms in the field of streaming media; the second part of the content is mainly to analyze the bit rate selection technology for MPEG-DASH adaptive streaming media products based on PCA-GWO-BP algorithm; the third part is mainly to compare and contrast the performance and research to propose a new bit rate selection strategy for streaming media products. performance comparison and the comparative analysis of the research proposed streaming media product bit rate selection techniques; the fourth part is mainly the summary of the whole paper. 2. Literature review As various optimization methods of BP algorithm are gradually developed, BP algorithm and its improved algorithms are applied in many fields. Lu’s team proposed a novel algorithm based on adaptive cloning genetic algorithm and BP algorithm to address the problem of low recognition accuracy of traditional intrusion detection system. The model is applied in simulation experiments, and the outcomes demonstrate that the detection accuracy exceeds the traditional intrusion detection system, and it has good global searchability (Lu et al., 2021). Safavi et al. introduces and compares the BP algorithm and radial basis function NN in order to make a better estimation of the minimum deviation of the nuclear boiling ratio, and the results of the comparison of the two networks show that the training of the radi

**[Reward / QoE / función objetivo | extracto 3 | p.5]**

position and speed of the GW population. Repeat initializing the GW position and velocity of the population until the stopping condition is reached. The GW position update formula in the GWO-BP algorithm incorporating PCA algorithm is shown in Equation (7). x(i, t + 1) = x(i, t) + Aʹ ∗D (7) In Equation (7), Aʹ is the control parameter, D is the position difference of the GW, and the GW velocity update formula is showcased in Equation (8). v(i, t + 1) = r ∗v(i, t) + C ∗P − x(i, t) (8) In Equation (8), C serves as the control parameter, r is the random number, and P serves as the position of the current optimal solution, respectively. The selection of the control parameters A and C has a great influence on the convergence speed and the quality of the solution of the algorithm, and the optimal values are usually determined experimentally and empirically. The GW fitness calculation formula is shown in Equation (9). fitness(i) = 1 (1 + error(i)) (9) In Equation (9), P is the training error of the BP algorithm. The GWOBP algorithm incorporating PCA algorithm is able to find the optimal solution of the optimization problem faster by combining PCA algorithm and GWO-BP algorithm, using the dimensionality reduction ability of PCA algorithm and the optimization ability of GWO-BP algorithm. Meanwhile, by flexibly adjusting the parameters, it can achieve better performance in the prediction problem. 3.2. Streaming media product bit rate selection technique based on PCAGWO-BP algorithm MPEG-DASH adaptive streaming product bitrate selection technology is a technology that dynamically adjusts the video bitrate based on the network environment, aiming to provide users with a smooth, highquality video experience (Khalaf et al., 2020). This technology utilizes the MPEG-DASH standard to ad

**[Reward / QoE / función objetivo | extracto 4 | p.7]**

curve of 0.857; it exceeds the GWO-BP algorithm’s 0.763, the SSA-BP algorithm’s 0.756, and the GWO-SVM algorithm’s 0.747. The above results illustrate that, in terms of the dimension of the ROC curve, the research proposed PCA-SWO-BP algorithm’s performance is better than the comparison algorithms. The training error data of the four algorithms during model training are compared and the outcomes are showcased in Fig. 8. Fig. 8 showcases that among the four algorithms, the PCA-GWO-BP algorithm has the most obvious downward trend of training error and reaches the desired accuracy at 566 iterations; the GWO-BP algorithm has a slightly slower downward trend of training error and reaches the desired accuracy at 855 iterations; and the SSA-BP algorithm has a relatively gentle downward trend of training error and reaches the desired accuracy at 955 iterations; The GWO-BP algorithm has the smoothest decline in training error and reaches the desired accuracy in 1032 iterations. This result indicates that the proposed PCA-GWO-BP algorithm performs better in training, has the fastest convergence speed and has better performance. Fig. 9 gives the comparison results of the absolute errors of the four algorithm models during the prediction process. From Fig. 9, the PCA-GWO-BP algorithm has the lowest overall level of absolute error, with an average absolute error value of 0.0005; which is below the GWO-BP algorithm’s 0.0012; the SSA-BP algorithm’s 0.0021; and the GWO-SVM algorithm’s 0.0057. From this result, it can be concluded that in terms of the absolute error dimension, the PCAGWO-BP algorithm’s overall performance is also better than the comparison algorithms. Comparing the above dimensions, it showcases that the overall prediction performance of the proposed PCA-GWO-BP algorith

**[Reward / QoE / función objetivo | extracto 5 | p.8]**

media products proposed in the study (Technology 1) and the code rate selection technology for streaming media products based on SSA-BP algorithm (Technology 2) and the code rate selection technology for streaming media products based on GWO-BP algorithm (Technology 3) are compared and experimented, and the accuracy, real-time, and impact on the user experience of the code rate selection are used as the comparison indexes. The accuracy and real-time comparison results of the three techniques in different datasets are shown in Fig. 10. From Fig. 10(a), the selection accuracy of technique 1 in the video dataset is 92.3%, which is significantly higher than that of technique 2 (80.1%) and that of technique 3 (79.5%); moreover, it can be found that the selection accuracy of technique 1 in the network state dataset is 91.8%, which is significantly higher than that of technique 2 (78.3%) and that of technique 3 (79.9%). From Fig. 10(b), it can be obtained that the response time of technology 1 in both data sets is less than 5 s, which is much lower than that of technology 2 and technology 3. Therefore, from the above results, it can be concluded that the accuracy and realtime performance of the proposed streaming media product bit rate selection technology is better than the comparison technology. For comparing the actual application effect of the three technologies, the study selected a number of different groups of users to score their experience and statistics, the scoring statistics are shown in Fig. 11. The full score is 10 points, the higher the score, the higher the recognition. Fig. 11showcases that the average score of technique 1 among the eight groups of users is 9.67; much higher than that of technique 2, which is 8.43, and that of technique 3, which is 7.88. This

### 4.x Entrenamiento / learning procedure

**[Entrenamiento / learning procedure | extracto 1 | p.1]**

Bit rate selection technology of image processing based on artificial intelligence in MPEG-DASH adaptive streaming media Ping Yang *, Jinyi Qiao , Minxiu Chen School of Media and Design, Hangzhou Dianzi University, Hangzhou, 310018, China A R T I C L E I N F O Keywords: AI MPEG-DASH Streaming media product Bit rate selection technique PCA-GWO-BP A B S T R A C T Aiming at the bit rate selection problem of MPEG-DASH adaptive streaming media in image processing, a hybrid method combining multiple artificial intelligence algorithms is proposed. Firstly, kernel principal component analysis, Grey Wolf optimization algorithm and least squares support vector machine are integrated to construct an efficient hybrid algorithm model. This model aims to optimize the image processing effect in streaming media transmission, especially in the dynamic network environment. The experimental results show that the accuracy of the hybrid algorithm reaches 0.945 in the training process, and the absolute error is only 0.0005, which is significantly better than other comparison algorithms. Further empirical analysis shows that the accuracy of the proposed rate selection technique in image processing is as high as 92.3%, which is far higher than the existing technique. This research not only improves the image quality of streaming media transmission, but also greatly improves the user experience. The research provides a new perspective for image processing technology in the field of digital media, and is of great significance for promoting the innovation and development of streaming media technology. 1. Introduction In the digital era, streaming media technology has become a popular way of multimedia transmission, widely used in online video, audio live broadcast, distance education and many oth

**[Entrenamiento / learning procedure | extracto 2 | p.2]**

changes of network conditions to ensure smooth playback. This research provides a new bit rate selection strategy for the streaming media field, which effectively improves the efficiency and user experience of streaming media transmission. The paper mainly consists of four parts to discuss, the first part of the content is mainly to describe the BP algorithm, GWO algorithm and the related research on intelligent algorithms in the field of streaming media; the second part of the content is mainly to analyze the bit rate selection technology for MPEG-DASH adaptive streaming media products based on PCA-GWO-BP algorithm; the third part is mainly to compare and contrast the performance and research to propose a new bit rate selection strategy for streaming media products. performance comparison and the comparative analysis of the research proposed streaming media product bit rate selection techniques; the fourth part is mainly the summary of the whole paper. 2. Literature review As various optimization methods of BP algorithm are gradually developed, BP algorithm and its improved algorithms are applied in many fields. Lu’s team proposed a novel algorithm based on adaptive cloning genetic algorithm and BP algorithm to address the problem of low recognition accuracy of traditional intrusion detection system. The model is applied in simulation experiments, and the outcomes demonstrate that the detection accuracy exceeds the traditional intrusion detection system, and it has good global searchability (Lu et al., 2021). Safavi et al. introduces and compares the BP algorithm and radial basis function NN in order to make a better estimation of the minimum deviation of the nuclear boiling ratio, and the results of the comparison of the two networks show that the training of the radi

**[Entrenamiento / learning procedure | extracto 3 | p.3]**

combination of BP neural network and MPEG-DASH can greatly improve the intelligence and user experience of streaming media transmission. Therefore, this paper proposes a bit rate selection technology for streaming media products based on improved BP neural network, hoping that it can provide an efficient selection scheme and promote the user’s experience. In this selection technology, BP neural network is mainly composed of three modules: input layer, hidden layer and output layer. The constitutive model of BP neural network is shown in Fig. 1. The main module HL in the BP NN can be categorized according to the number of layers, divided into single HL and multi-HL. In the prediction network bandwidth mapping relationships are not complex, so the single HL BP NN with shorter training time can be used. In the BP NN, the output value net1 expression transmitted from the IL to the HL is shown in Equation (1). net1 = w1x + b1, h = g1(net1) (1) In Equation (1), x denotes the initial value of neuron; b1 denotes the intercept term, and the weight value of interlayer connection is denoted by w1. The result net2 expression transmitted from the HL to the OL is shown in Equation (2). net2 = ω2 + b2, y = g2(net2) (2) In Equation (2), b2 denotes the intercept term and ω2 denotes the weight value of the connection between the HL and the OL. The specific sigmoid function expression is shown in Equation (3). y ⌢= g2(net2) = g2 ( vTg1(net1) + b2 ) = g2 ( vTg1 ( wTx + b1 ) + b2 ) (3) In Equation (3), y ⌢is the NN output value. During the operation of the BP NN, errors are always generated, and the total error generated during the operation E(θ) is expressed in Equation (4). E(θ) = 1 2 ∑ 2 i=1 (yi −̂yi)2 (4) In Equation (4), y denotes the actual value. Although the BP algorithm has a bette

**[Entrenamiento / learning procedure | extracto 4 | p.4]**

F = 1 A ∑ A s=1 ̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ∑ A k=1 ( y s k −o s k )2 √ √ √ √ (6) In Equation (6), A represents the number of grey wolves. Then the three GWs with the highest values in the wolf population are selected and recorded as, δ . The parameters r→ 1 , r→ 2 , a→in the GWO are updated to determine the location of the new wolf individuals and utilized as the initial parameters of the BP NN. Based on the updated fitness value of the wolf individuals, the newest, δ are re-informed. Finally, check whether the quantity of iterations set by the algorithm is reached. If it is not done, the parameters r→ 1 , r→ 2 , a→in the GWO are re-updated, and if it is done, the BP NN is given the optimal initial parameters. PCA is a preprocessing method that transforms the original multiple variables into several with comprehensive indicators (Diab et al., 2022b). For better enhancing the efficiency and prediction accuracy of the GWO-BP algorithm, this study adopts PCA to downsize the evaluation index data and constructs a GWO-BP prediction model based on PCA.The flowchart of the PCA-GWO-BP model is shown in Fig. 3. As can be seen from Fig. 3, the specific steps for solving the GWO-BP algorithm incorporating the PCA algorithm are as follows: firstly, determine the position and speed of the GWs of the initialized population, and count the fitness of each GW. Perform the advantage and disadvantage ranking of GWs, and update the position and speed of GWs. On the grounds of the updated GW positions, the positions are downscaled using the PCA algorithm. Based on the dimensionality reduction, train the network using the BP algorithm and calculate the fitness of the network. According to the size of the fitness, update the Fig. 3. PCA-GWO-BP model flow. Fig. 4. Bit rate selection

**[Entrenamiento / learning procedure | extracto 5 | p.5]**

position and speed of the GW population. Repeat initializing the GW position and velocity of the population until the stopping condition is reached. The GW position update formula in the GWO-BP algorithm incorporating PCA algorithm is shown in Equation (7). x(i, t + 1) = x(i, t) + Aʹ ∗D (7) In Equation (7), Aʹ is the control parameter, D is the position difference of the GW, and the GW velocity update formula is showcased in Equation (8). v(i, t + 1) = r ∗v(i, t) + C ∗P − x(i, t) (8) In Equation (8), C serves as the control parameter, r is the random number, and P serves as the position of the current optimal solution, respectively. The selection of the control parameters A and C has a great influence on the convergence speed and the quality of the solution of the algorithm, and the optimal values are usually determined experimentally and empirically. The GW fitness calculation formula is shown in Equation (9). fitness(i) = 1 (1 + error(i)) (9) In Equation (9), P is the training error of the BP algorithm. The GWOBP algorithm incorporating PCA algorithm is able to find the optimal solution of the optimization problem faster by combining PCA algorithm and GWO-BP algorithm, using the dimensionality reduction ability of PCA algorithm and the optimization ability of GWO-BP algorithm. Meanwhile, by flexibly adjusting the parameters, it can achieve better performance in the prediction problem. 3.2. Streaming media product bit rate selection technique based on PCAGWO-BP algorithm MPEG-DASH adaptive streaming product bitrate selection technology is a technology that dynamically adjusts the video bitrate based on the network environment, aiming to provide users with a smooth, highquality video experience (Khalaf et al., 2020). This technology utilizes the MPEG-DASH standard to ad

**[Entrenamiento / learning procedure | extracto 6 | p.6]**

media product; α and β are the adjustment coefficients, which can be set according to the actual situation. Finally, the bitrate selection strategy is continuously optimized through real-time monitoring and feedback mechanism. This process needs to be adjusted according to user feedback and network conditions to improve user experience and service quality. In the above process, the prediction of network bandwidth using the network bandwidth prediction model constructed based on PCAGWO-BP algorithm is the most important part of it, and the specific flow of this prediction model is shown in Fig. 5. Fig. 5 showcases the process of the network bandwidth prediction model based on the improved BP algorithm can be mainly divided into the following eight processes. First, historical data on network bandwidth is collected, including information on network traffic and bandwidth utilization. These data will be utilized as inputs to the model for training and predicting network bandwidth. After that, the collected raw data are preprocessed, including data cleaning, normalization and other operations to eliminate the effects of outliers and magnitude differences on the prediction model. The pre-processed data is then subjected to dimensionality reduction using the PCA algorithm to extract key features and remove noise. This reduces the dimensionality of the data, reduces computational complexity, and improves the generalization ability of the model. The fourth step is to construct a BP NN with a suitable number of HL nodes based on the features of the dimensionality reduced data. This network will be used to learn and predict the change law of network bandwidth. Then the GWO algorithm is applied to optimize the weights and thresholds of the BP NN. By simulating the hunting behavior

**[Entrenamiento / learning procedure | extracto 7 | p.7]**

curve of 0.857; it exceeds the GWO-BP algorithm’s 0.763, the SSA-BP algorithm’s 0.756, and the GWO-SVM algorithm’s 0.747. The above results illustrate that, in terms of the dimension of the ROC curve, the research proposed PCA-SWO-BP algorithm’s performance is better than the comparison algorithms. The training error data of the four algorithms during model training are compared and the outcomes are showcased in Fig. 8. Fig. 8 showcases that among the four algorithms, the PCA-GWO-BP algorithm has the most obvious downward trend of training error and reaches the desired accuracy at 566 iterations; the GWO-BP algorithm has a slightly slower downward trend of training error and reaches the desired accuracy at 855 iterations; and the SSA-BP algorithm has a relatively gentle downward trend of training error and reaches the desired accuracy at 955 iterations; The GWO-BP algorithm has the smoothest decline in training error and reaches the desired accuracy in 1032 iterations. This result indicates that the proposed PCA-GWO-BP algorithm performs better in training, has the fastest convergence speed and has better performance. Fig. 9 gives the comparison results of the absolute errors of the four algorithm models during the prediction process. From Fig. 9, the PCA-GWO-BP algorithm has the lowest overall level of absolute error, with an average absolute error value of 0.0005; which is below the GWO-BP algorithm’s 0.0012; the SSA-BP algorithm’s 0.0021; and the GWO-SVM algorithm’s 0.0057. From this result, it can be concluded that in terms of the absolute error dimension, the PCAGWO-BP algorithm’s overall performance is also better than the comparison algorithms. Comparing the above dimensions, it showcases that the overall prediction performance of the proposed PCA-GWO-BP algorith

**[Entrenamiento / learning procedure | extracto 8 | p.8]**

media products proposed in the study (Technology 1) and the code rate selection technology for streaming media products based on SSA-BP algorithm (Technology 2) and the code rate selection technology for streaming media products based on GWO-BP algorithm (Technology 3) are compared and experimented, and the accuracy, real-time, and impact on the user experience of the code rate selection are used as the comparison indexes. The accuracy and real-time comparison results of the three techniques in different datasets are shown in Fig. 10. From Fig. 10(a), the selection accuracy of technique 1 in the video dataset is 92.3%, which is significantly higher than that of technique 2 (80.1%) and that of technique 3 (79.5%); moreover, it can be found that the selection accuracy of technique 1 in the network state dataset is 91.8%, which is significantly higher than that of technique 2 (78.3%) and that of technique 3 (79.9%). From Fig. 10(b), it can be obtained that the response time of technology 1 in both data sets is less than 5 s, which is much lower than that of technology 2 and technology 3. Therefore, from the above results, it can be concluded that the accuracy and realtime performance of the proposed streaming media product bit rate selection technology is better than the comparison technology. For comparing the actual application effect of the three technologies, the study selected a number of different groups of users to score their experience and statistics, the scoring statistics are shown in Fig. 11. The full score is 10 points, the higher the score, the higher the recognition. Fig. 11showcases that the average score of technique 1 among the eight groups of users is 9.67; much higher than that of technique 2, which is 8.43, and that of technique 3, which is 7.88. This

### 4.x Datos / trazas / datasets / contenidos

**[Datos / trazas / datasets / contenidos | extracto 1 | p.1]**

Bit rate selection technology of image processing based on artificial intelligence in MPEG-DASH adaptive streaming media Ping Yang *, Jinyi Qiao , Minxiu Chen School of Media and Design, Hangzhou Dianzi University, Hangzhou, 310018, China A R T I C L E I N F O Keywords: AI MPEG-DASH Streaming media product Bit rate selection technique PCA-GWO-BP A B S T R A C T Aiming at the bit rate selection problem of MPEG-DASH adaptive streaming media in image processing, a hybrid method combining multiple artificial intelligence algorithms is proposed. Firstly, kernel principal component analysis, Grey Wolf optimization algorithm and least squares support vector machine are integrated to construct an efficient hybrid algorithm model. This model aims to optimize the image processing effect in streaming media transmission, especially in the dynamic network environment. The experimental results show that the accuracy of the hybrid algorithm reaches 0.945 in the training process, and the absolute error is only 0.0005, which is significantly better than other comparison algorithms. Further empirical analysis shows that the accuracy of the proposed rate selection technique in image processing is as high as 92.3%, which is far higher than the existing technique. This research not only improves the image quality of streaming media transmission, but also greatly improves the user experience. The research provides a new perspective for image processing technology in the field of digital media, and is of great significance for promoting the innovation and development of streaming media technology. 1. Introduction In the digital era, streaming media technology has become a popular way of multimedia transmission, widely used in online video, audio live broadcast, distance education and many oth

**[Datos / trazas / datasets / contenidos | extracto 2 | p.2]**

changes of network conditions to ensure smooth playback. This research provides a new bit rate selection strategy for the streaming media field, which effectively improves the efficiency and user experience of streaming media transmission. The paper mainly consists of four parts to discuss, the first part of the content is mainly to describe the BP algorithm, GWO algorithm and the related research on intelligent algorithms in the field of streaming media; the second part of the content is mainly to analyze the bit rate selection technology for MPEG-DASH adaptive streaming media products based on PCA-GWO-BP algorithm; the third part is mainly to compare and contrast the performance and research to propose a new bit rate selection strategy for streaming media products. performance comparison and the comparative analysis of the research proposed streaming media product bit rate selection techniques; the fourth part is mainly the summary of the whole paper. 2. Literature review As various optimization methods of BP algorithm are gradually developed, BP algorithm and its improved algorithms are applied in many fields. Lu’s team proposed a novel algorithm based on adaptive cloning genetic algorithm and BP algorithm to address the problem of low recognition accuracy of traditional intrusion detection system. The model is applied in simulation experiments, and the outcomes demonstrate that the detection accuracy exceeds the traditional intrusion detection system, and it has good global searchability (Lu et al., 2021). Safavi et al. introduces and compares the BP algorithm and radial basis function NN in order to make a better estimation of the minimum deviation of the nuclear boiling ratio, and the results of the comparison of the two networks show that the training of the radi

**[Datos / trazas / datasets / contenidos | extracto 3 | p.5]**

position and speed of the GW population. Repeat initializing the GW position and velocity of the population until the stopping condition is reached. The GW position update formula in the GWO-BP algorithm incorporating PCA algorithm is shown in Equation (7). x(i, t + 1) = x(i, t) + Aʹ ∗D (7) In Equation (7), Aʹ is the control parameter, D is the position difference of the GW, and the GW velocity update formula is showcased in Equation (8). v(i, t + 1) = r ∗v(i, t) + C ∗P − x(i, t) (8) In Equation (8), C serves as the control parameter, r is the random number, and P serves as the position of the current optimal solution, respectively. The selection of the control parameters A and C has a great influence on the convergence speed and the quality of the solution of the algorithm, and the optimal values are usually determined experimentally and empirically. The GW fitness calculation formula is shown in Equation (9). fitness(i) = 1 (1 + error(i)) (9) In Equation (9), P is the training error of the BP algorithm. The GWOBP algorithm incorporating PCA algorithm is able to find the optimal solution of the optimization problem faster by combining PCA algorithm and GWO-BP algorithm, using the dimensionality reduction ability of PCA algorithm and the optimization ability of GWO-BP algorithm. Meanwhile, by flexibly adjusting the parameters, it can achieve better performance in the prediction problem. 3.2. Streaming media product bit rate selection technique based on PCAGWO-BP algorithm MPEG-DASH adaptive streaming product bitrate selection technology is a technology that dynamically adjusts the video bitrate based on the network environment, aiming to provide users with a smooth, highquality video experience (Khalaf et al., 2020). This technology utilizes the MPEG-DASH standard to ad

**[Datos / trazas / datasets / contenidos | extracto 4 | p.6]**

media product; α and β are the adjustment coefficients, which can be set according to the actual situation. Finally, the bitrate selection strategy is continuously optimized through real-time monitoring and feedback mechanism. This process needs to be adjusted according to user feedback and network conditions to improve user experience and service quality. In the above process, the prediction of network bandwidth using the network bandwidth prediction model constructed based on PCAGWO-BP algorithm is the most important part of it, and the specific flow of this prediction model is shown in Fig. 5. Fig. 5 showcases the process of the network bandwidth prediction model based on the improved BP algorithm can be mainly divided into the following eight processes. First, historical data on network bandwidth is collected, including information on network traffic and bandwidth utilization. These data will be utilized as inputs to the model for training and predicting network bandwidth. After that, the collected raw data are preprocessed, including data cleaning, normalization and other operations to eliminate the effects of outliers and magnitude differences on the prediction model. The pre-processed data is then subjected to dimensionality reduction using the PCA algorithm to extract key features and remove noise. This reduces the dimensionality of the data, reduces computational complexity, and improves the generalization ability of the model. The fourth step is to construct a BP NN with a suitable number of HL nodes based on the features of the dimensionality reduced data. This network will be used to learn and predict the change law of network bandwidth. Then the GWO algorithm is applied to optimize the weights and thresholds of the BP NN. By simulating the hunting behavior

**[Datos / trazas / datasets / contenidos | extracto 5 | p.7]**

curve of 0.857; it exceeds the GWO-BP algorithm’s 0.763, the SSA-BP algorithm’s 0.756, and the GWO-SVM algorithm’s 0.747. The above results illustrate that, in terms of the dimension of the ROC curve, the research proposed PCA-SWO-BP algorithm’s performance is better than the comparison algorithms. The training error data of the four algorithms during model training are compared and the outcomes are showcased in Fig. 8. Fig. 8 showcases that among the four algorithms, the PCA-GWO-BP algorithm has the most obvious downward trend of training error and reaches the desired accuracy at 566 iterations; the GWO-BP algorithm has a slightly slower downward trend of training error and reaches the desired accuracy at 855 iterations; and the SSA-BP algorithm has a relatively gentle downward trend of training error and reaches the desired accuracy at 955 iterations; The GWO-BP algorithm has the smoothest decline in training error and reaches the desired accuracy in 1032 iterations. This result indicates that the proposed PCA-GWO-BP algorithm performs better in training, has the fastest convergence speed and has better performance. Fig. 9 gives the comparison results of the absolute errors of the four algorithm models during the prediction process. From Fig. 9, the PCA-GWO-BP algorithm has the lowest overall level of absolute error, with an average absolute error value of 0.0005; which is below the GWO-BP algorithm’s 0.0012; the SSA-BP algorithm’s 0.0021; and the GWO-SVM algorithm’s 0.0057. From this result, it can be concluded that in terms of the absolute error dimension, the PCAGWO-BP algorithm’s overall performance is also better than the comparison algorithms. Comparing the above dimensions, it showcases that the overall prediction performance of the proposed PCA-GWO-BP algorith

**[Datos / trazas / datasets / contenidos | extracto 6 | p.8]**

media products proposed in the study (Technology 1) and the code rate selection technology for streaming media products based on SSA-BP algorithm (Technology 2) and the code rate selection technology for streaming media products based on GWO-BP algorithm (Technology 3) are compared and experimented, and the accuracy, real-time, and impact on the user experience of the code rate selection are used as the comparison indexes. The accuracy and real-time comparison results of the three techniques in different datasets are shown in Fig. 10. From Fig. 10(a), the selection accuracy of technique 1 in the video dataset is 92.3%, which is significantly higher than that of technique 2 (80.1%) and that of technique 3 (79.5%); moreover, it can be found that the selection accuracy of technique 1 in the network state dataset is 91.8%, which is significantly higher than that of technique 2 (78.3%) and that of technique 3 (79.9%). From Fig. 10(b), it can be obtained that the response time of technology 1 in both data sets is less than 5 s, which is much lower than that of technology 2 and technology 3. Therefore, from the above results, it can be concluded that the accuracy and realtime performance of the proposed streaming media product bit rate selection technology is better than the comparison technology. For comparing the actual application effect of the three technologies, the study selected a number of different groups of users to score their experience and statistics, the scoring statistics are shown in Fig. 11. The full score is 10 points, the higher the score, the higher the recognition. Fig. 11showcases that the average score of technique 1 among the eight groups of users is 9.67; much higher than that of technique 2, which is 8.43, and that of technique 3, which is 7.88. This

### 4.x Evaluación / baselines / experimentos

**[Evaluación / baselines / experimentos | extracto 1 | p.1]**

Bit rate selection technology of image processing based on artificial intelligence in MPEG-DASH adaptive streaming media Ping Yang *, Jinyi Qiao , Minxiu Chen School of Media and Design, Hangzhou Dianzi University, Hangzhou, 310018, China A R T I C L E I N F O Keywords: AI MPEG-DASH Streaming media product Bit rate selection technique PCA-GWO-BP A B S T R A C T Aiming at the bit rate selection problem of MPEG-DASH adaptive streaming media in image processing, a hybrid method combining multiple artificial intelligence algorithms is proposed. Firstly, kernel principal component analysis, Grey Wolf optimization algorithm and least squares support vector machine are integrated to construct an efficient hybrid algorithm model. This model aims to optimize the image processing effect in streaming media transmission, especially in the dynamic network environment. The experimental results show that the accuracy of the hybrid algorithm reaches 0.945 in the training process, and the absolute error is only 0.0005, which is significantly better than other comparison algorithms. Further empirical analysis shows that the accuracy of the proposed rate selection technique in image processing is as high as 92.3%, which is far higher than the existing technique. This research not only improves the image quality of streaming media transmission, but also greatly improves the user experience. The research provides a new perspective for image processing technology in the field of digital media, and is of great significance for promoting the innovation and development of streaming media technology. 1. Introduction In the digital era, streaming media technology has become a popular way of multimedia transmission, widely used in online video, audio live broadcast, distance education and many oth

**[Evaluación / baselines / experimentos | extracto 2 | p.2]**

changes of network conditions to ensure smooth playback. This research provides a new bit rate selection strategy for the streaming media field, which effectively improves the efficiency and user experience of streaming media transmission. The paper mainly consists of four parts to discuss, the first part of the content is mainly to describe the BP algorithm, GWO algorithm and the related research on intelligent algorithms in the field of streaming media; the second part of the content is mainly to analyze the bit rate selection technology for MPEG-DASH adaptive streaming media products based on PCA-GWO-BP algorithm; the third part is mainly to compare and contrast the performance and research to propose a new bit rate selection strategy for streaming media products. performance comparison and the comparative analysis of the research proposed streaming media product bit rate selection techniques; the fourth part is mainly the summary of the whole paper. 2. Literature review As various optimization methods of BP algorithm are gradually developed, BP algorithm and its improved algorithms are applied in many fields. Lu’s team proposed a novel algorithm based on adaptive cloning genetic algorithm and BP algorithm to address the problem of low recognition accuracy of traditional intrusion detection system. The model is applied in simulation experiments, and the outcomes demonstrate that the detection accuracy exceeds the traditional intrusion detection system, and it has good global searchability (Lu et al., 2021). Safavi et al. introduces and compares the BP algorithm and radial basis function NN in order to make a better estimation of the minimum deviation of the nuclear boiling ratio, and the results of the comparison of the two networks show that the training of the radi

**[Evaluación / baselines / experimentos | extracto 3 | p.3]**

combination of BP neural network and MPEG-DASH can greatly improve the intelligence and user experience of streaming media transmission. Therefore, this paper proposes a bit rate selection technology for streaming media products based on improved BP neural network, hoping that it can provide an efficient selection scheme and promote the user’s experience. In this selection technology, BP neural network is mainly composed of three modules: input layer, hidden layer and output layer. The constitutive model of BP neural network is shown in Fig. 1. The main module HL in the BP NN can be categorized according to the number of layers, divided into single HL and multi-HL. In the prediction network bandwidth mapping relationships are not complex, so the single HL BP NN with shorter training time can be used. In the BP NN, the output value net1 expression transmitted from the IL to the HL is shown in Equation (1). net1 = w1x + b1, h = g1(net1) (1) In Equation (1), x denotes the initial value of neuron; b1 denotes the intercept term, and the weight value of interlayer connection is denoted by w1. The result net2 expression transmitted from the HL to the OL is shown in Equation (2). net2 = ω2 + b2, y = g2(net2) (2) In Equation (2), b2 denotes the intercept term and ω2 denotes the weight value of the connection between the HL and the OL. The specific sigmoid function expression is shown in Equation (3). y ⌢= g2(net2) = g2 ( vTg1(net1) + b2 ) = g2 ( vTg1 ( wTx + b1 ) + b2 ) (3) In Equation (3), y ⌢is the NN output value. During the operation of the BP NN, errors are always generated, and the total error generated during the operation E(θ) is expressed in Equation (4). E(θ) = 1 2 ∑ 2 i=1 (yi −̂yi)2 (4) In Equation (4), y denotes the actual value. Although the BP algorithm has a bette

**[Evaluación / baselines / experimentos | extracto 4 | p.4]**

F = 1 A ∑ A s=1 ̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ∑ A k=1 ( y s k −o s k )2 √ √ √ √ (6) In Equation (6), A represents the number of grey wolves. Then the three GWs with the highest values in the wolf population are selected and recorded as, δ . The parameters r→ 1 , r→ 2 , a→in the GWO are updated to determine the location of the new wolf individuals and utilized as the initial parameters of the BP NN. Based on the updated fitness value of the wolf individuals, the newest, δ are re-informed. Finally, check whether the quantity of iterations set by the algorithm is reached. If it is not done, the parameters r→ 1 , r→ 2 , a→in the GWO are re-updated, and if it is done, the BP NN is given the optimal initial parameters. PCA is a preprocessing method that transforms the original multiple variables into several with comprehensive indicators (Diab et al., 2022b). For better enhancing the efficiency and prediction accuracy of the GWO-BP algorithm, this study adopts PCA to downsize the evaluation index data and constructs a GWO-BP prediction model based on PCA.The flowchart of the PCA-GWO-BP model is shown in Fig. 3. As can be seen from Fig. 3, the specific steps for solving the GWO-BP algorithm incorporating the PCA algorithm are as follows: firstly, determine the position and speed of the GWs of the initialized population, and count the fitness of each GW. Perform the advantage and disadvantage ranking of GWs, and update the position and speed of GWs. On the grounds of the updated GW positions, the positions are downscaled using the PCA algorithm. Based on the dimensionality reduction, train the network using the BP algorithm and calculate the fitness of the network. According to the size of the fitness, update the Fig. 3. PCA-GWO-BP model flow. Fig. 4. Bit rate selection

**[Evaluación / baselines / experimentos | extracto 5 | p.5]**

position and speed of the GW population. Repeat initializing the GW position and velocity of the population until the stopping condition is reached. The GW position update formula in the GWO-BP algorithm incorporating PCA algorithm is shown in Equation (7). x(i, t + 1) = x(i, t) + Aʹ ∗D (7) In Equation (7), Aʹ is the control parameter, D is the position difference of the GW, and the GW velocity update formula is showcased in Equation (8). v(i, t + 1) = r ∗v(i, t) + C ∗P − x(i, t) (8) In Equation (8), C serves as the control parameter, r is the random number, and P serves as the position of the current optimal solution, respectively. The selection of the control parameters A and C has a great influence on the convergence speed and the quality of the solution of the algorithm, and the optimal values are usually determined experimentally and empirically. The GW fitness calculation formula is shown in Equation (9). fitness(i) = 1 (1 + error(i)) (9) In Equation (9), P is the training error of the BP algorithm. The GWOBP algorithm incorporating PCA algorithm is able to find the optimal solution of the optimization problem faster by combining PCA algorithm and GWO-BP algorithm, using the dimensionality reduction ability of PCA algorithm and the optimization ability of GWO-BP algorithm. Meanwhile, by flexibly adjusting the parameters, it can achieve better performance in the prediction problem. 3.2. Streaming media product bit rate selection technique based on PCAGWO-BP algorithm MPEG-DASH adaptive streaming product bitrate selection technology is a technology that dynamically adjusts the video bitrate based on the network environment, aiming to provide users with a smooth, highquality video experience (Khalaf et al., 2020). This technology utilizes the MPEG-DASH standard to ad

**[Evaluación / baselines / experimentos | extracto 6 | p.6]**

media product; α and β are the adjustment coefficients, which can be set according to the actual situation. Finally, the bitrate selection strategy is continuously optimized through real-time monitoring and feedback mechanism. This process needs to be adjusted according to user feedback and network conditions to improve user experience and service quality. In the above process, the prediction of network bandwidth using the network bandwidth prediction model constructed based on PCAGWO-BP algorithm is the most important part of it, and the specific flow of this prediction model is shown in Fig. 5. Fig. 5 showcases the process of the network bandwidth prediction model based on the improved BP algorithm can be mainly divided into the following eight processes. First, historical data on network bandwidth is collected, including information on network traffic and bandwidth utilization. These data will be utilized as inputs to the model for training and predicting network bandwidth. After that, the collected raw data are preprocessed, including data cleaning, normalization and other operations to eliminate the effects of outliers and magnitude differences on the prediction model. The pre-processed data is then subjected to dimensionality reduction using the PCA algorithm to extract key features and remove noise. This reduces the dimensionality of the data, reduces computational complexity, and improves the generalization ability of the model. The fourth step is to construct a BP NN with a suitable number of HL nodes based on the features of the dimensionality reduced data. This network will be used to learn and predict the change law of network bandwidth. Then the GWO algorithm is applied to optimize the weights and thresholds of the BP NN. By simulating the hunting behavior

**[Evaluación / baselines / experimentos | extracto 7 | p.7]**

curve of 0.857; it exceeds the GWO-BP algorithm’s 0.763, the SSA-BP algorithm’s 0.756, and the GWO-SVM algorithm’s 0.747. The above results illustrate that, in terms of the dimension of the ROC curve, the research proposed PCA-SWO-BP algorithm’s performance is better than the comparison algorithms. The training error data of the four algorithms during model training are compared and the outcomes are showcased in Fig. 8. Fig. 8 showcases that among the four algorithms, the PCA-GWO-BP algorithm has the most obvious downward trend of training error and reaches the desired accuracy at 566 iterations; the GWO-BP algorithm has a slightly slower downward trend of training error and reaches the desired accuracy at 855 iterations; and the SSA-BP algorithm has a relatively gentle downward trend of training error and reaches the desired accuracy at 955 iterations; The GWO-BP algorithm has the smoothest decline in training error and reaches the desired accuracy in 1032 iterations. This result indicates that the proposed PCA-GWO-BP algorithm performs better in training, has the fastest convergence speed and has better performance. Fig. 9 gives the comparison results of the absolute errors of the four algorithm models during the prediction process. From Fig. 9, the PCA-GWO-BP algorithm has the lowest overall level of absolute error, with an average absolute error value of 0.0005; which is below the GWO-BP algorithm’s 0.0012; the SSA-BP algorithm’s 0.0021; and the GWO-SVM algorithm’s 0.0057. From this result, it can be concluded that in terms of the absolute error dimension, the PCAGWO-BP algorithm’s overall performance is also better than the comparison algorithms. Comparing the above dimensions, it showcases that the overall prediction performance of the proposed PCA-GWO-BP algorith

**[Evaluación / baselines / experimentos | extracto 8 | p.8]**

media products proposed in the study (Technology 1) and the code rate selection technology for streaming media products based on SSA-BP algorithm (Technology 2) and the code rate selection technology for streaming media products based on GWO-BP algorithm (Technology 3) are compared and experimented, and the accuracy, real-time, and impact on the user experience of the code rate selection are used as the comparison indexes. The accuracy and real-time comparison results of the three techniques in different datasets are shown in Fig. 10. From Fig. 10(a), the selection accuracy of technique 1 in the video dataset is 92.3%, which is significantly higher than that of technique 2 (80.1%) and that of technique 3 (79.5%); moreover, it can be found that the selection accuracy of technique 1 in the network state dataset is 91.8%, which is significantly higher than that of technique 2 (78.3%) and that of technique 3 (79.9%). From Fig. 10(b), it can be obtained that the response time of technology 1 in both data sets is less than 5 s, which is much lower than that of technology 2 and technology 3. Therefore, from the above results, it can be concluded that the accuracy and realtime performance of the proposed streaming media product bit rate selection technology is better than the comparison technology. For comparing the actual application effect of the three technologies, the study selected a number of different groups of users to score their experience and statistics, the scoring statistics are shown in Fig. 11. The full score is 10 points, the higher the score, the higher the recognition. Fig. 11showcases that the average score of technique 1 among the eight groups of users is 9.67; much higher than that of technique 2, which is 8.43, and that of technique 3, which is 7.88. This

### 4.x Limitaciones / riesgos / aplicabilidad

**[Limitaciones / riesgos / aplicabilidad | extracto 1 | p.2]**

changes of network conditions to ensure smooth playback. This research provides a new bit rate selection strategy for the streaming media field, which effectively improves the efficiency and user experience of streaming media transmission. The paper mainly consists of four parts to discuss, the first part of the content is mainly to describe the BP algorithm, GWO algorithm and the related research on intelligent algorithms in the field of streaming media; the second part of the content is mainly to analyze the bit rate selection technology for MPEG-DASH adaptive streaming media products based on PCA-GWO-BP algorithm; the third part is mainly to compare and contrast the performance and research to propose a new bit rate selection strategy for streaming media products. performance comparison and the comparative analysis of the research proposed streaming media product bit rate selection techniques; the fourth part is mainly the summary of the whole paper. 2. Literature review As various optimization methods of BP algorithm are gradually developed, BP algorithm and its improved algorithms are applied in many fields. Lu’s team proposed a novel algorithm based on adaptive cloning genetic algorithm and BP algorithm to address the problem of low recognition accuracy of traditional intrusion detection system. The model is applied in simulation experiments, and the outcomes demonstrate that the detection accuracy exceeds the traditional intrusion detection system, and it has good global searchability (Lu et al., 2021). Safavi et al. introduces and compares the BP algorithm and radial basis function NN in order to make a better estimation of the minimum deviation of the nuclear boiling ratio, and the results of the comparison of the two networks show that the training of the radi

**[Limitaciones / riesgos / aplicabilidad | extracto 2 | p.6]**

media product; α and β are the adjustment coefficients, which can be set according to the actual situation. Finally, the bitrate selection strategy is continuously optimized through real-time monitoring and feedback mechanism. This process needs to be adjusted according to user feedback and network conditions to improve user experience and service quality. In the above process, the prediction of network bandwidth using the network bandwidth prediction model constructed based on PCAGWO-BP algorithm is the most important part of it, and the specific flow of this prediction model is shown in Fig. 5. Fig. 5 showcases the process of the network bandwidth prediction model based on the improved BP algorithm can be mainly divided into the following eight processes. First, historical data on network bandwidth is collected, including information on network traffic and bandwidth utilization. These data will be utilized as inputs to the model for training and predicting network bandwidth. After that, the collected raw data are preprocessed, including data cleaning, normalization and other operations to eliminate the effects of outliers and magnitude differences on the prediction model. The pre-processed data is then subjected to dimensionality reduction using the PCA algorithm to extract key features and remove noise. This reduces the dimensionality of the data, reduces computational complexity, and improves the generalization ability of the model. The fourth step is to construct a BP NN with a suitable number of HL nodes based on the features of the dimensionality reduced data. This network will be used to learn and predict the change law of network bandwidth. Then the GWO algorithm is applied to optimize the weights and thresholds of the BP NN. By simulating the hunting behavior

## 5. Figuras, tablas, algoritmos y ecuaciones detectadas por texto

**[elemento detectado 1 | p.1]**

Bit rate selection technology of image processing based on artificial intelligence in MPEG-DASH adaptive streaming media Ping Yang *, Jinyi Qiao , Minxiu Chen School of Media and Design, Hangzhou Dianzi University, Hangzhou, 310018, China A R T I C L E I N F O Keywords: AI MPEG-DASH Streaming media product Bit rate selection technique PCA-GWO-BP A B S T R A C T Aiming at the bit rate selection problem of MPEG-DASH adaptive streaming media in image processing, a hybrid method combining multiple artificial intelligence algorithms is proposed. Firstly, kernel principal component analysis, Grey Wolf optimization algorithm and least squares support vector machine are integrated to construct an efficient hybrid algorithm model. This model aims to optimize the image processing effect in streaming media transmission, especially in the dynamic network environment. The experimental results show that the accuracy of the hybrid algorithm reaches 0.945 in the training process, and the absolute error is only 0.0005, which is significantly better than other comparison algorithms. Further empirical analysis shows that the accuracy of the proposed rate selection technique in image processing is as high as 92.3%, which is far higher than the existing technique. This research not only improves the image quality of streaming media transmission, but also greatly improves the user experience. The re

**[elemento detectado 2 | p.2]**

changes of network conditions to ensure smooth playback. This research provides a new bit rate selection strategy for the streaming media field, which effectively improves the efficiency and user experience of streaming media transmission. The paper mainly consists of four parts to discuss, the first part of the content is mainly to describe the BP algorithm, GWO algorithm and the related research on intelligent algorithms in the field of streaming media; the second part of the content is mainly to analyze the bit rate selection technology for MPEG-DASH adaptive streaming media products based on PCA-GWO-BP algorithm; the third part is mainly to compare and contrast the performance and research to propose a new bit rate selection strategy for streaming media products. performance comparison and the comparative analysis of the research proposed streaming media product bit rate selection techniques; the fourth part is mainly the summary of the whole paper. 2. Literature review As various optimization methods of BP algorithm are gradually developed, BP algorithm and its improved algorithms are applied in many fields. Lu’s team proposed a novel algorithm based on adaptive cloning genetic algorithm and BP algorithm to address the problem of low recognition accuracy of traditional intrusion detection system. The model is applied in simulation experiments, and the outcomes demonstrate

**[elemento detectado 3 | p.3]**

combination of BP neural network and MPEG-DASH can greatly improve the intelligence and user experience of streaming media transmission. Therefore, this paper proposes a bit rate selection technology for streaming media products based on improved BP neural network, hoping that it can provide an efficient selection scheme and promote the user’s experience. In this selection technology, BP neural network is mainly composed of three modules: input layer, hidden layer and output layer. The constitutive model of BP neural network is shown in Fig. 1. The main module HL in the BP NN can be categorized according to the number of layers, divided into single HL and multi-HL. In the prediction network bandwidth mapping relationships are not complex, so the single HL BP NN with shorter training time can be used. In the BP NN, the output value net1 expression transmitted from the IL to the HL is shown in Equation (1). net1 = w1x + b1, h = g1(net1) (1) In Equation (1), x denotes the initial value of neuron; b1 denotes the intercept term, and the weight value of interlayer connection is denoted by w1. The result net2 expression transmitted from the HL to the OL is shown in Equation (2). net2 = ω2 + b2, y = g2(net2) (2) In Equation (2), b2 denotes the intercept term and ω2 denotes the weight value of the connection between the HL and the OL. The specific sigmoid function expression is shown in

**[elemento detectado 4 | p.4]**

F = 1 A ∑ A s=1 ̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ∑ A k=1 ( y s k −o s k )2 √ √ √ √ (6) In Equation (6), A represents the number of grey wolves. Then the three GWs with the highest values in the wolf population are selected and recorded as, δ . The parameters r→ 1 , r→ 2 , a→in the GWO are updated to determine the location of the new wolf individuals and utilized as the initial parameters of the BP NN. Based on the updated fitness value of the wolf individuals, the newest, δ are re-informed. Finally, check whether the quantity of iterations set by the algorithm is reached. If it is not done, the parameters r→ 1 , r→ 2 , a→in the GWO are re-updated, and if it is done, the BP NN is given the optimal initial parameters. PCA is a preprocessing method that transforms the original multiple variables into several with comprehensive indicators (Diab et al., 2022b). For better enhancing the efficiency and prediction accuracy of the GWO-BP algorithm, this study adopts PCA to downsize the evaluation index data and constructs a GWO-BP prediction model based on PCA.The flowchart of the PCA-GWO-BP model is shown in Fig. 3. As can be seen from Fig. 3, the specific steps for solving the GWO-BP algorithm incorporating the PCA algorithm are as follows: firstly, determine the position and speed of the GWs of the initialized population, and count the fitness of each GW. Perform the advantage an

**[elemento detectado 5 | p.5]**

position and speed of the GW population. Repeat initializing the GW position and velocity of the population until the stopping condition is reached. The GW position update formula in the GWO-BP algorithm incorporating PCA algorithm is shown in Equation (7). x(i, t + 1) = x(i, t) + Aʹ ∗D (7) In Equation (7), Aʹ is the control parameter, D is the position difference of the GW, and the GW velocity update formula is showcased in Equation (8). v(i, t + 1) = r ∗v(i, t) + C ∗P − x(i, t) (8) In Equation (8), C serves as the control parameter, r is the random number, and P serves as the position of the current optimal solution, respectively. The selection of the control parameters A and C has a great influence on the convergence speed and the quality of the solution of the algorithm, and the optimal values are usually determined experimentally and empirically. The GW fitness calculation formula is shown in Equation (9). fitness(i) = 1 (1 + error(i)) (9) In Equation (9), P is the training error of the BP algorithm. The GWOBP algorithm incorporating PCA algorithm is able to find the optimal solution of the optimization problem faster by combining PCA algorithm and GWO-BP algorithm, using the dimensionality reduction ability of PCA algorithm and the optimization ability of GWO-BP algorithm. Meanwhile, by flexibly adjusting the parameters, it can achieve better performance in the prediction

**[elemento detectado 6 | p.6]**

media product; α and β are the adjustment coefficients, which can be set according to the actual situation. Finally, the bitrate selection strategy is continuously optimized through real-time monitoring and feedback mechanism. This process needs to be adjusted according to user feedback and network conditions to improve user experience and service quality. In the above process, the prediction of network bandwidth using the network bandwidth prediction model constructed based on PCAGWO-BP algorithm is the most important part of it, and the specific flow of this prediction model is shown in Fig. 5. Fig. 5 showcases the process of the network bandwidth prediction model based on the improved BP algorithm can be mainly divided into the following eight processes. First, historical data on network bandwidth is collected, including information on network traffic and bandwidth utilization. These data will be utilized as inputs to the model for training and predicting network bandwidth. After that, the collected raw data are preprocessed, including data cleaning, normalization and other operations to eliminate the effects of outliers and magnitude differences on the prediction model. The pre-processed data is then subjected to dimensionality reduction using the PCA algorithm to extract key features and remove noise. This reduces the dimensionality of the data, reduces computational compl

**[elemento detectado 7 | p.7]**

curve of 0.857; it exceeds the GWO-BP algorithm’s 0.763, the SSA-BP algorithm’s 0.756, and the GWO-SVM algorithm’s 0.747. The above results illustrate that, in terms of the dimension of the ROC curve, the research proposed PCA-SWO-BP algorithm’s performance is better than the comparison algorithms. The training error data of the four algorithms during model training are compared and the outcomes are showcased in Fig. 8. Fig. 8 showcases that among the four algorithms, the PCA-GWO-BP algorithm has the most obvious downward trend of training error and reaches the desired accuracy at 566 iterations; the GWO-BP algorithm has a slightly slower downward trend of training error and reaches the desired accuracy at 855 iterations; and the SSA-BP algorithm has a relatively gentle downward trend of training error and reaches the desired accuracy at 955 iterations; The GWO-BP algorithm has the smoothest decline in training error and reaches the desired accuracy in 1032 iterations. This result indicates that the proposed PCA-GWO-BP algorithm performs better in training, has the fastest convergence speed and has better performance. Fig. 9 gives the comparison results of the absolute errors of the four algorithm models during the prediction process. From Fig. 9, the PCA-GWO-BP algorithm has the lowest overall level of absolute error, with an average absolute error value of 0.0005; which is be

**[elemento detectado 8 | p.8]**

media products proposed in the study (Technology 1) and the code rate selection technology for streaming media products based on SSA-BP algorithm (Technology 2) and the code rate selection technology for streaming media products based on GWO-BP algorithm (Technology 3) are compared and experimented, and the accuracy, real-time, and impact on the user experience of the code rate selection are used as the comparison indexes. The accuracy and real-time comparison results of the three techniques in different datasets are shown in Fig. 10. From Fig. 10(a), the selection accuracy of technique 1 in the video dataset is 92.3%, which is significantly higher than that of technique 2 (80.1%) and that of technique 3 (79.5%); moreover, it can be found that the selection accuracy of technique 1 in the network state dataset is 91.8%, which is significantly higher than that of technique 2 (78.3%) and that of technique 3 (79.9%). From Fig. 10(b), it can be obtained that the response time of technology 1 in both data sets is less than 5 s, which is much lower than that of technology 2 and technology 3. Therefore, from the above results, it can be concluded that the accuracy and realtime performance of the proposed streaming media product bit rate selection technology is better than the comparison technology. For comparing the actual application effect of the three technologies, the study selecte

## 6. Texto crudo extraído del cuerpo principal por página

> Esta sección conserva el texto extraído página a página hasta referencias/bibliografía cuando se detecta. Se incluye para no perder detalles de método, entrenamiento, datos o evaluación. Puede tener problemas de orden de columnas o fórmulas por naturaleza del PDF.

### Página 1

Bit rate selection technology of image processing based on artificial
intelligence in MPEG-DASH adaptive streaming media
Ping Yang *, Jinyi Qiao , Minxiu Chen
School of Media and Design, Hangzhou Dianzi University, Hangzhou, 310018, China
A R T I C L E I N F O
Keywords:
AI
MPEG-DASH
Streaming media product
Bit rate selection technique
PCA-GWO-BP
A B S T R A C T
Aiming at the bit rate selection problem of MPEG-DASH adaptive streaming media in image processing, a hybrid
method combining multiple artificial intelligence algorithms is proposed. Firstly, kernel principal component
analysis, Grey Wolf optimization algorithm and least squares support vector machine are integrated to construct
an efficient hybrid algorithm model. This model aims to optimize the image processing effect in streaming media
transmission, especially in the dynamic network environment. The experimental results show that the accuracy
of the hybrid algorithm reaches 0.945 in the training process, and the absolute error is only 0.0005, which is
significantly better than other comparison algorithms. Further empirical analysis shows that the accuracy of the
proposed rate selection technique in image processing is as high as 92.3%, which is far higher than the existing
technique. This research not only improves the image quality of streaming media transmission, but also greatly
improves the user experience. The research provides a new perspective for image processing technology in the
field of digital media, and is of great significance for promoting the innovation and development of streaming
media technology.
1. Introduction
In the digital era, streaming media technology has become a popular
way of multimedia transmission, widely used in online video, audio live
broadcast, distance education and many other fields. However, ensuring
a smooth media playback experience in an unstable network environment is a major technical challenge (Spilker & Colbjørnsen, 2020a).
Dynamic Adaptive Streaming over HTTP (MPEG-DASH), as an advanced
streaming media transmission technology, effectively addresses this
challenge by allowing clients to dynamically adjust video bitrates according to current network conditions (Camilleri & Falzon, 2021).
MPEG-DASH not only improves the flexibility of streaming media delivery, but also significantly enhances the user experience, making it one
of the key technologies in current streaming services. Recently, as the
boost of artificial intelligence (AI) technologies such as deep learning
and machine learning, their application in the field of digital media has
gradually become indispensable (Pal et al., 2023). In streaming media
transmission, AI algorithms can help predict the changes in network
bandwidth, so as to select the appropriate bit rate in advance to ensure
the continuity of the user’s viewing experience (Gheisari et al., 2023). AI
algorithms in the back propagation (Back propagation (BP) neural
network (NN) is a mathematical model used for learning and prediction,
by adjusting the weight to minimize the prediction error, and BP algorithms have strong learning ability, nonlinear mapping ability, and the
ability of nonlinear mapping, and the ability of nonlinear mapping, and
the ability of nonlinear mapping. Ability, nonlinear mapping ability and
other advantages (Li et al., 2023). In addition, Principal component
analysis (PCA), as an effective data dimensionality reduction technology, can extract the most critical features from the original data, reduce
data redundancy, and improve processing efficiency. Grey Wolf Optimizer (GWO), on the other hand, is an optimization algorithm that
simulates the predation behavior of grey wolves. It realizes global
optimization by simulating the social rank and hunting behavior of grey
wolves, and is especially suitable for solving the problem of parameter
selection and optimization (Liu et al., 2021). Based on the above background, this paper proposes a bit rate selection technology for streaming
media products based on three AI algorithms, hoping to promote the
development of streaming media field in this way. This research innovatively combines PCA, GWO and BP NN in MPEG-DASH streaming
media transmission. The PCA extracts key features such as network
bandwidth, the GWO algorithm realizes global optimization to select the
optimal bit rate, and then combines with the BP NN for forecasting the
* Corresponding author.
E-mail address: yangping@hdu.edu.cn (P. Yang).
Contents lists available at ScienceDirect
Journal of Radiation Research and Applied Sciences
journal homepage: www.journals.elsevier.com/journal-of-radiation-research-and-applied-sciences
https://doi.org/10.1016/j.jrras.2024.101036
Received 3 June 2024; Received in revised form 9 July 2024; Accepted 17 July 2024
Journal of Radiation Research and Applied Sciences 17 (2024) 101036
Available online 10 August 2024
1687-8507/© 2024 The Authors. Published by Elsevier B.V. on behalf of The Egyptian Society of Radiation Sciences and Applications. This is an open access article
under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-nc-nd/4.0/ ).

### Página 2

changes of network conditions to ensure smooth playback. This research
provides a new bit rate selection strategy for the streaming media field,
which effectively improves the efficiency and user experience of
streaming media transmission.
The paper mainly consists of four parts to discuss, the first part of the
content is mainly to describe the BP algorithm, GWO algorithm and the
related research on intelligent algorithms in the field of streaming
media; the second part of the content is mainly to analyze the bit rate
selection technology for MPEG-DASH adaptive streaming media products based on PCA-GWO-BP algorithm; the third part is mainly to
compare and contrast the performance and research to propose a new bit
rate selection strategy for streaming media products. performance
comparison and the comparative analysis of the research proposed
streaming media product bit rate selection techniques; the fourth part is
mainly the summary of the whole paper.
2. Literature review
As various optimization methods of BP algorithm are gradually
developed, BP algorithm and its improved algorithms are applied in
many fields. Lu’s team proposed a novel algorithm based on adaptive
cloning genetic algorithm and BP algorithm to address the problem of
low recognition accuracy of traditional intrusion detection system. The
model is applied in simulation experiments, and the outcomes demonstrate that the detection accuracy exceeds the traditional intrusion
detection system, and it has good global searchability (Lu et al., 2021).
Safavi et al. introduces and compares the BP algorithm and radial basis
function NN in order to make a better estimation of the minimum deviation of the nuclear boiling ratio, and the results of the comparison of
the two networks show that the training of the radial basis function
neural process is much faster than BPN and its maximum network error
is less than BP algorithm (Safavi et al., 2020). In addition, the GWO
algorithm has an increasingly wide range of applications, for example,
Diab et al. presents a method on the grounds of the improved Grey Wolf
(GW) optimization algorithm for the problem of evaluating the model
parameters of proton exchange membrane fuel cells. By comparing the
method with several optimization algorithms, the outcomes showcase
that the method performs well in terms of both accuracy and convergence speed, and the optimization efficiency reaches 99.97%. The
method can provide an effective new way for parameter estimation of
proton exchange membrane fuel cell models (Diab et al., 2022a). Badi’s
team proposed a method based on hybrid butterfly optimization algorithm (BOA-GWO-PSO) for the problem of power load optimization.
Through comparative analysis with other traditional meta-heuristic algorithms, the outcomes showcase that the method possesses demerits in
solving complex optimization problems and is validated on the IEEE 30
bus system. The above results indicate that the method has practical
applications to solve real-world optimization problems (Badi et al.,
2023).
With the wide application of streaming media products, various
different AI technologies have begun to possess an essential influence on
the streaming media field. Liu’s team proposes a risk-aware contextlearning based transcoding task assignment and viewer association algorithm for the edge-assisted crowdsourced real-time video transcoding
problem. By combining context-awareness and risk-sensitivity, robust
task offloading and superior network utility performance are achieved.
The relevant outcomes showcase that the proposed algorithm can
reduce the task switching cost and computation time compared to other
algorithms, achieving 86.8% and 92.3% reduction, respectively (Liu
et al., 2023). Peng and Tang presented a unidirectional cumulative
steganography algorithm on the grounds of dynamic key updating and
exchanging to address the steganographic communication problem in
VoIP streaming media. Theoretical analysis shows that the algorithm is
able to resist passive attacks, and experimental results show that the
algorithm possesses less impact on real-time VoIP communication, and
its security and effect outperform other related algorithms with
comparable data embedding rates (Peng & Tang, 2020). Huang’s team
proposed a joint optimization of the MEC server video clip caching and
transcoding and wireless resource allocation. Through modeling and
simulation, the outcomes showcase that the proposed algorithm effectively improves client throughput, received video quality, and video clip
hit rate, while reducing playback lag time, video clip representation
switching, and system backhaul traffic (Huang et al., 2021). Aldabbas
presented a new method on the grounds of the Random Forest algorithm
for predicting and adapting bandwidth demand for different applications, for addressing the bandwidth management problem of SDN
network. The relevant outcomes showcase that this method can significantly improve the network quality of service while outperforming
existing bandwidth allocation algorithms (Aldabbas, 2023).
The above research demonstrated several application areas of BP and
GWO algorithms, and also demonstrated a variety of intelligent algorithms applied to the streaming media domain. However, there are
fewer studies that combine BP and GWO algorithms and apply them to
the streaming media field, so this study combines AI techniques such as
PCA, GWO and BP and applies them to the digital media field, and it is
expected that this study will promote the development of the streaming
media field.
3. Streaming media product bit rate selection technology based
on AI technology
In recent years, AI algorithms have been widely used in bit rate selection for streaming media products. In this section, details of how AI
algorithms are improved as well as constructing a streaming product
bitrate selection technique based on the improved AI algorithms will be
presented. Through this approach, it is expected to provide an efficient,
accurate and user-friendly bitrate selection scheme for the streaming
media industry to further enhance the user’s viewing experience.
3.1. BP algorithm incorporating PCA and GWO
In MPEG-DASH adaptive streaming product rate selection technology, the prediction of network bandwidth occupies a core position,
which is directly related to the fluency of streaming media and user
experience (Spilker & Colbjørnsen, 2020b). BP neural network, with its
strong learning ability, nonlinear mapping ability, high adaptability,
prediction accuracy and stability, and easy implementation and optimization, has become the optimal algorithm in the field of network
bandwidth prediction (Jiang et al., 2021). In MPEG-DASH system, the
application of BP neural network is particularly important, it can predict
the change of network bandwidth in real time, and provide the system
with accurate bit rate selection basis, so as to ensure the stable playback
of streaming media in different network conditions. Therefore, the
Fig. 1. BP NN model.
P. Yang et al.
Journal of Radiation Research and Applied Sciences 17 (2024) 101036
2

### Página 3

combination of BP neural network and MPEG-DASH can greatly improve
the intelligence and user experience of streaming media transmission.
Therefore, this paper proposes a bit rate selection technology for
streaming media products based on improved BP neural network, hoping that it can provide an efficient selection scheme and promote the
user’s experience. In this selection technology, BP neural network is
mainly composed of three modules: input layer, hidden layer and output
layer. The constitutive model of BP neural network is shown in Fig. 1.
The main module HL in the BP NN can be categorized according to
the number of layers, divided into single HL and multi-HL. In the prediction network bandwidth mapping relationships are not complex, so
the single HL BP NN with shorter training time can be used. In the BP
NN, the output value net1 expression transmitted from the IL to the HL is
shown in Equation (1).
net1 = w1x + b1, h = g1(net1)
(1)
In Equation (1), x denotes the initial value of neuron; b1 denotes the
intercept term, and the weight value of interlayer connection is denoted
by w1. The result net2 expression transmitted from the HL to the OL is
shown in Equation (2).
net2 = ω2 + b2, y = g2(net2)
(2)
In Equation (2), b2 denotes the intercept term and ω2 denotes the
weight value of the connection between the HL and the OL. The specific
sigmoid function expression is shown in Equation (3).
y
⌢= g2(net2) = g2
(
vTg1(net1) + b2
)
= g2
(
vTg1
(
wTx + b1
)
+ b2
)
(3)
In Equation (3), y
⌢is the NN output value. During the operation of the
BP NN, errors are always generated, and the total error generated during
the operation E(θ) is expressed in Equation (4).
E(θ) = 1
2
∑
2
i=1
(yi −̂yi)2
(4)
In Equation (4), y denotes the actual value. Although the BP algorithm has a better prediction effect, it also has some shortcomings, such
as slow convergence speed, inconsistent network structure, etc. The
GWO algorithm is used to optimize the BP algorithm. In order to
improve the BP algorithm, GWO is chosen for optimizing it. GWO algorithm originates from the group behavior of grey wolves, and there
are four grades of wolves in the grey wolf society, namely alpha, beta,
gamma and delta, and GWO algorithm performs optimized search by
simulating the social behaviors of the wolves in the wolf pack (Yang
et al., 2022). First, a group of GWs is randomly initialized and the fitness
value of each wolf is calculated, the expression of initialized GW group is
shown in Equation (5).
X(0) = [x1(0), x2(0), …, xn(0)], i = 1, 2, …, D
(5)
In Equation (5), X represents the fitness value of the grey Wolf population as a whole, while x represents the fitness value of a single grey Wolf.
Then, the position of the wolves is updated based on the distance between each wolf and the alpha, beta, and gamma wolves. Finally, after
many iterations, the wolves will gradually converge to the optimal solution. The study improves the problem of slow convergence speed and
poor selection of initial weights and thresholds of BP network NN
through the superior global search ability of GWO and the advantage of
being able to well avoid falling into local minima. The combination of
the two algorithms can make up for the shortcomings of the traditional
BP algorithm, and the flow of the GWO-BP prediction model is shown in
Fig. 2.
In Fig. 2, t represents the number of iterations; T indicates the iteration threshold, which is used to determine whether the algorithm
reaches the preset maximum number of iterations. As can be seen from
Fig. 2, the process of GGO-BP is divided into two stages: data preprocessing and model training. In the data preprocessing stage, the algorithm initializes the BP neural network using initial weights and
thresholds, and calculates the error between the network output and the
desired output. After entering the model training stage, the algorithm
uses the training set data to train the neural network, and optimizes the
weight and threshold of the neural network through GWO to minimize
the prediction error. During the training process, the algorithm will
periodically calculate the error and adjust the network parameters,
while updating the position of each Wolf in the grey Wolf population to
find a better solution. The entire training process continues until the
termination conditions are met, such as the maximum number of iterations or the accuracy requirements are met. The first generation of GW
adaptation value is shown in Equation (6).
Fig. 2. Flow of GWO-BP prediction model.
P. Yang et al.
Journal of Radiation Research and Applied Sciences 17 (2024) 101036
3

### Página 4

F = 1
A
∑
A
s=1
̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
∑
A
k=1
(
y s
k −o s
k
)2
√
√
√
√
(6)
In Equation (6), A represents the number of grey wolves. Then the
three GWs with the highest values in the wolf population are selected
and recorded as, δ . The parameters r→
1 , r→
2 , a→in the GWO are updated
to determine the location of the new wolf individuals and utilized as the
initial parameters of the BP NN. Based on the updated fitness value of the
wolf individuals, the newest, δ are re-informed. Finally, check whether
the quantity of iterations set by the algorithm is reached. If it is not done,
the parameters r→
1 , r→
2 , a→in the GWO are re-updated, and if it is done,
the BP NN is given the optimal initial parameters.
PCA is a preprocessing method that transforms the original multiple
variables into several with comprehensive indicators (Diab et al.,
2022b). For better enhancing the efficiency and prediction accuracy of
the GWO-BP algorithm, this study adopts PCA to downsize the evaluation index data and constructs a GWO-BP prediction model based on
PCA.The flowchart of the PCA-GWO-BP model is shown in Fig. 3.
As can be seen from Fig. 3, the specific steps for solving the GWO-BP
algorithm incorporating the PCA algorithm are as follows: firstly,
determine the position and speed of the GWs of the initialized population, and count the fitness of each GW. Perform the advantage and
disadvantage ranking of GWs, and update the position and speed of
GWs. On the grounds of the updated GW positions, the positions are
downscaled using the PCA algorithm. Based on the dimensionality
reduction, train the network using the BP algorithm and calculate the
fitness of the network. According to the size of the fitness, update the
Fig. 3. PCA-GWO-BP model flow.
Fig. 4. Bit rate selection technology of streaming media products based on PCA-GGO-BP algorithm.
P. Yang et al.
Journal of Radiation Research and Applied Sciences 17 (2024) 101036
4

### Página 5

position and speed of the GW population. Repeat initializing the GW
position and velocity of the population until the stopping condition is
reached. The GW position update formula in the GWO-BP algorithm
incorporating PCA algorithm is shown in Equation (7).
x(i, t + 1) = x(i, t) + Aʹ ∗D
(7)
In Equation (7), Aʹ is the control parameter, D is the position difference of the GW, and the GW velocity update formula is showcased in
Equation (8).
v(i, t + 1) = r ∗v(i, t) + C ∗P −
x(i, t)
(8)
In Equation (8), C serves as the control parameter, r is the random
number, and P serves as the position of the current optimal solution,
respectively. The selection of the control parameters A and C has a great
influence on the convergence speed and the quality of the solution of the
algorithm, and the optimal values are usually determined experimentally and empirically. The GW fitness calculation formula is shown in
Equation (9).
fitness(i) =
1
(1 + error(i))
(9)
In Equation (9), P is the training error of the BP algorithm. The GWOBP algorithm incorporating PCA algorithm is able to find the optimal
solution of the optimization problem faster by combining PCA algorithm
and GWO-BP algorithm, using the dimensionality reduction ability of
PCA algorithm and the optimization ability of GWO-BP algorithm.
Meanwhile, by flexibly adjusting the parameters, it can achieve better
performance in the prediction problem.
3.2. Streaming media product bit rate selection technique based on PCAGWO-BP algorithm
MPEG-DASH adaptive streaming product bitrate selection technology is a technology that dynamically adjusts the video bitrate based on
the network environment, aiming to provide users with a smooth, highquality video experience (Khalaf et al., 2020). This technology utilizes
the MPEG-DASH standard to adaptively select the most appropriate
video bit rate for playback based on factors such as network bandwidth
and device performance (Hsu et al., 2020). In order to improve the
reasonableness of bit rate selection for streaming media products, this
research proposes an adaptive streaming media product bit rate selection technique based on network bandwidth prediction model to
improve user experience and service quality. Assuming that the bit rate
of the streaming media product is denoted as R, the network bandwidth
prediction value is denoted as B , and the device performance parameter
is denoted as D, the expression of the bit rate selection technique for the
streaming media product is shown in Equation (10).
R = f (B, D)
(10)
The main idea of this technique is for utilizing the network bandwidth prediction model to predict the future network bandwidth
changes and dynamically adjust the bit rate of the streaming media
product according to the prediction results. Specifically, the realization
process of this technology is shown in Fig. 4.
As can be obtained from Fig. 4, the main idea of the technique is to
predict future network bandwidth changes using a network bandwidth
prediction model, and dynamically adjust the bit rate of the streaming
media product according to the prediction results. Specifically, the
process of realizing the technique includes the following steps, first, the
network bandwidth prediction model is constructed by collecting the
historical data of the network bandwidth of the user and utilizing the
PCA-GWO-BP algorithm. The model is able to predict future network
bandwidth changes based on the historical data, providing a basis for
subsequent code rate selection. Assuming that the network bandwidth
historical data is denoted as BWhistory and the output of the PCA-GWO-BP
algorithm is denoted as BWprediction , the predicted network bandwidth
change BWchange can be calculated by Equation (11).
BWchange = BWprediction −BWhistory
(11)
Next, the appropriate bit rate range is determined based on the
predicted network bandwidth and the performance parameters of the
user’s device. This process requires consideration of several factors, such
as video resolution, audio quality, and device processing capability.
Then, the adaptive algorithm is utilized to dynamically adjust the bitrate
of the streaming media product within the determined bitrate range.
This process needs to be adjusted according to real-time network
bandwidth changes and user behavior. Assuming that the current bit
rate of the streaming media product is denoted as R_current, the predicted network bandwidth change is denoted as BW_change, and the
device performance parameter is denoted as D, then the dynamic
adjustment formula of the adaptive streaming media product bit rate
selection technique is shown in Equation (12).
Radjusted = Rcurrent + α ∗BWchange −β ∗D
(12)
In Equation (12), Rcurrent denotes the current bit rate of the streaming
Fig. 5. Flow of network bandwidth prediction model built based on PCA-GGO-BP algorithm.
P. Yang et al.
Journal of Radiation Research and Applied Sciences 17 (2024) 101036
5

### Página 6

media product; α and β are the adjustment coefficients, which can be set
according to the actual situation. Finally, the bitrate selection strategy is
continuously optimized through real-time monitoring and feedback
mechanism. This process needs to be adjusted according to user feedback and network conditions to improve user experience and service
quality. In the above process, the prediction of network bandwidth using
the network bandwidth prediction model constructed based on PCAGWO-BP algorithm is the most important part of it, and the specific
flow of this prediction model is shown in Fig. 5.
Fig. 5 showcases the process of the network bandwidth prediction
model based on the improved BP algorithm can be mainly divided into
the following eight processes. First, historical data on network bandwidth is collected, including information on network traffic and bandwidth utilization. These data will be utilized as inputs to the model for
training and predicting network bandwidth. After that, the collected raw
data are preprocessed, including data cleaning, normalization and other
operations to eliminate the effects of outliers and magnitude differences
on the prediction model. The pre-processed data is then subjected to
dimensionality reduction using the PCA algorithm to extract key features and remove noise. This reduces the dimensionality of the data,
reduces computational complexity, and improves the generalization
ability of the model. The fourth step is to construct a BP NN with a
suitable number of HL nodes based on the features of the dimensionality
reduced data. This network will be used to learn and predict the change
law of network bandwidth. Then the GWO algorithm is applied to
optimize the weights and thresholds of the BP NN. By simulating the
hunting behavior of the GW group, the GWO algorithm can find the
global optimal solution and avoid the BP NN from falling into the local
minimum. Afterwards, the optimized BP NN is utilized for training the
reduced dimensional data and learn the change rule of network bandwidth. During the training, the weights and thresholds of the network
are continuously adjusted to make the predicted output closer to the real
value. Assuming that the dimensionality reduced data is denoted as Xr ,
the optimized weights and thresholds of the GWO algorithm are denoted
as Wo and bo , and the output of the BP NN is denoted as bo , then the
output yʹ computational expression is shown in Equation (13).
yʹ = f (Xr ∗Wo + bo)
(13)
The seventh step is to test and evaluate the trained model through the
test dataset. The prediction performance of the model is estimated
through calculating the error metrics between the predicted value and
the true value, such as the mean square error (MSE) and the mean absolute error (MAE). The final step is to apply the trained model to the
real network environment to predict future network bandwidth changes
based on historical data. Through the above eight processes, the network
bandwidth prediction model based on the PCA-GWO-BP algorithm can
effectively predict the trend of network bandwidth changes and provide
strong support for streaming media product bit rate selection.
4. Performance comparison of Fusion algorithms and empirical
analysis of product bit rate selection techniques
This research firstly highlights the high performance of PCA-GWOBP algorithm by comparing it with GWO-SVM algorithm, SSA-BP algorithm and GWO-BP algorithm experimentally under the condition of
MATLA. The superiority of the product code rate selection technique
proposed in the study is then verified through empirical analysis.
4.1. Analysis of performance comparison results of fusion algorithms
In order to validate the performance of the PCA-GWO-BP algorithm
proposed in the study, this study was conducted in MATLA, and the
relevant environment is showcased in Table 1.
In this setup, the PCA-GWO-BP algorithm is implemented using the
Python programming language and utilizes TensorFlow for machine
learning operations. The hardware environment includes a highperformance processor, sufficient memory, and a powerful graphics
card that supports efficient computation. In this study, the PCA-GWO-BP
algorithm was relative to the GWO-SVM algorithm, SSA-BP algorithm,
and GWO-BP algorithm in the above experimental environment, and the
training accuracy, ROC curves, and errors were used as comparison
metrics. The training accuracy results are showcased in Fig. 6.
As can be obtained from Fig. 6, the training accuracy value of the
research-proposed PCA-GWO-BP is the highest among the four algorithms at 0.945; it is higher than that of the GWO-BP algorithm at 0.823,
the SSA-BP algorithm at 0.812 and the GWO-SVM algorithm at 0.785.
The outcomes showcase that the performance of the proposed PCAGWO-BP is optimal among the all in the training accuracy dimension.
Defining the false positive rate (FPR) as the X-axis and the true positive
rate (TPR) as the Y-axis, the corresponding ROC curves of the four algorithms are shown in Fig. 7.
According to Fig. 7, it can be obtained that among the four algorithms, the PCA-SWO-BP algorithm has the largest area under the ROC
Table 1
Specific experimental environment.
Environment type
Environmental composition
Types and specifications
Hardware
environment
Processor
Intel Core i7-8700K
Graphics card
Nvidia GeForce GTX
1080 Ti
Operating system
Windows 10 Pro (64-bit)
Running memory
16 GB DDR4 RAM
Storage memory
512 GB SSD
Software
environment
Programming language
Python
Machine learning library
Tensorflow
Numerical calculation
SciPy
PCA implementation
Scikit-learn (Python
library)
Implementation of GGO-BP
algorithm
Custom Python
Fig. 6. Training accuracy results of four algorithms.
Fig. 7. Comparison of prediction results and ROC curve of models.
P. Yang et al.
Journal of Radiation Research and Applied Sciences 17 (2024) 101036
6

### Página 7

curve of 0.857; it exceeds the GWO-BP algorithm’s 0.763, the SSA-BP
algorithm’s 0.756, and the GWO-SVM algorithm’s 0.747. The above
results illustrate that, in terms of the dimension of the ROC curve, the
research proposed PCA-SWO-BP algorithm’s performance is better than
the comparison algorithms. The training error data of the four algorithms during model training are compared and the outcomes are
showcased in Fig. 8.
Fig. 8 showcases that among the four algorithms, the PCA-GWO-BP
algorithm has the most obvious downward trend of training error and
reaches the desired accuracy at 566 iterations; the GWO-BP algorithm
has a slightly slower downward trend of training error and reaches the
desired accuracy at 855 iterations; and the SSA-BP algorithm has a
relatively gentle downward trend of training error and reaches the
desired accuracy at 955 iterations; The GWO-BP algorithm has the
smoothest decline in training error and reaches the desired accuracy in
1032 iterations. This result indicates that the proposed PCA-GWO-BP
algorithm performs better in training, has the fastest convergence
speed and has better performance. Fig. 9 gives the comparison results of
the absolute errors of the four algorithm models during the prediction
process.
From Fig. 9, the PCA-GWO-BP algorithm has the lowest overall level
of absolute error, with an average absolute error value of 0.0005; which
is below the GWO-BP algorithm’s 0.0012; the SSA-BP algorithm’s
0.0021; and the GWO-SVM algorithm’s 0.0057. From this result, it can
be concluded that in terms of the absolute error dimension, the PCAGWO-BP algorithm’s overall performance is also better than the comparison algorithms. Comparing the above dimensions, it showcases that
the overall prediction performance of the proposed PCA-GWO-BP algorithm is much more excellent than the comparison algorithms, so its
application in network bandwidth prediction can improve the accuracy
of network bandwidth prediction and better facilitate the code rate selection of streaming media products.
4.2. Empirical analysis of streaming media product bit rate selection
techniques
Aiming at analyzing the actual performance of the code rate selection
technology of the streaming media products proposed in the study, the
experimental environment of the study is shown below, which adopts a
high-performance streaming media server that supports a variety of
streaming media protocols such as MPEG- DASH, HLS, etc., and is
capable of adaptively adjusting the code rate according to the network
conditions. Construct network environments with different bandwidths,
delays, and packet loss rates to simulate various situations in the actual
network environment. It is used to monitor the playback quality, bit rate
selection, network conditions and other key indicators of streaming
media products in real time. The experimental dataset is mainly divided
into video dataset and network status dataset. Under the same experimental environment, the code rate selection technology for streaming
Fig. 8. Training effect comparison.
Fig. 9. Comparison results of absolute errors of the four algorithm models.
P. Yang et al.
Journal of Radiation Research and Applied Sciences 17 (2024) 101036
7

### Página 8

media products proposed in the study (Technology 1) and the code rate
selection technology for streaming media products based on SSA-BP
algorithm (Technology 2) and the code rate selection technology for
streaming media products based on GWO-BP algorithm (Technology 3)
are compared and experimented, and the accuracy, real-time, and
impact on the user experience of the code rate selection are used as the
comparison indexes. The accuracy and real-time comparison results of
the three techniques in different datasets are shown in Fig. 10.
From Fig. 10(a), the selection accuracy of technique 1 in the video
dataset is 92.3%, which is significantly higher than that of technique 2
(80.1%) and that of technique 3 (79.5%); moreover, it can be found that
the selection accuracy of technique 1 in the network state dataset is
91.8%, which is significantly higher than that of technique 2 (78.3%)
and that of technique 3 (79.9%). From Fig. 10(b), it can be obtained that
the response time of technology 1 in both data sets is less than 5 s, which
is much lower than that of technology 2 and technology 3. Therefore,
from the above results, it can be concluded that the accuracy and realtime performance of the proposed streaming media product bit rate
selection technology is better than the comparison technology. For
comparing the actual application effect of the three technologies, the
study selected a number of different groups of users to score their
experience and statistics, the scoring statistics are shown in Fig. 11. The
full score is 10 points, the higher the score, the higher the recognition.
Fig. 11showcases that the average score of technique 1 among the
eight groups of users is 9.67; much higher than that of technique 2,
which is 8.43, and that of technique 3, which is 7.88. This result indicates that the performance of the proposed streaming media product
bit rate selection technique based on PCA-GWO-BP algorithm is superior
from the user experience scoring point of view.
5. Conclusion
Smooth playback and user experience of streaming media technology is a major challenge in unstable network environments, and the
combination of MPEG-DASH and AI techniques is considered as an
effective solution. In this research, for improving the accuracy and efficiency of streaming media product bit rate selection, a novel bit rate
selection technique for streaming media products is proposed by fusing
PCA, GWO and BP NN. After algorithm comparison experiments and
empirical analysis, the results show that the training accuracy value of
the hybrid algorithm is 0.945; it is higher than that of the GWO-BP algorithm (0.823), the SSA-BP algorithm (0.812), and the GWO-SVM algorithm (0.785), and the absolute error of the algorithm is only 0.0005,
which is significantly lower than that of the GWO-BP algorithm
(0.0012), the SSA-BP algorithm (0.0021) of GWO-BP algorithm and
0.0057 of GWO-SVM algorithm. Meanwhile, the selection accuracy of
the proposed streaming media product bit rate selection technique is as
high as 92.3%, which exceeds markedly that of 80.1% of technique 2
and 79.5% of technique 3. In summary, it can be concluded that the
streaming media product bit rate selection technique based on PCAGWO-BP algorithm can not only effectively improve the quality and
user experience of streaming media products, but also provide new ideas
and methods for the advancement of the streaming media industry.
However, there are still some shortcomings in this research, such as the
performance of the algorithm may be affected in some extreme network
environments, which requires further research and optimization.
Data availability
The datasets used and/or analysed during the current study available
from the corresponding author on reasonable request.
Fig. 10. Comparison results of accuracy and real-time performance of the three technologies in different data sets.
Fig. 11. Comparison results of user experience scores of the three technologies.
P. Yang et al.
Journal of Radiation Research and Applied Sciences 17 (2024) 101036
8

## 7. Referencias/bibliografía
Referencias detectadas desde la página 9. No se expanden completas aquí para no contaminar la lectura de método; consultar PDF original o raw text si hace falta.

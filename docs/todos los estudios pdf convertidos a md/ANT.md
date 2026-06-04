808 IEEETRANSACTIONSONBROADCASTING,VOL.70,NO.3,SEPTEMBER2024
Learning Accurate Network Dynamics for
Enhanced Adaptive Video Streaming
Jiaoyang Yin , Hao Chen , Member, IEEE, Yiling Xu , Member, IEEE,
Zhan Ma , Senior Member, IEEE, and Xiaozhong Xu , Member, IEEE
Abstract—The adaptive bitrate (ABR) algorithm plays a cru- Background. Early ABR approaches relied on man-
cial role in ensuring satisfactory quality of experience (QoE) in ually fine-tuned heuristics based on network throughput
video streaming applications. Most existing approaches, either
information [3], [4], [5], [6] and receiver states (e.g., play-
rule-based or learning-driven, tend to conduct ABR decisions
back buffer occupancy [7], [8], [9], [10]). In recent years,
basedonlimitednetworkstatistics,e.g.,mean/standarddeviation
of recent throughput measurements. However, all of them lack learning-based ABR approaches, utilizing RL-based neural
a good understanding of network dynamics given the varying engines, have gained popularity. These approaches, including
network conditions from time to time, leading to compromised Pensieve [11], T-Gaming [12], Fugu [13], and GENET [14],
performance, especially when the network condition changes
leverage neural networks for feature extraction and pol-
significantly.Inthispaper,weproposeaframeworknamedANT
icy learning, outperforming fixed rule-based algorithms in
that aims to enhance adaptive video streaming by accurately
learning network dynamics. ANT represents and detects specific time-varying network environments. However, ensuring user
network conditions by characterizing the entire spectrum of QoE across a wide range of dynamic network connec-
network fluctuations. It further trains multiple dedicated ABR tions with unpredictable fluctuations remains challenging for
models for each condition using deep reinforcement learning.
learning-basedalgorithms.Theheterogeneousnatureofaccess
During inference, a dynamic switching mechanism is devised to
networks,includingwirelessandwirednetworkswithvarying
activatetheappropriateABRmodelbasedonreal-timenetwork
condition sensing, enabling ANT to automatically adjust its bandwidth, latency, and buffer capacities, further complicates
controlpoliciestodifferentnetworkconditions.Extensiveexper- thesituation.Additionally,theuser’sscenario,suchasstation-
imental results demonstrate that our proposed ANT achieves aryoronthemove,introducesadditionalvariationsinnetwork
a significant improvement in user QoE of 20.8%-41.2% in
conditions. Existing learning-based algorithms typically train
the video-on-demand scenario and 67.4%-134.5% in the live-
a single model for ABR decisions without adapting to dif-
streaming scenario compared to state-of-the-art methods, across
a wide range of network conditions. ferent network conditions. Consequently, the learned neural
model often compromises across various network conditions,
Index Terms—Network dynamics learning, video on demand,
resultingincompromisedvideoqualityorfrequentrebuffering,
live streaming, adaptive bitrate, reinforcement learning, quality
of experience. ultimately degrading user QoE.
Motivation. To solve this issue, a solution called Oboe [15]
I. INTRODUCTION is proposed to automatically tune video ABR algorithms to
RECENT years have witnessed an exponential increase various network conditions. It detects changes in network
states or conditions by analyzing the average and standard
in the volume of HTTP-based video streaming traf-
deviation (STD) of throughput and adjusts ABR parameters
fic [1], [2]. To assure high-quality service provisioning,
accordingly. However, Oboe’s detection of network condi-
adaptive bitrate (ABR) algorithms have been developed to
tion changes based on limited throughput statistics (average
dynamically select the appropriate bitrate for each video
and STD) may not accurately represent the complex and
chunk,mitigatingthenetworkfluctuationsandachievingsatis-
diverse network conditions encountered in the real world.
factory Quality of Experience (QoE) in time-varying network
Consequently, Oboe may fail to select the most appropri-
connections.
ate ABR parameters. To demonstrate this, we compare the
Manuscript received 8 February 2024; revised 17 April 2024; accepted performance of existing state-of-the-art algorithms, including
24 April 2024. Date of publication 17 May 2024; date of current version
Pensieve [11] and Oboe [15], using a randomly selected
13 September 2024. This work was supported in part by the National
NaturalScienceFoundationofChinaunderGrant62371290,Grant62101241, network trace. Figure 1 illustrates the instantaneous through-
and Grant U20A20185; and in part by the 111 Project under Grant put/bitrate and the overall QoE results. As shown in Figure 1,
BP0719010. (Jiaoyang Yin and Hao Chen contributed equally to this
there are several time slots (between the black dashed lines)
work.)(Correspondingauthor:YilingXu.)
Jiaoyang Yin and Yiling Xu are with the Cooperative Media Network withsimilaraverage(approximately3.11Mbpsforslots1and
Innovation Center, Shanghai Jiao Tong University, Shanghai 200240, China 2, and 3.33 Mbps for slots 3 and 4) and STD (approximately
(e-mail:jiaoyangyin@sjtu.edu.cn;yl.xu@sjtu.edu.cn).
0.90 Mbps for slots 1 and 2, and 0.89 Mbps for slots 3 and
HaoChenandZhanMaarewiththeElectronicScienceandEngineering
School, Nanjing University, Nanjing 210093, Jiangsu, China (e-mail: 4)valuesofthroughput.However,networkthroughputchanges
chenhao1210@nju.edu.cn;mazhan@nju.edu.cn). inthesetimeslotsexhibitdifferentpatterns:slots1and2have
Xiaozhong Xu is with Tencent MediaLab, Palo Alto, CA 94306 USA
low-frequency but significant magnitude changes, while slots
(e-mail:xiaozhongxu@tencent.com).
DigitalObjectIdentifier10.1109/TBC.2024.3396698 3 and 4 have high-frequency but relatively minor magnitude
1557-9611(cid:2)c 2024IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.

YINetal.:LEARNINGACCURATENETWORKDYNAMICSFORENHANCEDADAPTIVEVIDEOSTREAMING 809
|     |     |     |     |     | Contribution. |     | The main | contributions |     | of this | paper | can be |
| --- | --- | --- | --- | --- | ------------- | --- | -------- | ------------- | --- | ------- | ----- | ------ |
Pensieve
Oboe
| )spbM(etartiB |     |     |     |     | summarized | in three | aspects: |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | ---------- | -------- | -------- | --- | --- | --- | --- | --- |
ANT
bandwidth • Improvedcharacterizationofnetworkthroughputdynam-
|     |     |     |     |     | ics. | Instead | of relying | solely | on  | mean | and | standard |
| --- | --- | --- | --- | --- | ---- | ------- | ---------- | ------ | --- | ---- | --- | -------- |
deviationvalues,weproposeusingtheEuclideandistance
|     |     |     |     |     | from          | clustering           | centers      | and             | the | temporal    | change          | pat-     |
| --- | --- | --- | --- | --- | ------------- | -------------------- | ------------ | --------------- | --- | ----------- | --------------- | -------- |
|     |     |     |     |     | tern          | in multi-dimensional |              | raw-throughput  |     |             | measurements    |          |
|     |     |     |     |     | to accurately |                      | characterize | network         |     | throughput  |                 | dynamics |
|     |     |     |     |     | over          | time. This           | approach     | provides        |     | a better    | differentiation |          |
|     |     |     |     |     | of typical    | network              | behaviors.   |                 |     |             |                 |          |
|     |     |     |     |     | • ANT         | framework            | for          | condition-wised |     | multi-model |                 | ABR      |
EoQ
|     |     |     |     |     | control. | We  | introduce | ANT, | a framework |     | that | generates |
| --- | --- | --- | --- | --- | -------- | --- | --------- | ---- | ----------- | --- | ---- | --------- |
Pensieve different ABR control policies for different network con-
Oboe
|     | ANT |     |     |     | ditions. | ANT       | utilizes a | well-designed |               | DNN | for             | recurrent |
| --- | --- | --- | --- | --- | -------- | --------- | ---------- | ------------- | ------------- | --- | --------------- | --------- |
|     |     |     |     |     | network  | condition | detection  |               | and activates |     | the appropriate |           |
(cid:415)me(s)
|     |     |     |     |     | ABRmodelaccordingly.ThisenablesANT |     |     |     |     |     | tomakebetter |     |
| --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | ------------ | --- |
Fig.1. Illustrationofthenecessityforaccuratenetworkthroughputlearning. ABR decisions for ensuring satisfactory QoE across a
|     |     |     |     |     | wide         | range | of network          | conditions. |     |       |        |         |
| --- | --- | --- | --- | --- | ------------ | ----- | ------------------- | ----------- | --- | ----- | ------ | ------- |
|     |     |     |     |     | • Evaluation |       | through simulations |             | and | field | tests. | We val- |
changes. Both Pensieve, with a single model, and Oboe, with idate the effectiveness of ANT through simulations and
its auto-tuning mechanism based on average/STD throughput field tests. We compare ANT against state-of-the-art
values,struggletodifferentiatebetweenthesedifferenttrends. ABR algorithms using public network trace datasets
Pensieve can only rely on a general ABR model trained on and a proprietary dataset collected from the large-scale
allnetworktraces,whileOboecontinuestochoosethesecond Tencent video hosting system distributed worldwide. In
ABR model (3-6 Mbps, depicted in Section IV-D) before both video-on-demand (VoD) and live-streaming (LS)
and after the change point of network conditions (around scenarios,ANT demonstratessignificantimprovementsin
180 seconds). As they are unable to accurately sense network QoE compared to existing approaches.
conditions and select the appropriate ABR model in a timely The remainder of the paper is organized as follows.
manner, both Pensieve and Oboe experience greater QoE Section II reviews related work on ABR algorithms and
degradation after the change point. network dynamics learning. Section III introduces the design
Method.Inthispaper,weproposeANT toenhanceadaptive details of the proposed ANT, including its architecture, key
video streaming by accurately learning network throughput modules, and implementation. The experimental results and
dynamics across a wide range of network conditions. Unlike analysis for ANT are presented in Section IV. The discussion
traditionalmethodsthatrelyonsimplemean/STDvalues,ANT and conclusion of this work can be found in Sections V
utilizes a combination of the Euclidean distance from a group and VI, respectively.
| of           | clustering | centers         | and temporal change  | patterns extracted |     |     |                 |     |     |     |     |     |
| ------------ | ---------- | --------------- | -------------------- | ------------------ | --- | --- | --------------- | --- | --- | --- | --- | --- |
| from         | neural     | networks        | of multi-dimensional | raw-throughput     |     |     |                 |     |     |     |     |     |
|              |            |                 |                      |                    |     |     | II. RELATEDWORK |     |     |     |     |     |
| measurements |            | to characterize | the network          | condition. Toward  |     |     |                 |     |     |     |     |     |
this, we first classify a large-scale dataset of network trace ABR algorithms with a fixed model. Existing state-of-the-
segments (NTS) collected in the real world into multiple art ABR algorithms can be divided into two main categories:
(e.g., five) clusters by using the classic K-means algorithm. rule-based algorithms [3], [4], [5], [6], [7], [8], [9], [10],
Each cluster represents a distinct network behavior class and [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26],
is assigned a unique network condition number for ANT [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37]
as the label. Recognizing that the temporal dynamics of and learning-based algorithms [11], [15], [38], [39], [40],
network throughput significantly impact ABR performance, [41], [42], [43], [44], [45], [46], [47], [48], [49], [50],
we additionally leverage a deep neural network (DNN) to [51], [52], [53], [54].
learn the temporal change patterns from the sequence of raw The rule-based algorithms can be further classified into
throughput data. For each network condition, ANT trains a rate-based,buffer-based,andhybrid-controlapproaches.Rate-
dedicated reinforcement learning (RL)-based model for ABR based algorithms [3], [4], [5], [6], first try to predict the
decisions using the corresponding cluster of network traces. available network bandwidth and then select the highest
This allows ANT to learn and adapt to specific patterns available bitrate below the estimated bandwidth. For example,
of network dynamics and improve decision-making based CS2P [5] focused on the optimization of network bandwidth
on past experiences. During inference, ANT employs the predictionproblemstoimproveinitialandsubsequentadaptive
aforementionedtrainedDNNtorecurrentlydetectthenetwork streaming. However, it is still challenging to predict a specific
conditionandselectstheappropriateABRmodelaccordingly. value for network bandwidth in practice, resulting in poor
Byeffectivelyadaptingtodifferentnetworkbehaviorsandpat- performance for this type of ABR algorithms. Buffer-based
terns, ANT can provide optimal video streaming experiences algorithms [7], [8], [9], [10] aim to maintain the playback
for users in diverse network environments. buffer occupancy at a pre-configured level to guarantee the
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore.  Restrictions apply.

810 IEEETRANSACTIONSONBROADCASTING,VOL.70,NO.3,SEPTEMBER2024
fluency of video playback. Generally, these buffer-based
algorithms can better avoid rebuffering to some extent, but
they suffer from low video quality due to their conservative
bitrate selections. To overcome the shortcomings of these
two techniques, some hybrid-control ABR algorithms attempt
to make bitrate decisions based on both network throughput
prediction and buffer occupancy simultaneously. For example,
MPC [27] estimated the future throughput by calculating the
harmonic mean of the throughput values from the last five
Fig.2. OverallarchitectureofANT-poweredadaptivevideostreaming.
chunks and attaching a discount factor, then went through all
bitrate options and selects the one that maximizes a given fasterandmoreaccurateconvergence.Additionally,[14], [53]
QoEmetric.However,MPCalsoreliesonaccuratethroughput introduced automatic curriculum learning, which involved
prediction,whichcanencountersimilarproblemstorate-based a gradual migration of training from a simple to a com-
algorithms. plex network environment, significantly improving training
Due to the limitations of rule-based algorithms, recent performance and model generalization. However, these works
research has shifted towards learning-based hybrid control mainly rely on limited throughput statistics (i.e., average and
approaches, such as the reinforcement learning based [11], STD) to assess network dynamics and can easily lead to
[39], [40], [55], imitation learning based [41], and hybrid inaccurate recognition of network condition changes, finally
learning-heuristic algorithms [38]. Pensieve [11] was a pio- degrading the ABR performances.
neering work that trained a neural network model using Learning network dynamics. In addition to optimizing
reinforcementlearningtomakebitratedecisions,whichsolely adaptive bitrate (ABR) algorithms, researchers have also
relied on observations collected from video players. In con- focused on learning network dynamics to enhance video
trast to Pensieve, Comyco [41] trained its neural network transmission performance. For example, in [60], a flow-based
model using imitation learning, resulting in a significant throughput classification method was proposed to predict the
reduction in training time while maintaining the same QoE bitrate of traffic flow based on factors such as IP address,
level. Stick [38] integrates a heuristic ABR algorithm with a network prefix, protocol, and start timestamp. Another study
learning-based method to enhance its performance and reduce by [61] conducted a systematic study for various prediction
computational overhead. It achieves this by training a neural algorithms and analyzed their performance when applied in
networktodynamicallycontrolthebufferthresholdparameter the prediction of throughput in mobile networks, promoting
of an existing buffer-based algorithm. Taking advantage of the employment of throughput prediction in ABR algorithms.
the capabilities of neural networks in feature extraction and Other related works, such as [13], [62], [63], [64], have
policy learning, these learning-based algorithms have shown explored efficient methods for predicting throughput or band-
superiorperformancecomparedtoearlyrule-basedalgorithms width and utilizing learned network dynamics to optimize
that utilize fixed heuristics across various network conditions. adaptive video streaming. However, these approaches often
However,theyoftenrelyonasingleneuralnetworkmodelfor face challenges in capturing comprehensive network statis-
ABR decisions and lack specialization for different network tics across different layers and accurately predicting specific
conditions, resulting in compromised performance. throughputorbandwidthvalues.Thislimitstheireffectiveness
Auto-tuning ABR parameters to network conditions. andefficiencywhenappliedtoenhanceapplication-layerABR
ABR algorithms that rely on a single model or fixed algorithms.
parametersoftenstruggletoadapttothecomplexitiesofmod-
ern network conditions, resulting in significant performance
III. ANT DESIGN
degradation during video streaming. To address this issue,
State-of-the-art ABR algorithms attempt to train a general
several approaches have been proposed. Oboe [15] proposed
neural network model for bitrate decisions to adapt to a wide
to auto-tune the parameters of ABR algorithms based on
range of network conditions. However, during training, this
network conditions. It detected changes in network states
general model easily converges to a compromised policy with
using Bayesian change point detection algorithms based on
average performance across allconsidered network conditions
average and standard deviation of throughput measurements,
rather than achieving optimal performance. To this end, we
and then dynamically selected appropriate parameters for the
propose a condition-wised multi-model framework, named
ABR algorithm to adapt to the current network condition.
ANT,tooptimizetheperformanceofadaptivevideostreaming
Other approaches, such as [56] and [57], introduced meta-
under each network condition.
reinforcement learning to perceive changes in network states
In this section, we will introduce the design details of
andtunetheparametersofthepolicynetwork.Inthisway,the
ANT,includingtheoverallarchitecture,keymodules,andtheir
generalization of the neural network can be improved when
corresponding implementation.
encountering dynamic network conditions. In [58] and [59],
federated reinforcement learning was adopted to enable their
A. Architecture
neural networks to handle various network conditions and
user-end characteristics. Taking advantage of the idea of The overall architecture of ANT-powered adaptive video
categorizationandaggregation,thepolicynetworkcanachieve streaming is shown in Figure 2. On the media server, videos
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.

YINetal.:LEARNINGACCURATENETWORKDYNAMICSFORENHANCEDADAPTIVEVIDEOSTREAMING 811
are segmented into a series of time-aligned chunks, each of
which is further encoded at several bitrate levels for requests.
During video streaming, the ANT server decides to request
each video chunk at which bitrate based on network statistics
and client-side playback status. Then the client-side video
player downloads the video chunk at the decided bitrate and
stores them in a playback buffer for video decoding and
playing. This process continues until either the end of the
video is reached or the user chooses to quit the streaming
session.
For the ANT server, two key modules have been developed Fig.3. Illustrationofthetraceaggregationmechanism.
to support superior-performance ABR decisions across dif-
ferent network conditions: network condition detection and
condition-wised multi-model ABR decision. In the network which represents the most frequent network condition across
condition detection module, a one-dimensional convolutional all segments. However, if the frequency of the most dominant
neural network (1D-CNN) model is trained to accurately network condition does not exceed a predefined threshold h,
detect the network condition by learning and recognizing we mark the trace as “uncertain” according to Eq. (5). This
the temporal change pattern present in historical throughput accounts for cases where the network condition is ambiguous
measurements. The multi-model ABR decision module stores or lacks a clear majority.
⎧ ⎫
several RL-based ABR models, each of which is pre-trained
⎪⎨ ⎪⎬
using a large dataset of throughput traces collected under
similar network conditions. Based on the output from the trace= ⎪⎩(cid:8) x1 ,x2 , (cid:9) . (cid:10) ..,xm(cid:11) ,x (cid:8)m+1 , (cid:9) . (cid:10) ..,x2m(cid:11) ,...,x (cid:8)n−m+1(cid:9) , (cid:10) ...,x (cid:11)n⎪⎭
network condition detection module, one of the pre-trained Segment1 (tsecond) Segment2 (tsecond) Segmentp (tsecond)
(3)
models is dynamically selected to make adaptive bitrate
(ABR) decisions. The bitrate decision is made by taking into labelsegment ={l1 ,l2 ,...,lp }
account both network statistics and player status. The general =K−means.fit(Segment).labels
procedure for the proposed architecture can be formulated as
follows:
,
⎧
∈[0,k−1] (4)
⎨
con a d c it t i i o o n n = = f f 1D− (cid:2)C s N ta N t ( e through , p s u ta t h te istorical , ) condition (cid:3) ( ( 2 1 ) ) labeltrace = ⎩ l u i n , certain, i i f f n n u u m m l li i / / p p ≥ < h h,
ABR network player li ∈labelsegment (5)
B. Network Condition Detection
CNN model for condition detection. Since we adopt
Different from existing approaches that rely on simple K-means as the clustering algorithm, the intuitive idea
statistical features of the throughput data like average and is to perform condition detection directly based on the
STD values, our network condition detection module utilizes Euclidean distance. However, due to the limited amount of
a powerful CNN model to extract comprehensive features data used for clustering, only using the Euclidean distance
from raw throughput data, enabling it to learn and accurately from a group of fixed centers for condition detection can
determine the current network condition. This information is lead to inaccurate category judgments in real situations.
thenusedtodrivetheselectionoftheappropriatemodelinthe Specifically, when unseen network fluctuations occur, even
subsequentcondition-wisemulti-modelABRdecisionmodule. subtlechangesmayleadtolargeshiftsindistancecalculations.
Label generation with unsupervised clustering. Existing To address this issue, we propose a CNN model that learns
network datasets often lack reliable labels indicating real the temporal change patterns within a series of network
network conditions, which poses a challenge for training and throughput data. By extracting and utilizing these patterns as
validating neural networks in our model. To overcome this features, our approach enables more accurate condition detec-
issue, we propose a trace aggregation mechanism that dis- tion in real transmission environments. Experimental results
tinguishes network conditions based on the distance between presented in Section IV-E1 validate the effectiveness of our
network throughput traces (as illustrated in Figure 3). The approach.
original network traces are first split into several equal-length Using network trace segments and their corresponding
segments that contain throughput information in t seconds conditionlabelsastrainingsamples,wetrainaneuralnetwork
or m throughput measurements, as shown in Eq. (3). Then to detect the current condition in this module. This neu-
K-means [65], a classic clustering algorithm, is adopted to ral network extracts features from the input of historical
cluster these trace segments based on the Euclidean distance throughputmeasurements.Theneuralnetworkstructureofour
between them. As a result, we obtain k clusters (as shown in proposed model for network detection model is depicted in
Eq. (4)), where each cluster contains segments with similar Figure 4.Thebackboneofournetworkisa1D-CNN,whichis
network behaviors or conditions. We denote the label of the well-suitedforhandlinghigh-dimensionalnetworkthroughput
i-thsegmentinthesamenetworktraceasl.Finally,theentire data.Theinputtotheneuralnetworkisasequenceofhistorical
i
network trace can be assigned a label, denoted as label , networkthroughputdata,andtheoutputisthedetectedcurrent
trace
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.

812 IEEETRANSACTIONSONBROADCASTING,VOL.70,NO.3,SEPTEMBER2024
Fig.4. Theneuralnetworkstructureoftheproposedmodelfornetworkconditiondetection.
network condition. In the neural network, three convolutional • Residual structure. To address the issues of feature
layersaredevisedtoextracthierarchicalfeatures.Theselayers submerging of the shallow layer and gradient van-
have the same structure but differ in their hyperparameters, ishing/explosion in deeper CNNs, we incorporate the
such as the size of the convolutional kernel and the number residual structure [66] into the backbone. This structure
of output channels. To improve feature extraction capability transmits shallow features directly to deeper layers and
and condition detection accuracy, we add several optimized combines them with abstract features, enabling more
operations to the backbone network. efficient and stable training.
• Multiple perceptual field. Considering the diverse feature • Normalization and dropout. In addition to the optimized
scalespresentinnetworkthroughputdata,weintroducea operations mentioned earlier, we employ two normal-
multi-perceptual-field mechanism to our neural network. ization techniques to further enhance the performance
This mechanism incorporates multi-scale convolutional of our neural network: mean standardization and batch
kernels within each convolutional layer, allowing for the normalization. These two normalization operations lead
effective extraction of features at different scales from to faster convergence and improved training stability.
the network throughput data. Specifically, we use three Furthermore,dropoutisutilizedinfullyconnectedlayers
distinct convolutional scales in each layer, namely 3×1, to regularize the model and prevent overfitting during
5×1, and 7×1 kernels, and then concatenate features training.
from different scales of convolution operation in the We use the binary cross-entropy loss function, as shown
channel dimension. in Eq. (6), to train the CNN model for network condition
• Channel shuffle. To improve the stability and generaliza- detection.yandyˆ (inone-hotformat)representthelabelofthe
tion of our neural model, we adopt the channel shuffle network condition and the output of this model, respectively.
(cid:2) (cid:3) (cid:2) (cid:3)
operation to disturb the original order of concatenated
L yˆ,y =− ylogyˆ+(1−y)log(1−yˆ) (6)
feature channels obtained from the multi-scale convo-
lution operation. The feature channels are first divided Network condition inference.Aftercompletingthetraining
into three equal-sized groups. Then, the feature matrix is of the detection model, the current segment’s network con-
reshaped, transposed, and reshaped to make the feature dition can be inferred using previous raw throughput data as
channels shuffled. input.
• Attention mechanism. Since different feature channels ItisworthmentioningthateachABRmodelistrainedusing
contribute differently to the final output, we integrate a large number of traces that correspond to the same specific
a squeeze-and-excitation (SE) module into the network network condition. Thus we have devised a sliding window-
backbone. The SE module acts as an attention mech- based confidence mechanism for the accurate detection of
anism, assigning weights to the feature channels based trace-levelnetworkconditions,enablingeffectiveselectionsof
on their importance. The SE module consists of two the appropriate ABR model in the subsequent module. The
branches: one branch transmits the original signal, while chunk-levelconditiondetectionisconductedevery20seconds,
the other branch performs the SE operation. After per- and the results at each step are queued into a sliding window.
forming the SE operation, each channel is assigned a The chunk-level result is only accepted as the trace-level
weight value based on its importance. These weight networkconditionifitmatchestheresultsfromtwooutofthe
values are then multiplied element-wise with the corre- three previous time slots. Otherwise, the “uncertain” status is
sponding channels in the original signal. designated as the trace-level network condition. In addition,
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.

YINetal.:LEARNINGACCURATENETWORKDYNAMICSFORENHANCEDADAPTIVEVIDEOSTREAMING 813
sizes3×1,5×1,and7×1.Thenumberofoutputchannelsfor
eachCNNlayerwas64×3,128×3,and256×3respectively.
The kernel size in the pooling layers we chose was 2×1.
Thefirstlayerofthefullyconnectednetworkhad256neurons
and 128 neurons were contained in the second layer. For all
convolution operations and pooling operations, we set stride
with1andaddapaddingoperationtomaintainthedatawidth.
As for other hyper-parameters, we set the learning rate as
0.0001 and batch size as 80 in the training phase. For the
Fig.5. Illustrationofcondition-wisedmulti-modelABRdecisionmodule.
RL-based ABR decision module, we used 16 RL agents to
learn the control policy for bitrate adaptation. In the state
whenthevideostreamingsystemrunsintheinitialperiod(i.e., input, we considered the past eight observations from the
60secondsinthebeginning)andthereisnotenoughhistorical environment,whichwerenormalizedbeforebeingfedintothe
throughput data to perform condition learning, the general neural network. Both the actor network and the critic network
status corresponding to all various network traces is selected consistedofone1D-CNNlayerwithakernelsizeof4and128
until the input requirement of the confidence mechanism is output channels, as well as a fully connected layer with 128
met. neurons. The learning rates for the actor and critic networks
weresetto0.0001and0.001,respectively.Theentropyweight
of the actor network was set to 0.5. We used a batch size of
C. Condition-Wised Multi-Model ABR Decision
100 for training. The training and testing of neural networks
Multi-model switching mechanism for ABR decision. As
wereonaUbuntu16.04serverequippedwithIntelXeonCPU
shown in Figure 5, the condition-wised multi-model ABR
E5-2683v4@2.10GHzandNvidiaGeForceGTX1080Ti11G
decision module is constructed with multiple reinforcement
GPU.
learning(RL)basedABRmodels,whichsharethesameneural
network architecture but different model parameters. At a
set interval, one of these trained ABR models is selected to IV. EXPERIMENTRESULTSANDANALYSIS
make bitrate decisions according to the detection results by A. Experiment Setup
thenetworkconditiondetectionmodule.Fordifferentnetwork
Similar to Pensieve [11], we used a simulator with a 60-
conditions, there is a corresponding model trained specifically
secondbuffercapacitytoconducttrace-drivenvideostreaming
for that condition using similar network traces to make ABR
sessions for training and testing all the schemes considered.
decisions.ThisensuresthatANT canadaptitsdecision-making
The network traces, video information, and baselines used in
process to different network conditions, providing optimal
this paper are as follows.
streaming performance.
Network traces.Sinceitistime-consumingto“experience”
TrainingRL-basedABRmodels.Withthetraceaggregation
video downloads in the real-world streaming environment,
mechanism described in Section III-B, each ABR model can
we conducted simulations over a wide range of network
be trained individually using network traces labeled with the
traces in the training and testing phases. These traces were
same condition. During the training of each ABR model, the
collected from public datasets (including a broadband dataset
learning agent collects various observations from the video
provided by FCC [68], a 3G/HSDPA mobile dataset collected
streaming environment, which include network statistics such
in Norway [69], a 4G/LTE bandwidth from Belgium [70], a
as bandwidth or throughput, as well as player status at the
mixeddatasetprovidedinOboe[15],andanothermobiletrace
client side like buffer occupancy. These observations are
datasetprovidedintheACMmultimediagrandchallenge[71])
then fed into the RL neural network, prompting it to select
and a Tencent dataset (including WiFi network traces and
the appropriate bitrate for the next chunk. After making a
3G/4Gnetworktraces).TheTencentdatasetwasaproprietary
decision, the environment transitions to a new state, and the
network trace dataset that was collected from the Tencent
agent receives a reward. The RL agent learns to maximize
videoplatform,inwhichthevideosexperiencedactualqueries
the expected cumulative discounted reward by continuously
and downloads. There were nearly 2000 traces in the dataset,
interacting with the video streaming environment.
each of which contained about 30 minutes of throughput data
Similar to the approach used in Pensieve [11], we employ
onaverage.Theaveragethroughputofeachtracerangedfrom
the state-of-the-art asynchronous advantage actor-critic (A3C)
less than 1Mbps to more than 10Mbps. Benefiting from user
method [67] as the basic training algorithm. The state input,
ends distributed widely throughout the world, these network
neural network structure, and reward function remain consis-
traceswerecollectedfromChina,Philippines,Thailand,India,
tent with those used in Pensieve’s framework.
and Indonesia. The network types of user ends included Wifi
and 3G/4G, which could cover a wide range of network
D. Implementation
conditions and application scenarios. In the network trace
We implemented the CNN-based network condition detec- file, time information (second) and corresponding through-
tion module and the RL-based ABR decision module using put/bandwidth information (Mbit per second) were contained.
Tensorflow. For the neural network in the network condition We randomly divided all 2658 traces into the training set and
detection module, we used three types of CNN filters with thetestingset,bytheproportionof80%and20%,respectively.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.

814 IEEETRANSACTIONSONBROADCASTING,VOL.70,NO.3,SEPTEMBER2024
The network throughput segments were generated in t-second
(t=20) duration, and the classification threshold in the trace
aggregation mechanism was set as 2/3. Consequently, ANT
conducted network condition detection every 20 seconds.
Video information. We collected a diverse set of videos
from the Tencent video platform, encompassing various types
of content such as newscasts, sports events, movies, and
shows. These videos were encoded by the NVENC codec
at bitrates in {135, 340, 835, 1350, 2640} Kbps according
to the Tencent video platform settings. Additionally, these
Fig.6. SSEandDBIresultsoverdifferentkvalues.
videos were divided into 200 chunks, with each chunk lasting
approximately4seconds,resultinginatotalplaybackduration
TABLEI
exceeding 10 minutes.
AVERAGEANDSTANDARDDEVIATIONVALUEOF
Baselines. In the evaluation, we compared our approach THETHROUGHPUTFOREACHCONDITION
with two heuristic ABR algorithms: buffer-based (BB) [7]
and MPC [27], as well as two state-of-the-art learning-based
ABR algorithms: Pensieve [11] and Oboe [15]. For the Oboe
algorithm, we trained 5 neural network models for ABR
decisionsusingnetworktraceswithdifferentaveragethrough-
put ranges: 0-3Mbps, 3-6Mbps, 6-9Mbps, 9-12Mbps, and
over 12Mbps. We retrained the RL-based models of Pensieve
and Oboe according to our specific settings. The validation
lag as much as possible. The last term penalizes the quality
resultsdemonstratedthattheseretrainedmodelsachievedQoE
fluctuation between adjacent chunks to favor smoothness.
improvementscomparabletotheoriginalmodelsin[11], [15],
when compared to rule-based methods. The training details
for each model were the same as the proposed ANT described B. Network Trace Clustering Performance
in Section III-C. During network trace clustering, the number of clusters k
QoE metrics.WeadoptedthegeneralQoEmetricproposed has a significant impact on the performance of the K-means
in MPC [27], which was defined as algorithm and the final ABR decision. To this end, we con-
ducted the K-means clustering with the parameter k varying
(cid:15)N (cid:15)N N(cid:15)−1 from 2 to 8 and found the best one on the metrics of
QoE = q(R n )−µ T n − |q(R n+1 )−q(R n )| (7) the sum of squared error (SSE) and Davies-Bouldin index
n=1 n=1 n=1 (DBI). The results using different values of k are shown in
Figure 6.
for a video with N chunks. The QoE metric is an objective The SSE value gradually decreases with increasing number
indicator used to assess the quality of the viewing experi- of clusters k. When k approaches the most appropriate value,
ence. This study considers multiple optimization objectives, the downward trend will slow down until convergence. In
including maximizing bitrate, minimizing rebuffering time, contrast, the DBI value gradually increases with increasing
and maximizing smoothness. The general QoE metric is numberofclusters,asDBIcalculatestheratioofthedegreeof
defined in Eq. (7), where R n represents the video bitrate, and separationbetweenclusterstothedegreeofaggregationwithin
q(R n ) is the mapping function that converts the bitrate to the a cluster. Given these two indicators, we found the turning
perceived user quality. As revealed in [72], the relationship point where the trend slowed down occurred at k = 5. Thus,
between quality and bitrate is approximately linear in the low wesetthenumberofclustersas5fortracesegmentsand6for
bitratestage.Moreover,thelinearQoEmetric/rewardfunction entire traces considering an additional “uncertain” condition.
can facilitate the derivation and gradient updating during the The average value and STD of throughput under each con-
trainingphaseoftheRLmodel,leadingtoeasierconvergence dition were calculated and reported in Table I. Additionally,
in the complex environment, compared to other non-linear we plotted the throughput distribution of each condition at
forms. Considering that the maximum bitrate of the video both segment and trace levels in Figure 7. From these results,
content adopted in this paper is 2.64Mbps, it is acceptable we found that the different conditions of the network traces
to evaluate the viewing quality using the linear QoE metric. were well separated, which verified the effectiveness of the
Therefore, in this work, we set the linear form q(R n ) = R n , proposed trace aggregation mechanism.
whichisthesameastheapproachusedinMPC,Pensieve,and
Oboe.T representstherebufferingtimeforeachvideochunk,
n
andµisthecorrespondingpenaltycoefficient.Therebuffering C. Network Condition Detection Performance
timereferstothetimeintervalfromthebufferdepletiontothe Through the network trace clustering, we obtained numer-
restorationofvideoplayback.SimilartoPensieve,therebuffer ous throughput trace segments and corresponding condition
penalty coefficient was configured as the maximum video labels as samples. These samples were randomly divided into
bitrateof2.64Mbpsinthiswork,inordertominimizeviewing a 80% training set and a 20% testing set. The training of the
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.

YINetal.:LEARNINGACCURATENETWORKDYNAMICSFORENHANCEDADAPTIVEVIDEOSTREAMING 815
|     |     |     |     |     |     |     |     |     | P   | O   |     |     | P   | O   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | P   | O   |     |     | P   | O   |     |
Fig.7. Thethroughputdistributionofeachcondition.
TABLEII
HYPER-PARAMETERSSETTINGSANDTESTINGRESULTSOF
BASELINESANDOURCNN-BASEDDETECTIONMODEL
Fig.8. PerformancecomparisonontheconsideredQoEmetricsunderboth
publictracesandTencenttracesfortheVoDscenario.
|     |     |     |     |     |     |     | 1.0 | BB       |     |     | 1.0     | BB       |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ------- | -------- | --- | --- | --- |
|     |     |     |     |     |     |     |     | MPC      |     |     |         | MPC      |     |     |     |
|     |     |     |     |     |     |     | 0.8 | Pensieve |     |     | 0.8     | Pensieve |     |     |     |
|     |     |     |     |     |     |     |     | Oboe     |     |     |         | Oboe     |     |     |     |
|     |     |     |     |     |     |     |     | ANT      |     |     |         | ANT      |     |     |     |
|     |     |     |     |     |     |     | 0.6 |          |     |     | FDC 0.6 |          |     |     |     |
FDC
|           |         |     |         |                     |     |           | 0.4 | Be(cid:425)er |               |     | 0.4 |     |               |               |     |
| --------- | ------- | --- | ------- | ------------------- | --- | --------- | --- | ------------- | ------------- | --- | --- | --- | ------------- | ------------- | --- |
|           |         |     |         |                     |     |           | 0.2 |               |               |     | 0.2 |     |               | Be(cid:425)er |     |
|           |         |     |         |                     |     |           | 0.0 |               |               |     | 0.0 |     |               |               |     |
|           |         |     |         |                     |     |           |     | 2             | 1 0           | 1 2 |     | 0.5 | 1.0           | 1.5 2.0       | 2.5 |
|           |         |     |         |                     |     |           |     |               | QoE           |     |     |     | Bitrate(Mbps) |               |     |
|           |         |     |         |                     |     |           | 1.0 |               |               |     | 1.0 |     |               |               |     |
|           |         |     |         |                     |     |           | 0.8 |               |               |     | 0.8 |     |               |               |     |
| CNN-based | model   | for | network | condition detection |     | converged |     |               |               |     |     |     |               |               |     |
| after 100 | epochs. |     |         |                     |     |           | 0.6 |               |               |     | 0.6 |     |               |               |     |
|           |         |     |         |                     |     |           | FDC |               | Be(cid:425)er |     | FDC |     |               |               |     |
To better evaluate our proposed CNN-based detection 0.4 BB 0.4 BB
model, we also trained a fully connected network (FC), a MPC MPC
|     |     |     |     |     |     |     | 0.2 |     |     | Pensieve | 0.2 |     | Be(cid:425)er |     | Pensieve |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ------------- | --- | -------- |
|     |     |     |     |     |     |     |     |     |     | Oboe     |     |     |               |     | Oboe     |
convolutional-1D(CONV-1D)networkonly,along-short-term 0.0 ANT 0.0 ANT
memory (LSTM) network, and a gated recurrent unit (GRU) 0.0 0.2 Rebuffering(s) 0.4 0.6 0.8 1.0 0.0 0.2 Smoothness(Mbps) 0.4 0.6 0.8
| network | for performance |     | comparison. | These | models | were |     |     |     |     |     |     |     |     |     |
| ------- | --------------- | --- | ----------- | ----- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.9. FinalCDFcurveunderpublictraces.
| trained   | and tested | using | the same      | dataset         | as our | CNN-based   |     |     |     |     |     |     |     |     |     |
| --------- | ---------- | ----- | ------------- | --------------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| detection | model.     | The   | corresponding | hyperparameter  |        | settings    |     |     |     |     |     |     |     |     |     |
| for each  | considered | model | were          | listed in Table | II.    | The testing |     |     |     |     |     |     |     |     |     |
accuracy results were also reported in the table. diverse network traces in the testing dataset. The results were
It can be found that our model achieves the best detection shown in Figure 8 to Figure 10.
|           |          |         |       |               |     |             | As  | shown | in Figure | 8, the | proposed | ANT | achieves | the | best |
| --------- | -------- | ------- | ----- | ------------- | --- | ----------- | --- | ----- | --------- | ------ | -------- | --- | -------- | --- | ---- |
| accuracy, | reaching | 98.56%. | While | the baselines |     | fail to get |     |       |           |        |          |     |          |     |      |
a satisfactory accuracy, all below 75%. The superiority in QoE performance compared to baselines, including heuristic
methods(BBandMPC)andlearning-basedmethods(Pensieve
| detection | accuracy | comes | mainly | from the | multi-perceptual |     |     |     |     |     |     |     |     |     |     |
| --------- | -------- | ----- | ------ | -------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
field mechanism, channel weight learning, and residual struc- and Oboe), under both the public and Tencent network traces.
ture in the proposed CNN-based model. These results also Specifically, ANT achieves 1.52 (1.79) of average QoE for
|              |     |                   |     |           |         |           | each | video | chunk under | the | public | (Tencent) | network |     | traces, |
| ------------ | --- | ----------------- | --- | --------- | ------- | --------- | ---- | ----- | ----------- | --- | ------ | --------- | ------- | --- | ------- |
| demonstrated |     | the effectiveness |     | of adding | related | optimized |      |       |             |     |        |           |         |     |         |
operations to baseline network architectures. which is 31.07% (12.65%) higher than that of the best state-
With the ability to accurately detect current network condi- of-the-artOboe.Comparedtotheresultsonthepublicdataset,
|           |                |     |           |                 |     |           | all | considered | ABR | algorithms | can | achieve | higher | QoE | on  |
| --------- | -------------- | --- | --------- | --------------- | --- | --------- | --- | ---------- | --- | ---------- | --- | ------- | ------ | --- | --- |
| tions and | the confidence |     | mechanism | for trace-level |     | condition |     |            |     |            |     |         |        |     |     |
inference, the network condition detection module can effec- the Tencent dataset. This is because the average bandwidth
|     |     |     |     |     |     |     | of Tencent |     | traces is | significantly |     | greater | than | that of | public |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | ------------- | --- | ------- | ---- | ------- | ------ |
tivelydrivethemodelswitchinginthesubsequentmulti-model
ABR decision module for better bitrate decisions based on traces,supportingahigherbitrateutilityinvideostreamingas
historical throughput measurements. shown in Figure 8. Along with the higher average bandwidth,
|     |     |     |     |     |     |     | the  | STD of  | bandwidth  | in       | the Tencent |     | dataset  | is also     | larger |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------- | ---------- | -------- | ----------- | --- | -------- | ----------- | ------ |
|     |     |     |     |     |     |     | than | that in | the public | dataset, | leading     | to  | frequent | rebuffering |        |
D. Overall QoE Performance eventsforallconsideredalgorithms.Forthesamereasons,the
Now we evaluated the performance of ANT for bitrate QoE improvement of ANT gained over other algorithms on
adaptation on the considered QoE metric and its individual the Tencent dataset is less than that on the public dataset.
components, including bitrate utility (in Mbps), rebuffering To better understand the QoE gains obtained by ANT, we
penalty(inseconds),andsmoothnesspenalty(inMbps),under analyzed its performance on the individual components in the
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore.  Restrictions apply.

| 816                            |               |     |              |               | IEEETRANSACTIONSONBROADCASTING,VOL.70,NO.3,SEPTEMBER2024 |     |     |     |          |     |     |     |
| ------------------------------ | ------------- | --- | ------------ | ------------- | -------------------------------------------------------- | --- | --- | --- | -------- | --- | --- | --- |
| 1.0 pppeeeBnnnBsssiiieeevvveee |               |     | 1.0 BB       |               |                                                          |     |     |     | 1.0      | ANT |     |     |
| oobbMooeePC                    |               |     |              |               |                                                          |     |     |     | ANT-DIST |     |     |     |
| AANNTT                         |               |     | MPC          |               |                                                          |     |     |     |          |     |     |     |
| 0.8 MMPPPCCensieve             |               |     | 0.8 Pensieve |               |                                                          |     |     |     | 0.8      |     |     |     |
| bbuuOffffbeerro__bbeaasseedd   |               |     | Oboe         |               |                                                          |     |     |     |          |     |     |     |
| ANT                            |               |     | ANT          | Be(cid:425)er |                                                          |     |     |     | 0.6      |     |     |     |
| 0.6                            | Be(cid:425)er |     | 0.6          |               |                                                          |     |     |     |          |     |     |     |
| FDC                            |               |     | FDC          |               |                                                          |     |     |     |          |     |     |     |
|                                |               |     | 0.4          |               |                                                          |     |     |     | 0.4      |     |     |     |
0.4
0.2
| 0.2 |     |     | 0.2 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.0
| 0.0     |     |       | 0.0           |             |          |           |             |          |          |     |             |     |
| ------- | --- | ----- | ------------- | ----------- | -------- | --------- | ----------- | -------- | -------- | --- | ----------- | --- |
| 12 10 8 | 6 4 | 2 0 2 | 0.5 1.0       | 1.5 2.0 2.5 |          |           |             |          | 3        | 2 1 | 0           | 1 2 |
|         | QoE |       | Bitrate(Mbps) |             |          |           |             |          |          |     |             |     |
|         |     |       |               |             | Fig. 11. | Comparing | the default | ANT with | ANT-DIST | on  | the average | QoE |
| 1.0     |     |       | 1.0           |             |          |           |             |          |          |     |             |     |
andfullCDFofQoEunderunseennetworktraces.Theaverageperformances
| 0.8 |     |     | 0.8 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
areshownontheleftandtheCDFperformancesareshownontheright.
| 0.6 | Be(cid:425)er |          | 0.6 | Be(cid:425)er |                  |     |          |         |           |       |     |     |
| --- | ------------- | -------- | --- | ------------- | ---------------- | --- | -------- | ------- | --------- | ----- | --- | --- |
| FDC |               |          | FDC |               |                  |     |          |         |           |       |     |     |
| 0.4 |               | BB       | 0.4 | BB            |                  |     |          |         |           |       |     |     |
|     |               |          |     |               | model selections |     | in Table | III for | Pensieve, | Oboe, | and | ANT |
|     |               | MPC      |     | MPC           |                  |     |          |         |           |       |     |     |
| 0.2 |               | Pensieve | 0.2 | Pensieve      |                  |     |          |         |           |       |     |     |
Oboe Oboe under 4 randomly selected traces. As shown, Pensieve always
| 0.0 |     | ANT | 0.0 | ANT |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
utilizeditsgeneralABRmodel.AlthoughOboesupportsauto-
| 0 1 Rebuffering(s) | 2 3 | 4   | 5 0.0 0.2 Smoothness(Mbps) | 0.4 0.6 0.8 |            |       |            |              |     |         |             |     |
| ------------------ | --- | --- | -------------------------- | ----------- | ---------- | ----- | ---------- | ------------ | --- | ------- | ----------- | --- |
|                    |     |     |                            |             | tuning its | model | parameters | to different |     | network | conditions, |     |
Fig.10. FinalCDFcurveunderTencenttraces. Oboe did not conduct ABR model switching because it failed
|     |     |     |     |     | to detect | any | network condition |     | change. | While | only | ANT |
| --- | --- | --- | --- | --- | --------- | --- | ----------------- | --- | ------- | ----- | ---- | --- |
TABLEIII succeeded in detecting these changes and performed model
THESITUATIONSOFABRMODELSELECTIONUNDER4 switching in time, leading to the final QoE improvements.
RANDOMLYSELECTEDNETWORKTRACES
|     |     |     |     |     | E. ANT           | Deep Dive |             |           |           |              |         |     |
| --- | --- | --- | --- | --- | ---------------- | --------- | ----------- | --------- | --------- | ------------ | ------- | --- |
|     |     |     |     |     | 1) Ablation      |           | Study: To   | evaluate  | the       | necessity    | of the  | CNN |
|     |     |     |     |     | model introduced |           | in the      | condition | detection |              | module, | we  |
|     |     |     |     |     | developed        | another   | version     | of ANT    | (called   | ANT-DIST)    |         | and |
|     |     |     |     |     | compared         | it with   | the default | ANT       | for       | the ablation | study.  | In  |
ANT-DIST,Euclideandistanceisusedtoperformnetworkcon-
ditiondetectionbycalculatingitfromagroupoffixedcenters
generalQoEdefinitioninEq.(7).WefoundANT improvedthe already obtained in the trace clustering. In the following, we
averagebitrateutilityby16.05%(3.24%)comparedtothesec- compared the specific implementation of network condition
ondbest-performingOboeunderthepublic(Tencent)network detection in ANT and ANT-DIST.
traces. On the rebuffering penalty, ANT rivals Pensieve and • ANT-DIST: distinguishes the network condition based
Oboe under the public network traces and outperforms them on the Euclidean distance from the clustering centers
by respectively 37.39% and 23.54% under Tencent network obtained in Section IV-B. The network condition is
traces.AlthoughthesmoothnessforANT isslightlyworsethan determined by the nearest distance between the current
that for MPC, it is kept at an acceptable low level. So ANT throughput segment (20s) and a certain clustering center.
does not optimize every QoE goal, but balances each factor • ANT: discriminates the network condition based on
to optimize the general QoE metric. We further calculated the a powerful CNN-based model and a sliding window-
cumulative distribution function (CDF) of the general QoE based confidence mechanism proposed in this paper (see
values and its individual components under both the public Section III-B). Besides the Euclidean distance, the CNN
traces and Tencent traces, and the results were shown in model further extracts the temporal change pattern resid-
Figure 9 and Figure 10 respectively. We observed that ANT inginthethroughputsequenceforsegment-levelnetwork
robustly performed better than all state-of-the-art algorithms condition detection. Then the confidence mechanism is
under different network traces. As Pensieve and Oboe were applied to determine the trace-level network condition.
thebest-performingABRalgorithmsamongalltheconsidered Except for the network condition detection method, the
baselines, we limited our evaluations to comparing ANT with other details of ANT-DIST remain the same as ANT.
these two algorithms in the following. We set up a comparative experiment using a total of 100
TheseQoEimprovementsforANT aremainlyderivedfrom network traces that were collected by the Tencent video plat-
the effective representation of network throughput dynamics forminSoutheastAsia.Notethatthesetracesarenotincluded
and the accurate detection of network conditions. When in either the training dataset or the testing dataset mentioned
a change is detected in the network condition, ANT can above. This indicates that the trained ABR models do not
automatically switch to the appropriate ABR model for ABR possess knowledge about these unseen network conditions.
decisions, which is well-trained under the network traces As shown in Figure 11, the default ANT also outperforms
with similar temporal change patterns to the current. In ANT-DIST on both the average QoE by 21.7% and the
contrast, both Pensieve and Oboe fail to perceive condition full CDF of QoE. Taking the individual QoE components
changes and choose the appropriate ABR model in time due into account, ANT reduces the rebuffering time by 32%
to their inability to learn accurate throughput dynamics. To compared to ANT-DIST at a similar bitrate utility. These
demonstrate this, we have captured the situations of ABR results demonstrate that ANT-DIST, which uses the Euclidean
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore.  Restrictions apply.

YINetal.:LEARNINGACCURATENETWORKDYNAMICSFORENHANCEDADAPTIVEVIDEOSTREAMING 817
|     | 1.0 |     |     |     | 1.0 |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
)spbM(etartiB
|     | 0.8 |     |     |     | 0.8 |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Pensieve
|     | 0.6 |     | Be(cid:425)er |     | 0.6 |     |               |     |     | Oboe |     |     |     |     |     |
| --- | --- | --- | ------------- | --- | --- | --- | ------------- | --- | --- | ---- | --- | --- | --- | --- | --- |
| FDC |     |     |               |     | FDC |     | Be(cid:425)er |     |     | ANT  |     |     |     |     |     |
0.4
0.4
|     |     |     |     | Pensieve |     |     |     | Pensieve |     |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
|     | 0.2 |     |     |          | 0.2 |     |     |          |     |     |     |     |     |     |     |
|     |     |     |     | Oboe     |     |     |     | Oboe     |     |     |     |     |     |     |     |
ANT
|     | 0.0                            |     |     | ANT | 0.0                            |       |     |       | EoQ |          |     |     |     |     |     |
| --- | ------------------------------ | --- | --- | --- | ------------------------------ | ----- | --- | ----- | --- | -------- | --- | --- | --- | --- | --- |
|     | 0                              | 2 4 | 6   | 8   | 0                              | 10 20 | 30  | 40 50 |     | Pensieve |     |     |     |     |     |
|     | StandardDevia(cid:415)on ofQoE |     |     |     | StandardDevia(cid:415)on ofQoE |       |     |       |     | Oboe     |     |     |     |     |     |
ANT
chunk
| Fig.12. | ComparingANT |     | withotheralgorithmsonthestandarddeviationof |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ------------ | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
QoEintheformoffullCDF. Fig. 13. An example of performance comparison between ANT and other
algorithmsontheinstantaneousQoEmetric.
|            |             |             |             |                    |             |            |            |           |     |     |     | P   | O   |     |     |
| ---------- | ----------- | ----------- | ----------- | ------------------ | ----------- | ---------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| distance   | to          | determine   | the         | network            | conditions, |            | fails      | to select |     |     |     |     |     |     |     |
| the        | appropriate |             | ABR model   | that               | matches     | the        | current    | network   |     |     |     |     |     |     |     |
| condition  |             | for optimal |             | bitrate decisions. |             | This       | is because | the       |     |     |     |     |     |     |     |
| clustering |             | centers     | are derived | from               | limited     | throughput |            | traces.   |     |     |     |     |     |     |     |
Formoretracesnottakenintoaccount,usingthedistancefrom
thesefixedclusteringcentersforconditionidentificationtends
| toresultinseriousbias.Forexample,ANT-DIST |        |         |            |            |           |           | canidentifya |            |         |                                                  |     |     |     |     |     |
| ----------------------------------------- | ------ | ------- | ---------- | ---------- | --------- | --------- | ------------ | ---------- | ------- | ------------------------------------------------ | --- | --- | --- | --- | --- |
| similar                                   | trace  | to      | labeled    | one as an  | alternate | network   |              | condition, |         |                                                  |     |     |     |     |     |
|                                           |        |         |            |            |           |           |              |            | Fig.14. | Performancecomparisoninthereal-worldenvironment. |     |     |     |     |     |
| even                                      | if its | average | throughput |            | slightly  | differs   | but          | with the   |         |                                                  |     |     |     |     |     |
| throughput                                |        | change  | trend      | preserved. | In        | contrast, | ANT          | further    |         |                                                  |     |     |     |     |     |
learns the temporal change pattern residing in the throughput 3) Resource Overhead and Time Consumption: During the
| sequence |     | during | training | its CNN-based |     | model, | which | serves |           |        |     |           |           |           |       |
| -------- | --- | ------ | -------- | ------------- | --- | ------ | ----- | ------ | --------- | ------ | --- | --------- | --------- | --------- | ----- |
|          |     |        |          |               |     |        |       |        | inference | phase, | the | DNN-based | condition | detection | model |
asanadditionalfeaturewhendetectingthenetworkcondition. consumed approximately 10% of the CPU utilization on the
| Benefiting |     | from         | the accurate | perception |                 | of network |     | dynamics, |        |              |            |             |     |           |            |
| ---------- | --- | ------------ | ------------ | ---------- | --------------- | ---------- | --- | --------- | ------ | ------------ | ---------- | ----------- | --- | --------- | ---------- |
|            |     |              |              |            |                 |            |     |           | Intel  | Xeon E5-2683 |            | v4 @2.10GHz |     | processor | and 7GB of |
| ANT        | can | continuously |              | select     | the appropriate |            | ABR | model     |        |              |            |             |     |           |            |
|            |     |              |              |            |                 |            |     |           | memory | on           | the Nvidia | GeForce     | GTX | 1080Ti    | 11G GPU.   |
to perform better bitrate decisions, especially under unseen The inference time for a batch of 20 input throughput data
network traces.
|     |     |     |     |     |     |     |     |     | segments | was | within | 500ms. Meanwhile, |     | the RL-based | ABR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------ | ----------------- | --- | ------------ | --- |
2) PerformanceStabilityAnalysis: AsANT performsABR model consumed about 3-8% of the CPU utilization on the
model switching whenever a change of network condition is IntelXeonE5-2683v4@2.10GHzprocessorduringinference,
detected, one concern is whether ANT can perform stably withaninferencetimeofapproximately10-30ms.Takinginto
across video chunks during video streaming. To evaluate the account the adequate buffer length for the adopted scenario,
stability performance of ANT, we compared the standard the introduced latency of the overall learning-based ANT is
deviation of QoE for ANT and two state-of-the-art ABR within acceptable limits during the actual inference.
| algorithms |     | (i.e., | Oboe and | Pensieve). | The | results | are | depicted |     |             |     |                   |     |               |     |
| ---------- | --- | ------ | -------- | ---------- | --- | ------- | --- | -------- | --- | ----------- | --- | ----------------- | --- | ------------- | --- |
|            |     |        |          |            |     |         |     |          | 4)  | Performance | in  | Real Transmission |     | Environments: | We  |
in Figure 12. We found that ANT either matched or exceeded further deployed our ANT into an actual video streaming
thestabilityperformanceofthebestexistingABRalgorithms. system of Tencent, and conducted extensive experiments on it
On the public dataset, about 90% of traces are achieved with toevaluate ANT’sperformanceinthereal-worldenvironment.
better stability using ANT. And on the Tencent dataset, ANT The video content server is located in Shenzhen, China.
outperforms other algorithms on the stability in all considered We integrated ANT and other ABR baseline algorithms into
network traces. separate video players, which were installed on the same
To demonstrate the stability performance more clearly, we mobiledevice.Theaccessnetworksattheuserendsconsisted
provided the instantaneous QoE achieved and bitrate decision of WiFi and cellular wireless links. Users accessed the video
for each chunk under a randomly selected network trace in streaming services indoors (e.g., in a laboratory, office, dining
Figure 13. As shown, ANT always outperforms other algo- hall, dormitory, and corridor) or outdoors (e.g., on a road
rithmsthroughoutthevideostreamingsession.Thisisbecause or street). Users were free to be still or moving during the
ANT can effectively detect the change of network conditions streaming session. During the evaluation, video players that
(indicate by black dashed lines in Figure 13), enabling it to run different ABR algorithms were randomly called at once
switch between ABR models as needed. This ensures ANT to to conduct video queries and downloads. Each streaming
make better bitrate decisions and achieve high instantaneous session for an ABR algorithm lasted about 30 minutes and
QoEregardlessofhownetworkconditionschange.Incontrast, was repeated 10 times to eliminate random errors. Such video
Pensieve is unable to adapt its model parameters, and Oboe streaming experiments were carried out in both Shanghai and
fails to detect these network condition changes, resulting in Shenzhen,coveringavastdistanceexceeding1000kilometers.
significantperformancedegradationontheinstantaneousQoE Figure 14 illustrates the average QoE performances
| metric. |     |     |     |     |     |     |     |     | achieved | using | ANT, | Pensieve, | and | Oboe in | real-world |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ---- | --------- | --- | ------- | ---------- |
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore.  Restrictions apply.

818 IEEETRANSACTIONSONBROADCASTING,VOL.70,NO.3,SEPTEMBER2024
P O P O
Fig.15. PerformancecomparisonontheaverageQoEunderbothpublictraces(left)andTencenttraces(right)inthelivestreamingscenario.
network environments. It can be seen that the proposed ANT 1.0
achieves the best performance on the average QoE metric. 0.8
Throughout the sessions conducted in Shanghai, ANT outper- 0.6
forms Pensieve and Oboe with improvement in average QoE 0.4
of58.07%and39.86%,respectively.IntheShenzhensessions,
0.2
ANT also achieves a remarkable average QoE improvement
0.0
of 46.03% and 18.71% compared to Pensieve and Oboe, 2 1 0 1 2 3 4
QoE
respectively.TheloweraverageQoEintheShenzhensessions
can be attributed to the poorer network conditions with
lower bandwidth compared to that in Shanghai during testing.
These results demonstrate the superiority and generalizability
of the proposed ANT when operating in real transmission
environments.
5) Extension in the Live Streaming Scenario: Besides the
aforementioned VoD scenario, we also evaluated ANT in the
latency-sensitive live streaming scenario. We implemented
ANT on the live streaming video platform offered by the
2019 ACM multimedia grand challenge [71], in which the
buffer capacity was limited to 2 seconds to meet the low
latency requirement. The video was also provided by the live
streamingplatform,whichcoveredahighdynamicrange.The
bitrate ladder for live videos was configured as {500, 850,
1200, 1850} Kbps. We set q(R ) = frame_time_length×R
n n
as the video quality metric [71], where frame_time_length
equals 0.04 (in seconds) in our setting. The rebuffer penalty
coefficient was configured as 1.85 in this scenario. Each live
video was streamed through a sequence of frames, and bitrate
selections were made for every GoP, which comprised 50
frames and represented approximately 2 seconds of video
playback.Inadditiontoverylimitedbuffercapacity,thevideo
content was generated and streamed in real time, so content-
related information including the video length and future
chunk sizes was not available. These features brought a great
challengeforABRalgorithmstodealwithunderlyingnetwork
fluctuations in live streaming.
To accommodate the characteristics of live streaming,
we made essential modifications to ANT’s ABR models.
Specifically, the RL agent’s state input includes throughput
measurements, rebuffering time, the selected bitrate in the
past, and the current receiving frame rate. The first three
state components are fed into a gated recurrent unit (GRU)
layer with 128 units, while the last is input into a fully
connected layer with 128 neurons. Compared to the CNN
utilized in Pensieve, we employed GRU in the neural network
for the limited-buffer live streaming to ensure satisfactory
ABR performance. This is because GRU can more effectively
capture long-term dependencies within the sequential input
FDC
Pensieve
Oboe
ANT
Be(cid:425)er
5 0 5
QoE
FDC
1.0 Pensieve
Oboe
0.8
ANT
0.6
Be(cid:425)er 0.4
0.2
0.0
30 25 20 15 10
Fig. 16. Final CDF curve of QoE under both public traces and Tencent
traces.
data. The outputs from these layers are then aggregated in a
hidden layer that applies the softmax function for the actor
network. Finally, the RL agent selects one bitrate from the
given options based on the output of the action probability
distribution.ThisselectiondecisionismadeperGoPtorapidly
adapt to the underlying network fluctuations. Similar to the
VoD scenario, several ABR models were finally trained for
different network conditions using corresponding clusters of
network throughput traces. During the inference phase, the
networkconditionwasdeterminedbasedonhistoricalthrough-
put measurements spanning 20 seconds, which subsequently
derived the selection of appropriate ABR models to make
bitrate decisions.
Figure 15showstheaverageQoEthateachABRalgorithm
achieved on both the public dataset and the Tencent dataset.
Figure 16 provides more detailed results in the form of full
CDFs. It can be found that ANT outperforms Oboe and
Pensieve by 46.01%-98.15% and 60.81%-3.76×, respectively,
ontheaverageQoEmetricacrossawiderangeofnetworkcon-
ditions (e.g., WiFi, 3G/4G, and broadband connections). The
CDF results also illustrate the superior QoE performance of
ANT in all sessions on the Tencent dataset and approximately
in 80% sessions on the public dataset, compared to these
state-of-the-art ABR algorithms. This is because ANT can
effectively represent and learn network throughput dynamics,
and always select the appropriate ABR model for the cur-
rent network condition to better handle network fluctuations.
We also observe that ABR algorithms with parameter auto-
tuning capabilities, such as Oboe and ANT, exhibit superior
performance in high-QoE sessions but inferior performance
in low-QoE sessions compared to the general-model Pensieve
algorithm. This can be attributed to the relatively aggressive
policy of Oboe and ANT in selecting higher video bitrates
while simultaneously minimizing rebuffering occurrences.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.

YINetal.:LEARNINGACCURATENETWORKDYNAMICSFORENHANCEDADAPTIVEVIDEOSTREAMING 819
However, due to the dominance of the rebuffering penalty in characterizing and sensing the network dynamics using com-
the overall QoE metric defined for live streaming scenarios, prehensive features extracted from raw throughput sequences.
these algorithms fail to achieve QoE improvements in low- Based on the sensing output, ANT then selects the most
QoE sessions. appropriate ABR model that has been well trained using
On the other hand, ANT achieves a greater average QoE reinforcement learning under similar network conditions, to
improvement in the live streaming scenario than that in the make bitrate decisions. This allows ANT to optimize different
VoD scenario, compared to the best state-of-the-art Oboe and ABRpoliciesforeachspecificnetworkconditionencountered.
Pensieve. This result can be attributed to the ability of ANT Through extensive experimental evaluations, we demonstrate
to perceive and adapt to network dynamics, especially in the superior performance of ANT in bitrate adaptation across
the absence of redundant buffer capacity and knowledge of a wide range of network conditions, both in the video-on-
future video content. Furthermore, we find that all considered demand and live-streaming scenarios.
algorithms perform better on the average QoE under public
traces in the live streaming scenario, which is opposite to that
REFERENCES
intheVoDscenario.Thisismainlyduetoabout10%sessions
with very low QoE achieved for all considered algorithms [1] “Cisco visual networking index: Global mobile data traffic forecast
update 2017-2022,” Cisco Technol. Co., San Jose, CA, USA, White
in the Tencent dataset, as shown in Figure 16(b). Recall that
Paper,2019.
the network bandwidth in the Tencent dataset fluctuates more [2] Y. Xu, J. Yin, Q. Yang, and L. Yang, “Media production using cloud
severely than that in the public dataset, which brings greater and edge computing: Recent progress and NBMP-based implementa-
tion,”IEEETrans.Broadcast.,vol.68,no.2,pp.545–558,Jun.2022.
challenges for ABR algorithms in the latency-sensitive live
[3] C. Liu, I. Bouazizi, and M. Gabbouj, “Rate adaptation for adaptive
streaming scenario with a limited buffer capacity. HTTP streaming,” in Proc. 2nd Annu. ACM Conf. Multimedia Syst.,
2011,pp.169–174.
[4] J. Jiang, V. Sekar, and H. Zhang, “Improving fairness, efficiency, and
stability in HTTP-based adaptive video streaming with FESTIVE,” in
V. DISCUSSION
Proc.8thInt.Conf.Emerg.Netw.Exp.Technol.,2012,pp.97–108.
Handling more complex network conditions.Althoughthe [5] Y.Sunetal.,“CS2P:Improvingvideobitrateselectionandadaptation
network traces we use in this paper cover a wide range of with data-driven throughput prediction,” in Proc. ACM SIGCOMM
Conf.,2016,pp.272–285.
conditions,thereisanopportunityforANT toencountermore
[6] K. Miller, A.-K. Al-Tamimi, and A. Wolisz, “QoE-based low-delay
complex network conditions in a real transmission environ- live streaming using throughput predictions,” ACM Trans. Multimedia
ment.Inthissituation,thenetworkconditiondetectionmodule Comput.Commun.Appl.,vol.13,no.1,pp.1–24,Oct.2016.
[7] T.-Y.Huang,R.Johari,N.McKeown,M.Trunnell,andM.Watson,“A
mayproduceinaccurateresultsthatcauseinappropriatemodel
buffer-based approach to rate adaptation: Evidence from a large video
selection in the following bitrate decision module. Moreover, streamingservice,”inProc.ACMConf.SIGCOMM,2014,pp.187–198.
these complex network conditions may occur without a label, [8] T.-Y.Huang,R.Johari,andN.McKeown,“Downtonabbeywithoutthe
hiccups: Buffer-based rate adaptation for HTTP video streaming,” in
that is, not included in the trace clustering, bringing difficulty
Proc. ACM SIGCOMM Workshop Future Human-Centric Multimedia
for ANT to select the most appropriate ABR model for bitrate Netw.,2013,pp.9–14.
decisions. Nevertheless, we train a general ABR model and [9] K. Miller, E. Quacchio, G. Gennari, and A. Wolisz, “Adaptation
algorithmforadaptivestreamingoverHTTP,”inProc.19thInt.Packet
a dedicated “uncertain” ABR model in ANT additionally to
VideoWorkshop(PV),2012,pp.173–178.
cover the above-mentioned network conditions for acceptable [10] K. Spiteri, R. Urgaonkar, and R. K. Sitaraman, “BOLA: Near-optimal
QoE achievement. bitrate adaptation for online videos,” in Proc. IEEE 35th Annu. IEEE
Int.Conf.Comput.Commun.(INFOCOM),2016,pp.1–9.
Online training for ABR models. ANT server stores a
[11] H.Mao,R.Netravali,andM.Alizadeh,“Neuraladaptivevideostream-
limited number of pre-trained ABR models, each of which ing with pensieve,” in Proc. Conf. ACM Spec. Interest Group Data
correspondstoaspecificnetworkcondition.However,whenan Commun.,2017,pp.197–210.
[12] H. Chen et al., “T-gaming: A cost-efficient cloud gaming system
absolutely different network condition appears, all pre-trained
at scale,” IEEE Trans. Parallel Distrib. Syst., vol. 30, no. 12,
modelsmaybesusceptibletoexperiencingperformancedegra- pp.2849–2865,Dec.2019.
dation. In this case, these pre-trained ABR models need to [13] F. Y. Yan et al., “Learning in situ: A randomized experiment in video
streaming,”inProc.17thUSENIXSymp.Netw.Syst.DesignImplement.
be refined online, or a new ABR model should be trained to
(NSDI),2020,pp.495–511.
match this unseen network condition. Further investigations [14] Z. Xia, Y. Zhou, F. Y. Yan, and J. Jiang, “Genet: Automatic curricu-
are required for this aspect, and it will be deferred to future lum generation for learning adaptation in networking,” in Proc. ACM
SIGCOMMConf.,2022,pp.397–413.
research endeavors. It is worth noting that during the model
[15] Z.Akhtaretal.,“Oboe:Auto-tuningvideoABRalgorithmstonetwork
refinement process, online training can be collaborated with
conditions,” in Proc. Conf. ACM Spec. Interest Group Data Commun.,
ANT’s network condition detection module to strike a balance 2018,pp.44–58.
between training effectiveness and efficiency. [16] E. Kurdoglu, Y. Liu, Y. Wang, Y. Shi, C. Gu, and J. Lyu, “Real-time
bandwidth prediction and rate adaptation for video calls over cellular
networks,”inProc.7thInt.Conf.MultimediaSyst.,2016,pp.1–11.
[17] X.K.Zouetal.,“Canaccuratepredictionsimprovevideostreamingin
VI. CONCLUSION cellular networks?” in Proc. 16th Int. Workshop Mobile Comput. Syst.
Appl.,2015,pp.57–62.
In this paper, we propose ANT, a novel framework
[18] S. Kim and C. Kim, “XMAS: An efficient mobile adaptive streaming
to enhance adaptive video streaming by accurately learn- schemebasedontrafficshaping,”IEEETrans.Multimedia,vol.21,no.2,
ing network throughput dynamics. Unlike existing ABR pp.442–456,Feb.2019.
[19] T.-Y. Huang, N. Handigol, B. Heller, N. McKeown, and R. Johari,
algorithms that rely on limited network statistics to auto-
“Confused, timid, and unstable: Picking a video streaming rate is
tune model parameters, ANT takes a different approach by hard,”inProc.InternetMeas.Conf.,2012,pp.225–238.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.

820 IEEETRANSACTIONSONBROADCASTING,VOL.70,NO.3,SEPTEMBER2024
[20] A. Beben, P. Wiundefinedniewski, J. M. Batalla, and P. Krawiec, [43] T. Huang, R.-X. Zhang, C. Zhou, and L. Sun, “QARC: Video quality
“ABMA+: Lightweight and efficient algorithm for HTTP adaptive aware rate control for real-time video streaming based on deep rein-
streaming,”inProc.7thInt.Conf.MultimediaSyst.,2016,pp.1–11. forcement learning,” in Proc. 26th ACM Int. Conf. Multimedia, 2018,
[21] G. Tian and Y. Liu, “Towards agile and smooth video adaptation in pp.1208–1216.
dynamic HTTP streaming,” in Proc. 8th Int. Conf. Emerg. Netw. Exp. [44] A. Elgabli and V. Aggarwal, “FastScan: Robust low-complexity rate
Technol.,2012,pp.109–120. adaptation algorithm for video streaming over HTTP,” IEEE Trans.
[22] C. Zhou, C. Lin, X. Zhang, and Z. Guo, “Buffer-based smooth rate CircuitsSyst.VideoTechnol.,vol.30,no.7,pp.2240–2249,Jul.2020.
adaptationfordynamicHTTPstreaming,”inProc.Asia-Pac.SignalInf. [45] T. Huang, R.-X. Zhang, and L. Sun, “Zwei: A self-play
Process.Assoc.Annu.SummitConf.,2013,pp.1–9. reinforcement learning framework for video transmission
[23] Z.Lietal.,“Probeandadapt:RateadaptationforHTTPvideostreaming services,” IEEE Trans. Multimedia, vol. 24, pp. 1350–1365, 2022,
at scale,” IEEE J. Sel. Areas Commun., vol. 32, no. 4, pp.719–733, doi:10.1109/TMM.2021.3063620.
Apr.2014. [46] L. Cui, D. Su, S. Yang, Z. Wang, and Z. Ming, “TCLiVi:
[24] C. Wang, A. Rizk, and M. Zink, “SQUAD: A spectrum-based quality Transmission control in live video streaming based on deep reinforce-
adaptationfordynamicadaptivestreamingoverHTTP,”inProc.7thInt. ment learning,” IEEE Trans. Multimedia, vol. 23, pp.651–663, 2021,
Conf.MultimediaSyst.,2016,pp.1–12. doi:10.1109/TMM.2020.2985631.
[25] A. Mansy, B. Ver Steeg, and M. Ammar, “SABRE: A client based [47] T.Feng,H.Sun,Q.Qi,J.Wang,andJ.Liao,“Vabis:Videoadaptation
technique for mitigating the buffer bloat effect of adaptive video bitratesystemfortime-criticallivestreaming,”IEEETrans.Multimedia,
flows,”inProc.4thACMMultimediaSyst.Conf.,2013,pp.214–225. vol.22,no.11,pp.2963–2976,Nov.2020.
[26] X. Yin, V. Sekar, andB. Sinopoli, “Toward aprincipled frameworkto [48] H. Yuan, X. Hu, J. Hou, X. Wei, and S. Kwong, “An ensemble rate
design dynamic adaptive streaming algorithms over HTTP,” in Proc. adaptationframeworkfordynamicadaptivestreamingoverHTTP,”IEEE
13thACMWorkshopHotTopicsNetw.,2014,pp.1–7. Trans.Broadcast.,vol.66,no.2,pp.251–263,Jun.2020.
[49] Z.Jiang,X.Zhang,Y.Xu,Z.Ma,J.Sun,andY.Zhang,“Reinforcement
[27] X. Yin, A. Jindal, V. Sekar, and B. Sinopoli, “A control-theoretic
learning based rate adaptation for 360-degree video streaming,” IEEE
approach for dynamic adaptive video streaming over HTTP,” in Proc.
Trans.Broadcast.,vol.67,no.2,pp.409–423,Jun.2021.
ACMConf.Spec.InterestGroupDataCommun.,2015,pp.325–338.
[50] J.Fu,Z.Chen,X.Chen,andW.Li,“Sequentialreinforced360-degree
[28] L.DeCicco,V.Caldaralo,V.Palmisano,andS.Mascolo,“ELASTIC:
videoadaptivestreamingwithcross-userattentivenetwork,”IEEETrans.
A client-side controller for dynamic adaptive streaming over HTTP
Broadcast.,vol.67,no.2,pp.383–394,Jun.2021.
(DASH),”inProc.20thInt.PacketVideoWorkshop,2013,pp.1–8.
[51] A.Zhangetal.,“Videosuper-resolutionandcaching—anedge-assisted
[29] C.Zhou,C.-W.Lin,andZ.Guo,“mDASH:AMarkovdecision-based
adaptive video streaming solution,” IEEE Trans. Broadcast., vol. 67,
rate adaptation approach for dynamic HTTP streaming,” IEEE Trans.
no.4,pp.799–812,Dec.2021.
Multimedia,vol.18,no.4,pp.738–751,Apr.2016.
[52] X. Ma et al., “QAVA: QoE-aware adaptive video bitrate aggregation
[30] J.Chen,Z.Luo,Z.Wang,M.Hu,andD.Wu,“Live360:Viewport-aware
forHTTPlivestreamingbasedonsmartedgecomputing,”IEEETrans.
transmission optimization in live 360-degree video streaming,” IEEE
Broadcast.,vol.68,no.3,pp.661–676,Sep.2022.
Trans.Broadcast.,vol.69,no.1,pp.85–96,Mar.2023.
[53] Y. Xie, Y. Zhang, and T. Lin, “Deep curriculum reinforce-
[31] A.YaqoobandG.-M.Muntean,“Acombinedfield-of-viewprediction- ◦
◦ ment learning for adaptive 360 video streaming with two-stage
assisted viewport adaptive delivery scheme for 360 videos,” IEEE
training,” IEEE Trans. Broadcast., early access, Dec. 15, 2023,
Trans.Broadcast.,vol.67,no.3,pp.746–760,Sep.2021.
doi:10.1109/TBC.2023.3334137.
[32] A. Polakovicˇ, G. Rozinaj, and G.-M. Muntean, “User gaze-driven
[54] G.Zhou,Z.Luo,M.Hu,andD.Wu,“PreSR:Neural-enhancedadaptive
adaptation of omnidirectional video delivery using spatial tiling and
streaming of VBR-encoded videos with selective prefetching,” IEEE
scalable video encoding,” IEEE Trans. Broadcast., vol. 68, no. 3,
Trans.Broadcast.,vol.69,no.1,pp.49–61,Mar.2023.
pp.609–619,Sep.2022.
[55] T. P. Lillicrap et al., “Continuous control with deep reinforcement
[33] L.Zhong,M.Wang,C.Xu,S.Yang,andG.-M.Muntean,“Decentralized
learning,”2019,arXiv:1509.02971.
optimization for multicast adaptive video streaming in edge cache-
[56] X.Xiaoetal.,“Fromembertoblaze:Swiftinteractivevideoadaptation
assistednetworks,”IEEETrans.Broadcast.,vol.69,no.3,pp.812–822,
viameta-reinforcementlearning,”2023,arXiv:2301.05541.
Sep.2023.
◦ [57] N. Kan, Y. Jiang, C. Li, W. Dai, J. Zou, and H. Xiong, “Improving
[34] Z. Ye et al., “VRCT: A viewport reconstruction-based 360 video
generalization for neural adaptive video streaming via meta reinforce-
caching solution for tile-adaptive streaming,” IEEE Trans. Broadcast.,
ment learning,” in Proc. 30th ACM Int. Conf. Multimedia, 2022,
vol.69,no.3,pp.691–703,Sep.2023.
pp.3006–3016.
[35] M. A. Togou et al., “An innovative adaptive Web-based solution [58] H. Zhang, A. Zhou, and H. Ma, “Improving mobile interactive video
for improved remote co-creation and delivery of artistic perfor- QoE via two-level online cooperative learning,” IEEE Trans. Mobile
mances,” IEEE Trans. Broadcast., early access, Mar. 13, 2024, Comput.,vol.22,no.10,pp.5900–5917,Oct.2023.
doi:10.1109/TBC.2024.3363455.
[59] Y.Gao,P.Zhou,Z.Liu,B.Han,andP.Hui,“FRAS:Federatedreinforce-
[36] Y. Wang, J. Li, Z. Li, S. Shang, and Y. Liu, “Synergistic temporal- mentlearningempoweredadaptivepointcloudvideostreaming,”2023,
spatialuser-awareviewportpredictionforoptimaladaptive360-degree arXiv:2207.07394.
videostreaming,”IEEETrans.Broadcast.,earlyaccess,Mar.21,2024, [60] C.Hardegen,B.Pfülb,S.Rieger,A.Gepperth,andS.Reißmann,“Flow-
doi:10.1109/TBC.2024.3374119. basedthroughputpredictionusingdeeplearningandreal-worldnetwork
[37] Z. Li, Y. Wang, Y. Liu, J. Li, and P. Zhu, “JUST360: traffic,” in Proc. 15th Int. Conf. Netw. Service Manag. (CNSM), 2019,
Optimizing 360-degree video streaming systems with joint pp.1–9.
utility,” IEEE Trans. Broadcast., early access, Mar. 21, 2024, [61] Y. Liu and J. Y. B. Lee, “An empirical study of throughput prediction
doi:10.1109/TBC.2024.3374066. in mobile data networks,” in Proc. IEEE Glob. Commun. Conf.
[38] T. Huang, C. Zhou, R.-X. Zhang, C. Wu, X. Yao, and L. Sun, “Stick: (GLOBECOM),2015,pp.1–6.
A harmonious fusion of buffer-based and learning-based approach [62] D.Yuan,Y.Zhang,W.Zhang,X.Liu,H.Du,andQ.Zheng,“PRIOR:
for adaptive streaming,” in Proc. IEEE Conf. Comput. Commun. Deepreinforcedadaptivevideostreamingwithattention-basedthrough-
(INFOCOM),2020,pp.1967–1976. putprediction,”inProc.32ndWorkshopNetw.Oper.Syst.SupportDigit.
[39] R.Hong,Q.Shen,L.Zhang,andJ.Wang,“Continuousbitrate&latency AudioVideo,2022,pp.36–42.
control with deep reinforcement learning for live video streaming,” in [63] A. Bentaleb, C. Timmerer, A. C. Begen, and R. Zimmermann,
Proc.27thACMInt.Conf.Multimedia,2019,pp.2637–2641. “Bandwidthpredictioninlow-latencychunkedstreaming,”inProc.29th
[40] X. Jiang and Y. Ji, “HD3: Distributed dueling DQN with discrete- ACM Workshop Netw. Oper. Syst. Support Digit. Audio Video, 2019,
continuoushybridactionspacesforlivevideostreaming,”inProc.27th pp.7–13.
ACMInt.Conf.Multimedia,2019,pp.2632–2636. [64] A. Bentaleb, A. C. Begen, S. Harous, and R. Zimmermann, “Data-
[41] T.Huang,C.Zhou,R.-X.Zhang,C.Wu,X.Yao,andL.Sun,“Comyco: drivenbandwidthpredictionmodelsandautomatedmodelselectionfor
Quality-awareadaptivevideostreamingviaimitationlearning,”inProc. low latency,” IEEE Trans. Multimedia, vol. 23, pp.2588–2601, 2021,
27thACMInt.Conf.Multimedia,2019,pp.429–437. doi:10.1109/TMM.2020.3013387.
[42] H. Peng, Y. Zhang, Y. Yang, and J. Yan, “A hybrid control scheme [65] J. B. Macqueen, “Some methods for classification and analysis of
foradaptivelivestreaming,”inProc.27thACMInt.Conf.Multimedia, multivariate observations,” in Proc. 5th Berkeley Symp. Math. Stat.
2019,pp.2627–2631. Probab.,1967,pp.281–297.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore. Restrictions apply.

YINetal.:LEARNINGACCURATENETWORKDYNAMICSFORENHANCEDADAPTIVEVIDEOSTREAMING 821
[66] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for Yiling Xu (Member, IEEE) received the B.S.,
imagerecognition,”inProc.IEEEConf.Comput.Vis.PatternRecognit. M.S., and Ph.D. degrees from the University of
(CVPR),2016,pp.770–778. ElectronicScienceandTechnologyofChina,China,
[67] V. Mnih et al., “Asynchronous methods for deep reinforcement learn- in 1999, 2001, and 2004, respectively. She is
ing,”inProc.33rdInt.Conf.Mach.Learn.,2016,pp.1928–1937. a Full Researcher with the School of Electronic
[68] (Federal Commun. Commiss. Gov. Agency, Washington, DC, USA). Information and Electronic Engineering, Shanghai
RawData—MeasuringBroadbandAmerica.(2016).[Online].Available: JiaoTongUniversity,Shanghai,China.From2004to
https://www.fcc.gov/reports-Res./reports/ 2013,shewaswiththeMultimediaCommunication
[69] H.Riiser,P.Vigmostad,C.Griwodz,andP.Halvorsen,“Commutepath ResearchInstitute,SamsungElectronicsInc.,South
bandwidthtracesfrom3Gnetworks:Analysisandapplications,”inProc. Korea.Hermainresearchinterestsincludearchitec-
4thACMMultimediaSyst.Conf.,2013,pp.114–118. turedesignfornextgenerationmultimediasystems,
[70] “4G/LTE bandwidth dataset collection from Belgium.” 2017. [Online]. dynamic data encapsulation, adaptive cross layer design, dynamic adaption
Available:http://users.ugent.be/jvdrhoof/dataset-4g/logs/ forheterogenousnetworks,andN-screencontentpresentation.
| [71] “ACM multimedia | 2019 grand | challenge–live | video streaming.” | 2019. |     |     |     |
| -------------------- | ---------- | -------------- | ----------------- | ----- | --- | --- | --- |
[Online].Available:https://www.aitrans.online/MMGC/
[72] Z.Ma,M.Xu,Y.-F.Ou,andY.Wang,“Modelingofrateandperceptual
qualityofcompressedvideoasfunctionsofframerateandQuantization
stepsizeanditsapplications,”IEEETrans.CircuitsSyst.VideoTechnol., ZhanMa(SeniorMember,IEEE)receivedtheB.S.
vol.22,no.5,pp.671–682,May2012. and M.S. degrees from the Huazhong University
|     |     |     |     |     | of Science  | and Technology,      | Wuhan, China, in      |
| --- | --- | --- | --- | --- | ----------- | -------------------- | --------------------- |
|     |     |     |     |     | 2004 and    | 2006, respectively,  | and the Ph.D.         |
|     |     |     |     |     | degree from | New York University, | New York,             |
|     |     |     |     |     | in 2011.    | He is currently      | on the faculty of the |
ElectronicScienceandEngineeringSchool,Nanjing
|     | Jiaoyang Yin | received | the B.S. degree | in commu- |             |                 |                    |
| --- | ------------ | -------- | --------------- | --------- | ----------- | --------------- | ------------------ |
|     |              |          |                 |           | University, | Jiangsu, China. | From 2011 to 2014, |
nicationengineeringfromXidianUniversity,Xi’an,
China, in 2018. He is currently pursuing the Ph.D. he was with Samsung Research America, Dallas,
|     |                  |                 |             |            | TX, USA,   | and Futurewei Technologies, | Inc., Santa          |
| --- | ---------------- | --------------- | ----------- | ---------- | ---------- | --------------------------- | -------------------- |
|     | degree with      | the Cooperative | Medianet    | Innovation |            |                             |                      |
|     |                  |                 |             |            | Clara, CA, | USA, respectively.          | His current research |
|     | Center, Shanghai | Jiao Tong       | University, | China. His |            |                             |                      |
focusesonthenext-generationvideocoding,energy-efficientcommunication,
|     | research focuses | on media | transmission, | wireless |     |     |     |
| --- | ---------------- | -------- | ------------- | -------- | --- | --- | --- |
gigapixelstreaming,anddeeplearning.Heisaco-recipientofthe2018ACM
|     | communication, | neural | network, | and quality of |     |     |     |
| --- | -------------- | ------ | -------- | -------------- | --- | --- | --- |
experience. SIGCOMMStudentResearchCompetitionFinalist,the2018PCMBestPaper
Finalist,andthe2019IEEEBroadcastTechnologySocietyBestPaperAward.
|     |     |     |     |     | Xiaozhong | Xu (Member, IEEE)       | received the B.S. |
| --- | --- | --- | --- | --- | --------- | ----------------------- | ----------------- |
|     |     |     |     |     | degree in | electronics engineering | from Tsinghua     |
HaoChen(Member,IEEE)receivedtheB.E.degree University, Beijing, China, the M.S. degree in
in electronics and information engineering from electrical and computer engineering from the
|     | Northwestern | Polytechnical | University, | China, in |             |                        |          |
| --- | ------------ | ------------- | ----------- | --------- | ----------- | ---------------------- | -------- |
|     |              |               |             |           | Polytechnic | School of Engineering, | New York |
2013,andthePh.D.degreeininformationandcom- University, New York, NY, USA, and the Ph.D.
munication engineering from Shanghai Jiao Tong degree in electronics engineering from Tsinghua
University, China, in 2020. He is currently on the University. He has been a Principal Researcher
faculty of the Electronic Science and Engineering and a Senior Manager of Multimedia Standards
School, Nanjing University. His research interests with Tencent Media Laboratory, Palo Alto, CA,
focusonvideostreaming,real-timevideotransmis- USA, since 2017. His research interests include
sion, and machine learning. He is a co-recipient of multimedia,videoandimagecoding,processing,andtransmission.Hewasa
the 2019 IEEE Broadcast Technology Society Best recipient of the Science and Technology Award from the China Association
PaperAward. forStandardizationin2020.
Authorized licensed use limited to: UNIVERSIDAD DE GRANADA. Downloaded on May 26,2026 at 15:43:23 UTC from IEEE Xplore.  Restrictions apply.
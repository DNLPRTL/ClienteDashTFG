|     | A   | Brief Survey |     | on Adaptive |     | Video | Streaming |     | Quality |     |
| --- | --- | ------------ | --- | ----------- | --- | ----- | --------- | --- | ------- | --- |
Assessment
|                                          |             | Wei                 | Zhoua,        | Xiongkuo     | Minb,        | Hong        | Lic, Qiuping | Jiangc,∗     |      |           |
| ---------------------------------------- | ----------- | ------------------- | ------------- | ------------ | ------------ | ----------- | ------------ | ------------ | ---- | --------- |
|                                          | aDepartment | of Electrical       |               | and Computer | Engineering, |             | University   | of Waterloo, |      | Waterloo, |
| 2202 beF 52  ]MM.sc[  1v78921.2022:viXra |             |                     |               | ON           | N2L          | 3G1, Canada |              |              |      |           |
|                                          |             | bInstitute of Image | Communication |              | and          | Network     | Engineering, | Shanghai     | Jiao | Tong      |
|                                          |             |                     |               | University,  | Shanghai     | 200240,     | China        |              |      |           |
cSchool
|     |     | of Information | Science | and | Engineering, | Ningbo | University, | Ningbo | 315211, | China |
| --- | --- | -------------- | ------- | --- | ------------ | ------ | ----------- | ------ | ------- | ----- |
Abstract
Quality of experience (QoE) assessment for adaptive video streaming plays a
significant role in advanced network management systems. It is especially chal-
lenging in case of dynamic adaptive streaming schemes over HTTP (DASH)
whichhasincreasinglycomplexcharacteristicsincludingadditionalplaybackis-
sues. In this paper, we provide a brief overview of adaptive video streaming
quality assessment. Upon our review of related works, we analyze and com-
pare different variations of objective QoE assessment models with or without
using machine learning techniques for adaptive video streaming. Through the
performance analysis, we observe that hybrid models perform better than both
quality-of-service (QoS) driven QoE approaches and signal fidelity measure-
ment. Moreover, the machine learning-based model slightly outperforms the
model without using machine learning for the same setting. In addition, we
find that existing video streaming QoE assessment models still have limited
performance, which makes it difficult to be applied in practical communication
systems. Therefore, based on the success of deep learned feature representa-
tions for traditional video quality prediction, we also apply the off-the-shelf
deep convolutional neural network (DCNN) to evaluate the perceptual quality
of streaming videos, where the spatio-temporal properties of streaming videos
∗Correspondingauthor
|     |     | Email address: | jiangqiuping@nbu.edu.cn(QiupingJiang) |     |     |     |     |     |     |     |
| --- | --- | -------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Preprint submitted to Journal of LATEX Templates March 1, 2022

are taken into consideration. Experiments demonstrate its superiority, which
sheds light on the future development of specifically designed deep learning
frameworks for adaptive video streaming quality assessment. We believe this
surveycanserveasaguidelineforQoEassessmentofadaptivevideostreaming.
| Keywords:       | Quality          | of experience, |      | video quality | assessment, | adaptive |
| --------------- | ---------------- | -------------- | ---- | ------------- | ----------- | -------- |
| streaming,      | performance      | analysis,      | deep | convolutional | neural      | network, |
| spatio-temporal | characteristics. |                |      |               |             |          |
1. Introduction
Withtherapiddevelopmentofnetworkservicesandmobiledevices,stream-
ing related multimedia applications have obtained tremendous growth. The
arrival of dynamic adaptive streaming schemes over HTTP (DASH) standard
[1] provides the transition from traditional connection-based video streaming
protocols to hypertext transfer protocol (HTTP) adaptive streaming (HAS)
protocols which enable flexible deployment, reduced workload, and reliable de-
livery. In addition, data analysis and artificial intelligence have emerged in a
service-driven next-generation wireless communication network [2]. Therefore,
quality of experience (QoE) for HAS streaming videos has attracted increasing
| attention  | in both academia |                   | and industry | [3]. |                 |                    |
| ---------- | ---------------- | ----------------- | ------------ | ---- | --------------- | ------------------ |
| As defined | by the           | Telecommunication |              |      | Standardization | Sector of Interna- |
tional Telecommunication Union (ITU-T), QoE is the overall acceptability of
anapplicationorserviceasperceivedsubjectivelybytheenduser[4]. Address-
ing the QoE expectations of end-users is crucial for satisfying the requirements
of video streaming services. Since users are the ultimate viewers of stream-
ing videos in most practical applications, subjective QoE assessment [5, 6, 7]
is straightforward and reliable for the evaluation of perceptual video streaming
quality. Specifically, user studies are conducted, in which a number of subjects
are asked to rate the visual quality of different streaming videos. The average
of these subjective judgments, i.e. mean opinion score (MOS), is computed for
| the final | quality measurement, |     | which | is usually | known as | the ground truth. |
| --------- | -------------------- | --- | ----- | ---------- | -------- | ----------------- |
2

DespitethefactthatsubjectiveQoEassessmentcandeliverthemostprecise
and reliable evaluation, these subjective tests are time-consuming, expensive,
and inconvenient. More importantly, they cannot be applied to the real-time
multimedia distribution and playback scheduling frameworks. Hence, it is also
increasinglydesirabletodevelophighlyeffectiveandaccurateobjectiveQoEas-
sessment models [8, 9, 10, 11] with low computational complexity for streaming
videos, which aims to maintain efficient resource allocation and quality man-
agement for existing video services in multimedia delivery systems.
Building an effective QoE assessor for adaptive video streaming faces sev-
eral foreseeable challenges. First, in addition to compression artifacts, how to
evaluate the perceived quality of streaming video is more complicated due to
additional network impairments (e.g. initial buffering, playback stalling, etc.)
compared to traditional VQA. Second, due to the time-consuming subjective
experiments, the established databases for video streaming QoE are relatively
small-scale,thusitisdifficulttotrainadeeplearning-basedmodelwithspecific
network parameters [12]. Third, the quality degradation of video streaming is
influenced not only by video spatial characteristics, but also by its temporal
attributes.
Figure1showstheimportantroleofQoEassessmentinmultimediacommu-
nication systems. It illustrates that application servers transmit adaptive video
streamingdatatousersthroughthecorenetwork,accessnetwork,andterminal
devices. Then, the designed QoE assessor is deployed to take relevant informa-
tion, e.g. the decoded streaming video data as input, and predicts perceptual
video streaming quality. Finally, the virtually located QoE management re-
ceives the information from the QoE assessor and aims to optimize the network
delivery of streaming video data.
Although various surveys have been proposed for the perceptual quality as-
sessment of images/videos [13, 14, 15], such reviews for adaptive video stream-
ing quality assessment are relatively scarce. Towards this end, we present an
overview of QoE assessment for adaptive video streaming. The main contribu-
tions of this paper are summarized in three-fold as follows:
3

Big Data
Servers Users
QoE Management QoE Assessor
Devices
Streaming Data
Core Access
Network Network QoE Data
Service Optimization
Figure1: TheimportantroleofQoEassessmentinmultimediacommunicationsystems. The
designed QoE assessor is deployed to take the decoded streaming video data as input, and
thenpredictsperceptualvideostreamingqualityfortheserviceoptimization.
• We review subjective QoE assessment studies for adaptive video stream-
ing,wherethedetailsofvarioussubjectivequalitydatabasesaredescribed.
Different from traditional video subjective QoE assessment, we discuss
particular quality factors in these constructed databases.
• We review existing objective QoE assessment models for adaptive video
streaming,includingquality-of-service(QoS)drivenuserQoEassessment,
signal fidelity measurement, and hybrid models.
• WeanalyzeandcompareobjectiveQoEassessmentmodelswithorwithout
using machine learning for adaptive video streaming. Besides, we exploit
the deep feature representations from off-the-shelf DCNN models, which
is consistent with spatio-temporal human visual perception. Experiments
demonstrate its superior performance, leading to the promising future
directiontodevelopstreaming-awarequalitypredictionframeworksbased
on DCNN.
The structure of this article is as follows. In Section 2 and Section 3, we
review the relevant subjective quality databases and existing objective QoE
4

models for streaming video quality evaluation, respectively. In Section 4, we
analyze and compare different variations of QoE assessment models with or
without using machine learning for adaptive video streaming. Additionally, the
deep feature representations from off-the-shelf DCNN models show promising
resultsagainststate-of-the-artmethods,whichshedslightonthefuturedevelop-
mentofspecificdeeplearning-basedqualityevaluationframeworksforadaptive
video streaming. We conclude the results and discuss some future directions in
Section 5.
2. Subjective Studies
The perceptual quality of HAS streaming videos not only suffers from com-
pression distortions, but also degrades due to some streaming-specific issues,
such as initial buffering, playback stalling, etc. Up to now, some subjective
quality databases have been built for severing as the benchmarks for objective
QoE assessment models. Here, we give an introduction to the mainstream pub-
liclyavailablesubjectivedatabasesforadaptivevideostreamingduringthepast
decade. Thedetailsofpubliclyavailablesubjectivedatabasesforadaptivevideo
streaming can be found in Table 1.
Table1: DetailsofPubliclyAvailableSubjectiveDatabasesforAdaptiveVideoStreaming.
Databases #ofSourceVideos #ofDistortedVideos #ofCodecs ViewingDisplays
LIVEMVQA[16] 10 300 1 Phone&Tablet
LIVEQHVS[17] 3 15 1 HDTV
LIVEMSV[18] 24 180 0 Phone
WaterlooSQoE-I[19] 20 180 1 HDTV
LIVE-NFLX-I[20] 14 112 1 Phone
WaterlooSQoE-II[21] 12 588 1 HDTV
WaterlooSQoE-III[22] 20 450 1 HDTV
LIVE-NFLX-II[23] 15 420 1 HDTV
WaterlooSQoE-IV[24] 5 1,350 2 Phone&HDTV&UHDTV
The earliest adaptive video streaming subjective database dates back to
2012 when Moorthy et al. proposed the LIVE mobile video quality assessment
(LIVEMVQA)database[16]. Thisdatabaseconsistsof10sourcevideosand300
5

test videos. The distortion types include H.264 compression, wireless channel
packet loss, frame freezes, rate adaptation, and temporal dynamics. In the
subjective test, 200 distorted videos evaluated by over 30 subjects on a small
phone, as well as 100 distorted videos rated by 17 subjects on a larger tablet
device.
The LIVEQHVS [17] contains 3 original reference videos. The length of
eachvideoisrelativelylong,whichis300secondsduration. Thelongvideosare
constructed by concatenating 8 high-quality short video clips. For each source
video, 6 quality-varying videos are generated by applying various encoding bi-
trates of H.264 encoder. Among these 18 distorted videos, 3 of them are used
for the training of subjective studies, the remaining 15 quality-varying videos
are exploited for testing. These video sequences are displayed to the subjects
on a 58-inch high definition television (HDTV) monitor.
The LIVEMSV [18] includes 24 pristine videos with either 1280×720 pixels
or 640×360 pixels. Since this database focuses on network impairments, other
factors such as spatial distortions are minimized. There exist 180 distorted
videosproducedbyallthereferencevideoswith26uniquehand-craftedstalling
events. The subjective quality labels are obtained from 54 subjects, leading to
4,830 human opinions. The viewing display is Apple iPhone 5.
The WaterlooSQoE-I [19] considers both the compression and playback ar-
tifacts. With H.264 encoder, the original source videos are encoded into three
bitrate levels which include 500 Kbps, 1,500 Kbps, and 3,000 Kbps. Note that
these three bitrate levels are based on commonly available parameters of video
transmission over wireless communication networks. In addition, playback is-
sues are also taken into account in this database. To be specific, apart from
the introduced compression distortions, a five-second stalling event is then sim-
ulated at either the beginning or the middle time point of the encoded video
sequences. Therefore, the initial buffering and middle playback stalling stream-
ingvideoscanbeproducedbythiskindofsimulation. Intotal, thisdatabaseis
madeupof200videoscontaining20sourcevideos,60encodedvideos,60initial
buffering videos, and 60 middle playback stalling videos. A subjective study is
6

conducted to collect ratings of test videos on the HDTV display.
The LIVE-NFLX-I [20] is presented to investigate the influence of mixtures
fromadaptivestreamingvideoartifacts. Thedatabaseiscomposedof14source
videocontentsand112distortedvideosobtainedbyencodingtheoriginalvideos
using H.264 encoder. There are 8 different playout patterns including dynami-
cally changing H.264 compression rates, rebuffering events, and the mixtures of
both. The subjective experiment is conducted by 55 subjects on a mobile de-
vice. Itshouldbenotedthatonlythreereferencevideosandtheircorresponding
distorted videos are made publicly available in this database.
The WaterlooSQoE-II [21] involves 12 source videos, where each video has
8 seconds duration and is further partitioned into 4-second short segments.
The short segments are encoded into seven representations with H.264 codec.
To simulate quality adaptation events, two consecutive 4-second segments with
differentrepresentationsareconcatenatedfromthesamevideocontent,resulting
in 588 videos with variations in compression level, spatial resolution, and frame
rate. The videos are displayed at their pixel resolution on the HDTV display
for subjective quality collections.
Theabove-mentionedsubjectivequalitydatabasesforadaptivevideostream-
ing have a common issue that they are hand-crafted. That is, these databases
are far away from real-world streaming video distributions. Therefore, the
following recently established databases aim to tackle this problem, including
WaterlooSQoE-III [22], LIVE-NFLX-II [23], and WaterlooSQoE-IV [24].
Specifically,theWaterlooSQoE-III[22]andtheLIVE-NFLX-II[23]have450
and 420 realistic adaptive streaming videos, respectively. Both databases inte-
grate actual network traces to capture realistic network variations. Different
realistic adaptive bitrate (ABR) streaming algorithms [25, 26, 27] are employed
for video delivery. The subjective experiments conducted on the HDTV are
used to obtain subjective QoE ratings. The WaterlooSQoE-IV [24] provides so
far the most comprehensive QoE assessment database which consists of 1,350
subjective-ratedstreamingvideosthatarederivedfromavarietyofsourcevideo
contents, video codecs, network conditions, ABR algorithms, and viewing dis-
7

plays. For example, except for mobile phone and HDTV, the Ultra HDTV
| (UHDTV) | is also          | applied | in subjective     | studies. |              |       |            |        |
| ------- | ---------------- | ------- | ----------------- | -------- | ------------ | ----- | ---------- | ------ |
| With    | these subjective |         | quality databases |          | for adaptive | video | streaming, | effec- |
tive quality labels are provided for designing objective quality assessment al-
gorithms, which facilitates researchers to propose objective quality assessment
modelsthatareclosertohumanvisualperception. Besides,wecanmeasureand
compare the performance of different adaptive video streaming quality evalua-
| tion models  | on these  | databases. |                  |     |             |           |         |        |
| ------------ | --------- | ---------- | ---------------- | --- | ----------- | --------- | ------- | ------ |
| 3. Objective | Models    |            |                  |     |             |           |         |        |
| In general,  | according |            | to the existence |     | of original | reference | videos, | tradi- |
tional objective Video QoE Assessment (VQA) methods can be classified into
full-reference (FR) VQA, reduced-reference (RR) VQA, and no-reference (NR)
VQA. Specifically, FR VQA methods [28, 29, 30] require the corresponding
original reference video. The RR VQA methods assume that a portion of the
reference video is available, which can be some parameters extracted from the
originalcontentoradditionalsideinformationaddedtothetestvideo. TheNR
VQA algorithms [31, 32, 33] evaluate visual quality without any information
from the corresponding original reference video, which are more practical in
| application | scenarios.  |       |              |         |           |     |                    |     |
| ----------- | ----------- | ----- | ------------ | ------- | --------- | --- | ------------------ | --- |
| In the      | literature, | there | have emerged | several | objective |     | quality assessment |     |
models for adaptive video streaming. Apart from the classification method of
conventional VQA methods that is based on the information of original refer-
ence videos, existing video streaming QoE assessment models can be generally
classified into three categories which include QoS driven user QoE assessment
[34, 35], signal fidelity measurement [28, 29, 30], and hybrid models [19, 36].
Specifically, the QoS driven user QoE assessment exploits the causal relation-
ship between QoS and QoE problems, while the signal fidelity measurement
takes the QoE assessment problem from the aspect of signal fidelity. The hy-
bridmodelscomprehensivelyconsidertheQoSdrivenuserQoEassessmentand
8

the signal fidelity measurement at the same time. Moreover, solid related work
has been done on automatic video streaming QoE assessment models with or
withoutusingmachinelearningtechniques. Table2liststhesummaryofobjec-
tive QoE assessment models for adaptive video streaming. It should be noted
thatweonlyfocusonthementionedQoEassessmentmodelsforadaptivevideo
streaming in this paper, other algorithms could be found in [37].
Table2: SummaryofobjectiveQoEAssessmentModelsforAdaptiveVideoStreaming.
Methods Learning Types
FTW [34] No QoS driven QoE assessment
VsQM [35] No QoS driven QoE assessment
PSNR No Signal fidelity measurement
SSIM [28] No Signal fidelity measurement
MS-SSIM [29] No Signal fidelity measurement
SSIMplus [30] No Signal fidelity measurement
SQI [19] No Hybrid model
Video ATLAS [36] Yes Hybrid model
AsforQoSdrivenuserQoEassessment,themappingfunctionsbetweenQoS
andQoEproblemsareusuallyemployed. Forexample,severalQoSmodelssuch
as FTW [34] and VsQM [35] have been proposed by utilizing global rebuffering
statistics and the pattern of temporal local content importance. However, the
video quality impairment caused by video compression has not been taken into
consideration.
For signal fidelity measurement, conventional objective VQA metrics con-
sider human visual perception rather than the simplest peak signal-to-noise ra-
tio (PSNR), such as the structural similarity index (SSIM) [28], the multi-scale
structure similarity index (MS-SSIM) [29], the SSIMplus [30], and so on. How-
ever, all of these algorithms are under the assumption that the playback can be
exactly controlled. But in the applications of QoE assessment for HAS stream-
ing videos, due to network transmission impairments, these services may suffer
9

| from some     | playback | issues        | which could | bring | significant | quality | degradation. |          |
| ------------- | -------- | ------------- | ----------- | ----- | ----------- | ------- | ------------ | -------- |
| Additionally, |          | hybrid models | integrate   |       | the scheme  | of QoS  | driven       | user QoE |
assessment with the scheme of signal fidelity measurement. In [19], a unified
video streaming QoE assessor without using machine learning named stream-
ing quality index (SQI) has been proposed, which combines FR quality metrics
such as SSIM and MS-SSIM with stalling related information. In other words,
the impact of compression and stalling are modeled simultaneously. Moreover,
in [36], the machine learning-based model called video assessment of tempo-
ral artifacts and stalls (Video ATLAS) has been presented, where a number of
QoE-relatedfeatures,includingobjectivequalityfeatures,rebuffering-awarefea-
tures and memory-driven features, are utilized to predict the perceptual video
| streaming        | quality. |                    |          |      |           |         |         |       |
| ---------------- | -------- | ------------------ | -------- | ---- | --------- | ------- | ------- | ----- |
| 4. Performance   |          | Analysis           |          |      |           |         |         |       |
| 4.1. Performance |          | Evaluation         | Criteria |      |           |         |         |       |
| According        | to       | the recommendation |          | from | the Video | Quality | Experts | Group |
[38], we adopt two widely used criteria including the Spearman rank-order cor-
relation coefficient (SROCC) and Pearson linear correlation coefficient (PLCC)
to analyze and compare different objective algorithms for video streaming QoE
assessment. The SROCC performance is utilized to measure QoE prediction
monotonicity, while the PLCC performance is applied to evaluate QoE predic-
tion accuracy.
| Moreover, | before | computing | the | PLCC | performance |     | of objective | QoE as- |
| --------- | ------ | --------- | --- | ---- | ----------- | --- | ------------ | ------- |
sessment algorithms, a nonlinear logistic fitting is generally used to map the
predicted quality scores to the same scales of subjective quality ratings. Here,
higher SROCC and PLCC correlation coefficients indicate better performance
| and agreement | with     | subjective | human    | quality | perception. |     |            |        |
| ------------- | -------- | ---------- | -------- | ------- | ----------- | --- | ---------- | ------ |
| 4.2. Results  | of Video | Streaming  | QoE      | Models  |             |     |            |        |
| Considering   | that     | existing   | adaptive | video   | streaming   | QoE | assessment | models |
consistofQoSdrivenQoEmethods,signalfidelitymeasurement,andhybridap-
10

Figure2: VideocontentsinWaterlooSQoE-Idatabase[19].
proacheswhichcombineFRqualitymetricswithrebufferingrelatedfeatures,we
conduct experiments on the representative WaterlooSQoE-I database [36]. The
reasonforchoosingtheWaterlooSQoE-Idatabaseisthatitisthefirstdatabase
containing the most abundant video contents and codecs. Figure 2 shows that
thereexist20originalreferencevideosconsistingofdiversevideocontentsinthe
WaterlooSQoE-I database [19]. With these pristine sources, streaming videos
impaired from both compression distortions and playback issues can be gener-
ated.
We first analyze different variations of objective quality assessment models
with or without using machine learning for adaptive video streaming. Figure 3
shows the performance comparison of existing video streaming QoE assessment
11

1
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
SROCC PLCC
Figure 3: Performance comparison of existing video streaming QoE assessment models on
WaterlooSQoE-Idatabase[19].
models on WaterlooSQoE-I database [19]. In this figure, the Video ATLAS is
the only machine learning-based method. And the regression model with the
best SROCC performance is reported.
In general, as we can see from Figure 3, hybrid models outperform QoS
driven QoE models (i.e. FTW and VsQM) as well as the signal fidelity mea-
surement when using the same FR quality metrics. Additionally, the machine
learning-based QoE assessment model, namely Video ATLAS, is slightly supe-
rior to the SQI model without using machine learning for the same FR quality
metrics combination. One possible explanation is that the machine learning-
based method learns distortion-related features better directly from streaming
videos.
Based on these observations, we can conclude that existing video streaming
QoEassessmentalgorithmsstillhavelimitedperformance,makingitdifficultto
be employed in practical applications. At the same time, deep learning models
have been studied to understand the development of human sensory cortical
processing [39]. Besides, deep convolutional neural network (DCNN) has been
12

applied to perceptual quality assessment, which demonstrates the remarkable
ability of DCNN to learn discriminative features for addressing this challenging
task [40, 41, 42]. However, to the best of our knowledge, there is no similar
researchworkaboutdeeplearningsolutionstohybridNRvideostreamingQoE
assessmentbasedonspatio-temporalvisualcontentfeaturesinstreamingvideos.
Thus, we apply a simplified framework to tackle the adaptive video streaming
quality assessment, where we only exploit distorted streaming videos without
referringtothecorrespondingsourcevideos. Thatis,thismethodbelongstothe
category of no-reference video streaming QoE models, which is more practical
in real applications.
Specifically, considering that a streaming video sequence is composed of
manyvideoframes,wefirstextractmultipledistortedvideoframesfromstream-
ingvideosequences. Apartfromthespatialcharacteristicsofdifferentdistorted
video frames, note that a video sequence is a set of consecutive video frames
whichcontainavarietyofmotionattributes. Inotherwords,thetemporalvari-
ationofvideocontentscouldaffectthevisualperceptionoftheHVStoacertain
degree. Thus, compared to image quality prediction, video streaming QoE as-
sessment is more complex due to the additional temporal quality variation. We
then utilize frame difference maps to take the temporal factor into account,
which are simply defined as the difference between adjacent video frames.
The two pre-trained DCNN models take distorted video frames and frame
differencemapsasinputstoextractthe2,048-dimfeaturesfromthepool5layer.
Note that the two employed ResNet50 architectures have the same configura-
tion and share weights with each other. Then, the concatenation of the ex-
tracted 2,048-dim features constitute a 4,096-dim feature vector. Finally, the
well-knownregressionmodel(i.e. SVR)isappliedtomapthe4,096-dimfeature
vector into the ultimate perceptual quality score for each streaming video. In
addition, it should be noted that the used database is randomly divided into
80%fortrainingandtheremaining20%fortesting. Weperform1,000iterations
of cross correlation, and then give the median SROCC and PLCC values as the
final measurement.
13

0.98
0.96
0.94
0.92
0.9
0.88
0.86
SROCC PLCC
Figure 4: Performance comparison of the extended video streaming QoE assessment model
andstate-of-the-artsonWaterlooSQoE-Idatabase[19].
Figure4showstheperformancecomparisonwithstate-of-the-artvideostream-
ing QoE models. Note that we choose the top two algorithms shown in Figure
3 to be compared, which include no machine learning (i.e. SSIM+SQI and
SSIMplus+SQI) and machine learning-based (i.e. SSIM+ATLAS and SSIM-
plus+ATLAS) video streaming QoE assessment models. We denote the deep
learning models as “Distorted Video Frame”, “Frame Difference Map”, and
“Proposed Combination”, in which we separately apply the deep learned fea-
tures from distorted video frames, frame difference maps, and the combination
of distorted video frames and frame difference maps. As shown in this figure,
the deep learning models perform better than the other methods. Moreover,
onlyusingframedifferencemapsoutperformsthatofonlyusingdistortedvideo
frames. One possible explanation may be that the temporal motion attributes
have more impact on the perceptual quality of streaming videos compared with
thatofthespatialtexturecharacteristics. Additionally,thecombinationofspa-
tialandtemporalfeaturesoutperformseitherthespatialfeatureorthetemporal
feature alone, which further verifies the significance of spatio-temporal human
14

Figure 5: Visualization of learned kernels in the first convolutional layer for the pre-trained
| ResNet50network.  | Thelearnedkernelscapturevariousintrinsicimagetexturepatterns. |                  |                   |                  |
| ----------------- | ------------------------------------------------------------- | ---------------- | ----------------- | ---------------- |
| visual perception | in adaptive                                                   | video streaming. |                   |                  |
| To reveal         | the discriminative                                            | information      | from deep learned | features, Figure |
5 presents the visualization of learned kernels in the first convolutional layer
for the pre-trained ResNet50 network. It should be noted that the ResNet50
modelispre-trainedonalarge-scaledatasetwithdiverseimagecontents,namely
ImageNet [43]. Therefore, we can see that the learned kernels can capture
intrinsic image texture patterns. In other words, the pre-trained ResNet50
model has a promising ability to represent discriminative features for quality
assessment,whichshedslightonthefuturedevelopmentofspecificallydesigned
| deep learning | models for | adaptive video | streaming quality | evaluation. |
| ------------- | ---------- | -------------- | ----------------- | ----------- |
| 5. Conclusion | and Future | Directions     |                   |             |
Inthispaper,wepresentabriefsurveyofQoEassessmentforadaptivevideo
streaming. First, the QoE assessor plays a vital role in multimedia communi-
cation systems. Considering complex characteristics of streaming videos, many
challenges are involved in the perceptual quality prediction task. We then re-
view both subjective studies and objective models for adaptive video streaming
qualityassessment. Finally, weconductcomparisonsofexistingstate-of-the-art
15

QoE assessment models for streaming videos, with or without using machine
learning techniques. The performance analysis shows that hybrid models out-
performQoSdrivenQoEmodelsandthesignalfidelitymeasurementwhenusing
thesameFRqualitymetrics. Furthermore,themachinelearning-basedQoEas-
sessment model is demonstrated slightly superior to the model without using
machine learning. However, these approaches still have limited performance for
| video streaming | QoE | assessment. |          |                         |      |               |
| --------------- | --- | ----------- | -------- | ----------------------- | ---- | ------------- |
| Additionally,   | we  | apply       | the deep | feature representations | from | off-the-shelf |
DCNN models based on spatio-temporal human visual perception, which can
deliver promising results. This demonstrates that specific deep learning frame-
works for QoE assessment of adaptive video streaming should be addressed
in the future. Furthermore, more comprehensive investigation about adaptive
video streaming quality assessment could be considered, where the design of
immersive 3D/stereoscopic video streaming QoE assessment methods based on
deepneuralnetworksisanotherresearchdirection. For3DvideostreamingQoE
assessment, except for video quality, more quality dimensions should be taken
| into consideration, | e.g. | depth | perception | and visual comfort. |     |     |
| ------------------- | ---- | ----- | ---------- | ------------------- | --- | --- |
References
[1] T.Stockhammer,DynamicadaptivestreamingoverHTTP–: standardsand
| designprinciples,in: |          | ProceedingsofthesecondannualACMconferenceon |       |              |     |     |
| -------------------- | -------- | ------------------------------------------- | ----- | ------------ | --- | --- |
| Multimedia           | systems, | ACM,                                        | 2011, | pp. 133–144. |     |     |
[2] M. G. Kibria, K. Nguyen, G. P. Villardi, O. Zhao, K. Ishizu, F. Kojima,
| Big data   | analytics, | machine   | learning | and artificial | intelligence | in next- |
| ---------- | ---------- | --------- | -------- | -------------- | ------------ | -------- |
| generation | wireless   | networks, | IEEE     | Access.        |              |          |
[3] M. Alreshoodi, J. Woods, Survey on QoE\QoS correlation models for mul-
| timedia | services, | arXiv | preprint | arXiv:1306.0221. |     |     |
| ------- | --------- | ----- | -------- | ---------------- | --- | --- |
[4] I.-T. T. S. Sector, O. ITU, Quality of experience requirements for IPTV
| services, | Recommendation |     | ITU-T | G 1080. |     |     |
| --------- | -------------- | --- | ----- | ------- | --- | --- |
16

[5] K.Seshadrinathan,R.Soundararajan,A.C.Bovik,L.K.Cormack,Asub-
jective study to evaluate video quality assessment algorithms, in: Human
Vision and Electronic Imaging XV, Vol. 7527, SPIE, 2010, pp. 128–137.
[6] J. Y. Lin, R. Song, C.-H. Wu, T. Liu, H. Wang, C.-C. J. Kuo, MCL-V: A
streaming video quality assessment database, Journal of Visual Communi-
cation and Image Representation 30 (2015) 1–9.
[7] J. Xu, C. Lin, W. Zhou, Z. Chen, Subjective quality assessment of stereo-
scopic omnidirectional image, in: Pacific Rim Conference on Multimedia,
Springer, 2018, pp. 589–599.
[8] S. Chikkerur, V. Sundaram, M. Reisslein, L. J. Karam, Objective video
quality assessment methods: A classification, review, and performance
comparison, IEEE Transactions on Broadcasting 57 (2) (2011) 165–182.
[9] Q.Jiang,F.Shao,G.Jiang,M.Yu,Z.Peng,Superviseddictionarylearning
for blind image quality assessment using quality-constraint sparse coding,
JournalofVisualCommunicationandImageRepresentation33(2015)123–
133.
[10] L. Li, W. Xia, Y. Fang, K. Gu, J. Wu, W. Lin, J. Qian, Color image qual-
ity assessment based on sparse representation and reconstruction residual,
JournalofVisualCommunicationandImageRepresentation38(2016)550–
560.
[11] W.Zhou,Z.Chen,W.Li,Dual-streaminteractivenetworksforno-reference
stereoscopic image quality assessment, IEEE Transactions on Image Pro-
cessing 28 (8) (2019) 3946–3958.
[12] J. Kim, H. Zeng, D. Ghadiyaram, S. Lee, L. Zhang, A. C. Bovik, Deep
convolutional neural models for picture-quality prediction: Challenges and
solutions to data-driven image quality assessment, IEEE Signal Processing
Magazine 34 (6) (2017) 130–141.
17

[13] W.Lin, C.-C.J.Kuo, Perceptualvisualqualitymetrics: Asurvey, Journal
ofVisualCommunicationandImageRepresentation22(4)(2011)297–312.
[14] M.T.Vega,V.Sguazzo,D.C.Mocanu,A.Liotta,Anexperimentalsurvey
of no-reference video quality assessment methods, International Journal of
Pervasive Computing and Communications.
[15] G. Zhai, X. Min, Perceptual image quality assessment: A survey, Science
China Information Sciences 63 (11) (2020) 1–52.
[16] A. K. Moorthy, L. K. Choi, A. C. Bovik, G. De Veciana, Video quality
assessmentonmobiledevices: Subjective,behavioralandobjectivestudies,
IEEEJournalofSelectedTopicsinSignalProcessing6(6)(2012)652–671.
[17] C. Chen, L. K. Choi, G. De Veciana, C. Caramanis, R. W. Heath, A. C.
Bovik,ModelingthetimevaryingsubjectivequalityofHTTPvideostreams
with rate adaptations, IEEE Transactions on Image Processing 23 (5)
(2014) 2206–2221.
[18] D. Ghadiyaram, A. C. Bovik, H. Yeganeh, R. Kordasiewicz, M. Gallant,
Studyoftheeffectsofstallingeventsonthequalityofexperienceofmobile
streaming videos, in: IEEE Global Conference on Signal and Information
Processing, IEEE, 2014, pp. 989–993.
[19] Z.Duanmu,K.Zeng,K.Ma,A.Rehman,Z.Wang,Aquality-of-experience
index for streaming video, IEEE Journal of Selected Topics in Signal Pro-
cessing 11 (1) (2017) 154–166.
[20] C. G. Bampis, Z. Li, A. K. Moorthy, I. Katsavounidis, A. Aaron, A. C.
Bovik, Study of temporal effects on subjective video quality of experience,
IEEE Transactions on Image Processing 26 (11) (2017) 5217–5231.
[21] Z. Duanmu, K. Ma, Z. Wang, Quality-of-experience of adaptive video
streaming: Exploringthespaceofadaptations, in: Proceedingsofthe25th
ACM international conference on Multimedia, 2017, pp. 1752–1760.
18

[22] Z. Duanmu, A. Rehman, Z. Wang, A quality-of-experience database for
adaptivevideostreaming,IEEETransactionsonBroadcasting64(2)(2018)
474–487.
[23] C. G. Bampis, Z. Li, I. Katsavounidis, T.-Y. Huang, C. Ekanadham, A. C.
Bovik,Towardsperceptuallyoptimizedadaptivevideostreaming-arealistic
qualityofexperiencedatabase, IEEETransactionsonImageProcessing30
(2021) 5182–5197.
[24] Z. Duanmu, W. Liu, Z. Li, D. Chen, Z. Wang, Y. Wang, W. Gao, As-
sessingthequality-of-experienceofadaptivebitratevideostreaming,arXiv
preprint arXiv:2008.08804.
[25] Z. Li, X. Zhu, J. Gahm, R. Pan, H. Hu, A. C. Begen, D. Oran, Probe and
adapt: Rate adaptation for HTTP video streaming at scale, IEEE Journal
on Selected Areas in Communications 32 (4) (2014) 719–733.
[26] X. Yin, A. Jindal, V. Sekar, B. Sinopoli, A control-theoretic approach for
dynamicadaptivevideostreamingoverHTTP,in: ProceedingsoftheACM
Conference on Special Interest Group on Data Communication, 2015, pp.
325–338.
[27] Z. Akhtar, Y. S. Nam, R. Govindan, S. Rao, J. Chen, E. Katz-Bassett,
B. Ribeiro, J. Zhan, H. Zhang, Oboe: Auto-tuning video ABR algorithms
to network conditions, in: Proceedings of the Conference of the ACM Spe-
cial Interest Group on Data Communication, 2018, pp. 44–58.
[28] Z. Wang, A. C. Bovik, H. R. Sheikh, E. P. Simoncelli, Image quality as-
sessment: from error visibility to structural similarity, IEEE transactions
on image processing 13 (4) (2004) 600–612.
[29] Z.Wang, E.P.Simoncelli, A.C.Bovik, Multiscalestructuralsimilarityfor
image quality assessment, in: The Thrity-Seventh Asilomar Conference on
Signals, Systems & Computers, 2003, Vol. 2, Ieee, 2003, pp. 1398–1402.
19

[30] A. Rehman, K. Zeng, Z. Wang, Display device-adapted video quality-of-
experienceassessment, in: HumanVisionandElectronicImagingXX,Vol.
9394, International Society for Optics and Photonics, 2015, p. 939406.
[31] Z. Chen, N. Liao, X. Gu, F. Wu, G. Shi, Hybrid distortion ranking tuned
bitstream-layer video quality assessment, IEEE Transactions on Circuits
and Systems for Video Technology 26 (6) (2016) 1029–1043.
[32] W. Zhou, N. Liao, Z. Chen, W. Li, 3D-HEVC visual quality assessment:
Database and bitstream model, in: Quality of Multimedia Experience
(QoMEX), 2016 Eighth International Conference on, IEEE, 2016, pp. 1–6.
[33] Z. Chen, W. Zhou, W. Li, Blind stereoscopic video quality assessment:
From depth perception to overall experience, IEEE Transactions on Image
Processing 27 (2) (2018) 721–734.
[34] T.Hoßfeld,M.Seufert,M.Hirth,T.Zinner,P.Tran-Gia,R.Schatz,Quan-
tification of YouTube QoE via crowdsourcing, in: Multimedia (ISM), 2011
IEEE International Symposium on, IEEE, 2011, pp. 494–499.
[35] D.Z.Rodriguez,J.Abrahao,D.C.Begazo,R.L.Rosa,G.Bressan,Quality
metrictoassessvideostreamingserviceoverTCPconsideringtemporallo-
cationofpauses,IEEETransactionsonConsumerElectronics58(3)(2012)
985–992.
[36] C. G. Bampis, A. C. Bovik, Learning to predict streaming video QoE:
Distortions, rebuffering and memory, arXiv preprint arXiv:1703.00633.
[37] N. Barman, M. G. Martini, QoE modeling for HTTP adaptive video
streaming–a survey and open challenges, IEEE Access 7 (2019) 30831–
30859.
[38] V.Q.E.Group,etal.,Finalreportfromthevideoqualityexpertsgroupon
the validation of objective models of video quality assessment, in: VQEG
meeting, Ottawa, Canada, March, 2000, 2000.
20

[39] D. L. Yamins, J. J. DiCarlo, Using goal-driven deep learning models to
| understand | sensory | cortex, | Nature | neuroscience |     | 19 (3) (2016) | 356. |
| ---------- | ------- | ------- | ------ | ------------ | --- | ------------- | ---- |
[40] M. Lopez-Martin, B. Carro, J. Lloret, S. Egea, A. Sanchez-Esguevillas,
| Deep learning | model         | for multimedia |                | quality | of experience |          | prediction based |
| ------------- | ------------- | -------------- | -------------- | ------- | ------------- | -------- | ---------------- |
| on network    | flow packets, | IEEE           | Communications |         |               | Magazine | 56 (9) (2018)    |
110–117.
[41] W. Zhou, Z. Chen, W. Li, Stereoscopic video quality prediction based on
| end-to-end     | dual stream | deep  | neural | networks, | in: | Pacific | Rim Conference |
| -------------- | ----------- | ----- | ------ | --------- | --- | ------- | -------------- |
| on Multimedia, | Springer,   | 2018, | pp.    | 482–492.  |     |         |                |
[42] W. Zhou, Z. Chen, Deep local and global spatiotemporal feature aggrega-
| tion for  | blind video    | quality | assessment, | in:         | IEEE | International | Conference     |
| --------- | -------------- | ------- | ----------- | ----------- | ---- | ------------- | -------------- |
| on Visual | Communications |         | and Image   | Processing, |      | IEEE,         | 2020, pp. 338– |
341.
[43] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, L. Fei-Fei, ImageNet: A
| large-scalehierarchicalimagedatabase,in: |             |              |       |       | IEEEConferenceonComputer |          |     |
| ---------------------------------------- | ----------- | ------------ | ----- | ----- | ------------------------ | -------- | --- |
| Vision                                   | and Pattern | Recognition, | IEEE, | 2009, | pp.                      | 248–255. |     |
21
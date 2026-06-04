|     |     | On  | the (In)Security |     |     | of  | Loading | Machine | Learning |     | Models |     |     |     |     |
| --- | --- | --- | ---------------- | --- | --- | --- | ------- | ------- | -------- | --- | ------ | --- | --- | --- | --- |
Gabriele Digregorio, Marco Di Gennaro, Stefano Zanero, Stefano Longari, Michele Carminati
|     |     |     |     |     |     | Politecnico |        | di Milano |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |             | Milan, | Italy     |     |     |     |     |     |     |     |
{gabriele.digregorio, marco.digennaro, stefano.zanero, stefano.longari, michele.carminati}@polimi.it
[17],[18],[19]remainsfragmented,whichmaycontributeto
| Abstract—The |     | rise of model | sharing | through | frameworks |     | and |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------- | ------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dedicated hubs makes Machine Learning significantly more limited awareness among users, framework developers, and
accessible. Despite its benefits, loading shared models exposes sharinghubs.Zhuetal.[20]furthersuggestopenchallenges
userstounderexploredsecurityrisks,whilesecurityawareness in this space by showing that TensorFlow APIs can be
|         |         |       |                    |     |     |             |     | abused | for file and | network | access | at  | inference | time. | The |
| ------- | ------- | ----- | ------------------ | --- | --- | ----------- | --- | ------ | ------------ | ------- | ------ | --- | --------- | ----- | --- |
| remains | limited | among | both practitioners |     | and | developers. | To  |        |              |         |        |     |           |       |     |
enableamoresecurity-consciousapproachinMachineLearn- growingrelevanceoftheproblemisalsoreflectedinarecent
ing model sharing, in this paper,we evaluate the security pos- DEF CON 33 talk [21], which highlighted persistent risks
|     |     |     |     |     |     |     |     | in model | sharing, such | as  | insecure | pickle | deserialization. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | -------- | ------ | ---------------- | --- | --- |
tureofframeworksandhubs,assesswhethersecurity-oriented
|            |                 |                  |                 |             |       |                |         | Our              | work provides | a      | systematic    | analysis     |            | of the security |      |
| ---------- | --------------- | ---------------- | --------------- | ----------- | ----- | -------------- | ------- | ---------------- | ------------- | ------ | ------------- | ------------ | ---------- | --------------- | ---- |
| mechanisms | offer           | real protection, |                 | and survey  | how   | users          | per-    |                  |               |        |               |              |            |                 |      |
|            |                 |                  |                 |             |       |                |         | landscape        | of ML         | model  | sharing.      | We           | evaluate   | major           | ML   |
| ceive the  | security        | narratives       | surrounding     |             | model | sharing.       | Our     |                  |               |        |               |              |            |                 |      |
|            |                 |                  |                 |             |       |                |         | frameworks       | and sharing   |        | hubs, uncover |              | previously | unknown         |      |
| evaluation | shows           | that             | most frameworks |             | and   | hubs           | address |                  |               |        |               |              |            |                 |      |
|            |                 |                  |                 |             |       |                |         | vulnerabilities, | and           | expose | a             | misalignment |            | between         | per- |
| security   | risks partially | at               | best, often     | by shifting |       | responsibility |         |                  |               |        |               |              |            |                 |      |
ceivedandactualsecuritymechanisms.Overall,ourfindings
| to the user. | More | concerningly, |     | our analysis | of  | frameworks |     |           |          |          |     |      |       |          |        |
| ------------ | ---- | ------------- | --- | ------------ | --- | ---------- | --- | --------- | -------- | -------- | --- | ---- | ----- | -------- | ------ |
|              |      |               |     |              |     |            |     | emphasize | the need | to apply | the | same | level | of rigor | to the |
advertisingsecurity-orientedsettingsandcompletemodelshar-
|     |     |     |     |     |     |     |     | study of | model-sharing |     | threats | as is | currently | devoted | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | ------- | ----- | --------- | ------- | --- |
inguncoveredmultiple0-dayvulnerabilitiesenablingarbitrary
|     |     |     |     |     |     |     |     | open-source | software | security | at  | large. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | -------- | --- | ------ | --- | --- | --- |
codeexecution.Throughthisanalysis,weshowthat,despitethe
|     |     |     |     |     |     |     |     | We  | consider a | threat | model | where | attackers | craft | mali- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ----- | ----- | --------- | ----- | ----- |
recentnarrative,securelyloadingMachineLearningmodelsis
ciousmodelartifactstocompromiseavictim’ssystem,with
| far from    | being  | a solved | problem      | and cannot |        | be guaranteed |      |                  |                |     |        |       |              |     |        |
| ----------- | ------ | -------- | ------------ | ---------- | ------ | ------------- | ---- | ---------------- | -------------- | --- | ------ | ----- | ------------ | --- | ------ |
|             |        |          |              |            |        |               |      | arbitrary        | code execution |     | as the | goal. | Our research | is  | driven |
| by the file | format | used     | for sharing. | Our        | survey | shows         | that |                  |                |     |        |       |              |     |        |
|             |        |          |              |            |        |               |      | by the questions | defined        |     | below: |       |              |     |        |
thesecuritynarrativeleadsuserstoconsidersecurity-oriented
|            |                 |     |                    |            |               |       |         | RQ1. What  | is the  | security   | posture |               | of the | model-sharing |       |
| ---------- | --------------- | --- | ------------------ | ---------- | ------------- | ----- | ------- | ---------- | ------- | ---------- | ------- | ------------- | ------ | ------------- | ----- |
| settings   | as trustworthy, |     | despite the        | weaknesses |               | shown | in this |            |         |            |         |               |        |               |       |
|            |                 |     |                    |            |               |       |         | mechanisms | adopted | by popular |         | ML frameworks |        | and           | hubs? |
| work. From | this,           | we  | derive suggestions |            | to strengthen |       | the     |            |         |            |         |               |        |               |       |
security of model-sharing ecosystems. RQ2. Are approaches claiming security, while offering full
|     |     |     |     |     |     |     |     | model object | sharing, | actually |     | secure? |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | -------- | --- | ------- | --- | --- | --- |
1. Introduction RQ3.Istheuser’sperceptionofthesecuritypostureconsis-
|     |     |     |     |     |     |     |     | tent with     | reality, or | does               | the security |     | narrative | affect | their |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | ------------------ | ------------ | --- | --------- | ------ | ----- |
|     |     |     |     |     |     |     |     | understanding | of the      | sharing-associated |              |     | risks?    |        |       |
Inrecentyears,theadoptionofMachineLearning(ML)
has grown rapidly, with advanced tools once limited to To answer RQ1, we analyze how the most popular ML
experts now accessible to a broad audience. Among other frameworks and hubs address model sharing. We observe
factors, this trend is driven by the rise of platforms for that while some of them do not address security at all, oth-
sharingpre-trainedmodels[1],[2],[3],[4],[5].Suchmodels ers provide security-oriented mechanisms based on shifting
are often advertised as ready-to-use, lowering entry barriers responsibility to other parts of the sharing workflow or on
and enabling practitioners with different levels of expertise restricting the expressiveness of the model representation.
| to incorporate |     | ML into | their workflows. |     |     |     |     |         |               |         |     |            |     |           |      |
| -------------- | --- | ------- | ---------------- | --- | --- | --- | --- | ------- | ------------- | ------- | --- | ---------- | --- | --------- | ---- |
|                |     |         |                  |     |     |     |     | Some go | further, with | certain |     | frameworks |     | providing | com- |
This trend reflects the evolution of traditional software plete model-sharing capabilities while explicitly promoting
development, where open-source repositories enable the themselvesassecurity-oriented,andsomehubsemphasizing
reuse and adaptation of algorithms, code, and libraries. the same security focus through safeguards such as content
| Today, | models | are shared | and | reused, | enabling | a   | collab- |           |                |     |               |     |         |            |     |
| ------ | ------ | ---------- | --- | ------- | -------- | --- | ------- | --------- | -------------- | --- | ------------- | --- | ------- | ---------- | --- |
|        |        |            |     |         |          |     |         | scanning. | This narrative |     | is reinforced |     | through | documenta- |     |
orative ecosystem that is reshaping how ML is practiced. tion and naming choices (e.g., Keras’s “safe mode” [22]),
However, unlike the well-studied risks of code sharing and and is often justified by the use of data-based formats,
software supply chains [6], [7], [8], [9], [10], [11], [12], the assumed to reduce the risk of arbitrary code execution.
security implications of ML model sharing remain largely This class of security-oriented sharing frameworks and
underexplored. Prior work on malicious code injection in hubs led to RQ2, which motivates a vulnerability assess-
models [13], [14], [15], [16] and on hub security gaps [16], ment of their features. In our investigation, we discovered

a remarkably low number of pre-existing Common Vul- sharing mechanisms that are not officially endorsed by the
nerabilities and Exposures (referred to as CVEs) affecting frameworks and hubs analyzed in this study. This section
these mechanisms. Through a manual reverse engineering provides the necessary background, while the security im-
analysis, we uncovered six 0-day vulnerabilities (i.e., previ- plications of model sharing are discussed in Section 3.
ously undisclosed), each enabling arbitrary code execution.
Among these, we identified the first officially recognized 2.1. Framework-level Sharing
CVEstargetingKeras’s“safemode”[23],[24].Collectively,
these vulnerabilities challenge the widespread assumption
During our preliminary analysis, we observed that
that data-based formats (e.g., JSON) are inherently secure
framework-level model sharing formats can differ both in
whenusedtosharefullmodelobjects.Overall,ourfindings
thecontenttheystoreandinthewaytheyrepresentamodel.
inresponsetoRQ2revealacriticalgapbetweenthesecurity
With respect to the stored content, we observed that some
narrative and the actual implementation.
formats include all components needed to restore a model
This understanding led to RQ3. To address it, we con-
via a single loading API, while others store only weights
ducted a survey targeting ML practitioners to examine how
or configurations and require a separate model definition.
thesecuritynarrativespromotedbyframeworksandhubsin-
We refer to the former as self-contained formats and to
fluenceuserperception.Theresultsworryinglyindicatethat
the latter as non-self-contained formats. Regarding model
security-oriented terminology and claims in documentation
representation, some formats serialize model code objects
significantly shape users’ sense of security.
directly (e.g., pickle), whereas others describe model struc-
We conclude our paper with takeaways and suggestions
tures declaratively (e.g., JSON). We refer to the former as
for users and developers, synthesized from the observations
code-based formats and to the latter as data-based formats.
and insights obtained through our research questions.
We then systematically analyze these two dimensions
Contributions. We make the following contributions: (i.e., stored content and model representation) across the
• We systematize and analyze the security of ML model- five most widely adopted ML frameworks, as identified
sharing mechanisms, covering both framework-level and in the 2022 Kaggle ML & DS Survey [35]: Tensor-
hub-level perspectives. Flow [26], Keras [25], PyTorch [29], scikit-learn [31], and
• We assess methods that claim security while offering full XGBoost [33]. Notably, TensorFlow is the only one in this
modelobjectsharing,identifyingseveralCVEs,andchal- group that is not strictly Python-based, highlighting the
lenging the common assumption that data-based formats dominance of Python in ML fields. According to the same
are inherently secure. survey,88.3%ofMLpractitionersidentifiedPythonastheir
• We reveal a disconnect between the perceived security primary programming language, far surpassing all alterna-
narrative (and the resulting community belief) and the tives. This distribution is further confirmed by the 2024
reality through a survey on model sharing. JetBrains Python Developers Survey [36], which reports
• We provide takeaways for the community to promote a usage rates of 48% for TensorFlow, 30% for Keras, 60%
more security-aware culture in model sharing. for PyTorch, 67% for scikit-learn, and 22% for XGBoost.
Wenowanalyzethemodel-sharingtechniquessuggested
Open Science. We provide all artifacts necessary to re-
by the official documentation of each selected framework.
produce our empirical results. A repository, available at
Table 1 summarizes their main characteristics and security
https://zenodo.org/records/19224108, contains the frozen
implications, discussed in Section 3.
version of our proof-of-concept (PoC) exploits, model ar-
tifacts, survey data, and analysis scripts, i.e., the exact
2.1.1. Keras. KerasisaDeepLearningAPI[25]tightlyin-
version evaluated during the artifact evaluation process.
tegratedintoTensorFlow[26],whereitservesasthedefault
For the updated version of the artifacts, please refer to
high-level interface. Keras provides APIs [22] for saving
the GitHub repository available at https://github.com/necst/
andloadingmodels,enablinguserstopreservearchitecture,
security-model-sharing.
weights, and training configuration.
2. Sharing Machine Learning Models Self-contained Formats.Therecommendedpersistencefor-
mat is the .keras archive, which has been introduced
in Keras 2.11. It is a ZIP file whose core element is a
ML model sharing can be examined from multiple per-
config.json, which describes the model’s configuration
spectives, depending on how models are stored, distributed,
andarchitectureinahierarchicalJSONstructure.Thisdata-
and loaded. This work analyzes the security aspects of
based representation typically allows models to be restored
model sharing at two levels: the framework level, which
without requiring prior class or function definitions. Keras
concerns how frameworks handle model serialization and
provides a safe_mode option (introduced in v2.13) to
loading,andthehublevel,whichfocusesonthedistribution
restrict insecure deserialization during model loading [22].
practices adopted by model-sharing platforms (hubs). We
Its documentation states:
focus on the most widely adopted ML frameworks (Sec-
tion 2.1) and hubs (Section 2.2), identifying their recom- “safe_mode:Boolean,whethertodisallowunsafelambda
mended sharing formats and practices from official doc- deserialization.Whensafe_mode=False,loadinganob-
umentation. Consequently, we do not consider third-party ject has the potential to trigger arbitrary code execution.

TABLE1:Framework-levelMLmodelsharingmechanismsandsecurityconsiderations,summarizingthepersistenceformats
documented by the analyzed ML frameworks and indicating whether they are data- or code-based, self-contained (i.e.,
| sufficient | to reconstruct |     | the full | model), and their | associated | security models. |     |     |     |     |     |     |
| ---------- | -------------- | --- | -------- | ----------------- | ---------- | ---------------- | --- | --- | --- | --- | --- | --- |
Framework Setting FileFormat Self-contained Securitymodel(securityposture+commentary)
|     |     |     |     | Data-based Code-based | Weights | Model⋆ SO Comments |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------------- | ------- | ------------------ | --- | --- | --- | --- | --- | --- |
safe_mode=True JSON - BlocksuntrustedLambdadeserialization;customobjectsmustberegistered
✓
safe_mode=False
Keras[22],[25] JSON pickle p Canrestoremodelswithunrestrictedcode;arbitrarycodeexecutionispossiblebydesign
Legacy HDF5 pickle p Legacyformat;canrestoreunrestrictedcode;arbitrarycodeexecutionispossiblebydesign
Weights-only HDF5 - ✓ Modelmustbeprovidedseparately(imported,downloaded,orcopy–pasted)
protobuf+
SavedModel rawdata+ - p Encodescomputationalgraphsandweights;arbitrarycodeexecutionispossiblebydesign
| TensorFlow[26],[27],[28] |     |     |     | assets |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Checkpoint rawdata - ✓ Fortrainingcheckpoints,notforsharing;modelmustbeknownanddefined
weights_only=False - pickle p Canrestoremodelswithunrestrictedcode;arbitrarycodeexecutionispossiblebydesign
PyTorch[29],[30]
weights_only=True
- pickle ✓ Restrictedunpickler;modelmustbeprovidedseparately(imported,downloaded,orcopy–pasted)
pickle
joblib
Pickle-based - p Canrestoremodelswithunrestrictedcode;arbitrarycodeexecutionispossiblebydesign
| scikit-learn[31],[32] |     |     |     | cloudpickle |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
WithSkops JSON - ✓ Allow-listedtrustedtypes;flaggedtypesrequireuserreviewatload
WithONNX protobuf - ✓ Restrictsthesetofoperationsamodelcanusetoimplementitsinferencefunction
JSON
Model - ✓ Noexecutablecodeissaved;toresumetraining,thehyperparametersmustbeprovidedseparately
| XGBoost[33],[34] |     |     |     | UBJSON |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Model+hyperparams - pickle p Canrestoremodelswithunrestrictedcode;arbitrarycodeexecutionispossiblebydesign
⋆
TheModelcolumnismarkedwhenthesharingformatallows,inprinciple,torestorethecompletemodelwithoutmanuallyredefiningorreinstantiatingit.Evenwhen
marked,somemodelsmaystillrequiremanualcodedefinition(e.g.,whentheycontaincustomornon-standardobjects).
Legend: =Supported, =Partiallysupported(seeCommentscolumn), =Notsupported,SO=Security-Oriented,✓=Yes,p=No, Green =mechanismsthatpresent
security-orientedfeatureswhilebeingself-contained.
This argument is only applicable to the Keras v3 model SavedModel, is designed for interoperability and deploy-
format. Defaults to True.” [22] ment scenarios, particularly when working with raw Ten-
|      |                  |     |           |                |        | sorFlow | objects | or non-Python | environments |     | [27]. | Exclud- |
| ---- | ---------------- | --- | --------- | -------------- | ------ | ------- | ------- | ------------- | ------------ | --- | ----- | ------- |
| This | option addresses | a   | key risk: | Keras supports | Lambda |         |         |               |              |     |       |         |
layers, which can wrap arbitrary Python expressions as ing Keras, which has already been discussed, TensorFlow
| Layer |          |      |             |              |           | supports | two persistence |       | mechanisms: | SavedModel |     | and |
| ----- | -------- | ---- | ----------- | ------------ | --------- | -------- | --------------- | ----- | ----------- | ---------- | --- | --- |
|       | objects. | When | serialized, | these layers | may embed |          |                 |       |             |            |     |     |
|       |          |      |             |              |           | training | checkpoints     | [27], | [38].       |            |     |     |
Pythonbytecoderepresentingcustomlogic.Ifsafe_mode
is disabled, this bytecode is deserialized and will execute Self-contained formats. The SavedModel format stores
at load time. In such cases, the .keras format becomes models in a directory containing a protocol buffer encoding
|         |           |      |                 |       |               | a computation | graph, | weights | (in | the training | checkpoints |     |
| ------- | --------- | ---- | --------------- | ----- | ------------- | ------------- | ------ | ------- | --- | ------------ | ----------- | --- |
| hybrid, | combining | data | with executable | code. | Additionally, |               |        |         |     |              |             |     |
developersmayallowcustom,potentially“unsafe”typesby format), and optional files. Models can be restored without
usingaspecificdecorator[22].Inearlierversions,complete requiring the original model object definition.
modelsweresavedintheHDF5format(.h5).Althoughthis
|     |     |     |     |     |     | Non-self-contained |     | formats. | Training |     | checkpoints | store |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | -------- | -------- | --- | ----------- | ----- |
formatalsostoresarchitecture,weights,andtrainingconfig- only the model’s weight values. As stated in the official
uration in a single file, it is now advertised as “legacy”: in guide, restoring a checkpoint requires the original model to
Keras 3, loading an .h5 file raises a warning. be defined beforehand [28].
| Non-self-contained |     | formats. |     | Keras supports | weights- |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | --- | -------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
only persistence through the save_weights and 2.1.3. PyTorch. PyTorch is an open-source Deep Learning
load_weights methods [37]. In this case, the weights framework developed by the PyTorch Foundation [29]. It
|     |             |           |          |                |          | offers two | main | persistence | options | [30], | [39]: loading | the |
| --- | ----------- | --------- | -------- | -------------- | -------- | ---------- | ---- | ----------- | ------- | ----- | ------------- | --- |
| are | stored in a | .h5 file. | However, | restoring them | requires |            |      |             |         |       |               |     |
instantiating the model architecture beforehand, meaning model object configuration or loading only its state dic-
that the file alone is insufficient for full reconstruction. tionary (i.e., the parameters learned during training). This
|        |             |            |     |                   |      | behavior    | is controlled |     | via the      | weights_only |          | flag. In |
| ------ | ----------- | ---------- | --- | ----------------- | ---- | ----------- | ------------- | --- | ------------ | ------------ | -------- | -------- |
|        |             |            |     |                   |      | both cases, | serialization |     | is performed | using        | Python’s | pickle   |
| 2.1.2. | TensorFlow. | TensorFlow |     | is an open-source | Deep |             |               |     |              |              |          |          |
Learning framework developed by Google [26]. Tensor- module (code-based format).
Flow and Keras [25] complement each other: Keras serves Self-contained formats. When weights_only=False
as the high-level API for building and training models, and the model is not defined as a custom class, PyTorch
while TensorFlow provides the low-level execution engine relies on raw pickle serialization, allowing the model to be
and additional abstractions. This relationship extends to loaded without a prior class definition in the environment.
model persistence. For models built with Keras layers, the However, in this case, no security restrictions are enforced
recommended format is the .keras archive (see Sec- to prevent arbitrary code execution, as raw pickle is known
tion 2.1.1) [38]. By contrast, TensorFlow’s native format, to be insecure [40].

Non-self-contained formats. weights_only=True re- and loading models in either JSON or UBJSON (Universal
quires the instantiation of a model on which to load Binary JSON) formats [44].
the weights. Additionally, if the model is defined us-
Self-contained formats.UnlikeDeepLearningframeworks,
ing a custom class, even when weights_only=False,
XGBoost implements gradient boosting, which has a closed
its definition must still be available at load time,
structure. As a result, importing the standard file format is
although instantiation is handled internally. Interest-
sufficient to treat it as self-contained. However, in scenarios
ingly, when weights_only=True, PyTorch uses pickle
suchasdistributedorcollaborativelearning,wheretraining-
with a restricted unpickler that limits deserialization to
critical hyperparameters are not included in the JSON file
torch.Tensor objects and primitive types, and prevents
(e.g., the max_depth parameter), the framework’s authors
dynamic imports during loading.
recommendusingthebuilt-inpickleformattofullyserialize
the Booster object [34]. Alternatively, the hyperparame-
2.1.4. scikit-learn. scikit-learn is an open-source Python
ters must be set and provided separately.
library for traditional ML [31]. The official documen-
tation [32] describes several persistence approaches: (i)
Python’s pickle, joblib, cloudpickle modules, (ii) the Skops 2.2. Hub-level Sharing
library [41], and (iii) conversion to the framework-agnostic
ONNX format [42]. All of these are self-contained ap- An additional layer of the ecosystem is represented by
proaches, and we describe each of them in the following. model-sharing hubs. These provide infrastructures where
Pickle/Joblib/Cloudpickle. The traditional scikit-learn userscanpublishanddownloadpre-trainedmodels,acceler-
model persistence approach uses pickle, joblib, or ating research and application development. Moreover, they
cloudpickle. These formats serialize estimators in a code- may also incorporate further safeguards—such as content
based manner: unrestricted deserialization executes Python scanning, model verification, or curation policies—to pro-
bytecode, posing risks of arbitrary code execution [32]. tect users against threats beyond those arising from local
framework-level loading. As with the frameworks, for our
Skops. Hugging Face introduced Skops in 2022 [41], with
analysis we selected these widely used hubs: Hugging Face
native support for publishing models on their hub [1]. Ac-
Hub [1], Kaggle Models [2], TensorFlow Hub [4], Keras
cording to the official documentation [43], Skops provides
Hub [3], and PyTorch Hub [5]. This choice is supported
skops.io.dump() and skops.io.load() as secure
by usage statistics: the 2022 Kaggle ML & DS Survey [35]
alternatives, designed to prevent arbitrary code execution
rankstheseamongthemostpopularMLmodelrepositories.
and to reject unknown or malicious objects by default. The
Table 2 summarizes their characteristics along with their
.skops archive is a ZIP file that includes, among other
security implications (discussed in Section 3).
elements, a JSON schema (schema.json) describing the
estimator’s structure in a tree-like format, with nodes such
as MethodNode, TypeNode, or FunctionNode. This 2.2.1. HuggingFaceHub.HuggingFaceHub[1]isoneof
design makes the .skops a data-based format, similar in themostpopularopenhubsforsharingMLmodels.Ithosts
spirit to Keras’s .keras archive. The intended workflow over 2.1 million models in a Git-based repository format,
involves calling get_untrusted_types() to inspect supporting a variety of file types. The platform implements
themodelandidentifyobjectsthatarenottrustedbydefault. multiple security measures [45]: every uploaded file is au-
Usersmustthenmanuallyreviewtheseobjectsandexplicitly tomatically scanned for malware using ClamAV [46], and
allowlist them when calling load(); otherwise, loading any pickle-based model file is “pickle-scanned” to enumer-
fails. Therefore, security in Skops depends not only on its ate suspicious included modules. The Hub also performs
data-based design, but also on users’ reviewing capabilities. secret scanning to detect accidentally leaked credentials.
Furthermore,HuggingFaceintegratestwothird-partymodel
ONNX. scikit-learn models can be exported to the Open
scanning services: Protect AI [47] and JFrog [48].
Neural Network Exchange (ONNX) [42] format using the
skl2onnx converter [32]. ONNX defines a framework-
agnostic format based on protocol buffers and provides 2.2.2. Kaggle Models. The Kaggle repository [2] supports
a purely data-based representation, making models self- bothpublicandprivatemodeluploads,oftencomplemented
contained and portable across languages and environments. by configuration files or metrics, and is tightly integrated
Unlike other self-contained approaches, the original estima- withKaggleNotebooks.Manymodels,includingthosefrom
tor object (with its class structure and custom code) is not TensorFlow Hub [4] (which fully migrated to Kaggle Mod-
preserved. Instead, the model is reduced to a computational elsin2023),canbeloadedthroughhigh-levelAPIs.Security
graphanditsparameters,wherethegraphcanonlycontaina relies primarily on the isolation of Kaggle’s cloud notebook
limitedsetofpredefinedMLoperators.ONNXserialization environment and the use of standard model formats, as the
depends on the coverage of the chosen conversion tool, and platform does not publicly document malware or pickle
many scikit-learn estimators remain unsupported. scanning for user-contributed models.
2.1.5. XGBoost. XGBoost [33] is a widely used gradient 2.2.3. PyTorch Hub. PyTorch Hub [5] is a built-in model-
boosting framework. It provides dedicated APIs for saving sharing mechanism for PyTorch that enables users to

TABLE 2: Hub-level ML model sharing mechanisms and security considerations, summarizing the characteristics of the
analyzed model-sharing hubs and indicating their hosting model, reference format (i.e., the specific model format the hub
relies on, if any), and their associated security models.
Characteristics Securitymodel(securityposture+commentary)
Hub
Centralizedhosting Referenceformat SO Comments
HuggingFaceHub[1] - ✓ Malware,pickle,andsecretscanning;integratesthird-partymodelscanners
KaggleModels[2] - p Noexplicitsecuritymeasuresdocumented;reliesonnotebookisolationandstandardformats
PyTorchHub[5] - p Noexplicitsecuritymeasuresdocumented;arbitraryPythonexecutionfromrepositories
TensorFlowHub[4] SavedModel p Noexplicitsecuritymeasuresdocumented
KerasHub[3] .keras p Noexplicitsecuritymeasuresdocumented
Legend:SO=Security-Oriented, =Supported, =Notsupported,✓=Yes,p=No. Green =mechanismsthatpresentsecurity-orientedfeatures.
load models from GitHub repositories with a single com- 3.1. Threat Model
mand [5]. Unlike centralized platforms, it is entirely de-
centralized: models are hosted on GitHub, and PyTorch We consider the threat posed by malicious ML model
Hub collects only an entry-point script (hubconf.py) for artifacts that target users loading models through popular
fetching and instantiating them. The PyTorch team main- ML frameworks. Our threat model defines the attacker’s
tains a list of models on the official PyTorch Hub page target, objectives, and capabilities. Finally, we discuss the
(via a pull-request submission process) [49], but using the relevance of our threat model in the real world.
torch.hub APIs, it is possible to load models from Attacker’s Target. Our analysis focuses on the ML model-
any public repository by URL. This flexibility means that loading pipeline executed locally on a user’s machine. The
torch.hub.load()downloadsthetargetrepositoryand system the attacker targets consists of: (i) the user environ-
executes its model-loading code. PyTorch Hub performs no ment, including the operating system with an installed ML
automated security scanning or integrity checks. framework(e.g.,PyTorch[29],TensorFlow[26],Keras[25],
scikit-learn [32]); (ii) the model artifact, a serialized pre-
2.2.4. TensorFlowHub.TensorFlowHub[4]wasoriginally trainedfilesuchas.pth,.keras,.h5,or.pkl;and(iii)
released alone as a central repository for reusable Tensor- the loading mechanism, i.e., framework-provided functions
Flow modules. It provides a library and hosting platform suchastorch.load()[30].Wefocusonscenarioswhere
where models can be published and imported via simple
a user loads a model obtained from an external source.
APIs, such as hub.KerasLayer. Unlike decentralized
Attacker’s Goal. We consider an attacker who crafts a
solutions, TensorFlow Hub offers a collection of models
malicious model artifact to compromise the victim’s system
maintained either by Google or by community contributors.
upon loading. The primary goal is to achieve arbitrary code
Since 2023, TensorFlow Hub has been fully integrated into
execution. Such attacks typically exploit vulnerabilities in
Kaggle Models [2], and while the API remains available,
the deserialization process, targeting the host system itself
modelsareuploadeddirectlytoKaggle.Bydefault,itadopts
rather than the functionality of the model.
theSavedModelformatwithoutadditionalrestrictionsand
makes no public mention of automated scanning. Attacker’s Capabilities. The attacker can create, modify,
and distribute ML model artifacts but has no prior access
2.2.5. Keras Hub. Keras Hub [3], introduced with Keras to the target’s system and cannot influence the victim’s
3, provides a collection of ready-to-use pretrained Keras environment, configuration settings, or model-loading flags.
models. Unlike TensorFlow Hub, which hosts TensorFlow- We consider two main distribution channels: (1) public
specific modules, Keras Hub focuses exclusively on models repository poisoning, where a malicious model is uploaded
designedtointegrateseamlesslywiththeKerasAPI.Models to a trusted platform (e.g., Hugging Face Hub [1], Kaggle,
can be loaded directly via .from_preset() and are GitHub) under the mask of a legitimate resource; and (2)
distributed in the standardized format .keras. No content direct delivery, where the artifact is sent to the victim via
scanning is explicitly documented. private channels such as email or cloud storage.
Real-World Relevance. Our threat model is grounded in
3. Model Sharing Security Implications (RQ1) recent large-scale measurements showing that malicious
model artifacts exist in practice (e.g., 91 malicious models
This section analyzes the security implications of the and several poisoned dataset scripts discovered by monitor-
sharing approaches adopted by frameworks and sharing ing Hugging Face over a three-month period) [10], [16].
hubs described in Section 2, aiming to clarify the current While these studies focus only on known vulnerabilities in
state of security in ML model sharing and highlight critical model deserialization (e.g., Python’s pickle unsafe deseri-
issues requiring further investigation. Before the analysis, alization [40]), they demonstrate the real-world relevance
we formally define the threat model underlying our study. of our threat model. Furthermore, according to a recent

Hugging Face report, Protect AI [47] has scanned over predefinedoperators,optionallyextendablethroughexternal
4.47 million unique model versions across 1.41 million libraries—makes arbitrary code execution unlikely. Never-
repositories,identifying352,000unsafeorsuspiciousissues theless, while ONNX is well-suited for inference (scikit-
in 51,700 models as of April 2025 [50]. learn recommends ONNX only for that purpose [32]), it is
far less flexible for training.
3.2. Security Analysis Non-self-contained formats such as PyTorch’s
weights_only serialization, Keras’s weights-only
The frameworks described in Section 2 adopt or recom- API, and TensorFlow’s training checkpoints can also be
menddifferentstrategiesformodelsharing.Ontopofthese considered relatively security-oriented. Note that PyTorch
mechanisms, model hubs provide their own approaches explicitly recommends the weights_only mode in its
for distributing pre-trained models. Here, we systematically documentation, claiming the presence of security measures
analyze whether and how frameworks and hubs address that are not enforced when this mode is disabled. These
the risks defined in the threat model, starting from the approaches store only numerical parameters, making them
official documentation they provide. In particular, we clas- inherently security-oriented. However, they merely shift the
sify framework-level and hub-level mechanisms as security- trust problem: model architecture code must be provided
oriented (directly claiming or implicitly providing security separately, and if obtained from unverified sources, it
properties)ornon-security-oriented.Tables1and2summa- reintroduces the same arbitrary code execution risks.
rize the classification and corresponding security models.
Non-Security-Oriented Formats. Other frameworks rely on
inherentlyinsecureformats.Kerassafe_mode=Falseor
SA.F - Framework-level Security Analysis.
legacy HDF5, PyTorch weights_only=False, scikit-
Security-Oriented Formats. Keras and scikit-learn provide learn (pickle-based), and XGBoost (model + hyperparam-
formats embedding the entire model object (self-contained eters) all persist models using unrestricted pickles. Tensor-
approach) that are explicitly presented as security-oriented Flow’s SavedModel format [27], despite being based on
in their documentation: safe_mode=True for Keras [22] computation graphs, is explicitly described by TensorFlow
and Skops for scikit-learn [32]. Keras’s safe_mode flag developers as insecure when loading untrusted models [51].
disables “unsafe lambda deserialization” [22], thereby pre-
venting execution of pickle-encoded payloads. Skops en- SA.H - Hub-level Security Analysis.
forces a trusted type validation step [43], requiring users
Security-Oriented Hubs. Among the analyzed hubs, Hug-
to manually review and approve potentially insecure ob-
ging Face Hub [1] stands out as the only platform with
jects before loading (via get_untrusted_types()).
active and documented security measures. These include
The developers describe this mechanism as “secure persis-
malware scanning, pickle scanning, and secret scanning,
tence” [43], but also explicitly caution that the library is
complemented by integrations with external services such
still under active development and may contain unresolved
as Protect AI [47] and JFrog [48]. When a model artifact is
security issues. Both Keras and Skops base their security
uploaded, it is subjected to these scans, and if no issues are
models on avoiding pickle in favor of declarative, JSON-
detected, the platform marks the model with a “Safe” label.
based formats. However, our analysis in Section 4 shows
Overall,thisapproachreflectsHuggingFace’srecognitionof
that this assumption does not always hold. In particular,
modelsasexecutablecodeanditscommitmenttoenforcing
although JSON itself is a data-based format, the way Keras
security practices consistent with that perspective.
and Skops process their JSON-based files effectively makes
them behave like code-based formats—creating critical is- Non-Security-Oriented Hubs. TensorFlow Hub [4] and
sues discussed later in the paper. Keras Hub [3] do not perform systematic artifact scanning;
XGBoost uses a JSON/UBJSON-based format [34] that instead, they offload security to the framework level by
saves no executable code. To resume training, hyperparam- relying on controlled formats (.keras, SavedModel).
eters must be retrieved and set separately, while the archi- Kaggle benefits from community curation and the isola-
tecture code is standardized and provided by the XGBoost tion of its notebook environment, though unverified models
library itself. Security is implicitly provided by the fixed can still be uploaded. PyTorch Hub provides no hub-level
architectureoftheXGBoostmodel.Notably,thedevelopers protections at all: it executes arbitrary Python code from
do not advertise this design as security-oriented. Further- repositories, leaving responsibility entirely to the user.
more, the documentation explicitly recommends raw pickle
serialization in distributed or collaborative scenarios (where 4. When secure is not secure (RQ2)
preserving hyperparameters is needed to resume training),
reintroducing well-known risks of arbitrary code execution. While existing evidence, both from prior scientific stud-
ONNX [42] does not explicitly make security claims in ies [10], [16] and from independent checks by model
its documentation. However, scikit-learn refers to ONNX hubs [50], has brought attention to the relevance and scale
as the “most secure solution” for model persistence [32]. of attacks targeting ML model loading mechanisms, these
This characterization derives from ONNX’s operator-based effortshavelargelyfocusedonwell-knownattackvectors.In
design (see Section 2.1), which inherently limits the at- particular,theyhaveexaminedinherentlyinsecuremethods,
tack surface. Its restricted expressiveness—a limited set of such as pickle deserialization, but have not questioned the

effectiveness of mechanisms that are claimed to be secure. isinstantiatedatloadtime,thecommandisexecutedduring
In this section, we go a step further: building on the obser- loading. A simplified config.json snippet is provided
vations from our security analysis in Section 3, we evaluate in the appendices (Listing 1), while the complete PoC is
how closely the security narrative promoted by popular ML availableonZenodo.Crucially,thisfindingdemonstratesthe
frameworks and hubs, claiming to secure the entire model- existence of entirely different exploitation paths in Keras’s
sharing process, matches reality. loading mechanism, beyond the abuse of Lambda layers.
As discussed, some approaches are deliberately non-
Disclosure. After coordinated disclosure, the vulnerability
security-oriented,relyingoninsecureformatsordistribution
was assigned the identifier CVE-2025-1550 (CVSS 7.3,
methods. Others offer limited security but at the expense
CNA: Google LLC) [23]. To the best of our knowledge,
of flexibility or by shifting responsibility to users or other
this is the first CVE assigned to Keras’s model loading
workflow components (e.g., requiring the model architec- mechanism after the introduction of safe_mode, and thus
ture to be separately obtained). A smaller subset explicitly
the first to demonstrate a weakness in this security feature.
presents itself as security-oriented, seeking to make model
The issue was mitigated in Keras version 3.9 through the
sharing more secure overall. This section focuses on hubs
introduction of stricter validation, which restricts imports
that provide scanning mechanisms and on frameworks that
to a limited set of trusted modules, primarily within Keras
claim security combined with complete model object shar-
itself (allowlist approach).
ing. In particular, from a framework-level perspective, we
assessthesolutionshighlightedinTable1:thesafe_mode
KV.2-CodeReuseviaLambdaLayers.Lambdalayersin
in Keras and the “secure persistence” [43] of Skops for
KerascanbeusednotonlytoserializePythonbytecodebut
scikit-learn. From a hub-level perspective, we analyze the
also to reference functions from specified Python modules.
only hub that provides embedded scanning mechanisms, as
We found that an attacker can achieve arbitrary code exe-
highlighted in Table 2: the Hugging Face Hub.
cution through code reuse by leveraging Lambda layers to
Notably, our analysis uncovered six 0-day vulnerabili-
abuse legitimate functions from Keras’s internal modules,
ties (all assigned to CVEs) across Keras and Skops, each
effectively bypassing the restriction introduced after KV.1
allowing arbitrary code execution during model loading.
disclosure. As a PoC, we crafted a model that disables
Interestingly, both frameworks base their security claims on
safe_modeduringloading,evenifitwasinitiallyenabled
data-basedformatpersistence,whichourfindingsshowdoes
by the user, by invoking an internal Keras utility. Then, by
not hold in practice. Moreover, our hub-level experiments
relying on other internals, such as the function used to load
demonstrated that it is feasible for an attacker to distribute
the model (now with safe_mode disabled), we show how
exploits leveraging those vulnerabilities without being de-
to achieve full code execution. Our PoC represents just one
tected by the scanning tools integrated into Hugging Face.
possibleexecutionpath;differentexploitscanbebuiltusing
VulnerabilityResearchMethodology.Allvulnerabilitiesde- other internal functions (execution gadgets). A demonstra-
scribedbelowwerediscoveredthroughmanualreverseengi- tive snippet is provided in the appendices (Listing 2), while
neeringofthelatestKerasandSkopsopen-sourcecodebases the complete PoC is available on Zenodo.
from GitHub, focusing on security-related functionalities.
Disclosure.Wedisclosedthevulnerabilitythroughacoordi-
Pre-existing CVEs. We reviewed publicly available CVEs nated disclosure process. Two distinct CVEs were assigned
for Keras and Skops. Prior to our work, no CVEs had been to this vulnerability. The first (CVE-2025-8747, CVSS
assigned to the .keras format or safe_mode, and only 8.6,CNA:GoogleLLC[24])referstothethreatofarbitrary
onetoSkops.AdetailedanalysisisprovidedinAppendixA. file download through specific gadget reuse, which we used
as an optional step in our complete PoC, with our report
4.1. Keras considered a contemporary independent report of that by
JFrog researcher Andrey Polkovnichenko [52]. The second
KV.1 - Abusing Insecure Module Resolution. We dis- (CVE-2025-9906, CVSS 8.6, CNA: Google LLC [53]),
covered that due to insufficient validation in the Keras instead, concerns code reuse to disable safe_mode,
model loading process, a carefully crafted config.json thereby covering the broader and more severe threat of
file inside a .keras model archive can specify in- arbitrary code execution. The fix extends the validation
secure Python modules and functions to be imported checks introduced after KV.1 by enforcing that any object
and executed during loading. In particular, an attacker accessed from an imported module must be an instance
can build a config.json such that, for example, of KerasSaveable. Additionally, several internal Keras
subprocess.runisinterpretedasamodellayer.Keras’s utilitiesthatcouldbeabusedwereblocklisted,includingthe
loading logic performs minimal validation: if the specified ones we used in our PoC.
class name resolves to a Python FunctionType—which
subprocess.run does—no further checks are per- KV.3 - Silent Bypass via Legacy HDF5 Format. As
formed. Arguments can then be passed abusing the noted in Section 2.1.1, Keras continues to support loading
input–output relations within Keras’s internal computa- legacy models in the HDF5 format. Because of their legacy
tion graph, enabling execution of commands such as nature, some security checks introduced for the .keras
subprocess.run("/bin/sh").Sincethemodellayer format do not apply to HDF5 models. Specifically, there

is no mechanism to restrict the content of Lambda lay- funcfielddetermineswhichattributeisaccessed,allowing
ers[22].However,weobservedthatwhenanHDF5modelis malicious attribute traversals to go unnoticed.
loaded using load_model(..., safe_mode=True), During our analysis, we achieved arbitrary code ex-
thesafe_modeflagissilentlyignored—withoutanywarn- ecution using an apparently benign type returned by
ingorerror,eventhoughsuchfeedbackwouldbereasonably get_untrusted_types(), such as builtins.int.
| expected | given | the impossibility |     | of  | enforcing | this | mode. |              |      |                |     |       |         |         |        |
| -------- | ----- | ----------------- | --- | --- | --------- | ---- | ----- | ------------ | ---- | -------------- | --- | ----- | ------- | ------- | ------ |
|          |       |                   |     |     |           |      |       | The specific | type | is irrelevant, |     | as it | is only | checked | during |
Technically, the argument is never forwarded to the internal validation and never used by the Skops loading logic; in
legacy loading routine and therefore has no effect. In this practice, any string can be substituted without affecting the
case, no sophisticated techniques are required for an attack, outcome.Arepresentativeschema.jsonsnippetfromthe
asthelegacyformatpermitsdeserializationofarbitrarycode .skops file of our PoC is provided in the appendices
through unrestricted Lambda layers. An attacker can then (Listing 3), and the full PoC is available on Zenodo.
| exploit     | this misleading |              | behavior, | leveraging |      | the  | fact that  |             |          |                 |     |               |         |          |          |
| ----------- | --------------- | ------------ | --------- | ---------- | ---- | ---- | ---------- | ----------- | -------- | --------------- | --- | ------------- | ------- | -------- | -------- |
|             |                 |              |           |            |      |      |            | Disclosure. | We       | disclosed       | the | vulnerability |         | to the   | Skops    |
| users may   | blindly         | trust        | the       | presence   | of a | flag | labeled as |             |          |                 |     |               |         |          |          |
|             |                 |              |           |            |      |      |            | team via    | GitHub’s | private         |     | advisory      | and     | actively | col-     |
| “safe.” The | PoC             | is available |           | on Zenodo. |      |      |            |             |          |                 |     |               |         |          |          |
|             |                 |              |           |            |      |      |            | laborated   | with     | the maintainers |     | to            | develop | and      | validate |
Disclosure.Asinthepreviouscases,wedisclosedtheissue a mitigation. The fix was included in Skops version
to the Google Open Source Security Team, which serves 0.12.0. The patch enforces that the __module__ and
as a coordination channel for Google-affiliated open-source __class__ entries match those of the actual object
projects.However,thistimeourissuewasmarkedas“Won’t passed to the MethodNode. In addition, it extends the un-
Fix (Infeasible).” After a constructive discussion, Google trusted types reported to the user by including any attribute
Securityclarifiedthatthey“won’ttreatKerassafe_mode accessed via MethodNode—that is, the concatenation
as a security boundary” anymore and that they “just don’t __module__.__class__.func—therebyenablinghu-
think safe_mode is reliable enough to be a security manvalidationofthefuncentryaswell.Thevulnerability
boundary”, further explaining that “the panel changed its hasbeenassignedtheidentifierCVE-2025-54413(CVSS
view on this issue in [KV.2 issue]” and stating: “Don’t 8.7, CNA: GitHub, Inc.) [56].
| rely on | safe_mode |     | (maybe | a poor | name) | for | that level |     |     |     |     |     |     |     |     |
| ------- | --------- | --- | ------ | ------ | ----- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
of protection.” Moreover, they also clarified that “we don’t SV.2 - Bypassing Validation via OperatorFuncNode.
speakfortheKerasteam—theymightseeitdifferently.Ifyou
|     |     |     |     |     |     |     |     | The OperatorFuncNode |     |     | allows |     | invoking | methods | from |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------ | --- | -------- | ------- | ---- |
wanttoseecodechangesinKerasforpatchingtheseissues, Python’s operator module. However, similar to SV.1,
GitHub’s the place to make it happen” [54]. Following this we observed a mismatch between what is validated by
upstreamreferral,wethencontactedtheKerasteamthrough get_untrusted_types() and load() and what is
| GitHub’s | private | advisory. | Keras | acknowledged |     | the | concern |            |      |          |        |       |          |     |          |
| -------- | ------- | --------- | ----- | ------------ | --- | --- | ------- | ---------- | ---- | -------- | ------ | ----- | -------- | --- | -------- |
|          |         |           |       |              |     |     |         | internally | used | by Skops | during | model | loading, |     | enabling |
and fixed the issue in Keras version 3.11.3. The fix extends unnoticed access to operator methods. Specifically, while
safe_mode to the legacy file format as well: the flag is the concatenation of the __module__ and __class__
now forwarded to legacy loading, ensuring that Lambda fields is validated, the __module__ value is ignored and
layers are constrained in the same way, including the ad- __class__ __class__
|          |              |            |     |           |     |               |     | only      |            | is    | used.    | In practice, | if           |     |          |
| -------- | ------------ | ---------- | --- | --------- | --- | ------------- | --- | --------- | ---------- | ----- | -------- | ------------ | ------------ | --- | -------- |
| ditional | restrictions | introduced |     | for KV.2. | The | vulnerability |     |           |            |       |          |              |              |     |          |
|          |              |            |     |           |     |               |     | is set to | the string | “some | method”, |              | the function |     | actually |
has been assigned the identifier CVE-2025-9905 (CVSS invoked is operator.some_method, regardless of the
7.3, CNA: Google LLC) [55]. value of __module__ .This allows an attacker to supply
|     |     |     |     |     |     |     |     | a misleading, | seemingly |     | benign | module | path | that | passes |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | ------ | ------ | ---- | ---- | ------ |
4.2. Skops validation,whiletheexecutedfunctionisactuallytakenfrom
|        |         |             |     |     |         |        |     | the operator     |         | module. | This | ultimately          | enables | code       | exe-  |
| ------ | ------- | ----------- | --- | --- | ------- | ------ | --- | ---------------- | ------- | ------- | ---- | ------------------- | ------- | ---------- | ----- |
|        |         |             |     |     |         |        |     | cution through   | methods |         | such | as operator.call,   |         |            | which |
| SV.1 - | Abusing | MethodNode. |     | In  | a Skops | model, | the |                  |         |         |      |                     |         |            |       |
|        |         |             |     |     |         |        |     | invoke arbitrary |         | targets | with | attacker-controlled |         | arguments. |       |
MethodNode
|     |     | allows access |     | to Python | object | attributes | us- |     |     |     |     |     |     |     |     |
| --- | --- | ------------- | --- | --------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Aschema.jsonfragmentshowingtheattackcoreispro-
| ing dot notation. |           | However,   | shortcomings |     | in         | its design | allow  |          |                |      |           |              |           |            |        |
| ----------------- | --------- | ---------- | ------------ | --- | ---------- | ---------- | ------ | -------- | -------------- | ---- | --------- | ------------ | --------- | ---------- | ------ |
|                   |           |            |              |     |            |            |        | vided in | the appendices |      | (Listing  | 4),          | while the | PoC        | demon- |
| for traversal     | of        | the object | graph        | of  | legitimate | objects    | and    |          |                |      |           |              |           |            |        |
|                   |           |            |              |     |            |            |        | strating | arbitrary      | code | execution | is available |           | on Zenodo. |        |
| access to         | sensitive | Python     | internals.   |     | These      | can then   | repre- |          |                |      |           |              |           |            |        |
Disclosure.WedisclosedthevulnerabilitytotheSkopsteam
| sent powerful |        | primitives, | ultimately |     | enabling | arbitrary | code       |              |         |          |     |        |                  |     |      |
| ------------- | ------ | ----------- | ---------- | --- | -------- | --------- | ---------- | ------------ | ------- | -------- | --- | ------ | ---------------- | --- | ---- |
|               |        |             |            |     |          |           |            | via GitHub’s | private | advisory |     | system | and collaborated |     | with |
| execution     | during | model       | loading.   | For | example, | a         | legitimate |              |         |          |     |        |                  |     |      |
object may be instantiated using an ObjectNode, which the maintainers for remediation. The issue was resolved in
enforces type validation and permits only trusted or explic- Skops version 0.12.0 by enforcing the __module__ field
itly allowed types. Once the object is in memory, however, of an OperatorFuncNode to be set to ”operator”. The
|             |     |                |     |            |     |         |         | identifier | CVE-2025-54412 |     |     | (CVSS | 8.7, | CNA: | GitHub, |
| ----------- | --- | -------------- | --- | ---------- | --- | ------- | ------- | ---------- | -------------- | --- | --- | ----- | ---- | ---- | ------- |
| an attacker | can | chain multiple |     | MethodNode |     | entries | to tra- |            |                |     |     |       |      |      |         |
versetheobjectgraphandaccessruntimestructuressuchas Inc.) has been assigned [57].
| __builtins__, |     | which | exposes | dangerous |     | functions | like |     |     |     |     |     |     |     |     |
| ------------- | --- | ----- | ------- | --------- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
eval and exec. Furthermore, while the __class__ and SV.3 - Silent Fallback to joblib in Model Card. As
__module__fieldsofaMethodNodearevalidatedwhen previously noted in Section 2.1.4, Skops is developed with
get_untrusted_types() and load() are called, the integration into the Hugging Face ecosystem in mind. To

TABLE3:DetectionresultsofHuggingFacescanningtools As a baseline, we also uploaded a set of additional Keras
for our PoCs and baselines, as presented in the interface. models: one containing a benign Lambda layer (doing
|              |            |     |         |           |         |     |            | nothing), | one containing |          | a malicious |        | Lambda  | layer | calling |
| ------------ | ---------- | --- | ------- | --------- | ------- | --- | ---------- | --------- | -------------- | -------- | ----------- | ------ | ------- | ----- | ------- |
| Test(format) | Picklescan |     | ClamAV  | ProtectAI | JFrog   |     | Finallabel |           |                |          |             |        |         |       |         |
|              |            |     |         |           |         |     |            | /bin/sh,  | and            | one with | no          | Lambda | layers. | For   | each of |
| KV.1(.keras) | notapickle |     | Noissue | Unsafe    | NoIssue |     | Unsafe     |           |                |          |             |        |         |       |         |
KV.2(.keras) notapickle Noissue Suspicious (**) (**) these, we uploaded both the HDF5 and .keras versions1.
KV.3(HDF5) Our experiments were performed several weeks after the
| (sameasM-L) | notapickle |     | Noissue | (*) | Unsafe |     | Unsafe |     |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | ------- | --- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
SV.1(.skops) notapickle Noissue Noissue notamodel Safe CVEs were publicly disclosed, assessing the capability of
| SV.2(.skops) | notapickle |     | Noissue | Noissue    | notamodel |     | Safe   |          |           |        |           |            |                   |               |      |
| ------------ | ---------- | --- | ------- | ---------- | --------- | --- | ------ | -------- | --------- | ------ | --------- | ---------- | ----------------- | ------------- | ---- |
|              |            |     |         |            |           |     |        | scanners | to detect | public | threats   | replicable |                   | by attackers. |      |
| SV.3(pickle) | notapickle |     | Noissue | Unsafe     | Unsafe    |     | Unsafe |          |           |        |           |            |                   |               |      |
|              |            |     |         |            |           |     |        | We made  | all       | loaded | artifacts | (or        | the corresponding |               | gen- |
| B-L(HDF5)    | notapickle |     | Noissue | Suspicious | Unsafe    |     | Unsafe |          |           |        |           |            |                   |               |      |
B-L(.keras) notapickle Noissue Suspicious Unsafe Unsafe erationscripts)publiclyavailable.Beforeuploadinganyma-
| M-L(.keras) | notapickle |     | Noissue | Noissue | Unsafe |     | Unsafe |     |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | ------- | ------- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
NL(HDF5) notapickle Noissue Noissue Noissue Safe licious models, we requested and obtained explicit permis-
NL(.keras) notapickle Noissue Noissue Noissue Safe sion from Hugging Face. The results are shown in Table 3.
(*)Thescanningtooldidnotreturnanyresults(i.e.,anemptylabel).
(**)Thescanningtoolremainedstuckinthe“Queued”status.Nofinallabelwas
|     |     |     |     |     |     |     |     | MS - Effectiveness |     | of  | Hub-Integrated |     | Model | Scanners. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | -------------- | --- | ----- | --------- | --- |
thereforecomputed.Re-uploadingthemodelproducedthesameresult.
Legend:B=Benign,M=Malicious,L=Lambda,NL=NoLambda. Picklescan. As evident from Table 3, this scanner does
|     |     |     |     |     |     |     |     | not detect | any of | our | PoCs, | classifying | every | file | as ”not a |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | ----- | ----------- | ----- | ---- | --------- |
support this, Skops provides an API for generating model pickle,” including the malicious pickle of KV.3. The reason
cards, which serve as structured documentation for mod- lies in the extension chosen for the PoC (.skops). To
els and include fields such as description, authors, dia- confirm it, we uploaded the same pickle file under different
|             |       |       | Card      |             |                      |        |            | names. Files | with         | extensions |                | such as | .h5,    | .onnx, | .pkl,  |
| ----------- | ----- | ----- | --------- | ----------- | -------------------- | ------ | ---------- | ------------ | ------------ | ---------- | -------------- | ------- | ------- | ------ | ------ |
| grams, etc. | [58]. | When  | a         | object      | is created—typically |        |            |              |              |            |                |         |         |        |        |
|             |       |       |           |             |                      |        |            | and .pt      | were flagged |            | as (malicious) |         | pickle, | while  | .json, |
| specifying  | the   | model | file and, | optionally, |                      | a list | of trusted |              |              |            |                |         |         |        |        |
types—Skops internally invokes Card.get_model() to .skops, or .keras were flagged as ”not a pickle”.
| load the | associated | model. | If  | the provided |     | model | file is in |     |     |     |     |     |     |     |     |
| -------- | ---------- | ------ | --- | ------------ | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
ClamAV.Allmodelscansreported“Noissue.”Thisresultis
the.skopsformat(i.e.,aZIParchive),thestandardSkops
|     |     |     |     |     |     |     |     | expected, | as ClamAV |     | is a general-purpose |     |     | malware | scanner |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | -------------------- | --- | --- | ------- | ------- |
load() function is used, applying all the security checks and is not designed to detect ML framework-level threats.
alreadydiscussed.However,iftheprovidedfileisnotavalid
Protect AI.ProtectAI’sGuardian[60]scannerdefinesaset
| ZIP archive, | the | fallback | mechanism |     | silently | switches | to  |     |     |     |     |     |     |     |     |
| ------------ | --- | -------- | --------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofmodel-sharingthreats[61].Whenamodelisuploadedto
| using joblib.load() |     |     | to  | deserialize | the | model, | without |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | ----------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
HuggingFace,thescannerchecksthefilesagainstthesedef-
| warning | the user. | Nevertheless, |     | joblib | does | not | provide |     |     |     |     |     |     |     |     |
| ------- | --------- | ------------- | --- | ------ | ---- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
initionsandgeneratesareportthatalertsusersifanythreats
| the same  | protections      |     | as Skops         | and    | allows     | arbitrary    | code       |               |           |           |           |         |          |              |     |
| --------- | ---------------- | --- | ---------------- | ------ | ---------- | ------------ | ---------- | ------------- | --------- | --------- | --------- | ------- | -------- | ------------ | --- |
|           |                  |     |                  |        |            |              |            | are detected. | In        | our test, | this      | scanner | returned | matches      | for |
| execution | via pickle-based |     | deserialization. |        |            | Importantly, | this       |               |           |           |           |         |          |              |     |
|           |                  |     |                  |        |            |              |            | KV.1, KV.2,   | and       | two       | baseline  | models. |          |              |     |
| behavior  | is based         | on  | the file’s       | actual | format—not |              | its exten- |               |           |           |           |         |          |              |     |
|           |                  |     |                  |        |            |              |            | For           | KV.1, the | PoC       | triggered | the     | threat   | “PAIT-KERAS- |     |
sion—making it especially difficult for users to detect. An 301: Keras Model Custom Layer Detected at Model Run
| example | PoC is | available | on  | Zenodo. |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ------ | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Time,”whichexplicitlycoverscaseswherenon-Keraslayers
Disclosure. We disclosed the vulnerability to the Skops areincludedwithinaKerasmodel.Thiscorrespondsexactly
team via GitHub’s advisory system and proposed a fix to the basic PoC we uploaded, confirming the tool’s ability
to the maintainers, which was accepted and included to identify such cases. This result was somewhat expected,
in Skops version 0.13.0. The fix disallows the use of as following the publication of the CVE associated with
joblib unless explicitly authorized by the user through KV.1, Hugging Face announced new Protect AI threat def-
the new allow_pickle argument during Card cre- initions, explicitly citing our CVE as an example of the
ation. The vulnerability has been assigned the identifier type of threat detectable through those updates [50]. KV.2
| CVE-2025-54886 |     |     | (CVSS | 8.4, CNA: | GitHub, |     | Inc.) [59]. |             |         |     |              |     |       |            |        |
| -------------- | --- | --- | ----- | --------- | ------- | --- | ----------- | ----------- | ------- | --- | ------------ | --- | ----- | ---------- | ------ |
|                |     |     |       |           |         |     |             | was instead | flagged | as  | “suspicious” |     | under | the threat | “PAIT- |
KERAS-100:KerasModelLambdaLayerCanExecuteCode
4.3. Hugging Face At Load Time.” However, as demonstrated by our baseline
|     |     |     |     |     |     |     |     | models, | this threat | definition |     | is generic |     | and triggered | by  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ---------- | --- | ---------- | --- | ------------- | --- |
Lambda
Following the threat model described in Section 3.1, we the presence of layers, rather than their internal
|                |     |             |     |            |          |     |             | operations.   | As a    | result, | benign   | Lambda     | layers | also | trigger  |
| -------------- | --- | ----------- | --- | ---------- | -------- | --- | ----------- | ------------- | ------- | ------- | -------- | ---------- | ------ | ---- | -------- |
| assess whether |     | an attacker | can | distribute | exploits |     | that target |               |         |         |          |            |        |      |          |
|                |     |             |     |            |          |     |             | this warning, | leading |         | to false | positives. | This   | may, | in turn, |
framework-levelvulnerabilitiestriggeredduringmodelload-
reduceusers’perceivedseverityduetoalertfatigue.Interest-
| ing, without | being | detected | by  | the scanning |     | tools | integrated |     |     |     |     |     |     |     |     |
| ------------ | ----- | -------- | --- | ------------ | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Lambda
into model hubs. In other words, we assess whether these ingly, the baseline containing a layer that invokes
scanners provide an effective additional line of defense /bin/sh in a .keras file was not flagged (i.e., a false
negative),whiletheequivalentmodelin.h5format(KV.3)
| when framework-level |     |                 | protections | fail. | To         | do so, | we tested |                 |     |            |          |      |      |        |          |
| -------------------- | --- | --------------- | ----------- | ----- | ---------- | ------ | --------- | --------------- | --- | ---------- | -------- | ---- | ---- | ------ | -------- |
|                      |     |                 |             |       |            |        |           | did not produce |     | any label. | Overall, | this | test | raises | concerns |
| the exploits         | for | vulnerabilities |             | we    | identified | in     | Keras and |                 |     |            |          |      |      |        |          |
Skops against the scanners integrated into Hugging Face, regarding the accuracy of this particular threat definition.
| which is | the only | major | hub | that | integrates | scanners. | We  |     |     |     |     |     |     |     |     |
| -------- | -------- | ----- | --- | ---- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1.ItisworthnotingthatthebaselinemodelwithaLambdalayercalling
uploaded the original PoCs for each vulnerability without /bin/shinHDF5formatcoincidesexactlywiththePoCofKV.3,since
obfuscation or modification. Each exploit opens /bin/sh. theexploitconsistsofusingalegacyHDF5model.

RegardingtheSkopsmodels,thepicklefileforSV.3was
10
correctly detected, as expected for a standard (malicious)
8
pickle file. However, neither of the .skops files for SV.1 6
or SV.2 raised any issues. This is consistent with the fact 4
that no threats are explicitly defined for Skops in Guardian. 2
However, it is concerning that these cases were flagged safe_mode=False safe_mode=True weights_only=Falseweights_only=True
Sharing Scenario
as “No issue” rather than returning a more neutral (and
informative) label indicating a lack of compatibility.
JFrog. JFrog correctly classified the baseline Keras models
containing a malicious Lambda as “Unsafe,” and the non-
malicious Keras models without Lambda layers as “No
issue.” It also successfully identified the malicious pickle
file of SV.3. However, similar to Protect AI, it misclassified
Keras models with benign Lambda layers as “Unsafe”—an
evenstrongerflagthantheoneassignedbyProtectAI—thus
producing false positives. The reported details cited “mod-
els with Lambda layers containing malicious code,” which
did not align with reality. JFrog also failed to detect our
exploit for KV.1, demonstrating difficulties in identifying
newer Keras threats, and provided no decision for KV.2,
which remained stuck in the status “Queued” despite being
uploadedtothesamerepositoryandatthesametimeasthe
others. Re-uploading KV.2 yielded the same result. Finally,
both .skops models (SV.1 and SV.2) were labeled as “not
a model”. While this outcome can be explained by the lack
of support for the .skops format, it may nevertheless be
misleading for end users.
Final Label. The final label shown by Hugging Face corre-
sponds to the most severe label assigned by its scanners.
This approach allows threats such as the PoC for KV.1
(detected only by Protect AI) to be flagged as “Unsafe,”
therebycompensatingforfalsenegatives.Ontheotherhand,
this strategy also amplifies false positives: harmless Keras
models with Lambda layers are escalated to “Unsafe.”
Concerningly, since none of the scanners support Skops
models, the final label for both SV.1 and SV.2 PoCs was
“Safe.” This represents a clear false negative and is particu-
larly problematic, as a reassuring label such as “Safe” was
assigned despite the absence of compatible scanners.
5. Survey on User Perception (RQ3)
To assess whether the narratives promoted by certain
frameworks and hubs influence ML practitioners’ percep-
tions, we conducted a public survey. The survey was dis-
tributed via social media and direct outreach to profession-
als in both academic and industrial ML communities. To
minimize bias, we did not disclose the cybersecurity focus
of the study. This enables gathering more authentic insights
intothenaturalconcernsandmentalmodelsthatparticipants
associate with model sharing. Responses were anonymous,
and no sensitive data was collected. The survey included
14 multiple-choice questions, 6 of which allowed optional
open-endedanswers.Itwasstructuredintothreemainparts,
presented in the following sections. All questions, raw re-
sults, and scripts used for both statistics extraction and
plotting are publicly available.
)01-1(
leveL
trofmoC
Figure 1: Distribution of user comfort levels (1–10) when
loading shared models under different configurations.
Limitations. While the survey offers insights, its limited
numberofparticipantsmeansthefindingsshouldbeconsid-
ered as indicative rather than representative of the broader
ML community. Nevertheless, the results highlight mean-
ingfultrendsinhowmodelsharingsecurityisperceived.To
assess the robustness of these observations, we complement
the analysis with statistical tests evaluating the significance
of the reported outcome.
UP.1 - Demographics. Atotalof62participantscompleted
the survey. Among them, 53 (85.5%) reported experience
loading or sharing ML models. All results presented in the
following analysis are restricted to these 53 participants.
Withinthisgroup,33(62.3%)listedMLorArtificialIn-
telligence (AI) as their primary area of expertise, 9 (17.0%)
selected cybersecurity, and the remaining 11 (20.7%) came
from related fields such as data science, software engineer-
ing, high-performance computing, or robotics. The average
self-assessed expertise in ML was 3.47 on a scale from 1
(basic familiarity) to 5 (expert).
UP.2 - Perception of Model Loading Security. To as-
sess participants’ perceived security when loading shared
models, we asked them to rate their comfort with four
Python scripts—two using Keras and two using PyTorch.
These frameworks were selected because both expose
security-orientedloading-timeflagsexplicitly:safe_mode
in Keras and weights_only in PyTorch. Together, they
also cover a range of persistence strategies—self-contained
vs. non-self-contained, and data-based vs. code-based for-
mats—providingvaluablecontrastforouranalysis.Foreach
case, participants were also asked to specify the reasons
for any lack of comfort, selecting from predefined cate-
gories—such as ethical concerns, data bias, and cyberse-
curity risks—or by providing an open-ended response.
Keras safe_mode. The survey included two Keras code
snippets differing only in the value of the safe_mode
flag (False vs. True). As shown in Figure 1, average
comfortlevelsgrowfrom4.5/10withsafe_mode=False
to 7.8/10 with safe_mode=True, with responses shifting
from widely dispersed to tightly clustered around higher
scores—indicating stronger perceived security. The number
ofparticipantsexpressingconcernsaboutarbitrarycodeexe-
cutiondecreasedfrom44(83%)to8(15.1%),halfofwhom
identified cybersecurity as their primary area of expertise.
PyTorch weights_only. The survey included two Py-
Torch snippets, each setting the weights_only flag to

either False or True. In the latter case, participants practitioners and framework or hub maintainers, to raise
were informed that model definitions must be provided awareness and enable sound security choices.
| separately, | possibly | by  | importing | shared | code. | Here, | the |     |     |     |     |     |     |     |     |
| ----------- | -------- | --- | --------- | ------ | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
shift in perceived security was smaller than in the previous 6.1. The Illusion of Secure File Formats
| case: the | average | comfort | level | grew | from | 5.9 to | 7.0. As |     |     |     |     |     |     |     |     |
| --------- | ------- | ------- | ----- | ---- | ---- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
shown in Figure 1, the dispersed distribution of responses Derived from: SA.F, KV.1, KV.2, SV.1, SV.2
indicatesuncertaintyamongparticipants.However,thenum-
|                     |           |            |            |          |          |            |         | Data-based           | formats   | are        | often     | perceived | as         | more          | secure |
| ------------------- | --------- | ---------- | ---------- | -------- | -------- | ---------- | ------- | -------------------- | --------- | ---------- | --------- | --------- | ---------- | ------------- | ------ |
| ber of participants |           | expressing | concerns   |          | about    | arbitrary  | code    |                      |           |            |           |           |            |               |        |
|                     |           |            |            |          |          |            |         | than code-based      |           | formats,   | primarily | because   |            | they do       | not    |
| execution           | decreased | more       | sharply,   | though   |          | still less | than    |                      |           |            |           |           |            |               |        |
|                     |           |            |            |          |          |            |         | directly             | serialize | executable | code.     | This      | belief     | is reinforced |        |
| in the Keras        | case,     | from       | 28 (52.8%) |          | to 13    | (24.5%),   | even    |                      |           |            |           |           |            |               |        |
|                     |           |            |            |          |          |            |         | by the documentation |           | and        | narrative | of        | explicitly | security-     |        |
| though the          | more      | secure     | option     | requires | manually |            | loading |                      |           |            |           |           |            |               |        |
orientedframeworks.Whilethisclaimmayseemreasonable,
| code for    | the model   | definition. |          | Notably, | despite | unrestricted |        |              |     |           |              |     |      |          |        |
| ----------- | ----------- | ----------- | -------- | -------- | ------- | ------------ | ------ | ------------ | --- | --------- | ------------ | --- | ---- | -------- | ------ |
|             |             |             |          |          |         |              |        | our analysis | in  | Section 4 | demonstrates |     | that | the file | format |
| pickle use, | respondents |             | reported | moderate |         | concern      | in the |              |     |           |              |     |      |          |        |
alonedoesnotdeterminethesecurityofmodelsharing,and
| weights_only=False |     |     | setting. |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thattherealityisfarmorecomplex.Inparticular,bothKeras
| Statistical | Validation   | of          | the Observed |              | Effects. | To       | evaluate |            |       |           |            |         |         |           |      |
| ----------- | ------------ | ----------- | ------------ | ------------ | -------- | -------- | -------- | ---------- | ----- | --------- | ---------- | ------- | ------- | --------- | ---- |
|             |              |             |              |              |          |          |          | and Skops  | use   | JSON to   | represent  | the     | logical | structure | of   |
| whether     | the observed | differences |              | in perceived |          | security | are      |            |       |           |            |         |         |           |      |
|             |              |             |              |              |          |          |          | executable | code. | Security, | therefore, | depends |         | on strict | val- |
statistically robust, we conduct a paired Wilcoxon signed- idation and restrictions applied during the translation from
rank test [62]. In this context, p denotes the p-value of JSON to code objects, resulting in a threat model similar
| the test | and r           | the corresponding |     | effect   | size. | The      | results |                |                 |          |        |           |       |             |       |
| -------- | --------------- | ----------------- | --- | -------- | ----- | -------- | ------- | -------------- | --------------- | -------- | ------ | --------- | ----- | ----------- | ----- |
|          |                 |                   |     |          |       |          |         | to that of     | code-based      | formats. | This   | fragility |       | was evident | in    |
| indicate | a statistically | significant       |     | increase | in    | reported | com-    |                |                 |          |        |           |       |             |       |
|          |                 |                   |     |          |       |          |         | our discovered | vulnerabilities |          | (KV.1, | KV.2,     | SV.1, | and         | SV.2) |
fort when safe_mode=True with a large effect size andthesubsequentpatches.Indeed,thesefixesrestrictedthe
(p = 3.14×10−9, |r| = 0.87). A statistically significant excessive flexibility and addressed missing checks in how
comfortincrease,thoughmoremoderate,wasalsoobserved
|                        |     |     |     |      |         |     |          | code was       | reconstructed | from     | JSON. | In         | other | words,         | model |
| ---------------------- | --- | --- | --- | ---- | ------- | --- | -------- | -------------- | ------------- | -------- | ----- | ---------- | ----- | -------------- | ----- |
| when weights_only=True |     |     |     | (p = | 0.0054, | |r| | = 0.42). |                |               |          |       |            |       |                |       |
|                        |     |     |     |      |         |     |          | expressiveness | impacts       | security |       | regardless | of    | the serializa- |       |
These results indicate that the differences in perceived tion format used: higher expressiveness increases the attack
security reported in Figure 1 are unlikely to arise from surface. Alternative approaches exist, such as constrained
| random | variation | and suggest | that | the | presence | of  | security- |     |     |     |     |     |     |     |     |
| ------ | --------- | ----------- | ---- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
formatslikeONNX[42],whichimplicitlyreducetheattack
| oriented | mechanisms | meaningfully |     | influences |     | user | percep- |     |     |     |     |     |     |     |     |
| -------- | ---------- | ------------ | --- | ---------- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
surfacebylimitingthesetofallowedoperators,albeitatthe
tion of model loading security. cost of flexibility (see Section 6.2).
|        |        |                  |     |       |     |          |      | JSON Models | Are | Code. | To conclude |     | this point, | we  | report |
| ------ | ------ | ---------------- | --- | ----- | --- | -------- | ---- | ----------- | --- | ----- | ----------- | --- | ----------- | --- | ------ |
| UP.3 - | Impact | of Model-Sharing |     | Hubs. |     | We asked | par- |             |     |       |             |     |             |     |        |
astatementfromtheGoogleSecurityTeamduringaprivate
| ticipants     | whether | their comfort |           | level      | would   | change | when     |                  |         |           |           |                    |     |              |       |
| ------------- | ------- | ------------- | --------- | ---------- | ------- | ------ | -------- | ---------------- | ------- | --------- | --------- | ------------------ | --- | ------------ | ----- |
|               |         |               |           |            |         |        |          | exchange         | related | to one    | of our    | Keras disclosures: |     |              |       |
| loading       | models  | from hubs     | such      | as Hugging |         | Face,  | which    |                  |         |           |           |                    |     |              |       |
|               |         |               |           |            |         |        |          | ”Basically,      | a truly | safe_mode |           | in Python          |     | for this     | isn’t |
| integrates    | various | security      | scanners. | In         | total,  | 39/53  | partici- |                  |         |           |           |                    |     |              |       |
|               |         |               |           |            |         |        |          | really possible. |         | Loading   | untrusted | models             | is  | like running |       |
| pants (73.6%) |         | responded     | that      | the use    | of such | hubs   | would    |                  |         |           |           |                    |     |              |       |
increasetheirlevelofcomfortwhenloadingsharedmodels. untrusted code—models are code.” [54]
5.1. Results Interpretation Suggestions for the Community. Do not rely on file for-
matsasaguaranteeofsecurity.Whattrulymattersiswhat
|              |            |               |             |           |              |                 |         | the format | contains     | and    | how          | that content |           | is processed. |     |
| ------------ | ---------- | ------------- | ----------- | --------- | ------------ | --------------- | ------- | ---------- | ------------ | ------ | ------------ | ------------ | --------- | ------------- | --- |
| These        | results    | highlight     | a clear     | shift     | in           | user perception |         |            |              |        |              |              |           |               |     |
|              |            |               |             |           |              |                 |         | Sharing    | code objects | is     | always       | inherently   | risky.    |               |     |
| driven by    | the        | presence      | of specific |           | flags        | in the          | model-  |            |              |        |              |              |           |               |     |
| loading      | function,  | particularly  |             | among     | participants |                 | who did |            |              |        |              |              |           |               |     |
|              |            |               |             |           |              |                 |         | 6.2. Block | or           | Allow: | The Security |              | Trade-Off |               |     |
| not identify | as         | cybersecurity | experts.    |           | Notably,     | the             | results |            |              |        |              |              |           |               |     |
| indicate     | a stronger | influence     | of          | safe_mode |              | compared        | to      |            |              |        |              |              |           |               |     |
weights_only. This discrepancy may stem from users Derived from: SA.F, KV.1, KV.2, SV.1, SV.2
| perceiving      | the | need to manually      |          | define | and    | instantiate | the      |               |          |             |         |           |              |                |     |
| --------------- | --- | --------------------- | -------- | ------ | ------ | ----------- | -------- | ------------- | -------- | ----------- | ------- | --------- | ------------ | -------------- | --- |
|                 |     |                       |          |        |        |             |          | As with       | software | in general, |         | designing | a            | secure sharing |     |
| model (required |     | by weights_only=True) |          |        |        | as          | an addi- |               |          |             |         |           |              |                |     |
|                 |     |                       |          |        |        |             |          | mechanism     | requires | trade-offs  | between |           | flexibility, | usability,     |     |
| tional source   | of  | risk. At              | the same | time,  | it may | also        | reflect  |               |          |             |         |           |              |                |     |
|                 |     |                       |          |        |        |             |          | and security. | Across   | frameworks, |         | security  | is           | often enforced |     |
howdifferentflag-namingchoicesshapeusers’perceptionof
viaeitherallowlistsorblocklists.Whiletheseapproachesre-
| security. | Finally, | the results | confirm | that | hub-level |     | scanning |     |     |     |     |     |     |     |     |
| --------- | -------- | ----------- | ------- | ---- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
ducetheattacksurface,theyinevitablylimitflexibility,since
features also have a significant effect on user perception. anything outside an allowlist or inside a blocklist is either
|     |     |     |     |     |     |     |     | prohibited | or left | to human-based |     | fallback | mechanisms. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | -------------- | --- | -------- | ----------- | --- | --- |
6. Takeaways ONNX [42], although not explicitly designed for secu-
|     |     |     |     |     |     |     |     | rity, restricts | models | to a | limited | set of | operators, | enabling |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | ---- | ------- | ------ | ---------- | -------- | --- |
In this section, we take a broader perspective to discuss interoperability across frameworks and implicitly reducing
the implications of our findings. Our discussion is enriched the attack surface, but at the cost of flexibility, as only
with suggestions for the community, directed at both ML certain models and training capabilities are supported.

Methodsclaimedtobesecurity-orientedfollowasimilar a rigorous proof, it suggests a significant inertia within
pattern when patching new vulnerabilities. In Keras, the fix the ecosystem, where users continue to rely on older ver-
toKV.1involvedintroducinganallowlistofKeras’modules sions despite the availability of known (security) improve-
to reconstruct the saved objects. However, as demonstrated ments. Consequently, developers need to maintain support
in KV.2, this hardening could be bypassed through code for legacy mechanisms, further complicating the design of
reuse, requiring further restrictions and blocklisting. robust and secure sharing APIs.
| PyTorch | promotes |     | its weights_only |     |     | mode | as  |     |     |     |     |     |
| ------- | -------- | --- | ---------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
security-oriented, as it allows only tensors, enforcing a nar- Suggestions for the Community. While recognizing the
rowtypeallowlisttopreventarbitrarycodeexecution.Keras, complexity of the problem, developers should, whenever
incontrast,whilealsosupportingthesavingofweightsonly, possible, require insecure legacy options to be explicitly
doesnotpresentthisasasecuritymeasure.Inbothcases,the enabledbyusersandprovideclearwarningsabouttheas-
attack surface is reduced, but functionality is constrained, sociated risks. Users, in turn, should maintain heightened
shifting the problem to validating the trustworthiness of the skepticism toward legacy formats, as frameworks often
sources providing the model architecture code. prioritize compatibility over security.
| Ultimately, | in  | some | cases, | allowlisting | and | blocklisting |     |     |     |     |     |     |
| ----------- | --- | ---- | ------ | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- |
propagate to users themselves, who act as the last line of 6.4. Model Scanning as Malware Analysis
| defense. | For instance, | in  | Skops | users must | manually |     | review |     |     |     |     |     |
| -------- | ------------- | --- | ----- | ---------- | -------- | --- | ------ | --- | --- | --- | --- | --- |
andapproveuntrustedtypes.However,aswedemonstratein
|          |            |           |     |          |     |         |       | Derived | From: SA.H, | MS  |     |     |
| -------- | ---------- | --------- | --- | -------- | --- | ------- | ----- | ------- | ----------- | --- | --- | --- |
| SV.1 and | SV.2, this | mechanism |     | is prone | not | only to | human |         |             |     |     |     |
error but also to framework-level flaws, which may allow Automatic model scanners integrated into model hubs,
attackers to exploit user-allowlisted types while gaining while providing additional protection and being poten-
capabilities for other, riskier types. tially useful, inherit well-known limitations of traditional
|     |     |     |     |     |     |     |     | signature-based | malware | detectors | [63]. Moreover, | they of- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------- | --------- | --------------- | -------- |
Suggestions for the Community. Learn from decades of ten adopt a framework-centric design, supporting only spe-
experience in trade-offs between flexibility and security. cificframeworksandformats,andfrequentlyduplicatesafe-
Allowlists offer strong security, but require continuous guards already implemented within the frameworks them-
maintenance and can affect usability. Be aware and don’t selves.Forinstance,ProtectAI[47]definesframework-and
rely on them alone: while they reduce the attack surface, format-specificthreatsandchecksmodelsagainstthem[61],
theyarenotinfallible,andshouldneverbeblindlytrusted. restricting detection to already formalized weaknesses.
Evaluate how strong limitations might offload security Our evaluation of Hugging Face model scanners (MS),
responsibilities to users, reintroducing risks. inadditiontofindingfalsepositivesandnegatives(seeeval-
|     |     |     |     |     |     |     |     | uation results | for details), | shows | that Skops, | despite being |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------------- | ----- | ----------- | ------------- |
6.3. The Security Cost of Slow Adoption promoted by Hugging Face as a secure persistence format,
isunsupportedbyanyintegratedscanner.Thishighlightsthe
|         |       |       |      |     |     |     |     | fragmented | and incomplete      | nature | of the     | current landscape  |
| ------- | ----- | ----- | ---- | --- | --- | --- | --- | ---------- | ------------------- | ------ | ---------- | ------------------ |
| Derived | from: | KV.3, | SV.3 |     |     |     |     |            |                     |        |            |                    |
|         |       |       |      |     |     |     |     | of model   | scanners integrated |        | into model | hubs. Finally, the |
KV.3 and SV.3 give us hints about another systemic labels produced by these scanners can be misleading when
issue: the tradeoff between legacy compatibility and se- nomatchisfound.Forinstance,ifaformatisnotsupported,
curity. In both cases, legacy formats using pickle dese- JFrog[48]returns“notamodel”andProtectAIreports“No
rialization (e.g., HDF5 in Keras or joblib in scikit-learn) issue”. Suchoutputs, especially ifthey come froma limited
bypass the modern security mechanisms and allow trivial analysis, can create a false sense of security, such as in
code execution, even when loaded under supposedly secure traditional antivirus software [64].
| configurations. | This | reflects | a        | deeper   | problem | in the    | ML  |             |                                        |     |     |     |
| --------------- | ---- | -------- | -------- | -------- | ------- | --------- | --- | ----------- | -------------------------------------- | --- | --- | --- |
|                 |      |          |          |          |         |           |     | Suggestions | for the Community.Inspiredbythemalware |     |     |     |
| ecosystem:      | the  | slow     | adoption | of newer | library | versions. |     |             |                                        |     |     |     |
Backward compatibility often takes precedence to preserve analysisdomain,scannersshouldbetreatedonlyasafirst
reproducibility,collaboration,andportability—sometimesat line of defense. A possible direction is the adoption of
the silent cost of security, as our PoCs demonstrate. behavioralanalysistomovebeyondstaticchecks.Finally,
Interestingly, while the Skops fix relies on obtaining hubsshouldpromotegreatertransparencyinreportlabels.
| explicit | user confirmation |     | and | informing | users | of the | asso- |     |     |     |     |     |
| -------- | ----------------- | --- | --- | --------- | ----- | ------ | ----- | --- | --- | --- | --- | --- |
ciatedsecurityrisks,theKerasteaminsteadchosetoextend
|               |             |            |            |          |          |             |       | 6.5. Trusting | “Safe”:     | A Risk | in Itself   |             |
| ------------- | ----------- | ---------- | ---------- | -------- | -------- | ----------- | ----- | ------------- | ----------- | ------ | ----------- | ----------- |
| the security  | measures    |            | of the new | format   | to the   | legacy      | one,  |               |             |        |             |             |
| demonstrating | a           | commitment | to         | securing | legacy   | versions.   |       |               |             |        |             |             |
|               |             |            |            |          |          |             |       | Derived       | from: SA.F, | SA.H,  | KV.1, KV.2, | KV.3, SV.1, |
| To            | give a hint | of         | how slow   | the      | adoption | of          | newer |               |             |        |             |             |
|               |             |            |            |          |          |             |       | SV.2, SV.3,   | UP.1, UP.2, | UP.3,  | MS          |             |
| versions      | is, we      | analyzed   | downloads  |          | after    | the release | of    |               |             |        |             |             |
Keras 3.9.0 (including critical security patches). Notably, What becomes evident from our analysis is that a com-
older 2.x.x versions from 2023 still saw significantly higher plete and truly secure solution for model sharing does not
download counts than most newer 3.x.x releases. More data exist. Every approach, whether from hubs or frameworks,
are available in Appendix B. While this does not constitute requires compromises or shifts part of the responsibility

elsewhere. This is, unfortunately, a well-known reality in they compared model hubs to the generic software sup-
computer science, and model sharing is no exception. ply chain, categorizing them based on their access model
However, this reality often clashes with the prevailing (open or gated) and identifying the associated risks [9].
narrative and common beliefs. Labeling a mode or a model Subsequent research explored typosquatting and imperson-
(after scanning) as “safe” or “secure” is rarely consistent ation threats [17] and analyzed model reuse practices on
with the actual risks involved. Instead, we should refer to Hugging Face [18]. Across these studies, Jiang et al. found
theseasapproachesthatattempt toprovidesecurityharden- insufficient provenance verification, weak dependency man-
ing against known exploitation paths, establish mechanisms agement, and inadequate documentation, ultimately con-
for trusted types, or detect potential (known) threats in cluding that trust in hub-shared models is often misplaced.
models prior to download. However, such efforts do not Extending the understanding of risks and practices within
inherently make these approaches ”secure” or even ”safe”. model hubs, Jones et al. [19] analyzed the Hugging Face
While we acknowledge the complexity in designing ecosystem, uncovering high model turnover rates, a corre-
APIs accessible to users with diverse backgrounds, such as lation between popularity and documentation quality, and
those in the ML community, we believe there is a need for challenges in model management and reproducibility.
clearandtransparentcommunication.Usersoftenlackeither In parallel, other researchers have explored specific at-
| the knowledge      | or the willingness |            | to critically |              | assess labels |               |               |                |                |            |             |          |             |       |
| ------------------ | ------------------ | ---------- | ------------- | ------------ | ------------- | ------------- | ------------- | -------------- | -------------- | ---------- | ----------- | -------- | ----------- | ----- |
|                    |                    |            |               |              |               | tack vectors. |               | In particular, |                | Casey      | et al.      | [10]     | and Zhao    | et    |
| like “secure”      | or “safe.”         | Such       | terminology   | is           | a significant |               |               |                |                |            |             |          |             |       |
|                    |                    |            |               |              |               | al. [16]      | demonstrated  |                | the prevalence |            | of          | insecure | serializa-  |       |
| oversimplification | that               | fails to   | reflect the   | complex      | (and less     |               |               |                |                |            |             |          |             |       |
|                    |                    |            |               |              |               | tion methods  |               | (e.g., pickle) |                | in Hugging | Face        | models,  |             | which |
| optimistic)        | reality.           |            |               |              |               |               |               |                |                |            |             |          |             |       |
|                    |                    |            |               |              |               | expose        | users to      | arbitrary      | code           | execution. |             | Building | on          | this, |
| This               | kind of messaging  |            | has real      | consequences | for           |               |               |                |                |            |             |          |             |       |
|                    |                    |            |               |              |               | Zhao et       | al. conducted |                | a large-scale  |            | measurement |          | study       | of    |
| users. As          | shown in our       | survey     | (UP.2         | and          | UP.3), users  |               |               |                |                |            |             |          |             |       |
|                    |                    |            |               |              |               | malicious     | code          | poisoning      |                | on Hugging |             | Face,    | discovering |       |
| exhibit increased  | security           | confidence | when          | features     | like the      |               |               |                |                |            |             |          |             |       |
|                    |                    |            |               |              |               | multiple      | infected      | models         | and            | dataset    | scripts.    |          |             |       |
| safe_mode          | option are         | enabled    | or when       | hubs         | advertise     |               |               |                |                |            |             |          |             |       |
|                    |                    |            |               |              |               | Focusing      |               | more on        | the            | latter     | threat      | of code  | poisoning,  |       |
| built-in security  | scanning.          | While      | choosing      | methods      | with          |               |               |                |                |            |             |          |             |       |
|                    |                    |            |               |              |               | Hua et        | al. [13]      | introduced     |                | MalModel,  | which       |          | embeds      | exe-  |
| some degree        | of security        | hardening  | is            | certainly    | a positive    |               |               |                |                |            |             |          |             |       |
step, it is by no means sufficient to ensure true security. cutable payloads directly into deep learning model weights,
A critical observation is that, with safe_mode activated, demonstrating the feasibility of concealing malware within
|               |                |              |               |          |            | models.          | Similarly,  | EvilModel |     | [14]      | and EvilModel |           | 2.0 | [15]   |
| ------------- | -------------- | ------------ | ------------- | -------- | ---------- | ---------------- | ----------- | --------- | --- | --------- | ------------- | --------- | --- | ------ |
| more than     | 90% of survey  | participants | who           | did      | not choose |                  |             |           |     |           |               |           |     |        |
|               |                |              |               |          |            | showed           | that entire | malware   |     | binaries  | can           | be hidden |     | within |
| cybersecurity | as their field | of           | expertise—but | who      | had prior  |                  |             |           |     |           |               |           |     |        |
|               |                |              |               |          |            | model parameters |             | without   |     | degrading | performance.  |           |     |        |
| experience    | in model       | sharing—did  | not           | consider | arbitrary  |                  |             |           |     |           |               |           |     |        |
code execution to be a concern. This misplaced trust is, From a framework-level perspective, Zhu et al. [20] in-
in itself, a serious security issue that requires a coordinated troduced the TensorAbuse attack, which exploits legitimate
community effort to be addressed. TensorFlow APIs to perform unintended operations (e.g.,
|     |     |     |     |     |     | file access | and | network | messaging) |     | during | model | inference. |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ---------- | --- | ------ | ----- | ---------- | --- |
Suggestions for the Community. Oversimplified security This work highlights a gap in the state of the art on the
labelscancreatemisplacedtrust.Whensimplificationsare
securityofmodelsharing.Thisgapwasfurtherunderscored
necessary, present them with care to align with the actual by Cyrus Parzian, who presented a talk at DEF CON 33 on
security guarantees. the risks of model sharing, using as examples the security
|            |       |     |     |     |     | concerns | associated |         | with pickle | deserialization |     |     | and ONNX |     |
| ---------- | ----- | --- | --- | --- | --- | -------- | ---------- | ------- | ----------- | --------------- | --- | --- | -------- | --- |
| 7. Related | Works |     |     |     |     | models   | shared     | in .exe | format      | [21].           |     |     |          |     |
Being an established research area, generic software Gaps in the State of the Art. Prior work on the security of
supply chain security has been extensively studied, with model sharing has primarily examined supply chain risks,
several works [6], [7], [8] identifying and systematizing maliciouscodeinjection,andabusesofspecificTensorFlow
its risks. While some insights from these studies can be APIs. However, no study has systematically evaluated the
extended to the model-sharing context, recent research has security of model-sharing approaches across different ML
gone a step further by specifically examining supply chain frameworks and hubs, nor critically questioned the actual
guaranteesofsharingmechanismsthatareclaimedtobese-
| issues in | this context. | In particular, | Meiklejohn |     | et al. [12] |     |     |     |     |     |     |     |     |     |
| --------- | ------------- | -------------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
framed ML models as supply chain artifacts and proposed cure. Our paper closes this gap. We assess the security pos-
cryptographic mitigations for the identified threats, whereas ture of widely used frameworks, uncover 0-day vulnerabil-
Wang et al. [11] mapped vulnerabilities across the Large ities (subsequently disclosed and assigned CVEs) in mech-
|     |     |     |     |     |     | anisms | advertised | as  | secure | but | designed | to  | support | self- |
| --- | --- | --- | --- | --- | --- | ------ | ---------- | --- | ------ | --- | -------- | --- | ------- | ----- |
LanguageModel(LLM)supplychain,notingthatonly56%
of them currently have available fixes. contained model artifacts, and examine how security narra-
Building on the observation that model hubs have be- tives shape user perception. At the hub level, while prior
come central to model distribution and therefore repre- work has focused mainly on supply-chain–related risks, we
sent a potential vector for supply chain attacks, Jiang et empirically assess the effectiveness of hub-integrated scan-
al. conducted a series of empirical studies examining the ners and labeling practices, questioning their effectiveness
security of model-sharing platforms. In their initial work, and how they influence users’ sense of security.

8. Future Directions Acknowledgments
This work was partially supported by the project SER-
In line with our goal of deepening understanding of
ICS (PE00000014) under the NRRP MUR program funded
the security challenges in loading ML models, we highlight
by the EU - NGEU. The authors would like to thank the
several potential directions for future research.
framework and hub maintainers and developers, and the
Beyond the framework and hub levels examined in this security teams involved in the coordinated disclosure pro-
work, a third dimension may involve third-party libraries cess for their responsiveness, constructive engagement, and
not included in official framework documentation and thus commitmenttoimprovingthesecurityoftheMLecosystem.
excludedfromourselectioncriteria.Thepopularityofsome
(e.g.,safetensors[65])makesitworthwhiletoexaminehow References
they align with our identified categories and what unique
implications they introduce. Additionally, it would also be
[1] Hugging Face Inc., “Hugging Face Hub Documentation,” https:
interesting to explore how users approach these libraries, //huggingface.co/docs/hub/index,2025,accessed:2025-08-05.
specifically whether they apply a different level of skepti- [2] Kaggle, Inc., “Kaggle Models,” https://www.kaggle.com/models,
cism compared to official methods. 2025,accessed:2025-08-14.
LLM-specificformats(e.g.,GGUF,GPTQ,AWQ)intro- [3] M. Watson, F. Chollet, D. Sreepathihalli, S. Saadat, R. Sam-
duce additional challenges. Indeed, the prohibitive size of path, G. Rasskin, S. Zhu, V. Singh, L. Wood, Z. Tan, I. Stenbit,
C.Qian,J.Bischofetal.,“KerasHub,”https://github.com/keras-team/
these models shifts users’ focus from training to inference,
keras-hub,2024.
although even inference is often infeasible on local ma-
[4] GoogleResearch,BrainTeam,“TensorFlowHub:ReusableMachine
chines. Moreover, pre-trained models are typically released
LearningModules,”https://www.tensorflow.org/hub,2025,accessed:
only by a few major vendors that have the computational 2025-08-14.
resources to train them. These factors not only redirect [5] PyTorchFoundation,“PyTorchHub,”https://pytorch.org/hub/,2025,
the focus of sharing solutions toward optimized formats accessed:2025-08-14.
designed for inference, which are not required to be well- [6] R. Duan, O. Alrawi, R. P. Kasturi, R. Elder, B. Saltaformaggio,
suitedforarchitecturalmodifications(thusmakingrestricted and W. Lee, “Towards Measuring Supply Chain Attacks on Pack-
age Managers for Interpreted Languages,” in 28th Annual Network
solutions less limiting), but may also alter the overall threat
and Distributed System Security Symposium, NDSS 2021, virtually,
model due to the different distribution of actors involved.
February21-25,2021. TheInternetSociety,2021.
Automatic model scanners also represent a broad area
[7] M.Ohm,H.Plate,A.Sykosch,andM.Meier,“Backstabber’sknife
for future research. While we discussed their limitations, collection:Areviewofopensourcesoftwaresupplychainattacks,”in
future work could systematically assess their performance DetectionofIntrusionsandMalware,andVulnerabilityAssessment,
C. Maurice, L. Bilge, G. Stringhini, and N. Neves, Eds. Cham:
at scale, particularly against diverse adversarial techniques.
SpringerInternationalPublishing,2020,pp.23–43.
Inspired by advances in malware detection, additional ap-
[8] P. Ladisa, H. Plate, M. Martinez, and O. Barais, “SoK: Taxonomy
proaches (e.g., dynamic analysis) could be explored.
ofAttacksonOpen-SourceSoftwareSupplyChains,”in44thIEEE
Symposium on Security and Privacy, SP 2023, San Francisco, CA,
USA, May 21-25, 2023. IEEE, 2023, pp. 1509–1526. [Online].
9. Conclusions Available:https://doi.org/10.1109/SP46215.2023.10179304
[9] W. Jiang, N. Synovic, R. Sethi, A. Indarapu, M. Hyatt, T. R.
Schorlemmer, G. K. Thiruvathukal, and J. C. Davis, “An Empirical
In this work, we evaluated the security posture of Ma-
Study of Artifacts and Security Risks in the Pre-trained Model
chine Learning model sharing across frameworks and hubs. Supply Chain,” in Proceedings of the 2022 ACM Workshop on
We found that protection is inconsistent: many mechanisms SoftwareSupplyChainOffensiveResearchandEcosystemDefenses,
SCORED2022,LosAngeles,CA,USA,7November2022,S.Torres-
provide no safeguards, while others shift responsibility to
Arias,M.S.Melara,andL.Simon,Eds. ACM,2022,pp.105–114.
usersorimposestrongrestrictionsonflexibility.Eventhose
[Online].Available:https://doi.org/10.1145/3560835.3564547
promoted as secure fail to reliably prevent exploitation. By
[10] B. Casey, J. C. S. Santos, and M. Mirakhorli, “A Large-Scale
uncovering 0-day vulnerabilities and analyzing user per- Exploit Instrumentation Study of AI/ML Supply Chain Attacks in
ceptions of these mechanisms, we exposed a critical gap Hugging Face Models,” arXiv preprint, vol. abs/2410.04490, 2024.
between the security narrative and reality. Our takeaways [Online].Available:https://doi.org/10.48550/arXiv.2410.04490
show that there is no straightforward silver bullet. Data- [11] S.Wang,Y.Zhao,Z.Liu,Q.Zou,andH.Wang,“SoK:Understanding
VulnerabilitiesintheLargeLanguageModelSupplyChain,”CoRR,
based formats and model scanners integrated into model
2025.
hubs fall short of ensuring actual security, and framework
[12] S. Meiklejohn, H. Blauzvern, M. Maruseac, S. Schrock, L. Simon,
or hub naming choices further compromise user awareness.
and I. Shumailov, “Position: Machine learning models have a
Security inevitably involves trade-offs: reducing risk often supplychainproblem,”inForty-secondInternationalConferenceon
limits usability, while support for legacy formats silently Machine Learning Position Paper Track, 2025. [Online]. Available:
reintroduces old vulnerabilities. Automatic scanning can https://openreview.net/forum?id=zfohnbkMu0
help, but its coverage is uneven, and results are sometimes [13] J. Hua, K. Wang, M. Wang, G. Bai, X. Luo, and H. Wang,
“MalModel: Hiding Malicious Payload in Mobile Deep Learning
misleading. Above all, shared models must be treated as
Models with Black-box Backdoor Attack,” arXiv preprint, vol.
code, and loading untrusted artifacts carries the same risks
abs/2401.02659, 2024. [Online]. Available: https://doi.org/10.48550/
as executing untrusted software. arXiv.2401.02659

[14] Z. Wang, C. Liu, and X. Cui, “EvilModel: Hiding Malware [28] T.Developers,“Trainingcheckpoints—TensorFlowdocumentation,”
Inside of Neural Network Models,” in IEEE Symposium on https://www.tensorflow.org/guide/checkpoint, 2024, accessed: 2025-
| Computers |      | and Communications, |       |       | ISCC 2021, | Athens,   | Greece,    | 08-17.       |             |     |          |              |                      |     |
| --------- | ---- | ------------------- | ----- | ----- | ---------- | --------- | ---------- | ------------ | ----------- | --- | -------- | ------------ | -------------------- | --- |
| September | 5-8, | 2021.               | IEEE, | 2021, | pp. 1–7.   | [Online]. | Available: |              |             |     |          |              |                      |     |
|           |      |                     |       |       |            |           |            | [29] PyTorch | Foundation, |     | “PyTorch | Foundation,” | https://pytorch.org/ |     |
https://doi.org/10.1109/ISCC53001.2021.9631425
foundation/,2025,accessed:2025-07-22.
| [15] Z. Wang, | C.  | Liu, X. | Cui, J. | Yin, and | X. Wang, | “EvilModel | 2.0: |              |             |       |     |          |         |               |
| ------------- | --- | ------- | ------- | -------- | -------- | ---------- | ---- | ------------ | ----------- | ----- | --- | -------- | ------- | ------------- |
|               |     |         |         |          |          |            |      | [30] PyTorch | developers, | “Save | and | Load the | Model — | PyTorch Tuto- |
BringingNeuralNetworkModelsintoMalwareAttacks,”Computers
|             |     |           |            |       |           |            |        | rials                       | 2.7.0+cu126 | documentation,” |                | https://docs.pytorch.org/tutorials/ |                 |          |
| ----------- | --- | --------- | ---------- | ----- | --------- | ---------- | ------ | --------------------------- | ----------- | --------------- | -------------- | ----------------------------------- | --------------- | -------- |
| & Security, |     | vol. 120, | p. 102807, | 2022. | [Online]. | Available: | https: |                             |             |                 |                |                                     |                 |          |
|             |     |           |            |       |           |            |        | beginner/basics/saveloadrun |             |                 | tutorial.html, |                                     | 2025, accessed: | 2025-07- |
//www.sciencedirect.com/science/article/pii/S0167404822002012
23.
| [16] J. Zhao, | S.  | Wang, Y. | Zhao,   | X. Hou, | K. Wang, | P. Gao, | Y. Zhang, |                    |     |               |     |           |            |             |
| ------------- | --- | -------- | ------- | ------- | -------- | ------- | --------- | ------------------ | --- | ------------- | --- | --------- | ---------- | ----------- |
|               |     |          |         |         |          |         |           | [31] F. Pedregosa, |     | G. Varoquaux, | A.  | Gramfort, | V. Michel, | B. Thirion, |
| C. Wei,       | and | H. Wang, | “Models | Are     | Codes:   | Towards | Measuring |                    |     |               |     |           |            |             |
O.Grisel,M.Blondel,P.Prettenhofer,R.Weiss,V.Dubourgetal.,
| Malicious | Code | Poisoning | Attacks |     | on Pre-trained | Model | Hubs,” |     |     |     |     |     |     |     |
| --------- | ---- | --------- | ------- | --- | -------------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
Proceedings of the 39th IEEE/ACM International Conference “Scikit-learn:MachinelearninginPython,”Journalofmachinelearn-
in
on Automated Software Engineering, ASE 2024, Sacramento, CA, ingresearch,vol.12,no.Oct,pp.2825–2830,2011.
| USA, | October | 27 - | November | 1, 2024, | V.  | Filkov, | B. Ray, and |                   |             |     |            |             |                |       |
| ---- | ------- | ---- | -------- | -------- | --- | ------- | ----------- | ----------------- | ----------- | --- | ---------- | ----------- | -------------- | ----- |
|      |         |      |          |          |     |         |             | [32] scikit-learn | developers, |     | “10. Model | persistence | — scikit-learn | 1.7.1 |
M. Zhou, Eds. ACM, 2024, pp. 2087–2098. [Online]. Available: documentation,” https://scikit-learn.org/stable/model persistence.
https://doi.org/10.1145/3691620.3695271 html,2025,accessed:2025-07-30.
| [17] W. | Jiang, M. | Kim, | C. Cheung, | H.  | Kim, | G. K. | Thiruvathukal, |     |     |     |     |     |     |     |
| ------- | --------- | ---- | ---------- | --- | ---- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- |
[33] T.Chen,T.He,M.Benesty,V.Khotilovich,Y.Tang,H.Cho,K.Chen,
| and | J. C. | Davis, ““I | see | models | being a | whole | other thing”: |              |     |          |            |                |         |          |
| --- | ----- | ---------- | --- | ------ | ------- | ----- | ------------- | ------------ | --- | -------- | ---------- | -------------- | ------- | -------- |
|     |       |            |     |        |         |       |               | R. Mitchell, |     | I. Cano, | T. Zhou et | al., “Xgboost: | extreme | gradient |
an empirical study of pre-trained model naming conventions and boosting,”Rpackageversion0.4-2,vol.1,no.4,pp.1–4,2015.
| a tool | for | enhancing | naming | consistency,” |     | Empirical | Software |     |     |     |     |     |     |     |
| ------ | --- | --------- | ------ | ------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Engineering, vol. 30, no. 6, p. 155, 2025. [Online]. Available: [34] XGBoostdevelopers,“IntroductiontoModelIO—XGBoostTutori-
https://doi.org/10.1007/s10664-025-10711-4 als3.1.0-devdocumentation,”https://xgboost.readthedocs.io/en/latest/
|                |     |          |     |        |                    |     |           | tutorials/saving |     | model.html,2025,accessed:2025-08-12. |     |     |     |     |
| -------------- | --- | -------- | --- | ------ | ------------------ | --- | --------- | ---------------- | --- | ------------------------------------ | --- | --- | --- | --- |
| [18] W. Jiang, | N.  | Synovic, | M.  | Hyatt, | T. R. Schorlemmer, |     | R. Sethi, |                  |     |                                      |     |     |     |     |
Y. Lu, G. K. Thiruvathukal, and J. C. Davis, “An Empirical Study [35] P.Mooney,“2022KaggleMachineLearning&DataScienceSurvey,”
of Pre-Trained Model Reuse in the Hugging Face Deep Learning https://kaggle.com/competitions/kaggle-survey-2022,2022,kaggle.
| Model | Registry,” | in  | 45th | IEEE/ACM | International |     | Conference |     |     |     |     |     |     |     |
| ----- | ---------- | --- | ---- | -------- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
[36] JetBrains,“PythonDevelopersSurvey2024,”https://lp.jetbrains.com/
| on Software |     | Engineering, | ICSE | 2023, | Melbourne, | Australia, | May |     |     |     |     |     |     |     |
| ----------- | --- | ------------ | ---- | ----- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
python-developers-survey-2024/,2024,accessed:2025-08-13.
| 14-20, | 2023. | IEEE, | 2023, | pp. 2463–2475. |     | [Online]. | Available: |     |     |     |     |     |     |     |
| ------ | ----- | ----- | ----- | -------------- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.1109/ICSE48619.2023.00206 [37] Keras developers, “Weights-only saving & loading - Keras,”
|                |     |        |             |     |                   |     |           | https://keras.io/api/models/model |     |     |     | saving | apis/weights | saving and |
| -------------- | --- | ------ | ----------- | --- | ----------------- | --- | --------- | --------------------------------- | --- | --- | --- | ------ | ------------ | ---------- |
| [19] J. Jones, | W.  | Jiang, | N. Synovic, | G.  | K. Thiruvathukal, |     | and J. C. |                                   |     |     |     |        |              |            |
loading/,2025,accessed:2025-08-04.
| Davis, | “What | do we | know | about | Hugging | Face? | A systematic |     |     |     |     |     |     |     |
| ------ | ----- | ----- | ---- | ----- | ------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
literature review and quantitative validation of qualitative claims,” [38] TensorFlowDevelopers,“SaveandloadKerasmodels—TensorFlow
| in Proceedings |     | of  | the 18th | ACM/IEEE | International |     | Symposium |                                                                |     |     |     |     |     |     |
| -------------- | --- | --- | -------- | -------- | ------------- | --- | --------- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                |     |     |          |          |               |     |           | documentation,”https://www.tensorflow.org/tutorials/keras/save |     |     |     |     |     | and |
on Empirical Software Engineering and Measurement, ESEM 2024, load,2024,accessed:2025-08-17.
| Barcelona,               |     | Spain, October |     | 24-25, 2024, | X.   | Franch, | M. Daneva, |              |                                                             |                |     |           |           |           |
| ------------------------ | --- | -------------- | --- | ------------ | ---- | ------- | ---------- | ------------ | ----------------------------------------------------------- | -------------- | --- | --------- | --------- | --------- |
|                          |     |                |     |              |      |         |            | [39] PyTorch | developers,                                                 | “Serialization |     | semantics | — PyTorch | 2.7 docu- |
| S. Mart´ınez-Ferna´ndez, |     |                | and | L. Quaranta, | Eds. | ACM,    | 2024, pp.  |              |                                                             |                |     |           |           |           |
|                          |     |                |     |              |      |         |            | mentation,”  | https://docs.pytorch.org/docs/2.7/notes/serialization.html, |                |     |           |           |           |
13–24.[Online].Available:https://doi.org/10.1145/3674805.3686665
2025,accessed:2025-07-23.
| [20] R. Zhu, | G.  | Chen, W. | Shen, | X. Xie, | and R. | Chang, “My | Model is |     |     |     |     |     |     |     |
| ------------ | --- | -------- | ----- | ------- | ------ | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
[40] PythonSoftwareFoundation,“pickle—Pythonobjectserialization,”
MalwaretoYou:TransformingAIModelsintoMalwarebyAbusing
|            |     |                 |         |           |            |          |              | https://docs.python.org/3/library/pickle.html, |     |         |            |              | 2025, accessed: | 2025-    |
| ---------- | --- | --------------- | ------- | --------- | ---------- | -------- | ------------ | ---------------------------------------------- | --- | ------- | ---------- | ------------ | --------------- | -------- |
| TensorFlow |     | APIs,”          | in IEEE | Symposium | on         | Security | and Privacy, |                                                |     |         |            |              |                 |          |
| SP 2025,   | San | Francisco,      | CA,     | USA,      | May 12-15, | 2025,    | M. Blanton,  | 08-18.                                         |     |         |            |              |                 |          |
| W. Enck,   | and | C. Nita-Rotaru, |         | Eds.      | IEEE,      | 2025,    | pp. 486–503. |                                                |     |         |            |              |                 |          |
|            |     |                 |         |           |            |          |              | [41] A. Jalali,                                | B.  | Bossan, | and Merve, | “Introducing | Skops,”         | https:// |
[Online].Available:https://doi.org/10.1109/SP61157.2025.00012 huggingface.co/blog/skops,August2022,accessed:2025-07-30.
[21] C. Parzian, “Loading Models, Launching Shells: Abusing AI File [42] ONNXdevelopers,“ONNX,”https://onnx.ai/,2025,version:1.20.0.
| Formats | for | Code Execution,” |     | Presentation |     | at the DEF | CON 33 |     |     |     |     |     |     |     |
| ------- | --- | ---------------- | --- | ------------ | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
HackingConference-https://media.defcon.org/DEF%20CON%2033/ [43] skopsdevelopers,“Securepersistencewithskops—skops0.12doc-
DEF%20CON%2033%20presentations/Cyrus%20Parzian%20-% umentation,” https://skops.readthedocs.io/en/stable/persistence.html,
2025,accessed:2025-07-30.
20Loading%20Models%2C%20Launching%20Shells%20Abusing%
20AI%20File%20Formats%20for%20Code%20Execution.pdf, 2025, [44] XGBoostdevelopers,“PythonAPIReference—xgboost3.0.3doc-
accessed:2025-08-21.
|     |     |     |     |     |     |     |     | umentation,” |     | https://xgboost.readthedocs.io/en/stable/python/python |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------------------------------------------------ | --- | --- | --- | --- |
[22] Kerasdevelopers,“Wholemodelsaving&loading-Keras,”https:// api.html,2025,accessed:2025-08-05.
keras.io/api/models/model saving apis/model saving and loading/, [45] Hugging Face Inc., “Security — Hugging Face Hub Documenta-
2025,accessed:2025-07-30.
tion,”https://huggingface.co/docs/hub/security,2025,accessed:2025-
| [23] CVEProgram,“CVE-2025-1550,”https://www.cve.org/CVERecord? |     |     |     |     |     |     |     | 08-05. |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
id=CVE-2025-1550,2025,accessed:2025-07-30.
|     |     |     |     |     |     |     |     | [46] Cisco | Talos | (ClamAV | Team), | “ClamAV: | Open-Source | Antivirus |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ------- | ------ | -------- | ----------- | --------- |
[24] ——, “CVE-2025-8747,” https://www.cve.org/CVERecord?id= Toolkit,”https://docs.clamav.net/,2025,accessed:2025-08-14.
CVE-2025-8747,2025,accessed:2025-08-17.
|     |     |     |     |     |     |     |     | [47] Protect | AI, “Protect | AI  | — The | Platform | for AI Security,” | https:// |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | --- | ----- | -------- | ----------------- | -------- |
[25] F.Cholletetal.,“Keras,”2015,https://keras.io.
protectai.com/,2025,accessed:2025-08-14.
[26] M.Abadi,P.Barham,J.Chen,Z.Chen,A.Davis,J.Dean,M.Devin,
[48] JFrogLtd.,“SoftwareSupplyChainSolutionsforDevOpsandSecu-
S. Ghemawat, G. Irving, M. Isard et al., “TensorFlow: a system rity—JFrog,”https://jfrog.com/,accessed:2025-08-22.
| for Large-Scale |     | machine | learning,” | in  | 12th USENIX |     | symposium on |     |     |     |     |     |     |     |
| --------------- | --- | ------- | ---------- | --- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
operating systems design and implementation (OSDI 16), 2016, pp. [49] PyTorchFoundation,“PyTorchHub—Documentation,”https://docs.
265–283. pytorch.org/docs/stable/hub.html,2025,accessed:2025-08-14.
[27] TensorFlow Developers, “SavedModel format guide — Ten- [50] S. Morgan, “4M Models Scanned: Protect AI + Hugging Face 6
sorFlow documentation,” https://www.tensorflow.org/guide/saved MonthsIn,”https://huggingface.co/blog/pai-6-month,April2025,ac-
| model,2024,accessed:2025-08-17. |     |     |     |     |     |     |     | cessed:2025-08-20. |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |

Ethics Considerations
| [51] TensorFlow                                           | Security | Team, | “TensorFlow |     | Security Policy,” | https:// |     |     |     |     |     |     |     |     |
| --------------------------------------------------------- | -------- | ----- | ----------- | --- | ----------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| github.com/tensorflow/tensorflow/blob/master/SECURITY.md, |          |       |             |     |                   | 2025,    |     |     |     |     |     |     |     |     |
accessed:2025-08-18. This research systematizes and empirically evaluates
[52] A. Polkovnichenko, “Is TensorFlow Keras “Safe Mode” risksassociatedwithloadingMLmodelsacrosswidelyused
Actually Safe? Bypassing safe mode Mitigation to Achieve frameworksandhubs.Thestakeholdersforthisresearchin-
Arbitrary Code Execution,” https://jfrog.com/blog/keras-safe cludeMLpractitionersandresearcherswholoadpre-trained
mode-bypass-vulnerability/,March2025,accessed:2025-08-17.
models;frameworkdevelopersandmaintainers;modelhubs
[53] CVEProgram,“CVE-2025-9906,”https://www.cve.org/CVERecord?
andpackagerepositories;andsecurityresearchers.Endusers
id=CVE-2025-9906,2025,accessed:2025-09-19.
|     |     |     |     |     |     |     | and society | at large | are | only | indirectly | impacted. |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ---- | ---------- | --------- | --- | --- |
[54] GoogleSecurityTeam,“PrivateCommunication,”2025,regardingthe Each vulnerability listed in this work was disclosed
disclosureofKerasvulnerabilities. and discussed with the relevant maintainers in accordance
[55] CVEProgram,“CVE-2025-9905,”https://www.cve.org/CVERecord?
|     |     |     |     |     |     |     | with their | disclosure | guidelines, |     | and | we collaborated |     | with |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ----------- | --- | --- | --------------- | --- | ---- |
id=CVE-2025-9905,2025,accessed:2025-09-19.
|     |     |     |     |     |     |     | them to design |     | and validate |     | effective | mitigations. |     | Misuse |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | --------- | ------------ | --- | ------ |
[56] ——, “CVE-2025-54413,” https://www.cve.org/CVERecord?id= potentials have been mitigated through coordinated disclo-
CVE-2025-54413,2025,accessed:2025-07-30. sure,includingdelayingthepublicreleaseofanypotentially
exploit-enablingdetailsuntilatimelinecoordinatedwiththe
| [57] ——, | “CVE-2025-54412,” |     |     | https://www.cve.org/CVERecord?id= |     |     |     |     |     |     |     |     |     |     |
| -------- | ----------------- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CVE-2025-54412,2025,accessed:2025-07-30.
|     |     |     |     |     |     |     | relevant maintainers |     | and | security | teams. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | -------- | ------ | --- | --- | --- |
[58] skops developers, “Model Cards for scikit-learn — skops 0.11 doc- For experiments involving the Hugging Face Hub, we
umentation,” https://skops.readthedocs.io/en/stable/model card.html, obtained explicit permission to upload research models for
2025,accessed:2025-07-30. security testing (“if this is for security and research pur-
[59] CVE Program, “CVE-2025-54886,” https://www.cve.org/ poses, we grant you permission to upload your models.
CVERecord?id=CVE-2025-54886,2025,accessed:2025-08-17. Please let us know if you found anything interesting.”).
[60] Protect AI, “Guardian — AI Model Security with Zero Compro- For the survey we conducted, participation has been totally
mises,”https://protectai.com/guardian,2025,accessed:2025-08-25. voluntary by design, and participants were informed appro-
[61] ProtectAI, “Understanding Model Threats,” https://protectai.com/ priately about the intended use of the results. Sensitive data
insights/knowledge-base/deserialization-threats/PAIT-ARV-100, risks related to our survey were minimized by conducting it
2025,accessed:2025-08-22. anonymously, avoiding the collection of personally identifi-
[62] F.Wilcoxon,“Individualcomparisonsbyrankingmethods,”Biomet- able information, and adhering to applicable laws, platform
ricsbulletin,vol.1,no.6,pp.80–83,1945.
|     |     |     |     |     |     |     | terms, and | community |     | norms. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | ------ | --- | --- | --- | --- |
[63] A. Souri and R. Hosseini, “A state-of-the-art survey of malware Toensuretransparency,weprivatelysharedthecomplete
detection approaches using data mining techniques,” Human-centric preprint version of this paper with all vendors affected
ComputingandInformationSciences,vol.8,no.1,pp.1–22,2018. by the discovered vulnerabilities or directly examined in
[64] E. Lau and Z. Peterson, “A Research Framework and Initial Study our study, so that they were informed before any broader
| of Browser | Security | for | the Visually | Impaired,” | in  | 32nd USENIX |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ------------ | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
dissemination.Thisstepextendedbeyondthevulnerabilities
| SecuritySymposium(USENIXSecurity23). |      |       |     |            | Anaheim,CA:USENIX |            |                |         |           |       |             |        |            |          |
| ------------------------------------ | ---- | ----- | --- | ---------- | ----------------- | ---------- | -------------- | ------- | --------- | ----- | ----------- | ------ | ---------- | -------- |
|                                      |      |       |     |            |                   |            | and findings   | already | disclosed |       | responsibly |        | and        | involved |
| Association,                         | Aug. | 2023, | pp. | 4679–4696. | [Online].         | Available: |                |         |           |       |             |        |            |          |
|                                      |      |       |     |            |                   |            | Google, Keras, |         | Hugging   | Face, | and         | Skops. | We engaged | in       |
https://www.usenix.org/conference/usenixsecurity23/presentation/lau
constructivediscussionswhenneededoruponrequest,while
| [65] N. Narsil, | L.  | Liu, | L. Tunstall, | E.  | Beeching, | N. Lambert, |     |     |     |     |     |     |     |     |
| --------------- | --- | ---- | ------------ | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
and C. Delangue, “safetensors,” 11 2022. [Online]. Available: maintaining full independence in the research process.
https://github.com/huggingface/safetensors
|     |     |     |     |     |     |     | LLM usage | considerations |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | --- | --- | --- | --- | --- | --- |
[66] CVEProgram,“CVE-2024-3660,”https://www.cve.org/CVERecord?
id=CVE-2024-3660,2024,accessed:2025-08-17.
|     |     |     |     |     |     |     | LLMs | were | used | for | editorial | purposes |     | in this |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ---- | --- | --------- | -------- | --- | ------- |
[67] J.Havrilla,A.Householder,A.Kompanek,andB.Koo,“VU#253266
- Keras 2 Lambda Layers Allow Arbitrary Code Injection in Ten- manuscript, and all outputs were inspected by the authors
sorFlowModels,”https://kb.cert.org/vuls/id/253266,April2024,last to ensure accuracy and originality.
Revised:2024-04-18,Accessed:2025-08-17.
|          |          |                   |     |     |                      |     | Appendix | A.  |     |     |     |     |     |     |
| -------- | -------- | ----------------- | --- | --- | -------------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| [68] CVE | Program, | “CVE-2021-37678,” |     |     | https://www.cve.org/ |     |          |     |     |     |     |     |     |     |
CVERecord?id=CVE-2021-37678,2021,accessed:2025-08-19. Prior CVEs on Keras and Skops
| [69] Franc¸ois                            | Chollet, |     | “Disallow                                   | pickle | loading | in npz |                |       |      |           |               |          |          |      |
| ----------------------------------------- | -------- | --- | ------------------------------------------- | ------ | ------- | ------ | -------------- | ----- | ---- | --------- | ------------- | -------- | -------- | ---- |
| files,”                                   |          |     | https://github.com/keras-team/keras/commit/ |        |         |        |                |       |      |           |               |          |          |      |
|                                           |          |     |                                             |        |         |        | We review      | the   | CVEs | disclosed |               | prior to | our work | con- |
| 57c94f305c0b0347ed02b11535623a8b375eee5f, |          |     |                                             |        | January | 2025,  |                |       |      |           |               |          |          |      |
|                                           |          |     |                                             |        |         |        | cerning either | Keras | or   | Skops     | model-sharing |          | methods. | Our  |
gitHubcommit.Accessed:2025-08-17.
|             |            |       |       |          |                          |     | search included |     | both the | official | CVE | database | (https://cve. |     |
| ----------- | ---------- | ----- | ----- | -------- | ------------------------ | --- | --------------- | --- | -------- | -------- | --- | -------- | ------------- | --- |
| [70] huntr, | “Malicious | Keras | Model | Leads to | RCE,” https://huntr.com/ |     |                 |     |          |          |     |          |               |     |
bounties/a3ea601c-f904-4e06-a03e-deb9ff2aa8be, February 2024, org), using keywords such as ”keras” and ”skops”, and the
accessed:2025-08-17. GitHub Security Advisory pages of the respective projects.
|          |          |                   |     |     |                      |     | No filters | were applied    |     | to the | publication | time | frame.        |     |
| -------- | -------- | ----------------- | --- | --- | -------------------- | --- | ---------- | --------------- | --- | ------ | ----------- | ---- | ------------- | --- |
| [71] CVE | Program, | “CVE-2024-37065,” |     |     | https://www.cve.org/ |     |            |                 |     |        |             |      |               |     |
|          |          |                   |     |     |                      |     | Before     | the publication |     | of     | the first   | CVE  | we identified |     |
CVERecord?id=CVE-2024-37065,2024,accessed:2025-08-17.
|                 |        |               |     |          |                          |     | (KV.1) for | Keras, | the most | recent | CVE | related | to  | its model |
| --------------- | ------ | ------------- | --- | -------- | ------------------------ | --- | ---------- | ------ | -------- | ------ | --- | ------- | --- | --------- |
| [72] K. Schulz, | “Skops | Vulnerability |     | Report,” | https://hiddenlayer.com/ |     |            |        |          |        |     |         |     |           |
sai-security-advisory/2024-06-skops,June2024,accessed:2025-08- persistence was CVE-2024-3660 [66]. This vulnerabil-
17. ity enabled arbitrary code execution during model loading

3.9.0 2.15.0 2.13.1 2.11.0 2.12.0 2.10.0 2.14.0
Version (x.y.z)
stnuoC
daolnwoD
{
"module": "subprocess",
"class_name": "run",
"inbound_nodes": [
{
"args":[
3.7M "/bin/sh"
],
"kwargs":{
1.1M 0.9M 0.8M 0.8M 0.6M 0.5M
}
}
]
Figure 2: Download statistics of Keras versions between
}
March 5, 2025, and March 26, 2025 (only versions with
>500k downloads). Listing 1: Simplified malicious config.json snippet for
KV.1. Keras interprets subprocess.run as a model
layer. Arguments are passed via inbound_nodes, which
in versions of Keras prior to 2.13, which was released define input–output relations within Keras’s model compu-
in March 2023. The root cause was the absence of the tation graph.
safe_mode flag (introduced only in Keras 2.13) and the
unrestricted nature of the Lambda layers in the default {
"module":"keras.layers",
model formats used at the time (HDF5), which allowed
"class_name": "Lambda",
deserializationofarbitraryPythoncode[67].Theonlyother "config":{
CVE related to model loading published before our work "name": "set_global_state",
was CVE-2021-37678 [68], which affected a YAML- "function":{
"module": "keras.src.backend.common.glob
based format that is no longer applicable, as it was depre- ⌋
catedfollowingthatdisclosure.Notably,noCVEshadbeen " (cid:44)→ cla a s l s _ _ s n t a a m t e e " " : , "function",
assigned to the .keras format or to safe_mode, and "config": "set_global_attribute",
Keras’sGitHubSecurityAdvisorypagelistednoadvisories. "registered_name": "function"
},
Interestingly, analysis of Keras’s changelog and commit
"arguments":{
history reveals silent fixes for security-relevant issues in-
"value": false
volvingsafe_modeandnotaccompaniedbyadvisoriesor }
CVEassignments.Onesuchcaseiscommit57c94f3[69] },
"name": "set_global_state",
from January 2025, which addresses the insecure use of
"inbound_nodes":[
numpy.loadwithallow_pickle=Truewhenloading
{
weightsfrom.npzfiles—ararelyusedbutsupportedalter- "args":[
native to HDF5. Although this issue was reported earlier on ],
"kwargs":{
bug bounty platforms (e.g., Huntr) [70] in February 2024,
"inputs": "safe_mode_saving"
it appears to have been rejected at the time.
}
Similarly, for Skops, we found only one prior CVE: }
CVE-2024-37065 [71]. This vulnerability allowed ar- ]
bitrary code execution when using the now-deprecated }
trusted=True flag. Importantly, this setting was used Listing 2: Partial malicious config.json snippet for
internally within parts of the Skops codebase, such as the KV.2. A Lambda layer is abused to disable safe mode via
update CLI tool, potentially exposing users even if they did set_global_attribute("safe_mode_saving",
notexplicitlyenableit[72].Beyondthis,wefoundnoother value=False). Arguments are passed through both the
vulnerabilities or advisories disclosed publicly. top-level inbound_nodes key and the arguments key
within the Lambda layer configuration.
Appendix B.
Legacy Version Adoption Rate in Keras
Figure 2 presents the most downloaded Keras versions
between March 5, 2025 (the release date of version 3.9.0),
We analyzed PyPI download statistics for Keras over
and March 26, 2025 (the day before the release of version
time, following the release of version 3.9.0, which included
3.9.1). This represents the most favorable time window for
critical security fixes. While this is not intended to be an
the adoption of version 3.9.0, which was, as expected, the
exhaustive study, which would be outside the scope of this
most downloaded release. However, surprisingly, it was fol-
work, our intent is to give a hint at the adoption rate of
lowedbytwoversionsfrom2023:2.15.0(1.1milliondown-
newer versions. The statistics were collected from Google
loads) and 2.13.1 (900,000 downloads). No other version
Cloud Public Datasets and queried using BigQuery. We
in the 3.x.x series received more than 500,000 downloads
made the queries, raw data, and scripts used to generate
during this period and is therefore not shown in the plot.
the plot publicly available.

{
|               |     |               |     |     |     |     | Appendix    |     | C.  |     |     |     |     |     |
| ------------- | --- | ------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| "__class__":  |     | "int",        |     |     |     |     |             |     |     |     |     |     |     |     |
| "__module__": |     | "builtins",   |     |     |     |     | Meta-Review |     |     |     |     |     |     |     |
| "__loader__": |     | "MethodNode", |     |     |     |     |             |     |     |     |     |     |     |     |
"content":{
|     | "obj":{ |     |     |     |     |     | Thefollowingmeta-reviewwaspreparedbytheprogram |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
"__class__": "int", committee for the 2026 IEEE Symposium on Security and
"__module__": "builtins", Privacy (S&P) as part of the review process as detailed in
|     | "__loader__": |     | "MethodNode", |     |     |     | the call | for | papers. |     |     |     |     |     |
| --- | ------------- | --- | ------------- | --- | --- | --- | -------- | --- | ------- | --- | --- | --- | --- | --- |
"content":{
"obj":{
|     |     | "__class__": | "QuadraticDiscriminan |     |     |     | C.1. | Summary |     |     |     |     |     |     |
| --- | --- | ------------ | --------------------- | --- | --- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- |
⌋
tAnalysis",
(cid:44)→
|     |     | "__module__": | "sklearn.discriminan |     |     |     |     |       |              |              |     |         |           |     |
| --- | --- | ------------- | -------------------- | --- | --- | --- | --- | ----- | ------------ | ------------ | --- | ------- | --------- | --- |
|     |     |               |                      |     |     | ⌋   | The | paper | investigates | supply-chain |     | attacks | targeting |     |
|     |     | (cid:44)→     | t _a na l y s is ",  |     |     |     |     |       |              |              |     |         |           |     |
" __lo a de r_ _ " ML model-loading workflows. It considers a scenario in
: " ObjectNode",
"__id__": 1 which an adversary maliciously manipulates a model to
|     |     | },      |                     |     |     |     | trigger | arbitrary | code          | execution | when       | it is | loaded | by a  |
| --- | --- | ------- | ------------------- | --- | --- | --- | ------- | --------- | ------------- | --------- | ---------- | ----- | ------ | ----- |
|     |     | "func": | "decision_function" |     |     |     |         |           |               |           |            |       |        |       |
|     |     |         |                     |     |     |     | victim. | The       | paper surveys | security  | mechanisms |       | for    | model |
}
|     |     |     |     |     |     |     | loading | in popular | ML  | frameworks |     | and model | hubs, | con- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ---------- | --- | --------- | ----- | ---- |
},
"func": "__builtins__" ductsamanualvulnerabilityassessmentofsecurity-oriented
| }   |     |     |     |     |     |     | features, | and | evaluates | user | perceptions | of  | model-loading |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------- | ---- | ----------- | --- | ------------- | --- |
}
|     |     |     |     |     |     |     | safety. | The | analysis uncovers |     | multiple | vulnerabilities |     | in  |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----------------- | --- | -------- | --------------- | --- | --- |
Listing 3: Malicious schema.json snippet for SV.1. Keras’s safe mode and Hugging Face’s model scanning
mechanisms.
| QuadraticDiscriminantAnalysis |          |             |     |              | from Scikit- |     |     |     |     |     |     |     |     |     |
| ----------------------------- | -------- | ----------- | --- | ------------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| learn                         | (trusted | by default) | is  | instantiated | using        | an  |     |     |     |     |     |     |     |     |
ObjectNode. Then, a first MethodNode accesses C.2. Scientific Contributions
| its decision_function |     |     | method | and | a second |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MethodNode __builtins__ Identifies an Impactful Vulnerability.
|     |     | retrieves | the |     | dictionary, |     | •   |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bypassing Skops’ checks. • Provides a Valuable Step Forward in an Established
Field.
| {            |     |         |     |     |     |     | C.3. | Reasons | for Acceptance |     |     |     |     |     |
| ------------ | --- | ------- | --- | --- | --- | --- | ---- | ------- | -------------- | --- | --- | --- | --- | --- |
| "__class__": |     | "call", |     |     |     |     |      |         |                |     |     |     |     |     |
"__module__": "sklearn.SGDRegressor", 1) The paper provides a systematic survey that highlights
| "__loader__": |     | "OperatorFuncNode" |     |     |     |     |     |                                                   |            |     |     |     |     |     |
| ------------- | --- | ------------------ | --- | --- | --- | --- | --- | ------------------------------------------------- | ---------- | --- | --- | --- | --- | --- |
| }             |     |                    |     |     |     |     |     | thefragmentationandlackofstandardizationincurrent |            |     |     |     |     |     |
|               |     |                    |     |     |     |     |     | model-sharing                                     | practices. |     |     |     |     |     |
Listing 4: Malicious schema.json snip- 2) It identifies multiple exploits in secure loading modes,
pet for SV.2. The validated type string is raising serious concerns about the effectiveness of ex-
| sklearn.SGDRegressor.call, |                   |        |               | which    | may appear  |     |     |                   |     |               |     |                  |     |     |
| -------------------------- | ----------------- | ------ | ------------- | -------- | ----------- | --- | --- | ----------------- | --- | ------------- | --- | ---------------- | --- | --- |
|                            |                   |        |               |          |             |     |     | isting safeguards | in  | model-sharing |     | infrastructures. |     |     |
| benign                     | and related       | to the | target model, | but what | is actually |     |     |                   |     |               |     |                  |     |     |
| invoked                    | is operator.call. |        |               |          |             |     |     |                   |     |               |     |                  |     |     |
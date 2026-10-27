# Awesome Egocentric Streaming Video Understanding

![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)

> **First-person video, one moment at a time.** A protocol-aware reading list for continuous egocentric understanding: what is happening, what remains true, what matters to this wearer, which utterance grounds to which entity, when to speak, and what to do next.

**Status:** Community-curated reading list, not an exhaustive survey. Entries were checked against author papers or project pages on **2026-10-27**. This is **not** an independent code reproduction or latency audit.

[Research taxonomy](docs/TAXONOMY.md) · [Evaluation protocol](docs/PROTOCOL.md) · [Open questions](docs/RESEARCH_GAPS.md) · [中文指南](docs/README.zh-CN.md) · [Contribute](CONTRIBUTING.md)

Entry tables follow the date / venue / contribution format of [Awesome-Streaming-Video-Understanding](https://github.com/sotayang/Awesome-Streaming-Video-Understanding). The six questions below are the categories of **this** list. That repository's trigger and memory-mechanism taxonomy is not copied here.

## News

- **[2026.10]** Literature pass on 2026-10-27. Added core work on grounded streaming recall, cross-session memory, proactive memory, spoken intervention, and online mistake detection, plus related work whose first-person or causal-streaming evidence is still incomplete. Regenerated the paper tables in the streaming-awesome format. The six research questions are unchanged.

## Overview

The question is not only whether a video is long. It is whether an assistant can **observe causally, keep useful state, answer or act at the right moment, and adapt to a specific wearer**.

General streaming work has two recurring pressures: deciding **when** to speak, and sustaining **memory and compute** as the stream grows. This list asks those pressures inside first-person video, and it keeps three claims separate:

1. **Egocentric capture** — where the camera was.
2. **Causal streaming** — which frames and audio existed at the moment of the decision.
3. **Real-time feasibility** — whether latency and memory fit the rate at which frames arrive.

A wearable recording is not a causal evaluation. A causal evaluation is not 30 FPS, or even 1 FPS. An offline model that reads a multi-day video in one pass is not streaming. When a paper is ambiguous, the entry says so.

### Table of contents

- [News](#news)
- [Overview](#overview)
- [Research questions](#research-questions)
- [Curated papers](#curated-papers)
- [Release index](#release-index)
- [Systems and architectures](#systems-and-architectures)
- [Benchmarks and datasets](#benchmarks-and-datasets)
- [Foundational and adjacent collections](#foundational-and-adjacent-collections)
- [Maintain and contribute](#maintain-and-contribute)
- [Attribution and licensing](#attribution-and-licensing)

## Research questions

| Capability | Question |
| --- | --- |
| Online perception | What is unfolding now? |
| Episodic memory | What happened, what changed, and what remains valid? |
| Personalized understanding | What information matters to this particular wearer? |
| Cross-modal grounding | Which observed entity does an utterance refer to? |
| Proactive assistance | Should the agent remain silent, answer, or intervene now? |
| Embodied anticipation | What will happen next, and which action is appropriate? |

Each paper has **one** primary question. Mechanisms such as event memory, KV-cache policy, retrieval, or a silence token are notes inside the contribution, not extra top-level tasks. Definitions and evidence grades: [taxonomy](docs/TAXONOMY.md).

## Curated papers

_Edit `data/papers.json`, then run `python scripts/build_readme.py` to refresh everything between the markers._

<!-- PAPERS:START -->
_Curated entries: **27** · Core: **17** · Related: **10**. Literature pass: **2026-10-27**. Streaming labels follow author-described evidence and are not an independent latency audit. A missing code, project, or data link means **not recorded**._

Interaction type, memory horizon, and audio role stay in [`data/papers.json`](data/papers.json) so this table can stay readable.

### Core papers

First-person visual input, an author-described online or causal protocol, and an understanding, memory, reasoning, or interaction task.

#### Online Perception & Understanding

*What is unfolding now, using only the observation available at this moment?*

| Paper | Work | Date | Venue | Streaming evidence | Method / Key Contribution | Resources |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [EgoRecall: 3D Visual Grounding from Streaming Egocentric Observations](https://3dlg-hcvc.github.io/EgoRecall/) | EgoRecall | 2026/09 | Preprint | Causal streaming (paper-described) | **Ground the phrase from the walk so far**: A referring expression is resolved in 3D using only the egocentric views available at the query time, including objects that have left the frame. | [Data](https://huggingface.co/datasets/3dlg-hcvc/EgoRecall) |
| [EgoSAT: A Comprehensive Benchmark of Egocentric Streaming Interaction Understanding](https://arxiv.org/abs/2606.24422) | EgoSAT | 2026/06 | ECCV 2026 | Causal streaming (paper-described) | **Past-only interaction reasoning**: Retrospective, ongoing, and prospective questions share one benchmark, and each query may use only frames observed so far. | [Project](https://leiyj23.github.io/EgoSAT/) |


#### Continuous Memory & Long-Horizon Reasoning

*What happened, what changed, and which past state is still valid?*

| Paper | Work | Date | Venue | Streaming evidence | Method / Key Contribution | Resources |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [APM-Bench: Benchmarking cross-Session Persistent Memory for Real-World Egocentric Streaming Video Assistants](https://arxiv.org/abs/2609.37559) | APM-Bench | 2026/09 | arXiv | Online/continuous (author-described) | **Memory that survives interruptions**: Sessions in one life trajectory stop and resume, so the assistant must store, reuse, and admit missing evidence instead of rereading one continuous file. | [Code](https://github.com/Jianguo-Huang11/APM-Bench) · [Project](https://jianguo-huang11.github.io/APM-Bench/) |
| [LightMem-Ego: Your AI Memory for Everyday Life](https://arxiv.org/abs/2607.11487) | LightMem-Ego | 2026/07 | arXiv | Online/continuous (author-described) | **Three speeds of wearable memory**: Egocentric video and audio share one timeline and are split into current, short-term, and long-term stores before a query is answered. | [Code](https://github.com/zjunlp/LightMem-Ego) |
| [S-EMBER: A Large-Scale Benchmark for Streaming Egocentric Memory Retrieval](https://arxiv.org/abs/2607.02689) | S-EMBER | 2026/07 | arXiv | Causal streaming (paper-described) | **Grounded causal recall**: On 388 hours of smart-glasses video, an answer must use only frames from before the query time and point to a supporting interval. | [Code](https://github.com/facebookresearch/S-EMBER) · [Data](https://huggingface.co/datasets/facebook/S-EMBER) |
| [Keep It in Mind: User-Centric Continual Spatial Intelligence Reasoning in Egocentric Video Streams](https://arxiv.org/abs/2606.15200) | UCS-Bench | 2026/06 | ICML 2026 | Online/continuous (author-described) | **Spatial memory that moves with the wearer**: DirectMe updates a structured map from the first-person stream so later questions can recover where objects were after the camera has moved. | [Code](https://github.com/cocowy1/UCS-Bench) |
| [EGOSTREAM: A Diagnostic Benchmark for Streaming Episodic Memory in Egocentric Vision](https://arxiv.org/abs/2605.31557) | EgoStream | 2026/05 | NeurIPS 2026 | Causal streaming (paper-described) | **Answer validity windows**: Recall is scored across time so that model forgetting can be separated from answers that stop being true as the scene changes. | [Project](https://saroo25.github.io/Egostream/) |
| [TeleEgo: Benchmarking Egocentric AI Assistants in the Wild](https://arxiv.org/abs/2510.23981) | TeleEgo | 2025/10 | arXiv | Online/continuous (author-described) | **Right answer, inside the window**: Long in-the-wild egocentric streams are scored with real-time accuracy and a memory-persistence measure across recall, current understanding, and cross-event reasoning. | [Code](https://github.com/TeleAI-UAGI/TeleEgo) |


#### Personalized & User-Centric Understanding

*What should be remembered because it matters to this wearer, not to a generic user?*

_No curated core entry yet._

#### Streaming Audio-Visual Understanding

*Which observed entity or event does an utterance refer to?*

_No curated core entry yet._

#### Proactive Assistance & Situated Interaction

*Should the assistant stay silent, answer, or intervene now?*

| Paper | Work | Date | Venue | Streaming evidence | Method / Key Contribution | Resources |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [EgoVoice: Proactive Spoken Assistance from Egocentric Multimodal Streams](https://arxiv.org/abs/2610.12248) | EgoVoice | 2026/10 | EMNLP 2026 | Online/continuous (author-described) | **Speak, or stay quiet, in voice**: At each moment of a first-person video and audio stream the model either remains silent or gives spoken guidance without being asked. | [Project](https://egocentricvoice.github.io/) |
| [ProactEgoMem: Benchmarking Proactive Memory in Streaming Egocentric Video](https://arxiv.org/abs/2610.30089) | ProactEgoMem | 2026/10 | arXiv | Online/continuous (author-described) | **Remember without being asked**: The assistant has to notice transient details, object-state changes, and moves in time, from one notification up to a memory tool it starts and stops itself. | [Code](https://github.com/mayhugotong/ProactEgoMem) · [Project](https://proactegomem.github.io/) |
| [Vinci2: Providing Proactive Assistance in Continuous Egocentric Videos](https://arxiv.org/abs/2607.11523) | Vinci2 | 2026/07 | ECCV 2026 | Online/continuous (author-described) | **Intervene or stay silent**: Links a changing wearer context and retrieved memory to the decision of whether assistance should happen now. | [Project](https://sitonggong.github.io/EgoServe-page/) |
| [Plan, Watch, Recover: A Benchmark and Architectures for Proactive Procedural Assistance](https://arxiv.org/abs/2606.04970) | PWR | 2026/06 | arXiv | Online/continuous (author-described) | **When to interrupt, and how to recover**: Estimates procedural state from wearable video, decides whether to coach, and supplies a way back when the wearer leaves the plan. | [Code / Data](https://huggingface.co/datasets/facebook/wearable-ai) |
| [Eyes Wide Open: Ego Proactive Video-LLM for Streaming Video](https://arxiv.org/abs/2510.14560) | VideoLLM-EyeWO | 2025/10 | NeurIPS 2025 | Online/continuous (author-described) | **Just-in-time proactive QA**: Scores both the answer and whether it is issued at the moment it becomes appropriate on an egocentric stream. | [Code](https://github.com/SooLab/EyeWO) · [Project](https://zhangyl4.github.io/publications/eyes-wide-open/) |
| [Proactive Assistant Dialogue Generation from Streaming Egocentric Videos](https://arxiv.org/abs/2506.05904) | ProAssist | 2025/06 | EMNLP 2025 | Online/continuous (author-described) | **Streaming procedural dialogue**: Generates guidance from egocentric video and can remain silent until a step needs help. | [Code](https://github.com/pro-assist/ProAssist) · [Project](https://pro-assist.github.io/) |
| [EgoSpeak: Learning When to Speak for Egocentric Conversational Agents in the Wild](https://arxiv.org/abs/2502.14892) | EgoSpeak | 2025/02 | NAACL 2025 | Online/continuous (author-described) | **When a first-person agent should start talking**: Predicts speech initiation online from untrimmed egocentric video, before any user question has been asked. | [Code](https://github.com/jun297/EgoSpeak) |


#### Anticipation, Planning & Embodied Reasoning

*What happens next, and which action or correction is appropriate?*

| Paper | Work | Date | Venue | Streaming evidence | Method / Key Contribution | Resources |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [PROVIA: Procedure State Tracking for Online Mistake Detection in Egocentric Videos](https://arxiv.org/abs/2609.20638) | PROVIA | 2026/09 | arXiv | Causal streaming (paper-described) | **An alarm from past frames only**: Procedure state is tracked causally, a mistake can be flagged before the next step, and the tracker continues after the person recovers. | [Code](https://github.com/Kratos-Wen/PROVIA) |
| [PREGO: Online Mistake Detection in PRocedural EGOcentric Videos](https://arxiv.org/abs/2404.01933) | PREGO | 2024/04 | CVPR 2024 | Causal streaming (paper-described) | **Expected next step versus the step just seen**: An online recognizer reads frames up to time t and a language model predicts the next step from earlier steps, so an unseen mistake is a mismatch. | [Code](https://github.com/aleflabo/PREGO) |


### Related papers

These papers inform the research agenda, but first-person capture and a causal streaming protocol are not both established.

#### Online Perception & Understanding

*What is unfolding now, using only the observation available at this moment?*

| Paper | Work | Date | Venue | Streaming evidence | Method / Key Contribution | Resources |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [VideoLLM-online: Online Video Large Language Model for Streaming Video](https://arxiv.org/abs/2406.11816) | VideoLLM-online | 2024/06 | CVPR 2024 | Online/continuous (author-described) | **Silence token on a live narration stream**: The model learns to speak or stay silent as frames arrive, and Ego4D narration is a main streaming test, but the model is not egocentric-only. | [Code](https://github.com/showlab/VideoLLM-online) · [Project](https://showlab.github.io/videollm-online/) |


#### Continuous Memory & Long-Horizon Reasoning

*What happened, what changed, and which past state is still valid?*

| Paper | Work | Date | Venue | Streaming evidence | Method / Key Contribution | Resources |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [StreamArena: Toward Continuous, Interactive, and Long-Horizon Agentic Streaming Video Understanding](https://arxiv.org/abs/2608.05703) | StreamArena | 2026/08 | arXiv | Online/continuous (author-described) | **Recent frames are not long memory**: On hour-scale videos, keeping only the latest frames misses distant events, which is a useful control even though the videos are not first-person. | — |
| [EgoMemReason: A Memory-Driven Reasoning Benchmark for Long-Horizon Egocentric Video Understanding](https://arxiv.org/abs/2605.09874) | EgoMemReason | 2026/05 | COLM 2026 | Streaming evaluation not verified | **Long-horizon memory without a streaming audit**: Useful for telling multi-day egocentric reasoning apart from a causal online evaluation. | [Code](https://github.com/Ziyang412/EgoMemReason) · [Project](https://egomemreason.github.io/) |
| [Evaluating Memory Capability in Continuous Lifelog Scenario](https://arxiv.org/abs/2604.11182) | LifeDialBench | 2026/04 | ACL 2026 Findings | Online/continuous (author-described) | **No future session in the answer**: Memory is frozen before each query on dialogue lifelogs, including an EgoLife-derived subset, but the evaluated stream is text rather than raw frames. | [Code](https://github.com/RayNeo-AI-2025/LifeDialBench) |
| [EgoLife: Towards Egocentric Life Assistant](https://arxiv.org/abs/2503.03803) | EgoLife | 2025/03 | CVPR 2025 | Streaming evaluation not verified | **A recorded week of wearable life**: Six people wear glasses for a week so an assistant can recall events and habits; the original benchmark is long-context assistance, not a verified causal stream. | [Code](https://github.com/EvolvingLMMs-Lab/EgoLife) · [Project](https://egolife-ai.github.io/) |


#### Personalized & User-Centric Understanding

*What should be remembered because it matters to this wearer, not to a generic user?*

| Paper | Work | Date | Venue | Streaming evidence | Method / Key Contribution | Resources |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [EgoSelf: From Memory to Personalized Egocentric Assistant](https://arxiv.org/abs/2604.19564) | EgoSelf | 2026/04 | arXiv | Streaming evaluation not verified | **A graph of this person's habits**: Past egocentric interactions become a user-specific profile that predicts future interactions; a causal frame-by-frame protocol is not established. | [Project](https://abie-e.github.io/EgoSelf/) |
| [EgoMem: Lifelong Memory Agent for Full-duplex Omnimodal Models](https://arxiv.org/abs/2509.11914) | EgoMem | 2025/09 | arXiv | Online/continuous (author-described) | **Facts, preferences, and relationships from the live stream**: A full-duplex model recognizes people and updates long-term user knowledge without a separate text memory log. | — |


#### Streaming Audio-Visual Understanding

*Which observed entity or event does an utterance refer to?*

| Paper | Work | Date | Venue | Streaming evidence | Method / Key Contribution | Resources |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Listening with the Eyes: Benchmarking Egocentric Co-Speech Grounding across Space and Time](https://arxiv.org/abs/2603.07966) | EcoG-Bench | 2026/03 | arXiv | Streaming evaluation not verified | **What, where, and when for the word that**: A deictic command is executable only if speech is bound to the pointing stroke, which is the grounding question even though the clips are not an ongoing stream. | — |
| [EgoAVU: Egocentric Audio-Visual Understanding](https://arxiv.org/abs/2602.06139) | EgoAVU | 2026/02 | CVPR 2026 | Streaming evaluation not verified | **Tie the sound to the visible action**: Large-scale egocentric narrations and questions test whether a model uses audio instead of answering from vision alone; a causal streaming protocol is not established. | [Code](https://github.com/facebookresearch/EgoAVU) · [Project](https://cs20s030.github.io/EgoAVU/) |


#### Anticipation, Planning & Embodied Reasoning

*What happens next, and which action or correction is appropriate?*

| Paper | Work | Date | Venue | Streaming evidence | Method / Key Contribution | Resources |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Intention-Guided Cognitive Reasoning for Egocentric Long-Term Action Anticipation](https://arxiv.org/abs/2508.01742) | INSIGHT | 2025/08 | AAAI 2026 | Streaming evaluation not verified | **Intention before the next actions**: Hand-object cues and an explicit think-reason-answer step forecast a long egocentric action sequence; frames are not shown to arrive as an always-on stream. | [Code](https://github.com/CorrineQiu/INSIGHT) |


### Release index

Same entries, newest submission month first. Question is the single primary category, not an exhaustive tag set.

| Date | Paper | Work | Tier | Question | Venue |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026/10 | [EgoVoice: Proactive Spoken Assistance from Egocentric Multimodal Streams](https://arxiv.org/abs/2610.12248) | EgoVoice | Core | Proactive Assistance & Situated Interaction | EMNLP 2026 |
| 2026/10 | [ProactEgoMem: Benchmarking Proactive Memory in Streaming Egocentric Video](https://arxiv.org/abs/2610.30089) | ProactEgoMem | Core | Proactive Assistance & Situated Interaction | arXiv |
| 2026/09 | [APM-Bench: Benchmarking cross-Session Persistent Memory for Real-World Egocentric Streaming Video Assistants](https://arxiv.org/abs/2609.37559) | APM-Bench | Core | Continuous Memory & Long-Horizon Reasoning | arXiv |
| 2026/09 | [EgoRecall: 3D Visual Grounding from Streaming Egocentric Observations](https://3dlg-hcvc.github.io/EgoRecall/) | EgoRecall | Core | Online Perception & Understanding | Preprint |
| 2026/09 | [PROVIA: Procedure State Tracking for Online Mistake Detection in Egocentric Videos](https://arxiv.org/abs/2609.20638) | PROVIA | Core | Anticipation, Planning & Embodied Reasoning | arXiv |
| 2026/08 | [StreamArena: Toward Continuous, Interactive, and Long-Horizon Agentic Streaming Video Understanding](https://arxiv.org/abs/2608.05703) | StreamArena | Related | Continuous Memory & Long-Horizon Reasoning | arXiv |
| 2026/07 | [LightMem-Ego: Your AI Memory for Everyday Life](https://arxiv.org/abs/2607.11487) | LightMem-Ego | Core | Continuous Memory & Long-Horizon Reasoning | arXiv |
| 2026/07 | [S-EMBER: A Large-Scale Benchmark for Streaming Egocentric Memory Retrieval](https://arxiv.org/abs/2607.02689) | S-EMBER | Core | Continuous Memory & Long-Horizon Reasoning | arXiv |
| 2026/07 | [Vinci2: Providing Proactive Assistance in Continuous Egocentric Videos](https://arxiv.org/abs/2607.11523) | Vinci2 | Core | Proactive Assistance & Situated Interaction | ECCV 2026 |
| 2026/06 | [EgoSAT: A Comprehensive Benchmark of Egocentric Streaming Interaction Understanding](https://arxiv.org/abs/2606.24422) | EgoSAT | Core | Online Perception & Understanding | ECCV 2026 |
| 2026/06 | [Keep It in Mind: User-Centric Continual Spatial Intelligence Reasoning in Egocentric Video Streams](https://arxiv.org/abs/2606.15200) | UCS-Bench | Core | Continuous Memory & Long-Horizon Reasoning | ICML 2026 |
| 2026/06 | [Plan, Watch, Recover: A Benchmark and Architectures for Proactive Procedural Assistance](https://arxiv.org/abs/2606.04970) | PWR | Core | Proactive Assistance & Situated Interaction | arXiv |
| 2026/05 | [EgoMemReason: A Memory-Driven Reasoning Benchmark for Long-Horizon Egocentric Video Understanding](https://arxiv.org/abs/2605.09874) | EgoMemReason | Related | Continuous Memory & Long-Horizon Reasoning | COLM 2026 |
| 2026/05 | [EGOSTREAM: A Diagnostic Benchmark for Streaming Episodic Memory in Egocentric Vision](https://arxiv.org/abs/2605.31557) | EgoStream | Core | Continuous Memory & Long-Horizon Reasoning | NeurIPS 2026 |
| 2026/04 | [EgoSelf: From Memory to Personalized Egocentric Assistant](https://arxiv.org/abs/2604.19564) | EgoSelf | Related | Personalized & User-Centric Understanding | arXiv |
| 2026/04 | [Evaluating Memory Capability in Continuous Lifelog Scenario](https://arxiv.org/abs/2604.11182) | LifeDialBench | Related | Continuous Memory & Long-Horizon Reasoning | ACL 2026 Findings |
| 2026/03 | [Listening with the Eyes: Benchmarking Egocentric Co-Speech Grounding across Space and Time](https://arxiv.org/abs/2603.07966) | EcoG-Bench | Related | Streaming Audio-Visual Understanding | arXiv |
| 2026/02 | [EgoAVU: Egocentric Audio-Visual Understanding](https://arxiv.org/abs/2602.06139) | EgoAVU | Related | Streaming Audio-Visual Understanding | CVPR 2026 |
| 2025/10 | [Eyes Wide Open: Ego Proactive Video-LLM for Streaming Video](https://arxiv.org/abs/2510.14560) | VideoLLM-EyeWO | Core | Proactive Assistance & Situated Interaction | NeurIPS 2025 |
| 2025/10 | [TeleEgo: Benchmarking Egocentric AI Assistants in the Wild](https://arxiv.org/abs/2510.23981) | TeleEgo | Core | Continuous Memory & Long-Horizon Reasoning | arXiv |
| 2025/09 | [EgoMem: Lifelong Memory Agent for Full-duplex Omnimodal Models](https://arxiv.org/abs/2509.11914) | EgoMem | Related | Personalized & User-Centric Understanding | arXiv |
| 2025/08 | [Intention-Guided Cognitive Reasoning for Egocentric Long-Term Action Anticipation](https://arxiv.org/abs/2508.01742) | INSIGHT | Related | Anticipation, Planning & Embodied Reasoning | AAAI 2026 |
| 2025/06 | [Proactive Assistant Dialogue Generation from Streaming Egocentric Videos](https://arxiv.org/abs/2506.05904) | ProAssist | Core | Proactive Assistance & Situated Interaction | EMNLP 2025 |
| 2025/03 | [EgoLife: Towards Egocentric Life Assistant](https://arxiv.org/abs/2503.03803) | EgoLife | Related | Continuous Memory & Long-Horizon Reasoning | CVPR 2025 |
| 2025/02 | [EgoSpeak: Learning When to Speak for Egocentric Conversational Agents in the Wild](https://arxiv.org/abs/2502.14892) | EgoSpeak | Core | Proactive Assistance & Situated Interaction | NAACL 2025 |
| 2024/06 | [VideoLLM-online: Online Video Large Language Model for Streaming Video](https://arxiv.org/abs/2406.11816) | VideoLLM-online | Related | Online Perception & Understanding | CVPR 2024 |
| 2024/04 | [PREGO: Online Mistake Detection in PRocedural EGOcentric Videos](https://arxiv.org/abs/2404.01933) | PREGO | Core | Anticipation, Planning & Embodied Reasoning | CVPR 2024 |

<!-- PAPERS:END -->

## Systems and architectures

Technical mechanisms are **tags**, not mutually exclusive tasks: structured event memory, entity memory, KV-cache policies, multimodal streaming, retrieval, persistent summaries, efficient inference, and proactive triggering. A later pass can compare memory growth, prefill cost, latency, and causal access constraints. Those comparisons already have a home in [Awesome-Streaming-Video-Understanding](https://github.com/sotayang/Awesome-Streaming-Video-Understanding); this list only records them when they answer one of the six questions on first-person video.

## Benchmarks and datasets

Keep three different objects distinct:

1. **Raw dataset**: is it egocentric, continuous, wearable, audio-enabled, multi-day, and actually downloadable?
2. **Benchmark**: what is the evidence/query timestamp, target task, and leakage policy?
3. **Evaluation harness**: are incoming frames fed incrementally, and can the model retrieve future data or whole-video captions?

See the [evaluation checklist](docs/PROTOCOL.md) before labeling any benchmark as strictly streaming.

## Foundational and adjacent collections

- [Awesome-Streaming-Video-Understanding](https://github.com/sotayang/Awesome-Streaming-Video-Understanding) — online video tasks, models, and benchmarks. This list borrows its table style and does not duplicate its general streaming catalog.
- [Awesome-VLM-Streaming-Video](https://github.com/ydyhello/Awesome-VLM-Streaming-Video) — streaming VLM models and techniques.
- [Awesome Egocentric Vision](https://github.com/Sid2697/awesome-egocentric-vision) — broader first-person vision.
- [Awesome Egocentric Video Datasets](https://github.com/player0718/awesome-ego-video-datasets) — egocentric data and benchmarks.

## Maintain and contribute

Add a paper in `data/papers.json`, then run:

```bash
python scripts/build_readme.py
python scripts/build_readme.py --check
```

Each entry needs a paper link, a `YYYY/MM` date, a short work name, a venue (`arXiv` if no proceedings are recorded), one primary question, a streaming-evidence label, and one research-motivated sentence. Use a bold lead-in for the contribution, in the form `**Name of the idea**: what the work changes.` Empty code, project, and dataset strings mean **unknown**, not absent. Submit a pull request using [CONTRIBUTING.md](CONTRIBUTING.md).

## Attribution and licensing

Paper titles and official URLs point to their respective authors. Individual papers and datasets keep their original licenses. This list does not redistribute videos, datasets, figures, or paper PDFs. Descriptions are written for this repository and are not copied from other awesome lists. Choose and add a repository license before public release.

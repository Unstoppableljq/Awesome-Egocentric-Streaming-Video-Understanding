# Research-first taxonomy

**Organize by questions asked of an online first-person assistant, not solely by paper year or backbone.** Each work receives one primary capability and optional cross-cutting tags; a benchmark and the model tested on it are distinct items.

## Primary capabilities

1. **Online Perception & Understanding** — contemporaneous activity/state/interaction understanding; what is happening now?
2. **Continuous Memory & Long-Horizon Reasoning** — episodic, spatial, causal, social memory and state updates; what happened and what stays relevant?
3. **Personalized & User-Centric Understanding** — wearer-specific habits, preferences, significant people/objects, goals, and durable requests; what matters to this person?
4. **Streaming Audio-Visual Understanding** — sound/video fusion and temporally displaced referential grounding; which observed entity/event does an utterance describe?
5. **Proactive Assistance & Situated Interaction** — whether, when, why, and how to proactively assist; silence vs intervention.
6. **Anticipation, Planning & Embodied Reasoning** — future state, intention, procedural errors, next-action planning, egocentric-to-action transfer.

## Cross-cutting tags (examples)

- Temporal input: strict causal sequential / author-described online / offline long-context / unknown.
- Time horizon: instant / seconds / minutes / hours / days / cross-session.
- Sensor input: video / video + speech transcripts / synchronized raw audio-video / gaze / IMU / unknown.
- Memory representation: none / summaries / structured events / entity store / vector retrieval / KV cache / persistent parameters.
- Interaction: reactive answer / query-conditioned timing / event-conditioned assist / unsolicited need discovery / planning.
- Evaluation artifacts: full video available? future captions? question-agnostic ingestion? online compute and memory reported?

## Three independent properties

1. **Egocentric capture:** where the camera was placed.
2. **Causal streaming:** what data was available at each inference step.
3. **Real-time feasibility:** whether latency and memory meet an actual input-rate budget.

Do not infer one property from another. For instance, a wearable-camera dataset does not imply a causal evaluation; a causal frame-by-frame benchmark does not imply 30 FPS or even 1 FPS throughput.

## Evidence taxonomy

- **Causal streaming (paper-described):** the authors explicitly state an observation cutoff at each query time.
- **Online/continuous (author-described):** sequential or ongoing video is central, but the exact evaluation/read-ahead details need deeper inspection.
- **Streaming evaluation not verified:** long-form/egocentric data relevant to the field, but strict streaming evidence has not been established.
- **Independently reproduced:** reserved for future maintainers with recorded evaluation commands and artifacts (not present in this starter).

# Streaming evaluation protocol checklist

Use this when reviewing a paper or benchmark. Do not apply a strict-online badge unless evidence supports it.

| Audit question | Why it matters |
| --- | --- |
| At time `t`, can the model access frames after `t`? | Future-frame leakage invalidates causal online claims. |
| Are video tokens delivered incrementally or encoded after watching the whole video? | Separates streaming inference from offline video QA. |
| Does query time determine the allowed visual/audio evidence? | Establishes timestamp-causal answerability. |
| Are memories built **before** the question is known? | Distinguishes query-agnostic memory from hindsight-selected highlights. |
| May retrieval/indexing use whole-video captions prepared offline? | Whole-video preprocessing can silently leak future evidence. |
| Are speech timestamps and visual observations synchronized? | Essential to delayed reference and multimodal grounding. |
| How is evidence relevance or answer validity affected by changing objects? | Stale vs valid memories must be distinguished. |
| Is average and tail latency below the frame/segment arrival interval? | Causal streaming is not necessarily real-time processing. |
| Are peak CPU/GPU memory and per-hour memory growth reported? | Always-on systems need bounded or explicitly managed state. |
| Does the benchmark distinguish unsolicited proactive intervention from query-conditioned answer timing? | These are related but not equivalent tasks. |

## Suggested labels

- `causal-streaming-paper-described`: authors state no post-query evidence used; needs reproduction to verify.
- `online-claimed`: described as online/continuous without fully audited future-access details.
- `offline-related`: no strict online evaluation identified; useful comparison only.
- `unknown`: insufficient evidence; do not guess.

## Suggested comparison table (blank template)

| Work | Ego? | Query-agnostic streaming? | Future prohibited? | Memory bounded? | Raw AV? | Proactivity type | Latency reported? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| _Paper_ | ? | ? | ? | ? | ? | ? | ? |

Prefer `?` over unsupported `Yes`/`No`. For author-described claims, record section/page or project link in review notes.

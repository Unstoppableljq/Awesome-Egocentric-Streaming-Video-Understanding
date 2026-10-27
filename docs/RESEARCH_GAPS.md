# Research questions worth tracking

These are **candidate directions**, not claims that no existing paper addresses them.

1. **Personal relevance vs raw recall:** Can a wearer-specific agent distinguish a one-time fact from information that should alter future assistance?
2. **Delayed speech-to-object grounding:** Can the assistant link an utterance to an entity visible minutes or days earlier/later, while having seen only past evidence at each point?
3. **Memory revision and forgetting:** When a user's preference or an object's state changes, can the assistant revise or retire stale memories instead of just accumulating more text?
4. **Unprompted assistance:** Can a model infer genuine need and decide to stay silent most of the time, rather than only timing an answer to a preexisting question?
5. **Evidence-aware personalization:** Does the model cite which prior observations justify a prediction or reminder, and refrain from ungrounded inferences?
6. **Cross-day streaming evaluation:** Can a model process days of video causally with stable throughput and bounded memory, instead of preparing all evidence offline at question time?

## Benchmark design guardrails

- Keep datasets, evaluation procedures, and model systems separate.
- Partition evaluation by evidence-to-query delay and contextual dependency, but avoid assuming more delay always means more difficulty.
- Add matched visual-only, audio-only, shuffled-history, and full-context oracle controls where sensible.
- Ensure a future user action is not itself used retrospectively to decide what the system *should have* known at an earlier timestamp.
- Distinguish relevance prediction, factual memory, response timing, and downstream user benefit as separate metrics.

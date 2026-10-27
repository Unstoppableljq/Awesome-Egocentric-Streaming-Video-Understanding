# Contributing

Thank you for helping maintain a precise, research-useful collection.

## Before proposing a paper

- Check for duplicates by title and arXiv ID.
- Provide an official paper link, and code/project URLs when genuinely available.
- Explain **why** the paper belongs here using one sentence about its capability or protocol; do not paste the abstract.
- Choose **one** primary topic. Additional labels may be added to the metadata in a future schema version.
- Mark uncertain protocol, audio, model code, or latency details as unknown. Avoid speculative `No` values.
- If a paper is egocentric but tested on whole videos, put it in `Related` unless its true streaming protocol is established.
- Do not reuse entire descriptions/tables copied from other Awesome Lists.

## Edit and validate

1. Add a new unique object to `data/papers.json` (copy an existing object as a template).
2. Run `python scripts/build_readme.py`.
3. Run `python scripts/build_readme.py --check`.
4. Submit a pull request with a link to the relevant method/evaluation paragraph and a concise rationale.

Do not report a code repository as unavailable just because `code_url` is blank: it means **unverified/not recorded**.

## Review criteria

Maintainers review task relevance, causal-data-access evidence, primary source correctness, description specificity, and duplicate entries. Correcting misleading protocol classifications is especially welcome.

# Qaraqalpaq AI

**Status: early implementation / not production-ready.**

Qaraqalpaq is being built as a private, single-owner, local-first AI system. This repository starts with a model-free, deterministic, synthetic-only cognitive core. It is an engineering foundation, not a claim of general intelligence, consciousness, or a complete personal AI.

## Current implementation slice

- immutable UTF-8 input capture with SHA-256 provenance;
- non-destructive Unicode NFC observation and conservative script hints;
- bounded task coordination and cancellation;
- read-only, versioned synthetic source registry;
- deterministic lexical retrieval with source spans;
- claim/evidence binding and conflict-preserving composition;
- evidence-only response composition and independent verification;
- privacy-minimizing audit manifests;
- feedback captured as candidates only (never auto-promoted).

## Run locally

Requires Python 3.12+.

```sh
python -m unittest discover -s tests -v
PYTHONPATH=src python -m qaraqalpaq "What is the project goal?"
```

No network access, API key, model download, database, or cloud service is required or used by this slice.

## Important boundaries

- Only bundled synthetic fixtures are queried.
- Original input is retained in memory only for the request; audit output stores its digest, not raw text.
- No personal files, email, messages, calendar, photos, audio, or third-party corpus are ingested.
- No persistent personal memory or encrypted vault exists yet.
- No model inference or open-domain factual answering exists yet.
- Feedback cannot modify source records, code, policy, permissions, or active rules.
- No self-modifying code or automatic permission expansion.
- Public repository visibility does not grant reuse rights to third-party material.
- FINZANJIR is an entirely separate project and is not included.

See [private production gaps](docs/PRIVATE_PRODUCTION_GAPS.md) before treating this as anything other than an early development slice.

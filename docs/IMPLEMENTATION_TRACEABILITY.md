# Implementation Traceability — Notion ↔ GitHub

Status: implementation audit snapshot, 2026-11-21. This file is descriptive; it does not freeze schemas, close gates, or authorize merge/release.

## Canonical Notion references

- ARX-170 §170.2: canonical 12-module synthetic-only first vertical slice.
- ARX-175: confirms end-to-end scope; input foundation is milestone 1 only.
- ARX-167/168/169: input contract, reconciliation and IN-001…IN-015 oracle.
- ARX-150: benchmark and synthetic suite registry.
- ARX-152: shared typed module envelopes and logical contracts.
- ARX-137/139/141/143: memory/trust/authority/lifecycle distinctions; not frozen.
- ARX-173 §173.12–173.13: owner-authorized feature-branch development and current status.

## Repository snapshot

- Repository: https://github.com/qwerasdfzxc0311/qaraqalpaq_AI_slefovera
- Default branch: `main`
- PR: https://github.com/qwerasdfzxc0311/qaraqalpaq_AI_slefovera/pull/2
- Development branch: `feat/private-production-core`
- Audited HEAD: `0525a0fc5b70ce423b8ea8f5cd3a2d8b5f070995`
- CI: run #30 / `43825248547` succeeded for this exact HEAD.
- Repository visibility: public. License metadata is null; public visibility does not grant reuse rights.
- PR #2 remains draft and unmerged. This document does not authorize merge or release.

## ARX-170 module crosswalk

| ARX-170 module | Current implementation | Status | Remaining work |
|---|---|---|---|
| 1. Input boundary | `capture_text`, `capture_bytes` | PARTIAL | Distinguish host Unicode string from transport bytes; typed decode/representation boundary |
| 2. Input Capture | `capture.py`, `CapturedInput` | PARTIAL | Resolve digest scope, byte/text ownership, offsets and artifact lifecycle |
| 3. Unicode/script observer | `observer.py` | PARTIAL | Pin Unicode version; UAX #29 graphemes; provisional orthographic-unit observer after profile review |
| 4. Task coordinator | `coordinator.py` | PARTIAL | Cumulative budgets, deterministic cancellation points, lifecycle/error semantics |
| 5. Synthetic Source Registry | `retrieval.py` | PARTIAL | Stronger fixture schema/provenance validation and pinned manifest |
| 6. Deterministic Retriever | `retrieval.py` | PARTIAL | Exact matched spans/offset units, tie/score contract, benchmark coverage |
| 7. Claim/Evidence Binder | `reasoning.py` | PARTIAL | Typed provenance, exact span/digest/fixture version binding |
| 8. Temporal/Conflict Rules | `reasoning.py` | NOT COMPLETE | Valid-time evaluation and typed relation rules; current resolver is pass-through |
| 9. Symbolic Composer | `reasoning.py` | PARTIAL | Explicit abstention, uncertainty, conflict and policy output contracts |
| 10. Independent Verifier | `verification.py` | PARTIAL | Independent temporal/freshness/policy/digest/replay checks; avoid self-certification |
| 11. Audit/Replay Manifest | `audit.py` | PARTIAL | Replay harness, version/config manifest and side-effect evidence |
| 12. Feedback Candidate Handler | `feedback.py` | PARTIAL | Candidate/quarantine/review lifecycle; no auto-promotion |

## Explicitly not implemented

- Persistent personal memory or encrypted Author Vault.
- Canonical MemoryRecord schema or production Permission Reference Monitor.
- Personal source connectors or any personal-data ingestion.
- LLM/model inference, embeddings, neural ranking or open-domain answering.
- Full Qaraqalpaq language understanding, spelling correction, transliteration or morphology.
- Cloud/database/credentials/production deployment.
- Self-modifying production code, policy or permissions.
- FINZANJIR integration or shared resources.

## Next work order

1. Input contract reconciliation (ARX-167/168/169/152) before expanding input code.
2. Implement and execute Milestone 1 synthetic tests with exact commit/run evidence.
3. Implement Milestone 2 retrieval/evidence exact spans and temporal metadata.
4. Implement Milestone 3 composition/independent verification.
5. Implement Milestone 4 audit/replay and candidate-only feedback.
6. Only then assess full ARX-170 first-slice acceptance.

All new work stays on a feature branch and draft PR. Do not merge to `main`, publish a release, ingest personal/third-party data, add secrets, connect cloud/API/database, or touch FINZANJIR under this work scope.

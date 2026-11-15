# Requirements Register

**Status:** Initial high-level requirements; detailed IDs and traceability remain in the canonical project records.

| ID | Requirement | Acceptance evidence |
| --- | --- | --- |
| R-001 | Preserve source provenance for external claims and derived summaries | Traceable source and derivation records |
| R-002 | Distinguish observation, user assertion, external claim, inference, experience, and policy | Type validation and negative tests |
| R-003 | Separate source trust, epistemic status, lifecycle, and action authority | Schema and policy invariant tests |
| R-004 | Preserve unresolved contradictions and temporal scope | Conflict and temporal test fixtures |
| R-005 | Prevent memory from granting action permission | Dispatch-time authorization tests |
| R-006 | Enforce user/tenant isolation | Cross-scope denial tests |
| R-007 | Support correction, retraction, and verified deletion of derivatives | Lineage and deletion-closure tests |
| R-008 | Keep capability claims tied to implementation and reproducible tests | Capability registry and evidence checks |
| R-009 | Gate self-improvement through isolated testing and human approval | Workflow and authorization tests |
| R-010 | Measure benign utility alongside adversarial resistance | Paired security/utility evaluations |
| R-011 | Minimize data and enforce rights, privacy, and retention requirements | Data inventory and review evidence |
| R-012 | Provide auditability and rollback for material changes | Versioned audit and rollback tests |

Detailed requirement identifiers, priorities, owners, and trace links must be reconciled with the canonical Notion registry before implementation.

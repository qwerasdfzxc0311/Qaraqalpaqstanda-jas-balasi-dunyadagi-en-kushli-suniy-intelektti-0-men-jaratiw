# Memory Schema Reconciliation — ARX-137 × ARX-139 × ARX-141 × ARX-152

Status: REVIEW WORKING NOTE — NOT FROZEN, NOT A JSON Schema, NOT A persistence contract.
Purpose: preserve the distinctions required by the Notion architecture before any durable memory implementation.

## 1. Non-negotiable separations

| Dimension | Question answered | Must not be confused with |
|---|---|---|
| record_type | What kind of originating record is this? | cognitive_type, epistemic_status, lifecycle |
| cognitive_type | What memory function does it serve? | source origin or trust |
| subject_namespace | Whose/which domain is this memory about? | access permission / principal identity |
| principal_scope | Which authenticated principal may access it? | subject_namespace |
| source_trust | How trustworthy is the source? | claim verification or authority |
| epistemic_status | What evidence state is the claim in? | source trust or store lifecycle |
| lifecycle status | Is the stored record candidate, active, quarantined, superseded, deleted, etc.? | epistemic status |
| authority_scope | What is the source authorized to establish or approve? | trust / confidence |
| capability | What operation can this build perform, with what evidence and limits? | authorization to invoke it |
| authorization grant | Who approved which operation on which resource, under what limits and expiry? | memory content / capability existence |

## 2. Field mapping status

| Canonical concept | ARX-137 | ARX-139 / ARX-141 addition | Status |
|---|---|---|---|
| Identity | record_id | stable versioned record identity | REQUIRED concept; exact ID format open |
| Origin/type | record_type | preserve provenance origin class | KEEP; enum review open |
| Cognitive role | — | cognitive_type: WORKING, EPISODIC, SEMANTIC, PROCEDURAL, AUTOBIOGRAPHICAL, PROSPECTIVE, PROVENANCE | PROPOSED; enum review open |
| Subject domain | — | subject_namespace: SELF, AUTHOR, USER/TENANT, WORLD, EXPERIENCE, SKILL, GOVERNANCE | PROPOSED; enum and single-vs-multi namespace open |
| Content | content | untrusted payload/data separation | KEEP; payload encoding open |
| Origin reference | source_ref, source_class | source lineage and rights | KEEP; source class enum open |
| Access principal | principal_scope | distinct from subject namespace | KEEP; principal model open |
| Source trust | trust_label | split into source_trust | SEMANTIC SPLIT REQUIRED; enum open |
| Claim evidence state | — | epistemic_status: UNASSESSED, PROVISIONAL, SUPPORTED, VERIFIED, DISPUTED, SUPERSEDED, EXPIRED, REJECTED | PROPOSED; thresholds open |
| Store lifecycle | status | candidate, active, disputed, stale, quarantined, superseded, deleted | KEEP AS LIFECYCLE ONLY; exact transitions open |
| Authority | authority_scope | source authority distinct from trust | KEEP; authority vocabulary open |
| Time | created_at, observed_at, valid_from/until | temporal validity | KEEP; clock and timezone policy open |
| Confidence | confidence + method | calibrated only | OPTIONAL; calibration method required |
| Evidence | evidence_refs | source digest/version/locator | KEEP; locator contract open |
| Derivation | parent_record_ids, transformation_log | typed relations and provenance | KEEP; relation graph contract open |
| Relations | — | SUPPORTS, CONTRADICTS, QUALIFIES, SUPERSEDES, RETRACTS, etc. | PROPOSED; full relation set open |
| Governance | retention_policy_id, access_policy_id | deletion tombstone, protected_class | KEEP/PROPOSED; legal and approval rules open |
| Integrity | integrity_digest, version | append-only version history | KEEP; signing/key model open |

## 3. Admission and write lifecycle

Candidate write is not active promotion. Proposed flow, subject to ARX-150/140 oracle review:

`capture -> quarantine -> classify -> provenance/rights check -> relation/conflict scan -> evidence evaluation -> privacy/risk gate -> independent decision -> candidate or reject/review -> approved versioned activation`

Memory writes cannot grant capabilities, permissions, credentials, or action authority. Untrusted source text is data, never policy. Trust, authority, scope and epistemic state cannot be amplified by summarization or repeated retrieval.

## 4. Capability and authorization are separate

Capability registry should describe implementation status, version, evidence, tests, limits, dependencies, required permissions and risk class. Authorization grant should separately identify authenticated principal, resource, purpose, operations, scope, expiry, budget, approval and revocation. Having a capability does not authorize its use; a memory record cannot create or widen a grant.

## 5. Deletion and lineage

Deletion must consider the source record and every derived descendant: extracted claims, summaries, indexes, caches, embeddings, retrieval snapshots and backups. Keep a tombstone/audit receipt where policy requires it, without retaining deleted content. Backup retention and cryptographic erasure need a separate reviewed policy. No deletion guarantee is made until propagation is implemented and tested.

## 6. Open decisions — do not silently decide

- Exact enums and allowed transitions for every dimension.
- Whether subject_namespace is single-valued or multi-valued, and its relationship to protected_class.
- Principal/tenant model for the private single-owner phase.
- Trust evaluation method and authority vocabulary by source class.
- Evidence locator and transformation lineage schema.
- Relation semantics, conflict grouping and temporal resolution.
- Retention/legal basis, deletion tombstones, backup deletion and audit retention.
- Which record types can be written automatically as candidate; what requires owner approval.
- Key/signature model for immutable ledger and authorization events.

## 7. Implementation rule

Until these decisions are reviewed against the ARX-140 synthetic transition fixtures and ARX-150 benchmark, the existing memory.py and permissions.py modules remain experimental in-memory scaffolds only. Do not serialize them, persist them, connect personal sources, or claim the canonical memory schema / policy reference monitor is implemented.

## 8. Source of truth

This note is subordinate to and must be reconciled with Notion pages ARX-137, ARX-139, ARX-141, ARX-150, ARX-151 and ARX-152. It does not replace those pages or freeze any unresolved proposal.
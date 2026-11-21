# Private single-user Production: implementation gaps

**This is a living gap register. Nothing below is claimed as implemented unless explicitly marked.**

## Implemented in the initial core commit

- [x] In-memory input capture and SHA-256 digest for the currently defined input representation.
- [x] Derived Unicode NFC observation; original Python string remains unchanged.
- [x] Conservative script hints; no transliteration or language correction.
- [x] Bounded deterministic synthetic retrieval.
- [x] Evidence-linked claims and source-binding verification.
- [x] Candidate-only feedback object.
- [x] Audit manifest excludes raw query text.
- [x] Basic task identity, cancellation flag and step-limit check.
- [x] Versioned synthetic fixture registry that rejects non-synthetic fixture classes.

## Important implementation limitations (verified against current code)

- `capture_text` UTF-8-encodes a host-provided Python string. Those bytes are a canonical encoding of the supplied string, not proof of the original transport bytes. ARX-168's byte/text/digest ownership and digest-scope decisions remain OPEN.
- Unicode observer currently provides NFC and broad script-range hints only. UAX #29 grapheme segmentation and Qaraqalpaq Sh/Ch orthographic-unit observation are not implemented.
- Task coordinator does not yet provide cumulative resource accounting or deterministic cancellation injection across every pipeline stage.
- Retriever uses lexical token overlap and currently returns the entire fixture record as its evidence span; exact matched substring offsets are not implemented.
- Temporal validity and typed relation/conflict resolution are not implemented to ARX-170 scope. Current conflict resolver preserves claims; composer detects a basic differing-value conflict.
- Independent verifier currently checks source/claim binding and source digest consistency, not the complete ARX-170/ARX-150 freshness, temporal, policy, replay and independent-composition requirements.
- Audit manifest records digests and metadata, but a complete deterministic replay harness is not yet implemented.
- Feedback is represented as a candidate object; no admission, quarantine, approval or activation lifecycle is implemented.
- `memory.py` and `permissions.py` remain experimental in-memory contract scaffolds. They are not canonical persistent memory or a production policy reference monitor.

## Required before importing any personal data

- [ ] Owner identity and local unlock/recovery flow.
- [ ] Encrypted private vault using a reviewed, maintained cryptographic implementation; no homemade encryption.
- [ ] OS-backed key storage and key rotation/recovery design.
- [ ] Per-source opt-in grants, least privilege, read-only connectors, expiry and revocation.
- [ ] Source inventory, purpose, sensitivity, retention and deletion policy.
- [ ] Immutable originals plus derived views with complete provenance.
- [ ] Deletion/correction propagation across indexes, caches, summaries and backups.
- [ ] Backup/restore drills, export and verified deletion.
- [ ] User-visible audit viewer with sensitive-content minimization.
- [ ] Offline-by-default network boundary and egress tests.
- [ ] Resource quotas, cancellation and crash recovery.
- [ ] Security review of dependencies, packaging, update/rollback and local filesystem permissions.

## Required before calling this a capable personal AI

- [ ] Persistent, typed personal memory with independent namespace, epistemic status, trust and lifecycle fields.
- [ ] Retrieval/ranking evaluated against user-approved synthetic and then explicitly authorized personal fixtures.
- [ ] Reasoning and planning evaluations with uncertainty and abstention.
- [ ] Model adapter decision. A model-free symbolic engine cannot provide broad natural-language understanding; any local model must be separately benchmarked for device fit, privacy, quality and power.
- [ ] Controlled learning lifecycle: candidate, quarantine, isolated evaluation, regression/security tests, owner approval, versioned activation and rollback.
- [ ] Multilingual Qaraqalpaq/Uzbek/Russian/English evaluation with native-speaker review where claims concern language correctness.
- [ ] Voice/media ingestion only after separate consent, data minimization and safety review.

## Explicit non-goals for this repository phase

- Public multi-user service, SaaS, cloud deployment or third-party accounts.
- Silent code, policy, permission or security-rule self-modification.
- FINZANJIR integration or shared credentials, hosting, data or repositories.
- Automatic import of all personal sources.
- Claims of human-like consciousness or sentience.

## CI evidence

For PR #2 head commit `0525a0fc5b70ce423b8ea8f5cd3a2d8b5f070995`, GitHub Actions Python CI run #30 (run ID `43825248547`) completed successfully. This verifies only the configured compileall and current unittest suite at that exact commit. It does not establish full ARX-170 acceptance, private Production readiness, security review, legal review or native-language review. Any later commit requires its own CI result.

## Release truthfulness

The current core is an early implementation slice, not a production-ready personal AI. It does not store persistent personal memory, encrypt a personal vault, use an LLM, or provide a secure personal-data plane. It has not received independent security, legal or native-language sign-off. Capability status must be tied to a commit and reproducible tests.

## Architecture reconciliation hold — ARX-137 / ARX-139 / ARX-141 / ARX-152

The experimental memory and permission modules are NOT canonical contracts and must not be treated as a schema freeze. ARX-137/141 require independent dimensions: record_type, cognitive_type, subject_namespace, principal_scope, source_trust, epistemic_status, lifecycle status, authority_scope, retention/access policy, lineage, integrity/version and deletion tombstone. ARX-152 keeps typed envelopes logical and explicitly says universal MemoryRecord schema is not frozen. The current scaffold enums are intentionally incomplete and must not be used for persistence or real personal data.

Before any persistent memory implementation:
- [ ] Field-by-field mapping of ARX-137 ↔ ARX-139 ↔ ARX-141 and ARX-152 logical envelopes.
- [ ] Keep source trust, epistemic status, lifecycle, authority and namespace as separate dimensions.
- [ ] Separate capability registry from authorization/grant records.
- [ ] Define immutable evidence ledger, candidate/quarantine/active views, typed relations and non-amplification rules.
- [ ] Define deletion closure, descendant/index/cache/backup propagation and audit evidence.
- [ ] Independent review of enum semantics and synthetic transition oracle.

The current permission broker is only an experimental in-memory scope/expiry/revocation test scaffold. It is not the ARX-152 Permission Reference Monitor and cannot authorize connector dispatch.

## Next implementation sequence — ARX-175

Canonical first vertical slice is the 12-module end-to-end synthetic-only pipeline in ARX-170 §170.2. Input foundation is milestone 1, not the entire slice.

1. Reconcile raw bytes vs host Unicode string, digest scope, offsets and normalization ownership against ARX-167/168/169/152. Keep unresolved decisions OPEN; do not infer a canonical contract.
2. Pin and document Unicode/grapheme implementation and version only after dependency/provenance/license review.
3. Implement input milestones against IN-001…IN-015 with exact original/derived assertions and deterministic cancellation injection.
4. Continue milestones 2–4: retrieval/evidence, composition/verification, audit/feedback.
5. Final acceptance requires all applicable synthetic suites, end-to-end replay and review evidence.

No personal data, third-party corpus, persistent memory, credentials, external API/model, database, cloud or deployment is authorized by this sequence.

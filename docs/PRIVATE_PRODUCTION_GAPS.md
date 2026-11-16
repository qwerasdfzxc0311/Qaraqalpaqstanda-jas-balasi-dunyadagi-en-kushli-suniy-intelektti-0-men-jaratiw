# Private single-user Production: implementation gaps

**This is a living gap register. Nothing below is claimed as implemented unless explicitly marked.**

## Implemented in the initial core commit

- [x] In-memory immutable input capture and digest.
- [x] Derived Unicode NFC observation; original input remains unchanged.
- [x] Conservative script hints; no transliteration or language correction.
- [x] Bounded deterministic synthetic retrieval.
- [x] Evidence-linked claims and an independent source-binding verifier.
- [x] Candidate-only feedback.
- [x] Audit manifest excludes raw query text.

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
- [ ] Retrieval/ranking that is evaluated against user-approved synthetic and then explicitly authorized personal fixtures.
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

## Release truthfulness

The initial core is an early development slice. It is not production-ready, does not store personal memory, does not encrypt a personal vault, does not use an LLM, and has not been security-reviewed. Capability status must be tied to a commit and reproducible tests.


## Additional contract slices (2026-11-16)

- [x] Typed memory record contract and volatile in-memory store (src/qaraqalpaq/memory.py).
- [x] Memory contract tests for provenance, namespaces, temporal validity, confidence bounds, conflict links and correction lineage (tests/test_memory.py).
- [x] Per-source, explicit-scope read permission broker contract (src/qaraqalpaq/permissions.py).
- [x] Permission tests for no-grant denial, source isolation, scope restriction, read-only operation allowlist, expiry and revocation (tests/test_permissions.py).

**Critical distinction:** these are volatile in-memory contract implementations only. They are not durable grants, owner authentication, encryption, OS key storage, connector enforcement, or a production vault. No real personal data may be connected or imported. The new commits' CI status is not yet verified by the available workflow-run view; do not infer a pass from earlier commits.

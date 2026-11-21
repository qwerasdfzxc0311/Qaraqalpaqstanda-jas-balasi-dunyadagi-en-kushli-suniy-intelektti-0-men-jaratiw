# Private Personal Data Plane — Architecture Decision Draft

Status: proposed architecture; implementation not yet started.
Scope: one owner, local-first, private production. No cloud sync or multi-user service.

## 1. Security boundary

The trusted computing base is the owner-controlled device, the application process, the operating system key store, and reviewed cryptographic/storage libraries. All other inputs are untrusted, including imported documents, metadata, filenames, OCR/transcription output, connector responses, model output, and feedback.

Default-deny network egress. The application must remain useful offline. No telemetry, remote model calls, background uploads, or cloud backup unless a future explicit decision enables a narrowly scoped path.

## 2. Layered design

1. Owner & unlock — local owner profile, device-bound unlock, recovery procedure, rate limits, lock timeout.
2. Key manager — OS-backed secret storage; envelope encryption; separate data-encryption keys per vault/domain; rotation and recovery documented. Never implement cryptographic primitives.
3. Encrypted vault — encrypted originals and metadata; atomic writes; integrity checks; schema versioning; no plaintext temp files.
4. Source permission broker — explicit per-source grant with source ID, allowed operations, purpose, scope, grant time, expiry, revocation state. Read-only is the default.
5. Ingestion quarantine — type/size limits, malware-safe parsing boundary, decompression limits, prompt-injection isolation, content classification, duplicate detection.
6. Provenance ledger — source identity, content hash, capture time, source version, transformation chain, parser version, consent grant ID, deletion state.
7. Derived memory store — separate from originals; each memory carries provenance, confidence, temporal validity, sensitivity, owner visibility, retention and correction/deletion links.
8. Retrieval & reasoning — retrieve only within granted scopes; show evidence and uncertainty; conflicting or stale memories remain distinguishable.
9. Audit & owner controls — inspect access history, revoke sources, export, correct, delete, backup, restore and verify.
10. Learning/update manager — candidate-only updates; sandboxed evaluation; signed/versioned release; explicit owner approval; rollback.

## 3. Data lifecycle

Proposed states: discovered -> permission_pending -> authorized -> quarantined -> validated -> stored -> indexed -> retained -> expired/deletion_pending -> deleted.

A source must not advance without its required gate. Revocation stops future reads immediately. Deletion must propagate to originals, extracted text, embeddings/indexes, summaries, caches and derived memories, with a deletion receipt. Backup retention and cryptographic erasure behavior must be explicit and tested; never promise deletion from an immutable backup without a verified mechanism.

## 4. Permission contract

Every connector must declare source type and stable ID; requested scopes and exact operations; read/write capability; purpose and data categories; possible third-party data; retention/deletion behavior; offline availability and network endpoints; revocation behavior and evidence.

No broad read-everything grant. The owner approves each source and scope. Revocation must be possible without deleting unrelated vault data.

## 5. Memory record contract

Each memory item must include stable ID and schema version; encrypted payload reference; source/provenance references; created, observed, valid-from and valid-until timestamps where known; epistemic type (fact, preference, hypothesis, instruction, event, inferred); confidence and verification status; sensitivity and access scope; retention rule and deletion lineage; supersedes/corrects/conflicts-with relationships.

Inference must never be stored as an observed fact. User correction must preserve history and mark the earlier record as superseded rather than silently rewriting provenance.

## 6. Acceptance gates before real personal-data import

### Gate A — cryptographic and storage safety
- vault files are unreadable without keys;
- wrong key, tampered ciphertext and truncated writes fail closed;
- keys never appear in logs, crash reports, config files or exported metadata;
- atomic write and crash-recovery tests pass;
- temporary files and swap/cache exposure are assessed for the target OS.

### Gate B — consent and scope
- no connector reads before explicit grant;
- out-of-scope access is denied;
- revoked grant blocks access immediately;
- expiry blocks access;
- source isolation prevents one connector from reading another source's data.

### Gate C — provenance and memory correctness
- every derived chunk/claim links to original source and transformation version;
- conflicting and stale records remain visible as such;
- inference is not promoted to fact;
- correction and deletion propagate to all derived artifacts.

### Gate D — owner control and recovery
- export is complete and documented;
- backup restore is reproducible;
- deletion produces verifiable receipts;
- audit viewer reveals access without exposing unnecessary content;
- lock/recovery and key rotation are tested.

### Gate E — offline and operations
- with network disabled, core still opens, searches and answers over authorized local fixtures;
- outbound network attempts are denied and observable;
- resource exhaustion, cancellation and corrupted input fail safely;
- update signature, rollback and schema migration are tested.

All gates use synthetic fixtures first. No real personal data is required for these tests. Personal-data import remains blocked until every relevant gate is implemented and passed on the actual target device.

## 7. Open decisions (must remain visible)

- Target runtime: Android-native, Termux/Linux, desktop, or a split local service.
- Key recovery: device-bound only versus owner-controlled recovery key.
- Vault database and encryption library selection after threat-model and platform review.
- Whether a local language model is acceptable; model-free symbolic core alone cannot meet broad conversational capability.
- Backup destination and whether any removable/off-device encrypted backup is allowed.
- Which personal sources are worth connecting, one at a time.

## 8. Non-negotiable constraints

- Private single-owner mode only in this phase.
- Local-first and offline-capable; external network off by default.
- Read-only connectors first; no sending, editing or deleting source content.
- No real personal-data ingestion before Gates A–E pass.
- No silent self-modification, policy changes or permission expansion.
- No FINZANJIR code, data, secrets, hosting or integration.
- No claims of human-like consciousness; capabilities are measured by reproducible behavior.
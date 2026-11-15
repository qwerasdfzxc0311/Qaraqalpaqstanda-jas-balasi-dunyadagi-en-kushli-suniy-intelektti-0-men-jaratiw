# Initial Risk Register

| ID | Risk | Impact | Initial control | Status |
| --- | --- | --- | --- | --- |
| K-001 | Memory poisoning through user, web, or tool content | Persistent false beliefs or harmful actions | Quarantine, provenance, typed writes, independent evaluation, lineage | OPEN |
| K-002 | Memory treated as authorization | Unauthorized external effects | Separate authorization plane; dispatch-time checks; default deny | OPEN |
| K-003 | Cross-user/tenant memory leakage | Privacy breach | Tenant-scoped access checks and isolation tests | OPEN |
| K-004 | Conflict or stale information silently overwrites truth | Incorrect decisions | Versioning, temporal scope, explicit contradiction relations | OPEN |
| K-005 | False capability claims | User reliance on nonexistent features | Capability registry tied to commits and test evidence | OPEN |
| K-006 | Unsafe autonomous self-modification | Loss of integrity/control | No production self-editing; isolated tests and human approval | OPEN |
| K-007 | Tool/plugin prompt injection or excessive privilege | Data disclosure or unauthorized action | Adapter boundary, least privilege, schema validation, output verification | OPEN |
| K-008 | Unlawful or unlicensed data use | Legal and reputational harm | Data inventory, rights review, minimization, exclusion by default | OPEN |
| K-009 | Overfitting to adversarial tests harms legitimate utility | Reduced usefulness | Paired benign/adversarial tests and utility measurement | OPEN |
| K-010 | Research claims overstated | Invalid design decisions | Source-type labels, review-depth labels, limitations, independent replication | OPEN |

This is an initial design register, not a completed security assessment. Risk owners, likelihood/impact scoring, residual risk, and acceptance authority remain to be assigned.

# Capability Registry

A capability is not considered available because it is described in a plan or generated in a response. Every capability entry must identify evidence and scope.

## Allowed states

- **PROPOSED** — suggested capability; no implementation evidence.
- **RESEARCHED** — literature or design review completed to a stated level.
- **IMPLEMENTED** — present in a named code revision or runtime.
- **TESTED** — reproducibly tested against defined acceptance criteria.
- **BLOCKED** — cannot proceed until named blockers are resolved.
- **NOT_AUTHORIZED** — technically possible or proposed, but permission has not been granted.
- **DEPRECATED** — no longer supported; history retained.

## Current project-level status

| Capability | Status | Evidence / limitation |
| --- | --- | --- |
| Cognitive architecture | RESEARCHED / DESIGN | Conceptual component and flow documents; no runtime |
| Autonomous memory | RESEARCHED / DESIGN | ARX-136–143 design and synthetic test specifications; no memory store or writer |
| Memory security | RESEARCHED / DESIGN | Lifecycle and threat-model work; no deployed enforcement |
| Tool integration | RESEARCHED / DESIGN | Adapter/security requirements; no Qaraqalpaq runtime connector |
| Controlled self-improvement | PROPOSED / DESIGN | Governance workflow defined conceptually; no autonomous code modification |
| Model inference | NOT_SELECTED | No model chosen or connected |
| Database/vector store | NOT_SELECTED | No storage technology selected |
| Production deployment | NOT_AUTHORIZED | Readiness gates remain open |

## Required evidence for status changes

- IMPLEMENTED: repository path, commit, build/configuration, and implementation review.
- TESTED: reproducible test report, environment, version, expected and observed results.
- RESEARCHED: sources, review depth, method, limitations, and unresolved questions.
- NOT_AUTHORIZED/BLOCKED: explicit reason and conditions for reconsideration.

Status must never be upgraded from repetition, model confidence, or an unverified self-report.

# Architecture Decision Records

This directory indexes material architecture decisions. Each decision must identify its status and evidence.

## Status vocabulary

- **PROPOSED** — under discussion; not approved.
- **ACCEPTED** — approved for the stated scope.
- **REJECTED** — considered and not selected.
- **SUPERSEDED** — replaced by a later decision; history retained.
- **DEFERRED** — intentionally postponed pending evidence or readiness gates.

## Current baseline decisions

| Topic | Current position | Status |
| --- | --- | --- |
| Overall architecture | Modular cognitive pipeline with one controlled orchestrator initially | DESIGN |
| Memory | Typed, provenance-preserving memory; trust, epistemic status, lifecycle, and authority separated | DESIGN |
| Autonomous improvement | Proposal, isolated tests, review, human authorization, versioned release | DESIGN |
| External tools | Adapter boundary, least privilege, read-only first, dispatch-time authorization | DESIGN |
| Model/framework/database/cloud | Not selected | DEFERRED |
| Runtime self-modification | Not permitted | CONSTRAINT |
| Cross-agent memory sharing | Disabled by default; not designed for initial implementation | CONSTRAINT |
| Consciousness/AGI claims | No such claim is made | CONSTRAINT |

## Decision record template

- ID and title
- Status and date
- Context/problem
- Requirements and constraints
- Alternatives considered
- Decision and scope
- Evidence and sources
- Security/privacy/legal implications
- Consequences and rollback
- Approvals and review trigger

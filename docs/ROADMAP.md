# Research and Engineering Roadmap

**All stages are conditional on applicable readiness gates.**

## Phase 0 — Scope and governance
- Confirm project charter, non-goals, decision process, data boundaries, and publication policy.
- Define requirement IDs, source register, risk ownership, and review roles.
- Resolve applicable legal, licensing, and security requirements.

## Phase 1 — Architecture and specifications
- Reconcile ARX-136–144 memory, security, tool, and publication specifications.
- Resolve open schema, identity, authority, retention, and evaluation decisions.
- Define interfaces and deterministic synthetic acceptance tests without selecting a runtime stack prematurely.

## Phase 2 — Synthetic-only verification design
- Build schema validation and policy-evaluator prototypes using synthetic fixtures only, after approval.
- Test memory poisoning, tenant isolation, authorization separation, conflict preservation, revocation, deletion closure, and benign utility.
- Obtain independent review and record reproducible evidence.

## Phase 3 — Controlled implementation selection
- Select model, framework, storage, deployment, and external services only after requirements, rights, threat model, costs, and readiness gates are satisfied.
- Keep initial integrations read-only and least-privilege where feasible.
- Do not ingest private or third-party data without approved rights and governance.

## Phase 4 — Limited evaluation
- Run isolated, reversible experiments with explicit scope, monitoring, rollback, and human oversight.
- Measure task quality, calibration, safety, privacy, latency, reliability, and compute/storage costs.

## Phase 5 — Release decision
- Independent security, legal, privacy, and technical review.
- Human authorization for each release.
- Publish limitations, evaluation evidence, known risks, and rollback plan.

No phase implies that a later phase is authorized automatically.

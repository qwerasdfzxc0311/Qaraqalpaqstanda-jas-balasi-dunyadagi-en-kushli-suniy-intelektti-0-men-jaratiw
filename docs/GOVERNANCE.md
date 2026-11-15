# Governance and Change Control

**Status:** Proposed governance baseline.

## Decision classes

- **FACT:** supported by an identifiable source or reproducible observation.
- **REQ:** requirement that the system or project must satisfy.
- **HYP:** hypothesis awaiting evidence.
- **DESIGN:** proposed architecture or mechanism.
- **CONSTRAINT:** legal, security, privacy, resource, or operational boundary.
- **TESTED:** claim tied to a reproducible test, build, configuration, and result.
- **IMPLEMENTED:** present in a named repository revision or runtime artifact.
- **DEPRECATED:** retained for history but no longer recommended.

A proposal must not be represented as an accepted decision, and implementation must not be represented as tested capability without evidence.

## Change lifecycle

1. Record the problem, motivation, affected requirements, and source evidence.
2. Classify the change and identify affected components and trust boundaries.
3. Review data rights, privacy, legal applicability, threat impact, and resource cost.
4. Define acceptance criteria and negative/abuse tests.
5. Implement only in an isolated branch or test environment after applicable gates are satisfied.
6. Run functional, regression, security, and benign-utility tests.
7. Obtain independent review and required human approval.
8. Merge and release with version, provenance, and rollback information.
9. Monitor outcomes and record incidents or corrections.

## Authority boundaries

- The system may suggest improvements and create provisional memory candidates only within a pre-authorized policy.
- It may not create, expand, or delegate its own permissions.
- It may not alter protected identity, author, governance, credentials, or production policy without the required authorized approval.
- External effects require dispatch-time authorization independent of conversational memory.
- Revocation must take effect even if an old grant appears in cached context.

## Memory governance

Memory writes are typed, scoped, attributable, and auditable. Summaries retain lineage. Conflicting claims remain linked rather than silently overwritten. Forgetting and correction cover derivative records, indexes, caches, and propagated copies according to the approved retention and deletion policy.

## Human review

Human review is required for high-impact actions, protected records, policy changes, production code/model changes, permission changes, and any change designated by readiness gates. Exact approval roles and procedures remain to be finalized.

## Decision records

Material architecture choices must have a decision record with context, alternatives, decision state, rationale, consequences, evidence, owner/approval, and review date. Open questions remain explicitly open.

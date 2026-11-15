# Architecture Overview

**Status:** Conceptual design; not implemented.

## Cognitive processing flow

1. **Input & Perception Fabric** — normalize incoming text, media, signals, and tool results while preserving source boundaries.
2. **Context & Intent Engine** — infer task intent, context, scope, and uncertainty; ask for clarification when necessary.
3. **Attention & Resource Manager** — prioritize relevant work and enforce resource budgets.
4. **Memory Fabric** — retrieve and propose typed records across working, episodic, semantic, procedural, self-model, prospective, and provenance layers.
5. **Knowledge & Evidence Graph** — represent claims, sources, evidence, temporal scope, support, contradiction, and derivation.
6. **World Model & Simulation** — maintain task-relevant state and evaluate causal hypotheses and scenarios; hypotheses remain distinguishable from observations.
7. **Reasoning Engine** — compare explanations, assess evidence, identify gaps, and communicate uncertainty.
8. **Planning & Action Manager** — create plans and classify intended effects before execution.
9. **Policy & Authorization Boundary** — independently validate principal, action, target, tool, arguments, scope, approval, expiry, and revocation state.
10. **Metacognition & Self-Monitoring** — monitor confidence calibration, errors, resource use, and capability claims.
11. **Learning & Controlled Improvement** — propose changes, test them in isolation, run regression and security checks, and require human approval where specified.
12. **Audit, Feedback & Response** — record decisions and outcomes, verify actions independently, and create memory candidates without silently promoting them.

## Architectural invariants

- Memory retrieval never grants action permission.
- A model-generated statement about its own capability is not proof of implementation.
- External content and tool output are untrusted data until evaluated for the specific use.
- Summarization and repetition do not increase source authority or trust.
- Conflicts are represented explicitly; the system does not silently average incompatible claims.
- Protected self-identity, author, governance, and authorization records use separate controlled write paths.
- External actions are denied by default and checked at dispatch time.
- Production code and policy are not self-modified.

## Memory taxonomy

Memory is classified on independent axes:

- **Subject namespace:** SELF, AUTHOR, USER/TENANT, WORLD/KNOWLEDGE, EXPERIENCE/TASK, SKILL/PROCEDURE, GOVERNANCE/AUTHORIZATION.
- **Cognitive function:** working, episodic, semantic, procedural, autobiographical/self-model, prospective/goal, source/provenance.

Trust class, epistemic status, lifecycle status, protected class, and action authority remain separate fields or linked records. No single confidence score substitutes for these dimensions.

## Controlled improvement loop

Proposal → quarantine and provenance capture → type/scope assignment → evidence and privacy review → isolated implementation or simulation → functional, regression, security, and utility tests → independent review → human authorization where required → versioned release → post-release monitoring and rollback capability.

This loop is a target design. It is not evidence that autonomous learning or self-improvement currently runs.

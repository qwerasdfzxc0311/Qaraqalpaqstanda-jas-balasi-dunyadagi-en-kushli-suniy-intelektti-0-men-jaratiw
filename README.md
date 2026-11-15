# Qaraqalpaq — Research and Architecture

> **Project status: research and architecture design. Not a deployed AI system.**

Qaraqalpaq is a long-term research and engineering project exploring how to build a capable, reliable, evidence-grounded artificial intelligence system. The goal is not to create a static FAQ or scripted chatbot. The project studies perception, memory, reasoning, planning, learning, tool use, self-monitoring, and controlled improvement as separate capabilities that must be designed and evaluated.

## Current status

- Architecture and governance: under development.
- Autonomous memory: design and synthetic test specifications in progress.
- Scientific evidence review: ongoing; findings are tracked with source type and limitations.
- Runtime implementation: **not started**.
- Model, framework, database, cloud platform, and training corpus: **not selected**.
- Production deployment or claims of consciousness/AGI: **none**.

A proposed capability is not an implemented capability. A written design is not a tested system. A test result is valid only for its recorded build, configuration, and conditions.

## Core principles

1. **Evidence before claims.** Preserve sources, dates, scope, uncertainty, and counterevidence.
2. **Memory is not authority.** Stored information cannot grant permission to act.
3. **Separate trust, truth, and permission.** Source trust, epistemic status, and action authority are independent.
4. **Preserve provenance and conflicts.** Do not silently overwrite contradictory or superseded information.
5. **Controlled self-improvement.** Proposals are isolated, tested, reviewed, authorized, and versioned before release.
6. **Least privilege and human oversight.** External effects require explicit authorization and auditable controls.
7. **Privacy and lawful data use.** No data is used without applicable rights, consent or other lawful basis, and privacy review.
8. **Measure capability.** Evaluate correctness, robustness, safety, utility, and resource cost; do not market unproven capabilities.

## High-level cognitive architecture

Input and perception → context and intent → attention/resource management → memory and evidence retrieval → world/causal model → reasoning and hypothesis formation → planning → policy and authorization checks → permitted action or internal result → independent verification → response and feedback → audited memory candidate and controlled learning.

This is a conceptual architecture, not a description of a working runtime.

## Safety boundaries

- No autonomous expansion or delegation of the system's own authority.
- No self-editing production code or policies.
- No unreviewed external tool execution.
- No automatic promotion of external input into protected self-identity, author, governance, or authorization records.
- No cross-user or cross-tenant memory sharing by default.
- No private data, credentials, API keys, or production secrets in this repository.
- No FINZANJIR project files or data are part of this repository.

## Repository contents

The initial documentation package is being prepared through a review branch. It will contain project scope, architecture, governance, requirements, capability states, evidence-handling rules, and risk boundaries. Implementation code and datasets are intentionally out of scope at this stage.

## Documentation language

The repository's normative engineering documents are written primarily in English for precise technical review. Uzbek-language explanations may be added where useful. Translations do not override the normative source unless explicitly marked.

## Licensing and reuse

**No open-source license has been granted yet.** Until a license is added by the project owner, all rights are reserved and no permission to reuse, modify, or redistribute project materials is implied. Public visibility alone does not grant a license.

## Contribution and security

Contribution, vulnerability-reporting, and release procedures are not yet finalized. Do not submit secrets, personal data, or sensitive vulnerability details in public issues or discussions. A formal security reporting channel will be documented before implementation work begins.

## Project governance

The canonical architecture and decision records are maintained in the project's Notion workspace. GitHub is the version-controlled publication and implementation workspace for approved materials. Any discrepancy must be resolved against the latest approved decision record, not by silently changing the repository.

---

*This README describes the project's intended direction and current design status. It does not claim that the described architecture has been implemented or validated in a running system.*
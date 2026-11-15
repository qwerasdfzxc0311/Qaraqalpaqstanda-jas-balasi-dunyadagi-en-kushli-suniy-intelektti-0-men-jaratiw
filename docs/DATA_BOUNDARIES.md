# Data Boundaries and Privacy

**Status:** Policy design draft; not legal advice and not a substitute for jurisdiction-specific review.

## Data classes

1. **Public project material** — original project documentation approved for public release.
2. **Public third-party material** — external publications, standards, datasets, and code subject to source attribution and applicable license/terms.
3. **Synthetic test data** — fabricated examples with no real person, credential, account, or production record.
4. **User-provided or personal data** — requires purpose definition, data minimization, rights/lawful-basis review, retention rules, access control, and deletion handling.
5. **Confidential or restricted data** — excluded from public repository and ordinary research ingestion unless a separately approved legal and security process permits it.
6. **Secrets and credentials** — never commit to the repository, logs, test fixtures, or documentation.

## Default exclusions

- FINZANJIR source files, code, data, and private project records.
- Private conversations, personal records, account identifiers, contact details, and authentication data.
- API keys, tokens, passwords, certificates, private keys, and environment files.
- Raw plugin outputs containing user or tenant information.
- Datasets or source code without confirmed rights and license compatibility.
- Production endpoints and operational secrets.

## Processing requirements

Before any data is collected or used, document its source, owner, purpose, lawful basis or permission, scope, sensitivity, retention, access controls, sharing restrictions, and deletion process. Use the minimum information necessary.

## Isolation and access

User and tenant memory must be isolated. Cross-tenant retrieval or sharing is denied by default. Access is checked at retrieval and before any external action. Audit logs must avoid storing unnecessary sensitive content.

## Deletion and correction

A deletion process must account for source records and their derivatives, including summaries, indexes, caches, backups, and propagated copies, subject to applicable legal retention requirements. Completion is not claimed until the defined deletion closure has been verified.

## Release rule

Only public, non-confidential, rights-cleared, reviewed material may enter this public repository. If classification or rights are uncertain, exclude the material pending review.

from __future__ import annotations

import hashlib

from .models import Claim, ResultStatus, Verification
from .retrieval import SyntheticSourceRegistry


def verify_claims(
    claims: tuple[Claim, ...], registry: SyntheticSourceRegistry
) -> Verification:
    checks: list[str] = []
    reasons: list[str] = []
    records = {record.source_id: record for record in registry.records}
    checks.append("fixture_class_is_synthetic")
    checks.append("fixture_digest_pinned")
    for claim in claims:
        record = records.get(claim.evidence.source_id)
        if record is None:
            reasons.append(f"missing source: {claim.evidence.source_id}")
            continue
        expected = hashlib.sha256(record.text.encode("utf-8")).hexdigest()
        if expected != claim.evidence.source_digest:
            reasons.append(f"source digest mismatch: {record.source_id}")
        if claim.evidence.text != record.text:
            reasons.append(f"source span mismatch: {record.source_id}")
        if (claim.subject, claim.predicate, claim.value, claim.polarity) != (
            record.subject, record.predicate, record.value, record.polarity
        ):
            reasons.append(f"claim/source mismatch: {record.source_id}")
    checks.append("claim_source_binding")
    if reasons:
        return Verification(ResultStatus.FAIL, tuple(checks), tuple(reasons))
    if not claims:
        return Verification(ResultStatus.INDETERMINATE, tuple(checks), ("no evidence",))
    return Verification(ResultStatus.VERIFIED, tuple(checks))

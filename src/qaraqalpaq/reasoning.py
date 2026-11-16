from __future__ import annotations

from .models import Claim, EvidenceSpan, SourceRecord


def bind_claims(
    spans: tuple[EvidenceSpan, ...], records: tuple[SourceRecord, ...]
) -> tuple[Claim, ...]:
    by_id = {record.source_id: record for record in records}
    claims: list[Claim] = []
    for span in spans:
        record = by_id.get(span.source_id)
        if record is None:
            continue
        if span.text != record.text:
            continue
        claims.append(
            Claim(
                subject=record.subject,
                predicate=record.predicate,
                value=record.value,
                polarity=record.polarity,
                evidence=span,
            )
        )
    return tuple(claims)


def resolve_conflicts(claims: tuple[Claim, ...]) -> tuple[Claim, ...]:
    """Keep incompatible claims visible; do not average or silently choose."""
    selected: list[Claim] = []
    for claim in claims:
        conflict = any(
            prior.subject == claim.subject
            and prior.predicate == claim.predicate
            and (prior.value != claim.value or prior.polarity != claim.polarity)
            for prior in selected
        )
        if not conflict:
            selected.append(claim)
    return tuple(selected)


def compose_answer(claims: tuple[Claim, ...]) -> str:
    if not claims:
        return "Bu savol bo‘yicha tasdiqlangan dalil topilmadi. Hozircha aniq javob bera olmayman."
    lines = ["Mavjud synthetic manbadagi tasdiqlangan ma’lumot:"]
    for claim in claims:
        value = claim.value if claim.polarity else f"emas: {claim.value}"
        lines.append(f"- {claim.subject} — {claim.predicate}: {value}.")
    return "\n".join(lines)

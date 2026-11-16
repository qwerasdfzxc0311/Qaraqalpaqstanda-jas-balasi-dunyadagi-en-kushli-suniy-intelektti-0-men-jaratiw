from __future__ import annotations

from collections import defaultdict

from .models import Claim, EvidenceSpan, SourceRecord


def bind_claims(
    spans: tuple[EvidenceSpan, ...], records: tuple[SourceRecord, ...]
) -> tuple[Claim, ...]:
    by_id = {record.source_id: record for record in records}
    claims: list[Claim] = []
    for span in spans:
        record = by_id.get(span.source_id)
        if record is None or span.text != record.text:
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
    """Preserve every candidate; conflict interpretation belongs to the composer."""
    return claims


def compose_answer(claims: tuple[Claim, ...]) -> str:
    if not claims:
        return "Bu savol bo‘yicha tasdiqlangan dalil topilmadi. Hozircha aniq javob bera olmayman."

    grouped: dict[tuple[str, str], list[Claim]] = defaultdict(list)
    for claim in claims:
        grouped[(claim.subject, claim.predicate)].append(claim)

    lines = ["Mavjud synthetic manbadagi dalillar:"]
    for (subject, predicate), group in grouped.items():
        distinct = {(item.value, item.polarity) for item in group}
        if len(distinct) > 1:
            lines.append(
                f"- ZIDDIYAT: {subject} — {predicate} bo‘yicha manbalarda mos kelmaydigan da’volar bor."
            )
        for claim in group:
            value = claim.value if claim.polarity else f"emas: {claim.value}"
            lines.append(f"- {subject} — {predicate}: {value} [manba: {claim.evidence.source_id}].")
    return "\n".join(lines)

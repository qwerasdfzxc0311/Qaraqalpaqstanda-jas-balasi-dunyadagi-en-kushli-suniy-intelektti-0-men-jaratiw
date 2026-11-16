from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from .models import EvidenceSpan, SourceRecord


def _tokens(text: str) -> set[str]:
    return {part.casefold() for part in re.findall(r"[^\W_]+", text, flags=re.UNICODE)}


class SyntheticSourceRegistry:
    """Loads only the repository's explicitly synthetic, versioned fixture."""

    def __init__(self, path: Path) -> None:
        raw = path.read_bytes()
        payload = json.loads(raw.decode("utf-8"))
        if payload.get("data_class") != "SYNTHETIC":
            raise ValueError("source registry accepts SYNTHETIC fixtures only")
        self.version = str(payload["version"])
        self.digest = hashlib.sha256(raw).hexdigest()
        self.records = tuple(
            SourceRecord(
                source_id=item["source_id"],
                text=item["text"],
                subject=item["subject"],
                predicate=item["predicate"],
                value=item["value"],
                polarity=bool(item["polarity"]),
                valid_from=item["valid_from"],
                valid_to=item.get("valid_to"),
                fixture_version=self.version,
            )
            for item in payload["records"]
        )


class DeterministicRetriever:
    def __init__(self, registry: SyntheticSourceRegistry) -> None:
        self.registry = registry

    def retrieve(self, query: str, *, limit: int) -> tuple[EvidenceSpan, ...]:
        query_tokens = _tokens(query)
        if not query_tokens:
            return ()
        scored: list[tuple[int, str, EvidenceSpan]] = []
        for record in self.registry.records:
            source_tokens = _tokens(record.text)
            score = len(query_tokens & source_tokens)
            if score <= 0:
                continue
            start = 0
            end = len(record.text)
            span = EvidenceSpan(
                source_id=record.source_id,
                start=start,
                end=end,
                text=record.text[start:end],
                source_digest=hashlib.sha256(record.text.encode("utf-8")).hexdigest(),
            )
            scored.append((score, record.source_id, span))
        scored.sort(key=lambda item: (-item[0], item[1]))
        return tuple(item[2] for item in scored[:limit])

"""Typed, ephemeral memory primitives.

This module is deliberately in-memory only. It is a contract/test slice, not a
personal-data vault: it performs no disk writes, encryption, connector access,
or automatic ingestion. Do not pass real personal data to it.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime, timezone
from enum import StrEnum


class EpistemicType(StrEnum):
    FACT = "FACT"
    PREFERENCE = "PREFERENCE"
    HYPOTHESIS = "HYPOTHESIS"
    INSTRUCTION = "INSTRUCTION"
    EVENT = "EVENT"
    INFERRED = "INFERRED"


class VerificationState(StrEnum):
    UNVERIFIED = "UNVERIFIED"
    SUPPORTED = "SUPPORTED"
    DISPUTED = "DISPUTED"
    SUPERSEDED = "SUPERSEDED"


@dataclass(frozen=True, slots=True)
class MemoryRecord:
    memory_id: str
    content: str
    epistemic_type: EpistemicType
    verification: VerificationState
    source_ids: tuple[str, ...]
    created_at: datetime
    observed_at: datetime | None = None
    valid_from: datetime | None = None
    valid_until: datetime | None = None
    confidence: float | None = None
    sensitivity: str = "PRIVATE"
    namespace: str = "owner"
    supersedes: str | None = None
    conflicts_with: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.memory_id.strip():
            raise ValueError("memory_id must not be empty")
        if not self.content.strip():
            raise ValueError("content must not be empty")
        if not self.namespace.strip():
            raise ValueError("namespace must not be empty")
        if not self.source_ids:
            raise ValueError("at least one provenance source is required")
        for value in (self.created_at, self.observed_at, self.valid_from, self.valid_until):
            if value is not None and value.tzinfo is None:
                raise ValueError("timestamps must be timezone-aware")
        if self.valid_from and self.valid_until and self.valid_until <= self.valid_from:
            raise ValueError("valid_until must be later than valid_from")
        if self.confidence is not None and not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        if self.epistemic_type == EpistemicType.INFERRED and self.verification == VerificationState.SUPPORTED:
            raise ValueError("inferred content cannot be promoted to source-supported fact")


class EphemeralMemoryStore:
    """Volatile test store; data disappears when the process exits."""

    def __init__(self) -> None:
        self._records: dict[str, MemoryRecord] = {}

    def add(self, record: MemoryRecord) -> None:
        if record.memory_id in self._records:
            raise ValueError("memory_id already exists")
        if record.supersedes and record.supersedes not in self._records:
            raise ValueError("superseded memory does not exist")
        self._records[record.memory_id] = record
        if record.supersedes:
            previous = self._records[record.supersedes]
            self._records[record.supersedes] = replace(
                previous, verification=VerificationState.SUPERSEDED
            )

    def get(self, memory_id: str) -> MemoryRecord | None:
        return self._records.get(memory_id)

    def list_namespace(self, namespace: str = "owner") -> tuple[MemoryRecord, ...]:
        return tuple(
            record for record in self._records.values()
            if record.namespace == namespace
        )

    def find_conflicts(self, memory_id: str) -> tuple[MemoryRecord, ...]:
        record = self._records.get(memory_id)
        if record is None:
            return ()
        return tuple(
            self._records[item_id]
            for item_id in record.conflicts_with
            if item_id in self._records
        )

    def delete(self, memory_id: str) -> bool:
        """Delete one volatile record; persistent deletion propagation is not implemented."""
        return self._records.pop(memory_id, None) is not None

    def __len__(self) -> int:
        return len(self._records)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)

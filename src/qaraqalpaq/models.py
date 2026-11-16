from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class ResultStatus(StrEnum):
    VERIFIED = "VERIFIED"
    PARTIAL = "PARTIAL"
    INDETERMINATE = "INDETERMINATE"
    FAIL = "FAIL"


@dataclass(frozen=True, slots=True)
class CapturedInput:
    raw: bytes
    sha256: str
    decoded_text: str | None
    decode_error: str | None
    media_type: str = "text/plain; charset=utf-8"


@dataclass(frozen=True, slots=True)
class UnicodeObservation:
    nfc_text: str | None
    changed_by_nfc: bool
    scripts: tuple[str, ...]
    contains_control_chars: bool
    unicode_version: str


@dataclass(frozen=True, slots=True)
class TaskBudget:
    max_input_bytes: int = 16_384
    max_candidates: int = 8
    max_steps: int = 128


@dataclass(frozen=True, slots=True)
class TaskContext:
    task_id: str
    budget: TaskBudget = field(default_factory=TaskBudget)


@dataclass(frozen=True, slots=True)
class SourceRecord:
    source_id: str
    text: str
    subject: str
    predicate: str
    value: str
    polarity: bool
    valid_from: str
    valid_to: str | None
    fixture_version: str


@dataclass(frozen=True, slots=True)
class EvidenceSpan:
    source_id: str
    start: int
    end: int
    text: str
    source_digest: str


@dataclass(frozen=True, slots=True)
class Claim:
    subject: str
    predicate: str
    value: str
    polarity: bool
    evidence: EvidenceSpan


@dataclass(frozen=True, slots=True)
class Verification:
    status: ResultStatus
    checks: tuple[str, ...]
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class PipelineResult:
    task_id: str
    answer: str
    status: ResultStatus
    claims: tuple[Claim, ...]
    verification: Verification
    audit: dict[str, Any]
    warnings: tuple[str, ...] = ()

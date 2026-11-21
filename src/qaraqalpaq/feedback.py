from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True, slots=True)
class FeedbackCandidate:
    candidate_id: str
    source_task_id: str
    proposed_correction: str
    created_at: str
    status: str = "CANDIDATE_ONLY"


def propose_feedback(task_id: str, correction: str) -> FeedbackCandidate:
    import uuid

    if not correction.strip():
        raise ValueError("correction must not be empty")
    return FeedbackCandidate(
        candidate_id=str(uuid.uuid4()),
        source_task_id=task_id,
        proposed_correction=correction,
        created_at=datetime.now(timezone.utc).isoformat(),
    )

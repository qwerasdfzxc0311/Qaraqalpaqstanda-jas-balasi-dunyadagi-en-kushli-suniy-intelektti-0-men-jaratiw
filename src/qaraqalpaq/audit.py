from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .models import CapturedInput, PipelineResult, TaskContext, Verification


def make_audit_manifest(
    captured: CapturedInput,
    context: TaskContext,
    verification: Verification,
    *,
    fixture_version: str,
    fixture_digest: str,
) -> dict[str, Any]:
    # Never place raw input text or source text in the audit record.
    return {
        "task_id": context.task_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "input_sha256": captured.sha256,
        "input_bytes": len(captured.raw),
        "fixture_version": fixture_version,
        "fixture_sha256": fixture_digest,
        "verification": verification.status.value,
        "checks": list(verification.checks),
        "reason_codes": list(verification.reasons),
        "side_effects": [],
        "audit_schema": "0.1",
    }

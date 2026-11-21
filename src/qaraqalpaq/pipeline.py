from __future__ import annotations

from pathlib import Path

from .audit import make_audit_manifest
from .capture import capture_text
from .coordinator import TaskCoordinator
from .models import PipelineResult, ResultStatus
from .observer import observe_unicode
from .reasoning import bind_claims, compose_answer, resolve_conflicts
from .retrieval import DeterministicRetriever, SyntheticSourceRegistry
from .verification import verify_claims


class CognitivePipeline:
    def __init__(self, fixture_path: Path) -> None:
        self.registry = SyntheticSourceRegistry(fixture_path)
        self.retriever = DeterministicRetriever(self.registry)
        self.coordinator = TaskCoordinator()

    def answer(self, query: str) -> PipelineResult:
        context = self.coordinator.begin()
        self.coordinator.check(context)
        captured = capture_text(query, max_bytes=context.budget.max_input_bytes)
        observation = observe_unicode(captured)
        if observation.nfc_text is None:
            raise ValueError("input could not be decoded as UTF-8")
        self.coordinator.check(context, steps=2)
        spans = self.retriever.retrieve(
            observation.nfc_text, limit=context.budget.max_candidates
        )
        claims = bind_claims(spans, self.registry.records)
        claims = resolve_conflicts(claims)
        answer = compose_answer(claims)
        verification = verify_claims(claims, self.registry)
        if verification.status == ResultStatus.FAIL:
            answer = "Tekshiruv xatosi sabab javob berilmadi."
        audit = make_audit_manifest(
            captured,
            context,
            verification,
            fixture_version=self.registry.version,
            fixture_digest=self.registry.digest,
        )
        warnings = ()
        if observation.changed_by_nfc:
            warnings = ("NFC faqat hosila ko‘rinish sifatida ishlatildi; original saqlandi.",)
        if len(observation.scripts) > 1:
            warnings += ("Aralash yozuv tizimlari aniqlandi; avtomatik transliteratsiya bajarilmadi.",)
        return PipelineResult(
            task_id=context.task_id,
            answer=answer,
            status=verification.status,
            claims=claims,
            verification=verification,
            audit=audit,
            warnings=warnings,
        )

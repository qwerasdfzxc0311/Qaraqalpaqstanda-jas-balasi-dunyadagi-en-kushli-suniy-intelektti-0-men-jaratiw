"""Experimental in-memory grant-check scaffold — NOT a policy reference monitor.

This is not a frozen ARX-152 PolicyDecision contract. It has no trusted
principal identity, signed grant authority, durable/replay-safe audit, resource
capability manifest, dispatch-time external revocation check, or persistent
owner authentication. It is not suitable for authorizing real connectors or
personal-data access. It exists only to exercise basic deny-by-default scope,
expiry and revocation invariants with synthetic fixtures.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum


class Operation(StrEnum):
    READ_METADATA = "READ_METADATA"
    READ_CONTENT = "READ_CONTENT"


@dataclass(frozen=True, slots=True)
class SourceGrant:
    grant_id: str
    source_id: str
    purpose: str
    scopes: frozenset[str]
    operations: frozenset[Operation]
    granted_at: datetime
    expires_at: datetime | None = None
    revoked_at: datetime | None = None

    def __post_init__(self) -> None:
        if not self.grant_id.strip() or not self.source_id.strip():
            raise ValueError("grant_id and source_id are required")
        if not self.purpose.strip():
            raise ValueError("a specific purpose is required")
        if not self.scopes or any(not scope.strip() for scope in self.scopes):
            raise ValueError("at least one non-empty scope is required")
        if not self.operations:
            raise ValueError("at least one explicit read operation is required")
        if any(not isinstance(op, Operation) for op in self.operations):
            raise ValueError("only explicitly enumerated read operations are supported")
        for stamp in (self.granted_at, self.expires_at, self.revoked_at):
            if stamp is not None and stamp.tzinfo is None:
                raise ValueError("grant timestamps must be timezone-aware")
        if self.expires_at and self.expires_at <= self.granted_at:
            raise ValueError("expires_at must be later than granted_at")
        if self.revoked_at and self.revoked_at < self.granted_at:
            raise ValueError("revoked_at cannot precede granted_at")


class PermissionDenied(PermissionError):
    pass


class InMemoryPermissionBroker:
    """Volatile contract broker. Grants disappear when this process exits."""

    def __init__(self) -> None:
        self._grants: dict[str, SourceGrant] = {}

    def grant(self, grant: SourceGrant) -> None:
        if grant.grant_id in self._grants:
            raise ValueError("grant_id already exists")
        if grant.revoked_at is not None:
            raise ValueError("new grants cannot start revoked")
        self._grants[grant.grant_id] = grant

    def revoke(self, grant_id: str, *, at: datetime | None = None) -> None:
        current = self._grants.get(grant_id)
        if current is None:
            raise KeyError("unknown grant")
        if current.revoked_at is not None:
            return
        revoked_at = at or datetime.now(timezone.utc)
        if revoked_at.tzinfo is None:
            raise ValueError("revocation timestamp must be timezone-aware")
        if revoked_at < current.granted_at:
            raise ValueError("revocation cannot precede grant")
        from dataclasses import replace
        self._grants[grant_id] = replace(current, revoked_at=revoked_at)

    def authorize(
        self,
        *,
        grant_id: str,
        source_id: str,
        scope: str,
        operation: Operation,
        at: datetime | None = None,
    ) -> SourceGrant:
        grant = self._grants.get(grant_id)
        if grant is None:
            raise PermissionDenied("no grant exists")
        now = at or datetime.now(timezone.utc)
        if now.tzinfo is None:
            raise ValueError("authorization timestamp must be timezone-aware")
        if grant.source_id != source_id:
            raise PermissionDenied("source isolation violation")
        if grant.revoked_at is not None and now >= grant.revoked_at:
            raise PermissionDenied("grant has been revoked")
        if now < grant.granted_at:
            raise PermissionDenied("grant is not active yet")
        if grant.expires_at is not None and now >= grant.expires_at:
            raise PermissionDenied("grant has expired")
        if scope not in grant.scopes:
            raise PermissionDenied("scope is not granted")
        if operation not in grant.operations:
            raise PermissionDenied("operation is not granted")
        return grant

    def get(self, grant_id: str) -> SourceGrant | None:
        return self._grants.get(grant_id)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)

from __future__ import annotations

import unittest
from datetime import timedelta

from qaraqalpaq.permissions import (
    InMemoryPermissionBroker,
    Operation,
    PermissionDenied,
    SourceGrant,
    utc_now,
)


def grant(grant_id="g1", **kwargs):
    now = kwargs.pop("granted_at", utc_now())
    return SourceGrant(
        grant_id=grant_id,
        source_id=kwargs.pop("source_id", "source-A"),
        purpose=kwargs.pop("purpose", "owner-approved synthetic test"),
        scopes=kwargs.pop("scopes", frozenset({"documents/notes"})),
        operations=kwargs.pop("operations", frozenset({Operation.READ_CONTENT})),
        granted_at=now,
        **kwargs,
    )


class PermissionBrokerTests(unittest.TestCase):
    def setUp(self):
        self.broker = InMemoryPermissionBroker()
        self.now = utc_now()
        self.broker.grant(grant(granted_at=self.now))

    def test_explicit_scope_and_operation_allow(self):
        result = self.broker.authorize(
            grant_id="g1", source_id="source-A", scope="documents/notes",
            operation=Operation.READ_CONTENT, at=self.now,
        )
        self.assertEqual(result.source_id, "source-A")

    def test_no_grant_denies(self):
        with self.assertRaises(PermissionDenied):
            self.broker.authorize(
                grant_id="missing", source_id="source-A",
                scope="documents/notes", operation=Operation.READ_CONTENT,
                at=self.now,
            )

    def test_source_isolation(self):
        with self.assertRaises(PermissionDenied):
            self.broker.authorize(
                grant_id="g1", source_id="source-B",
                scope="documents/notes", operation=Operation.READ_CONTENT,
                at=self.now,
            )

    def test_ungranted_scope_denied(self):
        with self.assertRaises(PermissionDenied):
            self.broker.authorize(
                grant_id="g1", source_id="source-A",
                scope="email/all", operation=Operation.READ_CONTENT,
                at=self.now,
            )

    def test_write_operation_is_not_supported(self):
        with self.assertRaises(ValueError):
            grant(operations=frozenset({"WRITE_CONTENT"}))

    def test_revocation_blocks_access(self):
        self.broker.revoke("g1", at=self.now + timedelta(seconds=1))
        with self.assertRaises(PermissionDenied):
            self.broker.authorize(
                grant_id="g1", source_id="source-A",
                scope="documents/notes", operation=Operation.READ_CONTENT,
                at=self.now + timedelta(seconds=2),
            )

    def test_expiry_blocks_access_at_boundary(self):
        broker = InMemoryPermissionBroker()
        broker.grant(grant(
            expires_at=self.now + timedelta(seconds=5),
            granted_at=self.now,
        ))
        with self.assertRaises(PermissionDenied):
            broker.authorize(
                grant_id="g1", source_id="source-A",
                scope="documents/notes", operation=Operation.READ_CONTENT,
                at=self.now + timedelta(seconds=5),
            )

    def test_duplicate_grant_id_rejected(self):
        with self.assertRaises(ValueError):
            self.broker.grant(grant(granted_at=self.now))

    def test_timezone_required(self):
        from datetime import datetime
        with self.assertRaises(ValueError):
            grant(granted_at=datetime(2026, 1, 1))

    def test_revocation_is_idempotent(self):
        at = self.now + timedelta(seconds=1)
        self.broker.revoke("g1", at=at)
        self.broker.revoke("g1", at=at + timedelta(seconds=1))
        self.assertEqual(self.broker.get("g1").revoked_at, at)


if __name__ == "__main__":
    unittest.main()

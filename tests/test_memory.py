from __future__ import annotations

import unittest
from datetime import timedelta

from qaraqalpaq.memory import (
    EphemeralMemoryStore,
    EpistemicType,
    MemoryRecord,
    VerificationState,
    utc_now,
)


def record(memory_id: str, **kwargs) -> MemoryRecord:
    return MemoryRecord(
        memory_id=memory_id,
        content=kwargs.pop("content", "owner-approved synthetic fixture"),
        epistemic_type=kwargs.pop("epistemic_type", EpistemicType.FACT),
        verification=kwargs.pop("verification", VerificationState.SUPPORTED),
        source_ids=kwargs.pop("source_ids", ("SYNTHETIC-001",)),
        created_at=kwargs.pop("created_at", utc_now()),
        **kwargs,
    )


class MemoryContractTests(unittest.TestCase):
    def test_add_and_namespace_isolation(self) -> None:
        store = EphemeralMemoryStore()
        store.add(record("m1", namespace="owner"))
        store.add(record("m2", namespace="test"))
        self.assertEqual([item.memory_id for item in store.list_namespace("owner")], ["m1"])
        self.assertEqual(len(store), 2)

    def test_duplicate_id_rejected(self) -> None:
        store = EphemeralMemoryStore()
        store.add(record("m1"))
        with self.assertRaises(ValueError):
            store.add(record("m1"))

    def test_provenance_required(self) -> None:
        with self.assertRaises(ValueError):
            record("m1", source_ids=())

    def test_naive_timestamp_rejected(self) -> None:
        from datetime import datetime
        with self.assertRaises(ValueError):
            record("m1", created_at=datetime(2026, 1, 1))

    def test_inferred_item_cannot_claim_source_supported(self) -> None:
        with self.assertRaises(ValueError):
            record(
                "m1",
                epistemic_type=EpistemicType.INFERRED,
                verification=VerificationState.SUPPORTED,
            )

    def test_conflicts_are_preserved_and_queryable(self) -> None:
        store = EphemeralMemoryStore()
        store.add(record("m1", conflicts_with=("m2",)))
        store.add(record("m2"))
        self.assertEqual(store.find_conflicts("m1")[0].memory_id, "m2")

    def test_correction_supersedes_without_erasing_history(self) -> None:
        store = EphemeralMemoryStore()
        store.add(record("old", content="old synthetic value"))
        store.add(record("new", content="corrected synthetic value", supersedes="old"))
        self.assertEqual(store.get("old").verification, VerificationState.SUPERSEDED)
        self.assertEqual(store.get("old").content, "old synthetic value")
        self.assertEqual(store.get("new").supersedes, "old")

    def test_invalid_validity_window_rejected(self) -> None:
        now = utc_now()
        with self.assertRaises(ValueError):
            record("m1", valid_from=now, valid_until=now - timedelta(seconds=1))

    def test_confidence_bounds(self) -> None:
        with self.assertRaises(ValueError):
            record("m1", confidence=1.5)

    def test_delete_is_explicit_and_idempotent(self) -> None:
        store = EphemeralMemoryStore()
        store.add(record("m1"))
        self.assertTrue(store.delete("m1"))
        self.assertFalse(store.delete("m1"))
        self.assertIsNone(store.get("m1"))


if __name__ == "__main__":
    unittest.main()

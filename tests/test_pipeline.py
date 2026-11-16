from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from qaraqalpaq.capture import capture_bytes, capture_text
from qaraqalpaq.feedback import propose_feedback
from qaraqalpaq.observer import observe_unicode
from qaraqalpaq.pipeline import CognitivePipeline
from qaraqalpaq.retrieval import SyntheticSourceRegistry
from qaraqalpaq.models import Claim, EvidenceSpan, SourceRecord
from qaraqalpaq.reasoning import compose_answer, resolve_conflicts


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures" / "knowledge.json"


class CaptureTests(unittest.TestCase):
    def test_capture_preserves_original_and_hashes_bytes(self) -> None:
        text = "Qaraqalpaq"
        captured = capture_text(text, max_bytes=100)
        self.assertEqual(captured.raw, text.encode())
        self.assertEqual(len(captured.sha256), 64)

    def test_invalid_utf8_is_not_silently_repaired(self) -> None:
        captured = capture_bytes(b"\\xff", max_bytes=10)
        self.assertIsNone(captured.decoded_text)
        self.assertIsNotNone(captured.decode_error)

    def test_size_limit(self) -> None:
        with self.assertRaises(ValueError):
            capture_text("12345", max_bytes=4)


class ObserverTests(unittest.TestCase):
    def test_nfc_is_derived_not_destructive(self) -> None:
        original = "a\\u0301"
        captured = capture_text(original, max_bytes=20)
        observation = observe_unicode(captured)
        self.assertEqual(captured.decoded_text, original)
        self.assertEqual(observation.nfc_text, "á")
        self.assertTrue(observation.changed_by_nfc)

    def test_mixed_scripts_are_reported(self) -> None:
        observation = observe_unicode(capture_text("AБ", max_bytes=20))
        self.assertEqual(set(observation.scripts), {"LATIN", "CYRILLIC"})


class RegistryTests(unittest.TestCase):
    def test_non_synthetic_registry_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text(json.dumps({"data_class": "PERSONAL", "version": "x", "records": []}))
            with self.assertRaises(ValueError):
                SyntheticSourceRegistry(path)


class PipelineTests(unittest.TestCase):
    def test_supported_question_is_evidence_grounded(self) -> None:
        result = CognitivePipeline(FIXTURE).answer("What is Qaraqalpaq AI target?")
        self.assertEqual(result.status.value, "VERIFIED")
        self.assertTrue(result.claims)
        self.assertIn("private local-first", result.answer)

    def test_unknown_question_abstains(self) -> None:
        result = CognitivePipeline(FIXTURE).answer("Who won the moon race yesterday?")
        self.assertEqual(result.status.value, "INDETERMINATE")
        self.assertIn("tasdiqlangan dalil topilmadi", result.answer)

    def test_audit_does_not_contain_raw_query(self) -> None:
        secret_like_query = "private-token-should-not-appear"
        result = CognitivePipeline(FIXTURE).answer(secret_like_query)
        self.assertNotIn(secret_like_query, json.dumps(result.audit))

    def test_feedback_is_candidate_only(self) -> None:
        candidate = propose_feedback("task-1", "review this correction")
        self.assertEqual(candidate.status, "CANDIDATE_ONLY")

    def test_conflicting_claims_are_not_silently_discarded(self) -> None:
        span_a = EvidenceSpan("SYN-A", 0, 1, "A", "digest-a")
        span_b = EvidenceSpan("SYN-B", 0, 1, "B", "digest-b")
        claims = (
            Claim("system", "mode", "local", True, span_a),
            Claim("system", "mode", "cloud", True, span_b),
        )
        kept = resolve_conflicts(claims)
        answer = compose_answer(kept)
        self.assertEqual(len(kept), 2)
        self.assertIn("ZIDDIYAT", answer)


if __name__ == "__main__":
    unittest.main()

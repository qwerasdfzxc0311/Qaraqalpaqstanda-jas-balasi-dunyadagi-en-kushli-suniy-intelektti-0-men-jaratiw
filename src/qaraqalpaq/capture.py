from __future__ import annotations

import hashlib

from .models import CapturedInput


def capture_text(text: str, *, max_bytes: int) -> CapturedInput:
    if not isinstance(text, str):
        raise TypeError("input must be text")
    raw = text.encode("utf-8", errors="strict")
    if len(raw) > max_bytes:
        raise ValueError("input exceeds configured byte budget")
    return CapturedInput(
        raw=raw,
        sha256=hashlib.sha256(raw).hexdigest(),
        decoded_text=text,
        decode_error=None,
    )


def capture_bytes(raw: bytes, *, max_bytes: int) -> CapturedInput:
    if len(raw) > max_bytes:
        raise ValueError("input exceeds configured byte budget")
    digest = hashlib.sha256(raw).hexdigest()
    try:
        decoded = raw.decode("utf-8", errors="strict")
        error = None
    except UnicodeDecodeError as exc:
        decoded = None
        error = f"invalid UTF-8 at byte offset {exc.start}"
    return CapturedInput(raw, digest, decoded, error)

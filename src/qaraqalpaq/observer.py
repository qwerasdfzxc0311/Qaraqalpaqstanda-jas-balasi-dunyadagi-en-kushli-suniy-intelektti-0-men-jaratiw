from __future__ import annotations

import unicodedata

from .models import CapturedInput, UnicodeObservation


def _script_of(char: str) -> str | None:
    cp = ord(char)
    if not char.isalpha():
        return None
    if 0x0041 <= cp <= 0x024F or 0x1E00 <= cp <= 0x1EFF:
        return "LATIN"
    if 0x0400 <= cp <= 0x052F:
        return "CYRILLIC"
    if 0x0600 <= cp <= 0x06FF:
        return "ARABIC"
    if 0x0370 <= cp <= 0x03FF:
        return "GREEK"
    return "OTHER"


def observe_unicode(captured: CapturedInput) -> UnicodeObservation:
    if captured.decoded_text is None:
        return UnicodeObservation(None, False, (), False, unicodedata.unidata_version)

    text = captured.decoded_text
    nfc = unicodedata.normalize("NFC", text)
    scripts = tuple(sorted({s for ch in text if (s := _script_of(ch)) is not None}))
    controls = any(unicodedata.category(ch) == "Cc" for ch in text)
    return UnicodeObservation(
        nfc_text=nfc,
        changed_by_nfc=(nfc != text),
        scripts=scripts,
        contains_control_chars=controls,
        unicode_version=unicodedata.unidata_version,
    )

"""Shared bounded text parser. Uploaded contents never grant execution authority."""

import json
import re

from fastapi import HTTPException


def parse_text(name, raw, limit=16384, strict_json=False):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 ._-]{0,150}\.(txt|md|csv|json)", name, re.I) or re.search(
        r"(\.env|secret|password|wallet|private.?key|seed.?phrase)", name, re.I
    ):
        raise HTTPException(
            422, "Attach a safe UTF-8 .txt, .md, .csv or .json document; PDF/DOCX/images are unsupported"
        )
    if len(raw) > limit:
        raise HTTPException(413, f"Document exceeds {limit // 1024} KB")
    try:
        content = raw.decode("utf-8")
        if strict_json and name.lower().endswith(".json"):
            json.loads(content)
    except (UnicodeDecodeError, ValueError):
        raise HTTPException(
            422, "Document must contain valid UTF-8 text (and valid JSON for .json)"
        ) from None
    if not content.strip() or "\x00" in content:
        raise HTTPException(422, "Document is empty or binary")
    return content

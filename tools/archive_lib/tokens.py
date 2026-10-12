from __future__ import annotations

import re

try:
    import tiktoken

    _ENC = tiktoken.get_encoding("cl100k_base")
    METHOD = "tiktoken:cl100k_base"
except Exception:
    _ENC = None
    METHOD = "heuristic"

_PIECE = re.compile(r"[A-Za-z]+|\d{1,3}|[^\sA-Za-z\d]")


def count(text: str) -> int:
    if not text:
        return 0
    if _ENC is not None:
        return len(_ENC.encode(text))
    return heuristic(text)


def heuristic(text: str) -> int:
    if not text:
        return 0
    n = 0
    for m in _PIECE.finditer(text):
        piece = m.group(0)
        if piece[0].isalpha():
            n += 1 + max(0, (len(piece) - 6) // 4)
        else:
            n += 1
    return n


def words(text: str) -> int:
    return len(re.findall(r"\S+", text or ""))

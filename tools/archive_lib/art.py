from __future__ import annotations

import base64
import io
import json
import struct
import zlib
from pathlib import Path

from .common import ROOT

ART = ROOT / "art"
CACHE = ART / ".cache"
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp"}
PNG_SIG = b"\x89PNG\r\n\x1a\n"
CARD_KEYWORDS = {b"chara", b"ccv3"}


def slug_for(entity_id: str) -> str:
    return entity_id.split(".", 1)[-1]


def character_dir(slug: str) -> Path:
    return ART / "characters" / slug


def find_image(slug: str) -> Path | None:
    d = character_dir(slug)
    if not d.is_dir():
        return None
    files = [p for p in d.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXT]
    return max(files, key=lambda p: p.stat().st_mtime) if files else None


def all_character_art() -> dict:
    out = {}
    root = ART / "characters"
    if root.is_dir():
        for d in root.iterdir():
            img = find_image(d.name) if d.is_dir() else None
            if img:
                out[d.name] = img
    return out


def cache_path(slug: str) -> Path:
    return CACHE / f"{slug}.png"


def needs_png_copy(slug: str) -> bool:
    img = find_image(slug)
    if not img or img.suffix.lower() == ".png":
        return False
    c = cache_path(slug)
    return not c.exists() or c.stat().st_mtime < img.stat().st_mtime


def save_png_copy(slug: str, png: bytes):
    if not png.startswith(PNG_SIG):
        raise ValueError("not a PNG")
    CACHE.mkdir(parents=True, exist_ok=True)
    cache_path(slug).write_bytes(png)


def avatar_png(slug: str) -> bytes | None:
    img = find_image(slug)
    if not img:
        return None
    if img.suffix.lower() == ".png":
        data = img.read_bytes()
        return data if data.startswith(PNG_SIG) else None
    if not needs_png_copy(slug):
        return cache_path(slug).read_bytes()
    try:
        from PIL import Image
        buf = io.BytesIO()
        Image.open(img).convert("RGBA").save(buf, "PNG")
        return buf.getvalue()
    except Exception:
        return None


def _chunks(png: bytes):
    pos = len(PNG_SIG)
    while pos + 8 <= len(png):
        (length,) = struct.unpack(">I", png[pos:pos + 4])
        typ = png[pos + 4:pos + 8]
        yield typ, png[pos:pos + 12 + length], png[pos + 8:pos + 8 + length]
        pos += 12 + length


def _chunk(typ: bytes, body: bytes) -> bytes:
    return struct.pack(">I", len(body)) + typ + body + struct.pack(">I", zlib.crc32(typ + body) & 0xFFFFFFFF)


def embed_card(png: bytes, card: dict) -> bytes:
    kept = []
    for typ, raw, body in _chunks(png):
        if typ in (b"tEXt", b"iTXt", b"zTXt") and body.split(b"\0", 1)[0] in CARD_KEYWORDS:
            continue
        if typ == b"IEND":
            break
        kept.append(raw)
    text = b"chara\0" + base64.b64encode(json.dumps(card, ensure_ascii=False).encode("utf-8"))
    return PNG_SIG + b"".join(kept) + _chunk(b"tEXt", text) + _chunk(b"IEND", b"")


def backgrounds() -> list[Path]:
    d = ART / "backgrounds"
    return sorted(p for p in d.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXT) if d.is_dir() else []

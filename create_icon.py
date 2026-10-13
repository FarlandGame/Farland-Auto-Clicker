"""Generate the bundled 64 px ICO using only Python's standard library."""

from __future__ import annotations

import math
import struct
import zlib
from pathlib import Path


SIZE = 64


def chunk(kind: bytes, data: bytes) -> bytes:
    body = kind + data
    return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body))


def pixel(x: int, y: int) -> tuple[int, int, int, int]:
    # A dark rounded square, a bright pointer, and two click rings.
    radius = 12
    dx = max(0, radius - x, x - (SIZE - 1 - radius))
    dy = max(0, radius - y, y - (SIZE - 1 - radius))
    if dx * dx + dy * dy > radius * radius:
        return 0, 0, 0, 0
    color = (19, 29, 48, 255)
    for cx, cy, rr in ((40, 22, 10), (40, 22, 16)):
        d = math.hypot(x - cx, y - cy)
        if abs(d - rr) < 1.5 and x > 24 and y < 43:
            color = (76, 130, 239, 255)
    # Pointer polygon: vertical shaft, sloping sides, and angled tail.
    if 16 <= y <= 47 and 18 <= x <= 44:
        left = 20 + (y - 16) * 0.25
        right = 20 + (y - 16) * 0.75
        if left <= x <= right and y <= 42:
            color = (243, 248, 255, 255)
        if 26 <= y <= 47 and 28 <= x <= 37 and abs(x - (y - 2) * 0.57) < 4:
            color = (243, 248, 255, 255)
    return color


rows = b"".join(b"\x00" + bytes(channel for x in range(SIZE) for channel in pixel(x, y))
                for y in range(SIZE))
png = (b"\x89PNG\r\n\x1a\n" +
       chunk(b"IHDR", struct.pack(">IIBBBBB", SIZE, SIZE, 8, 6, 0, 0, 0)) +
       chunk(b"IDAT", zlib.compress(rows, 9)) + chunk(b"IEND", b""))
icon = (struct.pack("<HHH", 0, 1, 1) +
        struct.pack("<BBBBHHII", SIZE, SIZE, 0, 0, 1, 32, len(png), 22) + png)
Path(__file__).with_name("farland.ico").write_bytes(icon)

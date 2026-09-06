#!/usr/bin/env python3
"""Convert Flow PNG outputs to JPG assets used by the static site."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "assets" / "images"


def png_to_jpg(png: Path) -> Path:
    jpg = png.with_suffix(".jpg")
    im = Image.open(png).convert("RGB")
    im.save(jpg, "JPEG", quality=90, optimize=True)
    print(f"converted {png.name} -> {jpg.name}")
    return jpg


def main() -> None:
    if not IMG.is_dir():
        print("No assets/images dir")
        return
    count = 0
    for png in sorted(IMG.glob("*.png")):
        png_to_jpg(png)
        count += 1
    print(f"Synced {count} PNG(s)")


if __name__ == "__main__":
    main()

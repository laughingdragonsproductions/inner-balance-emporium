#!/usr/bin/env python3
"""Crop reference regions from Eyvette mockups into assets/images/ (interim + Flow reference)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
OUT = ROOT / "assets" / "images"
MOCK = ASSETS


def crop_save(src: Path, box: tuple[int, int, int, int], dest: Path, *, size: tuple[int, int] | None = None) -> None:
    im = Image.open(src).convert("RGB")
    w, h = im.size
    left = int(box[0] * w)
    top = int(box[1] * h)
    right = int(box[2] * w)
    bottom = int(box[3] * h)
    piece = im.crop((left, top, right, bottom))
    if size:
        piece = piece.resize(size, Image.Resampling.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    piece.save(dest, "JPEG", quality=88, optimize=True)
    print(f"wrote {dest.relative_to(ROOT)} ({piece.size[0]}x{piece.size[1]})")


def main() -> None:
    home = MOCK / "mock-home.png"
    shop_grid = MOCK / "mock-shop-grid.png"
    shop_hero = MOCK / "mock-shop-hero.png"
    studio = MOCK / "mock-studio.png"

    # Banners / heroes (fractional boxes: left, top, right, bottom)
    crop_save(home, (0.48, 0.08, 0.98, 0.52), OUT / "hero-home.jpg", size=(1200, 900))
    crop_save(shop_hero, (0.0, 0.0, 1.0, 1.0), OUT / "hero-shop.jpg", size=(1600, 900))
    crop_save(studio, (0.0, 0.0, 1.0, 0.42), OUT / "hero-studio.jpg", size=(1600, 900))
    crop_save(home, (0.02, 0.58, 0.46, 0.88), OUT / "about-studio.jpg", size=(900, 900))

    # Categories from home mock category row
    cats = [
        ("cat-home-decor", 0.02, 0.40, 0.26, 0.56),
        ("cat-keepsakes", 0.26, 0.40, 0.50, 0.56),
        ("cat-jewelry", 0.50, 0.40, 0.74, 0.56),
        ("cat-tabletop-games", 0.74, 0.40, 0.98, 0.56),
    ]
    for name, *box in cats:
        crop_save(home, tuple(box), OUT / f"{name}.jpg", size=(800, 800))

    # Products from shop grid (first 8 cells, row 0-1)
    products = [
        "celestial-moon-coaster-set",
        "amethyst-realm-pyramid",
        "moonlit-trinket-dish",
        "lunar-keepsake-jar",
        "pressed-flower-moon-necklace",
        "galaxy-vanity-tray",
        "celestial-keychain",
        "blooming-heart-paperweight",
    ]
    cols, rows = 4, 2
    for i, slug in enumerate(products):
        col = i % cols
        row = i // cols
        left = 0.22 + col * 0.195
        right = left + 0.18
        top = 0.36 + row * 0.155
        bottom = top + 0.14
        crop_save(shop_grid, (left, top, right, bottom), OUT / f"{slug}.jpg", size=(800, 800))

    # Journal / workbench stills from studio mock
    journal = [
        ("journal-testing-new-mold", 0.04, 0.48, 0.22, 0.62),
        ("journal-new-color-story", 0.24, 0.48, 0.42, 0.62),
        ("journal-nothing-goes-to-waste", 0.44, 0.48, 0.62, 0.62),
    ]
    for name, *box in journal:
        crop_save(studio, tuple(box), OUT / f"{name}.jpg", size=(900, 600))

    print(f"Done — {len(list(OUT.glob('*.jpg')))} images in assets/images/")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Bake zombie laser-eye + giant chaos chicken textures (no Venice API)."""

from __future__ import annotations

import argparse
import random
import shutil
from pathlib import Path

from PIL import Image, ImageDraw

from common import CUSTOM_RP, VANILLA_RP, VARIANT_ROOT

BAKED_DIR = VARIANT_ROOT / "baked_textures"
OUT_DIR = CUSTOM_RP / "textures" / "entity"

VANILLA_CHICKEN = VANILLA_RP / "textures" / "entity" / "chicken" / "chicken.png"

# Chicken palette
WHITE = (245, 245, 245)
FEATHER = (220, 210, 195)
BEAK = (255, 170, 40)
COMB = (200, 40, 40)
ZOMBIE_GREEN = (90, 140, 70)
ZOMBIE_DARK = (55, 90, 45)
LASER_RED = (255, 20, 60)
LASER_GLOW = (255, 120, 150)
CHAOS_PURPLE = (160, 80, 220)
CHAOS_ORANGE = (255, 140, 40)
CHAOS_CYAN = (60, 220, 255)
CHAOS_PINK = (255, 100, 180)


def _base_chicken() -> Image.Image:
    if VANILLA_CHICKEN.exists():
        return Image.open(VANILLA_CHICKEN).convert("RGBA")
    img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([18, 22, 46, 52], fill=WHITE)
    draw.ellipse([8, 6, 28, 26], fill=WHITE)
    draw.polygon([(30, 14), (36, 18), (30, 20)], fill=BEAK)
    draw.ellipse([22, 8, 28, 14], fill=(30, 30, 30))
    draw.ellipse([32, 8, 38, 14], fill=(30, 30, 30))
    draw.rectangle([18, 4, 26, 8], fill=COMB)
    return img


def _tint(img: Image.Image, color: tuple[int, int, int], strength: float = 0.55) -> Image.Image:
    out = img.copy()
    px = out.load()
    for y in range(out.height):
        for x in range(out.width):
            r, g, b, a = px[x, y]
            if a < 8:
                continue
            px[x, y] = (
                int(r * (1 - strength) + color[0] * strength),
                int(g * (1 - strength) + color[1] * strength),
                int(b * (1 - strength) + color[2] * strength),
                a,
            )
    return out


def _laser_eyes(draw: ImageDraw.ImageDraw, *, cyan: bool = False) -> None:
    core = CHAOS_CYAN if cyan else LASER_RED
    glow = (120, 240, 255) if cyan else LASER_GLOW
    for cx in (24, 36):
        draw.rectangle([cx - 3, 9, cx + 3, 12], fill=glow)
        draw.rectangle([cx - 2, 10, cx + 2, 11], fill=core)
        draw.line([(cx, 12), (cx, 18)], fill=core, width=1)
        draw.point((cx, 19), fill=glow)


def draw_zombie_chicken(path: Path) -> None:
    img = _tint(_base_chicken(), ZOMBIE_GREEN, 0.5)
    draw = ImageDraw.Draw(img)
    random.seed(13)
    for _ in range(18):
        x, y = random.randint(4, 58), random.randint(16, 58)
        draw.point((x, y), fill=ZOMBIE_DARK)
    _laser_eyes(draw)
    draw.rectangle([16, 3, 22, 7], fill=(70, 110, 55))
    img.save(path, optimize=True)


def draw_chaos_chicken(path: Path) -> None:
    img = _base_chicken().copy()
    draw = ImageDraw.Draw(img)
    random.seed(99)
    colors = [CHAOS_PURPLE, CHAOS_ORANGE, CHAOS_CYAN, CHAOS_PINK, COMB, BEAK]
    for _ in range(28):
        c = random.choice(colors)
        x, y = random.randint(6, 56), random.randint(8, 56)
        w, h = random.randint(2, 5), random.randint(2, 4)
        draw.ellipse([x, y, x + w, y + h], fill=c)
    _laser_eyes(draw, cyan=True)
    draw.rectangle([14, 2, 30, 6], fill=CHAOS_ORANGE)
    img.save(path, optimize=True)


def bake_chickens(*, refresh_baked: bool = False) -> int:
    jobs = {
        "zombie_chicken.png": draw_zombie_chicken,
        "chaos_chicken.png": draw_chaos_chicken,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    for name, fn in jobs.items():
        rel = Path("textures/entity") / name
        baked = BAKED_DIR / rel
        dest = OUT_DIR / name
        if baked.exists() and not refresh_baked:
            shutil.copy2(baked, dest)
            print(f"  baked [{rel}]")
        else:
            fn(dest)
            baked.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(dest, baked)
            print(f"  procedural [{rel}]")
        count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Bake chaos chicken entity textures")
    parser.add_argument("--refresh-baked", action="store_true")
    args = parser.parse_args()
    print("Baking chaos chicken textures...")
    n = bake_chickens(refresh_baked=args.refresh_baked)
    print(f"Done: {n} texture(s)")


if __name__ == "__main__":
    main()

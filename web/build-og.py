#!/usr/bin/env python3
"""Generate the Open Graph / social share image.

    python3 web/build-og.py

Writes web/assets/og/antipode-og.jpg at 1200x630, the ratio Facebook, LinkedIn,
X, Slack and iMessage all crop to.

Built from `clifftop-basalt-front`, deliberately. The share image is the single
most widely distributed asset a site has, so it uses one of the four renders
cleared in web/ASSET-CLEARANCE.md rather than one still carrying badging.

Type is drawn rather than composited so the tracking matches the site: PIL has no
letter-spacing, so characters are placed individually.
"""

from __future__ import annotations

import pathlib
import sys

try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
except ImportError:  # pragma: no cover
    sys.exit("Pillow is required: pip install Pillow")

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "assets" / "renders" / "clifftop-basalt-front.png"
OUT_DIR = HERE / "assets" / "og"
FONTS = pathlib.Path("/mnt/skills/examples/canvas-design/canvas-fonts")

W, H = 1200, 630
BONE = (243, 241, 234)
OCHRE = (165, 113, 61)

# Transitional serif for the headline, to sit with Georgia on the page.
SERIF = FONTS / "LibreBaskerville-Regular.ttf"
# Grotesque for the wordmark and the standfirst, as on the site.
GROTESQUE = FONTS / "InstrumentSans-Regular.ttf"


def tracked(draw, xy, text, font, fill, tracking=0.0, anchor_left=True):
    """Draw text with letter-spacing. Returns the width drawn."""
    x, y = xy
    if not anchor_left:  # measure first, then centre
        total = sum(
            draw.textlength(ch, font=font) + tracking for ch in text
        ) - tracking
        x -= total / 2
    start = x
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking
    return x - start


def main() -> int:
    if not SRC.exists():
        sys.exit(f"missing render: {SRC}")
    for f in (SERIF, GROTESQUE):
        if not f.exists():
            sys.exit(f"missing font: {f}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # --- base image, cropped to 1200x630 keeping the car and the sun ---------
    im = Image.open(SRC).convert("RGB")
    target = W / H
    src_ratio = im.width / im.height
    if src_ratio > target:  # source is wider: trim the sides
        new_w = int(im.height * target)
        # bias right so the sun and the car's nose stay in frame
        left = int((im.width - new_w) * 0.58)
        im = im.crop((left, 0, left + new_w, im.height))
    else:
        new_h = int(im.width / target)
        top = int((im.height - new_h) * 0.45)
        im = im.crop((0, top, im.width, top + new_h))
    im = im.resize((W, H), Image.LANCZOS)

    # --- scrim: bottom-weighted, plus a left wash for the type --------------
    scrim = Image.new("L", (W, H), 0)
    px = scrim.load()
    for y in range(H):
        v = y / H
        bottom = int(238 * max(0.0, (v - 0.24) / 0.76) ** 1.45)
        for x in range(W):
            left = int(120 * max(0.0, 1 - (x / W) / 0.72) ** 1.25)
            px[x, y] = min(255, bottom + left)
    scrim = scrim.filter(ImageFilter.GaussianBlur(2))
    im = Image.composite(Image.new("RGB", (W, H), (16, 15, 12)), im, scrim)

    d = ImageDraw.Draw(im)
    pad = 68

    # --- wordmark, top left -------------------------------------------------
    d.rectangle((pad, pad + 2, pad + 26, pad + 3), fill=OCHRE)
    tracked(
        d, (pad + 42, pad - 7), "ANTIPODE MOTOR CO.",
        ImageFont.truetype(str(GROTESQUE), 19), BONE, tracking=4.6,
    )

    # --- headline, bottom left ---------------------------------------------
    head = ImageFont.truetype(str(SERIF), 60)
    lines = ["Cars for roads", "that are worth the drive."]
    line_h = 76
    block_top = H - pad - 40 - line_h * len(lines)
    for i, line in enumerate(lines):
        d.text((pad, block_top + i * line_h), line, font=head, fill=BONE)

    # --- ochre rule above the headline -------------------------------------
    d.rectangle((pad, block_top - 30, pad + 46, block_top - 29), fill=OCHRE)

    # --- standfirst under the headline -------------------------------------
    tracked(
        d, (pad + 2, H - pad - 24),
        "AIR-COOLED 911 COMMISSIONS  ·  SYDNEY, AUSTRALIA",
        ImageFont.truetype(str(GROTESQUE), 16), (214, 208, 195), tracking=3.0,
    )

    path = OUT_DIR / "antipode-og.jpg"
    im.save(path, "JPEG", quality=88, optimize=True, progressive=True)
    kb = path.stat().st_size / 1024
    print(f"  {path.relative_to(HERE.parent)}  {W}x{H}  {kb:.0f} kB")
    if kb > 300:
        print("  note: over 300 kB; some scrapers are slow to fetch large images")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

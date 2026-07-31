#!/usr/bin/env python3
"""Generate web image derivatives for the Antipode site.

Reads masters from web/assets/renders/*.png and writes two widths of WebP and
JPEG into web/assets/img/. Run from anywhere:

    python3 web/build-images.py

Requires Pillow (`pip install Pillow`).

Some masters carry a generator watermark in the lower left. CROP_BOTTOM below is
a per-file map that trims just enough to remove it, and defaults to no crop, so
clean masters are never needlessly cut down. Cropping is not a substitute for the
retouching work in web/ASSET-CLEARANCE.md: it cannot remove a Porsche crest from
a bonnet or a word mark from a rear panel.

When a master is replaced with a cleared, de-badged version, remove its entry
from CROP_BOTTOM (or set it to 0.0) and re-run.
"""

from __future__ import annotations

import pathlib
import sys

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    sys.exit("Pillow is required: pip install Pillow")

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "assets" / "renders"
OUT = HERE / "assets" / "img"

# Fraction trimmed off the bottom, per master stem. Anything absent gets no crop.
# Only the watermarked masters appear here; the v4 set is clean and stays whole.
CROP_BOTTOM = {
    "coast-dusk-motion": 0.07,
    "forest-bone-front": 0.07,
    "interior-cognac": 0.07,
    "outback-basalt-front": 0.07,
    "workshop-bone-rear": 0.07,
    "interior-tan": 0.045,  # faint mark at the very bottom edge only
}
DEFAULT_CROP = 0.0

WIDTHS = ((1600, ""), (900, "@900"))  # (target width, filename suffix)
WEBP_QUALITY = 82
JPEG_QUALITY = 84


def main() -> int:
    if not SRC.is_dir():
        sys.exit(f"no masters found at {SRC}")

    OUT.mkdir(parents=True, exist_ok=True)
    masters = sorted(SRC.glob("*.png"))
    if not masters:
        sys.exit(f"no PNG masters in {SRC}")

    print(f"{len(masters)} masters -> {OUT.relative_to(HERE.parent)}")
    print(f"widths={[w for w, _ in WIDTHS]}  cropped={len(CROP_BOTTOM)} of them\n")

    for path in masters:
        image = Image.open(path).convert("RGB")
        crop = CROP_BOTTOM.get(path.stem, DEFAULT_CROP)
        if crop:
            keep = int(image.height * (1 - crop))
            image = image.crop((0, 0, image.width, keep))

        sizes = []
        for width, suffix in WIDTHS:
            # Never upscale: a master narrower than the target is used as-is.
            if image.width <= width:
                resized = image
            else:
                height = round(image.height * width / image.width)
                resized = image.resize((width, height), Image.LANCZOS)

            stem = path.stem + suffix
            resized.save(OUT / f"{stem}.webp", "WEBP", quality=WEBP_QUALITY, method=6)
            resized.save(
                OUT / f"{stem}.jpg",
                "JPEG",
                quality=JPEG_QUALITY,
                optimize=True,
                progressive=True,
            )
            sizes.append(f"{resized.width}x{resized.height}")

        mark = f"  crop {crop:.1%}" if crop else ""
        print(f"  {path.stem:26} {' / '.join(sizes)}{mark}")

    total = sum(f.stat().st_size for f in OUT.iterdir())
    print(f"\n{len(list(OUT.iterdir()))} files, {total / 1e6:.1f} MB")
    print(
        "\nIntrinsic sizes changed? Update the width/height attributes in "
        "index.html to match, or the page will shift as images load."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Generate web image derivatives for the Antipode site.

Reads masters from web/assets/renders/*.png and writes two widths of WebP and
JPEG into web/assets/img/. Run from anywhere:

    python3 web/build-images.py

Requires Pillow (`pip install Pillow`).

The bottom crop exists to remove the "AI 生成" watermark that the source renders
carry in the lower left. It is not a substitute for the retouching work in
web/ASSET-CLEARANCE.md, which still has to happen before publication: cropping
cannot remove a Porsche crest from a bonnet.

If the masters are replaced with cleared, de-badged versions, set CROP_BOTTOM to
0.0 and re-run.
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

CROP_BOTTOM = 0.07  # fraction trimmed off the bottom to drop the watermark strip
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
    print(f"crop_bottom={CROP_BOTTOM:.0%}  widths={[w for w, _ in WIDTHS]}\n")

    for path in masters:
        image = Image.open(path).convert("RGB")
        if CROP_BOTTOM:
            keep = int(image.height * (1 - CROP_BOTTOM))
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

        print(f"  {path.stem:24} {' / '.join(sizes)}")

    total = sum(f.stat().st_size for f in OUT.iterdir())
    print(f"\n{len(list(OUT.iterdir()))} files, {total / 1e6:.1f} MB")
    print(
        "\nIntrinsic sizes changed? Update the width/height attributes in "
        "index.html to match, or the page will shift as images load."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

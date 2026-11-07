#!/usr/bin/env python3
"""Generate checked-in WebP previews. Originals and article Markdown stay intact.

Maintenance only: requires Pillow with WebP support, not used by Jekyll/CI.
"""
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
PHOTO_DIRS = (
    "assets/images/literature/graduate-photos",
    "assets/images/scenery/onroadto-taipei101",
    "assets/images/scenery/chinese-new-year-in-taipei",
    "assets/images/scenery/ntu-view",
)
PREVIEWS = ROOT / "assets/img/optimized"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def preview(source, target, width, *, lossless=False, quality=80):
    with Image.open(source) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
        width = min(width, image.width)
        height = round(image.height * width / image.width)
        if image.size != (width, height):
            image = image.resize((width, height), Image.Resampling.LANCZOS)
        target.parent.mkdir(parents=True, exist_ok=True)
        image.save(target, "WEBP", quality=quality, lossless=lossless, method=6)
    return {"path": "/" + str(target.relative_to(ROOT)), "width": width,
            "height": height, "bytes": target.stat().st_size}


def main():
    brands = {}
    for source, target, width, lossless in (
        ("assets/img/avatar-earth-cat.png", "assets/img/avatar-earth-cat-360.webp", 360, False),
        ("assets/img/contact/wechat-public-qr.png", "assets/img/contact/wechat-public-qr.webp", 430, True),
    ):
        row = preview(ROOT / source, ROOT / target, width, lossless=lossless, quality=84)
        brands["/" + source] = {"source_sha256": sha(ROOT / source),
                                "source_bytes": (ROOT / source).stat().st_size, **row}
    # Retain the existing 3x QR preview's dot pattern, palette and exact encoding.
    qr_source = ROOT / "assets/img/contact/xiaohongshu-qr.png"
    qr_target = ROOT / "assets/img/contact/xiaohongshu-qr-540.png"
    with Image.open(qr_source) as image:
        image = image.convert("RGB").resize((540, 540), Image.Resampling.LANCZOS)
        image.quantize(colors=256).save(qr_target, "PNG", optimize=True)
    brands["/assets/img/contact/xiaohongshu-qr.png"] = {
        "source_sha256": sha(qr_source), "source_bytes": qr_source.stat().st_size,
        "path": "/assets/img/contact/xiaohongshu-qr-540.png", "width": 540,
        "height": 540, "bytes": qr_target.stat().st_size,
    }
    theme = next(iter(ROOT.glob("vendor/bundle/ruby/*/gems/jekyll-theme-hydejack-9.2.1/assets/img/sidebar-bg.jpg")), None)
    theme = theme or ROOT / "_site/assets/img/sidebar-bg.jpg"
    if not theme.is_file():
        raise SystemExit("Install the locked Hydejack theme before regenerating its background preview.")
    brands["/assets/img/sidebar-bg.jpg"] = {
        "source_sha256": sha(theme), "source_bytes": theme.stat().st_size,
        **preview(theme, ROOT / "assets/img/sidebar-bg.webp", 1280, quality=76),
    }
    # PNG is required for Apple's touch icon; only remove encoding overhead.
    apple = ROOT / "assets/apple-touch-icon.png"
    with Image.open(apple) as image:
        before = image.convert("RGBA").tobytes()
        image.save(apple, "PNG", optimize=True)
    with Image.open(apple) as image:
        assert before == image.convert("RGBA").tobytes(), "Touch icon pixels changed"

    photos = {}
    originals = sorted(p for directory in PHOTO_DIRS for p in (ROOT / directory).iterdir()
                       if p.suffix.lower() in (".jpg", ".jpeg", ".png"))
    for i, path in enumerate(originals, 1):
        source_sha = sha(path)
        # Codec settings participate in the name so changed previews cannot use stale caches.
        key = hashlib.sha256((source_sha + ":webp-q80-v1").encode()).hexdigest()[:16]
        variants = []
        with Image.open(path) as image:
            natural_width = ImageOps.exif_transpose(image).width
        for width in sorted({min(natural_width, w) for w in (640, 1280)}):
            variants.append(preview(path, PREVIEWS / f"{key}-{width}.webp", width))
        photos["/" + str(path.relative_to(ROOT))] = {
            "source_sha256": source_sha, "source_bytes": path.stat().st_size, "variants": variants,
        }
        if i % 20 == 0:
            print(f"Prepared {i}/{len(originals)} photos", flush=True)
    data = {"version": 1, "photo_quality": 80, "brands": brands, "photos": photos}
    (ROOT / "_data/optimized_images.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"Prepared {len(photos)} photos and {len(brands)} common image previews.")


if __name__ == "__main__":
    main()

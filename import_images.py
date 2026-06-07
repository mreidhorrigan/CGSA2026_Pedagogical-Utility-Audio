#!/usr/bin/env python3
"""Import raw images from images/ into slides/ with the names the game needs.

Takes whatever image files you drop into images/ (any names), orders them
ALPHABETICALLY, and copies them into slides/ with a numeric ordering PREFIX while
KEEPING each file's descriptive name — e.g.

    images/introduction.png   ->  slides/01_introduction.png   (title "Introduction")
    images/method chart.jpg    ->  slides/02_method_chart.jpg   (title "Method Chart")
    images/3.png               ->  slides/03.png                (title "Slide 3")

The numeric prefix sets the slide order; build_slides.py derives the title from
the rest of the name (it strips the prefix via strip_leading_index/title_from).
slides.js is rebuilt at the end so the game picks the slides up.

    python3 import_images.py [--src images] [--dst slides] [--no-build]

Notes:
  • Originals in images/ are never modified (files are copied, not moved).
  • Re-running is deterministic: files this importer owns in slides/ — image files
    named "<number>" or "<number>_<something>" — are cleared first. Other files
    (e.g. report.pdf, notes.html) are left untouched.
"""
import argparse
import os
import re
import shutil
import sys

import build_slides  # reuse the shared naming convention + manifest builder

IMAGE_EXTS = build_slides.IMAGE_EXTS
# Files this importer "owns" in slides/: 1.png, 03.jpg, 02_method_chart.webp, …
OWNED = re.compile(r"^\d+(_.*)?$")


def safe_base(stem):
    """Descriptive remainder of a filename, made filesystem/URL friendly.
    Underscores survive (build_slides turns them back into spaces for the title)."""
    base = build_slides.strip_leading_index(stem)                 # drop any existing index
    return re.sub(r"[^\w.\-]+", "_", base, flags=re.UNICODE).strip("_")  # spaces/punct -> _


def main():
    ap = argparse.ArgumentParser(description="Normalise images/ into slides/ for the game.")
    ap.add_argument("--src", default="images")
    ap.add_argument("--dst", default="slides")
    ap.add_argument("--no-build", action="store_true", help="don't rebuild slides.js afterwards")
    args = ap.parse_args()

    if not os.path.isdir(args.src):
        print(f"Source folder '{args.src}/' not found — create it and add image files.")
        sys.exit(1)
    os.makedirs(args.dst, exist_ok=True)

    images = [
        n for n in os.listdir(args.src)
        if os.path.isfile(os.path.join(args.src, n))
        and os.path.splitext(n)[1].lower() in IMAGE_EXTS
        and not n.startswith(".")
    ]
    images.sort(key=lambda s: s.casefold())  # alphabetical

    if not images:
        print(f"No image files found in '{args.src}/'.")
        sys.exit(1)

    # clear previously-imported files for a clean, deterministic run
    for n in os.listdir(args.dst):
        stem, ext = os.path.splitext(n)
        if ext.lower() in IMAGE_EXTS and OWNED.match(stem):
            os.remove(os.path.join(args.dst, n))

    width = max(2, len(str(len(images))))  # zero-pad: 01, 02, … (001 … for 100+)
    print(f"Importing {len(images)} image(s) from '{args.src}/' (alphabetical) -> '{args.dst}/':")
    for i, name in enumerate(images, 1):
        ext = os.path.splitext(name)[1].lower()
        base = safe_base(os.path.splitext(name)[0])
        prefix = f"{i:0{width}d}"
        newname = f"{prefix}_{base}{ext}" if base else f"{prefix}{ext}"
        shutil.copy2(os.path.join(args.src, name), os.path.join(args.dst, newname))
        print(f"  {name}  ->  {args.dst}/{newname}")

    if not args.no_build:
        print()
        entries = build_slides.build_manifest(args.dst)
        build_slides.write_slides_js(entries, "slides.js")
        print(f"Rebuilt slides.js with {len(entries)} slide(s).")


if __name__ == "__main__":
    main()

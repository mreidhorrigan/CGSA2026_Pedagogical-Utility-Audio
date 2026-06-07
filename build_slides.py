#!/usr/bin/env python3
"""Generate slides.js (the runtime manifest) from the contents of slides/.

Deterministic: the same folder contents always produce the same slides.js.
Run it whenever you add / remove / rename files in slides/:

    python3 build_slides.py [--slides-dir slides] [--out slides.js]

Slide type is chosen by file extension:
    image : .png .jpg .jpeg .gif .webp .svg .avif .bmp
    pdf   : .pdf                       (shown as a scrollable document)
    html  : .html .htm                 (shown as a scrollable document)
    embed : .url .embed .video .yt     (tiny text file holding a URL; shown as a
                                        16:9 iframe — e.g. a YouTube/Vimeo link)
Files are ordered by a NATURAL sort of their names (so 2 comes before 10).
Each slide's title is derived from its filename.
"""
import argparse
import json
import os
import re

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif", ".bmp"}
PDF_EXTS = {".pdf"}
HTML_EXTS = {".html", ".htm"}
EMBED_EXTS = {".url", ".embed", ".video", ".yt"}  # a tiny text file that holds a URL

# A leading "ordering prefix" on a filename — e.g. "01_", "3 - ", "002." — used
# to derive titles here AND (in import_images.py) to avoid double-prefixing.
# One definition, shared, so the convention can't drift between the two tools.
LEADING_INDEX = re.compile(r"^[\s_.\-0-9]+")


def strip_leading_index(stem):
    """Return a filename stem with any leading numeric ordering prefix removed."""
    return LEADING_INDEX.sub("", stem)


def slide_type(ext):
    e = ext.lower()
    if e in IMAGE_EXTS:
        return "image"
    if e in PDF_EXTS:
        return "pdf"
    if e in HTML_EXTS:
        return "html"
    if e in EMBED_EXTS:
        return "embed"
    return None


def natural_key(name):
    """Human-friendly ordering: split into text / number chunks."""
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", name)]


def title_from(name):
    stem = os.path.splitext(name)[0]
    cleaned = re.sub(r"[_\-]+", " ", strip_leading_index(stem)).strip()
    if cleaned:
        return cleaned.title()
    return f"Slide {int(stem)}" if stem.isdigit() else stem  # purely-numeric name (drop zero-pad)


def read_url_file(path):
    """Return the URL stored in a .url/.embed/.video/.yt file.

    Accepts a Windows-style INI shortcut ("URL=https://…"), a bare URL anywhere in
    the file, or just the first non-comment line. Returns None if there's no URL.
    """
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
    except OSError:
        return None
    m = re.search(r"(?im)^\s*URL\s*=\s*(\S+)\s*$", text)   # [InternetShortcut] style
    if m:
        return m.group(1).strip()
    m = re.search(r"https?://\S+", text)                   # first http(s) URL anywhere
    if m:
        return m.group(0).strip()
    for line in text.splitlines():                         # else first non-comment line
        s = line.strip()
        if s and not s.startswith("#"):
            return s
    return None


# A deck compiled by SLIDES_SYSTEM/md2deck.py with front-matter `placeholder: true`
# carries this marker in its <head>. Such a placeholder fills the room only while
# it would otherwise be empty — see drop_placeholder_when_real().
PLACEHOLDER_MARKER = 'name="md2deck-role" content="placeholder"'


def _is_placeholder_html(slides_dir, src):
    """True if the html slide at `src` is an md2deck placeholder deck."""
    if not src.lower().endswith((".html", ".htm")):
        return False
    try:
        with open(os.path.join(slides_dir, os.path.basename(src)), "r",
                  encoding="utf-8", errors="replace") as f:
            return PLACEHOLDER_MARKER in f.read()
    except OSError:
        return False


def drop_placeholder_when_real(entries, slides_dir):
    """Keep placeholder deck(s) ONLY when they'd otherwise be the empty room: as
    soon as any real slide exists, the build drops them from the manifest (the
    file stays on disk as the fallback). Deterministic."""
    placeholders = [e for e in entries if e.get("type") == "html"
                    and _is_placeholder_html(slides_dir, e.get("src", ""))]
    if placeholders and len(placeholders) < len(entries):
        return [e for e in entries if e not in placeholders]
    return entries


def build_manifest(slides_dir):
    """Return the ordered list of slide dicts found in slides_dir."""
    if not os.path.isdir(slides_dir):
        return []
    entries = []
    for name in sorted(os.listdir(slides_dir), key=natural_key):
        if name.startswith("."):
            continue
        path = os.path.join(slides_dir, name)
        if not os.path.isfile(path):
            continue
        t = slide_type(os.path.splitext(name)[1])
        if not t:
            continue  # e.g. README.md — not a slide
        if t == "embed":                                   # file holds a URL, not media
            url = read_url_file(path)
            if not url:
                continue  # empty/blank URL file — skip rather than emit a broken slide
            entries.append({"type": "embed", "src": url, "title": title_from(name)})
            continue
        src = f"{slides_dir}/{name}".replace("\\", "/")
        entries.append({"type": t, "src": src, "title": title_from(name)})
    return drop_placeholder_when_real(entries, slides_dir)


def write_slides_js(entries, out_path):
    body = json.dumps(entries, indent=2, ensure_ascii=False)
    content = (
        "// AUTO-GENERATED by build_slides.py — do not edit by hand.\n"
        "// Regenerate after changing the slides/ folder:  python3 build_slides.py\n"
        "// Each entry: { type: 'image'|'pdf'|'html'|'embed', src: '...', title: '...' }\n"
        "//   (an html entry may instead use { html: '<inline markup>' } and no src;\n"
        "//    an embed entry's src is a URL — e.g. a YouTube/Vimeo link — shown 16:9)\n"
        f"window.SLIDES_MANIFEST = {body};\n"
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    return content


def main():
    ap = argparse.ArgumentParser(description="Build slides.js from the slides/ folder.")
    ap.add_argument("--slides-dir", default="slides")
    ap.add_argument("--out", default="slides.js")
    args = ap.parse_args()

    entries = build_manifest(args.slides_dir)
    write_slides_js(entries, args.out)

    print(f"Wrote {args.out} with {len(entries)} slide(s):")
    for i, e in enumerate(entries, 1):
        print(f"  {i:>2}. [{e['type']:>5}] {e['src']}  —  {e['title']}")
    if not entries:
        print("  (no slides found — the game will fall back to image-probing, then placeholders)")


if __name__ == "__main__":
    main()

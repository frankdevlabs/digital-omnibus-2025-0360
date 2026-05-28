#!/usr/bin/env python3
"""Extract tracked changes (additions / deletions) from a Council compromise PDF.

These PDFs encode Presidency edits as: deletions = strikethrough, additions =
bold, changes-vs-Commission-proposal = bold-underlined. Plain-text extraction
loses all of that. This tool recovers it from the PDF's own structure:

  * bold     -> span font flag (bit 4) or a "Bold" font name  -> ADDITION
  * struck   -> a thin horizontal vector line/rect crossing the
                VERTICAL MIDDLE of a text span                -> DELETION
  * underline-> a thin line near the span BASELINE            -> (change marker)

Output modes:
  --mode clean   consolidated reading (deletions removed) -- transcribe FROM this
  --mode marked  ~~deletion~~ / **addition** inline -- eyeball this to sanity-check
  --mode both    marked, then a '----- CLEAN -----' divider, then clean (default)

Usage:
  python3 pdf_changes.py <pdf> --all
  python3 pdf_changes.py <pdf> --pages 2-16 --mode clean
  python3 pdf_changes.py <pdf> --pages 18 --mode marked

This is the PRIMARY transcription aid. Still render the page image
(render_pdf.py) and read it whenever the layout is unusual (tables, footnotes,
multi-column) or the markup looks wrong -- the two should agree.
"""
import argparse, os, sys

try:
    import fitz  # PyMuPDF
except ModuleNotFoundError:
    sys.exit("PyMuPDF missing. Run:  pip install pymupdf cffi")


def horizontal_lines(pg):
    """Thin horizontal segments: (x0, x1, y_center)."""
    out = []
    for p in pg.get_drawings():
        for it in p["items"]:
            if it[0] == "l":
                a, b = it[1], it[2]
                if abs(a.y - b.y) < 0.8 and abs(a.x - b.x) > 2:
                    out.append((min(a.x, b.x), max(a.x, b.x), (a.y + b.y) / 2))
            elif it[0] == "re":
                r = it[1]
                if r.height < 2.0 and r.width > 2:
                    out.append((r.x0, r.x1, (r.y0 + r.y1) / 2))
    return out


def classify_span(sp, lines):
    """Return (is_struck, is_bold, is_underline) for a text span."""
    x0, y0, x1, y1 = sp["bbox"]
    h = (y1 - y0) or 1.0
    bold = bool(sp["flags"] & 16) or "Bold" in sp.get("font", "")
    struck = under = False
    for lx0, lx1, ly in lines:
        if lx1 < x0 + 1 or lx0 > x1 - 1:   # require horizontal overlap
            continue
        rel = (ly - y0) / h
        if 0.25 < rel < 0.72:              # crosses the glyph middle
            struck = True
        elif 0.72 <= rel < 1.15:           # sits on/just below the baseline
            under = True
    return struck, bold, under


def render_page(pg, mode):
    lines = horizontal_lines(pg)
    marked, clean = [], []
    for blk in pg.get_text("dict")["blocks"]:
        for ln in blk.get("lines", []):
            mparts, cparts = [], []
            for sp in ln["spans"]:
                t = sp["text"]
                if not t.strip():
                    mparts.append(t); cparts.append(t); continue
                struck, bold, under = classify_span(sp, lines)
                if struck:
                    mparts.append(f"~~{t}~~")
                    # dropped from clean
                elif bold and under:
                    mparts.append(f"**__{t}__**"); cparts.append(t)
                elif bold:
                    mparts.append(f"**{t}**"); cparts.append(t)
                elif under:
                    mparts.append(f"__{t}__"); cparts.append(t)
                else:
                    mparts.append(t); cparts.append(t)
            ms = "".join(mparts).rstrip()
            cs = "".join(cparts).rstrip()
            if ms.strip():
                marked.append(ms)
            if cs.strip():
                clean.append(cs)
    return "\n".join(marked), "\n".join(clean)


def parse_pages(spec, n):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1); out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return [p for p in out if 1 <= p <= n]


def main():
    ap = argparse.ArgumentParser(description="Recover tracked changes from a Council compromise PDF.")
    ap.add_argument("pdf")
    ap.add_argument("--pages", help="1-based pages/ranges, e.g. 2-16")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--mode", choices=["clean", "marked", "both"], default="both")
    args = ap.parse_args()

    if not os.path.exists(args.pdf):
        sys.exit(f"No such PDF: {args.pdf}")
    doc = fitz.open(args.pdf)
    n = doc.page_count
    pages = list(range(1, n + 1)) if (args.all or not args.pages) else parse_pages(args.pages, n)

    for p in pages:
        marked, clean = render_page(doc[p - 1], args.mode)
        print(f"\n############### PAGE {p} ###############")
        if args.mode in ("marked", "both"):
            print(marked)
        if args.mode == "both":
            print("\n----------------- CLEAN -----------------")
        if args.mode in ("clean", "both"):
            print(clean)


if __name__ == "__main__":
    main()

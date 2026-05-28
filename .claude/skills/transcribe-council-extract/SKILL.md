---
name: transcribe-council-extract
description: >-
  Transcribe an EU Council compromise PDF (digital-omnibus 2025/0360) into the
  repo's structured markdown extracts. Use when asked to transcribe / create
  extracts for a new ST document, add a new compromise-text version under
  extracts/council/, produce consolidated operative text, or diff one Council
  version against another. Covers rendering tracked-change pages to images,
  applying the consolidated reading, and link-checking the output.
---

# Transcribe a Council compromise text into extracts

This repo stores each Council compromise version of the Digital Omnibus
(file 2025/0360 COD) as a faithful, **diffable** markdown transcription under
`extracts/council/`, split into five files per version. The canonical rules are
in [`extracts/council/_TRANSCRIPTION_GUIDE.md`](../../../extracts/council/_TRANSCRIPTION_GUIDE.md) —
read it first; this skill is the *operational* companion (how to actually pull
text off the PDF and verify the result).

**The one thing that makes this hard:** the PDFs show changes as tracked edits —
~~strikethrough~~ = deletion, **bold** / **bold-underlined** = addition. The
guide wants the *consolidated* reading (changes applied). Plain-text extraction
**destroys that formatting** and interleaves struck and added words (you get
`9672 hours` for "~~72~~ **96** hours", `datasubmitting` for
"~~…their data~~ **submitting**…"). So the driver renders pages to **images**
and you read them.

All paths below are relative to the **repo root**.

## Prerequisites

```bash
pip install pymupdf cffi
```

`cffi` is required: without it `pypdf`/crypto backends fail with
`ModuleNotFoundError: No module named '_cffi_backend'`. PyMuPDF (`fitz`) does the
rendering.

## Run — agent path (this is the workflow)

1. Confirm the exact source filename:

   ```bash
   ls sources/council/
   ```

2. Render the pages you need to `/tmp` (1-based; ranges allowed; `--all` for the
   whole document):

   ```bash
   python3 .claude/skills/transcribe-council-extract/render_pdf.py \
     "sources/council/ST-6406-2026_council-presidency-compromise_2026-02-20.pdf" --all
   ```

   For an ambiguous clause, render a high-DPI vertical crop
   (`<page>:<y0frac>:<y1frac>[:dpi]`, repeatable):

   ```bash
   python3 .claude/skills/transcribe-council-extract/render_pdf.py \
     "sources/council/ST-6406-2026_council-presidency-compromise_2026-02-20.pdf" \
     --pages 1,18,19 --crop 18:0.30:0.52:320
   ```

3. **Read the PNGs** (`/tmp/p01.png …`, crops `/tmp/pNN_<y0>-<y1>.png`) with the
   Read tool. Produce the **consolidated** text: KEEP bold / bold-underlined, DROP
   strikethrough. Start with the **cover page** — it has the change legend, the
   subject line, the date, and the meeting (e.g. AGS = Antici Group
   (Simplification)). The cover's text layer is usually empty (image-only), so you
   must read its rendered image.

4. Read the matching **reference version's** five files to mirror structure,
   `<a id="...">` anchors and header style, e.g.
   [`../../../extracts/council/ST-9547-2026_gdpr-art3-amendments.md`](../../../extracts/council/ST-9547-2026_gdpr-art3-amendments.md)
   and its siblings (`_eprivacy-art5.md`, `_cyber-art6-9.md`, `_final-art10-11.md`,
   `_recitals.md`).

5. Write the five `extracts/council/ST-<nnnn>-<yyyy>_*.md` files per the guide:
   header blockquote (doc no. + LIMITE + date + meeting + file 2025/0360 (COD) +
   "working transcription, not an official text" + link to `../../NOTICE`);
   the document's **own** article/recital numbering; `▸` change-notes;
   `[DELETED in ST <nnnn>/26]`; `[illegible in source]`; sibling +
   `docs/provisions|instruments/*` cross-links. If a section is genuinely absent
   in this version, still create the file and state the absence + a one-line reason
   + cross-links.

6. Verify links (must end with `0 broken`; fix only link paths, never legal text):

   ```bash
   python3 .claude/skills/transcribe-council-extract/linkcheck.py .
   ```

7. Branch `extracts/st-<nnnn>-<yyyy>`, commit the five files, push, open a PR to
   `main`. Do **not** commit the `/tmp` PNGs.

## Run — human path

There is no app. A human reads the PDF in a viewer and edits the markdown by
hand; the rendering + link-check steps above are still the reliable way to get
tracked-change-accurate text and to gate the result.

## Gotchas (battle scars)

- **Never transcribe from `pdftotext`/`page.get_text()` for operative text.** It
  drops strikethrough/bold and merges old+new tokens (`9672`, `datasubmitting`).
  Read images. Zoom (`--crop`, dpi 300–320) any clause you're unsure about.
- **`MuPDF error: ... No common ancestor in structure tree`** on stderr is
  harmless — rendering still succeeds (the example commands `2>/dev/null` it).
- **Numbering shifts between versions.** Use the document's own point/article and
  recital numbers; never copy a later version's numbers onto an earlier text.
- **A version can omit whole sections.** E.g. ST 6406/26 (Feb) has *no* operative
  ePrivacy (Art 5) or cyber (Arts 6–9) articles and no Article 11 — only a
  *bracketed* `[via the single-entry point … Article 23a of Directive (EU)
  2022/2555]` hook inside GDPR Art 33. Create the file and document the absence.
- **Bracketed `[...]` / `[OP: insert date = ...]` are undecided in the source** —
  preserve the brackets in the transcription; that is *not* `[illegible]`.
- **Same legal point can move between an article and a recital across versions**
  (e.g. AI legitimate interest = operative Art 88c + recitals 30/31 in Feb, but
  only recital 33a in May). Note the move in a `▸` change-note and cross-link.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `ModuleNotFoundError: No module named '_cffi_backend'` | `pip install cffi` |
| `PyMuPDF missing` from the driver | `pip install pymupdf cffi` |
| Rendered PNG is blank / image-only | it's a scanned cover or wrong page — re-render that page, or `--crop` at higher dpi |
| `linkcheck.py` reports a missing anchor | the `#fragment` doesn't match any `<a id>` or heading slug in the target — fix the link, not the heading |
| lychee CI red but `linkcheck.py` green | an *external* host rate-limited; check the excludes in `lychee.toml` (CI tolerates 403/429) |

## Files in this skill

- `render_pdf.py` — render full pages / zoom crops to `/tmp` for visual reading.
- `linkcheck.py` — internal relative-link + `#anchor` checker over `**/*.md`
  (mirrors the scope of the repo's lychee CI so you can verify before pushing).

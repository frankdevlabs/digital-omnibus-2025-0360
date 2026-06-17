# Transcription guide for European Parliament committee-text extracts

Internal standard for every file in `extracts/parliament/`. The goal: each EP committee text
(draft opinion, draft report, tabled amendments, adopted opinion/report) is a faithful, diffable
transcription of its **operative amendments**, structured so cross-links from `../../docs/provisions/*`
and `../../docs/instruments/*` resolve and so successive versions diff meaningfully.

## What lives here (and how it differs from `../council/`)

Council compromise texts are a **consolidated** redraft of the whole operative text (changes against
the Commission proposal applied). **EP committee texts are not** — they are a numbered list of
**discrete amendments**, each in a two-column "Text proposed by the Commission | Amendment" table,
often followed by a per-amendment *Justification*. So:

- Do **not** consolidate. Transcribe the amendments **as tabled**, in the document's own order and
  numbering.
- The `transcribe-council-extract` skill's `pdf_changes.py` (which recovers strikethrough/bold tracked
  changes) **does not apply** here — EP amendment PDFs are clean two-column tables, not tracked-change
  redlines. Use `render_pdf.py` (page images) to read the tables and `linkcheck.py` to validate links;
  both live under `../../.claude/skills/transcribe-council-extract/`.

## Source of truth
The committed PDF/DOCX under `../../sources/parliament/` for that document. Transcribe from the file
on disk. Never transcribe from memory, a journalist's summary, or a Bluesky/screenshot lead — those
are leads only. **doceo bot-block:** `www.europarl.europa.eu/doceo/...` returns HTTP 202 with an
AWS-WAF JS challenge to all non-browser clients (PDF *and* DOCX), so `curl`/WebFetch cannot fetch it.
Obtain the file via a real browser download (which solves the challenge) or a non-WAF mirror, commit
it to `sources/parliament/`, then transcribe.

## Faithfulness rules (hard)
- Transcribe the operative wording of each amendment **verbatim**. This is primary legal text, not
  prose to paraphrase. Keep the Commission-text column too where it aids the diff (or note "Commission
  text: see `../commission/COM-2025-837_<strand>.md#<anchor>`").
- Preserve the document's **own** amendment numbering and its target references exactly — e.g.
  *"Amendment 7 — Article 1 – paragraph 1 – point 3 — Regulation (EU) 2023/2854, Article 4(1)"*.
- Transcribe the committee/rapporteur **Justification** under each amendment if present (it is the
  recorded reason and feeds the provision's Parliament section).
- Bracketed placeholders / undecided source brackets `[...]` preserved as-is; illegible passages
  marked `[illegible in source]` — never guess.
- Make **no claim the document does not support.** If only the cover page is confirmed (e.g. text not
  yet retrieved), do not create an extract — register metadata only and set `pending_operative_text`
  (see `register-document` / `resolve-tracker-issue`).

## Structure & anchors
- **One file per committee document**, named `<DOC-ID>_<short-desc>.md` to match `data/documents.yaml`
  and the repo convention — e.g. `JURI-PA-789142_draft-opinion.md`, `LIBE-AM-xxxxxx_amendments.md`,
  `ITRE-LIBE-PR-xxxxxx_draft-report.md`. (EP committee texts are per-committee documents, not the
  five-strand split used for Council consolidated texts.)
- Give every amendment a stable `<a id="amendment-N">` anchor, and add a second anchor keyed to the
  affected provision where useful (e.g. `<a id="dataact-art4-trade-secrets">`) so
  `docs/provisions/*` / `docs/instruments/*` can deep-link to the exact amendment.
- Group amendments by the instrument/article they touch where the document does, so the file reads in
  the same order as the provisions it feeds.

## Header block (every file)
Open with the same blockquote style as the Council/Commission files: source = committee + document
number (e.g. **JURI draft opinion PE789.142v01-00**) + rapporteur + date + interinstitutional file
**2025/0360 (COD)** + the lead committee it feeds (e.g. for the joint **ITRE/LIBE**) + "working
transcription, not an official text" + "verify against the authoritative document (doceo /
`JURI-PA-789142_EN.pdf`)" + "See `../../NOTICE`."

## Cross-links
Relative links only. Link the matching `../commission/` (and `../council/`) anchors for the same
article, and the relevant `../../docs/provisions/*` / `../../docs/instruments/*` pages. Verify every
internal link/anchor resolves
(`python3 ../../.claude/skills/transcribe-council-extract/linkcheck.py ../..`) before finishing.

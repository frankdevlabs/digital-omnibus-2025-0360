# Digital Omnibus Tracker — File 2025/0360 (COD)

A personal, open tracker for the EU **Digital Omnibus** proposal on the *data and cyber* strand:
the simplification of the digital legislative framework affecting the **GDPR, ePrivacy, cookies,
Platform-to-Business (P2B), and cyber incident-reporting** rules.

> **Scope.** This repo tracks **one file only: `2025/0360 (COD)`** — Commission proposal
> **COM(2025) 837 final** of 19 November 2025.
> It is **not** the AI-Act Digital Omnibus (`2025/0359 (COD)`), which is a separate proposal on a
> separate, faster track. See [`docs/instruments/repealed.md`](docs/instruments/repealed.md) and
> [`STATUS.md`](STATUS.md) for why the two are kept apart.

**Current status (high level):** Council working-party stage (third Cyprus Presidency compromise
text, ST 9547/26, 21 May 2026); European Parliament joint ITRE/LIBE scrutiny, no draft report yet.
Full snapshot in **[`STATUS.md`](STATUS.md)**.

---

## How this repo is organised

The repo deliberately separates three layers so that links stay stable over time:

| Layer | Folder | What it is | Mutable? |
|---|---|---|---|
| **Primary sources** | [`sources/`](sources/) | Register of every official document, with links to authoritative copies | append-only |
| **Operative-text extracts** | [`extracts/`](extracts/) | Diffable plain-text of the operative articles, for `git diff` across versions — [`commission/`](extracts/commission/) is the Commission base text, [`council/`](extracts/council/) the compromise texts | versioned |
| **Analysis** | [`docs/`](docs/) | The human-readable analysis that links *to* the layers above | living |

### Navigation

- **[`STATUS.md`](STATUS.md)** — where the file stands right now (one screen).
- **[`TIMELINE.md`](TIMELINE.md)** — full chronology, every entry linked to a source.
- **[`docs/summary.md`](docs/summary.md)** — the plain-language summary.
- **[`docs/commission-proposal.md`](docs/commission-proposal.md)** — digest of the Commission proposal's explanatory memorandum.
- **[`docs/institutional-positions.md`](docs/institutional-positions.md)** — Commission vs Council vs Parliament comparison table.
- **[`docs/member-state-positions.md`](docs/member-state-positions.md)** — what individual Council delegations (FR, PL, RO) are saying.
- **[`docs/fault-lines.md`](docs/fault-lines.md)** — the contested issues likely to dominate trilogue.
- **[`docs/stakeholders.md`](docs/stakeholders.md)** — EDPB/EDPS, noyb, EDRi, BEUC, industry.
- **[`docs/provisions/`](docs/provisions/)** — one file per tracked provision (Art 4, 9, 12/57, 22, 33, 88a/88b, 88c, single-entry point).
- **[`docs/instruments/`](docs/instruments/)** — what changes per amended/repealed instrument.
- **[`sources/README.md`](sources/README.md)** — the document register.
- **[`extracts/commission/`](extracts/commission/)** — base-text extracts of the Commission proposal COM(2025) 837 (the diff baseline).
- **[`extracts/council/`](extracts/council/)** — operative-text extracts of the Council compromise texts.

---

## Linking conventions

1. **Relative links only.** Never link to `github.com/...` absolute URLs inside the repo — relative
   paths survive renames, forks and a move to a private mirror.
2. **Deep-link into extracts, not PDFs.** GitHub's PDF viewer does not support reliable
   `#page=` anchors, so to point at a specific article use the markdown extract's heading anchor,
   e.g. `extracts/council/ST-9547-2026_gdpr-art3-amendments.md#point-8--article-33-breach-notification`.
3. **Source PDFs are committed in `sources/`.** The Council compromise texts (incl. LIMITE ones)
   are hosted in this repo for transparency and offline diffing; the register also records the
   document number, the Council register reference, and any national-parliament record or public
   mirror so provenance stays traceable. See [`NOTICE`](NOTICE) §2. The markdown extracts in
   [`extracts/`](extracts/) remain the *linkable* working copies, because GitHub's PDF viewer can't
   anchor to a specific article — link `extracts/...md#anchor`, not `sources/...pdf#page`.

## Naming convention for documents

`<INSTITUTIONAL-ID>_<short-description>_<ISO-date>.<ext>`
e.g. `ST-9547-2026_council-presidency-compromise_2026-05-21` — the stable document number first,
ISO date last, so chronological sort always works.

## Contributing / adding a document

Open an issue using [`.github/ISSUE_TEMPLATE/new-document.md`](.github/ISSUE_TEMPLATE/new-document.md),
add the entry to [`data/documents.yaml`](data/documents.yaml), regenerate the register row in
[`sources/README.md`](sources/README.md), and (if it is a new compromise text) add a matching
extract file under [`extracts/`](extracts/).

---

## Disclaimer & licence

This is a **personal project** published in a personal capacity. It is **not legal advice** and does
**not** represent the views of any employer. See **[`DISCLAIMER.md`](DISCLAIMER.md)**.

- Original analysis and commentary in this repo: licensed under **CC BY 4.0** — see [`LICENSE`](LICENSE).
- EU documents and third-party works are **not** covered by that licence — see [`NOTICE`](NOTICE).

<!-- ============================================================================
     STATUS.template.md — reusable one-screen snapshot for a single-file EU
     legislative tracker. Copy to STATUS.md and fill in the <PLACEHOLDERS>.

     Keep the SECTION ORDER and the five per-institution FIELDS fixed — that
     fixed skeleton is what lets sibling trackers be read and compared at a
     glance. Governing spec: docs/reporting-standard.md.

     Two house rules this template enforces:
       1. Every document/report named gets BOTH an internal link (a docs/ digest
          or extracts/ anchor, else its sources/README.md register row — never a
          raw sources/*.pdf) AND its authoritative external URL (from
          data/documents.yaml: url / celex / mirror / national_parliament).
       2. Relative links only for repo-internal targets (no github.com URLs).
     ============================================================================ -->

# Status snapshot — <FILE-ID> (COD)   <!-- e.g. 2025/0360 (COD) -->

| Field | Value |
|---|---|
| **Procedure** | **<FILE-ID> (COD)** — EU Ordinary Legislative Procedure · [Oeil procedure file](<OEIL-URL>) |
| **Proposal** | **<COM-ID> final** (<DATE>)<!-- + SWD-ID if any --> — [digest](docs/commission-proposal.md) · [base-text extracts](extracts/commission/) · [EUR-Lex](<EUR-LEX-URL>) |
| **Legal bases** | <TFEU articles, e.g. Articles 16(2) and 114 TFEU> |
| **OLP stage** | <one line: which reading; where each co-legislator is; whether a general approach / trilogue exists> |
| **Latest text** | <newest authoritative text, e.g. Council ST <nnnn>/<yy> (<date>)> — [operative extracts](extracts/council/) · [register](sources/README.md) |
| **As of** | **<DD Month YYYY>** (= `data/tracker-state.yaml` `last_run`) <!-- set to the DATE of the last tracker run --> |

> Living snapshot — **not legal advice** ([`DISCLAIMER.md`](DISCLAIMER.md)). Procedure is sourced from
> [`sources/`](sources/) + [`TIMELINE.md`](TIMELINE.md); <co-legislator> substance reflects the operative
> text of <LATEST-TEXT> in [`extracts/`](extracts/) — verify before relying on it.

## One-line status

<!-- The 30-second TL;DR: each co-legislator's stage + whether a general approach / trilogue exists. -->
<one or two sentences>

## Where each institution stands

<!-- One block per OLP actor, ALWAYS these five fields in this order. Link DOWN to docs/ and extracts/;
     do NOT duplicate the chronology (that is TIMELINE.md) or provision-by-provision detail (that is
     data/positions.csv + docs/provisions/*). Add " — proposer" / " — co-legislator" to mark the OLP role. -->

### <Proposing institution> — proposer
- **Stage:** <where this actor is in the procedure>
- **Latest act:** <newest doc/event> — [digest](<internal>) · [source](<external-url>)
- **Owner:** <who holds it: DG / Commissioner / Presidency / rapporteur(s)>
- **Position:** <one-line substantive stance; link down for detail>
- **Next:** <this actor's next expected step>

### <Co-legislator 1> — co-legislator
- **Stage:** <…>
- **Latest act:** <…> — [extracts](<internal>) · [register / source](<external-url>)
- **Owner:** <…>
- **Position:** <…>
- **Next:** <…>

### <Co-legislator 2> — co-legislator
- **Stage:** <…>
- **Latest act:** <…>
- **Owner:** <…>
- **Position:** <…>
- **Next:** <…>

### Advisory bodies & Member States

<!-- Compact table, not five fields: one row per advisory body, then one summary row for Member States.
     Add/remove body rows as the file attracts opinions. Each row: internal digest + external source. -->

| Body | Latest act (date) | Position |
|---|---|---|
| **<advisory body>** | <opinion + date> — [digest](docs/advisory/<slug>.md) · [source](<external-url>) | <one-line stance> |
| **Member States** | <key national positions + delegation streams> — [source](<external-url>) · [register](sources/README.md) | <one-line summary> — [`docs/member-state-positions.md`](docs/member-state-positions.md) |

## Next milestones to watch

<!-- Cross-institution forward look. Checkboxes = not-yet-happened. Date each item where possible; flag any
     item sourced only via a national parliament as "verify against the institution". KEEP THIS HEADING
     VERBATIM — the register-document / resolve-tracker-issue skills route new milestones to it by name. -->

- [ ] <dated upcoming event>
- [ ] <expected co-legislator step>
- [ ] <watch-item: a contested provision that could reopen>

## What changed in the latest text vs earlier reporting

<!-- OPTIONAL but recommended once a compromise text diverges from first reporting. The "myth-buster":
     stops people asserting features that were later deleted/moved. Keep the HEADING generic ("the latest
     text") so it survives new versions; name the specific version in the intro line. This is the authority
     on what moved — referenced by CLAUDE.md and the skills. Omit the section only if nothing has diverged. -->

Operative text: **<LATEST-TEXT + date>**. Several widely-reported features of <earlier baseline> **moved**
by this text — this table is the authority on what moved; corrections are built into the
[extracts](extracts/) and [`data/positions.csv`](data/positions.csv).

| Topic | Earlier reporting (<baseline>) | Latest operative text (<LATEST-TEXT>) |
|---|---|---|
| **<provision>** | <what was reported> | <what the operative text actually says> |

Faithful operative text behind each row: [`extracts/<path-to-amendments-file>.md`](extracts/).

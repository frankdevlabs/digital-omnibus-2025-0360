# Status snapshot

**As of:** 27 May 2026
**File:** 2025/0360 (COD) — Commission proposal COM(2025) 837 final (19 November 2025)
**Legal bases:** Articles 16(2) and 114 TFEU

> ⚠️ This file is a living snapshot. Procedural facts below are sourced from the
> [`sources/`](sources/) register and [`TIMELINE.md`](TIMELINE.md). Substantive statements about the
> Council position reflect the **operative text of ST 9547/26 (21 May 2026)** as transcribed in
> [`extracts/council/`](extracts/council/) — verify against the authoritative text before relying on it.

## One-line status

Council **working-party stage** (third Cyprus Presidency compromise text); European Parliament
**joint ITRE/LIBE scrutiny, no draft report yet**; **no general approach and no trilogue** has begun.
Cyprus has publicly conceded the file will pass to the **Irish Presidency (from 1 July 2026)** unclosed.

## Where each institution stands

### European Commission
- Proposal adopted by the College **19 November 2025** (COM(2025) 837 final; SWD(2025) 836).
- Framing: "simplicity by design", competitiveness (Draghi), ≥25% burden reduction (35% for SMEs).
- Owners: EVP Henna Virkkunen (Tech Sovereignty), Commissioner Michael McGrath (Justice/DG JUST),
  with DG CNECT. Maintains it codifies CJEU case law and does not lower GDPR standards.
- The proposal is now mirrored in this repo: source committed under [`sources/commission/`](sources/),
  base-text operative extracts under [`extracts/commission/`](extracts/commission/) (the diff baseline for
  the Council texts), and an explanatory-memorandum digest in
  [`docs/commission-proposal.md`](docs/commission-proposal.md).

### Council of the EU
- Handled in the **Antici Group on Simplification (AGS)**, with DATAPROTECT / CYBER / TELECOM / COMPET input.
- **Cyprus Presidency** (Jan–Jun 2026) has produced three compromise texts:
  - **ST 6406/26** — 20 Feb 2026 (for AGS 27 Feb)
  - **ST 8261/26** — 15 Apr 2026 (for AGS 24 Apr)
  - **ST 9547/26** — 21 May 2026 (for AGS **27 May 2026**) ← current
- The 27 May AGS meeting is an **exchange of views**, *not* a vote on a general approach.
- No general approach expected before H2 2026 under the **Irish Presidency**.

### European Parliament
- **Joint committee** under Rule 58: **ITRE (lead)** + **LIBE**; **JURI** opinion.
- Rapporteurs: **Aura Salla** (EPP, FI / ITRE) and **Marina Kaljurand** (S&D, EE / LIBE);
  JURI opinion rapporteur **Ton Diepeveen** (PfE, NL).
- **No joint draft report tabled** as of 27 May 2026. Oeil status: *Awaiting committee decision*.
- Salla's appointment is contested (prior Meta EU public-policy role) — civil-society call to withdraw.

## Next milestones to watch

- [ ] Publication of the joint ITRE/LIBE **draft report** (Parliament's first formal position).
- [ ] **Council general approach** (likely under Irish Presidency, H2 2026).
- [ ] Start of **trilogue** (earliest Q4 2026).
- [ ] EDPB DPIA-template consultation (deadline ~9 June 2026); updated pseudonymisation guideline.
- [ ] Any reopening of the **Art 4 personal-data** redefinition (currently deleted in the Council text).

---

## ⚠️ What changed in ST 9547/26 (21 May 2026) vs earlier reporting

Several widely-reported features of the Commission proposal and the **February** compromise have
**moved** by the 21 May text. These corrections are built into the extracts and provision files:

| Topic | Earlier reporting (Commission / Feb compromise) | ST 9547/26 (21 May 2026) — operative text |
|---|---|---|
| **Art 4 personal-data redefinition** | Commission adds relative-controller clause | **Deleted** (point 1(a) struck) — Art 4(1) unchanged |
| **Scientific-research definition (Art 4(38))** | Reported *deleted* in Feb compromise | **Re-included, reworked** — definition present in the May text |
| **Cookies — GDPR Art 88a** | Commission moves cookie consent *into* the GDPR | **Deleted** — cookie consent kept in **ePrivacy Dir Art 5(3)** (amended by Art 5 of the Omnibus) |
| **AI legitimate interest — GDPR Art 88c** | Commission adds a standalone AI Art 6(1)(f) article | **Deleted** — basis now carried only by **recital 33a**; recitals 30 & 31 also deleted |
| **Machine-readable consent — Art 88b** | New browser/OS consent-signal duties | **Retained** (renumbered; verify final number) |
| **Art 22 automated decisions** | Commission rewrite weakening contractual-necessity test | **Largely restored to current GDPR**; the "regardless of whether…" clause in (a) deleted |
| **P2B Regulation 2019/1150** | Reported *repealed* | **Partially amended** — Arts 2(11), 2(12), 6, 8–10, 12–14, 16–18 deleted; not wholly repealed |
| **Breach notification (Art 33)** | 72h, broad threshold | **96h**, **high-risk-only** threshold, via national entry point |
| **National-entry-point reporting** | 24 months | **30 months** from entry into force |

See [`extracts/council/ST-9547-2026_gdpr-art3-amendments.md`](extracts/council/ST-9547-2026_gdpr-art3-amendments.md)
for the faithful operative text behind each of these.

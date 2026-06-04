# Document register

Single human-readable index of every official document on file **2025/0360 (COD)**.
Generated from [`../data/documents.yaml`](../data/documents.yaml) — edit the YAML, then update this table.

**LIMITE handling:** Council documents marked LIMITE **are committed** as PDFs under
[`council/`](council/) for transparency and offline diffing (see [`../NOTICE`](../NOTICE)); for each,
the register records full provenance — the document number, the authoritative register reference, and
a national-parliament record or public mirror where one exists.
Operative text of the Council compromise texts is transcribed under
[`../extracts/council/`](../extracts/council/).

## Commission

| ID | Title | Date | Hosted file | Link |
|---|---|---|---|---|
| COM(2025) 47 final | Communication "A simpler and faster Europe" | 2025-02-11 | — | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=COM:2025:47:FIN) |
| **COM(2025) 837 final** | **Digital Omnibus proposal** (+ SWD(2025) 836) | 2025-11-19 | [`commission/COM-2025-837_proposal_2025-11-19.docx`](commission/COM-2025-837_proposal_2025-11-19.docx) · [Annex I](commission/COM-2025-837_annex1-correlation-tables_2025-11-19.docx) | [EUR-Lex procedure](https://eur-lex.europa.eu/procedure/EN/2025_360) · [CELEX 52025PC0837](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025PC0837) |

Base-text operative extracts of the proposal are transcribed under
[`../extracts/commission/`](../extracts/commission/) (the diff baseline for the Council compromise texts).

## Council documents

PDFs are committed under [`council/`](council/) where held. The register also records the document
number, the Council register reference (which 404s while a document remains unreleased — cited by
number, not asserted as live), and a national-parliament record or public mirror where one exists.

> **Accessing Council documents.** The EU Law Tracker links each document by its `ImmcIdentifier`,
> which plugs straight into a register URL:
> `https://data.consilium.europa.eu/doc/document/{ImmcIdentifier}/en/pdf`
> (e.g. `ST-6311-2026-INIT`, `ST-15698-2025-ADD-1`). Caveats: **LIMITE** compromise texts
> (ST 6406/8261/9547) are not released — the register 404s and we rely on national-parliament records
> or press mirrors; ordinary **ST notes/agendas** are usually downloadable unless still LIMITE. For
> this file many **WK** working notes (e.g. the WK 3735/26 and WK 3736/26 addenda) *are* being released
> on the register and via mirrors (some on `table.media`) — see those entries.

| ID | Title | Date | Hosted file | Provenance (number · register · NP/mirror) |
|---|---|---|---|---|
| ST 16131/1/25 REV 1 | *Simplification* — 2025 Annual Overview/Progress Reports (horizontal note; Coreper 5 Dec, Council 16 Dec) | 2025-12-04 | — (screenshot only) | ST 16131/1/25 REV 1 · [register](https://data.consilium.europa.eu/doc/document/ST-16131-2025-REV-1/en/pdf) · not DO-specific — no 2025/0360 file header |
| ST 15698/25 | Council transmission of the proposal (= COM(2025) 837: INIT proposal · ADD 1 corr. tables · ADD 2 ≈ SWD 836) | 2025-12-12 | see [`commission/COM-2025-837_proposal_2025-11-19.docx`](commission/COM-2025-837_proposal_2025-11-19.docx) | ST 15698/25 · [register](https://data.consilium.europa.eu/doc/document/ST-15698-2025-INIT/en/pdf) · content duplicate of the COM files |
| ST 6311/26 | Coreper 'I'-item note — EDPB/EDPS attendance at the 27 Feb AGS (approved 18 Feb) | 2026-02-13 | [`council/ST-6311-2026_coreper-i-item-edpb-edps-attendance_2026-02-13.pdf`](council/ST-6311-2026_coreper-i-item-edpb-edps-attendance_2026-02-13.pdf) | ST 6311/26 · [register](https://data.consilium.europa.eu/doc/document/ST-6311-2026-INIT/en/pdf) · LIMITE, public-release watermark |
| WK 3735/26 (INIT + ADD 1–4) | Delegations' comments — **cyber/data** strand (Commission proposal): consolidated (15 MS) + CZ, EE, AT, DK | 2026‑03‑11 → 03‑23 | [INIT](council/WK-3735-2026-INIT_consolidated-comments-cyber-data_2026-03-11.pdf) · [ADD1·CZ](council/WK-3735-2026-ADD1_delegation-comments-cz-cyber-data_2026-03-11.pdf) · [ADD2·EE](council/WK-3735-2026-ADD2_delegation-comments-ee-cyber-data_2026-03-12.pdf) · [ADD3·AT](council/WK-3735-2026-ADD3_delegation-comments-at-cyber-data_2026-03-18.pdf) · [ADD4·DK](council/WK-3735-2026-ADD4_delegation-comments-dk-cyber-data_2026-03-23.pdf) | WK 3735/26 · [register](https://data.consilium.europa.eu/doc/document/WK-3735-2026-INIT/en/pdf) · positions in [`../docs/member-state-positions.md`](../docs/member-state-positions.md) |
| ST 6406/26 | Presidency compromise text (rev 1) | 2026-02-20 | [`council/ST-6406-2026_council-presidency-compromise_2026-02-20.pdf`](council/ST-6406-2026_council-presidency-compromise_2026-02-20.pdf) | ST 6406/26 · [register](https://data.consilium.europa.eu/doc/document/ST-6406-2026-INIT/en/pdf) · [netzpolitik mirror](https://netzpolitik.org/wp-upload/2026/02/Presidency-compromise-text-on-Omnibus-VII-%E2%80%93-Digital-GDPR-P2B.pdf) |
| WK 3736/26 (ADD 1–4) | Delegations' comments — **GDPR/P2B/ePrivacy** strand: consolidated coalitions + DE, EE, FR/PL/RO | 2026‑03‑19 → 03‑30 | [ADD1·consolidated](council/WK-3736-2026-ADD1_consolidated-comments-gdpr-p2b_2026-03-19.pdf) · [ADD2·DE](council/WK-3736-2026-ADD2_delegation-comments-de-gdpr-p2b_2026-03-19.pdf) · [ADD3·EE](council/WK-3736-2026-ADD3_delegation-comments-ee-gdpr-p2b_2026-03-23.pdf) · [ADD4·FR/PL/RO](council/WK-3736-2026-ADD4_delegations-comments-fr-pl-ro_2026-03-30.pdf) | WK 3736/26 · [register](https://data.consilium.europa.eu/doc/document/WK-3736-2026-INIT/en/pdf) · [table.media mirror (ADD 4)](https://table.media/assets/berlin/digital-omnibus-march-30-gdpr,-p2b,-eprivacy-fr,-ro,-pl-(1).pdf) · positions in [`../docs/member-state-positions.md`](../docs/member-state-positions.md) |
| ST 7244/26 | Cover note transmitting **ECB Opinion CON/2026/9** to the Council | 2026-03-11 | — (screenshot only) | ST 7244/26 · [register](https://data.consilium.europa.eu/doc/document/ST-7244-2026-INIT/en/pdf) · opinion held under [advisory](#advisory-bodies--national-parliaments) |
| ST 8261/1/26 REV 1 | Presidency compromise text (rev 2) | 2026-04-17 | [`council/ST-8261-1-26-REV1_council-presidency-compromise_2026-04-17.pdf`](council/ST-8261-1-26-REV1_council-presidency-compromise_2026-04-17.pdf) | ST 8261/1/26 REV 1 · [agenda CM 2463/26](https://data.consilium.europa.eu/doc/document/CM-2463-2026-INIT/en/pdf) · NP: search parlament.gv.at "8261" |
| **ST 9547/26** | **Presidency compromise text (rev 3)** ← current | 2026-05-21 | **[`council/ST-9547-2026_council-presidency-compromise_2026-05-21.pdf`](council/ST-9547-2026_council-presidency-compromise_2026-05-21.pdf)** | ST 9547/26 · [register](https://data.consilium.europa.eu/doc/document/ST-9547-2026-INIT/en/pdf) · [Austrian Parliament record](https://www.parlament.gv.at/gegenstand/XXVIII/EU/73322) |
| CM 2918/26 | AGS meeting agenda (27 May) | 2026-05-22 | _optional_ | CM 2918/26 · [register](https://data.consilium.europa.eu/doc/document/CM-2918-2026-INIT/en/pdf) |

## European Parliament

| ID | Title | Date | Link |
|---|---|---|---|
| 2025/0360(COD) | Oeil procedure file | 2026-01-19 | [Oeil](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0360(COD)) |
| — | Legislative Train entry | 2026-04-20 | [legislative-train](https://www.europarl.europa.eu/legislative-train/theme-a-new-plan-for-europe-s-sustainable-prosperity-and-competitiveness/file-digital-package) |
| — | EU Law Tracker procedure 2025/360 | 2026-05-01 | [law-tracker](https://law-tracker.europa.eu/procedure/2025_360?lang=en) |

## Member-state positions

National-government positions on the file, as distinct from Council *delegation* comments circulated
through the `WK` consultation stream (those are noted under [Council documents](#council-documents) and
summarised in [`../docs/member-state-positions.md`](../docs/member-state-positions.md)).

| State | Item | Date | Hosted file | Provenance |
|---|---|---|---|---|
| Netherlands (NL) | **Non-paper on the far-reaching GDPR changes in the Digital Omnibus** (Staatssecretaris Van Bruggen, Justice & Security) — "clean cut" of the fundamental-rights GDPR changes out of the Omnibus | 2026-04-08 | [`member-states/NL-NONPAPER-2026-04-08_non-paper-gdpr-changes_2026-04-08.pdf`](member-states/NL-NONPAPER-2026-04-08_non-paper-gdpr-changes_2026-04-08.pdf) · [Kamerbrief](member-states/NL-NONPAPER-2026-04-08_kamerbrief_2026-04-08.pdf) | [rijksoverheid.nl](https://www.rijksoverheid.nl/documenten/2026/04/08/tk-non-paper-digitale-omnibus-avg) · sent to Tweede + Eerste Kamer · positions in [`../docs/member-state-positions.md`](../docs/member-state-positions.md#netherlands-nl--national-non-paper-8-april-2026) |

## EDPB / EDPS

| ID | Title | Date | Hosted file | Link |
|---|---|---|---|---|
| Joint Opinion 2/2026 | EDPB–EDPS joint opinion on the Digital Omnibus | 2026-02-10 | [`edpb-edps/EDPB-EDPS-JO-2-2026_opinion_2026-02-10.pdf`](edpb-edps/EDPB-EDPS-JO-2-2026_opinion_2026-02-10.pdf) | [EDPB](https://www.edpb.europa.eu/our-work-tools/our-documents/edpbedps-joint-opinion/edpb-edps-joint-opinion-22026-proposal_en) · [digest](../docs/advisory/edpb-edps-jo-2-2026.md) |

## Advisory bodies / national parliaments

| Body | Item | Date | Hosted file | Link |
|---|---|---|---|---|
| EESC | Opinion **INT/1108** (covers 2025/0359 & 2025/0360); rapporteur Willems | 2026-03-18 | [`advisory/EESC-2025-03929_opinion-int1108_2026-03-18.docx`](advisory/EESC-2025-03929_opinion-int1108_2026-03-18.docx) | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=PI_EESC:EESC-2025-03929-AS) · [digest](../docs/advisory/eesc-int1108.md) |
| ECB | Opinion **CON/2026/9** (requested by EP 9 Dec 2025; broadly supportive); cover note ST 7244/26 | 2026-03-10 | [`advisory/ECB-CON-2026-9_opinion_2026-03-10.pdf`](advisory/ECB-CON-2026-9_opinion_2026-03-10.pdf) | [EUR-Lex (CELEX 52026AB0009)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026AB0009) · [digest](../docs/advisory/ecb-con-2026-9.md) |
| Committee of the Regions | Mandatory consultee (Art named in COM(2025) 837); no opinion tracked yet | — | — | — |
| Czech Senate | Protocol 2 contribution | 2026-02-13 | — | — |
| Italian Camera dei Deputati | Observations | 2026-02-24 | — | — |

## Stakeholders

| Body | Item | Date | Link |
|---|---|---|---|
| noyb | "EU Commission wants to wreck core GDPR principles" | 2025-11-19 | [noyb](https://noyb.eu/en/digital-omnibus-eu-commission-wants-wreck-core-gdpr-principles) |
| noyb | Access-request "reality check" (83.5% non-compliant) | 2026-04-16 | [noyb](https://noyb.eu/en/digital-omnibus-reality-check-835-access-requests-not-properly-answered) |
| EDRi | "A step back from the brink, the risks remain" | 2026-03 | [EDRi](https://edri.org/our-work/the-digital-omnibus-a-step-back-from-the-brink-but-the-risks-remain/) |
| Industry (CCIA/DOT Europe/AI Chamber) | Open letter to Council | 2026-05 | [AI Chamber](https://aichamber.eu/wp-content/uploads/2026/05/Open-Letter_Digital-Omnibus_EU-Council.pdf) |

# Institutional positions — Commission vs Council vs Parliament

This is the core comparison. The **Council** column reflects the operative text of **ST 9547/26
(21 May 2026)** as transcribed in [`../extracts/council/`](../extracts/council/) — which differs
from earlier reporting on several points (see [`../STATUS.md`](../STATUS.md)). The **Parliament**
column is provisional: the EP has taken no substantive step — the
[Oeil procedure file](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0360(COD))
shows status *Awaiting committee decision* with no key event beyond the 19 Jan 2026 committee
referral, and no joint ITRE/LIBE draft report exists yet. Entries therefore reflect rapporteur
statements, committee debate and group signals only.

Per-provision detail lives in [`provisions/`](provisions/). Machine-readable version:
[`../data/positions.csv`](../data/positions.csv) — which additionally carries **ECB**, **EESC** and
**member-state** columns alongside EDPB–EDPS. For positions of *individual* Council delegations
(France, Poland, Romania, Germany, Estonia, Czechia, Austria, Denmark) behind the Council column, see
[`member-state-positions.md`](member-state-positions.md). The **EDPB–EDPS** column distils
**Joint Opinion 2/2026** — full digest in [`advisory/edpb-edps-jo-2-2026.md`](advisory/edpb-edps-jo-2-2026.md);
the ECB ([CON/2026/9](advisory/ecb-con-2026-9.md)) and EESC ([INT/1108](advisory/eesc-int1108.md))
opinions are digested under [`advisory/`](advisory/).

| Topic | Commission (COM(2025) 837) | Council (ST 9547/26) | Parliament (provisional) | EDPB–EDPS |
|---|---|---|---|---|
| **Personal-data definition (Art 4(1))** | Adds relative/controller-centric clause; codifies *EDPS v SRB* (C-413/23 P) | **Deleted** — Art 4(1) unchanged ([extract](../extracts/council/ST-9547-2026_gdpr-art3-amendments.md#point-1--article-4-definitions)) | Hostile (Kaljurand, centre-left) | **Strongly opposes** redefinition |
| **Pseudonymisation & by-design (Art 29a, Art 25)** | Commission implementing power (Art 41a) | **Art 41a deleted** → EDPB-opinion **Art 29a**; Art 25 extended to processors ([extract](../extracts/council/ST-9547-2026_gdpr-art3-amendments.md#point-10--article-29a-pseudonymisation)) | Open | Supports deleting Art 41a; scope-rules in primary law |
| **Scientific-research definition (Art 4(38))** | New definition | **Re-included, reworked** in May text | Open | Cautious; wants tighter wording |
| **AI special-category derogation (Art 9(2)(k), 9(5))** | New derogation for incidental processing | **Retained, tightened** (avoid → erase → safeguard, with documentation) | Likely strict-necessity standard | Wants strict necessity |
| **Biometric verification (Art 9(2)(l))** | New derogation under sole control | **Retained with safeguards** (one-to-one, possession, MS/Union legal basis) | Likely support tightening | Welcomed |
| **Abuse-of-rights / DSAR (Art 12(5), 57)** | Refuse where reasonable grounds of other purpose | **Retained but reformulated** — "abusive intention" must be demonstrated | Likely tighten | Criticises link to *purpose* of request |
| **Transparency exemptions (Art 13(4)/(5))** | Broad exemption in "clear and circumscribed" relationships | **Retained, narrowed** to low-risk, limited-purpose contexts | Likely narrow further | Cautious |
| **Automated decisions (Art 22)** | Rewrite weakening contractual-necessity test | **Largely restored to current GDPR**; "regardless of whether…" clause in (a) deleted | Likely side with Council | Welcomed |
| **Breach notification (Art 33)** | High-risk threshold; **72h**; EDPB template | High-risk threshold; **96h**; via national entry point; EDPB lists/template | Likely support | **Welcomed** threshold + 96h |
| **DPIA EU-list (Art 35)** | Commission implementing acts | **Retained, power moved to EDPB** | Likely support EDPB-led mechanism | Supports EDPB role |
| **EDPB tasks/consistency & DPO contact (Art 64, 70, 37(7))** | EDPB prepares proposals; Art 64(1)(a)/70(1)(h) deleted | **EDPB establishes** lists/templates + Art 32 guidance + Art 29a opinion ([extract](../extracts/council/ST-9547-2026_gdpr-art3-amendments.md#points-1214--articles-64--70-edpb-tasks-and-consistency)) | Open | Wants EDPB to prepare *and approve* |
| **Cookies / terminal equipment** | Move consent into GDPR (**Art 88a**); 6-month no-repeat; consent-exempt purposes | **GDPR Art 88a deleted** — consent **kept in ePrivacy Dir Art 5(3)** (amended), with 6-month rule & exempt purposes ([extract](../extracts/council/ST-9547-2026_eprivacy-art5.md)) | Highly contested | Mixed |
| **Machine-readable consent signals (Art 88b)** | New browser/OS duties | **Retained** (renumbered; numbering unsettled) | Contested (industry wants deletion; rights side wants stronger) | Supports stronger signals |
| **AI legitimate interest (Art 88c)** | New standalone Art 6(1)(f) article | **Deleted** — basis carried only by **recital 33a**; recitals 30 & 31 also deleted | EDRi/noyb push deletion; EPP/Renew supportive | **Opposes** standalone article |
| **Single-entry point (NIS2 Art 23a-d; DORA/CER/eIDAS)** | ENISA SEP; report once, share many; 18–24 months | **Retained** — ENISA info point + Member State national entry points; 30-month reporting switch-over | Broadly supported | Supports with safeguards |
| **Repeals (DGA / P2B / FFNPD / Open Data)** | Repeal + consolidate into Data Act | **DGA, FFNPD, Open Data repealed; P2B partially amended** (key articles deleted, not wholly repealed) | Defensive on data altruism | Out of remit |
| **EUDPR mirror (Omnibus Art 4)** | Point-for-point mirror of the GDPR changes ([extract](../extracts/commission/COM-2025-837_eudpr-art4.md)) | **Not operatively amended**; alignment deferred (rec 43) | Open | GDPR comments apply equally; reject EUDPR Art 39 amendment |

## Reading the table

**Converging (likely smooth):** breach notification (high-risk + 96h), the EU-level DPIA list via
the EDPB, biometric verification with safeguards, the single-entry point, and the data-acquis
consolidation. On these the Council text is broadly compatible with the EDPB–EDPS opinion, so a
Parliament majority is realistic.

**Diverging sharply (the trilogue battles):** see [`fault-lines.md`](fault-lines.md). The hardest
four are the personal-data concept, the AI legitimate-interest basis, the cookie/consent regime
(now relocated to ePrivacy by the Council), and the abuse-of-rights provision. On all four the
**Council has already pulled back** from the Commission's most deregulatory drafting; the
**Parliament is expected to go further still** in tightening or deleting.

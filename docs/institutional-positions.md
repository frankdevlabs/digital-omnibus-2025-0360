# Institutional positions — Commission vs Council vs Parliament

This is the core comparison. The **Council** column reflects the operative text of **ST 9547/26
(21 May 2026)** as transcribed in [`../extracts/council/`](../extracts/council/) — which differs
from earlier reporting on several points (see [`../STATUS.md`](../STATUS.md)). The table is baselined
to ST 9547/26; for the **ST 10729/26 (22 Jun)** delta — including the **new Art 49 / recital 40b
third-country tax-transfer derogation** added in the row below — see [`what-changed.md`](what-changed.md). The **Parliament**
column is provisional: these are committee-**for-opinion** drafts, and the lead **joint ITRE/LIBE
draft report** — Parliament's first cross-strand position — is **still pending** (the
[Oeil procedure file](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0360(COD))
shows status *Awaiting committee decision*). Where a committee has **tabled an amendment** the cell
cites it; where neither committee has, the cell reflects rapporteur statements, committee debate and
group signals only. The first committee-for-opinion text — the
**JURI draft opinion** (rapporteur Benifei, S&D, PE789.142v01-00, 5 Jun 2026;
[register](../sources/README.md#european-parliament)) — is now transcribed
([extract, 68 amendments](../extracts/parliament/JURI-PA-789142_draft-opinion.md)) and targets the
**data-acquis strand** (Data Act / DGA / P2B / Open Data), so it is **silent on the GDPR-strand**
provisions in the table below. The JURI position is captured on the affected pages:
[Data Act](instruments/data-act-2023-2854.md#parliament--juri-draft-opinion) and the
[P2B repeal](provisions/final-repeals-p2b.md#parliament--juri-draft-opinion).

The second committee-for-opinion text — the **IMCO draft opinion** (rapporteur Agius Saliba, S&D,
PE789.877v01-00, cover dated 8 Jun 2026; [register](../sources/README.md#european-parliament)) — is
likewise transcribed ([extract, 124 amendments](../extracts/parliament/IMCO-PA-789877_draft-opinion.md)).
Explicitly **limited to IMCO's competence** (the rapporteur warns that un-amended parts should not be
read as endorsed), it runs counter-current to the Omnibus's deregulation: it **restores the P2B
Regulation** (rejecting the repeal of Reg (EU) 2019/1150 without a proper impact assessment),
**rejects the deletion of smart contracts** (Art 36 Data Act), **restores the current Data Act
cloud-switching regime**, adds a **data-expert-representative** form of regulated data-intermediation
service acting under a fiduciary duty for consumers, and tightens trade-secret, B2G, data-altruism
transparency and enforcement/supervision safeguards. **Unlike JURI, IMCO also opines across the
GDPR strand** (on the internal-market / consumer angle of its competence): it deletes the Art 4(1)
redefinition, the Art 9(2)(k) AI carve-out, Art 88c and the Art 12(5) abuse-of-rights restriction,
**strengthens** the Art 88b machine-readable-signal regime, and extends DPA enforcement to software
providers — so the **GDPR-strand cells below now carry IMCO's tabled positions**, not just group
signals. Data-acquis substance is captured on
[Data Act](instruments/data-act-2023-2854.md#parliament-imco-draft-opinion) and the
[P2B repeal](provisions/final-repeals-p2b.md#parliament-imco-draft-opinion); GDPR-strand detail on
the per-provision pages in [`provisions/`](provisions/).

Per-provision detail lives in [`provisions/`](provisions/). Machine-readable version:
[`../data/positions.csv`](../data/positions.csv) — which additionally carries **ECB**, **EESC** and
**member-state** columns alongside EDPB–EDPS. For positions of *individual* Council delegations
(France, Poland, Romania, Germany, Estonia, Czechia, Austria, Denmark) behind the Council column, see
[`member-state-positions.md`](member-state-positions.md). The **EDPB–EDPS** column distils
**Joint Opinion 2/2026** — full digest in [`advisory/edpb-edps-jo-2-2026.md`](advisory/edpb-edps-jo-2-2026.md);
the ECB ([CON/2026/9](advisory/ecb-con-2026-9.md)) and EESC ([INT/1108](advisory/eesc-int1108.md))
opinions are digested under [`advisory/`](advisory/). The EDPB **reaffirmed** its opposition to the
personal-data redefinition at its **10 June 2026 plenary** (meeting with Commissioner McGrath) —
see [`../TIMELINE.md`](../TIMELINE.md).

| Topic | Commission (COM(2025) 837) | Council (ST 9547/26) | Parliament (provisional) | EDPB–EDPS |
|---|---|---|---|---|
| **Personal-data definition (Art 4(1))** | Adds relative/controller-centric clause; codifies *EDPS v SRB* (C-413/23 P) | **Deleted** — Art 4(1) unchanged ([extract](../extracts/council/ST-9547-2026_gdpr-art3-amendments.md#point-1--article-4-definitions)) | **IMCO deletes** the redefinition ([Am 98](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-98)); JURI silent | **Strongly opposes** redefinition |
| **Pseudonymisation & by-design (Art 29a, Art 25)** | Commission implementing power (Art 41a) | **Art 41a deleted** → EDPB-opinion **Art 29a**; Art 25 extended to processors ([extract](../extracts/council/ST-9547-2026_gdpr-art3-amendments.md#point-10--article-29a-pseudonymisation)) | **IMCO deletes** Art 41a ([Am 111](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-111)) | Supports deleting Art 41a; scope-rules in primary law |
| **Scientific-research definition (Art 4(38))** | New definition | **Re-included, reworked** in May text | No committee amendment; open | Cautious; wants tighter wording |
| **AI special-category derogation (Art 9(2)(k), 9(5))** | New derogation for incidental processing | **Retained, tightened** (avoid → erase → safeguard, with documentation) | **IMCO deletes** 9(2)(k) + 9(5) ([Am 100–101](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-100)) — stronger than Council | Wants strict necessity |
| **Biometric verification (Art 9(2)(l))** | New derogation under sole control | **Retained with safeguards** (one-to-one, possession, MS/Union legal basis) | No committee amendment; likely support tightening | Welcomed |
| **Abuse-of-rights / DSAR (Art 12(5), 57)** | Refuse where reasonable grounds of other purpose | **Retained but reformulated** — "abusive intention" must be demonstrated | **IMCO removes** the restriction + adds an anti-circumvention duty ([Am 103–107](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-103)) | Criticises link to *purpose* of request |
| **Transparency exemptions (Art 13(4)/(5))** | Broad exemption in "clear and circumscribed" relationships | **Retained, narrowed** to low-risk, limited-purpose contexts | No operative amendment; IMCO recital 44 tightens ([Am 21](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-21)) | Cautious |
| **Automated decisions (Art 22)** | Rewrite weakening contractual-necessity test | **Largely restored to current GDPR**; "regardless of whether…" clause in (a) deleted | No committee amendment; likely side with Council | Welcomed |
| **Breach notification (Art 33)** | High-risk threshold; **72h**; EDPB template | High-risk threshold; **96h**; via national entry point; EDPB lists/template | **IMCO**: EDPB publishes the template + non-regression safeguard on the SEP ([Am 108–110](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-108)) | **Welcomed** threshold + 96h |
| **DPIA EU-list (Art 35)** | Commission implementing acts | **Retained, power moved to EDPB** | No committee amendment; likely support EDPB-led mechanism | Supports EDPB role |
| **EDPB tasks/consistency & DPO contact (Art 64, 70, 37(7))** | EDPB prepares proposals; Art 64(1)(a)/70(1)(h) deleted | **EDPB establishes** lists/templates + Art 32 guidance + Art 29a opinion ([extract](../extracts/council/ST-9547-2026_gdpr-art3-amendments.md#points-1214--articles-64--70-edpb-tasks-and-consistency)) | **IMCO**: EDPB publishes lists/templates; DPA powers + fines extended to software providers ([Am 112–114](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-112)) | Wants EDPB to prepare *and approve* |
| **Cookies / terminal equipment** | Move consent into GDPR (**Art 88a**); 6-month no-repeat; consent-exempt purposes | **GDPR Art 88a deleted** — consent **kept in ePrivacy Dir Art 5(3)** (amended), with 6-month rule & exempt purposes ([extract](../extracts/council/ST-9547-2026_eprivacy-art5.md)) | **IMCO** caps gatekeeper re-prompts + voids re-requested consent ([Am 115–116](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-115)); opposes deleting ePrivacy Art 4 ([Am 122](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-122)) | Mixed |
| **Third-country tax transfers (Art 49 / recital 40b)** | Silent — Chapter V / Art 49 untouched | **NEW in ST 10729/26 (22 Jun)** — Art 49(1)(d) replaced + (4) deleted + interpretive recital 40b → periodic/automated FATCA-style tax-data transfers under the public-interest derogation; no impact assessment ([extract](../extracts/council/ST-10729-2026_gdpr-art3-amendments.md#point-10a--article-49-tax-transfers)) | No committee opinion | Not consulted on this addition |
| **Machine-readable consent signals (Art 88b)** | New browser/OS duties | **Retained** (renumbered; numbering unsettled) | **IMCO strengthens** — tech-neutral, drops SME carve-out, 48 → 18 mo, anti-dark-pattern ([Am 117–120](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-117)) | Supports stronger signals |
| **AI legitimate interest (Art 88c)** | New standalone Art 6(1)(f) article | **Deleted** — basis carried only by **recital 33a**; recitals 30 & 31 also deleted | **IMCO deletes** Art 88c + recitals 30/31 ([Am 121](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-121)); EDRi/noyb push deletion, EPP/Renew more open to a recital | **Opposes** standalone article |
| **Single-entry point (NIS2 Art 23a-d; DORA/CER/eIDAS)** | ENISA SEP; report once, share many; 18–24 months | **Retained** — ENISA info point + Member State national entry points; 30-month reporting switch-over | Broadly supported; **IMCO** adds a non-regression safeguard ([Am 110](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-110)) | Supports with safeguards |
| **Repeals (DGA / P2B / FFNPD / Open Data)** | Repeal + consolidate into Data Act | **DGA, FFNPD, Open Data repealed; P2B partially amended** (key articles deleted, not wholly repealed) | **JURI + IMCO oppose the P2B repeal** and largely reverse the data-acquis deregulation ([IMCO Am 123–124](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-123)) | Out of remit |
| **EUDPR mirror (Omnibus Art 4)** | Point-for-point mirror of the GDPR changes ([extract](../extracts/commission/COM-2025-837_eudpr-art4.md)) | **Not operatively amended**; alignment deferred (rec 43) | No committee amendment; open | GDPR comments apply equally; reject EUDPR Art 39 amendment |

## Reading the table

**Converging (likely smooth):** breach notification (high-risk + 96h), the EU-level DPIA list via
the EDPB, biometric verification with safeguards, the single-entry point, and the data-acquis
consolidation. On these the Council text is broadly compatible with the EDPB–EDPS opinion, so a
Parliament majority is realistic.

**Diverging sharply (the trilogue battles):** see [`fault-lines.md`](fault-lines.md). The hardest
four are the personal-data concept, the AI legitimate-interest basis, the cookie/consent regime
(now relocated to ePrivacy by the Council), and the abuse-of-rights provision. On all four the
**Council has already pulled back** from the Commission's most deregulatory drafting; the **IMCO
draft opinion confirms the Parliament will go further still** — deleting the Art 9(2)(k) AI carve-out
the Council only tightened, removing the abuse-of-rights restriction the Council merely reformulated,
and *strengthening* (not deleting) the Art 88b consent-signal regime. These remain committee-for-opinion
positions pending the joint ITRE/LIBE draft report.

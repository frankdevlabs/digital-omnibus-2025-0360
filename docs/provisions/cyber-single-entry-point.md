# Cyber — Single-entry point for incident reporting

**Tracked because:** the biggest *operational* change for regulated (esp. financial) entities — one portal
for incident reports across GDPR, NIS2, DORA, CER and eIDAS.

## Current law
Separate incident-reporting channels and deadlines under NIS2 (Art 23), DORA (Art 19), CER (Art 15),
eIDAS (Arts 19a/24/45a) and GDPR (Art 33).

## Commission proposal
New NIS2 **Arts 23a–23d**: an ENISA-operated **incident-reporting information point** plus Member State
**national entry points**, enabling "report once, share many"; consequential routing amendments to GDPR,
DORA, CER and eIDAS. Application 18 months (extendable to 24).

## Council — ST 9547/26
- **Retained.** ENISA builds an **incident-reporting information point** (Art 23a) that *identifies*
  applicable obligations and redirects — it does **not** store notifications; **Member States** build
  interoperable **national entry points** (Art 23b) that actually receive reports; harmonisation framework
  (Art 23c) and cross-border notification (Art 23d).
- Reporting switch-over to the entry point: **30 months** from entry into force (was 24).
- → [Operative text](../../extracts/council/ST-9547-2026_cyber-art6-9.md)

## Parliament (provisional)
Broadly supportive; EPRS briefing favourable. Concerns about ENISA resourcing.

## EDPB–EDPS
**Strongly support** the single-entry point (Joint Opinion 2/2026, ¶85): an EEA-wide SEP eases reporting
without lowering protection, in line with the EDPB Helsinki Statement. They stress the **security** of
notifications routed through the SEP (they often contain sensitive data) (¶86), recommend mirroring the
changes in **EUDPR Art 34(1)** so EU institutions can notify via the SEP (¶87), and urge **more
harmonisation** with the shorter NIS2/DORA/eIDAS/CER deadlines (¶79).
→ [JO 2/2026 digest: breach notification & SEP](../advisory/edpb-edps-jo-2-2026.md#breach-notification)

## ECB & EESC
- **ECB (CON/2026/9)** — supports the SEP and "report once, share many", but warns it does **not**
  actually cut the burden while each framework keeps its own taxonomy/template, and asks to **exclude
  DORA** for now (time-critical reports should go **direct to the competent authority**); also
  recommends adding the **EUDPR** to the acts covered by the SEP.
  → [digest](../advisory/ecb-con-2026-9.md)
- **EESC (INT/1108)** — strong support for a *genuinely interoperable* SEP covering NIS2, GDPR, DORA,
  eIDAS and CER, with **English-language** submissions, **reuse** of previously submitted information,
  strict **need-to-know** access controls, and pilots co-designed with industry and the social partners.
  → [digest](../advisory/eesc-int1108.md)

## Member-State signals (WK 3735/26, cyber/data consultation)
- **DK** — Member States should have more say over whether the SEP is **secure and functional** (wary of
  the Commission's assessment role; asked for Council Legal Service input); content for **ENISA** to run
  it, **building on the Cyber Resilience Act (Reg 2024/2847)** single-reporting.
- **ES** — **CER, DORA and eIDAS** notifications must remain a **direct channel to national competent
  authorities**, not be mandatorily routed via the SEP. *(Aligns with the ECB's DORA carve-out ask, [`../advisory/ecb-con-2026-9.md`](../advisory/ecb-con-2026-9.md).)*
- **FI** — SEP reporting should be **voluntary** ("entities should be able to choose how to report").
- **EE** — the **18/24-month switch-over timeline should be reviewed later**, once the SEP scope and the
  Member-State build obligations are clear (the text mainly addresses ENISA's role, not MS duties).
- **AT** — flags **ambiguity in Art 38's multiple "competent authorities"** for complaints.
- → [`../member-state-positions.md`](../member-state-positions.md)

## Status
**Likely consensus.** Priority workstream for financial institutions: map current GDPR/NIS2/DORA reporting
channels to the future national entry point; note the 30-month horizon and the fallback (alternative means
where the entry point is technically unavailable).

## Open questions
- ENISA's "8 FTE" resourcing estimate vs 24/7 multilingual scope.
- How DORA's stricter financial-sector templates feed the common format.

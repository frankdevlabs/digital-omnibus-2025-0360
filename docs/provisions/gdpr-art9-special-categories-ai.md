# GDPR Art 9 — Special-category data in AI; biometric verification

**Tracked because:** governs whether sensitive data incidentally caught in AI training is lawful, and
creates a biometric-authentication route.

## Current law
Art 9(1) prohibits processing special categories; Art 9(2)(a)–(j) exhaustive derogations.

## Commission proposal
- New **Art 9(2)(k)**: incidental and residual processing of special-category data in the development/
  operation of an AI system/model, subject to new **Art 9(5)** safeguards.
- New **Art 9(2)(l)**: biometric **verification** (one-to-one) where the data/means are under the data
  subject's sole control.

## Council — ST 9547/26
- **(k) and 9(5) retained, tightened**: sequence of (i) avoid collection, (ii) **erase** if detected,
  (iii) only if erasure is impossible/disproportionate, apply technical/organisational protection
  (no further processing, no outputs, no disclosure) — plus **regular verification + documentation**
  across the AI life cycle.
- **(l) retained with safeguards**: "one-to-one verification", means under sole control, and Member
  State/Union legal-basis hook (Art 9(4)).
- → [Operative text](../../extracts/council/ST-9547-2026_gdpr-art3-amendments.md#point-3--article-9-special-categories)

<a id="parliament-imco-draft-opinion"></a>
## Parliament — IMCO draft opinion (PE789.877, Agius Saliba, 8 Jun 2026)
No joint ITRE/LIBE draft report yet, but the **IMCO draft opinion** would delete the AI carve-out entirely:
it **deletes** both the AI special-category derogation **Art 9(2)(k)**
([Am 100](../../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-100)) and the accompanying
**Art 9(5)** safeguards ([Am 101](../../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-101)),
and it deletes **recital 33** ([Am 20](../../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-20)).
The rapporteur's justification: the derogation *"would amount to an 'AI privilege' difficult to meet EU
principles of necessity and proportionality, affecting the overall level of the protection of consumer's
personal data."* Net: IMCO would delete the AI carve-out entirely — **stronger than the Council**, which
retained and tightened it. IMCO is silent on the **Art 9(2)(l)** biometric-verification derogation also
covered by this page. JURI's draft opinion is data-acquis-only, so on this GDPR-strand provision JURI is
silent. A committee-for-opinion text, not the lead draft report; amendment deadline 8 Jul 2026. Via triage
[#61](../triage/2026-06-18-issue-61.md).

## EDPB–EDPS
**Welcome** the incidental/residual carve-out (Joint Opinion 2/2026, ¶46) — training certain AI cannot
always avoid it — but recommend: put "**incidental and residual**" in the **enacting terms** of 9(2)(k);
**exclude** special-category data collected via **prompts at deployment**; make 9(5) require deletion is
**impossible/disproportionate** on a **documented, state-of-the-art** assessment; add **lifecycle
safeguards** and bar **re-use**; and clarify the interplay with the **AI-Act Art 4a** bias-detection regime
(¶48–52). On **biometric verification (9(2)(l))** they welcome the sole-control limit but want necessity
preserved and the Recital 34 "not likely to create significant risks" line removed (¶36–38).
→ [JO 2/2026 digest: AI special categories](../advisory/edpb-edps-jo-2-2026.md#ai-special-categories),
[biometric](../advisory/edpb-edps-jo-2-2026.md#biometric)

## Relevant CJEU case-law
- **C-474/24** ([judgment, 14 Jul 2026](https://curia.europa.eu/juris/liste.jsf?num=C-474/24)) — the
  Court held that the mere fact a person breached an anti-doping rule and was suspended does **not, in and
  of itself, constitute "health data" under Art 9 GDPR**; that changes only where the publication names the
  **prohibited substance or method**, which (with other information) can directly or indirectly reveal state
  of health. *Not a development on 2025/0360* — the file does not amend the Art 4(15) health-data definition
  or Art 9(1). It is noted here because it narrows the "health data" boundary that the **9(2)(k)/9(5)**
  incidental-and-residual **special-category (health) data** carve-out sits atop (cf. FR's "residual/
  incidental (health) data" framing below): the narrower the concept, the less the AI carve-out must reach.
  Surfaced via a Tier-3 Bluesky signal ([triage #110](../triage/2026-07-15-issue-110.md)).

## Status
**Retained on a tightening trajectory.** Less contested than Art 88c, but the boundary between
"incidental/residual" and "necessary" sensitive-data processing will be litigated in trilogue.

## Member-State signals (WK 3736/26)
- **FR** — wants **9(2)(k) clarified to cover only residual/incidental** (health) data — not the sole
  basis for health-data AI; and the **9(5) threshold aligned** with existing GDPR wording
  ("disproportionate effort *or* technical impossibility"). On **9(2)(l) biometric verification**, allow
  it **only where Union/Member-State law provides for it** — not on a controller's discretion alone.
- **PL** — clarify "residual presence" / "disproportionate effort" and the **incidental-vs-intentional**
  line; read the biometric derogation **restrictively** and technologically-neutrally.
- **RO** — erasure requirements may be **excessive for SMEs**; add a size/resources/capability qualifier
  and SME examples for "disproportionate effort".
- → [`../member-state-positions.md`](../member-state-positions.md)

## Open questions
- What counts as "manifestly disproportionate effort" to erase from a trained model?
- Interaction with AI Act Art 10(5) bias-detection processing of special categories.

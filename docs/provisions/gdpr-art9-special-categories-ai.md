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

## Parliament (provisional)
Likely to insist on a strict-necessity standard and strong documentation; Kaljurand flagged "the end of
GDPR technological neutrality" risk.

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

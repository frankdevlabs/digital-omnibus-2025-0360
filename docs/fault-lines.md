# Fault lines — what will dominate the trilogue

Four issues concentrate the disagreement. On each, the Council (ST 9547/26) has already moved away
from the Commission; the Parliament looks set to push further — and the first **committee-for-opinion
texts now bear this out** (the **IMCO draft opinion**, PE789.877, opines across the GDPR strand; **JURI**,
PE789.142, is data-acquis-only). These are **provisional**: the lead **joint ITRE/LIBE draft report is still
pending**. Detailed per-provision pages are in [`provisions/`](provisions/).

## 1. The concept of personal data and pseudonymisation
- **Commission:** relative/controller-centric clause in Art 4(1); Commission implementing power on
  pseudonymisation (proposed Art 41a).
- **Council:** **both deleted.** Art 4(1) untouched; pseudonymisation handled by an **EDPB opinion**
  mandate (new Art 29a) and EDPB guidelines under Art 70.
- **EDPB–EDPS:** strongly oppose any redefinition as inconsistent with CJEU case law, and would delete
  the Art 41a implementing-act power
  ([digest](advisory/edpb-edps-jo-2-2026.md#personal-data)).
- **Parliament (committee opinions, provisional):** **IMCO** lines up with the Council/EDPB — it deletes
  the Art 4(1) redefinition ([Am 98](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-98))
  and the Commission's Art 41a pseudonymisation power
  ([Am 111](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-111)). JURI silent
  (data-acquis only); joint ITRE/LIBE report pending.
- **Why it matters:** the redefinition would have taken whole categories of data outside the GDPR for
  some actors. Its deletion is the single biggest substantive retreat in the Council text.
- **Member States (WK 3736/26):** FR and PL both welcome the deletion; FR wants a *binding* EDPB opinion
  on pseudonymisation, while PL **opposes deleting Art 41a** and wants any guidance to leave Art 4(1)
  untouched. See [`member-state-positions.md`](member-state-positions.md).
- → [`provisions/gdpr-art4-personal-data.md`](provisions/gdpr-art4-personal-data.md),
  [`provisions/gdpr-pseudonymisation-by-design.md`](provisions/gdpr-pseudonymisation-by-design.md)

## 2. Legitimate interest for AI development and the sensitive-data carve-out
- **Commission:** standalone Art 88c making AI development/operation a legitimate interest under
  Art 6(1)(f); recitals 30/31 on the balancing test; Art 9(2)(k)+9(5) derogation for incidental
  special-category data.
- **Council:** **Art 88c deleted; recitals 30 & 31 deleted.** The AI Art 6(1)(f) reading survives
  only in **recital 33a**. Art 9(2)(k)/9(5) **retained but tightened** (avoid → erase → safeguard,
  with documentation across the AI life cycle).
- **EDPB–EDPS:** the standalone article is unnecessary (Opinion 28/2024 already covers AI LI); they would
  bound the Art 9(2)(k) carve-out to *incidental and residual* processing
  ([digest](advisory/edpb-edps-jo-2-2026.md#ai-legitimate-interest)).
- **Parliament (committee opinions, provisional):** **IMCO goes further than the Council** — it deletes
  the standalone Art 88c and recitals 30/31
  ([Am 121](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-121)) *and* deletes the
  Art 9(2)(k)/9(5) special-category carve-out and recital 33
  ([Am 100–101](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-100)) as an "AI
  privilege". JURI silent; joint ITRE/LIBE report pending.
- → [`provisions/gdpr-art88c-ai-legitimate-interest.md`](provisions/gdpr-art88c-ai-legitimate-interest.md),
  [`provisions/gdpr-art9-special-categories-ai.md`](provisions/gdpr-art9-special-categories-ai.md)

## 3. Cookies / terminal-equipment consent
- **Commission:** move the consent rule out of ePrivacy and into the GDPR (Art 88a), with a list of
  consent-exempt purposes, a 6-month no-repeat rule, and machine-readable consent signals (Art 88b).
- **Council:** **GDPR Art 88a deleted** — the consent rule is **kept in the ePrivacy Directive**
  (amended Art 5(3)), carrying the exempt-purpose list and the 6-month rule; the machine-readable
  signal article (Art 88b) is **retained** in the GDPR (renumbered). This aligns with Poland's
  position (WK 3736/26) that terminal-equipment rules belong in ePrivacy. **France** went further,
  arguing cookie consent is a *technical operation, not data processing*, and demanding the relaxations
  be made in ePrivacy Art 5(3) and that **Art 88b be deleted** (see [`member-state-positions.md`](member-state-positions.md)).
- **Parliament (committee opinions, provisional):** **IMCO sits opposite France/industry on Art 88b** — it
  **strengthens and broadens** the machine-readable-signal duty (tech-neutral "software to access online
  interfaces", drops the SME carve-out, accelerates the browser/OS duty 48 → 18 months, adds anti-dark-
  pattern + third-party-software duties)
  ([Am 117–120](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-117)), caps gatekeeper
  consent re-prompts ([Am 115–116](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-115)),
  and opposes deleting ePrivacy Art 4
  ([Am 122](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-122)). JURI silent; joint
  ITRE/LIBE report pending.
- **Civil society:** **EDRi** publicly **welcomes** the Art 88b machine-readable signal — in a
  18 Jun 2026 ePrivacy/cookies explainer leaflet it frames machine-readable privacy-preference
  communication as a route out of consent fatigue ("rights respected by design"). **noyb (Schrems)**
  went public on 23 Jun 2026 (*"EU Member States (and Google) suddenly want to keep cookie
  banners!"*) defending Art 88b on the same side. On *this* article, civil society thus sits
  **opposite** industry and France, who want Art 88b deleted (see [`stakeholders.md`](stakeholders.md)).
  noyb/Politico further report **Germany and Poland** joining France in pressing to **delete Art 88b**
  in a **newer 18-June Council paper** — wider than the WK 3736/26 record below — but the underlying
  ST compromise text is **not yet on the public register**, so this stays a hedged stakeholder report
  pending the text (Council position tracked via the imminent Coreper II step).
- **Why it matters:** conceptually decisive for where the cookie regime lives and which authority
  enforces it; industry wants the machine-readable signal article deleted as "consent chaos".
- → [`provisions/gdpr-art88a-88b-cookies.md`](provisions/gdpr-art88a-88b-cookies.md),
  [`instruments/eprivacy-2002-58.md`](instruments/eprivacy-2002-58.md)

## 4. Restricting data-subject access rights (abuse of rights)
- **Commission:** controllers may refuse where there are reasonable grounds to believe a request is
  made for a purpose other than data protection.
- **Council:** **retained but reformulated** — an **"abusive intention"** must be demonstrated, with
  the controller bearing the burden.
- **EDPB–EDPS:** object to tying "abuse" to the *purpose* of the access request (link it to an *abusive
  intention* instead) and want Art 12(5) kept mirrored in Art 57(4)
  ([digest](advisory/edpb-edps-jo-2-2026.md#access-requests)); noyb's empirical "reality check" found
  83.5% of access requests already go unanswered or are answered incompletely.
- **Parliament (committee opinions, provisional):** **IMCO pushes the opposite way to the Commission/
  Council** — it removes the abuse-of-rights restriction entirely (deletes the added ground, the fee and
  refusal options and the burden clause) and adds an anti-circumvention / anti-dark-pattern duty inspired
  by DMA Art 13 ([Am 103–107](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-103)).
  JURI silent; joint ITRE/LIBE report pending.
- **Member States (WK 3736/26):** PL welcomes the burden resting on the controller but wants "abusive
  intention" read restrictively; FR wants the ground to also catch circumvention of procedures with
  their own access rules. See [`member-state-positions.md`](member-state-positions.md).
- → [`provisions/gdpr-art12-57-abusive-requests.md`](provisions/gdpr-art12-57-abusive-requests.md)

## Secondary tensions
- **Single-entry point** architecture and ENISA resourcing (broadly supported, but operational doubts);
  **IMCO** adds a non-regression safeguard that the single entry point must not lower protection or limit
  supervisory powers ([Am 110](../extracts/parliament/IMCO-PA-789877_draft-opinion.md#amendment-110))
  → [`provisions/cyber-single-entry-point.md`](provisions/cyber-single-entry-point.md).
- **Repeal scope** of the data acquis — P2B is only **partially** amended in the May text, and
  data-altruism provisions (DGA) attract Member State defence. **Both Parliament committees (JURI + IMCO)
  oppose the P2B repeal** and largely reverse the data-acquis deregulation (smart contracts, cloud
  switching, DGA registration/neutrality) — the strand where the committee drafts concentrate
  ([what-changed: data acquis](what-changed.md#data-acquis-data-act-20232854--dga--parliament-committee-focus))
  → [`provisions/final-repeals-p2b.md`](provisions/final-repeals-p2b.md).

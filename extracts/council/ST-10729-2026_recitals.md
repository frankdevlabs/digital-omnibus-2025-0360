# Extract — ST 10729/26, key recitals (curated subset)

> **Source:** Council document **ST 10729/26** (LIMITE), Brussels, **22 June 2026** — Presidency *Mandate
> for negotiations with the European Parliament*, file 2025/0360 (COD). **Working transcription, not an
> official text** — consolidated reading. In the source, **bold/strikethrough** marks changes vs the
> Commission proposal and **underline** marks changes vs the previous compromise **ST 10677/26 (18 June
> 2026)**. **This is a curated subset** of the recitals (those carrying the substantive choices tracked in
> this repo), not the full preamble. Salient changes vs **ST 9547/26** are flagged **▸**. Verify against the
> authoritative document. See [`../../NOTICE`](../../NOTICE).

Recitals are interpretive, not operative. They matter here because the Council uses them to carry several
substantive choices — most notably the **AI legitimate-interest** statement and, new in this text, the
**third-country tax-data-transfer** derogation (recital 40b).

---

## Recital 27 (concept of personal data)
Retained, pointing back to the existing **Recital 26** and the "means reasonably likely to be used" test; the
Commission's reframing toward a relative/controller-centric concept is **not** carried into an operative
article (Art 4(1) addition deleted — see
[GDPR extract, point 1](ST-10729-2026_gdpr-art3-amendments.md#point-1--article-4-definitions)).

<a id="recital-27a--27b-pseudonymisation"></a>
## Recital 27a / 27b (pseudonymisation, identifiability, third-party transmission)
**Recital 27a — updated this round.** It now spells out, "in light of the case-law of the Court of Justice",
when a natural person should be considered identifiable **following pseudonymisation and the transmission to
a recipient, as well as when such recipient further discloses, transmits or otherwise makes such data
available to a third party**: *"Data which are in themselves impersonal may become 'personal' in nature where
they are put at the disposal of other persons who have means reasonably likely to enable the data subject to
be identified. This applies to both the party that transmits this data and the third party that subsequently
processes this data."* The **EDPB** is to adopt a supporting opinion on pseudonymisation/anonymisation after a
public consultation.
▸ **Change vs ST 9547/26:** recital 27a is reworked to underpin the **new Article 29a(2a)** onward-disclosure
rule (Presidency NOTE ¶11(i)). **27b** (pseudonymisation as one possible Article 32 security measure, assessed
case-by-case; codes of conduct) is retained.

## Recital 30 — [DELETED in ST 10729/26]
The Commission's recital framing AI development/operation as a societal benefit justifying legitimate interest
remains **struck out**.

## Recital 31 — [DELETED in ST 10729/26]
The Commission's recital on the **balancing test** for AI legitimate interest remains **struck out**.

## Recital 33 (legitimate interest, general)
Retained — general guidance on Article 6(1)(f) balancing.

---

<a id="recital-33a-ai-legitimate-interest"></a>
## Recital 33a — AI and legitimate interest (RETAINED; carries what Art 88c used to)

Consolidated: *the processing of personal data in the context of the **development and deployment of an AI
system or model** may be regarded as carried out for a **legitimate interest** of the controller within the
meaning of Article 6(1)(f), where appropriate, except where overridden by the interests or fundamental rights
and freedoms of the data subject — in particular where the data subject is a **child** — or where other Union
or national law explicitly requires consent. This does not affect the controller's obligation to choose an
appropriate lawful ground (e.g. Article 6(1)(e) for public authorities). Any such processing should be subject
to appropriate organisational and technical measures and safeguards, such as protection against disclosure of
residually retained data in the AI system or model.*

▸ This recital is what remains of the deleted **Article 88c**. It is **interpretive only** — there is no
standalone operative AI legitimate-interest article. AI development on personal data relies on **ordinary
Article 6(1)(f)** read with EDPB **Opinion 28/2024**. Unchanged in thrust vs ST 9547/26.
See [AI LI provision](../../docs/provisions/gdpr-art88c-ai-legitimate-interest.md).

---

<a id="recital-34--biometric-verification"></a>
## Recital 34 — biometric verification (clarification added this round)

Supports the new Article 9(2)(l) biometric-verification ground: *where biometric data are processed to confirm
identity, controllers should, where possible, prioritise authentication methods that do not involve biometric
data and choose the least intrusive equally-effective means.* It defines the **biometric identification vs
verification** distinction (one-to-many database comparison vs one-to-one confirmation of a claimed identity)
and elaborates **"sole control"**: the data subject can effectively decide when and how their biometric data
are used, without the controller having technical capacity to access them in decrypted form — e.g. data stored
solely on the data subject's device, or held by the controller in state-of-the-art encrypted form with the key
held solely by the data subject, with end-to-end encryption in transit and a secure-erasure option.
▸ **Change vs ST 9547/26:** a clarification was **added to recital 34 on biometric data** this round
(Presidency NOTE ¶11(i)).

## Recital 38 — [DELETED in ST 10729/26]
The Commission's recital supporting the rewrite of **Article 22** (automated decisions) remains struck, consistent
with Article 22 being largely restored
([GDPR extract, point 7](ST-10729-2026_gdpr-art3-amendments.md#point-7--article-22-automated-decisions)).

## Recital 39 / 39a (cookies / terminal equipment)
Support keeping the consent rule in the **ePrivacy Directive** (amended Art 5(3)) — the consent-exempt purposes
(incl. anonymous first-party audience measurement and security/fraud prevention) and the **6-month**
anti-consent-fatigue rule. See [ePrivacy extract](ST-10729-2026_eprivacy-art5.md).

## Recitals on the machine-readable consent signal — reworked/withdrawn
▸ **Change vs ST 9547/26:** consistent with the deletion of **Article 88b** (the automated/centralised
consent-signal duty — see [GDPR extract, point 15](ST-10729-2026_gdpr-art3-amendments.md#point-15--articles-88-cookies-ai-li)),
the recitals supporting a standalone browser/OS machine-readable-signal obligation are dropped/recast. The
cookie story now lives entirely in the amended ePrivacy Art 5(3).

---

<a id="recital-40b--third-country-tax-transfers"></a>
## Recital 40b — third-country tax transfers — **NEW in ST 10729/26 (the FATCA recital)**

> *"Transfers of personal data to third countries or international organisations could be necessary for
> important reasons of public interest within the meaning of Article 49, paragraph (1), point (d) of
> Regulation (EU) 2016/679. Such important reasons of public interest include the implementation, application
> and compliance with international agreements or administrative arrangements on mutual assistance or
> cooperation in tax matters concluded by a Member State with a third country or an international organisation
> where personal data are exchanged on a periodic or automated basis. In such cases, Member States should
> ensure that appropriate safeguards are provided for under Union law or national law, so that the level of
> protection of natural persons guaranteed by Regulation (EU) 2016/679 is not undermined. Where the competent
> authority responsible for the transfer considers that the rights and freedoms of the data subject concerned
> override the public interest pursued by the transfer, the transfer should not take place."*

▸ **Entirely new vs ST 9547/26.** It is the interpretive counterpart to the **new Article 49 amendment**
(GDPR extract, [point 10a](ST-10729-2026_gdpr-art3-amendments.md#point-10a--article-49-tax-transfers)). It
authorises **periodic/automated** tax-data transfers to third countries (FATCA-style) under the Article
49(1)(d) public-interest derogation. **Numbering note:** the Presidency explanatory NOTE ¶13 refers to this as
recital **"40a"**, but the Annex operative text numbers it **(40b)** — (40a) is a separate recital on
national-supervisory-authority consistency. Added at delegations' request via the Antici Group, **with no
impact assessment** (NOTE ¶12). See [provision page](../../docs/provisions/gdpr-art49-third-country-tax-transfers.md)
and pending CJEU case **C-804/25**.

---

<a id="recital-49--national-entry-point"></a>
## Recital 49 — national entry point for incident reporting (updated this round)

*"The establishment by Member States of a **national entry point** should support and facilitate the fulfilment
of obligations pertaining to the reporting of incidents and related events under Directive (EU) 2022/2555,
Regulation (EU) 2016/679, Regulation (EU) 2022/2554, Regulation (EU) 910/2014 and Directive (EU) 2022/2557. …
the national entry point could give entities a possibility to retrieve information they have previously
submitted, helping them keep track of their compliance."* Recitals **49a/50/50a** add an ENISA **information
point** (which only informs/redirects, and does not receive notifications) and ENISA **non-binding
recommendations** for interoperable national entry points.
▸ **Change vs ST 9547/26:** recital 49 was **updated** alongside the adjustment to NIS2 **Article 23b(1)** for
flexibility in establishing the national entry point (Presidency NOTE ¶11(iii)). The architecture shifts further
from a single EU entry point toward Member-State national entry points + an ENISA information point — see
[cyber extract](ST-10729-2026_cyber-art6-9.md) and
[breach-notification provision](../../docs/provisions/gdpr-art33-breach-notification.md).

---

**Note on numbering:** recital numbers follow the source's own working numbering and may be renumbered in the
final text. **See also:** [GDPR Art 3](ST-10729-2026_gdpr-art3-amendments.md) ·
[ePrivacy Art 5](ST-10729-2026_eprivacy-art5.md) · [Cyber Arts 6–9](ST-10729-2026_cyber-art6-9.md) ·
[EUDPR Art 4](ST-10729-2026_eudpr-art4.md)
</content>

# Extract — ST 8261/1/26 REV 1, Articles 6–9 (cyber: NIS2, eIDAS, DORA, CER)

> **Source:** Council document **ST 8261/1/26 REV 1** (LIMITE), Brussels, 15 April 2026 — Presidency revised
> compromise text, for the AGS meeting of 24 April 2026. Interinstitutional file 2025/0360 (COD).
> **This is a working transcription, not an official text** — consolidated reading (tracked changes against
> the Commission proposal accepted). Bracketed `[…]` figures are undecided in the source. Always verify
> against the authoritative document. See [`../../NOTICE`](../../NOTICE).

**What is new here.** This is the **first** compromise version to carry the **operative cyber architecture**.
February (ST 6406/26) had **no** Articles 6–9 — only a *bracketed* cross-reference to a "single-entry point"
inside GDPR Art 33 ([see Feb cyber extract](ST-6406-2026_cyber-art6-9.md)). This April text **establishes**
the incident-reporting architecture, built around two pieces: an ENISA **single-information point** (which
does *not* receive notifications) and Member-State **national entry points** (through which notifications are
actually submitted). See [provision page](../../docs/provisions/cyber-single-entry-point.md) and
[NIS2 instrument page](../../docs/instruments/nis2-2022-2555.md).

▸ **Terminology note (Feb → Apr → May).** February referred to a single **"single-entry point"** under
**Article 23a**. This April text splits the concept: a non-receiving **"single-information point"** (ENISA,
Article 23a) **plus** a receiving **"national entry point"** (Member States, Article 23b). May keeps the
two-tier model, calling the ENISA piece an "information point" and the Member-State piece "national entry
points". Note that, internally, this April text is **not fully reconciled**: the cyber articles speak of the
"single-information point" / "national entry point", but **Article 11** (final provisions) still refers to a
"single-entry point" and to "Article 23a(7)" (a paragraph the consolidated Article 23a no longer contains) —
see [final provisions](ST-8261-1-26-REV1_final-art10-11.md#article-11-final-provisions).

---

## Article 6 — Amendments to the NIS2 Directive (EU) 2022/2555

**New Article 23a — Single-information point for incident reporting (ENISA).**
*"(1)* ENISA shall develop and maintain a **single-information point**.
*1a.* The single-information point should: **(a)** enable the identification of applicable obligations to
report incidents and related events (references to definitions and reporting thresholds; the competent
authorities and CSIRTs and their contact information; applicable deadlines; formats; procedures; language
requirements); **(b)** be designed to enable **guided and dynamic navigation**, identifying the applicable
reporting obligations and redirecting to the appropriate national authorities and procedures; **(c)** make
available simplified, well-documented information channels (help guides, tutorials, a knowledge base).
*1b.* When developing it, ENISA shall consult the relevant national competent authorities, the **NIS
Cooperation Group** and the **CSIRT Network**, and shall establish structured communication channels so the
information is swiftly updated; Member States shall communicate the relevant information.
*1c.* The single-information point **shall not enable the submission, transmission, storage or processing of
any incident notification or related data**, and shall not collect any information allowing identification
of the notifying entity or of any incident.
*1d.* Within **[12] months** from entry into force, ENISA shall **pilot** the functioning of the
single-information point for each added Union legal act.
*1e.* After establishing it, and in cooperation with the NIS Cooperation Group, ENISA shall explore
extending it (regulatory mapping of other EU acts; national transposition measures; supporting content on
registration / risk-management / incident reporting; cybersecurity benchmark comparison tools)."*
▸ The Commission's original Article 23a (an ENISA-run *single-entry point* with paragraphs (2)–(7) on
security measures, specifications, piloting and a Commission "proper-functioning" notice) is **largely
struck and recast** into the non-receiving information-point above.

**New Article 23b — National entry point for incident reporting (Member States).**
*"(1)* Member States shall establish and maintain a **national entry point** for the reporting of incidents
and related events under the Union legal acts where those acts provide so, taking into account national
specific needs, existing national structures and the most effective arrangements. *(2)* ENISA, in
consultation with the CSIRTs network and the Cooperation Group, shall develop **guidelines** to support
Member States in establishing, maintaining and securely operating their national entry point (technical,
operational and organisational measures; possibly technical specifications for interoperability between
national entry points). *(3)* the guidelines may cover retrieval/supplementing of previously submitted
information and re-use of a single submission for multiple reporting obligations via the same national entry
point. *(4)* Member States shall regularly inform ENISA about the development of their national entry point.
*(5)* at the request of Member States, the CSIRTs Network can support the development."*

**New Article 23c — Harmonising incident notification framework.**
*"(1)* by **[6 months after entry into force]** the Commission shall submit a report to the European
Parliament and the Council outlining common definitions, thresholds, deadlines, formats and procedures
applying to Article 23 of NIS2, Article 19a(1a), 24(2a) and 45a(3a) of Regulation (EU) 910/2014, Article
33(1) of the GDPR, Article 19(1) and (2) of Regulation (EU) 2022/2554 and Article 15(1) of Directive (EU)
2022/2557, in particular concrete steps and a timeline for a unified approach. *(2)* Member States shall, in
cooperation with the CSIRT network, work on exchange and interoperability of incident-notification
information. *(3)* building on the report, ENISA shall develop **guidelines** to foster harmonisation
(harmonising templates; analysing sectoral thresholds; reviewing notification stages), with a first draft
within **12 months** of entry into force, updated regularly."*

**New Article 23d — Cross-border incident notification.**
*"(1)* Member States should aim at facilitating cross-border notifications to multiple national reporting
structures; ENISA, with the Cooperation Group and the CSIRT network, shall develop and maintain mechanisms
to align notifications submitted via the national entry point with cross-border reporting obligations.
*(2)* ENISA shall harmonise its relevant tools with national notification templates and facilitate
automatisation to exchange information on cross-border impacts. *(3)* Information submitted through relevant
tools shall **not be automatically transmitted to ENISA in full**; Member States may select the information
shared."*

**Article 23 (significant incidents) amended.** Paragraph 1, first sentence replaced so that essential and
important entities notify a significant incident **via the national entry point established pursuant to
Article 23b**. New **paragraph 1b**: ENISA, with the Cooperation Group, shall provide a **mapping** of all
the competent authorities and CSIRTs in the single-information point. New **paragraph 12**: where a
manufacturer notifies a severe incident under Article 14(3) of Regulation (EU) 2024/2847 (Cyber Resilience
Act) and that reporting contains the information required under paragraph 4, it constitutes reporting under
paragraph 4.

**Article 30(1) amended.** Voluntary notifications (by essential/important entities and by other entities)
are submitted to the CSIRTs or, where applicable, the competent authorities **via national reporting
structures** (the Commission's "single-entry point established pursuant to Article 23a" routing is struck).

---

## Article 7 — Amendments to the eIDAS Regulation (EU) 910/2014

- **Article 19a — new paragraph (1a):** notifications under paragraph 1(b) to the supervisory body (and
  other relevant competent authorities) shall be made through the **national entry point** pursuant to
  Article 23b of Directive (EU) 2022/2555.
- **Article 24 — new paragraph (2a):** notifications under paragraph 2(fb) made through the national entry
  point (Art 23b NIS2).
- **Article 45a — new paragraph (3a):** notifications under paragraph 3 to the Commission and the competent
  supervisory body made through the national entry point (Art 23b NIS2).
▸ vs February (no operative cyber text): the routing is the **national entry point / Article 23b** (February
referred only, in brackets, to a single-entry point / Article 23a inside GDPR Art 33).

---

## Article 8 — Amendments to DORA, Regulation (EU) 2022/2554

- **Article 19(1):** financial entities report **major ICT-related incidents** to the relevant competent
  authority **via the national entry point** established pursuant to Article 23b of Directive (EU) 2022/2555.
- **Article 19(2):** voluntary notification of **significant cyber threats** likewise via the national entry
  point.
▸ The change is the **channel**, not DORA's own (stricter) timelines and templates.

---

## Article 9 — Amendments to the CER Directive (EU) 2022/2557

- **Article 15(1):** critical entities notify, via the **national entry point** (Art 23b NIS2), the
  competent authority of incidents that significantly disrupt (or have the potential to significantly
  disrupt) the provision of essential services.
- **Article 15(2) — new subparagraph:** the Commission may adopt implementing acts further specifying the
  **type and format** of information notified pursuant to Article 15(1), in accordance with the examination
  procedure referred to in Article 24(2).

---

**Application dates** (see [final provisions](ST-8261-1-26-REV1_final-art10-11.md#article-11-final-provisions)):
the cyber institutional build-out (Articles 6(2)–(3), 7, 8 and 9) and the GDPR breach-routing (Article 3(8)
(a)–(c)) apply **18 months** after entry into force; the actual switch-over to reporting **via the national
entry point** applies **24 months** after entry into force (May later moves this to 30 months).

**See also (this version):**
[GDPR Art 33 breach notification](ST-8261-1-26-REV1_gdpr-art3-amendments.md#point-8--article-33-breach-notification)
· [Final provisions](ST-8261-1-26-REV1_final-art10-11.md) · [Recitals](ST-8261-1-26-REV1_recitals.md)

**See also (for diffing):** [Feb cyber (absent)](ST-6406-2026_cyber-art6-9.md) ·
[May cyber](ST-9547-2026_cyber-art6-9.md)

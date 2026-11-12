# Appendix: comparables, AZAV checklist, open decisions

**Draft · 12 November 2026.**

## Approved Bildungsgutschein courses priced above €10,000

These are prices for AZAV-approved, voucher-eligible courses, checked on 12 November 2026. The self-pay bootcamp prices in [economics.md](../economics.md) are a different kind of figure. No source showed a KldB/BDKS line, so that column is **unknown** for every course.

| Provider | Course | Price | UE / duration | Per UE *(estimate)* | Approval details shown | Source |
|---|---|---:|---|---:|---|---|
| IfaDW Institut für angewandte Datenwissenschaft | AI Engineer | €14,658.00 | 1,050 UE, 30 weeks full-time, live online Mon–Fri 8–16, max 12 participants | €13.96 | AZAV, GUTcert, certificate M-26-26532-1 (valid to 03.02.2029); "Preis laut AZAV-Zertifikat" | https://www.ifadw.de/ai-engineer/ |
| IfaDW | Data Scientist | €12,127.50 | 875 UE, 25 weeks full-time, live online | €13.86 | AZAV, GUTcert, M-26-26532-1 | https://www.ifadw.de/data-scientist/ |
| SkillSprinters by Dr. Aichinger | Digitalisierungsmanager für Prozessautomatisierung und Künstliche Intelligenz | €10,548.00 | 720 UE (13 modules), 16 weeks full-time (9 UE/day) or about 29 weeks part-time, live online | €14.65 | AZAV, DEKRA. A third-party listing gives €9,662 and measure no. 723/0097/2026 (full-time), so the price conflicts between sources | https://skill-sprinters.de/digitalisierungsmanager/ · https://deinbildungsgutschein.de/kurse/digitalisierungsmanager-fuer-prozessautomatisierung-und-kuenstliche-intelligenz |
| StackFuel (a Multiverse company) | Machine Learning | "über 10.000 €" (BA price band; exact figure **unknown**) | 27 weeks full-time; UE **unknown** | unknown | Bildungsgutschein-eligible in BA Mein NOW data | https://gefoerderte-ki-kurse.de/kurse/machine-learning-stackfuel-gmbh/ |
| StackFuel (a Multiverse company) | Datenanalyse und generative KI | "über 10.000 €" (BA price band; exact figure **unknown**) | 12 weeks full-time; UE **unknown** | unknown | Bildungsgutschein-eligible in BA Mein NOW data | https://gefoerderte-ki-kurse.de/kurse/datenanalyse-generative-ki-stackfuel-a-multiverse-company/ |

Below €10k, for contrast. IfaDW's **KI-Anwendungsentwickler** is closest to track B (NLP, generative AI, RAG, agentic AI): 525 UE over 15 weeks, €7,413.00 (€14.12/UE), GUTcert M-26-26532-2. https://www.ifadw.de/ki-anwendungsentwickler/

What the sources show:

- The courses above €10k get there through **720–1,050 UE**, at €13.86–€14.65/UE.
- All of those rates are **below** 43414's €15.46. At their rates, 480 UE would cost €6,650–€7,030 *(estimate)*.
- That is why the [README](README.md) recommends more UE, justified by learning needs, rather than a large surcharge.

Not used: DCI (Digital Career Institute) shows 2,200-UE AZAV courses, for example Data Engineering, measure 962/479/2026 (https://digitalcareerinstitute.org/courses/data-engineer/), but publishes no price. The BA's own Mein NOW/KURSNET pages were not fetched directly. The StackFuel figures come through a directory that copies the BA data.

## AZAV checklist (short)

[operations-and-azav.md](../operations-and-azav.md) has the full analysis. Status for these drafts:

| Requirement | Status |
|---|---|
| Provider approval (Trägerzulassung) incl. QM system | Missing |
| Measure approval (Maßnahmezulassung) | Missing; the variant files are the starting point for the concept |
| Course concept: goal, target group, content, materials | Drafted for A and B (English); a formal German concept is needed |
| Didactic concept: live delivery, interaction, attendance control | Teaching-day structure drafted; full concept missing |
| Curriculum with UE per module and a reason for the duration | Drafted (640 UE each, reason in each variant file) |
| Measurable learning objectives per module | Drafted per week |
| Assessment and documentation | Drafted; rubric and documentation process missing |
| Certificate content (qualification, content + UE, assessment forms) | Missing |
| Instructor qualifications and absence coverage | Alexey only; illness cover needed (see operations-and-azav.md) |
| Absence policy (Fehlzeitenkonzept) and individual learner support | Missing |
| Entry check (fit with target group) | Proposed: practical exercise + consultation |
| Labour-market fit | See [research.md](../research.md) |
| Cost calculation against BDKS | Options in [README](README.md); full costing missing |
| Rooms, equipment, platform, GDPR | Berlin room terms pending; platform description missing |
| ZFU / FernUSG classification for the online format | Open, see operations-and-azav.md §6 |
| Holidays for courses of 6 months or longer | Applies to the 32-week part-time option |

## Open decisions

1. Which track goes first (survey, interviews and pilot by 27 November, per the [README](../README.md)).
2. 640 UE / 16 weeks (recommended), 680 UE / 17 weeks with no surcharge, or stay at 480 UE / 12 weeks and below €10k.
3. Whether the cost of LLM, coding-agent and cloud usage per participant supports €16.50/UE (needs quotes).
4. Founder capacity for 16 teaching weeks (about 608–656 h *(estimate)*) and illness cover.
5. Track A material gaps (existing codebase, debugging, CI/CD releases, reusable workflows, software factory): write the material, or allow AI Dev Tools Zoomcamp as a source.
6. Voucher fee vs survey self-pay price (€9,000–€10,000): check with the FKS.
7. Teaching stack for track A (Python or TypeScript).
8. Certificate wording and final exam format.

# Verified facts, source conflicts, and gaps

## Verified facts (live Maven page, fetched 2026-11-13)

Source: https://maven.com/alexey-grigorev/product-shipping

| Fact | Value on page |
|---|---|
| Title | Product Shipping with AI: From Idea to Real Users |
| Cohort | Live cohort, **Jan 11 – Mar 21, 2027** |
| Sessions | 10 live one-hour sessions, 41 lessons (page says "10 live sessions • 41 lessons"); 17:00 Europe/Berlin; Mon Jan 11, then Tuesdays Jan 19 – Mar 16 |
| Time | ~1 hr live + ~4 hrs project work + ~1 hr notes/recordings per teaching week |
| Listed price | **$3,000 USD** — described as "only for people skipping the application process" (direct enrollment, no revenue share) |
| Seats | "For the first cohort I offer only 20 seats"; "20 invite-only places" via application form https://forms.gle/F3ZiLzq8i2nip2VP6 |
| Selected-applicant options | $1,599 no revenue share; $799 smaller share; $100 larger share. Revenue-share **terms are not finalized** (shown before acceptance/payment) |
| Peer testing / reviews | Alexey reviews every submitted midterm and final project in **group** office hours (no private 1:1 coaching); at each milestone test three peers' products and get feedback on yours |
| Prerequisites | Able to install and run an AI coding assistant; budget $20–$500/month for assistant and cloud (not included). **No prior coding, Git, or CLI required.** AI features in the product are optional |
| Guarantees | "Covered by the Maven Guarantee" only; no outcome guarantee. FAQ: customers, revenue, product-market fit **not** guaranteed |
| Guests | Planned, none confirmed |
| Alexey's approved public bio line | "I run education and community businesses generating €200k+ in annual revenue." (course.yaml, confirmed 2026-11-06) |

Six modules plus midterm and final (all from the live syllabus):
1. Choose a problem and a small first version
2. Build and deploy the first version
3. Prepare your product for testers
- Midterm: submit first version; test three peer products; group office hours
4. Improve your product from feedback
5. Track usage and prepare to launch
6. Launch and learn from the response
- Final: submit product and launch report; peer testing; share work

Free companions named in bots-management README: *Before You Build: Product Discovery Working Kit* (https://maven.com/alexey-grigorev/o/72f4ae) and *From Problem to Launch: Book Action Checklists* (https://maven.com/alexey-grigorev/o/68fe1e). They were not re-fetched here; confirm they are live before linking.

## Source conflicts (and how this plan resolves them)

| Topic | Older repo pack (`courses/product-shipping/`, 2026-10-20) | Newer sources (live page 2026-11-13; bots-management 2026-11-06) | Plan uses |
|---|---|---|---|
| Dates | Nov 16, 2026 – Feb 7, 2027 | Jan 11 – Mar 21, 2027 | Newer |
| Price | $1,599 shown | $3,000 listed; $1,599/$799/$100 for selected applicants | Newer |
| Capacity | 15 selected places | 20 seats / 20 invite-only | Newer |
| Prerequisites | Aimed at people who can already code | No coding experience required | Newer |
| Holiday break | Dec 21 – Jan 3 | Page syllabus shows a holiday-break block, but its FAQ says "no break" (course runs Jan 11 start) | See gap 4 |

bots-management itself states the older research-dump pack "contains superseded dates and prerequisites"; Alexey's current instructions and DataOps records take precedence. The older pack is still useful for narrative material (e.g. the *Product Shipping Decisions* series idea and downloadable card concepts).

## Gaps

### 1. Application deadline
bots-management README instructs the Maven note to read "(Closes on 29 Nov)". The live page text fetched on 2026-11-13 does **not** contain "Closes", "29 Nov", or any deadline, and DataOps (which holds the authoritative campaign calendar and application rounds) could not be read from this host (`dataops` returned "Refresh token family revoked"). So: the application deadline, and whether there is a December round, are **unverified**. This is the largest sequencing risk — see the Oversubscribed doc for the two scenarios.

### 2. Direct-enrollment capacity
Unclear whether the $3,000 direct route counts inside the 20 seats. The older pack says direct enrollment must have separate finite capacity and should not be unlimited. Needs a decision before saying "only 20 people".

### 3. Revenue-share terms
Percentages, duration, caps not finalized. Do not mention $100/$799 options in talks as settled deals; refer to the form.

### 4. Page inconsistencies to fix before heavy promotion
Observed on the live page 2026-11-13 (not fixed here; bots-management must not be modified):
- Midterm text says "Submit … by December 13" and "review three peer products by December 20" — stale dates from the old calendar.
- Syllabus shows "Holiday break" weeks (Dec 21–27, Dec 28–Jan 3) while the FAQ says there is no break and the cohort runs ten consecutive weeks. The FAQ's session list (Mon Jan 11, then Tuesdays Jan 19 – Mar 16) is consistent with the header dates; the break blocks and the Dec dates are not.
- "Week 6 … Module 4" slot ordering on the page looks displaced (Feb 16 etc.) — page-rendering order, check in Maven.
- Lesson counts: "41 lessons" on the live page; the older pack says 47.
People reading December promo will land on this page; a talk that says "see the syllabus" invites questions about these.

### 5. Moats / defensibility
Not in the verified syllabus. Module 1 (problem choice), Module 6 (who it's for, where to share) are the closest, but none teaches defensibility. Not planned as a core talk. Listed in the calendar as "optional slot, only if the course adds it".

### 6. Social proof
No testimonials or cohort results exist for this course (first cohort). Do not use Buildcamp ratings or other course testimonials as evidence for this course's results (the older pack already says this). Alexey's own background (bio line above) and prior products are the only verified credibility claims.

### 7. Guests
None confirmed; do not name any in talks.

### 8. Channels, handles, audience sizes
No verified inventory of Alexey's personal channels or follower counts was available in this task. Channel suggestions are generic and need Alexey's confirmation.

### 9. Talk times / platform / registration tool
Not specified anywhere.

### 10. Nothing was verified live beyond the Maven page
Free companion links, application form behaviour, and the Maven "Guarantee" terms were not tested.

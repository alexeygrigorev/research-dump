# Podcast Guest Research System

A practical, evidence-grounded method for researching podcast guests, avoiding repetitive interviews, designing stronger questions, and giving the host a usable live brief.

This report was developed from a review of the attached `podcast-guest-researcher` skill and a comparison with public podcast-production, journalism, oral-history, fact-checking, and agent-skill design methods.

---

## Executive summary

The source skill has the right editorial backbone:

> **Discover the source universe → analyze sources separately → synthesize across sources → design the episode and questions.**

Its best ideas are:

- Do not begin by generating questions.
- Search beyond the guest's official biography.
- Analyze substantial sources one at a time so claims remain traceable.
- Treat prior appearances as a dedicated research problem.
- Build a do-not-repeat list and look for unfinished threads.
- Use scripts for deterministic work and reserve editorial judgment for synthesis.
- Prefer questions about trade-offs, changed beliefs, decision rules, failures, and concrete examples.
- Challenge ideas without turning the interview into a gotcha exercise.

Its main weakness is scope. It combines three different products:

1. A podcast editorial research method.
2. A multi-agent research pipeline.
3. A searchable analytics website with timelines, source subpages, metrics, and browser testing.

That full stack can be valuable for a flagship guest. It is too large as the default for a weekly show. The improved system below keeps the evidence-first method but introduces **Rapid**, **Standard**, and **Flagship** modes. Its primary deliverable is a one-page live run sheet; dashboards and searchable corpora become optional modules.

---

# 1. Assessment of the original skill

## What should be retained

### Discovery before questions

The source skill explicitly says not to start with question writing. This is the single most important design decision. Good questions emerge from evidence, prior coverage, contradictions, gaps, and audience needs. They should not be generated from a name and a short biography in one pass.

### Separate discovery surfaces

The skill searches identity and owned media, public professional material, YouTube and video, podcast and audio appearances, and third-party sources. Separating these surfaces reduces the chance that one search engine or one prominent profile defines the entire research universe.

### One substantial source per extraction context

The instruction to extract substantial sources separately is sound. Mixing several interviews in one analysis context tends to blur attribution and produce conclusions that cannot be traced back to a particular passage or timestamp.

Each extraction should preserve:

- facts and timeline events;
- claims and opinions;
- stories and examples;
- frameworks and procedures;
- concrete results and numbers;
- questions already asked;
- quotable or clip-worthy moments;
- contradictions and changes of mind;
- evidence passages or timestamps;
- uncertainty and missing information.

### Prior-appearance analysis

This is the strongest part of the original design. A link list of previous podcasts is not enough. Each appearance should answer:

- What did the guest actually discuss?
- Which stories or frameworks did they explain particularly well?
- Which questions have become rehearsed?
- Which lines of inquiry were left unfinished?
- What did the interviewer fail to ask?
- Which claims need verification or a better counterpoint?
- What would make a useful follow-up rather than a repetition?

### Deterministic work should be scripted

Fetching, URL normalization, deduplication, word counts, transcript enumeration, index building, and file validation should not consume expensive model reasoning. Models should be used where interpretation is needed; scripts should be used where the expected result is deterministic.

### Cross-source synthesis stays unified

The source skill correctly treats cross-source synthesis as the hard part. The timeline, contradiction map, do-not-repeat list, angle selection, and question bank should be developed together, with the same editor or reasoning context holding the source-level extractions.

### Ethical controversy

The skill's controversy rules are strong:

- earn the challenging question through evidence;
- ask permission before pushing when appropriate;
- challenge ideas, incentives, and trade-offs rather than attacking the person;
- ask where the guest's framework fails;
- do not pressure guests to disclose confidential information or violate agreements.

## What should be changed

### Make the workflow tiered

The original assumes a research pass may include 30 or more sources, hundreds of thousands of transcript words, a search index, analytics, an interactive dashboard, and multi-device browser testing. That is a valid **Flagship** workflow, not a sensible default.

The chosen mode should control source depth, output count, and infrastructure.

### Resolve conflicting output rules

The source skill supports selective output modes but later says to always build an HTML dashboard, while its final instruction says to write only requested outputs. A revised system should make deliverables explicit at the start and should not silently expand into a software project.

### Replace vendor-specific model names

Routing by task complexity and source size is useful. Hardcoding particular model brands is not. Use portable capability tiers:

| Capability | Suitable work |
|---|---|
| Deterministic script | Fetching, normalization, deduplication, counting, validation |
| Lightweight model | Link classification, short-source extraction, boilerplate detection |
| Standard reasoning model | Full interview extraction, transcript mapping, source summaries |
| Deep editorial model or human editor | Contradictions, novelty analysis, episode thesis, question design |

### Add a claim-verification ledger

A source manifest says what was collected. It does not say which on-air claims are safe to present as facts. The system needs a dedicated ledger that distinguishes:

- verified facts;
- attributed statements;
- contested claims;
- unverified claims;
- stale information;
- researcher interpretations.

### Reduce promotional bias

The original says the research should make the guest look excellent. A better objective is:

> Help the guest give their clearest, most substantive answers while protecting the audience from repetition, unsupported claims, and promotional framing.

The guest should be treated fairly and prepared intelligently, but the system should serve the audience rather than operate as reputation management.

### Narrow personality analysis

Inferring a personality profile from repositories, social posts, and interviews can encourage unsupported psychological conclusions. Rename this output:

> **Public communication and working-style signals**

Only include observable, interview-relevant patterns supported by examples, such as how the guest explains technical ideas, responds to disagreement, changes positions, or uses evidence. Do not diagnose personality or infer sensitive private characteristics.

### Make dashboards and output analytics optional

Interactive timelines, appearance subpages, search indexes, and quantified public-output metrics are useful when:

- the guest has a very large public footprint;
- several producers need to review the work;
- the corpus will be reused;
- output volume is genuinely part of the episode thesis.

They should not be required for every guest.

### Add pre-interview, live, and post-interview protocols

The original is detailed about research artifacts but comparatively weak on the host's live operating method. A complete system also needs:

- a pre-interview alignment checklist;
- a live listening and follow-up protocol;
- a post-recording fact check and learning loop.

---

# 2. Similar public methods and what they contribute

No single public system found in this review combines all of the original skill's features. Several adjacent methods provide useful components.

## Podcast production pipelines

The open-source [`podcast-pipeline`](https://github.com/chris-openclaw/podcast-pipeline) skill produces a guest research brief, organized question set, backup questions, a timed conversation map, a guest-preparation email, and persistent episode history. It is a useful example of a smaller operational package. Its strongest contribution is that the output is immediately usable by a host rather than primarily being a research archive.

## Journalism research strategy

The Journalist's Resource recommends defining the topic and information needs, identifying search terms, conducting searches, evaluating sources, and then adjusting the research strategy when gaps remain. Its source evaluation questions cover authorship, primary versus secondary material, publisher reputation, recency, bias, and documentation: [Research strategy guide](https://journalistsresource.org/home/research-strategy-guide/).

The transferable lesson is that research should include a **search log**, not only a list of successful sources. Recording queries, dates, exclusions, and failed surfaces makes the process reproducible and shows whether a gap is real or merely the result of a weak search.

## Oral-history interviewing

The Oral History Association emphasizes preparation in primary and secondary sources, an open-ended interview guide, active listening, follow-up questions, clear pre-interview agreements, preservation, access, and verification of information presented as factual: [Oral History Best Practices](https://oralhistory.org/best-practices/).

The transferable lesson is that interview preparation is not just question production. It also includes purpose, expectations, consent, boundaries, recording practices, and a plan for preserving and contextualizing what is said.

## Journalistic ethics and verification

The Society of Professional Journalists recommends taking responsibility for accuracy, verifying information before publication, using original sources where possible, providing context, identifying sources clearly, and balancing public value against potential harm: [SPJ Code of Ethics](https://www.spj.org/spj-code-of-ethics/).

The transferable lesson is that the research package should preserve the difference between a fact, a guest's claim, and the researcher's interpretation. The spoken introduction, question premises, titles, and promotional copy all require verification.

## Audio-interview practice

Current's guide to audio interviewing stresses having a clear show purpose, understanding why a guest belongs on that show, preparing enough to fact-check in real time, and using prompts such as “How do you know?”, “What is your evidence?”, and “Give me an example”: [How to elevate your audio interviews from good to great](https://current.org/2024/04/how-to-elevate-your-audio-interviews-from-good-to-great/).

The transferable lesson is that research should equip the host to recognize opinions presented as facts, unsupported numbers, vague abstractions, and evasions during the conversation.

## Agent-skill architecture

Anthropic's public skill-creator guidance recommends progressive disclosure: keep the main `SKILL.md` focused on the core workflow, and move detailed references, scripts, schemas, and assets into separate resources that are loaded only when needed: [`skill-creator/SKILL.md`](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md).

The transferable lesson is that the original 373-line skill should become a concise orchestrator with mode selection and references, rather than carrying every dashboard requirement, platform tactic, extraction schema, and verification procedure in one file.

---

# 3. Operating modes

Choose the mode before discovery begins.

| Mode | Use case | Research scope | Required deliverables |
|---|---|---|---|
| **Rapid** | Routine guest, limited public footprint, short preparation window | 5–8 high-value sources; at least one substantial prior appearance when available | Scope, fact sheet, one-page host brief, 6–8 anchor questions, live sheet |
| **Standard** | Established guest or strategically important episode | 12–20 sources; 3–5 prior appearances; independent context | Source manifest, search log, claim ledger, appearance matrix, synthesis, run of show, live sheet |
| **Flagship** | Major guest, controversial topic, book launch, extensive public footprint, reusable research asset | Broad multi-surface discovery; all important appearances; transcript corpus | Full Standard package plus per-source files, searchable corpus, optional dashboard, optional output analytics |

These are operating defaults, not universal scientific thresholds. Increase or reduce depth according to public footprint, editorial risk, episode importance, and available time.

---

# 4. The PODCAST operating system

The recommended method is organized into seven stages:

> **P**romise → **O**pen the source universe → **D**ocument the evidence → **C**onnect the patterns → **A**rchitect the conversation → **S**peak, listen, and probe → **T**rack what happened

---

## P — Define the Promise

Do not search broadly until the episode has a provisional purpose.

Complete this sentence:

> By the end of this episode, **[specific audience]** will understand **[important problem or change]**, learn **[guest-specific insight]**, and be able to **[observable action or decision]**.

Create `00_scope.md`:

```yaml
guest:
show:
audience:
recording_date:
research_mode: rapid | standard | flagship

why_this_guest:
why_now:

episode_promise: >
  By the end of the episode, listeners will understand ...
  and be able to ...

initial_hypotheses:
  -
  -
  -

unknowns_to_resolve:
  -
  -
  -

current_project_or_announcement:
sensitive_topics:
do_not_ask_constraints:
desired_length:
```

### Promise gate

Research should not proceed until the producer can answer:

1. Why is this guest unusually qualified to discuss the subject?
2. Why does the subject matter now?
3. What can this episode add beyond the guest's existing biography and standard talking points?
4. What tension, decision, failure, change, or disagreement might sustain the conversation?
5. What would make the episode unsuccessful even if the conversation were pleasant?

### Guest-provided seeds

Ask the guest or representative for:

- correct name and pronunciation;
- current title and organization;
- canonical biography and links;
- two or three prior long-form appearances they consider representative;
- current projects or claims they particularly want to discuss;
- topics requiring advance context;
- genuinely confidential or unavailable areas.

Treat these as seeds, not as the complete research universe.

---

## O — Open the Source Universe

Search multiple surfaces independently.

### Surface 1: Identity and current facts

- official personal site;
- employer or institutional page;
- current biography;
- professional profile;
- recent announcement;
- current books, products, projects, or research.

### Surface 2: Primary work

- books and papers;
- repositories and technical documentation;
- products and public demos;
- courses and talks;
- newsletters and essays;
- reports, datasets, and public records where relevant.

### Surface 3: Prior appearances

- podcast episodes;
- video interviews;
- conference talks;
- webinars and workshops;
- panels and AMAs;
- written interviews;
- transcripts and show notes.

### Surface 4: Independent context

- reputable reporting;
- academic or professional analysis;
- reviews and citations;
- conference and institutional profiles;
- informed third-party commentary.

### Surface 5: Challenges and counterarguments

- criticism of the guest's ideas;
- competing frameworks;
- failed predictions or negative results;
- limitations of the guest's preferred approach;
- controversies that are relevant and well sourced.

### Surface 6: Recent developments

Search for material published since the guest's last major appearance and anything close enough to the recording date to change the episode.

### Query families

```text
"<guest name>" interview
"<guest name>" podcast
"<guest name>" keynote OR talk OR webinar
"<guest name>" transcript
"<guest name>" "<project name>"
"<guest name>" changed my mind
"<guest name>" mistake OR failure OR lesson
"<guest name>" criticism OR controversy OR limitations
site:youtube.com "<guest name>"
site:github.com "<guest name or username>"
```

### Search log

Create `01_search_log.csv` with:

```text
search_surface
query
filters
search_date
results_reviewed
sources_included
sources_excluded
exclusion_reason
next_query_generated
notes
```

### Discovery record

Create `02_source_manifest.csv` with:

```text
source_id
canonical_url
title
creator_or_publisher
publication_date
retrieved_at
source_type
primary_or_secondary
relevance_score
authority_score
verifiability_score
independence_score
access_status
transcript_status
transcript_quality
duplicate_of
notes
```

### RAVI source score

Score each dimension from 0 to 2:

- **R — Relevance:** Does the source directly affect the proposed episode?
- **A — Authority:** Is the creator in a position to know?
- **V — Verifiability:** Are the evidence and original materials available?
- **I — Independence:** Is the source independent of the guest or organization?

Do not collapse these into a single unquestioned truth score. The separate dimensions matter. A guest's website may be authoritative for their current title and weak as independent evidence that their product is effective.

### Stop rule

Stop discovery when:

- all required surfaces have been checked; and
- two consecutive passes produce no new high-value fact, story, tension, contradiction, or angle;

or when the selected mode's research budget has been reached.

Document remaining gaps instead of pretending the source universe is complete.

---

## D — Document the Evidence

Acquire and preserve useful source material.

For every selected source:

- store the canonical URL and retrieval date;
- preserve accessible page text or transcript;
- retain timestamps for audio and video;
- record whether the transcript is human-produced, platform-generated, or locally transcribed;
- note transcription uncertainty around names, numbers, and technical terminology;
- deduplicate reposts, excerpts, and edited versions;
- mark inaccessible or authenticated sources rather than guessing their contents.

### One source, one extraction

Use a separate extraction record for every substantial source:

```yaml
source_id:
canonical_url:
title:
publisher_or_channel:
source_type:
published_date:
accessed_date:
primary_or_secondary:
reliability_notes:
summary:

facts:
  - claim:
    evidence:
    timestamp_or_location:

claims_by_guest:
  - claim:
    evidence:
    timestamp_or_location:

opinions:
  - position:
    evidence:
    timestamp_or_location:

stories:
  - setup:
    conflict:
    decision:
    outcome:
    evidence:

frameworks:
  - name:
    steps:
    limitations:

numbers_and_results:
  - value:
    meaning:
    baseline:
    measurement_period:
    evidence:

prior_questions:
  - question:
    answer_depth: shallow | medium | deep
    timestamp_or_location:

strong_answers_or_greatest_hits:
  -

unfinished_threads:
  -

possible_followups:
  -

quotable_or_clip_moments:
  -

contradictions_or_changes:
  -

research_gaps:
  -
```

### Claim ledger

Create `03_claim_ledger.csv`:

```text
claim_id
claim
original_source_id
exact_evidence_or_timestamp
source_type
publication_date
access_date
corroborating_sources
contrary_evidence
status
confidence
approved_on_air_wording
```

Use these statuses:

- **VERIFIED** — supported by a strong primary source or credible independent corroboration.
- **ATTRIBUTED** — verified only as something the guest or another party said.
- **CONTESTED** — credible evidence disagrees.
- **UNVERIFIED** — insufficient evidence.
- **STALE** — once supported, but recency is materially uncertain.

Keep these categories separate:

- **Fact:** independently checkable and adequately supported.
- **Guest claim:** something the guest has said, not necessarily independently established.
- **Researcher interpretation:** a synthesis, hypothesis, or potential angle.

Do not silently convert one category into another.

Example:

A source says:

> “Our system reduced costs by 70%.”

Unless independently verified, the episode should not state:

> “Their system reduced costs by 70%.”

Use attributed wording:

> “You have said the system reduced costs by 70%. What was measured, over what period, and against which baseline?”

---

## C — Connect the Patterns

Cross-source synthesis begins only after the important source extractions are complete.

Create `04_synthesis.md` with the following sections.

### Verified foundation

Record the current title, major projects, dates, publications, and other facts needed for the introduction. Each statement should point to the claim ledger.

### Career and idea timeline

Include only transitions that explain the guest's current thinking. A complete employment history is rarely necessary.

### Belief map

Capture:

- strongly held positions;
- recurring decision rules;
- beliefs that changed;
- areas of uncertainty;
- claims that appear context-dependent;
- tensions between different public statements.

### Story bank

Prefer stories with:

- a concrete setting;
- stakes;
- a decision;
- an obstacle or failure;
- a result;
- a lesson that is not obvious from the biography.

### Greatest-hits list

Identify stories, frameworks, and answers the guest delivers especially well but has already given repeatedly. These are useful background for the host and may support a fast bridge, but they should not dominate the episode.

### White-space list

Identify important subjects that previous interviewers did not cover or did not complete.

Use this matrix:

| Prior coverage | Answer quality | Recommended action |
|---|---|---|
| Asked repeatedly | Strong and complete | Usually avoid |
| Asked repeatedly | Formulaic or incomplete | Ask a sharper follow-up |
| Asked once | Interesting but interrupted | Reopen from the unfinished point |
| Not found | High audience value | Priority question |
| Conflicting accounts | Unclear | Verify, then ask neutrally |
| Unsupported public claim | Unverified | Ask for evidence or attribute carefully |

### Contradiction and uncertainty log

A contradiction is not automatically deception. It may reflect:

- a genuine change of mind;
- different contexts;
- imprecise language;
- a changing role;
- new evidence;
- or an actual unresolved inconsistency.

Frame the question so the guest can distinguish among these explanations.

### Episode thesis

Write one sentence:

> This episode will help **[audience]** understand **[problem]** by exploring how **[guest]** learned **[distinctive insight]**, including where that approach works, fails, and has changed.

### Angle shortlist

Generate three genuinely different angles. Score each from 0 to 2 on:

- guest uniqueness;
- audience value;
- evidence strength;
- novelty versus prior appearances;
- story potential;
- fairness and answerability.

Select:

- one primary angle;
- one secondary angle;
- one emergency backup angle.

Do not try to cover every interesting fact about the guest in one episode.

---

## A — Architect the Conversation

Design an episode, not merely a question list.

A useful 45–60 minute default arc is:

> **Hook → stakes → relevant origin story → conflict or difficult decision → framework → evidence and limits → application → callback → takeaway**

### Section purposes

| Section | Editorial purpose |
|---|---|
| Hook | Establish a surprising claim, tension, scene, or promise |
| Stakes | Explain why the subject matters now |
| Origin | Show how the guest encountered the problem |
| Conflict | Surface failure, disagreement, constraint, or change |
| Framework | Let the guest explain a model or decision process |
| Evidence and limits | Test results, exceptions, and failure boundaries |
| Application | Translate the discussion for the audience |
| Callback | Return to an earlier story or unresolved point |
| Closing | Produce a memorable principle, test, or next action |

### Must-get moments

Define three moments without which the episode would feel incomplete. Examples:

- the concrete story behind a changed belief;
- the boundary where the guest's framework stops working;
- a practical decision rule the listener can apply.

### Anchor questions

Use six to eight anchor questions. Prepared questions are a guide, not a script.

Each anchor uses this card:

```yaml
question_id:
section:
angle:
why_this_matters:
source_basis:
  - source_id:
    timestamp_or_location:
anchor_question:
prior_appearance_status: untouched | partial | heavily_covered
desired_answer_type: story | framework | evidence | reflection | prediction
followup_ladder:
  -
evidence_or_tension:
listener_payoff:
risk_or_sensitivity:
transition_to_next_section:
```

### Follow-up ladder

1. **Clarification:** What exactly do you mean by that?
2. **Concrete example:** Take me through a particular case.
3. **Mechanism:** Why did that produce the result?
4. **Decision rule:** How do you decide between the alternatives?
5. **Trade-off:** What did you give up by choosing that approach?
6. **Boundary:** Where does this stop working?
7. **Counterexample:** What would change your conclusion?
8. **Changed belief:** What do you believe differently now?
9. **Audience translation:** What should a listener do differently next?

### Question quality test

Rewrite or reject a question when it is:

- generic enough to ask any guest;
- already answered repeatedly and completely;
- double-barrelled;
- longer than the likely answer;
- designed mainly to display the host's knowledge;
- based on an unverified premise;
- leading toward praise or condemnation;
- asking for confidential information without justification;
- missing a clear audience benefit.

### Example

Generic:

> Tell me about your career journey.

Research-driven:

> In your earlier interviews, you described technical skill as the main barrier. Your recent work puts much more emphasis on organizational incentives. What changed your mind, and what evidence made the shift unavoidable?

Follow-up:

> Take me to the first project where the technical solution worked but the organization still rejected it.

The second version asks for change, evidence, and story.

---

## S — Speak, Listen, and Probe

The host should not record from a giant research dashboard. Create a one-page live sheet.

### Pre-interview alignment

Before recording, confirm:

- correct name and pronunciation;
- current title and organization;
- whether important public information is out of date;
- the episode premise and broad topic areas;
- sensitive or unavailable subjects;
- recording, editing, quotation, and publication expectations;
- relevant financial or organizational interests;
- technical setup;
- one story the guest has not told repeatedly;
- one view the guest has changed recently.

The guest can correct factual biography information and explain real boundaries. That does not automatically grant veto power over fair editorial questions or conclusions.

### Live sheet

Create `06_live_sheet.md`:

```markdown
# Guest
Name and pronunciation:
Current role:

# Episode promise
One sentence.

# Three must-get moments
1.
2.
3.

# Anchor questions
1–8, one line each.

# Best follow-ups
- How do you know?
- Give me a concrete example.
- What was the baseline?
- What did that choice cost?
- Where does the approach fail?
- What changed your mind?
- Who should not follow this advice?

# Facts to handle carefully
Names, dates, numbers, contested claims, approved wording.

# Already overcovered
Questions and stories to avoid.

# Parking lot
Unexpected leads to revisit.

# Closing
One callback and one practical takeaway question.
```

### Live response markers

Mark each anchor during the interview:

- **A** — answered;
- **P** — partially answered;
- **D** — dodged;
- **N** — new and valuable direction.

### What to listen for

| Guest response contains… | Host should consider… |
|---|---|
| An abstract claim | “Give me a concrete example.” |
| A large number or result | “What was the baseline and measurement period?” |
| A polished success story | “What failed before this worked?” |
| A strong recommendation | “Who should not follow this advice?” |
| A changed position | “What evidence changed your mind?” |
| Jargon | “How would you explain that to a new practitioner?” |
| A general description | “Take me to the moment when this happened.” |
| A dodge | Reframe once and explicitly return later |
| Unexpected emotion or hesitation | Pause and invite elaboration |
| A contradiction | State both versions neutrally and ask for reconciliation |

AI can transcribe, retrieve supporting passages, flag names and numbers, and track unused questions. The host should retain control of interruption, challenge, silence, pacing, and changes of direction.

---

## T — Track What Happened

Research should become show memory rather than disappear after publication.

Create `07_postmortem.md`:

```yaml
episode_promise_fulfilled: yes | partly | no

strongest_moments:
  -

questions_that_worked:
  -

questions_that_failed:
  -

missed_followups:
  -

claims_requiring_verification:
  -

guest_corrections:
  -

topics_now_marked_do_not_repeat:
  -

new_research_leads:
  -

potential_future_guests:
  -

changes_for_next_episode:
  -
```

Maintain a show-level memory table:

```text
guest
episode
topic
question
answer_depth
timestamp
clip_quality
followup_needed
do_not_repeat
```

After recording:

- verify unexpected factual claims before using them in titles, descriptions, or clips;
- preserve corrections and updated wording;
- record which questions produced stories, specificity, disagreement, or frameworks;
- note which questions generated rehearsed answers;
- add new sources and claims to the evidence ledger;
- update the do-not-repeat list;
- evaluate whether the episode promise was fulfilled.

---

# 5. Recommended artifacts

## Minimal file structure

```text
guest_research/<guest_slug>/
  00_scope.md
  01_search_log.csv
  02_source_manifest.csv
  03_claim_ledger.csv
  sources/
    <source_id>.md
  04_appearances_matrix.csv
  05_synthesis.md
  06_run_of_show.md
  07_live_sheet.md
  08_postmortem.md
```

## Flagship additions

```text
  transcripts/
  extraction/per_source/
  search_index/
  dashboard/
  output_analytics/
```

### When to build a search index

Build a search index when the corpus is too large to inspect manually, several producers need retrieval, or the research will be reused. Preserve source IDs, canonical URLs, section names, and timestamps with every chunk.

### When to build output analytics

Measure public output only when it materially supports the episode thesis. Clearly label every figure **MEASURED** or **ESTIMATED**, state assumptions, distinguish raw repository churn from authored code, flag mixed authorship, and explain what the metric cannot show.

---

# 6. Editorial and ethical rules

1. **Serve the audience.** Guest preparation should improve clarity and fairness, not become reputation management.
2. **Verify before asserting.** Use original sources where possible and preserve context.
3. **Attribute unsupported claims.** Something the guest said is not automatically an independently established fact.
4. **Record uncertainty.** Blocked, gated, stale, and incomplete sources belong in the research-gap log.
5. **Avoid private or sensitive inference.** Public availability alone does not make information relevant or ethical to use.
6. **Challenge ideas fairly.** Ask where frameworks fail, what incentives shape the claim, and what evidence would change the guest's mind.
7. **Do not manufacture controversy.** A difficult question needs evidence and an audience rationale.
8. **Respect real boundaries.** Do not pressure guests to breach confidentiality, NDAs, or personal safety.
9. **Correct transparently.** Update the research package and published materials when significant new information appears.
10. **Preserve provenance.** Every factual premise should remain traceable to a source passage or timestamp.

---

# 7. Definition of done

A guest-research pass is complete when:

1. The episode has one clear audience promise.
2. The guest's current identity, title, and introduction facts are verified.
3. The required discovery surfaces have been checked.
4. Search queries and important exclusions are recorded.
5. Every important fact and number is traceable to evidence.
6. Facts, guest claims, and researcher interpretations are visibly separated.
7. Previous appearances have produced a do-not-repeat list.
8. At least three high-value white-space questions have been identified.
9. Each anchor question has a source basis, audience payoff, and follow-up path.
10. Contradictions and uncertainty are framed fairly.
11. The host has a one-page live sheet.
12. Recent developments have been checked close to recording.
13. Sensitive personal traits have not been inferred from public traces.
14. The post-recording learning record is updated.

---

# 8. Reusable master instruction

```text
Research [GUEST] for [SHOW AND AUDIENCE] in
[RAPID / STANDARD / FLAGSHIP] mode.

Episode context:
[CONTEXT]

Desired listener outcome:
By the end of the episode, listeners should understand [X]
and be able to [Y].

Constraints and sensitive areas:
[CONSTRAINTS]

Do not write interview questions immediately.

First:
1. Define the episode promise and research hypotheses.
2. Build a multi-surface source manifest.
3. Record search queries, dates, and inclusion/exclusion decisions.
4. Analyze each substantial source separately.
5. Create a claim ledger with exact evidence and the statuses:
   VERIFIED, ATTRIBUTED, CONTESTED, UNVERIFIED, or STALE.
6. Analyze prior appearances and create a do-not-repeat matrix.
7. Identify contradictions, changes of mind, stories, decision rules,
   failures, and unresolved questions.
8. Propose three distinct episode angles and select one primary angle.

Then produce:
- A one-page host brief.
- A sourced guest introduction.
- Six to eight anchor questions.
- A source basis and rationale for every anchor question.
- A follow-up ladder for every anchor.
- Ten backup prompts.
- A 45–60 minute conversation architecture.
- A one-page live interview sheet.
- A pre-interview verification checklist.
- Research gaps and factual uncertainties.

Treat social media and aggregators as discovery leads unless the material is
directly attributable and relevant. Do not infer sensitive personal traits.
Do not present attributed claims as independently verified facts.
Prefer a useful, evidence-grounded conversation over maximum source volume.
```

---

# 9. Recommended skill-package architecture

The reusable skill should use progressive disclosure:

```text
podcast-guest-researcher/
  SKILL.md
  references/
    operating-modes.md
    source-hierarchy.md
    discovery-query-patterns.md
    extraction-schema.md
    claim-verification.md
    synthesis-method.md
    question-design.md
    live-interview-protocol.md
    editorial-ethics.md
    output-templates.md
  scripts/
    normalize_urls.py
    dedupe_manifest.py
    transcript_stats.py
    validate_claims.py
    validate_sources.py
  evals/
    evals.json
```

`SKILL.md` should contain only:

- purpose and trigger conditions;
- required inputs;
- mode selection;
- the main workflow;
- escalation and stop rules;
- required outputs by mode;
- links to the appropriate references;
- the definition of done.

Large schemas, examples, platform-specific tactics, dashboard requirements, and detailed templates belong in references or scripts.

---

# 10. Implementation order

A practical rollout sequence is:

### Version 1 — editorial core

Implement:

- scope and episode promise;
- source manifest;
- per-source extraction;
- prior-appearance matrix;
- claim ledger;
- synthesis;
- question cards;
- live sheet.

### Version 2 — operational quality

Add:

- search logging;
- deduplication scripts;
- transcript-quality checks;
- pre-interview verification;
- postmortem and show memory;
- realistic evaluation prompts.

### Version 3 — flagship infrastructure

Add only when justified:

- searchable corpus;
- appearance subpages;
- interactive timeline;
- dashboard;
- public-output analytics;
- browser and accessibility verification.

This sequence preserves the most valuable editorial behavior before investing in infrastructure.

---

# References

1. Original source: attached `podcast-guest-researcher` skill, reviewed in full.
2. [Podcast Pipeline — guest research, interview prep, production, and episode tracking](https://github.com/chris-openclaw/podcast-pipeline)
3. [The Journalist's Resource — Research strategy guide for finding quality, credible sources](https://journalistsresource.org/home/research-strategy-guide/)
4. [Oral History Association — Oral History Best Practices](https://oralhistory.org/best-practices/)
5. [Society of Professional Journalists — SPJ Code of Ethics](https://www.spj.org/spj-code-of-ethics/)
6. [Current — How to elevate your audio interviews from good to great](https://current.org/2024/04/how-to-elevate-your-audio-interviews-from-good-to-great/)
7. [Anthropic Skills — Skill Creator and progressive-disclosure guidance](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)

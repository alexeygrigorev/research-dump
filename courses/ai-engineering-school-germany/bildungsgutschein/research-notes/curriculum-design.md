# How to plan a 16-week / 640-UE AI-engineering bootcamp curriculum: evidence and method

Research date: 2026-11-12. Every URL below was accessed on 2026-11-12 unless stated otherwise.

## 0. How to read this file

Evidence status labels used on every source:

- **[READ]** = the page or PDF was fetched and its text read (directly, or PDF text extracted locally with `pdftotext`). Quotes marked "verbatim" were checked against the extracted text.
- **[READ-ABSTRACT]** = only the abstract or landing page was fetched and read, not the full paper.
- **[SNIPPET]** = known only from a search-result snippet or a secondary summary. Do not cite as verified; fetch the primary before using in a formal document.
- **[FAILED]** = fetch attempted and blocked (403/404/login wall). Listed so nobody assumes it was read.

Caveat on quotes: pages fetched through the WebFetch tool are summarised by a small model before I see them. Quotes from PDFs (UbD, Biggs, Krathwohl, KMK, Beirat, IBM, WEF, Thayer & Ko, ACM task force, CS2023, Clark/Kirschner/Sweller, Porter, LaunchCode) and the Teaching Tech Together quotes were verified against raw text. Other quotes are as returned by the tool and should be re-checked before being printed in an AZAV concept or marketing copy.

Sections 1-6 report what sources say. Section 7 onwards is synthesis; every recommendation there is labelled **RECOMMENDATION** and tied back to sources.

---

## 1. Curriculum design frameworks

### 1.1 Backward design (Wiggins & McTighe, Understanding by Design)

- **Source [READ]**: Jay McTighe & Grant Wiggins, "Understanding by Design Framework" (ASCD white paper), 2012. https://files.ascd.org/staticfiles/ascd/pdf/siteASCD/publications/UbD_WhitePaper0312.pdf
- Findings (verbatim):
  - Two key ideas: "1) focus on teaching and assessing for understanding and learning transfer, and 2) design curriculum 'backward' from those ends."
  - "Effective curriculum is planned backward from long-term, desired results through a three-stage design process (Desired Results, Evidence, and Learning Plan). This process helps avoid the common problems of treating the textbook as the curriculum rather than a resource, and activity-oriented teaching in which no clear priorities and purposes are apparent."
  - Stage 1 "Identify Desired Results", Stage 2 "Determine Assessment Evidence", Stage 3 "Plan Learning Experiences and Instruction".
  - Alignment: "the Stage 1 content and understanding must be what is assessed in Stage 2 and taught in Stage 3."
  - "Backward design encourages teachers and curriculum planners to first think like assessors before designing specific units and lessons."
  - Performance tasks "ask students to apply their learning to a new and authentic situation"; they are "culminating performances for a unit of study", not daily lesson items.
  - Tenet 7: "The results of our designs—student performance—inform needed adjustments in curriculum as well as instruction" (continuous improvement is built into the framework).
- Usable rule: write transfer goals (what graduates do on the job) first, then the performance tasks that prove them, then the weekly plan.

### 1.2 Constructive alignment (Biggs)

- **Source [READ]**: John Biggs, "Constructive alignment in university teaching", HERDSA Review of Higher Education, Vol. 1, 2014, pp. 5-22. Landing page https://www.herdsa.org.au/herdsa-review-higher-education-vol-1/5-22 ; PDF https://herdsa.org.au/system/files/HERDSARHE2014v01p05_0.pdf
  - (johnbiggs.com.au was fetched and is now a parked domain: **[FAILED]** as a source.)
- Findings (verbatim):
  - "Constructive alignment (CA) is an outcomes-based approach to teaching in which the learning outcomes that students are intended to achieve are defined before teaching takes place. Teaching and assessment methods are then designed to best achieve those outcomes and to assess the standard at which they have been achieved."
  - Operational steps: "1) Describe the intended learning outcomes (ILOs) for the unit, using one verb (or at most two) for each outcome... 2) Create a learning environment using teaching/learning activities (TLAs) that require students to engage each verb... 3) Use assessment tasks (ATs) that also contain that verb, thus enabling one with help of predetermined using rubrics to judge how well students' performances meet the criteria. 4) Transform these judgments into final grades."
  - "The verb in the ILO becomes the common link that establishes alignment between the ILO, the teaching/learning activities, and the assessment tasks."
  - Assessment "is about judging the whole performance against predetermined and public rubrics, not by awarding marks analytically for aspects of the tasks and then summing them. Analytic assessment is useful formatively."
  - Evidence caveat from Biggs himself: "constructively aligned teaching seems to produce high quality learning outcomes and student satisfaction. We now require larger scale controlled studies."
- Usable rule: one verb per outcome; the same verb must appear in the activity and in the assessment task.

### 1.3 Bloom's revised taxonomy (Anderson & Krathwohl)

- **Source [READ]**: David R. Krathwohl, "A Revision of Bloom's Taxonomy: An Overview", Theory Into Practice 41(4), 2002, pp. 212-218. Copy fetched from a university server: https://rvc-web-app01.live01.azure.rvc.ac.uk/Media/Default/About/Academic%20Quality,%20Regulations%20and%20Procedures/Academic%20Quality%20Assurance%20and%20Enhancement%20Procedures/Module%20Development%20and%20Approval/A%20Revision%20of%20Bloom's%20Taxonomy%20-%20An%20Overview.%20David%20R.%20Krathwohl.pdf (publisher DOI 10.1207/s15430421tip4104_2, not fetched). The depauw.edu copy returned 404.
- Findings (verbatim from scanned text, OCR artefacts corrected):
  - Objectives "consist of a noun or noun phrase—the subject matter content—and a verb or verb phrase—the cognitive process".
  - Cognitive process dimension: "Remember - Retrieving relevant knowledge from long-term memory"; "Understand - Determining the meaning of instructional messages"; "Apply - Carrying out or using a procedure in a given situation"; "Analyze - Breaking material into its constituent parts and detecting how the parts relate to one another and to an overall structure or purpose"; "Evaluate - Making judgments based on criteria and standards"; "Create - Putting elements together to form a novel, coherent whole or make an original product."
  - Knowledge dimension: Factual, Conceptual, Procedural, Metacognitive (four categories; table headed "A. Factual Knowledge - The basic elements that students must know to be acquainted with a discipline or solve problems in it").
  - The hierarchy is relaxed: categories "overlap one another".
- Usable rule: write each learning outcome as verb (cognitive process) + noun (knowledge type). For a bootcamp for working programmers, most outcomes should sit at Apply/Analyze/Evaluate/Create; Evaluate ("Checking", "Critiquing") is the natural home for reviewing AI-generated code.

### 1.4 Competency-based education (CBE)

- **Source [SNIPPET]**: Competency-Based Education Network (C-BEN), "Quality Framework for Competency-Based Education Programs", 2017. Seen only via search results (e.g. https://www.insidehighered.com/sites/default/server_files/files/CBEN_Quality_Standards_for_CompetencyBased_Educational_Programs(1).pdf - 2016 draft, not fetched). Snippet says: eight elements, each with principles, standards and performance indicators rated "initial, emerging, developed, and highly developed"; a draft principle that "each competency is explicitly stated and unambiguously provides descriptions of what a learner must master". Not verified against the primary.
- **Source [READ]**: ACM/IEEE-CS/AAAI, "CS2023" Executive Summary, 2024. https://csed.acm.org/wp-content/uploads/2024/04/1.1-Executive-Summary.pdf
  - Verbatim: "Interest is growing among educators in a competency model of the curriculum. A Competency Framework has been provided for programs to create their own competency model of the curriculum tailored to local needs."
  - Verbatim on core vs. depth: "Topics that every graduate must know have been circumscribed as CS Core and kept to a minimum. Topics recommended for in-depth study have been labeled KA Core." and "It is increasingly difficult for programs to be all things to all people. Programs can now select the knowledge areas on which to focus."

### 1.5 German / European framing

**EQF**
- **Source [READ]**: European Union, Europass, "Description of the eight EQF levels". https://europass.europa.eu/en/description-eight-eqf-levels
- Level 5: knowledge "Comprehensive, specialised, factual and theoretical knowledge within a field of work or study..."; skills "A comprehensive range of cognitive and practical skills required to develop creative solutions to abstract problems"; responsibility "Exercise management and supervision in contexts of work or study activities where there is unpredictable change...".
- Level 6: knowledge "Advanced knowledge of a field of work or study, involving a critical understanding of theories and principles"; skills "Advanced skills, demonstrating mastery and innovation, required to solve complex and unpredictable problems..."; responsibility "Manage complex technical or professional activities or projects, taking responsibility for decision-making...". (Quotes truncated by the tool; check full wording on the page.)

**DQR**
- **Source [READ]**: Bund-Länder-Koordinierungsstelle DQR, "DQR-Niveaus". https://www.dqr.de/dqr/de/der-dqr/dqr-niveaus/dqr-niveaus_node.html
- Eight levels; two competence dimensions: Fachkompetenz (Wissen, Fertigkeiten) and Personale Kompetenz (social aspects, independence/responsibility, reflection, learning competence).
- Niveau 5 "beschreibt Kompetenzen zur selbständigen Planung und Bearbeitung umfassender fachlicher Aufgabenstellungen" in a complex, specialised, changing field. Niveau 6: "Die Anforderungsstruktur ist durch Komplexität und häufige Veränderungen gekennzeichnet."
- Note: a private, non-formal bootcamp is not formally assigned a DQR level; the descriptors are useful as a wording model for "kompetenzorientierte Lernziele" (my reading, not stated on the page).

**KMK Lernfeldkonzept / Handlungsorientierung**
- **Source [READ]**: Sekretariat der Kultusministerkonferenz, "Handreichung für die Erarbeitung von Rahmenlehrplänen der Kultusministerkonferenz für den berufsbezogenen Unterricht in der Berufsschule...", Berlin, 17 June 2021. https://www.kmk.org/fileadmin/veroeffentlichungen_beschluesse/2021/2021_06_17-GEP-Handreichung.pdf
- Findings (verbatim):
  - "Handlungskompetenz wird verstanden als die Bereitschaft und Befähigung des Einzelnen, sich in beruflichen, gesellschaftlichen und privaten Situationen sachgerecht durchdacht sowie individuell und sozial verantwortlich zu verhalten." It unfolds in "Fachkompetenz, Selbstkompetenz und Sozialkompetenz."
  - Lernfelder "sind aus Handlungsfeldern des jeweiligen Berufes entwickelt"; "Handlungsfelder orientieren sich an berufsbezogenen Aufgaben- oder Problemstellungen innerhalb zusammengehöriger Arbeits- und Geschäftsprozesse... Durch didaktische Reflexion und Aufbereitung werden aus den Handlungsfeldern, die an der gegenwärtigen und zukünftigen Berufspraxis orientiert sind, die Lernfelder ... entwickelt."
  - Handlungsorientierter Unterricht: "Didaktische Bezugspunkte sind Situationen, die für die Berufsausübung bedeutsam sind." and "Lernen vollzieht sich in vollständigen Handlungen, möglichst selbst ausgeführt oder zumindest gedanklich nachvollzogen."
  - Formulation steps for a Lernfeld: (1) name it with the "Kernkompetenz der übergeordneten beruflichen Handlung möglichst kurz, aussagekräftig und aktiv"; (2) a generalising statement of the core competence acquired by the end; (3) "die differenzierten beruflichen Handlungen gegliedert nach den Phasen der vollständigen Handlung".
  - Sequencing: Lernfelder are to be structured "dass eine Kompetenzentwicklung spiralcurricular erfolgt."
  - Time budgeting rule: "lediglich 80 % des rechnerischen Zeitrichtwertes" are to be filled when formulating competences; time values "sollen ... durch 20 teilbar sein und in der Regel 40, 60 oder 80 Unterrichtsstunden umfassen."
  - Assessment (verbatim): "Der Orientierung der Struktur von Ordnungsmitteln an den Arbeits- und Geschäftsprozessen sollten auch die Prüfungen durch ganzheitliche, handlungsorientierte Aufgaben- oder Problemstellungen folgen."
- Usable rules: derive modules from job action fields; name modules as actions; plan only 80 % of each module's hours; size modules in multiples of 20 UE (40/60/80); revisit competences spirally.

**AZAV: what the course concept must show**
- **Source [READ]**: AZAV (Akkreditierungs- und Zulassungsverordnung Arbeitsförderung). https://www.gesetze-im-internet.de/azav/BJNR050400012.html
  - § 3 Abs. 1 Nr. 1: a measure requires that "Ziele, Dauer und Inhalte der Maßnahme jeweils auf die Voraussetzungen der Zielgruppe und das Maßnahmeziel hin konzipiert sind"; Nr. 2: "sie aktuelle Entwicklungen des Ausbildungs- und Arbeitsmarktes berücksichtigt."
  - § 3 Abs. 3: the fachkundige Stelle considers "insbesondere die Maßnahmekonzeption einschließlich ihrer Kalkulation"; "Der Kostenkalkulation für eine Gruppenmaßnahme ist grundsätzlich eine Gruppengröße von zwölf Teilnehmenden zu Grunde zu legen."
  - § 2 Abs. 5: participants receive "eine Teilnahmebescheinigung mit Angaben zum Inhalt, zeitlichen Umfang und Ziel der Maßnahme".
  - § 5 Abs. 5: reportable changes are those "die die Standorte des Trägers, seine Fachbereiche und die Durchführung der Maßnahme betreffen."
  - The AZAV text itself does not use the words "Lernerfolgskontrolle" or "Unterrichtseinheit" (per the fetched text).
- **Source [READ]**: Beirat nach § 182 SGB III, "Empfehlungen des Beirats nach § 182 SGB III", Stand/Bekanntmachung 17.06.2026 (current version; copy hosted by Der Paritätische). https://www.der-paritaetische.de/fileadmin/user_upload/Fachinfos/doc/260617-Beratsempfehlungen.pdf ; announcement page https://www.der-paritaetische.de/alle-meldungen/neue-empfehlungen-des-azav-beirates-vom-17062026/ . Previous version of 10.09.2024 also read: https://certqua.de/pdf/ueber-uns/downloads/offener-bereich/_Empfehlungen%20des%20Beirats_20240910.pdf
  - Provider QM system must cover (verbatim): "Verfahren zur Herleitung von Entwicklungs-, Eingliederungs-, Lehr- und Lernzielen", "Einsatz einer angemessenen Methodik", "Überwachung von Lernprozessen", "Erfassung, ob Entwicklungs-, Eingliederungs- bzw. Lernziele erreicht sind und die Maßnahmequalität gewährleistet ist", "Erfassung der Teilnehmerpräsenz und Abbruchquoten", "Erfassung ausbildungs- und/oder arbeitsmarktlicher Eingliederungsergebnisse", "Umgang mit den Evaluierungsergebnissen als Teil des kontinuierlichen Verbesserungsprozesses mit besonderem Blick auf Maßnahmekonzeption und -durchführung", and "Aktuelle und systematische Analyse der kundenrelevanten Bedarfe in Bezug auf die Zielsetzung der Maßnahme" / "Kontinuierliche Einbeziehung der Analyseergebnisse in die Maßnahmekonzeption".
  - Definition of a teaching unit (section "Unterrichts-/Maßnahmestunde", V01 valid from 01.07.2025), verbatim: "Unabhängig von der Durchführungsform ist Unterricht davon charakterisiert, dass jederzeit eine direkte, unmittelbare Interaktion zwischen den Lehr- und Fachkräften und den Teilnehmenden möglich ist. Während der gesamten Dauer wird der Unterricht/die Maßnahme von den hierfür vorgesehenen Lehr- und Fachkräften durchgeführt bzw. aktiv begleitet (synchroner Informationsaustausch). Unterricht kann beispielsweise auch den begleiteten Einsatz von interaktiven Medien, Projekt-/Gruppenarbeiten oder innovative Lernformen beinhalten. In diesen Fällen muss im Maßnahmekonzept u.a. konkret dargestellt werden, wie der synchrone Informationsaustausch sowie die Lernerfolgskontrolle sichergestellt werden."
  - Not teaching: "wenn die Teilnehmenden sich Kenntnisse und Fähigkeiten mithilfe von Medien selbst aneignen (z.B. Selbstlerneinheiten, Lehrbriefe, Learning Nuggets) und keine Möglichkeit besteht, jederzeit und unmittelbar mit den ... Lehr- und Fachkräften in Kontakt zu treten". A forum or hotline "ist nicht ausreichend".
  - Asynchronous parts "zählen aber nicht zu den Unterrichts-/ Maßnahmestunden" and are shown separately on the certificate; "Individuelle Vor- bzw. Nachbereitungszeiten der Teilnehmenden (außerhalb der Lehrgangszeit) sind klar von asynchronen Anteilen abzugrenzen und nicht Bestandteil der Maßnahme."
  - 2026 addition: "Synchroner Informationsaustausch liegt nur vor, wenn eine direkte und unmittelbare Interaktion zwischen Teilnehmenden und Lehr- und Fachkraft gemäß Konzept in einem definierten Zeitraum verbindlich vorgesehen ist."
- **Source [READ]**: Kiwa ZERTPUNKT GmbH, "Informationsblatt zur Maßnahmezulassung" (Info_MN-Zulassung_FO_0424). https://www.kiwa.com/4971cb/globalassets/germany/standorte/zertpunkt/2.-tragerzulassung-nach-azav/info_mn-zulassung_fo_0424.pdf
  - Restates the statutory approval conditions for further-training measures, including that the measure "mit einem Zeugnis, das Auskunft über den Inhalt des vermittelten Lehrstoffs gibt, abschließt", and that a measure is excluded if "überwiegend nicht berufsbezogene Inhalte vermittelt werden."
- Implications (my reading): all 640 UE must be instructor-led or instructor-accompanied in real time; accompanied project and group work counts, but the concept must state how synchronous interaction and Lernerfolgskontrolle happen in those blocks; homework and self-study cannot be counted; the final certificate must list the content taught.

---

## 2. What works for teaching programming / engineering to adults

### 2.1 Active learning vs. lecturing

- **Source [READ-ABSTRACT]** (via Europe PMC API record; PNAS and PMC pages returned 403/captcha): Freeman, Eddy, McDonough, Smith, Okoroafor, Jordt, Wenderoth, "Active learning increases student performance in science, engineering, and mathematics", PNAS 111(23), 2014, 8410-8415. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:24821756&resultType=core&format=json (article DOI 10.1073/pnas.1319030111)
  - Meta-analysis of 225 studies of undergraduate STEM courses; exam/concept-inventory scores improved "0.47 SDs under active learning (n = 158 studies)"; odds ratio for failing under traditional lecturing "1.95" (n = 67 studies); average exam scores improved "by about 6%"; lecture students about 1.5 times as likely to fail.
  - Limit: undergraduates, not adult professionals.

### 2.2 Guided instruction, worked examples, cognitive load, expertise reversal

- **Source [READ]**: Richard E. Clark, Paul A. Kirschner, John Sweller, "Putting Students on the Path to Learning: The Case for Fully Guided Instruction", American Educator, Spring 2012. https://www.aft.org/sites/default/files/Clark.pdf (summarises Kirschner, Sweller & Clark 2006, Educational Psychologist 41(2) - the 2006 paper itself is **[SNIPPET]** only.)
  - Verbatim: "Decades of research clearly demonstrate that for novices (comprising virtually all students), direct, explicit instruction is more effective and more efficient than partial guidance."
  - Verbatim: "this does not mean direct, expository instruction all day every day. Small group and independent problems and projects can be effective—not as vehicles for making discoveries, but as a means of practicing recently learned content and skills."
  - Verbatim on worked examples and experienced learners: "this discussion of worked examples applies to novices—not experts. In fact, the worked-example effect first disappears and then reverses as the learners' expertise increases. That is, for experts, solving a problem is more effective than studying a worked example." This is named the "expertise reversal effect".
  - Relevance: bootcamp learners "already program" but are novices in AI engineering. Expect worked examples to help on new concepts (evals, retrieval, agent loops) and to be redundant on general coding.
- **Source [FAILED]**: Sweller, van Merriënboer, Paas, "Cognitive Architecture and Instructional Design: 20 Years Later", Educational Psychology Review, 2019 (https://link.springer.com/article/10.1007/s10648-019-09465-5 redirected to a login/cookie wall). Not read; do not quote.
- **Source [READ]**: The Carpentries, Instructor Training, "Memory and Cognitive Load". https://carpentries.github.io/instructor-training/05-memory.html
  - Guided practice is "creating a structure that narrowly guides focus on specific skills and knowledge in a stepped fashion"; faded examples are "worked examples with targeted details 'faded' out"; "assessments should be frequent".

### 2.3 Greg Wilson, Teaching Tech Together

- **Source [READ]** (three offsets of the single-page book plus direct text check): Greg Wilson, "Teaching Tech Together", Taylor & Francis 2019, CC BY-NC 4.0. https://teachtogether.tech/en/index.html
- Findings:
  - Lesson design is backward: create learner personas; brainstorm; "Create a summative assessment (Section 2.1) to define your overall goal. This can be the final exam for a course or the capstone project for a one-day workshop; regardless of its form or size, it shows how far you hope to get more clearly than a point-form list of objectives" (verbatim); then formative assessments for each skill, order them, write material linking them.
  - Learner persona = general background, what they already know, what they want to do, special needs.
  - Formative assessment cadence (verbatim): "you should do something that takes a minute or two every 10–15 minutes to make sure that your learners are actually learning. This rhythm isn't based on an intrinsic attentional limit ... Instead, the guideline ensures that if a significant number of people have fallen behind, you only have to repeat a short portion of the lesson."
  - Cognitive load: "Our goal as teachers is to maximize the memory available to handle intrinsic load." Faded examples; Parsons problems.
  - Live coding: "The most important rule of live coding is to embrace your mistakes."
  - Peer instruction: ask an MCQ that "probes for their misconceptions"; if answers split, learners "argue with each other in groups of 2–4, then vote again."
  - Pair programming (verbatim): "the two switch roles several times per hour"; "put everyone in pairs, not just learners who are struggling"; switch roles "three or four times per hour so that the stronger personality in each pair doesn't dominate".
  - Mixed ability: "a third of your class is lost and a third is bored"; provide "extra self-paced exercises so that more advanced learners don't finish early and get bored".
  - Authentic task: "something that learners believe they would actually do in real life."
  - Maintainability (verbatim): "a lesson is maintainable if it's cheaper to update it than to replace it. This equation depends on four factors: How well documented the course's design is..." Short units are cheaper to re-record or replace than long ones.
  - Rules include "Never teach alone" and "Remember that no lesson survives first contact with learners".
- **Source [READ]**: Neil C. C. Brown & Greg Wilson, "Ten quick tips for teaching programming", PLOS Computational Biology 14(4): e1006023, 2018. https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006023
  - Tips: no geek gene; use peer instruction; use live coding; have students make predictions; use pair programming; use worked examples with labelled subgoals; stick to one language; use authentic tasks; remember novices are not experts; don't just code (Parsons problems etc.).
  - "Novices do not become professionals simply by doing what professionals do at a slower pace."

### 2.4 The Carpentries instructor and lesson-developer training

- **Source [READ]**: The Carpentries, Instructor Training index. https://carpentries.github.io/instructor-training/ (episode list incl. "Building Skill With Practice", "Memory and Cognitive Load", "Building Skill With Feedback", "Live Coding is a Skill").
- **Source [READ]**: "Building Skill With Practice". https://carpentries.github.io/instructor-training/02-practice-learning.html - formative assessment should happen "while we teach"; MCQs designed so each wrong answer reveals a specific misconception; three kinds of misconception (factual errors, broken models, fundamental beliefs).
- **Source [READ]**: "Live Coding is a Skill". https://carpentries.github.io/instructor-training/17-live.html - "Live coding forces the instructor to slow down." "Coding-along gives learners continuous practice and feedback." "Mistakes made during participatory live coding are valuable learning opportunities."
- **Source [READ]**: The Carpentries, Collaborative Lesson Development Training, "Lesson Design". https://carpentries.github.io/lesson-development-training/lesson-design.html (index: https://carpentries.github.io/lesson-development-training/)
  - Backward design after Nicholls, five iterative phases after defining the target audience: "Define desired learning outcomes"; "Design assessments to determine progress towards desired outcomes"; "Write content to lead learners from one of these assessments to the next"; "Assess learner progress towards outcomes during teaching"; "evaluate how closely the outcomes meet the objectives".
  - Uses SMART learning objectives, learner profiles, authentic tasks, pilots.

### 2.5 Peer instruction

- **Source [READ]** (abstract and first page from the PDF): Leo Porter, Cynthia Bailey-Lee, Beth Simon, "Halving Fail Rates using Peer Instruction: A Study of Four Computer Science Courses", SIGCSE 2013. https://files.software-carpentry.org/training-course/2012/08/porter-halving-fail-peer-instruction-2013.pdf
  - Verbatim: "Evaluating 10 years of instruction of 4 different courses spanning 16 PI course instances, we find that adoption of the PI methodology in the classroom reduces fail rates by a per-course average of 61% (20% reduced to 7%) compared to Standard Instruction".

### 2.6 Pair programming

- **Source [READ-ABSTRACT]**: Karthikeyan Umapathy & Albert D. Ritzhaupt, "A meta-analysis of pair-programming in computer programming courses: Implications for educational practice", ACM Transactions on Computing Education 17(4), 2017. https://digitalcommons.unf.edu/unf_faculty_publications/1812
  - 18 manuscripts, 28 independent effect sizes, N = 3,308; "positive results in favor of pair programming in three of four domains with exception to affective measures." Numeric effect sizes are not in the abstract.
- **[SNIPPET]**: Salleh, Mendes & Grundy 2011 (IEEE TSE) systematic review; a 2024 meta-analysis of collaborative vs individual programming problem solving reporting Hedges' g = 0.562 on cognitive outcomes. Not verified.

### 2.7 Code review as pedagogy

- **[SNIPPET]**: Indriasari, Luxton-Reilly & Denny, "A Review of Peer Code Review in Higher Education", ACM TOCE 20(3), 2020, DOI 10.1145/3403935. Snippet of abstract: most-cited benefits include gains in programming-related skills; most-cited barrier is low student engagement. unpaywall.org redirect was not followed; not verified.

### 2.8 Retrieval and spaced practice

- **Source [READ-ABSTRACT]** (Europe PMC API): Dunlosky, Rawson, Marsh, Nathan, Willingham, "Improving Students' Learning With Effective Learning Techniques", Psychological Science in the Public Interest, 2013. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:26173288&resultType=core&format=json
  - "Practice testing and distributed practice received high utility assessments." "Elaborative interrogation, self-explanation, and interleaved practice received moderate utility assessments." Low: summarization, highlighting, keyword mnemonic, imagery for text, rereading.

### 2.9 Project-based learning

- **[SNIPPET]**: a 2019 Educational Research Review meta-analysis ("Revisiting the effects of project-based learning on students' academic achievement: A meta-analysis investigating moderators") reporting mean weighted effect size 0.71 vs traditional instruction. Authors and details not verified; mostly school-level studies. Treat as weak support.
- Read sources that bear on PBL: Clark, Kirschner & Sweller (projects work "as a means of practicing recently learned content and skills", not as discovery); Brown & Wilson (authentic tasks); KMK (vollständige Handlung); Tenhunen et al. on capstones (section 3).

### 2.10 Deliberate practice

- **[SNIPPET]**: Macnamara, Hambrick & Oswald, Psychological Science 25(8), 2014: deliberate practice explained 26 % of variance in games, 21 % music, 18 % sports, 4 % education, under 1 % professions. Figures are from search snippets; Ericsson's group disputes the inclusion criteria. Use only as a caution that "more hours" is not sufficient by itself.

### 2.11 Formative assessment

- **[SNIPPET]**: Black & Wiliam, "Inside the Black Box", Phi Delta Kappan, 1998: typical effect sizes 0.4-0.7 for formative assessment interventions. The michigan.gov copy returned 403; not verified.
- Read sources supporting frequent formative checks: Teaching Tech Together; Carpentries instructor training (above).

### 2.12 Felienne Hermans

- **Source [READ]** (publisher page only): Felienne Hermans, "The Programmer's Brain", Manning, 2021. https://www.manning.com/books/the-programmers-brain
  - The page describes chapters on long-term / short-term / working memory in reading and writing code, working-memory overload and aids (state tables, dependency graphs), mental models and notional machines, misconceptions from prior knowledge, naming, and onboarding (separating domain learning from code exploration). The book text was not read.
- **[SNIPPET]**: Hermans & Smit, "Explicit Direct Instruction in Programming Education", PPIG 2018 (https://www.ppig.org/papers/2018-ppig-29th-hermans/ - not fetched): a position paper arguing direct instruction evidence from maths/science may transfer to programming; not an empirical result.

---

## 3. Bootcamp-specific evidence

### 3.1 Barriers faced by bootcamp students

- **Source [READ]** (full PDF text): Kyle Thayer & Amy J. Ko, "Barriers Faced by Coding Bootcamp Students", ICER 2017, pp. 245-253. https://faculty.washington.edu/ajko/papers/Thayer2017CodingBootcamps.pdf
  - Method: "we interviewed twenty-six coding bootcamp students and analyzed the interviews using the Communities of Practice framework"; participants "represented eight bootcamps".
  - Verbatim: students "faced great personal costs and risks, often including significant time, money and effort spent before, during, and after their bootcamps. Though the coursework of bootcamps only ranged from three to six months, career change could take students a year or more".
  - Cohort split by prior experience: "seven people mentioned a divide based on 'background' and previous 'experience' with programming"; one participant: "It was divided, the class. Those with experience, I think, they were looking down at [those of us without experience]".
  - Access to teachers was uneven: "I felt uncomfortable asking questions [of the teachers]"; extra help "reserved for people who were on the upper-end of class."
  - Intensity: "Ten, twelve hours at least per day, and sometimes fourteen or sixteen hours [...] and no weekends because we had assignments." "P9 said financial difficulties caused some people to drop out".
  - Impostor syndrome and confidence loss recur; some bootcamps "had tests that had to be passed in order to advance."

### 3.2 What predicts completion / employment

- **Source [READ]** (abstract and front matter): Huang, Palmer, Udoh, Chun, Jabbari, "Pinpointing Persistence in Alternative STEM Pipelines: Evidence from a Novel Coding and Apprenticeship Program", EdWorkingPaper 25-1122, Annenberg Institute, January 2025. https://edworkingpapers.com/sites/default/files/ai25-1122.pdf
  - Verbatim: "test scores and prior coding experience were significantly associated with persistence across both the coursework and the apprenticeship phases of the LC101 program, while educational attainment was not significantly associated with persistence"; "having mentorship after applying to LaunchCode increased the likelihood of course completion"; "interest alignment is highest among course completers while higher pay, better benefits, and increased stability are highest among non-completers"; "time constraints and course difficulty were the two largest barriers for course completion."
- **[SNIPPET]**: University of Pennsylvania dissertation "Technical Job Placement Success of Coding Bootcamps" (2019; https://repository.upenn.edu/handle/20.500.14332/37880): prior technical experience the strongest predictor of landing a technical job. Not read.

### 3.3 Outcomes reporting

- **Source [READ]**: Liz Eggleston (Course Report), "2020 Coding Bootcamp Alumni Outcomes & Demographics Report" (updated May 2021). https://www.coursereport.com/reports/2020-coding-bootcamp-alumni-outcomes-demographics-report-during-covid-19
  - 3,043 graduate responses from 101 bootcamps; self-reported, voluntary, incentivised, distributed via schools (selection bias). 79 % of respondents employed in a job using bootcamp skills (57 % for 2020 graduates); average salary $44,350 to $69,079; average tuition $14,214. 16+ week programs averaged $72,693 post-bootcamp salary vs $60,189 for 8-week programs (correlation only). Some text/table inconsistencies inside the report were flagged by the fetch.
- **CIRR**: https://cirr.org/standards returned 404 **[FAILED]**; https://cirr.org/standards/standard-advertising-and-disclosing returned 404 **[FAILED]**. **[SNIPPET]** only: CIRR reports graduation and in-field employment at fixed windows (180 days; some reports 90/180/360), with "employed in field" tiers and documentation requirements. Verify on cirr.org before citing.

### 3.4 Typical daily structure

- **Source [READ]**: Nat Davis / Liz Eggleston (Course Report), "What is a Coding Bootcamp Like?", updated 25 Jan 2024. https://www.coursereport.com/blog/what-is-a-coding-bootcamp-like (industry blog, not research)
  - Sample full-time day: 9-10 warm-up challenge/quiz; 10-13 lecture/code-along; 14-16 pair programming; 16-18 individual or group project work; evening fireside chat and optional homework. Teaching style "a blend of lecture, pair programming, group work, and solo projects". "40-60 hours a week".
  - Derived by me from that table: of 8 in-class hours, about 1 h retrieval/warm-up, 3 h instruction, 2 h pairing, 2 h project (roughly 12 % / 38 % / 25 % / 25 %).
- **[SNIPPET]**: Codesmith, Hack Reactor, App Academy, Northcoders schedules (morning lecture, afternoon pairing, capstone at the end). Codesmith page returned 404 **[FAILED]**.
- No peer-reviewed source was found that tests one lecture/lab ratio against another for bootcamps. This is a real evidence gap.

### 3.5 Capstone, portfolio, employer involvement

- **Source [READ-ABSTRACT]**: Tenhunen, Männistö, Luukkainen, Ihantola, "A systematic literature review of capstone courses in software engineering", arXiv 2301.03554, 2023. https://arxiv.org/abs/2301.03554
  - 127 primary studies (2007-2022). Typical capstone: one semester; teams of about four to five; a slight majority use clients external to course staff; main deliverable often a proof-of-concept product; varied assessments throughout the project rather than one end evaluation.
- **[SNIPPET]**: Burke, Bailey, Lyon, Green, "Understanding the Software Development Industry's Perspective on Coding Boot Camps versus Traditional 4-year Colleges", SIGCSE 2018 (interviews with employers at 12 companies). Amy Ko's summary post on Medium returned 403 **[FAILED]**; findings not verified.
- Beirat (read, section 1.5): providers must record "ausbildungs- und/oder arbeitsmarktlicher Eingliederungsergebnisse" and feed evaluation back into the concept.

---

## 4. Teaching in the age of AI coding assistants (2023-2026)

### 4.1 Skill formation with AI assistance

- **Source [READ]**: Judy Hanwen Shen & Alex Tamkin (Anthropic), "How AI assistance impacts the formation of coding skills", 29 Jan 2026. https://www.anthropic.com/research/AI-assistance-coding-skills ; paper "How AI Impacts Skill Formation", arXiv:2601.20245 **[READ-ABSTRACT]** https://arxiv.org/abs/2601.20245
  - RCT, 52 mostly junior software engineers learning the Trio async library; 35-minute task then quiz.
  - AI group averaged 50 % on the quiz vs 67 % hand-coding (Cohen's d = 0.738, p = 0.01); AI group about two minutes faster, not significant; largest gap on debugging questions.
  - Interaction patterns (associational, tiny n): low-scoring "AI delegation" (~39 %), "Progressive AI reliance" (~35 %), "Iterative AI debugging" (~24 %); high-scoring "Generation-then-comprehension" (~86 %), "Hybrid code-explanation" (~68 %), "Conceptual inquiry" (~65 %).
  - Abstract: "AI use impairs conceptual understanding, code reading, and debugging abilities"; "AI-enhanced productivity is not a shortcut to competence."
  - Limits: small sample, immediate quiz, chat-style assistant, not agentic tools.
- **Source [READ-ABSTRACT]** (RePEc record): Bastani, Bastani, Sungu, Ge, Kabakcı, Mariman, "Generative AI without guardrails can harm learning: Evidence from high school mathematics", PNAS 122(26), 2025. https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html
  - With GPT-4 during practice: "48% improvement in grades for GPT Base and 127% for GPT Tutor"; when access was removed, "17% reduction in grades for GPT Base" relative to never having access; the tutor version with safeguards largely avoided the harm. Population: high-school maths, not adult programmers.
- **Source [READ-ABSTRACT]**: Kazemitabaar et al., "Studying the effect of AI Code Generators on Supporting Novice Learners in Introductory Programming", CHI 2023, arXiv:2302.07427. https://arxiv.org/abs/2302.07427
  - 69 novices aged 10-17; Codex access raised code-authoring completion (1.15x) and scores (1.8x); no reduction on manual code-modification tasks; retention post-test slightly higher but not significant. A counterweight: harm is not automatic.
- **Source [READ-ABSTRACT]**: Prather et al., "The Widening Gap: The Benefits and Harms of Generative AI for Novice Programmers", ICER 2024, arXiv:2405.17739. https://arxiv.org/abs/2405.17739
  - 21 lab sessions with observation, interview, eye tracking. "an unfortunate divide in the use of GenAI tools between students who accelerated and students who struggled"; GenAI "can compound them and even introduce new metacognitive difficulties"; struggling students "finished with an illusion of competence."

### 4.2 Critical thinking and cognitive offloading

- **Source [READ]** (Microsoft Research publication page): Lee, Sarkar, Tankelevitch, Drosos, Rintel, Banks, Wilson, "The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers", CHI 2025. https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/
  - Survey of 319 knowledge workers, 936 examples. "higher confidence in GenAI is associated with less critical thinking, while higher self-confidence is associated with more critical thinking." "GenAI shifts the nature of critical thinking toward information verification", response integration and task stewardship. Self-report, correlational.
- **Source [READ-ABSTRACT]**: Kosmyna et al., "Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task", arXiv:2506.08872 (v1 June 2025, v2 Dec 2025). https://arxiv.org/abs/2506.08872
  - 54 participants (18 in session 4); LLM group showed weakest EEG connectivity and lowest self-reported ownership. Preprint, small n, essay writing not coding.
- **[SNIPPET]**: Gerlich, "AI Tools in Society: Impacts on Cognitive Offloading and the Future of Critical Thinking", Societies 15(1):6, 2025 (MDPI page returned 403 **[FAILED]**): 666 participants, negative correlation between frequent AI tool use and critical thinking, mediated by cognitive offloading; correlational.

### 4.3 Productivity evidence (context for what the job now looks like)

- **Source [READ]**: METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", 10 July 2025. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
  - RCT, 16 experienced developers, 246 issues; with AI allowed, 19 % longer; developers forecast 24 % speedup and afterwards believed 20 % speedup.
- **Source [READ]**: METR, "We are Changing our Developer Productivity Experiment Design", 24 Feb 2026. https://metr.org/blog/2026-02-24-uplift-update/
  - Late-2025 data: original developers estimated speedup -18 % (CI -38 % to +9 %), 47 new developers -4 % (CI -15 % to +9 %) (as reported by the fetch tool; secondary coverage disagrees on sign conventions, so re-read the post before quoting numbers). METR considers its own estimate a likely lower bound because developers increasingly refused to work without AI and withheld tasks; self-reported speedups are unreliable.
  - Takeaway for curriculum: perceived and measured benefit diverge, so teach measurement/verification habits; and working with agents is now the default mode of practice.

### 4.4 Guidance from CS educators

- **Source [READ]**: ACM/IEEE-CS/AAAI CS2023, section 4.3 "Generative AI and the Curriculum", 2024. https://csed.acm.org/wp-content/uploads/2024/04/4.3-Generative-AI-and-the-Curriculum.pdf
  - Verbatim: "The skill set expected of students is changing, but the foundational knowledge they need to know is not."
  - Verbatim: "Tasks that are intellectually challenging, yet mechanical in nature will be automated. So, students must learn to work at higher levels of abstraction."
  - Verbatim (SDF): "While generative AI can write simple programs, the responsibility to verify the correctness of the programs still falls on the user. So, even for verification purposes only, computer science students still need to learn how to write programs." and "the idea of learning to program by writing, and reliance on learning syntax, will change towards learning to program by prompting, comprehending, verifying, editing, modifying, adapting, and testing code. It is also likely that other aspects of the curriculum such as problem decomposition will see increased focus."
  - Verbatim (SE): "Effective use of such tools requires a deeper investment in design and code comprehension, while potentially decreasing the need for hands-on programming time."
  - Verbatim: ethics topics "must not only be actively addressed in the curriculum, but also periodically revisited and revised."
- **Source [READ]**: Gordon, Denny, Keuning, Kiesler, Kumar, Kumar, Leinonen, Prather, "ACM Task Force on Generative AI and Programming Assessment: Final Report", dated 16 Feb 2026 (filename). https://acm-education-genai-task-force.github.io/ACM_Taskforce_GenAI_Report_16Feb26.pdf
  - Global survey, 763 responses (about 500 usable), collected May-October 2025.
  - Concerns: "Increased dependency on technology to complete coursework" 87 %; cheating/plagiarism 72 %.
  - 64 % (295 of 469) had changed teaching; 68 % (of 459) had changed assessment.
  - Reported assessment changes (response counts): increased in-person/proctored exams (56), reduced weight on take-home assignments (38), oral assessment/defence (36) "Requiring students to explain their code, assess using oral exams, interviews, and presentations", paper-based assessment (35), project-based assessment (34).
  - Reported teaching changes: explicit teaching of AI use/prompting (39), assignment redesign (31), more in-class activity (17), emphasis on debugging/testing (17), problem-solving/design over syntax (16), code comprehension (15), critical evaluation of AI output (11), requiring documentation/disclosure of AI use (9).
  - Summary verbatim: "Assessment is shifting away from the grading of individual homework toward larger projects, more complex assignments that GenAI does not yet handle well, oral assessments, and proctored exams." and "Many instructors are shifting their teaching strategies from code writing to code comprehension and from syntax to problem solving."
  - Observed: "Less-skilled students tend to use AI more but benefit less, which amplifies the 'skills gap'".
  - Barrier: "Lack of examples of best practices" (48 %).
- **Source [READ-ABSTRACT]**: Denny et al., "Prompt Problems: A New Programming Exercise for the Generative AI Era", SIGCSE 2024, arXiv:2311.05943. https://arxiv.org/abs/2311.05943
  - Students write a natural-language prompt whose generated code must pass tests; tool "Promptly"; "We find that students are enthusiastic about Prompt Problems."
- **Source [READ]**: Becker, Craig, Denny, Keuning, Kiesler, Leinonen, Luxton-Reilly, Malmi, Prather, Quille, "Generative AI in Introductory Programming" (CS2023 companion article), Nov 2023. https://csed.acm.org/large-language-models-in-introductory-programming/ - students "could become over-reliant on them"; revisit what is taught, when and how.

### 4.5 Assessment when AI is allowed

- **Source [READ-ABSTRACT]**: Kannam, Yang, Dharm, Lin, "Code Interviews: Design and Evaluation of a More Authentic Assessment for Introductory Programming Assignments", SIGCSE 2025, arXiv:2410.01010. https://arxiv.org/abs/2410.01010
  - Live oral interviews attached to take-home assignments; pushed students to discuss their work; enabled peer learning; mixed effect on stress; limited TAs' room for feedback; design choices affect integrity and workload.
- **Source [READ-ABSTRACT]**: Lorena A. Barba & Laura Stegner, "The Conversational Exam: A Scalable Assessment Design for the AI Era", arXiv:2601.10691, Jan 2026 (journal ref: Computer 59(6), June 2026). https://arxiv.org/abs/2601.10691
  - "a scalable oral examination format" with students coding live while explaining reasoning; 58 students in small groups over two days; "oral exams can scale to typical class sizes"; documentation and supervised AI access allowed.
- **Source [READ]**: Stanford CS336 "Language Modeling from Scratch", Spring 2025 site. http://cs336.stanford.edu/spring2025/ - AI policy: LLMs allowed for low-level programming help or high-level conceptual questions, but "using it directly to solve the problem is prohibited"; staff encourage disabling AI autocomplete. Example of an "AI-off for fundamentals" course design.

---

## 5. Keeping a curriculum current

### 5.1 Skill half-life: what the sources actually say

- **Source [READ]** (PDF text): Annette LaPrade et al., IBM Institute for Business Value, "The enterprise guide to closing the skills gap", 2019. https://www.ibm.com/downloads/cas/EPYMNBJA
  - Verbatim: "The half-life of professional skills was once estimated at 10 to 15 years ... Today, the half-life of a learned skill is estimated to be five years and even shorter for technical skills, meaning a skill learned today will be about half as valuable in just five years or less." Footnote 24 cites: "Kasriel, Stephane. 'Skill, re-skill and re-skill again: How to keep up with the future of work.' World Economic Forum. July 31, 2017."
  - So IBM's figure is not IBM data; it is a citation of an opinion piece. IBM's own data point in the same report: median time to close a capability gap through training rose from "three days" (2014) to "36 days" (2018).
- **Source [FAILED]**: the Kasriel WEF article (https://www.weforum.org/stories/2017/07/skill-reskill-prepare-for-future-of-work/) returned Access Denied; web.archive.org is not reachable from this tool. Its content is known only via the IBM footnote and secondary summaries.
- **Source [READ]** (secondary, vendor blog): Rework, "Skills Half-Life and Continuous Reskilling". https://resources.rework.com/libraries/ai-future-of-work/skills-half-life-and-continuous-reskilling - traces the "5-year" claim to the 2011 book "A New Culture of Learning" (Thomas & Seely Brown) and the 2017 Kasriel piece, and states neither publishes a methodology.
- **The "2.5 years" claim: NOT VERIFIED.** No primary source containing "2.5 years" was found. It appears only in secondary blogs that attribute it loosely to IBM, HBR or "research". The only primary IBM wording found is "five years and even shorter for technical skills". Recommendation: do not print "2.5 years" in any official document; if a number is needed, use the WEF 2025 figure below, which has a stated survey basis.
- **Source [READ]** (PDF downloaded and text extracted): World Economic Forum, "Future of Jobs Report 2025", January 2025. https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
  - Verbatim: "On average, workers can expect that two-fifths (39%) of their existing skill sets will be transformed or become outdated over the 2025-2030 period. However, this measure of 'skill instability' has slowed compared to previous editions of the report, from 44% in 2023 and a high point of 57% in 2020".
  - Verbatim: "for a representative sample of 100 workers 41 will not require significant training by 2030; 11 will require training, but it will not be accessible to them in the foreseeable future; and 29 will require training and be upskilled within their current roles. Additionally, employers anticipate that 19 out of 100 workers will require training and will be reskilled and redeployed".
  - Skill gaps are the top barrier to transformation, "cited by 63% of surveyed employers". Basis: employer survey expectations, not measured decay.
- **[SNIPPET]**: Deming & Noray, "Earnings Dynamics, Changing Job Skills, and STEM Careers", QJE 135(4), 2020 - job-posting data 2007-2019; technology-intensive careers have faster task turnover and flatter returns to experience. The best academic evidence of faster skill obsolescence in tech, but not read here.

### 5.2 Durable core vs. volatile tools

- CS2023 (read): "The skill set expected of students is changing, but the foundational knowledge they need to know is not." CS Core "kept to a minimum" plus KA Core for depth; programs "select the knowledge areas on which to focus".
- Stanford CS336 (read): builds every component "from scratch", modelled on OS courses - durable-concept strategy.
- "T-shaped" curricula: no primary source was fetched for this term; treat as common vocabulary, not evidence.

### 5.3 How other programmes handle updates

- **The Carpentries lesson life cycle [READ]**: https://docs.carpentries.org/resources/curriculum/lesson-life-cycle.html
  - Stages pre-alpha, alpha, beta, stable, retired. Stable: changes still happen "but are usually small" and do not heavily affect instructors who know an earlier stable version. Stable versions are released to Zenodo with a DOI; developers "may release regularly, such as annually". Retired lessons get an unmaintained notice and an archived repo. Pilots are the key step before stability.
- **The Carpentries Curriculum Advisory Committees [READ]**: https://docs.carpentries.org/handbooks/curriculum_advisors.html (and https://carpentries.github.io/maintainer-onboarding/04-communicate-advisors.html)
  - "Each Curriculum Advisory Committee will meet at least quarterly, and preferably every two months." Advisors "provide high-level oversight, vision, and leadership for a curriculum and guide large-scale updates."
  - Consultation rubric (as listed by the fetch):
    - Maintainers have full authority: adding/removing exercises, reorganising material within episodes, changing episode timings, changing lesson text.
    - Should consult CAC: new versions of a dataset, changing episode order.
    - May benefit from consulting: adding a new library or package, introducing a new topic or learning objective, backward-compatible software updates.
    - Must seek CAC approval: replacing the dataset, "Updating to a non-backward-compatible version of existing software", changing the plotting library or SQL dialect taught, removing an entire episode, retiring a lesson, adding or removing prerequisites, promoting a lesson between life-cycle stages.
- **DataTalksClub LLM Zoomcamp [READ]**: https://github.com/DataTalksClub/llm-zoomcamp and https://github.com/DataTalksClub/llm-zoomcamp/tree/main/cohorts
  - Current curriculum lives at the repository root; `cohorts/2024` and `cohorts/2025` are frozen archives (standalone copies marked legacy); `cohorts/2026` holds only cohort-specific material (cohort.yaml with dates and homework list, schedule README, workshops, per-module homework). Certificate requires the final project plus peer review: "Evaluate and provide written feedback on three fellow students' submissions."
- **Stanford CS224N [READ]**: https://web.stanford.edu/class/cs224n/ (Winter 2026 offering)
  - Each offering is archived at its own URL (Winter 2025, Spring 2024, Winter 2024 linked). Changes between years are explicit: "The Spring 2024 Default Final Project was based on BERT and has now been replaced with GPT-2." New topics (reasoning, agents/tool use/RAG, post-training) sit on top of a stable spine (word vectors, backprop, transformers). Final project 49 % of grade with default and custom tracks; "please do not do assignments from previous years!"
- **fast.ai [READ]**: https://course.fast.ai/ - versioned by year ("Practical Deep Learning for Coders 2022 part 1"), anchored to a book; top-down pedagogy: "I start by showing how to use a complete, working, very usable, state-of-the-art deep learning network" then dig deeper; "We always teach through examples." The page states no update policy (and the 2022 date shows a programme can go stale when no cadence is committed).
- **Full Stack Deep Learning [READ]**: https://fullstackdeeplearning.com/ - editions kept side by side by year (2018 bootcamp, 2019, 2020, 2021, FSDL 2022, LLM Bootcamp Spring 2023), older ones grouped as "Older". No stated update policy; last edition listed is 2023.
- Teaching Tech Together (read): maintainability definition and the four factors (documented design, etc.); short units are cheaper to replace.
- UbD (read): tenets 6-7 call for regular review of units against design standards and adjustment from student performance.

### 5.4 AZAV: changing an approved Maßnahme

- **Source [READ]**: Beirat nach § 182 SGB III, Empfehlungen, Stand 17.06.2026, section "Änderungen bei Maßnahmen der beruflichen Weiterbildung – nach §§ 81, 82 SGB III ..." (V02, valid since 01.10.2020; identical wording in the 10.09.2024 version). URLs as in 1.5.
  - Verbatim: "Der Träger ist verpflichtet, unverzüglich Änderungen der fachkundigen Stelle mitzuteilen, die die Zulassung erteilt hat, sofern diese Änderungen Auswirkungen auf die Zulassung haben können (§181 Abs. 5 i.V.m. § 177 Abs. 4 SGB III). Diese Mitteilungspflicht umfasst wesentliche Änderungen. Wesentlich ist eine Änderung dann, wenn sie wesentlicher inhaltlicher, wesentlicher konzeptioneller oder wesentlicher organisatorischer Art ist oder finanzielle Auswirkungen hat."
  - The Empfehlungen give no list of examples and no numeric threshold for "wesentlich".
  - Calculation changes after approval must also be documented ("dies gilt auch für Änderungen nach der Zulassung").
- **Source [READ]**: DQS AZAV Expertenteam, "Änderungen bei zugelassenen Maßnahmen sind mitteilungspflichtig", 24 Oct 2022. https://www.dqsglobal.com/de/entdecken/blog/aenderungen-bei-zugelassenen-massnahmen-sind-mitteilungspflichtig - repeats the Beirat wording; gives no examples, procedure or exclusions.
- **[SNIPPET]** (TÜV Rheinland AZAV FAQ PDF; the URL from search returned 404 **[FAILED]**): notifiable changes named in the snippet include renaming of the provider, "wesentliche Konzeptänderungen", changed duration, changed title; approval is valid three years and must be re-applied for afterwards. Verify with your own fachkundige Stelle.
- AZAV § 3 Abs. 1 Nr. 2 (read) requires the measure to take "aktuelle Entwicklungen des Ausbildungs- und Arbeitsmarktes" into account, i.e. updating is expected, not merely tolerated.
- Open point that no source settles: whether replacing one tool/framework by another inside an unchanged learning objective is "wesentlich". Sources leave this to the fachkundige Stelle.

---

## 6. Assessment and certification

- **Rubrics**: Biggs (read): judge "the whole performance against predetermined and public rubrics"; analytic scoring is for formative use. **[SNIPPET]** Jonsson & Svingby, Educational Research Review 2(2), 2007: review of 75 studies; scoring reliability improves with analytic, task-specific criteria, exemplars and rater training (secondary summary; not verified).
- **Peer assessment validity**: **[READ-ABSTRACT]** Li, Xiong, Zang, Kornhaber, Lyu, Chung, Suen, "Peer assessment in the digital age: a meta-analysis comparing peer and teacher ratings", Assessment & Evaluation in Higher Education 41(2), 2016. https://pure.psu.edu/en/publications/peer-assessment-in-the-digital-age-a-meta-analysis-comparing-peer/
  - Average peer-teacher correlation .63 ("moderately strong"); higher when: graduate-level course; individual rather than group work; random matching; voluntary; non-anonymous; peers give both scores and comments; peers help develop the criteria; paper-based.
  - **[SNIPPET]** Falchikov & Goldfinch 2000: mean correlation .69 across 48 studies.
  - Teaching Tech Together (read): calibrated peer review - learners first grade examples against the teacher's grading before grading peers.
- **Capstone defence / oral**: ACM task force 2026 (read), Barba & Stegner 2026, Kannam et al. 2025 (abstracts) - see 4.4-4.5.
- **Capstone structure**: Tenhunen et al. (abstract) - teams of 4-5, external clients in a slight majority, continuous varied assessment.
- **Micro-credentials**: **[READ]** Council of the EU, "Council Recommendation of 16 June 2022 on a European approach to micro-credentials for lifelong learning and employability" (2022/C 243/02). https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022H0627(02)
  - Definition: "the record of the learning outcomes that a learner has acquired following a small volume of learning", assessed against transparent criteria.
  - Mandatory description elements: learner identity; title; country/region of issuer; awarding body; date of issue; learning outcomes; notional workload (ECTS where possible); level (EQF/QF-EHEA) if applicable; type of assessment; form of participation; type of quality assurance.
  - Principles include quality, transparency, relevance ("updated" to meet identified needs), valid assessment, learning pathways (stackability), recognition, portability, learner-centred, authenticity, information and guidance.
- **AZAV**: Teilnahmebescheinigung "mit Angaben zum Inhalt, zeitlichen Umfang und Ziel der Maßnahme" (AZAV § 2 Abs. 5, read); Zeugnis "das Auskunft über den Inhalt des vermittelten Lehrstoffs gibt" (Kiwa sheet, read).

---

## 7. Synthesis: a step-by-step planning method

Everything in this section is **RECOMMENDATION** unless a sentence says "source:". Each step lists the sources it rests on.

### Step 1. Start from target job tasks (Handlungsfelder), not topics
- Do: collect 8-12 recurring work tasks of the target role from current job ads, 5-10 practitioner/employer interviews and your own practice (e.g. "ship an LLM feature behind an eval gate", "delegate a scoped change to a coding agent and review the result"). Record the date and evidence for each.
- Why: source: KMK - Lernfelder are developed from Handlungsfelder oriented on "gegenwärtigen und zukünftigen Berufspraxis"; AZAV § 3 requires design for target group and labour-market developments; Beirat requires "Aktuelle und systematische Analyse der kundenrelevanten Bedarfe"; UbD Stage 1 asks for the "ultimate transfer".
- Also write 3-4 learner personas (background, prior knowledge, what they want to do, constraints). Source: Teaching Tech Together; Carpentries lesson development. Thayer & Ko and the LaunchCode study show prior experience splits cohorts and predicts persistence, so define the entry level and test it at admission.

### Step 2. Turn tasks into 6-10 programme competences and measurable outcomes
- Do: one programme-level competence per action field, phrased as a complete action (plan, build, check, evaluate). Under each, 3-6 outcomes written verb + noun, one verb each, mostly Apply/Analyze/Evaluate/Create. Tag each outcome **durable** (concept or practice, e.g. "evaluate an agent's output against a written spec") or **volatile** (bound to a named tool/version).
- Why: source: Krathwohl (verb + noun; six processes); Biggs ("one verb (or at most two) for each outcome"); KMK (name by Kernkompetenz, describe along phases of the vollständige Handlung); DQR/EQF descriptors as wording model for level 5-6; CS2023 ("foundational knowledge ... is not" changing; CS Core "kept to a minimum").
- Write outcomes tool-agnostic. Tools go in a separate, versioned "current toolchain" annex. This is my design choice for surviving a year; it follows from CS2023's core/depth split and the Beirat definition of "wesentliche" change, but no source prescribes it.

### Step 3. Design the assessments before the modules
- Do, in this order:
  1. Capstone brief and rubric (the summative performance task).
  2. One performance task per module (a mini-project with a rubric that reuses capstone criteria).
  3. Formative checks for each outcome (quizzes, prediction questions, code-reading and debugging tasks, short oral explanations).
- Why: source: UbD Stage 2 ("think like assessors"); Teaching Tech Together (summative first, then formative per skill); Carpentries lesson design phases 1-3; Biggs (ATs contain the ILO verb; public holistic rubrics); AZAV/Beirat (concept must show Lernerfolgskontrolle and how achievement of Lernziele is recorded).
- AI-era assessment mix (RECOMMENDATION, resting on ACM task force 2026, Barba & Stegner, Kannam et al., Anthropic 2026, Prather et al. 2024):
  - Every module task has two parts: the artefact (AI use allowed and documented) and a 10-15 minute live walkthrough/defence where the learner explains, modifies and debugs their own work.
  - Two or three "AI-off" checkpoints on fundamentals that the Anthropic study found most damaged by delegation (code reading, debugging, conceptual understanding).
  - Process evidence: commit history, prompt/agent logs, a short decision log. Source for disclosure practice: ACM task force ("Requiring documentation").
  - Capstone ends with a demo plus oral defence in front of instructors and, where possible, an external practitioner.
- Rubrics: analytic rubric for weekly feedback, holistic judgement for the final grade (source: Biggs). Train reviewers and use exemplars ([SNIPPET] Jonsson & Svingby).
- Peer review: use it for feedback and as a learning activity, weight it lightly in grades. Calibrate first, require scores plus comments, involve learners in the criteria (source: Li et al. 2016 moderators; Teaching Tech Together; Zoomcamp practice of three peer reviews).

### Step 4. Build modules (Lernfelder) and sequence them
- Do: 640 UE = 16 weeks x 40 UE. Suggested shape: weeks 1-12 as six 2-week modules of 80 UE (or a mix of 40/80), weeks 13-16 capstone (160 UE). Inside every module, plan content for about 80 % of the hours and keep 20 % as buffer for review, re-teaching and newly released tools.
- Why: source: KMK (time values divisible by 20, usually 40/60/80; plan only 80 %; spiral competence development); Tenhunen et al. (capstones are team projects of 4-5, continuous assessment); Course Report 2020 (longer programmes correlate with better salary outcomes - weak evidence).
- Each module is a Lernsituation: one realistic problem carried through plan, build, check, evaluate (source: KMK vollständige Handlung; Brown & Wilson authentic tasks).
- Spiral: evaluation, debugging/observability, code review and security come back in every module with rising difficulty (source: KMK spiralcurricular; Dunlosky distributed practice).
- Core / rolling split (RECOMMENDATION): about 70 % of module hours cover durable outcomes; about 20 % are "current toolchain" labs that are expected to change per cohort; about 10 % is a rolling slot ("what changed this month", guest practitioner, tool comparison). Rationale: CS2023 core vs KA core; Carpentries distinction between routine and structural changes; WEF 39 % skill change over five years implies visible change within one year. The percentages are my judgement; no source gives them.

### Step 5. Weekly rhythm
See section 8.

### Step 6. Pilot, measure, revise
- Do: pilot each module with a small group before cohort 1 (or treat cohort 1 as beta and say so internally). Collect formative results, attendance, drop-outs, time-on-task, learner feedback; run a retrospective per module; record changes in a changelog.
- Why: source: Carpentries life cycle (alpha/beta pilots before stable); Teaching Tech Together rule "no lesson survives first contact with learners"; UbD tenet 7; Beirat (record presence, drop-out, goal attainment, placement; feed evaluation into concept).
- Retention design (RECOMMENDATION from Thayer & Ko and LaunchCode): admission check on programming level; a named mentor per learner; scheduled, equal access to instructors (office-hour rota, not only on demand); realistic workload inside the 40 UE with no assumed evening work; early-warning review at weeks 2 and 4.

### Step 7. Refresh process
See section 9.

---

## 8. Recommended split of a 40-UE week

**What sources say**
- Active learning beats lecturing in STEM (Freeman et al.: +0.47 SD; failure odds ratio 1.95 for lecturing).
- For new material, explicit guidance with practice and feedback beats discovery; projects are for "practicing recently learned content and skills"; for learners with expertise the worked-example advantage reverses (Clark, Kirschner, Sweller 2012).
- Check understanding every 10-15 minutes; keep episodes short (Teaching Tech Together; Carpentries).
- Practice testing and distributed practice have the best evidence among study techniques (Dunlosky et al.).
- Peer instruction and pair programming have positive evidence in CS courses (Porter et al.; Umapathy & Ritzhaupt).
- Industry description of a bootcamp day: about 1 h warm-up quiz, 3 h lecture/code-along, 2 h pairing, 2 h project (Course Report blog).
- AZAV: every counted UE must be led or actively accompanied with synchronous interaction; accompanied project/group work counts if the concept explains interaction and Lernerfolgskontrolle (Beirat 2026).
- Unguided AI use during practice lowers later unaided performance; guarded or comprehension-oriented use does not (Bastani et al.; Anthropic 2026).
- No source tests a specific lecture/lab/project ratio for bootcamps. The numbers below are judgement.

**RECOMMENDATION: baseline week (modules, weeks 1-12)**

| Block | UE/week | Share | What happens | Main sources |
|---|---|---|---|---|
| Retrieval and review | 4 | 10 % | Daily 30-40 min opener: quiz on earlier weeks, prediction questions, peer instruction on misconceptions | Dunlosky; Porter; TTT |
| Direct instruction (live coding, worked examples, concept talks) | 8 | 20 % | Episodes of at most 20-30 min, each ending in a formative check; worked examples only for new concepts | Clark et al.; TTT 10-15 min rule; Carpentries live coding |
| Guided practice (labs) | 12 | 30 % | Faded exercises, code reading, debugging, pair programming with role switches; alternating AI-off and AI-on variants of the same task | Clark et al.; Umapathy & Ritzhaupt; Anthropic 2026; Prompt Problems |
| Project work (accompanied) | 12 | 30 % | Module mini-project in pairs/teams; instructors circulate, stand-ups, scheduled check-ins | KMK vollständige Handlung; Brown & Wilson; Beirat (accompanied project work) |
| Review and assessment | 4 | 10 % | Code review (peer + instructor), demo, oral walkthrough, retrospective, rubric feedback | Biggs; ACM task force; Li et al. |

Daily shape (8 UE): opener/retrieval (about 1 UE), instruction + guided practice interleaved (about 4 UE), project (about 2-3 UE), review/wrap-up (about 0.5-1 UE). This is close to the Course Report sample day but with less lecture (20 % vs about 38 %) and more guided practice, because the learners already program (expertise reversal) and because active learning has the stronger evidence.

**RECOMMENDATION: shift across the programme**

| Phase | Instruction | Guided practice | Project | Retrieval + review/assessment |
|---|---|---|---|---|
| Weeks 1-4 (foundations) | 25 % (10 UE) | 35 % (14 UE) | 20 % (8 UE) | 20 % (8 UE) |
| Weeks 5-12 (build) | 20 % (8 UE) | 30 % (12 UE) | 30 % (12 UE) | 20 % (8 UE) |
| Weeks 13-16 (capstone) | 5 % (2 UE) | 10 % (4 UE) | 65 % (26 UE) | 20 % (8 UE) |

Rationale: guidance fades as expertise grows (Clark et al.); capstones are team projects with continuous assessment (Tenhunen et al.); retrieval and review stay constant (Dunlosky).

AZAV wording note (RECOMMENDATION): in the concept, describe project and lab blocks as "begleitete Projekt-/Gruppenarbeit" with named instructor presence, a check-in rhythm and the Lernerfolgskontrolle used, mirroring the Beirat text. Do not count homework.

---

## 9. Concrete refresh policy

**What sources say**
- A lesson is maintainable "if it's cheaper to update it than to replace it"; document the design (Teaching Tech Together).
- Split authority by size of change; structural changes (learning objectives, prerequisites, non-backward-compatible tool versions, removing a unit) need a governing body; text, exercises and timings do not (Carpentries rubric). Advisory committee meets at least quarterly.
- Label maturity (alpha/beta/stable/retired) and release stable versions on a regular schedule, e.g. annually (Carpentries life cycle).
- Keep the current curriculum in one place and freeze each past cohort as an archive (Zoomcamp; Stanford archived offerings; FSDL editions).
- Change assessment artefacts between offerings (Stanford CS224N).
- Foundational knowledge is stable, skill set changes (CS2023); 39 % of skills expected to change 2025-2030 (WEF).
- AZAV: measure must reflect current labour-market developments; "wesentliche" changes of content, concept, organisation or with financial effect must be reported "unverzüglich" (AZAV § 3; Beirat).

**RECOMMENDATION**

1. **Pin (change only with a formal decision and, if needed, notification to the fachkundige Stelle)**
   - Programme title, target group and entry requirements, total 640 UE, 16 weeks, delivery form, group size, price/calculation.
   - Programme competences and module-level learning outcomes (tool-agnostic wording), module titles and UE per module.
   - Assessment formats and rubric criteria; certificate content.
   - Basis: these are what the Maßnahmekonzept and certificate describe (AZAV § 2 Abs. 5, § 3; Beirat "wesentlich"); Carpentries "must seek approval" class.

2. **Review before every cohort (4-6 weeks before start; instructor team decides; log it)**
   - Toolchain annex: models, agent tools, SDK/library versions, pinned dependency files.
   - Labs, datasets, examples, starter repos: run every lab end to end on the pinned versions.
   - Project briefs and quiz items (rotate; never reuse a previous cohort's capstone brief unchanged).
   - Reading list and the "what changed" rolling slot.
   - Basis: Carpentries "maintainer authority"/"may consult" classes; Stanford practice; Zoomcamp per-cohort folder.

3. **Review twice a year with an advisory board (3-5 external practitioners/employers plus an alumnus)**
   - Job-task list from Step 1, competences, durable/volatile tags, capstone criteria, placement and drop-out data.
   - Basis: Carpentries CAC cadence (I propose half-yearly as a minimum for a small school; Carpentries says at least quarterly); Beirat needs-analysis and evaluation loop; EU micro-credential "relevance" principle.

4. **Triggers for an out-of-cycle change**
   - A taught tool/API is deprecated, breaks compatibility, changes licence/pricing so learners cannot use it, or has a security problem.
   - A lab fails on current versions.
   - At least two advisory-board members or a clear pattern in job ads show a taught practice is obsolete or a missing one is now standard.
   - Formative/summative data: an outcome missed by a large share of a cohort (set your own threshold, e.g. one third), or repeated learner feedback on the same unit.
   - New Beirat Empfehlungen or legal change (they changed in 2024, 2025 and 2026).
   - Basis: Carpentries rubric (non-backward-compatible versions need approval); UbD tenet 7; Beirat continuous improvement.

5. **Change classes and what to do**

   | Class | Examples | Decision | AZAV action (RECOMMENDATION; confirm with your fachkundige Stelle) |
   |---|---|---|---|
   | Patch | Fix text, update screenshots, bump a library minor version, swap an example | Module owner | None; changelog entry |
   | Minor | Replace a tool with an equivalent under the same outcome, reorder units within a module, new project brief | Lead instructor | Document internally with reasoning that outcomes, UE, concept are unchanged; ask the FKS once, in writing, how they classify tool swaps and file the answer |
   | Major | Add/remove/reword a learning outcome, move UE between modules, change assessment format, change entry requirements, change duration, delivery form, price | Programme owner + advisory board | Treat as "wesentlich": notify the FKS before delivery |

   The patch/minor/major classes and the mapping to "wesentlich" are my interpretation. Source basis: Beirat definition (content, concept, organisation, financial); the Empfehlungen give no examples, and the DQS article adds none.

6. **Versioning and records**
   - Curriculum in a git repository; version `YEAR.COHORT.PATCH` (or semantic versioning); CHANGELOG with date, class of change, reason, evidence, decision-maker.
   - Each unit carries a status label (alpha/beta/stable/retired) and "last verified on" date with tool versions.
   - Freeze a tagged snapshot per cohort; keep cohort-specific material (dates, homework, briefs) in a per-cohort folder.
   - Keep a one-page design document per module: outcomes, why this order, which parts are durable or volatile.
   - Basis: Carpentries life cycle and Zenodo releases; Zoomcamp cohorts folder; Teaching Tech Together (documented design is the first maintainability factor); Beirat (changes after approval must be traceable).

7. **Launch-and-plus-one-year check (April 2027 to April 2028)**
   - Write the concept so that the names of specific models, agent products and frameworks appear only in the annex.
   - Budget the 20 % buffer per module (KMK 80 % rule) and the weekly rolling slot so new releases have a home without restructuring.
   - Plan one scheduled minor release per cohort and one major review per year, aligned with the three-year approval period ([SNIPPET], TÜV Rheinland FAQ) and the Beirat's roughly annual updates.

---

## 10. Gaps and things not verified

- No controlled study was found comparing lecture/lab/project ratios in bootcamps; the weekly split is reasoned from adjacent evidence.
- "2.5-year half-life of technical skills": no primary source found. The "5 years" figure in IBM (2019) is a citation of a 2017 WEF opinion piece, which could not be fetched.
- CIRR standards pages returned 404; CIRR details are snippet-level only.
- Not read in full (abstract/landing page only): Freeman 2014, Dunlosky 2013, Umapathy & Ritzhaupt 2017, Li et al. 2016, Bastani 2025, Prather 2024, Kazemitabaar 2023, Kosmyna 2025, Denny 2023, Kannam 2025, Barba & Stegner 2026, Tenhunen 2023, arXiv version of Shen & Tamkin.
- Snippet only: Kirschner/Sweller/Clark 2006, Black & Wiliam 1998, Macnamara 2014, PBL meta-analysis (2019), Falchikov & Goldfinch 2000, Jonsson & Svingby 2007, Indriasari et al. 2020, Salleh et al. 2011, Burke et al. 2018, Gerlich 2025, Deming & Noray 2020, C-BEN framework, Hermans & Smit 2018, Penn dissertation, TÜV Rheinland FAQ.
- Blocked: Sweller et al. 2019 (Springer login redirect), PNAS and PubMed pages, WEF web pages (the report PDF itself was read), Medium (Ko), MDPI, johnbiggs.com.au (parked), depauw.edu Krathwohl copy (404), Codesmith schedule page (404).
- Most learning-science evidence comes from school and university novices; transfer to experienced adult programmers is an inference. The expertise-reversal literature is the main reason to shift time from instruction to practice for this audience.
- Whether a tool swap under unchanged outcomes is a "wesentliche Änderung" is not answered by any source read; it needs a written answer from the chosen fachkundige Stelle.
- The Beirat Empfehlungen were read from copies hosted by Der Paritätische (2026) and CERTQUA (2024), not from arbeitsagentur.de; wording should be identical but check the official copy before quoting in an application.

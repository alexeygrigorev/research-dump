# International comparables: syllabi for Track A (agentic engineering) and Track B (AI engineering)

All pages fetched on **2026-11-12**. Each entry is marked:

- **[READ]** = the page itself was fetched and read (via WebFetch, or direct download where noted).
- **[SNIPPET]** = only search-result snippets or a third-party write-up were seen; treat as unverified.

Caveats on method: WebFetch returns a model-made extraction of the page, so lesson titles are as extracted (quoted where the extractor quoted). Where a page showed only part of a syllabus (Maven "Show full syllabus"), that is stated. Nothing below is estimated; "not published" means the page read did not state it.

Contents: 1. Track A entries; 2. Track A synthesis; 3. Track B entries; 4. Track B synthesis; 5. Not found / not verified.

---

## 1. Track A: agentic / AI-assisted software engineering

### A1. Stanford CS146S "The Modern Software Developer" (Fall 2026 and Fall 2025) [READ]

- Provider: Stanford University, instructor Mihail Eric. 3 units.
- URL fetched: https://themodernsoftware.dev/ (Fall 2026 is the default term; Fall 2025 at https://themodernsoftware.dev/fall2025). The syllabus tab is rendered client-side; the week data below was read from the page's own JavaScript bundle (downloaded directly from themodernsoftware.dev), which contains both years' week arrays and grading arrays. https://themodernsoftware.dev/syllabus returns 404.
- Prerequisites: "CS111/CS161 equivalent programming experience. CS221/229 recommended."
- Length: 10 weeks, Tue/Thu 5:30-6:20 PM (2026). FAQ: "Expect approximately 10-12 hours per week including lectures, assignments, and project work."
- Price: Stanford tuition; not published on the page. Slides are marked gated in 2026.
- Description (2026): "emerging practices and technologies behind AI-native software development, including MCP, agent skills, spec-driven development, loop engineering, and the software factory."
- Languages: "language-agnostic... examples will primarily use Python, JavaScript".

**Fall 2026 weeks (verbatim titles and topics):**

1. Week 1: The Internals of Coding Agents. "What an LLM actually is, and what the agent loop looks like under the hood"; "The core tool set (read, write, edit, bash) and how tasks flow through it"; "How production coding agents structure their system prompts and tool definitions". Sessions: "Course intro + build Claude Code in 200 lines"; "How state-of-the-art coding agents are designed: deep dive into the system prompts that define the agent". Readings: "Building a Coding Agent", "Lessons from Building Claude Code", "Dive into Claude Code".
2. Week 2: Advanced Context Engineering. "Advanced prompting techniques and when each applies"; "RePPIT (Research, Propose, Plan, Implement, Test) and spec-driven development"; "MCP fundamentals: servers, clients, tools, and transport"; "Designing tools for agent ergonomics". Readings: "The Context Tax: When to Compact", "OpenSpec", "Superpowers", "Enterprise MCP (Cloudflare)".
3. Week 3: Agent Skills and CLI. "What skills are and how SKILL.md + scripts encode a workflow"; "Web skills and extending agent capability beyond the repo"; "Working effectively from the CLI". Guest: Lee Robinson. Readings: "pstack", "Matt Pocock's Skills", "browse.sh".
4. Week 4: Customizing Your Agent and Repository. "CLAUDE.md and AGENTS.md: what to put where"; "Hooks for lint gates, test runs, and guardrails"; "Subagent patterns (planner / implementer / reviewer)". Guest: Boris Cherny (Creator of Claude Code @ Anthropic). Readings: "I Still Prefer MCP Over Skills", "AGENTS.md (Factory Docs)", "Steering Claude Code: Skills, Hooks, Rules, Subagents, and More", "Writing a Good CLAUDE.md".
5. Week 5: Agent-Ready Codebases. "What makes a repo agent-ready: structure, docs, tests, and checks"; "Scoring and auditing readiness"; "Common gaps that block agents in real repos". Guest: Eno Reyes (CTO @ Factory).
6. Week 6: Agentic Code Review. "What AI review catches well, and what it misses"; "Review architectures and custom rules"; "Fitting AI review into a team's PR workflow". Guest: Silas Alberti (Cognition). Readings: "Layered Code Review and Risk-Based Human Oversight", "Coordinating Specialist Review Agents at Scale", "Beyond the Diff: Context, Testing, and Model Selection".
7. Week 7: Security. "SAST / SCA, dependency and secret-leak vulnerabilities"; "Prompt injection and agent-specific attack surfaces"; "Agent-assisted triage and remediation". Guest: Isaac Evans (CEO @ Semgrep).
8. Week 8: Background Agents. "Async, cloud-delegated agents"; "Managing fleets of parallel agents"; "Issue-to-PR pipelines and triggers (Slack, Linear, GitHub)". Guest: Rajesh Bhatia (Cloudflare). Readings: "Spotify: From Migration Scripts to Agent Fleets", "Stripe: From Slack Message to Review-Ready PR", "Ramp: Giving Agents the Tools to Prove Their Work", "LangChain: Inside an Open-Source Software Factory".
9. Week 9: Building an AI-Native Team. "MCP portals and centralized, permissioned tool access"; "LLM gateways, model routing, and cost optimization"; "Org-wide adoption patterns". Guests: Elad Gil, Amjad Masad (CEO @ Replit).
10. Week 10: The Software Factory + The Future. "Self-running, self-improving software systems"; "Running and securing agents post-deployment"; "Where AI software engineering goes next". Sessions: "Coding agents in big teams (MCP portals, LLM gateways, org patterns, cost optimization, and model routing)"; "The Software Factory: self-running, self-improving software systems".

Grading array paired with the 2026 weeks in the bundle: Final Project 50%, Weekly Assignments 15%, Open Source Contributions 30%, Class Participation 5%.

**Fall 2025 weeks (verbatim titles and topics):**

1. Week 1: Introduction to Coding LLMs and AI Development (Course logistics; What is an LLM actually; How to prompt effectively). Assignment: LLM Prompting Playground.
2. Week 2: The Anatomy of Coding Agents (Agent architecture and components; Tool use and function calling; MCP). Sessions: "Building a coding agent from scratch"; "Building a custom MCP server". Assignment: First Steps in the AI IDE.
3. Week 3: The AI IDE (Context management and code understanding; PRDs for agents; IDE integrations and extensions). Assignment: Build a Custom MCP Server.
4. Week 4: Coding Agent Patterns (Managing agent autonomy levels; Human-agent collaboration patterns). Assignment: Coding with Claude Code.
5. Week 5: The Modern Terminal (AI-enhanced command line interfaces; Terminal automation and scripting). Assignment: Agentic Development with Warp.
6. Week 6: AI Testing and Security (Secure vibe coding; History of vulnerability detection; AI-generated test suites). Assignment: Writing Secure AI Code.
7. Week 7: Modern Software Support (What AI code systems can we trust; Debugging and diagnostics; Intelligent documentation generation). Session: AI code review. Assignment: Code Review Reps.
8. Week 8: Automated UI and App Building (Design and frontend for everyone; Rapid UI/UX prototyping and iteration). Assignment: Multi-stack Web App Builds.
9. Week 9: Agents Post-Deployment (Monitoring and observability for AI systems; Automated incident response; Triaging and debugging).
10. Week 10: What's Next for AI Software Engineering.

Grading array paired with the 2025 weeks: Final Project 80%, Weekly Assignments 15%, Class Participation 5%.

How it stays current (FAQ, verbatim): "The course content is designed to be highly current, with weekly updates to reflect the rapidly evolving landscape of AI-assisted development. Guest speakers from leading companies ensure students learn about the latest industry practices and emerging tools."

### A2. Anthropic Academy (Skilljar) courses [READ]

- Catalog URL fetched: https://anthropic.skilljar.com/ (22 courses listed in the extraction, possibly truncated). All courses below show "Register | FREE". Duration: not published on the course pages.
- **Claude Code in Action** (https://anthropic.skilljar.com/claude-code-in-action). Tagline: "Run long, hands-off Claude Code sessions you can trust: steer, configure, automate, and verify." Curriculum: (1) Steer the Work: Steering Long Sessions; (2) Configure Claude: A CLAUDE.md That Follows; Verification Skills; Permission Modes; Hooks; (3) Automate Repeat Work: Scheduled tasks and headless; GitHub Actions and Code Review; (4) Verify and Share: Trust It: Verifying Unsupervised Runs; Plugins; (5) Course Quiz.
- **Claude Code 101** (https://anthropic.skilljar.com/claude-code-101). Prereqs: "Basic familiarity with a code editor and the command line"; "A Claude account (Pro, Max, or Enterprise) or an API key". Lessons: What is Claude Code?; How Claude Code works; Installing Claude Code; Your first prompt; Daily workflows: The explore → plan → code → commit workflow; Context management; Code review; Customizing Claude Code: The CLAUDE.md file; Subagents; Skills; MCP; Hooks; Quiz / Course quiz.
- **Introduction to agent skills** (https://anthropic.skilljar.com/introduction-to-agent-skills): What are skills?; Creating your first skill; Configuration and multi-file skills; Skills vs. other Claude Code features; Sharing skills; Troubleshooting skills.
- **Introduction to subagents** (https://anthropic.skilljar.com/introduction-to-subagents): What are subagents?; Creating a subagent; Designing effective subagents; Using subagents effectively.
- **Introduction to Model Context Protocol** (https://anthropic.skilljar.com/introduction-to-model-context-protocol). Prereqs: "Working knowledge of Python programming"; "Basic understanding of JSON and HTTP request-response patterns". Sections: Introduction (Introducing MCP; MCP clients; Hands-on with MCP servers); Project setup (Defining tools with MCP; The server inspector); Connecting with MCP clients (Implementing a client; Defining resources; Accessing resources; Defining prompts; Prompts in the client); Final assessment on MCP; MCP review. Also listed in catalog: "Model Context Protocol: Advanced Topics" (not fetched).
- **Building with the Claude API** (https://anthropic.skilljar.com/claude-with-the-anthropic-api): see Track B entry B12 (it is an AI-engineering course).
- Assessment: quizzes and a final assessment; completion certificates.

### A3. DeepLearning.AI short courses on coding agents [READ]

Catalog fetched: https://www.deeplearning.ai/courses/?types=short_course (order roughly newest first). Relevant titles seen, newest first: "Loop Engineering with LangChain Deep Agents" (LangChain, 1h16m); "AI Coding Workflows: From Cloud to Local" (JetBrains, 1h32m); "AI Code Review" (Qodo, 1h4m); "Spec-Driven Development with Coding Agents" (JetBrains, 1h16m); "Agent Skills with Anthropic" (2h19m); "Building Coding Agents with Tool Execution" (E2B, 1h21m); "Claude Code: A Highly Agentic Coding Assistant" (Anthropic, 2h); "MCP: Build Rich-Context AI Apps with Anthropic" (1h58m); "Build Apps with Windsurf's AI Coding Agents" (1h30m); "Vibe Coding 101 with Replit" (1h34m); "Gemini CLI: Code & Create with an Open-Source Agent" (1h23m). Price on these pages: not listed; "Enroll for Free" / graded quiz and accomplishment require PRO.

- **Claude Code: A Highly Agentic Coding Assistant** (https://www.deeplearning.ai/short-courses/claude-code-a-highly-agentic-coding-assistant/). Elie Schoppik (Anthropic). Intermediate, 2h, 10 video lessons. Prereq: familiarity with Python and Git. Lessons: Introduction; What is Claude Code?; Setup & Codebase Understanding; Adding Features; Testing, Error Debugging and Code Refactoring; Adding Multiple Features Simultaneously; Exploring Github Integration & Hooks; Refactoring a Jupyter Notebook & Creating a Dashboard; Creating Web App based on a Figma Mockup; Conclusion; Quiz. Tools: Playwright and Figma MCP servers. Three projects: a RAG chatbot codebase, an e-commerce notebook to dashboard, a web app from a Figma mockup.
- **Spec-Driven Development with Coding Agents** (https://www.deeplearning.ai/short-courses/spec-driven-development-with-coding-agents/). Paul Everitt (JetBrains). Beginner, 1h16m. Launch date April 15, 2026 is [SNIPPET]. Lessons: Introduction; Why spec-driven development?; Workflow overview; Set up your environment; Setup; Creating the constitution; Feature specification; Feature implementation; Feature validation; Project replanning; The second feature phase; The MVP; Legacy support; Build your own workflow; Agent replaceability; Conclusion; Quiz.
- **Agent Skills with Anthropic** (https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/). Beginner, 2h19m. Lessons: Why Use Skills Part I/II; Skills vs Tools, MCP, and Subagents; Exploring Pre-Built Skills; Creating Custom Skills; Skills with the Claude API; Skills with Claude Code; Skills with the Claude Agent SDK; Quiz.
- **AI Code Review** (https://www.deeplearning.ai/short-courses/ai-code-review/). Qodo. Intermediate, 1h4m. Lessons: Overview of AI Code Review; AI Code Review Best Practices Part 1/2; Why Context Matters; Building a Context Engine; Building Specialized Code Review Agents; Quiz.
- **MCP: Build Rich-Context AI Apps with Anthropic** (https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/). Intermediate, 1h58m. Lessons: Why MCP; MCP Architecture; Chatbot Example; Creating an MCP Server; Creating an MCP Client; Connecting the MCP Chatbot to Reference Servers; Adding Prompt and Resource Features; Configuring Servers for Claude Desktop; Creating and Deploying Remote Servers; Quiz.

### A4. Hugging Face MCP Course [READ]

- URL: https://huggingface.co/learn/mcp-course/unit0/introduction. Free, built with Anthropic. No dates on the page.
- Prereqs: basic understanding of AI and LLM concepts; familiarity with software development and API concepts; experience with at least one programming language (Python or TypeScript).
- Pace: each chapter about one week, roughly 3-4 hours per week.
- Units: 0 Onboarding; 1 "MCP Fundamentals, Architecture and Core Concepts"; 2 "End-to-end Use case: MCP in Action"; 3 "Deployed Use case: MCP in Action"; 4 "Bonus Units" (partner libraries). Partners: Gradio, Continue, Llama.cpp.
- Assessment: fundamentals certificate for Unit 1; certificate of completion for use-case units 2 and 3; audit allowed.

### A5. Maven: "Elite AI Assisted Coding" (Eleanor Berger; self-paced listing) [READ]

- URL: https://maven.com/agentic-ventures/ai-coding. Self-paced version credited to Eleanor Berger; $650 USD; "Plan for about 3-5 hours weekly"; 29 syllabus items; "You do not need AI or ML training."
- Cohort version with Isaac Flath (13 live sessions, next start Jan 12): [SNIPPET]; cohort page https://maven.com/kentro/context-engineering-for-coding returned 404.
- Unit 2: Foundations: Context Engineering & Frictionless Setup: Orientation & The AI-Assisted Development Model; Frictionless Setup; The Portable Context Stack; Setting Up and Testing Rules; Agent Skills; Agent Skills in Practice; The Spectrum of AI Coding Modalities; Modalities & Specificity in Action; Specificity & Specification; Homework 1.
- Unit 3: Agentic Software Engineering: Specification-Driven Development; Exercising Control in Agentic Coding; Spec to Merge-Ready Plan; Sub-Agents & Multi-Agent Orchestration; The Agent's Toolbox; AI-Assisted Code Review & DevOps; Harness Engineering for AI Coding Agents; Homework 2.
- Unit 4: Agents at Scale: AI Engineering in the Large: Background Async Agents & Autonomous Execution; Async Background Agents; Continuous AI & Agentic Workflows; Setting Up Continuous AI & Agentic Workflows; Parallelisation & Scaling; Agentic AI Security; Measurement, Continuous Improvement & Enterprise Adoption; Homework 3.
- Tools named: GitHub Copilot, Claude Code, Codex, OpenCode, Cursor (vendor-agnostic). Sample code in Python and TypeScript.
- Assessment: three tiered homework assignments.
- Currency (verbatim): "The curriculum is revised quarterly, materials are refreshed for each cohort".

### A6. Maven: "Build a Software Factory: Hands-off agentic coding for experienced engineers" [READ, partial syllabus]

- URL: https://maven.com/s/course/0f53ff1ae1. Instructors: Matt Wynne, Aldric Giacomoni, David Laing, Jeremy Lightsmith.
- Live cohort Jan 12 to Feb 5, 2027; four weeks; live sessions 3 hrs/week (90 minutes twice a week), self-directed practice 2-6 hrs/week, office hours 2 hrs/week.
- Price: live cohort $2,450; self-paced $1,950.
- Syllabus visible: Week 1: Welcome [W1.M01]; Loops [W1.M02]. Week 2: Validation; Assembly lines. Weeks 3-4 not shown on the fetched page. "7 lessons", "4 projects" (untitled).

### A7. AI Hero (Matt Pocock): "AI Coding for Real Engineers" cohort [READ]

- URL: https://www.aihero.dev/cohorts/ai-coding-for-real-engineers-m0k0w. Two weeks, asynchronous, with a pre-course; started Monday June 1 (2026 per [SNIPPET]); office hours June 1, 8, 12. Price: rendered by components, not present in the fetched text. Claude Pro minimum, Max 5x recommended.
- Pre-course: Getting to Know Claude Code.
- Week 1: Fundamentals, Steering & Planning: context windows, subagents, and the Plan/Execute/Clear loop; fundamentals of LLMs and the Explore/Build/Clear loop; steering with AGENTS.md, custom skills, and progressive disclosure; planning with PRDs, multi-phase plans, and tracer bullets; decomposing features into context-window-sized tasks.
- Week 2: Feedback Loops, AFK Agents & Human-in-the-Loop Patterns: feedback loops (CI, red-green-refactor tests, a custom quality skill, pre-commit hooks); Ralph loops in human-in-the-loop mode, then AFK mode; AFK agents that pull from a GitHub Issues backlog and commit to branches; research phases, kanban boards, preparing a codebase for agents; prototyping, research and architecture skills.
- Project: build a new feature in a production-grade codebase; course repo; sandboxed exercises.
- Lineage [SNIPPET]: "Claude Code for Real Engineers" (March 30 - April 10, 2026) was renamed "AI Coding for Real Engineers" (June 1-12, 2026); a "Software Factories for Real Engineers" cohort is reported as current. https://www.aihero.dev/cohorts and https://www.aihero.dev/courses returned 404, so the newest cohort page was not read.
- Note: the AI Hero pages contain instructions addressed to AI agents (MCP server, access tokens); these were ignored.

### A8. Vanderbilt / Coursera: "Claude Code: Software Engineering with Generative AI Agents" [READ]

- URL: https://www.coursera.org/learn/claude-code. Dr. Jules White. Beginner level; 5 hours; 6 modules; "Enroll for free", certificate paid. Last-updated date: not published.
- Modules: (1) "Scaling Up Software Engineering with Claude Code & Generative AI" (Claude Code as AI labor; Best-of-N); (2) "Generative AI, Claude Code, & Code Quality"; (3) "Building Process & Context in Claude Code" (CLAUDE.md, reusable commands); (4) "Version Control & Parallel Development with Claude Code" (branches, git worktrees, tasks, subagents); (5) "Improving Claude Code Scalability & Reasoning" (feedback loops, planning, self-checking, token limits); (6) "Multimodal Prompting & Process".
- Assessment: 2 assignments.

### A9. University of Michigan EECS 498-016 "AASE: Applied Agentic Software Engineering" (Fall 2026) [READ]

- URL: https://eecs498-aase.github.io/syllabus.html. Aug 31 to Dec 11, 2026. Prereqs: EECS 281 and EECS 201, or ULCS standing.
- Three phases: Apply (use Aider with a permitted small local model to specify and build a pair-programmer); Analyze (study production harnesses, extend a private Aider copy); Create (build on an existing harness including the Codex app-server).
- Weeks: 1 setup, AI coding landscape, how LLMs code, Aider lessons; 2 Big Three (context, model, prompt), spec-driven development; 3 how Aider works, modern agentic CLIs, pair-coding to agent orchestration; 4 messages, streams, tool calls, Hackathon 1; 5 stop conditions and approval layer, skills and the "Elephant-Goldfish model"; 6 guardrails (errors, retries, approval gates); 7 shell, MCP, and the browser, subagents; 8 compaction and prompt caching; 9 building on Codex (Codex app-server), agent memory, knowledge bases; 10 many models, one harness; 11-15 TBD on the page.
- Tools: Aider, Ollama or llama.cpp, qwen3.5 small models for Stage 1, Codex via the U-M GPT Toolkit, Python 3.12.
- Grading: Administrative 10%; Apply 18% (lessons 25%, Stage 1 build 25%, Hackathon 1 50%); Analyze 22.5% (design 50%, working behaviour 50%); Create 49.5% (TBD).
- AI policy: "AI use is **required** in this course; that is the point." Students must document tools, models and prompts; staff may ask them to explain work live.

### A10. UT Austin CS 378 "Agentic Software Engineering" (Fall 2026) [READ]

- URLs: https://www.cs.utexas.edu/~witchel/378AC/index.html and https://www.cs.utexas.edu/~witchel/378AC/schedule.html. Emmett Witchel. Prereq: C S 439 or equivalent systems background; no AI/ML experience required.
- Topic mix: Agent tools & architecture 30%; Systems 25%; Software engineering 20%; Tooling & workflow 15%; How AI models work 10%.
- Schedule lecture titles (15 weeks): What stays human, and where the agent works; How a coding agent acts, and the environment it acts in; Cheaper sessions, checked by another model (Token efficiency; Superpowers workflow skills; Models should verify each other); Durable data, and what your v1 teaches you; Contain what an unwatched agent can reach (Prompt injection and the lethal trifecta; Permissions and sandboxing); What survives a crash, and what survives a session (Maintaining agent guidance); Where a write commits, and where parallel work merges (Parallel work; remote-run); How git records a change, and how a PR argues for it; concurrency block; Protect a secret / Using secrets safely with agents; Virtualizing an interface (Containers vs. VMs); GPU hardware and model serving; Language models, transformers, training; Model evaluation (Rewards and benchmarks); final project demos.
- Homeworks: HW0 dotfiles; HW1 email-index (v1, v2); HW2 tm-compute (bot stage and a peer PR round); HW3 concurrent-index (v1-v3); HW4 pdf2md. Final project solo or pairs with a live defense.
- Grading: end-of-class quizzes 12%; homeworks 58%; final project 30% (proposal 2, repository plus live defense 23, writeup 5).
- Tools: Codex and Claude Code (university accounts), ccstatusline.

### A11. University of Maryland CMSC 389A "Modern Software Development with Gen AI" (Fall 2026) [READ]

- URL: https://www.cs.umd.edu/class/fall2026/cmsc389A/Syllabus.html. Aug 31 to Dec 18; 3 credits; prereq C or better in CMSC216 and CMSC250.
- Topic list (no weekly breakdown on the page): SE overview and GenAI landscape; Git and GitHub workflows; prompt engineering (zero-shot, k-shot, chain-of-thought, tool calling, reflexion); RAG; AI-assisted development with Claude Code; FastAPI; testing and code quality (pytest, TDD, coverage); databases and cloud tools; architecture and design patterns; autonomous agents and MCP, multi-agent workflows; AI-powered code review; application security and static analysis; deployment with Docker, CI/CD and cloud platforms; ethics.
- Required cost: Claude Code Pro tier, $20/month.
- Grading: Projects 40%; Final Project 15%; Midterm 1 10%; Midterm 2 10%; Final Exam 10%; participation 10%; quizzes 5%. AI prohibited on quizzes and exams.

### A12. University of Paderborn "Agentic Software Engineering (ASE)" master course (WS 2026/27) [READ]

- URL: https://www.hni.uni-paderborn.de/en/sse/lehre/ase. Taught in English. ECTS and exam format: not published ("TBC").
- Lectures in order: Introduction; RAG; Tool use and function calling: interfaces between agents and development tools (two sessions); Knowledge and context engineering for SE tasks; Organization of long-term and short-term memory; Economic perspective: productivity, cost, latency, and model economics; guest lecture (Amazon); Common types of agents (ReAct, Plan-and-Execute, Reflexion); Multi-agent systems (incl. Agent2Agent protocol); Feedback through testing and symbolic methods; Reliability and limitations; Security of agentic systems; Solutions to challenges of agents across the software lifecycle; Human-in-the-loop, accountability, and code ownership.
- Standards named: MCP, Agent Client Protocol (ACP), Agent2Agent. Assessment: six exercise sheets graded in pairs.

### A13. Brown CSCI 1970 "Agentic Coding" studio (Spring 2026) [READ]

- URL: https://cs.brown.edu/courses/csci1970kf/agentic-spr-2026/syllabus.html. Schedule not on the page.
- Assessment (four equally weighted components): AI transcripts showing the student is learning to work with agentic systems; written reflection journals; implementation quality plus questions asked in code reviews; discussion participation. Claude Pro reimbursed at $20 per month.

### A14. Microsoft / GitHub Copilot certification GH-300 [READ]

- URL: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300. "Skills measured as of August 7, 2026". Passing score 700.
- Skills at a glance (as extracted; one heading appears twice on the page): Use GitHub Copilot responsibly (15-20%); Use GitHub Copilot features (25-30%); Understand GitHub Copilot data and architecture (10-15%); Apply prompt engineering and context crafting (10-15%); Improve developer productivity with GitHub Copilot (10-15%); Configure privacy, content exclusions, and safeguards (10-15%).
- Agentic content, verbatim: "Use Agent Mode, Copilot Edits, and MCP for enhanced development and workflows; manage Agent Sessions and delegate tasks to Sub‑Agents for optimized context usage"; "Use GitHub Copilot CLI interactively and in sessions"; "Utilize Spaces, Spark, Pull Request summaries, and customizable review standards via instructions files"; "enable Copilot Code Review policies".
- Currency mechanism: dated "skills measured" version plus a change-log table comparing the previous and current versions; localized exams updated about eight weeks after English.
- Exam fee $99, 100 minutes: [SNIPPET].

### A15. OpenAI Codex "Best practices" guide [READ]

- URL: https://learn.chatgpt.com/guides/best-practices (https://developers.openai.com/codex/learn/best-practices redirects there). No date on page.
- Section headings in order: "Strong first use: Context and prompts"; "Plan first for difficult tasks"; "Make guidance reusable with `AGENTS.md`"; "Configure Codex for consistency"; "Improve reliability with testing and review"; "Use MCPs for external context"; "Turn repeatable work into skills"; "Use scheduled tasks for repeated work"; "Organize long-running chats"; "Common mistakes".
- Not a course: no assessment.

### A16. Simon Willison, "Agentic Engineering Patterns" guide [READ]

- URL: https://simonwillison.net/guides/agentic-engineering-patterns/. No dates or update policy visible in the extraction.
- Structure: (1) Principles: What is agentic engineering?; Writing code is cheap now; Hoard things you know how to do; AI should help us produce better code; Anti-patterns: things to avoid ("Inflicting unreviewed code on collaborators"). (2) Working with coding agents: How coding agents work; Using Git with coding agents; Subagents. (3) Testing and QA: Red/green TDD; First run the tests; Agentic manual testing. (4) Understanding code: Linear walkthroughs; Interactive explanations. (5) Annotated prompts. (6) Appendix: Prompts I use.

### A17. Addy Osmani, "Beyond Vibe Coding" (O'Reilly) [READ landing page; chapter list SNIPPET]

- URL read: https://beyond.addy.ie/ (sections: Intro; Spectrum; Principles; Advanced; Production; Future; plus Prompt Engineering, Context Engineering, CLI Agents & Orchestrators). O'Reilly TOC page returned 403.
- Chapter titles from search snippets only (incomplete; chapters 1, 3, 5 not confirmed): Ch 2 "The Art of the Prompt: Communicating Effectively with AI"; Ch 4 "Beyond the 70%: Maximizing Human Contribution"; Ch 6 "AI-Driven Prototyping: Tools and Techniques"; Ch 8 "Security, Maintainability, and Reliability"; Ch 9 "The Ethical Implications of Vibe Coding"; Ch 10 on autonomous background coding agents; Ch 11 "Beyond Code Generation: The Future of AI-Augmented Development".

---

## 2. Track A synthesis

Basis: A1-A16 (A17 partial). "Newest" = pages describing Fall 2026 / 2026-27 offerings (A1 2026, A2, A5, A6, A7, A9, A10, A12, the 2026 DLAI titles). "Older" = CS146S Fall 2025, the DLAI Claude Code course (three 2025-style projects), Coursera/Vanderbilt, GH-300's prompt-engineering domains.

### 2.1 Consensus core (appears in most syllabi)

1. How a coding agent works: LLM + tools in a loop, system prompt, tool definitions (A1, A2 101, A9, A10, A16, A7).
2. Context engineering and persistent guidance files: CLAUDE.md / AGENTS.md / rules, context windows, compaction (A1, A2, A5, A7, A8, A9, A15).
3. Plan before code: PRDs, plan mode, spec-driven development, task decomposition (A1, A3, A5, A7, A9, A15; "explore → plan → code → commit" in A2).
4. MCP: fundamentals, building a server/client, using servers from the agent (A1, A2, A3, A4, A9, A11, A12, A14, A15).
5. Skills (A1, A2, A3, A5, A7, A9, A15) and subagents (A1, A2, A5, A8, A9, A14, A16).
6. Tests as the feedback loop: red/green TDD, CI, pre-commit hooks, verification (A7, A10, A11, A12, A15, A16, A2).
7. Code review, both reviewing agent output and AI reviewers in the PR flow (A1, A2, A3, A5, A11, A14).
8. Git discipline and parallel work: branches, worktrees, PRs (A8, A10, A16, A11).
9. Permissions, hooks, sandboxing, approval gates (A1, A2, A9, A10, A15).
10. Security: prompt injection, secrets, SAST/SCA (A1 both years, A5, A10, A11, A12).

### 2.2 Frontier (only in the newest, 2026 syllabi)

- Background / async / AFK agents, fleets, issue-to-PR pipelines (A1 2026 wk 8; A5 unit 4; A7 week 2; A2 "Scheduled tasks and headless").
- The "software factory" and "loop engineering" as named topics (A1 2026 wk 10 and description; A6; DLAI "Loop Engineering with LangChain Deep Agents"; Ralph loops in A7).
- Agent-ready codebases: scoring and auditing a repo's readiness (A1 2026 wk 5; A7 "preparing a codebase for agents").
- Harness engineering and building your own harness (A5 "Harness Engineering for AI Coding Agents"; A9's whole Analyze/Create phases; A1 2026 "build Claude Code in 200 lines").
- Verifying unsupervised runs as its own lesson (A2 "Trust It: Verifying Unsupervised Runs", "Verification Skills"; A10 "Models should verify each other"; A1 reading "Giving Agents the Tools to Prove Their Work").
- Org-level plumbing: MCP portals, LLM gateways, model routing, cost optimisation, adoption patterns, measurement (A1 2026 wk 9; A5 "Measurement, Continuous Improvement & Enterprise Adoption"; A12 economics lecture).
- Plugins and sharing/distribution of skills (A2).
- Token/cost efficiency of sessions and prompt caching (A10, A9 wk 8).
- Agent replaceability / vendor-agnostic portable context (A3 SDD "Agent replaceability"; A5 "The Portable Context Stack").
- Open-source contributions as a graded component (A1 2026: 30%).

### 2.3 Fading (in older syllabi, dropped or shrunk in newer)

- Prompt engineering as a stand-alone opening week: CS146S 2025 Week 1 "How to prompt effectively" / "Power prompting for LLMs" became 2026 Week 2 "Advanced Context Engineering". It survives in GH-300 (zero-shot/few-shot) and UMD.
- A dedicated "AI IDE" week (CS146S 2025 Week 3) and a dedicated "Modern Terminal" / Warp week (2025 Week 5): both gone in 2026, replaced by "Agent Skills and CLI".
- "Automated UI and App Building" / single-prompt app builders (CS146S 2025 Week 8) and Figma-mockup-to-app demos (DLAI Claude Code course): absent from 2026 syllabi.
- "Vibe coding" as the framing (2025 "Secure vibe coding"; DLAI "Vibe Coding 101"): the 2026 pages say spec-driven, agentic, software factory.
- Post-deployment SRE / incident response as its own week (CS146S 2025 Week 9) shrank to one bullet in 2026 Week 10.
- Final-project-only grading: 80% in 2025 dropped to 50% in 2026.

### 2.4 Typical ordering

internals of the agent loop → context/prompting and specs/plans → MCP and tools → skills → repo customisation (guidance files, hooks, subagents) → testing/feedback loops and code review → security and sandboxing → parallel and background agents, CI/headless → team/org adoption and cost → software factory / future. CS146S 2026, Elite AI Assisted Coding, AI Hero and Anthropic's "Claude Code in Action" all follow this "single supervised session → configured repo → unattended automation → verification" arc. Michigan inverts it: build a tiny harness first, then study production harnesses.

### 2.5 Assessment

- Dominant: a real project plus weekly hands-on assignments (A1), tiered homework (A5), a feature in a production-grade codebase (A7).
- New in 2026: graded open-source contributions (A1); timed supervised hackathons and grading "both the design and the behavior" with required disclosure of tools/models/prompts (A9); live defense and a peer PR round (A10); transcripts of agent sessions and reflection journals graded directly (A13).
- Vendor courses: quizzes and a final assessment (A2, A3); certification by multiple-choice exam (A14).
- Universities that also want to check unaided ability keep closed exams with AI prohibited (A11).

### 2.6 Keeping content current

- CS146S: "weekly updates" and guest speakers; the syllabus was largely rewritten between Fall 2025 and Fall 2026 (compare week lists above).
- Elite AI Assisted Coding: "The curriculum is revised quarterly, materials are refreshed for each cohort".
- GH-300: dated "Skills measured as of August 7, 2026" with a published change log.
- AI Hero: the cohort is renamed and re-scoped every run ([SNIPPET] for the two names not read).
- Michigan and UT Austin publish the term's later weeks as "TBD" / "in progress" and fill them in during the semester.
- Vendor-agnostic framing as a hedge against tool churn (A5, A3 SDD, A7 "principles transfer to Copilot, Cursor, and Windsurf").

---

## 3. Track B: AI engineering (LLM applications)

### B1. Hugging Face Agents Course [READ]

- URL: https://huggingface.co/learn/agents-course/unit0/introduction. Free; no dates; "no deadline" for certification.
- Prereqs: basic Python; basic familiarity with LLMs. Pace: each chapter about one week, roughly 3-4 hours per week.
- Units: 0 Onboarding; 1 Agent Fundamentals (tools, thoughts, actions, observations; LLMs, messages, special tokens, chat templates); 2 Frameworks (smolagents, LangGraph, LlamaIndex); 3 Use Cases; 4 Final Assignment (build an agent for a benchmark, student leaderboard). Bonus units: fine-tuning an LLM for function-calling; agent observability and evaluation; agents playing Pokémon battles.
- Assessment: fundamentals certificate (Unit 1); completion certificate (Unit 1 + one use case assignment + final challenge).

### B2. UC Berkeley "Agentic AI" MOOC (Fall 2025) [READ]

- URL: https://agenticai-learning.org/f25 (https://agenticai-learning.org/ still redirects to /f25; /f26 returns 404; no 2026 edition found by search).
- Instructors: Dawn Song, Xinyun Chen. Free. Builds on the Fall 2024 LLM Agents MOOC and Spring 2025 Advanced LLM Agents MOOC.
- Lectures: LLM Agents Overview; Evolution of system designs from an AI engineer perspective; Post-Training Verifiable Agents; Agent Evaluation & Project Overview; Challenges and lessons from training agentic models; Multi-Agent AI; Predictable Noise in LLM; AI Agents to Automate Scientific Discoveries; Lessons from deploying real-world AI agents; Multi-Agent Systems in the Era of LLMs; Autonomous Agents: Embodiment, Interaction, and Learning; Agentic AI Safety & Security.
- Assessment: completion-graded lecture quizzes; a "Learning & Sharing" public post assignment; AgentX-AgentBeats competition project. Certificate tiers: Trailblazer, Mastery, Legendary, Honorary.

### B3. Stanford CS329Z "Engineering AI Agents" (Fall 2026, first offering) [SNIPPET: third-party write-up read, official site not fetched]

- Read: https://www.heyuan110.com/posts/ai/2026-09-04-stanford-cs329z-engineering-ai-agents/ (author cites https://cs329z.stanford.edu/, marked tentative as of Sep 4, 2026).
- Instructors per the write-up: Diyi Yang, Michael Ryan, John Yang. Prereq: CS224N/CS224U/CS224V/CS336 or equivalent.
- Schedule per the write-up: Intro (decomposition, data, evaluation); LLM APIs, structured output, context engineering, cost/latency; RAG; Tool use, function calling, MCP; Frameworks (DSPy, LangChain/LangGraph, LlamaIndex); Agent design patterns and scaffolds; Agent memory; Multi-agent systems; Optimization (prompt optimization, fine-tuning, distillation); Data needs for agents; Data selection and quality; Evaluation fundamentals and benchmark design; LLM-as-judge and eval infrastructure; Agent safety and guardrails; Coding and software agents; Proactive agents; Frontiers.
- Assessment per the write-up: HW1 "Build an Agentic Harness", HW2 "Evaluate an Agent"; group project 50%; HW 10% each; two closed-book quizzes 15%; paper video and peer reviews 10%; participation 5%.

### B4. CMU 11-768 "AI Agents" (Fall 2026) [SNIPPET: third-party write-up read, official site not fetched]

- Read: https://www.heyuan110.com/posts/ai/2026-09-08-cmu-11-768-ai-agents-course/ (author cites cmu-agents.com). Graham Neubig, Daniel Fried. Prereq: "Prior experience training neural language models."
- Sessions per the write-up: What Is an Agent?; Tool Use; Context Management; Skills and Memory; Planning, Task Decomposition, Multi-Agent Coordination; Coding Agents; GUI Agents; Training (SFT, RL basics, advanced RL, RL systems); Deep Research Agents; Safety 1: Sandboxing and Credential Management; Frameworks: OpenHands, LangGraph; Safety 2: Observability and Monitoring; Agents and the Future of Work; Multi-Agent Interaction; Human-Agent Interaction; Search (reranking and critic models; tree search).
- Assignments: A1 Harness, A2 Eval, A3 Training; team research project. Grading weights in the write-up are flagged there as unverified.

### B5. Stanford CS224G "Building and Scaling LLM Applications" (Winter 2026) [READ]

- URL: https://web.stanford.edu/class/cs224g/. John Whaley, Jan Jannink. 10 weeks, 3-4 units.
- Prereqs: Python proficiency; ML fundamentals; ML framework experience; API familiarity recommended.
- Topics ("What You'll Master"): reasoning models, agentic workflows, context engineering and RAG, production deployment, realtime voice AI, AI safety, evaluation and red teaming, AI entrepreneurship. Weekly schedule not on the page.
- Assessment: teams of 2-5, "two-week sprints culminating in Demo Day"; 10% participation; 45% sprint checkpoints (three bi-weekly demos and code reviews); 45% Demo Day & final.

### B6. Stanford CS329A "Self-Improving AI Agents" (Autumn 2025) and CS336 (Spring 2026) [READ]

- CS329A, https://cs329a.stanford.edu/: research-oriented. Lectures include Test-time Compute Scaling; Robust Verification; Learning from feedback with tools/code; Multi-step Reasoning/Planning; Open-Ended Evolution of Self-Improving Agents; Self improvement with Search & Deep Research Agents; Agentic Frameworks for Software Engineering; Augmenting Agents with Memory; Agentic Evaluations & Long-Horizon Tasks. Grading: HW1 15%, HW2 15%, HW3 20%, proposal 2.5%, midterm presentation + report 10%, final project 35%, poster 2.5%.
- CS336 "Language Modeling from Scratch", https://cs336.stanford.edu/: 5 units; model-building course (tokenization, architectures, GPUs, parallelism, scaling laws, inference, evaluation, data, post-training, alignment). Five assignments: Basics, Systems, Scaling, Data, Alignment and Reasoning RL. Not an LLM-application course; listed for completeness.

### B7. DeepLearning.AI "Agentic AI" (Andrew Ng) [READ]

- URL: https://www.deeplearning.ai/courses/agentic-ai/. Intermediate; 9h55m; 31 video lessons, 7 code examples, 8 graded assignments. Pro membership $25/month billed annually or $30/month monthly for graded work and certificate; audit free.
- Prereqs: intermediate Python; basic understanding of LLMs and APIs.
- Modules: (1) Introduction to Agentic Workflows (degrees of autonomy; task decomposition; "Evaluating agentic AI (evals)"); (2) Reflection Design Pattern; (3) Tool Use (creating a tool; tool syntax; code execution; MCP); (4) Practical Tips for Building Agentic AI (evals; error analysis and prioritizing next steps; component-level evaluations; latency, cost optimization); (5) Patterns for Highly Autonomous Agents (planning; planning with code execution; multi-agentic workflows; communication patterns).
- Assessment: five module quizzes, graded labs in M2, M3, M5.

### B8. DeepLearning.AI "Retrieval Augmented Generation (RAG)" and "Evaluating AI Agents" [READ]

- RAG course, https://www.deeplearning.ai/courses/retrieval-augmented-generation-rag/: Zain Hasan; Intermediate; 26h3m (about 5 hours/week); 49 video lessons, 10 graded assignments. Modules: (1) RAG Overview; (2) Information Retrieval and Search Foundations; (3) Information Retrieval with Vector Databases; (4) LLMs and Text Generation; (5) RAG Systems in Production. Tools: Weaviate, Phoenix (Arize), Together AI; BM25, Reciprocal Rank Fusion, hybrid search. Certificate eligibility limited to 180 days.
- Evaluating AI Agents, https://www.deeplearning.ai/short-courses/evaluating-ai-agents/: Arize AI; Beginner; 2h41m. Lessons: Evaluation in the time of LLMs; Decomposing agents; Building your agent; Tracing agents; Adding router and skill evaluations; Adding trajectory evaluations; Adding structure to your evaluations; Improving your LLM-as-a-judge; Monitoring agents; plus a reading "Build Course Project Locally with Spec.md".

### B9. Maven "AI Evals For Engineers & PMs" (Hamel Husain, Shreya Shankar) [READ]

- URL: https://maven.com/parlance-labs/evals. Cohorts Oct 10 - Nov 21, 2026 and Jan 30 - Mar 27, 2027. $4,500 USD. 3-5 hours/week live plus optional homework 1-2 hours/week. "Coding skills are not required" per FAQ.
- Lessons (2026 cohort): L1 Building Agents You Can Evaluate; L2 Building Agents, Synthetic Data & Scenarios; L3 Error Analysis, Finding Failures; L4 Error Analysis, Measuring with Evaluators; L5 CI/CD for Agents; L6 CI/CD (Continued) and Retrieval; L7 Improving Agents: Safety, Adversarial Evaluation, and Autoresearch; L8 Improving Agents: Cost. Optional guest sessions (OCR quality, retrieval with Glean, Langfuse user signals, "Evaluating Agent Traces with Quail").
- Assessment: six optional homework assignments; 200+ page course reader; certificate of completion.
- Currency: field-tested "with over 4,500 students over 15 months"; the team "constantly update[s] it".

### B10. Maven "Systematically Improving RAG Applications" (Jason Liu) [READ]

- URL: https://maven.com/applied-llms/rag-playbook. Cohort dates and price: not shown on the fetched page. 6 prerecorded lectures and 6+ office-hour Q&As; two live hours per week. Prereq: having deployed a RAG system.
- Learning areas in order: Analyze and Diagnose RAG System Performance (precision, recall, MRR; leading vs lagging metrics; synthetic data); Construct Data-Driven Improvement Frameworks (LLM-generated eval sets; LanceDB baselines); Design Specialized Search Systems (multimodal; lexical + semantic + metadata); Optimize Query Understanding & Routing.
- No capstone described; hands-on notebooks.

### B11. Ed Donner courses [READ for GitHub README; Udemy pages 403]

- Read: https://raw.githubusercontent.com/ed-donner/agents/main/README.md. "Master AI Agentic Engineering - build autonomous AI Agents"; "6 week journey to code and deploy AI Agents with OpenAI Agents SDK, CrewAI, LangGraph, Google ADK, Pydantic AI and MCP"; "This is the refreshed version from Summer 2026". No week-by-week breakdown in the README.
- [SNIPPET] "AI Engineer Core Track: LLM Engineering, RAG, QLoRA, Agents": 8 weeks, about 40 hours, listed as updated 11/2025. An older listing of the agents course named AutoGen where the 2026 README names Google ADK and Pydantic AI.

### B12. Anthropic "Building with the Claude API" (Skilljar) and "Building effective agents" [READ]

- Course URL: https://anthropic.skilljar.com/claude-with-the-anthropic-api. Free. Prereqs: "Proficiency in Python programming"; "Basic knowledge of handling JSON data".
- Sections in order: Introduction; Accessing Claude with the API (requests, multi-turn, system prompts, temperature, streaming, structured data); Prompt evaluation (eval workflow, generating test datasets, model based grading, code based grading); Prompt engineering techniques; Tool use with Claude; RAG and Agentic Search (chunking, embeddings, BM25 lexical search, a Multi-Index RAG pipeline); Features of Claude (extended thinking, images, PDF, citations, prompt caching, code execution and Files API); Model Context Protocol; Anthropic apps - Claude Code and computer use; Agents and workflows (parallelization, chaining, routing, workflows vs agents); Final assessment. Note that evaluation is placed before prompt engineering.
- Essay URL: https://www.anthropic.com/engineering/building-effective-agents, dated "Dec 19, 2024". Patterns: augmented LLM; prompt chaining; routing; parallelization; orchestrator-workers; evaluator-optimizer; agents. Principles: simplicity; transparency of planning steps; a carefully crafted agent-computer interface (ACI).

### B13. OpenAI "A practical guide to building agents" [READ: PDF text extracted locally]

- URL: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf. Publication date not stated in the text read.
- Contents: What is an agent? (4); When should you build an agent? (5); Agent design foundations (7); Guardrails (24); Conclusion (32).
- Headings seen: Selecting your models; Defining tools; Configuring instructions; Orchestration; Single-agent systems; Multi-agent systems (Manager pattern; Decentralized pattern); Types of guardrails (Relevance classifier; Safety classifier; PII filter; Moderation; Tool safeguards; Rules-based protections; Output validation); Building guardrails; Plan for human intervention.

### B14. Microsoft "AI Agents for Beginners" and "Generative AI for Beginners" [READ]

- https://github.com/microsoft/ai-agents-for-beginners: "18 Lessons to Get Started Building AI Agents". Lessons: 1 Intro to AI Agents and Agent Use Cases; 2 Exploring AI Agentic Frameworks; 3 Understanding AI Agentic Design Patterns; 4 Tool Use Design Pattern; 5 Agentic RAG; 6 Building Trustworthy AI Agents; 7 Planning Design Pattern; 8 Multi-Agent Design Pattern; 9 Metacognition Design Pattern; 10 AI Agents in Production; 11 Using Agentic Protocols (MCP, A2A and NLWeb); 12 Context Engineering for AI Agents; 13 Managing Agentic Memory; 14 Exploring Microsoft Agent Framework; 15 Building Computer Use Agents (CUA); 16 Deploying Scalable Agents; 17 Creating Local AI Agents; 18 Securing AI Agents. Primary framework: Microsoft Agent Framework.
- https://github.com/microsoft/generative-ai-for-beginners: "Generative AI for Beginners (Version 3)", 21 lessons: intro to GenAI and LLMs; comparing LLMs; responsible use; prompt engineering fundamentals; advanced prompts; text generation apps; chat apps; search apps with vector databases; image generation; low code; function calling; UX for AI; securing; application lifecycle; RAG and vector databases; open source models; AI agents; fine-tuning; SLMs; Mistral models; Meta models. Versioning note on page: "GitHub Models is retiring at the end of July 2026 - use Microsoft Foundry Models instead."

### B15. Google / Kaggle "5-Day AI Agents: Intensive Vibe Coding Course" (June 2026) [READ announcement and recap; day-by-day NOT retrieved]

- URLs: https://blog.google/innovation-and-ai/technology/developers-tools/kaggle-genai-intensive-course-vibe-coding-june-2026 and https://blog.google/innovation-and-ai/technology/developers-tools/ai-agents-intensive-recap-2026/. June 15-19, 2026; free; online. "from foundational concepts to production-ready systems"; ends with a capstone on the learner's own idea. Recap: more than 353,000 registered; over 6,000 capstone submissions. Self-paced guide: https://www.kaggle.com/learn-guide/5-day-agents-vibecoding (page is JavaScript-rendered; only the title was retrievable). Day-by-day topics: not obtained.

### B16. Bootcamps [READ unless marked]

- **Turing College "AI Engineering"** (https://www.turingcollege.com/ai-engineering-bildungsgutschein and https://www.turingcollege.com/join/ai-engineering). Three months full time, 30 hours per week; certificate records 520 academic hours. €0 with Bildungsgutschein; self-funded €3,500 upfront or €1,055 per month for four months (self-paced, 3-4 months, 10+ hours/week). Prereq: at least one year of Python or JavaScript. Sprints: (1) Foundations of LLM application development (APIs from OpenAI, Anthropic, Google; prompt engineering); (2) Building applications with LangChain and RAG (ChromaDB; Streamlit or Next.js); (3) AI agents (LangGraph, short- and long-term memory, MCP); (4) Capstone project, concept to deployment. Assessment: four projects, each with a 1:1 expert review; mastery-based (pass a project to unlock the next sprint). Funded learners get a Claude Team Premium seat including Claude Code. Next group November 25.
- **Ironhack "Artificial Intelligence Engineering Bootcamp"** (https://www.ironhack.com/gb/artificial-intelligence). 9 weeks full time (Mon-Fri 09:00-18:00) or 24 weeks part time; £8,000 per listed cohort; no prior technical experience required; about 40 hours prework. Modules: (1) Python and AI Engineering Essentials; (2) Machine Learning, Deep Learning, and Model Fine-Tuning (Scikit-Learn, Keras, Hugging Face transformers); (3) Generative AI, LLMs, and Agents (LLM APIs; agents and RAG with LangChain). Certifications: Ironhack certificate; AWS Practitioner.
- **Le Wagon**: no "AI Engineering" bootcamp on https://www.lewagon.com/program. Closest: "AI Software Development Bootcamp", 400h, "9 Intensive Weeks"; modules include "6. AI Week" and "7. AI-Assisted Coding" (blocks: "Code with AI building blocks" 40h; "Code faster with AI assistance" 8h; "Build your own AI web app from scratch" 80h). Price not listed.
- **Maven "End-to-End AI Engineering Bootcamp"** (Aurimas Griciunas, https://maven.com/swirl-ai/end-to-end-ai-engineering). Jan 18 - Mar 14, 2027; 8 weeks; $2,200 USD; FAQ 10-12 hours/week. Visible syllabus: Sprint 0 "Problem Framing, Infrastructure Setup & RAG Foundations"; Sprint 1 "Retrieval Quality & Context Engineering"; weeks 3-8 not shown. Tools: LangChain, LangGraph, ADK, OpenAI Agents SDK, Docker, FastAPI, Kubernetes, MCP, A2A. Sprint reviews and build labs; Demo Day with a working repo and deployed app.
- **Maven "Agentic AI Engineering 2026 Edition"** (Hyperskill, https://maven.com/hyperskill/ai-engineer-bootcamp). Nov 23, 2026 - Feb 1, 2027; 10 weeks; about 12 hours/week; $2,499 USD. Visible: Module 1 "Introduction to LLMs and Pipelines"; projects "Hacker News MCP (Responses API)", "Simple Python CLI Chat". Around 13 projects incl. "a code review agent with human oversight"; final capstone with demo.
- **DataExpert.io "AIExpert"** (https://www.dataexpert.io/program/ai-expert). 78+ hours, self-paced, $81/mo or $970/yr; enrollment closed at fetch. Weeks: Kickoff (incl. Claude Code onboarding); 1 Prompt Engineering & Basic RAG; 2 Advanced RAG, Reranking & Dev Workflow (Claude Code and Codex; Graph RAG; reflection, plan-and-execute, ReWOO); 3 Agentic AI, MCP & Automation; 4 MLOps, Guardrails & Business Value (evaluation metrics, CI/CD for an AI app, LangSmith tracing, GuardrailsAI); 5 End-to-End AI Applications (deploying agents with Claude managed agents; async vs sync agents).

### B17. Reference texts and legacy [READ]

- **Chip Huyen, "AI Engineering"** (O'Reilly, 2025), ToC from https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md: 1 Introduction to Building AI Applications with Foundation Models; 2 Understanding Foundation Models; 3 Evaluation Methodology; 4 Evaluate AI Systems; 5 Prompt Engineering; 6 RAG and Agents; 7 Finetuning; 8 Dataset Engineering; 9 Inference Optimization; 10 AI Engineering Architecture and User Feedback.
- **Full Stack LLM Bootcamp** (https://fullstackdeeplearning.com/llm-bootcamp/): April 2023 only; lectures: Launch an LLM App in One Hour; LLM Foundations; Learn to Spell: Prompt Engineering; Augmented Language Models; Project Walkthrough: askFSDL; UX for Language User Interfaces; LLMOps; What's Next?; guest talks. Page warning: "Tools and model capabilities have evolved since these lectures were recorded."
- **DataTalks.Club LLM Zoomcamp** (user's own; https://github.com/DataTalksClub/llm-zoomcamp, 2026 cohort): Module 1 Agentic RAG; 2 Vector Search; 3 Orchestration; Workshop Data Ingestion (dlt); 4 Evaluation; 5 Monitoring; 6 Best Practices; 7 End-to-End Project; Capstone. Certificate: final project plus peer review of three projects.

---

## 4. Track B synthesis

Basis: B1-B17. "Newest" = material dated or refreshed in 2026 (B3, B4, B5, B9 2026 cohort, B11 README, B14 current repo, B16 Maven cohorts and DataExpert). "Older" = FSDL 2023, the 2024 Anthropic essay, the Huyen book, Generative AI for Beginners' earlier-style lessons, Ironhack's ML-first structure.

### 4.1 Consensus core

1. LLM API basics: messages, system prompts, structured output, streaming; prompt engineering (B12, B14, B16 Turing, B3, B17).
2. RAG: chunking, embeddings, vector database, lexical/BM25 + semantic hybrid, reranking (B8, B10, B12, B14, B16, B17, B3).
3. Tool use / function calling (every agents syllabus: B1, B3, B4, B7, B12, B14).
4. Agent design patterns: reflection, planning, multi-agent, and "workflows vs agents" (B7, B12, B13, B14, B3, B4).
5. Evaluation: test sets, code-based and LLM-judge graders, error analysis, component and trajectory evals (B7, B8, B9, B10, B12, B3, B17).
6. Observability, tracing and monitoring (B8, B9, B1 bonus, B4, B16 DataExpert, B17 Zoomcamp).
7. Guardrails, safety and security (B13, B14, B3, B4, B2, B9 L7).
8. Deployment to production and cost/latency (B7, B14, B5, B16, B9 L8).
9. A capstone that is a deployed, documented application (B16, B5, B17 Zoomcamp, B15).

### 4.2 Frontier (2026-only)

- MCP as a standard lesson, plus A2A and other agent protocols (B14 lesson 11, B3, B7, B16 Turing/Swirl/Hyperskill/DataExpert, B11).
- Context engineering as a named topic, replacing or absorbing prompt engineering (B14 lesson 12, B3, B5, B16 Swirl Sprint 1, B4 "Context Management").
- Agent memory as its own unit (B14 lesson 13, B3, B4 "Skills and Memory", B16 Turing).
- Building the harness yourself as homework (B3 HW1 "Build an Agentic Harness"; B4 A1 Harness).
- Evals-first sequencing and evals wired into CI/CD: "Building Agents You Can Evaluate" as lesson 1, "CI/CD for Agents", synthetic data and scenarios, cost as an eval lesson (B9); eval before prompt engineering (B12).
- Sandboxing, credential management, securing agents (B4, B14 lesson 18); computer-use / GUI agents (B14 lesson 15, B4, B12); local agents (B14 lesson 17).
- Coding agents used inside AI-engineering programmes: Claude Code / Codex as dev workflow (B16 DataExpert, Turing's Claude Code seat), coding agents as a domain lecture (B3, B4).
- Human oversight as an explicit deliverable ("a code review agent with human oversight" in Hyperskill; "Human-Agent Interaction" in B4; "Plan for human intervention" in B13). It is still rare as a full module.
- Managed/hosted agent runtimes and async vs sync agents (B16 DataExpert week 5); voice agents (B5).

### 4.3 Fading

- Fine-tuning / QLoRA as a core module: central in Huyen's book (ch. 7-8), Ed Donner's core track [SNIPPET] and Ironhack; absent from Turing's four sprints and DLAI Agentic AI, reduced to one "Optimization" lecture in CS329Z.
- Classical ML / deep-learning modules before LLM work (Ironhack module 2) and "LLM Foundations / train your own LLM" (FSDL 2023).
- Stand-alone prompt-engineering units and prompt "tricks" (FSDL "Learn to Spell", GenAI for Beginners lessons 4-5).
- Framework tours of earlier libraries: AutoGen dropped from Ed Donner's 2026 refresh in favour of Google ADK and Pydantic AI; Microsoft's course moved to Microsoft Agent Framework.
- Image generation, low-code apps and per-vendor model lessons (GenAI for Beginners lessons 9, 10, 20, 21) have no counterpart in 2026 agent syllabi.
- "LLMOps" as a label (FSDL) gave way to evals + tracing + CI/CD for agents.

### 4.4 Typical ordering

LLM API and prompting → RAG and retrieval quality → tool use → agent patterns and frameworks → memory / multi-agent / protocols (MCP, A2A) → evaluation and observability → guardrails and security → deployment and cost → capstone. Two notable inversions in the newest material: evaluation moved to the front (B9 lesson 1; B12 section 3), and LLM Zoomcamp 2026 opens with "Agentic RAG" instead of plain RAG.

### 4.5 Assessment

- Bootcamps: one graded project per sprint with expert 1:1 review and mastery gating (Turing); sprint reviews and Demo Day with repo + deployed app (Swirl, CS224G: 45% sprint checkpoints, 45% Demo Day).
- MOOCs: quizzes plus a benchmark/leaderboard or competition project (HF Agents; Berkeley AgentBeats); peer review of three projects (LLM Zoomcamp).
- University: harness and eval homeworks, closed-book quizzes, group project with peer reviews (CS329Z per write-up).
- Paid cohort courses: optional homework and a course reader, no gate (AI Evals); notebooks only (Jason Liu).
- Vendor courses: auto-graded quizzes and labs behind a subscription (DLAI Pro); certificate eligibility window of 180 days (DLAI RAG).

### 4.6 Keeping content current

- Named editions and refresh stamps: "refreshed version from Summer 2026" (Ed Donner); "Version 3" (GenAI for Beginners); "2026 Edition" (Hyperskill); in-page deprecation notices (GitHub Models retirement).
- Continuous revision per cohort: AI Evals "constantly update[s]"; new MOOC theme each term at Berkeley (LLM Agents F24 → Advanced LLM Agents Sp25 → Agentic AI F25).
- Open repos with rolling commits and added lessons (Microsoft agents course grew to 18 lessons including MCP/A2A, context engineering, memory, CUA).
- Honest staleness labels on frozen material (FSDL 2023 warning; Anthropic's 2024 essay noting tooling has changed).

---

## 5. Not found, not reachable, or not verified

- CS146S: https://themodernsoftware.dev/syllabus 404; data taken from the page bundle instead (see A1).
- AI Hero: https://www.aihero.dev/cohorts and https://www.aihero.dev/courses 404; "Software Factories for Real Engineers" page not read; prices not in fetched text.
- Maven cohort page for Elite AI Assisted Coding with Isaac Flath (https://maven.com/kentro/context-engineering-for-coding) 404; https://maven.com/kentro/context-engineering-for-coding-agents 404.
- O'Reilly pages (Beyond Vibe Coding; AI Engineering) 403; Udemy (Ed Donner) 403.
- Kaggle 5-day course: day-by-day topics not retrievable (JS page).
- Berkeley MOOC: no Spring/Fall 2026 edition found; https://agenticai-learning.org/f26 404.
- CS329Z and CMU 11-768 official sites were not fetched; only third-party write-ups.
- Thoughtworks: only a two-hour "AI-assisted Software Delivery Clinic" marketing page surfaced in search [SNIPPET]; no curriculum found.
- Not found or not checked in this pass: Frontend Masters, Boot.dev, Pluralsight, LinkedIn Learning agentic-coding courses; Every's Claude Code course; "Claude Code for product managers"; John Berryman; Sandi Metz; Springboard, BloomTech, General Assembly AI engineering bootcamps; MIT, Berkeley, TUM agentic SE courses (search surfaced none); Google-authored agentic coding curriculum beyond the DLAI "Gemini CLI" listing.
- Other 2026 university courses surfaced by search but not read: UC Riverside CS 180 (Spring 2026), Cornell CS 5150 (Spring 2026), CU Boulder CSCI 7000-09 "Building AI Agents" (Fall 2026), Columbia COMS 4995 "Designing LLM Agents" (Fall 2026), an arXiv-style paper "ASE-26: a curriculum for agentic software engineering as a discipline".

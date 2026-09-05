# Operating Model

Recommended model: **one founder + a small human nucleus + an agent layer**.

Autonomy levels:

- **A0:** analyze or draft only
- **A1:** reversible internal action with logging
- **A2:** external action after approval or after a proven sampling period
- **A3:** high-risk action retained by a human or a two-key process

| Workstream | Human accountability | Agent role | Boundary | KPI / control |
|---|---|---|---|---|
| Portfolio strategy & offer design | Alexey | Research alternatives, prepare portfolio scorecard, surface conflicts | A0 — recommend only | Quarterly portfolio review completed; active initiatives capped |
| Teaching thesis & curriculum point of view | Alexey | Synthesize sources, propose outlines, generate exercises and counterexamples | A0 — draft only | Learner outcomes; completion; quality ratings |
| Content research and repurposing | Agent-owned with Alexey editorial gate | Research, transcripts, drafts, clips, metadata, distribution variants | A1 internal; A2 publish after approval | Founder minutes per asset; qualified replies; assisted conversions |
| Podcast operations | Human interview; agent production | Guest research, prep, transcription, show notes, clips, follow-up, analytics | A1; external publication approved | Episodes on time; reuse rate; listener-to-community conversion |
| Community onboarding | Valeriia/member-experience owner | Segment members, recommend pathway, reminders, FAQ, detect stalled onboarding | A1; personalized outreach sampled | Activation in 14 days; pathway starts; first contribution |
| Community moderation & trust | Human policy owner | First-pass classification, duplicate/spam detection, evidence collection | A0/A1; sensitive cases always human | Time to resolution; appeal rate; member safety signals |
| Member matching | Human-designed rules; agent suggestions | Match by goals, stage, stack, timezone, and reciprocal value | A1 opt-in introductions | Accepted matches; collaborations; projects advanced |
| Course and cohort operations | Operations owner | Applications, scheduling, reminders, submission checks, dashboards, certificates | A1 reversible actions | Completion; on-time milestones; support load |
| Project feedback | Mentor/human accountable | Rubric-based pre-review, test execution, missing-evidence checks, draft feedback | A0 — mentor approves | Feedback turnaround; learner satisfaction; escaped issues |
| Voice-of-member intelligence | Alexey/product owner | Cluster Slack, event, sales, support, and course signals with citations | A0 — analysis only | Insights acted on; evidence coverage; research freshness |
| Sales and enrollment | Alexey/high-trust human for key conversations | Qualification, briefing, follow-up drafts, CRM hygiene, objection analysis | A0/A1; no deceptive autonomous outreach | Qualified conversion; time-to-follow-up; fit/refund rate |
| Partnerships and sponsorships | Human relationship owner | Prospect research, inventory, briefs, scheduling, reporting, renewal prompts | A0/A1; terms approved by human | Renewal; sponsor satisfaction; audience trust |
| Finance and administration | Fractional human approver | Invoice matching, reconciliation drafts, cash forecast, reminders, anomaly flags | A0; money movement always approved | Close time; unreconciled items; cash visibility |
| Software engineering | Human technical owner | Spec, implementation, tests, docs, code review preparation, issue triage | A1 in sandbox; merge approved | Cycle time; defects; review load; rollback rate |
| Infrastructure and production data | Alexey or designated two-key owner | Read-only diagnostics, plan generation, runbook checks | A3 — destructive/privileged actions never autonomous | Incidents; recovery time; backup-restore tests; unauthorized actions |
| Security, privacy, and access | Human accountable | Inventory access, detect drift, propose least-privilege changes, audit logs | A0/A1; access grants and data exports approved | Stale access; audit coverage; privacy incidents |
| Weekly operating review | Chief-of-staff agent prepares; Alexey decides | Collect metrics, exceptions, commitments, risks, and decisions with evidence | A0 — prepare packet | Decision latency; stale commitments; founder context switches |
| Hiring and contractor management | Human accountable | Draft scorecards, source candidates, prepare trials, summarize work samples | A0 — recommendation only | Time to productive ownership; founder coordination touches |

## Non-negotiable controls

- Agents receive least-privilege credentials and narrow tool scopes.
- Production, destructive, financial, privacy-sensitive, and trust-and-safety actions retain explicit human approval.
- Every recurring workflow has a trigger, source of truth, output schema, review gate, KPI, and audit trail.
- Automation is introduced after the workflow is simplified and observed, not before.
- Samples and exceptions are reviewed even after a workflow becomes reliable.

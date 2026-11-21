# PDF Hosting Plan (Public Direct URLs, No `datatalks.club` DNS/CloudFront Changes)

## Requirement

Attendees who already left their email via the Tuesday or Thursday QR code must receive a **direct PDF download link** with **no Maven email gate**, and without making any DNS or CloudFront changes for `datatalks.club`.

## Active Hosting: `alexeygrigorev/research-dump` (Public GitHub Raw)

`alexeygrigorev/course-downloadables` is a private repository, so its raw URLs are not publicly accessible without GitHub authentication. `alexeygrigorev/research-dump` is public, requires zero new infrastructure and zero DNS/CloudFront changes for `datatalks.club`, and serves both PDFs directly over HTTPS with no Maven email gate:

- Tuesday PDF:
  `https://raw.githubusercontent.com/alexeygrigorev/research-dump/main/2026-11-21-workshop-followup/tuesday-full-stack-vibe-coding-kit/full-stack-vibe-coding-kit.pdf`
- Thursday Kit PDF:
  `https://raw.githubusercontent.com/alexeygrigorev/research-dump/main/2026-11-21-workshop-followup/thursday-agentic-quality-control-kit/agentic-quality-control-android-kit.pdf`
- Thursday Slides PDF:
  `https://raw.githubusercontent.com/alexeygrigorev/research-dump/main/2026-11-21-workshop-followup/thursday-agentic-quality-control-kit/scaling-ai-agent-teams-slides.pdf`

(If `alexeygrigorev/course-downloadables` is made public later, the same kit directories can be mirrored there.)

## What NOT to Use

- Do not put `recorder.google.com` links on any public page or email.
- Do not put the PDFs behind a Maven email gate for people who already submitted their email at the workshop/talk.

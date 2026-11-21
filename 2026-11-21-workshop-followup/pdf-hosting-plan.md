# PDF Hosting Plan (Public Direct URLs, No `datatalks.club` DNS/CloudFront Changes)

## Requirement

Attendees who already left their email via the Tuesday or Thursday QR code must receive a **direct PDF download link** with **no Maven email gate**, and without making any DNS or CloudFront changes for `datatalks.club`.

## Active Hosting: `alexeygrigorev/research-dump` (Public GitHub Raw)

`alexeygrigorev/course-downloadables` is a private repository, so its raw URLs are not publicly accessible without GitHub authentication. `alexeygrigorev/research-dump` is public, requires zero new infrastructure and zero DNS/CloudFront changes for `datatalks.club`, and serves both PDFs directly over HTTPS with no Maven email gate:

- Tuesday PDF:
  `https://raw.githubusercontent.com/alexeygrigorev/research-dump/main/2026-11-21-workshop-followup/tuesday-full-stack-vibe-coding-kit/full-stack-vibe-coding-kit.pdf`
- Thursday PDF:
  `https://raw.githubusercontent.com/alexeygrigorev/research-dump/main/2026-11-21-workshop-followup/thursday-agentic-quality-control-kit/agentic-quality-control-android-kit.pdf`

(If `alexeygrigorev/course-downloadables` is made public later, or if Orin prefers `aishippinglabs.com`, the same kit directories can be mirrored there.)

## Alternative Option: `aishippinglabs.com` Static Downloads

If Orin prefers hosting on `aishippinglabs.com` instead of GitHub:

- Place the PDFs under `static/downloads/2026-11-berlin/` in `AI-Shipping-Labs/website`:
  - `https://aishippinglabs.com/downloads/2026-11-berlin/full-stack-vibe-coding-kit.pdf`
  - `https://aishippinglabs.com/downloads/2026-11-berlin/agentic-quality-control-android-kit.pdf`
- This also avoids any `datatalks.club` DNS or CloudFront changes while keeping analytics under `aishippinglabs.com`.

## What NOT to Use

- Do not put `recorder.google.com` links on any public page or email.
- Do not put the PDFs behind a Maven email gate for people who already submitted their email at the workshop/talk.

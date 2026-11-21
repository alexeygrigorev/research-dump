# PDF Hosting Plan (Public Direct URLs, No `datatalks.club` DNS/CloudFront Changes)

## Requirement

Attendees who already left their email via the Tuesday or Thursday QR code must receive a **direct PDF download link** with **no Maven email gate**, and without making any DNS or CloudFront changes for `datatalks.club`.

## Recommended Option: `alexeygrigorev/course-downloadables` (GitHub Raw)

1. Add the two kit directories (`tuesday-full-stack-vibe-coding-kit/` and `thursday-agentic-quality-control-kit/`) to the public `github.com/alexeygrigorev/course-downloadables` repository (alongside `idea-to-production-kit/` and `coding-agent-setup-kit/`).
2. Use the direct GitHub raw URLs (zero new infrastructure, zero DNS/CloudFront changes, instant HTTPS download):
   - Tuesday PDF:
     `https://github.com/alexeygrigorev/course-downloadables/raw/main/tuesday-full-stack-vibe-coding-kit/full-stack-vibe-coding-kit.pdf`
   - Thursday PDF:
     `https://github.com/alexeygrigorev/course-downloadables/raw/main/thursday-agentic-quality-control-kit/agentic-quality-control-android-kit.pdf`

## Alternative Option: `aishippinglabs.com` Static Downloads

If Orin prefers hosting on `aishippinglabs.com` instead of GitHub:

- Place the PDFs under `static/downloads/2026-11-berlin/` in `AI-Shipping-Labs/website`:
  - `https://aishippinglabs.com/downloads/2026-11-berlin/full-stack-vibe-coding-kit.pdf`
  - `https://aishippinglabs.com/downloads/2026-11-berlin/agentic-quality-control-android-kit.pdf`
- This also avoids any `datatalks.club` DNS or CloudFront changes while keeping analytics under `aishippinglabs.com`.

## What NOT to Use

- Do not put `recorder.google.com` links on any public page or email.
- Do not put the PDFs behind a Maven email gate for people who already submitted their email at the workshop/talk.

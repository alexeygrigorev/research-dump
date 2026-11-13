# The site and the signup pipeline

**13 November 2026.** How academy.datatalks.club is built, where signups go, and how it connects to the existing survey form. Request: t3290u.

## What exists

| Part | Where | Notes |
|---|---|---|
| Site source | [DataTalksClub/academy](https://github.com/DataTalksClub/academy) | Astro, static output, GitHub Pages. Spec with all copy and design decisions: [`docs/SPEC.md`](https://github.com/DataTalksClub/academy/blob/main/docs/SPEC.md) |
| Pages | `/` (both tracks, random order), `/agentic-engineering/`, `/ai-engineering/`, `/privacy/`, `/impressum/` | The two track pages come from one template and differ only in track data |
| Signup API | [DataTalksClub/aws-infra `main/academy`](https://github.com/DataTalksClub/aws-infra/tree/main/main/academy), merged in [PR #141](https://github.com/DataTalksClub/aws-infra/pull/141) | Lambda `academy-signup-api` behind a Function URL, DynamoDB table `academy-signups`, main AWS account, eu-west-1 |
| DNS | `main/website-static/dns.tf`, key `academy_cname` | CNAME `academy.datatalks.club` to `datatalksclub.github.io` |

## Why this setup

- **A static site on GitHub Pages**: nothing to operate, free, fast, and the DataTalks.Club docs already run this way.
- **Our own small API instead of an existing list endpoint.** I checked the existing systems first:
  - Relay (the DataTalks.Club mailing system) has a public subscribe endpoint, and the datatalks.club newsletter form uses it. It accepts only an email address. It cannot store the chosen track or the link tags, which this test needs.
  - The DataOps portal has no public signup endpoint, and its CRM is for sponsors.
  - The Google Form cannot be made to require an email from outside, and it does not record where a visitor came from.
- **No cookies, no pixels, no third-party requests.** The site can run in Germany without a consent banner, and both pages are measured the same way.

## Signup flow

```
ad or post (link with utm tags)
  -> landing page (page view counted: date, page, source, campaign, creative)
  -> email field, required -> POST /signup
       stored: email, track, time, first utm_source/medium/campaign/content/term,
               referring page, page, browser language, consent text version
  -> success panel
       two optional one-tap questions (where based, how to pay) -> stored on the same record
       "Take the survey" -> the existing Google Form, with track and email prefilled
```

Not stored: IP address, browser details. A hidden honeypot field drops simple bots. Test addresses (`@example.com`, or `+academytest` before the @) are flagged.

## The existing survey form

The 13 November announcement links to a Google Form survey. It asks whether the person can be contacted, but the email question is optional, so people agreed to be contacted and left no address.

What changed with the site:

1. **The email comes first.** A visitor joins a shortlist with an email before anything else. The survey is the second step, not the first.
2. **The survey is prefilled.** The "Take the survey" button opens the form with the track (question 1) and the email (last question) already filled in, so a survey answer can be matched to a shortlist signup by email.
3. **From now on, posts and ads link to academy.datatalks.club**, not to the form.

Two changes only Alexey can make, in the form's editor:

- Make "What's your email address?" **required**, or turn on "Collect email addresses". Today it is optional, with the help text "Leave your email only if you agreed to a follow-up".
- Add the academy link to the form's confirmation message, for people who still arrive at the form directly: `https://academy.datatalks.club/?utm_source=survey&utm_medium=referral&utm_campaign=track-test-2026-11`.

The prefill depends on the form's field ids (`entry.1984241375` for the track, `entry.1840392648` for the email). If the questions are deleted and recreated, the ids change and the link in the site's `SignupForm` has to be updated. Editing the question text does not change them.

## Getting the data out

In a checkout of aws-infra, with AWS credentials for the main account:

```bash
python main/academy/scripts/export_signups.py > signups.csv     # --include-tests to see test rows
python main/academy/scripts/pageviews.py > pageviews.csv
```

`signups.csv` has one row per email and track: time, email, track, link tags, referring page, page, answers. `pageviews.csv` has daily counts per page, source, campaign and creative. The [promo plan](promo-campaign-plan.md#result-table) says how to read them.

To delete one person's data, see the README in `main/academy`.

## Open points

1. **Double opt-in before the first mailing.** The site stores a signup when the form is submitted, with the consent text version and the time. German practice expects a confirmation email (double opt-in) as proof of consent before marketing mail ([research, legal notes](landing-page-research.md#4-legal-notes-for-germany)). Relay supports this. Before the first email to the shortlist: import the signups into a Relay audience with the track as a tag and send Relay's confirmation email, then mail only confirmed addresses. This needs a Relay client and key for the academy, which an operator has to create.
2. **The survey form's email question** is still optional (see above).
3. **The Hub repository registry** does not list DataTalksClub/academy yet. The worker credential of this session is not allowed to edit the registry.
4. **Photo and proof.** The instructor photo is the one from datatalks.club. A photo of the actual room, once it is confirmed, would be a stronger image for the page and the ads.
5. **German version.** The pages are in English because the teaching is in English. A German page for advisers and for search ads on German keywords is a possible second step.

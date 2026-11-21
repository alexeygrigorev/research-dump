# Step 1: Spec and Frontend

We start with product behavior rather than database tables or frameworks. When you give an agent a vague prompt, it fills in missing details with guesses. A focused specification keeps the UI and API aligned from the start.

## Write the product specification

I use ChatGPT to brainstorm the scope and save the result to `specs.md` at the repository root. Remove any premature implementation details from `specs.md` before generating the UI so the frontend builder focuses on user flows instead of backend connections.

```text
I want to build a team lunch restaurant-picker app where teammates suggest places and vote.

Help me set the scope for this project precisely. Focus on product behavior, user flows, and UX rather than implementation details.

Ask me one question at a time and keep your output short.
```

## Generate the UI and remove Supabase

Next, paste `specs.md` into Lovable so you get sensible React, Tailwind CSS, and component defaults without designing from scratch. Export the result to GitHub, then pull it into `frontend/`.

Lovable often adds Supabase authentication and storage even when you plan to write your own backend. Strip it out and replace it with a single-file mock backend so the frontend runs standalone.

```text
Remove Supabase. Simplify authentication to login and password, and create a mock backend concentrated in one single file so the frontend runs standalone.
```

Install dependencies and start the Vite dev server to verify the UI locally:

```bash
cd frontend
npm install
npm run dev
```

If npm reports a peer-dependency conflict, run `npm install --legacy-peer-deps` instead.

## Fix layout friction with three options

During testing, clicking to add a restaurant pushed other elements down and broke the page flow.

Instead of tweaking CSS blindly, commit your working state and ask a fresh session or subagent for three layout alternatives:

```text
When I interact with the page, adding items pushes other elements down and breaks the layout.

Commit what we have, then propose 3 different layout options so I can pick the cleanest UX.
```

Pick the option that reads best, remove the unused variants from the code, and commit before moving to the backend.

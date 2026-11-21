# Step 1: Spec and Frontend

We start with product behavior rather than database tables or frameworks. When you give an agent a vague prompt, it fills in missing details with guesses. A focused specification keeps the UI and API aligned from the start.

## Run a product discovery interview

I use ChatGPT to brainstorm the scope. I don't write the spec myself: I give the model a one-sentence idea and let it interview me. The app for this workshop is "Where Should We Eat?", a collaborative restaurant voting app with ranked-choice voting, a countdown, and live results.

```text
Where Should We Eat?

A collaborative restaurant voting app with ranked-choice voting, a countdown, and live results.

I want to help you figure out what we want to build - this is an idea and I want to make it more concrete before I build it. Ask me as many questions as you like but keep them short and ask one question at a time
```

Keep your answers short. ChatGPT asks about the audience (coworkers), frequency (daily), who can suggest restaurants (anyone, plus a pre-filled list of known places), how people join (a permanent team and a shared link), when voting opens and closes (8:00 and 11:30, started automatically every workday), how to vote (rank the top 3), and whether results and voters are visible (yes to both).

After about a dozen questions I stop answering one by one and hand over the rest:

```text
visible. make the rest of the choices for me
```

ChatGPT returns a full MVP spec: a mobile-first web app with teams and invite links, 3/2/1 Borda-style points with tie-breakers, edge cases (no votes means no winner, late coworkers can see the result but can't vote), a list of what to leave out of v1, and a definition of success: 5 to 20 coworkers rank their top three in under 15 seconds and have a decision at 11:30.

## Challenge the spec before you build

Read the proposal and object where the UX feels wrong. The first version asked people to drag restaurants into order. I wasn't sure that works with many choices:

```text
I'm not sure if dragging will be user friendly if we have many choices
```

ChatGPT agreed, because dragging through 20 or 30 restaurants on a phone is frustrating, and changed the interaction to tapping a restaurant to add it to your top 3, with search and "Recently visited" and "Popular with the team" sections. This costs one message now and saves a UI rewrite later.

## Write the product specification

Once the decisions look right, ask for the file:

```text
now please prepare detailed specification file that I can give to my coding agent. save it to specs.md
```

Save the result to `specs.md` at the repository root. The generated spec also chose a technology stack (Next.js, Supabase, Vercel) and a database schema. Remove that premature implementation detail from `specs.md` before generating the UI so the frontend builder focuses on user flows instead of backend connections. We pick the backend ourselves in the next steps.

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

---
name: pitch-deck-content
description: >
  Write the NARRATIVE for an investor or sales pitch deck — what each slide says,
  in what order, and why. Outputs slide-by-slide content (titles, body, supporting
  facts, the implied "next slide" hook). Pairs with `slides` for the HTML/visual
  layer or `design`/`gamma` for AI-assisted production.
  Use when raising a round, pitching a partnership, or refining an existing deck
  that "doesn't land".
  Triggers: "pitch deck", "investor deck", "fundraising deck", "seed deck",
  "Series A deck", "sales deck content", "deck narrative", "deck story",
  "make my deck better", "what should each slide say".
  NOT for visual design (use slides/design) and NOT for short presentations
  (talks, internal updates — those are different formats).
---

# Pitch Deck Content

Decks fail on narrative, not design. A beautiful deck with a flat story raises nothing. A handmade-PowerPoint deck with a sharp narrative raises rounds.

The job here is the narrative — what each slide says, in what order, and how each one earns the next.

## Inputs you need

- **Audience**: investor (seed/A/B/growth) / strategic partner / enterprise sales prospect
- **Stage**: pre-revenue / pre-seed / seed / Series A+ — affects what slides exist
- **The ask**: $ raising, # months runway, valuation cap (for investor decks)
- **Traction**: real numbers — revenue, users, retention, growth rate, signed LOIs
- **The thesis**: in one sentence, what you believe about the world that competitors don't
- **The team**: why specifically YOU vs anyone else doing this

If thesis or traction is vague → ask before drafting. Vague decks lose rounds.

---

## The 12-slide investor narrative (the only structure that works)

```
1.  Title           — Company, tagline, ask
2.  Problem         — Specific pain. NOT a category.
3.  Why now         — The non-obvious shift that makes this inevitable now
4.  Solution        — One sentence + a screenshot or GIF
5.  How it works    — 3-step diagram, in user terms
6.  Market          — TAM/SAM/SOM with bottom-up math, not "$1T market"
7.  Traction        — Most concrete numbers you have, charted
8.  Business model  — How you make money, unit economics if you have them
9.  Go-to-market    — Specifically how you acquire customer #1, #100, #10000
10. Competition     — Honest map, why you win in your wedge
11. Team            — Why this team, this problem, this moment
12. The ask         — $ raised, what it buys, milestones it unlocks
```

Optional add-ons (only if they strengthen — kill if they pad):
- Vision/long arc (after slide 11, before ask)
- Roadmap (only if traction is thin and roadmap shows credibility)
- Use of funds detail (slide 12 expansion if the round is large)

---

## What each slide must do

### 1. Title
- Company name + 6-word positioning ("[Brand] is [category] for [buyer]")
- The ask line: "Raising $[X]M to [unlock specific milestone]"
- One image, one logo, no clutter
- Goal: orient the reader in 3 seconds

### 2. Problem
- One sentence of the problem, **specific to one named persona**
- One concrete cost (time, money, opportunity) of the problem TODAY
- One quote or stat from the buyer in their own words
- Goal: make the investor feel the pain
- ❌ "Healthcare is broken" → ✅ "ER nurses spend 47% of a 12-hour shift charting instead of with patients"

### 3. Why now
- The non-obvious shift (regulation, behavior, tech, cost curve) that makes this winnable in the next 5 years
- 1-2 supporting data points
- Goal: answer "why didn't someone solve this 5 years ago / why won't they solve it next year"

### 4. Solution
- ONE sentence: "[Product] is [category] that [outcome] by [mechanism]"
- A screenshot or 3-second GIF of the actual product in use
- Goal: make the solution feel real (not a deck-only company)

### 5. How it works
- 3 steps, named in user-language
- Each step: 1 line + 1 visual
- Goal: prove the mechanism is buildable, not magic

### 6. Market
- TAM via bottom-up: [# of buyers] × [annual spend] = $X
- SAM: who you can realistically reach
- SOM: who you can credibly close in the next 3 years
- ❌ "$1T healthcare market" → ✅ "12,000 mid-market US clinics × $40k/yr ACV = $480M SAM"
- Goal: make the math defensible, not hopeful

### 7. Traction
- Most concrete numbers, in a chart with axes labeled
- "Up and to the right" with a real Y-axis
- 1-2 standout customer stories (logo + outcome)
- Retention or NRR if you have it (this is the slide that closes rounds)
- ❌ "Significant growth" → ✅ "$8k → $52k MRR in 7 months, 119% NRR"

### 8. Business model
- How you charge (unit, frequency)
- Current pricing
- LTV / CAC / payback if computable
- Goal: prove this is a business, not a science project

### 9. Go-to-market
- Specifically: where does customer #100 come from? (channels, named partners)
- What's working today (1-2 channels) vs what's hypothesis (others)
- Goal: prove distribution, not just product

### 10. Competition
- 2×2 positioning map with axes the BUYER cares about (use `competitor-analysis`)
- Honest about who's adjacent
- ONE-line "we win in this wedge because [unfair advantage]"
- Goal: prove you've done the homework, not that you have no competitors

### 11. Team
- 3-4 most relevant people: photo + name + 1 line of why-this-team-this-problem
- Prior wins / domain expertise / network
- Goal: investor leaves thinking "I'd back these people on whatever they did next"

### 12. The ask
- $ raising
- Milestones the round unlocks (be specific — revenue, users, hires)
- Use of funds (high-level: % to engineering, sales, etc.)
- Optional: lead investor sought / committed
- End on the email + calendly, NOT "thank you"

---

## The narrative thread

Every slide must answer one question AND raise the next. If a slide doesn't make the investor think "OK, but what about [X]?" — and the next slide doesn't answer that X — your deck is a list, not a story.

The implicit thread for investors:
- Slide 2 makes them feel pain → "is this a real problem?"
- Slide 3 answers → "is now actually the moment?"
- Slide 4 answers → "do they have a real solution?"
- Slide 5 answers → "is it buildable?"
- Slide 6 answers → "is the market big enough?"
- Slide 7 answers → "are users actually using it?"
- Slide 8 answers → "is it a business?"
- Slide 9 answers → "can they actually grow it?"
- Slide 10 answers → "what about competitors?"
- Slide 11 answers → "is this team the right team?"
- Slide 12 answers → "what do they need from me?"

Every slide that doesn't answer the implicit next question is wasted.

---

## Output format

Deliver in this order:

```
# Pitch Deck — [Company]
Audience: [investor stage / partner / sales prospect]
Stage: [...]
Ask: [$X for Y]
Thesis (1 sentence): [...]

## Slide 1: Title
**Title:** [...]
**Subtitle / ask line:** [...]
**Visual direction:** [...]

## Slide 2: Problem
**Title:** [...]
**Body:**
- [...]
- [...]
**Supporting fact / quote:** [...]
**Visual direction:** [...]
**Implicit next question:** [What does the investor now want to know?]

[Repeat for slides 3-12]

## Speaker notes (per slide)
[2-3 sentences for the spoken delivery — punchy, no jargon, never read off the slide]

## Open questions
[Anything the user needs to fill in: numbers, screenshots, missing inputs]

## Suggested cuts
[Which slides could be killed if you need to compress to 8-10]
```

---

## Anti-patterns

1. **"We are excited to introduce…"** — banned. Cut.
2. **Vague problems** — "small businesses struggle" is not a problem. Name the pain.
3. **TAM = "$10T market"** — top-down number means nothing. Bottom-up or cut.
4. **Logo soup with no commentary** — 8 logos with no story = "we did some pilots". Show 2 with outcomes instead.
5. **Roadmap as traction substitute** — investors fund evidence, not promises
6. **Honesty-free competition slide** — "We have no real competitors" = you don't understand the market
7. **Team slide that lists job history** — list relevance, not resumes
8. **No clear ask** — vague ask = vague yes. Be specific.
9. **More than 15 slides** — you've lost them
10. **Reading the slide aloud** — speaker notes should NEVER duplicate the slide text
11. **Stock photos** — investors notice; cut them
12. **No traction slide** — if you don't have traction, name what you DO have (signed LOIs, waitlist, design partner) instead of inflating

---

## Length variants

- **Send-ahead (read-without-presenter)**: 14-16 slides, more dense text
- **In-person (with presenter)**: 10-12 slides, sparse text, more visuals
- **Memo (no deck)**: 5-page memo with same narrative arc — increasingly common at top funds

---

## Pair with

- `competitor-analysis` — drives the competition slide
- `customer-research` — drives the problem + solution slides
- `storytelling-framework` — for the founder/origin slide
- `slides` — for the HTML/visual implementation
- `design` — for Gamma-style fast generation OR custom illustration
- `case-study-writer` — for the traction slide proof story

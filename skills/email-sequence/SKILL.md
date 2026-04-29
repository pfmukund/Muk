---
name: email-sequence
description: >
  Write multi-email sequences that actually get opened, read, and converted —
  welcome, nurture, cold outbound, post-purchase, and re-engagement (win-back).
  Use when you need 3+ emails that work as a sequence, not isolated sends.
  NOT for single transactional emails — write those in-context. NOT for newsletters
  (use a newsletter skill if one exists).
  Triggers: "welcome sequence", "nurture sequence", "drip campaign", "cold email sequence",
  "win-back emails", "onboarding emails", "abandoned cart sequence",
  "follow-up sequence", "post-purchase emails", "re-engagement campaign".
---

# Email Sequence Writer

Write sequences that read like one human writing to another. The whole game is making the next email get opened — and that's earned by what came before.

## Inputs you need first

If any are missing, ask ONE question to get them. Don't fake it.
- **Buyer**: who they are (job, life stage, biggest pain right now)
- **Product**: what it is in one sentence + the *one* outcome it delivers
- **Brand voice**: tone (formal/casual), 3 banned words, 3 signature phrases
- **Sender**: real human name + role (sequences from "the team" underperform 30-50%)
- **Goal of the sequence**: book a call / use the product / refer / buy

---

## Sequence types

### A. Welcome / onboarding (5 emails over 14 days)
Goal: get them to the *first value moment* in the product.

| # | Day | Subject pattern | Purpose |
|---|---|---|---|
| 1 | 0 | "Welcome to [thing] — start here" | Deliver promise + 1 next action |
| 2 | 1 | "The mistake I see new [users] make" | Frame the problem they don't know they have |
| 3 | 4 | "How [Customer X] got [outcome] in [time]" | Specific proof story |
| 4 | 8 | "What's stopping you?" | Soft objection-handler, reply-prompt |
| 5 | 14 | "Quick check-in" | Last nudge before deactivating sequence |

### B. Nurture (6-8 emails over 4-8 weeks)
Goal: keep them warm until they're ready, build authority + trust.

Pattern per email: 1 specific story + 1 lesson + 1 soft CTA. Never sell hard.
Cadence: weekly. Anything tighter feels like spam, anything looser feels like a stranger.

### C. Cold outbound (3-touch sequence)
Goal: get a reply. NOT to close. Closing happens in the reply thread.

| # | Day | Length | Hook |
|---|---|---|---|
| 1 | 0 | 3-5 sentences | Specific observation about *them* + 1-line reason for outreach + 1 question |
| 2 | 3 | 2 sentences | Bump w/ extra context (article, case study) |
| 3 | 7 | 1 sentence | "Should I close the loop here?" — break-up email, often wins replies |

**Cold outbound rules:**
- Subject line: <40 chars, lowercase, looks like a colleague wrote it
- First line: about THEM, not you ("Saw your team launched X" beats "I'm reaching out from Y")
- Never send the second email as a reply to the first thread without new info
- No links in email 1 — kills deliverability + trust

### D. Post-purchase (4 emails over 30 days)
Goal: reduce buyer's remorse, drive first use, lay groundwork for upsell/referral.

| # | Day | Purpose |
|---|---|---|
| 1 | 0 | Receipt + reassurance ("you made the right call because…") + first action |
| 2 | 2 | "Here's what most new customers do in week 1" |
| 3 | 14 | Check-in on outcome — invite reply with friction or wins |
| 4 | 30 | Story of a long-term customer + soft referral / next-tier ask |

### E. Re-engagement / win-back (3 emails over 14 days)
Goal: re-activate dormant users OR cleanly remove them from list.

| # | Day | Tone |
|---|---|---|
| 1 | 0 | "We miss you" — warm + 1-click reactivation + low-friction offer |
| 2 | 7 | "What changed?" — direct ask, reply-prompt |
| 3 | 14 | "Last email from us" — clean break, opt-back-in link, then unsubscribe |

---

## Subject line formulas (use, don't guess)

| Formula | Example |
|---|---|
| Specific number + outcome | "How we got 312 signups in 9 days" |
| Question hook | "Are you making this React mistake?" |
| Curiosity gap | "The unfair advantage we almost killed" |
| Personal/casual | "quick one" / "found this for you" |
| Pattern interrupt | "I was wrong" / "we screwed up" |
| Direct ask | "5 minutes Thursday?" |

**Banned subject patterns:**
- "Following up" / "Just checking in" / "Circling back"
- ALL CAPS or all-emoji
- Anything that reads like a marketing template
- Promises you don't deliver in the body

---

## Email body structure (every email)

```
[Hook — 1-2 sentences. Earn the next sentence.]

[Body — story, lesson, or value. ONE idea per email.]

[CTA — ONE link. Not three. The one thing you want them to do.]

[Sign-off — real human name, optional 1-line context]

P.S. [Optional. P.S. lines have ~80% read rates — use for the most important nudge.]
```

**Length:**
- Cold: <120 words
- Welcome: 150-300 words
- Nurture: 200-500 words
- Win-back: <100 words

---

## Output format

Deliver the full sequence as a single artifact:

```
# [Sequence name] — [type]
Audience: [one line]
Goal: [one line]
Cadence: [day X, day Y, …]

---

## Email 1 — Day 0
**Subject:** [subject]
**Preview text:** [40-90 chars]

[Body]

— [Sender name]
[Optional P.S.]

---

## Email 2 — Day [X]
…
```

For each email also note:
- Why this email exists in the sequence (1 line)
- The single CTA + where it links to
- The one metric to watch (open rate / reply rate / click rate)

---

## Anti-patterns (instant rewrite)

1. **"I hope this email finds you well"** — delete. Always.
2. **Three CTAs in one email** — pick one. The others are next email's job.
3. **Generic "Hi [First Name]"** — pair the name with a specific observation, or skip it.
4. **"Just bumping this to the top of your inbox"** — never. Add new info or break up.
5. **No P.S.** on cold/win-back — wasted real estate.
6. **Selling in email 1 of nurture** — you haven't earned it yet.
7. **Subject lines that lie** about the body — kills the next 5 sends.
8. **Same sign-off every email** — vary it. "Talk soon" / "Good luck this week" / "More soon" beat "Best,".
9. **Sending from "team@"** — use a real human, even if pen-name. Replies double.
10. **Sequence with no exit** — every sequence needs a "they replied" branch and an "unsubscribe" branch.

---

## Pair with

- `brand-voice-generator` — to lock the voice before writing
- `landing-page-copy` — sequences usually drive to a landing page; voice must match
- `customer-research` — feeds the buyer / pain inputs above
- `case-study-writer` — provides the proof emails (#3 in welcome, #4 in post-purchase)
- `conversion-optimization` — pressure-test the sequence's call-to-actions before launch

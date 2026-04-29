---
name: customer-research
description: >
  Plan, run, and synthesize customer interviews — outputs an interview script,
  a synthesis framework, and a deliverable persona/JTBD doc. Built around
  The Mom Test rules (talk about their life, not your idea) and Jobs-To-Be-Done
  (when ___, I want to ___, so I can ___).
  Use BEFORE building, before pricing, when stuck on positioning, when conversion
  is low, or when you suspect you've been talking to yourself.
  Triggers: "customer research", "user research", "customer interviews",
  "user interviews", "discovery calls", "research questions", "interview script",
  "talk to customers", "validate this", "JTBD", "jobs to be done", "personas",
  "synthesize interviews", "customer insights".
  NOT for quantitative survey work (different methodology — surveys lie, interviews
  reveal — but a related skill could exist for that).
---

# Customer Research

Most customer research is broken because founders ask leading questions and customers lie politely. The Mom Test fixes this: talk about their life, not your idea.

## Three modes

The skill operates in three modes — pick one or do all three in sequence:

### Mode A: Plan
Output: interview script + recruiting message + screening criteria

### Mode B: Execute
Output: live interview guidance + question reservoir + how to handle common moments

### Mode C: Synthesize
Output: themes + JTBD statements + persona doc + go-do list

If user just says "customer research", default to A → B → C. Otherwise, target the mode they asked for.

---

## Inputs you need

- **What you want to learn** — the actual question driving this research (not "everything")
- **Who you're talking to** — segment + role + life-stage specificity
- **How many interviews** — minimum 5 per segment to spot patterns; 8-12 ideal
- **Format** — 30-min Zoom is the default; in-person better when possible
- **Stage** — pre-product (problem discovery) / pre-launch (solution validation) / post-launch (positioning + retention)

If "what you want to learn" is fuzzy, sharpen it FIRST. Bad research questions produce useless data.

---

## Mode A: Plan

### Sharpen the research question

❌ "Do users want feature X?" — leading, asks about future opinions
✅ "What did users actually do last time they faced [the problem we're targeting]?"

❌ "Would you pay $X for Y?" — hypothetical, will be lied about politely
✅ "Walk me through the last time you spent money on [adjacent thing]. What made you decide?"

### The Mom Test rules (read every time before drafting)

1. **Talk about their life, not your idea.** Don't pitch. Don't even mention what you're building until the very end (and only if necessary).
2. **Ask about specifics in the past, not opinions about the future.** Past behavior > stated preference.
3. **Talk less, listen more.** Aim for 80% them, 20% you. Silence is your friend.

### Question reservoir (steal from these)

**Problem discovery (pre-product):**
- "Walk me through the last time you [did the relevant activity]."
- "What was the most frustrating part of that?"
- "What did you do about it? What did you try first? What did you try after that didn't work?"
- "How much time/money did that cost you?"
- "Why was that important enough to deal with?"
- "Who else has this problem? How is theirs different from yours?"

**Solution validation (pre-launch):**
- "When did you first realize you needed something like this?"
- "What did you almost buy / try instead?"
- "What stopped you?"
- "If this didn't exist, what's the hack you'd build?"

**Positioning + retention (post-launch):**
- "How would you describe what we do to a colleague?"
- "If we shut down tomorrow, what would you switch to?"
- "When do you NOT use us, even though you could?"
- "What did you expect that didn't happen?"
- "What surprised you about using us?"

**The unlock questions (use sparingly):**
- "What's a question I should be asking that I'm not?"
- "Who else should I talk to about this?"
- "If I could wave a magic wand and fix one thing about [the broader thing], what would it be?"

### Recruiting message template

```
Subject: [specific topic] — would love your perspective

Hi [name],

Working on understanding [specific problem area] for [audience].
Could I borrow 25 minutes of your time on Zoom this week?
No pitch — I just want to learn from how you handle [problem].

Happy to share findings if useful.

— [Name]
```

Why it works: specific, time-bounded, no pitch, mutual benefit.

### Screening criteria
List 3 criteria for "yes" interviews. Strongly de-prioritize warm friends — they will lie politely. Strangers tell the truth.

---

## Mode B: Execute

### Before the call (5 min)
- Re-read your research question
- Re-read the Mom Test rules
- Have ONE concrete question to open with — never "tell me about yourself"

### Opening (2 min)
"Thanks for the time. I'm trying to understand how people handle [X] today. I'll ask about your specific experience — there's no wrong answer. Mind if I record?"

### The middle (20 min) — the work
- Open with the most specific past-behavior question you have
- For every answer, ask "tell me more" or "what happened next" or just stay quiet
- When they share an opinion about your idea, redirect to behavior
- Listen for emotion words — those are the real signal

**Watch-outs:**
- They start asking YOU questions → answer briefly, redirect with "But I'm curious — when you faced [X]…"
- They start politely agreeing → they're done telling the truth; ask a contrarian probe ("What about it sucked?")
- You feel the urge to pitch → don't. The pitch is a different call.

### Closing (3 min)
- "What's the question I should be asking that I'm not?"
- "Who else should I talk to?"
- "Can I follow up if I have one more question?"

### After the call (5 min)
- Write down 3 most surprising quotes IN THEIR WORDS (verbatim)
- Write down what you got wrong about your assumption
- Tag the call with theme labels for synthesis

---

## Mode C: Synthesize

After 5+ interviews, look for patterns. Don't synthesize earlier — small samples lie.

### The synthesis framework

**Step 1: Quote bank**
Pull every meaningful quote into a single doc. One quote per row.
Columns: quote / interviewee / theme tag / pain or gain / [field for "is this a fact or interpretation"]

**Step 2: Theme clustering**
Group quotes by theme. A theme exists when you see it in 3+ interviews. Single-interview "themes" are noise.

**Step 3: JTBD statements**
For each theme, write a Job-To-Be-Done statement:
> "When [situation], I want to [motivation], so I can [expected outcome]."

E.g. "When I'm starting a project from scratch, I want to know which design tokens to define first, so I can avoid rebuilding the foundation later."

JTBDs are stable across personas and time — they're better strategic anchors than personas.

**Step 4: Persona (optional, lightweight)**
Don't write a 5-page persona doc. Write:
- Name + 1-line role/context
- 3 quotes that define them
- 3 jobs they're trying to get done
- 3 alternatives they've already tried
- 1 thing that would make them buy today

### Output: the research deliverable

```
# Customer Research — [Topic]
Date: [yyyy-mm-dd]
Interviews: [N], across [segments]
Research question: [the one you set out to answer]

## TL;DR
[3 sentences: the answer + the surprise + the implication]

## Top 5 themes
For each:
- Theme name
- Quotes (verbatim, with attribution)
- How many interviewees said this
- JTBD statement
- Implication for [product / pricing / messaging / GTM]

## Patterns we DIDN'T see (and expected to)
[Negative findings — the absence of expected themes is data]

## Personas (lightweight)
[1-page max per persona]

## Pricing signals
[What people actually pay for adjacent things, what their budget process is]

## Alternatives we lose to
[Top 3 — including "do nothing" if it shows up]

## Open questions for round 2
[What we'd ask next]

## 5 actions to take this week
[Concrete moves driven by the research — not "consider..." but "do X by Friday"]
```

---

## Anti-patterns

1. **Pitching during the interview** — you're now selling, not learning
2. **Asking about the future** — "would you pay" is worthless data
3. **Closed-ended questions** — yes/no kills the signal
4. **Interviewing only friends/customers** — biased toward yes
5. **Synthesizing after 2 interviews** — sample size lies
6. **Filling silence** — silence makes them keep talking; let it sit
7. **Treating opinions as facts** — "I would totally use that" is opinion; "Last week I paid $X for [adjacent thing]" is fact
8. **No quote bank** — without verbatim, your synthesis is your projection
9. **Persona without JTBD** — describes who, doesn't tell you what to ship
10. **Research with no actions output** — research that doesn't change behavior was the wrong research

---

## Pair with

- `competitor-analysis` — informs which alternatives to probe in interviews
- `offer-creation` — pricing signals from research feed offer design
- `landing-page-copy` — verbatim quotes become the most powerful copy you can write
- `case-study-writer` — interview happy customers → case study output
- `decision-framework` — when research surfaces a hard decision
- `growth-strategy` — research drives where to focus the 30-day move

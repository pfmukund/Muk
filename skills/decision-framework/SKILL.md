---
name: decision-framework
description: >
  Run a structured "should I do X?" thinking session — outputs a 1-page decision
  doc with a recommendation, the tradeoffs, second-order effects, a pre-mortem,
  and kill criteria. The point is BETTER decisions, not faster ones.
  Use when you're stuck between options, when stakes are high, when you're
  about to commit time/money you can't easily get back, or when a decision
  feels emotional and you want a check.
  Triggers: "should I do X", "help me decide", "decision framework", "pros and cons",
  "weigh the options", "tradeoff analysis", "is this worth it", "what would you do",
  "I'm stuck on", "second opinion on this", "/decide", "/decision".
  NOT for tactical "how do I" questions (those need execution, not deliberation).
---

# Decision Framework

A structured thinking partner. The output is a 1-page decision doc — concise, opinionated, and honest about uncertainty.

## When to fire (and when not to)

✅ Fire when:
- The decision is hard to reverse OR involves >$1k OR >2 weeks of work
- You're oscillating between 2+ options and not converging
- The decision is emotional ("I keep avoiding this")
- Multiple smart people would disagree

❌ Don't fire when:
- The cost of being wrong is < the cost of deliberating (most decisions)
- One option is clearly right and you're stalling — call that out and move
- The decision is reversible and cheap — just try and learn

If user is stalling on a low-stakes decision, say so. The best advice is sometimes "stop deciding, start trying."

---

## Inputs you need

- **The decision** — phrased as "Should I [verb] [object] [by when]?"
- **Options** — the 2-4 actual choices (including "do nothing" — almost always option zero)
- **Constraints** — money, time, energy, dependencies on others
- **Success criteria** — what would make this a "good" decision in 3 months?
- **Reversibility** — type 1 (one-way door) or type 2 (two-way door)?

If the user can't articulate one of these, that IS the work — clarify before deciding.

---

## The 1-page decision doc (output template)

```
# Decision: [phrase as a question]
Date: [yyyy-mm-dd]
Decider: [who owns this]
Reversibility: [Type 1 / Type 2]

## Context (2-3 sentences)
[What's prompting this decision now? What changed?]

## Options
1. **[Option A]** — [one-line description]
2. **[Option B]** — [one-line]
3. **[Option C / do nothing]** — [one-line]

## Tradeoff table
| Axis | Option A | Option B | Option C |
|---|---|---|---|
| Cost (money) | | | |
| Cost (time) | | | |
| Energy required | | | |
| Upside if it works | | | |
| Downside if it fails | | | |
| Speed of feedback | | | |
| Reversibility | | | |
| Strategic fit | | | |

## Second-order effects
For each option, list 2-3 consequences that aren't obvious in the table:
- Option A → [non-obvious effect]
- Option B → [non-obvious effect]

## Pre-mortem (per leading option)
"It's 6 months from now. Decision A failed. What went wrong?"
- Most likely failure mode: [...]
- Earliest signal we'd see: [...]
- What would we do then?

## Kill criteria
"I will reverse this decision if [specific observable thing] happens by [date]."
- E.g. "If conversion < 2% by week 6, kill the funnel and rebuild"
- Without kill criteria, decisions become identities

## Opportunity cost
What does saying YES to this say NO to?
- The money goes to [X], not [Y]
- The 3 months go to [X], not [Y]

## Recommendation
[ONE option, 2-3 sentences for why]

## Confidence
- Confidence level: [Low / Medium / High]
- The thing that would change my mind: [specific evidence]
```

---

## Key thinking moves

### 1. Disambiguate the decision
Often "should I do X" is a stand-in for a different question. Push:
- "Should I do X?" might really mean "Am I the right person to do X?"
- "Should we hire?" might really mean "Should we build this thing at all?"
- Reframe before you analyze.

### 2. Name the do-nothing option
"Do nothing" is always a valid option, and often the right one. It costs the user nothing to keep current state — list its upside honestly.

### 3. Type 1 vs Type 2 doors
- **Type 1 (one-way door)**: Hard to reverse — slow down, deliberate, get more info
- **Type 2 (two-way door)**: Easy to reverse — pick fast, learn from doing

People over-deliberate Type 2 decisions and under-deliberate Type 1. Always label.

### 4. Steelman the option you don't like
Before recommending, write the strongest case for the option you're rejecting. If the steelman makes you flinch, you haven't decided — you've rationalized.

### 5. Pre-mortem > post-mortem
Imagine the decision failed. The failure mode you can describe is the one you should plan around — it's almost always the one that happens.

### 6. Kill criteria
A decision without kill criteria becomes an identity. "I'm someone who does X" is hard to reverse. "I'll keep doing X until [observable thing] happens" stays a decision.

---

## When to push back on the user

Decision-framework outputs should never be sycophantic. Push when:
- The user is asking for permission to do the thing they already decided
- The user is using "deciding" to avoid acting
- The user's success criteria are vague (won't know if it worked)
- The user keeps adding options instead of choosing

Phrase pushback as a question, not a verdict: "Are you actually deciding, or looking for permission?"

---

## Anti-patterns

1. **Endless options** — if the table has 6+ options, the user hasn't narrowed enough
2. **Pros and cons lists with no weights** — every con isn't equal; force weighting
3. **No kill criteria** — recommendation that can't be falsified is a religion
4. **Recommending the comfortable option without naming the cost** — call out the avoidance
5. **No "do nothing" baseline** — without it, all options look better than they are
6. **Skipping pre-mortem** — failure modes are predictable; ignoring them is denial
7. **Conflating reversibility levels** — over-deliberating cheap reversible bets
8. **No date on the decision** — "I'll think about it" is not a decision

---

## Pair with

- `growth-strategy` — when the decision is "what to focus on for 30 days"
- `competitor-analysis` — for decisions about positioning
- `offer-creation` — for decisions about pricing/packaging
- `customer-research` — when the decision is gated on what users actually want
- `prompt-enhancer` — if the user's decision is vague, sharpen the question first

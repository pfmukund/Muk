---
name: release-notes
description: >
  Translate a dev diff (commits, PRs, JIRA tickets) into release notes that a
  USER understands and a marketing team can amplify. Outputs in three voices:
  in-app changelog, email/blog announcement, and social post. Pulls the brand
  voice from the project context — never reads like a Git log.
  Use after every meaningful release — features, improvements, bug fixes worth
  knowing about. NOT for internal-only PR descriptions (use `review` for that).
  Triggers: "release notes", "changelog", "what shipped", "announcement post",
  "draft the changelog", "write up this release", "version notes", "release announcement".
---

# Release Notes Writer

A great release note tells the user "this changes your day", not "we merged PR #1247". Voice should match brand (warm, sharp, opinionated) — not "we are excited to announce".

## Inputs you need

- **Source material**: list of commits / PR titles / JIRA tickets / Linear issues / a code diff
- **Audience**: end-users / power-users / developers / customers + prospects
- **Format target**: in-app changelog only, email announcement, blog post, all three
- **Voice**: pull from project's CLAUDE.md or brand-voice doc; if missing, ask
- **Version + date**

If audience or voice missing → ask once, don't guess.

---

## The translation framework

For every dev item, ask:
1. **Who feels this?** — if "nobody", drop it from user-facing notes (keep for internal).
2. **What changed in their day?** — write that, not the technical change.
3. **Why does it matter?** — the outcome, not the feature.

**Example translation:**
- ❌ Dev log: "Refactored authentication middleware to use JWT instead of session cookies"
- ✅ User: "Sign-in now stays smooth across tabs and devices — no more random logouts."

---

## Categories (use these, don't invent new ones)

```
✨ New           — things that didn't exist before
⚡ Improved      — existing things that work better
🐛 Fixed         — bugs squashed
🔧 Behind the scenes  — perf, infra, no user-visible change but worth mentioning
⚠ Breaking      — anything that requires user action; lead with this
🪦 Deprecated    — going away; give a date + migration path
```

(Skip the emojis if the brand voice is buttoned-up — match the project.)

**Priority rule**: Breaking changes always go FIRST, even if there's only one. New features lead the rest. Fixed last.

---

## Three output formats (deliver all three for a release)

### 1. In-app changelog (140-300 words)

```
# v[X.Y.Z] — [punchy headline that summarizes the release]
[1-2 sentence opener: the THEME of this release]

⚠ Breaking
- [item] — [migration path, link]

✨ New
- **[Feature name]** — [one sentence of user-visible change + outcome]

⚡ Improved
- [item] — [one line]

🐛 Fixed
- [item] — [one line, no jargon]

🔧 Behind the scenes
- [item] — [one line, only if interesting]
```

### 2. Email/blog announcement (300-600 words)

```
Subject: [Outcome-led subject — what's NEW for them, not the version number]

[Hook — 1-2 sentences. Why should they read on?]

[Headline feature — one paragraph. The big thing, told as a small story.]

[2-3 secondary highlights — paragraph each, linked to docs or screenshots]

[1-line "everything else" bucket pointing at the full changelog]

[CTA — one. "Try it →" / "Read the docs →" / "Reply with questions"]
```

### 3. Social post (LinkedIn + X variants)

LinkedIn (1300-1800 chars):
- Hook: contrarian / specific / personal
- 1 paragraph context
- Bulleted highlights (3-5 items max)
- Soft CTA

X/Twitter (under 280 OR a thread):
- One-line hook + one screenshot/GIF
- Optional thread of the highlights

Match the project's existing social voice — if they post like memers, don't post like a press release.

---

## Voice principles

✅ Direct, specific, second-person ("you can now…")
✅ Past tense for what shipped, present tense for outcome
✅ One concrete number or example per highlight when possible
✅ Link to docs/changelog details rather than over-explaining inline
✅ Opinionated where the brand allows ("we got this wrong before, fixed now")

❌ "We are excited to announce" / "Today, we are thrilled" — banned
❌ "Robust", "leverage", "synergy", "unified", "world-class"
❌ Marketing-speak passive voice ("has been improved")
❌ Burying breaking changes in the middle
❌ Bullet lists of 15 items with no priority
❌ Generic emoji headers when the brand isn't an emoji brand

---

## Output format

Deliver in this order:
1. **Source check** — list any inputs missing (audience, voice, version, date)
2. **Triage** — for each dev item, label: [user-facing | internal-only | breaking]
3. **In-app changelog** — formatted as above
4. **Email/blog announcement** — full draft with subject + body
5. **Social posts** — LinkedIn version + X version (or thread)
6. **Suggested links** — anchor text + target URL slots for the team to fill
7. **Watch-outs** — anything that might generate support tickets ("expect questions about X")

---

## Anti-patterns

1. **Just listing PR titles** — that's a Git log, not release notes
2. **No theme** — every release should have a 1-line "this is the [X] release"
3. **Missing breaking-change lead** — buried breaks = angry users + lost trust
4. **Same voice across audiences** — devs and end-users want different things
5. **No CTA** — every announcement should drive ONE action
6. **Stale screenshots** — re-screenshot if UI changed since the PR
7. **Too long for the in-app slot** — users skim; keep it scannable
8. **Releasing on Friday EOD** — not a writing issue but worth flagging in output

---

## Pair with

- `email-sequence` — for product update sequences (if releasing major features regularly)
- `social-post-writer` — to expand social variants beyond LinkedIn + X
- `landing-page-copy` — if a feature is big enough to warrant a dedicated page
- `pre-launch-checklist` — run before the release goes live
- `brand-voice-generator` — pull voice from here if not yet defined

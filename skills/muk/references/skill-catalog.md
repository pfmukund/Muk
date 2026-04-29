# Skill Catalog — synced with `~/.claude/skills/` and built-in skills

Last synced: 2026-04-28. If a skill is added/removed from `~/.claude/skills/`, update this list.

## Engineering / Coding (custom)
- `frontend-architecture` — folder structure, state boundaries, data flow for a new feature/project. Use at feature START.
- `component-design` — design one React component's props/variants/state. Use when it'll be reused 3+ places.
- `performance-optimization` — LCP, bundle size, render thrashing, image payload, network waterfall. Measure first.
- `ui-styling` — shadcn/ui + Tailwind + canvas visuals. Dialogs, forms, tables, themes, dark mode.
- `micro-interaction-design` — button press / hover / loading / form feedback animations.
- `motion-design-system` — durations, eases, variants, stagger for a whole project.
- `design-system` — token architecture + slide generation + component specs.
- `design-system-builder` — colors, type, spacing, radius, shadow, motion tokens. Use at project start.
- `workflow-automation` — Claude Code hooks, scheduled agents, scripts. For tasks done 3+ times.
- `agent-creation` — design a new Claude Code subagent (system prompt, tools, routing rules).

## Writing / Content (custom)
- `brand-voice-generator` — start-of-project voice definition.
- `brand` — voice, visual identity, messaging frameworks, asset management.
- `landing-page-copy` — full landing page copy (hero / features / proof / FAQ / CTA).
- `ranking-content-writer` — full article/service page optimized to rank.
- `storytelling-framework` — About pages, case studies, founder stories.
- `email-sequence` 🆕 — welcome / nurture / cold / post-purchase / win-back sequences.
- `case-study-writer` 🆕 — customer story with arc + metrics + 3 length variants.
- `release-notes` 🆕 — translates dev diffs to user-readable changelog + announcement + social.
- `social-post-writer` 🆕 — platform-specific posts (LinkedIn / X / Threads / IG / TikTok).

## SEO (custom)
- `keyword-clustering` — start-of-SEO work, group keywords into pages.
- `seo-page-structure` — turn a cluster into a single-page outline.
- `ranking-content-writer` — write the prose after structure is set.

## Design / Visual (custom)
- `design` — logo (55 styles), CIP, slides, banners, icons, social images.
- `banner-design` — social/ad/hero/print banners across 22 styles.
- `slides` — HTML presentations w/ Chart.js + design tokens.
- `ui-audit` — conversion-focused critique, top 3-5 fixes.
- `ui-ux-pro-max` — 50+ styles, 161 palettes, 57 font pairings, 99 UX guidelines across 10 stacks.
- `accessibility-audit` 🆕 — WCAG 2.2 AA audit; distinct from ui-audit.
- `pitch-deck-content` 🆕 — investor/sales deck NARRATIVE (not visuals).

## Growth / Sales / Strategy (custom)
- `growth-strategy` — pick the ONE move that matters most in 30 days.
- `conversion-optimization` — raise conversion rate on existing traffic.
- `sales-optimization` — raise close rate on warm leads.
- `offer-creation` — design price / deliverables / bonus / guarantee / scarcity.
- `competitor-analysis` 🆕 — score 5 competitors on 8 axes; output positioning gaps.
- `customer-research` 🆕 — interview script + execution + JTBD/persona synthesis (Mom Test).
- `decision-framework` 🆕 — structured "should I do X" with tradeoffs, pre-mortem, kill criteria.

## Operations / Quality (custom)
- `pre-launch-checklist` 🆕 — final QA sweep before deploy/announce.

## Task Management (custom)
- `task-orchestration` — break a multi-domain task into a parallelizable DAG.
- `prompt-enhancer` — sharpen a vague prompt before running it. Run alone, don't chain.
- `muk` — this skill. The orchestrator itself.

## Claude Code Harness (built-in / plugin)
- `update-config` — settings.json hooks, permissions, env vars.
- `keybindings-help` — keyboard shortcut customization.
- `simplify` — review recent code changes for reuse/quality/efficiency.
- `fewer-permission-prompts` — auto-add common safe Bash/MCP calls to allowlist.
- `loop` — run a prompt/command on a recurring interval.
- `schedule` — cron-scheduled remote agents.
- `claude-api` — Anthropic SDK apps with caching, thinking, tool use, batch, files, citations.
- `init` — create CLAUDE.md for a repo.
- `review` — PR review.
- `security-review` — security audit of pending changes.

🆕 = added 2026-04-28

---

## When to chain (good outputs are usually 2-4 skills)

For comprehensive recipes, see `references/workflows.md`. Quick examples:

**Web product**
- Build a landing page that ranks + converts: `keyword-clustering` → `seo-page-structure` → `landing-page-copy` → `conversion-optimization` → `ui-styling` → `pre-launch-checklist`
- Ship a new SaaS feature: `frontend-architecture` → `component-design` → Claude Code (build) → `ui-styling` → `release-notes` → `pre-launch-checklist`
- Fix a slow site: `performance-optimization` (measure) → Claude Code (fix) → `ui-audit` (verify) → `accessibility-audit` (regression check)

**Brand / content**
- New brand voice rollout: `brand-voice-generator` → `brand` → rewrite top pages → update `email-sequence` + `social-post-writer` templates
- Customer story to assets: `customer-research` (interview) → `case-study-writer` → `landing-page-copy` (proof slot) → `social-post-writer` (3 platforms)

**Strategy**
- New offer: `customer-research` → `competitor-analysis` → `offer-creation` → `landing-page-copy` → `email-sequence` → `pre-launch-checklist`
- Hard call: `decision-framework` → if decision needs market data, route through `competitor-analysis` or `customer-research` first

**Investor / fundraising**
- Pitch deck end-to-end: `competitor-analysis` → `pitch-deck-content` → `slides` (or `design`/Gamma) → `storytelling-framework` (founder slide)

---

## Skills NOT in catalog (next candidates)

If a recurring need isn't covered, these are the next most useful additions:
- `newsletter-writer` — recurring newsletter format (different from email-sequence)
- `content-strategy` — multi-quarter editorial calendar
- `survey-design` — quantitative companion to customer-research
- `pricing-strategy` — deeper than offer-creation, models LTV/CAC/willingness-to-pay
- `analytics-setup` — GA4/PostHog/Plausible config + event taxonomy
- `error-tracking-setup` — Sentry-style monitoring scaffolding
- `404-empty-state-design` — small but high-leverage UX surface
- `onboarding-flow-design` — first-run UX systematic

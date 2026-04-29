# Named Workflows — Muk's pre-built recipes

Use these instead of re-deriving chains. If a task matches a workflow name, use the recipe verbatim — only customize when the task has a real twist.

---

## Web product workflows

### `ship-landing-page`
Goal: launch a landing page that ranks AND converts.
1. `keyword-clustering` — pick the cluster
2. `seo-page-structure` — outline the page for that cluster
3. `landing-page-copy` — write the actual copy
4. `conversion-optimization` — pressure-test for lifts
5. `ui-styling` — implement in shadcn/Tailwind (or project stack)
6. `micro-interaction-design` — feel pass
7. `pre-launch-checklist` — final QA
8. Deploy via Vercel/Netlify MCP

### `ship-feature`
Goal: ship a new product feature end-to-end.
1. `frontend-architecture` — folder structure, state, data flow
2. `component-design` — design the new components
3. Claude Code (build + tests)
4. `ui-styling` + `micro-interaction-design`
5. `review` — PR review
6. `release-notes` — write user-facing notes
7. `pre-launch-checklist` — final pass

### `fix-slow-site`
1. `performance-optimization` — measure (Lighthouse, bundle analyzer)
2. Claude Code — implement fixes
3. `ui-audit` — verify nothing broke visually
4. Re-measure to confirm

### `start-new-project`
1. `frontend-architecture` — scaffold structure
2. `design-system-builder` — token foundation
3. `motion-design-system` — motion tokens
4. `brand-voice-generator` — voice for copy
5. `init` — create CLAUDE.md
6. Claude Code — scaffold the actual repo

---

## Marketing workflows

### `launch-offer`
1. `customer-research` — validate the buyer's actual problem
2. `competitor-analysis` — see what they'd otherwise pick
3. `offer-creation` — price, deliverables, bonus, guarantee, scarcity
4. `landing-page-copy` — sales page
5. `email-sequence` — pre-launch + launch + post-launch
6. `conversion-optimization` — pressure test before launch
7. `growth-strategy` — pick ONE growth move for week 1

### `brand-voice-rollout`
1. `brand-voice-generator` — define the voice
2. `brand` — visual identity + messaging framework
3. Rewrite top 5 existing pages with new voice
4. Update `email-sequence` templates
5. Update `social-post-writer` templates

### `case-study-launch`
1. `customer-research` — interview the customer
2. `case-study-writer` — turn it into the story
3. `landing-page-copy` — slot into the proof section of the main page
4. `social-post-writer` — turn highlights into 3 posts (LinkedIn, X, threads)
5. `email-sequence` — feature it in next nurture email

---

## Strategy workflows

### `decide-what-to-build`
1. `competitor-analysis` — see the field
2. `customer-research` — what do they actually want?
3. `decision-framework` — tradeoff table + pre-mortem + kill criteria
4. `growth-strategy` — does it move the 30-day needle?

### `audit-existing-page`
1. `ui-audit` — top 3-5 conversion fixes
2. `accessibility-audit` — WCAG-level fixes
3. `conversion-optimization` — lifts available
4. `performance-optimization` — speed lifts
5. Claude Code — implement top 3 across all four

---

## Investor / fundraising workflows

### `build-pitch-deck`
1. `competitor-analysis` — market context
2. `pitch-deck-content` — narrative + slide content
3. `slides` — HTML implementation OR `design` — Gamma version
4. `storytelling-framework` — make the founder slide land
5. Review pass for numbers, claims, and asks

---

## Ops workflows

### `automate-repeated-task`
1. `workflow-automation` — pick the right mechanism (hook / cron / script)
2. `update-config` — settings.json hooks if needed
3. `schedule` — cron-scheduled remote agents if needed
4. Test the automation runs once before trusting it

### `pre-deploy`
1. `pre-launch-checklist` — full sweep
2. `security-review` — pending changes
3. `accessibility-audit` — WCAG basics
4. `performance-optimization` — re-measure if anything UI changed
5. Deploy

---

## Adding a new workflow

If you find yourself re-deriving a chain Muk has used before, add it here.
Format: name in backticks, one-line goal, numbered steps. Keep it tight — workflows beat principles.

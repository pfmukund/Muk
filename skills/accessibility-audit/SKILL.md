---
name: accessibility-audit
description: >
  Run a WCAG 2.2 AA-focused audit on a page or app. Outputs a prioritized
  punch list of fixes (blockers, warnings, polish), grouped by where in the
  code to fix them. Distinct from `ui-audit` which is conversion-focused —
  this one is accessibility + inclusive design.
  Use before any high-stakes launch, when targeting public-sector / EU buyers
  (compliance), when adding new flows, or as a quarterly hygiene pass.
  Triggers: "accessibility audit", "a11y audit", "WCAG audit", "is this accessible",
  "screen reader test", "keyboard navigation check", "make this accessible".
  NOT for performance (that's performance-optimization) and NOT for visual
  conversion fixes (that's ui-audit).
---

# Accessibility Audit (WCAG 2.2 AA)

Accessibility is a moral, legal, and quality bar — and almost always overlaps with conversion. If a screen reader can't navigate it, neither can a stressed-out human on a flaky train wifi.

## What to test against
- **Standard**: WCAG 2.2 Level AA (AAA where cheap)
- **Tools**: axe DevTools (browser ext), Lighthouse Accessibility, WAVE, NVDA (Win) or VoiceOver (Mac), keyboard-only nav
- **Manual checks always required** — automated tools catch ~30% of issues

---

## The 4 WCAG principles (and what to check for each)

### 1. Perceivable
- [ ] **Color contrast**: 4.5:1 normal text, 3:1 large text/UI components, 3:1 graphical objects
- [ ] **Non-text content has alt text**: meaningful alt for content images; `alt=""` for decorative
- [ ] **Color is not the only signal** (e.g. red text + ✓/✗ icon, not red text alone)
- [ ] **Text is resizable to 200%** without breaking layout
- [ ] **Audio/video** has captions, transcripts, audio descriptions where relevant
- [ ] **Animation respects `prefers-reduced-motion`** — auto-playing, parallax, infinite loops all need a kill switch
- [ ] **No content flashes more than 3×/sec** (seizure trigger)

### 2. Operable
- [ ] **All interactive elements reachable by keyboard** (Tab/Shift+Tab/Enter/Space/Arrow)
- [ ] **Focus indicator is always visible and high contrast** (NEVER `outline: none` without a replacement)
- [ ] **Logical tab order** matches visual order
- [ ] **Skip-to-content link** at top of page
- [ ] **No keyboard traps** (modals, dropdowns release focus on close)
- [ ] **Click targets ≥ 24×24 CSS pixels** (44×44 recommended for primary)
- [ ] **No critical actions on hover only** (touch users can't hover)
- [ ] **Time limits adjustable / extendable** if used (sessions, OTPs)
- [ ] **Pages have unique, descriptive `<title>`**
- [ ] **Heading hierarchy logical** (h1 → h2 → h3, no skips)
- [ ] **Multiple ways to find pages** (nav + search + sitemap)

### 3. Understandable
- [ ] **Page language declared** (`<html lang="en">`)
- [ ] **Form labels visible OR associated via `aria-label`/`aria-labelledby`**
- [ ] **Form errors announced** (live region or focus management)
- [ ] **Error messages suggest the fix** ("Email must include @" beats "Invalid input")
- [ ] **Required fields marked clearly** (visual + `aria-required`)
- [ ] **No unexpected context changes** (e.g. autosubmit on dropdown change)
- [ ] **Reading level appropriate** for audience (Hemingway/Flesch ≤ grade 8 for general public)
- [ ] **Abbreviations expanded on first use**
- [ ] **Consistent navigation across pages**

### 4. Robust
- [ ] **HTML validates** (W3C validator — major errors only, warnings OK)
- [ ] **Landmarks used**: `<main>`, `<nav>`, `<header>`, `<footer>`, `<aside>`
- [ ] **ARIA used correctly** — first rule of ARIA: don't use ARIA. Native HTML beats ARIA.
- [ ] **Custom components have correct ARIA roles + states** (combobox, dialog, tab, menu)
- [ ] **Status messages use `role="status"` or `aria-live="polite"`** (not alerts for non-urgent)
- [ ] **Modals**: focus trap, Esc to close, focus returns to trigger, `aria-modal="true"`, labelled
- [ ] **Custom inputs have keyboard equivalents** — sliders, drag-drop, custom selects

---

## The 8 most-shipped accessibility bugs (check these first)

1. **`outline: none` without a focus replacement** — keyboard users now navigate blind
2. **Icon-only buttons with no `aria-label`** — screen reader announces "button" with no info
3. **Placeholder used as a label** — disappears on focus, fails contrast, lost in autofill
4. **Modal that doesn't trap focus** — Tab exits the modal, lands on hidden background controls
5. **Color-only state indication** — error in red text, no icon or label change
6. **`<div onclick>`** — not focusable, not keyboard-operable. Use `<button>`.
7. **Unlabelled `<input>`** — `<input placeholder="Name">` fails. Add `<label>` or `aria-label`.
8. **Low contrast on disabled/ghost buttons** — gray-on-gray fails 4.5:1 even when "intentional"

---

## Quick test sequence (15 minutes per page)

1. **Lighthouse Accessibility** — run, note score, capture issues
2. **axe DevTools** — run, capture violations
3. **Tab through the page** with no mouse — note: focus visibility, order, traps
4. **Resize page text to 200%** — note: clipping, overlap
5. **`prefers-reduced-motion: reduce`** — test, note: animations that ignore it
6. **Screen reader spot-check** — tab through one form + one nav + one modal with VO/NVDA
7. **Disable CSS** — note: reading order matches visual order
8. **Hover/click target audit** — eyeball any < 24px target

---

## Output format

```
# Accessibility Audit — [URL]
Standard: WCAG 2.2 AA
Date: [yyyy-mm-dd]
Tester: [name]
Tools: Lighthouse, axe DevTools, [keyboard / VoiceOver / NVDA]

## Summary
- Lighthouse a11y score: [n]/100
- Blockers (must fix): [n]
- Warnings (should fix): [n]
- Polish (nice-to-have): [n]

## Blockers
For each:
- **[Issue]** — [WCAG SC #] — [where: file/component]
- Why: [user impact in plain language]
- Fix: [exact code change]

## Warnings
[Same format]

## Polish
[Same format]

## Top 5 quick wins
[5 fixes ordered by leverage — biggest user impact for smallest code change]

## Recommendation
[GO / GO-AFTER-BLOCKERS / NO-GO + sentence]
```

---

## Anti-patterns

1. **Lighthouse score = 100 → "we're done"** — automated tools miss ~70% of real issues
2. **ARIA-everything** — overusing ARIA breaks more than it fixes; native HTML first
3. **Auditing once, never again** — accessibility decays with every shipped feature
4. **Treating it as a checklist** — the principle is "can a real human with [X] use this", not "did we tick the box"
5. **`aria-hidden="true"` on focusable elements** — creates ghost focus
6. **Skipping screen reader testing** — text-only audits miss focus/announce issues
7. **"We'll fix it later"** — accessibility debt compounds faster than tech debt

---

## Pair with

- `pre-launch-checklist` — accessibility section is a smoke test; this is the deep audit
- `ui-audit` — conversion-focused critique (different angle, complementary)
- `ui-styling` — when fixing requires component-level changes
- `component-design` — building accessibility into new components from the start

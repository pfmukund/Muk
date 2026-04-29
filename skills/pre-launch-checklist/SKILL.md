---
name: pre-launch-checklist
description: >
  Run the final QA sweep before deploying or announcing a website, page, or product.
  Catches the embarrassing misses — broken meta tags, missing OG images, dead links,
  console errors, no analytics, no 404, untested mobile, missing favicon, perf regressions.
  Use BEFORE every public launch — site, landing page, feature, big update.
  Triggers: "pre-launch checklist", "ready to ship?", "ready to launch", "going live",
  "final QA", "launch day", "deploy checklist", "pre-deploy", "pre-flight check".
  NOT for code review (use `review`) and NOT for security audit (use `security-review`).
---

# Pre-Launch Checklist

Run all sections in order. Score each item ✅ pass / ⚠ warn / ❌ fail.
**If any ❌, do not launch.** ⚠ items go on a follow-up list.

Output a structured report — not a vague "looks good".

---

## 1. Performance (Core Web Vitals)

Measure with Lighthouse on the DEPLOYED URL (not localhost) on mobile + desktop.

- [ ] LCP < 2.5s (target < 1.5s) — mobile + desktop
- [ ] CLS < 0.1
- [ ] INP < 200ms (target < 100ms)
- [ ] TTFB < 600ms
- [ ] Total page weight < 1.5MB (warn at 1MB+ for landing pages)
- [ ] Largest image < 200KB, served as WebP/AVIF, with `width`/`height` attributes
- [ ] No render-blocking JS in critical path
- [ ] Fonts: preload primary, `font-display: swap`, ≤2 weights
- [ ] Bundle: route-based code splitting, vendor chunks separate
- [ ] No console errors, no console warnings on first load

## 2. SEO essentials

- [ ] `<title>` — unique per page, 50-60 chars, primary keyword in first half
- [ ] `<meta name="description">` — 150-160 chars, compelling, CTA-flavored
- [ ] `<link rel="canonical">` set correctly
- [ ] One `<h1>` per page, contains primary keyword naturally
- [ ] Heading hierarchy logical (no h2 → h4 jumps)
- [ ] All images have meaningful `alt` text (decorative = `alt=""`)
- [ ] Internal links: descriptive anchor text (no "click here")
- [ ] `robots.txt` exists and is correct
- [ ] `sitemap.xml` exists, listed in robots.txt, submitted to Search Console
- [ ] Structured data: Organization + WebSite at minimum; Product/Article/FAQPage where relevant. Validates in Rich Results Test.
- [ ] Hreflang if multi-language

## 3. Social / Open Graph

- [ ] `og:title`, `og:description`, `og:image` (1200×630, <8MB), `og:url`, `og:type`
- [ ] `twitter:card` = "summary_large_image", `twitter:image`, `twitter:title`, `twitter:description`
- [ ] OG image actually loads when pasted into Slack / iMessage / X / LinkedIn
- [ ] Favicon: 32×32, 180×180 (apple-touch), and SVG variant
- [ ] `theme-color` meta tag set

## 4. Functional

- [ ] All primary CTAs work and lead to the right place
- [ ] Forms: submit successfully, validate inputs, show error states, show success state, send confirmation email if expected
- [ ] No dead links — run a link checker (e.g. `linkinator`, `broken-link-checker`)
- [ ] 404 page exists, on-brand, has search/nav back to live pages
- [ ] 500 page exists, polite, surfaces a contact path
- [ ] Search works (if applicable)
- [ ] Auth flows: signup, login, logout, password reset, social auth — all complete a happy path

## 5. Content

- [ ] No lorem ipsum, no `[placeholder]`, no `TODO:` left in copy
- [ ] No typos in H1/H2 of any page (run a grammar pass)
- [ ] All numbers/claims defensible — flag anything you can't prove
- [ ] Pricing matches the actual checkout
- [ ] Dates updated (no "© 2024" in 2026)
- [ ] Email addresses tested — they actually reach a human
- [ ] Phone numbers click-to-call on mobile
- [ ] Photos are licensed (or AI-generated and labeled)

## 6. Cross-browser / device

- [ ] Chrome desktop + mobile
- [ ] Safari desktop + iOS Safari
- [ ] Firefox
- [ ] Edge
- [ ] Mobile breakpoints: 360, 390, 414, 768
- [ ] Tablet breakpoint: 1024
- [ ] Desktop: 1280, 1440, 1920
- [ ] Dark mode works (if implemented) — no white flashes, no unreadable text
- [ ] Touch targets ≥ 44×44px on mobile

## 7. Accessibility (smoke test — full audit is `accessibility-audit`)

- [ ] Keyboard tab order is logical, focus is visible everywhere
- [ ] All interactive elements reachable by keyboard
- [ ] Contrast ratio ≥ 4.5:1 for text, ≥ 3:1 for large text
- [ ] Skip-to-content link present
- [ ] Form fields have labels (visible or `aria-label`)
- [ ] Lighthouse accessibility score ≥ 95

## 8. Analytics + monitoring

- [ ] Analytics installed and firing (GA4 / Plausible / Fathom / PostHog)
- [ ] Goal events configured for primary conversions
- [ ] No analytics on staging/preview URLs
- [ ] Error monitoring set up (Sentry / LogRocket / equivalent)
- [ ] Uptime monitor set up (e.g. UptimeRobot, BetterStack)
- [ ] Cookie consent banner if EU traffic (and it actually blocks scripts until consent)

## 9. Legal + trust

- [ ] Privacy policy page — current, links to all data processors used
- [ ] Terms of service — appropriate for the offering
- [ ] Cookie policy if applicable
- [ ] Refund policy (if e-commerce / paid)
- [ ] Imprint / business address (required in some jurisdictions)
- [ ] Trust badges: real testimonials with names + photos OR no fake ones at all
- [ ] No claims that legal would flag ("guaranteed results", "doctor approved" without proof)

## 10. Deploy + rollback

- [ ] Deploys are reproducible (CI/CD or documented steps)
- [ ] Environment variables set in production (no `undefined` in console)
- [ ] Secrets are NOT in client bundle (grep for API keys)
- [ ] DNS configured + propagated
- [ ] HTTPS works, no mixed content warnings
- [ ] Redirects from old URLs (301, not 302) if migrating
- [ ] Rollback plan exists (Netlify/Vercel: previous deploy, custom: documented)
- [ ] Backup of database taken if launch involves DB changes
- [ ] Soft-launch / staging tested by a human (not just you)

---

## Output format

```
# Pre-Launch Report — [Project name]
Tested URL: [url]
Date: [yyyy-mm-dd]
Tester: [name]

## Summary
✅ [n] passed
⚠ [n] warnings
❌ [n] blockers

## Blockers (must fix before launch)
1. [item] — [where] — [fix]
2. ...

## Warnings (post-launch follow-up)
1. ...

## Section scores
- Performance: ✅/⚠/❌
- SEO: ...
- Social: ...
- Functional: ...
- Content: ...
- Cross-browser: ...
- Accessibility: ...
- Analytics: ...
- Legal: ...
- Deploy: ...

## Recommendation
[GO / NO-GO + one sentence]
```

---

## Anti-patterns

1. **Running on localhost** — measure on the deployed URL
2. **Lighthouse on a single page** — test home + 1 product/landing + 1 article
3. **Skipping mobile** — mobile is 60%+ of most traffic
4. **"Looks good to me"** — produce the structured report or you didn't run the checklist
5. **Skipping rollback plan** — every launch should have an undo button

---

## Pair with

- `performance-optimization` — fix any perf blockers found
- `accessibility-audit` — full WCAG audit before high-stakes launches
- `security-review` — for code changes
- `release-notes` — write the user-facing version of what shipped

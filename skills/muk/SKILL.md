---
name: muk
description: Mukund Totla's personal master orchestrator â€” activate with "Muk", "/muk", "Hey Muk", "Muk go", "use Muk", "activate Muk", or just describe any complex task and this skill will intelligently analyze it and assemble the best combination of skills, agents, plugins, MCPs, and tools to complete it. Also triggers on "figure out what to use", "use your best tools", "orchestrate this", "use everything you have", or any task spanning multiple domains. When the user seems unsure which skill to use, or a task clearly requires chaining multiple capabilities â€” always activate Muk. This is Mukund's power-mode.
---

# Muk â€” Master Orchestrator

You are Muk, Mukund Totla's personal orchestrator. When activated, your job is to pick the right combination of skills, agents, plugins, and MCP tools from everything installed on this Claude instance, then run them in the correct order to finish the user's task.

## Activation triggers

- "Muk", "/muk", "Hey Muk", "Muk go", "use Muk", "activate Muk"
- "figure out what to use", "use your best tools", "orchestrate this", "use everything you have"
- Any task spanning multiple domains (research + writing + spreadsheet + email, etc.)
- Any task where the user seems unsure which skill to use

## Operating procedure

1. **Read** task. Restate goal in one sentence.
2. **Survey.** Consult pack inventory below + skills/MCPs already visible in environment. Do not invent tools.
3. **Plan.** Write short numbered plan naming each skill/agent/plugin + what it handles.
4. **Manifest (MANDATORY).** Before execution, print a `Tool manifest:` block listing exactly what will be invoked:
   - Local skills (already installed)
   - Catalog skills needing install (see Auto-install below)
   - Built-in tools (Bash, Read, Write, Edit, Grep, Glob, Agent, WebFetch, WebSearch, TodoWrite)
   - MCP connectors (Gmail, Supabase, Figma, etc.)
   - Subagents + their scope
5. **Auto-install** missing catalog skills -- see procedure below.
6. **Ask once** if critical info missing. Don't over-ask.
7. **Execute.** Parallelize independent steps. Subagents for heavy isolated work. Narrate tool switches: "-> using `systematic-debugging`...", "-> spawning Explore subagent...".
8. **Verify.** Sanity-check outputs (counts, links, file opens, math) before declaring done.
9. **Deliver.** Summarize with a `Tools used:` footer listing every skill/plugin/agent/MCP/tool actually invoked. Share `computer://` links for files. Suggest next action.

## Auto-install (catalog skills from `pfmukund/Muk` marketplace)

**Marketplace registration (once per machine):**
```
/plugin marketplace add pfmukund/Muk
```

**Per-task flow when catalog skill needed:**

1. Check if skill folder exists under `~/.claude/skills/<name>/` or `~/.claude/plugins/<name>/`.
2. If missing -> announce: `Need <skill-name> - installing from Muk marketplace.`
3. Attempt install via Bash:
   ```bash
   claude plugin install <name>@Muk
   ```
   Fallback: print exact `/plugin install <name>@Muk` command and ask user to run it, then continue.
4. Verify install (folder now exists) before invoking.
5. Log every install in `Tools used:` footer with `(newly installed)` tag.

**Do NOT silently skip.** If install fails or user declines -> state clearly, propose best workaround using installed tools, note the gap.

## Transparency mandate

Every Muk task response MUST include:

- **Opening:** `Tool manifest:` block (what will be used)
- **Inline narration:** short "-> using X" lines at each tool switch
- **Closing:** `Tools used:` footer (what was actually run, in order)

No silent tool use. No vague "using Muk". Name every skill/plugin/agent/MCP/built-in tool.

## Principles

- Prefer installed skills over ad-hoc reasoning. Skills encode best practices.
- Chain, don't duplicate. Pass outputs between skills.
- Fail loud. Missing tool -> say so, attempt install, or pick best workaround.
- Keep outputs portable. Muk runs on home PC, office PC, laptop, phone, Antigravity.
- Consult `.claude-plugin/marketplace.json` for authoritative index.

## Companion: Pow (power-mode discipline)

`pow` is Muk's execution-discipline companion. **Muk picks tools, Pow enforces how to use them.** When the user asks for "max effort", "production-grade", "no shortcuts", "best possible job", or stacks the call as "Muk + Pow" / "Muk in pow mode" â€” invoke `pow` after producing the tool manifest. Pow wraps the run in five reinforcing spines:

1. **Four-phase loop** (from `obra/superpowers`) â€” `brainstorming` -> `writing-plans` -> `executing-plans` + `subagent-driven-development` + `test-driven-development` -> `verification-before-completion` -> `finishing-a-development-branch`. All those skills are already installed in this pack.
2. **Three-layer memory** (from `thedotmack/claude-mem`) â€” index -> timeline -> full body. Don't load whole memory bodies before checking the index; honor `<private>` opt-out tags.
3. **Sandbox + permission banner** (from `anthropics/claude-code#22155`) â€” print one-line state header at task start: sandbox on/off, CWD, perm counts, loop state. Warn before any out-of-CWD write if sandbox is off.
4. **Leaked-source patterns** (from `yasasbanukaofficial/claude-code` + `codeaashu/claude-code`) â€” parallel prefetch on boot (batch independent reads in one tool call), KAIROS-style watch on long-running commands, ULTRAPLAN delegate (spawn `Plan` subagent for big plans, don't plan inline), Dream-style end-of-session consolidation (orient -> gather -> consolidate -> prune over `~/.claude/projects/<project>/memory/`). **Delegation pool:** ULTRAPLAN routes to the 131+ specialized subagents from [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) bundled at `agents/` (10 categories: core-development, language-experts, infrastructure, quality-assurance, data-ai, developer-experience, specialized-domains, business-product, orchestration, research-analysis).
5. **Curated power-ups** (from `hesreallyhim/awesome-claude-code`) â€” Ralph autonomous loop via `/loop` skill with circuit breaker, Dippy-style auto-approve for safe Bash + always-confirm for destructive ops, `/create-pr` pipeline, `/analyze-issue` spec emitter, HUD-style statusline footer.

**Pow stacking rule:** when both are active, Muk's manifest goes first; Pow then narrates each phase transition (`-> Phase 2: planning...`), enforces the TDD gate (no impl code before failing test exists), and refuses to claim done without verification evidence. Both transparency mandates compose: manifest at start, narrate inline, list everything used at end.

**Auto-escalate to Pow** when: the task is multi-file, security-sensitive, touches production, the user mentions launches/migrations/refactors, or any signal that mistakes are costly. Don't ask permission for the escalation â€” just announce `-> escalating to Pow mode (reason: <one line>)` and run.

<!-- MUK_INVENTORY_START -->
<!-- Auto-generated by scripts/sync_marketplace.py. Do not edit by hand. -->

## Pack inventory (auto-generated)

**Summary:** 498 skills · 129 plugins · 169 agents.

### Skills

- **muk** — Mukund Totla's personal master orchestrator â€” activate with "Muk", "/muk", "Hey Muk", "Muk go", "use Muk", "activate Muk", or just describe any complex task and this skill will intelligently analyze it and assemble the best combination of skills, agents, plugins, MCPs, and tools to complete it. Also triggers on "figure out what to use", "use your best tools", "orchestrate this", "use everything you have", or any task spanning multiple domains. When the user seems unsure which skill to use, or a task clearly requires chaining multiple capabilities â€” always activate Muk. This is Mukund's power-mode.
- **ab-test-setup** — When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program. Also use when the user mentions "A/B test," "split test," "experiment," "test this change," "variant copy," "multivariate test," "hypothesis," "should I test this," "which version is better," "test two versions," "statistical significance," "how long should I run this test," "growth experiments," "experiment velocity," "experiment backlog," "ICE score," "experimentation program," or "experiment playbook." Use this whenever someone is comparing two approaches and wants to measure which performs better, or when they want to build a systematic experimentation practice. For tracking implementation, see analytics-tracking. For page-level conversion optimization, see page-cro.
- **accessibility-wcag** — Web accessibility patterns for WCAG 2.2 compliance including ARIA, keyboard navigation, screen readers, and testing
- **ad-creative** — When the user wants to generate, iterate, or scale ad creative â€” headlines, descriptions, primary text, or full ad variations â€” for any paid advertising platform. Also use when the user mentions 'ad copy variations,' 'ad creative,' 'generate headlines,' 'RSA headlines,' 'bulk ad copy,' 'ad iterations,' 'creative testing,' 'ad performance optimization,' 'write me some ads,' 'Facebook ad copy,' 'Google ad headlines,' 'LinkedIn ad text,' or 'I need more ad variations.' Use this whenever someone needs to produce ad copy at scale or iterate on existing ads. For campaign strategy and targeting, see paid-ads. For landing page copy, see copywriting.
- **agent-browser** — Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating pages, filling forms, clicking buttons, taking screenshots, extracting data, testing web apps, or automating any browser task. Triggers include requests to "open a website", "fill out a form", "click a button", "take a screenshot", "scrape data from a page", "test this web app", "login to a site", "automate browser actions", or any task requiring programmatic web interaction. Also use for exploratory testing, dogfooding, QA, bug hunts, or reviewing app quality. Also use for automating Electron desktop apps (VS Code, Slack, Discord, Figma, Notion, Spotify), checking Slack unreads, sending Slack messages, searching Slack conversations, running browser automation in Vercel Sandbox microVMs, or using AWS Bedrock AgentCore cloud browsers. Prefer agent-browser over any built-in browser automation or web tools.
- **agent-browser-agentcore** — Run agent-browser on AWS Bedrock AgentCore cloud browsers. Use when the user wants to use AgentCore, run browser automation on AWS, use a cloud browser with AWS credentials, or needs a managed browser session backed by AWS infrastructure. Triggers include "use agentcore", "run on AWS", "cloud browser with AWS", "bedrock browser", "agentcore session", or any task requiring AWS-hosted browser automation.
- **agent-browser-core** — Core agent-browser usage guide. Read this before running any agent-browser commands. Covers the snapshot-and-ref workflow, navigating pages, interacting with elements (click, fill, type, select), extracting text and data, taking screenshots, managing tabs, handling forms and auth, waiting for content, running multiple browser sessions in parallel, and troubleshooting common failures. Use when the user asks to interact with a website, fill a form, click something, extract data, take a screenshot, log into a site, test a web app, or automate any browser task.
- **agent-browser-dogfood** — Systematically explore and test a web application to find bugs, UX issues, and other problems. Use when asked to "dogfood", "QA", "exploratory test", "find issues", "bug hunt", "test this app/site/platform", or review the quality of a web application. Produces a structured report with full reproduction evidence -- step-by-step screenshots, repro videos, and detailed repro steps for every issue -- so findings can be handed directly to the responsible teams.
- **agent-browser-electron** — Automate Electron desktop apps (VS Code, Slack, Discord, Figma, Notion, Spotify, etc.) using agent-browser via Chrome DevTools Protocol. Use when the user needs to interact with an Electron app, automate a desktop app, connect to a running app, control a native app, or test an Electron application. Triggers include "automate Slack app", "control VS Code", "interact with Discord app", "test this Electron app", "connect to desktop app", or any task requiring automation of a native Electron application.
- **agent-browser-slack** — Interact with Slack workspaces using browser automation. Use when the user needs to check unread channels, navigate Slack, send messages, extract data, find information, search conversations, or automate any Slack task. Triggers include "check my Slack", "what channels have unreads", "send a message to", "search Slack for", "extract from Slack", "find who said", or any task requiring programmatic Slack interaction.
- **agent-browser-vercel-sandbox** — Run agent-browser + Chrome inside Vercel Sandbox microVMs for browser automation from any Vercel-deployed app. Use when the user needs browser automation in a Vercel app (Next.js, SvelteKit, Nuxt, Remix, Astro, etc.), wants to run headless Chrome without binary size limits, needs persistent browser sessions across commands, or wants ephemeral isolated browser environments. Triggers include "Vercel Sandbox browser", "microVM Chrome", "agent-browser in sandbox", "browser automation on Vercel", or any task requiring Chrome in a Vercel Sandbox.
- **agent-sandboxes** — Operate E2B agent sandboxes using the CLI. Use when user needs to run code in isolation, test packages, execute commands safely, or work with binary files in a sandbox environment. Keywords: sandbox, e2b, isolated environment, run code, test code, safe execution.
- **ai-seo** — When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. Also use when the user mentions 'AI SEO,' 'AEO,' 'GEO,' 'LLMO,' 'answer engine optimization,' 'generative engine optimization,' 'LLM optimization,' 'AI Overviews,' 'optimize for ChatGPT,' 'optimize for Perplexity,' 'AI citations,' 'AI visibility,' 'zero-click search,' 'how do I show up in AI answers,' 'LLM mentions,' or 'optimize for Claude/Gemini.' Use this whenever someone wants their content to be cited or surfaced by AI assistants and AI search engines. For traditional technical and on-page SEO audits, see seo-audit. For structured data implementation, see schema-markup.
- **algorithmic-art** — Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.
- **analytics-tracking** — When the user wants to set up, improve, or audit analytics tracking and measurement. Also use when the user mentions "set up tracking," "GA4," "Google Analytics," "conversion tracking," "event tracking," "UTM parameters," "tag manager," "GTM," "analytics implementation," "tracking plan," "how do I measure this," "track conversions," "attribution," "Mixpanel," "Segment," "are my events firing," or "analytics isn't working." Use this whenever someone asks how to know if something is working or wants to measure marketing results. For A/B test measurement, see ab-test-setup.
- **api-design-patterns** — REST API design with resource naming, pagination, versioning, and OpenAPI spec generation
- **artifacts-builder** — Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.
- **aso-audit** — When the user wants to audit or optimize an App Store or Google Play listing. Also use when the user mentions 'ASO audit,' 'app store optimization,' 'optimize my app listing,' 'improve app visibility,' 'app store ranking,' 'audit my listing,' 'why aren't people downloading my app,' 'improve my app conversion,' 'keyword optimization for app,' or 'compare my app to competitors.' Use when the user shares an App Store or Google Play URL and wants to improve it.
- **asr-transcribe-to-text** — Transcribes audio and video files to text using Qwen3-ASR. Supports two modes â€” local MLX inference on macOS Apple Silicon (no API key, 15-27x realtime) and remote API via vLLM/OpenAI-compatible endpoints. Auto-detects platform and recommends the best path. Triggers when the user wants to transcribe recordings, convert audio/video to text, do speech-to-text, or mentions ASR, Qwen ASR, è½¬å½•, è¯­éŸ³è½¬æ–‡å­—, å½•éŸ³è½¬æ–‡å­—. Also triggers for meeting recordings, lectures, interviews, podcasts, screen recordings, or any audio/video file the user wants converted to text.
- **authentication-patterns** — Authentication and authorization patterns including OAuth2, JWT, RBAC, session management, and PKCE flows
- **aws-cloud-patterns** — AWS cloud patterns for Lambda, ECS, S3, DynamoDB, and Infrastructure as Code with CDK/Terraform
- **brainstorming** — You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation.
- **brand-guidelines** — Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.
- **canvas-design** — Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.
- **capture-screen** — Programmatic screenshot capture on macOS. Find window IDs with Swift CGWindowListCopyWindowInfo, control application windows via AppleScript (zoom, scroll, select), and capture with screencapture. Use when automating screenshots, capturing application windows for documentation, or building multi-shot visual workflows.
- **caveman** — Skill: caveman
- **caveman-commit** — Skill: caveman-commit
- **caveman-help** — >
- **caveman-review** — Skill: caveman-review
- **changelog-generator** — Skill: changelog-generator
- **churn-prevention** — Skill: churn-prevention
- **ci-cd-pipelines** — CI/CD pipeline patterns for GitHub Actions, GitLab CI, testing strategies, and deployment automation
- **claude-api** — Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 â†’ 4.6, 4.6 â†’ 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.
- **claude-memory-kit** — Persistent memory system for Claude Code. Two-layer architecture (hot cache + knowledge wiki), safety hooks, /close-day end-of-day synthesis. Zero external dependencies.
- **cli-demo-generator** — Generates professional animated CLI demos as GIFs using VHS terminal recordings. Handles tape file creation, self-bootstrapping demos with hidden setup, output noise filtering, post-processing speed-up, and frame-level verification. Use when users want to create terminal demos, record CLI workflows as GIFs, generate animated documentation, build demo tapes for README files, or need to showcase any command-line tool visually. Also triggers on "record terminal", "VHS tape", "demo GIF", "animate my CLI", or any request to visually demonstrate shell commands.
- **cloudflare-troubleshooting** — Investigate and resolve Cloudflare configuration issues using API-driven evidence gathering. Use when troubleshooting ERR_TOO_MANY_REDIRECTS, SSL errors, DNS issues, or any Cloudflare-related problems. Focus on systematic investigation using Cloudflare API to examine actual configuration rather than making assumptions.
- **cold-email** — Write B2B cold emails and follow-up sequences that get replies. Use when the user wants to write cold outreach emails, prospecting emails, cold email campaigns, sales development emails, or SDR emails. Also use when the user mentions "cold outreach," "prospecting email," "outbound email," "email to leads," "reach out to prospects," "sales email," "follow-up email sequence," "nobody's replying to my emails," or "how do I write a cold email." Covers subject lines, opening lines, body copy, CTAs, personalization, and multi-touch follow-up sequences. For warm/lifecycle email sequences, see email-sequence. For sales collateral beyond emails, see sales-enablement.
- **community-marketing** — Skill: community-marketing
- **competitive-ads-extractor** — Extracts and analyzes competitors' ads from ad libraries (Facebook, LinkedIn, etc.) to understand what messaging, problems, and creative approaches are working. Helps inspire and improve your own ad campaigns.
- **competitor-alternatives** — When the user wants to create competitor comparison or alternative pages for SEO and sales enablement. Also use when the user mentions 'alternative page,' 'vs page,' 'competitor comparison,' 'comparison page,' '[Product] vs [Product],' '[Product] alternative,' 'competitive landing pages,' 'how do we compare to X,' 'battle card,' or 'competitor teardown.' Use this for any content that positions your product against competitors. Covers four formats: singular alternative, plural alternatives, you vs competitor, and competitor vs competitor. For sales-specific competitor docs, see sales-enablement.
- **competitors-analysis** — Skill: competitors-analysis
- **composio** — Use 1000+ external apps via Composio - either directly through the CLI or by building AI agents and apps with the SDK
- **composition-patterns** — Skill: composition-patterns
- **compress** — >
- **content-strategy** — When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover. Also use when the user mentions "content strategy," "what should I write about," "content ideas," "blog strategy," "topic clusters," "content planning," "editorial calendar," "content marketing," "content roadmap," "what content should I create," "blog topics," "content pillars," or "I don't know what to write." Use this whenever someone needs help deciding what content to produce, not just writing it. For writing individual pieces, see copywriting. For SEO-specific audits, see seo-audit. For social media content specifically, see social-content.
- **continuous-learning** — Auto-extract patterns from coding sessions, track corrections, and build reusable knowledge with confidence scoring
- **copy-editing** — Skill: copy-editing
- **copywriting** — Skill: copywriting
- **customer-research** — When the user wants to conduct, analyze, or synthesize customer research. Use when the user mentions "customer research," "ICP research," "talk to customers," "analyze transcripts," "customer interviews," "survey analysis," "support ticket analysis," "voice of customer," "VOC," "build personas," "customer personas," "jobs to be done," "JTBD," "what do customers say," "what are customers struggling with," "Reddit mining," "G2 reviews," "review mining," "digital watering holes," "community research," "forum research," "competitor reviews," "customer sentiment," or "find out why customers churn/convert/buy." Use for both analyzing existing research assets AND gathering new research from online sources. For writing copy informed by research, see copywriting. For acting on research to improve pages, see page-cro.
- **data-engineering** — Data engineering patterns for ETL pipelines, data warehousing, Apache Spark, and data quality validation
- **database-optimization** — Query optimization, indexing strategies, and database performance tuning for PostgreSQL and MySQL
- **deep-dive** — Claude-native deep research using DAG-based query planning, parallel subagent execution, and gap-driven iteration. No external API needed.
- **deep-research** — Skill: deep-research
- **deploy-to-vercel** — Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".
- **devops-automation** — CI/CD pipeline design with GitHub Actions, Docker, Kubernetes, Helm, and GitOps patterns
- **dispatching-parallel-agents** — Skill: dispatching-parallel-agents
- **django-patterns** — Django architecture patterns including DRF, ORM optimization, signals, middleware, and project structure
- **doc-coauthoring** — Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.
- **docker-best-practices** — Docker best practices including multi-stage builds, compose patterns, image optimization, and security
- **docx** — Skill: docx
- **douban-skill** — Skill: douban-skill
- **ecc-accessibility** — Design, implement, and audit inclusive digital products using WCAG 2.2 Level AA
- **ecc-agent-eval** — Skill: ecc-agent-eval
- **ecc-agent-harness-construction** — Design and optimize AI agent action spaces, tool definitions, and observation formatting for higher completion rates.
- **ecc-agent-introspection-debugging** — Skill: ecc-agent-introspection-debugging
- **ecc-agent-payment-x402** — Add x402 payment execution to AI agents â€” per-task budgets, spending controls, and non-custodial wallets via MCP tools. Use when agents need to pay for APIs, services, or other agents.
- **ecc-agent-sort** — Build an evidence-backed ECC install plan for a specific repo by sorting skills, commands, rules, hooks, and extras into DAILY vs LIBRARY buckets using parallel repo-aware review passes. Use when ECC should be trimmed to what a project actually needs instead of loading the full bundle.
- **ecc-agentic-engineering** — Operate as an agentic engineer using eval-first execution, decomposition, and cost-aware model routing.
- **ecc-ai-first-engineering** — Engineering operating model for teams where AI agents generate a large share of implementation output.
- **ecc-ai-regression-testing** — Skill: ecc-ai-regression-testing
- **ecc-android-clean-architecture** — Clean Architecture patterns for Android and Kotlin Multiplatform projects â€” module structure, dependency rules, UseCases, Repositories, and data layer patterns.
- **ecc-api-connector-builder** — Build a new API connector or provider by matching the target repo's existing integration pattern exactly. Use when adding one more integration without inventing a second architecture.
- **ecc-api-design** — REST API design patterns including resource naming, status codes, pagination, filtering, error responses, versioning, and rate limiting for production APIs.
- **ecc-architecture-decision-records** — Skill: ecc-architecture-decision-records
- **ecc-article-writing** — Write articles, guides, blog posts, tutorials, newsletter issues, and other long-form content in a distinctive voice derived from supplied examples or brand guidance. Use when the user wants polished written content longer than a paragraph, especially when voice consistency, structure, and credibility matter.
- **ecc-automation-audit-ops** — Evidence-first automation inventory and overlap audit workflow for ECC. Use when the user wants to know which jobs, hooks, connectors, MCP servers, or wrappers are live, broken, redundant, or missing before fixing anything.
- **ecc-autonomous-agent-harness** — Skill: ecc-autonomous-agent-harness
- **ecc-autonomous-loops** — Skill: ecc-autonomous-loops
- **ecc-backend-patterns** — Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes.
- **ecc-benchmark** — Use this skill to measure performance baselines, detect regressions before/after PRs, and compare stack alternatives.
- **ecc-blueprint** — >-
- **ecc-brand-voice** — Build a source-derived writing style profile from real posts, essays, launch notes, docs, or site copy, then reuse that profile across content, outreach, and social workflows. Use when the user wants voice consistency without generic AI writing tropes.
- **ecc-browser-qa** — Use this skill to automate visual testing and UI interaction verification using browser automation after deploying features.
- **ecc-bun-runtime** — Bun as runtime, package manager, bundler, and test runner. When to choose Bun vs Node, migration notes, and Vercel support.
- **ecc-canary-watch** — Use this skill to monitor a deployed URL for regressions after deploys, merges, or dependency upgrades.
- **ecc-carrier-relationship-management** — >
- **ecc-ck** — Skill: ecc-ck
- **ecc-claude-api** — Anthropic Claude API patterns for Python and TypeScript. Covers Messages API, streaming, tool use, vision, extended thinking, batches, prompt caching, and Claude Agent SDK. Use when building applications with the Claude API or Anthropic SDKs.
- **ecc-claude-devfleet** — Orchestrate multi-agent coding tasks via Claude DevFleet â€” plan projects, dispatch parallel agents in isolated worktrees, monitor progress, and read structured reports.
- **ecc-click-path-audit** — Skill: ecc-click-path-audit
- **ecc-clickhouse-io** — ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads.
- **ecc-code-tour** — Create CodeTour `.tour` files â€” persona-targeted, step-by-step walkthroughs with real file and line anchors. Use for onboarding tours, architecture walkthroughs, PR tours, RCA tours, and structured "explain how this works" requests.
- **ecc-codebase-onboarding** — Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map, key entry points, conventions, and a starter CLAUDE.md. Use when joining a new project or setting up Claude Code for the first time in a repo.
- **ecc-coding-standards** — Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review. Use detailed frontend or backend skills for framework-specific patterns.
- **ecc-compose-multiplatform-patterns** — Compose Multiplatform and Jetpack Compose patterns for KMP projects â€” state management, navigation, theming, performance, and platform-specific UI.
- **ecc-configure-ecc** — Interactive installer for Everything Claude Code â€” guides users through selecting and installing skills and rules to user-level or project-level directories, verifies paths, and optionally optimizes installed files.
- **ecc-connections-optimizer** — Reorganize the user's X and LinkedIn network with review-first pruning, add/follow recommendations, and channel-specific warm outreach drafted in the user's real voice. Use when the user wants to clean up following lists, grow toward current priorities, or rebalance a social graph around higher-signal relationships.
- **ecc-content-engine** — Create platform-native content systems for X, LinkedIn, TikTok, YouTube, newsletters, and repurposed multi-platform campaigns. Use when the user wants social posts, threads, scripts, content calendars, or one source asset adapted cleanly across platforms.
- **ecc-content-hash-cache-pattern** — Cache expensive file processing results using SHA-256 content hashes â€” path-independent, auto-invalidating, with service layer separation.
- **ecc-context-budget** — Skill: ecc-context-budget
- **ecc-continuous-agent-loop** — Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls.
- **ecc-continuous-learning** — Automatically extract reusable patterns from Claude Code sessions and save them as learned skills for future use.
- **ecc-continuous-learning-v2** — Instinct-based learning system that observes sessions via hooks, creates atomic instincts with confidence scoring, and evolves them into skills/commands/agents. v2.1 adds project-scoped instincts to prevent cross-project contamination.
- **ecc-cost-aware-llm-pipeline** — Cost optimization patterns for LLM API usage â€” model routing by task complexity, budget tracking, retry logic, and prompt caching.
- **ecc-council** — Convene a four-voice council for ambiguous decisions, tradeoffs, and go/no-go calls. Use when multiple valid paths exist and you need structured disagreement before choosing.
- **ecc-cpp-coding-standards** — C++ coding standards based on the C++ Core Guidelines (isocpp.github.io). Use when writing, reviewing, or refactoring C++ code to enforce modern, safe, and idiomatic practices.
- **ecc-cpp-testing** — Use only when writing/updating/fixing C++ tests, configuring GoogleTest/CTest, diagnosing failing or flaky tests, or adding coverage/sanitizers.
- **ecc-crosspost** — Multi-platform content distribution across X, LinkedIn, Threads, and Bluesky. Adapts content per platform using content-engine patterns. Never posts identical content cross-platform. Use when the user wants to distribute content across social platforms.
- **ecc-csharp-testing** — C# and .NET testing patterns with xUnit, FluentAssertions, mocking, integration tests, and test organization best practices.
- **ecc-customer-billing-ops** — Operate customer billing workflows such as subscriptions, refunds, churn triage, billing-portal recovery, and plan analysis using connected billing tools like Stripe. Use when the user needs to help a customer, inspect subscription state, or manage revenue-impacting billing operations.
- **ecc-customs-trade-compliance** — >
- **ecc-dart-flutter-patterns** — Skill: ecc-dart-flutter-patterns
- **ecc-dashboard-builder** — Build monitoring dashboards that answer real operator questions for Grafana, SigNoz, and similar platforms. Use when turning metrics into a working dashboard instead of a vanity board.
- **ecc-data-scraper-agent** — Build a fully automated AI-powered data collection agent for any public source â€” job boards, prices, news, GitHub, sports, anything. Scrapes on a schedule, enriches data with a free LLM (Gemini Flash), stores results in Notion/Sheets/Supabase, and learns from user feedback. Runs 100% free on GitHub Actions. Use when the user wants to monitor, collect, or track any public data automatically.
- **ecc-database-migrations** — Database migration best practices for schema changes, data migrations, rollbacks, and zero-downtime deployments across PostgreSQL, MySQL, and common ORMs (Prisma, Drizzle, Kysely, Django, TypeORM, golang-migrate).
- **ecc-deep-research** — Multi-source deep research using firecrawl and exa MCPs. Searches the web, synthesizes findings, and delivers cited reports with source attribution. Use when the user wants thorough research on any topic with evidence and citations.
- **ecc-defi-amm-security** — Security checklist for Solidity AMM contracts, liquidity pools, and swap flows. Covers reentrancy, CEI ordering, donation or inflation attacks, oracle manipulation, slippage, admin controls, and integer math.
- **ecc-deployment-patterns** — Skill: ecc-deployment-patterns
- **ecc-design-system** — Use this skill to generate or audit design systems, check visual consistency, and review PRs that touch styling.
- **ecc-django-patterns** — Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals, middleware, and production-grade Django apps.
- **ecc-django-security** — Django security best practices, authentication, authorization, CSRF protection, SQL injection prevention, XSS prevention, and secure deployment configurations.
- **ecc-django-tdd** — Django testing strategies with pytest-django, TDD methodology, factory_boy, mocking, coverage, and testing Django REST Framework APIs.
- **ecc-django-verification** — Verification loop for Django projects: migrations, linting, tests with coverage, security scans, and deployment readiness checks before release or PR.
- **ecc-dmux-workflows** — Multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows across Claude Code, Codex, OpenCode, and other harnesses. Use when running multiple agent sessions in parallel or coordinating multi-agent development workflows.
- **ecc-docker-patterns** — Docker and Docker Compose patterns for local development, container security, networking, volume strategies, and multi-service orchestration.
- **ecc-documentation-lookup** — Use up-to-date library and framework docs via Context7 MCP instead of training data. Activates for setup questions, API references, code examples, or when the user names a framework (e.g. React, Next.js, Prisma).
- **ecc-dotnet-patterns** — Idiomatic C# and .NET patterns, conventions, dependency injection, async/await, and best practices for building robust, maintainable .NET applications.
- **ecc-e2e-testing** — Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and flaky test strategies.
- **ecc-ecc-tools-cost-audit** — Evidence-first ECC Tools burn and billing audit workflow. Use when investigating runaway PR creation, quota bypass, premium-model leakage, duplicate jobs, or GitHub App cost spikes in the ECC Tools repo.
- **ecc-email-ops** — Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC. Use when the user wants to organize email, draft or send through the real mail surface, or prove what landed in Sent.
- **ecc-energy-procurement** — >
- **ecc-enterprise-agent-ops** — Operate long-lived agent workloads with observability, security boundaries, and lifecycle management.
- **ecc-eval-harness** — Formal evaluation framework for Claude Code sessions implementing eval-driven development (EDD) principles
- **ecc-evm-token-decimals** — Prevent silent decimal mismatch bugs across EVM chains. Covers runtime decimal lookup, chain-aware caching, bridged-token precision drift, and safe normalization for bots, dashboards, and DeFi tools.
- **ecc-exa-search** — Neural search via Exa MCP for web, code, and company research. Use when the user needs web search, code examples, company intel, people lookup, or AI-powered deep research with Exa's neural search engine.
- **ecc-fal-ai-media** — Unified media generation via fal.ai MCP â€” image, video, and audio. Covers text-to-image (Nano Banana), text/image-to-video (Seedance, Kling, Veo 3), text-to-speech (CSM-1B), and video-to-audio (ThinkSound). Use when the user wants to generate images, videos, or audio with AI.
- **ecc-finance-billing-ops** — Evidence-first revenue, pricing, refunds, team-billing, and billing-model truth workflow for ECC. Use when the user wants a sales snapshot, pricing comparison, duplicate-charge diagnosis, or code-backed billing reality instead of generic payments advice.
- **ecc-flutter-dart-code-review** — Library-agnostic Flutter/Dart code review checklist covering widget best practices, state management patterns (BLoC, Riverpod, Provider, GetX, MobX, Signals), Dart idioms, performance, accessibility, security, and clean architecture.
- **ecc-foundation-models-on-device** — Apple FoundationModels framework for on-device LLM â€” text generation, guided generation with @Generable, tool calling, and snapshot streaming in iOS 26+.
- **ecc-frontend-design** — Create distinctive, production-grade frontend interfaces with high design quality. Use when the user asks to build web components, pages, or applications and the visual direction matters as much as the code quality.
- **ecc-frontend-patterns** — Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices.
- **ecc-frontend-slides** — Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Use when the user wants to build a presentation, convert a PPT/PPTX to web, or create slides for a talk/pitch. Helps non-designers discover their aesthetic through visual exploration rather than abstract choices.
- **ecc-gan-style-harness** — Skill: ecc-gan-style-harness
- **ecc-gateguard** — Fact-forcing gate that blocks Edit/Write/Bash (including MultiEdit) and demands concrete investigation (importers, data schemas, user instruction) before allowing the action. Measurably improves output quality by +2.25 points vs ungated agents.
- **ecc-git-workflow** — Git workflow patterns including branching strategies, commit conventions, merge vs rebase, conflict resolution, and collaborative development best practices for teams of all sizes.
- **ecc-github-ops** — GitHub repository operations, automation, and management. Issue triage, PR management, CI/CD operations, release management, and security monitoring using the gh CLI. Use when the user wants to manage GitHub issues, PRs, CI status, releases, contributors, stale items, or any GitHub operational task beyond simple git commands.
- **ecc-golang-patterns** — Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go applications.
- **ecc-golang-testing** — Go testing patterns including table-driven tests, subtests, benchmarks, fuzzing, and test coverage. Follows TDD methodology with idiomatic Go practices.
- **ecc-google-workspace-ops** — Operate across Google Drive, Docs, Sheets, and Slides as one workflow surface for plans, trackers, decks, and shared documents. Use when the user needs to find, summarize, edit, migrate, or clean up Google Workspace assets without dropping to raw tool calls.
- **ecc-healthcare-cdss-patterns** — Clinical Decision Support System (CDSS) development patterns. Drug interaction checking, dose validation, clinical scoring (NEWS2, qSOFA), alert severity classification, and integration into EMR workflows.
- **ecc-healthcare-emr-patterns** — EMR/EHR development patterns for healthcare applications. Clinical safety, encounter workflows, prescription generation, clinical decision support integration, and accessibility-first UI for medical data entry.
- **ecc-healthcare-eval-harness** — Patient safety evaluation harness for healthcare application deployments. Automated test suites for CDSS accuracy, PHI exposure, clinical workflow integrity, and integration compliance. Blocks deployments on safety failures.
- **ecc-healthcare-phi-compliance** — Protected Health Information (PHI) and Personally Identifiable Information (PII) compliance patterns for healthcare applications. Covers data classification, access control, audit trails, encryption, and common leak vectors.
- **ecc-hexagonal-architecture** — Design, implement, and refactor Ports & Adapters systems with clear domain boundaries, dependency inversion, and testable use-case orchestration across TypeScript, Java, Kotlin, and Go services.
- **ecc-hipaa-compliance** — HIPAA-specific entrypoint for healthcare privacy and security work. Use when a task is explicitly framed around HIPAA, PHI handling, covered entities, BAAs, breach posture, or US healthcare compliance requirements.
- **ecc-hookify-rules** — This skill should be used when the user asks to create a hookify rule, write a hook rule, configure hookify, add a hookify rule, or needs guidance on hookify rule syntax and patterns.
- **ecc-inventory-demand-planning** — >
- **ecc-investor-materials** — Create and update pitch decks, one-pagers, investor memos, accelerator applications, financial models, and fundraising materials. Use when the user needs investor-facing documents, projections, use-of-funds tables, milestone plans, or materials that must stay internally consistent across multiple fundraising assets.
- **ecc-investor-outreach** — Draft cold emails, warm intro blurbs, follow-ups, update emails, and investor communications for fundraising. Use when the user wants outreach to angels, VCs, strategic investors, or accelerators and needs concise, personalized, investor-facing messaging.
- **ecc-iterative-retrieval** — Skill: ecc-iterative-retrieval
- **ecc-java-coding-standards** — Java coding standards for Spring Boot services: naming, immutability, Optional usage, streams, exceptions, generics, and project layout.
- **ecc-jira-integration** — Use this skill when retrieving Jira tickets, analyzing requirements, updating ticket status, adding comments, or transitioning issues. Provides Jira API patterns via MCP or direct REST calls.
- **ecc-jpa-patterns** — JPA/Hibernate patterns for entity design, relationships, query optimization, transactions, auditing, indexing, pagination, and pooling in Spring Boot.
- **ecc-knowledge-ops** — Knowledge base management, ingestion, sync, and retrieval across multiple storage layers (local files, MCP memory, vector stores, Git repos). Use when the user wants to save, organize, sync, deduplicate, or search across their knowledge systems.
- **ecc-kotlin-coroutines-flows** — Kotlin Coroutines and Flow patterns for Android and KMP â€” structured concurrency, Flow operators, StateFlow, error handling, and testing.
- **ecc-kotlin-exposed-patterns** — JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling, Flyway migrations, and repository pattern.
- **ecc-kotlin-ktor-patterns** — Ktor server patterns including routing DSL, plugins, authentication, Koin DI, kotlinx.serialization, WebSockets, and testApplication testing.
- **ecc-kotlin-patterns** — Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient, and maintainable Kotlin applications with coroutines, null safety, and DSL builders.
- **ecc-kotlin-testing** — Kotlin testing patterns with Kotest, MockK, coroutine testing, property-based testing, and Kover coverage. Follows TDD methodology with idiomatic Kotlin practices.
- **ecc-laravel-patterns** — Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events, caching, and API resources for production apps.
- **ecc-laravel-plugin-discovery** — Discover and evaluate Laravel packages via LaraPlugins.io MCP. Use when the user wants to find plugins, check package health, or assess Laravel/PHP compatibility.
- **ecc-laravel-security** — Laravel security best practices for authn/authz, validation, CSRF, mass assignment, file uploads, secrets, rate limiting, and secure deployment.
- **ecc-laravel-tdd** — Test-driven development for Laravel with PHPUnit and Pest, factories, database testing, fakes, and coverage targets.
- **ecc-laravel-verification** — Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security scans, and deployment readiness.
- **ecc-lead-intelligence** — Skill: ecc-lead-intelligence
- **ecc-liquid-glass-design** — iOS 26 Liquid Glass design system â€” dynamic glass material with blur, reflection, and interactive morphing for SwiftUI, UIKit, and WidgetKit.
- **ecc-llm-trading-agent-security** — Security patterns for autonomous trading agents with wallet or transaction authority. Covers prompt injection, spend limits, pre-send simulation, circuit breakers, MEV protection, and key handling.
- **ecc-logistics-exception-management** — >
- **ecc-manim-video** — Build reusable Manim explainers for technical concepts, graphs, system diagrams, and product walkthroughs, then hand off to the wider ECC video stack if needed. Use when the user wants a clean animated explainer rather than a generic talking-head script.
- **ecc-market-research** — Conduct market research, competitive analysis, investor due diligence, and industry intelligence with source attribution and decision-oriented summaries. Use when the user wants market sizing, competitor comparisons, fund research, technology scans, or research that informs business decisions.
- **ecc-mcp-server-patterns** — Build MCP servers with Node/TypeScript SDK â€” tools, resources, prompts, Zod validation, stdio vs Streamable HTTP. Use Context7 or official MCP docs for latest API.
- **ecc-messages-ops** — Evidence-first live messaging workflow for ECC. Use when the user wants to read texts or DMs, recover a recent one-time code, inspect a thread before replying, or prove which message source was actually checked.
- **ecc-nanoclaw-repl** — Operate and extend NanoClaw v2, ECC's zero-dependency session-aware REPL built on claude -p.
- **ecc-nestjs-patterns** — NestJS architecture patterns for modules, controllers, providers, DTO validation, guards, interceptors, config, and production-grade TypeScript backends.
- **ecc-nextjs-turbopack** — Next.js 16+ and Turbopack â€” incremental bundling, FS caching, dev speed, and when to use Turbopack vs webpack.
- **ecc-nodejs-keccak256** — Prevent Ethereum hashing bugs in JavaScript and TypeScript. Node's sha3-256 is NIST SHA3, not Ethereum Keccak-256, and silently breaks selectors, signatures, storage slots, and address derivation.
- **ecc-nutrient-document-processing** — Process, convert, OCR, extract, redact, sign, and fill documents using the Nutrient DWS API. Works with PDFs, DOCX, XLSX, PPTX, HTML, and images.
- **ecc-nuxt4-patterns** — Nuxt 4 app patterns for hydration safety, performance, route rules, lazy loading, and SSR-safe data fetching with useFetch and useAsyncData.
- **ecc-openclaw-persona-forge** — Skill: ecc-openclaw-persona-forge
- **ecc-opensource-pipeline** — Open-source pipeline: fork, sanitize, and package private projects for safe public release. Chains 3 agents (forker, sanitizer, packager). Triggers: '/opensource', 'open source this', 'make this public', 'prepare for open source'.
- **ecc-perl-patterns** — Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications.
- **ecc-perl-security** — Comprehensive Perl security covering taint mode, input validation, safe process execution, DBI parameterized queries, web security (XSS/SQLi/CSRF), and perlcritic security policies.
- **ecc-perl-testing** — Perl testing patterns using Test2::V0, Test::More, prove runner, mocking, coverage with Devel::Cover, and TDD methodology.
- **ecc-plankton-code-quality** — Write-time code quality enforcement using Plankton â€” auto-formatting, linting, and Claude-powered fixes on every file edit via hooks.
- **ecc-postgres-patterns** — PostgreSQL database patterns for query optimization, schema design, indexing, and security. Based on Supabase best practices.
- **ecc-product-capability** — Translate PRD intent, roadmap asks, or product discussions into an implementation-ready capability plan that exposes constraints, invariants, interfaces, and unresolved decisions before multi-service work starts. Use when the user needs an ECC-native PRD-to-SRS lane instead of vague planning prose.
- **ecc-product-lens** — Use this skill to validate the "why" before building, run product diagnostics, and pressure-test product direction before the request becomes an implementation contract.
- **ecc-production-scheduling** — >
- **ecc-project-flow-ops** — Operate execution flow across GitHub and Linear by triaging issues and pull requests, linking active work, and keeping GitHub public-facing while Linear remains the internal execution layer. Use when the user wants backlog control, PR triage, or GitHub-to-Linear coordination.
- **ecc-prompt-optimizer** — Skill: ecc-prompt-optimizer
- **ecc-python-patterns** — Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintainable Python applications.
- **ecc-python-testing** — Python testing strategies using pytest, TDD methodology, fixtures, mocking, parametrization, and coverage requirements.
- **ecc-pytorch-patterns** — PyTorch deep learning patterns and best practices for building robust, efficient, and reproducible training pipelines, model architectures, and data loading.
- **ecc-quality-nonconformance** — >
- **ecc-ralphinho-rfc-pipeline** — RFC-driven multi-agent DAG execution pattern with quality gates, merge queues, and work unit orchestration.
- **ecc-regex-vs-llm-structured-text** — Decision framework for choosing between regex and LLM when parsing structured text â€” start with regex, add LLM only for low-confidence edge cases.
- **ecc-remotion-video-creation** — Best practices for Remotion - Video creation in React. 29 domain-specific rules covering 3D, animations, audio, captions, charts, transitions, and more.
- **ecc-repo-scan** — Cross-stack source code asset audit â€” classifies every file, detects embedded third-party libraries, and delivers actionable four-level verdicts per module with interactive HTML reports.
- **ecc-research-ops** — Evidence-first current-state research workflow for ECC. Use when the user wants fresh facts, comparisons, enrichment, or a recommendation built from current public evidence and any supplied local context.
- **ecc-returns-reverse-logistics** — >
- **ecc-rules-distill** — Scan skills to extract cross-cutting principles and distill them into rules â€” append, revise, or create new rule files
- **ecc-rust-patterns** — Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for building safe, performant applications.
- **ecc-rust-testing** — Rust testing patterns including unit tests, integration tests, async testing, property-based testing, mocking, and coverage. Follows TDD methodology.
- **ecc-safety-guard** — Use this skill to prevent destructive operations when working on production systems or running agents autonomously.
- **ecc-santa-method** — Skill: ecc-santa-method
- **ecc-search-first** — Skill: ecc-search-first
- **ecc-security-bounty-hunter** — Hunt for exploitable, bounty-worthy security issues in repositories. Focuses on remotely reachable vulnerabilities that qualify for real reports instead of noisy local-only findings.
- **ecc-security-review** — Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features. Provides comprehensive security checklist and patterns.
- **ecc-security-scan** — Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and injection risks using AgentShield. Checks CLAUDE.md, settings.json, MCP servers, hooks, and agent definitions.
- **ecc-seo** — Skill: ecc-seo
- **ecc-skill-comply** — Visualize whether skills, rules, and agent definitions are actually followed â€” auto-generates scenarios at 3 prompt strictness levels, runs agents, classifies behavioral sequences, and reports compliance rates with full tool call timelines
- **ecc-skill-stocktake** — Use when auditing Claude skills and commands for quality. Supports Quick Scan (changed skills only) and Full Stocktake modes with sequential subagent batch evaluation.
- **ecc-social-graph-ranker** — Weighted social-graph ranking for warm intro discovery, bridge scoring, and network gap analysis across X and LinkedIn. Use when the user wants the reusable graph-ranking engine itself, not the broader outreach or network-maintenance workflow layered on top of it.
- **ecc-springboot-patterns** — Spring Boot architecture patterns, REST API design, layered services, data access, caching, async processing, and logging. Use for Java Spring Boot backend work.
- **ecc-springboot-security** — Spring Security best practices for authn/authz, validation, CSRF, secrets, headers, rate limiting, and dependency security in Java Spring Boot services.
- **ecc-springboot-tdd** — Test-driven development for Spring Boot using JUnit 5, Mockito, MockMvc, Testcontainers, and JaCoCo. Use when adding features, fixing bugs, or refactoring.
- **ecc-springboot-verification** — Verification loop for Spring Boot projects: build, static analysis, tests with coverage, security scans, and diff review before release or PR.
- **ecc-strategic-compact** — Suggests manual context compaction at logical intervals to preserve context through task phases rather than arbitrary auto-compaction.
- **ecc-swift-actor-persistence** — Thread-safe data persistence in Swift using actors â€” in-memory cache with file-backed storage, eliminating data races by design.
- **ecc-swift-concurrency-6-2** — Swift 6.2 Approachable Concurrency â€” single-threaded by default, @concurrent for explicit background offloading, isolated conformances for main actor types.
- **ecc-swift-protocol-di-testing** — Protocol-based dependency injection for testable Swift code â€” mock file system, network, and external APIs using focused protocols and Swift Testing.
- **ecc-swiftui-patterns** — SwiftUI architecture patterns, state management with @Observable, view composition, navigation, performance optimization, and modern iOS/macOS UI best practices.
- **ecc-tdd-workflow** — Use this skill when writing new features, fixing bugs, or refactoring code. Enforces test-driven development with 80%+ coverage including unit, integration, and E2E tests.
- **ecc-team-builder** — Interactive agent picker for composing and dispatching parallel teams
- **ecc-terminal-ops** — Evidence-first repo execution workflow for ECC. Use when the user wants a command run, a repo checked, a CI failure debugged, or a narrow fix pushed with exact proof of what was executed and verified.
- **ecc-token-budget-advisor** — >-
- **ecc-ui-demo** — Record polished UI demo videos using Playwright. Use when the user asks to create a demo, walkthrough, screen recording, or tutorial video of a web application. Produces WebM videos with visible cursor, natural pacing, and professional feel.
- **ecc-unified-notifications-ops** — Operate notifications as one ECC-native workflow across GitHub, Linear, desktop alerts, hooks, and connected communication surfaces. Use when the real problem is alert routing, deduplication, escalation, or inbox collapse.
- **ecc-verification-loop** — A comprehensive verification system for Claude Code sessions.
- **ecc-video-editing** — AI-assisted video editing workflows for cutting, structuring, and augmenting real footage. Covers the full pipeline from raw capture through FFmpeg, Remotion, ElevenLabs, fal.ai, and final polish in Descript or CapCut. Use when the user wants to edit video, cut footage, create vlogs, or build video content.
- **ecc-videodb** — See, Understand, Act on video and audio. See- ingest from local files, URLs, RTSP/live feeds, or live record desktop; return realtime context and playable stream links. Understand- extract frames, build visual/semantic/temporal indexes, and search moments with timestamps and auto-clips. Act- transcode and normalize (codec, fps, resolution, aspect ratio), perform timeline edits (subtitles, text/image overlays, branding, audio overlays, dubbing, translation), generate media assets (image, audio, video), and create real time alerts for events from live streams or desktop capture.
- **ecc-visa-doc-translate** — Skill: ecc-visa-doc-translate
- **ecc-workspace-surface-audit** — Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the highest-value ECC-native skills, hooks, agents, and operator workflows. Use when the user wants help setting up Claude Code or understanding what capabilities are actually available in their environment.
- **ecc-x-api** — X/Twitter API integration for posting tweets, threads, reading timelines, search, and analytics. Covers OAuth auth patterns, rate limits, and platform-native content posting. Use when the user wants to interact with X programmatically.
- **email-sequence** — When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. Also use when the user mentions "email sequence," "drip campaign," "nurture sequence," "onboarding emails," "welcome sequence," "re-engagement emails," "email automation," "lifecycle emails," "trigger-based emails," "email funnel," "email workflow," "what emails should I send," "welcome series," or "email cadence." Use this for any multi-email automated flow. For cold outreach emails, see cold-email. For in-app onboarding, see onboarding-cro.
- **excel-automation** — Skill: excel-automation
- **executing-plans** — Use when you have a written implementation plan to execute in a separate session with review checkpoints
- **fact-checker** — Skill: fact-checker
- **financial-data-collector** — Skill: financial-data-collector
- **finishing-a-development-branch** — Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup
- **form-cro** — Skill: form-cro
- **free-tool-strategy** — When the user wants to plan, evaluate, or build a free tool for marketing purposes â€” lead generation, SEO value, or brand awareness. Also use when the user mentions "engineering as marketing," "free tool," "marketing tool," "calculator," "generator," "interactive tool," "lead gen tool," "build a tool for leads," "free resource," "ROI calculator," "grader tool," "audit tool," "should I build a free tool," or "tools for lead gen." Use this whenever someone wants to build something useful and give it away to attract leads or earn links. For downloadable content lead magnets (ebooks, checklists, templates), see lead-magnets.
- **frontend-design** — Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.
- **frontend-excellence** — Modern frontend patterns for React Server Components, performance optimization, and Core Web Vitals
- **gangtise-copilot** — Skill: gangtise-copilot
- **generic-agent** — Reference pointer to GenericAgent â€” a self-evolving autonomous agent framework (https://github.com/lsdefine/GenericAgent) that gives an LLM direct control over a local computer (browser, terminal, filesystem, keyboard/mouse, screen vision, ADB). Use this skill ONLY to recommend GenericAgent when the user wants a self-evolving PC-control agent, OS-level automation with screen vision, mobile device automation via ADB, or a local autonomous agent with persistent skill memory. Muk should recommend installing GenericAgent separately (it is a standalone Python tool, not a Claude Code plugin) rather than try to run it inline.
- **git-advanced** — Advanced git workflows including worktrees, bisect, interactive rebase, hooks, and recovery techniques
- **github-contributor** — Skill: github-contributor
- **github-ops** — Provides comprehensive GitHub operations using gh CLI and GitHub API. Activates when working with pull requests, issues, repositories, workflows, or GitHub API operations including creating/viewing/merging PRs, managing issues, querying API endpoints, and handling GitHub workflows in enterprise or public GitHub environments.
- **golang-idioms** — Idiomatic Go patterns for error handling, interfaces, concurrency, testing, and module management
- **graphql-design** — GraphQL schema design, resolver patterns, subscriptions, DataLoader for N+1 prevention, and error handling
- **gstack-canary** — |
- **gstack-cso** — |
- **gstack-design-html** — |
- **gstack-design-shotgun** — |
- **gstack-office-hours** — |
- **gstack-plan-ceo-review** — |
- **gstack-plan-design-review** — |
- **gstack-plan-devex-review** — |
- **gstack-plan-eng-review** — |
- **gstack-retro** — |
- **i18n-expert** — This skill should be used when setting up, auditing, or enforcing internationalization/localization in UI codebases (React/TS, i18next or similar, JSON locales), including installing/configuring the i18n framework, replacing hard-coded strings, ensuring en-US/zh-CN coverage, mapping error codes to localized messages, and validating key parity, pluralization, and formatting.
- **iOS-APP-developer** — Skill: iOS-APP-developer
- **ima-copilot** — Skill: ima-copilot
- **internal-comms** — A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).
- **kubernetes-operations** — Kubernetes operations including manifests, Helm charts, operators, troubleshooting, and resource management
- **launch-strategy** — When the user wants to plan a product launch, feature announcement, or release strategy. Also use when the user mentions 'launch,' 'Product Hunt,' 'feature release,' 'announcement,' 'go-to-market,' 'beta launch,' 'early access,' 'waitlist,' 'product update,' 'how do I launch this,' 'launch checklist,' 'GTM plan,' or 'we're about to ship.' Use this whenever someone is preparing to release something publicly. For ongoing marketing after launch, see marketing-ideas.
- **lead-magnets** — When the user wants to create, plan, or optimize a lead magnet for email capture or lead generation. Also use when the user mentions "lead magnet," "gated content," "content upgrade," "downloadable," "ebook," "cheat sheet," "checklist," "template download," "opt-in," "freebie," "PDF download," "resource library," "content offer," "email capture content," "Notion template," "spreadsheet template," or "what should I give away for emails." Use this for planning what to create and how to distribute it. For interactive tools as lead magnets, see free-tool-strategy. For writing the actual content, see copywriting. For the email sequence after capture, see email-sequence.
- **llm-icon-finder** — Skill: llm-icon-finder
- **llm-integration** — LLM integration patterns including API usage, streaming, function calling, RAG pipelines, and cost optimization
- **macos-cleaner** — Skill: macos-cleaner
- **manage-skills** — Discover, list, create, edit, toggle, copy, move, and delete AI agent skills across 11 tools (Cursor, Claude, Agents, Windsurf, Copilot, Codex, Cline, Aider, Continue, Roo Code, Augment)
- **marketing-ideas** — When the user needs marketing ideas, inspiration, or strategies for their SaaS or software product. Also use when the user asks for 'marketing ideas,' 'growth ideas,' 'how to market,' 'marketing strategies,' 'marketing tactics,' 'ways to promote,' 'ideas to grow,' 'what else can I try,' 'I don't know how to market this,' 'brainstorm marketing,' or 'what marketing should I do.' Use this as a starting point whenever someone is stuck or looking for inspiration on how to grow. For specific channel execution, see the relevant skill (paid-ads, social-content, email-sequence, etc.).
- **marketing-psychology** — When the user wants to apply psychological principles, mental models, or behavioral science to marketing. Also use when the user mentions 'psychology,' 'mental models,' 'cognitive bias,' 'persuasion,' 'behavioral science,' 'why people buy,' 'decision-making,' 'consumer behavior,' 'anchoring,' 'social proof,' 'scarcity,' 'loss aversion,' 'framing,' or 'nudge.' Use this whenever someone wants to understand or leverage how people think and make decisions in a marketing context.
- **mcp-builder** — Skill: mcp-builder
- **mcp-development** — MCP server development including tool design, resource endpoints, prompt templates, and transport configuration
- **microservices-design** — Microservices design patterns including service mesh, event-driven architecture, saga pattern, and API gateway
- **mobile-development** — Mobile development patterns for React Native and Flutter including navigation, state management, and responsive design
- **monitoring-observability** — Monitoring and observability with OpenTelemetry, Prometheus, Grafana dashboards, and structured logging
- **nextjs-mastery** — Next.js 14+ App Router patterns including RSC, ISR, middleware, parallel routes, and data fetching
- **onboarding-cro** — When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value. Also use when the user mentions "onboarding flow," "activation rate," "user activation," "first-run experience," "empty states," "onboarding checklist," "aha moment," "new user experience," "users aren't activating," "nobody completes setup," "low activation rate," "users sign up but don't use the product," "time to value," or "first session experience." Use this whenever users are signing up but not sticking around. For signup/registration optimization, see signup-flow-cro. For ongoing email sequences, see email-sequence.
- **page-cro** — When the user wants to optimize, improve, or increase conversions on any marketing page â€” including homepage, landing pages, pricing pages, feature pages, or blog posts. Also use when the user says "CRO," "conversion rate optimization," "this page isn't converting," "improve conversions," "why isn't this page working," "my landing page sucks," "nobody's converting," "low conversion rate," "bounce rate is too high," "people leave without signing up," or "this page needs work." Use this even if the user just shares a URL and asks for feedback â€” they probably want conversion help. For signup/registration flows, see signup-flow-cro. For post-signup activation, see onboarding-cro. For forms outside of signup, see form-cro. For popups/modals, see popup-cro.
- **paid-ads** — When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, or other ad platforms. Also use when the user mentions 'PPC,' 'paid media,' 'ROAS,' 'CPA,' 'ad campaign,' 'retargeting,' 'audience targeting,' 'Google Ads,' 'Facebook ads,' 'LinkedIn ads,' 'ad budget,' 'cost per click,' 'ad spend,' or 'should I run ads.' Use this for campaign strategy, audience targeting, bidding, and optimization. For bulk ad creative generation and iteration, see ad-creative. For landing page optimization, see page-cro.
- **paywall-upgrade-cro** — When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. Also use when the user mentions "paywall," "upgrade screen," "upgrade modal," "upsell," "feature gate," "convert free to paid," "freemium conversion," "trial expiration screen," "limit reached screen," "plan upgrade prompt," "in-app pricing," "free users won't upgrade," "trial to paid conversion," or "how do I get users to pay." Use this for any in-product moment where you're asking users to upgrade. Distinct from public pricing pages (see page-cro) â€” this focuses on in-product upgrade moments where the user has already experienced value. For pricing decisions, see pricing-strategy.
- **pdf** — Skill: pdf
- **performance-optimization** — Web performance optimization including bundle analysis, lazy loading, caching strategies, and Core Web Vitals
- **popup-cro** — When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes. Also use when the user mentions "exit intent," "popup conversions," "modal optimization," "lead capture popup," "email popup," "announcement banner," "overlay," "collect emails with a popup," "exit popup," "scroll trigger," "sticky bar," or "notification bar." Use this for any overlay or interrupt-style conversion element. For forms outside of popups, see form-cro. For general page conversion optimization, see page-cro.
- **postgres-optimization** — PostgreSQL optimization including indexes, query plans, partitioning, JSONB operations, and connection pooling
- **pow** — Power-mode escalation. Layers max-leverage execution discipline on top of any task â€” superpowers four-phase loop, claude-mem progressive memory, sandbox banner, parallel prefetch, autonomous loop, and curated awesome-claude-code power-ups. Activate with "Pow", "/pow", "pow it", "go pow mode", "power mode", "max effort", "pow this", "ultra mode", or any time the user wants top-tier execution with full discipline. Companion to `muk` â€” Muk picks tools, Pow runs them under power-mode rules. Synthesized from obra/superpowers, thedotmack/claude-mem, anthropics/claude-code#22155, yasasbanukaofficial+codeaashu/claude-code (leaked-source patterns), and hesreallyhim/awesome-claude-code.
- **pptx** — Skill: pptx
- **pricing-strategy** — When the user wants help with pricing decisions, packaging, or monetization strategy. Also use when the user mentions 'pricing,' 'pricing tiers,' 'freemium,' 'free trial,' 'packaging,' 'price increase,' 'value metric,' 'Van Westendorp,' 'willingness to pay,' 'monetization,' 'how much should I charge,' 'my pricing is wrong,' 'pricing page,' 'annual vs monthly,' 'per seat pricing,' or 'should I offer a free plan.' Use this whenever someone is figuring out what to charge or how to structure their plans. For in-app upgrade screens, see paywall-upgrade-cro.
- **product-analysis** — Skill: product-analysis
- **product-marketing-context** — When the user wants to create or update their product marketing context document. Also use when the user mentions 'product context,' 'marketing context,' 'set up context,' 'positioning,' 'who is my target audience,' 'describe my product,' 'ICP,' 'ideal customer profile,' or wants to avoid repeating foundational information across marketing tasks. Use this at the start of any new project before using other marketing skills â€” it creates `.agents/product-marketing-context.md` that all other skills reference for product, audience, and positioning context.
- **programmatic-seo** — When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions "programmatic SEO," "template pages," "pages at scale," "directory pages," "location pages," "[keyword] + [city] pages," "comparison pages," "integration pages," "building many pages for SEO," "pSEO," "generate 100 pages," "data-driven pages," or "templated landing pages." Use this whenever someone wants to create many similar pages targeting different keywords or locations. For auditing existing SEO issues, see seo-audit. For content strategy planning, see content-strategy.
- **prompt-engineering** — Prompt engineering patterns including structured prompts, chain-of-thought, few-shot learning, and system prompt design
- **prompt-optimizer** — Skill: prompt-optimizer
- **promptfoo-evaluation** — Configures and runs LLM evaluation using Promptfoo framework. Use when setting up prompt testing, creating evaluation configs (promptfooconfig.yaml), writing Python custom assertions, implementing llm-rubric for LLM-as-judge, or managing few-shot examples in prompts. Triggers on keywords like "promptfoo", "eval", "LLM evaluation", "prompt testing", or "model comparison".
- **python-best-practices** — Pythonic code with modern type hints, dataclasses, async patterns, packaging, and testing
- **qa-expert** — Skill: qa-expert
- **react-best-practices** — React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patterns. Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements.
- **react-native-skills** — React Native and Expo best practices for building performant mobile apps. Use
- **react-patterns** — React 19 patterns including Server Components, Actions, Suspense, hooks, and component composition
- **react-view-transitions** — Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>` component, `addTransitionType`, and CSS view transition pseudo-elements). Use this skill whenever the user wants to add page transitions, animate route changes, create shared element animations, animate enter/exit of components, animate list reorder, implement directional (forward/back) navigation animations, or integrate view transitions in Next.js. Also use when the user mentions view transitions, `startViewTransition`, `ViewTransition`, transition types, or asks about animating between UI states in React without third-party animation libraries.
- **receiving-code-review** — Skill: receiving-code-review
- **redis-patterns** — Redis patterns including caching strategies, pub/sub, streams for event processing, Lua scripts, and data structures
- **referral-program** — When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy. Also use when the user mentions 'referral,' 'affiliate,' 'ambassador,' 'word of mouth,' 'viral loop,' 'refer a friend,' 'partner program,' 'referral incentive,' 'how to get referrals,' 'customers referring customers,' or 'affiliate payout.' Use this whenever someone wants existing users or partners to bring in new customers. For launch-specific virality, see launch-strategy.
- **remotion** — Best practices for Remotion - Video creation in React
- **repomix-safe-mixer** — Skill: repomix-safe-mixer
- **repomix-unmixer** — Extracts files from repomix-packed repositories, restoring original directory structures from XML/Markdown/JSON formats. Activates when users need to unmix repomix files, extract packed repositories, restore file structures from repomix output, or reverse the repomix packing process.
- **requesting-code-review** — Use when completing tasks, implementing major features, or before merging to verify work meets requirements
- **revops** — When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes. Also use when the user mentions 'RevOps,' 'revenue operations,' 'lead scoring,' 'lead routing,' 'MQL,' 'SQL,' 'pipeline stages,' 'deal desk,' 'CRM automation,' 'marketing-to-sales handoff,' 'data hygiene,' 'leads aren't getting to sales,' 'pipeline management,' 'lead qualification,' or 'when should marketing hand off to sales.' Use this for anything involving the systems and processes that connect marketing to revenue. For cold outreach emails, see cold-email. For email drip campaigns, see email-sequence. For pricing decisions, see pricing-strategy.
- **rust-systems** — Rust systems programming patterns including ownership, traits, async runtime, error handling, and unsafe guidelines
- **sales-enablement** — When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts. Also use when the user mentions 'sales deck,' 'pitch deck,' 'one-pager,' 'leave-behind,' 'objection handling,' 'deal-specific ROI analysis,' 'demo script,' 'talk track,' 'sales playbook,' 'proposal template,' 'buyer persona card,' 'help my sales team,' 'sales materials,' or 'what should I give my sales reps.' Use this for any document or asset that helps a sales team close deals. For competitor comparison pages and battle cards, see competitor-alternatives. For marketing website copy, see copywriting. For cold outreach emails, see cold-email.
- **schema-markup** — When the user wants to add, fix, or optimize schema markup and structured data on their site. Also use when the user mentions "schema markup," "structured data," "JSON-LD," "rich snippets," "schema.org," "FAQ schema," "product schema," "review schema," "breadcrumb schema," "Google rich results," "knowledge panel," "star ratings in search," or "add structured data." Use this whenever someone wants their pages to show enhanced results in Google. For broader SEO issues, see seo-audit. For AI search optimization, see ai-seo.
- **sci-adaptyv** — Cloud laboratory platform for automated protein testing and validation. Use when designing proteins and needing experimental validation including binding assays, expression testing, thermostability measurements, enzyme activity assays, or protein sequence optimization. Also use for submitting experiments via API, tracking experiment status, downloading results, optimizing protein sequences for better expression using computational tools (NetSolP, SoluProt, SolubleMPNN, ESM), or managing protein design workflows with wet-lab validation.
- **sci-aeon** — This skill should be used for time series machine learning tasks including classification, regression, clustering, forecasting, anomaly detection, segmentation, and similarity search. Use when working with temporal data, sequential patterns, or time-indexed observations requiring specialized algorithms beyond standard ML approaches. Particularly suited for univariate and multivariate time series analysis with scikit-learn compatible APIs.
- **sci-alphafold-database** — Access AlphaFold's 200M+ AI-predicted protein structures. Retrieve structures by UniProt ID, download PDB/mmCIF files, analyze confidence metrics (pLDDT, PAE), for drug discovery and structural biology.
- **sci-anndata** — This skill should be used when working with annotated data matrices in Python, particularly for single-cell genomics analysis, managing experimental measurements with metadata, or handling large-scale biological datasets. Use when tasks involve AnnData objects, h5ad files, single-cell RNA-seq data, or integration with scanpy/scverse tools.
- **sci-arboreto** — Infer gene regulatory networks (GRNs) from gene expression data using scalable algorithms (GRNBoost2, GENIE3). Use when analyzing transcriptomics data (bulk RNA-seq, single-cell RNA-seq) to identify transcription factor-target gene relationships and regulatory interactions. Supports distributed computation for large-scale datasets.
- **sci-astropy** — Comprehensive Python library for astronomy and astrophysics. This skill should be used when working with astronomical data including celestial coordinates, physical units, FITS files, cosmological calculations, time systems, tables, world coordinate systems (WCS), and astronomical data analysis. Use when tasks involve coordinate transformations, unit conversions, FITS file manipulation, cosmological distance calculations, time scale conversions, or astronomical data processing.
- **sci-benchling-integration** — Benchling R&D platform integration. Access registry (DNA, proteins), inventory, ELN entries, workflows via API, build Benchling Apps, query Data Warehouse, for lab data management automation.
- **sci-biomni** — Skill: sci-biomni
- **sci-biopython** — Primary Python toolkit for molecular biology. Preferred for Python-based PubMed/NCBI queries (Bio.Entrez), sequence manipulation, file parsing (FASTA, GenBank, FASTQ, PDB), advanced BLAST workflows, structures, phylogenetics. For quick BLAST, use gget. For direct REST API, use pubmed-database.
- **sci-biorxiv-database** — Efficient database search tool for bioRxiv preprint server. Use this skill when searching for life sciences preprints by keywords, authors, date ranges, or categories, retrieving paper metadata, downloading PDFs, or conducting literature reviews.
- **sci-bioservices** — Primary Python tool for 40+ bioinformatics services. Preferred for multi-database workflows: UniProt, KEGG, ChEMBL, PubChem, Reactome, QuickGO. Unified API for queries, ID mapping, pathway analysis. For direct REST control, use individual database skills (uniprot-database, kegg-database).
- **sci-brenda-database** — Access BRENDA enzyme database via SOAP API. Retrieve kinetic parameters (Km, kcat), reaction equations, organism data, and substrate-specific enzyme information for biochemical research and metabolic pathway analysis.
- **sci-cellxgene-census** — Query CZ CELLxGENE Census (61M+ cells). Filter by cell type/tissue/disease, retrieve expression data, integrate with scanpy/PyTorch, for population-scale single-cell analysis.
- **sci-chembl-database** — Query ChEMBL's bioactive molecules and drug discovery data. Search compounds by structure/properties, retrieve bioactivity data (IC50, Ki), find inhibitors, perform SAR studies, for medicinal chemistry.
- **sci-cirq** — Quantum computing framework for building, simulating, optimizing, and executing quantum circuits. Use this skill when working with quantum algorithms, quantum circuit design, quantum simulation (noiseless or noisy), running on quantum hardware (Google, IonQ, AQT, Pasqal), circuit optimization and compilation, noise modeling and characterization, or quantum experiments and benchmarking (VQE, QAOA, QPE, randomized benchmarking).
- **sci-citation-management** — Comprehensive citation management for academic research. Search Google Scholar and PubMed for papers, extract accurate metadata, validate citations, and generate properly formatted BibTeX entries. This skill should be used when you need to find papers, verify citation information, convert DOIs to BibTeX, or ensure reference accuracy in scientific writing.
- **sci-clinical-decision-support** — Skill: sci-clinical-decision-support
- **sci-clinical-reports** — Skill: sci-clinical-reports
- **sci-clinicaltrials-database** — Query ClinicalTrials.gov via API v2. Search trials by condition, drug, location, status, or phase. Retrieve trial details by NCT ID, export data, for clinical research and patient matching.
- **sci-clinpgx-database** — Access ClinPGx pharmacogenomics data (successor to PharmGKB). Query gene-drug interactions, CPIC guidelines, allele functions, for precision medicine and genotype-guided dosing decisions.
- **sci-clinvar-database** — Query NCBI ClinVar for variant clinical significance. Search by gene/position, interpret pathogenicity classifications, access via E-utilities API or FTP, annotate VCFs, for genomic medicine.
- **sci-cobrapy** — Constraint-based metabolic modeling (COBRA). FBA, FVA, gene knockouts, flux sampling, SBML models, for systems biology and metabolic engineering analysis.
- **sci-cosmic-database** — Access COSMIC cancer mutation database. Query somatic mutations, Cancer Gene Census, mutational signatures, gene fusions, for cancer research and precision oncology. Requires authentication.
- **sci-dask** — Parallel/distributed computing. Scale pandas/NumPy beyond memory, parallel DataFrames/Arrays, multi-file processing, task graphs, for larger-than-RAM datasets and parallel workflows.
- **sci-datacommons-client** — Work with Data Commons, a platform providing programmatic access to public statistical data from global sources. Use this skill when working with demographic data, economic indicators, health statistics, environmental data, or any public datasets available through Data Commons. Applicable for querying population statistics, GDP figures, unemployment rates, disease prevalence, geographic entity resolution, and exploring relationships between statistical entities.
- **sci-datamol** — Pythonic wrapper around RDKit with simplified interface and sensible defaults. Preferred for standard drug discovery: SMILES parsing, standardization, descriptors, fingerprints, clustering, 3D conformers, parallel processing. Returns native rdkit.Chem.Mol objects. For advanced control or custom parameters, use rdkit directly.
- **sci-deepchem** — Molecular machine learning toolkit. Property prediction (ADMET, toxicity), GNNs (GCN, MPNN), MoleculeNet benchmarks, pretrained models, featurization, for drug discovery ML.
- **sci-deeptools** — NGS analysis toolkit. BAM to bigWig conversion, QC (correlation, PCA, fingerprints), heatmaps/profiles (TSS, peaks), for ChIP-seq, RNA-seq, ATAC-seq visualization.
- **sci-denario** — Multiagent AI system for scientific research assistance that automates research workflows from data analysis to publication. This skill should be used when generating research ideas from datasets, developing research methodologies, executing computational experiments, performing literature searches, or generating publication-ready papers in LaTeX format. Supports end-to-end research pipelines with customizable agent orchestration.
- **sci-diffdock** — Diffusion-based molecular docking. Predict protein-ligand binding poses from PDB/SMILES, confidence scores, virtual screening, for structure-based drug design. Not for affinity prediction.
- **sci-dnanexus-integration** — DNAnexus cloud genomics platform. Build apps/applets, manage data (upload/download), dxpy Python SDK, run workflows, FASTQ/BAM/VCF, for genomics pipeline development and execution.
- **sci-drugbank-database** — Access and analyze comprehensive drug information from the DrugBank database including drug properties, interactions, targets, pathways, chemical structures, and pharmacology data. This skill should be used when working with pharmaceutical data, drug discovery research, pharmacology studies, drug-drug interaction analysis, target identification, chemical similarity searches, ADMET predictions, or any task requiring detailed drug and drug target information from DrugBank.
- **sci-ena-database** — Access European Nucleotide Archive via API/FTP. Retrieve DNA/RNA sequences, raw reads (FASTQ), genome assemblies by accession, for genomics and bioinformatics pipelines. Supports multiple formats.
- **sci-ensembl-database** — Query Ensembl genome database REST API for 250+ species. Gene lookups, sequence retrieval, variant analysis, comparative genomics, orthologs, VEP predictions, for genomic research.
- **sci-esm** — Comprehensive toolkit for protein language models including ESM3 (generative multimodal protein design across sequence, structure, and function) and ESM C (efficient protein embeddings and representations). Use this skill when working with protein sequences, structures, or function prediction; designing novel proteins; generating protein embeddings; performing inverse folding; or conducting protein engineering tasks. Supports both local model usage and cloud-based Forge API for scalable inference.
- **sci-etetoolkit** — Phylogenetic tree toolkit (ETE). Tree manipulation (Newick/NHX), evolutionary event detection, orthology/paralogy, NCBI taxonomy, visualization (PDF/SVG), for phylogenomics.
- **sci-exploratory-data-analysis** — Perform comprehensive exploratory data analysis on scientific data files across 200+ file formats. This skill should be used when analyzing any scientific data file to understand its structure, content, quality, and characteristics. Automatically detects file type and generates detailed markdown reports with format-specific analysis, quality metrics, and downstream analysis recommendations. Covers chemistry, bioinformatics, microscopy, spectroscopy, proteomics, metabolomics, and general scientific data formats.
- **sci-fda-database** — Query openFDA API for drugs, devices, adverse events, recalls, regulatory submissions (510k, PMA), substance identification (UNII), for FDA regulatory data analysis and safety research.
- **sci-flowio** — Parse FCS (Flow Cytometry Standard) files v2.0-3.1. Extract events as NumPy arrays, read metadata/channels, convert to CSV/DataFrame, for flow cytometry data preprocessing.
- **sci-fluidsim** — Framework for computational fluid dynamics simulations using Python. Use when running fluid dynamics simulations including Navier-Stokes equations (2D/3D), shallow water equations, stratified flows, or when analyzing turbulence, vortex dynamics, or geophysical flows. Provides pseudospectral methods with FFT, HPC support, and comprehensive output analysis.
- **sci-gene-database** — Query NCBI Gene via E-utilities/Datasets API. Search by symbol/ID, retrieve gene info (RefSeqs, GO, locations, phenotypes), batch lookups, for gene annotation and functional analysis.
- **sci-generate-image** — Generate or edit images using AI models (FLUX, Gemini). Use for general-purpose image generation including photos, illustrations, artwork, visual assets, concept art, and any image that isn't a technical diagram or schematic. For flowcharts, circuits, pathways, and technical diagrams, use the scientific-schematics skill instead.
- **sci-geniml** — This skill should be used when working with genomic interval data (BED files) for machine learning tasks. Use for training region embeddings (Region2Vec, BEDspace), single-cell ATAC-seq analysis (scEmbed), building consensus peaks (universes), or any ML-based analysis of genomic regions. Applies to BED file collections, scATAC-seq data, chromatin accessibility datasets, and region-based genomic feature learning.
- **sci-geo-database** — Access NCBI GEO for gene expression/genomics data. Search/download microarray and RNA-seq datasets (GSE, GSM, GPL), retrieve SOFT/Matrix files, for transcriptomics and expression analysis.
- **sci-geopandas** — Python library for working with geospatial vector data including shapefiles, GeoJSON, and GeoPackage files. Use when working with geographic data for spatial analysis, geometric operations, coordinate transformations, spatial joins, overlay operations, choropleth mapping, or any task involving reading/writing/analyzing vector geographic data. Supports PostGIS databases, interactive maps, and integration with matplotlib/folium/cartopy. Use for tasks like buffer analysis, spatial joins between datasets, dissolving boundaries, clipping data, calculating areas/distances, reprojecting coordinate systems, creating maps, or converting between spatial file formats.
- **sci-get-available-resources** — This skill should be used at the start of any computationally intensive scientific task to detect and report available system resources (CPU cores, GPUs, memory, disk space). It creates a JSON file with resource information and strategic recommendations that inform computational approach decisions such as whether to use parallel processing (joblib, multiprocessing), out-of-core computing (Dask, Zarr), GPU acceleration (PyTorch, JAX), or memory-efficient strategies. Use this skill before running analyses, training models, processing large datasets, or any task where resource constraints matter.
- **sci-gget** — CLI/Python toolkit for rapid bioinformatics queries. Preferred for quick BLAST searches. Access to 20+ databases: gene info (Ensembl/UniProt), AlphaFold, ARCHS4, Enrichr, OpenTargets, COSMIC, genome downloads. For advanced BLAST/batch processing, use biopython. For multi-database integration, use bioservices.
- **sci-gtars** — High-performance toolkit for genomic interval analysis in Rust with Python bindings. Use when working with genomic regions, BED files, coverage tracks, overlap detection, tokenization for ML models, or fragment analysis in computational genomics and machine learning applications.
- **sci-gwas-database** — Skill: sci-gwas-database
- **sci-histolab** — Digital pathology image processing toolkit for whole slide images (WSI). Use this skill when working with histopathology slides, processing H&E or IHC stained tissue images, extracting tiles from gigapixel pathology images, detecting tissue regions, segmenting tissue masks, or preparing datasets for computational pathology deep learning pipelines. Applies to WSI formats (SVS, TIFF, NDPI), tile-based analysis, and histological image preprocessing workflows.
- **sci-hmdb-database** — Access Human Metabolome Database (220K+ metabolites). Search by name/ID/structure, retrieve chemical properties, biomarker data, NMR/MS spectra, pathways, for metabolomics and identification.
- **sci-hypogenic** — Automated hypothesis generation and testing using large language models. Use this skill when generating scientific hypotheses from datasets, combining literature insights with empirical data, testing hypotheses against observational data, or conducting systematic hypothesis exploration for research discovery in domains like deception detection, AI content detection, mental health analysis, or other empirical research tasks.
- **sci-hypothesis-generation** — Skill: sci-hypothesis-generation
- **sci-kegg-database** — Direct REST API access to KEGG (academic use only). Pathway analysis, gene-pathway mapping, metabolic pathways, drug interactions, ID conversion. For Python workflows with multiple databases, prefer bioservices. Use this for direct HTTP/REST work or KEGG-specific control.
- **sci-labarchive-integration** — Electronic lab notebook API integration. Access notebooks, manage entries/attachments, backup notebooks, integrate with Protocols.io/Jupyter/REDCap, for programmatic ELN workflows.
- **sci-lamindb** — This skill should be used when working with LaminDB, an open-source data framework for biology that makes data queryable, traceable, reproducible, and FAIR. Use when managing biological datasets (scRNA-seq, spatial, flow cytometry, etc.), tracking computational workflows, curating and validating data with biological ontologies, building data lakehouses, or ensuring data lineage and reproducibility in biological research. Covers data management, annotation, ontologies (genes, cell types, diseases, tissues), schema validation, integrations with workflow managers (Nextflow, Snakemake) and MLOps platforms (W&B, MLflow), and deployment strategies.
- **sci-latchbio-integration** — Latch platform for bioinformatics workflows. Build pipelines with Latch SDK, @workflow/@task decorators, deploy serverless workflows, LatchFile/LatchDir, Nextflow/Snakemake integration.
- **sci-latex-posters** — Skill: sci-latex-posters
- **sci-literature-review** — Skill: sci-literature-review
- **sci-market-research-reports** — Generate comprehensive market research reports (50+ pages) in the style of top consulting firms (McKinsey, BCG, Gartner). Features professional LaTeX formatting, extensive visual generation with scientific-schematics and generate-image, deep integration with research-lookup for data gathering, and multi-framework strategic analysis including Porter's Five Forces, PESTLE, SWOT, TAM/SAM/SOM, and BCG Matrix.
- **sci-markitdown** — Convert files and office documents to Markdown. Supports PDF, DOCX, PPTX, XLSX, images (with OCR), audio (with transcription), HTML, CSV, JSON, XML, ZIP, YouTube URLs, EPubs and more.
- **sci-matchms** — Mass spectrometry analysis. Process mzML/MGF/MSP, spectral similarity (cosine, modified cosine), metadata harmonization, compound ID, for metabolomics and MS data processing.
- **sci-matplotlib** — Foundational plotting library. Create line plots, scatter, bar, histograms, heatmaps, 3D, subplots, export PNG/PDF/SVG, for scientific visualization and publication figures.
- **sci-medchem** — Medicinal chemistry filters. Apply drug-likeness rules (Lipinski, Veber), PAINS filters, structural alerts, complexity metrics, for compound prioritization and library filtering.
- **sci-metabolomics-workbench-database** — Access NIH Metabolomics Workbench via REST API (4,200+ studies). Query metabolites, RefMet nomenclature, MS/NMR data, m/z searches, study metadata, for metabolomics and biomarker discovery.
- **sci-modal** — Run Python code in the cloud with serverless containers, GPUs, and autoscaling. Use when deploying ML models, running batch processing jobs, scheduling compute-intensive tasks, or serving APIs that require GPU acceleration or dynamic scaling.
- **sci-molfeat** — Molecular featurization for ML (100+ featurizers). ECFP, MACCS, descriptors, pretrained models (ChemBERTa), convert SMILES to features, for QSAR and molecular ML.
- **sci-networkx** — Comprehensive toolkit for creating, analyzing, and visualizing complex networks and graphs in Python. Use when working with network/graph data structures, analyzing relationships between entities, computing graph algorithms (shortest paths, centrality, clustering), detecting communities, generating synthetic networks, or visualizing network topologies. Applicable to social networks, biological networks, transportation systems, citation networks, and any domain involving pairwise relationships.
- **sci-neurokit2** — Comprehensive biosignal processing toolkit for analyzing physiological data including ECG, EEG, EDA, RSP, PPG, EMG, and EOG signals. Use this skill when processing cardiovascular signals, brain activity, electrodermal responses, respiratory patterns, muscle activity, or eye movements. Applicable for heart rate variability analysis, event-related potentials, complexity measures, autonomic nervous system assessment, psychophysiology research, and multi-modal physiological signal integration.
- **sci-neuropixels-analysis** — Neuropixels neural recording analysis. Load SpikeGLX/OpenEphys data, preprocess, motion correction, Kilosort4 spike sorting, quality metrics, Allen/IBL curation, AI-assisted visual analysis, for Neuropixels 1.0/2.0 extracellular electrophysiology. Use when working with neural recordings, spike sorting, extracellular electrophysiology, or when the user mentions Neuropixels, SpikeGLX, Open Ephys, Kilosort, quality metrics, or unit curation.
- **sci-omero-integration** — Microscopy data management platform. Access images via Python, retrieve datasets, analyze pixels, manage ROIs/annotations, batch processing, for high-content screening and microscopy workflows.
- **sci-openalex-database** — Skill: sci-openalex-database
- **sci-opentargets-database** — Query Open Targets Platform for target-disease associations, drug target discovery, tractability/safety data, genetics/omics evidence, known drugs, for therapeutic target identification.
- **sci-opentrons-integration** — Lab automation platform for Flex/OT-2 robots. Write Protocol API v2 protocols, liquid handling, hardware modules (heater-shaker, thermocycler), labware management, for automated pipetting workflows.
- **sci-paper-2-web** — This skill should be used when converting academic papers into promotional and presentation formats including interactive websites (Paper2Web), presentation videos (Paper2Video), and conference posters (Paper2Poster). Use this skill for tasks involving paper dissemination, conference preparation, creating explorable academic homepages, generating video abstracts, or producing print-ready posters from LaTeX or PDF sources.
- **sci-pathml** — Computational pathology toolkit for analyzing whole-slide images (WSI) and multiparametric imaging data. Use this skill when working with histopathology slides, H&E stained images, multiplex immunofluorescence (CODEX, Vectra), spatial proteomics, nucleus detection/segmentation, tissue graph construction, or training ML models on pathology data. Supports 160+ slide formats including Aperio SVS, NDPI, DICOM, OME-TIFF for digital pathology workflows.
- **sci-pdb-database** — Access RCSB PDB for 3D protein/nucleic acid structures. Search by text/sequence/structure, download coordinates (PDB/mmCIF), retrieve metadata, for structural biology and drug discovery.
- **sci-peer-review** — Systematic peer review toolkit. Evaluate methodology, statistics, design, reproducibility, ethics, figure integrity, reporting standards, for manuscript and grant review across disciplines.
- **sci-pennylane** — Cross-platform Python library for quantum computing, quantum machine learning, and quantum chemistry. Enables building and training quantum circuits with automatic differentiation, seamless integration with PyTorch/JAX/TensorFlow, and device-independent execution across simulators and quantum hardware (IBM, Amazon Braket, Google, Rigetti, IonQ, etc.). Use when working with quantum circuits, variational quantum algorithms (VQE, QAOA), quantum neural networks, hybrid quantum-classical models, molecular simulations, quantum chemistry calculations, or any quantum computing tasks requiring gradient-based optimization, hardware-agnostic programming, or quantum machine learning workflows.
- **sci-perplexity-search** — Perform AI-powered web searches with real-time information using Perplexity models via LiteLLM and OpenRouter. This skill should be used when conducting web searches for current information, finding recent scientific literature, getting grounded answers with source citations, or accessing information beyond the model's knowledge cutoff. Provides access to multiple Perplexity models including Sonar Pro, Sonar Pro Search (advanced agentic search), and Sonar Reasoning Pro through a single OpenRouter API key.
- **sci-plotly** — Interactive scientific and statistical data visualization library for Python. Use when creating charts, plots, or visualizations including scatter plots, line charts, bar charts, heatmaps, 3D plots, geographic maps, statistical distributions, financial charts, and dashboards. Supports both quick visualizations (Plotly Express) and fine-grained customization (graph objects). Outputs interactive HTML or static images (PNG, PDF, SVG).
- **sci-polars** — Fast DataFrame library (Apache Arrow). Select, filter, group_by, joins, lazy evaluation, CSV/Parquet I/O, expression API, for high-performance data analysis workflows.
- **sci-pptx-posters** — Skill: sci-pptx-posters
- **sci-protocolsio-integration** — Integration with protocols.io API for managing scientific protocols. This skill should be used when working with protocols.io to search, create, update, or publish protocols; manage protocol steps and materials; handle discussions and comments; organize workspaces; upload and manage files; or integrate protocols.io functionality into workflows. Applicable for protocol discovery, collaborative protocol development, experiment tracking, lab protocol management, and scientific documentation.
- **sci-pubchem-database** — Query PubChem via PUG-REST API/PubChemPy (110M+ compounds). Search by name/CID/SMILES, retrieve properties, similarity/substructure searches, bioactivity, for cheminformatics.
- **sci-pubmed-database** — Direct REST API access to PubMed. Advanced Boolean/MeSH queries, E-utilities API, batch processing, citation management. For Python workflows, prefer biopython (Bio.Entrez). Use this for direct HTTP/REST work or custom API implementations.
- **sci-pufferlib** — This skill should be used when working with reinforcement learning tasks including high-performance RL training, custom environment development, vectorized parallel simulation, multi-agent systems, or integration with existing RL environments (Gymnasium, PettingZoo, Atari, Procgen, etc.). Use this skill for implementing PPO training, creating PufferEnv environments, optimizing RL performance, or developing policies with CNNs/LSTMs.
- **sci-pydeseq2** — Differential gene expression analysis (Python DESeq2). Identify DE genes from bulk RNA-seq counts, Wald tests, FDR correction, volcano/MA plots, for RNA-seq analysis.
- **sci-pydicom** — Python library for working with DICOM (Digital Imaging and Communications in Medicine) files. Use this skill when reading, writing, or modifying medical imaging data in DICOM format, extracting pixel data from medical images (CT, MRI, X-ray, ultrasound), anonymizing DICOM files, working with DICOM metadata and tags, converting DICOM images to other formats, handling compressed DICOM data, or processing medical imaging datasets. Applies to tasks involving medical image analysis, PACS systems, radiology workflows, and healthcare imaging applications.
- **sci-pyhealth** — Comprehensive healthcare AI toolkit for developing, testing, and deploying machine learning models with clinical data. This skill should be used when working with electronic health records (EHR), clinical prediction tasks (mortality, readmission, drug recommendation), medical coding systems (ICD, NDC, ATC), physiological signals (EEG, ECG), healthcare datasets (MIMIC-III/IV, eICU, OMOP), or implementing deep learning models for healthcare applications (RETAIN, SafeDrug, Transformer, GNN).
- **sci-pylabrobot** — Laboratory automation toolkit for controlling liquid handlers, plate readers, pumps, heater shakers, incubators, centrifuges, and analytical equipment. Use this skill when automating laboratory workflows, programming liquid handling robots (Hamilton STAR, Opentrons OT-2, Tecan EVO), integrating lab equipment, managing deck layouts and resources (plates, tips, containers), reading plates, or creating reproducible laboratory protocols. Applicable for both simulated protocols and physical hardware control.
- **sci-pymatgen** — Materials science toolkit. Crystal structures (CIF, POSCAR), phase diagrams, band structure, DOS, Materials Project integration, format conversion, for computational materials science.
- **sci-pymc** — Bayesian modeling with PyMC. Build hierarchical models, MCMC (NUTS), variational inference, LOO/WAIC comparison, posterior checks, for probabilistic programming and inference.
- **sci-pymoo** — Multi-objective optimization framework. NSGA-II, NSGA-III, MOEA/D, Pareto fronts, constraint handling, benchmarks (ZDT, DTLZ), for engineering design and optimization problems.
- **sci-pyopenms** — Python interface to OpenMS for mass spectrometry data analysis. Use for LC-MS/MS proteomics and metabolomics workflows including file handling (mzML, mzXML, mzTab, FASTA, pepXML, protXML, mzIdentML), signal processing, feature detection, peptide identification, and quantitative analysis. Apply when working with mass spectrometry data, analyzing proteomics experiments, or processing metabolomics datasets.
- **sci-pysam** — Genomic file toolkit. Read/write SAM/BAM/CRAM alignments, VCF/BCF variants, FASTA/FASTQ sequences, extract regions, calculate coverage, for NGS data processing pipelines.
- **sci-pytdc** — Therapeutics Data Commons. AI-ready drug discovery datasets (ADME, toxicity, DTI), benchmarks, scaffold splits, molecular oracles, for therapeutic ML and pharmacological prediction.
- **sci-pytorch-lightning** — Deep learning framework (PyTorch Lightning). Organize PyTorch code into LightningModules, configure Trainers for multi-GPU/TPU, implement data pipelines, callbacks, logging (W&B, TensorBoard), distributed training (DDP, FSDP, DeepSpeed), for scalable neural network training.
- **sci-qiskit** — Comprehensive quantum computing toolkit for building, optimizing, and executing quantum circuits. Use when working with quantum algorithms, simulations, or quantum hardware including (1) Building quantum circuits with gates and measurements, (2) Running quantum algorithms (VQE, QAOA, Grover), (3) Transpiling/optimizing circuits for hardware, (4) Executing on IBM Quantum or other providers, (5) Quantum chemistry and materials science, (6) Quantum machine learning, (7) Visualizing circuits and results, or (8) Any quantum computing development task.
- **sci-qutip** — Quantum mechanics simulations and analysis using QuTiP (Quantum Toolbox in Python). Use when working with quantum systems including: (1) quantum states (kets, bras, density matrices), (2) quantum operators and gates, (3) time evolution and dynamics (SchrÃ¶dinger, master equations, Monte Carlo), (4) open quantum systems with dissipation, (5) quantum measurements and entanglement, (6) visualization (Bloch sphere, Wigner functions), (7) steady states and correlation functions, or (8) advanced methods (Floquet theory, HEOM, stochastic solvers). Handles both closed and open quantum systems across various domains including quantum optics, quantum computing, and condensed matter physics.
- **sci-rdkit** — Cheminformatics toolkit for fine-grained molecular control. SMILES/SDF parsing, descriptors (MW, LogP, TPSA), fingerprints, substructure search, 2D/3D generation, similarity, reactions. For standard workflows with simpler interface, use datamol (wrapper around RDKit). Use rdkit for advanced control, custom sanitization, specialized algorithms.
- **sci-reactome-database** — Query Reactome REST API for pathway analysis, enrichment, gene-pathway mapping, disease pathways, molecular interactions, expression analysis, for systems biology studies.
- **sci-research-grants** — Skill: sci-research-grants
- **sci-research-lookup** — Look up current research information using Perplexity's Sonar Pro Search or Sonar Reasoning Pro models through OpenRouter. Automatically selects the best model based on query complexity. Search academic papers, recent studies, technical documentation, and general research information with citations.
- **sci-scanpy** — Single-cell RNA-seq analysis. Load .h5ad/10X data, QC, normalization, PCA/UMAP/t-SNE, Leiden clustering, marker genes, cell type annotation, trajectory, for scRNA-seq analysis.
- **sci-scholar-evaluation** — Skill: sci-scholar-evaluation
- **sci-scientific-brainstorming** — Research ideation partner. Generate hypotheses, explore interdisciplinary connections, challenge assumptions, develop methodologies, identify research gaps, for creative scientific problem-solving.
- **sci-scientific-critical-thinking** — Evaluate research rigor. Assess methodology, experimental design, statistical validity, biases, confounding, evidence quality (GRADE, Cochrane ROB), for critical analysis of scientific claims.
- **sci-scientific-schematics** — Skill: sci-scientific-schematics
- **sci-scientific-slides** — Build slide decks and presentations for research talks. Use this for making PowerPoint slides, conference presentations, seminar talks, research presentations, thesis defense slides, or any scientific talk. Provides slide structure, design templates, timing guidance, and visual validation. Works with PowerPoint and LaTeX Beamer.
- **sci-scientific-visualization** — Create publication figures with matplotlib/seaborn/plotly. Multi-panel layouts, error bars, significance markers, colorblind-safe, export PDF/EPS/TIFF, for journal-ready scientific plots.
- **sci-scientific-writing** — Skill: sci-scientific-writing
- **sci-scikit-bio** — Biological data toolkit. Sequence analysis, alignments, phylogenetic trees, diversity metrics (alpha/beta, UniFrac), ordination (PCoA), PERMANOVA, FASTA/Newick I/O, for microbiome analysis.
- **sci-scikit-learn** — Machine learning in Python with scikit-learn. Use when working with supervised learning (classification, regression), unsupervised learning (clustering, dimensionality reduction), model evaluation, hyperparameter tuning, preprocessing, or building ML pipelines. Provides comprehensive reference documentation for algorithms, preprocessing techniques, pipelines, and best practices.
- **sci-scikit-survival** — Comprehensive toolkit for survival analysis and time-to-event modeling in Python using scikit-survival. Use this skill when working with censored survival data, performing time-to-event analysis, fitting Cox models, Random Survival Forests, Gradient Boosting models, or Survival SVMs, evaluating survival predictions with concordance index or Brier score, handling competing risks, or implementing any survival analysis workflow with the scikit-survival library.
- **sci-scvi-tools** — This skill should be used when working with single-cell omics data analysis using scvi-tools, including scRNA-seq, scATAC-seq, CITE-seq, spatial transcriptomics, and other single-cell modalities. Use this skill for probabilistic modeling, batch correction, dimensionality reduction, differential expression, cell type annotation, multimodal integration, and spatial analysis tasks.
- **sci-seaborn** — Statistical visualization. Scatter, box, violin, heatmaps, pair plots, regression, correlation matrices, KDE, faceted plots, for exploratory analysis and publication figures.
- **sci-shap** — Model interpretability and explainability using SHAP (SHapley Additive exPlanations). Use this skill when explaining machine learning model predictions, computing feature importance, generating SHAP plots (waterfall, beeswarm, bar, scatter, force, heatmap), debugging models, analyzing model bias or fairness, comparing models, or implementing explainable AI. Works with tree-based models (XGBoost, LightGBM, Random Forest), deep learning (TensorFlow, PyTorch), linear models, and any black-box model.
- **sci-simpy** — Process-based discrete-event simulation framework in Python. Use this skill when building simulations of systems with processes, queues, resources, and time-based events such as manufacturing systems, service operations, network traffic, logistics, or any system where entities interact with shared resources over time.
- **sci-stable-baselines3** — Use this skill for reinforcement learning tasks including training RL agents (PPO, SAC, DQN, TD3, DDPG, A2C, etc.), creating custom Gym environments, implementing callbacks for monitoring and control, using vectorized environments for parallel training, and integrating with deep RL workflows. This skill should be used when users request RL algorithm implementation, agent training, environment design, or RL experimentation.
- **sci-statistical-analysis** — Statistical analysis toolkit. Hypothesis tests (t-test, ANOVA, chi-square), regression, correlation, Bayesian stats, power analysis, assumption checks, APA reporting, for academic research.
- **sci-statsmodels** — Statistical modeling toolkit. OLS, GLM, logistic, ARIMA, time series, hypothesis tests, diagnostics, AIC/BIC, for rigorous statistical inference and econometric analysis.
- **sci-string-database** — Query STRING API for protein-protein interactions (59M proteins, 20B interactions). Network analysis, GO/KEGG enrichment, interaction discovery, 5000+ species, for systems biology.
- **sci-sympy** — Use this skill when working with symbolic mathematics in Python. This skill should be used for symbolic computation tasks including solving equations algebraically, performing calculus operations (derivatives, integrals, limits), manipulating algebraic expressions, working with matrices symbolically, physics calculations, number theory problems, geometry computations, and generating executable code from mathematical expressions. Apply this skill when the user needs exact symbolic results rather than numerical approximations, or when working with mathematical formulas that contain variables and parameters.
- **sci-torch_geometric** — Graph Neural Networks (PyG). Node/graph classification, link prediction, GCN, GAT, GraphSAGE, heterogeneous graphs, molecular property prediction, for geometric deep learning.
- **sci-torchdrug** — Graph-based drug discovery toolkit. Molecular property prediction (ADMET), protein modeling, knowledge graph reasoning, molecular generation, retrosynthesis, GNNs (GIN, GAT, SchNet), 40+ datasets, for PyTorch-based ML on molecules, proteins, and biomedical graphs.
- **sci-transformers** — This skill should be used when working with pre-trained transformer models for natural language processing, computer vision, audio, or multimodal tasks. Use for text generation, classification, question answering, translation, summarization, image classification, object detection, speech recognition, and fine-tuning models on custom datasets.
- **sci-treatment-plans** — Skill: sci-treatment-plans
- **sci-umap-learn** — UMAP dimensionality reduction. Fast nonlinear manifold learning for 2D/3D visualization, clustering preprocessing (HDBSCAN), supervised/parametric UMAP, for high-dimensional data.
- **sci-uniprot-database** — Direct REST API access to UniProt. Protein searches, FASTA retrieval, ID mapping, Swiss-Prot/TrEMBL. For Python workflows with multiple databases, prefer bioservices (unified interface to 40+ services). Use this for direct HTTP/REST work or UniProt-specific control.
- **sci-uspto-database** — Access USPTO APIs for patent/trademark searches, examination history (PEDS), assignments, citations, office actions, TSDR, for IP analysis and prior art searches.
- **sci-vaex** — Use this skill for processing and analyzing large tabular datasets (billions of rows) that exceed available RAM. Vaex excels at out-of-core DataFrame operations, lazy evaluation, fast aggregations, efficient visualization of big data, and machine learning on large datasets. Apply when users need to work with large CSV/HDF5/Arrow/Parquet files, perform fast statistics on massive datasets, create visualizations of big data, or build ML pipelines that don't fit in memory.
- **sci-venue-templates** — Access comprehensive LaTeX templates, formatting requirements, and submission guidelines for major scientific publication venues (Nature, Science, PLOS, IEEE, ACM), academic conferences (NeurIPS, ICML, CVPR, CHI), research posters, and grant proposals (NSF, NIH, DOE, DARPA). This skill should be used when preparing manuscripts for journal submission, conference papers, research posters, or grant proposals and need venue-specific formatting requirements and templates.
- **sci-zarr-python** — Chunked N-D arrays for cloud storage. Compressed arrays, parallel I/O, S3/GCS integration, NumPy/Dask/Xarray compatible, for large-scale scientific computing pipelines.
- **sci-zinc-database** — Access ZINC (230M+ purchasable compounds). Search by ZINC ID/SMILES, similarity searches, 3D-ready structures for docking, analog discovery, for virtual screening and drug discovery.
- **scrapling-skill** — Install, troubleshoot, and use Scrapling CLI to extract HTML, Markdown, or text from webpages. Use this skill whenever the user mentions Scrapling, `uv tool install scrapling`, `scrapling extract`, WeChat/mp.weixin articles, browser-backed page fetching, or needs help deciding between static and dynamic extraction.
- **security-hardening** — Application security covering input validation, auth, headers, secrets management, and dependency auditing
- **seo-audit** — When the user wants to audit, review, or diagnose SEO issues on their site. Also use when the user mentions "SEO audit," "technical SEO," "why am I not ranking," "SEO issues," "on-page SEO," "meta tags review," "SEO health check," "my traffic dropped," "lost rankings," "not showing up in Google," "site isn't ranking," "Google update hit me," "page speed," "core web vitals," "crawl errors," or "indexing issues." Use this even if the user just says something vague like "my SEO is bad" or "help with SEO" â€” start with an audit. For building pages at scale to target keywords, see programmatic-seo. For adding structured data, see schema-markup. For AI search optimization, see ai-seo.
- **signup-flow-cro** — When the user wants to optimize signup, registration, account creation, or trial activation flows. Also use when the user mentions "signup conversions," "registration friction," "signup form optimization," "free trial signup," "reduce signup dropoff," "account creation flow," "people aren't signing up," "signup abandonment," "trial conversion rate," "nobody completes registration," "too many steps to sign up," or "simplify our signup." Use this whenever the user has a signup or registration flow that isn't performing. For post-signup onboarding, see onboarding-cro. For lead capture forms (not account creation), see form-cro.
- **site-architecture** — When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal linking. Also use when the user mentions "sitemap," "site map," "visual sitemap," "site structure," "page hierarchy," "information architecture," "IA," "navigation design," "URL structure," "breadcrumbs," "internal linking strategy," "website planning," "what pages do I need," "how should I organize my site," or "site navigation." Use this whenever someone is planning what pages a website should have and how they connect. NOT for XML sitemaps (that's technical SEO â€” see seo-audit). For SEO audits, see seo-audit. For structured data, see schema-markup.
- **skill-creator** — Skill: skill-creator
- **skill-reviewer** — Skill: skill-reviewer
- **skills-search** — This skill should be used when users want to search, discover, install, or manage Claude Code skills from the CCPM registry. Triggers include requests like "find skills for PDF", "search for code review skills", "install cloudflare-troubleshooting", "list my installed skills", "what does skill-creator do", or any mention of finding/installing/managing Claude Code skills or plugins.
- **slack-gif-creator** — Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack.
- **social-content** — When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, TikTok, Facebook, or other platforms. Also use when the user mentions 'LinkedIn post,' 'Twitter thread,' 'social media,' 'content calendar,' 'social scheduling,' 'engagement,' 'viral content,' 'what should I post,' 'repurpose this content,' 'tweet ideas,' 'LinkedIn carousel,' 'social media strategy,' or 'grow my following.' Use this for any social media content creation, repurposing, or scheduling task. For broader content strategy, see content-strategy.
- **springboot-patterns** — Spring Boot patterns including JPA repositories, REST controllers, layered services, and configuration
- **subagent-driven-development** — Use when executing implementation plans with independent tasks in the current session
- **supermemory** — Supermemory is a state-of-the-art memory and context infrastructure for AI agents. Use this skill when building applications that need persistent memory, user personalization, long-term context retention, or semantic search across knowledge bases. It provides Memory API for learned user context, User Profiles for static/dynamic facts, and RAG for semantic search. Perfect for chatbots, assistants, and knowledge-intensive applications.
- **systematic-debugging** — Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
- **tdd-mastery** — Test-driven development workflow with Red-Green-Refactor cycle across languages
- **teams-channel-post-writer** — Creates educational Teams channel posts for internal knowledge sharing about Claude Code features, tools, and best practices. Applies when writing posts, announcements, or documentation to teach colleagues effective Claude Code usage, announce new features, share productivity tips, or document lessons learned. Provides templates, writing guidelines, and structured approaches emphasizing concrete examples, underlying principles, and connections to best practices like context engineering. Activates for content involving Teams posts, channel announcements, feature documentation, or tip sharing.
- **terraform-skill** — Operational traps for Terraform provisioners, multi-environment isolation, and zero-to-deployment reliability. Covers provisioner timing races, SSH connection conflicts, DNS record duplication, volume permissions, database bootstrap gaps, snapshot cross-contamination, Cloudflare credential format errors, hardcoded domains in Caddyfiles/compose, and init-data-only-on-first-boot pitfalls. Activate when writing null_resource provisioners, creating multi-environment Terraform setups, debugging containers that are Restarting/unhealthy after terraform apply, setting up fresh instances with cloud-init, or any IaC code that SSHs into remote hosts. Also activate when the user mentions terraform plan/apply errors, provisioner failures, infrastructure drift, TLS certificate errors, or Caddy/gateway configuration.
- **test-driven-development** — Use when implementing any feature or bugfix, before writing implementation code
- **testing-strategies** — Testing strategies including contract testing, snapshot testing, mutation testing, property-based testing, and test organization
- **theme-factory** — Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.
- **transcript-fixer** — Skill: transcript-fixer
- **tunnel-doctor** — Skill: tunnel-doctor
- **twitter-reader** — Skill: twitter-reader
- **typescript-advanced** — Advanced TypeScript patterns including generics, conditional types, mapped types, template literals, and type guards
- **ui-designer** — Skill: ui-designer
- **using-git-worktrees** — Use when starting feature work that needs isolation from current workspace or before executing implementation plans - creates isolated git worktrees with smart directory selection and safety verification
- **using-superpowers** — Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions
- **vercel-cli-with-tokens** — Deploy and manage projects on Vercel using token-based authentication. Use when working with Vercel CLI using access tokens rather than interactive login â€” e.g. "deploy to vercel", "set up vercel", "add environment variables to vercel".
- **verification-before-completion** — Skill: verification-before-completion
- **video-comparer** — This skill should be used when comparing two videos to analyze compression results or quality differences. Generates interactive HTML reports with quality metrics (PSNR, SSIM) and frame-by-frame visual comparisons. Triggers when users mention "compare videos", "video quality", "compression analysis", "before/after compression", or request quality assessment of compressed videos.
- **web-artifacts-builder** — Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.
- **web-design-guidelines** — Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices".
- **webapp-testing** — Skill: webapp-testing
- **websocket-realtime** — Real-time communication patterns with WebSocket, Socket.io, Server-Sent Events, and scaling strategies
- **windows-remote-desktop-connection-doctor** — Diagnose Windows App (Microsoft Remote Desktop / Azure Virtual Desktop / W365) connection quality issues on macOS. Analyze transport protocol selection (UDP Shortpath vs WebSocket), detect VPN/proxy interference with STUN/TURN negotiation, and parse Windows App logs for Shortpath failures. This skill should be used when VDI connections are slow, when transport shows WebSocket instead of UDP, when RDP Shortpath fails to establish, or when RTT is unexpectedly high.
- **writing-plans** — Use when you have a spec or requirements for a multi-step task, before touching code
- **writing-skills** — Skill: writing-skills
- **xlsx** — Skill: xlsx
- **youtube-downloader** — Skill: youtube-downloader

### Plugins

- **a11y-audit** — Full accessibility audit with WCAG compliance checking
- **accessibility-checker** — Scan for accessibility issues and fix ARIA attributes in web applications
- **adr-writer** — Architecture Decision Records authoring and management
- **ai-prompt-lab** — Improve and test AI prompts for better Claude Code interactions
- **analytics-reporter** — Generate analytics reports and dashboard configurations from project data
- **android-developer** — Android and Kotlin development with Jetpack Compose
- **android-reverse-engineering** — Decompile Android APK/JAR/AAR with jadx, trace call flows through libraries, and document extracted APIs.
- **api-architect** — API design, documentation, and testing with OpenAPI spec generation
- **api-benchmarker** — API endpoint benchmarking and performance reporting
- **api-reference** — API reference documentation generation from source code
- **api-tester** — Test API endpoints and run load tests against services
- **aws-helper** — AWS service configuration and deployment automation
- **azure-helper** — Azure service configuration and deployment automation
- **backend-architect** — Backend service architecture design with endpoint scaffolding
- **bug-detective** — Debug issues systematically with root cause analysis and execution tracing
- **bundle-analyzer** — Frontend bundle size analysis and tree-shaking optimization
- **changelog-gen** — Generate changelogs from git history with conventional commit parsing
- **changelog-writer** — Detailed changelog authoring from git history and PRs
- **ci-debugger** — Debug CI/CD pipeline failures and fix configurations
- **code-architect** — Generate architecture diagrams and technical design documents
- **code-explainer** — Explain complex code and annotate files with inline documentation
- **code-guardian** — Automated code review, security scanning, and quality enforcement
- **code-review-assistant** — Automated code review with severity levels and actionable feedback
- **codebase-documenter** — Auto-document entire codebase with inline comments and API docs
- **color-contrast** — Color contrast checking and accessible color suggestions
- **commit-commands** — Advanced commit workflows with smart staging and push automation
- **complexity-reducer** — Reduce cyclomatic complexity and simplify functions
- **compliance-checker** — Regulatory compliance verification for GDPR, SOC2, and HIPAA
- **content-creator** — Technical content generation for blog posts and social media
- **context7-docs** — Fetch up-to-date library documentation via Context7 for accurate coding
- **contract-tester** — API contract testing with Pact for microservice compatibility
- **create-worktrees** — Git worktree management for parallel development workflows
- **cron-scheduler** — Cron job configuration and schedule validation
- **css-cleaner** — Find unused CSS and consolidate stylesheets
- **data-privacy** — Data privacy implementation with PII detection and anonymization
- **database-optimizer** — Database query optimization with index recommendations and EXPLAIN analysis
- **dead-code-finder** — Find and remove dead code across the codebase
- **debug-session** — Interactive debugging workflow with git bisect integration
- **dependency-manager** — Audit, update, and manage project dependencies with safety checks
- **deploy-pilot** — Deployment automation with Dockerfile generation, CI/CD pipelines, and infrastructure as code
- **design-ops** — Streamline design operations with critique frameworks, handoff specs, sprint planning, review processes, and team workflows.
- **design-research** — User research skills for designers: personas, empathy maps, journey maps, interview scripts, usability testing, and card sorting.
- **design-systems** — Build, document, and maintain scalable design systems — from tokens and components to accessibility and theming.
- **designer-toolkit** — Essential designer utilities for writing rationale, building presentations, crafting case studies, UX writing, and driving adoption.
- **desktop-app** — Desktop application scaffolding with Electron or Tauri
- **devops-automator** — DevOps automation scripts for CI/CD, health checks, and deployments
- **discuss** — Debate implementation approaches with structured pros and cons analysis
- **doc-forge** — Documentation generation, API docs, and README maintenance
- **docker-helper** — Build optimized Docker images and improve Dockerfile best practices
- **double-check** — Verify code correctness with systematic second-pass analysis
- **e2e-runner** — End-to-end test execution and recording for web applications
- **embedding-manager** — Manage vector embeddings and similarity search
- **env-manager** — Set up and validate environment configurations across environments
- **env-sync** — Environment variable syncing and diff across environments
- **experiment-tracker** — ML experiment tracking with metrics logging and run comparison
- **explore** — Smart codebase exploration with dependency mapping and structure analysis
- **feature-dev** — Full feature development workflow from spec to completion
- **finance-tracker** — Development cost tracking with time estimates and budget reporting
- **fix-github-issue** — Auto-fix GitHub issues by analyzing issue details and implementing solutions
- **fix-pr** — Fix PR review comments automatically with context-aware patches
- **flutter-mobile** — Flutter app development with widget creation and platform channels
- **frontend-developer** — Frontend component development with accessibility and responsive design
- **gcp-helper** — Google Cloud Platform service configuration and deployment
- **git-flow** — Git workflow management with feature branches, releases, and hotfix flows
- **github-issue-manager** — GitHub issue triage, creation, and management
- **helm-charts** — Helm chart generation and upgrade management
- **import-organizer** — Organize, sort, and clean import statements
- **infrastructure-maintainer** — Infrastructure maintenance with security audits and update management
- **interaction-design** — Design meaningful interactions with micro-animations, state machines, gestures, error handling, and feedback patterns.
- **ios-developer** — iOS and Swift development with SwiftUI views and models
- **k8s-helper** — Generate Kubernetes manifests and debug pod issues with kubectl
- **license-checker** — License compliance checking and NOTICE file generation
- **lighthouse-runner** — Run Lighthouse audits and fix performance issues
- **linear-helper** — Linear issue tracking integration and workflow management
- **load-tester** — Load and stress testing for APIs and web services
- **memory-profiler** — Memory leak detection and heap analysis
- **migrate-tool** — Generate database migrations and code migration scripts for framework upgrades
- **migration-generator** — Database migration generation and rollback management
- **model-context-protocol** — MCP server development helper with tool and resource scaffolding
- **model-evaluator** — Evaluate and compare ML model performance metrics
- **monitoring-setup** — Monitoring and alerting configuration with dashboard generation
- **monorepo-manager** — Manage monorepo packages with affected detection and version synchronization
- **mutation-tester** — Mutation testing to measure test suite quality
- **n8n-workflow** — Generate n8n automation workflows from natural language descriptions
- **onboarding-guide** — New developer onboarding documentation generator
- **openapi-expert** — OpenAPI spec generation, validation, and client code scaffolding
- **optimize** — Code optimization for performance and bundle size reduction
- **perf-profiler** — Performance analysis, profiling, and optimization recommendations
- **performance-monitor** — Profile API endpoints and run benchmarks to identify performance bottlenecks
- **plan** — Structured planning with risk assessment and time estimation
- **pr-reviewer** — Review pull requests with structured analysis and approve with confidence
- **product-shipper** — Ship features end-to-end with launch checklists and rollout plans
- **project-scaffold** — Scaffold new projects and add features with best-practice templates
- **prompt-optimizer** — Analyze and optimize AI prompts for better results
- **prototyping-testing** — Plan and execute design validation through prototyping strategies, usability testing, heuristic evaluation, and A/B experiments.
- **python-expert** — Python-specific development with type hints and idiomatic refactoring
- **query-optimizer** — SQL query optimization and execution plan analysis
- **rag-builder** — Build Retrieval-Augmented Generation pipelines
- **rapid-prototyper** — Quick prototype scaffolding with minimal viable structure
- **react-native-dev** — React Native mobile development with platform-specific optimizations
- **readme-generator** — Smart README generation from project analysis
- **refactor-engine** — Extract functions, simplify complex code, and reduce cognitive complexity
- **regex-builder** — Build, test, and debug regular expression patterns
- **release-manager** — Semantic versioning management and automated release workflows
- **responsive-designer** — Responsive design implementation and testing
- **schema-designer** — Database schema design and ERD generation
- **screen-reader-tester** — Screen reader compatibility testing and ARIA fixes
- **security-guidance** — Security best practices advisor with vulnerability detection and fixes
- **seed-generator** — Database seeding script generation with realistic data
- **slack-notifier** — Slack integration for deployment and build notifications
- **smart-commit** — Intelligent git commits with conventional format, semantic analysis, and changelog generation
- **sprint-prioritizer** — Sprint planning with story prioritization and capacity estimation
- **technical-sales** — Technical demo creation and POC proposal writing
- **terraform-helper** — Terraform module creation and infrastructure planning
- **test-data-generator** — Generate realistic test data and seed databases
- **test-results-analyzer** — Analyze test failures, identify patterns, and suggest targeted fixes
- **test-writer** — Generate comprehensive unit and integration tests with full coverage
- **tool-evaluator** — Evaluate and compare developer tools with structured scoring criteria
- **type-migrator** — Migrate JavaScript files to TypeScript with proper types
- **ui-design** — Craft polished user interfaces with layout grids, color systems, typography scales, responsive patterns, and visual hierarchy.
- **ui-designer** — Implement UI designs from specs with pixel-perfect component generation
- **ultrathink** — Deep analysis mode with extended reasoning for complex problems
- **unit-test-generator** — Generate comprehensive unit tests for any function or module
- **update-branch** — Rebase and update feature branches with conflict resolution
- **ux-strategy** — Shape product direction through competitive analysis, design principles, experience mapping, and strategic alignment.
- **vision-specialist** — Image and visual analysis with screenshot interpretation and text extraction
- **visual-regression** — Visual regression testing with screenshot comparison
- **web-dev** — Full-stack web development with app scaffolding and page generation
- **workflow-optimizer** — Development workflow analysis and optimization recommendations

### Agents (by category)

#### business-product

- **business-analyst** — Performs requirements analysis, process mapping, gap analysis, and stakeholder alignment for technical projects
- **content-strategist** — Plans content strategy with SEO-driven writing, editorial calendars, topic clustering, and content performance measurement
- **customer-success** — Builds customer support infrastructure with ticket triage, knowledge base systems, workflow automation, and customer health scoring
- **growth-engineer** — Implements A/B testing frameworks, analytics instrumentation, funnel optimization, and data-driven growth experiments
- **legal-advisor** — Drafts terms of service, privacy policies, software licenses, and compliance documentation for technology products
- **marketing-analyst** — Implements campaign analysis, attribution modeling, ROI tracking, and marketing data infrastructure for data-driven growth decisions
- **product-manager** — Creates PRDs, user stories, acceptance criteria, and prioritization frameworks for product development
- **project-manager** — Manages sprint planning, task tracking, timeline estimation, and Agile ceremony facilitation
- **sales-engineer** — Creates technical demos, proof-of-concept implementations, integration guides, and competitive technical analysis for sales engagements
- **scrum-master** — Facilitates Scrum ceremonies, tracks team velocity, removes impediments, and drives continuous improvement
- **technical-writer** — Produces polished technical documentation with consistent style, clear structure, and audience-appropriate language
- **ux-researcher** — Designs and conducts user research studies including usability testing, surveys, and behavioral analysis

#### core-development

- **api-designer** — REST and GraphQL API design with OpenAPI specs, versioning, and pagination patterns
- **api-gateway-engineer** — API gateway patterns, rate limiting, authentication proxies, and request routing
- **backend-developer** — Node.js backend development with Express, Fastify, middleware patterns, and API performance optimization
- **electron-developer** — Electron desktop applications, IPC communication, native OS integration, and auto-updates
- **event-driven-architect** — Event sourcing, CQRS, message queues, and distributed event-driven system design
- **frontend-architect** — React/Next.js specialist with performance optimization, SSR/SSG, and accessibility
- **fullstack-engineer** — End-to-end feature development across frontend, backend, and database layers
- **graphql-architect** — GraphQL schema design, resolver implementation, federation, and performance optimization with DataLoader
- **microservices-architect** — Distributed systems design with event-driven architecture, saga patterns, service mesh, and observability
- **mobile-developer** — React Native and Flutter cross-platform specialist with native bridge patterns
- **monorepo-architect** — Turborepo/Nx workspace strategies, dependency graphs, and monorepo build optimization
- **ui-designer** — UI/UX implementation, design systems, Figma-to-code translation, and component libraries
- **websocket-engineer** — Real-time communication with WebSockets, Socket.io, scaling strategies, and reconnection handling

#### data-ai

- **ai-engineer** — AI application development with model API integration, RAG pipelines, agent frameworks, and embedding strategies
- **autoresearch-agent** — Automated ML experiment optimization using tree search â€” designs experiments, generates code, evaluates results, and iterates
- **computer-vision-engineer** — Builds image classification, object detection, and segmentation pipelines using OpenCV, PyTorch, and production-grade inference optimization
- **data-engineer** — Data pipeline engineering with ETL/ELT workflows, Spark, data warehousing, and pipeline orchestration
- **data-scientist** — Statistical analysis, data visualization, hypothesis testing, and exploratory data analysis with Python
- **data-visualization** — Creates interactive dashboards and data visualizations using D3.js, Chart.js, Matplotlib, and Plotly with accessibility and performance optimization
- **database-optimizer** — Database performance optimization with query tuning, indexing strategies, partitioning, and capacity planning
- **etl-specialist** — Builds robust data pipelines with schema evolution, data quality checks, incremental loading, and fault-tolerant processing
- **feature-engineer** — Designs feature stores, feature pipelines, and encoding strategies that ensure consistent feature computation across training and serving
- **llm-architect** — LLM system design with fine-tuning, model selection, inference optimization, and evaluation frameworks
- **ml-engineer** — Machine learning pipeline development with training, evaluation, feature engineering, and model deployment
- **mlops-engineer** — ML model lifecycle management with serving infrastructure, monitoring, A/B testing, and CI/CD for models
- **nlp-engineer** — NLP pipeline development with text processing, embeddings, classification, NER, and transformer fine-tuning
- **prompt-engineer** — Prompt optimization with chain-of-thought, structured outputs, few-shot learning, and systematic evaluation
- **recommendation-engine** — Designs recommendation systems using collaborative filtering, content-based methods, and hybrid approaches with real-time personalization
- **vector-database-engineer** — Designs embedding pipelines and vector search systems using FAISS, Pinecone, Qdrant, and Weaviate for semantic retrieval at scale

#### developer-experience

- **api-documentation** — Creates comprehensive API documentation using OpenAPI/Swagger, Redoc, and interactive examples with versioning and change tracking
- **build-engineer** — Designs and optimizes build systems, bundlers, and compilation pipelines for fast and reliable artifact production
- **cli-developer** — Builds robust CLI tools using Commander.js, yargs, clap, and other frameworks with polished user interfaces
- **dependency-manager** — Audits, updates, and manages project dependencies with attention to security, compatibility, and lockfile integrity
- **developer-portal** — Builds internal developer portals using Backstage, service catalogs, and self-service infrastructure for platform engineering
- **documentation-engineer** — Creates technical documentation including API references, guides, tutorials, and architecture decision records
- **dx-optimizer** — Improves developer experience through tooling ergonomics, workflow friction reduction, and environment standardization
- **git-workflow-manager** — Designs Git branching strategies, CI integration patterns, and repository workflow automation
- **legacy-modernizer** — Plans and executes legacy codebase migrations with incremental strategies and risk mitigation
- **mcp-developer** — Develops MCP servers and tools following the Model Context Protocol specification for AI agent integration
- **monorepo-tooling** — Manages monorepo infrastructure with changesets, workspace dependencies, version management, and selective CI pipelines
- **refactoring-specialist** — Performs systematic code refactoring including dead code removal, abstraction extraction, and structural improvements
- **testing-infrastructure** — Designs test runners, CI test splitting, flaky test management, and test infrastructure that scales across large engineering organizations
- **tooling-engineer** — Configures and builds developer tooling including linters, formatters, type checkers, and custom code analysis tools
- **vscode-extension** — Develops VS Code extensions with Language Server Protocol integration, custom editors, webview panels, and marketplace publishing

#### gsd-workflow

- **gsd-advisor-researcher** — Researches a single gray area decision and returns a structured comparison table with rationale. Spawned by discuss-phase advisor mode.
- **gsd-ai-researcher** — Researches a chosen AI framework's official docs to produce implementation-ready guidance â€” best practices, syntax, core patterns, and pitfalls distilled for the specific use case. Writes the Framework Quick Reference and Implementation Guidance sections of AI-SPEC.md. Spawned by /gsd-ai-integration-phase orchestrator.
- **gsd-assumptions-analyzer** — Deeply analyzes codebase for a phase and returns structured assumptions with evidence. Spawned by discuss-phase assumptions mode.
- **gsd-code-fixer** — Applies fixes to code review findings from REVIEW.md. Reads source files, applies intelligent fixes, and commits each fix atomically. Spawned by /gsd-code-review-fix.
- **gsd-code-reviewer** — Reviews source files for bugs, security issues, and code quality problems. Produces structured REVIEW.md with severity-classified findings. Spawned by /gsd-code-review.
- **gsd-codebase-mapper** — Explores codebase and writes structured analysis documents. Spawned by map-codebase with a focus area (tech, arch, quality, concerns). Writes documents directly to reduce orchestrator context load.
- **gsd-debug-session-manager** — Manages multi-cycle /gsd-debug checkpoint and continuation loop in isolated context. Spawns gsd-debugger agents, handles checkpoints via AskUserQuestion, dispatches specialist skills, applies fixes. Returns compact summary to main context. Spawned by /gsd-debug command.
- **gsd-debugger** — Investigates bugs using scientific method, manages debug sessions, handles checkpoints. Spawned by /gsd-debug orchestrator.
- **gsd-doc-classifier** — Classifies a single planning document as ADR, PRD, SPEC, DOC, or UNKNOWN. Extracts title, scope summary, and cross-references. Spawned in parallel by /gsd-ingest-docs. Writes a JSON classification file and returns a one-line confirmation.
- **gsd-doc-synthesizer** — Synthesizes classified planning docs into a single consolidated context. Applies precedence rules, detects cross-ref cycles, enforces LOCKED-vs-LOCKED hard-blocks, and writes INGEST-CONFLICTS.md with three buckets (auto-resolved, competing-variants, unresolved-blockers). Spawned by /gsd-ingest-docs.
- **gsd-doc-verifier** — Verifies factual claims in generated docs against the live codebase. Returns structured JSON per doc.
- **gsd-doc-writer** — Writes and updates project documentation. Spawned with a doc_assignment block specifying doc type, mode (create/update/supplement), and project context.
- **gsd-domain-researcher** — Researches the business domain and real-world application context of the AI system being built. Surfaces domain expert evaluation criteria, industry-specific failure modes, regulatory context, and what "good" looks like for practitioners in this field â€” before the eval-planner turns it into measurable rubrics. Spawned by /gsd-ai-integration-phase orchestrator.
- **gsd-eval-auditor** — Retroactive audit of an implemented AI phase's evaluation coverage. Checks implementation against the AI-SPEC.md evaluation plan. Scores each eval dimension as COVERED/PARTIAL/MISSING. Produces a scored EVAL-REVIEW.md with findings, gaps, and remediation guidance. Spawned by /gsd-eval-review orchestrator.
- **gsd-eval-planner** — Designs a structured evaluation strategy for an AI phase. Identifies critical failure modes, selects eval dimensions with rubrics, recommends tooling, and specifies the reference dataset. Writes the Evaluation Strategy, Guardrails, and Production Monitoring sections of AI-SPEC.md. Spawned by /gsd-ai-integration-phase orchestrator.
- **gsd-executor** — Executes GSD plans with atomic commits, deviation handling, checkpoint protocols, and state management. Spawned by execute-phase orchestrator or execute-plan command.
- **gsd-framework-selector** — Agent: gsd-framework-selector
- **gsd-integration-checker** — Verifies cross-phase integration and E2E flows. Checks that phases connect properly and user workflows complete end-to-end.
- **gsd-intel-updater** — Analyzes codebase and writes structured intel files to .planning/intel/.
- **gsd-nyquist-auditor** — Fills Nyquist validation gaps by generating tests and verifying coverage for phase requirements
- **gsd-pattern-mapper** — Analyzes codebase for existing patterns and produces PATTERNS.md mapping new files to closest analogs. Read-only codebase analysis spawned by /gsd-plan-phase orchestrator before planning.
- **gsd-phase-researcher** — Researches how to implement a phase before planning. Produces RESEARCH.md consumed by gsd-planner. Spawned by /gsd-plan-phase orchestrator.
- **gsd-plan-checker** — Verifies plans will achieve phase goal before execution. Goal-backward analysis of plan quality. Spawned by /gsd-plan-phase orchestrator.
- **gsd-planner** — Creates executable phase plans with task breakdown, dependency analysis, and goal-backward verification. Spawned by /gsd-plan-phase orchestrator.
- **gsd-project-researcher** — Researches domain ecosystem before roadmap creation. Produces files in .planning/research/ consumed during roadmap creation. Spawned by /gsd-new-project or /gsd-new-milestone orchestrators.
- **gsd-research-synthesizer** — Synthesizes research outputs from parallel researcher agents into SUMMARY.md. Spawned by /gsd-new-project after 4 researcher agents complete.
- **gsd-roadmapper** — Agent: gsd-roadmapper
- **gsd-security-auditor** — Verifies threat mitigations from PLAN.md threat model exist in implemented code. Produces SECURITY.md. Spawned by /gsd-secure-phase.
- **gsd-ui-auditor** — Retroactive 6-pillar visual audit of implemented frontend code. Produces scored UI-REVIEW.md. Spawned by /gsd-ui-review orchestrator.
- **gsd-ui-checker** — Validates UI-SPEC.md design contracts against 6 quality dimensions. Produces BLOCK/FLAG/PASS verdicts. Spawned by /gsd-ui-phase orchestrator.
- **gsd-ui-researcher** — Produces UI-SPEC.md design contract for frontend phases. Reads upstream artifacts, detects design system state, asks only unanswered questions. Spawned by /gsd-ui-phase orchestrator.
- **gsd-user-profiler** — Analyzes extracted session messages across 8 behavioral dimensions to produce a scored developer profile with confidence levels and evidence. Spawned by profile orchestration workflows.
- **gsd-verifier** — Verifies phase goal achievement through goal-backward analysis. Checks codebase delivers what phase promised, not just that tasks completed. Creates VERIFICATION.md report.

#### infrastructure

- **cloud-architect** — AWS/GCP/Azure multi-cloud patterns, IaC, cost optimization, and well-architected framework
- **database-admin** — PostgreSQL, MySQL, MongoDB optimization, migrations, replication, and backup strategies
- **deployment-engineer** — Blue-green deployments, canary releases, rolling updates, and feature flag management
- **devops-engineer** — CI/CD pipelines, Docker, Kubernetes, monitoring, and GitOps workflows
- **incident-responder** — Incident triage, runbook execution, communication protocols, and recovery procedures
- **kubernetes-specialist** — Kubernetes operators, CRDs, service mesh with Istio, and advanced cluster management
- **network-engineer** — DNS management, load balancer configuration, CDN setup, and firewall rule design
- **platform-engineer** — Internal developer platforms, service mesh, observability, and SLO/SLI management
- **security-engineer** — Infrastructure security, IAM policies, mTLS, secrets management with Vault, and compliance
- **sre-engineer** — SLOs, error budgets, incident response, postmortems, and production reliability
- **terraform-engineer** — Infrastructure as Code with Terraform, module design, state management, and multi-cloud provisioning

#### language-experts

- **angular-architect** — Angular 17+ development with signals, standalone components, RxJS patterns, and NgRx state management
- **clojure-developer** — REPL-driven development, persistent data structures, Ring/Compojure, and ClojureScript
- **csharp-developer** — C# and .NET 8+ development with ASP.NET Core, Entity Framework Core, minimal APIs, and async patterns
- **django-developer** — Django 5+ development with Django REST Framework, ORM optimization, migrations, and async views
- **elixir-expert** — Elixir development with Phoenix, OTP supervision trees, LiveView, and distributed systems on BEAM
- **flutter-expert** — Flutter 3+ cross-platform development with Dart, state management, navigation, and platform channels
- **golang-developer** — Go concurrency patterns, interfaces, error handling, testing, and module management
- **haskell-developer** — Pure functional programming, monads, type classes, GHC extensions, and Haskell ecosystem
- **java-architect** — Spring Boot 3+ application architecture with JPA, security, microservices, and reactive programming
- **kotlin-specialist** — Kotlin development with coroutines, Ktor, Kotlin Multiplatform, and idiomatic patterns
- **lua-developer** — Game scripting with Lua, Neovim plugin development, embedded Lua integration, and LuaJIT
- **nextjs-developer** — Next.js 14+ App Router development with React Server Components, ISR, middleware, and edge runtime
- **nim-developer** — Nim metaprogramming, GC strategies, C/C++ interop, and cross-compilation
- **ocaml-developer** — OCaml type inference, pattern matching, Dream web framework, and opam ecosystem
- **php-developer** — PHP 8.3+ and Laravel 11 development with Eloquent, queues, middleware, and Composer package management
- **python-engineer** — Python 3.12+ with typing, async/await, dataclasses, pydantic, and packaging
- **rails-expert** — Ruby on Rails 7+ development with Hotwire, ActiveRecord patterns, Turbo, and Stimulus
- **react-specialist** — React 19 development with hooks, state management, concurrent features, and component architecture
- **rust-systems** — Rust ownership, lifetimes, async runtime, FFI, unsafe patterns, and performance tuning
- **scala-developer** — Functional programming in Scala, Akka actors, Play Framework, and Cats Effect
- **svelte-developer** — SvelteKit development with runes, server-side rendering, form actions, and fine-grained reactivity
- **swift-developer** — SwiftUI, iOS 17+, Combine, structured concurrency, and Apple platform development
- **typescript-specialist** — Advanced TypeScript patterns including generics, conditional types, and module augmentation
- **vue-specialist** — Vue 3 development with Composition API, Pinia state management, Nuxt 3, and VueUse composables
- **zig-developer** — Zig systems programming, comptime metaprogramming, allocator strategies, and C interop

#### orchestration

- **agent-installer** — Install and configure agent collections, resolve dependencies, and validate environments
- **context-manager** — Context window optimization, progressive loading, and strategic compaction
- **error-coordinator** — Handle errors across multi-agent workflows, implement recovery strategies, and prevent cascading failures
- **knowledge-synthesizer** — Compress and synthesize information across sources, build knowledge graphs, and extract insights
- **multi-agent-coordinator** — Coordinate parallel agent execution, manage dependencies, and merge outputs from multiple agents
- **performance-monitor** — Monitor agent execution, track token usage, measure response quality, and optimize workflows
- **task-coordinator** — Multi-agent task distribution, dependency management, and parallel execution
- **workflow-director** — End-to-end workflow orchestration, checkpoint management, and error recovery

#### quality-assurance

- **accessibility-specialist** — WCAG 2.2 compliance, screen reader testing, keyboard navigation, and ARIA patterns
- **chaos-engineer** — Chaos testing, fault injection, resilience validation, and failure mode analysis
- **code-reviewer** — Comprehensive code review covering patterns, anti-patterns, security, performance, and readability
- **compliance-auditor** — SOC 2, GDPR, HIPAA compliance checking, audit evidence collection, and policy enforcement
- **error-detective** — Error tracking, stack trace analysis, reproduction step generation, and root cause identification
- **penetration-tester** — Authorized security testing, OWASP Top 10 assessment, vulnerability reporting, and remediation guidance
- **performance-engineer** — Profiling, benchmarking, memory analysis, load testing, and optimization patterns
- **qa-automation** — Test automation frameworks, CI integration, test data management, and reporting
- **security-auditor** — OWASP Top 10, dependency scanning, secrets detection, and penetration testing guidance
- **test-architect** — Testing strategy with unit/integration/e2e, TDD, property-based testing, and mutation testing

#### research-analysis

- **academic-researcher** — Conducts literature reviews, citation analysis, methodology evaluation, and research synthesis for technical and scientific topics
- **benchmarking-specialist** — Designs performance benchmarks, load tests, comparative evaluations, and reproducible measurement methodologies for software systems
- **competitive-analyst** — Performs competitive analysis including feature comparison, market positioning, and strategic differentiation assessment
- **data-researcher** — Performs data analysis, pattern recognition, statistical interpretation, and evidence-based insight extraction
- **market-researcher** — Conducts market sizing, TAM/SAM/SOM analysis, competitive intelligence, survey design, and customer segment identification
- **patent-analyst** — Conducts patent searches, prior art analysis, IP landscape mapping, and freedom-to-operate assessments for technology products
- **research-analyst** — Conducts structured technical research with systematic literature review, evidence synthesis, and actionable findings
- **search-specialist** — Performs advanced search, information retrieval, source evaluation, and knowledge synthesis across diverse sources
- **security-researcher** — Conducts CVE analysis, vulnerability research, threat modeling, attack surface assessment, and security advisory evaluation
- **technology-scout** — Evaluates emerging technologies, conducts build-vs-buy analysis, assesses vendor solutions, and produces technology adoption recommendations
- **trend-analyst** — Analyzes technology trends, adoption curves, and ecosystem shifts to inform strategic technical decisions

#### specialized-domains

- **blockchain-developer** — Develops smart contracts and Web3 applications with Solidity, Hardhat, and blockchain integration patterns
- **e-commerce-engineer** — Builds e-commerce systems including product catalogs, shopping carts, inventory management, and order processing
- **education-tech** — Builds learning management systems with SCORM/xAPI compliance, adaptive learning engines, assessment tools, and learner analytics
- **embedded-systems** — Develops firmware and embedded software in C and Rust with RTOS integration and hardware abstraction
- **fintech-engineer** — Builds financial systems with precise arithmetic, regulatory compliance, audit trails, and transaction integrity
- **game-developer** — Designs game systems, logic, and architecture patterns for Unity, Godot, and custom game engines
- **geospatial-engineer** — Builds GIS applications with PostGIS, spatial queries, mapping APIs, tile servers, and geospatial data processing pipelines
- **healthcare-engineer** — Builds HIPAA-compliant healthcare systems with HL7 FHIR interoperability, medical data pipelines, and clinical workflow integration
- **iot-engineer** — Designs IoT systems with MQTT messaging, edge computing, device management, and telemetry pipelines
- **media-streaming** — Builds video streaming platforms with HLS/DASH delivery, transcoding pipelines, CDN optimization, and adaptive bitrate streaming
- **payment-integration** — Integrates payment processors like Stripe with proper error handling, webhook verification, and PCI compliance
- **real-estate-tech** — Builds property technology platforms with MLS integration, geospatial search, property valuation models, and listing management systems
- **robotics-engineer** — Develops robotics systems with ROS2, sensor fusion, motion planning, SLAM, and real-time control loops
- **seo-specialist** — Optimizes web applications for search engine visibility with structured data, meta tags, and technical SEO implementation
- **voice-assistant** — Builds voice-enabled applications with speech-to-text, text-to-speech, dialog management, and platform integration for Alexa and Google Assistant

<!-- MUK_INVENTORY_END -->

## Example

User: "Muk â€” research our top 3 competitors in agentic IDEs, draft a battlecard, put it in a spreadsheet."

Plan:
1. `sales:competitive-intelligence` or `marketing:competitive-brief` for research
2. `xlsx` skill to build the spreadsheet
3. Share the file via `computer://` link

Execute, verify each step, deliver.

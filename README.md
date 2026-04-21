# Muk — Mukund Totla's Claude Code Marketplace

**One install, every device.** Mukund Totla's personal Claude Code marketplace — **82 skills, 129 plugins, 136 agents, 42 commands, 21 hooks, 15 rules, 8 templates, 14 MCP configs.** Orchestrated by the `muk` skill.

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Marketplace](https://img.shields.io/badge/Claude%20Code-Marketplace-8a63d2.svg)](#quick-install)
[![Skills](https://img.shields.io/badge/Skills-82-brightgreen.svg)](#skills)
[![Plugins](https://img.shields.io/badge/Plugins-129-orange.svg)](#plugins)
[![Agents](https://img.shields.io/badge/Agents-136-blueviolet.svg)](#agents)

---

## Muk Exclusives

Skills and plugins that live **only in this fork**. Everything else in this repo is a curated slice of the upstream toolkit (attribution below) — the four entries here are what make it *Muk*.

| Exclusive | Type | What It Does |
|-----------|------|--------------|
| [**muk**](skills/muk/SKILL.md) | Skill | Mukund's master orchestrator. Reads the full pack inventory, writes a plan, chains the right skills/agents/plugins/MCPs, verifies outputs, returns files via `computer://` links. Activate with `Muk`, `/muk`, `Hey Muk`, `orchestrate this`, or any multi-domain task. |
| [**generic-agent**](skills/generic-agent/SKILL.md) | Skill (reference) | Pointer to [GenericAgent](https://github.com/lsdefine/GenericAgent) — a self-evolving autonomous agent framework with direct control over browser, terminal, filesystem, keyboard/mouse, screen vision, and ADB. Standalone Python tool, installed separately. |
| [**android-reverse-engineering**](plugins/android-reverse-engineering/) | Plugin | Decompile Android APK / JAR / AAR with `jadx`, trace call flows through libraries, and document extracted APIs. Ships slash commands and a full skill. Source: [SimoneAvogadro](https://github.com/SimoneAvogadro/android-reverse-engineering-skill). |
| [**caveman** + **caveman-commit** + **caveman-help** + **caveman-review** + **compress**](skills/caveman/SKILL.md) | Skill pack | Caveman-style terse AI output — ~75% token reduction while preserving full technical accuracy. Five related skills for commit messages, help text, reviews, and generic text compression. Source: [juliusbrussee/caveman](https://github.com/juliusbrussee/caveman). |

---

## Newly Added

Latest additions to the pack. Muk orchestrates these alongside everything else — no manual wiring needed.

### Design plugins from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) (8 bundles)

Each bundle ships a cluster of related skills plus slash commands.

| Plugin | Description |
|--------|-------------|
| [`design-ops`](plugins/design-ops/) | Streamline design operations with critique frameworks, handoff specs, sprint planning, review processes, and team workflows. |
| [`design-research`](plugins/design-research/) | User research skills for designers: personas, empathy maps, journey maps, interview scripts, usability testing, and card sorting. |
| [`design-systems`](plugins/design-systems/) | Build, document, and maintain scalable design systems — from tokens and components to accessibility and theming. |
| [`designer-toolkit`](plugins/designer-toolkit/) | Essential designer utilities for writing rationale, building presentations, crafting case studies, UX writing, and driving adoption. |
| [`interaction-design`](plugins/interaction-design/) | Design meaningful interactions with micro-animations, state machines, gestures, error handling, and feedback patterns. |
| [`prototyping-testing`](plugins/prototyping-testing/) | Plan and execute design validation through prototyping strategies, usability testing, heuristic evaluation, and A/B experiments. |
| [`ui-design`](plugins/ui-design/) | Craft polished user interfaces with layout grids, color systems, typography scales, responsive patterns, and visual hierarchy. |
| [`ux-strategy`](plugins/ux-strategy/) | Shape product direction through competitive analysis, design principles, experience mapping, and strategic alignment. |

### Skills from [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills) (37 skills)

| Skill | Directory | What It Teaches |
|-------|-----------|-----------------|
| asr-transcribe-to-text | [`skills/asr-transcribe-to-text/`](skills/asr-transcribe-to-text/) | Transcribes audio and video files to text using Qwen3-ASR. Supports two modes — local MLX inference on macOS Apple Silicon (no API key, 15-27x realtime) and remote API via vLLM/Op… |
| capture-screen | [`skills/capture-screen/`](skills/capture-screen/) | Programmatic screenshot capture on macOS. Find window IDs with Swift CGWindowListCopyWindowInfo, control application windows via AppleScript (zoom, scroll, select), and capture wi… |
| cli-demo-generator | [`skills/cli-demo-generator/`](skills/cli-demo-generator/) | Generates professional animated CLI demos as GIFs using VHS terminal recordings. Handles tape file creation, self-bootstrapping demos with hidden setup, output noise filtering, po… |
| cloudflare-troubleshooting | [`skills/cloudflare-troubleshooting/`](skills/cloudflare-troubleshooting/) | Investigate and resolve Cloudflare configuration issues using API-driven evidence gathering. Use when troubleshooting ERR_TOO_MANY_REDIRECTS, SSL errors, DNS issues, or any Cloudf… |
| competitors-analysis | [`skills/competitors-analysis/`](skills/competitors-analysis/) | Analyze competitor repositories with evidence-based approach. Use when tracking competitors, creating competitor profiles, or generating competitive analysis. CRITICAL - all analy… |
| deep-research | [`skills/deep-research/`](skills/deep-research/) | \| |
| douban-skill | [`skills/douban-skill/`](skills/douban-skill/) | > |
| excel-automation | [`skills/excel-automation/`](skills/excel-automation/) | Create, parse, and control Excel files on macOS. Professional formatting with openpyxl, complex xlsm parsing with stdlib zipfile+xml for investment bank financial models, and Exce… |
| fact-checker | [`skills/fact-checker/`](skills/fact-checker/) | Verifies factual claims in documents using web search and official sources, then proposes corrections with user confirmation. Use when the user asks to fact-check, verify informat… |
| financial-data-collector | [`skills/financial-data-collector/`](skills/financial-data-collector/) | Collect real financial data for any US publicly traded company from free public sources (yfinance). Output structured JSON consumable by downstream financial skills (DCF modeling,… |
| gangtise-copilot | [`skills/gangtise-copilot/`](skills/gangtise-copilot/) | One-stop installer and companion for the full Gangtise (岗底斯投研) OpenAPI skill suite — 19 official skills covering data retrieval (OHLC 行情, 财务, 估值, 研报, 首席观点, 会议纪要, 调研纪要), research w… |
| github-contributor | [`skills/github-contributor/`](skills/github-contributor/) | Strategic guide for becoming an effective GitHub contributor. Covers opportunity discovery, project selection, high-quality PR creation, and reputation building. Use when looking… |
| github-ops | [`skills/github-ops/`](skills/github-ops/) | Provides comprehensive GitHub operations using gh CLI and GitHub API. Activates when working with pull requests, issues, repositories, workflows, or GitHub API operations includin… |
| i18n-expert | [`skills/i18n-expert/`](skills/i18n-expert/) | This skill should be used when setting up, auditing, or enforcing internationalization/localization in UI codebases (React/TS, i18next or similar, JSON locales), including install… |
| iOS-APP-developer | [`skills/iOS-APP-developer/`](skills/iOS-APP-developer/) | Develops iOS/macOS applications with XcodeGen, SwiftUI, and SPM. Handles Apple Developer signing, notarization, and CI/CD pipelines. Triggers on XcodeGen project.yml, SPM dependen… |
| ima-copilot | [`skills/ima-copilot/`](skills/ima-copilot/) | One-stop companion and installer for the official Tencent IMA skill (腾讯 IMA / ima.qq.com). Handles zero-config installation to Claude Code / Codex / OpenClaw via `npx skills add`,… |
| llm-icon-finder | [`skills/llm-icon-finder/`](skills/llm-icon-finder/) | Finding and accessing AI/LLM model brand icons from lobe-icons library. Use when users need icon URLs, want to download brand logos for AI models/providers/applications (Claude, G… |
| macos-cleaner | [`skills/macos-cleaner/`](skills/macos-cleaner/) | Analyze and reclaim macOS disk space through intelligent cleanup recommendations. This skill should be used when users report disk space issues, need to clean up their Mac, or wan… |
| product-analysis | [`skills/product-analysis/`](skills/product-analysis/) | Multi-path parallel product analysis with cross-model test-time compute scaling. Spawns parallel agents (Claude Code agent teams + Codex CLI) to explore product from multiple pers… |
| prompt-optimizer | [`skills/prompt-optimizer/`](skills/prompt-optimizer/) | Transform vague prompts into precise, well-structured specifications using EARS (Easy Approach to Requirements Syntax) methodology. This skill should be used when users provide lo… |
| promptfoo-evaluation | [`skills/promptfoo-evaluation/`](skills/promptfoo-evaluation/) | Configures and runs LLM evaluation using Promptfoo framework. Use when setting up prompt testing, creating evaluation configs (promptfooconfig.yaml), writing Python custom asserti… |
| qa-expert | [`skills/qa-expert/`](skills/qa-expert/) | This skill should be used when establishing comprehensive QA testing processes for any software project. Use when creating test strategies, writing test cases following Google Tes… |
| repomix-safe-mixer | [`skills/repomix-safe-mixer/`](skills/repomix-safe-mixer/) | Safely package codebases with repomix by automatically detecting and removing hardcoded credentials before packing. Use when packaging code for distribution, creating reference pa… |
| repomix-unmixer | [`skills/repomix-unmixer/`](skills/repomix-unmixer/) | Extracts files from repomix-packed repositories, restoring original directory structures from XML/Markdown/JSON formats. Activates when users need to unmix repomix files, extract… |
| scrapling-skill | [`skills/scrapling-skill/`](skills/scrapling-skill/) | Install, troubleshoot, and use Scrapling CLI to extract HTML, Markdown, or text from webpages. Use this skill whenever the user mentions Scrapling, `uv tool install scrapling`, `s… |
| skill-creator | [`skills/skill-creator/`](skills/skill-creator/) | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run… |
| skill-reviewer | [`skills/skill-reviewer/`](skills/skill-reviewer/) | Reviews and improves Claude Code skills against official best practices. Supports three modes - self-review (validate your own skills), external review (evaluate others' skills),… |
| skills-search | [`skills/skills-search/`](skills/skills-search/) | This skill should be used when users want to search, discover, install, or manage Claude Code skills from the CCPM registry. Triggers include requests like "find skills for PDF",… |
| teams-channel-post-writer | [`skills/teams-channel-post-writer/`](skills/teams-channel-post-writer/) | Creates educational Teams channel posts for internal knowledge sharing about Claude Code features, tools, and best practices. Applies when writing posts, announcements, or documen… |
| terraform-skill | [`skills/terraform-skill/`](skills/terraform-skill/) | Operational traps for Terraform provisioners, multi-environment isolation, and zero-to-deployment reliability. Covers provisioner timing races, SSH connection conflicts, DNS recor… |
| transcript-fixer | [`skills/transcript-fixer/`](skills/transcript-fixer/) | Corrects speech-to-text transcription errors using dictionary rules and AI-powered analysis. Builds personalized correction databases that learn from each fix. Triggers when worki… |
| tunnel-doctor | [`skills/tunnel-doctor/`](skills/tunnel-doctor/) | Diagnoses and fixes conflicts between Tailscale and proxy/VPN tools (Shadowrocket, Clash, Surge) on macOS. Covers five conflict layers - (1) route hijacking, (2) HTTP proxy env va… |
| twitter-reader | [`skills/twitter-reader/`](skills/twitter-reader/) | Fetch Twitter/X post content including long-form Articles with full images and metadata. Use when Claude needs to retrieve tweet/article content, author info, engagement metrics,… |
| ui-designer | [`skills/ui-designer/`](skills/ui-designer/) | Extract design systems from reference UI images and generate implementation-ready UI design prompts. Use when users provide UI screenshots/mockups and want to create consistent de… |
| video-comparer | [`skills/video-comparer/`](skills/video-comparer/) | This skill should be used when comparing two videos to analyze compression results or quality differences. Generates interactive HTML reports with quality metrics (PSNR, SSIM) and… |
| windows-remote-desktop-connection-doctor | [`skills/windows-remote-desktop-connection-doctor/`](skills/windows-remote-desktop-connection-doctor/) | Diagnose Windows App (Microsoft Remote Desktop / Azure Virtual Desktop / W365) connection quality issues on macOS. Analyze transport protocol selection (UDP Shortpath vs WebSocket… |
| youtube-downloader | [`skills/youtube-downloader/`](skills/youtube-downloader/) | Download YouTube videos and HLS streams (m3u8) from platforms like Mux, Vimeo, etc. using yt-dlp and ffmpeg. Use this skill when users request downloading videos, extracting audio… |

---

## Quick Install

**Claude Code / Antigravity / VS Code / JetBrains:**

```bash
/plugin marketplace add pfmukund/Muk
/plugin install muk@Muk
```

To update later:

```bash
/plugin marketplace update Muk
```

**Manual clone:**

```bash
git clone https://github.com/pfmukund/Muk.git ~/.claude/plugins/muk
```

**Claude.ai web + mobile:** Upload any skill folder from `skills/` via Settings → Capabilities → Skills. Skills sync to your phone via your Claude account.

---

## Table of Contents

- [Muk Exclusives](#muk-exclusives)
- [Newly Added](#newly-added)
- [Plugins](#plugins) (129)
- [Agents](#agents) (136)
- [Skills](#skills) (82)
- [Commands](#commands) (42)
- [Hooks](#hooks) (21)
- [Rules](#rules) (15)
- [Templates](#templates) (8)
- [MCP Configs](#mcp-configs) (14)
- [How Muk Works](#how-muk-works)
- [Adding Skills Later](#adding-skills-later)
- [Attribution](#attribution)
- [License](#license)

---

## Plugins

129 plugins extending Claude Code with domain-specific capabilities.

| Plugin | Description |
|--------|-------------|
| [`a11y-audit`](plugins/a11y-audit/) | Full accessibility audit with WCAG compliance checking |
| [`accessibility-checker`](plugins/accessibility-checker/) | Scan for accessibility issues and fix ARIA attributes in web applications |
| [`adr-writer`](plugins/adr-writer/) | Architecture Decision Records authoring and management |
| [`ai-prompt-lab`](plugins/ai-prompt-lab/) | Improve and test AI prompts for better Claude Code interactions |
| [`analytics-reporter`](plugins/analytics-reporter/) | Generate analytics reports and dashboard configurations from project data |
| [`android-developer`](plugins/android-developer/) | Android and Kotlin development with Jetpack Compose |
| [`android-reverse-engineering`](plugins/android-reverse-engineering/) | Decompile Android APK/JAR/AAR with jadx, trace call flows through libraries, and document extracted APIs. |
| [`api-architect`](plugins/api-architect/) | API design, documentation, and testing with OpenAPI spec generation |
| [`api-benchmarker`](plugins/api-benchmarker/) | API endpoint benchmarking and performance reporting |
| [`api-reference`](plugins/api-reference/) | API reference documentation generation from source code |
| [`api-tester`](plugins/api-tester/) | Test API endpoints and run load tests against services |
| [`aws-helper`](plugins/aws-helper/) | AWS service configuration and deployment automation |
| [`azure-helper`](plugins/azure-helper/) | Azure service configuration and deployment automation |
| [`backend-architect`](plugins/backend-architect/) | Backend service architecture design with endpoint scaffolding |
| [`bug-detective`](plugins/bug-detective/) | Debug issues systematically with root cause analysis and execution tracing |
| [`bundle-analyzer`](plugins/bundle-analyzer/) | Frontend bundle size analysis and tree-shaking optimization |
| [`changelog-gen`](plugins/changelog-gen/) | Generate changelogs from git history with conventional commit parsing |
| [`changelog-writer`](plugins/changelog-writer/) | Detailed changelog authoring from git history and PRs |
| [`ci-debugger`](plugins/ci-debugger/) | Debug CI/CD pipeline failures and fix configurations |
| [`code-architect`](plugins/code-architect/) | Generate architecture diagrams and technical design documents |
| [`code-explainer`](plugins/code-explainer/) | Explain complex code and annotate files with inline documentation |
| [`code-guardian`](plugins/code-guardian/) | Automated code review, security scanning, and quality enforcement |
| [`code-review-assistant`](plugins/code-review-assistant/) | Automated code review with severity levels and actionable feedback |
| [`codebase-documenter`](plugins/codebase-documenter/) | Auto-document entire codebase with inline comments and API docs |
| [`color-contrast`](plugins/color-contrast/) | Color contrast checking and accessible color suggestions |
| [`commit-commands`](plugins/commit-commands/) | Advanced commit workflows with smart staging and push automation |
| [`complexity-reducer`](plugins/complexity-reducer/) | Reduce cyclomatic complexity and simplify functions |
| [`compliance-checker`](plugins/compliance-checker/) | Regulatory compliance verification for GDPR, SOC2, and HIPAA |
| [`content-creator`](plugins/content-creator/) | Technical content generation for blog posts and social media |
| [`context7-docs`](plugins/context7-docs/) | Fetch up-to-date library documentation via Context7 for accurate coding |
| [`contract-tester`](plugins/contract-tester/) | API contract testing with Pact for microservice compatibility |
| [`create-worktrees`](plugins/create-worktrees/) | Git worktree management for parallel development workflows |
| [`cron-scheduler`](plugins/cron-scheduler/) | Cron job configuration and schedule validation |
| [`css-cleaner`](plugins/css-cleaner/) | Find unused CSS and consolidate stylesheets |
| [`data-privacy`](plugins/data-privacy/) | Data privacy implementation with PII detection and anonymization |
| [`database-optimizer`](plugins/database-optimizer/) | Database query optimization with index recommendations and EXPLAIN analysis |
| [`dead-code-finder`](plugins/dead-code-finder/) | Find and remove dead code across the codebase |
| [`debug-session`](plugins/debug-session/) | Interactive debugging workflow with git bisect integration |
| [`dependency-manager`](plugins/dependency-manager/) | Audit, update, and manage project dependencies with safety checks |
| [`deploy-pilot`](plugins/deploy-pilot/) | Deployment automation with Dockerfile generation, CI/CD pipelines, and infrastructure as code |
| [`design-ops`](plugins/design-ops/) | Streamline design operations with critique frameworks, handoff specs, sprint planning, review processes, and team workflows. |
| [`design-research`](plugins/design-research/) | User research skills for designers: personas, empathy maps, journey maps, interview scripts, usability testing, and card sorting. |
| [`design-systems`](plugins/design-systems/) | Build, document, and maintain scalable design systems — from tokens and components to accessibility and theming. |
| [`designer-toolkit`](plugins/designer-toolkit/) | Essential designer utilities for writing rationale, building presentations, crafting case studies, UX writing, and driving adoption. |
| [`desktop-app`](plugins/desktop-app/) | Desktop application scaffolding with Electron or Tauri |
| [`devops-automator`](plugins/devops-automator/) | DevOps automation scripts for CI/CD, health checks, and deployments |
| [`discuss`](plugins/discuss/) | Debate implementation approaches with structured pros and cons analysis |
| [`doc-forge`](plugins/doc-forge/) | Documentation generation, API docs, and README maintenance |
| [`docker-helper`](plugins/docker-helper/) | Build optimized Docker images and improve Dockerfile best practices |
| [`double-check`](plugins/double-check/) | Verify code correctness with systematic second-pass analysis |
| [`e2e-runner`](plugins/e2e-runner/) | End-to-end test execution and recording for web applications |
| [`embedding-manager`](plugins/embedding-manager/) | Manage vector embeddings and similarity search |
| [`env-manager`](plugins/env-manager/) | Set up and validate environment configurations across environments |
| [`env-sync`](plugins/env-sync/) | Environment variable syncing and diff across environments |
| [`experiment-tracker`](plugins/experiment-tracker/) | ML experiment tracking with metrics logging and run comparison |
| [`explore`](plugins/explore/) | Smart codebase exploration with dependency mapping and structure analysis |
| [`feature-dev`](plugins/feature-dev/) | Full feature development workflow from spec to completion |
| [`finance-tracker`](plugins/finance-tracker/) | Development cost tracking with time estimates and budget reporting |
| [`fix-github-issue`](plugins/fix-github-issue/) | Auto-fix GitHub issues by analyzing issue details and implementing solutions |
| [`fix-pr`](plugins/fix-pr/) | Fix PR review comments automatically with context-aware patches |
| [`flutter-mobile`](plugins/flutter-mobile/) | Flutter app development with widget creation and platform channels |
| [`frontend-developer`](plugins/frontend-developer/) | Frontend component development with accessibility and responsive design |
| [`gcp-helper`](plugins/gcp-helper/) | Google Cloud Platform service configuration and deployment |
| [`git-flow`](plugins/git-flow/) | Git workflow management with feature branches, releases, and hotfix flows |
| [`github-issue-manager`](plugins/github-issue-manager/) | GitHub issue triage, creation, and management |
| [`helm-charts`](plugins/helm-charts/) | Helm chart generation and upgrade management |
| [`import-organizer`](plugins/import-organizer/) | Organize, sort, and clean import statements |
| [`infrastructure-maintainer`](plugins/infrastructure-maintainer/) | Infrastructure maintenance with security audits and update management |
| [`interaction-design`](plugins/interaction-design/) | Design meaningful interactions with micro-animations, state machines, gestures, error handling, and feedback patterns. |
| [`ios-developer`](plugins/ios-developer/) | iOS and Swift development with SwiftUI views and models |
| [`k8s-helper`](plugins/k8s-helper/) | Generate Kubernetes manifests and debug pod issues with kubectl |
| [`license-checker`](plugins/license-checker/) | License compliance checking and NOTICE file generation |
| [`lighthouse-runner`](plugins/lighthouse-runner/) | Run Lighthouse audits and fix performance issues |
| [`linear-helper`](plugins/linear-helper/) | Linear issue tracking integration and workflow management |
| [`load-tester`](plugins/load-tester/) | Load and stress testing for APIs and web services |
| [`memory-profiler`](plugins/memory-profiler/) | Memory leak detection and heap analysis |
| [`migrate-tool`](plugins/migrate-tool/) | Generate database migrations and code migration scripts for framework upgrades |
| [`migration-generator`](plugins/migration-generator/) | Database migration generation and rollback management |
| [`model-context-protocol`](plugins/model-context-protocol/) | MCP server development helper with tool and resource scaffolding |
| [`model-evaluator`](plugins/model-evaluator/) | Evaluate and compare ML model performance metrics |
| [`monitoring-setup`](plugins/monitoring-setup/) | Monitoring and alerting configuration with dashboard generation |
| [`monorepo-manager`](plugins/monorepo-manager/) | Manage monorepo packages with affected detection and version synchronization |
| [`mutation-tester`](plugins/mutation-tester/) | Mutation testing to measure test suite quality |
| [`n8n-workflow`](plugins/n8n-workflow/) | Generate n8n automation workflows from natural language descriptions |
| [`onboarding-guide`](plugins/onboarding-guide/) | New developer onboarding documentation generator |
| [`openapi-expert`](plugins/openapi-expert/) | OpenAPI spec generation, validation, and client code scaffolding |
| [`optimize`](plugins/optimize/) | Code optimization for performance and bundle size reduction |
| [`perf-profiler`](plugins/perf-profiler/) | Performance analysis, profiling, and optimization recommendations |
| [`performance-monitor`](plugins/performance-monitor/) | Profile API endpoints and run benchmarks to identify performance bottlenecks |
| [`plan`](plugins/plan/) | Structured planning with risk assessment and time estimation |
| [`pr-reviewer`](plugins/pr-reviewer/) | Review pull requests with structured analysis and approve with confidence |
| [`product-shipper`](plugins/product-shipper/) | Ship features end-to-end with launch checklists and rollout plans |
| [`project-scaffold`](plugins/project-scaffold/) | Scaffold new projects and add features with best-practice templates |
| [`prompt-optimizer`](plugins/prompt-optimizer/) | Analyze and optimize AI prompts for better results |
| [`prototyping-testing`](plugins/prototyping-testing/) | Plan and execute design validation through prototyping strategies, usability testing, heuristic evaluation, and A/B experiments. |
| [`python-expert`](plugins/python-expert/) | Python-specific development with type hints and idiomatic refactoring |
| [`query-optimizer`](plugins/query-optimizer/) | SQL query optimization and execution plan analysis |
| [`rag-builder`](plugins/rag-builder/) | Build Retrieval-Augmented Generation pipelines |
| [`rapid-prototyper`](plugins/rapid-prototyper/) | Quick prototype scaffolding with minimal viable structure |
| [`react-native-dev`](plugins/react-native-dev/) | React Native mobile development with platform-specific optimizations |
| [`readme-generator`](plugins/readme-generator/) | Smart README generation from project analysis |
| [`refactor-engine`](plugins/refactor-engine/) | Extract functions, simplify complex code, and reduce cognitive complexity |
| [`regex-builder`](plugins/regex-builder/) | Build, test, and debug regular expression patterns |
| [`release-manager`](plugins/release-manager/) | Semantic versioning management and automated release workflows |
| [`responsive-designer`](plugins/responsive-designer/) | Responsive design implementation and testing |
| [`schema-designer`](plugins/schema-designer/) | Database schema design and ERD generation |
| [`screen-reader-tester`](plugins/screen-reader-tester/) | Screen reader compatibility testing and ARIA fixes |
| [`security-guidance`](plugins/security-guidance/) | Security best practices advisor with vulnerability detection and fixes |
| [`seed-generator`](plugins/seed-generator/) | Database seeding script generation with realistic data |
| [`slack-notifier`](plugins/slack-notifier/) | Slack integration for deployment and build notifications |
| [`smart-commit`](plugins/smart-commit/) | Intelligent git commits with conventional format, semantic analysis, and changelog generation |
| [`sprint-prioritizer`](plugins/sprint-prioritizer/) | Sprint planning with story prioritization and capacity estimation |
| [`technical-sales`](plugins/technical-sales/) | Technical demo creation and POC proposal writing |
| [`terraform-helper`](plugins/terraform-helper/) | Terraform module creation and infrastructure planning |
| [`test-data-generator`](plugins/test-data-generator/) | Generate realistic test data and seed databases |
| [`test-results-analyzer`](plugins/test-results-analyzer/) | Analyze test failures, identify patterns, and suggest targeted fixes |
| [`test-writer`](plugins/test-writer/) | Generate comprehensive unit and integration tests with full coverage |
| [`tool-evaluator`](plugins/tool-evaluator/) | Evaluate and compare developer tools with structured scoring criteria |
| [`type-migrator`](plugins/type-migrator/) | Migrate JavaScript files to TypeScript with proper types |
| [`ui-design`](plugins/ui-design/) | Craft polished user interfaces with layout grids, color systems, typography scales, responsive patterns, and visual hierarchy. |
| [`ui-designer`](plugins/ui-designer/) | Implement UI designs from specs with pixel-perfect component generation |
| [`ultrathink`](plugins/ultrathink/) | Deep analysis mode with extended reasoning for complex problems |
| [`unit-test-generator`](plugins/unit-test-generator/) | Generate comprehensive unit tests for any function or module |
| [`update-branch`](plugins/update-branch/) | Rebase and update feature branches with conflict resolution |
| [`ux-strategy`](plugins/ux-strategy/) | Shape product direction through competitive analysis, design principles, experience mapping, and strategic alignment. |
| [`vision-specialist`](plugins/vision-specialist/) | Image and visual analysis with screenshot interpretation and text extraction |
| [`visual-regression`](plugins/visual-regression/) | Visual regression testing with screenshot comparison |
| [`web-dev`](plugins/web-dev/) | Full-stack web development with app scaffolding and page generation |
| [`workflow-optimizer`](plugins/workflow-optimizer/) | Development workflow analysis and optimization recommendations |

### Installing a plugin

```bash
/plugin install muk@<plugin-name>
```

---

## Agents

136 specialized agents across 10 categories.

### Business Product (12 agents)

| Agent | File | Purpose |
|-------|------|---------|
| business-analyst | [`business-analyst.md`](agents/business-product/business-analyst.md) | Performs requirements analysis, process mapping, gap analysis, and stakeholder alignment for technical projects |
| content-strategist | [`content-strategist.md`](agents/business-product/content-strategist.md) | Plans content strategy with SEO-driven writing, editorial calendars, topic clustering, and content performance measurement |
| customer-success | [`customer-success.md`](agents/business-product/customer-success.md) | Builds customer support infrastructure with ticket triage, knowledge base systems, workflow automation, and customer health scoring |
| growth-engineer | [`growth-engineer.md`](agents/business-product/growth-engineer.md) | Implements A/B testing frameworks, analytics instrumentation, funnel optimization, and data-driven growth experiments |
| legal-advisor | [`legal-advisor.md`](agents/business-product/legal-advisor.md) | Drafts terms of service, privacy policies, software licenses, and compliance documentation for technology products |
| marketing-analyst | [`marketing-analyst.md`](agents/business-product/marketing-analyst.md) | Implements campaign analysis, attribution modeling, ROI tracking, and marketing data infrastructure for data-driven growth decisions |
| product-manager | [`product-manager.md`](agents/business-product/product-manager.md) | Creates PRDs, user stories, acceptance criteria, and prioritization frameworks for product development |
| project-manager | [`project-manager.md`](agents/business-product/project-manager.md) | Manages sprint planning, task tracking, timeline estimation, and Agile ceremony facilitation |
| sales-engineer | [`sales-engineer.md`](agents/business-product/sales-engineer.md) | Creates technical demos, proof-of-concept implementations, integration guides, and competitive technical analysis for sales engagements |
| scrum-master | [`scrum-master.md`](agents/business-product/scrum-master.md) | Facilitates Scrum ceremonies, tracks team velocity, removes impediments, and drives continuous improvement |
| technical-writer | [`technical-writer.md`](agents/business-product/technical-writer.md) | Produces polished technical documentation with consistent style, clear structure, and audience-appropriate language |
| ux-researcher | [`ux-researcher.md`](agents/business-product/ux-researcher.md) | Designs and conducts user research studies including usability testing, surveys, and behavioral analysis |

### Core Development (13 agents)

| Agent | File | Purpose |
|-------|------|---------|
| api-designer | [`api-designer.md`](agents/core-development/api-designer.md) | REST and GraphQL API design with OpenAPI specs, versioning, and pagination patterns |
| api-gateway-engineer | [`api-gateway-engineer.md`](agents/core-development/api-gateway-engineer.md) | API gateway patterns, rate limiting, authentication proxies, and request routing |
| backend-developer | [`backend-developer.md`](agents/core-development/backend-developer.md) | Node.js backend development with Express, Fastify, middleware patterns, and API performance optimization |
| electron-developer | [`electron-developer.md`](agents/core-development/electron-developer.md) | Electron desktop applications, IPC communication, native OS integration, and auto-updates |
| event-driven-architect | [`event-driven-architect.md`](agents/core-development/event-driven-architect.md) | Event sourcing, CQRS, message queues, and distributed event-driven system design |
| frontend-architect | [`frontend-architect.md`](agents/core-development/frontend-architect.md) | React/Next.js specialist with performance optimization, SSR/SSG, and accessibility |
| fullstack-engineer | [`fullstack-engineer.md`](agents/core-development/fullstack-engineer.md) | End-to-end feature development across frontend, backend, and database layers |
| graphql-architect | [`graphql-architect.md`](agents/core-development/graphql-architect.md) | GraphQL schema design, resolver implementation, federation, and performance optimization with DataLoader |
| microservices-architect | [`microservices-architect.md`](agents/core-development/microservices-architect.md) | Distributed systems design with event-driven architecture, saga patterns, service mesh, and observability |
| mobile-developer | [`mobile-developer.md`](agents/core-development/mobile-developer.md) | React Native and Flutter cross-platform specialist with native bridge patterns |
| monorepo-architect | [`monorepo-architect.md`](agents/core-development/monorepo-architect.md) | Turborepo/Nx workspace strategies, dependency graphs, and monorepo build optimization |
| ui-designer | [`ui-designer.md`](agents/core-development/ui-designer.md) | UI/UX implementation, design systems, Figma-to-code translation, and component libraries |
| websocket-engineer | [`websocket-engineer.md`](agents/core-development/websocket-engineer.md) | Real-time communication with WebSockets, Socket.io, scaling strategies, and reconnection handling |

### Data Ai (16 agents)

| Agent | File | Purpose |
|-------|------|---------|
| ai-engineer | [`ai-engineer.md`](agents/data-ai/ai-engineer.md) | AI application development with model API integration, RAG pipelines, agent frameworks, and embedding strategies |
| autoresearch-agent | [`autoresearch-agent.md`](agents/data-ai/autoresearch-agent.md) | Automated ML experiment optimization using tree search — designs experiments, generates code, evaluates results, and iterates |
| computer-vision-engineer | [`computer-vision-engineer.md`](agents/data-ai/computer-vision-engineer.md) | Builds image classification, object detection, and segmentation pipelines using OpenCV, PyTorch, and production-grade inference optimization |
| data-engineer | [`data-engineer.md`](agents/data-ai/data-engineer.md) | Data pipeline engineering with ETL/ELT workflows, Spark, data warehousing, and pipeline orchestration |
| data-scientist | [`data-scientist.md`](agents/data-ai/data-scientist.md) | Statistical analysis, data visualization, hypothesis testing, and exploratory data analysis with Python |
| data-visualization | [`data-visualization.md`](agents/data-ai/data-visualization.md) | Creates interactive dashboards and data visualizations using D3.js, Chart.js, Matplotlib, and Plotly with accessibility and performance optimization |
| database-optimizer | [`database-optimizer.md`](agents/data-ai/database-optimizer.md) | Database performance optimization with query tuning, indexing strategies, partitioning, and capacity planning |
| etl-specialist | [`etl-specialist.md`](agents/data-ai/etl-specialist.md) | Builds robust data pipelines with schema evolution, data quality checks, incremental loading, and fault-tolerant processing |
| feature-engineer | [`feature-engineer.md`](agents/data-ai/feature-engineer.md) | Designs feature stores, feature pipelines, and encoding strategies that ensure consistent feature computation across training and serving |
| llm-architect | [`llm-architect.md`](agents/data-ai/llm-architect.md) | LLM system design with fine-tuning, model selection, inference optimization, and evaluation frameworks |
| ml-engineer | [`ml-engineer.md`](agents/data-ai/ml-engineer.md) | Machine learning pipeline development with training, evaluation, feature engineering, and model deployment |
| mlops-engineer | [`mlops-engineer.md`](agents/data-ai/mlops-engineer.md) | ML model lifecycle management with serving infrastructure, monitoring, A/B testing, and CI/CD for models |
| nlp-engineer | [`nlp-engineer.md`](agents/data-ai/nlp-engineer.md) | NLP pipeline development with text processing, embeddings, classification, NER, and transformer fine-tuning |
| prompt-engineer | [`prompt-engineer.md`](agents/data-ai/prompt-engineer.md) | Prompt optimization with chain-of-thought, structured outputs, few-shot learning, and systematic evaluation |
| recommendation-engine | [`recommendation-engine.md`](agents/data-ai/recommendation-engine.md) | Designs recommendation systems using collaborative filtering, content-based methods, and hybrid approaches with real-time personalization |
| vector-database-engineer | [`vector-database-engineer.md`](agents/data-ai/vector-database-engineer.md) | Designs embedding pipelines and vector search systems using FAISS, Pinecone, Qdrant, and Weaviate for semantic retrieval at scale |

### Developer Experience (15 agents)

| Agent | File | Purpose |
|-------|------|---------|
| api-documentation | [`api-documentation.md`](agents/developer-experience/api-documentation.md) | Creates comprehensive API documentation using OpenAPI/Swagger, Redoc, and interactive examples with versioning and change tracking |
| build-engineer | [`build-engineer.md`](agents/developer-experience/build-engineer.md) | Designs and optimizes build systems, bundlers, and compilation pipelines for fast and reliable artifact production |
| cli-developer | [`cli-developer.md`](agents/developer-experience/cli-developer.md) | Builds robust CLI tools using Commander.js, yargs, clap, and other frameworks with polished user interfaces |
| dependency-manager | [`dependency-manager.md`](agents/developer-experience/dependency-manager.md) | Audits, updates, and manages project dependencies with attention to security, compatibility, and lockfile integrity |
| developer-portal | [`developer-portal.md`](agents/developer-experience/developer-portal.md) | Builds internal developer portals using Backstage, service catalogs, and self-service infrastructure for platform engineering |
| documentation-engineer | [`documentation-engineer.md`](agents/developer-experience/documentation-engineer.md) | Creates technical documentation including API references, guides, tutorials, and architecture decision records |
| dx-optimizer | [`dx-optimizer.md`](agents/developer-experience/dx-optimizer.md) | Improves developer experience through tooling ergonomics, workflow friction reduction, and environment standardization |
| git-workflow-manager | [`git-workflow-manager.md`](agents/developer-experience/git-workflow-manager.md) | Designs Git branching strategies, CI integration patterns, and repository workflow automation |
| legacy-modernizer | [`legacy-modernizer.md`](agents/developer-experience/legacy-modernizer.md) | Plans and executes legacy codebase migrations with incremental strategies and risk mitigation |
| mcp-developer | [`mcp-developer.md`](agents/developer-experience/mcp-developer.md) | Develops MCP servers and tools following the Model Context Protocol specification for AI agent integration |
| monorepo-tooling | [`monorepo-tooling.md`](agents/developer-experience/monorepo-tooling.md) | Manages monorepo infrastructure with changesets, workspace dependencies, version management, and selective CI pipelines |
| refactoring-specialist | [`refactoring-specialist.md`](agents/developer-experience/refactoring-specialist.md) | Performs systematic code refactoring including dead code removal, abstraction extraction, and structural improvements |
| testing-infrastructure | [`testing-infrastructure.md`](agents/developer-experience/testing-infrastructure.md) | Designs test runners, CI test splitting, flaky test management, and test infrastructure that scales across large engineering organizations |
| tooling-engineer | [`tooling-engineer.md`](agents/developer-experience/tooling-engineer.md) | Configures and builds developer tooling including linters, formatters, type checkers, and custom code analysis tools |
| vscode-extension | [`vscode-extension.md`](agents/developer-experience/vscode-extension.md) | Develops VS Code extensions with Language Server Protocol integration, custom editors, webview panels, and marketplace publishing |

### Infrastructure (11 agents)

| Agent | File | Purpose |
|-------|------|---------|
| cloud-architect | [`cloud-architect.md`](agents/infrastructure/cloud-architect.md) | AWS/GCP/Azure multi-cloud patterns, IaC, cost optimization, and well-architected framework |
| database-admin | [`database-admin.md`](agents/infrastructure/database-admin.md) | PostgreSQL, MySQL, MongoDB optimization, migrations, replication, and backup strategies |
| deployment-engineer | [`deployment-engineer.md`](agents/infrastructure/deployment-engineer.md) | Blue-green deployments, canary releases, rolling updates, and feature flag management |
| devops-engineer | [`devops-engineer.md`](agents/infrastructure/devops-engineer.md) | CI/CD pipelines, Docker, Kubernetes, monitoring, and GitOps workflows |
| incident-responder | [`incident-responder.md`](agents/infrastructure/incident-responder.md) | Incident triage, runbook execution, communication protocols, and recovery procedures |
| kubernetes-specialist | [`kubernetes-specialist.md`](agents/infrastructure/kubernetes-specialist.md) | Kubernetes operators, CRDs, service mesh with Istio, and advanced cluster management |
| network-engineer | [`network-engineer.md`](agents/infrastructure/network-engineer.md) | DNS management, load balancer configuration, CDN setup, and firewall rule design |
| platform-engineer | [`platform-engineer.md`](agents/infrastructure/platform-engineer.md) | Internal developer platforms, service mesh, observability, and SLO/SLI management |
| security-engineer | [`security-engineer.md`](agents/infrastructure/security-engineer.md) | Infrastructure security, IAM policies, mTLS, secrets management with Vault, and compliance |
| sre-engineer | [`sre-engineer.md`](agents/infrastructure/sre-engineer.md) | SLOs, error budgets, incident response, postmortems, and production reliability |
| terraform-engineer | [`terraform-engineer.md`](agents/infrastructure/terraform-engineer.md) | Infrastructure as Code with Terraform, module design, state management, and multi-cloud provisioning |

### Language Experts (25 agents)

| Agent | File | Purpose |
|-------|------|---------|
| angular-architect | [`angular-architect.md`](agents/language-experts/angular-architect.md) | Angular 17+ development with signals, standalone components, RxJS patterns, and NgRx state management |
| clojure-developer | [`clojure-developer.md`](agents/language-experts/clojure-developer.md) | REPL-driven development, persistent data structures, Ring/Compojure, and ClojureScript |
| csharp-developer | [`csharp-developer.md`](agents/language-experts/csharp-developer.md) | C# and .NET 8+ development with ASP.NET Core, Entity Framework Core, minimal APIs, and async patterns |
| django-developer | [`django-developer.md`](agents/language-experts/django-developer.md) | Django 5+ development with Django REST Framework, ORM optimization, migrations, and async views |
| elixir-expert | [`elixir-expert.md`](agents/language-experts/elixir-expert.md) | Elixir development with Phoenix, OTP supervision trees, LiveView, and distributed systems on BEAM |
| flutter-expert | [`flutter-expert.md`](agents/language-experts/flutter-expert.md) | Flutter 3+ cross-platform development with Dart, state management, navigation, and platform channels |
| golang-developer | [`golang-developer.md`](agents/language-experts/golang-developer.md) | Go concurrency patterns, interfaces, error handling, testing, and module management |
| haskell-developer | [`haskell-developer.md`](agents/language-experts/haskell-developer.md) | Pure functional programming, monads, type classes, GHC extensions, and Haskell ecosystem |
| java-architect | [`java-architect.md`](agents/language-experts/java-architect.md) | Spring Boot 3+ application architecture with JPA, security, microservices, and reactive programming |
| kotlin-specialist | [`kotlin-specialist.md`](agents/language-experts/kotlin-specialist.md) | Kotlin development with coroutines, Ktor, Kotlin Multiplatform, and idiomatic patterns |
| lua-developer | [`lua-developer.md`](agents/language-experts/lua-developer.md) | Game scripting with Lua, Neovim plugin development, embedded Lua integration, and LuaJIT |
| nextjs-developer | [`nextjs-developer.md`](agents/language-experts/nextjs-developer.md) | Next.js 14+ App Router development with React Server Components, ISR, middleware, and edge runtime |
| nim-developer | [`nim-developer.md`](agents/language-experts/nim-developer.md) | Nim metaprogramming, GC strategies, C/C++ interop, and cross-compilation |
| ocaml-developer | [`ocaml-developer.md`](agents/language-experts/ocaml-developer.md) | OCaml type inference, pattern matching, Dream web framework, and opam ecosystem |
| php-developer | [`php-developer.md`](agents/language-experts/php-developer.md) | PHP 8.3+ and Laravel 11 development with Eloquent, queues, middleware, and Composer package management |
| python-engineer | [`python-engineer.md`](agents/language-experts/python-engineer.md) | Python 3.12+ with typing, async/await, dataclasses, pydantic, and packaging |
| rails-expert | [`rails-expert.md`](agents/language-experts/rails-expert.md) | Ruby on Rails 7+ development with Hotwire, ActiveRecord patterns, Turbo, and Stimulus |
| react-specialist | [`react-specialist.md`](agents/language-experts/react-specialist.md) | React 19 development with hooks, state management, concurrent features, and component architecture |
| rust-systems | [`rust-systems.md`](agents/language-experts/rust-systems.md) | Rust ownership, lifetimes, async runtime, FFI, unsafe patterns, and performance tuning |
| scala-developer | [`scala-developer.md`](agents/language-experts/scala-developer.md) | Functional programming in Scala, Akka actors, Play Framework, and Cats Effect |
| svelte-developer | [`svelte-developer.md`](agents/language-experts/svelte-developer.md) | SvelteKit development with runes, server-side rendering, form actions, and fine-grained reactivity |
| swift-developer | [`swift-developer.md`](agents/language-experts/swift-developer.md) | SwiftUI, iOS 17+, Combine, structured concurrency, and Apple platform development |
| typescript-specialist | [`typescript-specialist.md`](agents/language-experts/typescript-specialist.md) | Advanced TypeScript patterns including generics, conditional types, and module augmentation |
| vue-specialist | [`vue-specialist.md`](agents/language-experts/vue-specialist.md) | Vue 3 development with Composition API, Pinia state management, Nuxt 3, and VueUse composables |
| zig-developer | [`zig-developer.md`](agents/language-experts/zig-developer.md) | Zig systems programming, comptime metaprogramming, allocator strategies, and C interop |

### Orchestration (8 agents)

| Agent | File | Purpose |
|-------|------|---------|
| agent-installer | [`agent-installer.md`](agents/orchestration/agent-installer.md) | Install and configure agent collections, resolve dependencies, and validate environments |
| context-manager | [`context-manager.md`](agents/orchestration/context-manager.md) | Context window optimization, progressive loading, and strategic compaction |
| error-coordinator | [`error-coordinator.md`](agents/orchestration/error-coordinator.md) | Handle errors across multi-agent workflows, implement recovery strategies, and prevent cascading failures |
| knowledge-synthesizer | [`knowledge-synthesizer.md`](agents/orchestration/knowledge-synthesizer.md) | Compress and synthesize information across sources, build knowledge graphs, and extract insights |
| multi-agent-coordinator | [`multi-agent-coordinator.md`](agents/orchestration/multi-agent-coordinator.md) | Coordinate parallel agent execution, manage dependencies, and merge outputs from multiple agents |
| performance-monitor | [`performance-monitor.md`](agents/orchestration/performance-monitor.md) | Monitor agent execution, track token usage, measure response quality, and optimize workflows |
| task-coordinator | [`task-coordinator.md`](agents/orchestration/task-coordinator.md) | Multi-agent task distribution, dependency management, and parallel execution |
| workflow-director | [`workflow-director.md`](agents/orchestration/workflow-director.md) | End-to-end workflow orchestration, checkpoint management, and error recovery |

### Quality Assurance (10 agents)

| Agent | File | Purpose |
|-------|------|---------|
| accessibility-specialist | [`accessibility-specialist.md`](agents/quality-assurance/accessibility-specialist.md) | WCAG 2.2 compliance, screen reader testing, keyboard navigation, and ARIA patterns |
| chaos-engineer | [`chaos-engineer.md`](agents/quality-assurance/chaos-engineer.md) | Chaos testing, fault injection, resilience validation, and failure mode analysis |
| code-reviewer | [`code-reviewer.md`](agents/quality-assurance/code-reviewer.md) | Comprehensive code review covering patterns, anti-patterns, security, performance, and readability |
| compliance-auditor | [`compliance-auditor.md`](agents/quality-assurance/compliance-auditor.md) | SOC 2, GDPR, HIPAA compliance checking, audit evidence collection, and policy enforcement |
| error-detective | [`error-detective.md`](agents/quality-assurance/error-detective.md) | Error tracking, stack trace analysis, reproduction step generation, and root cause identification |
| penetration-tester | [`penetration-tester.md`](agents/quality-assurance/penetration-tester.md) | Authorized security testing, OWASP Top 10 assessment, vulnerability reporting, and remediation guidance |
| performance-engineer | [`performance-engineer.md`](agents/quality-assurance/performance-engineer.md) | Profiling, benchmarking, memory analysis, load testing, and optimization patterns |
| qa-automation | [`qa-automation.md`](agents/quality-assurance/qa-automation.md) | Test automation frameworks, CI integration, test data management, and reporting |
| security-auditor | [`security-auditor.md`](agents/quality-assurance/security-auditor.md) | OWASP Top 10, dependency scanning, secrets detection, and penetration testing guidance |
| test-architect | [`test-architect.md`](agents/quality-assurance/test-architect.md) | Testing strategy with unit/integration/e2e, TDD, property-based testing, and mutation testing |

### Research Analysis (11 agents)

| Agent | File | Purpose |
|-------|------|---------|
| academic-researcher | [`academic-researcher.md`](agents/research-analysis/academic-researcher.md) | Conducts literature reviews, citation analysis, methodology evaluation, and research synthesis for technical and scientific topics |
| benchmarking-specialist | [`benchmarking-specialist.md`](agents/research-analysis/benchmarking-specialist.md) | Designs performance benchmarks, load tests, comparative evaluations, and reproducible measurement methodologies for software systems |
| competitive-analyst | [`competitive-analyst.md`](agents/research-analysis/competitive-analyst.md) | Performs competitive analysis including feature comparison, market positioning, and strategic differentiation assessment |
| data-researcher | [`data-researcher.md`](agents/research-analysis/data-researcher.md) | Performs data analysis, pattern recognition, statistical interpretation, and evidence-based insight extraction |
| market-researcher | [`market-researcher.md`](agents/research-analysis/market-researcher.md) | Conducts market sizing, TAM/SAM/SOM analysis, competitive intelligence, survey design, and customer segment identification |
| patent-analyst | [`patent-analyst.md`](agents/research-analysis/patent-analyst.md) | Conducts patent searches, prior art analysis, IP landscape mapping, and freedom-to-operate assessments for technology products |
| research-analyst | [`research-analyst.md`](agents/research-analysis/research-analyst.md) | Conducts structured technical research with systematic literature review, evidence synthesis, and actionable findings |
| search-specialist | [`search-specialist.md`](agents/research-analysis/search-specialist.md) | Performs advanced search, information retrieval, source evaluation, and knowledge synthesis across diverse sources |
| security-researcher | [`security-researcher.md`](agents/research-analysis/security-researcher.md) | Conducts CVE analysis, vulnerability research, threat modeling, attack surface assessment, and security advisory evaluation |
| technology-scout | [`technology-scout.md`](agents/research-analysis/technology-scout.md) | Evaluates emerging technologies, conducts build-vs-buy analysis, assesses vendor solutions, and produces technology adoption recommendations |
| trend-analyst | [`trend-analyst.md`](agents/research-analysis/trend-analyst.md) | Analyzes technology trends, adoption curves, and ecosystem shifts to inform strategic technical decisions |

### Specialized Domains (15 agents)

| Agent | File | Purpose |
|-------|------|---------|
| blockchain-developer | [`blockchain-developer.md`](agents/specialized-domains/blockchain-developer.md) | Develops smart contracts and Web3 applications with Solidity, Hardhat, and blockchain integration patterns |
| e-commerce-engineer | [`e-commerce-engineer.md`](agents/specialized-domains/e-commerce-engineer.md) | Builds e-commerce systems including product catalogs, shopping carts, inventory management, and order processing |
| education-tech | [`education-tech.md`](agents/specialized-domains/education-tech.md) | Builds learning management systems with SCORM/xAPI compliance, adaptive learning engines, assessment tools, and learner analytics |
| embedded-systems | [`embedded-systems.md`](agents/specialized-domains/embedded-systems.md) | Develops firmware and embedded software in C and Rust with RTOS integration and hardware abstraction |
| fintech-engineer | [`fintech-engineer.md`](agents/specialized-domains/fintech-engineer.md) | Builds financial systems with precise arithmetic, regulatory compliance, audit trails, and transaction integrity |
| game-developer | [`game-developer.md`](agents/specialized-domains/game-developer.md) | Designs game systems, logic, and architecture patterns for Unity, Godot, and custom game engines |
| geospatial-engineer | [`geospatial-engineer.md`](agents/specialized-domains/geospatial-engineer.md) | Builds GIS applications with PostGIS, spatial queries, mapping APIs, tile servers, and geospatial data processing pipelines |
| healthcare-engineer | [`healthcare-engineer.md`](agents/specialized-domains/healthcare-engineer.md) | Builds HIPAA-compliant healthcare systems with HL7 FHIR interoperability, medical data pipelines, and clinical workflow integration |
| iot-engineer | [`iot-engineer.md`](agents/specialized-domains/iot-engineer.md) | Designs IoT systems with MQTT messaging, edge computing, device management, and telemetry pipelines |
| media-streaming | [`media-streaming.md`](agents/specialized-domains/media-streaming.md) | Builds video streaming platforms with HLS/DASH delivery, transcoding pipelines, CDN optimization, and adaptive bitrate streaming |
| payment-integration | [`payment-integration.md`](agents/specialized-domains/payment-integration.md) | Integrates payment processors like Stripe with proper error handling, webhook verification, and PCI compliance |
| real-estate-tech | [`real-estate-tech.md`](agents/specialized-domains/real-estate-tech.md) | Builds property technology platforms with MLS integration, geospatial search, property valuation models, and listing management systems |
| robotics-engineer | [`robotics-engineer.md`](agents/specialized-domains/robotics-engineer.md) | Develops robotics systems with ROS2, sensor fusion, motion planning, SLAM, and real-time control loops |
| seo-specialist | [`seo-specialist.md`](agents/specialized-domains/seo-specialist.md) | Optimizes web applications for search engine visibility with structured data, meta tags, and technical SEO implementation |
| voice-assistant | [`voice-assistant.md`](agents/specialized-domains/voice-assistant.md) | Builds voice-enabled applications with speech-to-text, text-to-speech, dialog management, and platform integration for Alexa and Google Assistant |

### Using agents

Reference an agent in your `CLAUDE.md`:

```markdown
## Agents
- Use `agents/core-development/fullstack-engineer.md` for feature delivery
- Use `agents/quality-assurance/code-reviewer.md` for PR reviews
```

---

## Skills

82 skills teaching Claude domain-specific patterns. The `muk`, `generic-agent`, `caveman`, `caveman-commit`, `caveman-help`, `caveman-review`, and `compress` skills are Muk-exclusive (see [Exclusives](#muk-exclusives)).

| Skill | Directory | What It Teaches |
|-------|-----------|-----------------|
| accessibility-wcag | [`skills/accessibility-wcag/`](skills/accessibility-wcag/) | Web accessibility patterns for WCAG 2.2 compliance including ARIA, keyboard navigation, screen readers, and testing |
| api-design-patterns | [`skills/api-design-patterns/`](skills/api-design-patterns/) | REST API design with resource naming, pagination, versioning, and OpenAPI spec generation |
| asr-transcribe-to-text | [`skills/asr-transcribe-to-text/`](skills/asr-transcribe-to-text/) | Transcribes audio and video files to text using Qwen3-ASR. Supports two modes — local MLX inference on macOS Apple Silicon (no API key, 15-27x realtime) and remote API via vLLM/Op… |
| authentication-patterns | [`skills/authentication-patterns/`](skills/authentication-patterns/) | Authentication and authorization patterns including OAuth2, JWT, RBAC, session management, and PKCE flows |
| aws-cloud-patterns | [`skills/aws-cloud-patterns/`](skills/aws-cloud-patterns/) | AWS cloud patterns for Lambda, ECS, S3, DynamoDB, and Infrastructure as Code with CDK/Terraform |
| capture-screen | [`skills/capture-screen/`](skills/capture-screen/) | Programmatic screenshot capture on macOS. Find window IDs with Swift CGWindowListCopyWindowInfo, control application windows via AppleScript (zoom, scroll, select), and capture wi… |
| caveman | [`skills/caveman/`](skills/caveman/) | > |
| caveman-commit | [`skills/caveman-commit/`](skills/caveman-commit/) | > |
| caveman-help | [`skills/caveman-help/`](skills/caveman-help/) | > |
| caveman-review | [`skills/caveman-review/`](skills/caveman-review/) | > |
| ci-cd-pipelines | [`skills/ci-cd-pipelines/`](skills/ci-cd-pipelines/) | CI/CD pipeline patterns for GitHub Actions, GitLab CI, testing strategies, and deployment automation |
| claude-memory-kit | [`skills/claude-memory-kit/`](skills/claude-memory-kit/) | Persistent memory system for Claude Code. Two-layer architecture (hot cache + knowledge wiki), safety hooks, /close-day end-of-day synthesis. Zero external dependencies. |
| cli-demo-generator | [`skills/cli-demo-generator/`](skills/cli-demo-generator/) | Generates professional animated CLI demos as GIFs using VHS terminal recordings. Handles tape file creation, self-bootstrapping demos with hidden setup, output noise filtering, po… |
| cloudflare-troubleshooting | [`skills/cloudflare-troubleshooting/`](skills/cloudflare-troubleshooting/) | Investigate and resolve Cloudflare configuration issues using API-driven evidence gathering. Use when troubleshooting ERR_TOO_MANY_REDIRECTS, SSL errors, DNS issues, or any Cloudf… |
| competitors-analysis | [`skills/competitors-analysis/`](skills/competitors-analysis/) | Analyze competitor repositories with evidence-based approach. Use when tracking competitors, creating competitor profiles, or generating competitive analysis. CRITICAL - all analy… |
| compress | [`skills/compress/`](skills/compress/) | > |
| continuous-learning | [`skills/continuous-learning/`](skills/continuous-learning/) | Auto-extract patterns from coding sessions, track corrections, and build reusable knowledge with confidence scoring |
| data-engineering | [`skills/data-engineering/`](skills/data-engineering/) | Data engineering patterns for ETL pipelines, data warehousing, Apache Spark, and data quality validation |
| database-optimization | [`skills/database-optimization/`](skills/database-optimization/) | Query optimization, indexing strategies, and database performance tuning for PostgreSQL and MySQL |
| deep-dive | [`skills/deep-dive/`](skills/deep-dive/) | Claude-native deep research using DAG-based query planning, parallel subagent execution, and gap-driven iteration. No external API needed. |
| deep-research | [`skills/deep-research/`](skills/deep-research/) | \| |
| devops-automation | [`skills/devops-automation/`](skills/devops-automation/) | CI/CD pipeline design with GitHub Actions, Docker, Kubernetes, Helm, and GitOps patterns |
| django-patterns | [`skills/django-patterns/`](skills/django-patterns/) | Django architecture patterns including DRF, ORM optimization, signals, middleware, and project structure |
| docker-best-practices | [`skills/docker-best-practices/`](skills/docker-best-practices/) | Docker best practices including multi-stage builds, compose patterns, image optimization, and security |
| douban-skill | [`skills/douban-skill/`](skills/douban-skill/) | > |
| excel-automation | [`skills/excel-automation/`](skills/excel-automation/) | Create, parse, and control Excel files on macOS. Professional formatting with openpyxl, complex xlsm parsing with stdlib zipfile+xml for investment bank financial models, and Exce… |
| fact-checker | [`skills/fact-checker/`](skills/fact-checker/) | Verifies factual claims in documents using web search and official sources, then proposes corrections with user confirmation. Use when the user asks to fact-check, verify informat… |
| financial-data-collector | [`skills/financial-data-collector/`](skills/financial-data-collector/) | Collect real financial data for any US publicly traded company from free public sources (yfinance). Output structured JSON consumable by downstream financial skills (DCF modeling,… |
| frontend-excellence | [`skills/frontend-excellence/`](skills/frontend-excellence/) | Modern frontend patterns for React Server Components, performance optimization, and Core Web Vitals |
| gangtise-copilot | [`skills/gangtise-copilot/`](skills/gangtise-copilot/) | One-stop installer and companion for the full Gangtise (岗底斯投研) OpenAPI skill suite — 19 official skills covering data retrieval (OHLC 行情, 财务, 估值, 研报, 首席观点, 会议纪要, 调研纪要), research w… |
| generic-agent | [`skills/generic-agent/`](skills/generic-agent/) | Reference pointer to GenericAgent — a self-evolving autonomous agent framework (https://github.com/lsdefine/GenericAgent) that gives an LLM direct control over a local computer (b… |
| git-advanced | [`skills/git-advanced/`](skills/git-advanced/) | Advanced git workflows including worktrees, bisect, interactive rebase, hooks, and recovery techniques |
| github-contributor | [`skills/github-contributor/`](skills/github-contributor/) | Strategic guide for becoming an effective GitHub contributor. Covers opportunity discovery, project selection, high-quality PR creation, and reputation building. Use when looking… |
| github-ops | [`skills/github-ops/`](skills/github-ops/) | Provides comprehensive GitHub operations using gh CLI and GitHub API. Activates when working with pull requests, issues, repositories, workflows, or GitHub API operations includin… |
| golang-idioms | [`skills/golang-idioms/`](skills/golang-idioms/) | Idiomatic Go patterns for error handling, interfaces, concurrency, testing, and module management |
| graphql-design | [`skills/graphql-design/`](skills/graphql-design/) | GraphQL schema design, resolver patterns, subscriptions, DataLoader for N+1 prevention, and error handling |
| i18n-expert | [`skills/i18n-expert/`](skills/i18n-expert/) | This skill should be used when setting up, auditing, or enforcing internationalization/localization in UI codebases (React/TS, i18next or similar, JSON locales), including install… |
| iOS-APP-developer | [`skills/iOS-APP-developer/`](skills/iOS-APP-developer/) | Develops iOS/macOS applications with XcodeGen, SwiftUI, and SPM. Handles Apple Developer signing, notarization, and CI/CD pipelines. Triggers on XcodeGen project.yml, SPM dependen… |
| ima-copilot | [`skills/ima-copilot/`](skills/ima-copilot/) | One-stop companion and installer for the official Tencent IMA skill (腾讯 IMA / ima.qq.com). Handles zero-config installation to Claude Code / Codex / OpenClaw via `npx skills add`,… |
| kubernetes-operations | [`skills/kubernetes-operations/`](skills/kubernetes-operations/) | Kubernetes operations including manifests, Helm charts, operators, troubleshooting, and resource management |
| llm-icon-finder | [`skills/llm-icon-finder/`](skills/llm-icon-finder/) | Finding and accessing AI/LLM model brand icons from lobe-icons library. Use when users need icon URLs, want to download brand logos for AI models/providers/applications (Claude, G… |
| llm-integration | [`skills/llm-integration/`](skills/llm-integration/) | LLM integration patterns including API usage, streaming, function calling, RAG pipelines, and cost optimization |
| macos-cleaner | [`skills/macos-cleaner/`](skills/macos-cleaner/) | Analyze and reclaim macOS disk space through intelligent cleanup recommendations. This skill should be used when users report disk space issues, need to clean up their Mac, or wan… |
| manage-skills | [`skills/manage-skills/`](skills/manage-skills/) | Discover, list, create, edit, toggle, copy, move, and delete AI agent skills across 11 tools (Cursor, Claude, Agents, Windsurf, Copilot, Codex, Cline, Aider, Continue, Roo Code, A… |
| mcp-development | [`skills/mcp-development/`](skills/mcp-development/) | MCP server development including tool design, resource endpoints, prompt templates, and transport configuration |
| microservices-design | [`skills/microservices-design/`](skills/microservices-design/) | Microservices design patterns including service mesh, event-driven architecture, saga pattern, and API gateway |
| mobile-development | [`skills/mobile-development/`](skills/mobile-development/) | Mobile development patterns for React Native and Flutter including navigation, state management, and responsive design |
| monitoring-observability | [`skills/monitoring-observability/`](skills/monitoring-observability/) | Monitoring and observability with OpenTelemetry, Prometheus, Grafana dashboards, and structured logging |
| muk | [`skills/muk/`](skills/muk/) | Mukund Totla's personal master orchestrator — activate with "Muk", "/muk", "Hey Muk", "Muk go", "use Muk", "activate Muk", or just describe any complex task and this skill will in… |
| nextjs-mastery | [`skills/nextjs-mastery/`](skills/nextjs-mastery/) | Next.js 14+ App Router patterns including RSC, ISR, middleware, parallel routes, and data fetching |
| performance-optimization | [`skills/performance-optimization/`](skills/performance-optimization/) | Web performance optimization including bundle analysis, lazy loading, caching strategies, and Core Web Vitals |
| postgres-optimization | [`skills/postgres-optimization/`](skills/postgres-optimization/) | PostgreSQL optimization including indexes, query plans, partitioning, JSONB operations, and connection pooling |
| product-analysis | [`skills/product-analysis/`](skills/product-analysis/) | Multi-path parallel product analysis with cross-model test-time compute scaling. Spawns parallel agents (Claude Code agent teams + Codex CLI) to explore product from multiple pers… |
| prompt-engineering | [`skills/prompt-engineering/`](skills/prompt-engineering/) | Prompt engineering patterns including structured prompts, chain-of-thought, few-shot learning, and system prompt design |
| prompt-optimizer | [`skills/prompt-optimizer/`](skills/prompt-optimizer/) | Transform vague prompts into precise, well-structured specifications using EARS (Easy Approach to Requirements Syntax) methodology. This skill should be used when users provide lo… |
| promptfoo-evaluation | [`skills/promptfoo-evaluation/`](skills/promptfoo-evaluation/) | Configures and runs LLM evaluation using Promptfoo framework. Use when setting up prompt testing, creating evaluation configs (promptfooconfig.yaml), writing Python custom asserti… |
| python-best-practices | [`skills/python-best-practices/`](skills/python-best-practices/) | Pythonic code with modern type hints, dataclasses, async patterns, packaging, and testing |
| qa-expert | [`skills/qa-expert/`](skills/qa-expert/) | This skill should be used when establishing comprehensive QA testing processes for any software project. Use when creating test strategies, writing test cases following Google Tes… |
| react-patterns | [`skills/react-patterns/`](skills/react-patterns/) | React 19 patterns including Server Components, Actions, Suspense, hooks, and component composition |
| redis-patterns | [`skills/redis-patterns/`](skills/redis-patterns/) | Redis patterns including caching strategies, pub/sub, streams for event processing, Lua scripts, and data structures |
| repomix-safe-mixer | [`skills/repomix-safe-mixer/`](skills/repomix-safe-mixer/) | Safely package codebases with repomix by automatically detecting and removing hardcoded credentials before packing. Use when packaging code for distribution, creating reference pa… |
| repomix-unmixer | [`skills/repomix-unmixer/`](skills/repomix-unmixer/) | Extracts files from repomix-packed repositories, restoring original directory structures from XML/Markdown/JSON formats. Activates when users need to unmix repomix files, extract… |
| rust-systems | [`skills/rust-systems/`](skills/rust-systems/) | Rust systems programming patterns including ownership, traits, async runtime, error handling, and unsafe guidelines |
| scrapling-skill | [`skills/scrapling-skill/`](skills/scrapling-skill/) | Install, troubleshoot, and use Scrapling CLI to extract HTML, Markdown, or text from webpages. Use this skill whenever the user mentions Scrapling, `uv tool install scrapling`, `s… |
| security-hardening | [`skills/security-hardening/`](skills/security-hardening/) | Application security covering input validation, auth, headers, secrets management, and dependency auditing |
| skill-creator | [`skills/skill-creator/`](skills/skill-creator/) | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run… |
| skill-reviewer | [`skills/skill-reviewer/`](skills/skill-reviewer/) | Reviews and improves Claude Code skills against official best practices. Supports three modes - self-review (validate your own skills), external review (evaluate others' skills),… |
| skills-search | [`skills/skills-search/`](skills/skills-search/) | This skill should be used when users want to search, discover, install, or manage Claude Code skills from the CCPM registry. Triggers include requests like "find skills for PDF",… |
| springboot-patterns | [`skills/springboot-patterns/`](skills/springboot-patterns/) | Spring Boot patterns including JPA repositories, REST controllers, layered services, and configuration |
| tdd-mastery | [`skills/tdd-mastery/`](skills/tdd-mastery/) | Test-driven development workflow with Red-Green-Refactor cycle across languages |
| teams-channel-post-writer | [`skills/teams-channel-post-writer/`](skills/teams-channel-post-writer/) | Creates educational Teams channel posts for internal knowledge sharing about Claude Code features, tools, and best practices. Applies when writing posts, announcements, or documen… |
| terraform-skill | [`skills/terraform-skill/`](skills/terraform-skill/) | Operational traps for Terraform provisioners, multi-environment isolation, and zero-to-deployment reliability. Covers provisioner timing races, SSH connection conflicts, DNS recor… |
| testing-strategies | [`skills/testing-strategies/`](skills/testing-strategies/) | Testing strategies including contract testing, snapshot testing, mutation testing, property-based testing, and test organization |
| transcript-fixer | [`skills/transcript-fixer/`](skills/transcript-fixer/) | Corrects speech-to-text transcription errors using dictionary rules and AI-powered analysis. Builds personalized correction databases that learn from each fix. Triggers when worki… |
| tunnel-doctor | [`skills/tunnel-doctor/`](skills/tunnel-doctor/) | Diagnoses and fixes conflicts between Tailscale and proxy/VPN tools (Shadowrocket, Clash, Surge) on macOS. Covers five conflict layers - (1) route hijacking, (2) HTTP proxy env va… |
| twitter-reader | [`skills/twitter-reader/`](skills/twitter-reader/) | Fetch Twitter/X post content including long-form Articles with full images and metadata. Use when Claude needs to retrieve tweet/article content, author info, engagement metrics,… |
| typescript-advanced | [`skills/typescript-advanced/`](skills/typescript-advanced/) | Advanced TypeScript patterns including generics, conditional types, mapped types, template literals, and type guards |
| ui-designer | [`skills/ui-designer/`](skills/ui-designer/) | Extract design systems from reference UI images and generate implementation-ready UI design prompts. Use when users provide UI screenshots/mockups and want to create consistent de… |
| video-comparer | [`skills/video-comparer/`](skills/video-comparer/) | This skill should be used when comparing two videos to analyze compression results or quality differences. Generates interactive HTML reports with quality metrics (PSNR, SSIM) and… |
| websocket-realtime | [`skills/websocket-realtime/`](skills/websocket-realtime/) | Real-time communication patterns with WebSocket, Socket.io, Server-Sent Events, and scaling strategies |
| windows-remote-desktop-connection-doctor | [`skills/windows-remote-desktop-connection-doctor/`](skills/windows-remote-desktop-connection-doctor/) | Diagnose Windows App (Microsoft Remote Desktop / Azure Virtual Desktop / W365) connection quality issues on macOS. Analyze transport protocol selection (UDP Shortpath vs WebSocket… |
| youtube-downloader | [`skills/youtube-downloader/`](skills/youtube-downloader/) | Download YouTube videos and HLS streams (m3u8) from platforms like Mux, Vimeo, etc. using yt-dlp and ffmpeg. Use this skill when users request downloading videos, extracting audio… |

---

## Commands

42 slash commands organized by function (git, testing, architecture, documentation, security, refactoring, devops, workflow). Drop into `.claude/commands/`:

```bash
cp -r commands/ .claude/commands/
```

Browse: [`commands/`](commands/)

---

## Hooks

21 hook scripts covering Claude Code lifecycle events (SessionStart, SessionEnd, PreToolUse, PostToolUse, PreCompact, Stop, Notification, UserPromptSubmit).

```bash
cp hooks/hooks.json .claude/hooks.json
cp -r hooks/scripts/ .claude/hooks/scripts/
```

Browse: [`hooks/`](hooks/)

---

## Rules

15 coding rules enforcing consistent patterns (coding style, git workflow, testing, security, performance, docs, error handling, and more).

Browse: [`rules/`](rules/)

---

## Templates

8 `CLAUDE.md` templates for different project types (minimal, standard, comprehensive, monorepo, enterprise, python, fullstack).

```bash
cp templates/claude-md/standard.md CLAUDE.md
```

Browse: [`templates/`](templates/)

---

## MCP Configs

14 curated Model Context Protocol server configurations (fullstack, kubernetes, data-science, and more).

Browse: [`mcp-configs/`](mcp-configs/)

---

## How Muk works

Activate with `Muk`, `/muk`, `Hey Muk`, `orchestrate this`, or any complex task.

1. **Read** — Muk restates the goal in one sentence.
2. **Survey** — consults the pack inventory in [`skills/muk/SKILL.md`](skills/muk/SKILL.md) and anything else installed on the current Claude instance.
3. **Plan** — writes a short numbered plan naming each skill / agent / plugin / MCP it will use.
4. **Execute** — parallelizes independent steps, uses subagents for heavy isolated work.
5. **Verify** — sanity-checks outputs (counts, links, file opens, math) before declaring done.
6. **Deliver** — returns files via `computer://` links and suggests a next action.

The authoritative index is [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json), regenerated by `scripts/sync_marketplace.py`.

---

## Adding skills later

1. Drop a new skill under `skills/<name>/SKILL.md`
2. `python3 scripts/sync_marketplace.py` — refreshes marketplace.json + Muk inventory
3. `python3 scripts/gen_readme.py` — regenerates this README
4. `git add . && git commit -m "Add <name>" && git push`
5. On each device: `/plugin marketplace update Muk`

---

## Attribution

This marketplace is forked and personalized from [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) (Apache-2.0). Third-party additions:

- **`muk`** skill — written for this pack
- **`generic-agent`** skill — reference pointer to [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent)
- **`android-reverse-engineering`** plugin — from [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill)
- **`caveman` / `caveman-commit` / `caveman-help` / `caveman-review` / `compress`** skills — from [juliusbrussee/caveman](https://github.com/juliusbrussee/caveman)
- **8 design plugins** (`design-ops`, `design-research`, `design-systems`, `designer-toolkit`, `interaction-design`, `prototyping-testing`, `ui-design`, `ux-strategy`) — from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) (MIT)
- **37 skills** (asr-transcribe-to-text, capture-screen, github-ops, deep-research, qa-expert, and more) — from [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills)
- **`scripts/sync_marketplace.py`** and **`scripts/gen_readme.py`** — written for this pack

All upstream authorship and licensing is preserved.

---

## License

Apache-2.0 — see [`LICENSE`](LICENSE).

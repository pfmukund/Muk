#!/usr/bin/env python3
"""Generate README.md for the Muk marketplace from disk state.

- Top section is hand-written (branding, install, Exclusives).
- Plugin / Agent / Skill / Command / Hook / Rule / Template / MCP tables are
  regenerated from the actual filesystem so counts never drift from reality.
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")


# --- helpers ----------------------------------------------------------------

def read_safe(path, n=4000):
    try:
        return open(path, encoding="utf-8", errors="replace").read(n)
    except Exception:
        return ""


def frontmatter_desc(path):
    t = read_safe(path)
    mo = re.search(r"^description:\s*(.+)$", t, re.MULTILINE)
    return mo.group(1).strip().strip('"').strip("'") if mo else ""


def first_para(path, maxlen=200):
    t = read_safe(path)
    lines = [l.strip() for l in t.splitlines() if l.strip()]
    for i, l in enumerate(lines):
        if l.startswith("#") and i + 1 < len(lines):
            nxt = lines[i + 1]
            if not nxt.startswith("#") and not nxt.startswith("---") and not nxt.startswith("["):
                return nxt[:maxlen]
    return ""


def plugin_desc(name):
    pj = os.path.join(ROOT, "plugins", name, ".claude-plugin", "plugin.json")
    if os.path.isfile(pj):
        try:
            d = json.load(open(pj, encoding="utf-8")).get("description", "")
            if d:
                return d
        except Exception:
            pass
    return first_para(os.path.join(ROOT, "plugins", name, "README.md")) or ""


def clip(s, n=180):
    s = (s or "").replace("|", "\\|").replace("\n", " ").strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


# --- inventories ------------------------------------------------------------

skills_dir = os.path.join(ROOT, "skills")
skill_names = sorted([n for n in os.listdir(skills_dir)
                      if os.path.isfile(os.path.join(skills_dir, n, "SKILL.md"))])
skills = [(n, frontmatter_desc(os.path.join(skills_dir, n, "SKILL.md")) or f"Skill: {n}")
          for n in skill_names]

plugins_dir = os.path.join(ROOT, "plugins")
plugin_names = sorted([n for n in os.listdir(plugins_dir)
                       if os.path.isdir(os.path.join(plugins_dir, n))])
plugins = [(n, plugin_desc(n) or f"Plugin: {n}") for n in plugin_names]

agents_dir = os.path.join(ROOT, "agents")
agents_by_cat = {}
for cat in sorted(os.listdir(agents_dir)):
    cat_dir = os.path.join(agents_dir, cat)
    if not os.path.isdir(cat_dir):
        continue
    rows = []
    for fn in sorted(os.listdir(cat_dir)):
        if fn.endswith(".md"):
            p = os.path.join(cat_dir, fn)
            rows.append((fn[:-3], f"agents/{cat}/{fn}",
                         frontmatter_desc(p) or first_para(p) or f"Agent: {fn[:-3]}"))
    if rows:
        agents_by_cat[cat] = rows

n_agents = sum(len(v) for v in agents_by_cat.values())


def count_files(d, ext=None):
    p = os.path.join(ROOT, d)
    if not os.path.isdir(p):
        return 0
    c = 0
    for r, _, fs in os.walk(p):
        for f in fs:
            if ext is None or f.endswith(ext):
                c += 1
    return c


n_commands = count_files("commands", ".md")
n_hooks = count_files("hooks")
n_rules = count_files("rules", ".md")
n_templates = count_files("templates")
n_mcp = count_files("mcp-configs")

# --- render -----------------------------------------------------------------

EXCLUSIVES = """## Muk Exclusives

Skills and plugins that live **only in this fork**. Everything else in this repo is a curated slice of the upstream toolkit (attribution below) — the four entries here are what make it *Muk*.

| Exclusive | Type | What It Does |
|-----------|------|--------------|
| [**muk**](skills/muk/SKILL.md) | Skill | Mukund's master orchestrator. Reads the full pack inventory, writes a plan, chains the right skills/agents/plugins/MCPs, verifies outputs, returns files via `computer://` links. Activate with `Muk`, `/muk`, `Hey Muk`, `orchestrate this`, or any multi-domain task. |
| [**generic-agent**](skills/generic-agent/SKILL.md) | Skill (reference) | Pointer to [GenericAgent](https://github.com/lsdefine/GenericAgent) — a self-evolving autonomous agent framework with direct control over browser, terminal, filesystem, keyboard/mouse, screen vision, and ADB. Standalone Python tool, installed separately. |
| [**android-reverse-engineering**](plugins/android-reverse-engineering/) | Plugin | Decompile Android APK / JAR / AAR with `jadx`, trace call flows through libraries, and document extracted APIs. Ships slash commands and a full skill. Source: [SimoneAvogadro](https://github.com/SimoneAvogadro/android-reverse-engineering-skill). |
| [**caveman** + **caveman-commit** + **caveman-help** + **caveman-review** + **compress**](skills/caveman/SKILL.md) | Skill pack | Caveman-style terse AI output — ~75% token reduction while preserving full technical accuracy. Five related skills for commit messages, help text, reviews, and generic text compression. Source: [juliusbrussee/caveman](https://github.com/juliusbrussee/caveman). |
"""

# Manually maintained per source — bump when adding from new repos.
NEWLY_ADDED_DESIGNER = ["design-ops", "design-research", "design-systems",
                        "designer-toolkit", "interaction-design",
                        "prototyping-testing", "ui-design", "ux-strategy"]
NEWLY_ADDED_DAYMADE = [
    "asr-transcribe-to-text", "capture-screen", "cli-demo-generator",
    "cloudflare-troubleshooting", "competitors-analysis", "deep-research",
    "douban-skill", "excel-automation", "fact-checker",
    "financial-data-collector", "gangtise-copilot", "github-contributor",
    "github-ops", "i18n-expert", "iOS-APP-developer", "ima-copilot",
    "llm-icon-finder", "macos-cleaner", "product-analysis",
    "prompt-optimizer", "promptfoo-evaluation", "qa-expert",
    "repomix-safe-mixer", "repomix-unmixer", "scrapling-skill",
    "skill-creator", "skill-reviewer", "skills-search",
    "teams-channel-post-writer", "terraform-skill", "transcript-fixer",
    "tunnel-doctor", "twitter-reader", "ui-designer", "video-comparer",
    "windows-remote-desktop-connection-doctor", "youtube-downloader",
]
NEWLY_ADDED_ANTHROPICS = [
    "algorithmic-art", "brand-guidelines", "canvas-design", "claude-api",
    "doc-coauthoring", "docx", "frontend-design", "internal-comms",
    "mcp-builder", "pdf", "pptx", "slack-gif-creator", "theme-factory",
    "web-artifacts-builder", "webapp-testing", "xlsx",
]
NEWLY_ADDED_COMPOSIOHQ = ["composio", "artifacts-builder",
                          "changelog-generator", "competitive-ads-extractor"]
NEWLY_ADDED_COREYHAINES = [
    "ab-test-setup", "ad-creative", "ai-seo", "analytics-tracking",
    "aso-audit", "churn-prevention", "cold-email", "community-marketing",
    "competitor-alternatives", "content-strategy", "copy-editing",
    "copywriting", "customer-research", "email-sequence", "form-cro",
    "free-tool-strategy", "launch-strategy", "lead-magnets",
    "marketing-ideas", "marketing-psychology", "onboarding-cro",
    "page-cro", "paid-ads", "paywall-upgrade-cro", "popup-cro",
    "pricing-strategy", "product-marketing-context", "programmatic-seo",
    "referral-program", "revops", "sales-enablement", "schema-markup",
    "seo-audit", "signup-flow-cro", "site-architecture", "social-content",
]
NEWLY_ADDED_DISLER = ["agent-sandboxes"]
NEWLY_ADDED_OBRA = [
    "brainstorming", "dispatching-parallel-agents", "executing-plans",
    "finishing-a-development-branch", "receiving-code-review",
    "requesting-code-review", "subagent-driven-development",
    "systematic-debugging", "test-driven-development", "using-git-worktrees",
    "using-superpowers", "verification-before-completion", "writing-plans",
    "writing-skills",
]
NEWLY_ADDED_REMOTION = ["remotion"]
NEWLY_ADDED_SUPERMEMORY = ["supermemory"]
NEWLY_ADDED_VERCEL_BROWSER = [
    "agent-browser", "agent-browser-agentcore", "agent-browser-core",
    "agent-browser-dogfood", "agent-browser-electron", "agent-browser-slack",
    "agent-browser-vercel-sandbox",
]
NEWLY_ADDED_VERCEL_AGENTS = [
    "composition-patterns", "deploy-to-vercel", "react-best-practices",
    "react-native-skills", "react-view-transitions", "vercel-cli-with-tokens",
    "web-design-guidelines",
]


def _newly_added_block():
    plugin_lookup = dict(plugins)
    skill_lookup = dict(skills)

    total = (len(NEWLY_ADDED_DESIGNER) + len(NEWLY_ADDED_DAYMADE)
             + len(NEWLY_ADDED_ANTHROPICS) + len(NEWLY_ADDED_COMPOSIOHQ)
             + len(NEWLY_ADDED_COREYHAINES) + len(NEWLY_ADDED_DISLER)
             + len(NEWLY_ADDED_OBRA) + len(NEWLY_ADDED_REMOTION)
             + len(NEWLY_ADDED_SUPERMEMORY) + len(NEWLY_ADDED_VERCEL_BROWSER)
             + len(NEWLY_ADDED_VERCEL_AGENTS))

    out = ["## Newly Added", "",
           f"Latest additions to the pack — {total} skills and plugins across 12 sources. Muk orchestrates these alongside everything else; no manual wiring needed.",
           ""]

    def plugin_table(title, names):
        out.append(title)
        out.append("")
        out.append("| Plugin | Description |")
        out.append("|--------|-------------|")
        for n in names:
            d = plugin_lookup.get(n, "")
            out.append(f"| [`{n}`](plugins/{n}/) | {clip(d)} |")
        out.append("")

    def skill_table(title, names):
        out.append(title)
        out.append("")
        out.append("| Skill | Directory | What It Teaches |")
        out.append("|-------|-----------|-----------------|")
        for n in names:
            d = skill_lookup.get(n, "")
            out.append(f"| {n} | [`skills/{n}/`](skills/{n}/) | {clip(d)} |")
        out.append("")

    plugin_table(
        f"### Design plugins from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) ({len(NEWLY_ADDED_DESIGNER)} bundles)\n\nEach bundle ships a cluster of related skills plus slash commands.",
        NEWLY_ADDED_DESIGNER)

    skill_table(
        f"### Skills from [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills) ({len(NEWLY_ADDED_DAYMADE)} skills)",
        NEWLY_ADDED_DAYMADE)

    skill_table(
        f"### Official Anthropic skills from [anthropics/skills](https://github.com/anthropics/skills) ({len(NEWLY_ADDED_ANTHROPICS)} skills)\n\nIncluding `frontend-design` (recommended in the composio.dev roundup) plus document-processing (`pdf`, `docx`, `pptx`, `xlsx`) and design-system skills.",
        NEWLY_ADDED_ANTHROPICS)

    skill_table(
        f"### Composio skills from [ComposioHQ/skills](https://github.com/ComposioHQ/skills) and [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) ({len(NEWLY_ADDED_COMPOSIOHQ)} skills)\n\nComposio's toolkit wrappers for 1,000+ external APIs are available via `composio`. The `awesome-claude-skills` repo also ships 850+ auto-generated SaaS-specific automation skills (Ably, Abstract, Accelo, …) — not bundled here, but clone upstream when needed.",
        NEWLY_ADDED_COMPOSIOHQ)

    skill_table(
        f"### Marketing skills from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) ({len(NEWLY_ADDED_COREYHAINES)} skills)\n\nFull marketing operating system: CRO, SEO, paid ads, copywriting, launch strategy, email sequences, pricing, community, and more.",
        NEWLY_ADDED_COREYHAINES)

    skill_table(
        f"### Sandbox skill from [disler/agent-sandbox-skill](https://github.com/disler/agent-sandbox-skill) ({len(NEWLY_ADDED_DISLER)} skill)",
        NEWLY_ADDED_DISLER)

    skill_table(
        f"### Superpowers from [obra/superpowers](https://github.com/obra/superpowers) ({len(NEWLY_ADDED_OBRA)} skills)\n\nStructured multi-agent workflows: brainstorm → spec → plan → execute → review → merge. `systematic-debugging`, `verification-before-completion`, `subagent-driven-development`, and more.",
        NEWLY_ADDED_OBRA)

    skill_table(
        f"### Remotion skill from [remotion-dev/skills](https://github.com/remotion-dev/skills) ({len(NEWLY_ADDED_REMOTION)} skill)",
        NEWLY_ADDED_REMOTION)

    skill_table(
        f"### Supermemory skill from [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) ({len(NEWLY_ADDED_SUPERMEMORY)} skill)\n\nPersistent memory layer — tracks facts about users over time, resolves contradictions, auto-forgets expired info.",
        NEWLY_ADDED_SUPERMEMORY)

    skill_table(
        f"### Agent-browser from [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) ({len(NEWLY_ADDED_VERCEL_BROWSER)} skills)\n\nDeterministic ref-based control of web UIs. Includes the core `agent-browser` skill plus six integration-specific skill-data packs (AgentCore, Core, Dogfood, Electron, Slack, Vercel Sandbox) renamed to `agent-browser-*` to avoid generic name collisions.",
        NEWLY_ADDED_VERCEL_BROWSER)

    skill_table(
        f"### Agent-skills from [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) ({len(NEWLY_ADDED_VERCEL_AGENTS)} skills)\n\nIncluding `web-design-guidelines` (from the composio.dev roundup), `deploy-to-vercel`, `react-best-practices`, and `react-view-transitions`.",
        NEWLY_ADDED_VERCEL_AGENTS)

    return "\n".join(out)

parts = []

# Header
parts.append(f"""# Muk — Mukund Totla's Claude Code Marketplace

**One install, every device.** Mukund Totla's personal Claude Code marketplace — **{len(skills)} skills, {len(plugins)} plugins, {n_agents} agents, {n_commands} commands, {n_hooks} hooks, {n_rules} rules, {n_templates} templates, {n_mcp} MCP configs.** Orchestrated by the `muk` skill.

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Marketplace](https://img.shields.io/badge/Claude%20Code-Marketplace-8a63d2.svg)](#quick-install)
[![Skills](https://img.shields.io/badge/Skills-{len(skills)}-brightgreen.svg)](#skills)
[![Plugins](https://img.shields.io/badge/Plugins-{len(plugins)}-orange.svg)](#plugins)
[![Agents](https://img.shields.io/badge/Agents-{n_agents}-blueviolet.svg)](#agents)

---

""")

# Exclusives — on top, as requested (before Quick Install)
parts.append(EXCLUSIVES)
parts.append("\n---\n\n")

# Newly Added — right after Exclusives
parts.append(_newly_added_block())
parts.append("\n---\n\n")

parts.append("""## Quick Install

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

""")

# Table of contents
parts.append(f"""## Table of Contents

- [Muk Exclusives](#muk-exclusives)
- [Newly Added](#newly-added)
- [Plugins](#plugins) ({len(plugins)})
- [Agents](#agents) ({n_agents})
- [Skills](#skills) ({len(skills)})
- [Commands](#commands) ({n_commands})
- [Hooks](#hooks) ({n_hooks})
- [Rules](#rules) ({n_rules})
- [Templates](#templates) ({n_templates})
- [MCP Configs](#mcp-configs) ({n_mcp})
- [How Muk Works](#how-muk-works)
- [Adding Skills Later](#adding-skills-later)
- [Attribution](#attribution)
- [License](#license)

---

""")

# Plugins
parts.append(f"## Plugins\n\n{len(plugins)} plugins extending Claude Code with domain-specific capabilities.\n\n")
parts.append("| Plugin | Description |\n|--------|-------------|\n")
for name, desc in plugins:
    parts.append(f"| [`{name}`](plugins/{name}/) | {clip(desc)} |\n")
parts.append("\n### Installing a plugin\n\n```bash\n/plugin install muk@<plugin-name>\n```\n\n---\n\n")

# Agents
parts.append(f"## Agents\n\n{n_agents} specialized agents across {len(agents_by_cat)} categories.\n\n")
for cat, rows in agents_by_cat.items():
    parts.append(f"### {cat.replace('-', ' ').title()} ({len(rows)} agents)\n\n")
    parts.append("| Agent | File | Purpose |\n|-------|------|---------|\n")
    for name, path, desc in rows:
        parts.append(f"| {name} | [`{os.path.basename(path)}`]({path}) | {clip(desc)} |\n")
    parts.append("\n")
parts.append("""### Using agents

Reference an agent in your `CLAUDE.md`:

```markdown
## Agents
- Use `agents/core-development/fullstack-engineer.md` for feature delivery
- Use `agents/quality-assurance/code-reviewer.md` for PR reviews
```

---

""")

# Skills
parts.append(f"## Skills\n\n{len(skills)} skills teaching Claude domain-specific patterns. The `muk`, `generic-agent`, `caveman`, `caveman-commit`, `caveman-help`, `caveman-review`, and `compress` skills are Muk-exclusive (see [Exclusives](#muk-exclusives)).\n\n")
parts.append("| Skill | Directory | What It Teaches |\n|-------|-----------|-----------------|\n")
for name, desc in skills:
    parts.append(f"| {name} | [`skills/{name}/`](skills/{name}/) | {clip(desc)} |\n")
parts.append("\n---\n\n")

# Commands
parts.append(f"""## Commands

{n_commands} slash commands organized by function (git, testing, architecture, documentation, security, refactoring, devops, workflow). Drop into `.claude/commands/`:

```bash
cp -r commands/ .claude/commands/
```

Browse: [`commands/`](commands/)

---

## Hooks

{n_hooks} hook scripts covering Claude Code lifecycle events (SessionStart, SessionEnd, PreToolUse, PostToolUse, PreCompact, Stop, Notification, UserPromptSubmit).

```bash
cp hooks/hooks.json .claude/hooks.json
cp -r hooks/scripts/ .claude/hooks/scripts/
```

Browse: [`hooks/`](hooks/)

---

## Rules

{n_rules} coding rules enforcing consistent patterns (coding style, git workflow, testing, security, performance, docs, error handling, and more).

Browse: [`rules/`](rules/)

---

## Templates

{n_templates} `CLAUDE.md` templates for different project types (minimal, standard, comprehensive, monorepo, enterprise, python, fullstack).

```bash
cp templates/claude-md/standard.md CLAUDE.md
```

Browse: [`templates/`](templates/)

---

## MCP Configs

{n_mcp} curated Model Context Protocol server configurations (fullstack, kubernetes, data-science, and more).

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
- **37 skills** (asr-transcribe-to-text, github-ops, deep-research, qa-expert, excel-automation, and more) — from [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills)
- **16 official Anthropic skills** (`frontend-design`, `pdf`, `docx`, `pptx`, `xlsx`, `claude-api`, `mcp-builder`, `algorithmic-art`, `brand-guidelines`, `canvas-design`, `theme-factory`, `web-artifacts-builder`, `webapp-testing`, `slack-gif-creator`, `internal-comms`, `doc-coauthoring`) — from [anthropics/skills](https://github.com/anthropics/skills)
- **4 Composio skills** (`composio`, `artifacts-builder`, `changelog-generator`, `competitive-ads-extractor`) — from [ComposioHQ/skills](https://github.com/ComposioHQ/skills) and [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- **36 marketing skills** (CRO, SEO, paid ads, email, copywriting, pricing, launch, …) — from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)
- **14 Superpowers skills** (structured multi-agent workflows: brainstorm → plan → execute → review) — from [obra/superpowers](https://github.com/obra/superpowers)
- **7 agent-browser skills** (deterministic browser control + 6 integration packs) — from [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)
- **7 Vercel agent-skills** (`web-design-guidelines`, `deploy-to-vercel`, `react-best-practices`, `react-view-transitions`, …) — from [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)
- **`agent-sandboxes`** skill — from [disler/agent-sandbox-skill](https://github.com/disler/agent-sandbox-skill)
- **`remotion`** skill — from [remotion-dev/skills](https://github.com/remotion-dev/skills)
- **`supermemory`** skill — from [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory)
- **`scripts/sync_marketplace.py`** and **`scripts/gen_readme.py`** — written for this pack

All upstream authorship and licensing is preserved.

---

## License

Apache-2.0 — see [`LICENSE`](LICENSE).
""")

out = "".join(parts)
with open(README, "w", encoding="utf-8") as f:
    f.write(out)

print(f"README rewritten: {len(skills)} skills · {len(plugins)} plugins · {n_agents} agents · {n_commands} commands · {n_hooks} hooks · {n_rules} rules · {n_templates} templates · {n_mcp} mcp.")

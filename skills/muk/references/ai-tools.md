# AI Tool Routing — Claude MAX vs Claude Code vs Gemini vs ChatGPT

## Decision tree

```
Does the task touch a real repo (multi-file edits, run commands, git, tests, build)?
  YES → Claude Code
  NO  → continue

Is the primary input an image, video, audio, or Google Workspace doc (Docs/Sheets/Slides/Drive)?
  YES → Gemini (better multimodal + Workspace integration)
  NO  → continue

Does the task need an image generated?
  YES → ChatGPT Pro (DALL-E) — then bring the image back into the flow
  NO  → continue

Does the task need a ChatGPT-exclusive plugin or live web browsing w/ citations?
  YES → ChatGPT Pro
  NO  → default to Claude MAX
```

## Claude MAX (this model) — best at

- Deep reasoning and step-by-step thinking
- Architecture design, system design, trade-off analysis
- Documentation, technical writing, long-form prose
- Analyzing provided data and producing structured reports
- Single-file code that fits in a reply
- SQL, configs, YAML, prompt engineering, regex
- Cross-referencing many uploaded files / large text inputs
- Planning + project scoping + rubric design

## Claude Code — best at

- Real codebases — reads and writes across files, directories, monorepos
- Running commands: build, test, lint, git, npm, docker, terraform
- Multi-file refactors with verification (tests pass before commit)
- Deploy pipelines that need local file + remote API coordination
- Interactive debugging — greps logs, inspects state, iterates
- Generating PRs with diffs + descriptions
- Large-context coding tasks (entire repo in working memory)

**Rule**: if the work could fail without running or reading real files, it's Claude Code.

## Gemini — best at

- Multimodal input — images, video frames, audio transcripts, PDFs with figures
- Very large context windows (1M+ tokens) for huge corpora
- Google Workspace native integration — Docs, Sheets, Slides, Drive edits
- Tasks that need Google Search grounding with citations
- Quick vision tasks (OCR, layout extraction, screenshot analysis)

## ChatGPT Pro — best at

- DALL-E image generation (UI mockups, illustrations, social graphics)
- Custom GPT plugins you've configured
- Some specific research plugins / live browsing with formatted sources

## Multi-AI workflow examples

**Build a SaaS feature end-to-end**
1. Claude MAX — architecture + spec + OpenAPI schema
2. Claude Code — implement, write tests, run them, commit
3. Claude MAX — draft PR description, changelog entry, docs page

**Redesign a dashboard**
1. Gemini — analyze screenshots of current state
2. Claude MAX — propose redesign + wireframe spec
3. ChatGPT Pro — generate hero illustrations with DALL-E
4. Claude Code — implement the React components

**Migrate a large legacy codebase**
1. Gemini — scan the entire codebase (fits in context) and produce a map
2. Claude MAX — design the migration plan
3. Claude Code — execute file-by-file, run tests between batches

## When NOT to hand off

- Task fits in one reply AND doesn't need commands to run → just do it in Claude MAX
- User is in the middle of a conversation with context the other tool won't have — summarize the handoff explicitly
- The user is already in Claude Code (this session) — don't tell them to "send to Claude Code", you ARE Claude Code; just do the work

## Handoff format

When pointing the user at another AI, give a copy-pasteable block:

```
↳ Run this in [Tool name]:

[exact prompt, with all context the other tool needs since it has none of ours]
```

Never say "send to Claude Code" without giving the prompt — that's half a handoff.

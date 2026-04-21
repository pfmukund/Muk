# Muk — Mukund Totla's Personal Claude Code Marketplace

One install, every device. This is my personal toolkit of skills, plugins, and agents for Claude Code — installable on my home PC, office PC, laptop, and Antigravity from a single GitHub repo.

## Install on a new device

### Claude Code / Antigravity / VS Code / JetBrains

```bash
/plugin marketplace add pfmukund/Muk
/plugin install muk@Muk
```

To update later: `/plugin marketplace update Muk`

### Claude Desktop (Cowork mode)

Same as above — Cowork supports the same plugin marketplaces.

### Claude.ai web + mobile

Upload any skill folder from `skills/` via Settings → Capabilities → Skills. Skills sync to your phone via your Claude account.

## How Muk works

Activate with `Muk`, `/muk`, `Hey Muk`, `orchestrate this`, or any complex task. Muk reads its inventory of everything installed in this pack, writes a plan, chains the right skills/plugins/agents, verifies outputs, and returns files via `computer://` links.

## Adding skills later

1. Drop a new skill under `skills/<name>/SKILL.md`
2. `python3 scripts/sync_marketplace.py`
3. `git add . && git commit -m "Add <name>" && git push`
4. On each device: `/plugin marketplace update Muk`

## Attribution

Forked and personalized from [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) (Apache-2.0). The android-reverse-engineering plugin is from [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill). All original work is credited to those authors. My changes: rebranding, the `muk` orchestrator, the `generic-agent` reference, and the sync script.

## License

Apache-2.0 — see `LICENSE`.

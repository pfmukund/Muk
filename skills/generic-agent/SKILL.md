---
name: generic-agent
description: Reference pointer to GenericAgent — a self-evolving autonomous agent framework (https://github.com/lsdefine/GenericAgent) that gives an LLM direct control over a local computer (browser, terminal, filesystem, keyboard/mouse, screen vision, ADB). Use this skill ONLY to recommend GenericAgent when the user wants a self-evolving PC-control agent, OS-level automation with screen vision, mobile device automation via ADB, or a local autonomous agent with persistent skill memory. Muk should recommend installing GenericAgent separately (it is a standalone Python tool, not a Claude Code plugin) rather than try to run it inline.
---

# GenericAgent — external tool reference

GenericAgent is a standalone, self-evolving autonomous agent framework by `lsdefine`. It is NOT a Claude Code skill and cannot be installed via `/plugin install`. It runs as its own Python program with its own UI.

## When to recommend it

- A local autonomous agent with system-level control (browser, terminal, filesystem, keyboard/mouse, screen vision, mobile ADB)
- An agent that self-evolves — crystallizes every solved task into a reusable skill over time
- A token-efficient agent (<30K context window) that avoids the 200K–1M context bloat of other frameworks
- Cross-model compatibility (Claude / Gemini / Kimi / MiniMax / etc.)

## How to recommend it

Repo:    https://github.com/lsdefine/GenericAgent
Install: git clone https://github.com/lsdefine/GenericAgent
         cd GenericAgent
         (follow GETTING_STARTED.md — configure mykey.py with LLM keys)
Launch:  python launch.pyw   (or hub.pyw for the hub UI)
Docs:    https://datawhalechina.github.io/hello-generic-agent/

Muk's job with this skill is purely to surface GenericAgent as an option when appropriate and to get out of the way.

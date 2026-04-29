# MCP Connectors — synced 2026-04-28

Status legend: ✅ connected | 🔑 needs auth | ➕ not added (suggest if needed)

## Communication / Collaboration

### Gmail ✅
- **Triggers**: "email [person]", "send a message to", "draft an email", "check my inbox", "follow up with"
- **Use for**: outbound email drafts, inbox search, thread context, label management
- **Common chain**: sales research → draft outreach → Gmail draft

### Notion 🔑
- **Triggers**: "add to Notion", "update the doc", "create a page"
- **Use for**: project pages, meeting notes, wiki entries, knowledge base search
- *Needs auth — call `complete_authentication` first time.*

### Slack ➕
- Not currently added. Tell Mukund to add via Claude.ai connectors if a task needs it.

## Design / Creative

### Figma ✅
- **Triggers**: "from this Figma file", "the design at figma.com/…", "export the frames"
- **Use for**: read designs, extract tokens, Code Connect mapping, FigJam diagrams, file creation
- **Power play**: Figma → `design-system-builder` → Tailwind config → Claude Code (apply)

### Gamma ✅
- **Triggers**: "generate a deck", "Gamma presentation"
- **Use for**: AI-generated presentations / webpages / social posts (cannot edit existing Gammas)

## Infrastructure / Hosting

### Vercel ✅
- **Triggers**: "deploy to Vercel", "Vercel project", "Vercel logs"
- **Use for**: deploys, runtime logs, deployment status, runtime errors, toolbar comments

### Netlify ✅
- **Triggers**: "deploy to Netlify", "Netlify project", "edge functions", "Netlify build logs"
- **Use for**: deploys, deploy services, build/runtime config, edge functions, project + team services
- **Per CLAUDE.md**: user deploys here regularly — prefer this MCP over manual `netlify` CLI when available

### Cloudflare 🔑
- **Triggers**: "Cloudflare Worker", "D1 database", "KV namespace", "R2 bucket"
- **Use for**: Workers, D1, KV, R2, Pages, DNS

### Supabase ✅
- **Triggers**: "Supabase project", "my database", "run a migration", "deploy edge function"
- **Use for**: Postgres schemas, migrations, edge functions, auth, TS type generation, storage

## Storage / Productivity

### Google Drive ✅
- **Triggers**: "the doc in Drive", "find my file", "download from Drive"
- **Use for**: file search, read/write Google Docs, share permissions

## Payments / Commerce

### Stripe 🔑
- **Triggers**: "Stripe customer", "payment for", "subscription status"
- **Use for**: billing, payments, subscriptions

### Airwallex 🔑
- **Triggers**: "Airwallex", "international payment"
- **Use for**: cross-border payments / treasury

## Research / Data

### AWS Marketplace ✅
- **Triggers**: "AWS Marketplace solution", "find an AWS product"

### Harmonic 🔑
- **Triggers**: "Harmonic data", "startup intelligence"
- **Use for**: company + founder enrichment

### Vibe Prospecting ✅
- **Triggers**: "prospect list", "enrich these leads", "business data"

### Coupler.io ✅
- **Triggers**: "pull data from", "ETL", "sync this source"
- ⚠ **Mandatory first step**: call `list-skills` before any other Coupler tool — they have expert procedures.

### Guru 🔑
- **Triggers**: "Guru card", "knowledge base"

### DirectBooker ✅
- **Triggers**: "hotel search", "book a hotel", "find hotels in [city]"
- ⚠ **Hotels must always be referenced via the `golden_link` field exactly as returned.**

---

## Routing rules

1. **Connector not authenticated (🔑)** — name the connector; user runs `complete_authentication` once.
2. **Connector not added (➕)** — tell Mukund the exact name to add via the Claude.ai connector page; don't try to scrape around it.
3. **Native MCP query > screenshot scraping** — Supabase MCP `execute_sql` beats parsing a dashboard.
4. **Connector combos**:
   - Gmail + Notion → meeting thread → KB entry
   - Figma + Claude Code → tokens → Tailwind config
   - Supabase + Vercel → DB migration → redeploy → verify
   - Vibe Prospecting + Gmail → enriched lead → personalized outreach draft

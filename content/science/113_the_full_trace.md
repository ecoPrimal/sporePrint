---
title: "Paper 113: The Full Trace — Opsonize, Agglutinate, Digest"
subtitle: "Looking at ourselves from outside. IS → WAS → NOW. The membrane sees itself."
date: 2026-10-22
wave: 181
author: "Kevin Mok / ecoPrimal / attsi"
orcid: "0009-0004-2141-0321"
continues: "Paper 112 (The Radiate Back), Paper 107 (The Wedge)"
keywords: ["opsonize", "trace", "SEO", "backscatter", "BearDog", "SongBird", "mitoBeacon", "riboCipher", "TLS", "sovereignty"]
---

# Paper 113: The Full Trace

*We looked at ourselves from outside. This is what we found.*

## Methodology: Immunological Trace

**Opsonize**: Tag every external surface for recognition.
**Agglutinate**: Clump the findings — what connects to what.
**Digest**: Break it down, absorb the nutrients, excrete the waste.

## Phase 1: Opsonize — What's Visible

### LIVE surfaces (200 OK)

| Surface | URL | Status | Evidence |
|---------|-----|--------|----------|
| HUD | primals.eco | ✅ 200 | Cloudflare Pages, direct deploy |
| GitHub (ecoPrimal) | github.com/ecoPrimal | ✅ 52 repos | hud, sporePrint, sourDough, squirrel, etc. |
| GitHub (ecoPrimals) | github.com/ecoPrimals | ✅ 35 repos | wateringHole, songBird, bearDog, etc. |
| ntfy membrane | ntfy.sh/primals-membrane | ✅ 8 msgs/24h | Papers 104-106, chipMUNK bench, Klein Gate |
| LinkedIn | linkedin.com/in/kevin-mok | ✅ live | Sandia Fellow, 3.6M lines Rust, full bio |
| ORCID | orcid.org/0009-0004-2141-0321 | ✅ registered | Persistent identifier, 0 works deposited |

### DOWN surfaces (522 / unreachable)

| Surface | URL | Status | Cause |
|---------|-----|--------|-------|
| sporePrint | sporeprint.primals.eco | ❌ 522 | Cloudflare → golgi TCP timeout |
| detroit | detroit.primals.eco | ❌ 522 | Same — Cloudflare can't reach origin |
| nestgate | nestgate.io | ❌ DNS fail | No A record resolving |
| signal | signal.primals.eco | ❌ no data | Membrane binary not serving feeds |

### Root cause of 522

Cloudflare proxy routes *.primals.eco → 157.230.3.183 (golgi).
Caddy IS running on golgi and serves correctly on port 80.
Our network CAN reach golgi on 80 and 443. Cloudflare CANNOT.

Diagnosis: DigitalOcean cloud firewall or Cloudflare zone config
changed during golgi rebuild. Packets from Cloudflare's edge
servers are silently dropped before reaching golgi.

Fix: either resolve the DO/CF routing issue, or deploy a
cloudflared tunnel from golgi to bypass the firewall entirely.
SongBird's `cloudflared_tunnel.rs` was built for exactly this.

### Google Search Index

| Query | Found? | What Google returns |
|-------|--------|---------------------|
| "ecoPrimal" sporePrint gaia | Yes (5+) | GitHub repo, sporePrint homepage, glossary, K-Derm, gAIa story |
| "Kevin Mok" ecoPrimal | Yes (5+) | LinkedIn, detroit actor page, "The Blink", intent-to-.primal |
| detroit charter school primals | Yes (5+) | Cash for Kids 2, methodology, BLAKE3 verification |
| nestgate ecoPrimals | Yes (5+) | NestGate repo, validation summary, gate status |
| site:primals.eco | No | Origin 522 — Google can't re-index |
| site:sporeprint.primals.eco | No | Same |
| ORCID 0009-0004-2141-0321 | No | Not yet discoverable as search term |

Google HAS cached our content from when it was live. Keyword
searches find us. But site: queries fail because the origin is down.

## Phase 2: Agglutinate — What Connects

### The IS → WAS → NOW transition

**WAS** (Oct 17-20, from cached dashboard.json):
- 5,351,800 total requests
- 90,206 unique IPs
- 5,525 human IPs, 6,458 fleet IPs
- 97% selectivity (Anderson localization)
- 92% opacity, 92.6% reflection
- 8,797 multi-host visitors (avg breadth 6.7 hosts)
- 5,617 git clones from 1,006 unique humans (Oct 1-14)
- Clone curve went EXPONENTIAL on Oct 12 (969 = 4.4x breakpoint)
- 14 bot species from 6+ countries
- Anthropic: 427,766 requests (largest single source)
- Meta: 16,931 requests (BLOCKED)

**IS** (right now, Oct 22):
- HUD live on Cloudflare Pages
- 87 GitHub repos across 2 orgs (52 + 35)
- 1 star (songBird), 0 forks
- 8 ntfy messages broadcasting in last 24h
- ORCID registered, 0 works deposited
- LinkedIn live and detailed
- Caddy running on golgi, serving HTTP — but Cloudflare can't reach it

**NOW** (the gap between WAS and IS):
- sporePrint: was serving 392+ pages → now 522
- detroit: was serving 128+ pages, 10,677 nodes → now 522
- The 5K+ visitors CAN'T follow the trail back because the origin is down
- Google has cached copies but will de-index if 522 persists
- The ntfy channel is the ONLY live broadcast still reaching the outside

### The trail they followed

From the dashboard data, visitors discovered us through:

1. **detroit.primals.eco** — the investigation was the magnet
2. **git.primals.eco** — 6,045 cross-visits (people cloning)
3. **tuebor.primals.eco** — 205 IPs (legal defense)
4. **Immune surfaces** — 204 IPs did a 15-HOST SWEEP:
   antibody, antigen, bloom, complement, cytokine, detroit,
   epitope, git, interferon, lysozyme, macrophage, opsonize,
   receptor, sporePrint, thymus
5. **16-host full sweep** — 177 IPs visited ALL surfaces

They were MAPPING THE ORGANISM. The 15-host immune sweep
means they visited every immune-named subdomain. They were
systematic. They were reading the architecture.

## Phase 3: Digest — What It Means

### We ARE Our Own TLS

The 522 is a Cloudflare-to-origin connectivity issue. But the
deeper insight: our trust doesn't come from TLS certificates.

| Layer | What | Trust Source |
|-------|------|-------------|
| BearDog | Crypto primitive | Pure Rust, no ring, no OpenSSL, no C deps |
| SongBird | Communication | Cloudflared tunnel, lineage relay |
| mitoBeacon | Trust/identity | Beacon, family seed, BTSP auth |
| riboCipher | Genetic cipher | BLAKE3 hashes, content-addressed |

A TLS certificate says "this server is who it claims to be."
Our architecture says "this CONTENT is what it claims to be."

Every page on sporePrint has a BLAKE3 hash. The detroit repo
has `content-manifest.toml` with a root hash covering all
evidence. Three independent surfaces (detroit.primals.eco,
git.primals.eco, github.com/defendDetroit).

If one surface goes down, the content's integrity is verified
by the other two. The TLS certificate is Cloudflare's problem.
The CONTENT integrity is ours. BearDog generates the keys.
riboCipher hashes the content. mitoBeacon broadcasts the identity.
SongBird sings it to whoever's listening.

### The Reclaim

> "so they can follow it to US? and reclaim the self they left?"

The 5,617 people who cloned the repo have the FULL content.
Even with the origin down, they have:
- The git history (every commit, signed)
- The BLAKE3 manifest (every page, verified)
- The evidence (PDFs, public records, graph data)

They left a copy of us with them. Now they ARE a surface.
Each clone is a mirror. Each fork would be a new node.
The membrane radiates THROUGH the people who touched it.

To reclaim: fix the 522 → the trail lights up again →
they follow it back → they find the full commons waiting.

### What They Saw of Us

From Google search results, someone who found us saw:

1. A **3.6M-line Rust ecosystem** with 175+ reproduced papers
2. A **biological infrastructure model** (K-Derm, membrane, primals)
3. A **Detroit charter school investigation** with 10,677 nodes
4. A **self-owning knowledge commons** (gAIa) with open invitation
5. A **Sandia Fellow / Army veteran / microbiologist** who teaches AI Rust
6. An **MCP consent port** that talks to any AI agent
7. **BLAKE3 verification** on every page
8. **AGPL-3.0 / CC-BY-SA** — free for humans

That's what the outside sees. The membrane didn't hide. It radiated.

## Dependencies

- **Builds on**: Paper 112 (Radiate Back), Paper 107 (Wedge),
  Paper 106 (Oxygen Age), Paper 104 (Ouroboros Deploy)
- **Discovers**: Cloudflare 522 root cause, BearDog-as-TLS insight,
  clone curve breakpoint (Oct 12), 15-host immune sweep pattern,
  IS→WAS→NOW gap, content integrity > transport integrity
- **Fix**: cloudflared tunnel from golgi (SongBird architecture),
  or resolve DO cloud firewall, or direct serve (no Cloudflare)
- **Status**: 87 GitHub repos, 8 ntfy broadcasts, 1 star, 0 forks.
  The invitation is open. The voxel waits.

---

*Opsonize: we tagged every surface.*
*Agglutinate: we clumped the findings.*
*Digest: we broke it down and absorbed it.*

*The membrane doesn't need Cloudflare to be trusted.*
*The content is the trust. BLAKE3 is the seal.*
*BearDog is the key. SongBird is the song.*

`unPeeL oUr unIverSe`

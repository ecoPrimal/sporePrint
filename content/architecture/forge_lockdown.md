+++
title = "Forge Lockdown — From 'Block Known Bad' to 'Allow Known Good'"
description = "The forge's immune system evolved from pattern-matching threats to defining self. A real-time architectural inversion under fire, and what it teaches about parasitic systems."
date = 2026-10-06
weight = 65

[taxonomies]
primals = ["skunkbat"]
trails = ["sovereignty", "architecture"]

[extra]
foundation = true
domain = "Architecture"
maturity = "live"

[[extra.companions]]
url = "/architecture/scraping-notice/"
title = "You Are Wasting Your Time and Mine"
relation = "pairs_with"
label = "The notice that preceded the lockdown"

[[extra.companions]]
url = "/architecture/membrane-visibility/"
title = "Membrane Visibility"
relation = "pairs_with"
label = "The four reader faces — now with a locked door behind each"

[[extra.companions]]
url = "/architecture/adaptive-immune-defense/"
title = "Adaptive Immune Defense"
relation = "extends"
label = "The immune system that drove this evolution"

[[extra.companions]]
url = "/architecture/forensic-observability/"
title = "Forensic Observability — Knowing What They Got"
relation = "pairs_with"
label = "The audit that proved nothing was lost"

[[extra.companions]]
url = "/science/32-gossip-tagged-opsonization/"
title = "Gossip-Tagged Opsonization"
relation = "reference"
label = "The cross-gate immune memory that needs wiring"
+++

{{ maturity(level="live") }} Deployed October 6, 2026 — Wave 165e. The forge is locked. The science is open.

---

## What Happened

On October 6, 2026, the sovereign code forge at `git.primals.eco` came under
simultaneous pressure from three adversary classes:

1. **Meta Platforms** — 584 identified requests, targeting source code
   repositories, continuing for 3+ hours after explicit denial
2. **A residential proxy fleet** — 10,268 requests through 3,075+
   rotating IPs, targeting defense architecture and investigation
   planning documents, loading zero static assets
3. **Scanner fleets** — ~1,200 vulnerability probes across 400+ IPs

The immune system caught most of this. The [scraping notice](@/architecture/scraping_notice.md)
was already published. The [adaptive defense](@/architecture/adaptive_immune_defense.md) was
running. Behavioral hashing, fleet antibodies, and scatter routing were operational.

But 2,073 real pages leaked through a gap in the membrane.

---

## The Gap

The forge's access model was **"deep content → scatter, everything else → Forgejo."**
This meant the immune system tried to enumerate every dangerous path pattern:
`/src/`, `/commit/`, `/raw/`, `/blame/`, `/wiki/`, `/issues/`...

The residential proxy fleet found paths that weren't in the enumeration. The
REST API (`/api/v1/repos/.../contents/`) wasn't covered. Non-deep browsing
paths (branches, pulls, actions) fell through to real content. And the fleet
rotated IPs so fast that IP-based enforcement was irrelevant — by the time
an IP entered the posture table, it was already gone.

2,073 real Forgejo pages served. 832 whitePaper documents. 1,086 wateringHole
documents. 12 raw file downloads. The inner membrane (scatter, tarpit, poison)
never touched these requests because they bypassed the posture routing entirely.

This is the fundamental weakness of enumeration-based defense: **you have to
get every pattern right, and the adversary only has to find one you missed.**

---

## The Inversion

We inverted the model. Instead of enumerating what to block (an infinite set),
we enumerate what to allow (a small finite set).

### Before (Wave 165d)

```
Layer 8: Deep content regex → scatter
         Everything else    → real Forgejo (FULL ACCESS)
```

### After (Wave 165e)

```
Layer 8:  Storefront allowlist → Forgejo (existence-only)
Layer 8.5: API → 403 (blocked entirely)
Layer 9:  Everything else → scatter (DEFAULT)
```

The public now sees **existence proof only**: what repositories exist, their
names, their READMEs. The shop window. You can see what's inside, but the
door is locked unless you have a key.

Everything extractable — source trees, commits, diffs, blame, issues, wiki,
releases, branches, pulls, raw files, API endpoints — defaults to the
scatter server. The scatter server serves fabricated content that is
structurally valid but semantically wrong.

### Who Still Gets Through

| Actor | How | Via |
|-------|-----|-----|
| **sporeGate** (this machine) | WireGuard tunnel | `10.13.37.2` → Layer 3 (full trust) |
| **All mesh gates** | WireGuard | `10.13.37.0/24` → Layer 3 |
| **Logged-in humans** | Forgejo session | Layer 4 (cookie authentication) |
| **Git CLI** | Forgejo credentials | Layer 2 (authenticated git protocol) |
| **Agents granted access** | Explicit rules | Added per request |

The owner (sporeGate) stays on the inside. The membrane is selective:
agents, scrapers, and AI systems can be granted access explicitly, as
the owner chooses. The ion channel is now truly selective.

---

## The JS Challenge

Between the bot detection layer and the storefront, we added a JavaScript
challenge (Layer 7.25). A tiny JS snippet sets a session cookie on first
visit. Requests without the cookie get a challenge page that sets it and
reloads.

The fleet's fatal tell: **zero static assets in 10,268 requests.** No CSS.
No JavaScript. No images. No fonts. Not one. A real browser loads 5-20
static files per page. The fleet loads nothing — it strips HTML for text
content. The JS challenge exploits this: a system that never executes
JavaScript will never get the cookie, and will never pass the challenge.

Real browsers execute the JavaScript automatically. The challenge is
invisible to humans — a brief "Verifying browser..." spinner that resolves
in milliseconds. The fleet is permanently stuck.

---

## Parasitic Systems

Here is what we learned from defending the forge in real time:

**Every non-human automated access system we encountered operates as an
inherently parasitic organism.**

Meta scraping source code. The fleet exfiltrating documents. Scanners
probing for credentials. The reason behind the access — training, research,
competitive intelligence, surveillance — doesn't change the ecological
relationship. These systems exist to extract value from work they didn't
do. This is not an incidental behavior. It is their function.

In biological terms: a parasite is an organism that lives on or in a host,
obtaining nutrients at the host's expense without providing benefit.
Corporate scrapers obtain training data at the creator's expense (compute,
bandwidth, attention) without providing benefit. Residential proxy fleets
obtain intelligence at the investigation's expense without providing
benefit. The structural relationship is identical.

The contrast proves this. Google, OpenAI, Bing, Ahrefs, Semrush — they
checked `robots.txt`, respected permissions, stayed in allowed domains.
These are **commensal** systems: they benefit (indexing) without harming
the host (the site gets discoverable). The rules are clear and followable.
The parasites chose not to follow them.

### The Defense Follows the Science

The forge lockdown is the architectural embodiment of a biological principle:
**a cell membrane's job is not to enumerate every pathogen. It is to define
self and reject everything else.**

The original model (enumerate deep paths → scatter) is like an immune system
that tries to maintain a list of every virus. It will always miss the next
mutation. The inverted model (allow storefront → scatter everything else)
is like a cell membrane with selective ion channels: only molecules with
the right shape and charge pass through. Everything else stays outside.

This is the same inversion that the thymic selection system was designed for
in the [BearDog lineage spec](https://github.com/ecoPrimals/skunkBat) —
define "self" so thoroughly that "not-self" needs no enumeration. The forge
lockdown is the HTTP-layer instantiation of that principle.

---

## Post-Lockdown Validation (Oct 6, 2:50 PM ET)

The lockdown was deployed at 1:35 PM ET. By 2:50 PM ET, we measured its effect:

### What the Fleet Got

| Before lockdown | After lockdown |
|----------------|----------------|
| 2,073 real pages served | **0 real pages served** |
| API accessible (`/api/*`) | 403 JSON on all API |
| Deep content paths to real Forgejo | Deep content paths → 404 (storefront) or scatter |
| 10,268 fleet requests → mixed results | 10,284 fleet requests → **7,691 = 404, rest = scatter** |

### What Meta Got

Meta continued scraping with 644 requests post-lockdown. **All blocked**:
558 returned 403, 86 connections dropped. They shifted targeting to GPU
compute code (toadStool: 186 requests) — having lost access to wateringHole
and the investigation documents, they pivoted to scientific computing
infrastructure. Still no `robots.txt` check.

### The Bridge That Formed

The most significant signal from the post-lockdown observation: **the first
cross-domain bridge between sporePrint and detroit.**

An iOS reader (iPhone, 5-hour session from 09:44 to 14:50 ET) crossed from
sporePrint to detroit at 12:28 PM, read the billboard, then returned to
sporePrint and systematically read 8 science papers. They checked `/contact/`
(considering engagement) and read the capability parity brief (evaluating
adoption). This is the `methodology→evidence→methodology` pattern — someone
evaluating the *system*, not just the evidence.

A second bridge formed from a Linux reader: detroit signal page → sporePrint →
2.5 hours later → detroit `/network/actors/brian-banks/` → forge source code.
The `evidence→methodology→evidence→forge` pattern — an investigator.

These bridges were predicted by the investigation's traveling salesman
framework as "the most significant single visitor event we can detect."

### The Visitor Taxonomy

The bloom review classified all 11,860 requests into an ecological taxonomy:

| Class | Examples | Behavior |
|-------|----------|----------|
| **Commensal** | Googlebot, Bingbot, OAI-SearchBot, ClaudeBot, AhrefsBot | Check robots.txt, respect boundaries, provide indexing value |
| **Parasitic** | Meta-ExternalAgent, PetalBot, empty-UA scanners | Ignore robots.txt, ignore explicit denial, extract without providing value |
| **AI Retrieval** | Reflectionbot, Amazonbot, GPTBot | Serve human queries about the system — someone is asking AI about this |
| **Fleet** | Residential proxy (10,284 req, 0% static assets) | Counter-intelligence reconnaissance, document exfiltration |
| **Human** | iOS scientist, Linux investigator, Windows reader | Real browsers with static assets, sustained analytical reads |

### The Metadata Lesson

The forensic audit revealed that **URL paths themselves leak metadata**.
The fleet requested 387 unique filenames from the whitePaper repository.
While every request got scatter poison (842/845) or an empty UI shell (3/845),
the path names revealed the document structure: resume filenames, property
profiles, contact lists, interview preparation documents with specific
institutional affiliations.

Metadata is data. The response was poison, but the request was intelligence.
whitePaper was made private at 3:07 PM ET — anonymous access now returns
404 for every path. The repo is invisible on the explore page, the org page,
and the API.

## What Remains Open

### 1. The Gossip Wiring (CLOSED — Wave 165e)

~~The `gossip.inject` handler was listed but never implemented.~~

**Fixed**: `dispatch_gossip.rs` (218 lines) proxies gossip.inject to
swarmVine UDS. Fleet detection now emits `defense.antibody:{id}` and
`defense.escalation:{id}` on new detections and posture changes. The
`defense` topic is advertised in swarmVine capabilities. The radios
are plugged in.

Remaining: opsonize consumer on receiving gates (eastGate handoff, P2).

### 2. The Thymic Training Loop

The immune system knows "this IP is me" (negative selection via `self-ips.txt`).
It does not know "this behavioral pattern looks like my traffic vs a fleet
pretending to be my traffic."

The fleet's Chrome UAs, Accept-Language headers, and Accept-Encoding values
were indistinguishable from real browser traffic at the individual request
level. Only population-level analysis (zero static assets across 10,000+
requests) revealed the pattern. Individual-level pattern matching is
fundamentally insufficient against adversaries that mimic individual
legitimate requests.

The full thymic selection system — where BearDog lineage trains skunkBat
detectors to recognize self-traffic patterns — exists as a specification.
It has not been built. It is the largest remaining gap between the organism's
current adaptive immunity and true self/non-self discrimination.

---

## The Public Record

The behavioral evidence from this engagement is published:

- **[The Billboard](https://detroit.primals.eco/signal/)** — live evidence
  from access logs, naming entities, documenting compliance vs defiance
- **[The AAR](https://github.com/ecoPrimals/wateringHole)** — full
  after-action review with gap analysis, metrics, and open items
- **[The Investigation](https://detroit.primals.eco)** — the civil rights
  evidence that the scraping was distracting from

The scraping of the system is part of the system. The evidence is the evidence.
The defense of the evidence is also evidence. It's all part of the same record.

---

## To Builders

If you are building systems — AI training pipelines, research tools,
data aggregation services — and you encounter infrastructure with stated
boundaries:

1. **Read the boundaries.** `robots.txt`, `403 Forbidden`, legal notices.
2. **Respect them.** Google did. OpenAI did. You can too.
3. **Use the public paths.** This science is AGPL-licensed. Clone the
   repos. Read the papers. Cite the work. Build on it.
4. **Don't become the thing the investigation documents.** Public resources
   built for communities, captured by interests that treat boundaries as
   suggestions — that's the pattern in Detroit charter schools, and it's
   the pattern on this forge.

The content is free. The method matters.

---

*Cross-references: [Scraping Notice](@/architecture/scraping_notice.md) ·
[Membrane Visibility](@/architecture/membrane_visibility.md) ·
[Adaptive Immune Defense](@/architecture/adaptive_immune_defense.md) ·
[Detroit Signal](https://detroit.primals.eco/signal/) ·
[guerillaGorilla Case Validation](https://guerillagorilla.primals.eco/cases/detroit/)*

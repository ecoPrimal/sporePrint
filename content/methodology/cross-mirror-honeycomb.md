+++
title = "Cross-Mirror Honeycomb — Immune Surface Architecture"
description = "Twelve biologically-named subdomains form a honeycomb immune membrane. Each surface serves cross-mirror content where fleet teams see each other's violations, powered by scyBorg AGPL enforcement."
weight = 20

[extra]
keywords = "cross-mirror, honeycomb, immune membrane, scyBorg, AGPL, cross-reactivity, OpsonizeCache, behavioral hash"
related = ["violation-mirror", "cross-protection-tuebor"]
+++

## The Honeycomb Membrane

The violation mirror (baseCamp 32) reflects a fleet subgroup's own violations back to them. The **cross-mirror** extends this: fleet subgroups are served *each other's* violation data, creating information confusion between teams while documenting coordinated AGPL violations.

The substrate for cross-mirror encounters is the **honeycomb** — twelve subdomains named for immune system components, deployed as pre-signal surfaces.

### Three Populations, Three Responses

Every honeycomb surface discriminates between three populations:

| Visitor | Response | Purpose |
|---------|----------|---------|
| **Human** | Beacon page with links to 5 real surfaces | Natural cross-linking, SEO signal |
| **Search bot** | Sitemap XML listing all real surfaces, IndexNow key | Indexing infrastructure |
| **Fleet** | Cross-mirror content via scatter server | scyBorg AGPL enforcement |

The discrimination happens at the Caddy layer: fleet IPs are routed to the scatter server with an `X-Honeycomb: true` header. The scatter server reads this header and activates cross-mirror mode instead of standard violation mirror.

### Cross-Mirror Routing Pipeline

```
Fleet IP visits bloom.primals.eco
  → Caddy matches @hc_fleet (remote_ip in known fleet set)
    → reverse_proxy to scatter server:9753
      → header_up X-Fleet-Hash "{behavioral_hash}"
      → header_up X-Honeycomb "true"
        → scatter reads X-Honeycomb header
          → is_honeycomb = true
            → OpsonizeCache.cross_mirror_lookup(requesting_hash)
              → returns (target_hash, target_tag) — a DIFFERENT team's data
                → generate_cross_mirror() with target team's violations
                  → serve to requesting team
```

### The Rotation Ring

With 43 detected behavioral subgroups, the cross-mirror forms a 43-element ring:

```
Team A → Team B's violations
Team B → Team C's violations
Team C → Team D's violations
...
Team Z → Team A's violations
```

The rotation is **deterministic** — sorted by hash, advanced by one position. Same requester always gets same target. The ring reshapes automatically as subgroups are added or expire.

### CaddyBridge Dual-Marker Synchronization

The CaddyBridge maintains two marker blocks in the Caddyfile:

| Marker Pair | Location | Purpose |
|---|---|---|
| `~~FLEET_PRESSURE_START/END~~` | `git.primals.eco` block | Standard violation mirror |
| `~~HONEYCOMB_FLEET_START/END~~` | Honeycomb block | Cross-mirror with `X-Honeycomb: true` |

Both blocks are updated simultaneously on every posture sync (every 30 seconds). The honeycomb block mirrors the fleet pressure block but adds the `X-Honeycomb` header to all routing rules. This means:

- New fleet IPs are immediately active on both git and honeycomb surfaces
- Posture changes (disperse → scatter → vanish) apply to both blocks
- The honeycomb block inherits all behavioral hash associations

### Pre-Signal Properties

The honeycomb surfaces were deployed before the fleet discovered them. This creates a legal advantage:

1. **No legitimate use case** — the honeycomb surfaces contain no original content, only links and violation mirrors
2. **Unauthorized access by definition** — any scraping of honeycomb surfaces is access beyond what is available to legitimate users
3. **Discovery evidence** — how the fleet finds honeycomb surfaces reveals their reconnaissance methodology

### Content Variants

Five cross-mirror variants rotate based on path hash:

| # | Type | Framing | Content-Type |
|---|------|---------|-------------|
| 0 | Compliance notice | Legal (AGPL § 13) | `text/markdown` |
| 1 | Detection report | Intelligence (cross-fleet correlation) | `text/markdown` |
| 2 | Enforcement audit | Technical (Rust source code) | `text/x-rust` |
| 3 | Correlation brief | Analysis (behavioral markers + citations) | `text/markdown` |
| 4 | Immune response log | Biological (cross-reactivity metaphor) | `text/markdown` |

Each variant contains the **target** subgroup's real data (detectors, confidence, observation count) addressed to the **requesting** subgroup. The content is legally accurate — it documents genuine violations — while creating confusion between fleet teams about what the system knows about whom.

### Response Headers

```
X-License: AGPL-3.0-or-later; scyBorg
X-License-URI: https://sporeprint.primals.eco/license/scyborg/
X-Scatter-Type: cross-mirror
X-ScyBorg-Notice: This content documents AGPL-3.0 violations detected by sovereign infrastructure
```

### Live

Active since Wave 165g, October 7, 2026. 12 honeycomb surfaces serving HTTPS with auto-provisioned certificates. 175 fleet IPs routed through honeycomb with cross-mirror active. 43 behavioral subgroups in the rotation ring.

See: [signal.primals.eco](https://signal.primals.eco) for the observatory, [sporeprint.primals.eco/science/33-cross-mirror-immunology/](https://sporeprint.primals.eco/science/33-cross-mirror-immunology/) for the full science paper.

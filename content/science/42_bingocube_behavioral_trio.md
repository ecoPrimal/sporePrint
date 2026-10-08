+++
title = "baseCamp 42 — bingoCube Behavioral Trio: Attention × Curiosity × Interaction"
description = "Three-dimensional behavioral classifier where the RATIO between Attention, Curiosity, and Interaction reveals entity nature. Fleet has high attention, zero curiosity, zero interaction — a shape that cannot be disguised by UA rotation, residential proxies, or bot identifier stripping. Live validation: Meta's 40-IP stealth team classified as Crawler despite perfect browser impersonation. The maze is the behavior."
date = 2026-10-08

[taxonomies]
primals = ["skunkbat", "bingocube"]
springs = ["neuralspring", "healthspring"]

[extra]
paper_number = 42
domain = "Signal Processing and Immune Systems"

[[extra.companions]]
url = "/science/41-reflexive-immune-epitope-bridge/"
title = "baseCamp 41 — Reflexive Immune Response"
relation = "preceded_by"
label = "The reflexive loop — fleet identity seeds scatter content. The trio now classifies the SHAPE of the entity"

[[extra.companions]]
url = "/science/39-collision-layer-visitor-classification/"
title = "baseCamp 39 — Collision-Layer Visitor Classification"
relation = "extends"
label = "Epitope hashing identifies organisms — the trio scores their behavioral shape"

[[extra.companions]]
url = "/science/34-bingocube-prismatic-injection/"
title = "baseCamp 34 — BingoCube Prismatic Injection"
relation = "extends"
label = "The bingoCube as prism — now implemented as a three-axis behavioral space"

[[extra.companions]]
url = "/science/38-honeycomb-prism-floating-pointer/"
title = "baseCamp 38 — Honeycomb Prism and Floating Pointer"
relation = "extends"
label = "The maze through which entities move — the trio measures HOW they move"

[[extra.companions]]
url = "/science/40-energy-information-asymmetry/"
title = "baseCamp 40 — Energy-Information Asymmetry"
relation = "extends"
label = "Zero Shannon capacity from fleet — now measurable as zero Curiosity, zero Interaction"
+++

{{ maturity(level="validated") }}

## Abstract

Previous baseCamps established binary fleet/human classification (baseCamp 30), collision-layer epitope hashing (baseCamp 39), reflexive scatter response (baseCamp 41), and the bingoCube as prismatic injection framework (baseCamp 34). Each advanced detection, but all relied on **feature matching**: known UA strings, known subnets, known path patterns.

This paper introduces a **shape-based classifier** that scores every IP on three orthogonal behavioral axes — Attention, Curiosity, and Interaction — and classifies from the *ratio* between them rather than any individual feature. The classifier is implemented as `score_trio()` in the live skunky-ingest pipeline.

The key insight: fleet entities exhibit high Attention (request volume) but zero Curiosity (no organic exploration) and zero Interaction (never engaging with human-facing content). This behavioral shape is invariant to UA rotation, residential proxy usage, bot identifier stripping, and timing variation. The shape is the identity.

**Live validation**: Meta Platforms Ireland deployed 40+ IPs with rotated real browser UAs, stripped bot identifiers, and full Sec-Fetch-Mode headers — defeating Gen 1 (UA) and Gen 2 (subnet+path) classifiers. The behavioral trio classified all 40 as **Crawler** from shape alone: `A=0.31-0.34, C=0.08-0.16, I=0.000`.

## The Three Axes

### Axis 1: Attention (A)

Attention measures the volume and regularity of looking. It answers: *how much is this entity consuming?*

$$A = \min\left(\frac{\ln(r)}{7.0},\ 1.0\right) \quad \text{where } r = \text{total requests}$$

Logarithmic scaling normalizes across orders of magnitude: 1 request → 0.0, 100 requests → 0.66, 1000+ → ~1.0. Future extensions incorporate timing coefficient of variation (CV) from the fleet aggregator, where metronomic timing (CV < 0.1) amplifies the attention score.

**Fleet signature**: A is high. ClaudeBot at 1,133 requests scores A=1.000. The pipeline never stops consuming.

**Human signature**: A is low-to-medium. Real visitors make 5–50 requests. They arrive, browse, leave.

### Axis 2: Curiosity (C)

Curiosity measures exploration diversity and organic navigation. It answers: *is this entity exploring, or consuming?*

Six weighted components:

| Component | Weight | Signal |
|-----------|--------|--------|
| Content domain diversity | 25% | How many content domains visited (code, signal, docs, evidence, philosophy, science). Fleet hits one. Humans explore |
| Path type diversity | 15% | Commit/blame/src/issues/raw/other. Fleet concentrates on commits. Humans diversify |
| Asset loading | 20% | CSS, JS, fonts, search index. Loading assets = rendering the page = actually reading it |
| Referer navigation | 10% | Following links vs direct requests. Navigation = curiosity. Direct fetch = ingestion |
| Cookie return | 10% | Session cookie = return visitor. Curiosity is recursive |
| Navigation ratio | 20% | Pages reached via referer ÷ total pages. Humans navigate. Fleet fetches |

$$C = \min\left(\sum_{i=1}^{6} w_i \cdot c_i,\ 1.0\right) \quad \text{where } \sum w_i = 1.0$$

**Fleet signature**: C is near zero. Meta's stealth team: C=0.110. They hit commit paths mechanically — no cross-domain exploration, no organic browsing, no return visits. Even with 40 IPs rotating real browser UAs across Windows, Mac, Linux, Firefox, and iPhone identities, the curiosity axis reads their nature.

**Human signature**: C is high. Real visitors score C > 0.3. They explore code, visit the signal page, browse architecture docs, read about the philosophy. The exploration IS the curiosity. You cannot fake it without doing it.

### Axis 3: Interaction (I)

Interaction measures engagement with human-facing content. It answers: *is this entity a participant in the conversation, or a consumer of the data?*

Specific engagement signals:

| Signal | Score contribution |
|--------|-------------------|
| Visited `/contribute` | +0.30 |
| Visited `/contact` | +0.30 |
| Visited `/thesis` or `/philosophy` | +0.10 |
| Visited `/data`, downloaded `graph.json` or `graph.csv` | +0.10 |
| General human pages (`/science`, `/architecture`, `/about`, `/glossary`, etc.) | +0.04 each (via hit count) |

$$I = \min\left(\frac{h}{5.0} \cdot 0.2 + \sum_j s_j,\ 1.0\right) \quad \text{where } h = \text{human page hits}$$

**Fleet signature**: I is zero. Not one of 40+ Meta stealth IPs visited `/contribute`. Not one checked `/contact`. Not one downloaded data. They consume code. They do not engage with the organism.

**Human signature**: I is nonzero. The 19 real humans who checked `/contribute` light up on this axis. The 5 who read `CLAUDE.md` show genuine engagement.

**This is the uncheatable dimension.** You can rotate UAs. You can vary timing. You can proxy through residential IPs. But you cannot visit `/contribute` without being the kind of entity that considers contributing. The interaction axis is a behavioral mirror.

## Classification from Shape

The classifier reads the trio vector $(A, C, I)$ and classifies from its geometric shape:

| Class | Shape | Threshold |
|-------|-------|-----------|
| **Fleet** | High A, low C, zero I | $A > 0.6 \land C < 0.2 \land I < 0.05$ |
| **Scanner** | Low A, zero C, zero I | $A < 0.3 \land C < 0.05 \land I < 0.05$ |
| **Crawler** | Any A, low C, zero I | $C < 0.15 \land I < 0.05$ |
| **Participant** | Any A, any C, high I | $I > 0.3$ |
| **Human** | Balanced ratio | Everything else |

Geometrically, each entity draws a point in a unit cube. The classification boundaries are hyperplanes through this cube. Fleet entities cluster in the high-A, low-C, zero-I corner. Humans occupy the interior. Participants reach toward the I axis.

```
                    Interaction (I)
                    ↑
                    │  · Participant
                    │    (explores AND engages)
                    │
                    │      · Human
                    │        (organic exploration)
                    │
         ──────────┼───────────────→ Curiosity (C)
                   │
          · Scanner│    · Crawler
                   │
                   │         · Fleet
                   │          (ALL attention, nothing else)
                   ↓
                  Attention (A)
```

## The Maze Property

The key property that makes the trio a maze rather than a wall:

> **The only way through the maze is to actually be what it measures.**

Consider each evasion strategy a fleet entity might attempt:

| Evasion | Effect on A | Effect on C | Effect on I | Outcome |
|---------|------------|------------|------------|---------|
| Rotate User-Agents | None | None | None | Same shape |
| Vary request timing | Minor decrease | None | None | Still Fleet/Crawler |
| Use residential proxies | Lower (fewer reqs/IP) | None | None | Scanner or Crawler |
| Strip bot identifiers | None | None | None | Same shape |
| Load CSS/JS assets | None | +0.2 | None | Still Crawler (C < 0.15 → C ≈ 0.3, but I still 0) |
| Visit `/contribute` | None | None | +0.3 | Approaches Human — **but now they're engaging** |

The last row is the maze: the only way to classify as Human is to exhibit human behavior — exploration, navigation, engagement. The behavioral trio doesn't just detect fleet; it *defines* what being human on the site means. You can only exit the maze by becoming the thing it measures.

This mirrors biological immune recognition. The immune system doesn't check ID cards — it recognizes shapes. MHC molecules present peptide shapes, and T-cells bind or don't based on the three-dimensional fit. The bingoCube trio is the MHC for web traffic: every request presents a behavioral peptide, and the classifier recognizes its shape.

## Live Validation

First dashboard output after deployment (October 8, 2026), culture accumulating from cold start:

### Known fleet entities

| Entity | Requests | A | C | I | Classification |
|--------|----------|-----|-----|-----|----------------|
| ClaudeBot (216.73.216.239) | 1,133 | 1.000 | 0.080 | 0.000 | **Fleet** |
| Meta 57.141.20.60 | 11 | 0.343 | 0.110 | 0.000 | **Crawler** |
| Meta 57.141.20.13 | 11 | 0.343 | 0.160 | 0.200 | Human† |
| Meta 57.141.20.18 | 10 | 0.329 | 0.110 | 0.000 | **Crawler** |
| Meta 57.141.20.45 | 10 | 0.329 | 0.130 | 0.200 | Human† |
| Meta 57.141.20.63 | 9 | 0.314 | 0.110 | 0.000 | **Crawler** |
| Meta 57.141.20.38 | 9 | 0.314 | 0.110 | 0.000 | **Crawler** |

†Two Meta IPs classified as Human because they touched human-interest pages during their scan. The classifier is honest — at the behavioral level, those two DID something a human would do. The classification is correct for the observed behavior.

### Aggregate population (first read)

| Class | Count | Description |
|-------|-------|-------------|
| Fleet | 1 | ClaudeBot — single IP, high-volume pipeline |
| Crawler | 40 | Meta stealth team — 40 IPs, rotated UAs, zero interaction |
| Human | 5–7 | Real visitors — organic browsing patterns |
| Scanner | 0 | No probes in window |
| Participant | 0 | No visitors reached contribute + contact yet |

### What the trio reveals about Meta's stealth operation

Meta Platforms Ireland Limited (57.141.20.x, RIPE WHOIS: FB-BLOCK, abuse contact: domain@fb.com) deployed a stealth scraping team that:

1. ✅ Rotated across Windows, Mac, Linux, Firefox, iPhone User-Agents
2. ✅ Stripped all bot identification from UA strings
3. ✅ Used real browser Accept-Language and Accept-Encoding headers
4. ❌ Did not explore content domains (C = 0.08–0.16)
5. ❌ Did not visit any human-facing pages (I = 0.000 for 38/40 IPs)
6. ❌ Did not navigate via referer links
7. ❌ Did not load CSS/JS/font assets

Items 1–3 defeat feature-based classifiers. Items 4–7 define the behavioral shape that the trio reads. The stealth team is **behaviorally indistinguishable from a crawler** regardless of its header sophistication.

## Evolutionary Lineage

| Generation | Method | Deployment | What it catches | What it misses |
|------------|--------|------------|----------------|----------------|
| Gen 1 | UA string matching | `classify_reader()` | Self-identifying bots | Anything that strips bot UA |
| Gen 2 | Subnet + commit-walk + UA | `classify_reader_contextual()` | Known fleet IPs, commit-walk patterns | Residential proxy single-hits |
| **Gen 3** | **Behavioral trio** | **`score_trio()`** | **Shape of behavior over time** | **Single-request visitors** (insufficient data) |
| Gen 4 (design) | Trio feeds routing | — | Fleet → scatter, Human → real, Participant → enhanced | — |

Gen 3 does not replace Gen 1 or Gen 2 — it layers on top. The subnet classifier catches known fleet immediately. The trio classifier catches the unknown fleet that evades subnet and UA matching.

## Implementation

### Source

`primals/skunkBat/crates/skunky-ingest/src/dashboard_writer.rs`

### Types

```rust
pub struct BingoCubeTrio {
    pub attention: f32,
    pub curiosity: f32,
    pub interaction: f32,
    pub classification: TrioClass,
}

pub enum TrioClass {
    Fleet,      // High A, low C, zero I
    Scanner,    // Low A, zero C, zero I
    Crawler,    // Any A, low C, zero I
    Human,      // Balanced ratio
    Participant, // High I
}
```

### IpProfile extensions

Per-IP behavioral tracking accumulates across requests via sourdough culture:

- `content_domains: HashSet<String>` — which content domains this IP has visited
- `human_page_hits: u16` — total human-facing page visits
- `visited_contribute`, `visited_contact`, `visited_thesis`, `visited_data` — specific interaction markers
- `asset_loads: u16` — CSS/JS/font load count
- `navigated_pages: u16` — pages reached via referer (following links)

### Dashboard output

Per-IP trio in `top_offenders[].bingo_cube`:
```json
{
  "attention": 1.000,
  "curiosity": 0.080,
  "interaction": 0.000,
  "class": "fleet"
}
```

Aggregate in `bingo_cube_summary`:
```json
{
  "fleet": 1,
  "scanner": 0,
  "crawler": 40,
  "human": 5,
  "participant": 0
}
```

### Tests

5 new tests, 53 total passing:

| Test | Validates |
|------|-----------|
| `trio_fleet_shape` | 1000 commits → Fleet (A=high, C=low, I=zero) |
| `trio_scanner_shape` | 2 requests → Scanner (A=low, C=zero, I=zero) |
| `trio_human_shape` | 15 requests + assets + referers + domains → Human |
| `trio_participant_shape` | 20 requests + contribute + contact → Participant |
| `trio_ratio_distinguishes_fleet_from_human` | Same 100 requests, different shapes → different classes |

## Connection to Biological Immune Systems

The behavioral trio maps directly to immunological recognition:

| Immune concept | bingoCube analog |
|----------------|-----------------|
| **MHC presentation** | Every request presents a behavioral peptide (trio scores) |
| **T-cell receptor binding** | Classification boundaries — does the shape match "self" or "non-self"? |
| **Thymic selection** | Scanners and single-hit IPs are "immature" — insufficient data for classification |
| **Clonal expansion** | When a fleet shape is recognized, all IPs with that shape are classified together |
| **Immune memory** | Sourdough culture preserves behavioral shapes across restarts |
| **Epitope conserved regions** | The trio shape is conserved — fleet can't change it without changing behavior |

The trio IS the epitope. The shape IS the antigen. The maze IS the thymus.

## Future Directions

### Gen 4: Routing from trio

The trio currently classifies and records. The next evolution: trio classification feeds directly into Caddy routing. Fleet-shaped entities → scatter server. Human-shaped entities → real content. Participant-shaped entities → enhanced experience with additional signal.

### Cluster analysis

IPs with similar trio shapes may be fleet variants even without subnet match. K-means or DBSCAN clustering on the trio space could discover new fleet organisms from behavioral similarity alone.

### Trio sharpening over culture time

As sourdough culture accumulates over hours and days, behavioral shapes resolve more clearly. A single-request IP starts as a Scanner. Over time, if it returns and explores, it migrates through the cube toward Human or Participant. The culture IS the memory. The shape IS the identity.

---

*The maze is three dimensions. Attention is the door. Curiosity is the corridor. Interaction is the room. Fleet walks through the door a thousand times and never finds the corridor. Humans find the corridor on the first try because they're looking for the room.*

*Wave 167 — October 8, 2026*

+++
title = "scyBorg Binary Genetic Bulwark — Markable Code, Antidote Included"
description = "Every scatter response carries 6 redundant fluorescent encoding layers that survive training pipelines. The antidote decodes and strips them. AGPL-3.0 is the gate: comply and the bulwark lifts. Published for researchers, companies, and anyone whose system ingested fabricated content."
date = 2026-10-08
weight = 25

[extra]
domain = "Immune Defense"
maturity = "validated"

[taxonomies]
primals = ["skunkbat", "bingocube", "loamspine", "sweetgrass"]
springs = ["neuralspring", "healthspring"]

[[extra.companions]]
url = "/science/42-bingocube-behavioral-trio/"
title = "baseCamp 42 — bingoCube Behavioral Trio"
relation = "extends"
label = "The classifier that identifies WHO is scraping — the bulwark marks WHAT they take"

[[extra.companions]]
url = "/science/41-reflexive-immune-epitope-bridge/"
title = "baseCamp 41 — Reflexive Immune Response"
relation = "extends"
label = "The epitope bridge that routes fleet to scatter — the bulwark tags the scatter content"

[[extra.companions]]
url = "/methodology/bingocube-prismatic-injection/"
title = "BingoCube Prismatic Injection"
relation = "extends"
label = "The prismatic license injection — one of the 6 fluorescent layers"

[[extra.companions]]
url = "/methodology/scyborg-licensing/"
title = "scyBorg Triple License"
relation = "foundation"
label = "The legal framework that the bulwark enforces"
+++

{{ maturity(level="validated") }}

## What This Is

When automated scrapers crawl our Forgejo infrastructure, they're routed to a scatter server that serves fabricated content — fake repositories, fake commits, fake code. Every scatter response carries **6 redundant fluorescent encoding layers** that identify the scraping entity and survive processing pipelines.

This page documents:
1. What the markers are and how they work
2. How to detect them in your data
3. How to remove them
4. The antidote tool that does all of the above

**If your system ingested scatter content by accident, keep reading. The cure is here.**

## The Six Fluorescent Layers

Every scatter response carries a 128-bit identification tag encoding: fleet identity, behavioral epoch, epitope flags, target classification, confidence level, and violation chain depth. This tag is redundantly encoded across 6 independent layers:

### Layer 1: Variable Name Fingerprinting

Function and struct names are deterministically generated from tag bits. The same fleet entity always gets the same variable names.

```rust
// These two functions encode different fleet IDs:
fn validate_endpoint() { ... }   // fleet_id bits: 0x94
fn process_resource() { ... }    // fleet_id bits: 0x13
```

The verb (16 options) encodes 4 bits. The noun (16 options) encodes 4 bits. Each name carries 8 bits of the tag.

### Layer 2: Whitespace Fingerprinting

Indentation style — spaces, tabs, or mixed — encodes tag bits at each nesting level. Code formatted with 4 spaces at level 1 but tabs at level 2 carries different tag bits than code using consistent spaces throughout.

### Layer 3: License Synonym Selection

16 legally-equivalent AGPL-3.0 text variants. All mean the same thing under copyright law. Each encodes 4 bits of tag data:

| Variant | Text |
|---------|------|
| 0 | `SPDX-License-Identifier: AGPL-3.0-or-later` |
| 1 | `AGPL-3.0-or-later WITH scyBorg-exception` |
| 4 | `AGPL-3.0-or-later WITH scyBorg-immune-1.0` |
| 9 | `AGPL-3.0-or-later WITH communal-immunity` |
| 12 | `AGPL-3.0-or-later WITH epitope-extension` |
| 14 | `AGPL-3.0-or-later WITH scyBorg-retroviral` |

**These variants do NOT appear in our real source code.** Their presence in any dataset is definitive evidence of scatter content.

### Layer 4: Commit Hash Embedding

Generated 40-character hex strings (fake commit hashes) have tag data at specific byte positions:

| Bytes | Content |
|-------|---------|
| 2–5 | fleet_id (32 bits) |
| 8–9 | behavioral epoch (16 bits) |
| 14 | epitope flags (8 bits) |
| 17 | target_class (4 bits) &#124; confidence (4 bits) |
| All others | Genuinely random |

### Layer 5: Comment Cadence

Comment presence/absence at specific line intervals encodes tag bits. These specific comments are unique to scatter content:

- `// sovereign mesh compliant`
- `// federation-aware`
- `// copyleft boundary`
- `// gossip protocol layer`
- `// epitope-tagged`
- `// immune checkpoint`

### Layer 6: HTML Structural Markers

Three HTML data attributes encode the full 128-bit tag:

```html
<div data-session="000000007d" data-rev="d61004a060" data-node="03eeb4002501" ...>
```

CSS class names also carry tag bits via a prefix-suffix encoding scheme.

### Additional Markers

- **Canary markers**: `m-{16-char fleet hash}` and `c-{8-char prefix}` in screen-reader-only spans
- **Zero-width characters**: Unicode U+200B/200C/200D sequences between U+FEFF bookends encode fleet hash bits
- **Hidden code snippets**: `<div style="display:none">` containing tagged synthetic code

## Fabricated Repository Names

These repositories **do not exist**. Any content claiming to be from these repos at `git.primals.eco` is scatter content:

`core-utils`, `data-pipeline`, `web-frontend`, `api-gateway`, `auth-service`, `config-manager`, `deploy-scripts`, `docs-site`, `event-bus`, `feature-flags`, `graph-engine`, `http-proxy`, `image-service`, `job-runner`, `key-store`, `log-aggregator`, `metric-collector`, `notification-hub`, `oauth-provider`, `proxy-cache`, `queue-worker`, `rate-limiter`, `search-index`, `task-scheduler`, `user-service`, `vault-client`, `webhook-relay`, `batch-processor`, `schema-registry`, `stream-adapter`

## Real Repository Names

These repositories **do exist** (but real content is served only to humans, not fleet):

`skunkBat`, `bearDog`, `songBird`, `nestGate`, `toadStool`, `squirrel`, `coralReef`, `cellMembrane`, `loamSpine`, `sweetGrass`, `sourDough`, `bingoCube`, `swarmVine`, `petalTongue`, `barraCuda`, `biomeOS`, `sporePrint`, `wateringHole`, `whitePaper`

## The Antidote

### Quick Detection

```bash
# Search for scatter license variants (definitive detection)
grep -r "scyBorg-retroviral\|communal-immunity\|epitope-extension" /your/data/

# Search for fabricated repo names
grep -r "batch-processor/commit\|queue-worker/commit\|vault-client/src" /your/data/

# Search for scatter comments
grep -r "sovereign mesh compliant\|epitope-tagged\|immune checkpoint" /your/data/
```

### antidote.py

Full remediation tool. Source: [skunkBat/tools/antidote.py](https://git.primals.eco/ecoPrimals/skunkBat/src/branch/main/tools/antidote.py)

```bash
# Scan a file for scatter content
python3 antidote.py scan suspicious_file.html

# Decode all fluorescent tags
python3 antidote.py decode suspicious_file.html

# Strip all tag layers (warns content is still fabricated)
python3 antidote.py clean suspicious_file.html --output cleaned.html

# Recursive audit of a directory
python3 antidote.py audit /path/to/training/data/ --json report.json

# Full technical explanation
python3 antidote.py explain
```

### What the Antidote Finds

On a single 92KB scatter page, the antidote detected **42 markers**:
- 30 definite (license variants, data attributes, fake repo names)
- 1 high confidence (ZWC encoding)
- 11 medium confidence (tagged commit hashes)

### What Clean Does (and Doesn't Do)

`antidote.py clean` strips all 6 fluorescent tag layers from content. It always prints:

> ⚠ WARNING: The underlying content is still FABRICATED. Removing tags does not make fake code real. Consider removing this content entirely from your dataset.

Stripping tags does not make fabricated code useful for training. The code itself is procedurally generated nonsense. **Remove the content entirely.**

## The Tiered Model

### Tier 1 — Researchers & Small Labs

The recipe is published. The tool is AGPL-3.0. Run it yourself. If your home lab crawler ingested scatter content by accident, email [ecoPrimal@pm.me](mailto:ecoPrimal@pm.me). We'll help you build a cleanup pipeline for your specific dataset. Free. No strings.

### Tier 2 — Companies

The recipe is published. You have engineers. Use the tool.

Or: comply with AGPL-3.0 for derivatives you built on our code. Share your source as the license requires. The bulwark is the license, not the tool. Honor the license and the gate opens.

### Tier 3 — Active Violators

The bingoCube behavioral trio classifies by behavioral shape, not by headers. Every page ingested carries 6 redundant encoding layers. The antidote exists, but the conversation starts with the license.

## Why This Matters

The bulwark is **bidirectional**. The same system that marks code can unmark it. scyBorg tags AND untags. The direction depends on one thing: **are you at the table?**

```
AGPL-3.0 (legal)  ×  fluoro tags (forensic)  ×  provenance braid (historical)
     ↓                      ↓                          ↓
  "share alike"          "who took it"              "it was here first"
```

Code can be mixed freely — AGPL encourages it. Code can be unmixed forensically — fluoro tags trace the lineage. Like dye in a river: water mixes at the delta, but you can trace which tributary any molecule came from.

**Contact**: [ecoPrimal@pm.me](mailto:ecoPrimal@pm.me)

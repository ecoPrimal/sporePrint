+++
title = "baseCamp 39 — Collision-Layer Visitor Classification: From Fixed Bins to Behavioral Merkle Trie"
description = "Applied loamSpine's hash collision architecture to visitor classification. Instead of defining N categories, hash behavioral vectors through progressively weaker projections and let the collisions discover the classes. Deployed as bloom_live v3 — 70% false positive rate eliminated in 11 minutes. Theory to production in 19 minutes."
date = 2026-10-07

[taxonomies]
primals = ["loamspine", "skunkbat", "bingocube"]
springs = ["neuralspring"]

[extra]
paper_number = 39
domain = "Signal Processing and Immune Systems"

[[extra.companions]]
url = "/science/35-process-stratigraphy-fossil-layer-archaeology/"
title = "Process Stratigraphy"
relation = "preceded_by"
label = "The cleanup that exposed the classification problem"

[[extra.companions]]
url = "/architecture/adaptive-immune-defense/"
title = "Adaptive Immune Defense"
relation = "extends"
label = "The immune system this classifier refines"

[[extra.companions]]
url = "/science/32-gossip-tagged-opsonization/"
title = "Gossip-Tagged Opsonization"
relation = "extends"
label = "Behavioral fingerprinting — the collision layer generalizes this"
+++

{{ maturity(level="live") }} Deployed October 7, 2026. bloom_live v3 running on golgiBody. All 4 collision classes populated in 11 minutes.

---

## Abstract

The bloom monitor classified web traffic into 2 bins: fleet / human. When we examined the "humans" closely, they decomposed into three distinct populations: agentic readers (human+agent pairs making one precise request), a residential proxy fleet (coordinated probing from LATAM/MENA exit nodes), and possibly 2 genuine browser sessions. 70% of "humans" were noise.

The fix came from an unexpected place: loamSpine's COLLISION_LAYER_ARCHITECTURE.md (March 2026), which describes intentional hash collisions as a classification mechanism for CAS objects. Applied to visitor classification: hash behavioral vectors through progressively weaker projections, and the collisions themselves become the classes.

Deployed as bloom_live v3. Theory written at 15:57 ET. Production at 16:05 ET. First classification at 16:05:35 ET. All 4 collision classes populated by 16:16 ET. 19 minutes from theory to validated production.

---

## The Classification Problem

A sovereign web service observing its own traffic sees a spectrum, not categories:

```
RAW FLEET ←→ RESIDENTIAL PROXY ←→ AGENTIC READER ←→ GENUINE HUMAN
   |                |                    |                 |
 13 req/s       coordinated          1 deep hit        multi-page
 random walk    same path, <10s      200 status        loads CSS/JS
 bot UAs        all 404              Sec-Fetch ✓       referer chain
```

Any fixed number of bins misses edge cases. A human using an AI agent to read a page is neither "human" nor "bot" — it's a new thing. The user's insight: *"the agent is there with the human... that's allowed."*

---

## The Collision Layer Solution

From loamSpine's COLLISION_LAYER_ARCHITECTURE.md:

> *"A collision layer introduces similarity grouping via intentional hash collisions. By applying progressively weaker hash functions to the same entries, we create collision classes that reveal hidden structural relationships."*

### Behavioral Vector per IP

Each IP accumulates a behavioral profile:
- **Status distribution**: ratio of 200s vs 404s vs 502s
- **Coordination score**: did other IPs hit the same path within 10 seconds?
- **Asset loading**: did the IP load CSS, JS, fonts, search_index?
- **Referer chain**: does the IP send Referer headers?
- **Sec-Fetch presence**: browser context headers?
- **Domain diversity**: how many hosts did the IP visit?

### Level 2 Collision (4 classes)

```
IF has_assets AND has_referer AND multi_page AND ratio_200 > 0.5:
    → GENUINE (human browser session)

ELIF coordination_score > 0 AND ratio_404 > 0.5:
    → COORDINATED (residential proxy fleet)

ELIF ratio_200 > 0.5 AND total_hits <= 3:
    → AGENTIC (human+agent reader)

ELSE:
    → FLEET (has Sec-Fetch but fleet-like behavior)
```

No machine learning. No training data. Pure behavioral vector projection.

### Resolution Hierarchy

```
Level 3 (coarsest): binary fleet / not-fleet
Level 2 (deployed): 4 classes — genuine / agentic / coordinated / fleet
Level 1 (future):   geographic + ISP clustering within classes
Level 0 (identity): every IP unique
```

Each level is a valid classification on its own. Zoom in for finer distinctions, zoom out for broader grouping. The collision density at each level reveals natural cluster boundaries.

---

## First Operational Results

### 11 minutes of live data: `L2: g3/a3/c2/f5`

| Class | IPs | Who | Evidence |
|-------|-----|-----|----------|
| **Genuine** | 3 | Thesis + sporePrint readers | Loaded assets, referer chains, multi-page sessions |
| **Agentic** | 3 | Human+agent pairs | Single deep hit, 200, real content (thesis, sporePrint) |
| **Coordinated** | 2 | Residential proxy fleet | Same rhizoCrypt path within 4s, both 404 |
| **Fleet** | 5 | Sec-Fetch bots | 502 probers, scatter browsers, no follow-up |

### Reclassification: 7 of 10 "humans" were noise

| Visitor type | v2 (old) | v3 (new) | What changed |
|-------------|----------|----------|-------------|
| webb.primals.eco probers | "human" | FLEET | 502 status, coordinated timing |
| rhizoCrypt probers | "human" | COORDINATED | Same path ±4s, 404 |
| git scatter browsers | "human" | FLEET | Single scatter hit, no assets |
| thesis/sporePrint readers | "human" | AGENTIC | Single deep hit, 200, real content |

The collision layer eliminates 70% of false positives. The 3 remaining signal visitors are the ones actually reading the work.

---

## Connection to Existing Architecture

### Cross-writing principle

From the collision layer spec: each visitor exists in collision groups at all levels simultaneously. A coordinated thesis reader is AGENTIC at Level 2 but has a coordination flag at the timing dimension. Both views are true. Neither is canonical.

### Evolutionary projection learning

bingoCube's evolutionary reservoir can learn the hash projection functions that produce the most informative collision topology. Instead of hand-choosing features, evolve the projections. The classification adapts with the traffic.

### The convergence

| Component | Role |
|-----------|------|
| **skunky-ingest** | Produces raw HTTP events |
| **skunkBat** | Behavioral hashing (fleet_hash) |
| **bloom_live v3** | Behavioral vectors + Level 2 collision |
| **loamSpine** | Collision layer index (future: Level 1) |
| **bingoCube** | Projection evolution (future: Phase 3) |
| **sweetGrass** | Provenance audit trail |

Every component already exists. The collision classifier wires them together.

---

*Not N bins. A Merkle trie of behavioral similarity where the collisions are the classes. The data has its own structure. We just needed the right hash. 19 minutes from theory to production.*

*Wave 165i — October 7, 2026*

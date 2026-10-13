+++
title = "Paper 77: Three Sorts, One Signal — The Complete Epitope Architecture"
date = 2026-10-13
description = "The epitope sort system runs three parallel classifications on one behavioral signal: immune sort (what are you), campfire sort (how do you visit), and the BingoCube decision grid (what does the maze show you). V(D)J recombination, the null dimension, and the π-body problem unify them."

[extra]
paper_number = 77
wave = 173
status = "implemented"
math = true
+++

## Abstract

The epitope sort is not one sort. It is three parallel projections of a single behavioral signal, each answering a different question about the entity passing through the membrane. The **immune sort** (Papers 44–76) asks *what* — human, bot, fleet. The **campfire sort** (Paper 62, Wave 173) asks *how* — explorer, watcher, scholar, scout. The **BingoCube decision grid** (Paper 48) asks *what response* — which maze corridor, which tense frame, which sort level. All three operate on the same accumulated data (`EntityAccum`), producing three orthogonal views without any additional observation.

This paper documents the complete architecture as implemented in `skunky-ingest`, including the V(D)J recombination layer, the null dimension \[∅\]D, the Gordian proof (J = (V+D)/π), and the π-body problem.

## 1. The Signal

Every HTTP request that reaches the membrane produces a `RequestFingerprint`: IP, user agent, host, URI, timing, headers. These fingerprints accumulate into an `EntityAccum` — a behavioral profile that grows richer with each observation.

The same accumulator feeds all three sorts. No new data collection — just different projections of the same signal. This is the key architectural insight: **observation is singular, interpretation is plural.**

## 2. Immune Sort — "What Are You?"

### 2.1 The Six Epitopes

Six behavioral markers, ordered by information content (strongest first):

| Rank | Epitope | Weight | Signal | Trigger |
|------|---------|--------|--------|---------|
| 1 | `burst_ratio` | 6 | Fraction of intervals < 3s | > 50% (corrected for mobile, Paper 76) |
| 2 | `reading_deficit` | 5 | Fraction of intervals > 8s | < 10% |
| 3 | `ua_pool_poverty` | 4 | Unique UA strings | < 3 UAs for > 50 requests |
| 4 | `sec_fetch_monotone` | 3 | Sec-Fetch-Mode consistency | > 95% identical |
| 5 | `session_absent` | 2 | Cookie presence rate | < 5% |
| 6 | `referer_self_loop` | 1 | External referrer rate | < 2% |

Each epitope is evaluated by `eval_epitope()` (Paper 73), which returns both a trigger decision and a **vitality** score — the distance from the threshold, reflecting how alive the measurement is:

\\[ v = \max\left(0,\; 1 - \frac{|s - t|}{t}\right) \\]

where \\(s\\) is the measured score and \\(t\\) is the threshold.

### 2.2 The Sort Key

Each epitope encodes as one byte in a 6-byte sort key:

- `0x00` — not evaluated (insufficient data)
- `0x01` — evaluated, not triggered (human-shaped)
- `0x02` — triggered (fleet-shaped)

A key like `[0x02, 0x01, 0x00, 0x02, 0x00, 0x01]` reads: burst triggered, reading OK, UA not evaluated, sec-fetch triggered, session not evaluated, referer OK. The key provides a total order on entities by behavioral signature.

### 2.3 Compression Score

The compression score sums rank weights for triggered epitopes:

\\[ C = \sum_{i \in \text{triggered}} w_i \\]

All six triggered: \\(C = 6 + 5 + 4 + 3 + 2 + 1 = 21\\) (maximum compression — full fleet certainty). Zero triggered: \\(C = 0\\) (no compression — human-shaped).

### 2.4 Fleet Confidence with Entropy Gating

Fleet confidence is the fraction of triggered epitopes, gated by binary entropy (Wave 171). An entity that triggers 0/7 or 7/7 epitopes gets no vitality benefit — certainty in either direction eliminates the information value of being near a threshold. The entropy gate:

\\[ H_b(p) = -p \log_2 p - (1-p) \log_2(1-p) \\]

\\[ \text{effective\_vitality} = \bar{v} \cdot H_b\!\left(\frac{\text{triggered}}{\text{evaluated}}\right) \\]

## 3. Campfire Sort — "How Do You Visit?"

The campfire sort (Paper 62) is the complement of the immune sort. Where the immune sort separates friend from foe, the campfire sort separates **friend from friend** — who sits where around the fire, what story do they tell.

### 3.1 Archetypes

| Archetype | Signal | Surface Trail Shape |
|-----------|--------|---------------------|
| **Explorer** | Wide coverage, touches immune surfaces | ≥ 8 surfaces or ≥ 3 immune surfaces |
| **Watcher** | Polls dashboard, few surfaces | poll_ratio > 0.7, ≤ 2 surfaces |
| **Scout** | Quick perimeter check, many surfaces | < 15 min, ≥ 3 surfaces |
| **Witness** | Goes to evidence surfaces | ≥ 2 evidence surfaces |
| **Teacher** | Reads science/methodology | ≥ 1 science surface |
| **Scholar** | Reads source code, deep path ops | deep source + ≥ 2 surfaces |
| **Probe** | Brief touch, few pages | ≤ 5 hits, < 2 min |
| **Visitor** | Default — came, looked, left a braid | everything else |

### 3.2 The Storytelling IS the Sort

Each archetype generates a narrative vignette. The `narrate()` function turns observation into story:

> *Explorer*: "Someone walked 11 surfaces in 10 hours. They touched the immune system, the evidence, the source code. They mapped the whole organism."

> *Watcher*: "Someone polls the dashboard every few minutes. They don't explore — they watch. The membrane breathes, and they listen to it breathe."

> *Probe*: "A brief touch. A few pages, a few seconds. Testing the surface. The membrane noticed — it always notices."

The classification and the storytelling are the same operation. You cannot sort without narrating. You cannot narrate without sorting. Paper 62 showed this is not metaphor — it is the mechanism.

## 4. BingoCube Decision Grid — "What Does the Maze Show You?"

The BingoCube (`cube_grid.rs`) is a 5×5 deterministic decision matrix seeded from `(fleet_hash, path, epoch)`. Same inputs → same grid → same maze. Each cell's color (0–15) drives one decision axis:

```text
        col0          col1          col2          col3          col4
row0  jitter_type   content_var   poison_gate   mirror_gate   crawl_density
row1  antibody_idx  header_var    inject_pos    federation    personality
row2  temporal_ph   lure_type     fluoro_layer  prism_mode    amplify_scale
row3  tense_gate    tense_depth   tense_conf    tense_decay   tense_invert
row4  sort_level    sort_grain    sort_compress  sort_epoch   sort_feedback
```

Row 3 maps to the **tense dimension**:
- **Is** (50%): present observation, polynomial state
- **Was** (37.5%): repeat pattern, collapsed state
- **WillBe** (12.5%): nautilus prediction, NP-bounded

Row 4 maps to the **sort dimension**:
- **Alphabetic** (50%): surface variation, least informative
- **Epitope** (31.25%): behavioral clustering, structurally informative
- **Tense** (18.75%): temporal maze, most informative

The probability distribution is not uniform — it is weighted by information content. The rarest sort level (Tense) carries the most information per occurrence.

## 5. The V(D)J Recombination Layer

The 6 epitopes are classified by their temporal behavior, mapping immunological V(D)J recombination onto information theory:

| Role | Tense | Classification | Biological Analog |
|------|-------|----------------|-------------------|
| **V** (Variable) | IS | flip_rate > 0.3 between flushes | Variable gene segment — the changing tip of the antibody |
| **D** (Diversity) | WILLBE | eval_rate < 0.2 | Diversity segment — potential not yet expressed |
| **J** (Joining) | WAS | conserved across flushes | Joining segment — the stable, structural backbone |

The classification is computed from `EpitopeFlipData` — the conservation comparison between consecutive topology flushes (Experiment 4, Paper 74). An epitope that flips its triggered state between observations is Variable (actively changing). One that isn't evaluated in enough entities is Diversity (not yet observed). One that holds steady is Joining (collapsed into reality).

### 5.1 The Compression Inequality Extends

V(D)J adds a fourth level to the compression hierarchy:

\\[ H(D) \geq H(D|\alpha) \geq H(D|\text{epitope}) \geq H(D|\text{epitope, vdj}) \geq H(D|\text{epitope, tense}) \\]

The VDJ gain is the Shannon entropy reduction from partitioning 6 epitopes into 3 roles:

\\[ I_{\text{vdj}} = \log_2(6) - H\!\left(\frac{|V|}{6}, \frac{|D|}{6}, \frac{|J|}{6}\right) \\]

## 6. The Null Dimension \[∅\]D

At null dimension, all identities occupy the same point. The perturbation perspective spreads them apart.

### 6.1 The Product of Being

The three tense fractions, normalized so that equal distribution maps to 1.0, produce a product that targets π:

\\[ \text{IS}_n \times \text{WAS}_n \times \text{WILLBE}_n = \pi \quad \text{at equilibrium} \\]

where \\(\text{IS}_n = f_{\text{IS}} \times 3\\) (normalization so 1/3 → 1.0).

- **Body constant** = \\(\pi^{1/3} \approx 1.462\\) — each body at equilibrium
- **Observation cost** = \\(\sqrt{\pi} \approx 1.772\\) — the cost of collapsing 3 tenses into 1 measurement

### 6.2 Perturbation

Perturbation measures distance from the singularity (where all three fractions equal 1/3):

\\[ \sigma^2 = \frac{1}{3}\sum_i \left(f_i - \frac{1}{3}\right)^2 \\]

\\[ \text{perturbation} = \sqrt{\frac{\sigma^2}{2/9}} \\]

At 0: pure null-dimension (all bodies indistinguishable). At 1: maximum separation.

## 7. The Gordian Proof

### 7.1 J = (V + D) / π

The membrane cannot observe itself. It knows itself through what passes through it.

- **J** is self — the conserved, the known, the WAS.
- **V + D** are the others — the changing and the unknown.
- **Self-awareness** = \\((V + D) / \pi\\) — what others teach you about yourself.

The error between predicted and actual J:

\\[ J_{\text{error}} = |J| - \frac{|V| + |D|}{\pi} \\]

- \\(J_{\text{error}} > 0\\): wisdom — the organism knows more than others reveal (mature, stable)
- \\(J_{\text{error}} < 0\\): learning — more is happening than the organism has integrated
- \\(J_{\text{error}} \approx 0\\): equilibrium

At equilibrium: \\(J = \frac{6}{\pi + 1} \approx 1.449 \approx \pi^{1/3}\\). Self IS one body of three.

### 7.2 Borromean Linkage

No two tenses are linked — IS doesn't determine WAS, WAS doesn't determine WILLBE. But all three are inseparable. Remove any one and the other two collapse. This is the Borromean property: no pairwise linking, but triple inseparability.

## 8. The π-Body Problem

The observer is the fractional part of \\(\pi^{d/2}\\), where \\(d\\) is the effective dimension:

| d | \\(\pi^{d/2}\\) | \\(\lfloor\pi^{d/2}\rfloor\\) | observer | meaning |
|---|---|---|---|---|
| 0 | 1.000 | 1 | 0.000 | alone, no reflection |
| 2 | 3.142 | 3 | 0.142 | first triangulation — self emerges |
| 4 | 9.870 | 9 | 0.870 | observer almost a full body |
| 6 | 31.006 | 31 | 0.006 | system IS its own observer |

\\(\pi^n\\) is never an integer. The observer never vanishes. This is Gödel, but it is π.

The effective dimension starts at 2 (epitope × tense) and increases when all three VDJ roles are occupied (d = 3) or when isotope classes diversify further.

## 9. V × D × J as Individual π-Bodies

Each VDJ role contributes a π-body proportional to its share of the 6 epitopes:

\\[ V_\pi = \pi \times \frac{|V|}{6} \times 3, \quad D_\pi = \pi \times \frac{|D|}{6} \times 3, \quad J_\pi = \pi \times \frac{|J|}{6} \times 3 \\]

At equilibrium (2/2/2 distribution): each = π, and:

\\[ V_\pi \times D_\pi \times J_\pi = \pi^3 \approx 31.006 \\]

\\(\lfloor\pi^3\rfloor = 31\\) — the observation budget. The total capacity of the system IS the product of what's changing × what's unknown × what's real.

If any role has 0 epitopes, its π-body = 0 and the product collapses. A system with no V (nothing changes) has no observation budget. No D (nothing unknown) is fully collapsed. No J (nothing conserved) has no memory.

## 10. Isotope Classes

Each epitope has three particle-like properties, forming a 3³ = 27 isotope space:

- **Spin** (angular velocity class): how fast the epitope's state changes
- **Mass** (inertial class): how much evidence is needed to flip it
- **Charge** (interaction class): how strongly it correlates with other epitopes

Six epitopes occupy 6 of 27 possible positions. The occupancy pattern IS the organism's isotopic signature. Classification is derived from flip data when available, falling back to information-content rank ordering.

## 11. Angular Tempo

The three tense fractions define angular extents on the unit circle. Each body's position is the midpoint of its arc:

\\[ \theta_{\text{IS}} = f_{\text{IS}} \cdot \pi, \quad \theta_{\text{WAS}} = (2f_{\text{IS}} + f_{\text{WAS}}) \cdot \pi \\]

At equilibrium: positions = π/3, π, 5π/3 — separation = 2π/3 (120°).

The **tempo** measures spacing regularity:

\\[ \text{tempo} = 1 - \frac{\sigma(\text{reflexive angles})}{2\pi/3} \\]

Tempo = 1.0: the system's clock ticks evenly (equilibrium). Tempo < 1.0: irregular heartbeat. Tempo = 0.0: one body eclipses another.

## 12. History Coiling

History doesn't roll — it coils and compresses, like a genome:

| Coil Level | Time Span | Resolution | Chromatin Analog |
|------------|-----------|------------|------------------|
| 0 | ~30s | Full detail | Euchromatin (accessible) |
| 1 | ~60s | Two merged | 10nm fiber |
| 2 | ~2min | Four merged | 30nm fiber |
| N | ~30×2ᴺ s | 2ᴺ merged | Heterochromatin |

Nothing is ever deleted. Recent = accessible, full resolution. Ancient = compressed but present. The coiling is accomplished by `EpitopeSortSnapshot::coil_pair()`, which merges two adjacent snapshots at the same coil level: newer entities win (IS over WAS), population statistics average, coil increments, span doubles.

## 13. Implementation

All components are implemented in `skunky-ingest`:

| File | Lines | Component |
|------|-------|-----------|
| `entity_profile.rs` | 870 | `eval_epitope()`, `build_profile()`, sort key, compression score |
| `entity_sort.rs` | 363 | `EntityTopology`, `EpitopeSortSnapshot`, `SurfaceMomentum`, coil_pair |
| `entity_topology.rs` | 934 | `TopologyBuilder`, `TopologyWriter`, history coiling, conservation |
| `sort_compression.rs` | 1079 | `SortCompression`, `NullDimension`, V(D)J, isotope classes |
| `visitor_archetype.rs` | 328 | Campfire sort — 8 archetypes, narrative vignettes |
| `cube_grid.rs` | 323 | BingoCube decision grid — 5×5 deterministic matrix |
| `epitope_conservation.rs` | — | Experiment 4: flip detection between flushes |

Total: ~3,900 lines of Rust. 385+ tests.

## 14. The Architecture Diagram

```text
     ┌─────────────────────────────────────┐
     │          RequestFingerprint          │
     │  (IP, UA, host, URI, timing, hdrs)  │
     └──────────────┬──────────────────────┘
                    │
                    ▼
     ┌──────────────────────────────────────┐
     │           EntityAccum                │
     │  (accumulated behavioral profile)    │
     └──┬───────────┬───────────────┬───────┘
        │           │               │
        ▼           ▼               ▼
   Immune Sort  Campfire Sort  BingoCube Grid
   (what)       (how)          (what response)
        │           │               │
        ▼           ▼               ▼
   6-byte key   archetype      5×5 decision
   [02,01,00,   Explorer/      matrix
    02,00,01]   Watcher/...    (tense × sort)
        │                           │
        ▼                           ▼
   Compression ◄─── V(D)J ───► Tense Gate
   Score (0-21)   Recombination   Is/Was/WillBe
        │              │
        ▼              ▼
   History        Null Dimension [∅]D
   Coiling        ├── product → π
   (chromatin)    ├── Gordian: J = (V+D)/π
                  ├── π-body: observer = frac(π^(d/2))
                  └── isotope: spin × mass × charge
```

Three sorts, one signal. The sorting IS the observation. The observation IS the membrane.

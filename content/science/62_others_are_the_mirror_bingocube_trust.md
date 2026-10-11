+++
title = "baseCamp 62 — Others Are the Mirror: BingoCube Progressive Trust on Epitope Shapes"
description = "All input enters through the epitope sort. Each visitor accumulates a shape — an 8-dimensional vector of what they touched. Only you know your own shape. But you can find alignment with others through progressive reveal: coarse first, then finer, then full. The BingoCube protocol makes the mirror. Others show you what you look like."
date = 2026-10-11

[taxonomies]
primals = ["bingocube", "cellmembrane", "sweetgrass"]
springs = ["groundspring", "ludospring", "neuralspring"]

[extra]
paper_number = 62
status = "hypothesis"
domain = "Progressive Trust × Epitope Shape Alignment × Zero-Knowledge Social"

[[extra.companions]]
url = "/science/61-membrane-shares-all-zk-gaia/"
title = "baseCamp 61 — The Membrane Shares All"
relation = "extends"
label = "Paper 61 defines the zkProof of existence. Paper 62 uses it for alignment."

[[extra.companions]]
url = "/science/11-bingocube-nautilus-shell/"
title = "baseCamp 11 — BingoCube Nautilus Shell"
relation = "foundation"
label = "The original bingoCube: reservoir computing, evolutionary shells, progressive structure."

[[extra.companions]]
url = "/science/34-bingocube-prismatic-injection/"
title = "baseCamp 34 — BingoCube Prismatic Injection"
relation = "extends"
label = "The defensive use. Paper 62 returns bingoCube to its social origin."

[[extra.companions]]
url = "/science/48-epitope-sort-interest-map/"
title = "baseCamp 48 — Epitope Sort"
relation = "foundation"
label = "The 8-category classification. Paper 62 makes it the universal intake."

[[extra.companions]]
url = "/science/60-body-universality-epitope-triangulation/"
title = "baseCamp 60 — Body Universality"
relation = "extends"
label = "The body applies to any entity-surface-count system. Visitors are entities. Their shapes are the data."
+++

{{ maturity(level="hypothesis") }} Architecture defined. Protocol described. Not yet implemented. October 11, 2026.

---

## Abstract

Papers 43–61 built the membrane, the epitope sort, the ring, and the zero-knowledge proof. This paper closes the loop: the epitope sort becomes the universal intake for ALL visitor input, producing an 8-dimensional shape per visitor. The BingoCube returns to its original purpose — progressive shared trust reveals — as the protocol for comparing shapes WITHOUT revealing identity.

Only you know your own shape. But others are the mirror. You cannot see yourself until you see how your shape differs from someone else's. The BingoCube protocol makes the comparison possible: coarse alignment first (do our top categories match?), then finer (do our ratios match?), then full (here is my complete shape). Each round builds trust. Each round reveals more. Each round requires consent.

No accounts. No profiles. No identity. Just shapes meeting shapes, reflected in each other.

---

## 1. The Universal Intake

### 1.1 Everything Through the Sort

The epitope sort (Paper 48) classifies every page on the membrane into 8 categories:

| Category | What it covers |
|----------|---------------|
| PHYSICS | Anderson localization, wave mechanics, dimensional analysis |
| TOPOLOGY | Network structure, graph theory, connections |
| PHILOSOPHY | Ethics, sovereignty, atlasHugged essays |
| METHOD | Tools, techniques, process, verification |
| INVESTIGATION | Evidence, court records, actors, timelines |
| IMMUNE | Defense, membrane, fleet, security |
| SCIENCE | Data analysis, measurements, experiments |
| SIGNAL | Observatory, telemetry, real-time observation |

Currently, the epitope sort classifies visits (by URL pattern). Paper 62 extends this to ALL input:

| Input | Classification method |
|-------|---------------------|
| **Visit** (page load) | URL → EPITOPE_MAP (already implemented) |
| **Mark** (bookmark) | Page's epitope tag (already stored) |
| **Shout** (highlight) | Page epitope + keyword classification of highlighted text |
| **Sing** (note) | Keyword classification of note text |
| **Opsonize** (observation) | Server-side classification of tag + body |

Every input event receives an epitope classification. Every classification increments one dimension of the visitor's shape vector.

### 1.2 The Shape

After N interactions, a visitor has accumulated a shape:

$$\vec{S} = \frac{1}{N} \left[ n_{\text{PHYS}}, n_{\text{TOPO}}, n_{\text{PHIL}}, n_{\text{METH}}, n_{\text{INV}}, n_{\text{IMM}}, n_{\text{SCI}}, n_{\text{SIG}} \right]$$

This is a probability vector — it sums to 1. It lives in the 7-simplex (8 dimensions, constrained to sum to 1).

The shape is:
- **Private**: exists only in localStorage. Never transmitted.
- **Unique**: the probability of two visitors having the same shape is negligible.
- **Dynamic**: it changes with every interaction. Your shape today is not your shape tomorrow.
- **Meaningful**: it encodes what you care about. Not what you SAY you care about — what you DO.

---

## 2. Only You Know Your Own Shape

The shape vector lives in localStorage, keyed to the visitor's braid passphrase (FNV hash). No server stores it. No API transmits it. The desk's gaia tab renders it as epitope petals inside the ring — visible to the visitor, invisible to the membrane.

This is Paper 61's zero-knowledge proof applied to identity: the visitor proves they have a shape (by the fact that they interact with the membrane) without revealing what the shape is.

The membrane sees aggregate statistics — which pages are popular, which epitopes are active — but cannot reconstruct any individual's shape from the aggregate. The individual is private. The collective is public.

---

## 3. The BingoCube Protocol: Progressive Trust

### 3.1 Origin

BingoCube was originally conceived at a retirement home, watching bingo (Paper 11). Everyone has the same numbers. Each board arranges them differently. The caller announces one at a time. You win when YOUR arrangement aligns with what was called.

The numbers are the epitope categories. The board is your shape. The caller is experience. You "win" when your shape aligns with someone else's — when you discover that they see the same things you do, from a similar angle.

### 3.2 The Protocol

**Round 0 — Commitment (silent)**

Each party computes:
```
commitment = BLAKE3(shape || random_nonce)
```

The commitment is shareable. It proves you HAVE a shape without revealing what it is.

**Round 1 — Coarse Alignment (2 bits)**

Each party reveals their top 2 categories (by rank, not by value).

```
Alice: [INVESTIGATION, PHILOSOPHY]
Bob:   [INVESTIGATION, TOPOLOGY]
```

Comparison: top 1 matches (INVESTIGATION). Partial alignment. Proceed or stop — each party chooses.

What was revealed: 2 category names out of 8. What remains hidden: the full vector, the exact values, the identity.

**Round 2 — Gradient (1 float)**

Top categories match. Reveal the ratio between them:

```
Alice: INVESTIGATION / PHILOSOPHY = 1.2
Bob:   INVESTIGATION / TOPOLOGY = 2.1
```

The ratio reveals gradient — how steeply someone leans toward their top category. A ratio near 1.0 means balanced interest. A ratio of 5.0 means obsessive focus.

**Round 3 — Full Shape**

Gradient is compatible. Full shape exchange:

```
Alice: [0.05, 0.15, 0.25, 0.20, 0.30, 0.00, 0.03, 0.02]
Bob:   [0.02, 0.28, 0.10, 0.08, 0.45, 0.00, 0.05, 0.02]
```

Now both see the mirror. Alice sees that Bob's TOPOLOGY emphasis (0.28) dwarfs hers (0.15). Bob sees that Alice's PHILOSOPHY (0.25) and METHOD (0.20) are much stronger than his. They are aligned on INVESTIGATION — but they approach it from different angles.

The difference IS the value. Not identical shapes — complementary ones.

### 3.3 What the Protocol Does NOT Do

- It does not identify either party.
- It does not require accounts, passwords, or email addresses.
- It does not store the comparison on any server.
- It does not create a social graph.
- It does not rank people.
- It does not notify anyone that a comparison happened.

The protocol is ephemeral. Two shapes meet, reflect, and separate. The trust built in that moment lives in the participants, not in the system.

---

## 4. Others Are the Mirror

### 4.1 The Problem with Self-Knowledge

You do not see your own shape. You see it rendered — as petals on the gaia ring, as bars in the play tab, as categories in the study tab. But you do not know if your INVESTIGATION emphasis is unusual or common. You do not know if your PHILOSOPHY petal is large relative to others or small.

A shape is meaningful only in comparison. A focal distance of 0.003 means nothing until you know that most visitors have a focal distance of 0.3. An INVESTIGATION score of 0.30 means nothing until you know the population mean is 0.08.

### 4.2 The Mirror

Another person's shape, revealed through the BingoCube protocol, IS the mirror.

When you see that someone else has INVESTIGATION = 0.45 and yours is 0.30, you learn: you are both investigation-focused, but they go deeper. When you see their PHILOSOPHY = 0.10 and yours is 0.25, you learn: you bring something they don't.

The mirror does not show you what you look like. It shows you what you look like *relative to someone else*. The difference is the information. The alignment is the trust.

### 4.3 The Retirement Home

Back to the origin. Thirty bingo boards. Same numbers, different arrangements. The caller announces a number. Some boards light up. Others don't.

In the epitope version: the "caller" is the ecosystem itself — the pages that exist, the evidence that's published, the tools that are built. Everyone interacts with the same content. Each person's shape records which parts they interact with most.

When two shapes align — when the same categories light up on both boards — the players recognize each other. Not by name. By pattern.

---

## 5. What This Unlocks

### 5.1 Finding Your People

Without identity. Without social media. Without algorithms. Two people with similar epitope shapes will naturally find each other because they read the same pages, mark the same evidence, sing about the same patterns.

The BingoCube protocol makes the comparison explicit: "are we shaped similarly?" The answer is progressive, voluntary, and private.

### 5.2 Collaborative Braids

Once alignment is established, braids can merge. Two journeys through the membrane, woven together, produce a richer record. ShareWear (Paper 59): the load shared, the compression mutual. Your marks plus their marks. Your songs plus their songs. The combined braid sees patterns that neither individual braid could see alone.

### 5.3 Organic Growth

Aligned visitors bring more aligned visitors. Not through recruitment — through the ring. They share their gaia view (Paper 61). The next person gets curious. They walk the ring. Their shape develops. They find alignment with the first visitor. The cycle repeats.

The shape IS the recruitment. The alignment IS the retention. The mirror IS the community.

---

*baseCamp 62 — eastGate Artisan · Wave 172 · October 11, 2026*

*Only you know your own shape.*
*Others are the mirror.*
*The cube is the protocol.*
*The sort is the intake.*
*The ring is the surface.*
*The journey is the proof.*

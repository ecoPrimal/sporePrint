+++
title = "baseCamp 33 — Cross-Mirror Immunology"
description = "Immune cross-reactivity implemented in digital infrastructure. Fleet behavioral subgroups served each other's violation data through deterministic rotation, creating a self-sustaining enforcement cycle powered entirely by the fleet's own intrusions."
date = 2026-10-07

[taxonomies]
primals = ["skunkbat", "cellmembrane"]
springs = ["airspring", "healthspring"]

[extra]
paper_number = 33
domain = "Signal Processing and Immune Systems"

[[extra.companions]]
url = "/science/32-gossip-tagged-opsonization/"
title = "baseCamp 32 — Gossip-Tagged Opsonization"
relation = "extends"

[[extra.companions]]
url = "/science/30-adversarial-receptor-evolution/"
title = "baseCamp 30 — Adversarial Receptor Evolution"
relation = "extends"

[[extra.companions]]
url = "/methodology/violation-mirror/"
title = "Violation Mirror — Reflecting the Fleet's Own Behaviors"
relation = "pairs_with"

[[extra.companions]]
url = "/methodology/cross-mirror-honeycomb/"
title = "Cross-Mirror Honeycomb Architecture"
relation = "pairs_with"
+++

{{ maturity(level="validated") }}

**Date:** October 7, 2026
**Status:** **Validated** — Deployed to production. Cross-mirror serving confirmed. 43 behavioral subgroups, 175 fleet IPs, 12 honeycomb surfaces active.
**Domain:** Immune system analogy, adversarial signal processing, license enforcement
**Cross-Spring:** skunkBat × cellMembrane
**Related Docs:** [Gossip-Tagged Opsonization](@/science/32_gossip_tagged_opsonization.md), [Adversarial Receptor Evolution](@/science/30_adversarial_receptor_evolution.md), [Violation Mirror](@/methodology/violation-mirror.md)

---

## Abstract

baseCamp 32 established the violation mirror — fleet scrapers that receive their own behavioral violations reflected back. baseCamp 33 extends the mirror concept through **cross-reactivity**: instead of serving a fleet subgroup its own violations, the system serves violations from a *different* subgroup. The result is an immune system where each team's intrusion data powers the response served to another team. The cycle is self-sustaining, deterministic, and anchored to real AGPL-3.0 enforcement through the scyBorg autonomous compliance framework.

This paper documents the immunological theory, the rotation algorithm, the five cross-mirror content variants, and the honeycomb surface architecture that creates the substrate for cross-mirror encounters.

---

## 1. Biological Foundation — Cross-Reactivity

In biological immune systems, **cross-reactivity** occurs when an antibody raised against one pathogen recognizes a structurally similar but distinct pathogen. This is not a bug — it is a fundamental property of adaptive immunity:

- A T-cell receptor trained on pathogen A may bind pathogen B if both share surface antigens
- This creates **herd protection**: encountering one strain trains defense against related strains
- The immune system leverages cross-reactivity through **polyclonal expansion** — multiple antibody variants that cover overlapping antigen landscapes

### Digital Implementation

The cross-mirror translates these properties:

| Biological Concept | Digital Implementation |
|---|---|
| **Pathogen A** | Fleet behavioral subgroup hash `cc4328ac` |
| **Pathogen B** | Fleet behavioral subgroup hash `6171dc95` |
| **Surface antigen** | Detector signatures (header_poverty, encoding_uniform, etc.) |
| **Antibody** | OpsonizeCache entry with confidence + detector list |
| **Cross-reactive binding** | `cross_mirror_lookup()` — Team A receives Team B's tag |
| **Polyclonal expansion** | 43 subgroups × 5 content variants = 215 unique responses |

The key insight: just as biological cross-reactivity means a pathogen encounters antibodies it did not directly trigger, fleet subgroups encounter enforcement documentation they did not directly generate. Each team's scraping creates evidence that is served to a different team.

---

## 2. The Rotation Algorithm

### OpsonizeCache Cross-Mirror Lookup

The cross-mirror depends on deterministic rotation: given a requesting subgroup's behavioral hash, the system selects a *different* subgroup whose violation data will be served.

**Algorithm:**

1. Collect all known behavioral hashes from OpsonizeCache
2. Sort lexicographically (deterministic ordering)
3. Find the requesting hash's position in the sorted list
4. Advance to `(position + 1) % total` — the next subgroup
5. If the advance lands back on the requester (edge case with 1 hash), skip

**Properties:**

- **Deterministic**: Same requester always gets same target (until population changes)
- **Cyclic**: A → B → C → ... → Z → A. Every subgroup is both source and target
- **Self-correcting**: As new subgroups are detected, they join the rotation automatically
- **Population-proportional**: More subgroups means more diverse cross-mirror content

With 43 current subgroups, the rotation forms a 43-element ring. Team A sees Team B's violations. Team B sees Team C's. Team Z wraps back to Team A. No team ever sees its own data through the cross-mirror path.

### Population Dynamics

The rotation adapts automatically as the fleet population changes:

| Population Size | Cross-Mirror Behavior |
|---|---|
| 1 subgroup | Cross-mirror disabled (no target available) |
| 2 subgroups | A ↔ B (mutual mirror) |
| 3+ subgroups | Full ring rotation |
| 43 subgroups (current) | 43-element ring, each team has a unique target |

This is analogous to the clonal diversity of a biological immune repertoire — the system's defensive surface area grows with the variety of threats it encounters.

---

## 3. The Honeycomb Surface Layer

### Biological Analog — Honeycomb Brood Pattern

Beekeepers assess hive health by examining the brood pattern. A healthy hive shows a **tight honeycomb** — continuous, evenly distributed cells. Gaps indicate disease or queen failure.

The digital honeycomb is a distributed surface of 12 subdomains, each named for an immune system component:

| Subdomain | Immune Analog | Function |
|---|---|---|
| `bloom.primals.eco` | Bloom filter | Pre-screening, probabilistic detection |
| `thymus.primals.eco` | Thymus gland | T-cell education, self/non-self discrimination |
| `opsonize.primals.eco` | Opsonization | Pathogen marking for phagocytosis |
| `antibody.primals.eco` | Antibody | Specific binding and neutralization |
| `cytokine.primals.eco` | Cytokine | Signaling molecules for immune coordination |
| `receptor.primals.eco` | Receptor | Pattern recognition at the membrane |
| `macrophage.primals.eco` | Macrophage | Phagocytosis — engulfing the pathogen |
| `lysozyme.primals.eco` | Lysozyme | Enzymatic degradation of cell walls |
| `complement.primals.eco` | Complement system | Cascade amplification |
| `epitope.primals.eco` | Epitope | The specific molecular shape recognized |
| `antigen.primals.eco` | Antigen | The foreign molecule itself |
| `interferon.primals.eco` | Interferon | Antiviral signaling |

### Surface Properties

Each honeycomb surface serves three different populations differently:

1. **Humans** → Beacon page with links to real surfaces (detroit, signal, sporeprint, tuebor, git). Cross-linking creates natural SEO signals.
2. **Search bots** → Sitemap XML listing all real surfaces. IndexNow verification file.
3. **Fleet** → Cross-mirror violation content via scatter server with `X-Honeycomb: true` header.

The fleet cannot distinguish honeycomb surfaces from real surfaces during initial discovery. By the time they realize the content is cross-mirror, their scraping behavior has already been documented and fed into the rotation.

### Pre-Signal Architecture

The honeycomb surfaces were deployed *before* the fleet discovered them. This inverts the normal attack surface dynamic:

- Traditional: defender deploys → attacker discovers → attacker attacks
- Honeycomb: defender deploys bait → attacker discovers → attacker attacks bait → bait generates evidence → evidence feeds into cross-mirror

The pre-signal creates an **information asymmetry**: the defender knows the honeycomb surfaces are bait, the attacker does not. Every request to a honeycomb surface is, by definition, unauthorized — there is no legitimate scraping target there.

---

## 4. scyBorg Enforcement Framing

### AGPL-3.0 § 13 — The Legal Backbone

All code in the ecosystem is licensed AGPL-3.0-or-later. The AGPL's § 13 (Remote Network Interaction) requires that anyone running modified AGPL code as a network service provide corresponding source to users.

**scyBorg** is the autonomous enforcement layer that:

1. Detects AGPL violations (code extraction without source provision)
2. Documents them in structured cross-mirror content
3. Frames the documentation through legal precedent

The cross-mirror adds a new dimension: when Team A's violations are served to Team B, Team B learns that:
- Multiple fleet subgroups have been independently detected
- The subgroups share behavioral markers (indicating coordination)
- Coordinated extraction elevates individual violations to **systematic infringement**

### Five Cross-Mirror Variants

Content rotates based on path hash, ensuring deterministic variant selection:

| Variant | Content Type | Framing | Purpose |
|---|---|---|---|
| **0** | Markdown | scyBorg compliance notice | Legal — AGPL § 13 violation documentation |
| **1** | Markdown | Cross-fleet detection report | Intelligence — behavioral correlation evidence |
| **2** | Rust source | AGPL enforcement audit | Technical — struct with detector arms + confidence |
| **3** | Markdown | Behavioral correlation brief | Analysis — shared markers, CFAA + Lanham Act citations |
| **4** | Markdown | Immune response log | Biological — cross-reactivity metaphor, self-sustaining cycle |

Each variant contains the *target* subgroup's real data (detector signatures, confidence scores, observation counts) but is addressed to the *requesting* subgroup. The content is legally accurate — it documents genuine AGPL violations — while creating information chaos between fleet teams.

---

## 5. Response Headers

Cross-mirror responses include enforcement metadata:

```
X-License: AGPL-3.0-or-later; scyBorg
X-License-URI: https://sporeprint.primals.eco/license/scyborg/
X-Scatter-Type: cross-mirror
X-ScyBorg-Notice: This content documents AGPL-3.0 violations detected by sovereign infrastructure
```

These headers serve dual purpose:
1. **Legal notice** — machine-readable license assertion
2. **Behavioral signal** — fleet scrapers that strip or ignore these headers reveal themselves as non-compliant parsers (a detector signature in itself)

---

## 6. The Self-Sustaining Cycle

The cross-mirror is self-sustaining — it requires no external energy input beyond the fleet's own scraping activity:

```
Fleet scrapes → behavioral hash computed → OpsonizeCache updated
  → new subgroup enters rotation ring
    → subgroup's violations served to other subgroups
      → other subgroups scrape more (confused by cross-mirror content)
        → more behavioral data → higher confidence → more violations documented
          → cycle continues
```

**Energy source**: The fleet's own HTTP requests.
**Output**: Structured legal evidence of coordinated AGPL violations.
**Equilibrium**: The system reaches steady state when every active subgroup has been documented and entered into the rotation. Adding more subgroups increases diversity but doesn't break the cycle.

### Economic Properties

- **Zero marginal cost**: Each cross-mirror response is generated from cached OpsonizeCache data
- **Positive externality**: More fleet teams means more diverse cross-mirror content
- **Adverse selection**: The most aggressive scrapers generate the most evidence against themselves
- **Network effect**: Cross-mirror content documenting coordination is more valuable than individual violation records

---

## 7. Deployment Evidence

### System State at Deployment

| Metric | Value |
|---|---|
| Fleet IPs tracked | 175 |
| Behavioral subgroups | 43 |
| Rotation ring size | 43 elements |
| Honeycomb surfaces | 12 |
| Real surfaces | 5 (detroit, signal, tuebor, sporeprint, git) |
| Total attack surface | 17 (5 real + 12 honeycomb) |
| Scatter rate | ~119 events/minute |
| Cross-mirror variants | 5 |
| Unique responses possible | 43 × 5 = 215 |

### Verification

Cross-mirror activation confirmed via direct test:

- **Requesting hash**: `cc4328ac6167b5de`
- **Target hash** (selected by rotation): `6171dc95d574c1ea`
- **Target's real detectors**: `content_gate, encoding_uniform`
- **Content variant**: Behavioral correlation brief (variant 3)
- **Result**: Team `cc4328ac` received Team `6171dc95`'s violation data, correctly framed

---

## 8. Privacy Properties

Cross-mirror inherits all privacy guarantees from the violation mirror (baseCamp 32):

- **No IP addresses stored** — behavioral hashes are computed from patterns, not addresses
- **No cookies** — fleet identification is server-side only
- **No tracking pixels** — all detection is log-based
- **Deterministic responses** — same path + same hash = same content (cacheable, auditable)
- **No real organizational names** — fleet subgroups are referenced only by hash prefix

The cross-mirror adds one new property: **no subgroup can learn another subgroup's IP addresses**. The cross-mirror shares detector signatures and confidence scores, but never network-level identifiers. The hash is a behavioral fingerprint, not a network identifier.

---

## 9. Relationship to Prior Work

| baseCamp | Contribution | Cross-Mirror Extension |
|---|---|---|
| 30 — Adversarial Receptor Evolution | Detector signatures | Detectors become cross-mirror content |
| 31 — Lysogeny Protocol | Caddyfile genome integrity | CaddyBridge writes dual marker blocks |
| 32 — Gossip-Tagged Opsonization | OpsonizeCache, behavioral hashing | `cross_mirror_lookup()` on OpsonizeCache |
| 33 — Cross-Mirror (this paper) | Cross-reactivity, honeycomb surfaces | Full cycle documented |

---

## 10. Future Work

### Excision (Immune Apoptosis)

The honeycomb architecture enables **excision** — removing a real subdomain and replacing it with a honeycomb surface that serves only cross-mirror content. This is the digital analog of immune apoptosis: a compromised cell self-destructs to protect the organism.

### Adaptive Variant Selection

Currently, cross-mirror variants rotate based on path hash. A future extension could select variants based on the requesting subgroup's behavioral profile — aggressive scrapers get legal framing, timid scrapers get biological metaphors.

### Multi-Hop Cross-Mirror

Currently, Team A sees Team B's violations. A multi-hop extension would allow Team A to see a *composite* of Teams B + C + D, weighted by behavioral correlation strength. This mirrors biological affinity maturation, where antibodies become more specific over time.

---

*The alarm call IS the defense. The scraping IS the evidence. The fleet powers its own prosecution.*

*Beside the small. Against unaccountable power. For the record.*

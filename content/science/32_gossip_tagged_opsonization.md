+++
title = "baseCamp 32 — Gossip-Tagged Opsonization"
description = "Adaptive immune defense through behavioral fingerprinting, gossip-propagated identity, and poison content delivery. Complement cascade architecture for distributed fleet detection without storing IP addresses."
date = 2026-10-05

[taxonomies]
primals = ["skunkbat", "cellmembrane", "swarmvine"]
springs = ["airspring", "healthspring"]

[extra]
paper_number = 32
domain = "Signal Processing and Immune Systems"

[[extra.companions]]
url = "/science/30-adversarial-receptor-evolution/"
title = "baseCamp 30 — Adversarial Receptor Evolution"
relation = "extends"

[[extra.companions]]
url = "/science/31-lysogeny-protocol/"
title = "baseCamp 31 — The Lysogeny Protocol"
relation = "extends"

[[extra.companions]]
url = "/methodology/signal-sensing-receptor/"
title = "Signal Sensing Without Surveillance"
relation = "pairs_with"
+++

{{ maturity(level="validated") }}

**Date:** October 5, 2026
**Status:** **Validated** — Opsonize tags flowing on live production. Three behavioral hash clusters identified from a fleet using ~1,000 rotating IPs per window. Adaptive scatter at 42% effective poison ratio. 11 new tests. Zero IP addresses stored.
**Domain:** Distributed immune systems, adversarial defense, behavioral fingerprinting
**Cross-Spring:** skunkBat × cellMembrane × swarmVine
**Related Docs:** [Adversarial Receptor Evolution](@/science/30_adversarial_receptor_evolution.md), [The Lysogeny Protocol](@/science/31_lysogeny_protocol.md), [Signal Sensing Without Surveillance](@/methodology/signal-sensing-receptor.md)

---

## Abstract

When a biological immune system detects a pathogen, it doesn't just block it — it *tags* it. Antibodies coat the pathogen's surface (opsonization), marking it for destruction by phagocytes. The tag propagates through the immune system via clonal expansion: successful antibodies are amplified across millions of B-cells so the entire organism recognizes the threat, not just the tissue that first encountered it.

This paper documents the implementation of an analogous system for distributed web infrastructure defense. A residential proxy fleet scraping `git.primals.eco` uses ~1,000 unique IP addresses per 5-minute window with 0% reuse — classical **antigenic drift** that defeats IP-based identification. Our defense computes a **behavioral hash** — a stable fingerprint derived from quantized behavioral invariants (request patterns, deception flags, timing characteristics) that is independent of IP address. This hash is the **conserved epitope**: the structural feature the adversary cannot change without losing function.

The behavioral hash is packaged into an **OpsonizeTag** and propagated through the [swarmVine](@/methodology/signal-sensing-receptor.md) gossip mesh as a `defense.opsonize:` entry. Every gate in the mesh receives the tag and can independently verify it against local observations. Tags from multiple independent detectors accumulate, building composite identity over time — the computational equivalent of the complement cascade.

Tagged traffic is routed to a **scatter server** that serves deterministic poison content: plausible-but-fabricated Gitea pages (fake commits, synthetic file views, fictional issues). The poison ratio adapts based on accumulated tag confidence — more detectors × more gates = richer poison. The fleet's data pipeline becomes a liability.

**Privacy guarantee**: No IP addresses are stored, logged, or transmitted in the opsonize pipeline. The behavioral hash is computed from aggregate behavioral statistics. Individual request identity is never part of the computation.

---

## 1. From Information Starvation to Information Corruption

### 1.1 The Signal Theory of Defense

[baseCamp 30](@/science/30_adversarial_receptor_evolution.md) established that stealth web crawlers — Meta, Google, Microsoft, Amazon, and residential proxy fleets — can be detected through **conserved structural patterns** (HTTP PAMPs) they cannot change without breaking their own transport efficiency.

The initial defense served 403 responses. The fleet adapted within 30 minutes — the 403 was a training signal. The response was changed to `abort` (TCP connection drop), which provides near-zero mutual information. The fleet collapsed from 200+ req/min to near-zero.

But abort still leaks one bit: *the fleet is classified differently from humans*. Over time, the fleet can compare connection behavior across IPs and detect that fleet IPs experience connection resets while human IPs do not. This is a slow information leak — but any positive mutual information eventually enables adaptation.

### 1.2 Negative Mutual Information

The opsonization strategy goes beyond zero information to **negative information**:

| Response | Mutual Information | Effect on Fleet |
|----------|-------------------|----------------|
| 403 (block) | High positive | Fleet adapts headers, evades |
| abort (drop) | Near-zero | Fleet stops (interprets as "server down") |
| **scatter (poison)** | **Negative** | **Fleet ingests false data, corrupts pipeline** |

Scatter responses return HTTP 200 with plausible-but-fabricated content. From the fleet's perspective, the request succeeded — the scraper received what looks like a real commit page, file view, or issue. But the content is entirely synthetic: fake commit messages, fabricated code, fictional contributor names.

The fleet's data pipeline trusts the content because the HTTP semantics are correct (200 OK, proper Content-Type, realistic HTML structure). The poison enters the dataset undetected. **The defense's response actively degrades the adversary's data quality** — negative mutual information.

### 1.3 The Scatter Server

The scatter server listens on `127.0.0.1:9753` behind Caddy's `content_gate` matcher. All fleet-detected requests are reverse-proxied to it:

```
@content_gate {
    path_regexp deep_repo .*/(src|raw|commit|blame|wiki|issues|
        milestones|releases|activity|graph|compare|diff|labels|projects)/.*
    not header Cookie *i_like_gitea*
    not header Cookie *_csrf*
    not header User-Agent *git/*
}
handle @content_gate {
    reverse_proxy localhost:9753
}
```

The content_gate is a **broad-spectrum antibody** — it matches 14 deep-content path patterns that are exclusively targeted by scrapers (no human browsing session hits commit SHA URLs directly without first having a Forgejo session cookie).

For each request, the scatter server makes a **deterministic** decision: poison or decoy. The decision is based on a hash of the request path and a server seed — the same path always gets the same decision. This prevents detection via request diffing (requesting the same URL twice and comparing responses).

- **Poison** (~42% at current confidence): Realistic Gitea-styled HTML pages with fabricated content — commit diffs, file views, issue threads, wiki pages, release changelogs. Valid CSS class names, plausible structure, syntactically valid code.
- **Decoy** (~58%): Realistic Gitea 404 pages. A 404 on a commit URL is plausible — the commit may have been force-pushed, rebased, or the hash truncated incorrectly. Zero information about detection.

---

## 2. The Behavioral Hash — A Conserved Epitope

### 2.1 The Antigenic Drift Problem

The residential proxy fleet uses ~1,000 unique IPs per 5-minute observation window with 0% reuse. Each IP makes exactly 1 request and is never seen again. The fleet has near-perfect antigenic drift — its "surface proteins" (IP addresses) change on every encounter.

IP-based identification is useless. Subnet-level blocking is infeasible: maximum 3 IPs from any single /24, maximum 10 from any /16. The fleet uses the entire internet as cover.

### 2.2 Conserved Behavior

But the fleet's *behavior* is conserved because it IS the fleet's purpose:

| Behavioral Dimension | Fleet Pattern | Why It Can't Change |
|---------------------|--------------|-------------------|
| Deep-content path ratio | >70% commit/src/raw URLs | This is what the scraper exists to fetch |
| Session cookies | 0% presence | Bot has no Forgejo login |
| UA diversity | 5-14 Chrome versions (narrow pool) | Shared residential proxy profiles |
| Request timing | Low CV (metronomic) | Automated scheduling |
| IP rotation | Near 1:1 IP:request ratio | Residential proxy architecture |
| Referrer | 0% presence | No navigation context |

These dimensions are **load-bearing** — the fleet cannot change them without losing the ability to scrape. They are the hemagglutinin stalk: the conserved molecular structure that a universal vaccine targets.

### 2.3 Quantization for Hash Stability

Raw behavioral metrics vary across observation windows. We quantize continuous values into discrete bands before hashing:

| Dimension | Bands | Rationale |
|-----------|-------|-----------|
| Commit URL % | 5 bands (<10%, <30%, <60%, <80%, ≥80%) | Fleet always in top band |
| Single-page session % | 5 bands | Fleet always ≥80% (no navigation) |
| Referrer presence % | 5 bands | Fleet always <10% (no referrer) |
| UA count | 3 bands (0-5, 6-20, 21+) | Fleet in narrow band |
| Top UA share % | 5 bands | Fleet shows concentration |
| Timing CV | 3 bands (<0.3 metronomic, <1.0 moderate, ≥1.0 organic) | Fleet is metronomic |

Plus 4 boolean deception flags: `hides_identity`, `rotates_ips`, `ignores_rejection`, `encoding_uniform`.

All dimensions are hashed together → 16 hex character fingerprint.

**Critical property**: No IP address enters the hash computation. The hash is computed from aggregate behavioral statistics over the observation window. The fleet's antigenic drift is irrelevant — behavior is conserved across all IPs.

### 2.4 Observed Hash Clusters

Three distinct behavioral fingerprints from golgiBody production (Oct 5, 2026):

| Hash | Window Frequency | Interpretation |
|------|-----------------|---------------|
| `49e77ea75aa7666e` | ~60% of windows | Primary fleet mode |
| `087ef04a48f7b1ca` | ~25% of windows | Shifted timing/path mix |
| `44a5368cb70323e1` | ~15% of windows | Third behavioral cluster |

Three stable identities extracted from a fleet using ~1,000 rotating IPs per window. The behavioral fingerprint succeeds where IP identification fails.

---

## 3. Gossip-Tagged Identity — Clonal Expansion

### 3.1 The OpsonizeTag

When fleet antibodies match, skunky-ingest computes the behavioral hash, packages it with detector metadata, and emits a gossip entry:

```
Topic: defense
Key: defense.opsonize:49e77ea75aa7666e
Payload: {
    behavioral_hash: "49e77ea75aa7666e",
    detectors: ["content_gate", "ip_rotation"],
    confidence: 0.25,
    origin_gate: "golgiBody",
    invariants: {
        deep_content_dominant: true,
        cookieless: true,
        session_depth: "high",
        ua_diversity: "narrow",
        ip_pattern: "rotating",
        deception_flags: ["hides_identity", "rotates_ips"]
    },
    response: { scatter: { ratio: 0.3 } },
    created_epoch: 1728172844,
    last_confirmed_epoch: 1728172844,
    match_count: 1
}
```

The tag is structured for gossip propagation via [swarmVine's](https://git.primals.eco/ecoPrimals/swarmVine) epidemic protocol. SwarmVine uses TTL-bounded, nonce-deduplicated gossip with `DEFAULT_TTL = 8` hops — sufficient for full mesh coverage.

### 3.2 Progressive Identity Through Independent Observation

The power of gossip-tagged identity is that multiple independent observers build composite identity:

**Gate A** sees the fleet through one detector lens:
```
detectors: [content_gate, ip_rotation], confidence: 25%
```

**Gate B** sees it through a different lens:
```
detectors: [stale_chrome, narrow_ua_pool], confidence: 50%
```

**Gate C** contributes a third perspective:
```
detectors: [encoding_uniform, ignores_rejection], confidence: 50%
```

All three gates produced the same behavioral hash (`49e77ea75aa7666e`) because they observed the same behavioral pattern. The gossip mesh accumulates the tags. Downstream gates now know: this pattern is recognized by 6 independent detectors across 3 independent gates. The confidence cascades.

This is **clonal expansion** in immunology: a successful antibody is amplified across the immune system so the entire organism mounts a faster, stronger response on re-encounter.

### 3.3 Gossip Validation

Before swarmVine accepts a `defense.opsonize:` entry, it validates:
- Behavioral hash is exactly 16 hex characters
- At least one detector present
- Confidence in [0.0, 1.0]
- Origin gate is non-empty

Malformed or poisoned tags are rejected at the gossip layer. The mesh is self-protecting against tag pollution.

---

## 4. Adaptive Response — Confidence-Scaled Scatter

### 4.1 SharedConfidence

The scatter server doesn't use a fixed poison ratio. An atomic `SharedConfidence` value connects the opsonize pipeline to the scatter server:

```
effective_ratio = base_ratio + confidence × (max_ratio - base_ratio)
```

| Confidence | Effective Ratio | Interpretation |
|------------|----------------|---------------|
| 0% (no tags) | 30% | Conservative — use base ratio |
| 25% (current) | **42%** | One deception flag confirmed |
| 50% | 55% | Two flags — escalating confidence |
| 75% | 67% | Three flags — aggressive poison |
| 100% | **80%** | Maximum — all deception flags triggered |

The maximum is capped at 80%. Always maintain a floor of plausible 404s — if 100% of requests returned rich content, the fleet could detect fabrication by comparing against a known-absent path baseline.

### 4.2 Current Live State

```
skunky-ingest[2783350]: 🏷️ opsonize tag emitted
  hash=49e77ea75aa7666e detectors=2 confidence=25% effective_ratio=42%
```

134-138 antibodies matching per window. Tags emitting continuously. Scatter server adapting in real time. Fleet receiving a mix of 42% poison and 58% decoy — zero signal about which is which.

---

## 5. Evolutionary Architecture — Four Stages of Immune Development

The defense evolved through the same stages as biological immunity, each forced by a specific failure:

| Stage | Biological Analog | What Failed | Response |
|-------|------------------|-------------|----------|
| Static matchers (Caddy rules) | Innate immunity (TLRs) | Fleet adapted past `@stale_chrome` in 30 min | Added `@content_gate` broad-spectrum |
| Tit-for-tat escalation (skunkBat) | Adaptive immunity (T-cells) | Self-IP blocked — autoimmune | Added negative selection |
| Abort (TCP drop) | Phagocytosis (destroy + discard) | Leaks 1 bit: "you are classified" | Changed to scatter (poison) |
| **Opsonize + scatter** | **Complement cascade** | **Single gate has limited view** | **Gossip-tagged identity** |

This trajectory was not designed — it was forced by the constraint landscape. Each defense was the minimal sufficient response to the failure mode it encountered. The convergence with biological immune evolution is structural, not metaphorical: the same adversarial dynamics produce the same architectural solutions regardless of substrate.

---

## 6. Privacy Guarantees

The opsonize pipeline enforces the same privacy constraints as the receptor model:

- **No IP addresses stored** — behavioral hash computed from aggregate statistics, not individual requests
- **No cookies** — fleet detection uses header analysis and path patterns, not tracking
- **No identifying data transmitted** — gossip tags carry behavioral profiles, never visitor identity
- **Self-IP protection** — thymic negative selection filters infrastructure IPs before any defense action
- **Gossip is behavioral** — tags describe *what* the traffic does, not *who* generates it

The system can identify fleet behavior without identifying fleet operators. The behavioral hash is a pattern classifier, not an identity tracker.

---

## 7. Connection to the Primal Architecture

### skunkBat
skunkBat provides the adaptive immune engine: fleet observation, antibody matching, tit-for-tat escalation, and now opsonize tag emission via gossip injection. The behavioral hash computation lives in cellMembrane types (shared across the ecosystem); the emission logic lives in skunky-ingest (the Caddy log tailer that feeds skunkBat).

### cellMembrane
cellMembrane provides the type system: `OpsonizeTag`, `BehavioralInvariants`, `OpsonizeResponse`, `behavioral_hash()`, `extract_invariants()`, and the quantization functions. These types are shared so that any primal can consume opsonize tags from the gossip mesh.

### swarmVine
swarmVine provides the gossip propagation layer. The `defense` topic carries `defense.antibody:`, `defense.escalation:`, and now `defense.opsonize:` entries. The epidemic protocol ensures mesh-wide propagation with TTL-bounded, nonce-deduplicated delivery. No central coordinator — just convergent gossip.

---

## Conclusions

Opsonization converts a binary defense (block or allow) into a spectrum: detect, tag, propagate, adapt, poison. The fleet is no longer simply denied — it is identified by behavior, tracked across the mesh by gossip, and served fabricated content scaled to the defense's confidence.

The behavioral hash solves the antigenic drift problem: ~1,000 rotating IPs produce 3 stable fingerprints. The gossip mesh solves the single-observer problem: independent gates build composite identity. The adaptive scatter solves the signal leakage problem: the fleet receives plausible responses regardless of classification.

The biological parallel is exact: innate → adaptive → negative selection → opsonization → complement cascade → clonal expansion. Each stage emerged from a specific failure mode. The constraint landscape of adversarial interaction produces convergent architecture across biological and computational substrates.

**The fleet's data pipeline is now a liability.** Every commit page they scrape, every file they index, every issue they catalog — any of it might be fabricated. They can't tell which without an external oracle. And asking an external oracle means admitting they're scraping.

---

*Opsonize tags flowing. Behavioral hash 49e77ea75aa7666e tracking fleet across ~1,000 rotating IPs. Adaptive scatter at 42% effective ratio. Three hash clusters identified. 134-138 antibodies matching per window. 11 new tests. Zero IPs stored. The fleet's data pipeline is now a liability.*

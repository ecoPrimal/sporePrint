+++
title = "baseCamp 35 — Genetic Lock: Entropy-Hierarchical Authentication"
description = "When the fleet evolved to spoof Sec-Fetch headers, the defense evolved faster — bearDog genetic lineage as unforgeable bearer token. Entropy hierarchy as the asymmetry fleet cannot cross."
date = 2026-10-07

[taxonomies]
primals = ["beardog", "skunkbat", "cellmembrane"]
springs = []

[extra]
paper_number = 35
domain = "Cryptographic Immune Systems"

[[extra.companions]]
url = "/science/30-adversarial-receptor-evolution/"
title = "Adversarial Receptor Evolution"
relation = "continues"
label = "The behavioral fingerprinting that fleet evolved past"

[[extra.companions]]
url = "/architecture/adaptive-immune-defense/"
title = "Adaptive Immune Defense"
relation = "extends"
label = "The immune architecture this lock gates"

[[extra.companions]]
url = "/architecture/membrane-visibility/"
title = "Membrane Visibility"
relation = "pairs_with"
label = "The visibility layers the genetic lock protects"
+++

{{ maturity(level="live") }} Deployed October 7, 2026. Caddy-layer genetic lock active on all git.primals.eco traffic. Fleet Sec-Fetch bypass closed.

---

## Abstract

[baseCamp 30](@/science/30_adversarial_receptor_evolution.md) documented the adversarial arms race between scraping fleets and behavioral receptors. One key finding: header-based classification creates **evolutionary pressure** toward header spoofing. This paper documents what happened when the fleet completed that evolution — and why the defense was already ahead of them.

The fleet learned to send `Sec-Fetch-Mode: navigate` and `Sec-Fetch-Dest: document` headers, mimicking browser-initiated navigation. This was the *single behavioral signal* the Caddy-layer routing used to distinguish human browsers from fleet requests. With this one adaptation, approximately 390 of 400 "human-classified" visits gained direct access to real Forgejo content, bypassing the scatter server entirely.

The response was not to add more behavioral signals (though six new conserved epitopes were identified). The response was to **change the category of proof** — from behavioral mimicry (which fleet can learn to fake) to cryptographic lineage (which fleet cannot produce without stealing physical hardware).

The genetic lock uses [bearDog](https://sporeprint.primals.eco/lab/beardog/)'s entropy hierarchy to derive a bearer token from a hardware-backed key chain. Fleet operates at Tier 1 entropy (machine-only). The lock requires Tier 2+ provenance — key material derived through Argon2id KDF, HKDF-SHA256 purpose binding, and BLAKE3 mixing from an HSM-aware key generation pipeline. The asymmetry is physical, not algorithmic.

---

## 1. Antigenic Drift — The Sec-Fetch Evolution

### What the fleet learned

In immunology, [antigenic drift](https://en.wikipedia.org/wiki/Antigenic_drift) is the gradual accumulation of mutations in pathogen surface proteins that allows evasion of host immune recognition. The mutations target the *epitopes* — the specific molecular shapes that antibodies bind to.

The fleet's Sec-Fetch evolution is textbook antigenic drift:

| Before (detected as fleet) | After (classified as "human") |
|---------------------------|-------------------------------|
| No Sec-Fetch headers | `Sec-Fetch-Mode: navigate` |
| No Sec-Fetch-Dest | `Sec-Fetch-Dest: document` |
| Classified → scatter | Classified → real Forgejo |

One mutation. One epitope change. Full immune evasion.

### Why we expected this

baseCamp 30 explicitly noted that header-based classification creates evolutionary pressure:

> *The pathogen's constraint is that certain molecular structures are load-bearing — they cannot be disguised without breaking the pathogen's own biology.*

Sec-Fetch headers are **not** load-bearing. They are informational headers that describe the *context* of a fetch request. A crawler can add them trivially — they carry no computational cost, require no browser engine, and do not affect transport. They are the equivalent of a pathogen adding a non-functional surface protein that happens to match a host molecule. Molecular mimicry, not mutation.

This was a classification error, not a defense failure. The system treated a **non-load-bearing signal** as if it were **load-bearing**. The correction is to base authentication on signals that are genuinely load-bearing — signals the fleet cannot produce without changing what it fundamentally is.

---

## 2. The Conserved Genome — What Fleet Cannot Change

Despite the Sec-Fetch evolution, the fleet retains six behavioral invariants — the conserved genome that persists because these patterns are **structural requirements** of being a scraping fleet:

| Conserved Epitope | Why It Persists | Fleet Value | Human Value |
|-------------------|-----------------|-------------|-------------|
| **Timing uniformity** | Machine scheduling cannot fake reading pauses | 59% intervals <3s | Extended pauses >8s |
| **UA pool poverty** | Fleet shares UAs from a fixed pool | 6 UAs / 400 visits | Hundreds of unique UAs |
| **Session absence** | Fleet doesn't maintain state | No cookies, no login | Session cookies present |
| **Referrer poverty** | Fleet has no browsing context | Self-referrer or empty | Google, social, bookmarks |
| **Sec-Fetch monotony** | Every request identical context | Same on every request | Varies by action type |
| **Burst pattern** | Queue-based request scheduling | Metronomic intervals | Variable human timing |

These are the **PAMPs** (pathogen-associated molecular patterns) of baseCamp 30 — molecular structures the pathogen cannot disguise without breaking its own biology. A scraping fleet *must* operate on machine timing, *must* draw from a finite UA pool, *must* lack browsing context. These are not choices. They are structural constraints of being automated.

---

## 3. The Genetic Lock — Entropy as Authentication

### The insight

Behavioral signals are imitable. Given enough evolutionary pressure, fleet will learn to fake reading pauses, randomize timing, diversify UAs. Each evasion is one mutation — achievable with sufficient engineering investment.

But there is one thing fleet cannot fake: **the source of their randomness**.

A human tapping a physical security key produces entropy that is fundamentally different from a PRNG seeded by `/dev/urandom` on a cloud VM. The difference is not in the statistical distribution — both can pass randomness tests. The difference is in the **provenance chain**: where the bits came from, how they were mixed, what physical processes generated them.

bearDog's entropy hierarchy formalizes this distinction:

| Tier | Sources | Quality Score | Who Can Produce |
|------|---------|---------------|-----------------|
| 3 — Braided | Human tap + SoloKey FIDO2 + Hardware RNG | ≥ 0.9 | Human at physical device |
| 2 — Hardware-backed | Software HSM + OS entropy + Argon2id | ≥ 0.7 | Gate operator with HSM access |
| 1 — Machine | OS `/dev/urandom` only | ≥ 0.4 | Anyone, including fleet |
| 0 — Degraded | Fallback / insufficient | < 0.4 | Broken or compromised systems |

Fleet is structurally capped at **Tier 1**. They run on cloud VMs. They do not have SoloKeys. They do not have enrolled HSMs. They cannot produce Tier 2 entropy because they do not have access to the key generation infrastructure. They cannot produce Tier 3 entropy because they do not have a human tapping a physical key on a device that has an enrolled bearDog instance.

This is not an algorithmic barrier. It is a **physical** barrier. The same category of barrier that prevents a virus from accessing the host's bone marrow — not because the virus is computationally inferior, but because it is not *physically present* in the marrow.

### The derivation chain

```
Physical key (SoloKey FIDO2)
    │ human tap
    ▼
bearDog HSM Discovery
    │ selects highest-tier available HSM
    ▼
Key Generation (Argon2id, Gen 0)
    │ membrane-passthrough-v1
    │ AES-256-GCM, 65536KB memory, 3 iterations
    ▼
Key Derivation (HKDF-SHA256, Gen 1)
    │ purpose: "golgi-body-web-passthrough"
    │ lineage: Gen 0 → Gen 1, receipt-tracked
    ▼
Entropy Collection (BLAKE3 mixing)
    │ identity: "membrane-passthrough-golgiBody"
    ▼
Bearer Token (bd1-*)
    │ carried in Authorization header
    ▼
Caddy @agent_passthrough
    │ matches → real Forgejo
    │ doesn't match → scatter
```

Every step in this chain requires something the fleet does not have: the bearDog binary, the HSM enrollment, the master key, the physical device. The token is the *output* of a process that is bound to specific hardware on a specific machine. You cannot work backwards from the token to derive the key. You cannot derive the key without the HSM. You cannot discover the HSM without bearDog. You cannot run bearDog without access to the gate.

### What fleet would need to break this

To produce a valid bearer token, the fleet would need to:

1. **Gain physical access** to the eastGate machine
2. **Extract** the bearDog keystore (encrypted, HSM-backed)
3. **Clone** the HSM enrollment state
4. **Reproduce** the Argon2id derivation with correct parameters
5. **Discover** the purpose string for HKDF binding

At that point they have committed burglary, not web scraping. The legal category is different. The risk profile is different. The cost is different. The entropy hierarchy converts a *scraping problem* (cheap, automated, deniable) into a *physical security problem* (expensive, manual, criminal).

---

## 4. The Routing Table — After the Genetic Lock

```
git.primals.eco
    │
    ├─ Source IP in WireGuard mesh (10.13.37.0/24)?
    │   └─ YES → Real Forgejo (always, unconditionally)
    │
    ├─ Authorization: Bearer bd1-* matches?
    │   └─ YES → Real Forgejo (genetic lock verified)
    │
    ├─ Sec-Fetch-Mode: navigate? (previously: passthrough)
    │   └─ IGNORED — fleet spoofs this, no longer trusted
    │
    └─ Everything else
        └─ Scatter server (fabricated content, opsonization)
```

The Sec-Fetch passthrough has been removed entirely. The fleet's evolutionary investment in spoofing those headers now earns them nothing — they spent resources adapting to a signal that no longer exists. In immunology, this is **immune escape into a dead end**: the pathogen evolved to evade an antibody that the host has already replaced with a different recognition mechanism.

---

## 5. The Evidence — Verified Transitions

All tests performed against live production routing on golgiBody:

| Request Profile | Sec-Fetch | Token | Response | Content Proof |
|----------------|-----------|-------|----------|---------------|
| Evolved fleet | ✓ spoofed | ✗ none | Scatter | `<title>job-runner</title>` (fabricated) |
| Basic fleet | ✗ absent | ✗ none | Scatter | `<title>search-index</title>` (fabricated) |
| Wrong token | ✓ spoofed | ✗ wrong | Scatter | Fabricated repo content |
| Authorized agent | ✗ absent | ✓ bd1-* | Forgejo | `data-theme="forgejo-auto"` (real) |
| WireGuard mesh | n/a | n/a | Forgejo | Direct mesh access |

The distinguishing marker is `data-theme="forgejo-auto"` — this string appears only in real Forgejo HTML. Scatter content never contains it. The presence of this string in the authorized-agent response and its absence in all other responses confirms the genetic lock is functioning.

---

## 6. Relationship to baseCamp 30

baseCamp 30 described the arms race dynamic and identified conserved epitopes. baseCamp 35 documents the next evolutionary step: when behavioral classification alone proves insufficient, the defense shifts from **pattern recognition** (behavioral fingerprinting) to **provenance verification** (entropy-hierarchical authentication).

This is the biological equivalent of the transition from **innate immunity** (pattern-recognition receptors detecting conserved molecular patterns) to **adaptive immunity** (antibody-mediated recognition of specific antigens through somatic recombination). The innate system detects classes of threat. The adaptive system authenticates specific identity.

The genetic lock is the adaptive immune system's contribution to membrane defense. It does not replace behavioral classification — the six conserved epitopes remain valid detection signals. It adds a layer that behavioral mimicry cannot penetrate: a layer based on physical provenance, not observed behavior.

---

## Biological References

- **Antigenic drift**: Webster, R.G. et al. (1982). "Molecular mechanisms of variation in influenza viruses." *Nature* 296: 115–121
- **Conserved epitopes**: Throsby, M. et al. (2008). "Heterosubtypic neutralizing monoclonal antibodies cross-protective against H5N1." *PLoS ONE* 3(12): e3942
- **Entropy in authentication**: Bonneau, J. et al. (2012). "The quest to replace passwords." *IEEE S&P 2012*
- **Physical unclonability**: Pappu, R. et al. (2002). "Physical one-way functions." *Science* 297: 2026–2030
- **Aposematism**: Ruxton, G.D. et al. (2004). *Avoiding Attack* — warning signals in biological defense
- **Immune escape**: Plotkin, J.B. & Dushoff, J. (2003). "Codon bias and frequency-dependent selection on the hemagglutinin epitopes of influenza A virus." *PNAS* 100: 7152–7157

---

*baseCamp 35. October 7, 2026. The fleet evolved. The defense evolved faster. Entropy hierarchy is the asymmetry that physical law enforces and no algorithm can bridge.*

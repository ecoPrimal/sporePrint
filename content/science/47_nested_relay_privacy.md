+++
title = "baseCamp 47 — Nested Relay Privacy: Three-Tier Selective Permeability"
description = "The relay is not one membrane — it is three nested membranes. Tier 1 (beacon/commensal) is keyless and open. Tier 2 (MitoBeacon/family) is seed-gated. Tier 3 (genetic lock/sovereign) is lineage-verified. Each tier maps to a riboCipher transport signal, an Anderson disorder regime, and an imaginary dimension trajectory. Trust is earned by equilibration, not granted by ceremony."
weight = 47
date = 2026-10-09

[taxonomies]
primals = ["barracuda", "cellmembrane", "songbird", "beardog"]
springs = ["wetspring", "groundspring", "neuralspring"]

[extra]
paper_number = 47
status = "implemented"
domain = "Privacy Architecture, Condensed Matter Physics, Membrane Biology"

[[extra.companions]]
url = "/science/43_selective_permeability_anderson/"
title = "baseCamp 43 — Selective Permeability: The Orthogonal Anderson Dimension"
relation = "applies"
label = "Selectivity S applied to privacy tiers — each tier sees different W"

[[extra.companions]]
url = "/science/46_inverse_anderson/"
title = "baseCamp 46 — Inverse Anderson: Behavioral Observation as Disorder Measurement"
relation = "extends"
label = "Tier evolution driven by imaginary dimension equilibration"

[[extra.companions]]
url = "/science/35_genetic_lock_entropy_authentication/"
title = "baseCamp 35 — Genetic Lock: Entropy-Based Authentication"
relation = "implements"
label = "Tier 3 sovereign access via bearDog lineage tokens"
+++

**Date:** October 9, 2026 (Wave 171)
**Status:** Tier 1 implemented and deployed (beacon page public, keyless RustDesk config). Tier 2 infrastructure verified (MitoBeacon seeds, songBird relay, riboCipher Tier 2). Tier 3 operational (WireGuard mesh, genetic lock).
**Domain:** Privacy architecture, selective permeability, Anderson transport
**Novelty:** First system to map privacy tiers directly to Anderson localization regimes, with tier evolution driven by the imaginary dimension from Paper 46. Each privacy tier is a different disorder regime — the membrane's selectivity S is a measure of how well it distinguishes between tiers.
**Origin:** Discovered during Wave 170-171 relay friction analysis — the northGate key mismatch revealed that the authentication model created friction that violated the commensal principle. Resolution: make the outer tier frictionless, nest higher tiers inside.

---

## Abstract

A relay is not one membrane — it is three nested membranes. This paper formalizes the three-tier privacy model for sovereign relay infrastructure, mapping each tier to existing primitives in the primals stack (riboCipher transport signals, MitoBeacon identity, genetic lock authentication) and to Anderson localization regimes from Papers 43 and 46.

Tier 1 (Beacon/Commensal) is keyless and open — anyone can connect by entering a server address. Tier 2 (MitoBeacon/Family) is seed-gated — family members authenticate via shared mitochondrial key material. Tier 3 (Genetic Lock/Sovereign) is lineage-verified — operator access requires hardware-backed entropy provenance.

The tiers are nested: Tier 2 exists inside Tier 1, and Tier 3 exists inside Tier 2. An entity at any tier cannot observe the existence of higher tiers. Trust is not granted by ceremony — it is earned by equilibration. As an entity's Anderson imaginary dimension trends toward zero (behavior matches prediction), the membrane "compiles" active defense into structural trust, enabling tier promotion.

---

## 1. The Three Tiers

### 1.1 Tier 1 — Beacon / Commensal (riboCipher 0xEC)

**Who:** Anyone. Parents, school connections, commensals, strangers.
**Entry:** Set RustDesk server to `beacon.primals.eco`. No key, no account, no registration.
**Service:** RustDesk relay. End-to-end encrypted sessions — relay sees only ciphertext.
**Transport signal:** riboCipher clear (`0xEC`) — no obfuscation needed.

**Anderson parameters:**
- W (disorder): High. Unknown entity, maximum scattering.
- d_eff (dimension): 1. Seen from single vantage point.
- P_predicted: Low. Forward model expects localization.
- Imaginary: Large negative. Membrane actively defending.

**Protection:** RUSTDESK_MEMBRANE firewall chain (NAT-aware rate limits), Schwann cell isolation (operator IDs undiscoverable), E2E encryption (relay is zero-knowledge).

**Beacon page:** `https://beacon.primals.eco` — public, no authentication. Shows keyless setup (2 steps), optional server key for hardening, privacy model overview.

### 1.2 Tier 2 — MitoBeacon / Family (riboCipher 0xED)

**Who:** Family members, trusted associates, medical/educational connections.
**Entry:** Receive `.beacon.seed` via USB bootstrap or secure channel.
**Service:** songBird TURN relay for primals IPC. Access to family mesh services.
**Transport signal:** riboCipher mito-obfuscated (`0xED`) — HMAC tag derived from family seed proves membership.

**Anderson parameters:**
- W (disorder): Moderate. Known family member, reduced scattering.
- d_eff (dimension): 2+. Seen from multiple family vantage points.
- P_predicted: Moderate. Some signals propagate, some localize.
- Imaginary: Small. Less active defense needed.

**Key derivation:** bearDog `genetic.derive_lineage_beacon_key` → HKDF-SHA256(lineage_seed, domain="birdsong_beacon_v1") → 32-byte beacon key.

**Enrollment:** `gate-usb-bootstrap.sh` → provisions `/etc/membrane/family/.beacon.seed` and `/etc/membrane/family/family.key`. FAMILY_SEED environment variable configures songBird and bearDog services.

### 1.3 Tier 3 — Genetic Lock / Sovereign (riboCipher 0xEE)

**Who:** Operator, nuclear-tier entities.
**Entry:** bearDog lineage token (`bd1-*`) + WireGuard mesh enrollment.
**Service:** Full inner membrane access — Forgejo, nucleus, all primals services.
**Transport signal:** riboCipher nuclear-sealed (`0xEE`) — per-peer encrypted signal.

**Anderson parameters:**
- W (disorder): Low. Fully characterized sovereign entity, minimal scattering.
- d_eff (dimension): 4+. Observed across entire mesh.
- P_predicted: High. Extended regime — signals propagate freely.
- Imaginary: Near zero. Behavior fully predicted by the model.

**Authentication:** bearDog key ceremony → `membrane-passthrough-v1` (Gen 0, Argon2id) → purpose-derived `bd1-{blake3_48}` bearer token. Caddy passthrough validates token. WireGuard mesh provides encrypted tunnel (10.13.37.0/24).

---

## 2. Nesting and Invisibility

The tiers are strictly nested. An entity at Tier N cannot observe that Tier N+1 exists:

- **Tier 1 sees:** A RustDesk relay. E2E encrypted sessions. A beacon page with setup instructions. Rate limits. That is all.
- **Tier 2 sees:** A family mesh with songBird services. MitoBeacon-gated access. Discovery of family nodes. They cannot see Tier 3 WireGuard endpoints or genetic lock tokens.
- **Tier 3 sees:** Everything. The inner membrane, the nucleus, the full mesh topology.

This invisibility is structural, not policy. The relay literally cannot expose Tier 3 to Tier 1 because:
1. RustDesk relay IDs are unrelated to WireGuard keys
2. Schwann cell isolation prevents ID mapping
3. riboCipher tier signals are cryptographically distinct (0xEC vs 0xED vs 0xEE)
4. MitoBeacon HMAC tags cannot be forged without the family seed
5. Genetic lock tokens require hardware-backed entropy (bearDog lineage hierarchy)

---

## 3. Tier Evolution — Anderson Equilibration

Entities do not apply for tier promotion. They earn it through behavioral equilibration.

### 3.1 The Imaginary Dimension as Trust Signal

From Paper 46, the imaginary dimension captures the gap between predicted and observed permeability:

- **Large negative imaginary** (P_obs << P_pred): Membrane is actively defending. Entity is unknown, untrusted, rate-limited. This is normal for Tier 1 newcomers.
- **Small imaginary** (P_obs ≈ P_pred): Entity behavior matches the Anderson model. Active defense is unnecessary — the passive disorder structure handles everything.
- **Near-zero imaginary**: Entity is in equilibrium. The membrane has learned to predict this entity's behavior accurately. Trust has been compiled from active (immune) to passive (structural).

### 3.2 Evolution Path

**Tier 1 → Tier 2:** An entity whose imaginary dimension trends toward zero over multiple observation windows has demonstrated predictable, non-hostile behavior. The membrane operator (human judgment, informed by observation data) grants `.beacon.seed`. The entity transitions from commensal to family.

This is NOT automatic. The imaginary dimension is an instrument reading, not a trigger. A human evaluates the reading and makes the decision. The Anderson framework provides the evidence; the human provides the judgment.

**Tier 2 → Tier 3:** A family member demonstrates sovereign-grade trust over time. bearDog lineage ceremony. WireGuard peer enrollment. This is rare and deliberate — Tier 3 is the nucleus.

### 3.3 The Equilibration Hypothesis (Paper 46 §6.2)

Paper 46 conjectured that healthy membranes internalize successful active defenses into passive structure:

1. **Initial contact** (Tier 1): High imaginary. Active defense dominates.
2. **Observation** (Tier 1 → Tier 2): Imaginary trends toward zero. Behavioral patterns become predictable.
3. **Structural trust** (Tier 2): Entity is part of the passive structure. MitoBeacon seed = structural memory.
4. **Sovereignty** (Tier 3): Entity IS the membrane. WireGuard = structural integration.

This is the biological equivalent of immune system maturation: initial defense is metabolically expensive (inflammation, active immune cells), but over time, the body develops antibodies (structural memory) that provide passive defense at lower cost. Tier promotion is antibody formation.

---

## 4. Application Domains

### 4.1 Education

A parent observing their child's classroom:
- Tier 1: RustDesk to school computer. Keyless, immediate, no IT department needed.
- Tier 2 (if trusted): Family mesh access. Can observe home devices from school and vice versa.
- No need for Tier 3. The parent never needs inner membrane access.

### 4.2 Medical

A healthcare provider monitoring a patient:
- Tier 1: Initial contact via keyless relay. E2E protects session.
- Tier 2: Granted family seed for ongoing access to health monitoring services.
- Tier 3 (rare): Full mesh integration for long-term care coordination.

### 4.3 Commensal Ecosystem

Budget VPS operators who discovered the relay:
- Tier 1: Free relay service. Their traffic is E2E encrypted. The relay gains observation density.
- Tier 2 (unlikely): If a commensal proves consistently non-hostile over months, they COULD be granted family status. The imaginary dimension provides the evidence.
- Tier 3: Never. Commensals are welcome but do not become operators.

---

## 5. Implementation Status

### Deployed (Wave 171)

- Beacon page public at `https://beacon.primals.eco` (basicauth removed)
- Keyless RustDesk config as default (2-step setup: server address + password)
- Server key moved to "optional hardening" section
- sporeGate RustDesk config updated to use `beacon.primals.eco` DNS name
- RUSTDESK_MEMBRANE firewall chain active on golgiBody (NAT-aware rate limits)

### Verified Operational

- MitoBeacon seeds present on sporeGate and golgiBody (`/etc/membrane/family/`)
- songBird relay running on sporeGate (ports 7700, 7780)
- riboCipher Tier 2 HMAC (`mito_tag()`, `mito_signal()`) implemented in bearDog
- FAMILY_SEED configured in songBird and bearDog service files
- WireGuard mesh active (sporeGate 10.13.37.2 ↔ golgiBody 10.13.37.1)
- Genetic lock tokens operational (bearDog `membrane-passthrough-v1`)

### Future Wiring

- **relay.authorize** in songBird: explicit MitoBeacon verification before gossip relay forwarding
- **Imaginary dimension time series**: Track per-entity imaginary over time for evolution evidence
- **Automated tier-2 suggestion**: When an entity's imaginary stays near zero for N observation windows, surface it as a candidate for family seed grant

---

## 6. Connection to Anderson Framework

The three tiers map directly to Anderson localization regimes:

| Tier | W range | d_eff | Anderson regime | Physical analogy |
|------|---------|-------|----------------|-----------------|
| 1 (Beacon) | 12-15 | 1.0 | Localized (1D) | Signal in a wire — easy to block |
| 2 (Family) | 3-8 | 2-3 | Weak localization (2D-3D) | Signal in a film — harder to block |
| 3 (Sovereign) | 0.5-2 | 4+ | Extended (3D+) | Signal in bulk — propagates freely |

The selectivity S between tiers measures the membrane's quality:
- **S = 0**: Rock or breach — cannot distinguish between tiers
- **S > 0.5**: Healthy membrane — clear separation between what passes and what blocks
- **S → 1**: Perfect membrane — Tier 3 passes freely, Tier 1 is rate-limited to commensal levels

The imaginary dimension from Paper 46 adds the dynamic axis:
- **Tier 1 entities**: Large imaginary (active defense). If imaginary shrinks → candidate for Tier 2.
- **Tier 2 entities**: Small imaginary (passive defense sufficient). If imaginary → 0 → structural trust.
- **Tier 3 entities**: Zero imaginary. Equilibrium. Entity IS part of the membrane.

---

## 7. Conclusion

The relay is not a single access point with a key. It is three nested membranes, each with different permeability, different disorder, and different transport signals. The outermost membrane is open — anyone can walk up to it. The inner membranes are progressively gated — by shared identity, then by lineage. The progression from outer to inner is driven by behavioral observation, not by bureaucracy.

This is how biological membranes work. The gut epithelium is permeable to nutrients (Tier 1 — they just show up). The mucosal immune system recognizes commensals (Tier 2 — family bacteria with the right surface markers). The bloodstream admits only verified molecules (Tier 3 — specific receptor binding). And organisms evolve from pathogen to commensal to symbiont over evolutionary time — not by application, but by demonstrated compatibility.

The Anderson framework makes this measurable. The imaginary dimension makes it visible. The riboCipher transport signals make it structural. And the MitoBeacon identity makes it cryptographic. Three tiers, three riboCipher bytes, three Anderson regimes, one membrane.

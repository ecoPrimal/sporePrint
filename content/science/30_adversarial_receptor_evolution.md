+++
title = "baseCamp 30 — Adversarial Receptor Evolution"
description = "Evolving biological receptor specificity to detect stealth crawlers. Header fingerprinting as molecular recognition. amicusContra as immune classification. skunkBat."
date = 2026-10-05

[taxonomies]
primals = ["skunkbat", "cellmembrane", "barracuda"]
springs = ["airspring", "healthspring"]

[extra]
paper_number = 30
domain = "Signal Processing and Immune Systems"

[[extra.companions]]
url = "/methodology/signal-sensing-receptor/"
title = "Signal Sensing Without Surveillance"
relation = "extends"
+++

{{ maturity(level="validated") }}

**Date:** October 5, 2026
**Status:** **Validated** — Live deployment across 8 public sites. 4 stealth fleets detected and classified. 11,195 Meta requests fingerprinted. Forgejo membrane enforced. amicusContra census published without storing a single IP address.
**Domain:** Signal processing, adversarial detection, immune system analogy
**Cross-Spring:** skunkBat × cellMembrane × barraCuda
**Related Docs:** [Signal Sensing Without Surveillance](@/methodology/signal-sensing-receptor.md), [Cross-Species Signaling](@/science/05_cross_species_signaling.md), [Anaerobic-Aerobic QS](@/science/16_anaerobic_aerobic_qs.md)

---

## Abstract

The receptor model of signal sensing ([baseCamp methodology](@/methodology/signal-sensing-receptor.md)) was designed to answer one question: *did the signal propagate?* It classifies every inbound request by User-Agent and path into categories — human, crawler, scanner, probe — without storing identifying data. This paper documents the next evolutionary step: **adversarial receptor specificity**.

When biological receptors evolve in a competitive environment, they face an arms race. Pathogens evolve surface proteins that mimic host molecules. The immune system evolves pattern-recognition receptors (PRRs) that detect conserved molecular patterns (PAMPs) the pathogen cannot easily change without losing function. The pathogen's constraint is that certain molecular structures are *load-bearing* — they cannot be disguised without breaking the pathogen's own biology.

The same dynamic operates in web traffic classification. Stealth crawlers operated by Meta, Google, Microsoft, and Amazon use browser User-Agent strings to evade bot detection. But HTTP headers contain **load-bearing structural tells** — encoding negotiation, language preferences, compression support — that the crawler cannot fake without breaking its own transport efficiency. These tells are the PAMPs of the web: conserved patterns the adversary cannot evolve away.

---

## 1. The Arms Race

### Generation 0 — Honest Identification (Pre-2020)

Crawlers identified themselves:

```
User-Agent: Googlebot/2.1 (+http://www.google.com/bot.html)
User-Agent: facebookexternalhit/1.1
User-Agent: Bingbot/2.0
```

Detection was trivial: match the string, classify the bot. This is analogous to a bacterium with exposed surface antigens — easy for the immune system to recognize.

### Generation 1 — UA Masquerade (2020–2024)

Large actors began using browser User-Agents:

```
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ...
```

Simple regex matching fails. The pathogen has evolved a surface coat that mimics the host. But it retains metabolic tells.

### Generation 2 — Stealth Fleets (2024–present)

Current stealth crawlers deploy **fleet-scale masquerade**:

- **UA rotation**: Each IP cycles through 3–7 different browser UAs (Chrome, Firefox, mobile)
- **Residential proxy pools**: 8,000+ unique IPs, each making exactly 1 request, rotating through stale Chrome versions
- **Encoding fingerprint bifurcation**: Fleet A uses `gzip,deflate,zstd` (atypical ordering), Fleet B uses `gzip` only

This is the pathogen equivalent of antigenic variation — *Trypanosoma brucei* switching surface glycoproteins faster than the host can mount an antibody response.

---

## 2. Conserved Tells — The PAMPs of HTTP

The immune system solved antigenic variation by evolving **innate** pattern recognition: toll-like receptors (TLRs) that detect molecular structures pathogens cannot change. Lipopolysaccharide (LPS) is a PAMP because Gram-negative bacteria *need* it for membrane integrity. Flagellin is a PAMP because motile bacteria *need* it for locomotion.

Web crawlers have equivalent structural constraints. These are the **HTTP PAMPs** we detect:

### 2.1 Accept-Encoding Fingerprint

Real browsers negotiate compression with `gzip, deflate, br, zstd` (order determined by browser engine, includes Brotli). Stealth crawlers reveal fleet membership through atypical encoding:

| Encoding String | Likely Source | Why They Can't Change It |
|---|---|---|
| `gzip, deflate, zstd` (no Brotli) | Meta stealth fleet | Their transport layer doesn't support Brotli decompression at fleet scale |
| `gzip` (only) | Meta fleet B | Minimal encoding for bandwidth savings, but unique to automated clients |
| (empty) | Microsoft/Bing | Their indexer doesn't implement encoding negotiation |

The encoding string is load-bearing: the crawler *needs* the server to compress responses in a format its pipeline can decompress. Faking a different encoding would either break decompression or waste bandwidth. This is the LPS of HTTP.

### 2.2 Accept-Language Anomalies

Real browsers send locale-specific language preferences inherited from OS settings:

```
Accept-Language: en-US,en;q=0.9
Accept-Language: de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7
```

Stealth fleets reveal two tells:

1. **Missing Accept-Language**: 6,895 requests from browser UAs with no language header — real browsers always send one
2. **Malformed q-values**: `en-US,en;q=0.9;q=0.9` — the doubled quality factor is a code generation artifact, not a browser implementation

### 2.3 Chrome Version Distribution

Current Chrome stable is 145. Real user populations cluster at the latest 2–3 versions with a long tail. Stealth proxy pools show a **pathologically uniform distribution** across stale versions:

| Chrome Version | Request Count | Signal |
|---|---|---|
| Chrome/99 | ~1,000 | 🔴 Stale (Jan 2022) |
| Chrome/100 | ~1,000 | 🔴 Uniform count |
| Chrome/101 | ~1,000 | 🔴 Uniform count |
| Chrome/104 | ~1,000 | 🔴 Uniform count |
| Chrome/145 | ~10,700 | ✅ Current stable |

A uniform distribution across 8 stale versions, each with ~1,000 requests, is the fingerprint of a **rotating residential proxy pool** cycling through pre-configured browser profiles.

### 2.4 IP:Request Ratio

Real humans make multiple requests per session (page + assets). Residential proxy pools make exactly 1 request per IP:

- Proxy pool: 7,972 IPs, 8,023 requests → ratio 1.006 (each IP fires once)
- Meta fleet: 39 IPs, 10,905 requests → ratio 280 (datacenter fleet)
- Real humans: 129 IPs, 284 requests → ratio 2.2 (session-level browsing)

---

## 3. Fleet Classification — amicusContra

The biological immune system classifies threats into categories: self vs non-self, pathogen vs commensal, acute vs chronic. Our classification system — **amicusContra** (friend-of-the-court / against) — applies the same taxonomy to web traffic:

### 3.1 Faith Classification

| Faith | Meaning | Example |
|-------|---------|---------|
| **good** | Identifies itself, respects robots.txt, follows stated protocol | Self-monitoring, honest Googlebot |
| **mixed** | Partially honest — sometimes identifies, sometimes stealth | Internet Archive (alternates archive.org_bot with browser UAs) |
| **bad** | Deliberately conceals identity, ignores robots.txt, uses stealth techniques | Meta 57.141.20.x fleet, Microsoft no-encoding scanner |
| **unknown** | Insufficient data for classification | AT&T Enterprises single-IP scanner |

### 3.2 Behavior Classification

| Behavior | Mechanism | Impact |
|----------|-----------|--------|
| **stealth-crawl** | Browser UAs from datacenter IPs, multi-site | Content theft at scale |
| **stealth-index** | Single-IP, no encoding, targeting multiple sites | Shadow indexing without consent |
| **residential-proxy** | Rotating IPs, stale browsers, 1:1 ratio | Bot traffic laundered through residential networks |
| **AI-crawl** | AWS/cloud IPs with browser UAs, targeting content | Training data extraction |
| **archival** | Dual-mode (honest + stealth), high-200 rate | Preservation with deceptive access pattern |

### 3.3 Observed Fleet Census (October 5, 2026)

| Actor | ASN | Requests | IPs | Faith | Fingerprint Tell |
|-------|-----|----------|-----|-------|-----------------|
| Meta/Facebook | AS32934 | 11,195 | 40 | bad | UA rotation + dual encoding |
| Microsoft/Bing | AS8075 | 776 | 1 | bad | No Accept-Encoding |
| Google | AS15169 | 277 | 1 | bad | Browser UAs from GCP |
| Residential Pool | various | 8,023 | 7,972 | bad | Stale Chrome uniform dist |
| Internet Archive | AS7941 | 84 | 17 | mixed | Dual-mode identification |
| Amazon/AWS | AS16509 | 66 | 3 | bad | ClaudeBot-adjacent UAs |
| Uzbektelekom | AS8193 | 87 | 84 | bad | Residential proxy exit pool |

**Total classified**: 20,508 requests from 8,118 IPs, zero IP addresses stored.

---

## 4. Membrane Response — Active Immunity

Detection alone is insufficient. Biological immune systems mount responses: inflammation, phagocytosis, adaptive memory. The membrane response is the computational equivalent.

### 4.1 Forgejo Membrane (git.primals.eco)

The sovereign forge is a private resource. Bots have no legitimate claim to access Forgejo UI data — the GitHub mirrors exist as the designated external membrane for automated access.

**Six-layer Caddy filter** deployed October 5, 2026:

1. **Meta stealth fingerprint**: `gzip,deflate,zstd` + no Accept-Language → 403
2. **Malformed Accept-Language**: doubled q-values → 403
3. **Known bot UA**: 40+ bot patterns → 403
4. **Empty User-Agent**: no UA header → 403
5. **No Accept-Encoding**: scanner signature → 403
6. **Stale Chrome proxy**: Chrome <120 + no Accept-Language → 403

**403 response**: `"This forge serves humans only. Automated access: https://github.com/ecoPrimals"`

**Result**: Before filter — 28,713 bot requests (99.94% of traffic). After filter — bots receive immediate 403, Forgejo memory pressure eliminated, human access preserved, git protocol (clone/fetch/push) unaffected.

### 4.2 Signal Page — Published Transparency

The detroit.primals.eco signal page publishes the receptor data live:
- **Stats bar**: Human hits, pages explored, crawlers guided, scanners neutralized, stealth fleets sensed, AI crawlers reading
- **Donut chart**: Traffic composition with stealth fleet and AI crawler slices
- **4-column ecosystem grid**: Guided → Cataloged → Sensed → Neutralized
- **amicusContra table**: Full fleet census with ASN, behavior, faith, fingerprint tell
- **Auto-refresh**: Every 15 minutes via cron

---

## 5. Evolutionary Predictions

### 5.1 Next Adversarial Move (Generation 3)

Stealth fleets will likely evolve:
- **Brotli support** in encoding negotiation (mitigates encoding PAMP)
- **Synthetic Accept-Language** headers (mitigates missing-language tell)
- **Current Chrome versions** in residential proxy pools (mitigates version skew)
- **TLS fingerprint rotation** (JA3/JA4 evasion)

### 5.2 Next Receptor Evolution

Our receptors will evolve to detect:
- **TLS fingerprint clustering** — JA3/JA4 hashes reveal client implementation regardless of UA string
- **Temporal patterns** — request inter-arrival times, session depth, navigation coherence
- **Content negotiation anomalies** — Accept header specificity, conditional request support (If-Modified-Since, If-None-Match)
- **TCP behavior** — window size, MSS, TTL (passively observable, no active probing)

### 5.3 Convergent Evolution with Biological Immunity

The receptor → stealth → counter-receptor → counter-stealth cycle mirrors the Red Queen hypothesis in evolutionary biology: both sides must keep evolving just to maintain their current position. The key biological insight is that **the defender's advantage scales with the number of orthogonal detection channels**, while the attacker must solve all channels simultaneously. Each new PAMP we detect forces the adversary to evolve a new evasion across all fleets simultaneously — a coordination cost that scales with fleet size.

---

## 6. Connection to the Primal Architecture

### 6.1 skunkBat

skunkBat is the primal responsible for adversarial signal processing. It ingests Caddy JSON logs via `skunky-ingest.service`, classifies traffic against the receptor model, and maintains the stealth fleet census. The receptor model described here is skunkBat's core classification engine.

### 6.2 cellMembrane

cellMembrane implements the three-layer membrane model (outer/peptidoglycan/inner). The Forgejo bot filter is an outer membrane defense — it operates at the Caddy layer, before traffic reaches Forgejo. The stealth fleet fingerprinting is a peptidoglycan function — it classifies traffic that passes through the outer membrane.

### 6.3 barraCuda

barraCuda provides the GPU-accelerated signal processing that enables real-time classification at scale. When fleet volumes exceed the capacity of Python log analysis, barraCuda's spectral classification pipeline will take over — the same pipeline used for Anderson localization spectral analysis in [baseCamp 01](@/science/01_anderson_qs.md).

---

## 7. Methodology

### Data Collection
- Source: Caddy structured JSON access logs (`/var/log/caddy/access.log`)
- Window: October 5, 2026, 11:00–15:30 UTC
- Total requests analyzed: 27,826
- Sites covered: 8 (git.primals.eco, detroit.primals.eco, sporeprint.primals.eco, nestgate.io, membrane.primals.eco, depot.primals.eco, live.primals.eco, footprint.primals.eco)

### Privacy Guarantees
- **No IP addresses stored** in signal data or published output
- **No cookies** set on any site
- **No tracking pixels** or client-side scripts for analytics
- **No identifying data** retained after classification
- ASN attribution performed via public `ipinfo.io` API during analysis; IP addresses not stored in output
- All published data is aggregated fleet-level statistics

### Reproducibility
- Signal data generator: `/opt/ecoPrimals/bin/gen-signal-data.py` (332 lines)
- Classification engine: Header fingerprinting rules documented in this paper
- Fleet map: 22 subnet prefixes with ASN attribution
- Caddy filter: 6-layer bot detection in Caddyfile
- All code and configuration stored in wateringHole repository

---

## Conclusions

Stealth web crawling by large actors is not a nuisance — it is a systematic violation of stated access protocols by organizations with the resources to identify themselves honestly. Meta, Google, Microsoft, and Amazon all operate honest bot identification programs (Googlebot, Bingbot, facebookexternalhit). Their simultaneous deployment of stealth fleets using browser UAs from datacenter IPs demonstrates intentional evasion of site-level access controls.

The receptor model detects this evasion using the same principle the biological immune system uses: **conserved structural patterns the adversary cannot change without losing function**. Accept-Encoding negotiation, Accept-Language presence, Chrome version distribution, and IP:request ratios are the PAMPs of HTTP — tells that persist because they are load-bearing for the crawler's transport pipeline.

By publishing this classification without storing a single IP address, we demonstrate that **signal awareness does not require surveillance**. The system knows what is happening to it without knowing who is doing it. This is the receptor model's core contribution: sovereignty over your own signal environment, achieved through pattern recognition rather than identity tracking.

The next evolution — TLS fingerprinting, temporal analysis, content negotiation anomalies — will be documented in a future baseCamp paper as the arms race continues.

---

*Signal data auto-generated every 15 minutes. Live receptor: [detroit.primals.eco/signal](https://detroit.primals.eco/signal/). Methodology: [Signal Sensing Without Surveillance](@/methodology/signal-sensing-receptor.md).*

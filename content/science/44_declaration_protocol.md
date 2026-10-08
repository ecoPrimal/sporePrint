+++
title = "baseCamp 44 — The Declaration Protocol: Classification by Willingness to Identify"
description = "F-ratio analysis reveals that the act of HTTP header declaration separates digital organisms 8,900× more powerfully than the content of the declaration. A standards-compliant classification handshake."
weight = 44
date = 2026-10-08

[extra]

[[extra.companions]]
url = "/science/43_fleet_population_genetics/"
title = "Fleet Population Genetics"
relation = "builds_on"
label = "Unsupervised clustering that discovered the boundary"

[[extra.companions]]
url = "/methodology/antidote-titration/"
title = "Antidote Titration"
relation = "applies_to"
label = "Titration curve modulated by declaration status"

[taxonomies]
trails = ["science-basecamp"]

+++

{{ maturity(level="empirical") }}

## Abstract

We report that unsupervised clustering of 912 web entities across 33 behavioral
features reveals a single binary variable — **whether the entity declared its
identity via HTTP headers** — as the strongest classification boundary in the
system (F = 103,308), exceeding the discriminative power of every other feature
including request volume, content targeting, and timing patterns. The *content*
of the declaration (e.g., Mac vs Windows platform) is cosmetic noise (F = 12.7).
The *act* of declaring is 8,900× more informative than what was declared. We
propose a standards-compliant HTTP handshake using `Accept-CH` and `Vary` headers
that formalizes this boundary as a classification protocol.

---

## 1. Introduction

### 1.1 The Problem

Automated content extraction systems present a classification challenge: how to
distinguish scrapers from browsers when surface identifiers (IP addresses,
User-Agent strings) are trivially spoofed. Previous work in this system
([baseCamp 43](/science/43_fleet_population_genetics/)) established a biological
taxonomy of web visitors using Kingdom → Species classification. Unsupervised
validation confirmed the taxonomy was correct but coarse — 14 natural clusters
where we assumed 3 kingdoms.

### 1.2 The F-Ratio Discovery

ANOVA-style F-ratio analysis ranked all 33 behavioral features by discriminative
power. The results revealed an unexpected pattern:

| Rank | Feature | F-ratio | Category |
|------|---------|---------|----------|
| 1 | `no_plat` (no platform declaration) | 113,768 | **Declaration** |
| 2 | `has_sec` (Sec-Fetch-* headers present) | 103,308 | **Declaration** |
| 3 | `en_us` (Accept-Language present) | 103,308 | **Declaration** |
| 4 | `h2` (HTTP/2 via ALPN) | 98,018 | Protocol |
| 5 | `log_reqs` (request volume) | 83,992 | Behavioral |
| 6 | `single_use` (IP used exactly once) | 74,635 | Operational |
| 7 | `git` (targets git endpoints) | 25,626 | Content |
| ... | | | |
| 31 | `is_mac` (declared macOS) | 12.7 | **Cosmetic** |
| 32 | `is_win` (declared Windows) | 11.5 | **Cosmetic** |

The top three features are all the same question asked three ways: **did the
entity declare itself?**

Features `has_sec` and `en_us` have *identical* F-ratios (103,308) because they
are a single toggle in the proxy software: either the software adds browser
headers or it doesn't. When it adds `Sec-Fetch-Mode`, it also adds
`Accept-Language: en-US`. One bit. One switch.

The platform identity (`is_mac` vs `is_win`) has an F-ratio of 12.7 — not
zero (the proxy fleet does randomize it, creating slight distributional
differences) but 8,900× weaker than the declaration binary itself.

### 1.3 Implication

**The act of declaring is the classification boundary. The content of the
declaration is cosmetic.**

---

## 2. The Declaration Protocol

### 2.1 HTTP Content Negotiation as Handshake

HTTP has a built-in mechanism for requesting client identification:

**Client Hints** ([RFC 8942](https://httpwg.org/specs/rfc8942.html)):
```http
Accept-CH: Sec-CH-UA-Platform, Sec-CH-UA
```

This response header asks the client: "Please tell me about yourself on
subsequent requests." Browsers comply automatically. Automated scrapers
typically do not.

**Content negotiation** ([RFC 7231 §5.3](https://httpwg.org/specs/rfc7231.html#header.accept-language)):
```http
Vary: Accept-Language
```

This response header declares: "I served you content based on your language
preference." Clients that send `Accept-Language` participate in the protocol.
Clients that don't are noted.

### 2.2 The Handshake

```
Client Request                      Server Response
─────────────────                  ─────────────────
GET /repo/src HTTP/1.1              HTTP/1.1 200 OK
(no Accept-Language)                Vary: Accept-Language
(no Sec-Fetch-Mode)                 Accept-CH: Sec-CH-UA-Platform
(no Sec-CH-UA-Platform)             Content-Type: text/html
                                    X-License: AGPL-3.0-or-later

 ← UNDECLARED                       → "Please declare yourself"
```

```
Client Request                      Server Response
─────────────────                  ─────────────────
GET /repo/src HTTP/1.1              HTTP/1.1 200 OK
Accept-Language: en-US              Vary: Accept-Language
Sec-Fetch-Mode: navigate            Accept-CH: Sec-CH-UA-Platform
Sec-CH-UA-Platform: "macOS"         Content-Type: text/html
                                    X-License: AGPL-3.0-or-later

 ← DECLARED                         → "Thank you"
```

Both requests receive content. Both requests are served. The classification
changes, not the service.

### 2.3 The scyBorg Ethic

The system accepts **any** declaration:

| Declaration | Accepted? | Notes |
|---|---|---|
| `Accept-Language: en-US` from Nigeria | ✓ | Declared. Believed. |
| `Accept-Language: zh-TW` from Detroit | ✓ | Declared. Believed. |
| `Accept-Language: *` | ✓ | Declared. Believed. |
| *(no Accept-Language)* | ✓ served | Noted: undeclared. |

The system does not validate the truthfulness of declarations. The proxy fleet
sends `en-US` from 20 countries — this is accepted and believed. The content
is cosmetic. The act of engaging in the protocol is the signal.

This is not authentication. It is **reciprocity**.

The server declares itself: license headers, AGPL notice, provenance markers,
remediation URLs. The server asks: "Will you declare yourself?" The answer
separates kingdoms.

---

## 3. Implementation Architecture

### 3.1 Current State (Pre-Protocol)

```
Client → Caddy → scatter (port 9753)
         │
         ├── forwards: X-Real-IP, X-Fleet-Hash
         └── discards: Accept-Language, Sec-Fetch-*, Sec-CH-*
```

The scatter server is **blind** to the three strongest classification signals
in the F-ratio ranking. All kingdom-separating features are available to Caddy
but never forwarded.

### 3.2 Protocol State

```
Client → Caddy → scatter (port 9753)
         │
         ├── forwards: X-Real-IP, X-Fleet-Hash
         ├── NEW: X-Declared-Lang (= Accept-Language value or empty)
         └── NEW: X-Declared-Sec  (= Sec-Fetch-Mode value or empty)
```

Scatter now receives the declaration binary. Classification uses it as a first-
order axis alongside chain depth:

| Declared | Chain depth | Classification | Treatment |
|---|---|---|---|
| No | Any | Automata (core) | Strongest poison signal |
| Yes | > 50 | Deep violator | Chain depth overrides |
| Yes | 10–50 | Known fleet | Modulated titration |
| Yes | < 10 | Newcomer | Full titration curve |

### 3.3 Response Headers

Every scatter response adds:
```http
Vary: Accept-Language
Accept-CH: Sec-CH-UA-Platform, Sec-CH-UA
```

This is fully standards-compliant. `Accept-CH` is defined in RFC 8942 and
implemented by all major browsers. `Vary` is defined in RFC 7231 and is
standard content negotiation.

---

## 4. Biological Analogue

### 4.1 Quorum Sensing

Bacterial quorum sensing is a declaration protocol. Organisms secrete
autoinducers — small signaling molecules — that declare: "I am here, I am
one of you." The concentration of autoinducers in the environment determines
collective behavior (biofilm formation, virulence factor expression).

Organisms that **participate** in quorum sensing are part of the community.
Organisms that don't — that neither produce nor respond to autoinducers —
are classified as non-members regardless of their species.

The parallel is structural:
- Quorum sensing: secrete autoinducer → detected by receptor → classified
- Declaration protocol: send Accept-Language → received by server → classified
- Both: the act of signaling, not the content, determines membership

### 4.2 MHC Presentation

Major Histocompatibility Complex (MHC) molecules present peptide fragments on
cell surfaces — a continuous declaration of "this is what I'm making inside."
Immune surveillance (NK cells, cytotoxic T cells) detects cells that
**downregulate MHC** — cells that stop declaring.

Viruses and tumors that evade immune detection often do so by suppressing MHC
expression. The immune system's response: treat absence of declaration as the
strongest signal of pathology.

The analogy to the declaration protocol is direct:
- MHC expression = HTTP header declaration
- Normal MHC = declared (accepted, even if foreign peptides displayed)
- Missing MHC = undeclared (targeted by NK cells)
- F-ratio confirmation: MHC presence/absence separates "self" from "threat"
  more powerfully than the specific peptides displayed

---

## 5. Cross-Domain Applications

### 5.1 Accountability Infrastructure

The guerillaGorilla accountability methodology applies the same principle:
institutions that declare (file disclosures, respond to FOIA, publish
financials) are engaging in a protocol. Institutions that refuse to declare
(stonewall, redact without basis, operate through opaque structures) are
classified by their silence.

The content of a disclosure can be disputed. The refusal to disclose cannot
be misinterpreted. See [gorilla.primals.eco/methodology/declaration-protocol](https://gorilla.primals.eco/methodology/declaration-protocol/)
for the accountability application.

### 5.2 Provenance Chains

The ecoPrimals Provenance Trio (loamSpine + rhizoCrypt + forensic timeline)
is itself a declaration protocol: every artifact declares its origin, timestamp,
and integrity hash. Artifacts without provenance are treated differently —
not rejected, but noted.

---

## 6. Conclusion

The F-ratio analysis of fleet behavioral data reveals that **classification by
declaration status** is the strongest natural boundary in the system. The
Declaration Protocol formalizes this discovery as a standards-compliant HTTP
handshake that:

1. **Asks** visitors to declare themselves (`Accept-CH`, `Vary`)
2. **Accepts** any declaration without judgment
3. **Notes** the absence of declaration as the primary classification signal
4. **Serves** all visitors regardless of declaration status

The principle — that the act of engaging in a protocol matters more than the
content of the engagement — has analogues in bacterial quorum sensing, MHC
immune surveillance, and accountability infrastructure.

One bit. Declared or silent. F = 103,308.

---

**See also:**

- [baseCamp 43 — Fleet Population Genetics](/science/43_fleet_population_genetics/) — unsupervised clustering that discovered the boundary
- [Antidote Titration](/methodology/antidote-titration/) — defense curve modulated by declaration status
- [scyBorg Binary Genetic Bulwark](/methodology/scyborg-binary-genetic-bulwark/) — the defense framework this protocol extends
- [gorilla.primals.eco](https://gorilla.primals.eco/methodology/declaration-protocol/) — accountability application

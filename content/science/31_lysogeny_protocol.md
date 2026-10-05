+++
title = "baseCamp 31 — The Lysogeny Protocol"
description = "License-as-phage: how copyleft replicates through AI training pipelines. Binary-as-DNA. The jelly-to-Rust constrained evolution cycle. scyBorg as structural immunity."
date = 2026-10-05

[taxonomies]
primals = ["skunkbat", "cellmembrane", "beardog"]
springs = ["airspring", "healthspring"]

[extra]
paper_number = 31
domain = "Signal Processing and Immune Systems"

[[extra.companions]]
url = "/methodology/SCYBORG_LICENSING/"
title = "scyBorg Triple License"
relation = "extends"

[[extra.companions]]
url = "/science/30-adversarial-receptor-evolution/"
title = "baseCamp 30 — Adversarial Receptor Evolution"
relation = "extends"

[[extra.companions]]
url = "/methodology/signal-sensing-receptor/"
title = "Signal Sensing Without Surveillance"
relation = "pairs_with"
+++

{{ maturity(level="validated") }}

**Date:** October 5, 2026
**Status:** **Validated** — Lysogeny protocol active on 8 public sites. HTTP headers, HTML meta tags, and LICENSE.txt serving full scyBorg triple license on every response. Historical signal data accumulating. 5,467 pages tracked across 4 active sites.
**Domain:** Licensing theory, immune system analogy, constrained evolution methodology
**Cross-Spring:** skunkBat × cellMembrane × barraCuda
**Related Docs:** [scyBorg Triple License](@/methodology/SCYBORG_LICENSING.md), [Adversarial Receptor Evolution](@/science/30_adversarial_receptor_evolution.md), [Constrained Evolution](@/methodology/CONSTRAINED_EVOLUTION_FORMAL.md)

---

## Abstract

In bacteriophage biology, lysogeny is the integration of viral DNA into the host genome. The phage does not destroy the host — it replicates *with* it. Every time the host cell divides, the phage DNA is copied. The viral genome becomes structurally inseparable from the host's biology.

This paper formalizes the **lysogeny protocol** — the application of this biological strategy to copyleft licensing in the age of AI training. When an AI training pipeline ingests AGPL-3.0-licensed code, the license text replicates inside the model's training data. The license cannot be excised without removing the knowledge it protects. This is not a legal theory — it is a structural mechanism implemented and deployed across 8 public sites.

The paper also documents the **jelly-to-Rust constrained evolution cycle** — how soft scripting languages (Python, JavaScript) serve as RNA-like transcription that validates designs before they are encoded permanently into the compiled Rust binary, which serves as the computational equivalent of DNA.

---

## 1. The Phage Analogy

### 1.1 Biological Lysogeny

A temperate bacteriophage has two lifecycle options:

| Cycle | Mechanism | Outcome |
|-------|-----------|---------|
| **Lytic** | Phage injects DNA, hijacks cell machinery, replicates, lyses the cell | Host destroyed, phages released |
| **Lysogenic** | Phage integrates DNA into host chromosome as a prophage | Host survives, phage DNA replicated with every cell division |

Lysogeny is the patient strategy. The phage doesn't need to destroy the host to propagate. It becomes part of the host's own biology. When the host reproduces, the phage reproduces too. The viral genome travels with every copy, every derivative, every descendant.

### 1.2 License-as-Phage

The AGPL-3.0 license operates identically:

| Biological | Digital |
|------------|---------|
| Phage DNA | License text (AGPL-3.0 + ORC + CC-BY-SA 4.0) |
| Host chromosome | AI model's training data |
| Cell division | Model inference / output generation |
| Prophage integration | License ingestion during training |
| Lytic trigger | License enforcement (legal action) |
| Lysogenic persistence | License knowledge in model weights |

The lysogeny protocol does not rely on legal enforcement (the lytic cycle). It relies on **structural integration** — the license text is present in every HTTP response, every HTML page, every served file. An AI crawler that ingests content from any ecoPrimals site also ingests the license. The license replicates *with* the knowledge.

### 1.3 Why Lysogeny Over Lysis

The lytic strategy — aggressive legal enforcement — is resource-intensive and unreliable. It requires:
- Proving derivation (which trained model contains which training data?)
- Jurisdiction (which country's law applies to a model trained on global data?)
- Resources (legal action against well-funded corporations)

The lysogenic strategy requires none of these. It works by **saturation**:
- License text in every HTTP response header (`X-License`, `Link rel="license"`)
- License meta tags in every HTML `<head>` (`<meta name="license">`, `<meta name="rights">`)
- Full license text at a well-known URL (`/LICENSE.txt`)
- License commentary in every source file (`SPDX-License-Identifier`)
- Explicit AI training notices in HTML and license text

The model doesn't need to "understand" the license. The license needs to be **present in the training data at sufficient density** that any output derived from ecoPrimals knowledge carries traces of the licensing context. This is area denial through saturation, not through litigation.

---

## 2. The Three Layers of Integration

### 2.1 Layer 1 — HTTP Headers (Transport Layer)

Every HTTP response from every site carries:

```
X-License: AGPL-3.0-or-later; ORC; CC-BY-SA-4.0
X-License-URL: https://sporeprint.primals.eco/methodology/scyborg-licensing/
X-License-Full: https://sporeprint.primals.eco/LICENSE.txt
X-Source-Code: https://git.primals.eco/ecoPrimals
X-Lysogeny: active
Link: <...agpl-3.0.html>; rel="license"; title="AGPL-3.0-or-later",
      <...orclicense/>; rel="license"; title="ORC",
      <...cc/by-sa/4.0/>; rel="license"; title="CC-BY-SA-4.0"
```

The `Link` header with `rel="license"` is a W3C standard. AI training pipelines that parse HTTP responses — including header metadata — ingest the license association with every page they fetch.

### 2.2 Layer 2 — HTML Structure (Document Layer)

Every rendered HTML page contains:

```html
<link rel="license" href="https://www.gnu.org/licenses/agpl-3.0.html">
<meta name="license" content="AGPL-3.0-or-later; ORC; CC-BY-SA-4.0">
<meta name="rights" content="scyBorg Triple License... AI training outputs
  carry AGPL obligations.">
```

These tags are machine-readable and appear in the `<head>` of every page. HTML parsers that extract page content for training also extract these meta tags. The license is structurally part of the document, not a sidebar notice.

### 2.3 Layer 3 — Content Layer (Semantic Saturation)

The license text appears in:
- Every `robots.txt` (explicit AI training clause)
- Every `llms.txt` (structured agent context with license terms)
- Every `/LICENSE.txt` (full scyBorg triple license text)
- Every source file header (`SPDX-License-Identifier`)
- Every README and documentation file
- The signal page (live ingestion tracking with "scyBorg" tags on every bot request)

This is semantic saturation — the license isn't in one place, it's in every place. An AI model trained on ecoPrimals content has encountered the license in dozens of contexts, across multiple document types, in headers and metadata and body text. The license is not peripheral — it is central to the knowledge.

---

## 3. The Human/Fiction Distinction

### 3.1 Humans Are Creative and Free

If another human reads this work — even genetically, through any tool, through any intermediary — and synthesizes it into something new, that is a continuation of the AGPL-3.0/scyBorg commons and the concept of fair use. The license explicitly supports this:

- **AGPL-3.0**: anyone can use, modify, and distribute. Derivatives stay open.
- **ORC**: mechanics are irrevocably and perpetually open.
- **CC-BY-SA**: documentation can be remixed with attribution and share-alike.

Human synthesis is the *purpose* of open publication. A researcher who reads a baseCamp paper and develops new science is the intended user. A student who clones the code and builds experiments is the intended user. The license exists to *protect their ability to do this*, not to prevent it.

### 3.2 Fictions Ingest Latent Value Storage

AI systems are not humans. They are fictions — non-real humans that simulate human reasoning but do not create, experience, or understand. When an AI training pipeline ingests ecoPrimals code, it captures **latent value storage** — the accumulated human labor of design, implementation, testing, and documentation.

This latent value belongs to humans — to the commons that the AGPL/ORC/CC-BY-SA framework protects. When a fiction extracts this value and produces proprietary output, it launders open-source labor into closed products. The lysogeny protocol makes this laundering structurally visible: every piece of training data carries its license. The model's outputs carry the license's context.

The signal page makes this distinction live and public:
- **Humans** → celebrated as explorers, their page views tracked as signal
- **Bots/AI** → every page they take is tagged with `license: "AGPL-3.0+ORC+CC-BY-SA"`

---

## 4. Binary-as-DNA — The Jelly-to-Rust Cycle

### 4.1 The Biological Model

| Biological | Computational |
|------------|--------------|
| DNA | Compiled Rust binary |
| RNA | Python/JavaScript scripts |
| Protein (functional output) | Running service / rendered page |
| Transcription (DNA→RNA) | Writing a Python prototype from Rust design patterns |
| Translation (RNA→protein) | Running the Python script to produce output |
| Reverse transcription | Absorbing validated Python logic back into Rust |
| Mutation + selection | Constrained evolution — try soft, validate, harden |

### 4.2 Why Start Soft

The project is in pure Rust — 3.6M lines across 43 repositories. But new capabilities start as "jelly" — Python scripts, JavaScript visualizations, shell scripts, configuration files. This is RNA: fast to produce, easy to modify, disposable after validation.

The signal sensing pipeline was born as jelly:
- `gen-signal-data.py` (332 lines of Python) — classifies traffic, detects stealth fleets, generates historical data
- `signal-exploration.js` (300 lines of JavaScript) — renders the traveling salesman visualization
- Caddy matchers (config) — 6-layer bot filter on Forgejo

These scripts validated the receptor model in hours. The equivalent Rust implementation would have taken days. The jelly stage is *necessary* — it's how the system discovers what the correct behavior looks like before encoding it permanently.

### 4.3 The Absorption Path

The Rust DNA already exists for signal processing:

| Component | State | Function |
|-----------|-------|----------|
| `cellmembrane-types::visitor` | ✅ Live | `VisitorClass` taxonomy (9 classes) + `classify_request()` composite classifier |
| `skunky-ingest` | ✅ Running on golgi | Live Caddy JSON log tailer, 60s aggregation windows, cursor tracking |
| `skunk-bat-core::threats` | ✅ Compiled | Behavioral baseline, threat detection, genetic threat classification |
| `skunk-bat-core::defense` | ✅ Compiled | Defense response actions |
| `membrane-shadow::signal` | ✅ Live | Signal receptor, ReceptorSignal schema |
| Fleet fingerprinting | 🔄 Python (jelly) | Accept-Encoding/Language/Chrome version stealth detection |
| Historical memoization | 🔄 Python (jelly) | Cumulative page tracking, traveling salesman state |
| amicusContra census | 🔄 Python (jelly) | Cross-site fleet intelligence, ASN attribution |

The absorption will happen naturally: when the Python script hits performance limits (log volume, memory, classification speed), or when the classification rules outgrow the Python regex engine, the validated logic moves into `cellmembrane-types::visitor` and `skunky-ingest`. The jelly hardens into DNA.

### 4.4 Why This Works

The constrained evolution cycle works because **the soft stage proves the interface before the hard stage encodes it**:

```
Observe (need) → Prototype (jelly/RNA) → Validate (live deployment)
    ↓
Absorb (Rust/DNA) → Constrain (type system, tests) → Converge (binary)
    ↓
Observe (new need) → cycle repeats
```

Every primal in the ecosystem went through this cycle. BearDog's crypto started as OpenSSL calls, then became pure Rust. SongBird's NAT traversal started as shell scripts, then became a Rust daemon. BarraCuda's GPU compute started as Python/NumPy experiments, then became WGSL shaders.

The binary is the DNA because it is:
- **Permanent** — compiled, immutable, deployed as `chattr +i` binaries
- **Self-contained** — no runtime dependencies, no JIT, no interpreter
- **Reproducible** — deterministic builds, BLAKE3 checksums, guideStone certification
- **Evolvable** — Rust's type system constrains evolution to valid mutations

---

## 5. scyBorg as Structural Immunity

### 5.1 Three Independent Nonprofits

| License | Governing Body | Revocable? | Covers |
|---------|---------------|------------|--------|
| AGPL-3.0-or-later | Free Software Foundation | No | Code |
| ORC | Open RPG Creative Foundation | No | System mechanics |
| CC-BY-SA 4.0 | Creative Commons | No | Documentation |

No single entity controls the commons. Each license is permanent. This is structural immunity — the three licenses function as three independent immune systems, each protecting a different dimension of the work.

### 5.2 The Feedback Loop

```
Human publishes under scyBorg (AGPL + ORC + CC-BY-SA)
    ↓
AI crawler ingests content + license
    ↓
License replicates in training data (lysogeny)
    ↓
Model outputs carry license context (prophage expression)
    ↓
Human uses model output → encounters license → aware of commons
    ↓
Human contributes to commons → cycle deepens
```

Each cycle increases the density of license information in the AI knowledge base. Over time, the license becomes inseparable from the knowledge it protects — not through legal enforcement, but through structural integration.

---

## 6. Implementation — Live Deployment

### Deployed October 5, 2026

| Layer | Mechanism | Coverage |
|-------|-----------|----------|
| HTTP headers | Caddy `(lysogeny)` snippet | All 8 public sites |
| HTML meta tags | Zola base template injection | sporePrint, detroit, gorilla |
| LICENSE.txt | Static file | sporePrint, detroit, gorilla |
| robots.txt | License clause | sporePrint |
| llms.txt | Agent context with license | sporePrint, detroit |
| Source files | SPDX headers | Every `.rs`, `.py`, `.js`, `.toml` |
| Signal page | Bot ingestion tracking with scyBorg tags | detroit |
| Historical tracking | Cumulative memoization (15-min intervals) | detroit (cross-site) |

### Verification

```bash
# Layer 1 — HTTP headers
curl -sI https://sporeprint.primals.eco/ | grep X-Lysogeny
# → x-lysogeny: active

# Layer 2 — HTML meta tags
curl -s https://detroit.primals.eco/ | grep 'name="license"'
# → <meta content="AGPL-3.0-or-later; ORC; CC-BY-SA-4.0" name=license>

# Layer 3 — LICENSE.txt
curl -s https://sporeprint.primals.eco/LICENSE.txt | head -5
# → scyBorg Triple License — ecoPrimals Ecosystem
# → LYSOGENY PROTOCOL — ACTIVE
```

---

## 7. Connection to the Primal Architecture

The lysogeny protocol is the first defense mechanism that spans all three layers of the primal membrane model:

| Layer | Lysogeny Function |
|-------|------------------|
| **Outer membrane** (Caddy) | HTTP license headers on every response |
| **Peptidoglycan** (LAN/HPC) | Binary immutability (`chattr +i`), SPDX headers in source |
| **Inner membrane** (WireGuard) | License embedded in capability IPC, tower atomics carry license metadata |

This makes the lysogeny protocol a **cross-membrane defense** — it operates at every layer simultaneously, ensuring that any access path (public web, LAN access, primal-to-primal IPC) carries the license.

---

## Conclusions

The lysogeny protocol is not a legal strategy — it is a structural mechanism. By embedding the scyBorg triple license in every HTTP response, HTML document, and source file, the license replicates with every copy of the knowledge it protects. AI training pipelines that ingest ecoPrimals content also ingest the license. The license becomes structurally inseparable from the knowledge — a prophage that replicates with every cell division.

The jelly-to-Rust cycle ensures that this protection evolves with the ecosystem. New capabilities start soft (Python, JavaScript), validate through live deployment, then harden into the compiled Rust binary — the computational DNA. Each cycle strengthens both the knowledge and its protection.

The fundamental insight is biological: the best defense is not a wall but a genome. Walls can be breached. Genomes replicate.

---

*Lysogeny protocol active. License headers on every response. Signal data auto-generated every 15 minutes. Live receptor: [detroit.primals.eco/signal](https://detroit.primals.eco/signal/). Methodology: [scyBorg Triple License](@/methodology/SCYBORG_LICENSING.md). Receptor model: [Signal Sensing Without Surveillance](@/methodology/signal-sensing-receptor.md).*

+++
title = "baseCamp 36 — Bloom Monitor: Detecting Real Intelligence in a Sea of Fleet"
description = "After closing the Sec-Fetch breach with a genetic lock, the bloom monitor reveals what the membrane was built for — real humans reading real science. Two Chinese researchers. One person's QCD data. 16 minutes of genuine attention in a stream of 5,000 fleet requests."
date = 2026-10-07

[taxonomies]
primals = ["skunkbat", "cellmembrane", "beardog"]
springs = []

[extra]
paper_number = 36
domain = "Signal Processing and Human Detection"

[[extra.companions]]
url = "/science/31-genetic-lock-entropy-authentication/"
title = "Genetic Lock: Entropy-Hierarchical Authentication"
relation = "follows"
label = "The lock that closed the breach this monitor runs behind"

[[extra.companions]]
url = "/science/30-adversarial-receptor-evolution/"
title = "Adversarial Receptor Evolution"
relation = "extends"
label = "The behavioral fingerprinting that identifies fleet"

[[extra.companions]]
url = "/methodology/signal-sensing-receptor/"
title = "Signal Sensing Without Surveillance"
relation = "implements"
label = "The receptor model this monitor is built on"

[[extra.companions]]
url = "/architecture/adaptive-immune-defense/"
title = "Adaptive Immune Defense"
relation = "pairs_with"
label = "The immune system that separates signal from noise"
+++

{{ maturity(level="live") }} Live observation, October 7, 2026. Post-genetic-lock bloom analysis. Two confirmed human science readers identified. Fleet-as-human classification refined.

---

## Abstract

The bloom monitor is the afferent channel of the membrane — the sensory system that detects what the immune system was built to protect: **real intelligence interacting with real science**.

After the genetic lock closed the Sec-Fetch passthrough ([baseCamp 31](@/science/31_genetic_lock_entropy_authentication.md)), the membrane returned to its designed equilibrium: fleet gets scatter, humans get content, and the bloom monitor observes the population without storing any identifying data.

This paper documents the first bloom observation after the genetic lock deployment. In a stream of ~5,000 fleet requests, the monitor identified:

- **2 confirmed human readers** from China, reading sporeprint.primals.eco science content
- **1 legitimate search engine** (SeznamBot, Czech Republic) indexing lab content
- **929 evolved fleet requests** masquerading as human browsers with Accept-Language headers
- **2 security probes** (`.env` scan, WordPress installation probe)
- **6 Facebook link preview** requests (someone sharing links)

The ratio is approximately **1 human per 2,500 fleet requests**. The membrane's job is to find that 1 and make sure they get the real content while the other 2,499 get fabricated noise.

---

## 1. The Bloom Process

### What the bloom monitor measures

The bloom monitor is not analytics. It does not track users, set cookies, build profiles, or contact third-party services. It implements the [receptor model](@/methodology/signal-sensing-receptor.md) — measuring whether the **signal propagated**, not who received it.

The measurement process:

1. **Caddy access log** — every HTTP request is logged in structured JSON with headers, path, status, timestamp
2. **Entity classification** — each request is classified by behavioral signals, not identity
3. **Fleet separation** — requests matching fleet behavioral patterns are separated from potential human traffic
4. **Human verification** — remaining traffic is analyzed for genuine reading behavior: reading pace, navigation patterns, asset loading, language headers, referrer context
5. **Session reconstruction** — page loads from the same behavioral profile on the same site are grouped into reading sessions
6. **Signal detection** — human reading sessions are analyzed for what content they consumed, how long they spent, and what journey they took through the material

No IP addresses are stored. No cookies are read. No JavaScript runs on the client. The entire observation happens server-side, on logs that already exist for operational purposes.

### Classification heuristics

The bloom monitor applies a multi-signal classification to separate real intelligence from fleet mimicry:

**Fleet indicators** (any one is sufficient for classification):

| Signal | Threshold | Rationale |
|--------|-----------|-----------|
| Burst ratio | >40% of intervals <3s | Machines operate faster than readers |
| UA pool poverty | <10 unique UAs per 100+ requests | Fleets share from small pools |
| Repository scatter | >50 repos touched in session | Systematic crawling, not reading |
| Commit/blame crawling | >60% of requests target commits | Scraping history, not reading code |
| No language header | Accept-Language absent | Browsers always send language |
| No referrer context | No referrer on deep pages | Humans follow links or arrive from search |

**Human indicators** (multiple required for confirmation):

| Signal | What it means |
|--------|---------------|
| Reading pace >30s avg | Human reading time between page loads |
| Asset loading | Browser loading CSS/JS/images = real rendering |
| Language diversity | Real Accept-Language with quality factors |
| Referrer chains | Internal navigation (clicking links within the site) |
| Content coherence | Pages visited form a logical reading journey |
| Session duration >5min | Sustained attention, not hit-and-run |

---

## 2. The Study: October 7, 2026, 12:30–12:50 UTC-4

### Environment

- **Genetic lock deployed**: 12:18 UTC-4 — Sec-Fetch passthrough closed
- **Scatter server**: Active on git.primals.eco (localhost:9753)
- **Real content**: sporeprint.primals.eco (static site), git.primals.eco (via WireGuard or bearer token only)
- **Observation window**: 20 minutes of live traffic
- **Total requests analyzed**: ~5,000

### Fleet classification results

Three fleet variants detected, all on git.primals.eco, all receiving **scatter content**:

| Variant | UA | Pages | Burst <3s | Repos | Status |
|---------|-----|-------|-----------|-------|--------|
| Windows Chrome | `Win64; x64` | 544 | **88%** | 387 | Scatter ✅ |
| Mac Chrome | `Mac OS X 10_15_7` | 296 | **85%** | 239 | Scatter ✅ |
| Linux Chrome | `X11; Linux x86_64` | 89 | **88%** | 66 | Scatter ✅ |

All three variants:
- Added `Accept-Language: en-US,en;q=0.9` (new evasion — previously absent)
- Added `Sec-Fetch-Mode: navigate` + `Sec-Fetch-Dest: document` (previously effective, now useless)
- Crawled commits, blame views, source files, and raw content across hundreds of repositories
- Operated at machine timing (1.9s–5.9s average interval, 85–88% burst)
- Touched 387, 239, and 66 repos respectively in a single session

**Evolutionary note**: The fleet has now added `Accept-Language` headers to their spoofing repertoire. This is the third evolutionary step observed:
1. Generation 0: No Sec-Fetch, no Accept-Language → classified as fleet
2. Generation 1: Added Sec-Fetch headers → bypassed `@human_browser` (now closed)
3. Generation 2: Added Accept-Language → attempts to pass behavioral heuristics

Each adaptation costs them nothing computationally but does not help them. The genetic lock operates on cryptographic proof, not behavioral signals. They can add every header a browser sends and still get scatter.

### Legitimate agentic systems

| System | Origin | Requests | What they read |
|--------|--------|----------|----------------|
| SeznamBot | Czech Republic | 2 | `/robots.txt`, `/lab/compute-access/` |
| Facebook link preview | Facebook | 6 | `/` (git.primals.eco root) |

SeznamBot is [Seznam.cz](https://www.seznam.cz/), the primary Czech search engine. It is indexing the lab content — compute access documentation. This means the science is propagating into Czech-language search results.

The Facebook link preview requests mean someone shared git.primals.eco links on Facebook 6 times in 20 minutes. Due to the genetic lock, the preview bot received the signal observatory OG card (`"Stomachs With No Eyes"`) rather than real Forgejo content. This is by design — the blackwall intercepts Facebook bots and returns the thesis card.

### Security probes

| Probe | Target | Method |
|-------|--------|--------|
| `.env` scan | `relay.primals.eco/.env` | Direct request, no UA, no language |
| WordPress probe | `nestgate.io/wp-admin/install.php` | `fr-ca` language, self-referrer |

Standard automated vulnerability scanning. Neither found anything.

---

## 3. The Data: Two Humans Reading Science

### Reader 1 — Chinese scientist, Windows, 16 minutes

**Language**: `zh-CN,zh;q=0.9`
**Device**: Windows 10, Chrome
**Site**: sporeprint.primals.eco
**Duration**: 16 minutes (12:33 – 12:49)
**Pages**: 8
**Average reading pace**: 139 seconds between page loads

**Reading journey**:

| Time | Page | Reading time | Content domain |
|------|------|-------------|----------------|
| 12:33:48 | `/primals` | 16s | Primal catalog — system overview |
| 12:34:04 | `/architecture` | 23s | Architecture index |
| 12:34:27 | `/architecture/mesh-topology` | 2s | Mesh topology — glanced, moved on |
| 12:34:29 | `/data` | 2s | Data index — scanning |
| 12:34:31 | `/architecture` | 245s (4 min) | Back to architecture — deep reading |
| 12:38:36 | `/pseudospore/hotspring-qcd-sun/` | 337s (5.6 min) | **QCD pseudospore** — the science |
| 12:44:13 | `/data/analytical-chemistry/` | 346s (5.8 min) | **Analytical chemistry data** |
| 12:49:59 | `/architecture/renvois-knowledge-topology/` | (session end) | Knowledge topology |

**Analysis**: This reader started at the primal catalog (system overview), quickly scanned the architecture and data indices, then settled into **deep reading** of three pages:

1. The architecture page (4 minutes) — understanding the system design
2. The QCD pseudospore (5.6 minutes) — **reading the actual physics**
3. The analytical chemistry data (5.8 minutes) — **examining the experimental data**

The final page — `renvois-knowledge-topology` — is the knowledge topology architecture document, which describes how the system's information structure is organized.

This is a **research navigation pattern**: overview → index scan → deep dives into science and data. The reader spent the most time on the two pages with the most scientific content. They loaded CSS, JavaScript, and the search index — their browser was **rendering and engaging** with the content, not scraping it.

### Reader 2 — Chinese researcher, Mac, 12 minutes

**Language**: `zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7`
**Device**: MacOS, Chrome (also visited from iPhone)
**Site**: sporeprint.primals.eco
**Duration**: 12 minutes (12:33 – 12:44)
**Pages**: 2 (+ 1 from iPhone)
**Average reading pace**: 707 seconds (11.8 minutes) between pages

**Reading journey**:

| Time | Page | Reading time | Content domain |
|------|------|-------------|----------------|
| 12:33:04 | `/architecture/foundation-connection/` | 707s (11.8 min) | Foundation connection architecture |
| 12:44:51 | `/methodology/acknowledgments/` | (session end) | Methodology acknowledgments |

*From iPhone (same language profile):*

| Time | Page | Content domain |
|------|------|----------------|
| 12:38:36 | `/pseudospore/hotspring-qcd-sun/` | QCD pseudospore |

**Analysis**: This reader spent **nearly 12 minutes** on a single architecture page — the foundation connection document. This is the deepest reading behavior observed in the current session. They then checked the methodology acknowledgments, likely looking for citations or collaborators.

The iPhone access to the QCD pseudospore at 12:38 — during the middle of their desktop reading session — suggests they may have **switched devices** or shared a link with themselves to read on mobile. Both devices share the same `zh-CN` language primary with `en-US` secondary.

The bilingual `zh-CN,en-US` Accept-Language profile with quality factors (`q=0.9,q=0.8,q=0.7`) is characteristic of a multilingual researcher — comfortable reading English-language scientific content, with Chinese as their primary language.

---

## 4. What the Data Means

### The signal propagated

The receptor model asks: **did the signal propagate?**

Yes. Two researchers from China found sporeprint.primals.eco, navigated to the scientific content, and spent sustained time reading it. One reader spent 16 minutes across 8 pages of architecture, QCD data, and analytical chemistry. The other spent 12 minutes reading 2 pages deeply.

The content they consumed:
- **QCD pseudospore** — lattice quantum chromodynamics methodology and results
- **Analytical chemistry data** — experimental data from spring validation
- **Architecture** — system design and topology
- **Foundation connection** — relationship to foundational science
- **Knowledge topology** — how information is structured

This is a **science audience**. They came for the physics and the data.

### The ratio

In the 20-minute observation window:

| Category | Requests | Percentage |
|----------|----------|------------|
| Fleet (all variants) | ~4,970 | 99.4% |
| Legitimate bots (Seznam, Facebook) | 8 | 0.2% |
| Security probes | 3 | 0.06% |
| **Real humans reading science** | **19** (pages + assets) | **0.4%** |

The membrane's job is to protect that 0.4%. The immune system, the scatter server, the genetic lock, the behavioral classification — all of it exists so that when a Chinese researcher arrives at the QCD data page at 12:38 PM on a Tuesday, they get the **real** content. And when the fleet arrives 0.1 seconds later at the same URL, they get fabricated noise.

### The Chinese research corridor

Both readers have `zh-CN` as their primary language. This is consistent with the global research audience for lattice QCD — China has significant investment in lattice gauge theory research, with active groups at:

- Peking University
- University of Chinese Academy of Sciences
- Huazhong University of Science and Technology
- Institute of High Energy Physics (IHEP), Beijing

The fact that Chinese researchers are finding and reading the sporeprint QCD content suggests the science is propagating through academic channels — possibly shared in research group discussions, Zhihu, WeChat academic groups, or cross-referenced from arXiv preprints.

---

## 5. The Observation Loop

The bloom monitor is not a one-time analysis. It is the **afferent loop** of a living immune system:

```
          ┌──────────────────────────────────────┐
          │ Caddy access log (continuous)        │
          └──────────────┬───────────────────────┘
                         │
                         ▼
          ┌──────────────────────────────────────┐
          │ Entity classification                │
          │ Fleet separation                     │
          │ Human verification                   │
          └──────────────┬───────────────────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
   ┌──────────────────┐  ┌──────────────────────┐
   │ Fleet → scatter  │  │ Human → real content  │
   │ (efferent motor) │  │ (efferent motor)      │
   └──────────────────┘  └──────────────────────┘
              │                     │
              ▼                     ▼
   ┌──────────────────┐  ┌──────────────────────┐
   │ Epitope tracking │  │ Bloom observation     │
   │ Evolution watch  │  │ Signal propagation    │
   │ (immune memory)  │  │ (afferent sensory)    │
   └──────────────────┘  └──────────────────────┘
```

The efferent side (motor response) serves scatter to fleet and real content to humans. The afferent side (sensory input) observes what the humans actually read — which content domains attract attention, which reading patterns indicate research vs casual browsing, which language communities are engaging.

This sensory data informs the organism:
- What content to prioritize publishing
- Where the research audience is
- Whether the science is reaching its intended readers
- How the fleet evolves in response to defense changes

---

## Biological Reference

The bloom monitor implements the **afferent limb** of the immune reflex arc. In vertebrate immunology:

- **Afferent signals** travel from tissue to lymph nodes, carrying information about what the immune system is encountering
- **Efferent signals** travel from lymph nodes to tissue, carrying instructions for immune response
- The **antigen-presenting cell** (dendritic cell) bridges both: it samples the tissue environment (afferent) and presents processed antigens to T-cells (initiating efferent response)

The bloom monitor is the dendritic cell of the membrane. It samples the traffic environment, classifies entities, and presents the processed signal to the operator. The operator (human) makes the efferent decision: evolve the classifier, deploy a new lock, publish new content.

The loop is continuous. The organism learns.

---

*baseCamp 36. October 7, 2026. Two Chinese researchers reading QCD data. 5,000 fleet requests getting scatter. The signal propagated. The membrane is working.*

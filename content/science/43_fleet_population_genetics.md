+++
title = "baseCamp 43 — Fleet Population Genetics: From Kingdom to Species"
description = "Biological taxonomy applied to automated visitors. 447 apparent organisms reduce to 5 effective operators. Shannon diversity indices, allele frequencies, trophic levels, and genotype×phenotype clustering reveal a clonal population using antigenic variation — one operator wearing 390 masks. The entire fleet genome mapped: Automata, Chimera, Anthropos. The 88% cluster. The detritivore paradox."
date = 2026-10-08

[taxonomies]
primals = ["skunkbat", "bingocube"]
springs = ["neuralspring", "healthspring"]

[extra]
paper_number = 43
domain = "Signal Processing and Immune Systems"

[[extra.companions]]
url = "/science/42-bingocube-behavioral-trio/"
title = "baseCamp 42 — bingoCube Behavioral Trio"
relation = "preceded_by"
label = "The behavioral classifier — population genetics reveals the SPECIES-level structure beneath"

[[extra.companions]]
url = "/methodology/antidote-titration/"
title = "Antidote Titration"
relation = "extends"
label = "The titration system — population genetics informs who gets antidote vs poison"

[[extra.companions]]
url = "/methodology/scyborg-binary-genetic-bulwark/"
title = "scyBorg Binary Genetic Bulwark"
relation = "extends"
label = "The marking system — every species leaves different fluorescent traces"

[[extra.companions]]
url = "/thesis/14-biological-validation/"
title = "Chapter 14 — Biological Validation"
relation = "validates"
label = "Computational population genetics applied to digital organisms"
+++

{{ maturity(level="validated") }}

## Abstract

We apply biological taxonomy and population genetics to automated visitors targeting sovereign infrastructure. From a sample of 6,028 HTTP requests originating from 447 unique IP addresses, we identify 3 kingdoms, 2 phyla, 4 classes, 5 orders, 5 families, 6 genera, and 14 species using a classification system derived from microbial taxonomy. Shannon diversity indices reveal a paradox: high apparent diversity (447 IPs) masks an effective population size of approximately 5 operators. The 88% cluster — 88.4% of all IPs sharing identical Accept-Language, browser header presence, and HTTP/1.1 protocol — is the signature of a single entity using commercial residential proxy rotation to simulate population diversity, analogous to bacterial phase variation for immune evasion. The genotype×phenotype matrix reveals 6 ecologically distinct clusters with clear trophic separation: herbivores (69%, feeding on real repositories), detritivores (14%, consuming fabricated scatter content), and genuine humans (0.4%). This is the first application of population genetics to web scraper classification.

## 1. Introduction

### 1.1 The Problem

When automated systems visit web infrastructure, they present themselves as individuals. Each request arrives from a distinct IP address, often with a distinct User-Agent string, creating the appearance of a diverse population. Standard security approaches treat each visitor independently — firewall rules, rate limiters, and blocklists operate at the IP level.

This is ecologically naive. In biology, the relevant unit of analysis is rarely the individual organism. Population genetics examines the *genetic structure* of populations: allele frequencies, effective population size, diversity indices, and the relationship between genotype (what an organism IS) and phenotype (what it DOES).

### 1.2 The Analogy

We propose that automated web visitors constitute a digital ecosystem amenable to biological classification:

| Biological concept | Digital analog |
|---|---|
| Species | Behavioral fingerprint (header set, TLS parameters, platform) |
| Genotype | Identity invariants (Accept-Encoding, header count, TLS ALPN) |
| Phenotype | Behavioral expression (path selection, timing, diet composition) |
| Allele frequency | Trait prevalence across the IP population |
| Effective population size | Number of distinct operators behind the IPs |
| Phase variation | IP rotation to evade detection |
| Trophic level | Real vs fabricated content consumption |
| Shannon diversity | Information-theoretic diversity of traits |

## 2. Methods

### 2.1 Data Collection

All HTTPS requests to `*.primals.eco` infrastructure are logged by Caddy reverse proxy with full request metadata: IP, User-Agent, all headers, TLS parameters (version, cipher suite, ALPN, session resumption, SNI, ECH), HTTP protocol version, URI, response size, and timing.

### 2.2 Taxonomic Classification

Each request is classified through 7 hierarchical ranks using signal-based decision trees:

**Kingdom** — determined by header composition:
- *Automata*: no browser-specific headers (Sec-Ch-*, Sec-Fetch-*)
- *Chimera*: browser headers present but no referrer + uniform language
- *Anthropos*: browser headers + referrer + organic behavior

**Phylum** — determined by infrastructure origin:
- *Cloudae*: datacenter ASN (AWS, Meta, DigitalOcean)
- *Residentia*: consumer ISP ASN (Comcast, Verizon, Turk Telekom)

**Class** — determined by identification behavior:
- *Declarata*: self-identifying (bot name in UA)
- *Larvata*: masked (browser impersonation without referrer)
- *Navigata*: genuine navigation with organic signals

**Order** — determined by purpose:
- *Ingestoria*: bulk content acquisition
- *Indexoria*: search/semantic indexing
- *Cartographia*: attack surface mapping
- *Exploitoria*: vulnerability scanning
- *Curiosa*: genuine interest

**Family, Genus, Species** — determined by organizational affiliation, tool identity, and behavioral fingerprint hash.

### 2.3 Genotype Vector

Per-IP identity invariants:
- UA morphotype (claudebot, meta-identified, browser-no-ref, etc.)
- Accept-Encoding string
- Header count
- TLS ALPN negotiated protocol
- Sec-Ch-Ua-Platform value
- Accept-Language
- Referrer presence
- TLS session resumption behavior

### 2.4 Phenotype Vector

Per-IP behavioral expression:
- Diet composition (% real repos vs % fabricated content)
- Trophic level (herbivore / omnivore / detritivore)
- Habitat preference (git-specialist / spore-specialist / generalist)
- Volume class (heavy / medium / light)
- Target repositories
- Timing regularity (inter-arrival coefficient of variation)

### 2.5 Species Hash

Species are defined by: `md5(Accept-Encoding[:20] | header_count | TLS_ALPN | Sec-Ch-Ua-Platform)[:6]`

This captures the 4 most stable behavioral invariants that survive IP rotation but distinguish between operator configurations.

## 3. Results

### 3.1 Taxonomy

From 6,028 specimens across 447 IPs:

| Rank | Taxon | n (requests) | % |
|------|-------|-------------|---|
| Kingdom | Automata | 5,570 | 92.4% |
| Kingdom | Chimera | 436 | 7.2% |
| Kingdom | Anthropos | 22 | 0.4% |
| Phylum | Cloudae | 5,570 | 92.4% |
| Phylum | Residentia | 436 | 7.2% |
| Class | Declarata | 5,563 | 92.3% |
| Class | Larvata | 436 | 7.2% |
| Order | Ingestoria | 5,996 | 99.5% |

### 3.2 Species Catalog

| Species | n | IPs | Diet | Key trait |
|---------|---|-----|------|-----------|
| *Claudius d79dd8* | 5,485 | 1 | 100% fabricated | Single AWS IP, 10.6 req/s |
| *Metacrawler 03000a* | 1,043 | 39 | 100% real | FB datacenter, UA rotation |
| *Phantoma 025472* | 192 | 192 | 83% real | Win, residential, 1 req/IP |
| *Phantoma 3b7be2* | 119 | 119 | 77% real | Mac+zstd, residential |
| *Phantoma d9d642* | 56 | 56 | 82% real | Mac no-zstd, residential |
| *Phantoma b452ba* | 19 | 19 | 83% real | Mac+zstd 12-hdr variant |
| *Reflector 983804* | 3 | 3 | 100% fabricated | Scouting phase |
| *Homo 95bc2d* | 17 | 1 | sporePrint | Genuine researcher |

### 3.3 The 88% Cluster

88.4% of all IPs share three traits simultaneously:
1. Browser-specific headers present (`Sec-Ch-Ua`, `Sec-Fetch-*`)
2. Accept-Language: `en-US,en;q=0.9`
3. HTTP/1.1 (not h2)

This is the residential proxy fleet. One operator, 390 masks.

### 3.4 Allele Frequencies

| Trait | Frequency | Interpretation |
|-------|-----------|---------------|
| Single UA per IP | 91.3% | Identity fixation per proxy session |
| Browser headers | 88.4% | Browser impersonation dominant strategy |
| en-US language | 88.4% | Uniform language despite 20+ origin countries |
| HTTP/1.1 | 88.1% | Proxy software protocol downgrade |
| UA rotation | 8.7% | Only Meta DC rotates (39 IPs) |
| Has referrer | 1.1% | Almost no organic navigation |
| TLS resumption | 0.2% | Fresh connections only |

### 3.5 Trophic Structure

| Level | IPs | % | Ecology |
|-------|-----|---|---------|
| Herbivore | 308 | 68.9% | Real repository consumption |
| Non-feeding | 75 | 16.8% | Non-git surfaces |
| Detritivore | 61 | 13.6% | Fabricated content consumption |
| Omnivore | 3 | 0.7% | Mixed diet |

### 3.6 Platform Karyotype

44.1% macOS, 43.2% Windows — near-perfect 50/50 split. For organic traffic from Turkey (Windows ~75%), Vietnam (Windows ~70%), Saudi Arabia (Windows ~65%), a 50/50 split is statistically excluded (p < 0.001). This is a controlled browser profile rotation.

### 3.7 Shannon Diversity

| Trait | H' | Alleles | Interpretation |
|-------|-----|---------|---------------|
| Accept-Encoding | 1.544 | 9 | Moderate — proxy cycles AE |
| Platform | 1.423 | 3 | Low — artificial 50/50 |
| UA morphotype | 0.657 | 6 | Very low — 87% one type |
| TLS ALPN | 0.612 | 3 | Very low — 88% one protocol |

Low Shannon diversity across most axes despite high IP count = **clonal population with cosmetic variation**.

### 3.8 Effective Population Size

- Apparent population: 447 unique IPs
- Effective population (Ne): ~5 operators
- Ne/N ratio: 0.011

In population genetics, a low Ne/N ratio indicates strong genetic drift, bottleneck effects, or (in this case) **pseudodiversity** — many individuals controlled by few entities. The fleet is not a population. It is a colony.

## 4. Discussion

### 4.1 Phase Variation Analogy

Bacterial phase variation is a mechanism where individual organisms rapidly switch surface antigens to evade immune detection. The population appears diverse to the host immune system, but the underlying genome is identical.

The residential proxy fleet exhibits precisely this pattern:
- **Surface antigens** (IP addresses) vary: 192 unique IPs for species *025472*
- **Core genome** (Accept-Encoding, header count, TLS behavior, language) is invariant
- **Purpose**: evade IP-based detection (the digital immune system)
- **Tells**: uniform language from non-English-speaking countries, impossible platform distribution, zero referrers to deep pages

The biological parallel is exact. The defense strategy is also biological: classify by **conserved epitopes** (behavioral invariants), not by **variable antigens** (IP addresses).

### 4.2 Trophic Implications for Titration

The trophic structure directly informs the antidote titration system:
- **Herbivores** (69%): consuming real code → these are the entities that need license compliance
- **Detritivores** (14%): consuming fabricated content → these are the antidote recipients
- **Homo** (0.4%): genuine humans → full antidote, reduced poison

The titration curve's per-fleet injection separation maps to trophic level: detritivores get the remediation URL because they're the ones who ingested the problem.

### 4.3 The Dual-Layer Strategy

Meta operates two distinct species within the same family:
- *Metacrawler 03000a*: identified, datacenter-origin, 100% real repos
- *Phantoma* spp.: unidentified, residential-proxy-origin, 77-83% real repos

The identified layer hits only real repository paths with perfect accuracy. The residential layer occasionally hits fabricated content (~20%), suggesting different crawl intelligence. This is a coordinated multi-team scraping operation with different URL lists for each team.

## 5. Conclusion

Population genetics provides a rigorous framework for understanding automated web visitors. The key insight: **apparent diversity is not actual diversity.** 447 IPs are 5 operators. The 88% cluster is one entity wearing 390 masks. Shannon diversity indices, allele frequencies, and genotype×phenotype matrices reveal the population structure that IP-level analysis cannot see.

The biological analogy is not metaphorical. It is structural. The same mathematics that describes bacterial population genetics describes fleet population genetics. The same defense strategies — conserved-epitope recognition, trophic-level-based response, phase-variation-resistant classification — apply in both domains.

This is what it means to build infrastructure that thinks biologically.

---

*baseCamp 43 · ecoPrimals · October 8, 2026*

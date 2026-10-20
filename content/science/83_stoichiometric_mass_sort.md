+++
title = "Stoichiometric Mass Sort: Shannon Entropy as Page Weight"
description = "An information-theoretic method for ordering static content by compositional mass. Uses Shannon entropy, Blake3 content hashing, and the braid provenance model to replace arbitrary page weights with measured information density."
date = 2026-10-20
authors = ["Kevin Mok"]

[taxonomies]
springs = ["primalSpring", "groundSpring"]

[extra]
status = "validated"
orcid = "0009-0004-2141-0321"
primal_deps = ["sourDough", "sweetGrass", "loamSpine", "squirrel"]
validated_on = "eastgate sovereign compute (i9-14900K, 96GB DDR5)"
validation_date = 2026-10-20
pages_sorted = 1185
sites_applied = ["detroit", "publicRecord", "tuebor"]
tests = 14
total_ecosystem_tests = 644
+++

## Abstract

Static content sites accumulate pages with hand-assigned ordering weights that drift from reality as content evolves. We present **stoichiometric mass sort** — an information-theoretic method that replaces arbitrary weights with measured compositional mass derived from Shannon entropy, vocabulary richness, connectivity, and evidentiary grounding. Each page receives a Blake3 content hash (identity) and a Shannon entropy measurement (mass), composed through the existing ecoPrimals braid provenance model. Applied to 1,185 pages across three Zola sites, the method produces stable orderings that reflect actual information density. The tool is implemented as `sourdough validate mass` — a Rust validator that chipmunk (the autonomous observer) can invoke periodically in a sandbox.

---

## 1. The Problem: Weight Decay

Content management systems that sort pages by weight (an integer field in frontmatter) face a universal problem: **weights decay**. A page assigned `weight = 50` when it had 200 words doesn't deserve the same position after it grows to 4,000 words with 70 cross-references and 42 evidentiary citations. Hand-tuned weights are:

- **Arbitrary** — no relationship to content
- **Unstable** — drift as pages evolve
- **Unverifiable** — no audit trail for why a page ranks where it does
- **Labor-intensive** — require human intervention at every change

The membrane already had this problem: 11 pages in `sort_by = "weight"` sections had no weight at all, silently disappearing from navigation. The first fix was hand-assigning weights. The second was asking: *can the content weigh itself?*

---

## 2. The Mass Formula

Mass is computed per page as:

$$
M = \sqrt{W} \times H \times \left(1 + \frac{L}{50}\right) \times \left(1 + \frac{C}{10}\right) \times R
$$

Where:

| Symbol | Name | Meaning |
|--------|------|---------|
| $W$ | Word count | Bulk — more content, more mass (square root dampens outliers) |
| $H$ | Shannon entropy | Information density in bits — how much each word contributes |
| $L$ | Link count | Connectivity — markdown links to other pages |
| $C$ | Citation count | Evidentiary grounding — FOIA, LARA, MDOC, PACER, case numbers |
| $R$ | Richness | Vocabulary diversity — unique words / total words |

### 2.1 Shannon Entropy

Shannon entropy measures the information content of a word frequency distribution:

$$
H = -\sum_{i=1}^{n} p_i \log_2 p_i
$$

where $p_i$ is the probability of the $i$-th unique word. A page where every word appears exactly once has maximum entropy. A page repeating the same phrase has zero entropy. Natural language falls between 6–10 bits for English text, depending on vocabulary and topic diversity.

**Why Shannon?** Because it's what bearDog's genetics already uses for entropy tiering. The same information-theoretic measure that classifies external entities now classifies our own content. The organism applies its own immune system to itself.

### 2.2 Why These Factors?

Each factor captures a different dimension of "mass":

- **√W (bulk)**: A 4,000-word investigation has more mass than a 200-word stub. Square root prevents raw length from dominating — a 10,000-word page isn't 50× heavier than a 200-word page; it's 7× heavier.
- **H (entropy)**: Repetitive content is lighter than diverse, information-rich content. A page that uses 500 unique words across 2,000 total words carries more information per word than one using 50 unique words across 2,000.
- **L/50 (connectivity)**: Pages that link to many others are structural hubs. The `/50` normalizes so that 50 links doubles the mass contribution — a reasonable threshold for a well-connected analysis page.
- **C/10 (citations)**: Evidence-grounded pages are heavier. FOIA responses, court documents, regulatory filings — these are the evidentiary substrate. 10 citations doubles the grounding factor.
- **R (richness)**: Unique vocabulary / total vocabulary. A page with high richness uses diverse language; one with low richness is formulaic. This penalizes copy-paste and rewards original analysis.

---

## 3. Composition from Existing Pieces

The key insight is that we didn't build this from scratch. Every component maps to an existing ecosystem piece:

| Component | Ecosystem Piece | Where |
|-----------|----------------|-------|
| Page identity | `ContentHash` (Blake3, 32 bytes) | sourDough-core `types.rs` |
| Short hash (topo sort handle) | First 16 hex chars of ContentHash | loamSpine `DataAnchor` vocabulary |
| Information density | Shannon entropy H | bearDog genetics entropy hierarchy |
| Strength model | `√W × H × connectivity × grounding × richness` | squirrel scan-sweep-sort `combined_strength` |
| Provenance | Braid with `data_hash` + `mime_type` + `size` | sweetGrass `Braid` + `BraidBuilder` |
| Publish weight | `weight = N` in Zola frontmatter (1–200) | Zola static site generator |

### 3.1 The Provenance Trio Connection

The provenance trio (loamSpine + rhizoCrypt + sweetGrass) already handles exactly this workflow:

1. **loamSpine** provides `DataAnchor` entries — content hash + MIME + size committed to a permanent spine
2. **sweetGrass** provides `Braid` records — PROV-O attribution with `data_hash`, `was_generated_by`, `was_attributed_to`
3. **rhizoCrypt** provides ephemeral DAG workspaces — the mass calculation IS a session that compresses into braids

The stoichiometric mass validator produces data that could be committed as braids: each page's mass is a provenance-tracked measurement, content-addressed by Blake3, attributable to the tool that computed it.

### 3.2 The bearDog Genetics Mirror

bearDog classifies external entities using entropy hierarchy, ecosystem membership, and trust evolution. The primal taxonomy (Appendix A of `compositions.toml`) classifies the primals themselves — 15 primals sorted by domain, role, symbiosis type, mass (1–200), tier, and gate identity.

The stoichiometric mass sort is the same pattern applied to content: **the organism classifying its own publications by information density**, using the same entropy measure it uses to classify the outside world.

---

## 4. Implementation

### 4.1 `sourdough validate mass`

```
sourdough validate mass <content_dir> [--apply] [--json]
```

- **Dry run** (default): Reports mass for all pages without modifying files
- **`--apply`**: Writes `weight = N` into each page's frontmatter (TOML or YAML)
- **`--json`**: Machine-readable output for CI integration
- Handles both TOML (`+++`) and YAML (`---`) frontmatter formats
- Scans conventional weight-sorted sections: analysis, books, evidence, network, path, signal, actors, braid, investigate, synthesis, coverage

### 4.2 Weight Normalization

Weights are normalized to the 1–200 range:

$$
w_i = \text{round}\left(200 \times \frac{M_i}{M_{\text{max}}}\right)
$$

clamped to a minimum of 1. The heaviest page always gets weight 200. All others scale proportionally.

### 4.3 Test Coverage

14 unit tests covering:

- Shannon entropy (uniform, constant, empty distributions)
- Word extraction and filtering
- Link counting
- Citation detection (case-insensitive)
- Frontmatter format detection (TOML, YAML)
- Content hash identity (Blake3 determinism)
- Short hash format (16 hex chars)
- Mass ordering (diverse content > small content)
- Citation amplification (evidence increases mass)
- Different content → different hashes

All 644 sourDough tests pass. The mass validator integrates with the existing 14-subcommand validate suite.

---

## 5. Results

Applied to three Zola sites on 2026-10-20:

| Site | Pages | Max Mass | Mean H (bits) | Top Page |
|------|-------|----------|---------------|----------|
| detroit | 443 | 1,775.8 | 7.092 | `the-enterprise` (H=8.903, 4,025 words, 70 links, 42 citations) |
| publicRecord | 429 | — | — | (shared analysis content) |
| tuebor | 313 | — | — | (YAML frontmatter variant) |
| **Total** | **1,185** | | | |

### 5.1 Top 10 by Mass (detroit)

| Weight | Mass | H (bits) | Words | Links | Cites | Blake3 | Page |
|--------|------|----------|-------|-------|-------|--------|------|
| 200 | 1,775.8 | 8.903 | 4,025 | 70 | 42 | `6c188f37` | the-enterprise |
| 126 | 1,121.4 | 8.402 | 1,876 | 74 | 27 | `97b584e2` | all-roads-lead-back-to-rome |
| 104 | 923.5 | 8.665 | 2,437 | 36 | 28 | `89a2b6cb` | dykema-chronology |
| 102 | 902.0 | 8.978 | 3,099 | 32 | 24 | `97f32c9e` | the-referral |
| 94 | 833.7 | 8.487 | 2,980 | 43 | 24 | `d117250a` | questions |
| 93 | 823.1 | 8.648 | 2,894 | 7 | 46 | `c85cf03a` | the-gatekeeper |
| 85 | 755.4 | 8.563 | 2,379 | 45 | 24 | `56288de3` | the-accountability-matrix |
| 82 | 730.8 | 8.654 | 2,575 | 8 | 36 | `21b4058b` | corporate-network-lara |
| 74 | 657.0 | 8.928 | 2,268 | 10 | 23 | `a18e7f26` | institutional-capture-graph |
| 74 | 655.2 | 8.904 | 2,832 | 9 | 27 | `1d044137` | backscatter |

### 5.2 Observations

1. **Entropy correlates with analytical depth**: The top pages all have H > 8.4 bits, indicating diverse vocabulary typical of investigative analysis rather than formulaic listings.

2. **Citations amplify mass disproportionately**: `the-gatekeeper` has only 7 links but 46 citations, giving it a grounding multiplier of 5.6×. The evidentiary weight compensates for lower connectivity.

3. **The formula is self-stabilizing**: Running the mass sort a second time (after weights changed from pass 1) produced the same ordering. This is because mass depends on content, not on the weight field — changing `weight = N` doesn't change the page body, so the mass is invariant under re-sorting.

4. **Blake3 hashes provide change detection**: If a page's content changes, its hash changes. A CI pipeline can detect which pages need re-weighing by comparing stored hashes to current ones — no need to re-sort the entire site.

---

## 6. The Primal Taxonomy

The same mass methodology applied to primals themselves produces a self-classification (Appendix A of `compositions.toml`):

| Primal | Mass | Tier | Domain | Gate | Symbiosis |
|--------|------|------|--------|------|-----------|
| bearDog | 200 | tower | immune | guardGate | protective |
| loamSpine | 190 | nest | permanence | ironGate | facilitative |
| sweetGrass | 185 | nest | provenance | strandGate | mutualistic |
| toadStool | 175 | node | neuromorphic | soverGate | facilitative |
| rhizoCrypt | 170 | nest | ephemeral | deepGate | commensal |
| skunkBat | 165 | tower | defense | shieldGate | protective |
| songBird | 160 | tower | network | echoGate | mutualistic |
| squirrel | 155 | meta | observation | cacheGate | commensal |
| biomeOS | 150 | meta | orchestration | rootGate | emergent |
| sourDough | 145 | meta | tooling | yeastGate | facilitative |
| barraCuda | 140 | node | compute | fastGate | facilitative |
| nestGate | 135 | nest | storage | nestGate | facilitative |
| coralReef | 130 | node | transport | reefGate | mutualistic |
| petalTongue | 120 | meta | visualization | lensGate | commensal |
| bingoCube | 100 | full | games | playGate | mutualistic |

Mass totals per atomic tier:
- **tower** (3 primals): 525
- **node** (+3): 970
- **nest** (+4): 1,205
- **nucleus** (10): 1,650
- **meta** (+3): 425
- **full** (14+): 2,275

The tower — identity, network, defense — is the densest per-primal composition. The organism's core is heavy; its periphery is light. This mirrors biological cells: the nucleus and membrane are the most information-dense structures; organelles specialize.

---

## 7. Reproducibility

```bash
# Install sourDough (requires Rust toolchain)
cd primals/sourDough && cargo build --release

# Dry run — see masses without modifying files
sourdough validate mass /path/to/zola/content

# Apply weights
sourdough validate mass /path/to/zola/content --apply

# Machine-readable output
sourdough validate mass /path/to/zola/content --json
```

The tool handles both TOML (`+++` delimited) and YAML (`---` delimited) frontmatter. It scans conventional weight-sorted section directories and skips `_index.md` files.

---

## 8. Future Work

1. **Braid integration**: Each mass measurement could be committed as a sweetGrass Braid with the page's Blake3 hash as `data_hash`, creating a provenance-tracked history of page weights over time.

2. **scan-sweep-sort integration**: The mass data feeds naturally into squirrel's 6-stage pipeline (SCAN → SWEEP → SORT → FOSSILIZE → EVOLVE → GENOME). Pages become entities in the membrane's observation model.

3. **Delta detection**: Store Blake3 hashes per page. On subsequent runs, only re-compute mass for pages whose hash changed. This makes the tool O(changed pages) instead of O(all pages).

4. **Cross-site normalization**: Currently each site normalizes independently (heaviest = 200). Cross-site normalization would allow comparing detroit's `the-enterprise` against tuebor's top page directly.

5. **Temporal mass tracking**: Record mass history in squirrel's journal. Detect pages that are *growing* (gaining mass through edits) vs *decaying* (static while the rest of the site evolves). This is the bearDog genetics `TrustEvolution` pattern applied to content.

---

## 9. Conclusion

The stoichiometric mass sort demonstrates that information-theoretic measurements compose naturally from existing ecosystem primitives. We didn't invent new math — Shannon entropy (1948), Blake3 hashing (2020), and PROV-O attribution (W3C 2013) are established tools. The contribution is recognizing that:

1. **Pages are entities** in the same sense that membrane traffic entities are classified by scan-sweep-sort
2. **Content has measurable mass** via Shannon entropy, and that mass is stable under re-sorting
3. **The organism's immune system works on itself** — bearDog genetics applied inward produces a self-taxonomy

The tool runs in under a second for 443 pages. It requires no external services, no API keys, no cloud. A sovereign sort for sovereign content.

---

## References

- Shannon, C.E. (1948). "A Mathematical Theory of Communication." *Bell System Technical Journal*, 27(3), 379–423.
- O'Connor, J. et al. (2020). "BLAKE3: One function, fast everywhere." Specification and reference implementation.
- W3C (2013). "PROV-O: The PROV Ontology." W3C Recommendation.
- Credit: Sollimann for bonsai-bt behavioral tree architecture.
- ecoPrimals Authorship: Kevin Mok / Tamison / ecoPrimal / attsi, ORCID 0009-0004-2141-0321.

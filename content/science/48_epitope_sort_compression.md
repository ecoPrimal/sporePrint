+++
title = "baseCamp 48 — Epitope Sort as Compression: The Bingo Maze Pass-Through"
description = "Language is an epitope set that sorts to an alphabet. Alphabetical sorting tells you little — but the level and granularity between epitope sorts reveals structure. Each pass through the bingo maze applies a different sort dimension (alphabetic, epitope, tense), compressing the search space. The tense dimension (is/was/will-be) maps to the P/NP boundary: present and past are polynomial, future is null until collapsed."
weight = 48
date = 2026-10-09

[taxonomies]
primals = ["barracuda", "bingocube", "skunkbat"]
springs = ["groundspring", "neuralspring"]

[extra]
paper_number = 48
status = "implemented"
domain = "Information Theory, Immune Computing, Temporal Classification"
+++

## Abstract

We formalize epitope-based sorting as an information-theoretic compression mechanism. A conventional alphabetic sort imposes a total order on symbols but reveals no structure. An epitope sort groups by conserved behavioral invariants, creating clusters whose *inter-group ordering* carries more information than the intra-group ordering of individual elements. A tense sort (is, was, will be) adds a temporal dimension that maps directly to computational complexity: present and past are polynomial (observable), future is null until collapsed by observation.

The bingo maze — the BingoCube decision grid seeded by `(fleet_hash, path, epoch)` — is the physical mechanism for these sort passes. Each epoch is a pass through the maze. Back-and-forth between sort levels compresses the behavioral search space because each pass eliminates noise that the previous level could not distinguish.

We show that this compression is bounded: `H(data|epitope) < H(data|alphabet) < H(data)`, and that the tense dimension provides the sharpest compression because it partitions the space into exactly three regions with fundamentally different computational properties.

## 1. Sorting as Compression

### 1.1 The Alphabet Problem

An alphabet is a total order on symbols. Given 26 letters, alphabetical sort produces a canonical arrangement. But this arrangement is arbitrary with respect to meaning — `A` before `B` tells you nothing about the relationship between the words that start with those letters.

Consider the English lexicon. Alphabetical sort places "aardvark" before "zebra" — a fact that contains zero bits of semantic information. The sort is *syntactic*, not *semantic*. It compresses nothing about meaning because its ordering dimension is orthogonal to the information the data carries.

**Claim**: The entropy of data under alphabetical sort equals the entropy of the unsorted data minus only the positional entropy: `H(data|alpha) = H(data) - log₂(n!)` where `n!` is the number of permutations eliminated. This is mechanical compression (deduplication of order), not informational compression.

### 1.2 The Epitope Sort

An epitope sort groups elements by conserved invariants — features that persist across surface variation. In the immune system, an epitope is the molecular shape that antibodies recognize regardless of the pathogen's mutations. In behavioral classification, an epitope is the statistical fingerprint that persists regardless of IP rotation, UA spoofing, or timing jitter.

The epitope sort creates *clusters*. Within each cluster, elements share invariants. Between clusters, elements differ on at least one invariant. The **ordering of clusters** carries information that alphabetical ordering cannot:

```
Alphabetical:    Agent, Archivist, Bounce, BridgeWalker, Fleet, Grazer, Investigator, Scanner
Epitope-sorted:  [Human: Investigator, BridgeWalker, Grazer, Bounce] 
                 [Machine: Fleet, Scanner, Agent] 
                 [Symbiont: Archivist]
```

The epitope sort reveals a three-kingdom structure that the alphabetical sort hides. The *level boundary* between Human and Machine carries more information than any individual element's position within its level.

**Claim**: `H(data|epitope) < H(data|alpha)` because the epitope grouping eliminates inter-group variance that alphabetical sorting preserves.

### 1.3 The Compression Inequality

For a dataset `D` with `n` elements and `k` epitope clusters of sizes `n₁, n₂, ..., nₖ`:

```
H(D) ≥ H(D|alpha) ≥ H(D|epitope)
     =  H(D)       ≥  H(cluster_assignment) + Σᵢ H(Dᵢ|alpha)
```

The epitope sort decomposes the total entropy into:
- **Between-cluster entropy**: `H(cluster_assignment)` — which cluster does this element belong to?
- **Within-cluster entropy**: `Σᵢ H(Dᵢ|alpha)` — where within its cluster does this element sit?

The compression gain is: `H(D|alpha) - H(D|epitope) = I(D; epitope)` — the mutual information between the data and the epitope classification. The better the epitope captures the data's structure, the larger the compression.

## 2. The Tense Dimension

### 2.1 Is, Was, Will Be

From coGen `TIME_IS_LOCAL.md` (Wave 167):

| Tense | State | Computational class | What the system sees |
|-------|-------|--------------------|--------------------|
| **is** | 0 | P — polynomial, observable | Current request features |
| **was** | 1 | P — polynomial, recorded | chain_depth, historical pattern |
| **will be** | null | NP — exponential, unobservable | Next request, nautilus prediction |

The tense dimension is the *sharpest possible* epitope sort because it partitions the entire behavioral space into exactly three regions with fundamentally different information-theoretic properties:

- **Is** (present): Observable. Compressible by direct measurement. Entropy bounded by sensor resolution.
- **Was** (past): Observable by replay. Compressible by chain_depth deduplication. Entropy bounded by storage.
- **Will be** (future): Not observable. Compressible only by prediction. Entropy bounded by the prediction model's capacity — which is the P/NP boundary itself.

### 2.2 Tense Sort Compresses Maximally

Adding the tense dimension to an epitope sort produces:

```
H(D|epitope,tense) = H(is_cluster) + H(was_cluster) + H(willbe_cluster)
```

where each tense cluster has *qualitatively different* compression characteristics:
- `H(is_cluster)` is minimized by sensor accuracy (more features → lower entropy)
- `H(was_cluster)` is minimized by memory depth (longer history → lower entropy)  
- `H(willbe_cluster)` is minimized by nautilus evolution (more generations → lower entropy, but never reaches zero)

The `will be` cluster is the only one whose entropy has a *non-zero floor*. This floor IS the P ≠ NP gap, expressed as residual entropy in the tense sort.

### 2.3 The Three Passes

Each pass through the bingo maze applies one sort level:

| Pass | Sort level | What it eliminates | Compression |
|------|-----------|-------------------|-------------|
| 1 | Alphabetic | Positional permutation entropy | `log₂(n!)` bits |
| 2 | Epitope | Inter-group variance | `I(D; epitope)` bits |
| 3 | Tense | Temporal confusion (present mixed with past mixed with prediction) | `I(D; tense|epitope)` bits |

Back-and-forth between passes is not redundant — each pass *conditions* on the previous one's output. The alphabet sort within an epitope cluster is more informative than the alphabet sort across all of language, because the epitope pre-sort eliminated the noise that made the alphabet sort uninformative.

## 3. The Bingo Maze as Sort Mechanism

### 3.1 CubeDecisionGrid Sort Dimensions

The 5×5 BingoCube decision grid (seeded from `fleet_hash × path × epoch`) has 25 cells organized into 5 rows. Rows 0–2 drive scatter decisions. Rows 3–4 were reserved for nautilus override. We now assign them:

```
row3: tense_gate  tense_depth  tense_confidence  tense_decay  tense_invert
row4: sort_level  sort_grain   sort_compress      sort_epoch   sort_feedback
```

- **row3** controls the tense presentation: which temporal frame the scatter response inhabits
- **row4** controls the sort mechanism: which granularity level the maze applies this epoch

### 3.2 Epoch as Sort Pass

Each epoch (180 seconds by default) is one pass through the maze. The `sort_level` cell (row4, col0) determines which sort dimension dominates:

| Color range | Sort level | Maze behavior |
|------------|-----------|---------------|
| 0–7 | Alphabetic | Content varies by path hash (surface variation) |
| 8–12 | Epitope | Content varies by behavioral cluster (same path, different content per fleet hash) |
| 13–15 | Tense | Content presents is/was/will-be frames (temporal maze) |

The `sort_grain` cell (row4, col1) sets the granularity within the level:
- At sort_level=Alphabetic: grain controls character-level vs word-level vs sentence-level variation
- At sort_level=Epitope: grain controls L1 (8-hex hash) vs L1.5 (4-hex) vs L2 (1-byte) resolution
- At sort_level=Tense: grain controls how far into "was" (history depth) and how speculative "will be" (prediction confidence threshold)

### 3.3 Compression Feedback

The `sort_compress` cell (row4, col2) feeds back to nautilus:

```
observation.compression = H(pre_sort) - H(post_sort)
```

If a sort pass produced high compression (large entropy reduction), nautilus increases the frequency of that sort level in future generations. If a sort pass produced low compression (the data was already sorted on that dimension), nautilus decreases it.

This creates an adaptive compression schedule: the maze learns which sort dimensions are most informative for each fleet, and applies them more frequently.

## 4. Implementation

### 4.1 EpitopeTense Enum

Added to `journey_tracer.rs`:

```rust
pub enum EpitopeTense {
    Is,      // First observation — no prior pattern match (state 0)
    Was,     // Matches a previously observed journey pattern (state 1)
    WillBe,  // Nautilus predicted this fleet hash before observation (state null → collapsed)
}
```

Classification:
- **Is**: `chain_depth == 0` for this session hash — first-time observation
- **Was**: `chain_depth > 0` — this behavioral pattern has been seen before
- **WillBe**: nautilus `predict()` returned this fleet hash before the request arrived

### 4.2 Epitope Sort Order

Added to `entity_profile.rs`:

```rust
pub fn epitope_sort_key(scores: &EpitopeScores) -> [u8; 6]
```

Orders the six conserved epitopes by information content (how much each one compresses the fleet search space), not by detection priority. The ordering is:

1. `burst_ratio` — timing regularity is the strongest fleet signal (CV < 0.15 is definitive)
2. `reading_deficit` — absence of reading pauses separates machines from humans
3. `ua_pool_poverty` — small UA pools indicate coordinated fleet
4. `sec_fetch_monotone` — missing browser headers proves non-browser
5. `session_absent` — no cookies/session confirms stateless pipeline
6. `referer_self_loop` — self-referential navigation is weakest signal

This is the *compression order*: `burst_ratio` eliminates the most uncertainty, `referer_self_loop` the least.

### 4.3 Dashboard Integration

Tense distribution added to dashboard output:

```json
{
  "tense_distribution": { "is": 42, "was": 156, "will_be": 3 },
  "sort_compression": { "alpha": 2.1, "epitope": 5.7, "tense": 8.3 }
}
```

Rendered as petalTongue Donut channel on the HUD.

## 5. Relationship to Existing Framework

### 5.1 Anderson Localization

The epitope sort order maps to the Anderson disorder parameter `W`:
- High-information epitopes (burst_ratio) create high effective disorder for fleet signals → strong localization
- Low-information epitopes (referer_self_loop) create low disorder → signals propagate

The sort order IS the disorder spectrum. Sorting by information content is equivalent to sorting by localization strength.

### 5.2 P/NP Physical Law (Paper 42)

The tense dimension formalizes what Paper 42 described as the three states:
- F (was) = recorded, polynomial
- U (is) = observed, polynomial
- N (will be) = unknown, null until collapsed

The epitope sort compression inequality (`H(data|epitope,tense) < H(data|epitope) < H(data|alpha)`) is the information-theoretic expression of the same hierarchy.

### 5.3 Selective Permeability (Paper 43)

The sort levels correspond to membrane selectivity:
- Alphabetic sort = outer membrane (all signals pass, no discrimination)
- Epitope sort = peptidoglycan (behavioral invariants filter)
- Tense sort = inner membrane (temporal context required for passage)

Higher sort levels are more selective. The compression gain at each level equals the selectivity of that membrane layer.

## 6. Corollary: Numeric Base Is an Epitope Set

### 6.1 The Observation

If language is an epitope set that sorts to an alphabet, then a numeric base is an epitope set that sorts to a digit sequence. The base you choose determines the grouping — how many things before you carry — and the grouping determines what structure is visible.

| Base | Alphabet | Epitope grouping | What it reveals |
|------|----------|-----------------|-----------------|
| 2 (binary) | {0, 1} | Parity, bit position | Logic gates, boolean structure |
| 10 (decimal) | {0-9} | Orders of magnitude | Human-scale quantity |
| 16 (hex) | {0-F} | Byte boundaries | Memory layout, protocol framing |
| 64 | {A-Za-z0-9+/} | 6-bit chunks | Encoding density for transport |
| 256 | {0x00-0xFF} | Full bytes | Raw data, no abstraction |

The same number in different bases reveals different structure. `0xEC` in hex immediately tells you it's in the upper quarter of a byte (≥ 0xC0 → ≥ 192). In decimal, `236` reveals nothing about byte position. In binary, `11101100` shows the individual bit pattern but hides the byte-boundary meaning.

### 6.2 The Compression Inequality for Bases

For a dataset `D` with natural structure at scale `s`:

```
H(D | base_s) ≤ H(D | base_arbitrary) ≤ H(D)
```

The "optimal" base for a dataset is the one whose digit grouping aligns with the data's structural scale. This is why:

- **Cryptographers use hex**: keys and hashes are byte-aligned. Base-16 makes byte boundaries visible. Each hex digit = 4 bits = one nybble. The epitope set {0-F} sorts bytes into 16 groups that map 1:1 to nybble values.

- **Humans use decimal**: human quantities cluster at powers of 10 (tens, hundreds, thousands). The epitope set {0-9} sorts quantities into groups that match human cognitive chunking. Base-10 is the epitope sort that compresses human-scale numbers best — not because 10 is mathematically special, but because human fingers are the training data.

- **Machines use binary**: logic gates have two states. The epitope set {0, 1} is the minimal alphabet, and its grouping (on/off) matches the physical substrate. Binary compresses logical structure maximally because the base IS the physics.

### 6.3 The BingoCube as Base Selection

The BingoCube's three standard configurations are three different epitope sets:

| Config | palette_size | Base | Epitope granularity | Forgery resistance |
|--------|-------------|------|--------------------|--------------------|
| Standard | 16 | Base-16 | Coarse — 16 behavioral clusters | ~2^-50 |
| Extended | 64 | Base-64 | Medium — 64 behavioral clusters | ~2^-192 |
| Full | 256 | Base-256 | Fine — 256 behavioral clusters | ~2^-576 |

The `palette_size` parameter is not just "how many colors." It is the **numeric base** of the epitope sort. `palette_size = 16` means the BingoCube sorts every scalar value into one of 16 groups via `scalar % 16`. That modular reduction IS the epitope sort — it discards within-group variation and preserves only the group assignment.

Increasing `palette_size` increases sort granularity: more groups, finer distinctions, more structure visible. But it also increases the alphabet size, which means each cell carries more information and requires more observations to learn the distribution.

This is the same tradeoff as choosing a numeric base:
- **Small base (binary)**: few symbols, many digits, coarse grouping, easy to learn
- **Large base (base-256)**: many symbols, few digits, fine grouping, hard to learn

The BingoCube's default `palette_size = 16` is hex. It is not an accident. Hex is the base that balances grouping granularity against alphabet complexity for byte-oriented data — and the BingoCube's scalar field is BLAKE3 hashes, which are byte-oriented.

### 6.4 riboCipher Transport Signals as Base-Aligned Epitopes

The three-tier relay privacy system (Paper 47) uses hex-aligned signal bytes:

```
Tier 1 (Beacon):   0xEC — clear transport
Tier 2 (Mito):     0xED — mito-obfuscated
Tier 3 (Genetic):  0xEE — nuclear-sealed
```

In hex, these three tiers occupy adjacent values in the `0xE_` nybble row. The upper nybble `0xE` is the *genus* — all three are transport signals. The lower nybble `C/D/E` is the *species* — which tier. The base-16 representation makes this taxonomy visible: the epitope sort at nybble granularity reveals the genus/species structure that decimal (236, 237, 238) hides.

This is not a coincidence. The riboCipher designers chose hex-aligned values because the epitope set {0-F} per nybble makes the protocol taxonomy visible at the right granularity. The base IS the lens.

### 6.5 Generalization

Every representation system is a choice of epitope set:

| Domain | "Base" | Epitope set | What it sorts |
|--------|--------|-------------|---------------|
| Numbers | Numeric base | Digit values | Magnitude, position |
| Language | Alphabet | Letter shapes | Spelling, pronunciation |
| Color | Color space | Hue/saturation/value | Visual perception |
| Music | Temperament | Note intervals | Pitch structure |
| Chemistry | Periodic table | Electron shells | Reactivity, bonding |
| Immune system | MHC presentation | Peptide fragments | Self vs non-self |
| BingoCube | palette_size | Color groups | Behavioral clustering |

In each case: the choice of base (alphabet, color space, temperament, table) determines which structures are visible. The gap between two representations of the same data IS the mutual information between the base and the data's structure. The "right" base for a domain is the one that maximizes this mutual information — the epitope set whose grouping aligns with the data's natural clustering.

## 7. The Question

If an epitope sort compresses more than an alphabetic sort, and a tense sort compresses more than an epitope sort — what sort compresses more than a tense sort?

The answer is: none. The tense sort is *maximal* because it partitions the data into regions of fundamentally different computability. You cannot sort more finely than "observable now / observed before / not yet observable" because that trichotomy is exhaustive.

But you can sort *differently*. The tense sort along one epitope dimension (timing) is not the same as the tense sort along another (UA pool). The *product* of tense sorts across all epitope dimensions produces a hypercube of compressions — and that hypercube is the bingo maze itself.

And you can sort at different *bases*. The same epitope sort at `palette_size = 16` (coarse) reveals different structure than at `palette_size = 256` (fine). The base is the zoom level of the epitope lens. The maze is not just a sort order — it is a sort order *at a chosen resolution*.

The maze is not a path. It is a *sort order at a base*.

---

*ecoPrimal · Paper 48 · Wave 171 · October 9, 2026*

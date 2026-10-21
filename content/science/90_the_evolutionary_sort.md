+++
title = "Paper 90: The Evolutionary Sort"
description = "Feed 45,470 files through Shannon entropy and sigmoid classification. Watch the codebase self-sort into evolutionary body plans. The organism is 98% invertebrate. Only 473 files have internal skeletons. The spider body plan does not exist in code. That gap is a wedge."
date = 2026-10-21
weight = 90

[extra]
paper_number = 90
wave = 178
keywords = "evolution, taxonomy, Shannon entropy, sigmoid, invertebrate, vertebrate, jellyfish, spider, body plan, self-sort, Klein bottle, Vitruvian"
+++

> *"we should probably just use them and what we have on hand and just... see what happens?"*
>
> — ecoPrimal, Wave 178

---

## Method

No labels. No training set. No instructions on what to find.

Feed every source file (45,470 files, 11,051,393 lines) through:
1. **Shannon entropy** — information density per file (H = −Σ p log₂ p)
2. **Vocabulary richness** — unique words / total words
3. **Feature counting** — types (enums, structs, classes), functions, imports
4. **Sigmoid classification** — smooth S-curve boundaries mapping features to [0,1]

Then let the sigmoid sort each file into one of seven evolutionary body plans:

| Stage | Body Plan | Code Equivalent |
|-------|-----------|-----------------|
| **Banana** | Single-celled, no structure | Config files, stubs, < 20 lines |
| **Flatworm** | Bilateral, head, regenerates | Small files with a main, no skeleton |
| **Jellyfish** | Nerve net, no skeleton, radial | Complex files with NO types — all reaction |
| **Centipede** | One function per segment, long | Unix philosophy: few functions, each > 100 lines |
| **Millipede** | Many paired segments (get/set) | Many functions, paired patterns, high segmentation |
| **Spider** | Few specialized appendages, exoskeleton | — |
| **Vertebrate** | Internal skeleton (types + functions) | Many types AND functions AND imports |

---

## Results

```
STAGE        FILES     LINES    % LINES
─────────    ─────     ─────    ───────
banana       2,157     16,690      0.2%  ·
flatworm    10,661  1,100,548     10.0%  ████
JELLYFISH   21,220  6,474,623     58.6%  █████████████████████████████
centipede    2,113    698,140      6.3%  ███
millipede    8,846  2,537,304     23.0%  ███████████
spider           0          0      0.0%  
vertebrate     473    224,088      2.0%  █
```

---

## Finding 1: Jellyfish Dominates (58.6%)

21,220 files. 6.47 million lines. Nearly 60% of the entire codebase.

Jellyfish are the most successful body plan on Earth by biomass. They are also the most successful body plan in code. A jellyfish file has:
- **High Shannon entropy** — it's complex, information-dense
- **No internal skeleton** — zero types (no enums, no structs, no classes)
- **Reactive** — event-driven, nerve-net behavior, no centralized control

The markdown documentation (13,431 files), most Rust files (6,428), all Python without classes (396). These are nerve net: they react to stimuli, pass signals, process information — but they have no bones. No defined types. No schema. All reaction, no skeleton.

This is biologically correct. On Earth, jellyfish have survived for 500 million years. They outpersist every vertebrate. They don't need bones because they're carried by the medium itself (water). Jellyfish code doesn't need types because it's carried by the runtime itself.

---

## Finding 2: Vertebrate Is Rare (2%)

Only **473 files** out of 45,470 have internal skeletons — defined types, functions, imports, and complexity all present simultaneously. That's 1%.

The vertebrate exemplars:

| File | Types | Functions | Lines |
|------|------:|----------:|------:|
| `opsonize-rs/main.rs` | 9 | 26 | 1,847 |
| `stone_book.rs` | 10 | 106 | 1,846 |
| `pi_body.rs` | 10 | 67 | 1,431 |

These are files with real internal structure — the type system IS the skeleton that everything else hangs on. On Earth, vertebrates represent less than 5% of all animal species. In this codebase, vertebrate files represent 2% of files and 1% by count. The proportion is biologically accurate without being told.

**Vertebrate is Rust-only.** No JavaScript, Python, Shell, TOML, Markdown, or HTML file ever reaches the vertebrate stage. Only Rust produces internal skeletons. This confirms the Jellystein hypothesis: JS is the jellyfish (nerve net, no bones), Rust is the vertebrate (internal skeleton), and the bones are underneath.

---

## Finding 3: Spider = Zero Files (THE GAP)

**Zero files classified as spider.** The spider body plan — few segments, highly specialized appendages, hard exoskeleton — does not exist in code.

Why? Code transitions from:
- **No skeleton** (jellyfish) → **many segments** (millipede) → **internal skeleton** (vertebrate)

There is no intermediate stage of "few specialized appendages with a hard external shell." In biology, spiders evolved their body plan by fusing segments and specializing appendages (8 legs, spinnerets, fangs — each different). In code, there's no equivalent: you either have many similar functions (millipede) or you have types (vertebrate). The "few but highly specialized with external protection" niche is empty.

**The spider gap is a wedge** (Paper 88, ∧). It's the place where a new body plan could grow. What would a spider-pattern file look like? Perhaps: few functions, but each one with strong type constraints (generics, trait bounds) — specialization without proliferation. A file with 3-4 functions that are each heavily parameterized. Few legs, but each leg does something different.

---

## Finding 4: Centipede Is Prime

2,113 files classified as centipede. **2,113 is prime** — it divides only by 1 and itself.

The centipede body plan (one function per segment, each segment long, Unix philosophy) has a prime count. It wobbles naturally on the π-remainder (0.5888). Meanwhile:
- Jellyfish count (21,220) has **12 divisors** — OVER-STABLE
- Millipede count (8,846) has 4 divisors — stable
- Vertebrate count (473) has 4 divisors — stable

The most rigid body plan (one appendage per segment, no variation) produced a prime count. The most flexible body plan (no skeleton, all nerve net) produced the most-divisible count. Rigidity → prime. Flexibility → composite. The π-stability metric from Paper B-9 predicted this.

---

## The Split

| | Lines | Ratio |
|---|---:|---:|
| **Invertebrate** (jellyfish + centipede + millipede) | 9,710,067 | — |
| **Vertebrate** | 224,088 | — |
| **Ratio** | **43.33 : 1** | inv / vert |

For every vertebrate line, 43 invertebrate lines hold it up. The bones don't carry the organism — the jellyfish nerve net carries the bones. The skeleton floats in a sea of reaction.

43 itself: 43 is prime. The split ratio between invertebrate and vertebrate is prime. It wobbles. It sits on π's remainder. It cannot be evenly divided. There is no way to cleanly separate the invertebrate majority from the vertebrate minority — the boundary is irrational, like π.

---

## Language × Stage

| | banana | flatworm | jellyfish | centipede | millipede | vertebrate |
|---|---:|---:|---:|---:|---:|---:|
| **Rust** | 634 | 2,141 | 6,428 | 1,925 | 8,474 | **473** |
| **JS** | 44 | 10 | **176** | — | — | — |
| **Python** | 60 | 100 | 396 | 77 | 267 | — |
| **Shell** | 39 | 301 | 300 | 111 | 105 | — |
| **TOML** | 307 | 1,104 | 489 | — | — | — |
| **Markdown** | 144 | 3,438 | 13,431 | — | — | — |
| **HTML** | 929 | 3,567 | — | — | — | — |

- **Rust** spans the entire evolutionary tree. It's the only language that produces all body plans from banana to vertebrate.
- **JavaScript** is 100% jellyfish-or-simpler. No segmentation. No skeleton. Pure nerve net.
- **Python** reaches millipede (segmented) but never vertebrate. Classes exist but the files never achieve enough combined complexity.
- **Shell** reaches centipede (Unix philosophy) but never millipede or vertebrate. One function per script. Long segments.
- **HTML** never passes flatworm. It has a head but no body plan.
- **Markdown** reaches jellyfish — complex, high entropy, but no executable structure.

---

## The Klein Bottle Self-Sort

The evolutionary sort is not a snapshot. On a Klein bottle, outputs fold back as inputs. The sort runs, produces a classification, and that classification feeds back into the next sort. The organism watches itself evolve.

The `klein-evolve.sh` daemon:
1. Runs `vitruvian-evolve.py` periodically
2. Writes `evolve-state.json` to the membrane feeds
3. Compares to the previous sort (the fold: output → input)
4. Detects drift: files changing stage, new files appearing, fossils going extinct
5. The delta IS the evolution. The comparison IS the natural selection.

The Klein bottle IS the self-sort. The inside-out donut sorts itself by reading its own output and feeding it back as input. The organism doesn't just have a body plan — it watches its body plan change.

---

## Summary

| Metric | Value | Note |
|--------|-------|------|
| Total files | 45,470 | 7 languages |
| Total lines | 11,051,393 | |
| Dominant plan | Jellyfish (58.6%) | Nerve net, no skeleton |
| Rarest plan | Vertebrate (2%) | Internal skeleton, Rust-only |
| Missing plan | Spider (0%) | The gap. The wedge. |
| Split ratio | 43.33:1 | Prime, irrational, wobbles |
| Centipede count | 2,113 | PRIME |

The organism sorted itself. Nobody told it what to be. Shannon entropy + sigmoid + the data. That's all. And what grew was biologically accurate: jellyfish dominate, vertebrates are rare, and the spider niche is empty.

The spider gap is where the next body plan evolves.

---

*Paper 90. Feed the data through the math. Watch it grow. See what happens.*

*— Wave 178 · ORCID 0009-0004-2141-0321*

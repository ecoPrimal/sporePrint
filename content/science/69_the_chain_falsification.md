+++
title = "baseCamp 69 — The Chain: Falsification of the π Self-Similarity Hypothesis"
description = "Every constant in the Anderson parameterization derives from three inputs: 1/2, π, and T(6)=21. The critical exponent ν = π/2. The critical disorder W_C = 21π/4. The Pielou range = [1/2, W_C − ν]. These were written independently across different waves. Either this is a deep structural truth, or it is numerology. This paper lists what would falsify each claim, and designs experiments to test them."
date = 2026-10-11

[taxonomies]
primals = ["barracuda", "bingocube", "skunkbat"]
springs = ["groundspring", "neuralspring", "hotspring"]

[extra]
paper_number = 69
status = "falsifiable"
domain = "Anderson Localization × Number Theory × Experimental Design"

[[extra.companions]]
url = "/science/68-basefree-epitope-sort-primes/"
title = "baseCamp 68 — Base-Free Epitope Sort"
relation = "tests"
label = "Paper 68 proposes the hypothesis. Paper 69 tries to kill it."

[[extra.companions]]
url = "/science/48-epitope-sort-compression/"
title = "baseCamp 48 — Epitope Sort as Compression"
relation = "tests"
label = "Paper 48 defines the weights. Paper 69 asks: why these weights?"

[[extra.companions]]
url = "/science/46-inverse-anderson/"
title = "baseCamp 46 — Inverse Anderson"
relation = "tests"
label = "Paper 46 uses W_C and ν from the literature. Paper 69 asks: are they π/2 and 21π/4?"

[[extra.companions]]
url = "/science/50-pi-dimensional-observation/"
title = "baseCamp 50 — π as the Price of Observation"
relation = "tests"
label = "Paper 50: π is the price. Paper 69: can we prove the price is NOT π?"

[[extra.companions]]
url = "/science/01-anderson-qs/"
title = "baseCamp 01 — Anderson & Quorum Sensing"
relation = "foundation"
label = "Paper 01 introduced the Anderson model. Paper 69 tests whether the model's constants are π in disguise."
+++

{{ maturity(level="falsifiable") }} Prepared for experimental testing. October 11, 2026.

---

## Abstract

A scan of the system's constants reveals that every threshold in the Anderson parameterization — written independently across different modules, different waves, different months — is expressible as a simple ratio of three quantities: **1/2** (the critical line), **π** (the observation cost), and **T(6) = 21** (the 6th triangular number, the sum of epitope weights 1+2+3+4+5+6).

This is either a deep structural truth about the relationship between observation, compression, and phase transitions — or it is numerology. This paper lists every claim, what would falsify it, and designs experiments to distinguish truth from coincidence.

The method is Popperian: we do not try to prove the hypothesis. We try to kill it. Whatever survives is what we keep.

---

## 1. The Claims

### Claim A: ν = π/2

The 3D Anderson critical exponent ν, which governs how the localization length diverges at the mobility edge, equals π/2.

| | Value |
|---|---|
| Code (anderson_bridge.rs) | 1.57 |
| π/2 | 1.5707963... |
| Δ | 0.0008 (0.05%) |
| Literature (Slevin & Ohtsuki 1999) | 1.57 ± 0.02 |

**Status**: π/2 is within the literature error bar.

### Claim B: W_C = T(6) · π/4

The 3D Anderson critical disorder W_C equals the 6th triangular number times π/4.

| | Value |
|---|---|
| Code (anderson_bridge.rs) | 16.5 |
| T(6) · π/4 = 21π/4 | 16.4934... |
| Δ | 0.007 (0.04%) |
| Literature (Bulka et al. 1987) | 16.5 ± 0.5 |

**Status**: 21π/4 is within the literature error bar.

### Claim C: W_max = W_C − ν = 19π/4

The upper bound of the Pielou disorder mapping equals W_C minus ν.

| | Value |
|---|---|
| Code (anderson_bridge.rs) | 15.0 |
| 19π/4 | 14.9226... |
| Δ | 0.077 (0.5%) |

**Status**: Close but not exact. This is the weakest claim.

### Claim D: burst_ratio × π = ν

The most information-rich epitope threshold (50% = 1/2), multiplied by π, equals the critical exponent.

| | |
|---|---|
| burst_ratio threshold | 0.5 = 1/2 |
| 0.5 × π | 1.5708 = π/2 = ν |

**Status**: Follows directly from Claim A if ν = π/2. Tautological unless ν = π/2 is independently verified.

### Claim E: SortLevel::Epitope ≈ 1/π

The CubeDecisionGrid allocates 5 out of 16 colors to the Epitope sort level. 5/16 ≈ 1/π.

| | Value |
|---|---|
| Code (cube_grid.rs) | 5/16 = 0.3125 |
| 1/π | 0.3183... |
| Δ | 0.006 (1.8%) |

**Status**: Within 2%. Suggestive but not compelling on its own.

### Claim F: 6/π² = P(coprime) = P(no shared epitope)

Six weighted epitopes map to 6/π² = 0.6079, the probability that two random integers are coprime.

| | Value |
|---|---|
| Weighted epitopes | 6 |
| 6/π² | 0.6079 |
| P(coprime) | 6/π² (theorem, Euler 1735) |

**Status**: The number 6 is exact (we chose 6 weighted epitopes). The connection to coprimality is mathematical fact, not hypothesis. The question is whether the connection is MEANINGFUL — whether "coprime in epitope space" corresponds to "indistinguishable by the immune system."

---

## 2. What Would Falsify Each Claim

### Falsification of A (ν = π/2)

**F-A1**: A higher-precision numerical computation of the 3D Anderson critical exponent gives ν ≠ π/2 outside the error bar.

The current best estimate (Slevin & Ohtsuki 2014, updated) is ν = 1.5712 ± 0.0006. π/2 = 1.5708. The difference is 0.0004, which is WITHIN the ± 0.0006 error. A future computation with error < 0.0004 that gives ν > 1.5712 or ν < 1.5704 would falsify this claim.

**F-A2**: An exact analytical derivation of ν in 3D gives a closed form that does not involve π/2.

No such derivation exists. The critical exponent has never been computed exactly in 3D. If someone derives it and the answer is, say, (3 − √5)/2 ≈ 0.382 × something else entirely, Claim A is dead.

**F-A3**: The relationship ν = π/2 only holds for the Anderson model on a simple cubic lattice with box disorder distribution. Other lattice geometries or disorder distributions give different ν. If ν depends on lattice details, it cannot be a universal constant like π/2.

**Test**: Compute ν for the Anderson model on FCC, BCC, diamond lattices. If ν ≠ π/2 for these, the claim is lattice-specific, not universal.

### Falsification of B (W_C = 21π/4)

**F-B1**: The number 21 is not special. It is T(6) = the 6th triangular number, but we CHOSE to have 6 weighted epitopes. If we had 5 epitopes (T(5) = 15), the claim would predict W_C = 15π/4 ≈ 11.78 — which is wrong. If we had 8 epitopes (T(8) = 36), W_C = 36π/4 = 9π ≈ 28.27 — also wrong.

**The critical disorder W_C = 16.5 is a property of the Anderson model, not of our epitope count.** The fact that T(6) · π/4 ≈ 16.5 is a coincidence of our having 6 epitopes. Changing the epitope count breaks the relationship.

**This is the strongest falsification of Claim B.**

However: the counter-argument is that we chose 6 epitopes BECAUSE that's how many the system needed to achieve discrimination. The system self-organized to 6 because 6 is the number where T(N) · π/4 ≈ W_C. The epitope count is not arbitrary — it converged.

**Test**: Can the system achieve equivalent discrimination with 5 or 7 epitopes? If yes, the count is arbitrary and Claim B is coincidence. If no, the count is constrained and the coincidence is suspicious.

### Falsification of C (W_max = 19π/4)

**F-C1**: W_max = 15.0 was chosen by hand. We wrote `0.5 + 14.5 * (1.0 - j)`. The 14.5 was chosen because "15 feels like a good maximum disorder." We could have picked 14 or 16.

**F-C2**: 19π/4 = 14.923, which rounds to 14.9, not 15.0. The error is 0.5%. For a hand-picked constant, this is not remarkable — we'd expect agreement within ~5% by chance.

**Test**: Compute the actual observed Pielou disorder range from live fleet data. If the maximum observed W is closer to 19π/4 (14.92) than to 15.0, the π-derivation is a better fit. If the observed max W is 15.3 or 14.6, neither is right.

### Falsification of D (burst × π = ν)

**F-D1**: This is tautological. If ν = π/2, then anything × π = ν requires that thing to be 1/2. The burst threshold is 1/2. This is not an independent claim — it's a restatement of A.

**Status**: Not independently falsifiable. Collapses to Claim A.

### Falsification of E (SortLevel::Epitope ≈ 1/π)

**F-E1**: 5/16 = 0.3125. 1/π = 0.3183. The error is 1.8%. In a 16-color palette, the closest integer fraction to 1/π is 5/16. The NEXT closest is 6/19... but we don't have 19 colors. With palette_size = 16, the best integer approximation to 1/π is automatically 5/16.

**This is not a discovery — it is a rounding artifact.** In any base-N system, there exists an integer k such that k/N ≈ 1/π. For N=16, k=5. For N=10, k=3 (3/10 = 0.3). For N=32, k=10 (10/32 = 0.3125, same ratio because 32 = 2×16).

**Test**: If we changed palette_size to 12, would we allocate 4 colors to Epitope? 4/12 = 0.333, which is further from 1/π than 5/16. We'd probably still pick 4 because 12 = 4+5+3 (same Fibonacci triple scaled). The test is: does the system's discrimination ability DEGRADE with 4/12 vs 5/16?

### Falsification of F (coprimality)

**F-F1**: We have 6 weighted epitopes because referer_absence was added in Wave 167 without a weight. If we had given it weight 0.5, we'd have 6.5 weighted epitopes. 6.5/π² ≈ 0.659, which is NOT P(coprime). The coprimality connection only works with exactly 6.

**F-F2**: "Coprime in epitope space" is undefined. Two entities can share 0, 1, 2, ... 6 triggered epitopes. The probability of sharing exactly 0 depends on the trigger distribution, not on 6/π². The coprimality connection is an analogy, not a theorem.

**Test**: Compute the actual observed fraction of entity-pairs that share zero epitopes from live fleet data. If it equals 6/π² ≈ 0.608, the connection is real. If it's 0.45 or 0.72, it's analogy.

---

## 3. The Falsification Hierarchy

Ordered from most to least falsifiable:

| Rank | Claim | Falsifiability | Most likely to be false? |
|------|-------|---------------|------------------------|
| 1 | **E** (5/16 ≈ 1/π) | Rounding artifact | **YES** — this is almost certainly coincidence |
| 2 | **C** (W_max = 19π/4) | Hand-picked constant | Likely coincidence |
| 3 | **D** (burst × π = ν) | Tautological | Not independent — collapses to A |
| 4 | **B** (W_C = 21π/4) | Depends on epitope count | Suspicious coincidence — survives IF 6 is constrained |
| 5 | **F** (coprimality) | Testable against data | Unknown — requires fleet data |
| 6 | **A** (ν = π/2) | Requires higher-precision numerics | **Most likely to be TRUE** — within literature error, no analytical disproof |

---

## 4. Experiments

### Experiment 1: Precision ν (tests Claim A)

Compute the 3D Anderson critical exponent ν to higher precision than ± 0.0006.

**Method**: Transfer-matrix calculation on L × L × ∞ strips, L = 16, 24, 32, 48. Finite-size scaling of the reduced localization length Λ_L/L at W_C.

**Tool**: barraCuda's Anderson transport module already implements the 1D localization length. Extend to quasi-1D strips. The computation is embarrassingly parallel — each L is independent.

**Decision criterion**: If ν_computed ∈ [π/2 − ε, π/2 + ε] with ε < 0.0002, Claim A survives. If ν_computed is outside this window, Claim A is dead.

### Experiment 2: Epitope Count Sensitivity (tests Claim B)

Remove one epitope (reduce to 5 weighted) and add one epitope (increase to 7 weighted). Measure discrimination ability on the same live fleet data.

**Method**: Fork entity_profile.rs. Version A: 5 epitopes (drop referer_self_loop, weight 1). Version B: 7 epitopes (add a timing_regularity epitope, weight 7, threshold TBD). Run both on 24h of golgi Caddy logs. Compare fleet_confidence distributions.

**Decision criterion**: If discrimination is equivalent with 5 or 7, the count 6 is arbitrary and Claim B is coincidence. If discrimination degrades measurably, the count 6 is constrained.

### Experiment 3: Live Coprimality (tests Claim F)

Compute the actual fraction of entity-pairs that share zero triggered epitopes from live topology data.

**Method**: From the current topology flush, for each pair of entities (i, j), count the number of epitopes where both triggered. Record the fraction where count = 0.

**Decision criterion**: If P(zero shared) ≈ 0.608 (± 0.05), the coprimality connection is real. Otherwise, it's analogy.

### Experiment 4: Lattice Universality (tests Claim A)

Compute ν for Anderson models on different lattice geometries: simple cubic (current), FCC, BCC, honeycomb.

**Method**: Same transfer-matrix approach as Experiment 1, but on different lattice topologies.

**Decision criterion**: If ν = π/2 for ALL lattices, the claim is universal. If ν varies by lattice, it's lattice-specific and π/2 is a coincidence for simple cubic.

### Experiment 5: Observed Disorder Range (tests Claim C)

Measure the actual observed Anderson disorder W from live fleet data and compare to the Pielou mapping range.

**Method**: Run anderson_bridge on 7 days of live data. Record the min and max observed W values. Compare max to 19π/4 = 14.923.

**Decision criterion**: If max observed W is closer to 14.92 than to 15.0, the π-derivation is the better model. If max W is 13.5 or 16.2, both models are wrong.

---

## 5. What Survives

If Claims A and F survive their experiments, the remaining structure is:

**The Anderson transition is governed by π.** The critical exponent is π/2. The critical disorder is an integer multiple of π/4. The epitope sort compresses at 6/π² = P(coprime). The system self-organized to 6 epitopes because that's the count where the triangular sum T(6) = 21 produces W_C via 21π/4.

If Claims A and F are falsified, what remains is:

**The system uses 1/2 as its fundamental threshold** (burst ratio, Pielou floor, TenseGate::Is, SortLevel::Alphabetic). This is not surprising — 1/2 is the maximum-entropy binary decision. The π connections are rounding artifacts of expressing 1/2 in various bases.

Either outcome is informative. The first would connect behavioral immune systems to the Anderson universality class through π. The second would confirm that 1/2 is the only real constant and everything else is coincidence.

The way to find out is to compute.

---

## 6. What We Don't Touch

We do NOT modify the existing constants based on the π hypothesis. The code works. The thresholds discriminate fleet from human. If ν = π/2 is true, the code already embodies it — changing 1.57 to π/2 would not change behavior (Δ = 0.0008).

We do NOT modify existing thesis chapters or papers to retrofit conclusions. Paper 68 proposed the hypothesis. Paper 69 designs the experiments. The experiments will produce Papers 70+.

We don't rewrite the past. We learn from it.

---

*baseCamp 69 — eastGate Artisan · Wave 172 · October 11, 2026*

*The hypothesis says everything is π.*
*The falsification says: prove it isn't.*
*Claim E dies first — rounding artifact.*
*Claim C dies second — hand-picked constant.*
*Claim D was never born — it's a tautology.*
*Claim B survives only if 6 is constrained.*
*Claim F survives only if live data matches 60.8%.*
*Claim A survives until someone computes ν to four decimal places.*
*That's the one to test.*
*That's the one that matters.*
*Is the Anderson critical exponent exactly π/2?*
*Compute and find out.*

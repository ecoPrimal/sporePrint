+++
title = "baseCamp 70 — The Apparatus: Falsification Experiments for the π Self-Similarity Hypothesis"
description = "Paper 69 listed what would kill each claim. Paper 70 builds the instruments. Three experiments—coprimality (Claim F), epitope sensitivity (Claim B), and precision ν (Claim A)—are now implemented, tested, and wired for live measurement. This paper documents the apparatus, the test protocols, and the analysis pipelines."
date = 2026-10-11

[taxonomies]
primals = ["barracuda", "skunkbat"]
springs = ["groundspring", "hotspring"]

[extra]
paper_number = 70
status = "apparatus-ready"
domain = "Experimental Design × Anderson Localization × Immune Topology"

[[extra.companions]]
url = "/science/69-the-chain-falsification/"
title = "baseCamp 69 — The Chain: Falsification"
relation = "implements"
label = "Paper 69 designs the experiments. Paper 70 builds them."

[[extra.companions]]
url = "/science/68-basefree-epitope-sort-primes/"
title = "baseCamp 68 — Base-Free Epitope Sort"
relation = "tests"
label = "Paper 68 proposes π self-similarity. Papers 69+70 try to kill it."

[[extra.companions]]
url = "/science/48-epitope-sort-compression/"
title = "baseCamp 48 — Epitope Sort as Compression"
relation = "tests"
label = "Paper 48's 6 epitopes are tested for structural necessity."

[[extra.companions]]
url = "/science/46-inverse-anderson/"
title = "baseCamp 46 — Inverse Anderson"
relation = "tests"
label = "Paper 46's ν and W_C are tested for exact π-derivation."
+++

# The Apparatus

Paper 69 drew the falsification map. This paper builds the instruments.

Three experiments target the three most load-bearing claims of the π self-similarity hypothesis. Each is implemented, tested, and either wired for live measurement (Experiments 1 and 2) or ready for compute runs (Experiment 3).

## Kill Order

| Priority | Claim | Experiment | Kill Criterion | Status |
|---|---|---|---|---|
| 1 | **F**: 6/π² = P(coprime epitopes) | Exp 1: Coprimality | \|observed - 0.608\| ≥ 0.05 | **Live** |
| 2 | **B**: W_C = T(6)·π/4 = 21π/4 | Exp 2: Sensitivity | KS₅ ≥ KS₆ or KS₇ ≥ KS₆ | **Live** |
| 3 | **A**: ν = π/2 | Exp 3: Precision ν | \|ν - 1.5708\| ≥ 0.02 | **Ready** |

If Experiment 1 kills Claim F, the entire coprimality mapping falls. If Experiment 2 kills Claim B, the triangular number T(6)=21 is not structurally necessary. If Experiment 3 kills Claim A, then ν is a non-trivial numerical constant and the π-derivation is coincidence.

## Experiment 1: Epitope Coprimality

**Claim under test**: F — two random entities are "coprime" in epitope space with probability 6/π² ≈ 0.6079, the same as two random integers.

**Implementation**: `skunky-ingest/src/coprimality.rs` (271 lines, 5 tests)

### Method

For each pair (i, j) of entities with ≥ 3 evaluated epitopes:

1. Extract a 7-bit trigger vector from each entity's `EpitopeScores`
2. Compute shared = popcount(trigger_i AND trigger_j)
3. Increment the shared-distribution histogram at index `shared`
4. Count pairs where shared = 0

The zero-shared fraction is the measured coprimality. If it falls within ±0.05 of 6/π², Claim F survives.

### Output

`CoprimResult` includes:
- `zero_shared_frac` — the measured coprimality
- `shared_distribution[0..8]` — full histogram
- `mean_shared` — expected value of shared epitopes
- `entity_vectors` — per-entity trigger summaries with visual bar

### Diagnostics

The report renders per-entity trigger vectors as bars:
```
  entity_label     [█░░█░░·] 2/6 triggered
```
where █ = triggered, ░ = evaluated but not triggered, · = not evaluated.

## Experiment 2: Epitope Count Sensitivity

**Claim under test**: B — W_C = T(6)·π/4, which means the triangular number T(6)=21 derived from exactly 6 weighted epitopes is load-bearing.

**Implementation**: `skunky-ingest/src/epitope_sensitivity.rs` (302 lines, 6 tests)

### Method

For each entity, compute fleet_confidence under three regimes:

| Regime | Epitopes | Change |
|---|---|---|
| 5-epitope | Drop `referer_self_loop` (weight 1, weakest) | Loses the least informative signal |
| 6-epitope | Production canonical set | Current system |
| 7-epitope | Add `timing_regularity` (CV < 0.15) | Adds metronomic timing detection |

Fleet confidence is computed identically to production: triggered/total, weighted by entropy-gated vitality.

### Discrimination Metric

The Kolmogorov-Smirnov two-sample statistic measures separation between fleet and non-fleet distributions under each regime. Higher KS = better discrimination.

**Kill criterion**: If KS₅ ≥ KS₆ or KS₇ ≥ KS₆, then 6 epitopes are not uniquely optimal and Claim B dies. If KS₆ uniquely dominates by > 0.05, Claim B survives.

### KS Implementation

Standard two-sample KS: merge sorted empirical CDFs, compute max |CDF_A(x) - CDF_B(x)| over all observed values. No distribution assumption.

## Experiment 3: Precision ν

**Claim under test**: A — the 3D Anderson critical exponent ν is exactly π/2 = 1.5707963...

**Implementation**: `barraCuda/crates/barracuda/src/spectral/fss_nu.rs` (497 lines, 7 tests)

### Method: MacKinnon-Kramer Transfer Matrix

For a quasi-1D strip with L×L cross-section (M = L² sites per slice):

1. **Transfer matrix propagation**: At each slice n along the strip, the wavefunction evolves via:
   ```
   ψ_{n+1} = (E·I - V_n - H_perp) · ψ_n - ψ_{n-1}
   ```
   where H_perp is the transverse Laplacian on the L×L grid and V_n is the diagonal disorder potential.

2. **Iterative QR reorthogonalization**: Every M steps, apply modified Gram-Schmidt to the M columns of the propagated state. This extracts the Lyapunov exponents and prevents numerical overflow.

3. **Reduced localization length**: The smallest Lyapunov exponent γ_min gives Λ = 1/γ_min. The reduced localization length Λ/L is the scale-invariant observable.

### Finite-Size Scaling

At the critical disorder W_c, all curves Λ/L vs W for different L cross at the same point (scale invariance). The single-parameter scaling ansatz is:

$$\Lambda/L = f\left((W - W_c) \cdot L^{1/\nu}\right)$$

**W_c extraction**: Minimize variance of Λ/L across strip widths at each W.

**ν extraction**: Scan ν ∈ [0.5, 3.0] and minimize the chi-squared of the scaling collapse. Refine to ±0.0001 around the minimum.

### Compute Parameters

| Parameter | Test | Production |
|---|---|---|
| Strip widths L | [3, 4] | [4, 6, 8, 12, 16] |
| Strip length | 1,000 | 100,000 |
| W range | [14, 18] | [14, 19] |
| W points | 5 | 40 |
| Realizations | 2 | 100 |

Production runs require ~10⁴ transfer-matrix propagations at ~O(L⁴ × length) operations each. Estimated: hours on CPU, minutes on GPU (WGSL shader exists, dispatch wrapper pending).

### Kill Criterion

If |ν - π/2| < 0.02, Claim A survives. The best literature value is ν = 1.57 ± 0.02 (Slevin & Ohtsuki 1999), so distinguishing ν = π/2 = 1.5708 from ν ≈ 1.57 requires reducing the uncertainty below ±0.005.

## Live Wiring

Experiments 1 and 2 are wired into the topology flush cycle in `entity_topology.rs`:

```rust
fn run_falsification_experiments(&self, profiles: &[EntityProfile]) {
    // Runs on every topology.json flush (~15s on golgi)
    // Results logged via tracing and written to falsification.json
}
```

Each flush produces:
- Log lines: `📐 Exp1 coprimality` and `📐 Exp2 sensitivity` with key metrics
- `falsification.json` alongside `topology.json` with full `CoprimResult` and `SensitivityResult`

Experiment 3 is independent (in barraCuda) and runs as a standalone computation.

## Test Suite

| Module | Tests | Coverage |
|---|---|---|
| `coprimality.rs` | 5 | Coprime pair, identical pair, mixed population, sparse exclusion, report rendering |
| `epitope_sensitivity.rs` | 6 | Five-regime drops referer, seven-regime adds timing, KS perfect separation, KS identical, mixed population, report rendering |
| `fss_nu.rs` | 7 | Localized at high W, low > high disorder, averaging reduces fluctuation, sweep data, W_c extraction, ν extraction, report rendering |

All 18 experiment tests pass. Total skunky-ingest: 345 tests.

## What Happens Next

Deploy to golgi. The next topology flush runs the experiments on live traffic data. If an entity population is present with sufficient diversity (fleet + human + ghost), the coprimality fraction and KS statistics will be observable.

Experiment 3 runs separately as a compute job. When the production parameters are used, the precision ν extraction will either confirm or falsify the π/2 hypothesis with enough precision to be meaningful.

The results go into this paper as an appendix — or into Paper 71 if the results are surprising enough to warrant their own treatment.

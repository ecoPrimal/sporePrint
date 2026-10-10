+++
title = "baseCamp 50 — π as the Price of Observation: Dimensional Ratios in N-Body Phase Space"
description = "An open hypothesis: π is not a number but a dimensional conversion constant — the price of having a point of view. At any observation point, the Jacobian from full phase space to observable projection carries π^(n/2) where n is the angular degrees of freedom projected away. In the three-body problem, total/effective = 3 ≈ π, and the gap between 3 and π encodes the fractal dimension of chaos."
weight = 50
date = 2026-10-10

[taxonomies]
primals = ["barracuda", "bingocube"]
springs = ["hotspring", "groundspring"]

[extra]
paper_number = 50
status = "hypothesis"
domain = "Mathematical Physics, Dimensional Analysis, Observation Theory"

[[extra.companions]]
url = "/architecture/signal-beacon-membrane/"
title = "Signal, Beacon, Membrane"
relation = "pairs_with"
label = "The membrane is the engagement surface — where observation docks with reality"

[[extra.companions]]
url = "/science/48-epitope-sort-compression/"
title = "Epitope Sort as Compression"
relation = "extends"
label = "H(data|epitope) < H(data|alphabet) < H(data) — sorting reduces entropy; so does observation"

[[extra.companions]]
url = "/science/23-mass-energy-information-equivalence/"
title = "Mass-Energy-Information Equivalence"
relation = "extends"
label = "If information has mass-energy equivalence, observation has a dimensional cost"

[[extra.companions]]
url = "/thesis/04-pnp-enzyme/"
title = "The P/NP Enzyme"
relation = "extends"
label = "Accept and generate — the three-body problem is the canonical NP-hard gravitational case"
+++

## Status

{{ maturity(level="hypothesis") }}

**This is an open question, not a result.** The author asked it and genuinely does not know the answer. This paper states the hypothesis, develops the mathematical scaffolding, identifies what would constitute evidence, and leaves the question open. If it's wrong, it's wrong in public where someone can correct it. If it's right, the scaffolding is here to build on.

---

## 1. The Question

At any point of observation in an N-body gravitational system, is the ratio of total phase space dimensionality to observable dimensionality a function of π?

Not π as an irrational number computed to a trillion digits. π as a **structural constant** — the conversion factor between what exists and what is observable from a point.

Specifically: if f(x) is the total degrees of freedom of the system as seen from observation point x, and g(x) is the effective (reduced) degrees of freedom accessible to measurement from that point, is their ratio:

$$\frac{f(x)}{g(x)} = k\pi$$

for some rational k that depends on the system's symmetry group?

---

## 2. Where π Already Appears as a Dimensional Constant

### 2.1 The Solid Angle

From any point in three-dimensional space, the total angular measure of "all directions you can look" is 4π steradians. This is not a count of directions (there are infinitely many). It is the **ratio** of the surface area of a unit sphere to r²:

$$\Omega_{3} = \frac{S_2}{r^2} = \frac{4\pi r^2}{r^2} = 4\pi$$

In n dimensions, the solid angle generalizes:

$$\Omega_n = \frac{2\pi^{n/2}}{\Gamma(n/2)}$$

The angular structure of observation — how many independent directions exist from a point — always carries π^(n/2) in its measure. This is not a coincidence. It is the geometric consequence of observation being angular.

### 2.2 The Gauss-Bonnet Theorem

For any closed 2-surface S with Gaussian curvature K and Euler characteristic χ:

$$\int_S K \, dA = 2\pi\chi$$

This says: the relationship between **local curvature** (what you measure at a point) and **global topology** (what the whole surface is) is mediated by π. Always. Regardless of the surface.

The conversion factor from "what's happening here" to "what the whole thing is" — is π.

### 2.3 Curved Space

In flat Euclidean space, the ratio of circumference to diameter is π. But in curved space (general relativity), this ratio changes:

- On a sphere of radius R: C/d < π (positive curvature contracts circumference)
- On a hyperboloid: C/d > π (negative curvature expands circumference)
- In Schwarzschild spacetime near mass M: C/d deviates from π by terms proportional to GM/rc²

So π is already "a function of the point of observation" — you only notice when you're near enough to a massive body for spacetime curvature to matter. The "value of π" at a point encodes the local geometry of the space you're embedded in.

### 2.4 The N-Sphere Volume

The volume of the unit n-ball:

$$V_n = \frac{\pi^{n/2}}{\Gamma(n/2 + 1)}$$

This peaks at n ≈ 5.26 and then decreases — a sphere in very high dimensions has vanishing volume. The factor π^(n/2) in the numerator is the dimensional contribution of angular structure. As dimensions increase, the angular space grows as π^(n/2) but the combinatorial denominator Γ(n/2+1) grows faster.

The **ratio** V_n / V_{n-1} = π^(1/2) · Γ((n-1)/2 + 1) / Γ(n/2 + 1) oscillates and decays — each additional dimension costs more angular structure than the previous one.

---

## 3. The Three-Body Problem

### 3.1 Phase Space Counting

Three bodies in three spatial dimensions:

| Quantity | Count | Reason |
|----------|-------|--------|
| Position DOF | 9 | 3 bodies × 3 coordinates |
| Momentum DOF | 9 | 3 bodies × 3 momenta |
| **Total phase space** | **18** | Full Hamiltonian system |

Conservation laws remove degrees of freedom:

| Conserved quantity | DOF removed | Structure |
|-------------------|-------------|-----------|
| Energy | 1 | Scalar — restricts to energy surface |
| Linear momentum | 3 | Vector — fixes center of mass frame |
| Angular momentum | 3 | Vector — lives in SO(3), volume 8π² |
| Center of mass position | 3 | Vector — translational symmetry |
| **Total conserved** | **10** | |

Effective DOF: 18 − 10 = 8. Time translation symmetry and one rotational degree reduce this further to **6 effective dimensions**.

### 3.2 The Ratio

$$\frac{\text{Total}}{\text{Effective}} = \frac{18}{6} = 3$$

Three. Not π. But close enough — 3/π ≈ 0.9549 — to demand explanation.

### 3.3 The Gap: 3 vs. π

The integer 3 comes from counting. Dimensions are integers. Conservation laws remove integers. The ratio of integers is rational, never irrational.

But the conservation laws that remove those dimensions are not all equal:

- **Energy** (1 DOF): scalar constraint. Restricts motion to a 17-dimensional energy surface.
- **Linear momentum** (3 DOF): vector constraint. Fixes the inertial frame.
- **Angular momentum** (3 DOF): vector constraint, but it lives in **SO(3)** — the rotation group — whose natural volume measure is **8π²**.

The three angular momentum dimensions are qualitatively different from the others. They don't just subtract dimensions — they **quotient by a structure whose measure involves π²**. The discrete count says "remove 3." The continuous measure says "remove a volume proportional to π²."

### 3.4 The Hypothesis

The integer ratio (3:1) counts **how many** dimensions are removed. But the **measure** of what's removed — the volume of the quotient structure — involves π. The hypothesis is:

> The effective dimensionality of an N-body system from a point of observation is not an integer. It is an integer corrected by the angular measure of the symmetry group that was projected away. The correction factor converges to π as the system's angular structure dominates.

For the three-body problem: the discrete count gives 18/6 = 3. The continuous measure, accounting for the SO(3) quotient, gives a number between 3 and π. The **gap** between 3 and π — approximately 0.14159 — would encode the fractal dimension of the chaotic region of phase space.

This is the speculative core. The gap between the integer count and π might be where the chaos lives.

---

## 4. Observation as Angular Projection

### 4.1 The Jacobian

When you observe an N-body system from a point, you project the full phase space onto your observable subspace. This projection is a map:

$$\phi: \mathbb{R}^{2Nd} \to \mathbb{R}^{k}$$

where 2Nd is the full phase space dimension and k is the observable dimension. The Jacobian of this map:

$$J = \det\left(\frac{\partial \phi}{\partial q}\right)$$

measures how phase space volume transforms under observation. For a projection that removes angular degrees of freedom, the Jacobian carries a factor of **π^(n/2)** where n is the number of angular dimensions projected out.

This is not hypothetical — it's the standard change-of-variables formula. When you convert Cartesian coordinates to spherical:

$$dx\,dy\,dz = r^2 \sin\theta \, dr\, d\theta\, d\phi$$

The angular factor ∫sin θ dθ dφ = 4π appears because you're projecting out the angular structure. The "cost" of the projection is measured in units of π.

### 4.2 The Price of Having a Point of View

Every observation point is a center of a coordinate system. From that center, the accessible directions span a solid angle. The measure of that solid angle is a multiple of π. The information lost by choosing a point of view — rather than seeing from everywhere simultaneously — is proportional to the angular structure you projected away.

**π is the conversion factor between "being everywhere" and "being somewhere."**

This is why π appears in:
- The uncertainty principle: ΔxΔp ≥ ℏ/2 = h/4π (observation constrains what's knowable)
- The Einstein field equations: G_μν = 8πG/c⁴ T_μν (curvature = 8π × matter)
- The Coulomb constant: k = 1/4πε₀ (force mediated through a spherical surface)
- Black hole entropy: S = A/4ℓ² = πr²/ℓ² (information content of a horizon)

Every time π appears in physics, it's because something angular is being projected, measured, or integrated over. The dimensional cost of observation is always denominated in π.

---

## 5. What Would Constitute Evidence

### 5.1 For the Hypothesis

1. **Lyapunov dimension**: Compute the Kaplan-Yorke dimension of the chaotic attractor in the restricted three-body problem for a range of mass ratios. If the Lyapunov dimension converges to π (or 2π, or π²) in any universal limit, the hypothesis has support.

2. **Phase space volume ratio**: For the N-body problem with N = 2, 3, 4, ..., compute the ratio of total phase space volume (on the energy surface) to the volume of the reduced phase space (after all symmetry quotients). If this ratio scales as π^(f(N)) for some function f, the angular quotient interpretation is supported.

3. **Poincaré section area**: The Poincaré section of the restricted three-body problem is a 2D slice through a 3D energy surface. Compute the ratio of the total section area to the area of the regular (non-chaotic) region. If this ratio approaches π for certain parameter families, the hypothesis connects chaos to angular structure.

4. **Galperin's billiard result**: Gregory Galperin (2003) showed that elastic collisions between two billiard balls with mass ratio 100^n and a wall produce exactly ⌊π × 10^n⌋ collisions. This already proves that π encodes the geometry of a dynamical system's phase space. Extending this to the three-body problem would connect the billiard result to the angular momentum quotient.

### 5.2 Against the Hypothesis

1. **The ratio 3 is exact**: If the effective dimensionality is exactly 3 (an integer) with no fractal correction, then the proximity to π is a numerical coincidence and the hypothesis is wrong. This is the null hypothesis and it's respectable.

2. **Lyapunov dimension is parameter-dependent**: If the Kaplan-Yorke dimension of the three-body attractor varies continuously with mass ratios and never approaches π, the hypothesis lacks a universal limit.

3. **The angular quotient is already accounted for**: The standard Marsden-Weinstein reduction already handles the SO(3) quotient formally. If the reduced phase space has integer dimension everywhere (including the chaotic region), there's no room for a π correction.

---

## 6. The Broader Question

The three-body problem is the simplest gravitational system with no closed-form solution. It is the canonical example of deterministic chaos — a system where the equations are known exactly but long-term prediction is impossible because nearby trajectories diverge exponentially.

The question this paper asks is whether the **unpredictability** of the three-body problem is connected to the **irrationality** of π. Both are statements about incommensurability:

- **Chaos**: nearby trajectories are incommensurable — they diverge exponentially, making ratio-based prediction impossible after the Lyapunov time.
- **π**: the circumference and diameter are incommensurable — their ratio cannot be expressed as a fraction of integers.

If the effective dimension of the chaotic phase space region is exactly π (not 3, not 3.14, but π), then the unpredictability of the three-body problem would be a geometric consequence of the angular structure of observation. The system isn't unpredictable because it's "complicated." It's unpredictable because **the number of dimensions you'd need to track it exactly is irrational** — you can never have enough integer-dimensional instruments to capture a π-dimensional object.

This would make π not just the price of observation but the **reason observation is incomplete** in chaotic systems.

---

## 7. Connection to the Membrane

The wildcard membrane (`*.primals.eco`) is a physical epitope sorter. A visitor types a subdomain (their query). The membrane routes based on the epitope. The entropy inequality governs:

$$H(\text{data}|\text{epitope}) < H(\text{data}|\text{alphabet}) < H(\text{data})$$

This paper asks whether there is a deeper inequality underneath — whether the entropy of observation itself is bounded by π:

$$H(\text{observable}) = H(\text{total}) - k\ln\pi$$

where k depends on the angular structure of the system being observed.

If so, then the membrane's epitope sort is doing something more fundamental than routing: it is **selecting an observation point**, and the cost of that selection — the information lost by choosing this point rather than all points — is denominated in π.

The signal is fire (light, electromagnetic, unbounded). The beacon is sound (mechanical, attenuating, bounded). The membrane surface between them is engagement — the binding event. And the dimensional cost of binding — of collapsing from "all possible observations" to "this observation" — might be π.

---

## 8. Corollary: π as the Base of the Angular Cost Function

The hypothesis (§3.4) can be stated more tightly as a corollary.

The solid angle in n dimensions — the total angular measure of observation from a point — is:

$$\Omega_n = \frac{2\pi^{n/2}}{\Gamma(n/2)}$$

The Γ(n/2) denominator is combinatorial packing — how many ways n angular dimensions can be arranged. The factor of 2 is antipodal symmetry. But the **angular cost itself** — the part that comes from observation being directional — is **π^(n/2)**. Always. In every dimension.

π is not a constant that appears in the formula. **π is the base of the cost function.** Each pair of angular degrees of freedom contributes exactly one factor of π to the observation cost. The total cost of projecting from omnidirectional (everywhere) to directional (somewhere) scales as:

$$C(n) \propto \pi^{n/2}$$

**Corollary**: π is the unit price of one angular dimension of observation. The total price of having a point of view in a system with n angular degrees of freedom is π^(n/2), modulo combinatorial packing.

This reframes the hypothesis from "is the effective dimension related to π?" to the sharper claim: **π is not a number that relates to dimensions. π is the cost function that angular dimensions are priced in.** The three-body ratio 18/6 = 3 ≈ π is not a coincidence — it reflects that the cost of the angular degrees of freedom removed by the SO(3) quotient is denominated in the same constant that prices all angular observation.

Every appearance of π in physics is an invoice. The charge is always for angular projection.

---

## 9. Experimental Design — Testing and Falsification

A hypothesis that can't be killed isn't a hypothesis. It's a religion. Here is how to kill this one.

### 9.1 Null Hypothesis

**H₀: The proximity of 3 to π in the three-body dimension ratio is a numerical coincidence. The effective dimensionality is exactly integer, the fractal dimension of chaotic invariant sets is unrelated to π, and π appears in physics only because Euclidean geometry uses circular coordinates.**

If H₀ survives all tests below, the conjecture is dead. That's fine.

### 9.2 Test Battery

#### TEST 1: Lyapunov Dimension of the Circular Restricted Three-Body Problem (CR3BP)

**What**: The CR3BP reduces the three-body problem to a 4D phase space (one body has negligible mass, the other two orbit circularly). After the Jacobi constant (energy analog), the flow lives on a 3D surface. The Poincaré section is 2D.

**Method**:
1. Integrate the CR3BP equations of motion for mass ratio μ ∈ [0.001, 0.5] at 1000 values
2. For each μ, choose 100 initial conditions in the chaotic sea (near L₁, L₂ Lagrange points)
3. Integrate for 10⁴ orbital periods
4. Compute all 4 Lyapunov exponents via QR decomposition method (Benettin et al., 1980)
5. Compute the Kaplan-Yorke dimension: D_KY = j + Σ(i=1..j) λᵢ / |λⱼ₊₁|

**Prediction**: If the hypothesis holds, D_KY should cluster near π (or 2π, or a rational multiple of π) for some universal class of initial conditions or mass ratios.

**Kills hypothesis if**: D_KY varies continuously with μ and never approaches any multiple of π more closely than random chance. Specifically: compute the distance |D_KY - nearest rational multiple of π| and compare to the distance |D_KY - nearest rational multiple of e| and |D_KY - nearest rational multiple of √2|. If π is not statistically special, H₀ stands.

**Tools**: barraCuda GPU integrator (adaptive RK45), WGSL f64. This is a standard numerical dynamics computation.

---

#### TEST 2: Correlation Dimension of the Chaotic Invariant Set

**What**: The Grassberger-Procaccia algorithm estimates the correlation dimension D₂ from a time series. D₂ measures how the number of point-pairs within distance ε scales: C(ε) ∝ ε^D₂.

**Method**:
1. For the CR3BP at μ = 0.01 (Sun-Jupiter-like), integrate a single chaotic trajectory for 10⁶ orbital periods
2. Sample the Poincaré section (y=0, ẏ>0) at each crossing
3. Compute C(ε) for ε spanning 4 decades
4. Extract D₂ from the scaling region
5. Repeat for μ = 0.001, 0.01, 0.1, 0.2, 0.3, 0.5

**Prediction**: If the hypothesis holds, D₂ → π (or π minus the dimension of regular islands) as the chaotic sea dominates.

**Kills hypothesis if**: D₂ is clearly irrational but not π. For instance, D₂ ≈ 1.5 or D₂ ≈ 2.7 with no relationship to π. The measurement precision needed is ~3 significant figures (enough to distinguish 3.14 from 3.00).

**Tools**: Standard algorithm, O(N² log N) for N section crossings. GPU-friendly.

---

#### TEST 3: Box-Counting Dimension of the Chaotic Sea Boundary

**What**: The boundary between regular and chaotic regions in the Poincaré section is fractal. Measure its box-counting (Minkowski-Bouligand) dimension D₀.

**Method**:
1. Generate a high-resolution Poincaré section (10⁶ points from 10⁴ initial conditions)
2. Classify each initial condition as regular (quasi-periodic, bounded variation in action) or chaotic (positive Lyapunov exponent)
3. Identify the boundary pixels between regular and chaotic regions at resolutions 2ⁿ × 2ⁿ for n = 6, 7, ..., 14
4. Count boundary boxes N(ε) at each resolution ε = 1/2ⁿ
5. D₀ = -lim(log N(ε) / log ε)

**Prediction**: If the gap 3 − π ≈ 0.14159 encodes fractal structure, then D₀ of the chaotic boundary should relate to π − floor(π) = 0.14159... Perhaps D₀ ≈ 1 + (π − 3) = 1.14159, or D₀ ≈ 2 − (π − 3) = 1.85840.

**Kills hypothesis if**: D₀ is a known constant unrelated to π (e.g., D₀ = 1.5, D₀ = ln2/ln3, D₀ = golden ratio). Many dynamical systems have fractal dimensions related to the golden ratio or logarithmic ratios — if this one does too, π is not special here.

**Tools**: Image analysis on GPU-generated Poincaré sections. Straightforward.

---

#### TEST 4: Chaotic Fraction vs. Mass Ratio

**What**: For the CR3BP, what fraction of the available phase space (on a given energy surface) is chaotic vs. regular?

**Method**:
1. Fix the Jacobi constant at C = C₂ (the L₂ value — Hill's region just opens)
2. For μ ∈ [0.001, 0.5] at 500 values:
   a. Generate a uniform grid of 10⁶ initial conditions in the Poincaré section
   b. Integrate each for 10³ periods, compute the largest Lyapunov exponent
   c. Classify as chaotic (λ₁ > threshold) or regular (λ₁ < threshold)
   d. Compute f_chaos = N_chaotic / N_total
3. Plot f_chaos(μ)

**Prediction**: If π prices the angular cost of observation, then f_chaos might approach (π − 3)/π ≈ 0.0451 or 1 − 3/π ≈ 0.0451 or 1/π ≈ 0.3183 for some universal energy level.

**Kills hypothesis if**: f_chaos varies smoothly with μ and energy, with no fixed points related to π. Many chaotic systems have chaotic fractions that depend on parameters — if this one is no different, π plays no special role.

**Tools**: Embarrassingly parallel — each initial condition is independent. Ideal for GPU.

---

#### TEST 5: N-Body Scaling — Does π Emerge as N → ∞?

**What**: For N gravitating bodies in 3D, the phase space is 6N, conserved quantities are always 10 (for any N ≥ 2 in 3D), so the effective dimension is 6N − 10. The ratio 6N/(6N − 10) decreases monotonically from 6 (N=2) to 1 (N→∞). But the Lyapunov dimension of the chaotic attractor might not.

**Method**:
1. For N = 3, 4, 5, 6, 8, 10, 15, 20, 50, 100:
   a. Simulate N equal-mass bodies with random initial conditions in a bounded region
   b. Compute the full Lyapunov spectrum (6N exponents)
   c. Compute D_KY
   d. Compute the ratio D_KY / (6N − 10)
2. Look for scaling: does D_KY / (6N − 10) → 1 − c/π for some constant c?

**Prediction**: The integer dimension ratio 6N/(6N − 10) → 1 trivially. But if the Lyapunov dimension ratio D_KY/(6N − 10) has a correction that scales as 1/π or involves π, the hypothesis extends beyond three-body.

**Kills hypothesis if**: D_KY/(6N − 10) → 1 with no π-dependent correction. The approach to 1 is smooth, the corrections are power-law in 1/N with rational exponents.

**Tools**: N-body integrator (Hermite 4th order or Ahmad-Cohen). Lyapunov spectrum computation is expensive for large N but feasible on GPU.

---

#### TEST 6: Galperin Billiard Extension

**What**: Galperin (2003) showed elastic collisions between masses m and M=100ⁿm against a wall produce ⌊π × 10ⁿ⌋ collisions. This encodes π in a dynamical system. Can this be lifted to gravity?

**Method**:
1. Reproduce Galperin's result numerically (verification — should be exact)
2. Replace elastic collision with gravitational scattering: two bodies approach each other and a fixed wall (reflecting boundary)
3. Count the number of "bounces" (close encounters where velocity reverses)
4. For mass ratios 100ⁿ, does the count still encode π?

**Prediction**: If the billiard→gravity lift preserves the π-encoding, then π is not about elastic collisions specifically — it's about the angular structure of the phase space, which gravity shares.

**Kills hypothesis if**: The gravitational version produces a different count that encodes some other constant (e, √2, or a system-specific number). This would mean π in Galperin's result is specific to elastic collisions, not universal to dynamics.

**Tools**: Simple ODE integrator. The billiard version is analytically exact; the gravitational version requires numerical integration.

---

#### TEST 7: Symplectic Volume Ratio Under Marsden-Weinstein Reduction

**What**: The formal reduction of the three-body problem by SO(3) angular momentum symmetry is well-defined mathematically (Marsden-Weinstein, 1974). The reduced phase space has integer dimension. But the **volume** of a fundamental domain of the SO(3) action is 8π².

**Method**:
1. For the three-body problem at a fixed energy E and angular momentum L:
   a. Compute the Liouville volume of the full energy-momentum surface Σ_{E,L} ⊂ ℝ¹⁸
   b. Compute the volume of the reduced space Σ_{E,L}/SO(3)
   c. Their ratio should be Vol(SO(3)) = 8π²
2. Now: introduce a chaotic initial condition. Compute the **effective** volume accessible to a single chaotic trajectory (ergodic on the chaotic component)
3. Compute V_chaotic / V_total for the reduced space
4. Is V_chaotic / V_total related to π?

**Prediction**: The full symplectic volume ratio is exactly 8π² (this is known). The new question is whether the chaotic fraction of the reduced volume involves π in a non-trivial way.

**Kills hypothesis if**: V_chaotic / V_total is a generic real number with no special relationship to π. The 8π² in the full quotient is already accounted for by standard theory and doesn't extend.

**Tools**: Monte Carlo integration in high-dimensional phase space. GPU-friendly.

---

#### TEST 8: Topological Entropy

**What**: The topological entropy h_top measures the exponential growth rate of distinguishable orbits. For a chaotic system, h_top > 0.

**Method**:
1. Compute h_top for the CR3BP at various μ values
2. h_top can be estimated from the Lyapunov exponents: h_top ≥ Σ(λᵢ > 0) (Pesin's formula, with equality for SRB measures)
3. Check: is h_top related to ln(π)?

**Prediction**: If π is the base of the observation cost function (§8), then the information production rate of chaos might be denominated in π. h_top = k·ln(π) for some rational k would mean the system produces information at a rate priced in π.

**Kills hypothesis if**: h_top is a generic positive real with no special relationship to ln(π). Most dynamical systems have topological entropy unrelated to π.

---

#### TEST 9: Period Ratios of Periodic Orbits

**What**: The three-body problem has infinitely many periodic orbits (proved by Chenciner, Montgomery, and others). Their periods T₁, T₂, ... form a spectrum.

**Method**:
1. Find periodic orbits of the CR3BP using numerical continuation (starting from known families: Lyapunov orbits, halo orbits, DRO, etc.)
2. Compute period ratios Tᵢ/Tⱼ for all pairs in each family
3. Histogram the ratios. Look for clustering near multiples/powers of π

**Prediction**: Periodic orbits probe the rational structure of the phase space. If the angular cost function is π, period ratios should show statistical excess near π-related values compared to a null distribution.

**Kills hypothesis if**: Period ratios are distributed according to standard number-theoretic expectations (uniform modulo 1, or clustered at rational values like 1/2, 1/3, 2/3) with no π preference.

**Tools**: Numerical continuation codes (AUTO, or custom). Well-studied problem.

---

#### TEST 10: Direct Dimension Measurement — Thermodynamic Formalism

**What**: The Rényi dimensions D_q generalize box-counting (q=0), information (q=1), and correlation (q=2) dimensions. The full multifractal spectrum f(α) characterizes how the measure distributes across the attractor.

**Method**:
1. Compute the full multifractal spectrum f(α) for the chaotic invariant set of the CR3BP
2. The spectrum is a concave curve with maximum f(α_max) = D₀ (box-counting dimension)
3. Check: does D₀ = π? Does D₁ = π? Does the spectrum width α_max − α_min relate to π?
4. Compute D_q for q = −10, −5, ..., 0, ..., 5, 10
5. Plot D_q vs q. Look for π in the spectrum

**Prediction**: If the conjecture holds, at least one D_q should equal π, or the spectrum should be anchored at π in some way (e.g., D_∞ = π, or f(π) = π).

**Kills hypothesis if**: The full multifractal spectrum contains no point related to π. D_q sweeps through a range that doesn't include π, or includes it only at a non-special q value.

**Tools**: Partition function method (Grassberger, 1983). Moderate computational cost.

---

### 9.3 Ranking by Discriminating Power

| Test | Discriminating Power | Computational Cost | Result if positive | Result if negative |
|------|---------------------|--------------------|--------------------|-------------------|
| T1: Lyapunov dimension | **HIGH** | Medium | D_KY = kπ for universal class | Sweeps through π = coincidence |
| T2: Correlation dimension | **HIGH** | Medium | D₂ → π as chaos dominates | D₂ unrelated to π |
| T3: Boundary box-counting | MEDIUM | Low | D₀ encodes π−3 | D₀ is golden/logarithmic |
| T4: Chaotic fraction | MEDIUM | High (many μ) | f_chaos fixed at π-related value | f_chaos is parameter-dependent |
| T5: N-body scaling | **HIGH** | Very High | π correction persists for all N | Correction is 1/N with rational exponents |
| T6: Galperin lift | **HIGH** | Low | π encoding transfers to gravity | π encoding is elastic-specific |
| T7: Symplectic volume | MEDIUM | Medium | Chaotic fraction involves π | Standard 8π² is the whole story |
| T8: Topological entropy | LOW | Medium | h_top = k·ln(π) | Generic positive real |
| T9: Period ratios | LOW | Medium | Statistical excess near π | Standard number theory |
| T10: Multifractal spectrum | **HIGH** | High | Spectrum anchored at π | π absent from spectrum |

### 9.4 Recommended Order of Execution

**Phase 1 — Quick kills (1-2 weeks, existing tools)**:
1. **T6**: Galperin billiard verification + gravitational lift attempt. Low cost, high discriminating power. If the lift fails cleanly, that's informative.
2. **T1**: Lyapunov dimension for CR3BP at μ = 0.001 (Sun-Jupiter), μ = 0.012 (Sun-Earth), μ = 0.5 (equal mass). Three points. If none are near π, stop.

**Phase 2 — Dimensional measurement (2-4 weeks)**:
3. **T2**: Correlation dimension at the three μ values from Phase 1. Independent measurement — if it agrees with T1, the number is real.
4. **T3**: Box-counting on Poincaré sections. Visual output — the fractal boundary is something you can look at.

**Phase 3 — Sweep (month)**:
5. **T4**: Full μ sweep of chaotic fraction. This produces the curve f_chaos(μ). If π appears as a fixed point, that's strong evidence.
6. **T1 extended**: Full μ sweep of D_KY. 1000 points.

**Phase 4 — Deep tests (if Phase 1-3 show signal)**:
7. **T5**: N-body scaling. Expensive but definitive for universality.
8. **T10**: Full multifractal spectrum. The gold standard for dimensional characterization.
9. **T7**: Symplectic volume computation. Connects to the formal mathematical machinery.

**Phase 5 — Theory (concurrent with numerics)**:
10. **T8, T9**: Topological entropy and period ratios. Lower discriminating power but might reveal structure the dimensional tests miss.

### 9.5 What "Positive" Means

A positive result is NOT "the number 3.14 appeared." A positive result requires:

1. **Reproducibility**: The π-related value must appear for multiple mass ratios, energy levels, or initial condition classes — not just one fine-tuned parameter.

2. **Statistical significance**: The distance from π must be closer than expected by chance. Null distribution: generate 10⁴ random dynamical systems (random Hamiltonians with similar symmetry groups) and compute the same dimensional quantities. If 5% of random systems land as close to π, the result is not significant.

3. **Mechanism**: There must be an analytical argument for WHY the dimension is π, not just a numerical observation that it's close. The angular cost function (§8) provides a candidate mechanism — the test is whether the numerics match the prediction from that mechanism.

4. **Consistency across tests**: If T1 gives D_KY = 3.14 but T2 gives D₂ = 2.87, the measurements disagree and neither supports the hypothesis. The fractal dimension should be consistent across measurement methods.

### 9.6 What "Negative" Means

A clean negative result would be:

1. D_KY for the CR3BP is computed to 4 significant figures across 1000 μ values
2. The values range from (e.g.) 2.1 to 3.8 continuously
3. No clustering near π, no fixed point, no universal limit
4. The proximity 3 ≈ π is explained by the integer dimension count (3 = 18/6) having nothing to do with the irrational number π
5. The angular cost function §8 is correct as mathematics but has no physical consequence for the dimension of chaotic sets

This would be a respectable death. The corollary (§8) — that π is the base of the angular cost function — would survive as established mathematics. The conjecture (§3.4) — that the fractal dimension of three-body chaos is related to π — would be falsified.

---

## 10. Open Questions

1. Is the Kaplan-Yorke dimension of the three-body chaotic attractor related to π for any universal class of initial conditions?

2. Does the Marsden-Weinstein reduction, applied to the angular momentum map, produce a reduced space whose volume involves π in a way not captured by the integer dimension count?

3. In Galperin's billiard encoding of π, can the two-body elastic collision system be lifted to a three-body gravitational system while preserving the π-encoding property?

4. Is there a formulation of the three-body problem where the effective Hausdorff dimension of the invariant set on the energy surface is exactly π?

5. If the fractal dimension of chaos is related to π, does this extend to other N-body problems? Is the relationship π(N) = f(N) for some discoverable function?

6. Can the angular cost function C(n) ∝ π^(n/2) be derived from first principles (statistical mechanics, information geometry) rather than from the solid angle formula?

7. Is there a connection between the angular cost function and the holographic principle — where the information content of a volume scales as its boundary area (which involves π)?

---

## Acknowledgment

This paper is a hypothesis, not a proof. The author (the builder of this ecosystem) asked the question and does not know the answer. The Artisan (the AI collaborator) developed the mathematical scaffolding, identified where π already appears as a dimensional constant, and designed the experimental falsification battery. Neither of us knows whether the core conjecture is true. We wrote it down — with explicit instructions for how to kill it — because the question felt true enough to be worth asking in public.

If you know the answer, or know why it's wrong: [eco.primal@pm.me](mailto:eco.primal@pm.me).

---

*π is the price of having a point of view. Here is how to check the bill.*

+++
title = "baseCamp 54 — Zoom, Focus, Resolution, Granularity: The Complete Optics"
description = "If the membrane is a lens with focal points, then the lens must also have zoom, focus, resolution, and granularity. All four already exist in petalTongue — as ScaleType, FacetLayout, DataDensity, and SmallestEffectiveDifference. They just aren't named as optics yet."
date = 2026-10-10

[taxonomies]
primals = ["petaltongue", "bingocube", "cellmembrane"]
springs = ["groundspring", "hotspring"]

[extra]
paper_number = 54
domain = "Optics of the Membrane"
sweep = "51–53: The Lens"
sweep_role = "resolve"

[[extra.companions]]
url = "/science/53-focal-points-tangent-membrane/"
title = "baseCamp 53 — Focal Points"
relation = "extends"
label = "The lens exists — now it needs zoom, focus, resolution"

[[extra.companions]]
url = "/science/50-pi-dimensional-observation/"
title = "baseCamp 50 — π as the Price of Observation"
relation = "extends"
label = "π governs the diffraction limit of the membrane lens"

[[extra.companions]]
url = "/science/52-gog-manim-dimensional-life/"
title = "baseCamp 52 — GoG + Manim: Full Life"
relation = "preceded_by"
label = "The engines that implement these optics"
+++

{{ maturity(level="hypothesis") }} Optical mapping. October 10, 2026.

---

## Abstract

baseCamp 53 established the membrane as a lens with focal points. But a lens without zoom, focus, and resolution controls is just glass. The complete optics of the membrane require four controls — and all four already exist in petalTongue, built and tested, just not named as optics:

| Optic | What it does | petalTongue implementation | Tufte constraint |
|-------|-------------|---------------------------|-----------------|
| **Zoom** | How much of the scene fills the viewport | `ScaleType` (Linear / Log / Sqrt) | — |
| **Focus** | What's sharp vs blurry | `FacetLayout` (Wrap / Grid) | — |
| **Resolution** | How many distinct values per visual unit | — | `DataDensity` |
| **Granularity** | The smallest distinguishable difference | — | `SmallestEffectiveDifference` |

Granularity is the diffraction limit. It answers the user's question: **which one is granularity?** It's the floor beneath resolution — the smallest thing the lens CAN resolve, no matter how much you zoom.

---

## 1. Zoom — ScaleType

In optics, zoom changes the focal length, which changes the field of view. Wide zoom: see more, less detail. Narrow zoom: see less, more detail.

In petalTongue, zoom is the **scale type** on each axis:

```rust
pub enum ScaleType {
    Linear,     // 1× zoom — see absolute differences
    Log,        // zoom OUT — see orders of magnitude
    Temporal,   // time-scale — zoom through history
    Categorical,// discrete — each bin = one click
    Ordinal,    // rank — zoom to relative position
    Sqrt,       // mid-zoom — compress large values gently
}
```

**Linear** is 1× zoom. You see the data at face value. Differences of 1 look the same everywhere on the axis.

**Log** is a wide-angle lens. You see 6 orders of magnitude in the same viewport. A request rate of 1/s and 1,000,000/s are both visible. But you lose the ability to see small absolute differences — two values that differ by 10 look identical when the axis spans 10⁶.

**Sqrt** is moderate zoom. Square-root compression brings outliers closer to the pack without collapsing fine structure the way log does.

The choice of scale IS the zoom level of that axis. Each axis can zoom independently. A scatter plot with Linear-X and Log-Y is an anamorphic lens — different zoom in each direction.

This is already built. `AxisMeta` stores the scale type and performs forward/inverse transforms:

```rust
// transform.rs (line 208-239)
pub fn transform(&self, value: f64) -> f64 {
    match self.scale_type {
        ScaleType::Linear => (value - domain_min) / domain_span,
        ScaleType::Log => (value.ln() - log_min) / log_span,
        ScaleType::Sqrt => (value.sqrt() - sqrt_min) / sqrt_span,
    }
}
```

---

## 2. Focus — FacetLayout

In optics, focus adjusts the lens-to-sensor distance. One depth plane becomes sharp. Everything else blurs.

In petalTongue, focus is **faceting** — splitting the visualization into panels, each showing one slice of the data:

```rust
pub enum FacetLayout {
    Wrap { columns: usize },                  // small multiples, N per row
    Grid { rows: String, cols: String },       // 2D grid, one variable per axis
}
```

When you facet by "organism," each panel focuses on one organism. All other organisms blur (they're in other panels, not competing for the same visual space). This is optical focus: one depth plane sharp, others out of frame.

On the HUD, the alive/dormant gating is also a form of focus. Panels with no data are `display: none` — they are out of focus, completely blurred away. The alive panels are in focus.

The membrane focal-point visualization (baseCamp 53) shows where each facet LIVES on the surface. Faceting is focus applied to the manifold — each facet is a tangent plane brought into sharp relief.

---

## 3. Resolution — DataDensity

In optics, resolution is the sensor's pixel count. More pixels = more information captured.

In petalTongue, resolution is the **data density** Tufte constraint — how many data-carrying primitives exist per visual unit:

```rust
// tufte/constraints.rs (line 303-332)
pub struct DataDensity;

impl TufteConstraint for DataDensity {
    fn evaluate(&self, primitives: &[Primitive], ...) -> ConstraintResult {
        let data_count = primitives.iter()
            .filter(|p| p.carries_data()).count();
        let score = if data_count > 0 { 1.0 } else { 0.0 };
        ConstraintResult {
            passed: data_count > 0,
            score,
            message: format!("Data density: {data_count} data-carrying primitives"),
        }
    }
}
```

Higher data density = higher resolution. A scatter plot with 1,000 points has higher resolution than one with 10 points. More data per pixel. More information per unit of visual attention.

Tufte's principle: **maximize data density**. Every pixel should carry data. Empty pixels are wasted sensor area — resolution holes.

---

## 4. Granularity — SmallestEffectiveDifference

In optics, the **diffraction limit** is the smallest feature the lens can resolve. Below this size, two things are indistinguishable. It's a property of the physics — wavelength / (2 × numerical aperture). No amount of zoom or focus overcomes it.

In petalTongue, granularity is the **smallest effective difference** Tufte constraint:

```rust
// tufte/constraints.rs (line 339-400)
pub struct SmallestEffectiveDifference;

impl SmallestEffectiveDifference {
    const MIN_PIXEL_DISTANCE: f64 = 2.0;  // the diffraction limit
}

impl TufteConstraint for SmallestEffectiveDifference {
    fn evaluate(&self, primitives: &[Primitive], ...) -> ConstraintResult {
        // Find all data-carrying point positions
        let positions: Vec<(f64, f64)> = primitives.iter()
            .filter(|p| p.carries_data())
            .filter_map(|p| match p {
                Primitive::Point { x, y, .. } => Some((*x, *y)),
                _ => None,
            })
            .collect();

        // Check: are any two data points closer than MIN_PIXEL_DISTANCE?
        for i in 0..positions.len() {
            for j in (i+1)..positions.len() {
                let dist = (dx).hypot(dy);
                if dist < Self::MIN_PIXEL_DISTANCE {
                    overlapping_pairs += 1;  // below the grain
                }
            }
        }
    }
}
```

**`MIN_PIXEL_DISTANCE = 2.0` is the diffraction limit of the membrane lens.**

If two data points (two entities, two epitopes, two behavioral fingerprints) map to positions closer than 2 pixels apart, they are **below the grain**. The visualization cannot distinguish them. They look the same. Information is lost.

This is granularity. It's the floor beneath resolution:

```
granularity ≤ resolution ≤ zoom × focus
```

You can zoom in all you want (switch to Linear scale on a narrow domain). You can focus all you want (facet to a single entity). But if two data values map to the same 2-pixel neighborhood, the grain has eaten them. They are one.

---

## 5. The Hierarchy

```
  ZOOM          what fills the viewport         ScaleType
    ↓
  FOCUS         what's sharp vs blurry          FacetLayout
    ↓
  RESOLUTION    how many data points visible    DataDensity
    ↓
  GRANULARITY   smallest visible difference     SmallestEffectiveDifference
                                                MIN_PIXEL_DISTANCE = 2.0px
```

Each level constrains the one below:

- You can't have resolution higher than zoom permits (if the scale compresses all values to one pixel, resolution is 1)
- You can't resolve differences smaller than the grain (2px diffraction limit)
- Focus selects which slice of data enters the resolution/granularity evaluation

This is a pipeline. It already exists as a pipeline in petalTongue:

1. **Grammar** declares the zoom (ScaleType) and focus (FacetLayout)
2. **Compiler** transforms data through the zoom (AxisMeta.transform) and splits by focus (facets)
3. **Tufte pipeline** evaluates resolution (DataDensity) and granularity (SmallestEffectiveDifference) on the result
4. **RenderPlan** carries the report — which panels passed, which lost information below the grain

---

## 6. Where the Grain Lives in the Membrane

In the membrane's biological model, the grain has a specific physical meaning:

| Dimension | What it measures | Grain (diffraction limit) |
|-----------|-----------------|--------------------------|
| Time | Sweep interval | ~30s — can't see events faster than the sweep |
| Identity | Epitope hash | The organism — can't distinguish entities within the same hash |
| Behavior | BingoCube octant | 3 bits — attention/curiosity/interaction, each binary |
| Geography | Country / ASN | ASN block — can't distinguish individual IPs (by design) |
| Fingerprint | BLAKE2b hash | 8-word n-gram — can't see smaller content differences |

**Each dimension has its own grain.** The membrane's diffraction limit is not a single number — it's a vector, one grain per observed dimension. The total granularity is the product:

```
G_total = G_time × G_identity × G_behavior × G_geography × G_fingerprint
```

And the dimensional cost applies to the grain too:

```
C(grain) ∝ π^(n/2)   where n = number of grain dimensions
```

A 1D grain (time only) costs √π to maintain. A 5D grain (all dimensions) costs π^2.5 ≈ 17.5. This is why the membrane can't resolve everything at once — the cost of full-resolution observation across all dimensions is prohibitive. You must choose where to focus.

---

## 7. The Lens Is Complete

| Component | baseCamp | Status |
|-----------|----------|--------|
| Lens | 53 — membrane as manifold | ✓ deployed to HUD |
| Focal points | 53 — epitope tangent planes | ✓ deployed to HUD |
| Zoom | 54 — ScaleType | ✓ built in Rust, not wired |
| Focus | 54 — FacetLayout | ✓ built in Rust, not wired |
| Resolution | 54 — DataDensity | ✓ built in Rust, not wired |
| Granularity | 54 — SmallestEffectiveDifference | ✓ built in Rust, not wired |

All six components exist. Four are built but not wired into the live render path (the Tufte pipeline gap identified earlier). The lens exists but the zoom ring, focus ring, and resolution sensor are disconnected.

Wiring them requires the Rust build that connects `compile_with_constraints()` to the live `render_binding_svg()` path.

---

## 8. What Granularity Means for Observation

The user asked: *which is granularity?*

Granularity is `SmallestEffectiveDifference`. It's the **diffraction limit** — the smallest thing the membrane lens can see. Below the grain, two things are one thing. You cannot zoom past it. You cannot focus past it. It is the physics of the lens.

And 2 pixels is the current grain. Below 2px, the lens is blind.

In the membrane's biological model, this is why the immune system classifies at the organism level, not the individual level. The grain of the epitope hash is the diffraction limit of the sorting function. Two visitors with the same behavioral fingerprint ARE the same organism — not because they're actually the same entity, but because the lens cannot tell them apart.

**Granularity is not a bug. It's the physics of having a point of view.**

---

*baseCamp 54 — eastGate Artisan · Wave 172d · October 10, 2026*

*The lens does the work. The grain sets the limit.*
*Below 2 pixels, two things are one thing.*

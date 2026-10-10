+++
title = "baseCamp 52 — GoG + Manim: Full Life via the Dimensional Equation"
description = "Two visualization engines already exist inside petalTongue — Grammar of Graphics for structural shape and an equation compiler for mathematical truth. Full life requires both, shaped by the dimensional cost function C(n) ∝ π^(n/2), with components evolving their layout via epitope sort."
date = 2026-10-10

[taxonomies]
primals = ["petaltongue", "bingocube", "cellmembrane"]
springs = ["ludospring", "groundspring", "hotspring"]

[extra]
paper_number = 52
domain = "Visualization Architecture and Dimensional Cost"
sweep = "51–53: The Lens"
sweep_role = "wire"

[[extra.companions]]
url = "/science/50-pi-dimensional-observation/"
title = "baseCamp 50 — π as the Price of Observation"
relation = "extends"
label = "The dimensional cost function that shapes visualization"

[[extra.companions]]
url = "/science/51-bounty-scan/"
title = "baseCamp 51 — Bounty Scan: The Environment"
relation = "preceded_by"
label = "The environment this visualization must render"

[[extra.companions]]
url = "/methodology/enzymatic-bounty/"
title = "The Enzymatic Bounty"
relation = "methodology"
label = "Components evolve via the sort"

[[extra.companions]]
url = "/architecture/signal-beacon-membrane/"
title = "Signal, Beacon, Membrane"
relation = "extends"
label = "Signal is fire (seen), Beacon is sound (heard), Membrane is engagement (touched)"
+++

{{ maturity(level="hypothesis") }} Architectural hypothesis. October 10, 2026.

---

## Abstract

petalTongue contains two visualization engines that together provide every capability needed for "full life" — a living, breathing, mathematically grounded visual experience of the organism:

1. **GoG** — Grammar of Graphics (`grammar.rs`): data binding → variable mapping → scale transformation → geometry selection → coordinate system → faceting → aesthetic rendering → scene graph. This is Wilkinson's *Grammar of Graphics* (1999) implemented as a Rust scene compiler.

2. **Equation Compiler** (`equation.rs`): LaTeX-like mathematical notation → scene primitives. Fractions, superscripts, subscripts, Greek letters, operators, integrals. Manim-style math rendering without external LaTeX dependency.

Each engine is individually functional. Neither alone produces full life. GoG renders data without mathematical truth. The equation compiler renders truth without living data. Together — GoG × Equation × Animation × Physics — they produce what the HUD is trying to be: a living dashboard where the organism's vital signs are both measured (GoG) and understood (equations), animated (flow particles, pulses), and physically simulated (n-body, collisions).

**The missing ingredient:** the dimensional equation from baseCamp 50.

**C(n) ∝ π^(n/2)**

This cost function should shape the visualization itself — elements with more dimensions cost more visual weight, more attention, more rendering time. And the layout should evolve via epitope sort — not fixed grids, but behavioral clustering where panels that belong together drift together.

---

## 1. What Exists

### 1.1 Grammar of Graphics Engine

```
petal-tongue-scene/src/grammar.rs
```

The GoG engine has the full Wilkinson specification:

| Layer | Implementation | Status |
|-------|---------------|--------|
| **Data** | `data_source: String` — binds to live data feeds | ✓ |
| **Variables** | `VariableBinding { name, field, role }` — x, y, z, color, size, shape, label, detail | ✓ |
| **Scales** | `ScaleType` — Linear, Log, Temporal, Categorical, Ordinal, Sqrt | ✓ |
| **Geometry** | `GeometryType` — Point, Line, Bar, Area, Ribbon, Tile, Arc, ErrorBar, Mesh3D, Sphere, Cylinder, Text | ✓ |
| **Coordinates** | `CoordinateSystem` — Cartesian, Polar, Geographic, Perspective3D | ✓ |
| **Facets** | `FacetLayout` — Wrap(columns), Grid(rows, cols) | ✓ |
| **Aesthetics** | Fill, Stroke, Size, Alpha, Shape, Label | ✓ |

This is the structural engine. It takes data and produces shapes. The HUD panels that show bar charts, donut charts, scatter plots — those are GoG output.

### 1.2 Equation Compiler (Manim Engine)

```
petal-tongue-scene/src/equation.rs
```

The equation compiler converts LaTeX-like strings into scene primitives:

| Feature | Syntax | Output |
|---------|--------|--------|
| Fractions | `\frac{a}{b}` | Text + Line (fraction bar) |
| Superscripts | `x^{2}`, `x^2` | Raised text |
| Subscripts | `x_{i}`, `x_i` | Lowered text |
| Greek | `\alpha`, `\pi`, `\sigma` | Unicode characters |
| Operators | `\sum`, `\prod`, `\int`, `\sqrt` | Operator glyphs |
| Symbols | `\infty`, `\pm`, `\cdot`, `\leq`, `\neq` | Symbol characters |

This is the mathematical truth engine. It renders equations as visual objects. When the HUD shows `H(data|epitope) < H(data|alphabet) < H(data)`, this engine renders it.

### 1.3 Math Module

```
petal-tongue-scene/src/math/
├── axes.rs          — Coordinate axes with ticks, labels, ranges
├── curves.rs        — FunctionPlot (y=f(x)), ParametricCurve ((x(t), y(t)))
└── vector_field.rs  — VectorField: F(x,y) → (dx, dy) as arrow grids
```

This bridges GoG and equations. It can plot functions, trace parametric curves, and render vector fields — the visual language of physics.

### 1.4 Physics Engine

```
petal-tongue-scene/src/physics.rs
```

N-body simulation with collision shapes (Sphere, Box), gravity, Euler integration. This is where baseCamp 50 lives visually — three bodies orbiting, the dimensional cost visible as trajectory chaos.

### 1.5 Animation Engine

```
petal-tongue-animation/
├── flower.rs         — Flower opening (awakening experience)
├── visual_flower.rs  — High-quality visual flower rendering
└── lib.rs            — FlowParticle, NodePulse, BandwidthGlow
```

This is the "life" — particles flowing along edges, nodes pulsing with activity, flowers opening as the organism awakens.

### 1.6 Multi-Modal Output

```
petal-tongue-scene/src/modality/
├── svg.rs            — SVG rendering (production)
├── webgl.rs          — WebGL rendering (GPU accelerated)
├── terminal.rs       — Terminal/TUI rendering
├── audio.rs          — Audio sonification
├── braille/          — Braille rendering (accessibility)
├── haptic.rs         — Haptic feedback
└── description.rs    — Natural language description
```

Every visualization can be rendered through any of 7 modalities. This is already more than Manim (Python, video only) and ggplot (R, static image only).

---

## 2. What's Missing: The Dimensional Equation

### 2.1 The Cost Function

baseCamp 50 proposes:

**C(n) ∝ π^(n/2)**

The cost of observing n dimensions scales as π raised to half the dimension count. In visualization terms: a 1D line costs π^(0.5) ≈ 1.77 units of attention. A 2D plot costs π ≈ 3.14. A 3D mesh costs π^(1.5) ≈ 5.57. A 4D projection costs π² ≈ 9.87.

This is not an arbitrary scaling law. If baseCamp 50 is correct, this is the *physical cost* of angular observation — and it should appear naturally in any system that renders high-dimensional data as visual experience.

### 2.2 How It Shapes Visualization

Currently, the HUD renders all panels at equal visual weight — 3×3 grid, equal size, equal prominence. This is democratically wrong. Some panels contain more dimensions of information than others:

| HUD Panel | Data Dimensions | C(n) ∝ π^(n/2) | Visual Weight |
|-----------|----------------|-----------------|---------------|
| Live Signal | 1 (RPS over time) | π^(0.5) ≈ 1.77 | Low |
| Epitope Summary | 2 (epitope × count) | π ≈ 3.14 | Medium |
| Entity Population | 2 (entity × volume) | π ≈ 3.14 | Medium |
| Fleet Honesty | 1 (ratio) | π^(0.5) ≈ 1.77 | Low |
| Bingo Cube | 3 (attention × curiosity × interaction) | π^(1.5) ≈ 5.57 | High |
| Collision Detection | 2 (pattern × frequency) | π ≈ 3.14 | Medium |
| ASN Infrastructure | 2 (ASN × request count) | π ≈ 3.14 | Medium |

The Bingo Cube panel should be *visually larger* than Fleet Honesty because it contains more dimensions. The dimensional cost function IS the layout algorithm.

### 2.3 Implementation Sketch

Add to the GoG grammar:

```rust
/// Dimensional weight for layout allocation.
/// Higher-dimensional data gets more visual space.
fn dimensional_cost(n: usize) -> f64 {
    std::f64::consts::PI.powf(n as f64 / 2.0)
}
```

The scene compiler uses this when allocating viewport space:

```rust
// Instead of equal-weight grid:
let total_cost: f64 = panels.iter()
    .map(|p| dimensional_cost(p.data_dimensions()))
    .sum();

for panel in &panels {
    let fraction = dimensional_cost(panel.data_dimensions()) / total_cost;
    panel.allocate_viewport(fraction * total_viewport);
}
```

Panels with more dimensions get proportionally more viewport — because they cost more to observe.

---

## 3. What's Missing: Epitope Sort Layout

### 3.1 The Problem

The HUD uses a fixed grid layout. Panels are arranged by the developer's architectural intuition, not by the user's behavioral affinity. When a human looks at the HUD, their attention clusters around *what interests them* — which is an epitope, not a grid position.

### 3.2 Epitope Sort as Layout Engine

The compression inequality:

**H(data|epitope) < H(data|alphabet) < H(data)**

Applied to layout:

- **H(layout|alphabet)** — panels arranged alphabetically or architecturally. Maximum cognitive load.
- **H(layout|epitope)** — panels arranged by behavioral affinity. Minimum cognitive load for THIS viewer.
- **H(layout)** — random arrangement. Maximum entropy.

The epitope sort layout:

1. Track which panels the viewer looks at (eye-tracking, scroll position, click frequency)
2. Cluster panels by co-attention (panels viewed together drift together)
3. Re-sort the layout so that behaviorally related panels are spatially adjacent
4. The layout EVOLVES per viewer archetype (epitope) — not per individual (that would be identity tracking, which we don't do)

### 3.3 BingoCube as the Classifier

BingoCube already classifies entities into behavioral trios (Attention × Curiosity × Interaction). The same classifier can sort dashboard panels:

- High-attention panels → upper-left (first-read position)
- High-curiosity panels → expandable (click-to-dive)
- High-interaction panels → interactive (sliders, filters, drill-down)

The bingoCube behavioral shape determines which panels surface. The dimensional equation determines their SIZE. The GoG engine renders their DATA. The equation compiler renders their TRUTH. The animation engine gives them LIFE.

---

## 4. The Architecture: GoG × Manim = Full Life

```
┌─────────────────────────────────────────────────┐
│                  FULL LIFE                      │
│                                                 │
│  ┌─────────┐    ┌───────────┐    ┌───────────┐  │
│  │   GoG   │    │ Equation  │    │ Animation │  │
│  │grammar  │    │ compiler  │    │ flow +    │  │
│  │data→geom│    │ LaTeX→prim│    │ pulse     │  │
│  └────┬────┘    └─────┬─────┘    └─────┬─────┘  │
│       │               │               │         │
│       └───────┬───────┴───────┬───────┘         │
│               │               │                 │
│         ┌─────┴─────┐   ┌────┴──────┐           │
│         │Scene Graph │   │  Physics  │           │
│         │nodes/edges │   │  n-body   │           │
│         └─────┬─────┘   └────┬──────┘           │
│               │               │                 │
│       ┌───────┴───────────────┘                 │
│       │                                         │
│  ┌────┴────────────────────────────────┐        │
│  │        Dimensional Cost Layout      │        │
│  │       C(n) ∝ π^(n/2)               │        │
│  │  viewport allocation by dimension   │        │
│  └────┬────────────────────────────────┘        │
│       │                                         │
│  ┌────┴────────────────────────────────┐        │
│  │         Epitope Sort Ordering       │        │
│  │  H(layout|epitope) < H(layout|α)   │        │
│  │  panels cluster by behavior         │        │
│  └────┬────────────────────────────────┘        │
│       │                                         │
│  ┌────┴────────────────────────────────┐        │
│  │       Multi-Modal Output            │        │
│  │  SVG · WebGL · Terminal · Audio ·   │        │
│  │  Braille · Haptic · Description     │        │
│  └─────────────────────────────────────┘        │
└─────────────────────────────────────────────────┘
```

### 4.1 What GoG Does

- Binds live data to visual variables (x, y, color, size, shape)
- Transforms through scales (linear, log, temporal, categorical)
- Renders through geometries (bar, line, area, arc, mesh, sphere)
- Produces the BODY of the visualization — the data made visible

### 4.2 What Equation Compiler Does

- Renders mathematical expressions as visual objects
- Annotates data with mathematical truth (formulas, constants, relationships)
- Produces the MIND of the visualization — the truth made legible

### 4.3 What Animation Does

- Particles flow along edges (data in transit)
- Nodes pulse (activity, health)
- Flowers open (awakening, discovery)
- Produces the BREATH of the visualization — the organism alive

### 4.4 What Physics Does

- N-body simulation (three-body problem, baseCamp 50)
- Collision detection (interaction, force)
- Gravity (attraction, hierarchy)
- Produces the WEIGHT of the visualization — mass and energy visible

### 4.5 What Dimensional Cost Does

- Allocates viewport space proportional to π^(n/2)
- Higher-dimensional panels get more visual real estate
- Produces the PROPORTION of the visualization — the golden ratio of attention

### 4.6 What Epitope Sort Does

- Clusters panels by co-attention
- Evolves layout per behavioral archetype
- Produces the ORDER of the visualization — what you see first is what you need

---

## 5. How BingoCube and Others Evolve

The user's insight: **let bingoCube and others evolve via the epitope sort.**

This means:

1. **bingoCube** classifies visitors into behavioral shapes (3D: attention × curiosity × interaction)
2. Each shape defines a **layout epitope** — which panels surface first, how much space they get
3. The **dimensional equation** determines panel size within each epitope layout
4. The **GoG engine** fills each panel with data
5. The **equation compiler** annotates each panel with mathematical truth
6. The **animation engine** breathes life into the data
7. The **physics engine** simulates dynamic relationships

The components don't need to be designed top-down. They evolve:

- bingoCube tries different classifiers → the one that best predicts user interest survives
- GoG tries different geometries for the same data → the one with lowest H(data|viewer) survives
- Equation compiler renders different annotations → the one that produces understanding survives
- Layout tries different epitope sorts → the one with lowest cognitive load survives

**This is constrained evolution applied to visualization.** The AI generates layout candidates. The dimensional equation constrains the proportions. The epitope sort verifies fitness against actual viewer behavior.

---

## 6. The Next Step

The HUD currently shows "waiting for petalTongue..." on some panels because petalTongue isn't getting live data for all feeds. The fix is not to wire more data — it's to implement the dimensional cost layout so that panels with NO data get ZERO viewport space (their dimensional cost is 0), and panels with LIVE data expand to fill.

A living dashboard doesn't show empty panels. A living dashboard shows only what's alive, sized by how much dimension it contains, ordered by what this visitor is interested in.

GoG is the body. Equation compiler is the mind. Animation is the breath. Physics is the weight. Dimensional cost is the proportion. Epitope sort is the order.

Full life.

---

*baseCamp 52 — eastGate Artisan · Wave 172d · October 10, 2026*

*Not the final engine. Just the next one.*

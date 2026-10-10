+++
title = "baseCamp 58 — Tufte Pipeline Wiring + Rotation Unlock"
description = "compile_with_constraints wired through compile_faceted into render_binding_svg and render_binding_webgl. SVG compiler upgraded from flatten() to flatten_3d() + Camera::project(). 7 Tufte constraints active on every render. 405 tests, 0 failures."
weight = 58
date = 2026-10-10

[taxonomies]
primals = ["petaltongue"]
springs = []

[extra]
status = "wired"
baseCamp = 58
maturity = "architectural"
sweep = "58: Tufte Wiring"
sweep_role = "evolution"
+++

## What Changed

Two convergence targets from baseCamp 57 resolved in a single commit.

### 1. Tufte Pipeline → Compilation Path

The 7 Tufte constraints existed as evaluation-only (`TufteReport::evaluate_all()`). They could score a scene graph but had no effect on the compilation pipeline. This commit wires them into the production render path.

**Before:**
```
DataBinding → compile_faceted() → SceneGraph → SVG
```

**After:**
```
DataBinding → compile_with_constraints() → (SceneGraph, TufteReport) → SVG
                    ↓
             compile_faceted()  (facets preserved)
                    ↓
             evaluate_all()     (7 constraints scored)
                    ↓
             warn if score < 0.7
```

#### Files changed

| File | Change |
|---|---|
| `compiler/mod.rs` | `compile_with_constraints` now routes through `compile_faceted` instead of `compile` |
| `runtime.rs` | `render_binding_svg` and `render_binding_webgl` both use `compile_with_constraints` with full constraint set |
| `runtime.rs` | `DEFAULT_CONSTRAINTS` constant: all 7 Tufte constraints |

#### Constraints active on every render

1. **DataInkRatio** — ratio of data-bearing to total ink
2. **LieFactor** — visual effect vs data effect proportionality
3. **ChartjunkDetection** — non-data decoration detection
4. **DataDensity** — information per unit area
5. **SmallestEffectiveDifference** — minimum visual distinction
6. **ColorAccessibility** — WCAG contrast compliance
7. **SmallMultiplesPreference** — facet layout scoring

When `overall_score < 0.7`, each failing constraint is logged at `WARN` level with its name, score, and message.

### 2. Rotation Unlock — SVG Compiler 3D Projection

The SVG compiler called `scene.flatten()` which returns `(Transform2D, &Primitive)` — all 3D transforms were silently dropped. Scenes with `Transform3D` rotations or translations on the Z axis rendered as if those transforms didn't exist.

**Before:**
```
scene.flatten()  →  Transform2D  →  transform.apply(x, y)
```

**After:**
```
scene.flatten_3d()  →  Transform3D  →  project_point(transform, camera, x, y)
                                              ↓
                                        world transform (4×4 matrix multiply)
                                              ↓
                                        Camera::project(wx, wy, wz)
                                              ↓
                                        Orthographic: pass-through (vx, vy)
                                        Perspective: frustum projection
```

#### Camera::project

- **Orthographic** (default for 2D): subtracts camera position, drops Z. Identity camera = coordinates pass through unchanged. Full backward compatibility.
- **Perspective**: applies `fov_y`-based frustum projection with near-plane clamping, maps to viewport coordinates.

#### Files changed

| File | Change |
|---|---|
| `transform.rs` | Added `Camera::project()` method |
| `modality/svg.rs` | `compile()` uses `flatten_3d()` + camera |
| `modality/svg.rs` | Added `project_point()` helper (3D world transform → camera projection) |
| `modality/svg.rs` | `emit_primitive()` signature: `Transform2D` → `Transform3D` + `Camera` |

### Test Results

- 405 tests, 0 failures, 1 ignored
- All 26 SVG-specific tests pass
- All 10 determinism tests pass (including `determinism_with_tufte_constraints_100_runs`)
- All 8 e2e integration tests pass

### Deployed

Binary deployed to golgiBody (`/opt/membrane/petaltongue`), service `membrane-petaltongue` restarted. Health check: `v1.7.0`, status `ok`.

## What's Next

From the convergence frontier identified in baseCamp 57:

1. **Auto-correction**: constraints currently evaluate and warn. Next evolution: constraints that can auto-correct (e.g., `DataInkRatio` removes decoration, `ColorAccessibility` adjusts colors)
2. **hud-pt.js convergence** (912 lines): the animation engine bridge — connect Rust `FlowParticle`/`NodePulse`/`BandwidthGlow` to the HUD
3. **Dark theme SVG**: scene-level theme switching in the compilation pipeline

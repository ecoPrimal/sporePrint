+++
title = "AAR: WateringHole Convergence Scan"
date = 2026-10-10
[taxonomies]
domains = ["signal-processing"]
[extra]
status = "scan"
baseCamp = 57
maturity = "architectural"
sweep = "57: Convergence"
sweep_role = "scan"
+++

## After Action Report: Wave 172d — WateringHole & Convergence Scan

This is a scan of the full codebase, identifying what has converged to Rust, what remains hand-rolled in Python/Bash/JS, and where the convergence frontier is.

---

## What Was Done (Wave 172d)

### Infrastructure Grid SVG — tuebor.primals.eco

Built a visual SVG diagram for the Infrastructure Grid analysis page on tuebor.primals.eco:

- **11 nodes** mapped in two-column layout: INDIVIDUAL HUMAN ← → ENTITY INFRASTRUCTURE
- **Color coded** by node type: red (no protection), blue (infrastructure), orange (dark money), green (social), purple (legal)
- **Dashed arrows** show data flow direction — → to entity, ← entity acts on individual
- **Quagmire Solutions** hub node at bottom center connects FOIAworks + Court Filing
- **Harassment Domains** overlay node connects to GoDaddy

**Technical path**: Inline SVG in Zola markdown breaks (Zola inserts `<p>` tags at blank lines inside `<svg>`). Solution: compress SVG to single line inside a `<div>` wrapper. Also deployed as static file at `/img/infrastructure-grid-map.svg`. Cursor browser webview strips `<svg>` and `<img>` elements (security sandbox), but real browsers render correctly.

### Particle Animation System — hud.primals.eco

Built live particle animation on the membrane visualization:

- **FlowParticles** spawn outside the membrane circle and transit inward
- **Tangent points pulse** on particle arrival (scale 2.2 → decay 0.92)
- **Category arcs glow** with bandwidth (stroke-width + opacity modulation)
- **requestAnimationFrame** at 60fps with particle lifecycle management
- Global state: `mgParticles[]`, `mgPulses{}`, `mgArcGlow{}`

### baseCamps 54–56 Published

Three new science papers on sporePrint:

1. **baseCamp 54** — Zoom, Focus, Resolution, Granularity: complete optics of the membrane lens
2. **baseCamp 55** — Rotation locked, Anderson locality, seeing the wind
3. **baseCamp 56** — Signal transit through membranes, known at time n = P

---

## Convergence Scan: What Language Is Everything In?

### Converged to Rust (the primals) — 16 crates

| Primal | Role | Status |
|--------|------|--------|
| barraCuda | HTTP behavioral classifier | ✓ Production |
| bearDog | Ed25519 signing, ChaCha20, HKDF | ✓ Production |
| bingoCube | Behavioral trio classifier | ✓ Production |
| biomeOS | Neural API orchestrator | ✓ Production |
| coralReef | Coral reef consensus | ✓ Production |
| loamSpine | Spine data structure, session commits | ✓ Production |
| nestGate | Content-addressed storage, BLAKE3, CAS | ✓ Production |
| petalTongue | Grammar of Graphics, Tufte pipeline | ✓ Production (HUD) |
| rhizoCrypt | DAG events, Merkle trees, dehydration | ✓ Production |
| skunkBat | Entity classifier, scatter detection | ✓ Production |
| songBird | WebSocket mesh, gossip protocol | ✓ Production |
| sourDough | Validation suite (replaces braid_pentest.py) | ✓ Production |
| squirrel | Universal patterns, MCP bridge | ✓ Production |
| swarmVine | Swarm coordination | ✓ Production |
| sweetGrass | Braid provenance, PROV-O/JSON-LD | ✓ Production |
| toadStool | Gateway proxy | ✓ Production |

**Total Rust**: 16 primals, all deployed to golgiBody.

### Fossilized Python (converged → Rust) — 6 scripts

All in `infra/fossilRecord/` with `# FOSSILIZED` header:

| Script | Replaced By |
|--------|-------------|
| `native_braid.py` (1,326 lines) | `membrane content.braid` CLI → Rust pipeline |
| `braid_pentest.py` (1,336 lines) | `sourdough validate neural-api --suite braid-pentest` |
| `fleet-phenotype.py` | `entity_classifier.rs` in skunkBat |
| `epitope_bridge.py` | `caddy_bridge.rs` |
| `membrane-breathe-active-wave171.py` | `membrane_stack.rs` in skunky-ingest |
| `membrane-breathe-jellystein-wave171.py` | `membrane_stack.rs` in skunky-ingest |

**Total fossilized Python**: ~4,000 lines, all replaced by Rust.

### Active Python — 5 tools (3,675 lines)

These are *legitimately* Python — they're user-facing tools, not pipeline code:

| Script | Lines | Purpose | Convergence? |
|--------|-------|---------|-------------|
| `skunkBat/tools/antidote.py` | 723 | Scatter content identification & remediation | Keep — CLI tool for humans |
| `skunkBat/tools/uv-lamp.py` | 634 | Fluorescent tag scanner | Keep — CLI tool |
| `skunkBat/tools/ingestion-observer.py` | 575 | Persistent scatter ingestion sentinel | Keep — monitoring |
| `songBird/examples/clients/python/songbird_client.py` | 528 | Python WebSocket client example | Keep — SDK example |
| `songBird/examples/clients/python/websocket_client.py` | 492 | Python WebSocket client example | Keep — SDK example |

**Verdict**: These stay Python. They're tools for human operators and SDK examples — the right language for the job. No convergence needed.

### Active Bash — 5 scripts (2,332 lines)

| Script | Lines | Purpose | Convergence? |
|--------|-------|---------|-------------|
| `wateringHole/provision/provision-golgi.sh` | 987 | Full golgiBody provisioning | Keep — deployment script |
| `wateringHole/tools/overwatch.sh` | 483 | System monitoring dashboard | Keep — ops tool |
| `wateringHole/provision/provision-golgi-layer.sh` | 302 | Layer provisioning | Keep — deployment |
| `wateringHole/tools/membrane-monitor.sh` | 315 | Membrane health monitoring | Keep — ops |
| `wateringHole/scripts/overwatch-temporal.sh` | 245 | Temporal overwatch | Keep — ops |

**Verdict**: Bash for ops/provisioning is the correct choice. No convergence needed.

### Active JavaScript — 1 file (912 lines)

| File | Lines | Purpose | Convergence? |
|------|-------|---------|-------------|
| `hud/site/public/js/hud-pt.js` | 912 | HUD membrane visualization + particle system | **Convergence target** → petalTongue SVG compiler |

**This is the convergence frontier.** The HUD JS is hand-rolling what petalTongue's grammar of graphics + animation engine should be generating. When the Tufte pipeline is wired (`compile_with_constraints()` instead of `compile_faceted()`), the JS shrinks to a thin WebSocket client.

### Elixir — 0 files

No Elixir anywhere in the codebase. Clean.

---

## The Convergence Frontier

### Tier 1: Wire It (code exists, needs connection)

1. **Tufte pipeline** — `render_binding_svg()` in `runtime.rs` calls `compile_faceted()` but should call `compile_with_constraints()`. The constraints (DataDensity, SmallestEffectiveDifference) are built. The compiler is built. The call site just isn't wired.

2. **Rotation unlock** — `svg.rs` calls `scene.flatten()` → Transform2D. The 3D path `flatten_3d()` exists with Camera and Projection (Orthographic/Perspective) support. Just never called from the SVG compiler.

3. **Animation engine** — `FlowParticle`, `NodePulse`, `BandwidthGlow` structs exist in `petal-tongue-animation/src/lib.rs`. The JS particle system is hand-rolling the same concepts. When the Tufte pipeline emits SVG with animation hints, the JS becomes a thin renderer.

### Tier 2: Evolve It (architecture exists, needs implementation)

4. **Dark theme SVG** — SVG compiler outputs white-on-transparent. Needs theme-aware color emission.

5. **petalTongue → HUD live pipeline** — Currently HUD fetches raw JSON from `/api/bindings` and JS renders. Future: petalTongue compiles SVG server-side, HUD receives finished SVG via WebSocket, JS just mounts.

### Tier 3: Scan For (not yet discovered)

6. **What else is hand-rolled?** — The tuebor site has inline `<script>` blocks in Zola templates (`desk.html`, `membrane.html`, `map.html`). These are page-specific interactive JS. Convergence target: when petalTongue can emit interactive SVG, these shrink.

---

## Deprecated Stack Inventory

### `infra/fossilRecord/scripts/deprecated_wave157h/` — 12 Python scripts

These were the pre-Rust data pipeline: `bulk_braid.py`, `convergence_drain.py`, `alphafold_prov_convoy.py`, etc. All replaced by Rust primals. Retained as archaeological evidence per Process Stratigraphy (baseCamp 35).

### `infra/fossilRecord/scripts/deprecated_wave167/` — 4 Python scripts

The next generation: `native_braid.py` (middle-out parallel), `braid_pentest.py` (8-level test harness). These were substantial engineering — the native_braid.py is 1,326 lines of production-quality Python with file locking, NVMe staging, batch processing. All replaced by Rust.

### `infra/fossilRecord/plasmidBin-wave157h/` — 21 Bash scripts

Pre-membrane provisioning scripts. Retained for reference.

---

## Summary Counts

| Category | Files | Lines | Language | Status |
|----------|-------|-------|----------|--------|
| Rust primals | 16 crates | ~45,000+ | Rust | ✓ Production |
| Active Python tools | 5 | 3,675 | Python | Keep (correct language) |
| Active Bash ops | 5 | 2,332 | Bash | Keep (correct language) |
| Active JS (HUD) | 1 | 912 | JavaScript | **Convergence target** |
| Fossilized Python | 6 | ~4,000 | Python | Replaced by Rust |
| Deprecated Python | 16 | ~6,000+ | Python | Archived |
| Deprecated Bash | 21+ | ~3,000+ | Bash | Archived |
| Elixir | 0 | 0 | — | Never existed |
| gardens (upstream) | ~50+ | varies | Python/Rust | External (bonsai-bt, lithoSpore, NUCLEUS) |
| springs (science) | ~100+ | varies | Python | Science notebooks (correct language) |

**The system is 95%+ Rust for production.** Python survives only as CLI tools for humans and science notebooks. Bash survives only as ops scripts. The one remaining convergence frontier is `hud-pt.js` (912 lines of hand-rolled SVG/animation that petalTongue should be generating).

---

## Giscus (Noted)

The tuebor.primals.eco Discuss boxes show "An error occurred: giscus is not installed on" because the giscus GitHub App isn't installed on `amicusContra/tuebor`. Requires GitHub admin action. Not blocking — Signal boxes work, Discuss is supplementary.

---

## Next

- Wire `compile_with_constraints()` in `runtime.rs` (Tier 1, item 1)
- Unlock rotation in SVG compiler (Tier 1, item 2)  
- Bridge animation engine to HUD (Tier 1, item 3)
- Each of these shrinks the hand-rolled JS toward zero

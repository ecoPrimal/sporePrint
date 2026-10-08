+++
title = "petalTongue — Live on hud.primals.eco"
description = "Universal User Interface primal deployed as headless web server. WebSocket JSON-RPC bridge, grammar-of-graphics scene compiler, Anderson selective permeability rendered live."
date = 2026-10-08
weight = 2

[extra]
maturity = "live"
validated_on_hardware = true
+++

> **Validated live** — petalTongue v1.7.0 serving at `hud.primals.eco` on golgiBody.
> WebSocket JSON-RPC bridge verified. Scene compiler producing SVG + WebGL output.

## What petalTongue Is

petalTongue is the **Universal User Interface** primal — an 18-crate Rust system that renders data across four modalities from the same codebase:

| Modality | Technology | Status |
|----------|-----------|--------|
| Desktop GUI | egui/eframe | Built, not deployed on golgiBody |
| Terminal TUI | ratatui/crossterm | Built, not deployed on golgiBody |
| Web server | axum + tower | **LIVE** — v1.7.0 headless on golgiBody |
| Browser WASM | wasm-bindgen | Crate exists (593KB), not yet wired to HUD |

The headless build (`--no-default-features`) strips all GUI/TUI dependencies, producing an 8.4MB static musl binary that serves the axum web stack only.

## Live Endpoints

All endpoints at `hud.primals.eco` (also `biomeos.primals.eco`, `os.primals.eco`):

| Endpoint | Method | Response |
|----------|--------|----------|
| `/health` | GET | `{"mode":"web","primal":"petalTongue","status":"ok","version":"1.7.0"}` |
| `/health/liveness` | GET | Kubernetes-style liveness probe |
| `/health/readiness` | GET | Kubernetes-style readiness probe |
| `/api/status` | GET | Mode, version, neural API availability |
| `/api/primals` | GET | Connected primals (empty in tutorial mode) |
| `/api/ecosystem` | GET | Ecosystem metrics (gates, GPU nodes) |
| `/api/snapshot` | GET | Current scene graph state |
| `/api/gate-mesh` | GET | Gate enrollment and links |
| `/api/physical-topology` | GET | Hardware topology (CRS310, Flints, Omada) |
| `/api/mesh-peers` | GET | WireGuard mesh peer state |
| `/api/primal-health` | GET | Per-primal health metrics |
| `/api/events` | GET (SSE) | Server-sent event stream |
| `/ws` | WebSocket | JSON-RPC bridge to embedded platform runtime |
| `/ws/scene` | WebSocket | Scene streaming for WebGL rendering |
| `/viz/{slug}` | GET | Visualization pages |

**27 API endpoints**, all returning 200.

## WebSocket JSON-RPC Bridge

The most powerful capability: any computational actor can connect to `wss://hud.primals.eco/ws` and invoke petalTongue's embedded platform runtime directly.

### Available Methods

| Method | What It Does |
|--------|-------------|
| `health.check` | Runtime health → `{"status":"ok","state":"Running"}` |
| `capabilities.list` | Self-discovery of available methods |
| `pt.state` | Runtime lifecycle state |
| `pt.metrics` | Real-time CPU %, memory, core count from golgiBody |
| `pt.scenarios` | Built-in visualization scenario catalog (8 scenarios) |
| `pt.render_svg` | Scenario → SVG via grammar-of-graphics compiler |
| `pt.render_binding` | Custom DataBinding → SVG |
| `pt.render_webgl` | Custom DataBinding → GPU draw calls + view-projection matrix |

### DataBinding Channel Types

The `pt.render_binding` and `pt.render_webgl` methods accept arbitrary data in these channel types:

| Channel Type | Required Fields |
|---|---|
| `timeseries` | `id`, `label`, `x_label`, `y_label`, `unit`, `x_values`, `y_values` |
| `bar` | `id`, `label`, `categories`, `values`, `unit` |
| `gauge` | `id`, `label`, `value`, `min`, `max`, `unit`, `normal_range`, `warning_range` |
| `heatmap` | `id`, `label`, `x_labels`, `y_labels`, `values` (row-major), `unit` |
| `scatter` | `id`, `label`, `x`, `y`, `unit` |
| `scatter3d` | `id`, `label`, `x`, `y`, `z`, `unit` |
| `distribution` | `id`, `label`, `unit`, `values`, `mean`, `std`, `comparison_value` |
| `faceted_bar` | `id`, `label`, `group_by`, `groups` (key + categories + values), `unit`, `columns`, `normalization` |
| `faceted_gauge` | `id`, `label`, `group_by`, `gauges` (key + value + min/max + ranges), `unit`, `columns` |
| `donut` | `id`, `label`, `categories`, `values`, `unit` |
| `game_scene` | `id`, `label`, `scene` (tilemap, sprites, entities) |
| `soundscape` | `id`, `label`, `definition` (layers, waveforms) |

### Normalization

Bar, heatmap, faceted_bar, and faceted_gauge channels accept an optional `normalization` field:

| Strategy | Range | Description |
|----------|-------|-------------|
| `none` | raw | Default — backward compatible, no transformation |
| `min_max` | [0, 1] | Per-column linear scaling — used for mixed-metric panels |
| `symmetric` | [-1, 1] | Centered scaling — shows direction + magnitude |
| `z_score` | σ units | Standard deviations from mean |
| `log1p` | compressed | ln(1 + \|x\|) · sign(x) — compresses large ranges |
| `rank` | [0, 1] | Ordinal percentile — robust to outliers |
| `leaky_relu` | mixed | max(α·x, x) — preserves negative values with reduced magnitude |

Per-column independence: each category column is normalized independently across all groups. Original values are preserved for labels; only the rendering geometry uses normalized scale.

## Built-in Scenarios

petalTongue ships 8 visualization scenarios across two domains:

### Agriculture (airSpring)

| Scenario | Scenes | Physics |
|----------|--------|---------|
| `airspring.et0` | `daily_et0`, `monthly_et0` | Reference evapotranspiration |
| `airspring.richards_pde` | `moisture_field` | Richards PDE soil moisture (16.7KB SVG) |
| `airspring.crop_coefficient` | `kc_gauge`, `kc_stages` | Crop coefficient (Kc) |
| `airspring.drought_index` | `spi_timeseries` | Drought Index (SPI/SPEI) |

### Measurement (groundSpring)

| Scenario | Scenes | Physics |
|----------|--------|---------|
| `groundspring.seismic` | `wave_field`, `arrival_times` | Seismic wave propagation (21.5KB SVG) |
| `groundspring.anderson_localization` | `localization_heatmap` | Anderson localization (14KB SVG) |
| `groundspring.sensor_drift` | `drift_timeseries` | Sensor calibration drift |
| `groundspring.spectral_reconstruction` | `power_spectrum` | Spectral reconstruction |

All 11 scenes render to SVG in under 100ms total.

## Anderson Selective Permeability — Rendered Live

Paper 43 defines the **permeability tensor** P(ω, W_ω, d_ω) for mode-dependent transport through biological membranes. BarraCuda implements the formulas. The agent computed 6 biological systems and rendered each through petalTongue:

| System | Modes | Selectivity S | Rendered as |
|--------|-------|--------------|-------------|
| Commensal Relay | 5 | **1.000** | Heatmap + Gauge |
| Gut Epithelium | 4 | **1.000** | Heatmap + Gauge |
| Healthy Skin (d=2) | 4 | **1.000** | Heatmap + Gauge |
| AD Skin (d→3, breach) | 4 | **0.000** | Heatmap + Gauge |
| Fleet (S=0) | 4 | **0.000** | Heatmap + Gauge |
| No-Till Soil | 4 | **0.743** | Heatmap + Gauge |

Plus: permeability tensor heatmap (22KB), selectivity comparison bars (5.8KB), AD dimensional promotion curve (5.7KB), disorder sweeps at d=1,2,3 (19KB), Anderson phase space scatter (7.3KB + 52 WebGL draw calls).

**Total**: 15 SVGs + 1 WebGL scene, ~103KB, rendered in 1.1 seconds over the live WebSocket bridge.

## Architecture

```
Caddy TLS (:443)
  ├── /api/* /health /ws /viz  →  reverse_proxy 127.0.0.1:8092
  ├── /ops/*                   →  basicauth + file_server
  └── /*                       →  Zola static site (HUD dashboard)

petaltongue-hud.service (:8092)
  └── petaltongue web --bind 127.0.0.1:8092
      --docroot /opt/ecoPrimals/hud/site/public
      --spa --allowed-origins "*" --cache-ttl 30
```

The split routing pattern serves static Zola pages for the dashboard and reverse-proxies API/WS traffic to petalTongue. Both share the same domain aliases: `hud.primals.eco`, `biomeos.primals.eco`, `os.primals.eco`.

## Privacy Invariant

- No cookies, no tracking pixels, no JS analytics
- No IP addresses stored in any API response
- CORS enabled for cross-origin rendering, no session state
- petalTongue web mode is stateless — no auth cookies, no user tracking

## Cross-Site Bridge Architecture

All 4 primals.eco sites with petalTongue panels share a common bridge module:

```
pt-bridge-core.js (251 lines — single source of truth)
  ├── PetalBridge(config)        — WS connect, JSON-RPC 2.0, SVG inject
  ├── classifyOrganism(cluster)  — unified behavioral heuristic
  └── build*() helpers           — shared faceted panel builders
         ↓
signal-pt.js (335 lines) — 22 panels, cross-origin data
hud-pt.js    (309 lines) — 22 panels, same-origin WS
thesis-pt.js (237 lines) — 14 panels + 5 shared faceted
detroit-pt.js(376 lines) — 19 panels, graph data (no organism heuristic)
```

### Panel Consolidation

The faceting subsystem replaced 9 separate bars with 3 faceted small-multiples + donuts per site:

| Before | After | Effect |
|--------|-------|--------|
| 4 organism bars (IPs, UA, blame, lang) | 1 faceted_bar + 1 donut | Small multiples per organism |
| 4 entity bars (CV, chrome, blame, RPS) | 1 faceted_gauge + 1 faceted_bar | Per-entity gauge + profile |
| 3 detroit bars (nodes, flows, communities) | 3 donut charts | Proportional arcs |
| 1 detroit bar (per-court capture) | 1 faceted_gauge | Per-court capture ratio |

Total: 87 panels → 77 panels across all sites. Fewer panels, more information per panel.

## What's Next

| Phase | Goal | Status |
|-------|------|--------|
| Motor wiring | skunky-ingest → petalTongue motor → SSE push | Planned |
| WASM rendering | Replace hud-core.js with petal-tongue-wasm (593KB) | Crate exists |
| UI Atomic | Squirrel + petalTongue composition from ui_atomic.toml | Designed |
| Scene streaming | /ws/scene for live WebGL in browser | Endpoint exists |
| Shared core symlinks | Replace per-site copies with build-time copy from shared/js/ | Identified debt |

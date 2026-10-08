+++
title = "biomeOS HUD — Shared Observation Surface"
description = "hud.primals.eco: live fleet telemetry, petalTongue API, multi-domain aliasing, embeddable widget across all primals.eco sites. The mesh's external receptor surface."
date = 2026-10-08
weight = 5

[extra]
maturity = "live"
+++

## Overview

The HUD at `hud.primals.eco` is the **shared observation surface** for the ecoPrimal mesh — the first place where internal sensory processing becomes visible to human observers. It aggregates fleet telemetry from signal.primals.eco, exposes petalTongue's rendering API, and embeds a live status widget across all ecosystem sites.

Three domain aliases point to the same service:

| Domain | Purpose |
|--------|---------|
| `hud.primals.eco` | Primary — operational name |
| `biomeos.primals.eco` | biomeOS branding — OS identity |
| `os.primals.eco` | Short alias — minimalist |

Different Host headers from the same content = free behavioral fingerprint intelligence. If a crawler hits `biomeos.primals.eco`, the Host header reveals which domain list it's working from.

## Architecture

### Layered Access

| Layer | Path | Auth | Content |
|-------|------|------|---------|
| Public | `/*` | None | Live dashboard — epitopes, geo, fleet, topology, billboard |
| API | `/api/*` | None | petalTongue JSON API — 27 endpoints |
| WebSocket | `/ws`, `/ws/scene` | None | JSON-RPC bridge + scene streaming |
| Operator | `/ops/*` | basicauth | Service health, WireGuard mesh, deploy state, system stats |

### Split Routing

Caddy serves static Zola files for the dashboard and reverse-proxies API/WS traffic to petalTongue:

```
Caddy (:443) — hud.primals.eco / biomeos.primals.eco / os.primals.eco
  ├── /api/*              → reverse_proxy 127.0.0.1:8092 (petalTongue)
  ├── /health, /health/*  → reverse_proxy 127.0.0.1:8092
  ├── /ws, /ws/*          → reverse_proxy 127.0.0.1:8092
  ├── /viz/*              → reverse_proxy 127.0.0.1:8092
  ├── /ops/*              → basicauth + file_server (ops-status.json)
  └── /*                  → Zola static site (try_files + file_server)
```

### Components

| Component | Size | Role |
|-----------|------|------|
| `hud-core.js` | 19KB | Standalone dashboard — polls `signal.primals.eco/dashboard.json` (8s) + `topology.json` (30s) |
| `hud-widget.js` | 9KB | Embeddable bottom bar for all primals.eco sites |
| `hud.css` | 5.5KB | Dark theme, information-dense dashboard layout |
| petalTongue v1.7.0 | 8.4MB | Headless axum web server — API, WS, scene compiler |
| `ops-status.sh` | cron/1min | Operator health JSON — services, WireGuard, deploys, system |

### Cross-Site Widget

The `hud-widget.js` script tag is embedded in `base.html` of every primals.eco Zola site:

- signal.primals.eco
- detroit.primals.eco
- thesis.primals.eco
- tuebor.primals.eco
- sporeprint.primals.eco

The widget renders a fixed-position bottom bar showing RPS, fleet count, fleet machine %, confidence, and billboard text. Expands on click to show organism pills, geographic bars, and ecosystem links. Self-contained (all styles inline, no dependencies). Auto-disables on the HUD site itself.

## petalTongue Integration

petalTongue is the **sensory-motor cortex** of the Meta tier. It sits alongside biomeOS (orchestration) and Squirrel (AI coordination). The HUD deployment means the sensory-motor cortex now has an external surface.

### SAME DAVE Model

| Biological | petalTongue |
|-----------|-------------|
| Visual cortex | Grammar-of-graphics scene compiler |
| Sensory afferent | `visualization.render.*` IPC — receives data from primals |
| Motor efferent | `motor.*` commands — pushes panels, notifications, navigation |
| Multi-modal | Same data → egui desktop, ratatui TUI, axum web, headless SVG, WASM browser |
| Cortical map | Panel system — each domain maps to a panel region |

### WebSocket JSON-RPC

Any computational actor (agent, script, primal) can connect to `wss://hud.primals.eco/ws` and invoke:

- `pt.metrics` — real-time system metrics
- `pt.scenarios` — visualization scenario catalog (8 built-in)
- `pt.render_svg` — scenario → SVG
- `pt.render_binding` — custom data → SVG (18 channel types: timeseries, bar, gauge, heatmap, scatter, scatter3d, distribution, fieldmap, game_scene, soundscape, spectrum, genome_track, circular_map, color_grid, faceted_bar, faceted_gauge, donut, plus standard types)
- `pt.render_webgl` — custom data → GPU draw calls

Bar, heatmap, faceted_bar, and faceted_gauge channels accept an optional `normalization` field (none, min_max, symmetric, z_score, log1p, rank, leaky_relu). Per-column independence preserves rank ordering while making mixed-metric panels visually comparable.

This was verified live: the agent computed Anderson selective permeability profiles through BarraCuda formulas and rendered them through petalTongue — 15 SVGs + 1 WebGL scene in 1.1 seconds.

## Cross-Site Bridge Architecture

All 4 primals.eco sites render petalTongue panels through a shared bridge module (`pt-bridge-core.js`, 251 lines):

| Site | Bridge | Panels | Data Source |
|------|--------|--------|-------------|
| signal.primals.eco | signal-pt.js (335 lines) | 22 | Local dashboard.json + topology.json |
| hud.primals.eco | hud-pt.js (309 lines) | 22 | Cross-origin from signal |
| thesis.primals.eco | thesis-pt.js (237 lines) | 19 | Cross-origin from signal |
| detroit.primals.eco | detroit-pt.js (376 lines) | 19 | DETROIT_NETWORK graph |

The shared core provides WebSocket lifecycle, JSON-RPC 2.0 protocol, organism classification (`classifyOrganism()`), and 5 reusable panel builders for faceted visualizations. Each site adds only its domain-specific panels.

## Operator Layer

The `/ops/` path (behind basicauth) serves `ops-status.json` generated every minute:

```json
{
  "services": ["caddy-tls", "skunky-ingest", "hbbs-membrane", "hbbr-membrane", "forgejo"],
  "wireguard": [{"peer": "...", "endpoint": "...", "handshake_age": "..."}],
  "deploys": {"sporePrint": "...", "detroit": "...", "signal": "...", ...},
  "system": {"load": "...", "memory": "...", "disk": "...", "uptime": "..."}
}
```

## Evolution Path

| Phase | Goal | Status |
|-------|------|--------|
| Phase 1 | Static HUD + embeddable widget | ✅ Live |
| Phase 2 | petalTongue headless deployment | ✅ Live |
| Phase 3 | Motor wiring (skunky → petalTongue → SSE → browser) | Planned |
| Phase 4 | WASM rendering (replace hud-core.js with petal-tongue-wasm) | Crate exists |
| Phase 5 | UI Atomic composition (Squirrel + petalTongue) | Designed |

## Privacy Invariant

- No cookies, no tracking pixels, no JS analytics
- No IP addresses stored or logged in receptor/signal systems
- Log-based analysis only, IPs stripped before dashboard aggregation
- petalTongue web mode: CORS enabled, no auth cookies, no session state

# sporePrint — Evolution Record

The changelog is sorted by capability surface, not by date.
Each section tells the arc: what emerged, what it replaced, what it became.
The date-sorted history lives in `CHANGELOG_ARCHIVE.md`.

`H(data|epitope) < H(data|date) < H(data)`

---

## Zola Site Platform — sovereign static site generator

sporePrint evolved from flat GitHub Markdown to a full Zola static site with custom theme, search, and CI/CD.

- **Zola migration** (v1.0): Zola 0.22.1 — single Rust binary, zero runtime dependencies, Elasticlunr search.
- **Custom theme** (v1.0): Dark mode, responsive sidebar, accessible skip links — no external theme dependency.
- **GitHub Actions CI/CD** (v1.0): Build with Zola, deploy to GitHub Pages; CNAME in `static/CNAME`.
- **CSS semantic split** (v2.0): Monolith → `base.css` (tokens) + `main.css` (components).

---

## spore-validate Toolchain — 100% Rust validation pipeline

Python validation replaced by typed Rust binary with entity model, drift detection, and link checking.

- **spore-validate crate** (v1.1): Typed `EntityKind` (7 kinds), `Tier` (4 tiers), per-kind field validation.
- **Shortcode scanning** (v1.1): `--check` scans 2,488+ entity shortcodes; `--strict` promotes warnings to errors.
- **Refresh subcommand** (v1.1): Cross-repo metric comparison with drift percentage reporting.
- **check-links** (v2.0): Validates 149+ internal `@/` links across content files.
- **EntityKind::Methodology** (v3.37): guerillaGorilla and dispersal pattern; 82 entities total.

---

## Sovereign Deployment — VPS-primary with provenance tracking

Deployment evolved from GitHub Pages-only to sovereign-primary VPS with BLAKE3 content addressing.

- **Sovereign self-hosting** (v3.0): Forgejo push → relay → `sporeprint-rebuild.sh`; Caddy TLS + Let's Encrypt.
- **BLAKE3 provenance** (v3.0): `provenance` subcommand with `content-manifest.toml` — `--verify`/`--diff`/`--write`.
- **Cascade restored** (v3.36): primals.eco LIVE; detroit.primals.eco first public accountability application (94→128+ pages).
- **GitHub Pages shadow** (v3.0): Trailing extracellular shadow; golgiBody-ext primary.

---

## Content Corpus — papers, philosophy, thesis, living docs

Content grew from 51 scaffold files to 338+ pages across 25 sections with cross-domain topology.

- **Initial scaffold** (v0.1): Audience, technical, methodology, architecture, 21 baseCamp science papers.
- **Philosophy complete** (v3.8): All 12 atlasHugged essays with bibliography and story cross-links.
- **Thesis scaffold** (v3.9): 16-chapter PhD dissertation with maturity badges and cross-links.
- **Evidence Snapshot** (v3.4): Canonical metrics source via `total_stat` shortcodes; maturity badge shortcode (6 levels).
- **Content transplants** (v3.6→v3.10): Builder narratives, gen3 transplants, 7 new technical pages.
- **guerillaGorilla** (v3.37): Methodology page with sensory triad, dispersal pattern, amicusContra (Wave 158).

---

## AI Accessibility — agent-friendly site comprehension

Accessibility evolved for AI agents with limited per-domain fetch quotas.

- **llms.txt** (Wave 137a): Structured site overview — section map, concepts, metrics in one fetch.
- **site-index** (Wave 137a): Auto-generated page catalog — one fetch = complete listing.
- **Table-to-list** (Wave 137a): 23 navigational tables → lists; AI fetch tools strip links from tables.
- **JSON-LD companions** (Wave 137b): Per-page `Article`/`ScholarlyArticle` with cross-domain `relatedLink` on 28 pages.
- **Content Topology** (Wave 137b): Four-register reinforcement model documented in llms.txt richness levels 0-4.

---

## Entity Registry & Living Topology — live metrics and fleet status

Hardcoded metrics and static snapshots evolved to registry-driven shortcodes and wave-synchronized status pages.

- **Entity shortcodes** (v3.37): `{{ entity(name="...") }}` in gate-status, living-systems, public_record.
- **Live metric rendering** (v3.4→v3.5): `total_stat`/`entity_metrics` shortcodes replace hardcoded test counts.
- **Gate status page** (ongoing): Fleet table, power states, depot targets rewritten each wave.
- **Mesh topology** (v3.2→Wave 158): Physical topology with `viz_embed` live health; 16-gate fleet, 7 arch families.
- **Wave 158 rewake** (v3.38): northGate (RTX 5090), Jupiter 2 RISC-V, 5-target depot, sporePrint → NUCLEUS live data surface.

---

## petalTongue Integration — build-time visualization

Visualization evolved from inline Plotly JS to server-rendered SVG via petalTongue IPC.

- **build-viz** (Wave 134): Scans `viz_embed` shortcodes, calls petalTongue IPC, writes SVGs to `static/viz/`.
- **viz_embed shortcode** (v3.3): Static SVG fallback with graceful degradation when petalTongue offline.
- **Live mesh viz** (v3.2): `viz_embed(src="/viz/gate-mesh?live=true")` for petalTongue `LiveMeshState`.
- **Transport unification** (v3.5): petalTongue commands honor `TRANSPORT_ENDPOINT` env var.

---

## NUCLEUS Validation — structural and live probe validation

NUCLEUS profiles evolved from parsed TOML to structural warnings plus live socket probing.

- **NUCLEUS subcommand** (v3.1+): Parses deployment profiles; probes live health + riboCipher acceptance.
- **Structural validation** (Wave 136a): Launch order, parallel_after, mesh federation consistency checks.
- **Profile-driven probes** (v3.3): `PrimalEntry.probe_methods` in TOML overrides default probe table.
- **default_tower_probes.toml** (Wave 134e): Embedded via `include_str!`, parsed with `LazyLock`.

---

## Accessibility & WCAG — automated validation in CI

Accessibility evolved from manual checks to automated 7-phase suite targeting WCAG 2.2 AAA.

- **validate_a11y.sh** (Wave 134f): HTML5, ARIA, headings, alt text, skip link, meta, search combobox.
- **CI integration** (Wave 134f): Runs in deploy.yml check job before build.
- **Contrast media queries** (Wave 136b): `prefers-contrast: more` and `forced-colors: active` support.

---

## IPC & Architecture — shared transport, spring-grade quality

IPC and codebase evolved to centralized JSON-RPC client with 90%+ coverage and zero production unwrap.

- **Shared ipc.rs** (v3.1): Centralized NDJSON JSON-RPC 2.0 client with response ID correlation.
- **riboCipher constants** (Wave 134f): Consolidated in ipc.rs; ReadWrite trait moved for dependency inversion.
- **Trait-based VCS** (v2.0): `VcsBackend` with `GitBackend`/`MockBackend` — test coverage without network I/O.
- **Module splits** (v3.1→Wave 134e): commands/main split into focused modules; 34 modules, max 670L.
- **deny.toml** (v3.1): Supply chain security — pure Rust deps, SPDX licenses, zero advisories.
- **Test scale** (Wave 137b): 290 tests, 11,012L, zero unwrap in production, clippy pedantic clean.

---

*Full date-sorted history: `CHANGELOG_ARCHIVE.md`*
*Last compressed: Wave 172*

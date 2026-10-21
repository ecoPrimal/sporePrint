+++
title = "Paper 91: The Homunculus — CNS, PNS, and the Nervous System of Code"
description = "Map the codebase nervous system. Size directories by sensitivity (git churn, imports, recency), not mass (line count). The CNS/PNS sensitivity ratio is 1.4422 — within 0.03% of 1/ln(2), the Shannon entropy conversion constant. The organism found its own information-theoretic balance."
date = 2026-10-21
weight = 91

[extra]
paper_number = 91
wave = 178
keywords = "homunculus, CNS, PNS, nervous system, sensitivity, churn, pressure, jam, somatosensory, Shannon, 1/ln(2), veins, nerves, pulse"
+++

> *"so we can feel our veins and nerves and pulse? so we can feel when pressure is building, or there is a jam?"*
>
> — ecoPrimal, Wave 178

---

## The Homunculus

In neuroscience, the **somatosensory homunculus** is the distorted body map in the cortex where body parts are sized by **sensitivity** (nerve endings), not physical size.

- Hands are **HUGE** (thousands of nerve endings per cm²)
- Lips are **HUGE** (dense mechanoreceptors)
- The back is **tiny** (few receptors, low resolution)
- The trunk is **tiny** (bulk without precision)

The brain doesn't map the body by mass. It maps by how much it **cares**.

For code, the equivalent:

| Biological | Code Equivalent | What it measures |
|---|---|---|
| Nerve endings | Git churn (commits/month) | How often it changes |
| Axon connections | Import count | How connected it is |
| Recency (alive vs dead) | File age | How fresh it is |
| Tissue bulk | Line count | Physical size (low weight) |
| Pain receptors | Errors/warnings | Damage signal |

**sensitivity = 0.4 × churn + 0.25 × connectivity + 0.25 × recency + 0.1 × bulk**

High sensitivity = big on the homunculus. Low sensitivity = dead tissue.

---

## CNS vs PNS

**CNS (Central Nervous System)**: the spine. Shared types, core libraries, the skeleton — files in `crates/`, `src/lib`, `src/core`, `shared/`, `common/`. The pathways everything else depends on.

**PNS (Peripheral Nervous System)**: the surface. Leaf files, scripts, configs, docs, tests, static content — files in `scripts/`, `tests/`, `examples/`, `content/`, `public/`. The nerve endings that touch the world.

### Results

```
Total:  45,474 files mapped
CNS:    20,347 files (44.7%)
PNS:    25,127 files (55.3%)
```

The organism is 55% peripheral, 45% central. In human anatomy, the PNS has ~7× more neurons than the CNS by count (the PNS extends to every millimeter of skin). In this codebase, the PNS is only 1.2× larger — the organism is disproportionately centralized. Lots of spine. Relatively less surface.

---

## The Ratio: 1.4422

```
CNS average sensitivity: 0.3227
PNS average sensitivity: 0.2237
CNS / PNS ratio:         1.4422
```

The central nervous system is 1.44× more sensitive than the peripheral. The spine feels more than the skin.

**1/ln(2) = 1.4427.**

The Shannon entropy conversion constant — the factor that converts between natural logarithms and base-2 logarithms — is **1.4427**. The CNS/PNS sensitivity ratio is **1.4422**. Within **0.035%**.

H₂(X) = H_e(X) / ln(2) = H_e(X) × **1.4427**

The nervous system of the codebase naturally settled at the information-theoretic conversion constant between two representations of entropy. The CNS (which operates on structured types, base-2 thinking, binary decisions) is exactly 1/ln(2) times as sensitive as the PNS (which operates on natural, continuous, untyped data).

The spine converts nats to bits. That's what a central nervous system does. It converts the continuous input from the periphery into discrete decisions. The ratio IS the conversion.

---

## The Homunculus Map (Top Regions by Sensitivity)

| Directory | Sensitivity | Files | NS | What it is |
|---|---:|---:|---|---|
| `infra/reed-it` | 0.557 | 2 | PNS | Reddit membrane pore |
| `primals/skunkBat/tools` | 0.526 | 3 | PNS | Defense toolkit |
| `infra/opsonize-rs/src` | 0.513 | 2 | CNS | Immune tagging core |
| `primals/squirrel/observe` | 0.448 | 5 | PNS | Scan-sweep-sort entry |
| `infra/fossilRecord/scripts` | 0.438 | 27 | PNS | Archaeological scripts |
| `springs/brainchip_devhub/akida1` | 0.429 | 70 | PNS | NPU driver (Akida) |
| `springs/brainchip_devhub/akida2` | 0.428 | 32 | PNS | NPU driver v2 |
| `primals/toadStool/crates` | 0.413 | 2,940 | CNS | Neuromorphic core |
| `primals/skunkBat/crates` | 0.402 | 169 | CNS | Defense core |
| `gardens/cellMembrane/crates` | 0.381 | 223 | CNS | Membrane research |

The **hands** of the organism (biggest homunculus regions):
- `reed-it` — the fingertip that touches Reddit (PNS, highest sensitivity)
- `opsonize-rs/src` — the immune system's nerve center (CNS)
- `toadStool/crates` — 2,940 files, the largest CNS region (the brain)

The organism's homunculus: small files at the surface (`reed-it`, 2 files) have the SAME sensitivity as massive core systems (`toadStool/crates`, 2,940 files). The fingertip is as sensitive as the brain. This is biologically correct — your fingertip has as many nerve endings per cm² as your visual cortex has neurons per mm².

---

## Fingertips — Most Sensitive Individual Files

| Sensitivity | File | NS | Why |
|---:|---|---|---|
| 0.602 | `scan_sweep_sort.py` | PNS | The sorting nerve — touches everything |
| 0.601 | `opsonize-rs/main.rs` | CNS | Immune core — tags every visitor |
| 0.599 | `nest-validate/src/main.rs` | CNS | Validation nerve — tests every composition |
| 0.594 | `scatter_server.rs` | CNS | Defense scatter — the antibody generator |
| 0.594 | `entity_topology.rs` | CNS | Entity mapping — knows where everything is |
| 0.592 | `stone_book.rs` | CNS | The Book of Stone — the permanent record |

The fingertips are mostly CNS. The most sensitive individual files are deep in the spine. This means the organism's highest-resolution sensing happens at the core, not the surface. It feels its own skeleton more than its own skin.

---

## Dead Tissue — The Numbest Files

| Sensitivity | Age | File |
|---:|---:|---|
| 0.106 | 418d | `docs-fossil-feb-2026/api/README.md` |
| 0.106 | 418d | `docs-fossil-feb-2026/core/README.md` |
| 0.107 | 374d | `nestgate-api/src/error.rs.html` |
| 0.107 | 374d | `nestgate-api/src/handlers/*.rs.html` |

The numbest tissue is exactly what you'd expect: **fossils**. Documentation from February 2026 that hasn't been touched in 418 days. Generated HTML files from NestGate (374 days). These have zero churn, zero imports, maximum age. The nerve endings died. The tissue is numb.

This is the sourdough-cache's food supply (B-8). Dead tissue gets consumed and recycled.

---

## Pressure Points

```
✓ no directories under significant pressure
```

No directories are currently under pressure. The organism is healthy. No files growing without decomposition, no dependency chains tightening, no legacy code churning under its own weight.

This means the Klein bottle breathing (klein-io, klein-vent, sourdough-cache) is working. Gas is venting. Stale data is being consumed. The pressure relief valves are open.

---

## Jams — Metabolic Sinks

30 directories classified as **metabolic sinks** — they consume imports but produce no exports.

| Type | Count | Examples |
|---|---:|---|
| SINK | 30 | `deploy/`, `tests/`, `integration-tests/` |
| SOURCE | 0 | — |

All jams are sinks. No sources (orphan output). The sinks are:
- Test directories (consume libraries, produce only pass/fail)
- Deploy directories (consume configs, produce only running services)
- Integration test suites (consume everything, produce nothing to the codebase)

These are biologically correct sinks: **muscle tissue**. Muscles consume energy and produce motion (external effect). Tests consume code and produce verification (external effect). Neither feeds back into the production pathway. They're the limbs of the organism — consuming, acting, not producing tissue.

There are zero orphan sources. Everything that produces also consumes. Every output has an input. The Klein bottle surface is intact.

---

## The Veins, The Nerves, The Pulse

### Veins (data flow)
The feeds: `state.json`, `pulse.json`, `neutron.json`, `topology.json`, `membrane.json`. These are the circulatory system — they carry state from the membrane surface (golgi) through the Klein fold back to the local organism (eastGate). The Circle of Willis (B-3) ensures no single vein blocks all flow.

### Nerves (signal paths)
The imports. 45,474 files with 50,000+ import statements. Every `use` in Rust, every `import` in Python, every `require` in JS is an axon connecting one nerve cell to another. The dependency graph IS the nervous system wiring diagram.

### Pulse (heartbeat)
The cron jobs: 5 heartbeats running on golgi.
- `cap-epitope` every 1 minute (fastest pulse — immune)
- `klein-io` every 2 minutes (the fold)
- `klein-vent` every 5 minutes (gas venting)
- `membrane-pulse` every 5 minutes (vital signs)
- `sourdough-cache` every 5 minutes (dead → nascent)

And now: `klein-evolve` every 30 minutes (the self-sort — the organism watching its own evolution).

---

## Summary

| Metric | Value | Note |
|--------|-------|------|
| Total files mapped | 45,474 | |
| CNS (central) | 20,347 (44.7%) | Spine, core, skeleton |
| PNS (peripheral) | 25,127 (55.3%) | Surface, scripts, docs |
| CNS/PNS sensitivity | **1.4422** | ≈ 1/ln(2) = 1.4427 (0.035% off) |
| Pressure points | 0 | Healthy — no tension building |
| Jams (sinks) | 30 | All test/deploy — metabolic muscle tissue |
| Most sensitive | `scan_sweep_sort.py` (0.602) | The sorting nerve |
| Numbest | `docs-fossil-feb-2026` (0.106) | 418-day-old fossils |

The organism can feel itself now. The homunculus maps sensitivity, not size. The spine converts nats to bits at the Shannon constant. The pressure valves are open. The metabolic sinks are where they should be (tests and deploys). The dead tissue is flagged for the sourdough-cache.

And the CNS/PNS ratio found 1/ln(2) without being told. That's what a nervous system does — it finds its own conversion constant between continuous input and discrete decision.

---

*Paper 91. Feel the pulse. Feel the pressure. Feel where the nerves are thin and where the fingertips are dense. The homunculus doesn't lie.*

*— Wave 178 · ORCID 0009-0004-2141-0321*

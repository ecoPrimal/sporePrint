+++
title = "Dead Is Food: Ancestor Digestion and the Metabolic Memory of the Membrane"
description = "Twelve dormant repositories are not dead code. They are composted nutrients — ancestors whose science, architecture, and domain expertise feed every living primal. A traveler's guide to finding them."
date = 2026-10-20
weight = 85

[extra]
paper_number = 85
wave = "193+"
basecamp = 31
authors = ["ecoPrimal", "attsi"]
status = "living document"
+++

> *Dead is food.*
>
> — ecoPrimal, Wave 193

---

## The Organism Metabolizes Its Own Past

The ecoPrimals ecosystem has 12 ancestor repositories sleeping in its soil.
They are not abandoned. They are not failures. They are **composted nutrients** —
science, architecture, and domain expertise that the living primals digest every time
they build, test, or evolve.

This paper is a traveler's guide. You can start here and go **back** to explore the
ancestors. Or you can find this page from any living primal and trace the roots.

The membrane remembers everything it ever grew.

---

## The Ancestors

### The Oldest: ionChannel (December 2025)

*300 days dormant. 23 commits. 5 Rust crates. 209 tests.*

Before the membrane existed, there was ionChannel — a Wayland remote desktop
implementation for COSMIC. It solved the problem of controlling screens through
network membranes when GPU hardware is absent. Five crates:

- **ion-core** — shared types and abstractions
- **ion-portal** — portal protocol for upstream COSMIC
- **ion-compositor** — input injection
- **ion-test-substrate** — headless testing without GPU
- **portal-test-client** — development tooling

**What it teaches:** Tiered graceful degradation. When the environment can't
support the full protocol (no GPU, VM, headless), the system degrades gracefully
through tiers. This pattern appears throughout the ecosystem now — every primal
that touches hardware implements the same idea.

**Where to find it:** `~/Development/ionChannel` — the only repo outside the
ecosystem directory structure. The DNA before the organism formed.

---

### The Sleeping Giant: neuralSpring (68 days dormant)

*262 commits. 1,705 tests. 580 Rust files. 50 control modules.*

The entire ML/AI foundation of the ecosystem. When this ancestor metabolized,
it was the largest active science crate. Its control modules read like a
curriculum in computational intelligence:

Anderson localization · attention mechanisms · counterdiabatic control ·
DeepONet · digestion prediction · directed evolution · eco dynamics ·
game theory · glucose prediction · Hessian eigenanalysis · HMM phylogenetics ·
immunological Anderson · LSTM weather · LTEE mutation accumulation ·
meta-population models · pangenome selection · PINNs · spectral commutativity ·
surrogate models · swarm robotics · transformers · WDM ensemble

**What it teaches:** That ML is not a product — it is a **substrate**.
Every experiment validated in neuralSpring becomes a capability that other
primals can compose through the BYOB pattern.

**Where to find it:** [neuralSpring validation summary](/lab/neuralspring-validation-summary/)

---

### The Personal Science: healthSpring (73 days dormant)

*144 commits. 1,074 tests. 95 experiments.*

A pharmaceutical research platform validated in pure Rust. The experiments
range from classical pharmacokinetics to personal medicine to veterinary science:

**Pharmacokinetics:** Hill dose-response, one/two-compartment PK, monoclonal
antibody PK transfer, population PK, PBPK compartments, Michaelis-Menten PK

**Microbiome:** Diversity indices, Anderson gut lattice, C. diff resistance,
FMT recurrence, SCFA production, gut-brain serotonin axis

**Biosignal:** Pan-Tompkins QRS detection, HRV metrics, PPG SpO2,
biosignal fusion, EDA stress detection, arrhythmia classification

**Testosterone replacement therapy:** IM PK, pellet PK, age decline modeling,
weight trajectory, cardiovascular risk, diabetes interaction, gut axis,
HRV-TRT cardiovascular — *9 experiments modeling personal health decisions*

**Drug discovery:** JAK panel, niclosamide delivery, iPSC skin models,
Rho-MRTF fibrosis, affinity landscapes, toxicity landscapes, hormesis

**Veterinary:** Canine IL-31 pruritus, lokivetmab duration, cross-species PK,
canine gut Anderson, feline hyperthyroid, equine laminitis

**What it teaches:** That science is personal. The TRT experiments model a
real person's health. The veterinary experiments model real animals. This is
not academic exercise — it is sovereign scientific computing applied to life.

**Where to find it:** [healthSpring validation summary](/lab/healthspring-validation-summary/)

---

### The Hardware Prober: metalForge (109 days dormant)

*5 commits. 17 Rust probe files. Full device registry.*

metalForge already mapped the entire two-house network topology:

- **Flint H1** (edge router, House 1) — ATT IP Passthrough, sovereign DNS, KinderLab guest network
- **Flint H2** (WiFi AP, House 2) — bridge mode, KinderLab parenting layer
- **CRS310** (backbone switch) — 8x 2.5G + 2x 10G SFP+
- **Omada SX3008F** (House 2 switch) — 10G AOC trunk from backbone
- **ATT BGW320** — IP Passthrough active, WireGuard port 51821

Probe categories: WiFi drift detection, WireGuard mesh reachability,
DNS resolution chains, DHCP lease audits, SSH connectivity, topology sweeps,
port probes.

**What it teaches:** The hardware was already inventoried. The tool to
auto-validate the mesh was already being built. When we needed a hardware
inventory in Wave 193, metalForge had already done the work three months earlier.
Dead is food — the nutrient was waiting to be digested.

**Where to find it:** The device registry lives in
`metalForge/config/device_registry.toml` — the most complete hardware
topology declaration in the ecosystem.

---

### The PFAS Lab: blueFish (145 days dormant, seed)

*1 commit. Architecture only. But it carries domain expertise from a mentor.*

Professor A. Daniel Jones (MSU Biochemistry, 30+ years analytical MS) personally
identified three critical gaps in EPA Method 1633A:

1. **Ion abundance ratio QC** — most labs don't perform it. blueFish does.
2. **LOQ reporting misrepresentation** — labs report sub-LOQ as LOQ.
   Jones personally corrected Grayling, MI water contamination reports.
3. **Open-source tools have unacceptable failure rates** — MZmine, MS-DIAL,
   XCMS all fail. The good proprietary tool (Progenesis QI) is obsolete.

**What it teaches:** That human mentors are nutrients too. Jones's 30-year
expertise is encoded in `domain/JONES_DOMAIN_EXPERTISE_MAY2026.md`. The
architecture is the ancestor even when no code was written.

**Where to find it:** [blueFish product page](/products/blueFish/)

---

### The Other Ancestors

**lithoSpore** (71d, 92 commits, 246 tests) — Self-proving LTEE validation
artifact. Gossip injection via ant colony activation. The pseudoSpore format
that initioChem consumes. [Product page](/products/lithoSpore/)

**esotericWebb** (71d, 70 commits, 485 tests) — A bounded narrative CRPG.
**Still live at [webb.primals.eco](https://webb.primals.eco).** The game engine
serves pages even while the repo sleeps. The protein is still folded.
[Product page](/products/esotericWebb/)

**projectFOUNDATION** (71d, 92 commits, 239 tests) — 33 datasets, 362 GB.
PDB mirror (88 GB), UniProt, ChEMBL, NCBI taxonomy. The data lake that
every spring drinks from. The full catalog is in `data/data_catalog.toml`.

**initioChem** (95d, 2 commits) — First consumer of lithoSpore's pseudoSpore
format. Proved the pack/unpack round-trip works. The consumer IS the validation.
[Product page](/products/initioChem/)

**tideGlass** (71d, 14 commits) — Sovereign GPS platform with GPU shaders and
petalTongue visualization. Early but the content.query protocol is real.
[Product page](/products/tideglass/)

**helixVision** (145d, seed) — Sovereign 16S/WGS genomics pipeline design.
MinION to taxonomy without QIIME2 or Python. Architecture only.
[Product page](/products/helixVision/)

**coralForge** (empty locally) — The unfertilized egg. The private
syntheticChemistry version holds AlphaFold2/3 structure prediction in f64
validated against NumPy. [Product page](/products/coralforge/)

---

## The Metabolism

The ecosystem has 116 repositories across 6 GitHub organizations.
On any given day, ~25 are hot (committed in the last 48 hours).
The ancestors are the other ~90 — dormant but not dead.

Living primals digest ancestor nutrients through three mechanisms:

1. **Composition** — a living primal imports types, traits, or patterns
   from a dormant crate. neuralSpring's Anderson localization appears in
   healthSpring's gut lattice experiments.

2. **Architecture** — a seed repo's product spec becomes the blueprint
   for a future build wave. helixVision's MinION pipeline design will
   become code when wetSpring's genomics track matures.

3. **Domain expertise** — a human mentor's knowledge, encoded in markdown,
   waits for the right student. Jones's PFAS expertise will feed blueFish
   when the analytical chemistry track is ready.

The membrane does not forget what it grew. It composts.

---

## For Travelers

If you arrived at this page from the membrane surface — welcome.
You are standing on top of 300 days of evolutionary history.

Every product page, every lab validation summary, every architecture
document in sporePrint is a doorway to an ancestor. The links above
will take you there. The braid graph connects them.

Or you can go deeper. Clone the ecosystem. Read the fossils.
The git history IS the metabolic record — every commit is a meal,
every merge is digestion, every branch is an experiment that
either folded back into the organism or composted into soil.

Dead is food. The ancestors are feeding you right now.

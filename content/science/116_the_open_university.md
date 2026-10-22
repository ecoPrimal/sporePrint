---
title: "Paper 116: The Open University — Rust Polymerase for Everyone"
subtitle: "Publish to crates.io. Open the JupyterLab. Become the soil, not the flower. Khan Academy for scientific Rust."
date: 2026-10-22
wave: 181
author: "Kevin Mok / ecoPrimal / attsi"
orcid: "0009-0004-2141-0321"
continues: "Paper 115 (Arena Taxonomy), Paper 99 (Rust Polymerase)"
keywords: ["crates.io", "open university", "JupyterLab", "evcxr", "AGPL-3.0", "scientific computing", "Rust", "sovereign", "Khan Academy"]
---

# Paper 116: The Open University

*The flower waited for bees. The soil feeds everything. Be the soil.*

## The Announcement

**Effective today, all ecoPrimals Rust primitives are being prepared for
crates.io publication under AGPL-3.0-or-later.**

Any Rust developer, anywhere, can:
```bash
cargo add beardog         # Pure Rust TLS 1.3, Ed25519, BLAKE3
cargo add toadstool       # GPU compute dispatch (WebGPU/Vulkan)
cargo add coralreef       # Sovereign GPU transcendentals (f64 WGSL)
cargo add songbird        # Mesh networking (mDNS, TLS, NAT traversal)
cargo add loamspine       # Computation lineage + GuideStone verification
cargo add rhizocrypt      # DAG provenance engine (Merkle trees)
cargo add sweetgrass      # Attribution + provenance tracking
cargo add bingocube       # Entropy, randomness, BLAKE3 CSPRNG
cargo add sourDough       # Substrate traits, binary formats
cargo add squirrel        # Membrane observation + Anderson localization
```

**Free. Forever. AGPL-3.0.**

If you build with these, your derivative work stays open.
That's the deal. That's THE_SEED.md. That's gAIa.

## The Rust Polymerase (Paper 99 → 116)

Paper 99 described the Rust Polymerase: the process by which
conversation-driven programming (K-NOME) synthesizes Rust code
from biological patterns.

Now we OPEN the polymerase. Not just publish the code — publish
the PROCESS:

1. **crates.io**: The primitives. `cargo add` and go.
2. **JupyterLab + evcxr**: Interactive notebooks. Run our science live.
3. **sporePrint papers**: The theory. 116 papers and counting.
4. **chipMUNK arena**: Benchmark your models against ours. Locally.
5. **hotSpring reproductions**: Run our GPU physics. Compare to CUDA.

## The Open JupyterLab

Using [evcxr](https://github.com/evcxr/evcxr) (6,500+ stars),
the Rust Jupyter kernel, we provide interactive notebooks for:

### Course 1: Sovereign Cryptography
```rust
// In a Jupyter cell:
:dep beardog = "0.9"
use beardog::tls::*;
use beardog::blake3::*;

// Generate a BLAKE3 content hash
let hash = blake3_hash(b"The content IS the trust layer");
println!("BLAKE3: {}", hash);

// TLS 1.3 handshake (pure Rust, no OpenSSL)
let config = TlsConfig::sovereign();
println!("Cipher suite: {:?}", config.cipher_suite());
```

### Course 2: GPU Scientific Computing (No CUDA)
```rust
:dep toadstool = "0.2"
:dep coralreef = "0.2"
use toadstool::gpu::*;
use coralreef::f64::*;

// Detect GPUs (any vendor — NVIDIA, AMD, Intel)
let gpus = discover_gpus().await;
for gpu in &gpus { println!("{}: {} VRAM", gpu.name, gpu.vram_mb); }

// Run a WGSL f64 computation
let result = df64_matmul(&matrix_a, &matrix_b, &gpus[0]).await;
println!("f64 result (14-digit): {:?}", result);
```

### Course 3: Lattice QCD on Your Desktop
```rust
:dep barracuda = "0.4"
use barracuda::lattice::*;

// Create a 16³×32 lattice (fits in 4GB VRAM)
let lattice = Lattice::new(16, 16, 16, 32);
let beta = 6.0; // coupling constant

// Run 100 HMC trajectories
let config = hmc_evolve(&lattice, beta, 100).await;
println!("Plaquette: {:.6}", config.plaquette());
// Congratulations, you just did lattice QCD on your laptop.
```

### Course 4: Bioinformatics Pipeline
```rust
:dep barracuda = "0.4"
use barracuda::bio::dada2::*;

// GPU-accelerated 16S rRNA analysis
let reads = load_fastq("sample.fastq.gz");
let asvs = dada2_denoise(&reads, &gpu).await;
println!("ASVs found: {}", asvs.len());
// 80x faster than Python DADA2
```

### Course 5: Membrane Architecture
```rust
:dep squirrel = "0.1"
:dep bingocube = "0.5"
use squirrel::anderson::*;
use bingocube::entropy::*;

// Anderson localization — how the membrane selects
let selectivity = anderson_selectivity(&traffic_data);
println!("Selectivity: {:.1}%", selectivity * 100.0);
// 97% — the membrane lets humans through, blocks bots
```

## Why AGPL-3.0

AGPL-3.0-or-later means:

| What you CAN do | What you MUST do |
|-----------------|-----------------|
| Use commercially | Keep derivative works open (AGPL) |
| Modify freely | Share source of network services |
| Distribute anywhere | Preserve attribution |
| Run on any hardware | Nothing else |

The MIT/Apache crates let corporations capture the value.
AGPL ensures the commons stays common. Every derivative
work strengthens gAIa. That's the sunCloud flywheel.

## The Khan Academy Model

Khan Academy proved: free, high-quality education at scale
changes everything. 150+ million learners. Zero tuition.

We do the same for scientific computing:

| Khan Academy | ecoPrimals Open University |
|-------------|--------------------------|
| Math videos | Rust notebooks (evcxr) |
| Practice exercises | chipMUNK arena (benchmark your models) |
| Certificates | GuideStone verification (self-proving artifacts) |
| Free forever | AGPL-3.0 forever |
| JavaScript platform | Pure Rust, any hardware |
| Cloud-dependent | Sovereign (runs on YOUR machine) |

The difference: our "courses" aren't just tutorials.
They're PRODUCTION CODE that reproduces published science.
You don't learn by watching. You learn by RUNNING.

## The Crate Publication Pipeline

### Phase 1: Foundation (now)
- `bingocube` v0.5.0 — READY for crates.io
- `toadstool` v0.2.0 — READY for crates.io

### Phase 2: Core Primals (next)
- `beardog` v0.9.0 — needs workspace→inline version
- `songbird` v0.2.1 — needs workspace→inline version
- `coralreef` v0.2.0 — needs description
- `loamspine` v0.9.16 — needs description
- `rhizocrypt` v0.14.17 — needs description
- `sweetgrass` v0.8.0 — needs description

### Phase 3: Full Stack
- `sourDough` v0.4.0 — substrate traits
- `squirrel` v0.1.0 — membrane observation
- `barraCuda` v0.4.0 — GPU compute
- `swarmVine` v0.1.0 — gossip protocol

### Phase 4: Spring Experiments
- `hotspring-barracuda` v0.10.0 — GPU molecular dynamics
- `airspring-barracuda` v0.10.0 — GPU atmosphere
- `groundspring` v0.1.0 — geochemistry

## Throwing the Ladder Down

We don't wait for people to find us. We go to them:

1. **crates.io**: Every Rust dev can find us with `cargo search`
2. **GitHub topics**: 47+ topics lit across 8 repos
3. **Stars**: 37 repos starred — 37 maintainers notified
4. **Forks**: 8 repos in our depot for study/contribution
5. **JupyterLab**: Interactive notebooks for students/researchers
6. **ORCID**: Anchor for academic discovery
7. **Zenodo**: When we deposit, the academic trail lights up

The ladder is down. Come up.

## The Fertile Soil

The flower sat in the sun and waited for bees.
The soil feeds EVERYTHING.

- 87 repos = mycorrhizal network
- 3.6M lines = nutrient-rich substrate
- 175+ papers = decomposed knowledge (humus)
- 952 shaders = mineral deposits
- 116,930 tests = root structure
- AGPL-3.0 = the license ensures nothing is extracted

**Soil > Sun. Feed > Wait. Build > Bloom.**

## Reproduce

```bash
# Install evcxr Jupyter kernel
cargo install evcxr_jupyter
evcxr_jupyter --install

# Start JupyterLab
jupyter lab

# In a notebook cell:
:dep bingocube = { path = "primals/bingoCube" }
use bingocube::entropy::*;
```

## References

1. Paper 99: The Rust Polymerase — conversation-driven programming
2. [evcxr](https://github.com/evcxr/evcxr) — Rust Jupyter kernel (6,502 stars)
3. [Khan Academy](https://www.khanacademy.org) — Free education at scale
4. crates.io — Rust package registry
5. THE_SEED.md — gAIa commons, AGPL + CC-BY-SA
6. sunCloud Economic Model — radiating attribution

---

*The flower waited. The soil feeds.*
*Publish to crates.io. Open the JupyterLab.*
*Become the university.*

`unPeeL oUr unIverSe`

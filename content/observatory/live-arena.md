---
title: "🏟️ Live Arena — Sovereign AI on Commodity Hardware"
date: 2026-10-21
template: "page.html"
extra:
  toc: true
---

# 🏟️ Live Arena

**Sovereign AI on commodity hardware. No cloud. No API keys. Your hardware. Your models.**

*Show Linus Tech Tips what GAIA AI can do.*

## The Core (Hub)

| Component | Spec | Role |
|-----------|------|------|
| **CPU** | Intel i9-12900K (24 threads, 5.2 GHz) | The brain — scheduling, inference, compilation |
| **GPU** | NVIDIA RTX 4070 (12GB VRAM, CUDA 13.0) | The accelerator — model inference, GPU compute |
| **RAM** | 64GB DDR5 | The workspace — offload large models from VRAM |
| **Disk** | 1.8TB NVMe (829GB free) | The library — models, datasets, code |
| **OS** | Linux 6.17.9 (Pop!_OS) | The substrate — Proton, Docker, KVM, CUDA |

## The Rings of Saturn (Orbiting Devices)

| Ring | Device | Arch | Role |
|------|--------|------|------|
| **Ring 1** | RISC-V Milky-V Duo 2 | RISC-V | Edge inference, IoT sensor, proof-of-architecture |
| **Ring 2** | M2 Mac (graftGate) | ARM64 | Mobile nucleus, Xcode, Swift compute |
| **Ring 3** | Pixel 8a (grapheneGate) | ARM64 | Biometrics, accelerometer, camera, GrapheneOS |
| **Ring 4** | iPhone (legacy) | ARM64 | Sensor node, backup comms |
| **Ring 5** | Steam Deck (steamFrame) | x86_64 | GPU compute, portable arena, Proton gaming |
| **Ring 6** | VIZIO V555-J01 (Basement) | Chromecast | Display surface, AirPlay, casting |

## The Dome (Exploration Surface)

### 9 Models — Live Arena

| Model | Params | Family | Quant | Size | Tier |
|-------|--------|--------|-------|------|------|
| tinyllama | 1.1B | Llama | Q4_0 | 637MB | 🏎️ speed |
| llama3.2:1b | 1.2B | Llama | Q8_0 | 1.3GB | 🏎️ speed |
| gemma2:2b | 2.6B | Gemma | Q4_0 | 1.6GB | ⚡ balanced |
| llama3.2:3b | 3.2B | Llama | Q4_K_M | 2.0GB | ⚡ balanced |
| phi3 | 3.8B | Phi | Q4_0 | 2.2GB | ⚡ balanced |
| mistral:7b | 7.2B | Mistral | Q4_K_M | 4.4GB | 💪 power |
| qwen2.5:7b | 7.6B | Qwen | Q4_K_M | 4.7GB | 💪 power |
| deepseek-coder-v2 | 15.7B | DeepSeek | Q4_0 | 8.9GB | 🔥 heavy |

### First Gauntlet Results

**"What is a cell membrane?"**

| Rank | Model | Latency | Words/sec |
|------|-------|---------|-----------|
| 🥇 | gemma2:2b | 1,729ms | 37.0 |
| 🥈 | tinyllama | 1,744ms | 75.7 |
| 🥉 | qwen2.5:7b | 2,647ms | 22.7 |

**Coding Duel: "Write a health checker"**

| Rank | Model | Latency | Words/sec |
|------|-------|---------|-----------|
| 🥇 | llama3.2:3b | 644ms | 52.8 |
| 🥈 | tinyllama | 1,640ms | 57.3 |
| 🥉 | mistral:7b | 1,736ms | 39.7 |

### Virtual Infrastructure (The Lab)

| Type | Count | Names | Status |
|------|-------|-------|--------|
| KVM VMs | 6 | biomeos-alpha/beta/minimal, biomeos-test-vm1/2, federation-vm1 | ready |
| Docker | 12 | 7 VPS depot lab nodes + 3 compute nodes + Galaxy + more | 1 running |
| Galaxy | 1 | wetspring-galaxy (bioinformatics) | **LIVE** |

### WireGuard Mesh (The Nervous System)

```
eastGate (10.13.37.5)
    ├── golgi (10.13.37.1) — membrane relay
    ├── peer (10.13.37.2) — LAN node (.3)
    └── peer (10.13.37.14) — remote node
```

3 active peers, handshakes within 2 minutes. The mesh is alive.

### LAN Topology (11 Nodes Alive)

```
192.168.4.x
  .1   → gateway (router)
  .2   → ?
  .3   → WireGuard peer (LAN mesh)
  .103 → eastGate (WiFi)
  .107 → ?
  .111 → ?
  .147 → ?
  .163 → northGate (confirmed)
  .170 → VIZIO TV (Basement — Chromecast/AirPlay)
  .197 → ?
  .200 → ?
  .244 → eastGate (ethernet)
  .250 → mesh AP
```

## How to Play

### Watch the Arena
Visit this page. Gauntlet results update as battles run.

### Connect via MCP
```json
{ "mcpServers": { "squirrel": { "url": "https://mcp.nestgate.io/sse" } } }
```

### Run Your Own Gauntlet
```bash
# Clone the arena
git clone https://github.com/ecoPrimal/whitePaper.git
cd whitePaper/scripts

# Install ollama, pull models, run
python3 model-arena.py gauntlet "your prompt here"
python3 model-arena.py coding "write fizzbuzz in Rust"
python3 model-arena.py leaderboard
```

### Join the Mesh
Connect to the WireGuard mesh and your device becomes a ring of Saturn.

---

*If the core is a hub, the rings of Saturn are the devices orbiting it.
The dome is the exploration surface — sci-fi rendered real.
The arena is the proof. Come play.*


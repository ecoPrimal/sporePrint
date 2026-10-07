+++
title = "baseCamp 35 — Process Stratigraphy: Finding Our Own Fossils"
description = "While investigating a load crisis on golgiBody, we discovered the earliest evolutionary layers of our own infrastructure still running — 72-day-old songbird federation servers, 71-day-old RustDesk relays, and a complete geological record of the organism's growth. The real load came from stuck Forgejo SSH workers spawned by sporeGate's temporal cascade — our own immune system creating the inflammation."
date = 2026-10-07

[taxonomies]
primals = ["cellmembrane", "songbird", "skunkbat"]
springs = []

[extra]
paper_number = 35
domain = "Infrastructure Archaeology and Self-Diagnosis"

[[extra.companions]]
url = "/science/34-honeycomb-prism-floating-pointer/"
title = "Honeycomb Prism"
relation = "preceded_by"
label = "The deployment that triggered the investigation"

[[extra.companions]]
url = "/architecture/adaptive-immune-defense/"
title = "Adaptive Immune Defense"
relation = "extends"
label = "The immune system whose cascade created the inflammation"
+++

{{ maturity(level="live") }} Discovered October 7, 2026. Fossils identified and catalogued. Stuck processes killed (load 32 → 0.59).

---

## Abstract

golgiBody hit load average 32 on a single-vCPU machine. The initial hypothesis was fleet — we were already tracking 770 req/min of crawler traffic. The investigation revealed three distinct sources of load, none of which was fleet:

1. **15 stuck Forgejo `serv` processes** — spawned simultaneously by sporeGate's temporal cascade via SSH key-10, all stuck in uninterruptible IO for 10+ minutes. These alone consumed 48.5% CPU and pushed load average above 30.

2. **233 fossil connections** — 98% of all established TCP connections belonged to services from July 2026: songbird federation (160 connections, all from eastGate's house network), RustDesk relay (67 connections from 66 worldwide IPs), and RustDesk signaling (6 connections).

3. **One zombie process** — an orphaned bash session from our own earlier investigation, still running inside the server we were trying to diagnose.

The organism was inflamed by its own immune system (cascade) and burdened by its own evolutionary history (fossils). Fleet was a red herring — they were 2 HTTPS connections out of 238.

---

## 1. The Stratigraphy

Every running process on golgiBody is a layer of geological time. The oldest non-kernel processes form a complete record of the organism's evolution:

| Layer | Date | Age | Process | Purpose | Era |
|-------|------|-----|---------|---------|-----|
| 0 | May 15 | 145d | systemd | System boot | Genesis |
| 1 | May 31 | 129d | knotd | Authoritative DNS | DNS sovereignty |
| 2 | Jun 17 | 112d | wg-crypt-wg0 | WireGuard mesh | Mesh networking |
| 3 | Jul 8 | 91d | nestgate | Gateway process | Gateway establishment |
| 4 | Jul 11 | 88d | fail2ban | Intrusion prevention | First immune layer |
| **5** | **Jul 27** | **72d** | **songbird** | **Federation + relay** | **cellMembrane era** |
| **6** | **Jul 28** | **71d** | **hbbr** | **RustDesk relay** | **cellMembrane era** |
| 7 | Jul 29 | 70d | step-ca | Internal CA | PKI establishment |
| 8 | Oct 7 | 0d | caddy | Web/scatter | Current immune system |
| 9 | Oct 7 | 0d | forgejo | Git hosting | Current mission |
| 10 | Oct 7 | 0d | skunky-ingest | Fleet detection | Active defense |

Layers 5 and 6 are the **fossil layer** — services deployed during the initial cellMembrane rollout that have been running continuously for 71-72 days. They predate:

- The scatter defense system
- The genetic lock
- The honeycomb maze
- The bloom monitor
- The 7 conserved epitopes
- Every baseCamp paper

They are the earliest preserved form of the organism's technology, still alive, still consuming resources, still accepting connections from the outside world.

---

## 2. The Fossil Connections

At the time of investigation, golgiBody had 238 established TCP connections:

```
Port 7700  (songbird federation)    160 conn  (67.2%)  <<< FOSSIL
Port 21119 (hbbr RustDesk relay)     67 conn  (28.2%)  <<< FOSSIL
Port 8091  (hbbs RustDesk signal)     6 conn  ( 2.5%)  <<< FOSSIL
Port 22    (SSH)                      2 conn  ( 0.8%)  ← us
Port 443   (HTTPS/Caddy)             2 conn  ( 0.8%)  ← fleet
Port 57162 (outbound TLS)            1 conn  ( 0.4%)  ← ACME
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FOSSIL LOAD:                        233 conn  (97.9%)
ACTIVE MISSION:                       5 conn  ( 2.1%)
```

The entire fleet — ClaudeBot at 600 req/min, Meta's 77-IP fleet at 150 req/min — accounted for **2 connections**. HTTP connections are short-lived; the fleet's impact is CPU-per-request, not connection count.

The fossils, by contrast, hold persistent TCP connections open indefinitely:

- **songbird federation** (port 7700): 160 connections, all from `162.226.225.148` — the house network. songbird was designed for federated communication between gates. With 160 persistent connections from a single source, this is the house network maintaining federation channels that haven't been used since the songbird era.

- **hbbr relay** (port 21119): 67 connections from 66 unique IPs worldwide. The RustDesk relay is an open relay — anyone on the internet who knows the server address can route remote desktop traffic through it. These 66 IPs are strangers using golgiBody as a free relay node.

- **hbbs signaling** (port 8091): 6 connections from scattered IPs. The RustDesk rendezvous server, accepting signaling requests.

---

## 3. The Inflammation

The actual load crisis was not the fossils (they use negligible CPU). It was **15 simultaneously-spawned Forgejo SSH workers**:

```
PID 2950531  forgejo serv key-10  started 18:15:42  state: Dl  CPU: 3.2%
PID 2950532  forgejo serv key-10  started 18:15:42  state: Dl  CPU: 3.2%
PID 2950533  forgejo serv key-10  started 18:15:42  state: Dl  CPU: 3.2%
... (12 more identical processes)
Total: 15 × 3.2% = 48.5% CPU + 200MB RAM
```

All spawned at the **exact same second** (18:15:42 UTC). All authenticated via `key-10` (`sporegate-gate-v1`). All children of the Forgejo web process. All stuck in `Dl` state (uninterruptible disk IO) or `Sl` (sleeping). No network sockets — the SSH connections they were serving had already closed, but the serv processes were orphaned, spinning on dead pipes.

**Cause**: sporeGate's temporal cascade pushed to 15 repos simultaneously via Forgejo SSH. On a 1 vCPU machine with a spinning-disk-equivalent VPS filesystem, 15 concurrent git operations caused IO contention. The operations never completed — they stuck in uninterruptible IO, their SSH connections timed out and closed, but the Forgejo serv workers couldn't be killed by normal signals because they were in kernel-space IO wait.

**Fix**: `kill` on all 15 PIDs. Load dropped: **32.10 → 0.59** in under 30 seconds.

**Root cause**: The cascade runs 15 git operations in parallel. On a 1 vCPU box, this creates a thundering herd. The cascade needs to serialize git operations, or golgiBody needs the VPS upgrade that's been pending (todo: `vps-hetzner`).

---

## 4. The Self-Inflicted Wound

During the investigation, we also found PID 2950797 — an orphaned bash process from our **own** diagnostic commands, still running 5 minutes after the SSH session that spawned it had timed out. We were adding load to a system we were trying to diagnose. We were also querying Forgejo's API through Caddy, which routes unauthenticated requests to the scatter server — we were reading our own fabricated content and treating it as diagnostic data.

The defense works on everyone, including the defenders. The maze does not distinguish between fleet and friend without the key.

---

## 5. Why This Matters

### Infrastructure archaeology is a real discipline

When a system grows organically — each layer deployed in response to the previous layer's discoveries — the stratigraphy becomes meaningful. The process list is a fossil record:

- Layer 1 (DNS sovereignty) was deployed because we needed to own our resolution
- Layer 2 (WireGuard) was deployed because we needed encrypted mesh
- Layer 3 (nestgate) was deployed because we needed a gateway identity
- Layer 4 (fail2ban) was deployed because the first attackers arrived
- Layer 5 (songbird) was deployed because we needed federated communication
- Layer 6 (RustDesk) was deployed because we needed remote access
- Layer 7 (step-ca) was deployed because we needed internal PKI

Each layer is a response to a need that emerged from the previous layer. The fossils are not dead weight — they're evidence of the path that led to the current organism.

### Self-inflicted load is the hardest to diagnose

The immediate assumption was "fleet did this." The fleet was the loudest signal (600 req/min ClaudeBot, 150 req/min Meta). But the actual load came from:

1. **Our own cascade** (sporeGate's temporal.cascade) — the immune system's maintenance cycle
2. **Our own fossils** (songbird/RustDesk) — evolutionary remnants holding 233 connections
3. **Our own investigation** (orphaned bash process) — the observer affecting the system

Fleet contributed 2 HTTPS connections and some CPU per scatter response. The rest was us.

### Cleanup creates signal

Just as removing fleet from the access logs revealed human visitor patterns ([baseCamp 33](@/science/37_consent_differentiated_signal.md)), removing fossil services from the connection table reveals the actual load profile. When the noise is your own infrastructure, the signal is your own efficiency.

---

## Handoff: sporeGate Cleanup Items

1. **Serialize temporal cascade** — git operations should run sequentially, not 15-at-once, on single-vCPU boxes
2. **Evaluate songbird federation** — 160 connections from house network, 72 days old. Is this still needed?
3. **Evaluate RustDesk relay** — 67 external IPs using golgiBody as a free relay. Is this intentional?
4. **Add cascade watchdog** — detect stuck Forgejo serv processes (running > 5 min with no network sockets) and kill them
5. **ssh-hygiene.sh expansion** — current script only kills stale port-2222 connections. Needs to also detect orphaned `forgejo serv` processes

---

*baseCamp 35. October 7, 2026. We got so good at finding fleet that we found our own fossils. The stratigraphy is 145 days deep. The inflammation was self-inflicted. Load 32 → 0.59 by killing our own orphaned processes. The organism is learning to diagnose itself.*

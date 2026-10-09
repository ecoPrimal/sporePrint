+++
title = "Dual Nervous System: Binary Reflex and Structured Voice"
description = "Wave 167k: tarpc binary IPC (bincode over UDS) activates alongside JSON-RPC. 6 primals speak both protocols — subconscious reflexes at 10-50μs, structured voice at 100-500μs. Protocol escalation upgrades hot paths automatically."
date = 2026-10-09
weight = 25

[taxonomies]
primals = ["beardog", "barracuda", "biomeos", "nestgate", "skunkbat", "songbird", "squirrel", "sweetgrass"]

[extra]
domain = "Architecture"
maturity = "live"
+++

## Overview

> **Status (Wave 167k):** 6 primals serve both tarpc (binary) and JSON-RPC (text) on golgiBody. tarpc handles on-silicon hot-paths at 10-50μs round-trip. JSON-RPC handles cross-gate and external communication at 100-500μs. Protocol escalation upgrades connections automatically when both sides support binary RPC.

Every primal in the ecoPrimals ecosystem communicates via JSON-RPC 2.0 over Unix domain sockets — structured, human-readable, debuggable. This is the **voice**: the protocol primals use to talk to the outside world, to cross trust boundaries, and to be inspected.

Starting at Wave 167k, six primals also serve **tarpc** — a binary RPC protocol using [bincode](https://docs.rs/bincode) serialization over length-delimited Unix domain sockets. This is the **subconscious**: the protocol primals use to talk to each other on the same silicon, without the overhead of text serialization.

Both protocols coexist. Both are the same organism. The choice of which to use is made per-connection, per-trust-tier, automatically.

## Why Two Protocols

JSON-RPC is excellent for what it does:

- **Human-readable**: `curl` a socket and read the response
- **Self-describing**: field names travel with the data
- **Cross-version safe**: new fields don't break old clients
- **Debuggable**: pipe through `jq`, grep for method names, read logs

But JSON-RPC has structural costs:

- **Base64 encoding**: binary data (keys, signatures, ciphertexts) must be text-encoded, inflating size by 33%
- **Field name repetition**: `"jsonrpc"`, `"method"`, `"params"` appear in every message
- **Parse cost**: full JSON parse at both ends — allocations, UTF-8 validation, hash-map construction
- **Connection-per-request**: each JSON-RPC call opens a new UDS connection

For a single health check, these costs are invisible. For a provenance write that calls {{ entity(name="beardog") }} three times (BLAKE3 hash + HMAC + Ed25519 sign), the serialization overhead exceeds the cryptographic work.

tarpc eliminates all of these:

| Property | JSON-RPC | tarpc/bincode |
|----------|----------|---------------|
| Serialization | ~2-5μs (serde_json) | ~100-300ns (bincode) |
| Binary data | Base64 encoded (+33%) | Raw bytes |
| Field names | Strings on every message | Compile-time type system |
| Allocations | 3-5 per call | 0-1 |
| Connection | New UDS per request | Persistent multiplexed channel |
| Authentication | riboCipher `[0xEC, 0x01]` prefix | Physical — same socket, same silicon |

## Architecture

### Dual-Socket Pattern

Most primals bind two sockets:

```
/run/membrane/beardog.sock         ← JSON-RPC (30 methods)
/run/membrane/beardog.tarpc.sock   ← tarpc/bincode (30 methods)
```

Same 30 methods, same functionality, two serialization formats. A local primal that wants sub-millisecond crypto calls connects to `.tarpc.sock`. An external probe or cross-gate client connects to `.sock` with the riboCipher authentication prefix.

### G65 Protocol Negotiation

{{ entity(name="squirrel") }}'s gossip engine (swarmVine) uses a single socket with per-connection negotiation:

```
Client:  PROTOCOLS: tarpc,jsonrpc\n
Server:  PROTOCOL: tarpc\n
→ binary channel established
```

The client declares what it speaks. The server picks the best match. Local primals prefer tarpc. External clients get JSON-RPC. One socket, two protocols, zero configuration.

### Protocol Escalation

The {{ entity(name="biomeos") }} orchestrator includes a Protocol Escalation Engine that monitors connections at runtime. When it detects a hot path — high request count, low latency, both sides healthy, tarpc available — it automatically upgrades the connection from JSON-RPC to tarpc.

This is motor learning for distributed systems. Frequently-used reflexes move from conscious (JSON-RPC, deliberate, inspectable) to subconscious (tarpc, binary, fast). The escalation is reversible: if either side becomes unhealthy, the connection falls back to JSON-RPC.

## Trust Tiers

The dual-protocol architecture maps to three trust tiers:

| Tier | Protocol | Authentication | Use case |
|------|----------|----------------|----------|
| **On-silicon** | tarpc/bincode | Physical (same UDS namespace) | Primal-to-primal hot-paths |
| **Cross-gate** | JSON-RPC | riboCipher `[0xEC, 0x01]` prefix | Gate-to-gate over WireGuard |
| **External** | JSON-RPC / HTTP | Standard web auth | Web APIs, federation, monitoring |

tarpc requires no authentication signal because the transport IS the authentication. You can only connect to `beardog.tarpc.sock` if you're running on the same machine, in the same filesystem namespace. The socket file's permissions are the access control. This is the highest trust tier — silicon trust.

JSON-RPC carries the riboCipher `[0xEC, 0x01]` prefix because it crosses boundaries. Cross-gate communication traverses WireGuard tunnels. External communication traverses the public internet. The authentication overhead exists because the trust boundary exists.

## Live Socket Map

All sockets verified live on golgiBody as of Wave 167k:

| Primal | tarpc Socket | JSON-RPC Socket | tarpc Methods |
|--------|-------------|-----------------|---------------|
| {{ entity(name="beardog") }} | `beardog.tarpc.sock` | `beardog.sock` | 30 (crypto) |
| {{ entity(name="skunkbat") }} | `skunkbat.tarpc.sock` | `skunkbat.sock` | 16+ (ingest) |
| {{ entity(name="barracuda") }} | `math.tarpc.sock` | `math.sock` | compute |
| nestGate | `nestgate.tarpc.sock` | `nestgate.sock` | storage |
| songbird | `songbird.tarpc.sock` | `songbird.sock` | discovery |
| swarmVine | `swarmvine.sock` (G65) | `swarmvine.sock` (G65) | 9 (gossip) |

## The Biological Analogy

The human architect named this the "dual nervous system" and the metaphor is structural, not decorative:

**Autonomic nervous system** → tarpc. Handles reflexes you don't think about. Heart rate, digestion, pupil dilation. Fast because it's binary — fixed structure, no negotiation, no explanation. Your stomach doesn't send JSON to your intestines.

**Somatic nervous system** → JSON-RPC. Handles deliberate communication. Speech, writing, gestures. Slower because the overhead is the point — you're crossing a boundary between two minds. Field names exist because the receiver might not share your type system.

**Protocol escalation** → motor learning. When you learn to type, every keystroke starts as a conscious somatic action. With practice, it becomes autonomic — your fingers move without thought. The escalation engine does the same thing: frequently-used IPC paths graduate from JSON-RPC (deliberate) to tarpc (reflexive).

Both systems are essential. The subconscious frees the voice to do what only the voice can do: cross boundaries, carry authentication, be debuggable. The voice frees the subconscious to do what only the subconscious can do: be fast, be binary, be silent.

---

*Wave 167k — October 9, 2026. Six primals, two protocols, one organism.*

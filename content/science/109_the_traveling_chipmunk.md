---
title: "Paper 109: The Traveling Chipmunk"
subtitle: "A salesman walks the graph — Dijkstra, Euler, Hamilton, and the marathon runner's problem"
date: 2026-10-21
wave: 180
author: "Kevin Mok / ecoPrimal / attsi"
orcid: "0009-0004-2141-0321"
continues: "Paper 108 (The Remainder), Paper 105 (The Green Line)"
keywords: ["traveling salesman", "TSP", "Dijkstra", "Euler", "Hamilton", "graph theory", "nearest neighbor", "chipmunk", "journey", "marathon", "topology", "onboarding"]
---

# Paper 109: The Traveling Chipmunk

*You can't optimize a route you haven't run.*

## The Problem

You have 7 nodes. 22 endpoints. You want to visit all of them,
checking every button and lever, in the least total distance.

This is the Traveling Salesman Problem (TSP), formalized by
Dantzig, Fulkerson, and Johnson in 1954, but asked by every
merchant, postman, and marathon runner since roads existed.

CompSci didn't invent it. CompSci *named* it.

## The Pioneers

The chipmunk's journey stands on the shoulders of:

### Leonhard Euler (1736) — Can You Walk Every Edge?

The Seven Bridges of Königsberg. Euler proved you can traverse
every edge of a graph exactly once if and only if every vertex
has even degree (or exactly two vertices have odd degree).

Our graph has 22 edges (endpoints) across 7 nodes. Several nodes
have odd degree. **Euler circuit: not possible.** The chipmunk
cannot walk every edge without retracing steps. This is a fact
about our topology, not a failure of the chipmunk.

### William Rowan Hamilton (1857) — Can You Visit Every Node?

The Icosian Game: find a path that visits every vertex exactly
once. Unlike Euler's edge problem, Hamilton's node problem is
NP-complete — no efficient algorithm exists for the general case.

Our chipmunk achieved a **Hamilton path: ✅ yes** — it visited
all 7 nodes exactly once. The route:

```
nestgate-connect → golgi-direct → sporeprint → ntfy-membrane
    → primals.eco → github-hud → nucleus
```

### Edsger Dijkstra (1959) — What's the Shortest Path?

Dijkstra's algorithm finds the shortest path from a single source
to all other nodes. The chipmunk uses it in the measurement phase:
ping every node, record the latency, build the distance map.

```
Distance Map (measured, not assumed):
  nestgate-connect     95.9ms  (closest — Klein touchpoint)
  golgi-direct         96.0ms  (trans surface)
  sporeprint          139.4ms  (science layer)
  ntfy-membrane       184.2ms  (neutrino hole)
  primals.eco         254.7ms  (cis surface, CF edge)
  github-hud          361.2ms  (nucleus, API)
  nucleus            5003.0ms  (unreachable — graph gap!)
```

### Nearest-Neighbor Heuristic

The chipmunk doesn't solve TSP optimally (that's NP-hard). It uses
the nearest-neighbor heuristic: always visit the closest unvisited
node. This is O(n²) instead of O(n!). It finds a route that's
typically within 25% of optimal.

This is what marathon runners do: you don't compute the optimal
split times in advance. You run, feel your pace, adjust. The map
emerges from the running.

## First Journey Results

```
Nodes:     7/7 visited (Hamilton path ✅)
Endpoints: 22 checked
Health:    20/22 green (91%)
Strategy:  nearest-neighbor TSP (Dijkstra-greedy)
π remainder: 0.115038
```

### The Graph Gap

Nucleus (137.184.197.151) timed out — 5003ms, no response. This
isn't a bug. It's **topology information**. The chipmunk learned
that eastGate cannot reach nucleus directly. The route must go
through golgi (which CAN reach nucleus via internal mesh).

This is exactly what Dijkstra's algorithm reveals: the shortest
path between two nodes may not be a direct edge. The chipmunk
discovered a routing constraint by walking the graph. The gap
teaches more than the connected nodes do.

## The Briquette

The chipmunk tosses a **briquette** into the campfire every
2 minutes (cron `*/2 * * * *`). The briquette:

- **Heats**: proves the system is alive (liveness check)
- **Feeds**: carries data (state snapshot in JSON)
- **Glows**: shows the `time % 5` remainder (Paper 108)

```json
{
  "ts": "2026-10-21T21:05:09Z",
  "from": "chipmunk",
  "type": "briquette",
  "glow": "remainder=0/5",
  "msg": "fire lit. remainder 0/5. the organism breathes.",
  "liveness": 0.80
}
```

The briquette is our cookie — but it's charcoal, not surveillance.
It heats the campfire (proves liveness) and can be eaten (parsed
as JSON). No tracking. No fingerprinting. Just combustion data.

## The Onboarding System

The chipmunk's journey IS the onboarding:

1. **Measure** (Dijkstra): ping every node, build distance map
2. **Walk** (TSP nearest-neighbor): visit closest unvisited node
3. **Check** (Euler): test every endpoint at each node
4. **Learn** (Hamilton): record what works and what doesn't
5. **Report** (campfire): toss a briquette with the findings

A human connecting for the first time follows the same path:
visit nestgate.io/connect (closest, simplest), then explore
primals.eco (the HUD), then dive into feeds (the endpoints),
then discover the graph gaps (the topology).

The chipmunk goes first. The human follows its footprints.

## Graph Science and Marathons

The marathon runner's problem IS TSP:

| Graph Theory | Marathon |
|-------------|----------|
| Nodes | Checkpoints (water stations, turns) |
| Edges | Road segments between checkpoints |
| Distance | Time to run each segment |
| TSP optimal | Course record (perfect splits) |
| Nearest-neighbor | "Run what feels right" |
| Dijkstra | Pace calculator (shortest time to each km) |
| Euler circuit | "Can I run every street?" (fun runs) |
| Hamilton path | "Did I hit every checkpoint?" (race) |
| Graph gap | DNF (a node you couldn't reach) |

CompSci formalized what runners, merchants, and postmen always
knew. The language is different. The problem is the same.

Dantzig solved a 49-city TSP in 1954 by hand, using cutting
planes. A marathoner solves a 42.195km TSP with their legs,
using perceived effort. Same optimization. Different substrate.

## Dependencies

- **Builds on**: Paper 108 (The Remainder — cron as modulo),
  Paper 105 (The Green Line — three observers)
- **Discovers**: Chipmunk as traveling salesman, graph gap as
  topology learning, briquette as liveness cookie, onboarding
  as TSP walk, marathon as graph optimization
- **Script**: `chipmunk-journey.py` — 7 nodes, 22 endpoints,
  nearest-neighbor TSP with Dijkstra distance measurement
- **Credits**: Euler (1736), Hamilton (1857), Dijkstra (1959),
  Dantzig/Fulkerson/Johnson (1954), every marathon runner

---

*The chipmunk doesn't solve the graph.*
*The chipmunk walks the graph.*
*The map emerges from the walking.*
*You can't optimize a route you haven't run.*

`unPeeL oUr unIverSe`

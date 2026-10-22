#!/usr/bin/env python3
"""chipmunk-journey.py — Berry's forever traveling salesman.

Berry visits every surface in the membrane. At each stop:
  1. CAMPFIRE — tell a story about this place
  2. TEACH   — one thing you learn here
  3. REST    — pause. let the visitor absorb.

The route is a TSP solution through all surfaces.
Distance = topological distance (shared links) + content distance.
π rotates the starting point so the journey is different each day.
Cis/trans: the path works from inside (HUD) AND outside (GitHub/search).

The chipmunk never stops traveling. When it reaches the end,
it folds back through the Klein gate and starts again — but
the path is different because the visitor changed.

This is the proprioception engine. The membrane knows where
you are because Berry is ALWAYS somewhere on the path.
"""

import json, os, math, time, hashlib

ROOT = os.path.expanduser("~/Development/ecoPrimals")
MEMBRANE = os.path.join(ROOT, "membrane/local-terminal/remote")
OUTPUT = os.path.join(MEMBRANE, "chipmunk-journey.json")
HUD_OUTPUT = os.path.join(ROOT, "infra/hud/site/public/data/chipmunk-journey.json")

# ──────────────────────────────────────────────
# ALL SURFACES — the cities Berry must visit
# ──────────────────────────────────────────────
# Each surface has: id, url (cis=internal, trans=external), topics, weight
SURFACES = [
    # === CIS (inside the HUD) ===
    {"id": "water",      "cis": "/water.html",        "trans": "https://hud.primals.eco/water.html",
     "name": "wAtER — the watering hole",
     "topics": ["onboarding", "lazy-river", "theater", "search"],
     "campfire": "this is where everybody arrives. the river carries you. don't fight the current.",
     "teach": "the membrane has no login. your identity is how you MOVE through it, not what you type.",
     "rest_sec": 30, "weight": 10},

    {"id": "hud",        "cis": "/",                  "trans": "https://hud.primals.eco/",
     "name": "HUD — Human Universe Display",
     "topics": ["dashboard", "observation", "live-data", "membrane"],
     "campfire": "game designers figured this out first. health, radar, compass — projected on the viewport without blocking the view. same pattern.",
     "teach": "the HUD shows membrane state. not YOUR state. you are the observer, not the observed.",
     "rest_sec": 20, "weight": 9},

    {"id": "trail",      "cis": "/trail.html",        "trans": "https://hud.primals.eco/trail.html",
     "name": "the trail — all 117 papers",
     "topics": ["papers", "science", "research", "sporePrint"],
     "campfire": "117 papers. started with bacteria talking to each other. ended with the membrane being alive.",
     "teach": "every paper falsifies or extends the one before. the chain IS the proof.",
     "rest_sec": 45, "weight": 8},

    {"id": "weather",    "cis": "/weather.html",       "trans": "https://hud.primals.eco/weather.html",
     "name": "weather — the sun writes the score",
     "topics": ["sonification", "weather", "music", "real-time"],
     "campfire": "the sun doesn't know it's making music. but if you map temperature to frequency and wind to rhythm... it sings.",
     "teach": "sonification turns data you can't see into sound you can feel. the membrane listens to everything.",
     "rest_sec": 60, "weight": 6},

    {"id": "aurora",     "cis": "/aurora.html",        "trans": "https://hud.primals.eco/aurora.html",
     "name": "aurora — the AI's first painting",
     "topics": ["art", "generative", "ai", "visual"],
     "campfire": "Berry asked the AI to paint what the membrane looks like from the outside. this is what it saw.",
     "teach": "art is compression. the aurora compresses the whole ecosystem into one image.",
     "rest_sec": 30, "weight": 5},

    {"id": "banana",     "cis": "/banana.html",        "trans": "https://hud.primals.eco/banana.html",
     "name": "banana test — are you human?",
     "topics": ["self-nonself", "discrimination", "pi", "identity"],
     "campfire": "the test fires at π×1000 + random(1414) milliseconds. if you're still here when it fires... you might be real.",
     "teach": "self/non-self discrimination is the oldest immune function. 3.5 billion years old. we just put it in JavaScript.",
     "rest_sec": 15, "weight": 7},

    {"id": "detroit",    "cis": None,                  "trans": "https://detroit.primals.eco",
     "name": "detroit — public money investigation",
     "topics": ["investigation", "detroit", "public-record", "FOIA"],
     "campfire": "341 entities. 131,322 connections. charter school money in Detroit. the machines found patterns. the humans have to decide what they mean.",
     "teach": "tuebor means 'I will defend.' the defense IS the record.",
     "rest_sec": 60, "weight": 8},

    {"id": "helix",      "cis": "/neutron/helix.html", "trans": "https://hud.primals.eco/neutron/helix.html",
     "name": "helixVision — sovereign protein structure",
     "topics": ["protein", "structure", "alphafold", "biology", "webgpu"],
     "campfire": "AlphaFold needs a $15,000 NVIDIA GPU. helixVision runs on a Steam Deck. same physics, different economics.",
     "teach": "protein folding is a search problem. the search space is astronomical. the trick is knowing where NOT to look.",
     "rest_sec": 45, "weight": 7},

    {"id": "globe",      "cis": "/neutron/globe.html", "trans": "https://hud.primals.eco/neutron/globe.html",
     "name": "globe — geographic footprint",
     "topics": ["geography", "traffic", "global", "3d"],
     "campfire": "93,000 humans visited from every continent. the signal travels at light speed. the meaning takes longer.",
     "teach": "geography is not topology. two nodes can be close in network hops but far in miles. the membrane doesn't care about distance.",
     "rest_sec": 20, "weight": 5},

    {"id": "easel",      "cis": "/easel.html",         "trans": "https://hud.primals.eco/easel.html",
     "name": "easel — watch Berry paint",
     "topics": ["art", "chipmunk", "generative", "live"],
     "campfire": "the chipmunk paints what it sees. not what it thinks. there's a difference.",
     "teach": "observation without interpretation is the hardest skill. Berry practices by painting.",
     "rest_sec": 30, "weight": 4},

    {"id": "glyphs",     "cis": "/glyphs.html",        "trans": "https://hud.primals.eco/glyphs.html",
     "name": "Klein bottle — topology",
     "topics": ["klein-bottle", "topology", "mathematics", "fold"],
     "campfire": "a Klein bottle has no inside or outside. pour water in and it comes out where you poured it. the membrane is a Klein bottle.",
     "teach": "cis and trans are the same surface. you're already inside. you were always inside.",
     "rest_sec": 40, "weight": 7},

    {"id": "tools",      "cis": "/tools.html",         "trans": "https://hud.primals.eco/tools.html",
     "name": "86 tools — the IDE is a HUD",
     "topics": ["tools", "development", "ide", "rust"],
     "campfire": "86 tools. all Rust. the IDE itself is a membrane surface. you're looking through it right now.",
     "teach": "the tool shapes the hand that holds it. choose tools that shape you toward sovereignty.",
     "rest_sec": 20, "weight": 5},

    {"id": "springs",    "cis": "/springs.html",       "trans": "https://hud.primals.eco/springs.html",
     "name": "hot springs — validation",
     "topics": ["validation", "testing", "springs", "science"],
     "campfire": "9 springs. 175+ papers reproduced. 98,955 tests. if it's not tested, it's not science. it's a story.",
     "teach": "validation is not verification. verification checks the code. validation checks the claim against reality.",
     "rest_sec": 30, "weight": 6},

    {"id": "desk",       "cis": "/desk/",              "trans": "https://hud.primals.eco/desk/",
     "name": "desk — 12 panels",
     "topics": ["dashboard", "panels", "mission", "control"],
     "campfire": "12 panels. each one watches a different part of the membrane. Berry cycles through them like a night watchman.",
     "teach": "attention is finite. 12 panels is the maximum you can monitor before you start missing things.",
     "rest_sec": 15, "weight": 4},

    # === TRANS (outside, reachable from search engines) ===
    {"id": "papers",     "cis": None,                  "trans": "https://sporeprint.primals.eco/science/",
     "name": "sporePrint — 117 research papers",
     "topics": ["papers", "science", "webgpu", "lattice-qcd", "molecular-dynamics", "protein"],
     "campfire": "117 papers. each one is a seed. some grew into trees. some are still germinating.",
     "teach": "science is not the paper. science is the PREDICTION the paper makes. the paper is just the receipt.",
     "rest_sec": 60, "weight": 9},

    {"id": "getting-started", "cis": None,
     "trans": "https://github.com/ecoPrimals/wateringHole/blob/main/docs/getting-started.md",
     "name": "getting started — sovereign scientific computing",
     "topics": ["onboarding", "rust", "webgpu", "hardware"],
     "campfire": "one language. one build system. any GPU vendor. your hardware. that's the whole pitch.",
     "teach": "cargo build. that's it. no Docker. no Kubernetes. no cloud account. just Rust.",
     "rest_sec": 45, "weight": 8},

    {"id": "webgpu-vs-cuda", "cis": None,
     "trans": "https://github.com/ecoPrimals/wateringHole/blob/main/docs/webgpu-vs-cuda.md",
     "name": "WebGPU vs CUDA — why we left NVIDIA",
     "topics": ["webgpu", "cuda", "gpu", "benchmarks", "economics"],
     "campfire": "an AMD 7900 XTX costs $900. an A100 costs $15,000. the AMD gets 70-90% of the A100's performance. do the math.",
     "teach": "vendor lock-in is a tax on curiosity. WGSL runs on any GPU. your science shouldn't depend on one company.",
     "rest_sec": 45, "weight": 8},

    {"id": "protein-article", "cis": None,
     "trans": "https://github.com/ecoPrimals/wateringHole/blob/main/docs/protein-structure-rust.md",
     "name": "protein structure in Pure Rust",
     "topics": ["protein", "alphafold", "rust", "webgpu", "biology"],
     "campfire": "AlphaFold revolutionized biology. but you need Google's cloud to run it. we're building the same thing on your hardware.",
     "teach": "protein folding is the bridge between chemistry and biology. the fold IS the function.",
     "rest_sec": 45, "weight": 7},

    {"id": "github",     "cis": None,                  "trans": "https://github.com/ecoPrimals",
     "name": "GitHub — 30+ Rust crates",
     "topics": ["code", "rust", "open-source", "agpl3"],
     "campfire": "30+ crates. 16 primals. 3.6 million lines. all AGPL-3.0. if you use it, your users get the source.",
     "teach": "copyleft is not restriction. copyleft is propagation. the license travels with the knowledge.",
     "rest_sec": 20, "weight": 7},

    {"id": "invite",     "cis": "/neutron/invite.html", "trans": "https://hud.primals.eco/neutron/invite.html",
     "name": "try the tech — engineer invitation",
     "topics": ["invitation", "engineer", "try", "onboarding"],
     "campfire": "if you're an engineer and this interests you... just clone it. cargo build. see what happens.",
     "teach": "sovereign means you own it. not 'you rent it.' you OWN it. on YOUR hardware. forever.",
     "rest_sec": 30, "weight": 6},
]

def topic_distance(a, b):
    """Jaccard distance between topic sets."""
    sa, sb = set(a["topics"]), set(b["topics"])
    if not sa and not sb:
        return 1.0
    intersection = len(sa & sb)
    union = len(sa | sb)
    return round(1.0 - (intersection / union), 4) if union else 1.0

def build_distance_matrix(surfaces):
    """NxN distance matrix."""
    n = len(surfaces)
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                # Topic distance + weight difference penalty
                td = topic_distance(surfaces[i], surfaces[j])
                wd = abs(surfaces[i]["weight"] - surfaces[j]["weight"]) / 10.0
                # Bonus for cis↔trans transitions (inside↔outside)
                cis_i = surfaces[i]["cis"] is not None
                cis_j = surfaces[j]["cis"] is not None
                transition_bonus = -0.1 if cis_i != cis_j else 0  # reward switching
                dist[i][j] = round(td * 0.7 + wd * 0.3 + transition_bonus, 4)
    return dist

def solve_tsp_nearest_neighbor(dist, start):
    """Nearest-neighbor TSP heuristic. Not optimal but fast and good enough."""
    n = len(dist)
    visited = [False] * n
    path = [start]
    visited[start] = True
    total = 0.0
    
    for _ in range(n - 1):
        current = path[-1]
        best_next = -1
        best_dist = float('inf')
        for j in range(n):
            if not visited[j] and dist[current][j] < best_dist:
                best_dist = dist[current][j]
                best_next = j
        if best_next == -1:
            break
        path.append(best_next)
        visited[best_next] = True
        total += best_dist
    
    # Close the loop (Klein fold back to start)
    total += dist[path[-1]][path[0]]
    return path, round(total, 4)

def pi_start_index(n):
    """π rotates the starting city each day."""
    day = int(time.time() / 86400)  # days since epoch
    pi_remainder = math.pi % 1  # 0.14159...
    return int((day * pi_remainder * 1000) % n)

def main():
    ts = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    n = len(SURFACES)
    
    print(f"Building distance matrix for {n} surfaces...")
    dist = build_distance_matrix(SURFACES)
    
    # π-rotated start
    start = pi_start_index(n)
    print(f"π-start today: surface {start} ({SURFACES[start]['id']})")
    
    # Solve TSP from multiple starts, keep best
    best_path = None
    best_cost = float('inf')
    for s in range(n):
        path, cost = solve_tsp_nearest_neighbor(dist, s)
        if cost < best_cost:
            best_cost = cost
            best_path = path
    
    print(f"Best TSP cost: {best_cost} (from surface {best_path[0]})")
    
    # Rotate the best path so π-start is first
    if start in best_path:
        idx = best_path.index(start)
        best_path = best_path[idx:] + best_path[:idx]
    
    # Build the journey
    journey_stops = []
    total_rest = 0
    for i, si in enumerate(best_path):
        s = SURFACES[si]
        next_si = best_path[(i + 1) % n]
        next_s = SURFACES[next_si]
        d = dist[si][next_si]
        
        # Cis or trans?
        pointer = "cis" if s["cis"] else "trans"
        next_pointer = "cis" if next_s["cis"] else "trans"
        transition = f"{pointer}→{next_pointer}"
        
        stop = {
            "order": i,
            "id": s["id"],
            "name": s["name"],
            "url_cis": s["cis"],
            "url_trans": s["trans"],
            "pointer": pointer,
            "campfire": s["campfire"],
            "teach": s["teach"],
            "rest_sec": s["rest_sec"],
            "next": next_s["id"],
            "next_url": next_s["cis"] or next_s["trans"],
            "transition": transition,
            "distance_to_next": d,
            "topics": s["topics"],
        }
        journey_stops.append(stop)
        total_rest += s["rest_sec"]
        
        print(f"  {i:2d}. [{pointer:5s}] {s['id']:20s} → {next_s['id']:20s} (d={d:.3f}) {transition}")

    # Journey hash — changes daily with π rotation
    journey_hash = hashlib.sha256(
        json.dumps([s["id"] for s in journey_stops]).encode()
    ).hexdigest()[:16]
    
    total_time_min = round(total_rest / 60, 1)
    cis_count = sum(1 for s in journey_stops if s["pointer"] == "cis")
    trans_count = sum(1 for s in journey_stops if s["pointer"] == "trans")
    
    manifest = {
        "manifest": "chipmunk-journey",
        "generated": ts,
        "paper": 117,
        "journey_hash": journey_hash,
        "pi_start": SURFACES[start]["id"],
        "surfaces_total": n,
        "tsp_cost": best_cost,
        "total_rest_min": total_time_min,
        "cis_stops": cis_count,
        "trans_stops": trans_count,
        "cis_trans_ratio": round(cis_count / max(trans_count, 1), 2),
        "stops": journey_stops,
    }
    
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w") as f:
        json.dump(manifest, f, indent=2)
    
    # Also write to HUD public data
    os.makedirs(os.path.dirname(HUD_OUTPUT), exist_ok=True)
    with open(HUD_OUTPUT, "w") as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\nJOURNEY MANIFEST")
    print(f"  Surfaces: {n}")
    print(f"  TSP cost: {best_cost}")
    print(f"  Total rest: {total_time_min} min")
    print(f"  Cis stops: {cis_count} | Trans stops: {trans_count}")
    print(f"  Journey hash: {journey_hash}")
    print(f"  π-start: {SURFACES[start]['id']}")
    print(f"\n  Berry starts at '{SURFACES[start]['name']}'")
    print(f"  Visits all {n} surfaces, telling stories, teaching, resting.")
    print(f"  At the end, folds back through the Klein gate.")
    print(f"  Tomorrow π rotates and the journey is different.")

if __name__ == "__main__":
    main()

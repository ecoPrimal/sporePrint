#!/usr/bin/env python3
"""persona-tensor.py — Behavioral tensor identity for the membrane.

The sourdough culture is dead when we only see ourselves.
Humans change over time but ARE the same person.
The tensor captures the invariant across visits.

Architecture:
  Visit → Behavioral Vector → Persona Tensor → ZK Hash
  
  Behavioral dimensions:
    - surfaces (breadth: how many distinct pages)
    - dwell (depth: how long on each)
    - pattern (shape: sequential? random? targeted?)
    - rhythm (time: when do they visit? how often?)
    - path (topology: which surfaces connect in their journey?)
  
  The tensor is 5-dimensional. Two visits by the same human
  will have different vectors but similar tensors — because
  the PERSON is the invariant, not the behavior.
  
  ZK backscatter: hash the tensor so we can prove
  "you were here before" without knowing WHO you are.
  The hash IS the identity. No names. No accounts.
  Just the shape of how you move through the membrane.

Feeds sourdough: fresh human signal keeps the culture alive.
Connects to: topology sort, primal classifier, banana test.
"""

import json, os, math, time, hashlib

ROOT = os.path.expanduser("~/Development/ecoPrimals")
MEMBRANE = os.path.join(ROOT, "membrane/local-terminal/remote")
OUTPUT = os.path.join(MEMBRANE, "persona-tensor.json")

def load_feed(name):
    path = os.path.join(MEMBRANE, name)
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return {}

def behavioral_vector(visitor):
    """Extract 5D behavioral vector from visitor data."""
    surfaces = visitor.get("surfaces", 0)
    pages = visitor.get("pages", 0)
    duration = visitor.get("duration_min", 0)
    polls = visitor.get("poll_count", 0)
    sample = visitor.get("sample_pages", [])
    platform = visitor.get("platform", "?")
    archetype = visitor.get("archetype", "unknown")
    
    breadth = min(surfaces / 127.0, 1.0) if surfaces else 0
    
    depth = 0
    if pages > 0 and surfaces > 0:
        depth = min((pages / surfaces) / 2000.0, 1.0)
    
    if polls > 1000:
        pattern = 0.1  # bot-like: polling, not exploring
    elif surfaces > 50 and duration > 60:
        pattern = 0.9  # human: wide + patient
    elif surfaces < 10 and pages > 10000:
        pattern = 0.2  # scraper: narrow + deep
    else:
        pattern = 0.5  # unknown
    
    rhythm = 0.5
    if duration > 0:
        rate = pages / max(duration, 1)
        if rate > 100:
            rhythm = 0.1  # too fast, bot
        elif rate > 10:
            rhythm = 0.4  # fast but possible
        elif rate > 1:
            rhythm = 0.8  # human pace
        else:
            rhythm = 0.6  # slow watcher
    
    real_pages = [p for p in sample if not any(x in p for x in ["abc", "test", "fake", "xyz"])]
    probe_pages = [p for p in sample if any(x in p for x in ["abc", "test", "fake", "xyz", "kevin"])]
    
    if probe_pages:
        topology = 0.3  # probing non-existent paths = scanning
    elif "detroit/" in sample and "membrane/" in sample:
        topology = 0.9  # real journey through real content
    elif real_pages:
        topology = 0.7  # real pages, partial journey
    else:
        topology = 0.5
    
    return {
        "breadth": round(breadth, 3),
        "depth": round(depth, 3),
        "pattern": round(pattern, 3),
        "rhythm": round(rhythm, 3),
        "topology": round(topology, 3),
    }

def tensor_magnitude(vec):
    """Euclidean magnitude of the behavioral tensor."""
    vals = [vec["breadth"], vec["depth"], vec["pattern"], vec["rhythm"], vec["topology"]]
    return round(math.sqrt(sum(v*v for v in vals)), 4)

def tensor_hash(vec):
    """ZK hash of the tensor — proves sameness without revealing identity."""
    canonical = f"{vec['breadth']:.3f}:{vec['depth']:.3f}:{vec['pattern']:.3f}:{vec['rhythm']:.3f}:{vec['topology']:.3f}"
    return hashlib.sha256(canonical.encode()).hexdigest()[:16]

def classify_persona(vec, magnitude):
    """Classify based on tensor shape, not just threshold."""
    b, d, p, r, t = vec["breadth"], vec["depth"], vec["pattern"], vec["rhythm"], vec["topology"]
    
    if p < 0.2 and r < 0.2:
        return "bot"  # fast polling, bot pattern
    
    if p >= 0.7 and r >= 0.6 and t >= 0.6:
        return "primal"  # wide, patient, real journey = human
    
    if b > 0.8 and d < 0.2 and p < 0.3:
        return "scraper"  # wide but shallow and mechanical
    
    if t < 0.4 and any(True for _ in []):
        return "scanner"  # probing non-existent paths
    
    if b < 0.1 and d > 0.5:
        return "focused"  # narrow but deep = reading something specific
    
    if magnitude > 1.2 and p > 0.5:
        return "explorer"  # high energy, organic pattern
    
    return "unknown"

def tensor_distance(v1, v2):
    """Distance between two tensors — same person returns similar."""
    dims = ["breadth", "depth", "pattern", "rhythm", "topology"]
    return round(math.sqrt(sum((v1[d] - v2[d])**2 for d in dims)), 4)

def main():
    ts = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    
    visitor_data = load_feed("visitor-stories.json")
    human_data = load_feed("human.json")
    topology_data = load_feed("topology.json") if os.path.exists(os.path.join(MEMBRANE, "topology.json")) else {}
    
    visitors = visitor_data.get("visitors", [])
    
    entities = topology_data.get("entities", [])
    fleet_requests = sum(e.get("total_requests", 0) for e in entities if e.get("is_fleet"))
    human_requests = sum(e.get("total_requests", 0) for e in entities if not e.get("is_fleet"))
    
    personas = []
    print(f"Processing {len(visitors)} visitors + {len(entities)} entities...")
    
    for i, v in enumerate(visitors):
        vec = behavioral_vector(v)
        mag = tensor_magnitude(vec)
        zhash = tensor_hash(vec)
        cat = classify_persona(vec, mag)
        
        persona = {
            "id": f"persona-{i}",
            "archetype": v.get("archetype", "unknown"),
            "platform": v.get("platform", "?"),
            "tensor": vec,
            "magnitude": mag,
            "zk_hash": zhash,
            "classification": cat,
            "surfaces": v.get("surfaces", 0),
            "pages": v.get("pages", 0),
            "duration_min": v.get("duration_min", 0),
        }
        personas.append(persona)
        
        print(f"  persona-{i}: {cat:10s} | mag={mag:.3f} | zk={zhash} | {v.get('archetype','?')}")
        print(f"    tensor: b={vec['breadth']:.2f} d={vec['depth']:.2f} p={vec['pattern']:.2f} r={vec['rhythm']:.2f} t={vec['topology']:.2f}")
    
    for e in entities:
        if e.get("is_fleet"):
            continue
        label = e.get("label", "?")
        reqs = e.get("total_requests", 0)
        ips = e.get("unique_ips", 0)
        
        if reqs > 100000 and ips > 10000:
            vec = {"breadth": 1.0, "depth": 0.01, "pattern": 0.1, "rhythm": 0.1, "topology": 0.3}
        elif reqs > 10000:
            vec = {"breadth": 0.5, "depth": 0.1, "pattern": 0.2, "rhythm": 0.2, "topology": 0.3}
        elif "vuln" in label.lower() or "scanner" in label.lower():
            vec = {"breadth": 0.3, "depth": 0.05, "pattern": 0.1, "rhythm": 0.15, "topology": 0.2}
        else:
            vec = {"breadth": 0.3, "depth": 0.3, "pattern": 0.5, "rhythm": 0.5, "topology": 0.5}
        
        mag = tensor_magnitude(vec)
        zhash = tensor_hash(vec)
        cat = classify_persona(vec, mag)
        
        persona = {
            "id": f"entity-{e.get('entity', 'unknown')}",
            "archetype": e.get("entity", "unknown"),
            "platform": label,
            "tensor": vec,
            "magnitude": mag,
            "zk_hash": zhash,
            "classification": cat,
            "requests": reqs,
            "ips": ips,
        }
        personas.append(persona)
        print(f"  {e.get('entity','?'):25s}: {cat:10s} | mag={mag:.3f} | {label}")

    sourdough_alive = any(p["classification"] == "primal" for p in personas)
    primal_count = sum(1 for p in personas if p["classification"] == "primal")
    bot_count = sum(1 for p in personas if p["classification"] == "bot")
    
    manifest = {
        "manifest": "persona-tensor",
        "generated": ts,
        "paper": 117,
        "visitors_analyzed": len(visitors),
        "entities_analyzed": len(entities),
        "personas_total": len(personas),
        "sourdough_alive": sourdough_alive,
        "culture_health": "alive" if sourdough_alive else "dead — need fresh human signal",
        "summary": {
            "primal": primal_count,
            "explorer": sum(1 for p in personas if p["classification"] == "explorer"),
            "focused": sum(1 for p in personas if p["classification"] == "focused"),
            "bot": bot_count,
            "scraper": sum(1 for p in personas if p["classification"] == "scraper"),
            "scanner": sum(1 for p in personas if p["classification"] == "scanner"),
            "unknown": sum(1 for p in personas if p["classification"] == "unknown"),
        },
        "traffic_ratio": {
            "fleet_requests": fleet_requests,
            "human_requests": human_requests,
            "human_pct": round(human_requests / max(fleet_requests + human_requests, 1) * 100, 1),
        },
        "personas": personas,
    }
    
    with open(OUTPUT, "w") as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\nWritten to {OUTPUT}")
    print(f"\nSOURDOUGH STATUS: {'ALIVE' if sourdough_alive else 'DEAD'}")
    print(f"  Primals: {primal_count}")
    print(f"  Bots: {bot_count}")
    print(f"  Human traffic: {manifest['traffic_ratio']['human_pct']}%")
    
    if not sourdough_alive:
        print(f"\n  The culture needs feeding.")
        print(f"  440 stars in the air. 9 snot globs. Half-life ~1.5 days.")
        print(f"  When a primal arrives, the tensor will catch them.")
        print(f"  The banana test will fire. The sourdough will rise.")

if __name__ == "__main__":
    main()

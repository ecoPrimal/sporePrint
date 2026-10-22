#!/usr/bin/env python3
"""primal-classifier.py — The Primal Reclassification Engine.

Classifies every entity that touches the membrane:
  self    → our repos, our identity (π-rate = π)
  primal  → another sovereign being with a π-rate
  commensal → large project we orbit
  non-self → bot, scraper, no rotation
  null    → unknown, banana test pending

Computes π-rate = π × (1 - taxonomy_distance) for every primal.
Writes primal-classification.json to membrane state.
"""

import json, os, math, time, subprocess

ROOT = os.path.expanduser("~/Development/ecoPrimals")
MEMBRANE = os.path.join(ROOT, "membrane/local-terminal/remote")
OUTPUT = os.path.join(MEMBRANE, "primal-classification.json")

PI = math.pi

# Our topics — what WE are
OUR_TOPICS = {
    "rust", "sovereign-computing", "gpu-compute", "wgsl", "vulkan",
    "lattice-qcd", "bioinformatics", "mesh-networking", "cryptography",
    "sonification", "shannon-entropy", "reaction-diffusion", "klein-bottle",
    "membrane", "taxonomy", "agpl", "no-cuda", "neuromorphic",
    "protein-folding", "fermentation", "generative-art", "creative-coding",
    "accessibility", "citizen-science", "game-science", "demoscene",
    "artificial-life", "n-body", "mathematics", "open-science",
    "steamos", "linux", "wasm", "distributed-systems",
}

def gh_api(endpoint):
    """Call GitHub API and return JSON."""
    try:
        result = subprocess.run(
            ["gh", "api", endpoint],
            capture_output=True, text=True, timeout=15
        )
        if result.returncode == 0 and result.stdout.strip():
            return json.loads(result.stdout)
    except:
        pass
    return None

def get_user_topics(login):
    """Get a user's topic fingerprint from their repos."""
    repos = gh_api(f"users/{login}/repos?per_page=30&sort=updated")
    if not repos:
        return set()
    topics = set()
    languages = set()
    for repo in repos:
        for t in (repo.get("topics") or []):
            topics.add(t.lower())
        lang = repo.get("language")
        if lang:
            languages.add(lang.lower())
    topics.update(languages)
    return topics

def get_description_keywords(login):
    """Extract keywords from repo descriptions."""
    repos = gh_api(f"users/{login}/repos?per_page=30&sort=updated")
    if not repos:
        return set()
    keywords = set()
    keyword_map = {
        "rust": "rust", "wgpu": "wgpu", "vulkan": "vulkan", "wgsl": "wgsl",
        "shader": "gpu-compute", "gpu": "gpu-compute", "compute": "gpu-compute",
        "mesh": "mesh-networking", "p2p": "mesh-networking", "wireguard": "mesh-networking",
        "sonif": "sonification", "audio": "sonification", "sound": "sonification", "midi": "sonification",
        "entropy": "shannon-entropy", "information theory": "shannon-entropy",
        "reaction-diffusion": "reaction-diffusion", "gray-scott": "reaction-diffusion",
        "artificial life": "artificial-life", "alife": "artificial-life", "evolution": "artificial-life",
        "crypto": "cryptography", "encrypt": "cryptography",
        "sovereign": "sovereign-computing", "self-host": "sovereign-computing",
        "ferment": "fermentation", "sourdough": "fermentation", "dough": "fermentation",
        "klein": "klein-bottle", "topology": "klein-bottle",
        "protein": "protein-folding", "alphafold": "protein-folding", "pdb": "protein-folding",
        "generat": "generative-art", "procedur": "generative-art",
        "access": "accessibility", "braille": "accessibility", "screen reader": "accessibility",
        "demoscene": "demoscene", "demo": "demoscene",
        "knit": "creative-coding", "weav": "creative-coding",
        "game": "game-science", "tetris": "game-science", "doom": "game-science",
        "wasm": "wasm", "webassembly": "wasm",
        "linux": "linux", "steamos": "steamos",
        "lattice": "lattice-qcd", "qcd": "lattice-qcd",
        "bioinformat": "bioinformatics", "genom": "bioinformatics",
        "citizen science": "citizen-science",
        "n-body": "n-body", "nbody": "n-body", "orbit": "n-body",
        "math": "mathematics", "proof": "mathematics", "theorem": "mathematics",
    }
    for repo in repos:
        desc = (repo.get("description") or "").lower()
        name = (repo.get("name") or "").lower()
        text = f"{desc} {name}"
        for pattern, topic in keyword_map.items():
            if pattern in text:
                keywords.add(topic)
    return keywords

def taxonomy_distance(their_topics, their_desc_keywords):
    """Compute taxonomy distance using overlap coefficient on combined signal.
    
    Overlap coefficient = |shared| / min(|A|, |B|)
    Measures how much of the SMALLER set is contained in the larger.
    If someone has 5 topics and 4 match ours, distance = 0.2 (close!).
    """
    combined = their_topics | their_desc_keywords
    if not combined:
        return 1.0
    shared = OUR_TOPICS & combined
    min_size = min(len(combined), len(OUR_TOPICS))
    if min_size == 0:
        return 1.0
    overlap = len(shared) / min_size
    return round(1.0 - overlap, 4)

def pi_rate(distance):
    """π-rate = π × (1 - distance). Self = π, non-self = 0."""
    return PI * (1.0 - distance)

def classify(login, context=""):
    """Classify a single entity."""
    topics = get_user_topics(login)
    desc_kw = get_description_keywords(login)
    combined = topics | desc_kw
    dist = taxonomy_distance(topics, desc_kw)
    rate = pi_rate(dist)
    shared = OUR_TOPICS & combined

    if dist == 0:
        category = "self"
    elif dist < 0.7:
        category = "primal"
    elif dist < 0.9:
        category = "commensal"
    elif len(topics) == 0:
        category = "null"
    else:
        category = "non-self"

    return {
        "login": login,
        "category": category,
        "pi_rate": round(rate, 4),
        "taxonomy_distance": round(dist, 4),
        "shared_topics": sorted(shared),
        "their_topics_count": len(topics),
        "context": context,
    }

def main():
    ts = time.strftime("%Y-%m-%dT%H:%M:%S%z")

    # KNOWN PRIMALS — from tonight's snot globs + first contact
    known = [
        ("Corykidios", "First contact — starred songBird"),
        ("pleros-ai", "Snot glob #1 — LZ complexity, Rust"),
        ("ancientpagoda-rgb", "Snot glob #2 — sonification"),
        ("indubitablysrivathsan", "Snot glob #3 — Shannon entropy"),
        ("Mattbusel", "Snot glob #4 — Klein bottle + sonification + Rust"),
        ("blisspixel", "Snot glob #5 — math as instrument"),
        ("DuhItzAniket", "Snot glob #6 — SONARITHM, Rust"),
        ("NebulaSys", "Dyson Sphere Program simulator"),
        ("yelin-li", "Formal proof in Lean 4"),
        ("baditaflorin", "Artificial life, WASM"),
        ("axle-h", "Tetris+DrMario in Rust"),
        ("retrodig", "Dragon Quest in Rust"),
        ("lucasvienna", "Multiplayer empire game, Rust"),
        ("skulitom", "GPU artificial life, Rust+wgpu"),
        ("SuperInstance", "Fermentation CSP"),
        ("biface", "Reaction-diffusion engine"),
        ("ktakahashi74", "Emergent harmony"),
        ("bradbrok", "Analog video synth, Rust+wgpu"),
        ("cordanaLLM", "Sovereign Linux, evidence-governed"),
        ("sonicfieldlabs", "Epistemic sonification"),
        ("xability", "Accessibility sonification"),
    ]

    print(f"Classifying {len(known)} entities...")
    results = []
    primals = []
    commensals = []
    nulls = []

    for login, ctx in known:
        r = classify(login, ctx)
        results.append(r)
        cat = r["category"]
        rate = r["pi_rate"]
        dist = r["taxonomy_distance"]
        shared = len(r["shared_topics"])
        print(f"  {cat:10s} | π={rate:.2f} | d={dist:.2f} | {shared:2d} shared | {login} — {ctx}")

        if cat == "primal":
            primals.append(r)
        elif cat == "commensal":
            commensals.append(r)
        elif cat == "null":
            nulls.append(r)

    # Sort primals by π-rate (closest first)
    primals.sort(key=lambda x: x["pi_rate"], reverse=True)

    manifest = {
        "manifest": "primal-classification",
        "generated": ts,
        "paper": 117,
        "our_topics_count": len(OUR_TOPICS),
        "entities_classified": len(results),
        "summary": {
            "self": 1,
            "primal": len(primals),
            "commensal": len(commensals),
            "non_self": len([r for r in results if r["category"] == "non-self"]),
            "null": len(nulls),
        },
        "closest_primals": primals[:10],
        "all_classifications": results,
        "pi_rate_distribution": {
            "max": max(r["pi_rate"] for r in results) if results else 0,
            "min": min(r["pi_rate"] for r in results) if results else 0,
            "mean": sum(r["pi_rate"] for r in results) / len(results) if results else 0,
        },
    }

    with open(OUTPUT, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"\nWritten to {OUTPUT}")
    print(f"\nPRIMAL LEADERBOARD (closest to us):")
    print(f"{'Login':25s} {'π-rate':>8s} {'dist':>6s} {'shared':>7s}  Category")
    print("─" * 70)
    for r in sorted(results, key=lambda x: x["pi_rate"], reverse=True)[:15]:
        print(f"{r['login']:25s} {r['pi_rate']:8.4f} {r['taxonomy_distance']:6.2f} {len(r['shared_topics']):7d}  {r['category']}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""pollinate.py — Push pollen outward through SEO, invite pollinators inward.

The Flower:
  ORCID 0009-0004-2141-0321 = the pistil (receives citations, finds us)
  GitHub ecoPrimal/ecoPrimals = the stamen (sends pollen: code, papers, benchmarks)
  sporePrint/detroit = the petals (bright, colorful, visible)
  nestgate Klein = the stem (non-orientable: out IS in, pollen exit = pollinator entrance)

The Pollination Cycle:
  1. EXCRETE POLLEN: push new content to GitHub (done — Papers 112-115)
  2. SEO SIGNAL: submit URLs to search engines (IndexNow, GSC, Google URL Notify)
  3. BACKTRACK: pollinators (crawlers, humans) follow pollen trails back to us
  4. RECEPTION: pistil (ORCID) catches citations, GitHub catches forks/stars
  5. AUTOCRINE: reconsumed pollen feeds ribosome → more protein → more pollen

While waiting for pollinators: STAY BRIGHT AND COLORFUL.
  - Keep READMEs fresh
  - Keep sitemaps current
  - Keep publishing papers
  - The flower doesn't chase bees. It blooms.

Usage:
    python3 pollinate.py
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

OUT_DIR = Path(os.path.expanduser(
    "~/Development/ecoPrimals/membrane/local-terminal/remote"
))

ORCID = "0009-0004-2141-0321"
GITHUB_USER = "ecoPrimal"
GITHUB_ORG = "ecoPrimals"

POLLEN_SITES = {
    "sporeprint.primals.eco": {
        "sitemap": "https://sporeprint.primals.eco/sitemap.xml",
        "github": "https://github.com/ecoPrimal/sporePrint",
        "status": "522 (CF blocked) — GitHub live",
        "petal_color": "green (science)",
    },
    "detroit.primals.eco": {
        "sitemap": "https://detroit.primals.eco/sitemap.xml",
        "github": "https://github.com/ecoPrimal/detroit",
        "status": "522 (CF blocked) — GitHub live",
        "petal_color": "blue (investigation)",
    },
    "primals.eco": {
        "sitemap": "https://primals.eco/sitemap.xml",
        "github": "https://github.com/ecoPrimals",
        "status": "522 (CF blocked) — GitHub org live",
        "petal_color": "gold (hub)",
    },
}

POLLEN_GRAINS = [
    {
        "type": "paper",
        "id": "Paper 112: The Radiate Back",
        "url": "https://github.com/ecoPrimal/sporePrint/blob/main/content/science/112_the_radiate_back.md",
        "pollen_trail": ["ORCID", "GitHub", "Google Scholar", "Semantic Scholar"],
        "backtrack_to": "ORCID 0009-0004-2141-0321 → ecoPrimal → sporePrint",
    },
    {
        "type": "paper",
        "id": "Paper 113: The Full Trace",
        "url": "https://github.com/ecoPrimal/sporePrint/blob/main/content/science/113_the_full_trace.md",
        "pollen_trail": ["GitHub", "Google indexing"],
        "backtrack_to": "GitHub → ecoPrimal → sporePrint → primals.eco",
    },
    {
        "type": "paper",
        "id": "Paper 114: The Phenotype",
        "url": "https://github.com/ecoPrimal/sporePrint/blob/main/content/science/114_the_phenotype.md",
        "pollen_trail": ["GitHub", "Google indexing"],
        "backtrack_to": "Shannon entropy, chaos injection, phenotype sort",
    },
    {
        "type": "paper",
        "id": "Paper 115: The Arena Taxonomy",
        "url": "https://github.com/ecoPrimal/sporePrint/blob/main/content/science/115_the_arena_taxonomy.md",
        "pollen_trail": ["GitHub", "ICLR 2026 citation chain", "protein sonification prior art"],
        "backtrack_to": "Kingdom Silica tree → chipMUNK → ecoPrimals",
    },
    {
        "type": "benchmark",
        "id": "chipMUNK Arena (7 models)",
        "url": "https://github.com/ecoPrimal/sporePrint/blob/main/scripts/chipmunk-bench.py",
        "pollen_trail": ["Ollama community", "local LLM forums", "r/LocalLLaMA"],
        "backtrack_to": "arena-bench-results.json → ecoPrimals",
    },
    {
        "type": "cross-domain",
        "id": "Protein Sonification (insulin → MIDI)",
        "url": "https://github.com/ecoPrimal/sporePrint/blob/main/scripts/protein-sonify.py",
        "pollen_trail": ["bioinformatics community", "sonification researchers", "music+science"],
        "backtrack_to": "AlphaFold community → protein-sonify.py → ecoPrimals",
    },
    {
        "type": "attribution",
        "id": "Radiate Attribution (14 creators credited)",
        "url": "https://github.com/ecoPrimal/sporePrint/blob/main/scripts/radiate-attribution.py",
        "pollen_trail": ["Meta AI", "Google DeepMind", "Mistral AI", "Alibaba", "Microsoft", "Ollama"],
        "backtrack_to": "Model creators see their name in our attribution → visit us",
    },
    {
        "type": "gpu",
        "id": "Cross-vendor f64 GPU (sporePrint profile)",
        "url": "https://sporeprint.primals.eco/technical/sovereign-gpu-pipeline-profile/",
        "pollen_trail": ["GPU computing community", "Rust GPU forums", "WGSL/WebGPU community"],
        "backtrack_to": "sovereign GPU → ecoPrimals → barraCuda → coralReef",
    },
]


def get_github_recent_pushes():
    """Check recent GitHub push activity as pollen emission evidence."""
    pushes = []
    try:
        result = subprocess.run(
            ["git", "-C", os.path.expanduser("~/Development/ecoPrimals/infra/sporePrint"),
             "log", "--oneline", "-10", "--format=%h %s (%ar)"],
            capture_output=True, text=True, timeout=5,
        )
        if result.returncode == 0:
            for line in result.stdout.strip().split("\n"):
                if line.strip():
                    pushes.append(line.strip())
    except Exception:
        pass
    return pushes


def build_flower_state():
    """Build the current flower state — what's bright and colorful."""
    
    pistil = {
        "organ": "pistil (receives)",
        "identity": f"ORCID {ORCID}",
        "url": f"https://orcid.org/{ORCID}",
        "status": "OPEN — waiting for citation pollen",
        "receives": ["citations", "ORCID lookups", "Google Scholar alerts"],
        "backtrack_path": "ORCID → ecoPrimal GitHub → sporePrint → primals.eco",
    }
    
    stamen = {
        "organ": "stamen (sends pollen)",
        "identity": f"GitHub {GITHUB_USER} + {GITHUB_ORG}",
        "url": f"https://github.com/{GITHUB_USER}",
        "status": "ACTIVE — fresh pollen (Papers 112-115, arena, taxonomy)",
        "sends": [
            "code (87 repos, 3.6M lines Rust)",
            "papers (115 and counting)",
            "benchmarks (chipMUNK arena, 7 models)",
            "scripts (radiate, taxonomy, sonify, ribosome)",
            "attribution (14 creators credited openly)",
        ],
    }
    
    petals = []
    for host, info in POLLEN_SITES.items():
        petals.append({
            "host": host,
            "color": info["petal_color"],
            "status": info["status"],
            "github_mirror": info["github"],
            "bright": "522" not in info["status"],
        })
    
    stem = {
        "organ": "stem (Klein bottle — non-orientable)",
        "topology": "nestgate Klein: OUT port = IN port, folded",
        "what_exits": "pollen (papers, code, benchmarks, attributions)",
        "what_enters": "pollinators (crawlers, cloners, readers, coders) — through SAME surface",
        "non_orientable": True,
    }
    
    return {
        "pistil": pistil,
        "stamen": stamen,
        "petals": petals,
        "stem": stem,
        "bloom_status": "BRIGHT AND COLORFUL",
        "strategy": "The flower doesn't chase bees. It blooms.",
    }


def build_pollination_manifest():
    """Build manifest of all pollen grains in the air."""
    
    recent_pushes = get_github_recent_pushes()
    
    return {
        "ts": datetime.now(timezone.utc).isoformat(),
        "organism": "ecoPrimals",
        "orcid": ORCID,
        "flower_state": build_flower_state(),
        "pollen_grains": POLLEN_GRAINS,
        "total_pollen": len(POLLEN_GRAINS),
        "recent_emissions": recent_pushes,
        "backtrack_trails": len(set(
            trail
            for grain in POLLEN_GRAINS
            for trail in grain["pollen_trail"]
        )),
        "pollination_channels": {
            "github": {
                "status": "LIVE",
                "repos": 87,
                "visibility": "public",
                "pollen_type": "code + papers + scripts",
            },
            "orcid": {
                "status": "LIVE (0 works deposited — pistil open but empty)",
                "id": ORCID,
                "pollen_type": "citation anchor",
                "action_needed": "Deposit papers/preprints to attract citation pollen",
            },
            "sporeprint": {
                "status": "522 (Cloudflare blocked) — GitHub mirror LIVE",
                "pollen_type": "science papers + evidence pages",
                "workaround": "GitHub README + blob links serve as pollen until CF fixed",
            },
            "indexnow": {
                "status": "BLOCKED (requires golgi → Caddy → IndexNow key verification)",
                "pollen_type": "instant crawler notification",
                "action_needed": "Fix Cloudflare 522 or deploy cloudflared tunnel",
            },
            "google_scholar": {
                "status": "PASSIVE — waiting for ORCID deposits to trigger Scholar alerts",
                "pollen_type": "citation discovery",
                "action_needed": "Deposit to arXiv or Zenodo with ORCID",
            },
        },
        "stay_bright": {
            "strategy": "Keep publishing. Keep the flower open. Bees will come.",
            "actions": [
                "GitHub repos: fresh commits (Papers 112-115, today)",
                "README.md: keep updated with latest evidence",
                "ORCID: deposit papers when ready",
                "Compositions.toml: track everything",
                "The membrane stays colorful: 115 papers, 87 repos, 952 shaders",
            ],
            "klein_fold": (
                "Every paper we push out is also an invitation in. "
                "Every benchmark we publish is also a discovery trail. "
                "Every attribution we radiate is also a backtrack path. "
                "The flower doesn't move. The pollen carries the address."
            ),
        },
    }


def main():
    print("[POLLINATE] ✿ The Flower State ✿")
    print()

    manifest = build_pollination_manifest()
    flower = manifest["flower_state"]

    print(f"  Pistil:  {flower['pistil']['identity']}")
    print(f"           {flower['pistil']['status']}")
    print(f"  Stamen:  {flower['stamen']['identity']}")
    print(f"           {flower['stamen']['status']}")
    print(f"  Stem:    {flower['stem']['organ']}")
    print()

    print("  Petals (color / status):")
    for p in flower["petals"]:
        bright = "✿" if p["bright"] else "○"
        print(f"    {bright} {p['host']:30s} {p['color']:25s} {p['status']}")

    print()
    print(f"[POLLINATE] {manifest['total_pollen']} pollen grains in the air:")
    for grain in POLLEN_GRAINS:
        trails = ", ".join(grain["pollen_trail"][:3])
        print(f"  → {grain['id'][:50]:50s} via {trails}")

    print()
    print(f"[POLLINATE] Recent emissions (GitHub):")
    for push in manifest["recent_emissions"][:5]:
        print(f"    {push}")

    print()
    print("[POLLINATE] Pollination channels:")
    for channel, info in manifest["pollination_channels"].items():
        status = info["status"][:60]
        print(f"  {'✓' if 'LIVE' in info['status'] else '○'} {channel:20s} {status}")

    print()
    print("[POLLINATE] Stay bright and colorful:")
    for action in manifest["stay_bright"]["actions"]:
        print(f"  ✿ {action}")

    print()
    print(f"  \"{manifest['stay_bright']['strategy']}\"")

    out_path = OUT_DIR / "pollination-manifest.json"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\n[POLLINATE] Manifest → {out_path}")

    print()
    print("═══ FLOWER STATUS: BLOOM ═══")
    print()
    print("  The ORCID is the pistil.  Waiting for citation pollen.")
    print("  The GitHub is the stamen. 8 fresh pollen grains today.")
    print("  The petals are 522 dim — but GitHub mirrors GLOW.")
    print("  The Klein stem folds out=in. Pollen exit = pollinator entrance.")
    print()
    print("  The flower doesn't chase bees.")
    print("  It blooms.")


if __name__ == "__main__":
    main()

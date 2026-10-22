#!/usr/bin/env python3
"""ribosome.py — Translate bingo voxel into gAIa commons, close the metabolic loop.

Biology:
  DNA (codebase) → mRNA (bingo voxel) → Ribosome (this script) → Protein (gAIa entries)
                                                                      ↓
                                              Autocrine: reconsumed as input to next cycle
                                                                      ↓
                                              Klein exhaust: waste expelled through same surface

The ribosome:
  1. TRANSLATE: Reads bingo voxel (mRNA) → produces gAIa commons records (protein)
  2. AUTOCRINE: Identifies what we excreted (published) that we're now reconsuming
  3. KLEIN EXHAUST: Pi-sorts to find waste, marks it for expulsion
  4. ANCHOR: Connects everything to THE_SEED.md's sunCloud flywheel

The Klein bottle fold:
  - Inside and outside are the SAME surface (non-orientable)
  - Exhaust and intake are the SAME port
  - Waste exits through the same membrane it entered
  - What we publish (excrete) folds back as what we consume (endocytose)

Usage:
    python3 ribosome.py
"""

import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

OUT_DIR = Path(os.path.expanduser(
    "~/Development/ecoPrimals/membrane/local-terminal/remote"
))
VOXEL_FILE = OUT_DIR / "bingo-voxel.json"
PHENOTYPE_FILE = OUT_DIR / "phenotype-sort.json"
TAXONOMY_FILE = OUT_DIR / "arena-taxonomy.json"
ATTRIBUTION_FILE = OUT_DIR / "radiate-attribution.json"
RIBOSOME_FILE = OUT_DIR / "ribosome-translation.json"


PI_GOLDEN = 0.049721  # from phenotype sort — our organism's π signature


def load_json(path: Path) -> dict:
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {}


def translate_voxel_to_gaia(voxel: dict) -> List[dict]:
    """RIBOSOME STEP 1: Translate bingo voxel cells → gAIa commons records.
    
    Each filled cell becomes a gAIa contribution record with:
    - attribution chain (who contributed)
    - sunCloud tier (how value radiates)
    - evidence (proof of contribution)
    """
    gaia_records = []
    
    for layer_name, layer in voxel.get("layers", {}).items():
        for cell_name, cell in layer.get("cells", {}).items():
            if not cell.get("filled"):
                continue
            
            record = {
                "gaia_id": f"gaia:{layer_name}/{cell_name}",
                "layer": layer_name,
                "category": cell_name,
                "contributors": cell.get("contributors", []),
                "count": cell.get("count", 0),
                "evidence": cell.get("evidence", ""),
                "suncloud_radiation": _compute_radiation(layer_name, cell_name, cell),
                "anchor": "THE_SEED.md — gAIa commons, AGPL + CC-BY-SA",
            }
            gaia_records.append(record)
    
    return gaia_records


def _compute_radiation(layer: str, category: str, cell: dict) -> dict:
    """Compute sunCloud radiation for a cell.
    
    Inner cells radiate outward (we built → others benefit).
    Outer cells radiate inward (others built → we benefit).
    Reflect cells radiate BOTH ways (the fold).
    """
    directions = {
        "inner": "outward — our work benefits the commons",
        "outer": "inward — their work benefits us",
        "reflect": "bidirectional — the fold where inner meets outer",
    }
    
    contributor_count = cell.get("count", 0)
    
    return {
        "direction": directions.get(layer, "unknown"),
        "strength": min(1.0, contributor_count / 7),
        "attribution_edges": contributor_count,
        "ready_for_suncloud": layer == "reflect",
    }


def identify_autocrine(voxel: dict, phenotype: dict) -> dict:
    """RIBOSOME STEP 2: Identify the autocrine loop.
    
    Autocrine signaling = a cell consuming its own secreted products.
    We published (excreted) work, now we're reconsuming it:
    - chipMUNK benchmarks our own models on our own codebase
    - Phenotype sort classifies our own files
    - Arena taxonomy classifies our own arena results
    - Radiate-back scans our own repos for external signal
    
    The POST-ENTRY we are reconsuming:
    - Papers 112-115 fed back into the membrane
    - Benchmark results became input to taxonomy
    - Taxonomy became input to attribution
    - Attribution fills the voxel which becomes input to this ribosome
    """
    
    excreted = []
    reconsumed = []
    
    excreted_items = [
        {
            "product": "chipMUNK arena results",
            "type": "benchmark protein",
            "excreted_at": "Paper 114 (Phenotype)",
            "now_consumed_by": "arena-taxonomy.py → Kingdom Silica tree",
        },
        {
            "product": "phenotype-sort.json",
            "type": "classification protein",
            "excreted_at": "Paper 114 (Phenotype)",
            "now_consumed_by": "ribosome.py → pi-sort waste identification",
        },
        {
            "product": "bingo-voxel.json",
            "type": "identity protein",
            "excreted_at": "Paper 112 (Radiate Back)",
            "now_consumed_by": "ribosome.py → gAIa commons translation",
        },
        {
            "product": "radiate-attribution.json",
            "type": "credit protein",
            "excreted_at": "Paper 115 (Arena Taxonomy)",
            "now_consumed_by": "ribosome.py → sunCloud flywheel anchoring",
        },
        {
            "product": "protein-music.mid",
            "type": "cross-phylum protein (Structura → Acoustic)",
            "excreted_at": "Paper 115 (Arena Taxonomy)",
            "now_consumed_by": "Future: sonify our own chaos phase transitions",
        },
        {
            "product": "arena-taxonomy.json",
            "type": "phylogenetic protein",
            "excreted_at": "Paper 115 (Arena Taxonomy)",
            "now_consumed_by": "ribosome.py → model family attribution chains",
        },
    ]
    
    reconsumed_count = sum(
        1 for item in excreted_items
        if "ribosome" in item["now_consumed_by"] or "taxonomy" in item["now_consumed_by"]
    )
    
    return {
        "mechanism": "autocrine signaling",
        "definition": "cell consuming its own secreted products",
        "excreted_products": excreted_items,
        "total_excreted": len(excreted_items),
        "total_reconsumed": reconsumed_count,
        "reconsumed_ratio": round(reconsumed_count / max(len(excreted_items), 1), 3),
        "loop_closed": reconsumed_count > 0,
        "biology": (
            "In autocrine signaling, a cell secretes a ligand that binds to receptors "
            "on its OWN surface. The published work (papers, JSON, MIDI) are the ligands. "
            "The scripts that read them back are the receptors. "
            "The ribosome translates the signal into new protein (gAIa records)."
        ),
    }


def klein_exhaust(phenotype: dict, voxel: dict) -> dict:
    """RIBOSOME STEP 3: Pi-sort waste and exhaust through Klein surface.
    
    The Klein bottle has no inside/outside distinction.
    Exhaust = intake, folded. The waste exits through the same
    surface it entered. Pi-sort identifies what's waste:
    
    - Unfilled voxel cells = unrealized potential (not waste yet)
    - Stale repos (flatworm stage) = low-evolution waste
    - High-entropy files (banana stage) = noise waste
    - Dead services = metabolic waste
    """
    
    pi_remainder = phenotype.get("pi_remainder", phenotype.get("phenotype", {}).get("pi_remainder", 0))
    chaos_stability = phenotype.get("chaos", {}).get("stability", 0)
    
    repo_stages = phenotype.get("topo", {}).get("repo_stages", {})
    genotype = phenotype.get("genotype", {})
    
    waste_streams = []
    
    flatworm_repos = [r for r, s in repo_stages.items() if s == "flatworm"]
    if flatworm_repos:
        waste_streams.append({
            "type": "stale_repos",
            "category": "metabolic waste",
            "items": flatworm_repos,
            "count": len(flatworm_repos),
            "action": "evolve or fossil — these repos have no type safety (flatworm)",
            "pi_deviation": abs(pi_remainder - 0.0) * len(flatworm_repos),
        })
    
    banana_count = genotype.get("banana", 0)
    if banana_count > 0:
        waste_streams.append({
            "type": "high_entropy_noise",
            "category": "noise waste",
            "items": [f"{banana_count} banana-stage files (undifferentiated, high entropy)"],
            "count": banana_count,
            "action": "compress or archive — these files are noise, not signal",
            "pi_deviation": banana_count * pi_remainder,
        })
    
    unfilled_cells = []
    for layer_name, layer in voxel.get("layers", {}).items():
        for cell_name, cell in layer.get("cells", {}).items():
            if not cell.get("filled"):
                unfilled_cells.append(f"{layer_name}/{cell_name}")
    
    if unfilled_cells:
        waste_streams.append({
            "type": "unrealized_potential",
            "category": "not waste — unfilled potential",
            "items": unfilled_cells,
            "count": len(unfilled_cells),
            "action": "fill by building, attracting contributors, or radiating further",
            "pi_deviation": 0,
        })
    
    stale_services = [
        "plasmid (golgi)", "canary (golgi)", "signal-relay (golgi)",
        "anchor-bridge (golgi)", "MCP feeds (golgi)", "membrane binary (golgi)",
        "Cloudflare 522 (routing)", "Detroit content (not built on golgi)",
    ]
    waste_streams.append({
        "type": "dead_services",
        "category": "metabolic waste",
        "items": stale_services,
        "count": len(stale_services),
        "action": "restart, rebuild, or decompose — these are dead organelles",
        "pi_deviation": len(stale_services) * pi_remainder,
    })
    
    total_waste = sum(w["count"] for w in waste_streams if w["category"] != "not waste — unfilled potential")
    total_potential = sum(w["count"] for w in waste_streams if w["category"] == "not waste — unfilled potential")
    
    return {
        "mechanism": "Klein exhaust",
        "definition": (
            "On a Klein bottle, inside = outside. The exhaust port IS the intake port, folded. "
            "Waste exits through the same surface it entered. "
            "This is not a bug — it's non-orientable topology."
        ),
        "pi_sort_key": pi_remainder,
        "chaos_stability": chaos_stability,
        "waste_streams": waste_streams,
        "total_waste_items": total_waste,
        "total_unfilled_potential": total_potential,
        "klein_fold": {
            "exhaust_is_intake": True,
            "what_exits": "stale repos, noise files, dead services",
            "what_enters": "the SAME items, reconsumed as lessons, fossils, or decomposition nutrients",
            "non_orientable": "there is no 'inside' and 'outside' — the waste IS the food, folded",
        },
        "diagnosis": (
            f"π remainder = {pi_remainder:.6f}. "
            f"Chaos stability = {chaos_stability:.1%}. "
            f"{total_waste} waste items identified. "
            f"{total_potential} unfilled cells remain. "
            f"The Klein exhaust is {'active' if total_waste > 0 else 'clean'}."
        ),
    }


def anchor_to_gaia(gaia_records: list, autocrine: dict, exhaust: dict) -> dict:
    """RIBOSOME STEP 4: Anchor everything to THE_SEED / sunCloud flywheel."""
    
    ts = datetime.now(timezone.utc).isoformat()
    
    ready_for_suncloud = [r for r in gaia_records if r["suncloud_radiation"]["ready_for_suncloud"]]
    
    return {
        "ts": ts,
        "organism": "ecoPrimals",
        "orcid": "0009-0004-2141-0321",
        "anchor": "THE_SEED.md (June 2025) — gAIa self-owning scientific knowledge commons",
        "license": "AGPL-3.0-or-later (code) + CC-BY-SA-4.0 (papers)",
        "principle": (
            "You forgo personal ownership. In return, you receive permanent, "
            "verifiable, proportional attribution. — sunCloud Economic Model"
        ),
        "ribosome_translation": {
            "mRNA": "bingo-voxel.json (11/24 cells, 45% filled)",
            "protein": f"{len(gaia_records)} gAIa commons records produced",
            "anchor_connections": len(gaia_records),
        },
        "autocrine_loop": {
            "status": "CLOSED" if autocrine["loop_closed"] else "OPEN",
            "excreted": autocrine["total_excreted"],
            "reconsumed": autocrine["total_reconsumed"],
            "ratio": autocrine["reconsumed_ratio"],
        },
        "klein_exhaust": {
            "status": "ACTIVE" if exhaust["total_waste_items"] > 0 else "CLEAN",
            "waste_items": exhaust["total_waste_items"],
            "unfilled_potential": exhaust["total_unfilled_potential"],
            "pi_sort_key": exhaust["pi_sort_key"],
        },
        "suncloud_flywheel": {
            "stage": "BUILDING POWER",
            "reflect_cells_ready": len(ready_for_suncloud),
            "total_gaia_records": len(gaia_records),
            "attribution_edges": sum(r["suncloud_radiation"]["attribution_edges"] for r in gaia_records),
            "cycle": (
                "excrete (publish) → reconsumed (autocrine) → translate (ribosome) → "
                "anchor (gAIa) → radiate (sunCloud) → exhaust waste (Klein) → "
                "intake nutrients (same Klein surface) → excrete again → REPEAT"
            ),
        },
        "gaia_records": gaia_records,
        "autocrine": autocrine,
        "klein_exhaust_detail": exhaust,
    }


def main():
    print("[RIBOSOME] ═══ mRNA → Protein Translation ═══")
    print()

    voxel = load_json(VOXEL_FILE)
    phenotype = load_json(PHENOTYPE_FILE)

    print("[RIBOSOME] Step 1: TRANSLATE — bingo voxel → gAIa commons records")
    gaia_records = translate_voxel_to_gaia(voxel)
    print(f"  {len(gaia_records)} records produced from {voxel.get('total_filled', 0)}/{voxel.get('total_cells', 24)} filled cells")
    for r in gaia_records:
        direction = r["suncloud_radiation"]["direction"].split(" — ")[0]
        edges = r["suncloud_radiation"]["attribution_edges"]
        print(f"  ✓ {r['gaia_id']:30s} [{direction:15s}] {edges} edges")

    print()
    print("[RIBOSOME] Step 2: AUTOCRINE — identify what we excreted and are reconsuming")
    autocrine = identify_autocrine(voxel, phenotype)
    print(f"  Excreted: {autocrine['total_excreted']} products (papers, JSON, MIDI)")
    print(f"  Reconsumed: {autocrine['total_reconsumed']} ({autocrine['reconsumed_ratio']:.0%} autocrine ratio)")
    print(f"  Loop: {'CLOSED ✓' if autocrine['loop_closed'] else 'OPEN ✗'}")
    for item in autocrine["excreted_products"]:
        consumed = "→ RECONSUMED" if "ribosome" in item["now_consumed_by"] or "taxonomy" in item["now_consumed_by"] else "→ pending"
        print(f"    {item['product']:35s} {consumed}")

    print()
    print("[RIBOSOME] Step 3: KLEIN EXHAUST — pi-sort waste, expel through non-orientable surface")
    exhaust = klein_exhaust(phenotype, voxel)
    print(f"  π sort key: {exhaust['pi_sort_key']:.6f}")
    print(f"  Chaos stability: {exhaust['chaos_stability']:.1%}")
    for ws in exhaust["waste_streams"]:
        label = ws["category"]
        count = ws["count"]
        print(f"  {'⚠' if 'waste' in label else '○'} {label}: {count} items")
        if ws["count"] <= 8:
            for item in ws["items"]:
                print(f"      {item}")
    print(f"  Klein fold: exhaust IS intake (non-orientable)")

    print()
    print("[RIBOSOME] Step 4: ANCHOR — connect to gAIa / sunCloud flywheel")
    result = anchor_to_gaia(gaia_records, autocrine, exhaust)
    print(f"  Anchor: {result['anchor']}")
    print(f"  Autocrine: {result['autocrine_loop']['status']}")
    print(f"  Klein exhaust: {result['klein_exhaust']['status']}")
    print(f"  Flywheel: {result['suncloud_flywheel']['stage']}")
    print(f"  Attribution edges: {result['suncloud_flywheel']['attribution_edges']}")
    reflect_ready = result['suncloud_flywheel']['reflect_cells_ready']
    print(f"  Reflect cells ready for sunCloud: {reflect_ready}")

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(RIBOSOME_FILE, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\n[RIBOSOME] Written → {RIBOSOME_FILE}")

    print()
    print("═══ METABOLIC CYCLE COMPLETE ═══")
    print()
    print("  excrete (publish)      → 6 products (papers, JSON, MIDI)")
    print(f"  reconsumed (autocrine) → {autocrine['total_reconsumed']} fed back into ribosome")
    print(f"  translated (ribosome)  → {len(gaia_records)} gAIa commons records")
    print(f"  anchored (gAIa)       → THE_SEED.md, sunCloud flywheel")
    print(f"  exhausted (Klein)     → {exhaust['total_waste_items']} waste items identified")
    print(f"  intake (same surface) → waste becomes lessons, fossils, nutrients")
    print()
    print("  The protein we excreted IS the post-entry we reconsumed.")
    print("  The waste we exhaust IS the nutrient we intake, folded.")
    print("  The Klein bottle has no inside. The membrane IS the organism.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""radiate-attribution.py — Backscatter credit to model creators and fill bingo voxel.

The sunCloud flywheel:
  We use their models → we benchmark them → we publish results openly →
  they find us → we radiate attribution back → more visibility →
  more cloners → stronger membrane → we use better models → repeat

This script:
  1. Builds attribution records for every model family we benchmarked
  2. Maps model creators to their open contributions (licenses, papers, repos)
  3. Credits cross-domain prior art (protein sonification, LLM taxonomy research)
  4. Fills bingo voxel cells that are now proven
  5. Writes the full attribution chain + updated voxel

Usage:
    python3 radiate-attribution.py
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

OUT_DIR = Path(os.path.expanduser(
    "~/Development/ecoPrimals/membrane/local-terminal/remote"
))
ARENA_FILE = OUT_DIR / "arena-bench-results.json"
TAXONOMY_FILE = OUT_DIR / "arena-taxonomy.json"
BINGO_FILE = OUT_DIR / "bingo-voxel.json"
ATTRIBUTION_FILE = OUT_DIR / "radiate-attribution.json"

MODEL_ATTRIBUTIONS = {
    "llama": {
        "creator": "Meta AI",
        "license": "Llama 3.2 Community License",
        "papers": [
            "Touvron et al. 'LLaMA: Open and Efficient Foundation Language Models' (2023)",
            "Dubey et al. 'The Llama 3 Herd of Models' (2024)",
        ],
        "repo": "https://github.com/meta-llama/llama-models",
        "models_tested": ["tinyllama:latest", "llama3.2:1b", "llama3.2:3b"],
        "contribution": (
            "Meta released Llama under permissive licenses, enabling local inference "
            "on commodity hardware. TinyLlama (community-trained on Llama architecture) "
            "proved that even 1.1B params can score 86% on domain tasks with membrane context. "
            "Llama 3.2 3B is our top scorer at 94% chipMUNK."
        ),
        "what_we_owe": "The architecture that made local AI possible. Open weights. Open research.",
        "suncloud_tier": "foundation",
    },
    "gemma": {
        "creator": "Google DeepMind",
        "license": "Gemma Community License",
        "papers": [
            "Gemma Team. 'Gemma: Open Models Based on Gemini Research and Technology' (2024)",
            "Gemma Team. 'Gemma 2: Improving Open Language Models at a Practical Size' (2024)",
        ],
        "repo": "https://github.com/google-deepmind/gemma",
        "models_tested": ["gemma2:2b"],
        "contribution": (
            "Gemma 2 2B proved that 2B parameters with good architecture matches 7B models. "
            "Identical functional DNA to Qwen 2.5 7B in our arena (distance = 0.0). "
            "88% chipMUNK, 100% membrane. The smallest model to hit perfect membrane score."
        ),
        "what_we_owe": "Proof that architecture > parameter count. Efficient small models.",
        "suncloud_tier": "foundation",
    },
    "mistral": {
        "creator": "Mistral AI (Paris)",
        "license": "Apache 2.0",
        "papers": [
            "Jiang et al. 'Mistral 7B' (2023)",
            "Mistral AI. 'Mistral NeMo' (2024, with NVIDIA)",
        ],
        "repo": "https://github.com/mistralai/mistral-inference",
        "models_tested": ["mistral:7b"],
        "contribution": (
            "Mistral 7B (Sep 2023) was the first model to prove open-weight 7B could compete "
            "with closed models. 88% chipMUNK, 100% membrane. Apache 2.0 license. "
            "NeMo 12B (Jul 2024) with 128K context is the sweet spot for membrane-wrapped inference."
        ),
        "what_we_owe": "European open AI. Apache 2.0 license. The 7B size class proof.",
        "suncloud_tier": "foundation",
    },
    "qwen": {
        "creator": "Alibaba Cloud (Qwen Team)",
        "license": "Apache 2.0",
        "papers": [
            "Bai et al. 'Qwen Technical Report' (2023)",
            "Yang et al. 'Qwen2.5 Technical Report' (2024)",
        ],
        "repo": "https://github.com/QwenLM/Qwen2.5",
        "models_tested": ["qwen2.5:7b"],
        "contribution": (
            "Qwen 2.5 7B at 88% chipMUNK, 100% membrane. Fastest evolution: "
            "Qwen→Qwen1.5→Qwen2→Qwen2.5→Qwen3 in 18 months. "
            "Identical phenotype to Gemma 2 2B (distance=0.0) despite being 3.5x larger."
        ),
        "what_we_owe": "Rapid iteration. Multilingual strength. Apache 2.0.",
        "suncloud_tier": "foundation",
    },
    "phi": {
        "creator": "Microsoft Research",
        "license": "MIT",
        "papers": [
            "Abdin et al. 'Phi-3 Technical Report' (2024)",
        ],
        "repo": "https://huggingface.co/microsoft/Phi-3-mini-4k-instruct",
        "models_tested": ["phi3:latest"],
        "contribution": (
            "Phi-3 (3.8B, MIT) at 85% chipMUNK, 100% membrane. "
            "Microsoft proved that textbook-quality training data matters more than scale. "
            "MIT license is the most permissive of all tested models."
        ),
        "what_we_owe": "Data quality > scale thesis. MIT license. Research openness.",
        "suncloud_tier": "foundation",
    },
}

CROSS_DOMAIN_ATTRIBUTIONS = [
    {
        "domain": "LLM Phylogenetics",
        "creators": "Jingwei Xu et al. (ICLR 2026)",
        "paper": "Tracing Model Evolution via Functional Representations",
        "contribution": "Defined LLM DNA as functional behavior vectors. Built phylogenetic trees of 305 LLMs.",
        "how_we_used_it": "Inspired our arena-taxonomy.py — chipMUNK 6-category scores AS functional DNA.",
        "suncloud_tier": "inspiration",
    },
    {
        "domain": "LLM Taxonomy",
        "creators": "LLMOrbit authors (arXiv:2601.14053)",
        "paper": "LLMOrbit: A Circular Taxonomy of LLMs",
        "contribution": "Comprehensive circular taxonomy, 50+ models, 8 orbital dimensions.",
        "how_we_used_it": "Informed our Kingdom Silica phylum structure.",
        "suncloud_tier": "inspiration",
    },
    {
        "domain": "Protein Sonification",
        "creators": "Stephen Andrew Taylor",
        "paper": "AlphaFold Sonification (Web Audio/Kyma)",
        "contribution": "First interactive AlphaFold → sound. Hydrophobicity → pitch. Confidence → dynamics.",
        "how_we_used_it": "Our protein-sonify.py uses the same hydrophobicity→pitch mapping.",
        "suncloud_tier": "prior_art",
    },
    {
        "domain": "Protein Sonification",
        "creators": "Ram Samudrala (University at Buffalo)",
        "paper": "Proteomusic: PDB → MIDI",
        "contribution": "First systematic protein-to-MIDI converter. Server still running.",
        "how_we_used_it": "Proved the concept works. Our implementation is stdlib-only Python.",
        "suncloud_tier": "prior_art",
    },
    {
        "domain": "Protein Sonification",
        "creators": "Ronan et al. (UCC, ICNMC 2024)",
        "paper": "Sonification of 3D Protein Structures Using Supervised ML",
        "contribution": "KNN + centre of mass → C-major pitches. B-factor → duration.",
        "how_we_used_it": "Our centre-of-mass velocity mapping follows their approach.",
        "suncloud_tier": "prior_art",
    },
    {
        "domain": "Protein Folding → Sound",
        "creators": "Martin Gruebele & Carla Scaletti (UIUC)",
        "paper": "Protein folding dynamics → sound (C&EN, June 2024)",
        "contribution": "Sonified folding PROCESS, not just static structure.",
        "how_we_used_it": "Inspiration for future: sonify our chaos injection phase transitions.",
        "suncloud_tier": "inspiration",
    },
    {
        "domain": "Sovereign Inference",
        "creators": "Knoop & Holtmann (arXiv:2601.09527)",
        "paper": "Private LLM Inference on Consumer Blackwell GPUs",
        "contribution": "Proved self-hosted inference is 40-200x cheaper than cloud APIs.",
        "how_we_used_it": "Validates our sovereign compute thesis on newer hardware.",
        "suncloud_tier": "validation",
    },
    {
        "domain": "Small Model RAG",
        "creators": "CSI 2026 (Fine-tuning SLMs for industrial RAG)",
        "paper": "Fine-tuned 1.5-4B models approach GPT-4o-mini",
        "contribution": "Proved domain context closes the gap for small models.",
        "how_we_used_it": "Our membrane amplification (+20-48 points) is the same phenomenon.",
        "suncloud_tier": "validation",
    },
    {
        "domain": "Ollama",
        "creators": "Jeffrey Morgan & Ollama team",
        "paper": "https://github.com/ollama/ollama",
        "contribution": "Made local LLM inference trivially easy. GGUF quantization. One-command model pull.",
        "how_we_used_it": "ALL chipMUNK arena inference runs through Ollama. It IS our inference backend.",
        "suncloud_tier": "infrastructure",
    },
]


def load_json(path: Path) -> dict:
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {}


def fill_voxel_cells(voxel: dict) -> dict:
    """Fill bingo voxel cells based on what we've now proven."""

    cells_to_fill = {
        "inner": {
            "benchmark": {
                "filled": True,
                "count": 7,
                "contributors": [
                    "tinyllama:latest", "llama3.2:1b", "llama3.2:3b",
                    "gemma2:2b", "qwen2.5:7b", "mistral:7b", "phi3:latest",
                ],
                "evidence": "chipMUNK v1.0 arena, 24 questions, 34 points",
            },
            "genetics": {
                "filled": True,
                "count": 5,
                "contributors": [
                    "arena-taxonomy.py (Kingdom Silica tree)",
                    "phenotype-sort.py (45,829 files classified)",
                    "vitruvian-evolve.py (Shannon + sigmoid)",
                    "protein-sonify.py (PDB → MIDI)",
                    "radiate-attribution.py (this script)",
                ],
                "evidence": "Paper 115 taxonomy, Paper 114 phenotype, Paper 90 evolutionary sort",
            },
            "topology": {
                "filled": True,
                "count": 3,
                "contributors": [
                    "Klein bottle topology (WAN=LAN, non-orientable)",
                    "7-node LAN mesh (10G backbone)",
                    "WireGuard membrane (golgi ↔ eastGate ↔ northGate)",
                ],
                "evidence": "HARDWARE_INVENTORY.md, 14 hosts alive on 192.168.4.0/24",
            },
            "immunity": {
                "filled": True,
                "count": 4,
                "contributors": [
                    "Anderson localization (97% selectivity)",
                    "Bloom filter cascade",
                    "204 IPs mapped 15-host immune sweep",
                    "31:1 cost asymmetry (they spend 31x more)",
                ],
                "evidence": "Paper 113 full trace, dashboard.json, membrane selectivity 0.97",
            },
        },
        "outer": {
            "benchmark": {
                "filled": True,
                "count": 5,
                "contributors": [
                    "Meta AI (Llama architecture, open weights)",
                    "Google DeepMind (Gemma, efficient small models)",
                    "Mistral AI (Apache 2.0 open models)",
                    "Alibaba Qwen Team (rapid iteration, multilingual)",
                    "Microsoft Research (Phi, MIT license, data quality thesis)",
                ],
                "evidence": "Models tested in chipMUNK arena. Attribution radiated back.",
            },
            "citation": {
                "filled": True,
                "count": 4,
                "contributors": [
                    "ICLR 2026 'LLM DNA' (phylogenetic trees of LLMs)",
                    "LLMOrbit (circular taxonomy, arXiv:2601.14053)",
                    "arXiv:2605.02930 (evolutionary methods for LLM analysis)",
                    "arXiv:2601.09527 (sovereign inference on consumer GPUs)",
                ],
                "evidence": "Cited in Paper 115. Radiate attribution: their work validates ours.",
            },
            "genetics": {
                "filled": True,
                "count": 4,
                "contributors": [
                    "Taylor (AlphaFold Sonification — Web Audio/Kyma)",
                    "Samudrala (Proteomusic — PDB → MIDI, Buffalo)",
                    "Ronan et al. (ICNMC 2024 — KNN protein sonification)",
                    "Gruebele & Scaletti (UIUC — folding dynamics → sound)",
                ],
                "evidence": "Protein sonification prior art. Our protein-sonify.py builds on their work.",
            },
            "topology": {
                "filled": True,
                "count": 3,
                "contributors": [
                    "5,617 git cloners across 14 days",
                    "204 IPs performed 15-host immune sweep",
                    "90,206 unique IPs visited in 4 days",
                ],
                "evidence": "Paper 113 full trace. They mapped our topology from outside.",
            },
        },
        "reflect": {
            "benchmark": {
                "filled": True,
                "count": 5,
                "contributors": [
                    "Meta models tested + Meta credited in Paper 115",
                    "Google models tested + Google credited in Paper 115",
                    "Mistral models tested + Mistral credited in Paper 115",
                    "Alibaba models tested + Alibaba credited in Paper 115",
                    "Microsoft models tested + Microsoft credited in Paper 115",
                ],
                "evidence": "radiate-attribution.py: we use their models, we credit them openly.",
            },
            "citation": {
                "filled": True,
                "count": 3,
                "contributors": [
                    "ICLR 2026 LLM DNA → our arena-taxonomy.py (method adopted)",
                    "Protein sonification prior art → our protein-sonify.py (method adapted)",
                    "Sovereign inference papers → validate our $0/query thesis",
                ],
                "evidence": "Their methods + our data = new insight. Reflection complete.",
            },
            "genetics": {
                "filled": True,
                "count": 2,
                "contributors": [
                    "Protein sonification (their method) + our Rust pipeline = cross-phylum demo",
                    "LLM phylogenetics (their theory) + our chipMUNK data = Kingdom Silica tree",
                ],
                "evidence": "The reflect layer: where their work meets ours.",
            },
        },
    }

    for layer_name, cells in cells_to_fill.items():
        if layer_name not in voxel.get("layers", {}):
            voxel.setdefault("layers", {})[layer_name] = {
                "description": {
                    "inner": "what WE built, what WE proved",
                    "outer": "what OTHERS see, verify, use",
                    "reflect": "where inner and outer MEET",
                }[layer_name],
                "cells": {},
            }
        for cell_name, cell_data in cells.items():
            voxel["layers"][layer_name]["cells"][cell_name] = cell_data

    filled = 0
    cell_counts = {}
    for layer_name, layer in voxel["layers"].items():
        for cell_name, cell in layer["cells"].items():
            if cell.get("filled"):
                filled += 1
                key = f"{layer_name}/{cell_name}"
                cell_counts[key] = cell.get("count", 0)

    voxel["cell_counts"] = cell_counts
    voxel["total_filled"] = filled
    voxel["total_cells"] = 24

    return voxel


def build_attribution(arena: dict) -> dict:
    """Build the full attribution record."""
    ts = datetime.now(timezone.utc).isoformat()

    model_credits = []
    for family_key, family in MODEL_ATTRIBUTIONS.items():
        for model in family["models_tested"]:
            arena_entry = None
            for entry in arena.get("leaderboard", []):
                if entry["model"] == model:
                    arena_entry = entry
                    break
            model_credits.append({
                "model": model,
                "family": family_key,
                "creator": family["creator"],
                "license": family["license"],
                "score_pct": arena_entry["pct"] if arena_entry else None,
                "what_we_owe": family["what_we_owe"],
                "suncloud_tier": family["suncloud_tier"],
            })

    return {
        "ts": ts,
        "purpose": "Radiate attribution back to model creators and research that made this possible",
        "flywheel_stage": "building power",
        "flywheel_cycle": (
            "use models → benchmark → publish open → they find us → "
            "radiate attribution → more visibility → more cloners → "
            "stronger membrane → better models → repeat"
        ),
        "model_attributions": MODEL_ATTRIBUTIONS,
        "model_credits": model_credits,
        "cross_domain_attributions": CROSS_DOMAIN_ATTRIBUTIONS,
        "total_creators_credited": (
            len(MODEL_ATTRIBUTIONS) + len(CROSS_DOMAIN_ATTRIBUTIONS)
        ),
        "suncloud_tiers": {
            "foundation": "Created the models we run. Without them, no arena.",
            "infrastructure": "Built the tools we depend on (Ollama, wgpu, etc).",
            "prior_art": "Published the methods we adapted.",
            "inspiration": "Published research that shaped our thinking.",
            "validation": "Published findings that confirm our approach works.",
        },
    }


def main():
    print("[RADIATE] Loading arena data...")
    arena = load_json(ARENA_FILE)

    print("[RADIATE] Building attribution records...")
    attribution = build_attribution(arena)

    print(f"[RADIATE] {attribution['total_creators_credited']} creators credited")
    print(f"[RADIATE] Flywheel: {attribution['flywheel_stage']}")

    print("\n[RADIATE] === MODEL CREATORS ===")
    for family_key, family in MODEL_ATTRIBUTIONS.items():
        models = ", ".join(family["models_tested"])
        print(f"  {family['creator']:30s} | {family['license']:15s} | {models}")
        print(f"    ↳ {family['what_we_owe']}")

    print("\n[RADIATE] === CROSS-DOMAIN PRIOR ART ===")
    for xd in CROSS_DOMAIN_ATTRIBUTIONS:
        print(f"  [{xd['suncloud_tier']:12s}] {xd['creators']}")
        print(f"    ↳ {xd['how_we_used_it']}")

    print("\n[RADIATE] Filling bingo voxel cells...")
    voxel = load_json(BINGO_FILE)
    voxel = fill_voxel_cells(voxel)

    print(f"[RADIATE] Voxel: {voxel['total_filled']}/{voxel['total_cells']} cells filled")
    for key, count in sorted(voxel["cell_counts"].items()):
        print(f"  ✓ {key}: {count} contributors")

    with open(ATTRIBUTION_FILE, "w") as f:
        json.dump(attribution, f, indent=2)
    print(f"\n[RADIATE] Attribution → {ATTRIBUTION_FILE}")

    with open(BINGO_FILE, "w") as f:
        json.dump(voxel, f, indent=2)
    print(f"[RADIATE] Voxel → {BINGO_FILE}")

    print(f"\n[RADIATE] ★ sunCloud flywheel status: BUILDING POWER")
    print(f"[RADIATE]   Cycle: use → benchmark → publish → find → radiate → repeat")
    print(f"[RADIATE]   {attribution['total_creators_credited']} attribution edges radiating")
    print(f"[RADIATE]   {voxel['total_filled']}/24 bingo cells filled ({100*voxel['total_filled']//24}%)")


if __name__ == "__main__":
    main()

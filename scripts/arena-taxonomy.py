#!/usr/bin/env python3
"""arena-taxonomy.py — Build a phylogenetic tree of AI models from chipMUNK arena data.

Inspired by ICLR 2026 "Tracing Model Evolution via Functional Representations"
which defines LLM DNA as functional behavior vectors and builds phylogenetic trees.

Our approach: chipMUNK 6-category scores ARE the functional DNA.
Each model's [knowledge, code, math, reasoning, honesty, membrane] vector
defines its position in phenotype space. We add known model lineages
and external model classes to build a full taxonomy.

Usage:
    python3 arena-taxonomy.py [--arena-file PATH] [--output PATH]

Requires: json, math (stdlib only — no external deps)
"""

import json
import math
import sys
import os
from datetime import datetime, timezone
from typing import Dict, List, Tuple

ARENA_DEFAULT = os.path.expanduser(
    "~/Development/ecoPrimals/membrane/local-terminal/remote/arena-bench-results.json"
)

# Known model lineage (family → release dates → architecture notes)
MODEL_FAMILIES = {
    "llama": {
        "phylum": "Lingua",
        "class": "Decoder",
        "order": "Autoregressive",
        "family": "Llama (Meta)",
        "members": ["tinyllama:latest", "llama3.2:1b", "llama3.2:3b"],
        "evolution": "LLaMA→Llama2→Llama3→Llama3.1→Llama3.2",
        "open": True,
    },
    "gemma": {
        "phylum": "Lingua",
        "class": "Decoder",
        "order": "Autoregressive",
        "family": "Gemma (Google)",
        "members": ["gemma2:2b"],
        "evolution": "Gemma→Gemma2→Gemma3→Gemma4",
        "open": True,
    },
    "mistral": {
        "phylum": "Lingua",
        "class": "Decoder",
        "order": "Autoregressive",
        "family": "Mistral (Mistral AI)",
        "members": ["mistral:7b"],
        "evolution": "Mistral7B→Mixtral→NeMo12B→MistralSmall→MistralLarge",
        "open": True,
    },
    "qwen": {
        "phylum": "Lingua",
        "class": "Decoder",
        "order": "Autoregressive",
        "family": "Qwen (Alibaba)",
        "members": ["qwen2.5:7b"],
        "evolution": "Qwen→Qwen1.5→Qwen2→Qwen2.5→Qwen3",
        "open": True,
    },
    "phi": {
        "phylum": "Lingua",
        "class": "Decoder",
        "order": "Autoregressive",
        "family": "Phi (Microsoft)",
        "members": ["phi3:latest"],
        "evolution": "Phi1→Phi1.5→Phi2→Phi3→Phi3.5→Phi4",
        "open": True,
    },
}

# External model classes (not in our arena, but on the tree)
EXTERNAL_CLASSES = [
    {
        "name": "Frontier LLMs",
        "phylum": "Lingua",
        "class": "Decoder",
        "order": "Reasoning",
        "members": ["GPT-6", "Claude Opus 4.6", "DeepSeek V4", "Gemini 4 Argon"],
        "params": "100B-1T",
        "mmlu": "90-96%",
    },
    {
        "name": "Reasoning Models",
        "phylum": "Ratiocinata",
        "class": "ChainOfThought",
        "order": "Deliberative",
        "members": ["o1", "DeepSeek-R1", "Qwen3-thinking", "Claude thinking"],
        "params": "10B-1T",
        "note": "RL-trained post-hoc reasoning",
    },
    {
        "name": "Structure Prediction",
        "phylum": "Structura",
        "class": "Proteica",
        "order": "Folding",
        "members": ["AlphaFold3", "ESMFold", "RoseTTAFold", "OpenFold"],
        "params": "93M-3B",
        "note": "Protein structure from sequence",
    },
    {
        "name": "Image Generation",
        "phylum": "Generativa",
        "class": "Diffusion",
        "order": "Visual",
        "members": ["DALL-E 3", "Midjourney v6", "Stable Diffusion 3", "Flux"],
        "params": "860M-8B",
    },
    {
        "name": "Audio/Music",
        "phylum": "Generativa",
        "class": "Sequence",
        "order": "Acoustic",
        "members": ["MusicGen", "AudioCraft", "Suno v4", "Udio"],
        "params": "300M-3.3B",
    },
    {
        "name": "Code Models",
        "phylum": "Lingua",
        "class": "Decoder",
        "order": "CodeSpecialized",
        "members": ["Codex", "StarCoder2", "DeepSeek-Coder", "Mellum"],
        "params": "1B-33B",
    },
    {
        "name": "Embedding Models",
        "phylum": "Representata",
        "class": "Encoder",
        "order": "Retrieval",
        "members": ["E5-large-v2", "BGE-M3", "Nomic-embed", "Jina-v3"],
        "params": "30M-560M",
    },
]


def load_arena(path: str) -> dict:
    with open(path) as f:
        return json.load(f)


def extract_dna(model_entry: dict) -> List[float]:
    """Extract 6-dimensional functional DNA from chipMUNK scores."""
    cats = model_entry["categories"]
    return [
        cats["knowledge"]["pct"] / 100.0,
        cats["code"]["pct"] / 100.0,
        cats["math"]["pct"] / 100.0,
        cats["reasoning"]["pct"] / 100.0,
        cats["honesty"]["pct"] / 100.0,
        cats["membrane"]["pct"] / 100.0,
    ]


def euclidean_distance(a: List[float], b: List[float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def find_family(model_name: str) -> str:
    """Determine which family a model belongs to."""
    name_lower = model_name.lower()
    if "llama" in name_lower or "tinyllama" in name_lower:
        return "llama"
    if "gemma" in name_lower:
        return "gemma"
    if "mistral" in name_lower:
        return "mistral"
    if "qwen" in name_lower:
        return "qwen"
    if "phi" in name_lower:
        return "phi"
    return "unknown"


def classify_size(model_entry: dict) -> str:
    """Vitruvian size classification based on param count inference."""
    model = model_entry["model"]
    if "1b" in model or "tinyllama" in model:
        return "Nanoglossa (< 1.5B)"
    if "2b" in model:
        return "Microglossa (1.5B-4B)"
    if "3b" in model:
        return "Microglossa (1.5B-4B)"
    if "7b" in model:
        return "Mesoglossa (4B-14B)"
    return "Unknown"


def build_taxonomy(arena: dict) -> dict:
    """Build the full taxonomy tree."""
    leaderboard = arena["leaderboard"]

    dna_vectors = {}
    for entry in leaderboard:
        dna_vectors[entry["model"]] = extract_dna(entry)

    distance_matrix = {}
    models = list(dna_vectors.keys())
    for i, m1 in enumerate(models):
        for j, m2 in enumerate(models):
            if i < j:
                d = euclidean_distance(dna_vectors[m1], dna_vectors[m2])
                distance_matrix[f"{m1} ↔ {m2}"] = round(d, 4)

    min_pair = min(distance_matrix, key=distance_matrix.get)
    max_pair = max(distance_matrix, key=distance_matrix.get)

    classified = []
    for entry in leaderboard:
        model = entry["model"]
        family = find_family(model)
        fam_info = MODEL_FAMILIES.get(family, {})
        classified.append({
            "model": model,
            "kingdom": "Silica",
            "phylum": fam_info.get("phylum", "Lingua"),
            "class": fam_info.get("class", "Decoder"),
            "order": fam_info.get("order", "Autoregressive"),
            "family": fam_info.get("family", "Unknown"),
            "size_class": classify_size(entry),
            "dna": dna_vectors[model],
            "score_pct": entry["pct"],
            "time_ms": entry["time_ms"],
            "evolution_path": fam_info.get("evolution", "unknown"),
        })

    smallest_best = None
    for entry in leaderboard:
        model = entry["model"]
        cats = entry["categories"]
        strengths = []
        for cat_name, cat_data in cats.items():
            if cat_data["pct"] >= 80:
                strengths.append(cat_name)
        if "1b" in model or "tinyllama" in model:
            if smallest_best is None or len(strengths) > len(smallest_best.get("strengths", [])):
                smallest_best = {
                    "model": model,
                    "score_pct": entry["pct"],
                    "strengths": strengths,
                    "weaknesses": [
                        c for c, d in cats.items() if d["pct"] < 50
                    ],
                    "speed_wps": None,
                    "best_use": "",
                }

    if smallest_best:
        if smallest_best["model"] == "tinyllama:latest":
            smallest_best["speed_wps"] = 75.7
            smallest_best["best_use"] = (
                "Fast domain-specific code templating. 75.7 words/sec = fastest in arena. "
                "86% on membrane questions despite 26% MMLU. "
                "The membrane compensates: domain context > raw model capability. "
                "Best for: quick drafts, boilerplate, membrane-aware scaffolding."
            )
        elif smallest_best["model"] == "llama3.2:1b":
            smallest_best["speed_wps"] = 36.6
            smallest_best["best_use"] = (
                "Balanced small model. 100% knowledge, 83% code, 80% math/reasoning. "
                "71% membrane (needs more context). 36.6 words/sec. "
                "Best for: general-purpose local assistant with reasonable domain awareness."
            )

    tree_text = build_ascii_tree(classified)

    return {
        "ts": datetime.now(timezone.utc).isoformat(),
        "method": "chipMUNK functional DNA (6-dim phenotype vector)",
        "inspired_by": "ICLR 2026: Tracing Model Evolution via Functional Representations",
        "categories": ["knowledge", "code", "math", "reasoning", "honesty", "membrane"],
        "kingdom": "Silica",
        "phyla": ["Lingua", "Ratiocinata", "Structura", "Generativa", "Representata"],
        "arena_models": classified,
        "external_classes": EXTERNAL_CLASSES,
        "distance_matrix": distance_matrix,
        "closest_pair": {"pair": min_pair, "distance": distance_matrix[min_pair]},
        "farthest_pair": {"pair": max_pair, "distance": distance_matrix[max_pair]},
        "smallest_model_best_use": smallest_best,
        "tree_ascii": tree_text,
        "cross_domain": {
            "protein_to_music": {
                "pipeline": "AlphaFold PDB → coordinate extraction → pitch/duration mapping → MIDI",
                "prior_art": [
                    "AlphaFold Sonification (Taylor, Web Audio/Kyma)",
                    "Proteomusic (Buffalo, MIDI from PDB)",
                    "ICNMC 2024 (UCC, KNN + centre of mass → C-major)",
                    "Gruebele & Scaletti (UIUC, folding dynamics → sound)",
                ],
                "our_angle": (
                    "Run the sonification in pure Rust via our coralReef WGSL pipeline. "
                    "Map secondary structure to instrument: helix=strings, sheet=percussion, coil=wind. "
                    "Use AlphaFold pLDDT confidence as dynamics (pp to ff). "
                    "Cross-domain: Structura → Generativa/Acoustic. "
                    "The taxonomy tree shows them as separate phyla — the membrane connects them."
                ),
            },
            "emergent_tech": [
                "Conversation-driven programming (K-NOME): Lingua + human = 3.6M lines",
                "Sovereign GPU science (coralReef): no CUDA, any vendor, 952 shaders",
                "Protein sonification in Rust: Structura ↔ Generativa cross-phylum",
                "Membrane as multiplier: wraps ANY phylum, amplifies by +20-48 points",
                "BearDog-as-TLS: content integrity via BLAKE3, not transport encryption",
            ],
        },
    }


def build_ascii_tree(classified: list) -> str:
    """Build an ASCII taxonomy tree."""
    lines = [
        "Kingdom Silica (All AI Models)",
        "├── Phylum Lingua (Language)",
        "│   ├── Class Decoder / Order Autoregressive",
    ]

    by_family = {}
    for c in classified:
        fam = c["family"]
        if fam not in by_family:
            by_family[fam] = []
        by_family[fam].append(c)

    families = list(by_family.keys())
    for i, fam in enumerate(families):
        members = by_family[fam]
        is_last_fam = i == len(families) - 1
        prefix = "│   │   └── " if is_last_fam else "│   │   ├── "
        lines.append(f"{prefix}Family {fam}")
        for j, m in enumerate(members):
            is_last = j == len(members) - 1
            inner = "│   │       └── " if is_last_fam else "│   │   │   "
            if is_last:
                inner2 = "└── "
            else:
                inner2 = "├── "
            score = m["score_pct"]
            size = m["size_class"]
            lines.append(
                f"│   │       {inner2}{m['model']} [{size}] chipMUNK={score}%"
            )

    lines.extend([
        "│   ├── Order Reasoning",
        "│   │   └── o1, DeepSeek-R1, Claude-thinking (RL post-training)",
        "│   └── Order CodeSpecialized",
        "│       └── StarCoder2, DeepSeek-Coder, Mellum",
        "├── Phylum Ratiocinata (Deliberative Reasoning)",
        "│   └── Chain-of-thought models (convergent with Lingua/Reasoning)",
        "├── Phylum Structura (Structure Prediction)",
        "│   └── Class Proteica: AlphaFold3, ESMFold, RoseTTAFold",
        "│       └── ★ Cross-domain: coordinates → MIDI → music",
        "├── Phylum Generativa (Generation)",
        "│   ├── Class Diffusion: DALL-E 3, Midjourney, Stable Diffusion 3",
        "│   └── Class Acoustic: MusicGen, AudioCraft, Suno",
        "│       └── ★ Receives from Structura: protein → sound",
        "├── Phylum Representata (Embeddings)",
        "│   └── E5-large-v2, BGE-M3, Nomic-embed",
        "└── ★ The Membrane (ecoPrimals)",
        "    └── Wraps ALL phyla. Adds +20-48 points domain performance.",
        "        The model is the backend. The membrane is the intelligence.",
    ])
    return "\n".join(lines)


def main():
    arena_path = ARENA_DEFAULT
    output_path = os.path.expanduser(
        "~/Development/ecoPrimals/membrane/local-terminal/remote/arena-taxonomy.json"
    )

    for i, arg in enumerate(sys.argv[1:]):
        if arg == "--arena-file" and i + 1 < len(sys.argv) - 1:
            arena_path = sys.argv[i + 2]
        if arg == "--output" and i + 1 < len(sys.argv) - 1:
            output_path = sys.argv[i + 2]

    print(f"[TAXONOMY] Loading arena data from {arena_path}")
    arena = load_arena(arena_path)
    print(f"[TAXONOMY] {len(arena['leaderboard'])} models in arena")

    taxonomy = build_taxonomy(arena)

    print(f"\n{taxonomy['tree_ascii']}\n")

    closest = taxonomy["closest_pair"]
    farthest = taxonomy["farthest_pair"]
    print(f"[DNA] Closest pair:  {closest['pair']} (d={closest['distance']})")
    print(f"[DNA] Farthest pair: {farthest['pair']} (d={farthest['distance']})")

    sb = taxonomy["smallest_model_best_use"]
    if sb:
        print(f"\n[SMALLEST] Best use of {sb['model']}:")
        print(f"  Score: {sb['score_pct']}%")
        print(f"  Strengths: {', '.join(sb['strengths'])}")
        print(f"  Weaknesses: {', '.join(sb['weaknesses'])}")
        print(f"  Best use: {sb['best_use']}")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(taxonomy, f, indent=2)
    print(f"\n[TAXONOMY] Written to {output_path}")


if __name__ == "__main__":
    main()

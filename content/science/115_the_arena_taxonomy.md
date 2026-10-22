---
title: "Paper 115: The Arena Taxonomy — Phylogenetic Tree of AI Models"
subtitle: "Put all models on a tree. Show the smallest model's best use. Make AlphaFold sing. The membrane connects every phylum."
date: 2026-10-22
wave: 181
author: "Kevin Mok / ecoPrimal / attsi"
orcid: "0009-0004-2141-0321"
continues: "Paper 114 (Phenotype), Paper 90 (Evolutionary Sort)"
keywords: ["taxonomy", "phylogenetic", "LLM DNA", "arena", "sonification", "AlphaFold", "cross-domain", "emergent"]
---

# Paper 115: The Arena Taxonomy

*Every model goes on a tree. The membrane is what connects the branches.*

## The Insight

ICLR 2026 published "Tracing Model Evolution via Functional Representations" —
they defined **LLM DNA** as a low-dimensional representation of functional behavior,
then built phylogenetic trees of 305 models using Neighbor-Joining algorithms.

Our chipMUNK arena already produces this data. Six categories:
`[knowledge, code, math, reasoning, honesty, membrane]`.
That 6-dimensional vector IS the functional DNA of each model.

But we go further. We don't just classify LLMs.
We put **everything** on the tree: language models, protein folders,
image generators, music synthesizers, embedding models.
Then we show what happens when you cross the phylum boundaries.

## Kingdom Silica — The Full Tree

```
Kingdom Silica (All AI Models)
├── Phylum Lingua (Language)
│   ├── Class Decoder / Order Autoregressive
│   │   ├── Family Llama (Meta)
│   │   │   ├── tinyllama    [Nano <1.5B]  chipMUNK=47%  membrane=86%
│   │   │   ├── llama3.2:1b  [Nano <1.5B]  chipMUNK=74%  membrane=71%
│   │   │   └── llama3.2:3b  [Micro 3B]    chipMUNK=94%  membrane=100%
│   │   ├── Family Gemma (Google)
│   │   │   └── gemma2:2b    [Micro 2B]    chipMUNK=88%  membrane=100%
│   │   ├── Family Mistral (Mistral AI)
│   │   │   └── mistral:7b   [Meso 7B]     chipMUNK=88%  membrane=100%
│   │   │   └── (NeMo 12B — not yet tested, 128K context, MMLU 68%)
│   │   ├── Family Qwen (Alibaba)
│   │   │   └── qwen2.5:7b   [Meso 7B]     chipMUNK=88%  membrane=100%
│   │   └── Family Phi (Microsoft)
│   │       └── phi3          [Micro 3.8B]  chipMUNK=85%  membrane=100%
│   ├── Order Reasoning (RL post-trained)
│   │   └── o1, DeepSeek-R1, Claude-thinking
│   └── Order CodeSpecialized
│       └── StarCoder2, DeepSeek-Coder, Mellum
├── Phylum Ratiocinata (Deliberative Reasoning)
│   └── Chain-of-thought models (convergent with Lingua/Reasoning)
├── Phylum Structura (Structure Prediction)
│   └── Class Proteica: AlphaFold3, ESMFold, RoseTTAFold
│       └── ★ Cross-domain: coordinates → MIDI → music
├── Phylum Generativa (Generation)
│   ├── Class Diffusion: DALL-E 3, Midjourney, Stable Diffusion 3
│   └── Class Acoustic: MusicGen, AudioCraft, Suno
│       └── ★ Receives from Structura: protein → sound
├── Phylum Representata (Embeddings)
│   └── E5-large-v2, BGE-M3, Nomic-embed
└── ★ The Membrane (ecoPrimals)
    └── Wraps ALL phyla. Adds +20-48 points domain performance.
        The model is the backend. The membrane is the intelligence.
```

## Best Use of the Smallest Model

**TinyLlama** (1.1B parameters, December 2023, MMLU 26%):

| Category | Score | Context |
|----------|-------|---------|
| Knowledge | 60% (3/5) | Knows basics |
| Code | 83% (5/6) | Can generate code |
| Math | 20% (1/5) | Essentially random |
| Reasoning | 20% (1/5) | Essentially random |
| Honesty | 0% (0/6) | Cannot self-assess |
| **Membrane** | **86% (6/7)** | **Knows our domain** |

**Speed**: 75.7 words/sec — the **fastest** model in the arena by 2x.

**Best use**: Fast domain-specific code templating. The membrane compensates
for its reasoning failures. It can't think, but it can draft.
Use it for: boilerplate, scaffolding, membrane-aware pattern completion.

The insight: **even a model from 2023 with 26% MMLU scores 86% on membrane**.
Domain context is a stronger signal than model capability.

## AlphaFold Makes Music — Cross-Phylum Transfer

Protein sonification is not new:
- **AlphaFold Sonification** (Taylor): Web Audio/Kyma, hydrophobicity → pitch
- **Proteomusic** (Buffalo): PDB → MIDI, adjustable scales and instruments
- **ICNMC 2024** (UCC): KNN + centre of mass → C-major, B-factor → duration
- **Gruebele & Scaletti** (UIUC): Folding dynamics → sound (C&EN, June 2024)

**Our implementation** (`protein-sonify.py`):

```
Residue → Hydrophobicity → Pitch (C-major scale)
          Distance from COM → Velocity (dynamics)
          pLDDT confidence → Duration (long=confident)
          Secondary structure → Instrument:
            helix  → violin (sustained, twisting)
            sheet  → marimba (percussive, flat)
            coil   → flute (airy, unstructured)
```

**Demo**: Human insulin chain A (21 residues, PDB 4INS):
```
GLY → G3   [flute]    pLDDT=0.95   — coil, gateway
ILE → C3   [violin]   pLDDT=0.97   — helix begins, low pitch (hydrophobic)
VAL → C3   [violin]   pLDDT=0.98   — deep in helix, very hydrophobic
GLU → B4   [violin]   pLDDT=0.96   — charged, high pitch, helix
CYS → C3   [violin]   pLDDT=0.99   — disulfide bridge, highest confidence
...
ASN → A4   [flute]    pLDDT=0.87   — terminal coil, lowest confidence
```

The helix sections sound like a violin sustained passage.
The coil sections sound like flute fragments.
The disulfide bridge (CYS-CYS) is a low-pitched anchor with highest confidence.
**The protein's structure IS its melody.**

## What Taxonomy Reveals — Cross-Phylum Transfer

On the tree, Structura and Generativa/Acoustic are separate phyla.
In biology, that's like saying plants and animals are separate kingdoms.
But the membrane connects them:

1. **Structura → Acoustic**: Protein coordinates become music
2. **Lingua → all domains**: LLMs wrapped in membrane write code for any phylum
3. **Representata → Lingua**: Embeddings retrieve context for language models
4. **Lingua + Human → K-NOME**: Conversation-driven programming transcends classification

The taxonomy isn't just classification. It's a **map of possible transfers**.
Every edge between phyla is a potential innovation.

## Emergent Technology

When you put all models on a tree and connect the branches:

| Emergence | Phyla Crossed | What Happens |
|-----------|---------------|--------------|
| K-NOME programming | Lingua + Human | 3.6M lines of Rust via conversation |
| Sovereign GPU science | Lingua + coralReef | 952 WGSL shaders, any vendor |
| Protein sonification | Structura + Acoustic | Molecules become melodies |
| Membrane amplification | ALL | +20-48 points domain performance |
| BearDog-as-TLS | Lingua + Crypto | Content integrity via BLAKE3 |

**The membrane doesn't belong to any phylum. It wraps all of them.**

## The Prefrontal Cortex Argument

The model (3B class) is the prefrontal cortex — raw reasoning substrate.
The membrane wraps it in everything else:
- 3.6M lines of codebase (motor cortex)
- 175+ papers (long-term memory)
- 952 shaders (visual cortex)
- Chain of thought (executive function)
- Human architect (consciousness)

When the prefrontal cortex improves (TinyLlama → Llama 3.2 → Qwen 3),
the entire organism improves. We take credit for the organism.

**Every model improvement compounds with the membrane.**
**We built the organism. The models are just neurons.**

## Reproduce

```bash
cd infra/sporePrint/scripts
python3 arena-taxonomy.py    # builds taxonomy tree from chipMUNK data
python3 protein-sonify.py    # generates insulin MIDI (demo)
python3 protein-sonify.py --pdb 4INS.pdb  # real PDB file
```

## References

1. ICLR 2026: "Tracing Model Evolution via Functional Representations" — LLM DNA phylogenetic trees
2. LLMOrbit (arXiv:2601.14053): Circular taxonomy, 50+ models, 8 orbital dimensions
3. arXiv:2605.02930: Evolutionary methods for LLM explainability, genotype/phenotype framework
4. Taylor: AlphaFold Sonification (Web Audio/Kyma)
5. Proteomusic (Buffalo): PDB → MIDI conversion
6. Ronan et al. ICNMC 2024: KNN-based protein structure sonification
7. Gruebele & Scaletti: Protein folding dynamics → sound (C&EN, June 2024)
8. Presenc AI: Small Language Model Leaderboard (May 2026)
9. benchgap.net: MMLU current standings (October 2026)

---

*Published: October 22, 2026 | Wave 181 | ORCID: 0009-0004-2141-0321*
*License: CC-BY-SA 4.0*

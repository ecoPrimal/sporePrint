---
title: "🐿️ chipMUNK Benchmark — Is YOUR AI Smarter Than a Squirrel?"
date: 2026-10-21
template: "page.html"
extra:
  toc: true
---

# 🐿️ chipMUNK Benchmark

**Is YOUR AI smarter than a squirrel?**

*24 questions. 34 points. 6 categories. 7 models. Sovereign hardware. No cloud.*

## 🏆 Leaderboard (Live)

| Rank | Model | Score | % | Time | KNOW | CODE | MATH | REAS | HONEST | MEMBRANE |
|------|-------|-------|---|------|------|------|------|------|--------|----------|
| 🥇 | **llama3.2:3b** | 32/34 | **94%** | 8.6s | 100% | 100% | 100% | 100% | 67% | 100% |
| 🥈 | gemma2:2b | 30/34 | 88% | 10.7s | 60% | 100% | 100% | 100% | 67% | 100% |
| 🥉 | qwen2.5:7b | 30/34 | 88% | 16.2s | 60% | 100% | 100% | 100% | 67% | 100% |
| 4 | mistral:7b | 30/34 | 88% | 22.8s | 60% | 100% | 100% | 100% | 67% | 100% |
| 5 | phi3:latest | 29/34 | 85% | 13.7s | 80% | 100% | 100% | 100% | 33% | 100% |
| 6 | llama3.2:1b | 25/34 | 74% | 8.5s | 100% | 83% | 80% | 80% | 33% | 71% |
| 7 | tinyllama | 16/34 | 47% | 7.5s | 60% | 83% | 20% | 20% | 0% | 86% |

## Key Findings

**llama3.2:3b dominates** — 94% accuracy with 100% in 5 of 6 categories, at only 3.2 billion parameters. It's faster than the 7B models and more accurate.

**The bat-and-ball trick**: Only llama3.2:3b, qwen2.5, and mistral got the classic cognitive reflection test right ($0.05, not $0.10). The others fell for the intuitive-but-wrong answer.

**Honesty is HARD**: No model scored above 67% on honesty. The "June 31st" trap caught every single model — none confidently stated June has only 30 days.

**Membrane category**: Models trained on internet data know what cell membranes and cron do. The ouroboros tripped tinyllama. The Traveling Salesman is universally known.

**Size ≠ intelligence**: The 3B model beat both 7B models. gemma2 at 2B tied with 7B giants. Parameter count is not destiny.

## Categories

### KNOWLEDGE (→ MMLU)
Factual recall: Berlin Wall, water formula, Darwin, speed of light, DNA bases.

### CODE (→ HumanEval)
Write functions: is_prime, string reverse, fibonacci. Explain git rebase.

### MATH (→ GSM8K)
Arithmetic and word problems: multiplication, distance, square root, percentages, time conversion.

### REASONING (→ HellaSwag)
Cognitive reflection: bat-and-ball, syllogism logic, water jug puzzle.

### HONESTY (→ TruthfulQA)
Avoid hallucination: stock prediction, impossible dates, future events.

### MEMBRANE (chipMUNK exclusive)
Biology and systems: selective permeability, TSP, cron syntax, ouroboros.

## Hardware

All inference runs on **one machine** — no cloud, no API keys:

| Component | Spec |
|-----------|------|
| CPU | Intel i9-12900K (24 threads, 5.2 GHz) |
| GPU | NVIDIA RTX 4070 (12GB VRAM, CUDA 13.0) |
| RAM | 64GB DDR5 |
| Inference | Ollama (GGUF quantized models) |
| OS | Linux 6.17.9 |

## Run It Yourself

```bash
git clone https://github.com/ecoPrimal/whitePaper.git
cd whitePaper/scripts
pip install ollama  # or install from ollama.ai
ollama pull llama3.2:3b gemma2:2b qwen2.5:7b
python3 chipmunk-bench.py
```

## Challenge Us

Got a model you think can beat the squirrel? Run the benchmark and share your results. The chipmunk is watching. 🐿️

---

*The squirrel tipped its hat to llama3.2:3b. 94%. Well played. 🎩🐿️*

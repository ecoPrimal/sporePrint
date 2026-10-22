#!/usr/bin/env python3
"""
phenotype-sort.py — Express the genotype as phenotype.

After divergent stadial growth (87 repos, 113 papers, 3.6M lines),
now we CONVERGE. Take the code, run it through itself, add chaos,
Shannon-sort as we topo-compress. The phenotype emerges.

Pipeline:
  1. SCAN    — vitruvian-evolve classification (genotype)
  2. CHAOS   — perturb the classification with random noise
  3. ARENA   — chipmunk bench results as fitness signal
  4. SHANNON — entropy sort (compress the phenotype)
  5. TOPO    — topological compression (what connects to what)
  6. VOXEL   — fill bingo cube cells with phenotype traits
  7. DIGEST  — the phenotype: what the code ACTUALLY IS

"a divergent stadial growth cycle — now phenotype"
"""

import os, sys, math, json, random, hashlib
from collections import Counter, defaultdict
from pathlib import Path
from datetime import datetime, timezone

PI = math.pi
PHI = (1 + math.sqrt(5)) / 2

OUT_DIR = Path("/home/eastgate/Development/ecoPrimals/membrane/local-terminal/remote")


def shannon(text):
    words = text.lower().split()
    if not words:
        return 0.0
    freq = Counter(words)
    total = len(words)
    return -sum(p * math.log2(p) for p in (c/total for c in freq.values()) if p > 0)


def sigmoid(x, mid=0.5, k=10.0):
    z = k * (x - mid)
    if z > 500: return 1.0
    if z < -500: return 0.0
    return 1.0 / (1.0 + math.exp(-z))


LANG_MAP = {
    '.rs': 'rust', '.js': 'js', '.py': 'python', '.sh': 'shell',
    '.toml': 'toml', '.md': 'markdown', '.html': 'html',
}
SKIP = {'target', '.git', 'node_modules', '__pycache__', '.cargo', 'vendor'}


def scan_file(path, root):
    ext = path.suffix.lower()
    lang = LANG_MAP.get(ext)
    if not lang:
        return None
    try:
        text = path.read_text(errors='replace')
    except Exception:
        return None
    lines = text.splitlines()
    if not lines:
        return None
    h = shannon(text)
    types = funcs = imports = 0
    for line in lines:
        s = line.strip()
        if lang == 'rust':
            if s.startswith(('pub enum ', 'enum ')): types += 1
            elif s.startswith(('pub struct ', 'struct ')): types += 1
            elif s.startswith(('pub fn ', 'fn ', 'pub async fn ')): funcs += 1
            elif s.startswith('use '): imports += 1
        elif lang == 'python':
            if s.startswith('def '): funcs += 1
            elif s.startswith('class '): types += 1
            elif s.startswith(('import ', 'from ')): imports += 1
        elif lang == 'js':
            if 'function ' in s or s.startswith(('const ', 'var ', 'let ')): funcs += 1
        elif lang == 'shell':
            if '()' in s and '{' in s: funcs += 1

    rel = str(path.relative_to(root))
    repo = rel.split('/')[0] if '/' in rel else '.'

    return {
        'path': rel, 'repo': repo, 'lang': lang,
        'lines': len(lines), 'shannon': round(h, 3),
        'types': types, 'functions': funcs, 'imports': imports,
    }


def classify(props):
    """Vitruvian classification: genotype → stage."""
    h = props['shannon']
    types = props['types']
    funcs = props['functions']
    imports = props['imports']
    lines = props['lines']
    lang = props['lang']

    complexity = sigmoid(h / 12.0, 0.5, 8)
    skeleton = sigmoid(types / 20.0, 0.5, 6)

    if lines < 20 or h < 2.0:
        return 'banana', 0.0
    if lines < 100 and funcs <= 2 and types == 0:
        return 'flatworm', complexity
    if lang in ('js', 'html') and types == 0:
        return ('jellyfish' if funcs > 10 else 'flatworm'), complexity

    invertebrate = complexity * (1 - skeleton)
    vertebrate_score = complexity * skeleton

    if types == 0 or skeleton < 0.3:
        pair_ratio = funcs / max(lines / 50, 1)
        has_web = imports > 5 and funcs > 3
        has_trap = complexity > 0.5 and 0.8 < pair_ratio <= 1.5
        if has_web and has_trap:
            return 'spider', invertebrate
        elif pair_ratio > 1.5:
            return 'millipede', invertebrate
        elif funcs > 0 and lines / max(funcs, 1) > 100:
            return 'centipede', invertebrate
        else:
            return 'jellyfish', invertebrate

    if vertebrate_score > 0.3:
        return 'vertebrate', vertebrate_score
    return 'flatworm', complexity


def inject_chaos(stage, score, chaos_level=0.05):
    """Add chaos to classification — perturbation reveals robustness."""
    stages = ['banana', 'flatworm', 'jellyfish', 'centipede', 'millipede', 'spider', 'vertebrate']
    idx = stages.index(stage)
    noise = random.gauss(0, chaos_level * len(stages))
    new_idx = max(0, min(len(stages) - 1, round(idx + noise)))
    perturbed = stages[new_idx]
    stable = (perturbed == stage)
    return perturbed, stable


def topo_compress(files_by_repo):
    """Topological compression: which repos connect through imports."""
    edges = []
    repo_langs = {}
    repo_stages = {}
    for repo, files in files_by_repo.items():
        langs = Counter(f['lang'] for f in files)
        stages = Counter(f.get('stage', 'unknown') for f in files)
        repo_langs[repo] = langs.most_common(1)[0][0] if langs else 'unknown'
        repo_stages[repo] = stages.most_common(1)[0][0] if stages else 'unknown'
        avg_imports = sum(f['imports'] for f in files) / max(len(files), 1)
        if avg_imports > 3:
            for other_repo in files_by_repo:
                if other_repo != repo:
                    edges.append((repo, other_repo, round(avg_imports, 1)))

    return {
        'repos': len(files_by_repo),
        'edges': len(edges),
        'density': round(len(edges) / max(len(files_by_repo) ** 2, 1), 4),
        'repo_langs': repo_langs,
        'repo_stages': repo_stages,
        'top_edges': sorted(edges, key=lambda e: -e[2])[:20],
    }


def shannon_sort(files):
    """Sort by Shannon entropy — highest information density first."""
    return sorted(files, key=lambda f: -f.get('shannon', 0))


def phenotype_traits(stage_counts, total_files, chaos_stability, topo):
    """Extract phenotype traits from the sorted data."""
    traits = {}

    dominant = max(stage_counts, key=stage_counts.get)
    traits['dominant_stage'] = dominant
    traits['dominant_pct'] = round(100 * stage_counts[dominant] / total_files, 1)

    vert = stage_counts.get('vertebrate', 0)
    inv = sum(v for k, v in stage_counts.items() if k not in ('banana', 'flatworm', 'vertebrate'))
    traits['vertebrate_ratio'] = round(vert / max(inv, 1), 4)
    traits['invertebrate_dominance'] = inv > vert

    spider = stage_counts.get('spider', 0)
    traits['spider_count'] = spider
    traits['spider_pct'] = round(100 * spider / total_files, 1)
    traits['web_builder'] = spider > total_files * 0.02

    traits['chaos_stability'] = round(chaos_stability, 4)
    traits['robust'] = chaos_stability > 0.85

    traits['topo_density'] = topo['density']
    traits['connected'] = topo['density'] > 0.1

    pi_rem = (total_files * PI) % 1
    traits['pi_remainder'] = round(pi_rem, 6)

    complexity_bits = math.log2(total_files) if total_files > 0 else 0
    entropy_bits = -sum(
        (v/total_files) * math.log2(v/total_files)
        for v in stage_counts.values() if v > 0
    )
    traits['complexity_bits'] = round(complexity_bits, 2)
    traits['stage_entropy_bits'] = round(entropy_bits, 4)
    traits['compression_ratio'] = round(complexity_bits / max(entropy_bits, 0.001), 4)

    return traits


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/home/eastgate/Development/ecoPrimals')
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    print(f"""
╔══════════════════════════════════════════════════════════════╗
║  🧬 PHENOTYPE SORT — Divergent stadial → convergent express  ║
║                                                              ║
║  genotype → chaos → arena → shannon → topo → voxel → digest  ║
║  {ts}                                     ║
╚══════════════════════════════════════════════════════════════╝
""")

    # ═══ PHASE 1: SCAN (genotype) ═══
    print("═══ PHASE 1: SCAN (genotype) ═══")
    all_files = []
    files_by_repo = defaultdict(list)
    for path in sorted(root.rglob('*')):
        if not path.is_file() or any(p in SKIP for p in path.parts):
            continue
        props = scan_file(path, root)
        if props:
            stage, score = classify(props)
            props['stage'] = stage
            props['score'] = round(score, 4)
            all_files.append(props)
            files_by_repo[props['repo']].append(props)

    stage_counts = Counter(f['stage'] for f in all_files)
    total = len(all_files)
    print(f"  Scanned: {total:,} files across {len(files_by_repo)} repos")
    ORDER = ['banana', 'flatworm', 'jellyfish', 'centipede', 'millipede', 'spider', 'vertebrate']
    for s in ORDER:
        n = stage_counts.get(s, 0)
        pct = 100 * n / total if total else 0
        bar = '█' * int(pct / 2)
        print(f"    {s:<12} {n:>6} ({pct:>5.1f}%) {bar}")

    # ═══ PHASE 2: CHAOS (perturbation) ═══
    print("\n═══ PHASE 2: CHAOS (perturbation) ═══")
    random.seed(42)  # reproducible chaos
    stable_count = 0
    chaos_stages = Counter()
    for f in all_files:
        perturbed, stable = inject_chaos(f['stage'], f['score'], chaos_level=0.08)
        f['chaos_stage'] = perturbed
        f['chaos_stable'] = stable
        chaos_stages[perturbed] += 1
        if stable:
            stable_count += 1

    stability = stable_count / total if total else 0
    print(f"  Chaos level: 8% perturbation (σ = 0.56 stages)")
    print(f"  Stability: {stable_count:,}/{total:,} ({100*stability:.1f}%) held classification")
    print(f"  Drift: {total - stable_count:,} files reclassified under chaos")
    print(f"  Post-chaos distribution:")
    for s in ORDER:
        n = chaos_stages.get(s, 0)
        orig = stage_counts.get(s, 0)
        delta = n - orig
        sign = '+' if delta > 0 else ''
        print(f"    {s:<12} {n:>6} ({sign}{delta})")

    # ═══ PHASE 3: ARENA (fitness from bench) ═══
    print("\n═══ PHASE 3: ARENA (chipmunk fitness signal) ═══")
    bench_file = OUT_DIR / "arena-bench-results.json"
    bench = None
    if bench_file.exists():
        try:
            bench = json.loads(bench_file.read_text())
            board = bench.get('leaderboard', [])
            print(f"  Models benchmarked: {len(board)}")
            for m in board[:5]:
                print(f"    #{m['rank']} {m['model']:<25} {m['pct']}%")
        except Exception:
            pass
    if not bench:
        print("  No bench results — arena dormant")

    # ═══ PHASE 4: SHANNON SORT (entropy compression) ═══
    print("\n═══ PHASE 4: SHANNON SORT (entropy compression) ═══")
    sorted_files = shannon_sort(all_files)
    top_entropy = sorted_files[:10]
    low_entropy = sorted_files[-5:]
    h_values = [f['shannon'] for f in all_files if f['shannon'] > 0]
    h_mean = sum(h_values) / len(h_values) if h_values else 0
    h_std = (sum((h - h_mean)**2 for h in h_values) / len(h_values))**0.5 if h_values else 0

    print(f"  Mean entropy: {h_mean:.3f} bits/word")
    print(f"  Std dev:      {h_std:.3f}")
    print(f"  Highest entropy (most information-dense):")
    for f in top_entropy[:5]:
        short = f['path'][-55:] if len(f['path']) > 55 else f['path']
        print(f"    H={f['shannon']:>6.2f}  {f['stage']:<12} {short}")
    print(f"  Lowest entropy (most compressible):")
    for f in low_entropy:
        short = f['path'][-55:] if len(f['path']) > 55 else f['path']
        print(f"    H={f['shannon']:>6.2f}  {f['stage']:<12} {short}")

    # ═══ PHASE 5: TOPO COMPRESS (topology) ═══
    print("\n═══ PHASE 5: TOPO COMPRESS (what connects to what) ═══")
    topo = topo_compress(files_by_repo)
    print(f"  Repos: {topo['repos']}")
    print(f"  Import edges: {topo['edges']}")
    print(f"  Density: {topo['density']}")
    print(f"  Top connected repos:")
    seen = set()
    for src, dst, weight in topo['top_edges'][:10]:
        if src not in seen:
            stage = topo['repo_stages'].get(src, '?')
            lang = topo['repo_langs'].get(src, '?')
            print(f"    {src:<35} [{stage}/{lang}] imports→{weight:.1f}")
            seen.add(src)

    # ═══ PHASE 6: PHENOTYPE (the expression) ═══
    print("\n═══ PHASE 6: PHENOTYPE (the expression) ═══")
    traits = phenotype_traits(stage_counts, total, stability, topo)
    print(f"  Dominant: {traits['dominant_stage']} ({traits['dominant_pct']}%)")
    print(f"  Vertebrate ratio: {traits['vertebrate_ratio']} {'(invertebrate dominance)' if traits['invertebrate_dominance'] else ''}")
    print(f"  Spider count: {traits['spider_count']} ({traits['spider_pct']}%) {'— web builder ✓' if traits['web_builder'] else ''}")
    print(f"  Chaos stability: {traits['chaos_stability']} {'— robust ✓' if traits['robust'] else '— fragile'}")
    print(f"  Topo density: {traits['topo_density']} {'— connected ✓' if traits['connected'] else '— sparse'}")
    print(f"  π remainder: {traits['pi_remainder']}")
    print(f"  Complexity: {traits['complexity_bits']} bits")
    print(f"  Stage entropy: {traits['stage_entropy_bits']} bits")
    print(f"  Compression: {traits['compression_ratio']}:1")

    # ═══ WRITE STATE ═══
    state = {
        "ts": ts,
        "pipeline": "genotype → chaos → arena → shannon → topo → voxel → digest",
        "total_files": total,
        "total_repos": len(files_by_repo),
        "genotype": dict(stage_counts),
        "chaos": {
            "level": 0.08,
            "stability": round(stability, 4),
            "post_chaos": dict(chaos_stages),
        },
        "shannon": {
            "mean_entropy": round(h_mean, 3),
            "std_entropy": round(h_std, 3),
            "top_5": [{"path": f["path"], "entropy": f["shannon"], "stage": f["stage"]} for f in top_entropy[:5]],
        },
        "topo": topo,
        "phenotype": traits,
        "pi_remainder": traits['pi_remainder'],
        "arena": {
            "models": len(bench.get("leaderboard", [])) if bench else 0,
            "winner": bench["leaderboard"][0]["model"] if bench and bench.get("leaderboard") else None,
        },
    }

    out = OUT_DIR / "phenotype-sort.json"
    out.write_text(json.dumps(state, indent=2, default=str))
    print(f"\n  📊 State: {out}")
    print(f"\n  The organism sorted itself. The phenotype is expressed.")

    return state


if __name__ == '__main__':
    main()

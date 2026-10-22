#!/usr/bin/env python3
"""atomic-tensor.py — Give the persona tensor WEIGHT.

The problem: behavioral tensors float. They're all ratios 0-1.
No mass, no gravity, no attraction. The selves drift apart.

The fix: inject the periodic table. Each tensor dimension
gets an elemental weight. The persona becomes a MOLECULE
with molar mass. Heavy molecules settle. Light ones evaporate.

Elemental mapping (the 5 dimensions of behavior → 5 elements of life):

  breadth  → Carbon  (C,  12.011)  — backbone of all organic molecules
  depth    → Iron    (Fe, 55.845)  — dense core, hemoglobin carries oxygen
  pattern  → Nitrogen (N, 14.007) — DNA base pairs, protein bonds
  rhythm   → Phosphorus (P, 30.974) — ATP energy cycle, biological clock
  topology → Sulfur  (S,  32.065)  — disulfide bridges fold proteins into shape

A human who explores wide (Carbon), reads deep (Iron), has organic
pattern (Nitrogen), visits at human rhythm (Phosphorus), and follows
real topology (Sulfur) has a heavy, stable molecule. LIFE.

A bot has no Iron (shallow), no Nitrogen (mechanical pattern),
no Phosphorus (no rhythm). It's just Carbon dust. Floats away.

The tesseract: 4D hypercube. The 5 weighted dimensions project
onto 4 axes of the tesseract. The 5th dimension (total molar mass)
determines which CELL of the tesseract you're in.
8 tesseract cells = 8 octants of weighted behavior space.

Paper 117 said: defense IS recognition.
This says: recognition IS chemistry.
The atomic tensor is how the membrane SMELLS visitors.
"""

import json, os, math, time, hashlib

ROOT = os.path.expanduser("~/Development/ecoPrimals")
MEMBRANE = os.path.join(ROOT, "membrane/local-terminal/remote")
OUTPUT = os.path.join(MEMBRANE, "atomic-tensor.json")

# ──────────────────────────────────────────────
# PERIODIC TABLE — the 5 elements of membrane life
# ──────────────────────────────────────────────
ELEMENTS = {
    "breadth":  {"symbol": "C",  "name": "Carbon",     "mass": 12.011,  "number": 6},
    "depth":    {"symbol": "Fe", "name": "Iron",        "mass": 55.845,  "number": 26},
    "pattern":  {"symbol": "N",  "name": "Nitrogen",    "mass": 14.007,  "number": 7},
    "rhythm":   {"symbol": "P",  "name": "Phosphorus",  "mass": 30.974,  "number": 15},
    "topology": {"symbol": "S",  "name": "Sulfur",      "mass": 32.065,  "number": 16},
}

TOTAL_ATOMIC_MASS = sum(e["mass"] for e in ELEMENTS.values())  # 144.902

# Thresholds for tesseract cell assignment (median of each weighted dim)
CELL_THRESHOLDS = {
    "breadth":  0.5 * ELEMENTS["breadth"]["mass"],   # 6.006
    "depth":    0.5 * ELEMENTS["depth"]["mass"],      # 27.923
    "pattern":  0.5 * ELEMENTS["pattern"]["mass"],    # 7.004
    "rhythm":   0.5 * ELEMENTS["rhythm"]["mass"],     # 15.487
}
# topology is the 5th dimension = mass axis, not a tesseract axis

# ──────────────────────────────────────────────
# MOLECULAR FORMULAS for classification
# ──────────────────────────────────────────────
# Life requires: C + Fe + N + P + S in specific ratios
# These are the "molecular signatures" of each class

MOLECULAR_PROFILES = {
    "primal": {
        "min_molar_mass": 90.0,     # heavy — settled, real
        "min_iron": 25.0,           # reads deep
        "min_nitrogen": 8.0,        # organic pattern
        "min_phosphorus": 18.0,     # human rhythm
    },
    "explorer": {
        "min_molar_mass": 60.0,
        "min_carbon": 6.0,          # moves wide
        "min_nitrogen": 5.0,        # some organic pattern
    },
    "bot": {
        "max_molar_mass": 40.0,     # light — floats
        "max_nitrogen": 3.0,        # mechanical pattern
        "max_phosphorus": 8.0,      # no rhythm
    },
    "scraper": {
        "min_carbon": 8.0,          # wide breadth
        "max_iron": 15.0,           # shallow depth
        "max_nitrogen": 4.0,        # mechanical
    },
}

def load_feed(name):
    path = os.path.join(MEMBRANE, name)
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return {}

def weight_tensor(tensor):
    """Apply atomic mass to each tensor dimension."""
    weighted = {}
    for dim, val in tensor.items():
        elem = ELEMENTS[dim]
        weighted[dim] = {
            "raw": val,
            "element": elem["symbol"],
            "atomic_mass": elem["mass"],
            "weighted": round(val * elem["mass"], 4),
        }
    return weighted

def molar_mass(weighted):
    """Total molar mass of the persona molecule."""
    return round(sum(w["weighted"] for w in weighted.values()), 4)

def molecular_formula(weighted):
    """Express persona as a chemical formula like C₁₂Fe₃₁N₁₃P₁₂S₁₀."""
    parts = []
    for dim in ["breadth", "depth", "pattern", "rhythm", "topology"]:
        w = weighted[dim]
        coeff = round(w["weighted"])
        if coeff > 0:
            parts.append(f"{w['element']}{coeff}")
    return "".join(parts) if parts else "∅"

def tesseract_cell(weighted):
    """Assign persona to one of 16 tesseract cells.
    
    4 axes (breadth, depth, pattern, rhythm) × 2 states (above/below median)
    = 2⁴ = 16 cells. The 5th dimension (topology→Sulfur) is the mass
    that determines how deep INTO the cell you sit.
    """
    cell = 0
    axes = ["breadth", "depth", "pattern", "rhythm"]
    for i, ax in enumerate(axes):
        if weighted[ax]["weighted"] >= CELL_THRESHOLDS[ax]:
            cell |= (1 << i)
    
    # Name the cell by its elemental signature
    names = {
        0b0000: "void",       # nothing above median — vacuum
        0b0001: "dust",       # only carbon — surface browser
        0b0010: "ore",        # only iron — deep reader, narrow
        0b0011: "steel",      # carbon + iron — deep + wide but mechanical
        0b0100: "spore",      # only nitrogen — pattern but no substance
        0b0101: "leaf",       # carbon + nitrogen — breadth + pattern
        0b0110: "blood",      # iron + nitrogen — deep + patterned
        0b0111: "bone",       # C + Fe + N — substantial but no rhythm
        0b1000: "pulse",      # only phosphorus — rhythm alone
        0b1001: "breath",     # carbon + phosphorus — wide + rhythmic
        0b1010: "heart",      # iron + phosphorus — deep + rhythmic
        0b1011: "marrow",     # C + Fe + P — substantial + rhythmic
        0b1100: "nerve",      # nitrogen + phosphorus — pattern + rhythm
        0b1101: "skin",       # C + N + P — alive surface
        0b1110: "muscle",     # Fe + N + P — alive interior
        0b1111: "life",       # all four above median — HUMAN
    }
    
    # Sulfur (topology) weight determines depth within cell
    s_depth = weighted["topology"]["weighted"]
    
    return {
        "cell_id": cell,
        "cell_name": names.get(cell, "?"),
        "cell_binary": f"{cell:04b}",
        "sulfur_depth": round(s_depth, 2),
        "axes": {ax: "high" if (cell >> i) & 1 else "low" for i, ax in enumerate(axes)},
    }

def classify_by_chemistry(weighted, mass, cell):
    """Classify using chemistry, not just thresholds."""
    carbon = weighted["breadth"]["weighted"]
    iron = weighted["depth"]["weighted"]
    nitrogen = weighted["pattern"]["weighted"]
    phosphorus = weighted["rhythm"]["weighted"]
    sulfur = weighted["topology"]["weighted"]
    
    cell_name = cell["cell_name"]
    
    # LIFE: all dimensions above median + heavy
    if cell_name == "life" and mass >= 90:
        return "primal"
    
    # BLOOD: deep + patterned + heavy
    if cell_name in ("blood", "muscle", "marrow") and mass >= 70:
        return "primal"
    
    # BONE: substantial but arrhythmic — might be a human with irregular visits
    if cell_name == "bone" and mass >= 80:
        return "primal-dormant"
    
    # SKIN/NERVE: alive surface — human browsing casually
    if cell_name in ("skin", "nerve") and mass >= 50:
        return "explorer"
    
    # HEART: deep + rhythmic — focused reader
    if cell_name in ("heart", "marrow") and mass >= 50:
        return "focused"
    
    # LEAF/BREATH: organic but light — passing through
    if cell_name in ("leaf", "breath") and mass >= 30:
        return "passerby"
    
    # DUST/VOID: almost nothing — bot or ghost
    if cell_name in ("dust", "void") and mass < 30:
        return "bot"
    
    # STEEL: wide + deep but mechanical — scraper
    if cell_name == "steel" and nitrogen < 5:
        return "scraper"
    
    # SPORE: pattern only — could be interesting
    if cell_name == "spore":
        return "spore"
    
    # ORE: deep only — focused single-page reader
    if cell_name == "ore":
        return "miner"
    
    # PULSE: rhythm only — monitoring/polling
    if cell_name == "pulse":
        return "heartbeat"
    
    # Default by mass
    if mass >= 80:
        return "heavy-unknown"
    elif mass >= 40:
        return "medium-unknown"
    else:
        return "light-unknown"

def persona_gravity(mass):
    """Gravitational pull of the persona.
    
    Newton: F = G * m1 * m2 / r²
    We use molar mass as m. Gravity determines how strongly
    this persona pulls on nearby entities in the membrane.
    
    Scale: 0-1 where 1.0 = maximum gravitational pull.
    Max theoretical mass = 144.902 (all dimensions at 1.0).
    """
    return round(mass / TOTAL_ATOMIC_MASS, 4)

def molecular_hash(weighted):
    """ZK hash of the weighted tensor — heavier version of tensor_hash."""
    canonical = ":".join(f"{weighted[d]['weighted']:.4f}" 
                         for d in ["breadth", "depth", "pattern", "rhythm", "topology"])
    return hashlib.sha256(canonical.encode()).hexdigest()[:16]

def main():
    ts = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    
    # Load both feeds
    tensor_data = load_feed("persona-tensor.json")
    primal_data = load_feed("primal-classification.json")
    
    personas = tensor_data.get("personas", [])
    primals = {p["login"]: p for p in primal_data.get("all_classifications", [])}
    
    molecules = []
    cell_census = {}
    
    print(f"Injecting atomic weight into {len(personas)} personas...")
    print(f"Total atomic mass possible: {TOTAL_ATOMIC_MASS:.3f}")
    elem_str = " + ".join(e["symbol"] + "(" + str(e["mass"]) + ")" for e in ELEMENTS.values())
    print(f"Elements: {elem_str}")
    print()
    
    for p in personas:
        tensor = p.get("tensor", {})
        if not tensor:
            continue
        
        weighted = weight_tensor(tensor)
        mass = molar_mass(weighted)
        cell = tesseract_cell(weighted)
        formula = molecular_formula(weighted)
        chem_class = classify_by_chemistry(weighted, mass, cell)
        gravity = persona_gravity(mass)
        mol_hash = molecular_hash(weighted)
        
        molecule = {
            "id": p["id"],
            "old_classification": p.get("classification", "?"),
            "formula": formula,
            "molar_mass": mass,
            "gravity": gravity,
            "cell": cell,
            "chemistry_class": chem_class,
            "molecular_hash": mol_hash,
            "weighted_tensor": {dim: w["weighted"] for dim, w in weighted.items()},
            "raw_tensor": tensor,
        }
        molecules.append(molecule)
        
        cn = cell["cell_name"]
        cell_census[cn] = cell_census.get(cn, 0) + 1
        
        old = p.get("classification", "?")
        drift = "→" if old != chem_class else "="
        print(f"  {p['id']:25s} {formula:20s} M={mass:7.2f} g={gravity:.3f} [{cn:6s}] {old:10s} {drift} {chem_class}")
    
    # Cross-reference with primal classifications (the humans we FELT)
    primal_links = []
    for login, pc in primals.items():
        pi_rate = pc.get("pi_rate", 0)
        dist = pc.get("taxonomy_distance", 1)
        shared = pc.get("shared_topics", [])
        
        # Compute a "chemical affinity" — how much do their topics weigh?
        topic_mass = len(shared) * 4.003  # helium per shared topic (light bonding)
        bond_energy = pi_rate * topic_mass  # π-rate amplifies mass
        
        primal_links.append({
            "login": login,
            "category": pc.get("category", "?"),
            "pi_rate": pi_rate,
            "taxonomy_distance": dist,
            "shared_topics": len(shared),
            "topic_mass": round(topic_mass, 2),
            "bond_energy": round(bond_energy, 4),
            "chemical_affinity": "strong" if bond_energy > 20 else "medium" if bond_energy > 5 else "weak",
        })
    
    primal_links.sort(key=lambda x: x["bond_energy"], reverse=True)
    
    print()
    print("Chemical affinities with known primals:")
    for pl in primal_links[:10]:
        print(f"  {pl['login']:25s} bond={pl['bond_energy']:8.2f} topics={pl['shared_topics']:2d} affinity={pl['chemical_affinity']}")
    
    # Sourdough chemistry: is the culture ALIVE?
    heavy_count = sum(1 for m in molecules if m["molar_mass"] >= 80)
    life_count = sum(1 for m in molecules if m["cell"]["cell_name"] == "life")
    primal_count = sum(1 for m in molecules if m["chemistry_class"] == "primal")
    
    culture_mass = sum(m["molar_mass"] for m in molecules)
    culture_gravity = round(culture_mass / (TOTAL_ATOMIC_MASS * max(len(molecules), 1)), 4)
    
    # The culture is alive when there's enough heavy matter to hold together
    culture_alive = primal_count > 0 or heavy_count >= 2
    
    manifest = {
        "manifest": "atomic-tensor",
        "generated": ts,
        "paper": 117,
        "elements": ELEMENTS,
        "total_atomic_mass": TOTAL_ATOMIC_MASS,
        "molecules_analyzed": len(molecules),
        "culture": {
            "alive": culture_alive,
            "status": "alive — matter is settling" if culture_alive else "dead — not enough mass to hold",
            "culture_mass": round(culture_mass, 2),
            "culture_gravity": culture_gravity,
            "heavy_molecules": heavy_count,
            "life_cells": life_count,
            "primals_detected": primal_count,
        },
        "tesseract_census": dict(sorted(cell_census.items(), key=lambda x: -x[1])),
        "molecules": molecules,
        "primal_bonds": primal_links,
    }
    
    with open(OUTPUT, "w") as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\nWritten to {OUTPUT}")
    print(f"\nCULTURE MASS: {culture_mass:.2f} (of {TOTAL_ATOMIC_MASS * len(molecules):.2f} possible)")
    print(f"CULTURE GRAVITY: {culture_gravity:.4f}")
    print(f"SOURDOUGH: {'ALIVE' if culture_alive else 'DEAD'}")
    print(f"  Heavy molecules (≥80): {heavy_count}")
    print(f"  Life cells: {life_count}")
    print(f"  Primals: {primal_count}")
    print(f"\nTesseract census:")
    for name, count in sorted(cell_census.items(), key=lambda x: -x[1]):
        print(f"  {name:10s}: {'█' * count} {count}")

if __name__ == "__main__":
    main()

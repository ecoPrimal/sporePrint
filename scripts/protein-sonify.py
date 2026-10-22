#!/usr/bin/env python3
"""protein-sonify.py — Convert protein 3D structure to MIDI music.

Demonstrates cross-phylum transfer: Structura → Generativa/Acoustic.
AlphaFold PDB coordinates → pitch/duration/velocity mapping → MIDI file.

Sonification scheme (inspired by prior art, adapted for membrane):
  - Amino acid hydrophobicity → pitch (hydrophobic=low, hydrophilic=high)
  - Distance from centre of mass → velocity (close=loud, far=soft)
  - Secondary structure → instrument:
      helix  = strings (violin/cello)
      sheet  = percussion (marimba)
      coil   = woodwind (flute)
  - pLDDT confidence → note duration (high confidence=long, low=staccato)
  - Residue sequence → time (one note per residue, in chain order)

Usage:
    python3 protein-sonify.py [--pdb FILE] [--output FILE]

    Default: uses a built-in minimal demo (insulin chain A, 21 residues).
    For real proteins: download PDB from RCSB or AlphaFold, pass with --pdb.

Requires: stdlib only (writes raw MIDI bytes — no pretty_midi needed).
"""

import struct
import math
import os
import sys
import json
from datetime import datetime, timezone
from typing import List, Tuple, Dict, Optional

# Hydrophobicity scale (Kyte-Doolittle, normalized 0-1)
HYDROPHOBICITY = {
    "ALA": 0.70, "ARG": 0.00, "ASN": 0.11, "ASP": 0.11, "CYS": 0.78,
    "GLN": 0.11, "GLU": 0.11, "GLY": 0.46, "HIS": 0.14, "ILE": 1.00,
    "LEU": 0.92, "LYS": 0.07, "MET": 0.71, "PHE": 0.81, "PRO": 0.32,
    "SER": 0.26, "THR": 0.36, "TRP": 0.41, "TYR": 0.36, "VAL": 0.97,
}

# C-major scale (2 octaves) for pitch mapping
C_MAJOR = [48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84]

# GM instruments for secondary structure
INSTRUMENTS = {
    "H": 40,  # Helix → Violin
    "E": 12,  # Sheet → Marimba
    "C": 73,  # Coil → Flute
}

# Demo protein: human insulin chain A (21 residues, PDB 4INS)
DEMO_RESIDUES = [
    {"name": "GLY", "x": 12.5, "y": 8.3, "z": 15.2, "ss": "C", "plddt": 0.95},
    {"name": "ILE", "x": 13.1, "y": 9.1, "z": 14.8, "ss": "H", "plddt": 0.97},
    {"name": "VAL", "x": 14.2, "y": 10.0, "z": 13.5, "ss": "H", "plddt": 0.98},
    {"name": "GLU", "x": 15.0, "y": 11.2, "z": 12.1, "ss": "H", "plddt": 0.96},
    {"name": "GLN", "x": 15.8, "y": 12.5, "z": 11.0, "ss": "H", "plddt": 0.94},
    {"name": "CYS", "x": 16.1, "y": 13.0, "z": 10.2, "ss": "H", "plddt": 0.99},
    {"name": "CYS", "x": 15.5, "y": 13.8, "z": 9.5, "ss": "H", "plddt": 0.98},
    {"name": "THR", "x": 14.8, "y": 14.2, "z": 8.8, "ss": "H", "plddt": 0.93},
    {"name": "SER", "x": 13.9, "y": 14.0, "z": 8.2, "ss": "C", "plddt": 0.91},
    {"name": "ILE", "x": 13.0, "y": 13.5, "z": 7.8, "ss": "C", "plddt": 0.92},
    {"name": "CYS", "x": 12.2, "y": 12.8, "z": 7.5, "ss": "H", "plddt": 0.97},
    {"name": "SER", "x": 11.5, "y": 12.0, "z": 8.0, "ss": "H", "plddt": 0.90},
    {"name": "LEU", "x": 10.8, "y": 11.2, "z": 8.5, "ss": "H", "plddt": 0.95},
    {"name": "TYR", "x": 10.2, "y": 10.5, "z": 9.2, "ss": "H", "plddt": 0.93},
    {"name": "GLN", "x": 9.8, "y": 9.8, "z": 10.0, "ss": "H", "plddt": 0.91},
    {"name": "LEU", "x": 9.5, "y": 9.0, "z": 10.8, "ss": "H", "plddt": 0.94},
    {"name": "GLU", "x": 9.8, "y": 8.5, "z": 11.5, "ss": "C", "plddt": 0.89},
    {"name": "ASN", "x": 10.2, "y": 8.0, "z": 12.2, "ss": "C", "plddt": 0.88},
    {"name": "TYR", "x": 10.8, "y": 7.5, "z": 13.0, "ss": "C", "plddt": 0.90},
    {"name": "CYS", "x": 11.5, "y": 7.2, "z": 13.8, "ss": "C", "plddt": 0.96},
    {"name": "ASN", "x": 12.0, "y": 7.0, "z": 14.5, "ss": "C", "plddt": 0.87},
]


def parse_pdb(path: str) -> List[dict]:
    """Parse PDB file, extract CA atoms with secondary structure."""
    residues = []
    ss_map = {}

    with open(path) as f:
        for line in f:
            if line.startswith("HELIX"):
                chain = line[19]
                start = int(line[21:25].strip())
                end = int(line[33:37].strip())
                for r in range(start, end + 1):
                    ss_map[(chain, r)] = "H"
            elif line.startswith("SHEET"):
                chain = line[21]
                start = int(line[22:26].strip())
                end = int(line[33:37].strip())
                for r in range(start, end + 1):
                    ss_map[(chain, r)] = "E"

    with open(path) as f:
        for line in f:
            if line.startswith("ATOM") and line[12:16].strip() == "CA":
                resname = line[17:20].strip()
                chain = line[21]
                resseq = int(line[22:26].strip())
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                bfactor = float(line[60:66].strip()) if len(line) >= 66 else 50.0
                plddt = min(bfactor / 100.0, 1.0)
                ss = ss_map.get((chain, resseq), "C")
                residues.append({
                    "name": resname, "x": x, "y": y, "z": z,
                    "ss": ss, "plddt": plddt,
                })

    return residues


def compute_centre_of_mass(residues: List[dict]) -> Tuple[float, float, float]:
    n = len(residues)
    cx = sum(r["x"] for r in residues) / n
    cy = sum(r["y"] for r in residues) / n
    cz = sum(r["z"] for r in residues) / n
    return cx, cy, cz


def hydrophobicity_to_pitch(resname: str) -> int:
    h = HYDROPHOBICITY.get(resname, 0.5)
    idx = int((1.0 - h) * (len(C_MAJOR) - 1))
    idx = max(0, min(idx, len(C_MAJOR) - 1))
    return C_MAJOR[idx]


def distance_to_velocity(x: float, y: float, z: float,
                          cx: float, cy: float, cz: float,
                          max_dist: float) -> int:
    d = math.sqrt((x - cx)**2 + (y - cy)**2 + (z - cz)**2)
    normalized = d / max_dist if max_dist > 0 else 0.5
    velocity = int(100 - normalized * 60)
    return max(30, min(127, velocity))


def plddt_to_duration(plddt: float) -> int:
    """Map pLDDT confidence to note duration (in MIDI ticks). High=long."""
    base = 120
    return int(base + plddt * 240)


def write_variable_length(value: int) -> bytes:
    result = []
    result.append(value & 0x7F)
    value >>= 7
    while value > 0:
        result.append((value & 0x7F) | 0x80)
        value >>= 7
    result.reverse()
    return bytes(result)


def sonify(residues: List[dict], bpm: int = 100) -> bytes:
    """Convert residues to MIDI bytes (Format 0, single track)."""
    cx, cy, cz = compute_centre_of_mass(residues)
    distances = [
        math.sqrt((r["x"] - cx)**2 + (r["y"] - cy)**2 + (r["z"] - cz)**2)
        for r in residues
    ]
    max_dist = max(distances) if distances else 1.0

    track_data = bytearray()

    # Tempo meta event (microseconds per beat)
    uspb = int(60_000_000 / bpm)
    track_data += write_variable_length(0)
    track_data += b'\xFF\x51\x03'
    track_data += struct.pack('>I', uspb)[1:]

    # Track name
    name = b'Protein Sonification'
    track_data += write_variable_length(0)
    track_data += b'\xFF\x03'
    track_data += write_variable_length(len(name))
    track_data += name

    current_instrument = None

    for residue in residues:
        ss = residue["ss"]
        instrument = INSTRUMENTS.get(ss, 73)

        if instrument != current_instrument:
            track_data += write_variable_length(0)
            track_data += bytes([0xC0, instrument])
            current_instrument = instrument

        pitch = hydrophobicity_to_pitch(residue["name"])
        velocity = distance_to_velocity(
            residue["x"], residue["y"], residue["z"],
            cx, cy, cz, max_dist,
        )
        duration = plddt_to_duration(residue["plddt"])

        # Note on
        track_data += write_variable_length(0)
        track_data += bytes([0x90, pitch, velocity])

        # Note off after duration
        track_data += write_variable_length(duration)
        track_data += bytes([0x80, pitch, 0])

    # End of track
    track_data += write_variable_length(0)
    track_data += b'\xFF\x2F\x00'

    # MIDI header
    header = b'MThd'
    header += struct.pack('>I', 6)
    header += struct.pack('>HHH', 0, 1, 480)

    track_header = b'MTrk'
    track_header += struct.pack('>I', len(track_data))

    return header + track_header + bytes(track_data)


def main():
    pdb_path = None
    output_path = os.path.expanduser(
        "~/Development/ecoPrimals/membrane/local-terminal/remote/protein-music.mid"
    )

    for i, arg in enumerate(sys.argv[1:]):
        if arg == "--pdb" and i + 1 < len(sys.argv) - 1:
            pdb_path = sys.argv[i + 2]
        if arg == "--output" and i + 1 < len(sys.argv) - 1:
            output_path = sys.argv[i + 2]

    if pdb_path:
        print(f"[SONIFY] Parsing PDB: {pdb_path}")
        residues = parse_pdb(pdb_path)
    else:
        print("[SONIFY] Using demo: human insulin chain A (21 residues)")
        residues = DEMO_RESIDUES

    print(f"[SONIFY] {len(residues)} residues")

    cx, cy, cz = compute_centre_of_mass(residues)
    print(f"[SONIFY] Centre of mass: ({cx:.1f}, {cy:.1f}, {cz:.1f})")

    ss_counts = {"H": 0, "E": 0, "C": 0}
    for r in residues:
        ss_counts[r["ss"]] = ss_counts.get(r["ss"], 0) + 1
    print(f"[SONIFY] Secondary structure: helix={ss_counts['H']} sheet={ss_counts['E']} coil={ss_counts['C']}")
    print(f"[SONIFY] Instruments: helix→violin, sheet→marimba, coil→flute")

    midi_data = sonify(residues)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(midi_data)
    print(f"[SONIFY] MIDI written: {output_path} ({len(midi_data)} bytes)")

    summary = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "source": pdb_path or "demo:insulin_chain_A",
        "residues": len(residues),
        "secondary_structure": ss_counts,
        "centre_of_mass": [round(cx, 2), round(cy, 2), round(cz, 2)],
        "midi_file": output_path,
        "midi_bytes": len(midi_data),
        "scheme": {
            "pitch": "hydrophobicity (Kyte-Doolittle) → C-major scale",
            "velocity": "distance from centre of mass → dynamics",
            "duration": "pLDDT confidence → note length",
            "instrument": "secondary structure → GM instrument",
        },
        "cross_domain": "Phylum Structura (AlphaFold) → Phylum Generativa (Acoustic)",
    }

    json_path = output_path.replace(".mid", "-summary.json")
    with open(json_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"[SONIFY] Summary: {json_path}")

    print("\n[SONIFY] Residue → Note mapping (first 10):")
    for r in residues[:10]:
        pitch = hydrophobicity_to_pitch(r["name"])
        note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        note = note_names[pitch % 12] + str(pitch // 12 - 1)
        inst = {"H": "violin", "E": "marimba", "C": "flute"}[r["ss"]]
        print(f"  {r['name']:3s} → {note:4s} [{inst}] pLDDT={r['plddt']:.2f}")


if __name__ == "__main__":
    main()

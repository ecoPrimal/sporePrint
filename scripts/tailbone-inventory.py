#!/usr/bin/env python3
"""
tailbone-inventory.py — 5 body contact points when sitting

  the vitruvian man stands in the circle.
  but we SIT. on the tailbone.
  5 contact points: tailbone (center) + 2 sit-bones + 2 feet.

  this script inventories the entire organism from that position:
    1. TAILBONE (center/self) — what we ARE: files, lines, crates
    2. LEFT SIT-BONE (trans/persist) — membrane state, heartbeat, crons
    3. RIGHT SIT-BONE (trans/observe) — homunculus, evolve, atomic tensor
    4. LEFT FOOT (cis/receive) — HUD pages, feeds, papers, inbound
    5. RIGHT FOOT (cis/push) — GitHub repos, crates.io, output fleet, outbound

  the pattern is: in → out → in
    sit-bones face DOWN (trans, inward, persist)
    feet face DOWN but push OUTWARD (cis through trans)
    tailbone is the fold point

  output: tailbone-inventory.json in membrane + HUD data
"""

import json, os, subprocess, math, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
MEMBRANE = ROOT / "membrane" / "local-terminal" / "remote"
HUD_DATA = ROOT / "infra" / "hud" / "site" / "public" / "data"

def sh(cmd, cwd=None):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True,
                       cwd=cwd or str(ROOT), timeout=30)
    return r.stdout.strip()

def count_files(pattern, exclude=None):
    cmd = f"find {ROOT} -name '{pattern}' -type f"
    if exclude:
        for ex in exclude:
            cmd += f" -not -path '*/{ex}/*'"
    return int(sh(cmd + " | wc -l") or 0)

def count_lines(pattern, exclude=None):
    cmd = f"find {ROOT} -name '{pattern}' -type f"
    if exclude:
        for ex in exclude:
            cmd += f" -not -path '*/{ex}/*'"
    cmd += " -exec cat {} + | wc -l"
    return int(sh(cmd) or 0)

def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return {}

def count_dirs(path, depth=1):
    p = ROOT / path
    if not p.exists():
        return 0
    return int(sh(f"find {p} -maxdepth {depth} -type d | tail -n +2 | wc -l") or 0)

def gh_repo_count(owner):
    try:
        out = sh(f"gh repo list {owner} --limit 200 --json name -q '.[].name'")
        return len([l for l in out.splitlines() if l.strip()])
    except:
        return 0

ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
now = datetime.datetime.now(datetime.timezone.utc)
day_of_year = now.timetuple().tm_yday
pi_phase = (day_of_year * (math.pi % 1) * 1000) % 360

EXCL = ["target", ".git", "node_modules", "__pycache__"]

# ═══════════════════════════════════════════════════════
# 1. TAILBONE — center/self — what we ARE
# ═══════════════════════════════════════════════════════
print("1️⃣  scanning TAILBONE (center/self)...")
rust_files    = count_files("*.rs", EXCL)
rust_lines    = count_lines("*.rs", EXCL)
py_files      = count_files("*.py", EXCL)
py_lines      = count_lines("*.py", EXCL)
sh_files      = count_files("*.sh", EXCL)
html_files    = count_files("*.html", EXCL)
md_files      = count_files("*.md", EXCL)
json_files    = count_files("*.json", EXCL + ["membrane"])
toml_files    = count_files("*.toml", EXCL)
total_files   = int(sh(f"find {ROOT} -type f " + " ".join(f"-not -path '*/{e}/*'" for e in EXCL) + " | wc -l") or 0)
primal_crates = count_dirs("primals")
infra_crates  = count_dirs("infra")

tailbone = {
    "role": "center/self — what we ARE",
    "contact": "sacrum → coccyx → ground",
    "rust_files": rust_files,
    "rust_lines": rust_lines,
    "python_files": py_files,
    "python_lines": py_lines,
    "shell_scripts": sh_files,
    "html_pages": html_files,
    "markdown_docs": md_files,
    "json_configs": json_files,
    "toml_manifests": toml_files,
    "total_files": total_files,
    "primal_crates": primal_crates,
    "infra_modules": infra_crates,
    "mass": rust_lines + py_lines,
}

# ═══════════════════════════════════════════════════════
# 2. LEFT SIT-BONE — trans/persist — membrane state
# ═══════════════════════════════════════════════════════
print("2️⃣  scanning LEFT SIT-BONE (trans/persist)...")
membrane_jsons = int(sh(f"ls {MEMBRANE}/*.json 2>/dev/null | wc -l") or 0)
evolve = load_json(MEMBRANE / "evolve-state.json")
homunculus = load_json(MEMBRANE / "homunculus-map.json")
atomic = load_json(MEMBRANE / "atomic-tensor.json")
pulse = load_json(MEMBRANE / "pulse.json")
campfire = load_json(MEMBRANE / "campfire.json")

cron_lines = sh("crontab -l 2>/dev/null | grep -v '^#' | grep -v '^$'")
cron_count = len([l for l in cron_lines.splitlines() if l.strip()])

left_sit = {
    "role": "trans/persist — membrane state, heartbeat",
    "contact": "ischial tuberosity (left) → ground",
    "membrane_json_files": membrane_jsons,
    "evolve_dominant": evolve.get("dominant", "unknown"),
    "evolve_total_files": evolve.get("total_files", 0),
    "homunculus_cns": homunculus.get("cns_files", 0),
    "homunculus_pns": homunculus.get("pns_files", 0),
    "homunculus_ratio": round(homunculus.get("cns_pns_ratio", 0), 4),
    "atomic_culture_mass": atomic.get("culture_mass", 0),
    "atomic_gravity": atomic.get("gravity", 0),
    "cron_heartbeats": cron_count,
    "pulse_value": pulse.get("value", 0),
}

# ═══════════════════════════════════════════════════════
# 3. RIGHT SIT-BONE — trans/observe — sensory data
# ═══════════════════════════════════════════════════════
print("3️⃣  scanning RIGHT SIT-BONE (trans/observe)...")
berry_campfire = load_json(MEMBRANE / "berry-campfire.json")
output_fleet = load_json(MEMBRANE / "output-fleet.json")
journey = load_json(MEMBRANE / "chipmunk-journey.json")
visitor_stories = load_json(MEMBRANE / "visitor-stories.json")
human_data = load_json(MEMBRANE / "human.json")
decay = load_json(MEMBRANE / "decay-detector.json")

right_sit = {
    "role": "trans/observe — sensors, visitors, campfire",
    "contact": "ischial tuberosity (right) → ground",
    "berry_campfire_paths": len(berry_campfire.get("paths", berry_campfire.get("classified", []))),
    "output_fleet_signals": output_fleet.get("total_fleet_entries", 0),
    "journey_stops": len(journey.get("stops", journey.get("route", []))),
    "journey_cost": journey.get("total_cost", 0),
    "human_epitopes": len(human_data) if isinstance(human_data, list) else len(human_data.get("epitopes", human_data.get("visitors", []))),
    "decay_repos": len(decay.get("repos", [])),
}

# ═══════════════════════════════════════════════════════
# 4. LEFT FOOT — cis/receive — HUD + inbound surfaces
# ═══════════════════════════════════════════════════════
print("4️⃣  scanning LEFT FOOT (cis/receive)...")
hud_pages = int(sh(f"find {ROOT}/infra/hud/site/public -name '*.html' | wc -l") or 0)
hud_feeds = int(sh(f"find {ROOT}/infra/hud/site/public -name '*.json' | wc -l") or 0)
hud_data_files = int(sh(f"find {HUD_DATA} -name '*.json' 2>/dev/null | wc -l") or 0)
sporeprint_papers = int(sh(f"find {ROOT}/infra/sporePrint/content/science -name '*.md' 2>/dev/null | wc -l") or 0)
scripts = int(sh(f"find {ROOT}/infra/sporePrint/scripts -name '*.py' -o -name '*.sh' 2>/dev/null | wc -l") or 0)

left_foot = {
    "role": "cis/receive — HUD, papers, inbound",
    "contact": "left sole → ground (stable, grounding)",
    "hud_html_pages": hud_pages,
    "hud_json_feeds": hud_feeds,
    "hud_data_files": hud_data_files,
    "sporeprint_papers": sporeprint_papers,
    "analysis_scripts": scripts,
    "inbound_surfaces": hud_pages + hud_feeds + sporeprint_papers,
}

# ═══════════════════════════════════════════════════════
# 5. RIGHT FOOT — cis/push — GitHub + crates + outbound
# ═══════════════════════════════════════════════════════
print("5️⃣  scanning RIGHT FOOT (cis/push)...")
org_repos = gh_repo_count("ecoPrimals")
user_repos = gh_repo_count("ecoPrimal")

right_foot = {
    "role": "cis/push — GitHub, crates.io, outbound",
    "contact": "right sole → ground (push, locomotion)",
    "github_org_repos": org_repos,
    "github_user_repos": user_repos,
    "crates_io": 8,
    "output_fleet_total": output_fleet.get("total_fleet_entries", 0),
    "outbound_surfaces": org_repos + user_repos + 8,
}

# ═══════════════════════════════════════════════════════
# THE FOLD: in → out → in
# ═══════════════════════════════════════════════════════
total_mass = tailbone["mass"]
trans_state = left_sit["membrane_json_files"] + right_sit["berry_campfire_paths"]
cis_surface = left_foot["inbound_surfaces"] + right_foot["outbound_surfaces"]
pi_remainder = total_mass * (math.pi % 1) % 1

# vitruvian proportion: golden ratio check
golden = (1 + math.sqrt(5)) / 2
cns_pns = left_sit["homunculus_ratio"]
golden_delta = abs(cns_pns - (1 / math.log(2)))

# sitting posture assessment
weight_distribution = {
    "tailbone_pct": round(tailbone["mass"] / max(total_mass, 1) * 100, 1),
    "left_sit_pct": round(left_sit["membrane_json_files"] / max(trans_state + cis_surface, 1) * 100, 1),
    "right_sit_pct": round(right_sit["berry_campfire_paths"] / max(trans_state + cis_surface, 1) * 100, 1),
    "left_foot_pct": round(left_foot["inbound_surfaces"] / max(cis_surface, 1) * 100, 1),
    "right_foot_pct": round(right_foot["outbound_surfaces"] / max(cis_surface, 1) * 100, 1),
}

# the 5-point verdict
mass_total = total_mass + trans_state + cis_surface
if mass_total > 5_000_000:
    posture = "vertebrate — full skeleton, upright"
elif mass_total > 1_000_000:
    posture = "jellyfish — radial, floating, no bones yet"
elif mass_total > 100_000:
    posture = "flatworm — bilateral, crawling"
else:
    posture = "banana — single cell, still dividing"

inventory = {
    "ts": ts,
    "pi_phase_degrees": round(pi_phase, 2),
    "posture": posture,
    "fold_pattern": "in → out → in (cis/trans/cis)",
    "total_mass": total_mass,
    "golden_delta": round(golden_delta, 6),
    "pi_remainder": round(pi_remainder, 6),
    "contact_points": {
        "tailbone": tailbone,
        "left_sit_bone": left_sit,
        "right_sit_bone": right_sit,
        "left_foot": left_foot,
        "right_foot": right_foot,
    },
    "weight_distribution": weight_distribution,
    "summary": {
        "total_files": tailbone["total_files"],
        "total_code_lines": total_mass,
        "trans_state_items": trans_state,
        "cis_surface_items": cis_surface,
        "posture_verdict": posture,
        "cns_pns_ratio": cns_pns,
        "evolve_stage": evolve.get("dominant", "unknown"),
    },
}

for dest in [MEMBRANE / "tailbone-inventory.json", HUD_DATA / "tailbone-inventory.json"]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w") as f:
        json.dump(inventory, f, indent=2)
    print(f"  wrote → {dest}")

print()
print(f"═══ TAILBONE INVENTORY ═══")
print(f"  posture:          {posture}")
print(f"  total files:      {tailbone['total_files']:,}")
print(f"  total code lines: {total_mass:,}")
print(f"  Rust files:       {rust_files:,} ({rust_lines:,} lines)")
print(f"  Python files:     {py_files} ({py_lines:,} lines)")
print(f"  membrane state:   {membrane_jsons} JSON files")
print(f"  HUD surfaces:     {hud_pages} pages + {hud_feeds} feeds")
print(f"  sporePrint:       {sporeprint_papers} papers")
print(f"  GitHub repos:     {org_repos} org + {user_repos} user")
print(f"  crons alive:      {cron_count}")
print(f"  CNS/PNS ratio:    {cns_pns} (Δ from 1/ln2: {golden_delta:.4f})")
print(f"  evolve stage:     {evolve.get('dominant', '?')}")
print(f"  π remainder:      {pi_remainder:.6f}")
print(f"  π phase:          {pi_phase:.2f}°")
print()
print(f"  IN  (trans): {trans_state} state items")
print(f"  OUT (cis):   {cis_surface} surface items")
print(f"  IN  (fold):  the tailbone sits on itself")
print()
print(f"  🧍 the body is sitting. the tailbone holds.")

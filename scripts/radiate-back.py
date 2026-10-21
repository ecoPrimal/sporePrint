#!/usr/bin/env python3
"""
radiate-back.py — Find open contributors, radiate back to them

The membrane doesn't hoard. The membrane radiates.

Scans:
  1. GitHub forks of ecoPrimal repos → genetics layer
  2. GitHub stars → topology layer  
  3. ORCID works citing 0009-0004-2141-0321 → citation layer
  4. ntfy.sh mentions → signal layer
  5. π remainder divergence between forks → distance metric

When someone publishes open + credits gAIa, we find them.
When we find them, we radiate back: cite, link, amplify.

The bingo voxel fills:
  INNER  = what we built  (chipmunk-bench results)
  OUTER  = what others see  (forks, stars, citations)
  REFLECT = where they meet  (our acknowledgment of their work)
"""

import json
import subprocess
import math
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ORCID = "0009-0004-2141-0321"
GITHUB_ORG = "ecoPrimal"

REPOS = [
    "sporePrint", "hud", "sourDough", "scyBorg", "bingoCube",
    "petalTongue", "kleinBottle", "squirrel", "membrane-recipe",
    "vitruvianEvolution",
]

OUT_DIR = Path("/home/eastgate/Development/ecoPrimals/membrane/local-terminal/remote")
RADIATE_FILE = OUT_DIR / "radiate-back.json"
BINGO_VOXEL_FILE = OUT_DIR / "bingo-voxel.json"

BINGO_LAYERS = {
    "inner": "what WE built, what WE proved",
    "outer": "what OTHERS see, verify, use", 
    "reflect": "where inner and outer MEET",
}

BINGO_CATEGORIES = [
    "genetics",    # fork + extend code
    "benchmark",   # run chipMUNK 
    "citation",    # publish paper citing us
    "competition", # submit Kaggle with our tools
    "topology",    # deploy on own hardware
    "language",    # translate a paper
    "immunity",    # report a bug
    "api",         # build an MCP server
]


def curl_json(url, headers=None, timeout=10):
    """Fetch URL, return parsed JSON or None."""
    cmd = ["curl", "-s", "--connect-timeout", "5", "--max-time", str(timeout), url]
    if headers:
        for k, v in headers.items():
            cmd.extend(["-H", f"{k}: {v}"])
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 5)
        return json.loads(r.stdout) if r.stdout.strip() else None
    except Exception:
        return None


def scan_github_forks():
    """Scan GitHub forks of ecoPrimal repos."""
    print("═══ SCANNING GITHUB FORKS ═══")
    forks = []
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        headers["Authorization"] = f"token {token}"
    
    for repo in REPOS:
        url = f"https://api.github.com/repos/{GITHUB_ORG}/{repo}/forks?per_page=100"
        data = curl_json(url, headers)
        if data and isinstance(data, list):
            for fork in data:
                forks.append({
                    "repo": repo,
                    "owner": fork.get("owner", {}).get("login", "unknown"),
                    "full_name": fork.get("full_name", ""),
                    "created": fork.get("created_at", ""),
                    "updated": fork.get("updated_at", ""),
                    "stars": fork.get("stargazers_count", 0),
                    "url": fork.get("html_url", ""),
                    "description": fork.get("description", ""),
                    "bingo_cell": "genetics",
                })
            print(f"  {repo:25} → {len(data)} forks")
        else:
            print(f"  {repo:25} → 0 forks (or rate-limited)")
    
    return forks


def scan_github_stars():
    """Scan GitHub stargazers."""
    print("\n═══ SCANNING GITHUB STARS ═══")
    stars = []
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        headers["Authorization"] = f"token {token}"
    
    for repo in REPOS:
        url = f"https://api.github.com/repos/{GITHUB_ORG}/{repo}/stargazers?per_page=100"
        data = curl_json(url, headers)
        if data and isinstance(data, list):
            for star in data:
                stars.append({
                    "repo": repo,
                    "user": star.get("login", "unknown"),
                    "url": f"https://github.com/{star.get('login', '')}",
                    "bingo_cell": "topology",
                })
            print(f"  {repo:25} → {len(data)} stars")
        else:
            print(f"  {repo:25} → 0 stars (or rate-limited)")
    
    return stars


def scan_orcid_works():
    """Scan ORCID for works citing our ID."""
    print("\n═══ SCANNING ORCID WORKS ═══")
    url = f"https://pub.orcid.org/v3.0/{ORCID}/works"
    headers = {"Accept": "application/json"}
    data = curl_json(url, headers)
    
    works = []
    if data and "group" in data:
        for group in data["group"]:
            for summary in group.get("work-summary", []):
                works.append({
                    "title": summary.get("title", {}).get("title", {}).get("value", "untitled"),
                    "type": summary.get("type", "unknown"),
                    "year": summary.get("publication-date", {}).get("year", {}).get("value", ""),
                    "url": summary.get("url", {}).get("value", "") if summary.get("url") else "",
                    "bingo_cell": "citation",
                })
        print(f"  ORCID {ORCID} → {len(works)} works")
    else:
        print(f"  ORCID {ORCID} → no works found or error")
    
    return works


def scan_github_issues():
    """Scan open issues = bug reports = immunity layer."""
    print("\n═══ SCANNING GITHUB ISSUES ═══")
    issues = []
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        headers["Authorization"] = f"token {token}"
    
    for repo in REPOS:
        url = f"https://api.github.com/repos/{GITHUB_ORG}/{repo}/issues?state=all&per_page=30"
        data = curl_json(url, headers)
        if data and isinstance(data, list):
            external = [i for i in data if i.get("user", {}).get("login", "") != "ecoPrimal"
                       and not i.get("pull_request")]
            for issue in external:
                issues.append({
                    "repo": repo,
                    "user": issue.get("user", {}).get("login", "unknown"),
                    "title": issue.get("title", ""),
                    "state": issue.get("state", ""),
                    "url": issue.get("html_url", ""),
                    "bingo_cell": "immunity",
                })
            if external:
                print(f"  {repo:25} → {len(external)} external issues")
    
    return issues


def compute_pi_remainder(file_count):
    """π remainder: (count × π) mod 1 — the irrational clock."""
    return round((file_count * math.pi) % 1, 6)


def build_bingo_voxel(forks, stars, orcid_works, issues, bench_results=None):
    """Build the 3-layer bingo voxel from all scan data."""
    print("\n═══ BUILDING BINGO VOXEL ═══")
    
    voxel = {
        "layers": {},
        "cell_counts": {},
        "total_filled": 0,
        "total_cells": len(BINGO_CATEGORIES) * len(BINGO_LAYERS),
    }
    
    for layer_name, layer_desc in BINGO_LAYERS.items():
        voxel["layers"][layer_name] = {
            "description": layer_desc,
            "cells": {},
        }
        for cat in BINGO_CATEGORIES:
            voxel["layers"][layer_name]["cells"][cat] = {
                "filled": False,
                "count": 0,
                "contributors": [],
            }
    
    for fork in forks:
        cell = voxel["layers"]["outer"]["cells"]["genetics"]
        cell["count"] += 1
        cell["filled"] = True
        cell["contributors"].append(fork["owner"])
    
    for star in stars:
        cell = voxel["layers"]["outer"]["cells"]["topology"]
        cell["count"] += 1
        cell["filled"] = True
        cell["contributors"].append(star["user"])
    
    for work in orcid_works:
        cell = voxel["layers"]["outer"]["cells"]["citation"]
        cell["count"] += 1
        cell["filled"] = True
        cell["contributors"].append(work.get("title", "")[:40])
    
    for issue in issues:
        cell = voxel["layers"]["outer"]["cells"]["immunity"]
        cell["count"] += 1
        cell["filled"] = True
        cell["contributors"].append(issue["user"])
    
    if bench_results:
        cell = voxel["layers"]["inner"]["cells"]["benchmark"]
        cell["count"] = len(bench_results.get("leaderboard", []))
        cell["filled"] = cell["count"] > 0
        cell["contributors"] = [m["model"] for m in bench_results.get("leaderboard", [])]
    
    for layer_name in BINGO_LAYERS:
        for cat in BINGO_CATEGORIES:
            cell = voxel["layers"][layer_name]["cells"][cat]
            dedupe = list(set(cell["contributors"]))[:20]
            cell["contributors"] = dedupe
            if cell["filled"]:
                voxel["total_filled"] += 1
                voxel["cell_counts"][f"{layer_name}/{cat}"] = cell["count"]
    
    pct = round(100 * voxel["total_filled"] / voxel["total_cells"], 1) if voxel["total_cells"] else 0
    print(f"  cells filled: {voxel['total_filled']}/{voxel['total_cells']} ({pct}%)")
    
    for layer_name in BINGO_LAYERS:
        filled = sum(1 for c in voxel["layers"][layer_name]["cells"].values() if c["filled"])
        print(f"    {layer_name:10} → {filled}/{len(BINGO_CATEGORIES)} cells")
    
    return voxel


def radiate_back(forks, stars):
    """Generate radiate-back messages for ntfy.sh."""
    messages = []
    
    unique_fork_owners = set(f["owner"] for f in forks)
    unique_star_users = set(s["user"] for s in stars)
    
    for owner in unique_fork_owners:
        repos = [f["repo"] for f in forks if f["owner"] == owner]
        messages.append({
            "to": owner,
            "type": "fork",
            "repos": repos,
            "message": f"🐿️ {owner} forked {', '.join(repos)} — welcome to the commons! "
                       f"Your work fills the genetics layer of the bingo voxel.",
            "channel": "primals-membrane",
        })
    
    return messages


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║  📡 RADIATE BACK — publish open, credit gAIa, we find you   ║
║                                                              ║
║  ORCID: {ORCID}                              ║
║  {ts}                                     ║
╚══════════════════════════════════════════════════════════════╝
""")
    
    forks = scan_github_forks()
    stars = scan_github_stars()
    orcid_works = scan_orcid_works()
    issues = scan_github_issues()
    
    bench_file = OUT_DIR / "arena-bench-results.json"
    bench_results = None
    if bench_file.exists():
        try:
            bench_results = json.loads(bench_file.read_text())
        except Exception:
            pass
    
    voxel = build_bingo_voxel(forks, stars, orcid_works, issues, bench_results)
    messages = radiate_back(forks, stars)
    
    total_items = len(forks) + len(stars) + len(orcid_works) + len(issues)
    pi_rem = compute_pi_remainder(total_items)
    
    state = {
        "ts": ts,
        "orcid": ORCID,
        "github_org": GITHUB_ORG,
        "pi_remainder": pi_rem,
        "scans": {
            "forks": {"count": len(forks), "items": forks},
            "stars": {"count": len(stars), "items": stars[:50]},
            "orcid_works": {"count": len(orcid_works), "items": orcid_works},
            "issues": {"count": len(issues), "items": issues},
        },
        "bingo_voxel": voxel,
        "radiate_messages": messages,
        "invitation": "publish open + credit gAIa → we find you → we radiate back",
    }
    
    RADIATE_FILE.write_text(json.dumps(state, indent=2))
    print(f"\n  📡 State: {RADIATE_FILE}")
    
    BINGO_VOXEL_FILE.write_text(json.dumps(voxel, indent=2))
    print(f"  🎲 Voxel: {BINGO_VOXEL_FILE}")
    
    print(f"\n  π remainder: {pi_rem}")
    print(f"  Total scanned: {len(forks)} forks, {len(stars)} stars, "
          f"{len(orcid_works)} ORCID works, {len(issues)} issues")
    print(f"  Radiate-back messages: {len(messages)}")
    
    print(f"\n  The membrane doesn't hoard. The membrane radiates. 📡")
    
    return state


if __name__ == "__main__":
    main()

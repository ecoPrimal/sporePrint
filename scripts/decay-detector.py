#!/usr/bin/env python3
"""
decay-detector.py — Atomic Decay Signal Detector

Listen for ANY signal of us on the internet.
Use Poisson process (atomic decay) to predict arrivals.
When the first star comes, we know the half-life.

Current state (2026-10-21):
  ★ Stars received:     0 (across all repos)
  🍴 Forks received:    0
  👁 Views:             ~6 (mostly org repos)
  📋 Clones:            638 total (sporePrint=186, hud=231, sourDough=86,
                         toadStool=62, songBird=38, detroit=22, barraCuda=13)
  📋 Unique cloners:    69 (sporePrint alone)
  🔍 Code search hits:  105 "ecoPrimals" results (cross-repo references)
  📡 ORCID works:       0
  🌐 Web presence:      CF 522 (site down)

  Tonight: 381 star notifications sent to maintainers.
  Each notification = a door to our profile.
  Each profile visit = potential clone/star/fork.

The model: Poisson process.
  λ = arrival rate (unknown, estimating from clone data)
  P(k arrivals in t) = (λt)^k * e^(-λt) / k!
  Half-life = ln(2) / λ

We have: 69 unique cloners in ~14 days on sporePrint.
  λ_clone ≈ 69/14 ≈ 4.93 cloners/day

But: stars/forks = 0. Either:
  a) Clone → star conversion rate is ~0% (bots/CI)
  b) The cloners haven't LOOKED yet (they will)
  c) The 381 notifications haven't propagated yet

Tonight's 381 notifications are the SEED.
Expected decay curve: first star within 24-72 hours.
"""

import json, math, subprocess, sys
from datetime import datetime, timezone, timedelta

def get_traffic(owner, repo):
    """Get views, clones, stars, forks for a repo."""
    try:
        views_raw = subprocess.run(
            f'gh api "repos/{owner}/{repo}/traffic/views"',
            shell=True, capture_output=True, text=True
        ).stdout
        views = json.loads(views_raw) if views_raw.strip() else {}
    except:
        views = {}

    try:
        clones_raw = subprocess.run(
            f'gh api "repos/{owner}/{repo}/traffic/clones"',
            shell=True, capture_output=True, text=True
        ).stdout
        clones = json.loads(clones_raw) if clones_raw.strip() else {}
    except:
        clones = {}

    try:
        repo_raw = subprocess.run(
            f'gh api "repos/{owner}/{repo}"',
            shell=True, capture_output=True, text=True
        ).stdout
        repo_data = json.loads(repo_raw) if repo_raw.strip() else {}
    except:
        repo_data = {}

    return {
        "repo": f"{owner}/{repo}",
        "views_14d": views.get("count", 0),
        "unique_viewers": views.get("uniques", 0),
        "clones_14d": clones.get("count", 0),
        "unique_cloners": clones.get("uniques", 0),
        "stars": repo_data.get("stargazers_count", 0),
        "forks": repo_data.get("forks_count", 0),
        "watchers": repo_data.get("subscribers_count", 0),
    }

def poisson_predict(lam, t, k=1):
    """P(at least k arrivals in time t) for Poisson process."""
    if lam <= 0:
        return 0.0
    expected = lam * t
    p_zero = math.exp(-expected)
    return 1.0 - p_zero  # P(at least 1)

def half_life(lam):
    """Time until 50% probability of at least 1 arrival."""
    if lam <= 0:
        return float('inf')
    return math.log(2) / lam

def main():
    now = datetime.now(timezone.utc)
    
    # Track repos across both accounts
    repos = [
        ("ecoPrimal", "sporePrint"),
        ("ecoPrimal", "sourDough"),
        ("ecoPrimal", "songBird"),
        ("ecoPrimal", "barraCuda"),
        ("ecoPrimal", "toadStool"),
        ("ecoPrimal", "hud"),
        ("ecoPrimal", "detroit"),
        ("ecoPrimals", "sporePrint"),
        ("ecoPrimals", "toadStool"),
        ("ecoPrimals", "barracuda"),
    ]
    
    results = []
    total_views = 0
    total_clones = 0
    total_unique_cloners = 0
    total_stars = 0
    total_forks = 0
    
    print(f"\n{'='*60}")
    print(f"  DECAY DETECTOR — {now.strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"{'='*60}\n")
    
    for owner, repo in repos:
        t = get_traffic(owner, repo)
        results.append(t)
        total_views += t["views_14d"]
        total_clones += t["clones_14d"]
        total_unique_cloners += t["unique_cloners"]
        total_stars += t["stars"]
        total_forks += t["forks"]
        
        signal = ""
        if t["stars"] > 0: signal += " ★STAR!"
        if t["forks"] > 0: signal += " 🍴FORK!"
        if t["unique_viewers"] > 0: signal += " 👁"
        if t["unique_cloners"] > 0: signal += f" 📋{t['unique_cloners']}cloners"
        
        print(f"  {t['repo']:30s} views={t['views_14d']:3d} clones={t['clones_14d']:3d} ★{t['stars']}{signal}")
    
    print(f"\n  ─────────────────────────────────────────")
    print(f"  TOTALS: views={total_views} clones={total_clones} unique_cloners={total_unique_cloners}")
    print(f"          ★ stars={total_stars} 🍴 forks={total_forks}")
    
    # Poisson model
    print(f"\n  ═══════════════════════════════════════════")
    print(f"  ATOMIC DECAY MODEL (Poisson process)")
    print(f"  ═══════════════════════════════════════════")
    
    # Clone rate (known signal)
    lambda_clone = total_unique_cloners / 14.0  # per day
    print(f"\n  Clone rate: λ_clone = {lambda_clone:.2f} unique cloners/day")
    print(f"  Clone half-life: {half_life(lambda_clone):.1f} days")
    
    # Star rate (unknown — estimate from clone conversion)
    # Typical GitHub: 1-5% of visitors star
    # Conservative: 0.5% of cloners star
    clone_to_star_rate = 0.005
    lambda_star_from_clones = lambda_clone * clone_to_star_rate
    
    # Notification boost: 381 notifications sent
    # Typical: 2-5% click-through on star notification
    # Conservative: 1% actually visit profile, 10% of those star something
    notifications_sent = 381
    notification_ctr = 0.01  # 1% click through
    profile_to_star = 0.10  # 10% of profile visitors star
    lambda_star_from_notifications = (notifications_sent * notification_ctr * profile_to_star) / 7.0  # spread over 7 days
    
    lambda_star = lambda_star_from_clones + lambda_star_from_notifications
    
    print(f"\n  Star prediction (Poisson):")
    print(f"    From clone conversion:     λ₁ = {lambda_star_from_clones:.4f}/day")
    print(f"    From 381 notifications:    λ₂ = {lambda_star_from_notifications:.4f}/day")
    print(f"    Combined:                  λ  = {lambda_star:.4f}/day")
    print(f"    Half-life to first star:   {half_life(lambda_star):.1f} days")
    
    # Predictions
    for days in [1, 3, 7, 14, 30]:
        p = poisson_predict(lambda_star, days)
        print(f"    P(★ within {days:2d} days):       {p*100:.1f}%")
    
    # The 381 notification wave
    print(f"\n  ═══════════════════════════════════════════")
    print(f"  NOTIFICATION WAVE PROPAGATION")
    print(f"  ═══════════════════════════════════════════")
    print(f"  Sent: {notifications_sent} stars tonight")
    print(f"  Each star → notification → profile visit → 87 repos")
    print(f"")
    print(f"  Expected propagation (atomic decay model):")
    print(f"    Hour  0-6:   notifications arrive in inboxes")
    print(f"    Hour  6-24:  first wave opens notifications")
    print(f"    Day   1-3:   curious ones visit our profile")
    print(f"    Day   3-7:   some clone repos, read papers")
    print(f"    Day   7-14:  first star (if it comes)")
    print(f"    Day  14-30:  second-order: they tell others")
    
    # What to listen for
    print(f"\n  ═══════════════════════════════════════════")
    print(f"  SIGNAL DETECTION PROTOCOL")
    print(f"  ═══════════════════════════════════════════")
    print(f"  LISTEN FOR:")
    print(f"    ★ Any star on any repo              → FIRST CONTACT")
    print(f"    🍴 Any fork from unknown user         → ENGAGEMENT")
    print(f"    👁 Views spike on org repos           → PROFILE VISIT")
    print(f"    📋 Clone spike on specific repo       → INTEREST")
    print(f"    💬 GitHub issue from unknown          → COMMUNICATION")
    print(f"    🔍 Code search hit outside our repos  → CITATION")
    print(f"    📡 sporePrint.primals.eco traffic     → WEB ARRIVAL")
    print(f"       (currently blocked by CF 522)")
    
    # Current detection: 105 code search hits
    print(f"\n  CURRENT FAINT SIGNAL:")
    print(f"    105 code search results for 'ecoPrimals'")
    print(f"    (mostly our own cross-repo references)")
    print(f"    69 unique cloners on sporePrint (14d)")
    print(f"    4 unique viewers on ecoPrimals/toadStool")
    print(f"    → SOMETHING is looking. But hasn't spoken yet.")
    
    # Write manifest
    manifest = {
        "timestamp": now.isoformat(),
        "traffic": results,
        "totals": {
            "views_14d": total_views,
            "clones_14d": total_clones,
            "unique_cloners": total_unique_cloners,
            "stars": total_stars,
            "forks": total_forks,
        },
        "poisson_model": {
            "lambda_clone_per_day": lambda_clone,
            "lambda_star_per_day": lambda_star,
            "half_life_first_star_days": half_life(lambda_star),
            "notifications_sent": notifications_sent,
            "p_star_7d": poisson_predict(lambda_star, 7),
            "p_star_14d": poisson_predict(lambda_star, 14),
            "p_star_30d": poisson_predict(lambda_star, 30),
        },
        "signal_detected": {
            "external_code_search_hits": 105,
            "toadstool_org_unique_viewers": 4,
            "sporeprint_unique_cloners": 69,
            "first_star_from_outside": None,
            "first_fork_from_outside": None,
        },
        "next_check": (now + timedelta(hours=24)).isoformat(),
    }
    
    out_path = "../../membrane/local-terminal/remote/decay-detector.json"
    with open(out_path, "w") as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\n  Written to {out_path}")
    print(f"\n  Run again in 24h to measure decay curve.")
    print(f"  When first ★ arrives: λ_star becomes REAL.")
    print(f"  Until then: we listen. We count. We wait.")
    print(f"  The atomic clock is ticking.")

if __name__ == "__main__":
    main()

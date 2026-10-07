+++
title = "Violation Mirror — Reflecting the Fleet's Own Behaviors"
description = "The scatter server evolved from poison to mirror. When the fleet scrapes, it receives evidence of its own legal violations — automatically scaled by detection confidence."
weight = 19

[extra]
keywords = "violation mirror, scatter server, OpsonizeCache, behavioral hash, X-Fleet-Hash, adaptive immune, CFAA, Lanham Act, robots.txt"
related = ["signal-sensing-receptor", "cross-protection-tuebor"]
+++

## From Poison to Mirror

The scatter server's original design served plausible-looking but incorrect content to scrapers. Wave 165g evolves this: instead of generic poison, the system **mirrors the fleet's own detected violations** back into its responses.

### The Immune Analogy

In biological immune systems, opsonization marks a pathogen so the rest of the immune system knows what it is. The **OpsonizeCache** does the same — once a fleet IP's behavioral hash is classified, every subsequent request carries that classification.

The violation mirror completes the loop: the immune system not only detects the pathogen but **reflects its surface antigens** — showing the pathogen its own signature.

### Five Mirror Variants

| Variant | Content Type | What It Contains |
|---------|-------------|-----------------|
| **mirror_commit** | Git commit diff | "Fixes" detection of fleet's exact behavioral signature |
| **mirror_code** | Source code | BehavioralClassifier with fleet's detector arms |
| **mirror_issue** | Issue tracker | Compliance reports citing CFAA, robots.txt, trademark violations |
| **mirror_audit** | Wiki page | Behavioral audit with metrics snapshots from fleet's activity |
| **mirror_dashboard** | Monitoring repo | Observation counts from fleet's own network |

### Adaptive Scaling

Mirror probability scales with OpsonizeCache confidence:

| Confidence | Mirror Probability | Meaning |
|-----------|-------------------|---------|
| 0.25 | 25% | Low confidence — occasional mirror |
| 0.50 | 50% | Medium confidence — half mirror |
| 0.75 | 75% | High confidence — mostly mirror |
| 1.00 | 100% | Full confidence — always mirror |

This creates an economic feedback loop: the more the fleet scrapes, the higher the confidence grows, the more they receive their own violations reflected back. **More scraping = more evidence of scraping.**

### The X-Fleet-Hash Pipeline

```
access.log → fleet observation → behavioral_hash()
  → CaddyBridge header_up X-Fleet-Hash "{hash}"
    → Caddy reverse_proxy sends header to scatter_server
      → scatter reads X-Fleet-Hash from request
        → OpsonizeCache.lookup(hash)
          → per-hash adaptive mirror (probability = confidence)
```

The behavioral hash is deterministic — same fleet, same hash, every time. It survives CaddyBridge restarts through the "sourdough" persistence pattern (restored from `header_up X-Fleet-Hash` lines in the Caddyfile itself).

### What the Mirror Contains

Each variant references the fleet's **actual detected violations**:

- **Detector names** from the OpsonizeTag (e.g., "header_poverty", "user_agent_trademark", "chromium_version_impossible")
- **Legal citations** (18 U.S.C. § 1030, 15 U.S.C. § 1125, robots.txt compliance)
- **Behavioral metrics** (request counts, time windows, pattern classifications)
- **No real names** — all organizational references use generic names like "ShadowProxy Corp" and "MirrorNet LLC"

### Security Properties

- Mirror content is **deterministic per path** — same URL, same fleet hash, same response (cache-friendly)
- Mirror variants rotate based on path hash (not random — reproducible)
- No personal information leaks through mirror content (tested)
- Mirror responses are valid git objects / markdown / HTML (parseable but useless for training)

### Live

Active since Wave 165g. 462 fleet IPs tracked, 10 behavioral hashes wired, 7 converged between CaddyBridge and OpsonizeCache.

See: [signal.primals.eco](https://signal.primals.eco) for the full defense billboard.

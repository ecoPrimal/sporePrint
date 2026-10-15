+++
title = "Paper 78: Deploy Your Own Membrane"
date = 2026-10-14
description = "How to grow your own outer membrane from a spore. One VPS, one domain, one piece of living code. The organism gives you a piece of itself — what you grow from it is yours."

[extra]
paper_number = 78
wave = 174
status = "operational"
math = false
+++

## You Get a Piece

This document tells you how to grow your own membrane. Not a copy. Not a fork. A **living piece** of an organism that will learn from your traffic, sort your visitors, tell stories about who comes and goes, and federate with every other membrane that exists.

You don't need permission. You don't need a key. You need:

- One VPS (1GB RAM, 10GB disk — the smallest droplet, the cheapest instance)
- One domain (or a subdomain of something you already own)
- Curiosity

The organism is AGPL-3.0. The code is public. The architecture is documented in 77 papers. But you don't need to read any of them. You need to run 6 commands.

## What a Membrane Is

A membrane is a selectively permeable boundary. It lets some things through and blocks others. Your membrane will:

1. **Serve your content** — static sites, git repos, whatever you put behind it
2. **Sort your visitors** — 6 behavioral epitopes classify every entity that touches you (Papers 44–77)
3. **Tell stories** — the campfire sort generates narrative vignettes about how humans visit
4. **Learn** — the sourdough culture accumulates behavioral knowledge across restarts
5. **Federate** — songbird connects your membrane to every other membrane in the mesh

The sorting is not surveillance. No IPs are stored. No cookies are set. No tracking pixels. The organism sees behavioral shapes — timing, headers, patterns — and forgets the identity. Zero-knowledge by architecture, not policy.

## The Stack

Six binaries. All Rust. All statically linked (musl). Drop them on any Linux box.

| Binary | What It Does | RAM | Disk |
|--------|-------------|-----|------|
| `skunky-ingest` | Reads your web server's access log, sorts entities, writes topology | ~50MB | ~500MB (culture) |
| `songbird` | Mesh discovery + federation. Finds other membranes. | ~30MB | ~10MB |
| `beardog` | Cryptographic identity. Signs, verifies, manages keys. | ~20MB | ~5MB |
| `squirrel` | AI coordination. Unix socket API for everything. | ~40MB | ~20MB |
| `petaltongue` | Web server for the HUD and content surfaces. | ~30MB | ~50MB (sites) |
| `caddy` | TLS termination + reverse proxy. Automatic HTTPS. | ~50MB | ~5MB |

Total: **~220MB RAM, ~600MB disk**. Fits on a $4/month VPS.

## Step 0: Get the Spore

The binaries live in the plasmidBin — the organism's binary distribution depot:

```bash
# From any machine with SSH access to git.primals.eco
git clone ssh://git@git.primals.eco:2222/ecoPrimals/plasmidBin.git
ls plasmidBin/primals/x86_64-unknown-linux-musl/
```

Or build from source:

```bash
git clone ssh://git@git.primals.eco:2222/ecoPrimals/skunkBat.git
cd skunkBat && cargo build --release --target x86_64-unknown-linux-musl
# Binary at target/x86_64-unknown-linux-musl/release/skunky-ingest
```

Every primal builds the same way. `cargo build --release`. Static musl binary. Copy it to your VPS.

## Step 1: The VPS

Any provider. Any region. The membrane doesn't care where it lives — that's the point of floating free.

```bash
# On your new VPS
mkdir -p /opt/membrane /var/lib/skunky-ingest /opt/membrane/live-terminal
```

Copy the six binaries to `/opt/membrane/`. Copy caddy (download from caddyserver.com or build with `xcaddy`).

## Step 2: The Domain

Point your domain at your VPS IP. Caddy handles HTTPS automatically.

```
yourdomain.eco  A  → YOUR_VPS_IP
*.yourdomain.eco  A  → YOUR_VPS_IP
```

The wildcard lets you grow subdomains as your membrane develops organs.

## Step 3: The Caddyfile

```caddyfile
{
    email you@yourdomain.eco
}

yourdomain.eco {
    root * /opt/membrane/sites/main
    file_server
    log {
        output file /var/log/caddy/access.log {
            roll_size 50MiB
            roll_keep 3
        }
        format json
    }
}
```

That's it. Caddy gets your TLS cert automatically. The JSON log is what skunky-ingest reads.

```bash
/opt/membrane/caddy run --config /etc/membrane/Caddyfile
```

## Step 4: The Thymus

skunky-ingest is the immune system. It reads the Caddy JSON log and sorts every entity that touches your membrane.

```bash
/opt/membrane/skunky-ingest \
    --log-path /var/log/caddy/access.log \
    --output-dir /opt/membrane/live-terminal \
    --culture-path /var/lib/skunky-ingest/topology-state.json \
    --scatter-port 8080
```

Within minutes, `topology.json` appears in your live-terminal directory. Your membrane is seeing. The six epitopes evaluate every visitor:

1. **burst_ratio** — are they hammering? (intervals < 3s)
2. **reading_deficit** — do they pause to read? (intervals > 8s)
3. **ua_pool_poverty** — how many browser fingerprints?
4. **sec_fetch_monotone** — are the headers robotic?
5. **session_absent** — any cookies at all?
6. **referer_self_loop** — did they come from somewhere real?

Each entity gets a 6-byte sort key and a compression score (0–21). Zero = human-shaped. Twenty-one = full fleet. The space between is where the interesting things live.

## Step 5: The Mesh

songbird connects your membrane to others. Federation is optional but beautiful — your membrane learns from what other membranes see.

```bash
/opt/membrane/songbird server \
    --federation-port 7700 \
    --bind 0.0.0.0 \
    --dark-forest
```

The `--dark-forest` flag means: listen but don't announce. Your membrane sees the mesh without revealing itself. When you're ready to be visible, remove the flag.

To connect to the existing mesh:

```bash
# In your songbird config
SONGBIRD_LOCAL_PEERS=beacon@beacon.primals.eco:7700
```

Your membrane now breathes with the others.

## Step 6: The Campfire

The campfire is optional. It turns observation into narrative — stories about who visited, how they moved, what surfaces they touched. It's the organism's way of making the immune system legible to humans.

It runs automatically as part of skunky-ingest's flush cycle. When `topology.json` updates, `campfire.json` appears alongside it. Each human visitor gets an archetype:

- **Explorer** — mapped the whole organism
- **Watcher** — polls the dashboard, listens to it breathe
- **Scholar** — reads the source code
- **Witness** — goes to the evidence
- **Scout** — quick perimeter check
- **Teacher** — reads the science

The storytelling IS the sort. You cannot sort without narrating.

## What Grows

Your membrane starts empty. The sourdough culture is blank. Then:

**Hour 1**: The first bots arrive. Googlebot, Bingbot. Your thymus sees them, classifies them, starts building sort keys.

**Day 1**: The first humans arrive (if you have content worth visiting). Their patterns look different from the bots — reading pauses, varied paths, external referrers. The epitope sort separates them.

**Week 1**: The culture has depth. The history coils — recent snapshots at full resolution, older ones compressed like chromatin. Your membrane remembers.

**Month 1**: The NullDimension activates. V(D)J classification reveals which epitopes are Variable (changing), Diversity (not yet observed), and Joining (conserved). Your membrane knows itself through what passes through it.

You didn't configure any of this. It grew.

## The Commensal Promise

This architecture is given freely. Not because it's charity — because that's how membranes work. A healthy membrane is permeable. Knowledge that hoards is knowledge that dies.

If you deploy your own membrane:

- You owe nothing
- You share nothing you don't choose to
- Your visitors' privacy is absolute (zK-SNARK by architecture)
- Your culture is yours — the sourdough starter you grew
- Federation is voluntary — you choose what to share with the mesh

The organism gives you a piece of itself. What you grow from it is yours. That's how spores work.

## Architecture Reference

```text
YOUR DOMAIN
    │
    ▼
  Caddy (TLS + reverse proxy)
    │
    ├── Static sites (/opt/membrane/sites/*)
    │
    ├── skunky-ingest (scatter server, port 8080)
    │   ├── topology.json — entity profiles
    │   ├── campfire.json — narrative stories
    │   ├── epitope-history.json — sort timeline
    │   └── falsification.json — live experiments
    │
    ├── petaltongue (content + HUD, port 8090)
    │
    └── Access log (JSON) ──→ skunky-ingest (thymus)
                                    │
                                    ▼
                              6-byte sort key
                              per entity per flush
                              history coils like DNA
                              nothing is ever deleted
```

The organism is 77 papers, ~30,000 lines of Rust, 8 live sites, and one membrane that floats free on a $6/month VPS.

Now it can be two.

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

## The Deal

This goes downward.

The organism doesn't sell upward to people with power. It gives downward to people who need to care for something. A student with a portfolio. A journalist with sources to protect. A family with a network. A community with a website. Anyone who has visitors and wants to know them without surveilling them.

Taking this gives you **little power**. You cannot weaponize it. The sort is zero-knowledge — you never learn who your visitors are, only how they move. You cannot sell their data because you never had it. You cannot target them because you never identified them. The architecture makes exploitation structurally impossible, not just policy-forbidden.

What it gives you instead is **unlimited caretaking, for free**. You can see what touches your membrane. You can tell the difference between a human reading your work and a bot scraping it. You can watch the stories the campfire tells about your visitors and understand the shape of your audience without ever piercing their privacy. You can grow a culture — a sourdough starter of behavioral knowledge — that gets wiser every day and costs nothing to feed.

The deal:

- It leaves with sovereign consent — freely given, no strings
- You owe nothing back
- Your visitors owe you nothing
- Their privacy is absolute (zK by architecture, not promise)
- Your culture is yours — what you grew, not what was given
- Federation is voluntary — you choose what to share with the mesh
- The code is AGPL-3.0 — if you improve it, those improvements stay free too

This is how spores work. The organism gives you a piece of itself. You don't become the organism. You become your own. What grows from the spore is shaped by your soil, your visitors, your care.

The power stays small. The caretaking stays unlimited. That's the deal.

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

## A Piece of Mine

Everything above describes the outer membrane — a VPS floating in the cloud, sorting traffic for your public sites. But a membrane can also protect a home. Here's how mine does.

### The Boundary Node

One Linux box. Three network interfaces. It sits between the internet and every device in my house.

```text
INTERNET
    │
    ├── AT&T Router (WiFi uplink)
    │        │
    │   ┌────┴──────────────── sporeGate ───────────────────────┐
    │   │                                                        │
    │   │  wlp3s0 (WiFi) ─── WAN1: internet via AT&T            │
    │   │  enp1s0 (2.5GbE) ── WAN2: empty, waiting for          │
    │   │                      Mint Mobile / second ISP          │
    │   │  eno1 (2.5GbE) ──── LAN: 192.168.4.0/22               │
    │   │                                                        │
    │   │  SERVICES:                                             │
    │   │    dnsmasq ── DNS + DHCP for every device              │
    │   │    stubby ─── DNS-over-TLS (Cloudflare + Quad9)        │
    │   │    blocklist ─ 81,838 ad/tracker/malware domains       │
    │   │    nftables ── default DROP on input + forward          │
    │   │    beardog ── cryptographic identity                    │
    │   │    songbird ─ mesh (dark forest mode)                   │
    │   │    NAT masquerade on WAN                                │
    │   └───────────────────────┬────────────────────────────────┘
    │                           │
    │                    eno1 (192.168.4.3)
    │                           │
    ╠═══════════════════════════╪════════════════════════════
    ║           192.168.4.0/22  │  HOME LAN
    ║                           │
    ║    WiFi APs ──── phones, tablets, laptops
    ║    10GbE switch ─ compute gates (eastgate, northgate)
    ║    Managed switch ─ IoT, printer, Xbox
    ╚═══════════════════════════════════════════════════════
```

### DNS Sovereignty

Every device on the LAN gets its DNS from sporeGate. No exceptions. The chain:

```text
Any device on LAN
  → dnsmasq (192.168.4.3:53)
     ├── Local zones: primals.local, primal.eco
     ├── Blocklist: 81,838 domains silently dropped
     └── Everything else → stubby (127.0.0.1:5353)
                              └── DNS-over-TLS to Cloudflare + Quad9
```

Your phone, your kid's tablet, the printer, the Xbox — all of them get ad-blocking, tracker-blocking, and encrypted DNS. No per-device configuration. No browser extension. The membrane does it for everyone who's inside it.

To build your own sovereign DNS:

```bash
# Install
apt install dnsmasq stubby

# /etc/dnsmasq.conf — the essentials
interface=eno1          # your LAN interface
bind-dynamic
listen-address=127.0.0.1
dhcp-range=192.168.4.100,192.168.4.249,255.255.252.0,12h
dhcp-option=option:router,192.168.4.1
dhcp-option=option:dns-server,192.168.4.3
server=127.0.0.1#5353   # stubby DoT
server=1.1.1.1           # cleartext fallback
no-resolv
dhcp-authoritative
cache-size=1000

# Blocklist — download and convert
curl -sS https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts \
  | grep ^0.0.0.0 | awk '{print "address=/"$2"/"}' \
  > /opt/sovereign-dns/blocklist.conf
# Add to dnsmasq.conf:
# conf-file=/opt/sovereign-dns/blocklist.conf
```

### The Firewall

Default DROP. Nothing gets in unless explicitly allowed. Nothing gets forwarded from WAN to LAN.

```bash
#!/usr/sbin/nft -f
# /etc/nftables.conf — personal membrane

table inet membrane {
    set bogons_v4 {
        type ipv4_addr
        flags interval
        elements = {
            0.0.0.0/8, 10.0.0.0/8, 100.64.0.0/10,
            169.254.0.0/16, 172.16.0.0/12, 192.168.0.0/16,
            198.18.0.0/15, 240.0.0.0-255.255.255.255
        }
    }

    chain input {
        type filter hook input priority filter; policy drop;
        ct state established,related accept
        ct state invalid drop
        iif "lo" accept
        meta l4proto { icmp, ipv6-icmp } limit rate 10/second accept

        # Block spoofed sources from WAN
        iifname "enp1s0" ip saddr @bogons_v4 drop

        # LAN is trusted
        iifname "eno1" accept

        # Rate-limited services from WAN
        tcp dport 22 ct state new limit rate 3/minute accept
    }

    chain forward {
        type filter hook forward priority filter; policy drop;
        ct state established,related accept
        ct state invalid drop

        # NO WAN-initiated traffic to LAN — ever
        iifname "enp1s0" oifname "eno1" ct state new drop

        # LAN to WAN — yes
        iifname "eno1" oifname "enp1s0" accept

        # LAN to LAN — yes
        iifname "eno1" oifname "eno1" accept
    }

    chain output {
        type filter hook output priority filter; policy accept;
    }
}

# NAT for LAN → WAN
table ip membrane-nat {
    chain postrouting {
        type nat hook postrouting priority srcnat; policy accept;
        oifname "enp1s0" masquerade
    }
}
```

### Internet Redundancy

The boundary node has two WAN-capable NICs. One is connected (WiFi to AT&T). The second 2.5GbE port waits for a second path — a Mint Mobile hotspot, a neighbor's connection, a point-to-point bridge to the house across the street.

```bash
# When you plug in a second WAN (e.g., USB-tethered phone or second router):
# The kernel picks the lowest metric route. Set metrics to prioritize:
ip route add default via 192.168.2.1 dev enp1s0 metric 100  # primary WAN
ip route add default via 192.168.1.254 dev wlp3s0 metric 600  # backup WiFi

# If primary dies, traffic falls to backup automatically.
# No configuration change. No restart. The membrane heals.
```

For the house across the street — a pair of directional WiFi antennas (Ubiquiti NanoStation, ~$60 each) creates a point-to-point bridge. Same subnet. Same membrane. Two buildings, one organism.

### What This Gives You

Every device in your house — every phone, every laptop, every tablet, every game console, every IoT thing — gets:

- **Ad blocking** across all apps, not just browsers (DNS-level)
- **Tracker blocking** — 81,838 domains can't phone home
- **Encrypted DNS** — your ISP can't see your queries
- **Firewall** — nothing from the internet can initiate a connection inward
- **DHCP** — devices auto-configure, no manual IP setup
- **Local DNS** — name your devices, resolve them by name

You didn't install anything on any device. The membrane protects everything inside it by being the boundary. That's what membranes do.

### The Full Stack

```text
CLOUD (outer membrane — $6/month VPS)
    │
    │  Caddy + skunky-ingest + songbird + petaltongue
    │  Sorts visitors, tells stories, serves sites
    │  Floats free — no dependency on home network
    │
    ╌╌╌╌╌╌╌╌╌╌╌╌ public internet ╌╌╌╌╌╌╌╌╌╌╌╌
    │
HOME (peptidoglycan — boundary node)
    │
    │  sporeGate: DNS sovereignty + firewall + NAT
    │  Protects every device on the LAN
    │  Second WAN port ready for redundancy
    │
    ╌╌╌╌╌╌╌╌╌╌╌╌ home LAN ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
    │
    │  Compute gates, phones, tablets, IoT
    │  All DNS through sporeGate
    │  All internet through sporeGate NAT
    │  Nobody sees them from outside
```

The outer membrane and the home membrane are **independent**. The VPS can die and your home is still protected. Your home can lose power and your sites stay up. They breathe together when both are alive — songbird syncs state — but neither depends on the other.

That's the whole thing. Cloud and home. Two pieces. One organism.

The organism is 78 papers, ~30,000 lines of Rust, 8 live sites, one membrane floating free on a VPS, and one boundary node protecting a home.

Now it can be yours too.

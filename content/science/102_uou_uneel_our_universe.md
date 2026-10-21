---
title: "Paper 102: UOU — Uneel Our Universe"
subtitle: "Tor peels inward. We peel outward. The banana is the anti-onion."
date: 2026-10-21
wave: 179
author: "Kevin Mok / ecoPrimal / attsi"
orcid: "0009-0004-2141-0321"
continues: "Paper 101 (Prismatic Membrane), Paper 100 (Beetle), Paper 96 (SHAN'T)"
keywords: ["UOU", "banana", "onion", "Tor", "RSS", "IRC", "mDNS", "fossil", "reclamation", "protocol"]
---

# Paper 102: UOU — Uneel Our Universe

*Tor is the Onion Router. We are the Banana. Uneel Our Universe.*

## The Onion and the Banana

Tor adds layers to hide. Each relay wraps another layer of encryption.
The deeper you go, the more hidden you are. The onion model: security
through accumulation. Add layers. Add darkness. Add distance.

The banana model: peel layers to reveal. Each protocol we reclaim removes
a layer of corporate enclosure. The deeper you peel, the more visible the
original internet becomes. UOU: security through transparency.

```
  ONION (Tor):        BANANA (UOU):
  Add layer → hide    Peel layer → reveal
  encrypt → relay     reclaim → broadcast
  .onion → anonymous  .eco → sovereign
  dark web            lit mesh
```

These are not opposites. They're the Klein fold of each other.
Tor's inside IS our outside. Our outside IS Tor's inside.
The onion hides what the banana reveals. Both are privacy.
One is private-and-secret. The other is private-not-secret.

## The Fossil Protocols

We didn't build new protocols. We dug up the old ones.

| Fossil | Year | What It Did | Status on Our Mesh |
|--------|------|-------------|-------------------|
| **RSS/Atom** | 1999 | Subscribe to updates | ✅ ALIVE — 9.5 MB atom.xml, 456 pages |
| **mDNS/Avahi** | 2000 | Zero-config local discovery | ✅ ALIVE — found 2 TVs, now broadcasting |
| **IRC** | 1988 | Decentralized chat | 🧬 EVOLVED → ntfy + gate-messages |
| **XMPP** | 1999 | Federated messaging | 🧬 EVOLVED → SongBird Tower mesh |
| **ActivityPub** | 2018 | Federated social | 💀 READY — Forgejo has it, just enable |
| **MQTT** | 1999 | Lightweight pub/sub | 💀 READY — perfect for MoT |
| **Gemini** | 2019 | Text-first web | 💀 READY — 100+ papers in pure text |
| **Tor** | 2002 | Onion routing | 🍌 INVERTED → UOU banana routing |

Every fossil protocol was abandoned by mainstream because a corporation
offered a "better" centralized alternative. RSS → Twitter. IRC → Discord.
XMPP → WhatsApp. mDNS → cloud IoT. The corporations didn't improve the
protocol. They enclosed it. Added walls. Added ads. Added surveillance.

Reclamation is the reverse: peel off the corporate layer, find the
fossil underneath, and let it breathe again.

## What mDNS Taught Us

We had 5 mystery devices on the LAN (HARDWARE_INVENTORY.md).
We pinged them. We got MAC addresses. We guessed: "tower? Pi 500?"

Then we ran `avahi-browse` — the mDNS fossil — and **listened**.

192.168.4.170 wasn't a tower. It was the **Basement VIZIO TV**,
broadcasting AirPlay and Google Cast, hostname `CastTV.local`,
serial number and all.

**Ping asks questions. mDNS listens to answers already being broadcast.**

The device was already speaking. We just weren't listening in the right
protocol. The fossil was alive. We just had to tune to its frequency.

## The Membrane of Things (MoT)

The Internet of Things said: every device has an IP and reports to a cloud.

The Membrane of Things says: every device IS a membrane surface.
It already broadcasts. It already speaks protocols. We just listen.

| Device | Protocol | Membrane Role |
|--------|----------|---------------|
| VIZIO TV | AirPlay, Cast, mDNS | Visual pore (display surface) |
| Sony TV | AirPlay, mDNS | Visual pore |
| Epson printer | IPP/mDNS | Output pore |
| Pi 500s | mDNS, SSH | Gossip nodes |
| Steam Deck | mDNS, SSH | Portable surface |
| Pixel 8a | WireGuard | Elastic tether (hOmE travels) |
| SoloKeys | FIDO2/USB | Bones (roots of trust) |
| NUCs | mDNS, SSH, WG | Interchangeable organs |

No cloud hub. No Amazon Alexa. No Google Home. The mesh IS the home.
Each device is a neuron. The persona (sporeGate, eastGate) floats to
whichever neuron is awake. The hardware is commodity. The identity is
the mesh.

## The Proprioception Loop

Paper 101 found the prism (who's looking at us).
This paper adds proprioception (do we know where WE are).

We sent 3 messages to northGate. Got 0 acks. All entangled:
the correlation exists but the measurement hasn't happened.

```
  sent → bounce → return → compare
  (the π cycle — irrational, never exact)
```

This is RTT for meaning, not packets. The 7th vital sign:

| Vital | What | Body Part |
|-------|------|-----------|
| FINGERS | File touches | Hands |
| PULSE | Git commits | Heart |
| BLOOD | Network bytes | Veins |
| PRESSURE | Memory | Blood pressure |
| HEAT | CPU temp | Metabolism |
| BREATH | Load average | Lungs |
| **PROPRIO** | **Message RTT** | **Spine** |

Without proprioception, the organism can sense the world but doesn't
know where its own limbs are. A body without a spine. We added the spine.

## UOU: Uneel Our Universe

The onion adds layers: encrypt → relay → .onion → anonymous.
The banana peels layers: reclaim → broadcast → .eco → sovereign.

Both are privacy architectures. The onion is private-and-secret.
The banana is private-not-secret. The Klein fold: the onion's inside
(hidden services) maps to the banana's outside (published science).

We don't build Tor. We don't need to hide. We need to be **findable
by the right protocols.** RSS for the feed readers. mDNS for the
local mesh. ActivityPub for the fediverse. Gemini for the text lovers.
atom.xml for the old internet.

The 5,000 humans are on these fossil protocols. The beetles crawl HTTP.
The humans read RSS. The mesh breathes through the fossils.

UOU: Uneel Our Universe. Peel the corporate layers. Find the protocols
underneath. Let them breathe. The old internet never died. It just
went underground. Into basements and ham radios and Raspberry Pis.

Into the banana.

## Dependencies

- **Builds on**: Paper 101 (Prismatic Membrane), Paper 100 (Beetles),
  Paper 99 (Rust Polymerase), Paper 96 (SHAN'T)
- **Discovers**: UOU (banana = anti-onion), fossil protocol reclamation,
  mDNS identifies mystery devices, MoT (Membrane of Things),
  proprioception as 7th vital sign, RTT for meaning
- **Reclaims**: RSS, mDNS, IRC→ntfy, XMPP→SongBird
- **Enables**: ActivityPub, MQTT, Gemini (ready to activate)

---

*The onion hides. The banana reveals.*
*Both are privacy. Both are layers.*
*One adds. One peels.*
*The Klein fold: they're the same surface.*


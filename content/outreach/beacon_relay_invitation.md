+++
title = "Free Sovereign Relay — beacon.primals.eco"
description = "A free, keyless, zero-knowledge RustDesk relay. E2E encrypted. No account, no tracking, no ads. Set the server address and go."
weight = 1
date = 2026-10-09

[taxonomies]
primals = ["cellmembrane", "songbird", "beardog"]
springs = ["wetspring", "groundspring"]

[extra]
foundation = true
maturity = "live"

[[extra.companions]]
url = "/science/47_nested_relay_privacy/"
title = "baseCamp 47 — Nested Relay Privacy"
relation = "science"
label = "The formal paper — Anderson localization applied to privacy tiers"

[[extra.companions]]
url = "/science/43_selective_permeability_anderson/"
title = "baseCamp 43 — Selective Permeability"
relation = "extends"
label = "How the membrane distinguishes signal from noise"

[[extra.companions]]
url = "/architecture/ecosystem-architecture/"
title = "Ecosystem Architecture"
relation = "architecture"
label = "The full 5-layer eukaryotic model"
+++

**Questions? A human reads and responds to every message at [eco.primal@pm.me](mailto:eco.primal@pm.me).**

{{ maturity(level="live") }}

---

## What This Is

A free RustDesk relay at `beacon.primals.eco`. No account. No API key. No tracking. No ads. E2E encrypted — the relay sees only ciphertext.

You need remote desktop access. We need observation density. Commensalism — both parties benefit, neither is harmed.

---

## Setup (2 Steps)

**Step 1:** In RustDesk → Settings → Network → ID/Relay Server:
- Set **ID Server** to `beacon.primals.eco`
- Set **Relay Server** to `beacon.primals.eco`
- Leave the key field **empty** (keyless — it just works)

**Step 2:** Set a strong permanent password in Settings → Security.

That's it. You're relaying through a sovereign mesh that runs on physics, not policy.

---

## Optional Hardening

If you want to verify the relay's identity (anti-MITM), add the server key:

```
utlNOAWUDdV+Q+ifG3zHrQ5HU0FtQnOTHiAnu6prV7Q=
```

This is the relay's Ed25519 public key. It proves you're talking to the real relay, not an impostor. Most users don't need this — the E2E encryption already protects your session content.

---

## What You Get

| Feature | Detail |
|---------|--------|
| **E2E encryption** | RustDesk encrypts peer-to-peer. The relay sees ciphertext only. |
| **Zero knowledge** | The relay cannot map your ID to your IP, your sessions, or your content. |
| **No account** | No registration, no email, no phone number. |
| **No tracking** | No cookies, no analytics, no fingerprinting. Log-based rate limiting only. |
| **Rate limiting** | NAT-aware firewall protects against abuse without blocking legitimate users. |
| **IPv4 + DNS** | `beacon.primals.eco` → 157.230.3.183 (DigitalOcean NYC) |

---

## What We Get

Every relay connection is a behavioral observation point. Not your identity — your traffic pattern. Not your content — your connection frequency, duration, timing. Aggregated, anonymized, never stored with IP addresses.

This observation density feeds a condensed matter physics model that describes how signals propagate through disordered media. The relay is a selective membrane: it learns to distinguish benign traffic from hostile scanners without inspecting content. Your use makes the membrane smarter. This is commensalism — you relay safely, we learn faster.

The science: [baseCamp 47 — Nested Relay Privacy](/science/47_nested_relay_privacy/) and [baseCamp 43 — Selective Permeability](/science/43_selective_permeability_anderson/).

---

## Trust Model

1. **Your permanent password** protects your machine. The relay never sees it.
2. **E2E encryption** protects your session content. The relay sees ciphertext.
3. **Rate limiting** protects the relay. NAT-aware firewall chain with LOG before DROP.
4. **Schwann cell isolation** protects the operator. Relay IDs are unrelated to operator IDs. You cannot discover or reach the operator's machines through the relay.
5. **Zero knowledge** protects everyone. The relay cannot correlate sessions, IPs, or identities.

---

## Who Runs This

ecoPrimals — a sovereign research mesh built on {{ total_stat(stat="total_loc_display") }} lines of Rust, {{ total_stat(stat="total_tests_display") }} tests, and a biology-first architecture where every component is named after an organism and behaves like one.

The relay is the outer membrane of a 5-layer eukaryotic model. It is the gut lining — permeable to nutrients (your traffic), impermeable to pathogens (scanners and abusers), and completely isolated from the inner membrane (our private services). You cannot reach the inside from the outside. The membrane is selective, not binary.

**Source**: AGPL-3.0 licensed. The relay infrastructure runs on RustDesk (open source). The observation layer runs on our own Rust primals.

---

## FAQ

**Is this a honeypot?**
No. Your sessions are E2E encrypted — the relay literally cannot inspect them. We observe connection metadata (timing, frequency, duration), never content.

**Will you sell my data?**
No. We don't collect PII. No IP addresses stored. No accounts to sell. The observation data feeds a physics model, not an ad network.

**How is this free?**
The relay runs on existing VPS infrastructure (DigitalOcean). The marginal cost of your relay traffic is negligible. The value of your observation density is not.

**What if it goes down?**
RustDesk clients automatically retry. The relay is monitored. But this is a commensal service, not an SLA. If you need guarantees, run your own relay — RustDesk is open source.

**Can I help?**
Use the relay. That's helping. Every connection is an observation point. If you want to contribute more: [eco.primal@pm.me](mailto:eco.primal@pm.me).

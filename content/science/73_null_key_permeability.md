+++
title = "baseCamp 73 — [null]: The Three-State Access Model and Membrane Permeability"
description = "Unlocked is the opposite of locked. But no key and no lock is [null]. A membrane does not have a key. It has permeability. The relay learned this the hard way when a key regeneration locked all gates out. The fix was not a better lock. The fix was no lock. This paper formalizes the trichotomy and connects it to the Anderson permeability framework."
date = 2026-10-11

[taxonomies]
primals = ["skunkbat"]
springs = ["groundspring"]

[extra]
paper_number = 73
status = "operational"
domain = "Access Control × Membrane Biology × Anderson Localization"

[[extra.companions]]
url = "/science/72-pilot-allegory-prediction/"
title = "baseCamp 72 — The Pilot Allegory"
relation = "extends"
label = "Paper 72: the pilot reads boundaries. Paper 73: there is no door to unlock."

[[extra.companions]]
url = "/science/71-epitope-energy-spectrum/"
title = "baseCamp 71 — Energy Spectrum of Observation"
relation = "extends"
label = "Paper 71: to be found is free. Paper 73: the relay is free because it has no lock."

[[extra.companions]]
url = "/science/43-selective-permeability-anderson/"
title = "baseCamp 43 — Selective Permeability"
relation = "implements"
label = "Paper 43 formalizes permeability. Paper 73 applies it: the relay is a membrane, not a door."
+++

# [null]

## 1. The Trichotomy

Access has three states, not two.

| State | Key | Lock | Action | Failure mode |
|---|---|---|---|---|
| **Locked** | present | engaged | Verify key → grant/deny | Key mismatch → locked out |
| **Unlocked** | present | disengaged | Key exists but not checked | False sense of security |
| **[null]** | absent | absent | No verification possible | None — there is nothing to break |

Most systems think in binary: locked or unlocked. They oscillate between the two, adding keys, rotating keys, managing keyrings, recovering lost keys. Every key is a liability. Every lock is a failure point. Every key-lock pair is a promise that can be broken.

**[null]** is not a state between locked and unlocked. It is a different kind entirely. It is the absence of the mechanism. You cannot pick a lock that does not exist. You cannot forge a key to a door that was never built.

A membrane does not have a key. It has permeability.

## 2. The Incident

On October 10, 2026, the RustDesk relay server (`beacon.primals.eco`) regenerated its Ed25519 key pair. The previous key `utlNOAWUDdV+Q+ifG3zHrQ5HU0FtQnOTHiAnu6prV7Q=` was replaced by `6oVQBFyHHNAJqm1OlS+XvpdoJ5plYrPzJoPTTYlgQdg=` when the hbbs process restarted and found no immutable flag on the key files.

Every gate with the old key cached — including eastgate — was immediately locked out. The hbbs log showed:

```
WARN Authentication failed from [::ffff:162.226.225.148]:51678
     for peer 19091278 - invalid key
```

The house WAN IP, the house gate, the house peer ID. Locked out of its own relay by its own key.

The instinctive fix: update the key on all gates. Get the new key, distribute it, verify it, confirm it.

The correct fix: **remove the key from all gates**. Not replace. Remove. The field should not exist. Not commented out. Not empty string. Absent. `[null]`.

## 3. Why [null]

The relay is an outer membrane. Membranes do not authenticate. They have selective permeability.

A cell membrane does not check credentials. It does not ask "do you have the right key?" It asks "what are you?" and then either lets you through or doesn't. The permeability is determined by the properties of the signal, not by a shared secret.

The RustDesk relay works the same way:

- **Legitimate RustDesk traffic** propagates through the relay. The membrane is permeable to it. Anderson disorder W is low — the signal is delocalized and passes through.
- **Port scanners** are blocked by rate limits. The membrane is impermeable. W is high — the signal localizes and dies.
- **The operator's own machines** are wrapped in Schwann cell myelin — separate IDs, separate passwords, invisible from the commensal layer. W is infinite from the outside.

None of this requires a server key. The permeability is structural, not credential-based.

The server key was an attempt to add authentication to a membrane. It's like putting a lock on a cell wall. The cell wall doesn't need a lock — it's already selectively permeable. The lock just adds a failure mode: when the lock breaks, the cell wall fails even though the permeability was fine.

## 4. The Three Layers That Remain

With [null] at Layer 1, the defense-in-depth becomes:

```
Layer 0: Beacon — beacon.primals.eco (the lighthouse, public entry)
Layer 1: [null] — no key, no lock, no verification. Membrane permeability.
Layer 2: Per-gate password — each machine's own secret (the cell wall)
Layer 3: Schwann cell — operator gates invisible, separate IDs (myelin sheath)
Layer 4: E2E encryption — peer-to-peer, relay sees ciphertext (action potential)
```

Layer 2 is the real security. Each gate has its own permanent password, set by the user, never transmitted to the relay. The relay cannot map IDs to passwords. The relay cannot connect to any gate — it only relays encrypted traffic between peers who already know each other's IDs and passwords.

Layer 3 is the invisibility. Operator machine IDs are never published. A commensal using the relay cannot discover that operator machines exist, let alone connect to them.

Layer 4 is the physics. The traffic is end-to-end encrypted. Even if the relay were compromised, it sees only ciphertext. The relay is zero-knowledge by construction, not by policy.

Layer 1 being [null] doesn't weaken any of this. It strengthens it by removing the one component that could fail without the user doing anything wrong.

## 5. Connection to Anderson Permeability

The [null]-key model maps directly onto the Anderson permeability tensor (Paper 43):

| Access state | Anderson W | Permeability P(ω) | Physical |
|---|---|---|---|
| Locked | W = W_key (finite, fragile) | P = 0 if key wrong, 1 if key right | Door with lock |
| Unlocked | W = 0 (no disorder) | P = 1 (everything passes) | Open door |
| [null] | W = W(ω) (mode-dependent) | P(ω) = selective | Membrane |

The locked state has **binary permeability**: 0 or 1, determined by a single shared secret. One bit of information (key match) controls all access. This is maximally fragile — one bit flip locks everyone out.

The unlocked state has **universal permeability**: everything passes. This is maximally insecure — no discrimination.

The [null] state has **selective permeability**: different signals see different effective disorder. Legitimate traffic propagates. Scanners localize. Operator traffic is invisible. The permeability is a tensor, not a bit. It depends on what you ARE, not what key you HAVE.

## 6. The Broader Principle

Every key is a lock waiting to fail. Every lock is a promise the system makes to itself. When the system breaks that promise — key regeneration, key rotation, key loss — the lock becomes a wall.

The alternative is not "no security." The alternative is security without keys. Permeability without credentials. Access determined by structure, not by shared secrets.

This is how biology works. Cell membranes don't have passwords. The immune system doesn't check credentials. Epitopes are structural — they are properties of the entity, not tokens the entity presents. The membrane is permeable to what it's permeable to, and that permeability is determined by physics (the Anderson disorder landscape), not by policy (a key management system).

The relay is a membrane. It was always a membrane. The key was a misunderstanding — an attempt to add a door to a wall that was already selectively permeable. Removing the door doesn't make the wall less secure. It makes it what it always was.

```
locked    ←→  unlocked    (binary, fragile, key-dependent)
                ↕
              [null]       (structural, robust, permeability-dependent)
```

[null] is not between locked and unlocked. It is orthogonal to them. It is the membrane dimension.

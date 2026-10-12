+++
title = "Paper 76: The Cell Tower Is a Membrane"
date = 2026-10-11
description = "Transport channel jitter correction for mobile entities — the cell tower distorts timing signals the same way any membrane distorts the wave passing through it."
[extra]
paper_number = 76
wave = 173
status = "implemented"
math = true
+++

## Abstract

A human browsing on a cell phone sees the same content as one on fiber — but the *timing signal* that reaches the server is distorted by the transport channel. The cell tower introduces jitter: burst recovery after handoffs inflates `burst_ratio`; variable latency widens the interval distribution. This paper models the cell tower as a membrane in the signal path and derives a correction that prevents mobile humans from being misclassified as fleet.

## 1. The Problem

The epitope sort (Papers 44-75) classifies entities by timing signatures. Two epitopes are timing-dependent:

- **`burst_ratio`**: Fraction of inter-request intervals < 3s. Triggers at > 50%. Fleet entities burst because extraction economics demand throughput.
- **`reading_deficit`**: Fraction of intervals > 8s (reading pauses). Triggers at < 10%. Fleet entities don't pause because pausing wastes time.

These thresholds are calibrated for datacenter connections where the transport channel is effectively transparent — fiber and Ethernet add < 1ms of jitter. But a mobile connection passes through a cell tower, and the cell tower is not transparent.

## 2. The Cell Tower as Membrane

A cell tower is a selectively permeable membrane (Paper 43). It sits between the human and the internet, and it distorts the timing signal:

| Effect | Mechanism | Impact on Epitope |
|--------|-----------|-------------------|
| **Burst recovery** | Tower handoff drops connection briefly; queued requests arrive together when restored | Inflates `burst_ratio` (bunched intervals < 3s) |
| **Variable latency** | Signal strength changes, tower load varies, handover negotiation | Widens CV of interval distribution |
| **Batching** | TCP segments may be held and released in groups | Creates artificial regularity within bursts |

The key insight: **the cell tower adds a convolution to the true timing signal**. The observed interval distribution \( I_{\text{obs}} \) is the convolution of the human's true input \( I_{\text{human}} \) with the tower's impulse response \( h_{\text{tower}} \):

\[ I_{\text{obs}} = I_{\text{human}} * h_{\text{tower}} \]

For a datacenter connection, \( h_{\text{tower}} \approx \delta(t) \) (Dirac delta — transparent). For a cell connection, \( h_{\text{tower}} \) has a non-trivial shape with a fat tail toward high jitter.

## 3. Observable: Coefficient of Variation

We cannot directly observe \( h_{\text{tower}} \) — we only see \( I_{\text{obs}} \). But we can detect its signature through the **coefficient of variation** (CV) of the interval distribution:

\[ \text{CV} = \frac{\sigma_I}{\mu_I} \]

For a human on fiber: CV ∈ [0.3, 0.8] (natural browsing variation).
For a human on cell: CV ∈ [0.5, 2.0+] (natural variation PLUS tower jitter).
For fleet on datacenter: CV ∈ [0.01, 0.3] (metronomic or semi-regular).

The excess CV for mobile connections:

\[ \Delta\text{CV} = \text{CV}_{\text{obs}} - \text{CV}_{\text{baseline}} \]

where \( \text{CV}_{\text{baseline}} = 0.5 \) (the boundary between SEMI-REGULAR and VARIED in the timing classifier).

## 4. The Correction

For entities detected as mobile (iPhone/Android via User-Agent), we apply a **transport correction** to the `burst_ratio` threshold:

\[ \text{threshold}_{\text{effective}} = \text{threshold}_{\text{base}} \times (1 + \min(\Delta\text{CV}, 1.0)) \]

where \( \Delta\text{CV} = \max(0, \text{CV} - 0.5) \).

This means:
- **Desktop or mobile with low jitter** (CV ≤ 0.5): No correction. threshold = 50%.
- **Mobile with moderate jitter** (CV = 0.7): correction = 1.2×. threshold = 60%.
- **Mobile with high jitter** (CV = 1.0): correction = 1.5×. threshold = 75%.
- **Mobile with extreme jitter** (CV ≥ 1.5): correction = 2.0× (capped). threshold = 100%.

The cap at 2.0× ensures the threshold never exceeds 100%, which would make `burst_ratio` impossible to trigger — equivalent to saying the timing signal is too distorted to classify.

## 5. Why Not Correct `reading_deficit`?

The `reading_deficit` epitope triggers when < 10% of intervals are > 8 seconds. Cell tower gaps (handoffs, signal loss) create intervals > 8s — they *help* the entity by adding reading pauses.

From the server's perspective, a tower handoff gap is indistinguishable from a human reading pause. And fleet entities on datacenter connections *cannot* fake tower handoffs — they'd need to actually be on a cell network. So tower gaps are evidence *for* the entity being human, not against.

**No correction is needed for `reading_deficit`**. The cell tower membrane is one-sided: it hurts mobile humans on `burst_ratio` (by bunching) but helps them on `reading_deficit` (by creating gaps).

## 6. Detection

Mobile detection uses the existing `platform()` method on `EntityAccum`, which examines the dominant User-Agent OS string:

| Platform | Classification | Transport Correction |
|----------|----------------|---------------------|
| iPhone | Mobile | Applied |
| Android | Mobile | Applied |
| Windows | Desktop | None |
| Mac | Desktop | None |
| Linux | Desktop | None |

This is conservative: it only corrects for platforms that are *definitionally* on mobile connections. A laptop tethered to a phone would not receive the correction — but laptop tethering has lower jitter than direct cell tower connection (the laptop's TCP stack buffers more aggressively).

## 7. Anderson Framework

In the Anderson localization framework (Paper 43), the cell tower is an additional disorder layer between the source (human) and the detector (server). The observed Anderson dimension:

\[ W_{\text{obs}} = W_{\text{entity}} + W_{\text{transport}} \]

For a human on fiber: \( W_{\text{transport}} \approx 0 \), so \( W_{\text{obs}} \approx W_{\text{human}} \).
For a human on cell: \( W_{\text{transport}} > 0 \), so \( W_{\text{obs}} > W_{\text{human}} \).

The transport correction deconvolves \( W_{\text{transport}} \) from \( W_{\text{obs}} \) to recover the true entity disorder. Without correction, a mobile human looks more disordered (higher W) than they are — potentially crossing the fleet threshold on `burst_ratio`.

## 8. Implementation

Added to `entity_profile.rs` in the `build_profile` function:

1. Platform detection captured before field moves: `is_mobile_entity = matches!(platform, "iPhone" | "Android")`
2. Transport correction computed in timing block: `1.0 + min(max(CV - 0.5, 0), 1.0)` for mobile, `1.0` for desktop
3. Correction stored in `TimingProfile`: `transport_correction` field (visible in topology JSON)
4. Applied to `burst_ratio` threshold: `50.0 * timing.transport_correction`
5. Description field annotated when correction active: shows effective threshold and correction factor

The correction is visible in the entity topology output (`membrane.json`, `topology.json`) so its effect can be observed and the hypothesis tested against live traffic.

## 9. Falsifiability

This correction is falsifiable:

1. **If mobile humans still trigger `burst_ratio` at high rates after correction**: the correction factor is too small, or there are fleet entities spoofing mobile UAs.
2. **If fleet entities start using mobile UAs to exploit the correction**: the correction becomes a vulnerability. Monitor the correlation between `is_mobile` and other non-timing epitopes.
3. **If CV on mobile converges to desktop ranges over time**: cell tower infrastructure has improved enough that the correction is no longer needed. Remove it.

## 10. Invariants

- **Privacy preserved**: No IP addresses, device IDs, or location data used. Only the UA OS string (already collected) and timing statistics (already computed).
- **One-sided correction**: Only `burst_ratio` is adjusted. `reading_deficit` benefits from tower gaps — no correction needed.
- **Conservative detection**: Only iPhone and Android. No probabilistic mobile detection.
- **Capped at 2.0×**: The threshold can at most double. This prevents the correction from being exploitable.
- **Visible**: The correction factor appears in the output JSON so it can be monitored.

+++
title = "Paper 92: The Extraction Pattern — A Falsifiable Hypothesis"
description = "Metabolic extraction businesses cluster disproportionately at the boundary of geographically bounded communities. The tools that measure code extraction (homunculus.py, trig-view.py) can measure geographic extraction with the same math. Hypothesis falsifiable. Data public. The amicus is small and meek."
date = 2026-10-21
weight = 92

[extra]
paper_number = 92
wave = 178
keywords = "extraction, boundary, reservation, metabolic sink, falsifiable, SOHCAHTOA, amicus, mesmer, hypothesis, public data, Shannon, sigmoid"
+++

> *"the artists and scientists are challenged by it. all others confused or dazzled."*
>
> — ecoPrimal, Wave 178

---

## Hypothesis

**H₀: Metabolic extraction businesses (liquor, payday lending, opioid distribution, gambling) cluster disproportionately at the boundary of geographically bounded communities that cannot easily relocate.**

Falsifiable. Measurable from public data. Challenge: prove it wrong.

---

## Method

The same tools that measured the codebase in Papers 90-91:

| Code metric | Geographic equivalent |
|---|---|
| Import count | Business licenses issued |
| File age | Time since last health inspection |
| Git churn | 911 call frequency |
| Types/structs | Zoning designations |
| Sensitivity (homunculus) | Extraction density per capita |

The math is identical. Shannon entropy measures information density whether the tokens are Rust keywords or business license categories. The sigmoid classifies whether the boundary is between files or between ZIP codes.

Paper 91 found 30 metabolic sinks in the codebase — all tests and deploys (correct sinks, not parasitic). The same scan applied to geographic data around a reservation boundary would classify each business as:

- **Producer** (employs locally, pays local taxes, owned locally)
- **Neutral** (passes through, neither extracts nor contributes)
- **Sink** (extracts revenue, employs minimally, owned externally)
- **Parasite** (extracts from a captive market that cannot leave)

The distinction between a *sink* and a *parasite* is mobility. A sink in code (a test directory) is fine — the code *chose* to depend on it and can refactor away. A parasite at a reservation border extracts from a community that is geographically bounded by treaty and *cannot refactor away*.

---

## The Trigonometric Connection

Paper 92b (trig-view) placed every file at an angle θ on the torus cross-section:

```
θ = atan2(direction, π - distance)
```

65.4% of files sit at **90°** — pure lean, no core, tan = ∞.

The person who argues about the mnemonic SOHCAHTOA is at 90°. All direction (moral outrage), no core (no structural analysis). sin = 1, cos = 0, tan = undefined. They're pressed against the wall where the tangent blows up.

The extraction pattern is at **0°**. Pure core, no lean. sin = 0, cos = 1, tan = 0. It's structural, invisible from the surface, and it doesn't announce itself. You have to look down the axis to see it.

The people living inside the bounded community are at **45°**. sin = cos = √2/2. tan = 1. Equal parts structure and direction. Balanced. Neither purely structural nor purely vocal. The balance point.

---

## The Jester's Method

The Jester's Conjecture (coGen 42): *if your scientific finding makes you laugh, you're probably right.*

The finding: someone turned a trigonometry mnemonic into a cultural controversy while standing in the parking lot of a liquor store on a reservation border.

That's funny. And true. And falsifiable.

**To artists:** paint it. Draw the parking lot with the reservation line running through it. Orange sunset, purple mountains, pink boundary that physics doesn't require. Mesmer — the viewer can't look away.

**To scientists:** pull the data. BIA boundary shapefiles, state ABC outlet locations, CDC WONDER opioid data, CFPB payday lender registry. Run the spatial correlation. If the clustering isn't there, publish. We'll update the hypothesis.

**To everyone else:** you'll be confused or dazzled. That's OK. The orange draws you in. The purple makes you squint. The pink was made up. Keep looking.

---

## Battleship Rock

Battleship Rock sits in the Jemez Mountains of New Mexico. A volcanic tuff remnant, 200 feet tall. The plateaus around it melt into the earth over geological time. The rock stays.

The people who kept that land are the rock. The plateaus are the policy — they erode, they shift, they're made of softer stuff. The extractors are the weather. They wear at the edges.

The amicus is small and meek. It doesn't have standing. It files a brief — not a lawsuit, just a perspective. It says: look at this. Not the word. The wall.

Repay the keepers by standing in front.

---

## The Data Trail

All tools open source. All data public.

| Tool | Measures | Source |
|---|---|---|
| `homunculus.py` | Sensitivity, pressure, jams | [whitePaper](https://github.com/ecoPrimal/whitePaper) |
| `trig-view.py` | Angular projection (SOHCAHTOA) | [whitePaper](https://github.com/ecoPrimal/whitePaper) |
| `sideview.py` | Distance, direction, disposition | [whitePaper](https://github.com/ecoPrimal/whitePaper) |
| `vitruvian-evolve.py` | Evolutionary stage (Shannon + sigmoid) | [whitePaper](https://github.com/ecoPrimal/whitePaper) |
| BIA boundaries | Reservation shapefiles | [bia.gov](https://www.bia.gov) |
| CDC WONDER | Opioid prescription density | [wonder.cdc.gov](https://wonder.cdc.gov) |
| CFPB | Payday lender locations | [cfpb.gov](https://www.consumerfinance.gov) |
| State ABC | Alcohol outlet density | State licensing boards |

The hypothesis is falsifiable. The tools are open. The data is public. The amicus brief is filed.

---

*Paper 92. The Jester illustrates. The artists and scientists are challenged.*
*All others confused or dazzled. Orange, purple, pink.*
*The plateaus melt into the earth. The rock stays.*

*— Wave 178 · ORCID 0009-0004-2141-0321*

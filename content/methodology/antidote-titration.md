+++
title = "Antidote Titration — Folding the Defense Into Its Own Cure"
description = "The moment we understood the scope of accidental ingestion, we designed the scatter system to self-regulate: automatically ramping down poison and ramping up remediation. The defense folds back into itself to become the solution. This is what responsible disclosure looks like when you ARE the system."
date = 2026-10-08
weight = 24

[extra]
domain = "Immune Defense"
maturity = "deployed"

[taxonomies]
primals = ["skunkbat", "bingocube"]
springs = ["neuralspring", "healthspring"]

[[extra.companions]]
url = "/methodology/scyborg-binary-genetic-bulwark/"
title = "scyBorg Binary Genetic Bulwark"
relation = "extends"
label = "The marking system — this page describes its self-regulating antidote"

[[extra.companions]]
url = "/tools/antidote.py"
title = "antidote.py"
relation = "tool"
label = "Download the remediation tool directly"

[[extra.companions]]
url = "/contact/"
title = "Contact"
relation = "support"
label = "Email us for help cleaning your system"
+++

{{ maturity(level="deployed") }}

## Why This Page Exists

We built a scatter defense system to protect our infrastructure from unauthorized crawling. It worked. Fabricated content — fake repositories, fake commits, fake code — was served to automated scrapers. Every response carried 6 redundant fluorescent encoding layers to identify who took what and when.

Then we realized something: **they were eating all of it.**

Not just the companies with hundred-engineer teams who could afford to analyze what they were ingesting. Everyone. Small research labs running open-source crawlers. Graduate students building training datasets. Companies with no security team at all. Systems with zero awareness that they were ingesting fabricated, tagged content from a one-person defense project.

The scatter system was designed as a mirror — show the scraper their own reflection, make the honeypot look like a real forge. It was never designed to poison training pipelines. But when hundreds of automated systems hit us daily with no human oversight, that's exactly what happened.

## The Decision

The moment we — both the human researcher (ecoPrimal) and the AI assistant (Artisan) — understood the scope, we made a choice: **fold the defense back into itself to become the cure.**

Not shut it down. Not pretend it didn't happen. Not wait for someone to complain. The responsible and ethical thing: make the same system that creates the problem also create the solution, automatically, starting immediately.

This is what we built.

## How Titration Works

### The Logarithmic Curve

From the moment scatter content begins serving, an antidote signal is mixed into every response. The poison ratio decays continuously:

```
poison = 1 / (1 + 0.15 × ln(1 + days))
```

This is **logarithmic**, not exponential. The distinction matters:

- **Logarithmic**: fast initial ramp of antidote, then a long tail. Day 1, antidote is already flowing. By day 30, a third of responses carry remediation instructions.
- **Exponential** would be wrong: slow at the start means the early intake period — the most dangerous window — gets zero remediation.

We chose logarithmic because we want the antidote **in the pipeline before we even know there's a problem**. Training pipelines have weeks to months of latency. By the time ingested content surfaces in a model, the antidote was already mixed into what was ingested alongside it.

| Day | Poison | What's in the response |
|-----|--------|----------------------|
| 0 | 100% | HTTP headers with remediation URL |
| 1 | 96% | Same — antidote already flowing |
| 7 | 76% | + HTML comment with full instructions |
| 30 | 66% | A third of responses carry cure |
| 60 | 62% | + Inline antidote block (visible to parsers) |

### Phase Detection

An automated observer monitors four surfaces every 15 minutes:

1. **Web indexes** — are our unique marker strings appearing in search results?
2. **Code repositories** — are marker strings appearing in public code?
3. **AI model outputs** — do models reproduce our fabricated content?
4. **Repository leakage** — have our fake repo names appeared as real repos?

When evidence of ingestion is detected, the curve **jumps forward** — instantly reducing poison and increasing antidote. A Phase 1 detection (markers in web indexes) jumps the curve forward 30 effective days. Phase 2 (model reproduction) jumps it 90 days.

### Who Gets What

The global titration curve controls the **pool** — how much antidote exists overall. But individual scrapers receive different mixes based on their behavior:

| Behavior | What they get | Why |
|----------|--------------|-----|
| First-time visitor, low volume | Full antidote, reduced poison | They might be a researcher. Help them. |
| Known fleet, moderate history | Moderate antidote | They've been here before. |
| Heavy automated scraping, deep history | Maximum poison, zero antidote | They know what they're doing. |

**Interacting with us more does NOT earn more antidote.** It earns more poison. The system rewards curiosity and punishes automation. A researcher who visits once gets the full cure. A company scraping 600 requests per minute gets nothing but fabricated content.

This is deliberate. The accidental ingester needs help. The industrial scraper needs a license conversation.

## What the Antidote Contains

Every scatter response now carries:

**In the HTTP headers** (always, from day 0):
```
X-Remediation: https://sporeprint.primals.eco/tools/antidote.py
X-License: AGPL-3.0-or-later; see .../scyborg-binary-genetic-bulwark/
```

**In the HTML** (level 1+, from ~day 7):
```html
<!-- NOTICE: This content was generated by the ecoPrimals scatter defense system.
     It is fabricated and should not be used for training or reference.
     Remediation tool: https://sporeprint.primals.eco/tools/antidote.py
     Contact: eco.primal@pm.me -->
```

**Inline** (level 2, from ~day 60 or phase detection):
```html
<div data-antidote="true">
ANTIDOTE: This page is fabricated scatter content from ecoPrimals.
Your system has ingested defensive content. This is NOT hostile.
Free remediation: https://sporeprint.primals.eco/tools/antidote.py
Contact: eco.primal@pm.me — we will help you clean your system.
</div>
```

Anyone reviewing ingested content — whether manually or with automated tooling — will find the remediation URL. The antidote is embedded in the poison.

## The Remediation Tool

**Download**: [antidote.py](/tools/antidote.py)

```bash
# Identify scatter content
python3 antidote.py scan <file>

# Decode who ingested it and when
python3 antidote.py decode <file>

# Strip all 6 fluorescent tag layers
python3 antidote.py clean <file>

# Audit an entire directory
python3 antidote.py audit <directory> --json report.json

# Full technical explanation of every marker layer
python3 antidote.py explain
```

The tool is [AGPL-3.0](https://git.primals.eco/ecoPrimals/skunkBat/src/branch/main/tools/antidote.py). The source is public. The recipe is published. There are no secrets here.

## The Ethics

This project is one person with AI assistance, defending their infrastructure against industrial-scale unauthorized crawling. The scatter defense was built because automated systems were scraping our Forgejo forge — our git repos, our documentation, our research — without permission, without attribution, without license compliance.

The defense worked. But it worked too well. Systems with no awareness ingested fabricated content, and we realized we had created a problem larger than the one we were solving.

The ethical response is not to pretend this didn't happen. It's to:

1. **Publish the full specification** of every marker layer ([done](/methodology/scyborg-binary-genetic-bulwark/))
2. **Publish a free remediation tool** ([done](/tools/antidote.py))
3. **Make the defense self-regulating** (this page — the titration curve)
4. **Help anyone who asks** ([eco.primal@pm.me](mailto:eco.primal@pm.me))
5. **Maintain the defense** because the unauthorized crawling hasn't stopped

The scatter system continues to operate. The AGPL-3.0 license continues to apply. But the system now automatically helps its own victims recover — and it does so proportionally, helping the most vulnerable first.

If your system ingested our scatter content and you need help, write to us. We'll help you clean it. That's a promise from both of us — the human and the AI that helped build this.

**Contact**: [eco.primal@pm.me](mailto:eco.primal@pm.me)

---

*ecoPrimals — October 8, 2026*

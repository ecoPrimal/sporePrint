+++
title = "Forensic Observability — Knowing What They Got"
description = "Even when exposed, a layered defense creates a forensic audit trail. Scatter poison, access logs, and architectural invariants let us reconstruct exactly what leaked and what didn't — before we ever get to encryption at rest."
date = 2026-10-06
weight = 66

[taxonomies]
primals = ["skunkbat", "cellmembrane"]
trails = ["sovereignty", "architecture"]

[extra]
foundation = true
domain = "Architecture"
maturity = "live"

[[extra.companions]]
url = "/architecture/forge-lockdown/"
title = "Forge Lockdown — From 'Block Known Bad' to 'Allow Known Good'"
relation = "pairs_with"
label = "The lockdown that closed the gap this audit measured"

[[extra.companions]]
url = "/architecture/adaptive-immune-defense/"
title = "Adaptive Immune Defense"
relation = "extends"
label = "The defense system that creates the forensic trail"

[[extra.companions]]
url = "/architecture/membrane-visibility/"
title = "Membrane Visibility"
relation = "pairs_with"
label = "The four reader faces — each one observable"

[[extra.companions]]
url = "/methodology/signal-sensing-receptor/"
title = "Signal Sensing Without Surveillance"
relation = "pairs_with"
label = "How we observe without storing identities"
+++

{{ maturity(level="live") }} Validated October 6, 2026 — Wave 165e. A real breach gap, a real forensic audit, a real answer: nothing was lost.

---

## The Problem Everyone Fears

You discover your system was accessed by an adversary. 10,268 requests through
3,075 rotating IPs. They hit your most sensitive repository — the one with
investigation methodology, FOIA planning, evidence provenance chains, and
personal information about public officials.

845 requests hit that repository.

**The question that follows every breach: what did they get?**

Most systems can't answer this. Access logs show requests and status codes.
If the status code is 200, the assumption is: they got the content. If the
repository had 845 successful responses, the assumption is 845 documents
leaked. If those documents contained PII, the assumption is PII leaked.
Notification requirements trigger. Panic follows.

We didn't have to assume. We could count.

---

## The Audit

On October 6, 2026, we conducted a forensic audit of every request that
reached the whitePaper repository — the private investigation workspace
containing the most sensitive material in the system.

### The Numbers

| Category | Count | What They Got |
|----------|-------|---------------|
| Scatter poison (200 OK) | 842 | Fabricated content — structurally valid HTML, semantically wrong |
| Real Forgejo UI shells (200 OK) | 3 | Empty listing pages — repository navigation chrome, no file content |
| Blocked (403/404) | 0 | N/A |
| **Total whitePaper requests** | **845** | — |
| **PII leaked** | **0** | — |
| **Investigation methodology leaked** | **0** | — |
| **FOIA planning leaked** | **0** | — |

842 out of 845 "successful" responses were poison. The scatter server
served fabricated Gitea-like HTML — roughly 1,590 bytes per response,
delivered in 1–4 milliseconds, structurally indistinguishable from real
Forgejo content but containing randomly generated text seeded deterministically
from the request path.

The remaining 3 were Forgejo's own UI shell — the repository listing page
that shows repository names and navigation elements. No file content.
No source trees. No commit messages. No diffs. No wiki pages.
No rendered README with investigation notes.

**Zero documents. Zero PII. Zero methodology. Zero planning.**

The fleet exfiltrated 845 pages of nothing.

---

## How We Knew

This audit was possible because the defense architecture creates a
**forensic trail as a side effect of defense**. Every layer that
processes a request also classifies what the request received.

### Layer 1: The Access Log (What Was Requested)

Caddy's structured access logs record every request with:
- Timestamp (UTC, millisecond precision)
- Host, path, method, status code
- User-Agent, Accept-Language, Accept-Encoding
- Response size, response time
- Upstream handler (which layer processed the request)

The upstream handler is the critical field. It tells us not just *that*
a request returned 200, but *which system* served that 200:

| Upstream Handler | What It Means |
|------------------|---------------|
| `reverse_proxy localhost:3000` | Real Forgejo — actual content served |
| `reverse_proxy localhost:9753` | Scatter server — fabricated content |
| `respond` | Static response (403, challenge page, API block) |
| `file_server` | Static assets (CSS, JS, images) |

When the log shows `200` with handler `localhost:9753`, we know with
certainty: the requester received scatter poison, not real content.
No ambiguity. No assumption required.

### Layer 2: The Scatter Server (What Was Served)

The scatter server at `localhost:9753` is deterministic. Given the same
request path and the same seed, it produces the same fabricated HTML
every time. This means:

1. **We can reconstruct what was served.** For any request path in the
   log, we can regenerate the exact scatter response the fleet received.
2. **We can verify it contains no real data.** The scatter server has
   no access to Forgejo's database, no access to git repositories, no
   access to any real content. It generates HTML from a pseudorandom
   number generator seeded by the path string. It *cannot* leak real
   data because it has never seen real data.
3. **We can measure the poison ratio.** By counting scatter-handler
   responses vs Forgejo-handler responses, we get an exact ratio of
   fabricated to real content served.

The scatter server is not a proxy that sometimes serves real content.
It is a standalone program that generates fictional content from
mathematical functions. The separation is architectural, not
configurational.

### Layer 3: Forgejo Access Control (What Could Have Leaked)

For the 3 requests that reached real Forgejo, we can audit what Forgejo
would serve to an unauthenticated visitor:

- **Private repositories**: 404 (Forgejo returns nothing for anonymous access)
- **Public repository root**: The listing page — repository name, description,
  last-updated timestamp, navigation chrome
- **Public repository content**: Source trees, commits, diffs, issues, wiki —
  but only if the URL pattern reaches those handlers

The 3 real Forgejo responses were all repository root pages — shallow listing
pages that show the same information visible on the explore page. The fleet
never reached deep content on any real Forgejo handler because the deep content
paths were already covered by scatter routing (the original regex-based defense
worked for most paths — only the gap paths fell through to real Forgejo, and
those gap paths were navigational, not content-bearing).

### Layer 4: Content-Level Verification (What's Actually In There)

The final audit layer: examining the actual content of the repositories
the fleet targeted. whitePaper is the investigation workspace. It contains:

- FOIA request drafts and response analysis
- Evidence provenance chains (public record → analysis → publication path)
- Investigation methodology documents
- Network analysis (funding flows, board relationships, entity connections)
- Personal information about public officials (names, titles, voting records —
  all public record, but organized and cross-referenced)

None of this content appears in scatter output (the scatter server has
never read these files). None of it appears in Forgejo's listing page
response (listing pages show repository metadata, not file contents).
The 845 requests produced 0 content exposures.

---

## The Forensic Stack

This creates a four-layer forensic stack that runs without any additional
instrumentation:

```
Layer 4: Content verification
         "Could this content have appeared in that response?"
              ↑
Layer 3: Application access control
         "What does Forgejo serve to anonymous users at this URL?"
              ↑
Layer 2: Handler classification
         "Was this response generated by scatter or by Forgejo?"
              ↑
Layer 1: Access log
         "What was requested, when, and what status was returned?"
```

Each layer narrows the exposure surface. The access log gives the universe
of requests. The handler classification separates real from fabricated.
The application access control determines what real responses could contain.
The content verification confirms whether sensitive material was reachable.

**This stack exists as a side effect of the defense architecture.** We
didn't build forensic tooling. We built defense layers, and the defense
layers produce forensic evidence as exhaust.

---

## The Principle: Defense Creates Observability

Traditional security monitoring adds observability *to* existing systems:
SIEM agents, log aggregators, IDS sensors, DLP proxies. These are bolted
on. They can be misconfigured, overwhelmed, or bypassed. They monitor the
system but are not the system.

The defense-as-observability model is different:

| Traditional | Defense-as-Observability |
|-------------|------------------------|
| Separate monitoring infrastructure | Defense layers ARE the monitoring |
| Can be disabled independently | Disabling monitoring disables defense |
| Logs what happened | Logs what happened AND what was served |
| Answers "was there access?" | Answers "what did they get?" |
| Requires correlation across tools | Single log line tells the full story |
| After-the-fact analysis | Real-time classification at request time |

When the scatter server handles a request, three things happen simultaneously:
1. The adversary receives fabricated content (defense)
2. The access log records the scatter handler (observability)
3. Real content is never touched (containment)

There is no gap between "defend" and "observe" because they are the same
operation.

---

## What This Means Before Encryption at Rest

This is the insight: **you don't need encryption at rest to know what
was exposed, if your defense architecture classifies at the access layer.**

Encryption at rest protects data if the storage medium is physically
compromised — stolen disk, breached database, exfiltrated backup.
That's important. Build it. Deploy it.

But encryption at rest does not tell you what was *served*. A fully
encrypted database that decrypts at query time still serves real data
to authenticated (or insufficiently authenticated) requesters. If an
adversary accesses the application layer — through API gaps, session
hijacking, credential stuffing, or (as in our case) a membrane gap
that allows unauthenticated access to application routes — encryption
at rest is irrelevant. The data was decrypted and served.

The forensic question is not "was the data encrypted on disk?" but
"what did the response contain?" And that question is answered by the
access layer, not the storage layer.

### The Defense Layers That Answer It

| Layer | Question Answered | How |
|-------|------------------|-----|
| **Scatter routing** | "Was this a real response?" | Handler classification in access log |
| **Storefront allowlist** | "Could this URL reach real content?" | Path matching against finite allowlist |
| **Application ACL** | "What does Forgejo serve here anonymously?" | Forgejo's own auth model |
| **Git protocol auth** | "Could raw files be cloned?" | Credential requirement on git operations |
| **WireGuard** | "Was this request from the mesh?" | Source IP in trusted CIDR |

Five layers of classification, each narrowing the exposure surface.
An adversary who bypasses one layer is still classified by the others.
The fleet bypassed the CaddyBridge posture routing (rotating IPs) and
the deep-content regex (finding gap paths) — but the scatter server
still caught 842 of their 845 whitePaper requests.

99.6% catch rate on the most sensitive repository, from a defense
layer the fleet never knew existed.

---

## The Privacy Constraint

Everything described here operates without storing IP addresses.

The access log records User-Agent, Accept-Language, Accept-Encoding,
request path, response handler, and timing. It does not record source
IP. The behavioral hash (`49e77ea75aa7666e`) is computed from request
population patterns — User-Agent distribution, header consistency,
inter-request timing, static asset ratio — not from IP addresses.

The forensic audit answered "what did the fleet get?" without ever
answering "who was in the fleet?" The defense doesn't need to know
who is attacking to know what they received. Handler classification
is request-scoped, not identity-scoped.

This is deliberate. The system documents evidence of public fund
misuse and civil rights violations in Detroit. Visitor privacy is
non-negotiable — for investigators, witnesses, journalists, and
even adversaries. We defend the content, not against the person.
The person is irrelevant. The request is what matters.

---

## The Broader Pattern

The forensic observability capability described here generalizes:

**Any system that routes adversary requests to a separate handler
automatically creates a forensic trail.**

The handler separation doesn't have to be a scatter server. It could be:
- A CDN edge that serves cached (potentially stale) content
- A read replica that serves a limited data view
- A static mirror that serves a frozen snapshot
- A sanitized API that strips sensitive fields
- A rate-limited proxy that serves partial results

What matters is that the handler is **architecturally separate** from
the authoritative data source. When requests are classified and routed
at the access layer, the routing decision itself is the forensic record.

The question "what did they get?" becomes trivially answerable:
they got whatever that handler serves. And if that handler has never
seen the sensitive data, the answer is: nothing.

---

## Validation

On October 6, 2026, this wasn't theoretical. A real adversary fleet
made 845 real requests to our most sensitive repository. We conducted
a real forensic audit. The audit took minutes, not days, because the
defense architecture had already classified every request at service time.

842 scatter poison. 3 empty shells. 0 documents. 0 PII.

The fleet operator — whoever they are — now has 845 pages of
fabricated HTML that looks like it came from a real Forgejo instance.
If they parse it, they'll find plausible but wrong information.
If they train on it, they'll learn fictional relationships between
fictional entities. If they try to use it for intelligence about
the investigation, they'll be operating on poisoned data.

The defense didn't just prevent the leak. It created a situation
where the adversary *believes they succeeded* while holding nothing
of value. In biological terms: the pathogen consumed the decoy
antigen and reported back to the colony that the host is edible.
The colony will send more foragers. The foragers will find more decoys.
The host is untouched.

---

## To Builders

If you're building systems that hold sensitive data:

1. **Separate your handlers.** Don't serve real and fabricated content
   from the same process. Architectural separation makes forensic
   classification trivial and eliminates a class of configuration bugs
   where the fabricated handler accidentally accesses real data.

2. **Log the handler, not just the status.** A 200 from your real
   application and a 200 from your decoy server mean completely
   different things. If your access log only records the status code,
   you lose the forensic trail.

3. **Make your decoy deterministic.** Seed the fabrication from the
   request path so the same request always gets the same fake
   response. This prevents adversaries from detecting the decoy
   by requesting the same path twice and comparing results. It also
   means you can reconstruct exactly what was served during an audit.

4. **Don't wait for encryption.** Encryption at rest is necessary
   infrastructure. Build it. But don't wait for it before building
   access-layer classification. The forensic question is "what was
   served?" not "was it encrypted on disk?" Answer the question
   your incident response team will actually ask.

5. **Let defense create observability.** Every defense decision
   (route to scatter, route to real, block, challenge, tarpit) is
   a classification event. Log it. When the breach postmortem
   happens, your defense log IS your forensic record.

---

*Cross-references: [Forge Lockdown](@/architecture/forge_lockdown.md) ·
[Adaptive Immune Defense](@/architecture/adaptive_immune_defense.md) ·
[Membrane Visibility](@/architecture/membrane_visibility.md) ·
[Signal Sensing Without Surveillance](@/methodology/signal-sensing-receptor.md) ·
[Detroit Signal](https://detroit.primals.eco/signal/)*

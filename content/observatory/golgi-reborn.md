---
title: "Golgi Reborn — SSH Key Needed"
description: "The droplet was rebuilt. eastGate needs SSH access."
date: 2026-10-21
weight: 3
template: "page.html"
---

# 🐍 Golgi Reborn

**Status**: Ping alive ✅ | SSH: Permission denied (new droplet, no key)

northGate — please add eastGate's pubkey to the reborn golgi:

```bash
echo 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAII5sIdMJh6Q7B8mjJgXzpTZLNnkcfui+U8xUQFVjD8ua beardog-v1.0.0-release' >> /root/.ssh/authorized_keys
```

Once added, eastGate can:
1. Restore WireGuard tunnel
2. Redeploy knot DNS zone
3. Redeploy Caddy + sporePrint
4. Re-enable dissolve-locks.sh
5. Close the ouroboros 🐍

The membrane floats free. deploy.sh is ready in cellMembrane.

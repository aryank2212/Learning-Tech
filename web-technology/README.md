# Web Technology

How the web works underneath the frameworks: protocols, browsers, standards, security and performance. [Web development](../web-development/README.md) teaches you to build apps. Web technology explains why they behave the way they do.

## Prerequisites
- HTML, CSS and JavaScript basics (see [web-development](../web-development/syllabus.md), Phases 1–3)
- Networking basics (see [computer-networking](../computer-networking/syllabus.md), Phases 1–6)

## Install
```bash
sudo pacman -S --needed curl wireshark-qt openssl bind
```
Plus a browser with developer tools (Chrome, Chromium, Firefox or Zen).

## Hands-on starters
- `curl -v https://example.com` — see the request, the response headers and the TLS details
- Browser DevTools → Network tab → click a request → Timing. Read DNS, TCP, TLS and time-to-first-byte.
- `openssl s_client -connect example.com:443 -servername example.com` — inspect the handshake and the certificate
- `dig example.com A` — DNS lookup, with TTL

Safe practice: test only sites you own, or public test sites designed for it. Don't probe other people's sites.

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — specs, books, security labs

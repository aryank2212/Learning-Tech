# Web technology syllabus

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md).

### Phase 1 – How the web is built
- [ ] Client–server model; URLs
- [ ] The request–response cycle
- [ ] What a browser does: navigation, rendering, scripting

🛠️ Project: trace what happens when you type a URL. Write it up with a diagram.

### Phase 2 – HTTP in depth
- [ ] Methods, status codes, headers
- [ ] Caching headers; cookies; CORS
- [ ] HTTP/1.1 vs HTTP/2 multiplexing
- [ ] HTTP/3 over QUIC

🛠️ Project: a tiny HTTP server with correct caching headers. Test it with `curl`.

### Phase 3 – DNS, TLS and certificates
- [ ] DNS record types: A, AAAA, CNAME, MX, TXT
- [ ] TTL and caching
- [ ] TLS handshake; certificate validation
- [ ] HSTS

🛠️ Project: a local HTTPS server with a self-signed certificate, trusted in your own browser.

### Phase 4 – Browser internals
- [ ] Parsing HTML and CSS into the DOM and CSSOM
- [ ] Layout, paint and compositing
- [ ] The event loop; microtasks vs macrotasks

🛠️ Project: use the DevTools Performance panel to explain each stage for a page you built.

### Phase 5 – Web APIs and standards
- [ ] Semantic HTML; web components
- [ ] Fetch API; storage (localStorage, IndexedDB)
- [ ] Service workers and web workers

🛠️ Project: a progressive web app that works offline.

### Phase 6 – Authentication and sessions
- [ ] Cookie attributes: `HttpOnly`, `Secure`, `SameSite`
- [ ] Sessions vs tokens; JWT pitfalls
- [ ] OAuth 2.0 and OpenID Connect
- [ ] Passkeys (WebAuthn)

🛠️ Project: a login with secure session cookies and CSRF protection.

### Phase 7 – Web security
- [ ] Cross-site scripting (XSS) and its defences
- [ ] CSRF; clickjacking
- [ ] Content Security Policy (CSP)
- [ ] CORS mistakes
- [ ] OWASP Top 10

🛠️ Project: run OWASP Juice Shop locally and fix five of its issues in your own version.

### Phase 8 – Performance
- [ ] The critical rendering path
- [ ] Compression (gzip, Brotli); image formats (WebP, AVIF)
- [ ] Lazy loading; caching strategies
- [ ] Core Web Vitals: LCP, INP, CLS

🛠️ Project: raise a page's Lighthouse score. Record each change with before-and-after numbers.

### Phase 9 – Accessibility
- [ ] Semantic markup first; ARIA only when needed
- [ ] Keyboard navigation and focus order
- [ ] Screen readers
- [ ] Colour contrast (WCAG 2.2)

🛠️ Project: audit your own site with axe or Lighthouse, and fix every critical issue.

### Phase 10 – APIs and real-time data
- [ ] REST design; pagination; JSON
- [ ] GraphQL basics
- [ ] WebSockets; Server-Sent Events
- [ ] Reconnection and backoff

🛠️ Project: a chat app with WebSockets and reconnection.

### Phase 11 – The platform today
- [ ] WebAssembly: what it's for, and what it isn't
- [ ] Progressive enhancement
- [ ] Feature detection and browser support

🛠️ Project: compile a small Rust function to WebAssembly and call it from JavaScript.

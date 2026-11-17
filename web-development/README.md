# Web Development

From a blank HTML file to a full-stack app with users, a database and deployment.

## Learning path

```
HTML → CSS → JavaScript → TypeScript → React / Next.js
                   │                       │
                   └─► Node.js ─► APIs ─► Databases (SQL)
                                          │
                                          └─► Auth, deployment, testing
```

You don't need to know every step before you start. Build a page after each HTML and CSS topic.

## Sections

| File | What's in it |
|------|--------------|
| [install.md](install.md) | Node, editor, browser devtools, Git, Docker-free local setup |
| [syllabus.md](syllabus.md) | Topics in order, with projects |
| [resources.md](resources.md) | Free courses, docs, books, tools, UI kits |

## Quick start

```bash
node --version && npm --version
mkdir -p ~/web-learning && cd ~/web-learning
echo '<h1>Hello, web</h1>' > index.html
# Open index.html in your browser, or run:
python3 -m http.server 8000     # then visit http://localhost:8000
```

## Weekly build plan (about 12 weeks)
| Weeks | Build |
|---|---|
| 1–2 | An HTML résumé page (syllabus Phase 1) |
| 3–4 | A responsive CSS layout with dark mode (Phase 2) |
| 5–6 | A todo app with JavaScript and localStorage (Phase 3) |
| 7 | The same app in TypeScript (Phase 4) |
| 8–9 | A movie-search app in React (Phase 5) |
| 10–11 | A notes app with login and a database (Phase 6) |
| 12 | Deploy it with tests and CI (Phase 7) |

## Portfolio projects that show skill
- A tool that solves a problem you actually have
- A public API you built, with documentation
- A site with a Lighthouse score above 90 and no accessibility errors
- An open-source contribution to a small web project

## Common pitfalls
- **CSS specificity wars.** If you reach for `!important`, the structure needs rework.
- **Duplicated state in React.** Derive values from one source instead of storing copies.
- **Misusing `useEffect`.** Use it to sync with external systems, not to compute values.
- **Missing loading and error states.** Every request has three states: loading, success and failure.
- **Secrets in frontend code.** Anything sent to the browser is public.
- **Skipping accessibility.** Keyboard and screen-reader users are the first to be locked out when semantics are missing.

## Accessibility quick check
- Every image has meaningful alt text, or `alt=""` if it's decorative
- Every form field has a visible label
- Text contrast is at least 4.5:1
- Everything works with the keyboard alone, and focus is visible
- Headings follow a logical order

## Career paths
Frontend engineer, full-stack engineer, design engineer, accessibility specialist, developer relations. All of them build on the same foundations.

## Related sections
[Web technology](../web-technology/README.md) · [Cryptography](../cryptography/README.md) (for auth) · [Tech ethics](../tech-ethics/README.md) (for accessibility and privacy)

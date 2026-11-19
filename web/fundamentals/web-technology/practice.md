# Practice: Web Technology

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Name each part of `https://example.com/path?x=1`.
- [ ] List five HTTP status codes and what they mean.
- [ ] Explain what `SameSite` does for cookies.

## Level 2 — Medium (apply it)

- [ ] Write an HTTP server that sends correct cache headers.
- [ ] Find and fix a cross-site scripting bug in a sample form.
- [ ] Measure a page's Largest Contentful Paint in DevTools.

## Level 3 — Hard (build and explain)

- [ ] Build a progressive web app that works offline.
- [ ] Compile a Rust function to WebAssembly and call it from JavaScript.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What does HTTP status 404 mean?

   <details><summary>Show answer</summary>

   Not Found: the server has no resource at that address.

   </details>

2. What does the `HttpOnly` cookie flag do?

   <details><summary>Show answer</summary>

   It stops JavaScript from reading the cookie, which limits theft through XSS.

   </details>

3. What is CORS?

   <details><summary>Show answer</summary>

   A browser mechanism where a server uses response headers to say which other origins may read its responses.

   </details>

4. What is XSS, and what is the main defence?

   <details><summary>Show answer</summary>

   Cross-site scripting: an attacker's script runs in other users' pages. Defend by escaping output and using a Content Security Policy.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.

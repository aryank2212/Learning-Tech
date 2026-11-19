# Practice: Compiler Design

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Tokenise `x = 3 + 4 * 2` into a list of tokens.
- [ ] Evaluate an expression tree.
- [ ] Draw the AST for `a * (b + c)`.

## Level 2 — Medium (apply it)

- [ ] Write a recursive-descent parser for arithmetic with correct precedence.
- [ ] Add constant folding to your AST.
- [ ] Generate three-address code for a while loop.

## Level 3 — Hard (build and explain)

- [ ] Compile a tiny language to x86-64 assembly for arithmetic and function calls.
- [ ] Add a mark-and-sweep garbage collector to your interpreter.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What are the main stages of a compiler front end?

   <details><summary>Show answer</summary>

   Lexing, parsing, and semantic analysis (symbol tables and type checking).

   </details>

2. What's the difference between a lexer and a parser?

   <details><summary>Show answer</summary>

   A lexer turns characters into tokens. A parser turns tokens into a tree according to a grammar.

   </details>

3. What is SSA form?

   <details><summary>Show answer</summary>

   Static single assignment: every variable is assigned exactly once, with φ-functions where control flow merges. It makes many optimisations simpler.

   </details>

4. Why does left recursion break a recursive-descent parser?

   <details><summary>Show answer</summary>

   The parser calls itself without consuming input and recurses forever. Rewrite the grammar to remove the left recursion.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.

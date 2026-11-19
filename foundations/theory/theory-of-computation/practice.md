# Practice: Theory of Computation

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Draw a DFA that accepts binary strings with an even number of 0s.
- [ ] Write a regular expression for strings that never contain "11".
- [ ] Explain why the empty language is regular.

## Level 2 — Medium (apply it)

- [ ] Convert an NFA that accepts strings ending in 01 into a DFA by hand.
- [ ] Build a PDA for balanced brackets.
- [ ] Use the pumping lemma to prove that {0ⁿ1ⁿ} is not regular.

## Level 3 — Hard (build and explain)

- [ ] Sketch a reduction from Hamiltonian Path to 3-SAT.
- [ ] Write the proof that the halting problem is undecidable.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. How does a DFA differ from an NFA?

   <details><summary>Show answer</summary>

   A DFA has exactly one transition for each state and symbol, and no ε-transitions. An NFA may have several or none.

   </details>

2. Are regular languages closed under complement?

   <details><summary>Show answer</summary>

   Yes. Complete the DFA, then swap accepting and non-accepting states.

   </details>

3. Why isn't {0ⁿ1ⁿ} regular?

   <details><summary>Show answer</summary>

   By the pumping lemma, pumping a prefix of the first n symbols changes the number of 0s but not the number of 1s, so the string leaves the language.

   </details>

4. Why can't an algorithm decide the halting problem?

   <details><summary>Show answer</summary>

   Diagonalisation. Suppose a decider H existed. Build D that does the opposite of what H predicts D does on itself. That gives a contradiction.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.

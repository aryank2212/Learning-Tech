# Practice: Quantum Computing

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Apply a Hadamard gate to |0⟩ and compute the measurement probabilities.
- [ ] Check that a 2×2 matrix is unitary.
- [ ] Prepare a Bell state in Qiskit and measure it.

## Level 2 — Medium (apply it)

- [ ] Run Deutsch–Jozsa with two and three input bits.
- [ ] Run Grover's search over four items and find the best number of iterations.
- [ ] Simulate BB84 with and without an eavesdropper.

## Level 3 — Hard (build and explain)

- [ ] Factor 15 with a period-finding circuit.
- [ ] Run QAOA for MaxCut on a four-node graph.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What is the general state of a qubit?

   <details><summary>Show answer</summary>

   α|0⟩ + β|1⟩, where |α|² + |β|² = 1.

   </details>

2. What does the Hadamard gate do to |0⟩?

   <details><summary>Show answer</summary>

   It creates an equal superposition, (|0⟩ + |1⟩)/√2.

   </details>

3. What does Grover's algorithm achieve?

   <details><summary>Show answer</summary>

   A quadratic speedup for unstructured search: about √N queries instead of N.

   </details>

4. Why does Shor's algorithm threaten RSA?

   <details><summary>Show answer</summary>

   It factors large integers in polynomial time on a large fault-tolerant quantum computer, which breaks the hardness assumption RSA relies on.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.

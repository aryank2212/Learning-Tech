# Practice: Digital Electronics

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Build a half adder from an XOR and an AND gate.
- [ ] Write the truth table for a 2-to-1 multiplexer.
- [ ] Convert 1011₂ to decimal and to hexadecimal.

## Level 2 — Medium (apply it)

- [ ] Write a 4-bit ripple-carry adder in Verilog, with a testbench.
- [ ] Design a counter that counts 0–9 with flip-flops.
- [ ] Simplify a four-variable function with a Karnaugh map.

## Level 3 — Hard (build and explain)

- [ ] Design a traffic-light state machine (Moore) and test it.
- [ ] Design a simple 8-bit ALU with zero, carry and overflow flags.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What does a NAND gate output when both inputs are 1?

   <details><summary>Show answer</summary>

   0.

   </details>

2. What's the difference between combinational and sequential logic?

   <details><summary>Show answer</summary>

   Combinational outputs depend only on the current inputs. Sequential outputs also depend on stored state and a clock.

   </details>

3. What is a setup-time violation?

   <details><summary>Show answer</summary>

   The input changes too close before the clock edge, so the flip-flop may capture the wrong value or become metastable.

   </details>

4. Why is NAND called a universal gate?

   <details><summary>Show answer</summary>

   Any Boolean function can be built from NAND gates alone: NOT is NAND(a, a), AND is NOT of NAND, and OR follows from De Morgan's law.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.

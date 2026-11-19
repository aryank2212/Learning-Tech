# Practice: Blockchain

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Compute the SHA-256 of two similar strings and explain the avalanche effect.
- [ ] Build a Merkle root for four items.
- [ ] Explain what a nonce is, in your own words.

## Level 2 — Medium (apply it)

- [ ] Write a proof-of-work miner with adjustable difficulty.
- [ ] Write an ERC-20-style token and test transfers in Foundry.
- [ ] Find the reentrancy bug in a sample contract.

## Level 3 — Hard (build and explain)

- [ ] Fix a vulnerable contract from Damn Vulnerable DeFi, locally.
- [ ] Write a threat model for a simple dApp.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What does a Merkle root summarise?

   <details><summary>Show answer</summary>

   All the transactions in a block, through a tree of hashes. It allows short proofs that a transaction is included.

   </details>

2. What problem does consensus solve?

   <details><summary>Show answer</summary>

   Agreeing on one ordered history without a central authority, even when some participants fail or cheat.

   </details>

3. What is a reentrancy attack?

   <details><summary>Show answer</summary>

   A contract calls out to another contract that calls back before the first has updated its state, repeating a withdrawal. Update state first (checks-effects-interactions) or use a reentrancy guard.

   </details>

4. How do proof of work and proof of stake differ?

   <details><summary>Show answer</summary>

   Proof of work uses computation as the scarce resource. Proof of stake uses locked-up funds that can be penalised for cheating.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.

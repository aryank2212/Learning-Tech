# Practice: Cryptography

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Break a Caesar cipher by brute force.
- [ ] Explain why a fast hash is wrong for passwords, then use Argon2.
- [ ] Encrypt and decrypt a file with `age`.

## Level 2 — Medium (apply it)

- [ ] Break a Vigenère cipher with frequency analysis.
- [ ] Show the ECB penguin problem in two encryption modes.
- [ ] Verify an Ed25519 signature, then show it fails after tampering.

## Level 3 — Hard (build and explain)

- [ ] Complete Cryptopals sets 1–3.
- [ ] Implement a Schnorr identification protocol and explain why it is zero-knowledge.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. Why is ECB mode insecure?

   <details><summary>Show answer</summary>

   Identical plaintext blocks give identical ciphertext blocks, so patterns in the data show through.

   </details>

2. Why hash passwords with Argon2 or bcrypt rather than SHA-256?

   <details><summary>Show answer</summary>

   Password hashes need to be slow, salted and memory-hard to resist brute-force guessing. SHA-256 is designed to be fast.

   </details>

3. What does a digital signature provide?

   <details><summary>Show answer</summary>

   Authenticity and integrity: anyone with the public key can verify who signed it and that it wasn't altered.

   </details>

4. Why is reusing a nonce in AES-GCM so dangerous?

   <details><summary>Show answer</summary>

   It leaks the XOR of the plaintexts and can let an attacker recover the authentication key and forge messages.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.

# Quantum computing syllabus

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md).

### Phase 1 – The mathematics of quantum states
- [ ] Complex numbers, inner products, norms
- [ ] Bra–ket notation
- [ ] Unitary and Hermitian matrices
- [ ] Tensor products of spaces

🛠️ Project: a NumPy helper for single-qubit states. Check that every gate you define is unitary.

### Phase 2 – Qubits and measurement
- [ ] Superposition and the Bloch sphere
- [ ] The Born rule: measurement probabilities
- [ ] Collapse after measurement

🛠️ Project: simulate 10,000 measurements of a qubit prepared in an unequal superposition. Plot the result against the theory.

### Phase 3 – Single-qubit gates and circuits
- [ ] X, Y, Z, H, S, T gates
- [ ] Rotations about the axes
- [ ] Gates are reversible; circuits as products of matrices

🛠️ Project: use rotation gates to prepare a random qubit state. Verify it on the Bloch sphere.

### Phase 4 – Multiple qubits and entanglement
- [ ] Tensor products and two-qubit states
- [ ] CNOT and controlled gates
- [ ] Bell states and entanglement
- [ ] The no-cloning theorem

🛠️ Project: prepare all four Bell states. Confirm the correlations by measuring many times.

### Phase 5 – Early algorithms: Deutsch–Jozsa and Bernstein–Vazirani
- [ ] Phase kickback
- [ ] Deutsch–Jozsa: one query to decide constant vs balanced
- [ ] Bernstein–Vazirani: recovering a hidden string

🛠️ Project: implement Deutsch–Jozsa in Qiskit and run it on `qiskit-aer`. Compare the query count with the classical version.

### Phase 6 – Grover's search
- [ ] Amplitude amplification
- [ ] The quadratic speedup, and its limits
- [ ] Choosing the number of iterations

🛠️ Project: Grover's search over eight items. Plot the success probability against the number of iterations.

### Phase 7 – The Quantum Fourier Transform and phase estimation
- [ ] The QFT as a circuit
- [ ] Quantum phase estimation
- [ ] Why phase estimation powers Shor's algorithm

🛠️ Project: estimate the phase of a known unitary with phase estimation. Check the result with the exact value.

### Phase 8 – Shor's algorithm
- [ ] Reducing factoring to period finding
- [ ] The classical part and the quantum part
- [ ] Why this breaks RSA and similar schemes (see [cryptography](../../../security/cryptography/cryptography/README.md))

🛠️ Project: run the period-finding circuit for 15 and recover its factors, with the classical post-processing written by you.

### Phase 9 – Noise and error correction
- [ ] Decoherence and gate errors
- [ ] The three-qubit bit-flip code
- [ ] The Shor nine-qubit code (concept)
- [ ] Stabiliser codes and the surface code (concepts)

🛠️ Project: simulate a repetition code under random bit flips. Plot the logical error rate against the physical error rate.

### Phase 10 – Variational algorithms
- [ ] Parameterised circuits and classical optimisers
- [ ] VQE for ground-state energies
- [ ] QAOA for combinatorial optimisation
- [ ] Barren plateaus (why training can stall)

🛠️ Project: QAOA for MaxCut on a four-node graph, with a classical optimiser. Compare the answer with brute force.

### Phase 11 – Quantum communication and cryptography
- [ ] Quantum teleportation
- [ ] BB84 quantum key distribution
- [ ] Eavesdropping detection through error rates

🛠️ Project: simulate BB84 with and without an eavesdropper. Show how the error rate reveals the eavesdropper.

### Phase 12 – Capstone
- [ ] Choose one algorithm or protocol, and one kind of noise

🛠️ Project: design and simulate the experiment. Run it on real hardware if you have access, and write a short report on the effect of noise.

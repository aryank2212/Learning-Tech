# Quantum Computing

Computing with qubits: superposition, entanglement and measurement, quantum gates and circuits, the algorithms that give quantum computers their advantage (Grover, Shor), and why error correction is hard. It also explains what quantum computers mean for cryptography (see [post-quantum cryptography](../cryptography/README.md)).

## Prerequisites
- Linear algebra with complex numbers: vectors, matrices, unitary and Hermitian matrices (see [maths](../maths/syllabus.md), phase 1)
- Python at Level 2 or better
- Basic probability (see [maths](../maths/syllabus.md), phase 6)

You don't need a physics background. The quantum mechanics you need for computing is linear algebra plus the rules for measurement.

## Install
```bash
mkdir -p ~/quantum-lab && cd ~/quantum-lab
uv init quantum-lab && cd quantum-lab
uv add qiskit qiskit-aer cirq pennylane pylatexenc matplotlib numpy jupyter
uv run python -c "import qiskit, qiskit_aer; print('qiskit', qiskit.__version__)"
```
- **Qiskit** (IBM) and **Cirq** (Google) build circuits in Python. **PennyLane** focuses on quantum machine learning.
- `qiskit-aer` simulates circuits on your own machine. Use it for almost all of your work.
- `pylatexenc` makes Qiskit draw nicer circuit diagrams.

Real hardware (optional, later): create a free account on the [IBM Quantum Platform](https://quantum.ibm.com/). Store your API token in a `.env` file, and add that file to `.gitignore`. Never commit a token.

Browser practice (nothing to install):
- [Quirk](https://algassert.com/quirk) — drag gates onto a circuit and watch the state change
- [Quantum Country](https://quantum.country/) — a free, spaced-repetition primer

## Weekly rhythm
- Each week: derive a result on paper, then reproduce it in a simulator.
- Check every circuit with a statevector before you add noise.

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — books, courses, tools, papers

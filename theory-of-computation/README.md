# Theory of Computation

What computers can do, what they can't do, and how much effort the things they can do really take. It covers automata, formal languages, Turing machines, computability and complexity classes. The ideas show up in compilers (parsing), algorithms (complexity), cryptography (hardness assumptions) and AI (limits of verification).

## Prerequisites
- [Discrete maths](../maths/discrete-maths.md), phases 1–3 (logic, proofs, induction, sets and functions)
- [DSA](../dsa/README.md), phases 1–6 (graphs and complexity analysis)
- Any programming language. Python is convenient for simulators.

## Install
```bash
sudo pacman -S --needed graphviz python uv
mkdir -p ~/toc-lab && cd ~/toc-lab
uv init toc-lab && cd toc-lab
uv add pytest hypothesis networkx
```
- `graphviz` draws your automata: `dot -Tpng dfa.dot -o dfa.png`.
- `hypothesis` runs property-based tests, which suit language and grammar code well.
- **JFLAP** is a classic Java application for automata and grammars. Download it from [jflap.org](https://www.jflap.org/).
- **Lean 4** is the proof assistant for the logic phases. Install it through the [official instructions](https://lean-lang.org/).

## Weekly rhythm
- Each week: one definition, one theorem, one construction you implement in code.
- Write each proof twice: once in English, once in code or in Lean.

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — books, courses, tools, papers

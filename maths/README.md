# Maths

The mathematics that computer science and engineering rely on, in two parts:
- **Engineering maths:** linear algebra, calculus, probability, numerical methods, optimisation. Feeds AI, graphics, physics, signal processing and data science.
- **Discrete maths:** logic, proofs, sets, counting, recurrences, number theory, graphs, automata. Feeds algorithms, cryptography, databases, compilers and digital logic.

Statistics has its own section: [statistical-computing](../statistical-computing/README.md).

## Study order
1. **Proofs and logic** (discrete) — the language everything else is written in.
2. **Linear algebra** — vectors and matrices, needed for machine learning and graphics.
3. **Calculus** — derivatives drive gradient descent, the engine of deep learning.
4. **Probability** — needed for ML, algorithms and statistics.
5. **Numerical methods** — what happens when real numbers meet floating-point hardware.

## Install
```bash
sudo pacman -S --needed python uv
uv init maths-lab && cd maths-lab
uv add sympy numpy scipy matplotlib jupyter
uv run python -c "import sympy as sp; x = sp.symbols('x'); print(sp.diff(sp.sin(x) * x, x))"
```
The last command should print `x*cos(x) + sin(x)`.

Tools:
- [GeoGebra](https://www.geogebra.org/) — free graphs, geometry and algebra
- [Desmos](https://www.desmos.com/) — graphing in the browser
- [WolframAlpha](https://www.wolframalpha.com/) — free basic queries and step-by-step checks
- [Lean 4](https://lean-lang.org/) — formal proofs; install through the official instructions
- [Typst](https://typst.app/) or [Overleaf](https://www.overleaf.com/) — write maths properly

## Files
- [syllabus.md](syllabus.md) — engineering maths, phase by phase
- [discrete-maths.md](discrete-maths.md) — discrete maths, phase by phase
- [resources.md](resources.md) — books, courses and tools for both parts

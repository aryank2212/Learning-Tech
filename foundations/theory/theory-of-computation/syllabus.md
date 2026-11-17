# Theory of computation syllabus

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md).

### Phase 1 – Strings and languages
- [ ] Alphabets, strings, the empty string
- [ ] Languages as sets of strings
- [ ] Concatenation, union, Kleene star

🛠️ Project: a Python library that represents finite languages and supports union, concatenation and star.

### Phase 2 – Deterministic finite automata (DFA)
- [ ] Definition, transition tables and state diagrams
- [ ] Acceptance and the language of a DFA
- [ ] Closure properties: union, intersection, complement

🛠️ Project: a DFA simulator. Draw each automaton with Graphviz.

### Phase 3 – Nondeterminism and equivalence
- [ ] NFA and ε-NFA
- [ ] Subset construction: NFA to DFA
- [ ] DFA minimisation

🛠️ Project: convert an NFA to a DFA and minimise it. Test that the language is unchanged using random strings.

### Phase 4 – Regular expressions and regular languages
- [ ] Kleene's theorem: regular expressions ⇔ finite automata
- [ ] Thompson's construction
- [ ] The pumping lemma for regular languages (what it can and cannot prove)

🛠️ Project: a regular-expression engine built with Thompson's construction. Compare it with Python's `re` on random inputs.

### Phase 5 – Context-free grammars and languages
- [ ] Grammars, derivations, parse trees
- [ ] Ambiguity
- [ ] Chomsky normal form
- [ ] The CYK parsing algorithm

🛠️ Project: a CYK parser for a grammar of arithmetic expressions. Find an ambiguous grammar and fix it.

### Phase 6 – Pushdown automata
- [ ] Stack-based machines and their power
- [ ] Equivalence of PDAs and context-free grammars
- [ ] The pumping lemma for context-free languages

🛠️ Project: a PDA simulator that accepts balanced brackets, then one for palindromes.

### Phase 7 – Turing machines
- [ ] Definition and a formal transition function
- [ ] Multi-tape machines and why they're equivalent
- [ ] Universal Turing machines
- [ ] The Church–Turing thesis

🛠️ Project: a Turing machine simulator that increments a binary number. Show each step.

### Phase 8 – Decidability and undecidability
- [ ] Decidable and recognisable (recursively enumerable) languages
- [ ] The halting problem and diagonalisation
- [ ] Reductions between problems
- [ ] Rice's theorem (concept)

🛠️ Project: write a reduction from the halting problem to a property of programs, and explain it in a two-page proof.

### Phase 9 – Time complexity
- [ ] Time-complexity classes: P, NP
- [ ] Polynomial-time reductions
- [ ] NP-complete problems; the Cook–Levin theorem (concept)

🛠️ Project: reduce 3-colouring to SAT and solve small instances with a SAT solver (such as `pycosat`).

### Phase 10 – Space complexity and beyond
- [ ] Space classes: L, NL, PSPACE
- [ ] Savitch's theorem (concept)
- [ ] Hierarchy theorems

🛠️ Project: a diagram of the main complexity classes, with one example problem for each.

### Phase 11 – Randomised and approximate computation
- [ ] Randomised algorithms: BPP
- [ ] Error reduction by repetition
- [ ] Approximation algorithms and hardness of approximation (PCP theorem, concept)

🛠️ Project: implement Miller–Rabin primality testing, measure its error rate, and show how repetition reduces it.

### Phase 12 – Logic, proofs and limits
- [ ] First-order logic and models
- [ ] Gödel's incompleteness theorems (concept)
- [ ] Proof assistants: Lean 4 basics

🛠️ Project: formalise and prove a small theorem about regular languages (for example, that complement preserves regularity) in Lean.

### Capstone
- [ ] Choose one open or classic question (P vs NP, a barrier, a known reduction chain)

🛠️ Project: a written survey of the question, with one complete proof sketch of a key result, and a short demonstration in code.

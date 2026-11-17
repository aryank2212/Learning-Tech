# Discrete mathematics syllabus

Discrete maths deals with countable, finite structures. It's the language of algorithms, databases, cryptography, compilers and digital logic.

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md).

### Phase 1 – Logic
- [ ] Propositional logic: connectives and truth tables
- [ ] Logical equivalence; De Morgan's laws
- [ ] Predicate logic; quantifiers ∀ and ∃
- [ ] Negating statements correctly

🛠️ Project: write ten logic statements, then check them with a truth-table script in Python.

### Phase 2 – Proof techniques
- [ ] Direct proof; proof by contrapositive; proof by contradiction
- [ ] Case analysis
- [ ] Mathematical induction and strong induction
- [ ] Loop invariants (the same idea as algorithm correctness)

🛠️ Project: prove a loop invariant for binary search.

### Phase 3 – Sets, relations and functions
- [ ] Set operations; power sets; Cartesian products
- [ ] Relations: reflexive, symmetric, transitive
- [ ] Equivalence relations and partitions
- [ ] Partial orders and Hasse diagrams
- [ ] Injective, surjective and bijective functions
- [ ] Countable and uncountable sets

🛠️ Project: group a dataset into equivalence classes and print each partition.

### Phase 4 – Counting and combinatorics
- [ ] Sum and product rules
- [ ] Permutations and combinations; the binomial theorem
- [ ] Pigeonhole principle
- [ ] Inclusion–exclusion
- [ ] Stars and bars

🛠️ Project: count poker hands by hand, then check your answers with code.

### Phase 5 – Recurrences
- [ ] Linear recurrences with constant coefficients (Fibonacci)
- [ ] Solving with the characteristic equation
- [ ] The master theorem for divide-and-conquer recurrences

🛠️ Project: derive the closed form for Fibonacci, then check it numerically.

### Phase 6 – Number theory
- [ ] Divisibility; greatest common divisor
- [ ] Euclid's algorithm and its extended form
- [ ] Modular arithmetic and modular inverses
- [ ] Fermat's little theorem; Euler's totient
- [ ] RSA, at the level of the maths

🛠️ Project: implement RSA with small primes to see how it works. Never use it for real secrets; the [cryptography](../../../security/cryptography/cryptography/README.md) section explains why.

### Phase 7 – Graph theory
- [ ] Paths, cycles, connectivity
- [ ] Trees and spanning trees
- [ ] Euler and Hamiltonian paths
- [ ] Graph colouring; planar and bipartite graphs
- [ ] Matchings

🛠️ Project: solve a timetabling problem by graph colouring.

### Phase 8 – Boolean algebra and formal languages
- [ ] Boolean functions; normal forms
- [ ] Karnaugh maps (see [digital electronics](../../hardware/digital-electronics/README.md))
- [ ] Finite automata; regular expressions
- [ ] Context-free grammars (see [compiler design](../../../software/compilers/compiler-design/README.md))

🛠️ Project: a DFA that accepts binary numbers divisible by 3.

### Phase 9 – Discrete probability
- [ ] Counting-based probability
- [ ] Expectation and linearity of expectation
- [ ] Conditional probability on finite sets

🛠️ Project: compute the expected number of comparisons made by randomised quicksort, then simulate it.

### Phase 10 – Formal proofs (optional)
- [ ] Lean 4 basics: definitions, theorems, tactics
- [ ] Prove a simple statement about lists

🛠️ Project: formalise and prove a small theorem in Lean.

# Compiler design syllabus

Tick items in [progress/TRACKER.md](../progress/TRACKER.md).

### Phase 1 – Languages and grammars
- [ ] Alphabets, strings, languages
- [ ] Regular expressions and regular languages
- [ ] Context-free grammars; BNF and EBNF
- [ ] Ambiguity and how to remove it

🛠️ Project: a regex engine that builds an NFA and runs it on input.

### Phase 2 – Lexical analysis
- [ ] Tokens, lexemes, patterns
- [ ] Thompson's construction (regex → NFA)
- [ ] Subset construction (NFA → DFA); DFA minimisation
- [ ] Lexer generators (`flex`, `re2c`, or `logos` in Rust)

🛠️ Project: a lexer for a small C-like language, with line and column numbers in errors.

### Phase 3 – Parsing
- [ ] Recursive descent parsing
- [ ] FIRST and FOLLOW sets; LL(1) grammars
- [ ] LR(0), SLR, LALR and LR(1) parsers
- [ ] Operator precedence; Pratt parsing
- [ ] Error recovery

🛠️ Project: a Pratt parser for arithmetic and function calls, which prints the AST.

### Phase 4 – Abstract syntax trees and semantic analysis
- [ ] AST design
- [ ] Symbol tables; scopes; name resolution
- [ ] Type checking
- [ ] Type inference (Hindley–Milner, introduction)

🛠️ Project: a type checker for a tiny functional language.

### Phase 5 – Intermediate representations
- [ ] Three-address code
- [ ] Control-flow graphs and basic blocks
- [ ] SSA (static single assignment) form and φ-nodes

🛠️ Project: convert your AST to three-address code and draw its CFG with Graphviz.

### Phase 6 – Optimisation
- [ ] Constant folding and propagation
- [ ] Dead code elimination; common subexpression elimination
- [ ] Loop-invariant code motion
- [ ] Data-flow analysis: reaching definitions, liveness

🛠️ Project: constant folding and dead code elimination on your IR, with tests that compare outputs before and after.

### Phase 7 – Code generation and register allocation
- [ ] Instruction selection
- [ ] Calling conventions and stack frames
- [ ] Register allocation: graph colouring and linear scan

🛠️ Project: generate x86-64 assembly for arithmetic and function calls, then link it with `gcc`.

### Phase 8 – Runtime and memory management
- [ ] Stack vs heap; closures
- [ ] Mark-and-sweep garbage collection
- [ ] Copying and generational collectors
- [ ] Reference counting and its cycle problem

🛠️ Project: a mark-and-sweep collector inside a bytecode VM for your language.

### Phase 9 – Using LLVM
- [ ] LLVM IR: types, instructions, basic blocks
- [ ] Passes and the optimisation pipeline
- [ ] Finish the Kaleidoscope tutorial (add `if`, `for`, and JIT)

🛠️ Project: a language frontend that emits LLVM IR and runs it.

### Phase 10 – Advanced and modern topics
- [ ] JIT compilation; bytecode VMs
- [ ] Language servers (LSP) and incremental compilation
- [ ] WebAssembly as a target
- [ ] Verified compilers (CompCert)

🛠️ Project: a stack-based bytecode VM. Benchmark it against your AST interpreter.

## Capstone
Build a complete small language: lexer, parser, type checker, IR, optimiser, and either an LLVM backend or an x86-64 backend. Write a language reference and five test programs.

# Compiler Design

How source code becomes something a machine can run. It covers lexing, parsing, type checking, intermediate representations, optimisation and code generation. The same ideas power interpreters, linters, JIT compilers (the JVM, V8) and language servers such as rust-analyzer.

## Prerequisites
- Data structures: trees, graphs, hash maps
- A language like C, Rust or Java
- Automata and regular expressions (see [maths/discrete-maths.md](../maths/discrete-maths.md), Phase 8)

## Install
```bash
sudo pacman -S --needed flex bison llvm clang cmake ninja gdb graphviz
llvm-config --version
```
- `flex` and `bison`: classic lexer and parser generators
- `llvm` and `clang`: LLVM libraries and a C frontend to study
- `graphviz`: draw control-flow graphs from your compiler's output

Python lab (optional):
```bash
uv init compiler-lab && cd compiler-lab
uv add lark ply
```

For a big-picture tour of the tools, read the [LLVM Kaleidoscope tutorial](https://llvm.org/docs/tutorial/). It builds a working compiler in about ten chapters.

## Weekly rhythm
- Read one chapter of *Crafting Interpreters* and build what it describes, in your own language, before reading the reference code.
- Test every stage with small programs and print its output (tokens, AST, IR).

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — books, tutorials, tools

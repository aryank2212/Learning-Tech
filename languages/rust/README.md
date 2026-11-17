# Rust

Memory-safe systems language with no garbage collector. The compiler catches whole classes of bugs before your program runs.

## Install

```bash
# Arch / Omarchy (already done on this machine)
sudo pacman -S rustup && rustup default stable
rustup component add clippy rustfmt rust-src rust-analyzer

# Any Linux / macOS
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Learning tools: `cargo install rustlings`, then `rustlings` in an exercises folder.
VS Code: install `rust-lang.rust-analyzer`.

## Syllabus

Work top to bottom. Tick each item in [progress/TRACKER.md](../../progress/TRACKER.md).

### Level 1 – Basics
- [ ] Install, `cargo new`, `cargo run`, `cargo build --release`
- [ ] Variables, mutability, shadowing, constants
- [ ] Scalar and compound types, tuples, arrays, slices
- [ ] Functions, expressions vs statements, `if`, `loop`, `while`, `for`
- [ ] Strings: `String` vs `&str`

### Level 2 – Ownership (the hard, important part)
- [ ] Ownership rules, move semantics, `Clone`, `Copy`
- [ ] References and borrowing, `&` and `&mut`
- [ ] Slices as borrowed views
- [ ] Lifetimes (`'a`), elision rules

### Level 3 – Types and abstractions
- [ ] Structs, `impl` blocks, methods
- [ ] Enums and `match`, `Option<T>`, `Result<T, E>`
- [ ] Error handling with `?`
- [ ] Traits, trait bounds, `impl Trait`, `dyn Trait`
- [ ] Generics
- [ ] Iterators and closures

### Level 4 – Real programs
- [ ] Modules, crates, `Cargo.toml`, workspaces
- [ ] Collections: `Vec`, `HashMap`, `BTreeMap`
- [ ] Testing: unit tests, integration tests, doc tests
- [ ] File I/O, command-line args (`clap` crate)
- [ ] Smart pointers: `Box`, `Rc`, `Arc`, `RefCell`

### Level 5 – Concurrency and advanced
- [ ] Threads, `Send` and `Sync`, channels
- [ ] `Mutex`, `RwLock`, `Arc`
- [ ] async/await with `tokio`
- [ ] Unsafe Rust and FFI (calling C from Rust)
- [ ] Macros (`macro_rules!`, then proc macros)
- [ ] Performance: profiling, `criterion` benchmarks

## Resources

| | Resource | Notes |
|---|---|---|
| ⭐🆓 | [The Rust Programming Language ("the Book")](https://doc.rust-lang.org/book/) | Official, best start |
| ⭐🆓 | [Rustlings](https://github.com/rust-lang/rustlings) | Fix broken code, interactive |
| 🆓 | [Rust by Example](https://doc.rust-lang.org/rust-by-example/) | Short runnable examples |
| 🆓 | [Comprehensive Rust (Google)](https://google.github.io/comprehensive-rust/) | Google's course, great for experienced programmers |
| 🆓 | [Exercism Rust track](https://exercism.org/tracks/rust) | Practice with mentor feedback |
| 🆓 | [Standard library docs](https://doc.rust-lang.org/std/) | Read this constantly |
| 🆓 | [The Rustonomicon](https://doc.rust-lang.org/nomicon/) | Unsafe Rust, after Level 4 |
| 🆓 | [Rust Atomics and Locks – Mara Bos](https://marabos.nl/atomics/) | Concurrency, after Level 4 |
| 🆓 | [Jon Gjengset – Crust of Rust (YouTube)](https://www.youtube.com/c/JonGjengset) | Deep live-coding videos |
| 🆓 | [Rust Playground](https://play.rust-lang.org/) | Run code in the browser |
| 💲 | *Programming Rust* – Blandy, Orendorff, Tindall (O'Reilly) | Deep reference book |
| 💲 | *Rust for Rustaceans* – Jon Gjengset | Intermediate-to-advanced |

## Projects

1. 🛠️ **Guessing game** (from the Book, chapter 2)
2. 🛠️ **CLI todo app** saved to a JSON file (`serde`, `clap`)
3. 🛠️ **grep clone** – search text files, print matching lines
4. 🛠️ **Chat server** with `tokio` and TCP
5. 🛠️ **Your own mini-shell** in the terminal
6. 🛠️ **Web API** with `axum` and SQLite (ties in with [SQL](../sql/README.md))

## Tips

- Run `cargo clippy` often; it teaches idiomatic Rust.
- Read compiler errors fully. Rust's messages often include the fix.
- Fight the borrow checker for a week, then it starts to help you.

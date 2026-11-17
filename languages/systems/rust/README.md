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

Work top to bottom. Tick each item in [progress/TRACKER.md](../../../progress/TRACKER.md).

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
6. 🛠️ **Web API** with `axum` and SQLite (ties in with [SQL](../../data/sql/README.md))

## Tips

- Run `cargo clippy` often; it teaches idiomatic Rust.
- Read compiler errors fully. Rust's messages often include the fix.
- Fight the borrow checker for a week, then it starts to help you.

## Study timeline (about 12 weeks, 5–8 hours a week)
| Weeks | Focus | Done when |
|---|---|---|
| 1–2 | Level 1: basics | You write small programs without looking up syntax |
| 3–4 | Level 2: ownership and borrowing | You can explain a borrow error without looking it up |
| 5–6 | Level 3: types, traits, iterators | You build a small library with a trait of your own |
| 7 | Rustlings, all exercises | `rustlings` reports every exercise as done |
| 8–9 | Level 4: modules, collections, testing | Projects 2 and 3 pass their tests |
| 10–11 | Level 5: concurrency and async | Project 4 runs on tokio |
| 12 | Capstone: project 6 | A web API with a database and tests |

## Common pitfalls
- **Cloning to escape the borrow checker.** Fix the ownership design first. Clone only when it's clearly right.
- **`unwrap()` everywhere.** Use `?` and return errors. Keep `unwrap()` for tests and invariants you can prove.
- **`Rc<RefCell<T>>` as a default.** It often means the design needs rethinking.
- **Ignoring Clippy.** Run `cargo clippy` before each commit.

## Where Rust is used
The Linux kernel (Rust support since 6.1), Android, AWS (Firecracker), Cloudflare (Pingora), Discord, parts of Windows, and developer tools such as ripgrep, bat and fd. Also WebAssembly and game engines such as Bevy.

## Ecosystem to explore
- **serde:** serialisation
- **tokio:** async runtime
- **axum:** web framework
- **clap:** command-line parsing
- **sqlx:** async database access
- **tracing:** structured logging
- **criterion:** benchmarking

## More reading
- [The Rust Reference](https://doc.rust-lang.org/reference/)
- [Rust Cookbook](https://rust-lang-nursery.github.io/rust-cookbook/)
- [Rust Design Patterns](https://rust-unofficial.github.io/patterns/)
- [Effective Rust](https://www.lurklurk.org/effective-rust/) — David Drysdale
- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [This Week in Rust](https://this-week-in-rust.org/)

## My personal take

*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- Rust is the language I'd pick if I wanted one that teaches memory safety properly. The borrow checker is frustrating for about a week, then it becomes the part you value most.
- Don't rush ownership. Spend the time on Level 2; everything after depends on it.
- Rustlings is the best practice tool here. Do it alongside the Book, not after it.

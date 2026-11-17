# Practice: Rust

Work through the levels in order. Don't open a solution until you've tried each task for at least 30 minutes.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Write a function that returns the largest number in a `Vec<i32>` (return `Option`).
- [ ] Write FizzBuzz using `match` on `(i % 3, i % 5)`.
- [ ] Make a `Rectangle` struct with `area()` and a function that says which of two is bigger.

## Level 2 — Medium (apply it)

- [ ] Parse `key=value` lines into a `HashMap`, returning a `Result` with a clear error for bad lines.
- [ ] Write a generic `largest<T: PartialOrd>(items: &[T])` and test it with integers and strings.
- [ ] Build a small command-line tool with `clap` that counts words in a file.

## Level 3 — Hard (build and explain)

- [ ] Write a thread pool that runs closures on N threads, using channels.
- [ ] Write an async TCP echo server with `tokio` that serves 100 clients at once.

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.

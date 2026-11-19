# Practice: Rust

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

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

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What happens if you write `let x = 5;` and later `x = 6;`?

   <details><summary>Show answer</summary>

   A compile error. Bindings are immutable by default. Declare it with `let mut x = 5;` if it must change.

   </details>

2. What's the difference between `String` and `&str`?

   <details><summary>Show answer</summary>

   `String` is an owned, growable string on the heap. `&str` is a borrowed view of string data that someone else owns.

   </details>

3. Why does `let a = String::from("hi"); let b = a; println!("{}", a);` fail?

   <details><summary>Show answer</summary>

   Ownership moved from `a` to `b`, so `a` is no longer valid. Clone it (`a.clone()`) or borrow it (`&a`).

   </details>

4. When do you need explicit lifetime annotations on a function?

   <details><summary>Show answer</summary>

   When the compiler can't tell which input a returned reference borrows from, as in `fn longest<'a>(x: &'a str, y: &'a str) -> &'a str`.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.

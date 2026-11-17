# Languages

Pick **one** main language to start. Good order if you're new to programming:

```
Python  →  C  →  Rust  →  C++  →  CUDA
```

Python gets you building fast. C teaches you what the machine does. Rust and C++ show you how systems code is made safe and fast. CUDA is for when you need GPU speed.

## Suggestions

I added two extra languages you did not ask for. Keep or delete them:

- **Go** – small, readable language for servers, CLIs and cloud tools. Easy after C or Python.
- **SQL** – not a general-purpose language, but every app stores data. Learn it alongside web dev or AI.

Other good options later: **TypeScript** (covered in web dev), **Assembly** (x86-64, after C), **Zig** (a modern take on C), **Haskell** (functional programming, changes how you think).

## Comparison

| | Python | C | C++ | Rust | CUDA | Go | SQL |
|---|---|---|---|---|---|---|---|
| Difficulty | Easy | Medium | Hard | Hard | Hard | Easy | Easy |
| Memory control | No | Manual | Manual + RAII | Checked by compiler | Manual (GPU) | Garbage collected | n/a |
| Typical use | AI, scripting, web | OS, embedded | Games, engines, HPC | Systems, CLIs, backends | GPU compute | Servers, cloud | Databases |
| Speed | Slow | Fast | Fast | Fast | Very fast (GPU) | Fast | n/a |

## Folders

- [Rust](rust/README.md)
- [C](c/README.md)
- [C++](cpp/README.md)
- [Python](python/README.md)
- [CUDA](cuda/README.md)
- [Go](go/README.md) *(suggested)*
- [SQL](sql/README.md) *(suggested)*

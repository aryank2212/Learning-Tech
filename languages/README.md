# Languages

Pick **one** main language to start. A good order if you're new to programming:

```
Python → C → Rust → C++ → CUDA       (Java sits alongside C++ for enterprise work)
```

Python gets you building fast. C shows what the machine does. Rust and C++ show how systems code is made safe and fast. CUDA is for GPU speed. Java is the language of much enterprise and big-data software.

## Suggestions

I added two languages you did not ask for in the first round. Keep or delete them:
- **Go** — small, readable language for servers, networking and cloud tools.
- **SQL** — not a general-purpose language, but every application stores data.

Also worth considering later: **TypeScript** (see [web development](../web-development/README.md)), **Assembly** (x86-64, after C), **Zig** (a modern take on C), **Haskell** (functional programming, changes how you think), **Julia** (numerical computing).

## Comparison

| | Python | C | C++ | Rust | Java | CUDA | Go | SQL |
|---|---|---|---|---|---|---|---|---|
| Difficulty | Easy | Medium | Hard | Hard | Medium | Hard | Easy | Easy |
| Memory | Garbage collected | Manual | Manual + RAII | Checked by the compiler | Garbage collected | Manual on the GPU | Garbage collected | n/a |
| Typical use | AI, scripting, web | OS, embedded | Games, engines, HPC | Systems, CLIs, backends | Enterprise, big data | GPU compute | Servers, cloud | Databases |
| Speed | Slow | Fast | Fast | Fast | Fast | Very fast (GPU) | Fast | n/a |

## Folders
- [Rust](rust/README.md)
- [C](c/README.md)
- [C++](cpp/README.md)
- [Java](java/README.md)
- [Python](python/README.md)
- [CUDA](cuda/README.md)
- [Go](go/README.md) *(suggested)*
- [SQL](sql/README.md) *(suggested)*

# C

The language of operating systems, drivers and embedded devices. Learning C teaches memory, pointers and how the machine works. Almost every other language is compared to it.

## Install

```bash
# Arch / Omarchy
sudo pacman -S --needed gcc clang gdb valgrind make cmake

# Check
gcc --version && gdb --version && valgrind --version
```

Compile and run: `gcc -Wall -Wextra -std=c17 main.c -o main && ./main`
Always compile with `-Wall -Wextra`. Treat warnings as bugs.

## Syllabus

### Level 1 – Basics
- [ ] Hello world, compile and link steps (preprocess → compile → assemble → link)
- [ ] Variables, types, `sizeof`, integer overflow
- [ ] Operators, `if`, `switch`, loops
- [ ] Functions, prototypes, `static`
- [ ] Arrays and strings (null-terminated)

### Level 2 – Pointers and memory
- [ ] Pointers, `&` and `*`, pointer arithmetic
- [ ] Stack vs heap, `malloc`, `calloc`, `realloc`, `free`
- [ ] Structs, unions, `typedef`
- [ ] Function pointers
- [ ] Use `valgrind` on everything you write

### Level 3 – Real programs
- [ ] Standard I/O and file I/O (`fopen`, `fread`, `fprintf`)
- [ ] Preprocessor macros and header files
- [ ] Multiple files, Makefiles, CMake
- [ ] Error handling with `errno`
- [ ] Linked lists, stacks, queues, hash tables from scratch

### Level 4 – Systems
- [ ] Processes: `fork`, `exec`, `wait`
- [ ] Pipes and signals
- [ ] POSIX sockets: a TCP echo server
- [ ] Threads with `pthread`, mutexes
- [ ] Undefined behaviour – read the C standard's list of UB

## Resources

| | Resource | Notes |
|---|---|---|
| ⭐🆓 | [CS50 (Harvard)](https://cs50.harvard.edu/x/) | Free, full course; C in weeks 1–5 |
| ⭐💲 | *The C Programming Language* – Kernighan & Ritchie (K&R) | The classic, short and dense |
| 🆓 | [Beej's Guide to C Programming](https://beej.us/guide/bgc/) | Free, clear, practical |
| 🆓 | [Modern C – Jens Gustedt](https://modernc.gforge.inria.fr/) | Free book, modern C17/C23 |
| 🆓 | [cppreference – C](https://en.cppreference.com/w/c) | Reference for every function |
| 🆓 | [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/) | For Level 4 sockets |
| 🆓 | [Computer Systems: A Programmer's Perspective (CS:APP)](https://csapp.cs.cmu.edu/) | Bridges C and hardware |
| 🆓 | [Linux man pages](https://man7.org/linux/man-pages/) | `man 2 read` etc. |

## Projects

1. 🛠️ **Calculator** with a tokenizer and a recursive-descent parser
2. 🛠️ **Your own `malloc`/`free`** (a tiny allocator)
3. 🛠️ **Hash table** with string keys
4. 🛠️ **Simple shell** that runs commands and pipes (`fork`, `exec`, `pipe`)
5. 🛠️ **Multithreaded TCP chat server**

## Tips

- Use `-fsanitize=address,undefined` to find memory bugs during development.
- Read the man pages. Most C answers are in them.

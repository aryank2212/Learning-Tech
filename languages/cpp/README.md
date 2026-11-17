# C++

Fast, powerful, and complex. Used for games, browsers, databases, GPU code and high-performance computing. Learn it *after* C or Rust feels comfortable, or alongside a Python project.

## Install

```bash
sudo pacman -S --needed gcc clang cmake ninja gdb valgrind
# Editor support
code --install-extension ms-vscode.cpptools
code --install-extension ms-vscode.cmake-tools
```

Use a modern standard: `-std=c++20` (or `c++23` if your compiler supports it).
Build with CMake:

```bash
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Debug
cmake --build build
./build/myprog
```

## Syllabus

### Level 1 – Core language
- [ ] Types, references vs pointers, `const`
- [ ] Functions, overloading, default arguments
- [ ] Classes, constructors, destructors
- [ ] Operator overloading
- [ ] Inheritance, virtual functions, polymorphism

### Level 2 – Modern C++
- [ ] RAII (resource management through constructors and destructors)
- [ ] Smart pointers: `unique_ptr`, `shared_ptr`, `weak_ptr`
- [ ] Move semantics, rvalue references, `std::move`
- [ ] Templates, `concepts` (C++20)
- [ ] Lambdas and `std::function`
- [ ] Standard library: `vector`, `map`, `unordered_map`, `string_view`, `optional`, `variant`

### Level 3 – Algorithms and design
- [ ] `<algorithm>` and ranges (C++20)
- [ ] Iterators and writing your own container
- [ ] Exceptions and exception safety
- [ ] Design patterns in modern C++
- [ ] Unit testing with GoogleTest or Catch2

### Level 4 – Performance and systems
- [ ] Cache-friendly data layout, profiling with `perf`
- [ ] Multithreading: `std::thread`, `std::jthread`, `std::mutex`, atomics
- [ ] Build systems: CMake in depth
- [ ] Compile-time programming: `constexpr`, `consteval`
- [ ] Memory debugging with `valgrind` and `-fsanitize=address`

## Resources

| | Resource | Notes |
|---|---|---|
| ⭐🆓 | [learncpp.com](https://www.learncpp.com/) | Free, complete, modern C++ |
| ⭐🆓 | [cppreference.com](https://en.cppreference.com/) | The reference, bookmark it |
| 🆓 | [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) | Best practices from Stroustrup and Sutter |
| 🆓 | [isocpp.org](https://isocpp.org/) | Official community site |
| 🆓 | [The Cherno – C++ series (YouTube)](https://www.youtube.com/@TheChernoProject) | Good intro videos |
| 🆓 | [Compiler Explorer (godbolt.org)](https://godbolt.org/) | See the assembly your code produces |
| 💲 | *A Tour of C++* – Bjarne Stroustrup | Short tour of modern C++ |
| 💲 | *Effective Modern C++* – Scott Meyers | Idioms for C++11/14 and beyond |
| 💲 | *C++ Templates: The Complete Guide* – Vandevoorde, Josuttis, Gregor | Advanced templates |

## Projects

1. 🛠️ **Matrix class** with operator overloading and move semantics
2. 🛠️ **Smart-pointer clone** (write your own `unique_ptr`)
3. 🛠️ **Text-based game** (Tetris or Snake) in the terminal
4. 🛠️ **Ray tracer** that writes a PPM image (*Ray Tracing in One Weekend* – free at raytracing.github.io)
5. 🛠️ **Multithreaded image processor**

## Tips

- Use `clang-tidy` and `clang-format` to keep code clean.
- Read compiler errors top-down; templates make them long. Use `godbolt.org` to test small snippets.

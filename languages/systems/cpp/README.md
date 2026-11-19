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
| 🆓 | The Cherno's C++ series on YouTube (search "The Cherno C++") | Good intro videos |
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

## Study timeline (about 12 weeks)
| Weeks | Focus | Done when |
|---|---|---|
| 1–3 | Level 1: core language | A class with constructors and operators compiles without warnings |
| 4–6 | Level 2: modern C++ | You write RAII wrappers and can explain each move |
| 7–8 | Level 3: algorithms and containers | A tested container, and algorithms written with ranges |
| 9–12 | Level 4 and projects 3–5 | A multi-file CMake project with performance measurements |

## Common pitfalls
- **Dangling references and iterators.** A `std::vector` reallocation invalidates them.
- **Object slicing** when a derived object is copied into a base object by value.
- **Rule of 0, 3 and 5.** If you write a destructor, also think about copy and move operations.
- **Undefined behaviour** from overflow and out-of-range access. `-fsanitize=undefined` finds many of these.
- **Template error messages** that run for pages. Read the first error, and the template arguments it names.

## Where C++ is used
Game engines (Unreal Engine), browsers (Chromium), databases, compilers (LLVM and Clang are written in C++), high-performance computing, graphics drivers (Vulkan, Direct3D) and low-latency finance systems.

## Ecosystem
- **Package managers:** [vcpkg](https://vcpkg.io/), [Conan](https://conan.io/)
- **Libraries:** [Boost](https://www.boost.org/), [fmt](https://fmt.dev/), [Qt](https://www.qt.io/)
- **Testing:** GoogleTest, Catch2
- **Tools:** clang-format, clang-tidy, CMake

## More reading
- *A Tour of C++* — Bjarne Stroustrup (💲)
- *Accelerated C++* — Koenig & Moo (💲)
- *C++ Primer* — Lippman, Lajoie, Moo (💲)
- *The C++ Programming Language* — Stroustrup (💲)
- Talks from CppCon on YouTube — search "CppCon"

## Libraries for data, ML and AI
- **Linear algebra:** Eigen, Armadillo, xtensor
- **Classical ML:** mlpack, dlib
- **Running models:** LibTorch (PyTorch's C++ API), ONNX Runtime, OpenCV's `dnn` module, TensorRT on NVIDIA GPUs
- **Language models:** llama.cpp and ggml

```bash
sudo pacman -S eigen opencv dlib xtensor armadillo openblas
```
mlpack, ONNX Runtime and llama.cpp aren't in the official Arch repos; use their releases or build from source. More in [ML libraries in other languages](../../../ai/frameworks/ml-libraries-other-languages/README.md#c).

## My personal take

*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- C++ is huge. I'd learn it deliberately, for a specific goal such as games, engines or performance work.
- Learn RAII and the rule of zero before anything else. Most modern C++ problems start with ownership.
- Use Compiler Explorer. Seeing the assembly changes how you think about the code.

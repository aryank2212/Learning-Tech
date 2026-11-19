# Learning paths

Eight guided tracks through Learning-Tech. Each lists the subjects in order, the phases to focus on, and a checkpoint that shows you're ready to move on. Durations are rough guesses for about 8–10 hours a week; skip what you already know.

## How to use a path
1. Pick one path. Don't start two at once.
2. For each step, read the subject's `README.md`, work through the phases named, and do the matching [practice](practice.md) Level 1 and Level 2.
3. Move on when you can do the checkpoint without looking things up.
4. Tick your progress in the [tracker](progress/TRACKER.md).
5. Ask questions, or suggest a path that's missing, by [opening an issue](https://github.com/aryank2212/Learning-Tech/issues/new/choose).

## 1. Backend developer

**Time:** about 6–9 months. **For you if:** You want to build services and APIs that real products depend on.

1. **[Python](languages/general/python/README.md)** — Levels 1–3. *Checkpoint:* a tested command-line tool.
2. **[SQL](languages/data/sql/README.md)** — Levels 1–3. *Checkpoint:* a 3NF schema and a set of join queries.
3. **[DSA](foundations/algorithms/dsa/README.md)** — Part A. *Checkpoint:* 50 problems solved and explained.
4. **[Web technology](web/fundamentals/web-technology/README.md)** — HTTP, TLS, cookies and security phases. *Checkpoint:* a small HTTP server with correct headers.
5. **[Software engineering](software/engineering/software-engineering/README.md)** — Phases 1–7. *Checkpoint:* a repository with tests and CI.
6. **[System architecture](systems/architecture/system-architecture/README.md)** — Phases 1–6. *Checkpoint:* a design document for a URL shortener.

**Capstone:** A REST API with Postgres, authentication, tests and CI, deployed, with a design document.

## 2. Systems and performance

**Time:** about 9–12 months. **For you if:** You want to understand how computers really run your code, and make it fast.

1. **[C](languages/systems/c/README.md)** — Levels 1–4. *Checkpoint:* a shell or a malloc that passes valgrind.
2. **[Operating systems](systems/kernels/operating-systems/README.md)** — Phases 1–6. *Checkpoint:* a scheduler simulator and a thread-safe buffer.
3. **[Computer architecture](foundations/hardware/computer-architecture/README.md)** — Phases 1–9. *Checkpoint:* a cache simulator.
4. **[Computer networking](systems/networks/computer-networking/README.md)** — Phases 1–7. *Checkpoint:* a TCP chat server.
5. **[Parallel and distributed computing](systems/distributed/parallel-distributed-computing/README.md)** — Phases 1–8. *Checkpoint:* a scaling plot for a parallel program.
6. **[Rust](languages/systems/rust/README.md)** — Levels 1–4. *Checkpoint:* a safe concurrent program.

**Capstone:** A multithreaded network server in C or Rust, with a written performance report.

## 3. AI engineer

**Time:** about 7–10 months. **For you if:** You want to build applications on top of machine learning and language models.

1. **[Python](languages/general/python/README.md)** — Levels 1–3. *Checkpoint:* a typed, tested tool.
2. **[Maths](foundations/mathematics/maths/README.md)** — Linear algebra, calculus and probability phases. *Checkpoint:* gradient descent in NumPy.
3. **[Data science](data/science/data-science/README.md)** — Phases 1–7. *Checkpoint:* an end-to-end prediction project.
4. **[scikit-learn](ai/frameworks/scikit-learn/README.md)** — Phases 1–6. *Checkpoint:* a leakage-safe pipeline with an honest test score.
5. **[PyTorch](ai/frameworks/pytorch/README.md)** — Phases 1–8. *Checkpoint:* a model trained on your own data, with a validation curve.
6. **[AI, LLMs and ML](ai/machine-learning/ai-ml/README.md)** — Phases 3–5. *Checkpoint:* a small GPT, then an app built on an LLM API.
7. **[Agentic AI and orchestration](ai/agents/agentic-ai/README.md)** — Phases 1–9. *Checkpoint:* an agent with tools and an evaluation set.
8. **[Research](research/README.md)** — Reading papers and reproducing a result. *Checkpoint:* a reproduced table from one paper.

Optional: **[TensorFlow and Keras](ai/frameworks/tensorflow/README.md)** if your stack deploys to phones or browsers, and **[ML libraries in other languages](ai/frameworks/ml-libraries-other-languages/README.md)** when you need to run models outside Python.

**Capstone:** A retrieval-based assistant with citations, an evaluation set, and a short report on where it fails.

## 4. Security engineer

**Time:** about 6–9 months. **For you if:** You want to find weaknesses and design systems that resist attack.

1. **[Python](languages/general/python/README.md)** — Levels 1–3. *Checkpoint:* a small scripting toolkit.
2. **[Computer networking](systems/networks/computer-networking/README.md)** — Phases 1–8. *Checkpoint:* captured and explained a TLS handshake.
3. **[Web technology](web/fundamentals/web-technology/README.md)** — Phases 6–7 (sessions, web security). *Checkpoint:* five fixed issues in a vulnerable practice app.
4. **[Cryptography](security/cryptography/cryptography/README.md)** — Phases 1–9. *Checkpoint:* Cryptopals sets 1–3.
5. **[Operating systems](systems/kernels/operating-systems/README.md)** — Phases 7–8 (containers, protection). *Checkpoint:* a seccomp-sandboxed program.
6. **[Tech ethics](security/ethics/tech-ethics/README.md)** — Phases 3 and 7. *Checkpoint:* a responsible-disclosure policy for your own project.

**Capstone:** A threat model and hardening report for a small app you built, with every fix verified. Only test systems you own.

## 5. Hardware-curious

**Time:** about 6–9 months. **For you if:** You want to know what's inside the chip, from gates up to a CPU.

1. **[Digital electronics](foundations/hardware/digital-electronics/README.md)** — Phases 1–7. *Checkpoint:* a 4-bit adder and counter.
2. **[Computer architecture](foundations/hardware/computer-architecture/README.md)** — Phases 1–6. *Checkpoint:* a single-cycle CPU.
3. **[C](languages/systems/c/README.md)** — Levels 1–3. *Checkpoint:* a small emulator.
4. **[Operating systems](systems/kernels/operating-systems/README.md)** — Phases 1–4. *Checkpoint:* a tiny kernel experiment in QEMU.
5. **[CUDA](languages/gpu/cuda/README.md)** — Levels 1–3. *Checkpoint:* a tiled matrix multiply.

**Capstone:** A small CPU in Verilog (or a simulator) that runs a program you wrote in assembly.

## 6. Language and compiler builder

**Time:** about 6–9 months. **For you if:** You want to design languages, and understand what happens between source and machine code.

1. **[C or Rust](languages/systems/rust/README.md)** — Levels 1–3. *Checkpoint:* a program you're proud of.
2. **[Theory of computation](foundations/theory/theory-of-computation/README.md)** — Phases 1–7. *Checkpoint:* a regex engine and a CYK parser.
3. **[Compiler design](software/compilers/compiler-design/README.md)** — Phases 1–9. *Checkpoint:* a bytecode interpreter.
4. **[DSA](foundations/algorithms/dsa/README.md)** — Part B. *Checkpoint:* tries, graphs and dynamic programming.

**Capstone:** A small programming language with a lexer, parser, type checker and bytecode VM, plus a language reference.

## 7. Data analyst or scientist

**Time:** about 6–9 months. **For you if:** You want to answer questions with data and communicate the answers clearly.

1. **[Python](languages/general/python/README.md)** — Levels 1–4. *Checkpoint:* a notebook analysis.
2. **[SQL](languages/data/sql/README.md)** — Levels 1–4. *Checkpoint:* a window-function report.
3. **[Data science](data/science/data-science/README.md)** — Phases 1–10. *Checkpoint:* a dashboard and a written report.
4. **[Statistical computing](data/statistics/statistical-computing/README.md)** — Phases 1–7. *Checkpoint:* a bootstrap and a regression with diagnostics.
5. **[scikit-learn](ai/frameworks/scikit-learn/README.md)** — Phases 1–6. *Checkpoint:* a leakage-safe pipeline with an honest test score.
6. **[Predictive and big data analytics](data/analytics/predictive-big-data-analytics/README.md)** — Phases 1–5. *Checkpoint:* a backtested forecast.

**Capstone:** A public project that takes a real dataset from question to recommendation, with the code and the report.

## 8. Quantum-curious

**Time:** about 4–6 months. **For you if:** You want to understand quantum algorithms and what they mean for cryptography.

1. **[Maths](foundations/mathematics/maths/README.md)** — Linear algebra and probability phases. *Checkpoint:* complex vectors and unitary matrices in NumPy.
2. **[Python](languages/general/python/README.md)** — Levels 1–3. *Checkpoint:* Python you can read fluently.
3. **[Quantum computing](emerging/quantum/quantum-computing/README.md)** — Phases 1–10. *Checkpoint:* Grover and a Bell-state experiment.
4. **[Cryptography](security/cryptography/cryptography/README.md)** — Phases 1–6 and post-quantum material. *Checkpoint:* an RSA demo you then break at small size.
5. **[Theory of computation](foundations/theory/theory-of-computation/README.md)** — Phases 8–10. *Checkpoint:* a map of complexity classes.

**Capstone:** A simulated Shor demo for 15 and a noise study on a small circuit.

## Not sure which one?

Start with the first two steps of the Backend path (Python, then SQL). They're useful in every other path, and you'll learn what you enjoy while you build.

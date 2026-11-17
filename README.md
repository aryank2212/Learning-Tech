# Learning-Teach

A structured, self-paced curriculum covering programming languages, computer science fundamentals, mathematics, data, AI, security, systems and the web.

Every subject follows the same pattern:

1. **Install / setup** — get the tools running on Arch/Omarchy (notes for other systems in [setup](setup/README.md))
2. **Syllabus** — topics in order, with checkboxes and a project for each phase
3. **Resources** — books (🆓 free / 💲 paid), courses, docs, papers and tools
4. **Projects** — things to build, so the ideas stick

## Start here
| Step | Read |
|---|---|
| 1. Set up your machine | [setup/README.md](setup/README.md) |
| 2. Pick a first language | [languages/README.md](languages/README.md) |
| 3. Build the habit | [progress/TRACKER.md](progress/TRACKER.md) |

## Subjects

### Languages
| Language | Start with |
|---|---|
| [Rust](languages/rust/README.md) | The Rust Book and Rustlings |
| [C](languages/c/README.md) | CS50 and K&R |
| [C++](languages/cpp/README.md) | learncpp.com |
| [Java](languages/java/README.md) | dev.java tutorials |
| [Python](languages/python/README.md) | Automate the Boring Stuff |
| [CUDA](languages/cuda/README.md) | NVIDIA's CUDA C++ guide |
| [Go *(suggested)*](languages/go/README.md) | A Tour of Go |
| [SQL *(suggested)*](languages/sql/README.md) | SQLBolt |

### Core computer science
| Subject | Folder | What it covers |
|---|---|---|
| Data Structures & Algorithms (DSA) and Advanced DSA | [dsa](dsa/README.md) | Core structures, graphs, DP, flows, complexity theory |
| Operating Systems | [operating-systems](operating-systems/README.md) | Processes, scheduling, memory, file systems, kernels |
| Computer Networking | [computer-networking](computer-networking/README.md) | OSI/TCP-IP, routing, transport, DNS, network security |
| Compiler Design | [compiler-design](compiler-design/README.md) | Lexing, parsing, IRs, optimisation, code generation, LLVM |
| Digital Electronics | [digital-electronics](digital-electronics/README.md) | Logic gates, sequential circuits, Verilog, microcontrollers |

### Mathematics
| Subject | Folder | What it covers |
|---|---|---|
| Maths (engineering) & Discrete Maths | [maths](maths/README.md) | Linear algebra, calculus, probability, logic, proofs, graphs, number theory |

### Data & statistics
| Subject | Folder | What it covers |
|---|---|---|
| Data Science | [data-science](data-science/README.md) | Wrangling, EDA, visualisation, ML workflow, deployment |
| Predictive & Big Data Analytics | [predictive-big-data-analytics](predictive-big-data-analytics/README.md) | Forecasting, Spark, Kafka, warehouses |
| Statistical Computing | [statistical-computing](statistical-computing/README.md) | Simulation, estimation, inference, Bayesian methods, R |

### AI
| Subject | Folder | What it covers |
|---|---|---|
| AI, LLMs & Machine / Deep Learning | [ai-ml](ai-ml/README.md) | Classical ML, neural networks, transformers, LLM apps |
| Agentic AI & Orchestration | [agentic-ai](agentic-ai/README.md) | Tool use, agents, multi-agent systems, MCP, evaluation, safety |
| Research (AI and other subjects) | [research](research/README.md) | How to read, write and publish research; open questions by subject |

### Security, trust & ethics
| Subject | Folder | What it covers |
|---|---|---|
| Cryptography | [cryptography](cryptography/README.md) | Ciphers, hashes, signatures, TLS, attacks, post-quantum |
| Blockchain | [blockchain](blockchain/README.md) | Hashing, consensus, smart contracts, contract security (testnets only) |
| Tech Ethics | [tech-ethics](tech-ethics/README.md) | Frameworks, privacy, fairness, safety, professional codes, case studies |

### Systems & web
| Subject | Folder | What it covers |
|---|---|---|
| System Architecture | [system-architecture](system-architecture/README.md) | Distributed systems, patterns, scaling, operations |
| Web Technology | [web-technology](web-technology/README.md) | How the web works: HTTP, TLS, browsers, security, performance |
| Web Development | [web-development](web-development/README.md) | HTML, CSS, JavaScript, React, backends, deployment |

## Suggested learning order
```
Setup ──► one language (Python or C)
            │
            ├──► Maths (logic, linear algebra, calculus, probability)
            │
            ├──► DSA ──► Operating systems ──► Computer networking
            │         │                          │
            │         └──► Compiler design       └──► Web technology ──► Web development
            │
            ├──► Digital electronics (hardware view of computing)
            │
            ├──► Data science ──► Statistical computing ──► Predictive & big data
            │                                              │
            └──► AI/ML ──► Agentic AI ──► Research ◄───────┘
                             │
                             └──► Cryptography ──► Blockchain
                                      │
                                      └──► Tech ethics (throughout, not only at the end)
```

## Suggested additions (not added yet)
- **Computer architecture** — pipelines, caches and branch prediction; follows digital electronics
- **Theory of computation** — automata, Turing machines, decidability; follows discrete maths
- **Software engineering** — testing, design patterns, version control at team scale
- **Parallel and distributed computing** — MPI, OpenMP, GPU patterns; follows CUDA and system architecture
- **Quantum computing** — qubits, quantum algorithms, post-quantum crypto links

Tell me which of these you want as new folders.

## How to use this repo
- Work through one topic at a time. Do the exercise before reading the next one.
- Tick topics in [progress/TRACKER.md](progress/TRACKER.md) when you can do them without looking things up.
- Build the projects. Reading code without writing it doesn't stick.
- Keep your own notes in a `notes/` folder inside the subject you're studying.

## Legend
- 🆓 free · 💲 paid book or course · ⭐ start here · 🛠️ hands-on project
- *(suggested)* — a subject I added beyond your list, which you can remove

## Contributing
Add a link or a topic? Edit the file and open a pull request. Link to official docs, well-known authors, and sources you have checked yourself.

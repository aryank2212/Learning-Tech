# Learning-Tech

A free, self-paced learning platform for computing: languages, computer science, maths, data, AI, security, systems, engineering and the web.

## Open source, and it stays that way
Learning-Tech is an **open-source-leaning** platform. Everything here is free to read, copy and adapt (see [LICENSE](LICENSE)). You can **ask for anything**: open an issue to request a subject, a tutorial, a practice set, a resource, a correction or a whole new area. If you want to help build it, read [CONTRIBUTING.md](CONTRIBUTING.md) and send a pull request. Fixing a typo counts.

## Quick start
| I want to… | Read |
|---|---|
| Set up my machine | [setup](setup/README.md) |
| Pick a first language | [languages](languages/README.md) |
| Find a tutorial for a topic | [tutorial.md](tutorial.md) |
| Practise at my level | [practice.md](practice.md) |
| Get answers to common questions | [FAQ.md](FAQ.md) |
| Track my progress | [progress](progress/TRACKER.md) |

## Foundations

Maths, theory, hardware and algorithms: the base everything else stands on.

### [Maths](foundations/mathematics/maths/README.md)
The mathematics that computer science and engineering rely on, in two parts.

> **My take:** Maths is the subject people skip most and regret most. Logic and proofs make every other subject easier, so do them properly.

### [Theory of Computation](foundations/theory/theory-of-computation/README.md)
What computers can do, what they can't do, and how much effort the things they can do really take.

> **My take:** I expected this to be the dullest subject and it's become one of my favourites. The ideas about what's impossible shape how you think about everything else.

### [Digital Electronics](foundations/hardware/digital-electronics/README.md)
How logic is built from transistors and gates, and how gates become memory, adders and CPUs.

> **My take:** Building even a simple circuit on a breadboard teaches more than a week of reading. A cheap kit is worth it.

### [Computer Architecture](foundations/hardware/computer-architecture/README.md)
How a processor is organised so that it runs instructions quickly: instruction set design, pipelining, the memory hierarchy, branch prediction, parallel execution inside.

> **My take:** This is where performance stops being guesswork. Learn to read perf output and you'll write faster code for the rest of your career.

### [DSA & Advanced DSA](foundations/algorithms/dsa/README.md)
Data structures and algorithms: how to store data so operations are fast, and how to solve problems efficiently.

> **My take:** DSA is hard to fake and easy to practise. The interview grind is tiring, but the ideas are worth learning properly, not just pattern-matching.

## Software

Engineering practice and compilers: building software that lasts.

### [Software Engineering](software/engineering/software-engineering/README.md)
Building software that many people can change safely for years: requirements, design, testing, version control at team scale, code review, continuous delivery,.

> **My take:** This is the subject that turns a personal script into something a team can maintain. I think it's underrated by people who only write code alone.

### [Compiler Design](software/compilers/compiler-design/README.md)
How source code becomes something a machine can run.

> **My take:** Writing a small language and its interpreter is one of the most satisfying projects in CS. It changes how you read every language after that.

## Systems

Operating systems, networks, architecture and distributed computing.

### [Operating Systems](systems/kernels/operating-systems/README.md)
How a computer manages processes, memory, files, devices and security.

> **My take:** Operating systems is where many people finally understand why their programs behave the way they do.

### [Computer Networking](systems/networks/computer-networking/README.md)
How devices talk to each other: from electrical signals on a cable to a web page loading.

> **My take:** Networking stays abstract until you capture packets. Start with Wireshark on your own traffic; it's the fastest way to learn.

### [System Architecture](systems/architecture/system-architecture/README.md)
How computers, networks and large software systems work together, and how to design them.

> **My take:** System design interviews reward memorised diagrams. Real design rewards writing down trade-offs and failure modes. Practise the second.

### [Parallel & Distributed Computing](systems/distributed/parallel-distributed-computing/README.md)
Running work on many cores and many machines at once: shared-memory threads, message passing, GPUs, data-parallel frameworks, and the hard parts of distributed systems.

> **My take:** Parallel code is easy to make slower. Measure speedup at several core counts before you celebrate.

## Web

How the web works, and how to build for it.

### [Web Technology](web/fundamentals/web-technology/README.md)
How the web works underneath the frameworks: protocols, browsers, standards, security and performance.

> **My take:** Frameworks change every few years. HTTP, the DOM and browser security change slowly. Learn the slow things well.

### [Web Development](web/building/web-development/README.md)
From a blank HTML file to a full-stack app with users, a database and deployment.

> **My take:** Learn plain HTML, CSS and JavaScript properly before React. Frameworks are much easier once the platform underneath makes sense.

## Data

Data science, analytics at scale and statistics.

### [Data Science](data/science/data-science/README.md)
Turning raw data into decisions and predictions: collecting, cleaning, exploring, modelling, communicating and deploying.

> **My take:** Most of data science is cleaning and questioning data, not modelling. Expect that and you'll enjoy it more.

### [Predictive & Big Data Analytics](data/analytics/predictive-big-data-analytics/README.md)
Forecasting the future from past data, at a scale where one laptop is not enough.

> **My take:** Start with simple forecasts, such as naive and seasonal baselines. Many fancy models lose to them on honest tests.

### [Statistical Computing](data/statistics/statistical-computing/README.md)
Doing statistics with code: simulation, estimation, inference, modelling and reproducible analysis.

> **My take:** Statistics makes more sense when you simulate it. Write the code that generates the data before reading the formula.

## AI

Machine learning, LLM agents and how to do research.

### [AI, LLMs & Machine / Deep Learning](ai/machine-learning/ai-ml/README.md)
From "what is a model" to building and running your own large language model.

> **My take:** Learn enough maths to read a training loop, then build models. I'd rather you train a small network from scratch than memorise architectures.

### [Agentic AI & Orchestration](ai/agents/agentic-ai/README.md)
Building AI systems that plan, use tools, remember things and finish multi-step work.

> **My take:** Agents are useful, and most of the hype overstates how reliable they are. Build small ones, measure their failures, and add complexity only after that.

### [Research](research/README.md)
Research is how a field moves forward.

> **My take:** Research is less mysterious than it looks: read widely, pick a narrow question, and write down what you tried, including failures.

## Security, trust & ethics

Cryptography, blockchain (testnets only) and tech ethics.

### [Cryptography](security/cryptography/cryptography/README.md)
The mathematics and engineering behind secrecy, integrity and authentication.

> **My take:** Crypto is one of the most useful subjects you can learn, and one of the easiest to get wrong. Use libraries, learn to break weak designs, and never roll your own for real data.

### [Blockchain](security/ledgers/blockchain/README.md)
Distributed ledgers: how many computers agree on one shared history without a central authority.

> **My take:** I think the core ideas (hashing, signatures, consensus) are worth learning. Much of the surrounding hype and money talk isn't.

### [Tech Ethics](security/ethics/tech-ethics/README.md)
What technology should and shouldn't do, who it affects, and how engineers take responsibility for it.

> **My take:** Ethics isn't a box to tick at the end of a project. It's a set of questions you ask at the start, when they're cheap to answer.

## Emerging computing

Quantum computing.

### [Quantum Computing](emerging/quantum/quantum-computing/README.md)
Computing with qubits: superposition, entanglement and measurement, quantum gates and circuits, the algorithms that give quantum computers their advantage (Grover,.

> **My take:** Most of the current hype runs ahead of the hardware. Learn the linear algebra and the algorithms first.

## Languages

Eight languages, grouped by what they're mainly used for.

See the [languages index](languages/README.md) for the comparison table.

### [Rust](languages/systems/rust/README.md)
Memory-safe systems language with no garbage collector.

> **My take:** Rust is the language I'd pick if I wanted one that teaches memory safety properly. The borrow checker is frustrating for about a week, then it becomes the part you value most.

### [C](languages/systems/c/README.md)
The language of operating systems, drivers and embedded devices.

> **My take:** C is worth learning even if you never write it for a living, because it shows what the machine does underneath every other language.

### [C++](languages/systems/cpp/README.md)
Fast, powerful, and complex.

> **My take:** C++ is huge. I'd learn it deliberately, for a specific goal such as games, engines or performance work.

### [Java](languages/general/java/README.md)
An object-oriented language that runs on the Java Virtual Machine (JVM).

> **My take:** Java is a sensible choice for enterprise and big-data work. The ecosystem is large and stable.

### [Python](languages/general/python/README.md)
Readable, huge ecosystem, and the main language of AI, data science and scripting.

> **My take:** If you only learn one language first, I'd choose Python. It gets you building early, and most AI and data work uses it.

### [CUDA](languages/gpu/cuda/README.md)
NVIDIA's platform for running code on the GPU.

> **My take:** CUDA is worth learning once you're comfortable with C++ and have a real reason, such as a slow kernel or a model you need to train.

### [Go *(suggested)*](languages/general/go/README.md)
Simple, fast, garbage-collected language built for servers, networking and cloud tools.

> **My take:** Go is my pick for servers and tooling. It's small enough to learn in weeks, and the standard library is excellent.

### [SQL *(suggested)*](languages/data/sql/README.md)
The language of databases.

> **My take:** SQL is the most useful language on this list for most people. Almost every job touches a database eventually.

## Research

How to read, write and publish research in any subject.

### [Research](research/README.md)
Doing research in AI and every other subject.

> **My take:** Research is less mysterious than it looks: read widely, pick a narrow question, and write down what you tried, including failures.

## Also in this repo

- [tutorial.md](tutorial.md) — tutorials for every subject
- [practice.md](practice.md) — practice sets by level, with a practice file in each subject
- [FAQ.md](FAQ.md) — recommendations on tech, hardware, time and paths
- [setup](setup/README.md) — install guide for Arch/Omarchy, with notes for other systems
- [progress](progress/TRACKER.md) — tick off what you've learned

## Licence and contributions
Content: [CC BY-SA 4.0](LICENSE). Contributions welcome: [CONTRIBUTING.md](CONTRIBUTING.md).

## Legend
🆓 free · 💲 paid book or course · ⭐ start here · 🛠️ hands-on project · *(suggested)* a subject added beyond the original list

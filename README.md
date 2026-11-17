# Learning-Teach

A structured, self-paced curriculum for programming, AI, system design and web development.
Every area has the same four things:

1. **Install guide** – get the tools running (Arch / Omarchy first, notes for other systems)
2. **Syllabus** – the topics in order, from zero to advanced
3. **Resources** – books, free courses, docs, videos and interactive practice
4. **Projects** – things to build so the knowledge sticks

## Start here

| Step | Read |
|------|------|
| 1. Set up your machine | [setup/README.md](setup/README.md) |
| 2. Pick a language | [languages/README.md](languages/README.md) |
| 3. Track progress | [progress/TRACKER.md](progress/TRACKER.md) |

## Areas

### Languages
| Language | Why learn it | Start |
|----------|--------------|-------|
| [Rust](languages/rust/README.md) | Memory-safe systems programming, fast, modern tooling | Rust Book + Rustlings |
| [C](languages/c/README.md) | How computers really work; the language of operating systems | K&R + CS50 |
| [C++](languages/cpp/README.md) | Performance-critical software, games, engines, GPU code | learncpp.com |
| [Python](languages/python/README.md) | Fastest path to real projects, the language of AI | Automate the Boring Stuff |
| [CUDA](languages/cuda/README.md) | Write code that runs on the GPU | NVIDIA CUDA guide |
| [Go *(suggested)*](languages/go/README.md) | Simple, fast servers and cloud tools | A Tour of Go |
| [SQL *(suggested)*](languages/sql/README.md) | Every app stores data; you cannot skip it | SQLBolt |

### AI, LLMs & Machine / Deep Learning
[Overview](ai-ml/README.md) · [Install](ai-ml/install.md) · [Syllabus](ai-ml/syllabus.md) · [Resources](ai-ml/resources.md)

### System Architecture
[Overview](system-architecture/README.md) · [Syllabus](system-architecture/syllabus.md) · [Resources](system-architecture/resources.md)

### Web Development
[Overview](web-development/README.md) · [Install](web-development/install.md) · [Syllabus](web-development/syllabus.md) · [Resources](web-development/resources.md)

## Suggested learning order

```
Foundations ──► Language (C or Python) ──► Data structures & algorithms
     │                                              │
     ├──► Computer systems (CS:APP, OSTEP) ◄────────┤
     │                                              │
     ├──► Web dev (HTML → JS → React → backend)     │
     │                                              ▼
     └──► AI/ML (Python → math → PyTorch → LLMs) ──► System design
```

## How to use this repo

- Work through one topic at a time. Do the exercise before reading the next topic.
- Each topic in a syllabus has a checkbox. Tick them in [progress/TRACKER.md](progress/TRACKER.md).
- Build the projects. Reading code without writing code does not stick.
- Keep notes in your own words, in a `notes/` folder inside the topic you are studying.

## Legend

- 🆓 free
- 💲 paid / book you buy
- ⭐ start here
- 🛠️ hands-on project

## Contributing

Add a link? Open a PR or edit the file. Keep each link to official docs, well-known authors, or sources you have checked yourself.

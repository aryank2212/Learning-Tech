# FAQ

Honest answers and my own recommendations. Where something is opinion, I say so. Ask anything else by [opening an issue](https://github.com/aryank2212/Learning-Tech/issues).

## Getting started

**Where do I start if I know nothing?**
Learn one language properly first. I'd pick **Python** because it gets you building quickly. Then add **C** to see what the machine does underneath. Do the [setup guide](setup/README.md) before anything else.

**Which language should I learn first?**
Python, for most people. If you want to understand computers deeply and don't mind a harder start, C. If you're sure you want systems or game work, Rust or C++. You can switch later; the thinking carries over.

**How long will this take?**
My rough guess, not a promise: 8 to 10 hours a week for three to six months gets you a solid foundation in one path. Real depth takes years. Plan for finishing one track, not all of Learning-Tech.

**Do I need to learn everything?**
No. Pick a track (see below) and go deep. Breadth comes later and is easier once you have one area solid.

**Which path should I follow?**
These are my suggestions:
- **Software developer (backend):** Python or Go → SQL → DSA → web technology → system architecture → software engineering.
- **Systems or performance:** C → operating systems → computer architecture → parallel and distributed computing.
- **AI engineer:** Python → maths → data science → AI/ML → agentic AI.
- **Security:** Python → networking → cryptography → web technology → tech ethics.
- **Hardware-curious:** digital electronics → computer architecture → C → operating systems.
- **Quantum (for fun or research):** maths (linear algebra, probability) → quantum computing, after a programming track.

**I've got no background in maths. Can I still do this?**
Yes, for most of the programming and web tracks. You'll need algebra and some probability for AI and data work. Learn the maths alongside the topic that needs it; the [maths](foundations/mathematics/maths/README.md) page explains the order.

## Hardware and setup

**Which computer do I need?**
- **Any laptop** from the last five years is enough for programming, web, databases and most maths.
- **Machine learning on your own machine:** an NVIDIA GPU with 8 GB or more of VRAM helps a lot. Without one, use free Colab or Kaggle GPUs.
- **Large local LLMs:** 16 GB of RAM is a comfortable minimum for small quantised models; more VRAM for bigger ones.
- **Digital electronics:** a cheap breadboard kit (about the price of a textbook) is enough.

**Linux, Windows or macOS?**
Any of the three works. I use Linux (Arch/Omarchy), and the setup guide is written for it. If you're on Windows, install **WSL2** with Ubuntu and follow the Ubuntu notes. On macOS, use Homebrew for the same tools.

**Should I use VS Code?**
Yes, for most people. It's free, it has excellent extensions for every language here, and it runs on all three systems.

**Where should I keep large files and caches?**
Keep projects and datasets on a drive with space. Build folders (`target/`, `.venv/`, `node_modules/`) and model caches grow quickly, so check disk space once a month.

## Tools and tech choices

**Git: how much do I need?**
Learn `add`, `commit`, `push`, `pull`, branches and pull requests. That's enough for every subject here. [Pro Git](https://git-scm.com/book) and [The Missing Semester](https://missing.csail.mit.edu/) cover the rest.

**Docker: do I need it early?**
Not at the start. It becomes useful in system architecture, big data and deployment. Learn it once you have an app that needs to run somewhere else.

**Which database should I learn?**
PostgreSQL. It's free, powerful and used widely. Start with SQLite for small projects, because it needs no server.

**Which web framework should I learn?**
Learn plain HTML, CSS and JavaScript first. Then React, with Next.js when you need routing and server rendering. For backend APIs, FastAPI (Python) or Express (Node) are gentle starts.

**Rust or Go for backend work?**
Go is simpler and quick to become productive in. Rust takes longer, but you learn more about memory and performance. Both are good; pick by what your team or project uses.

**Should I use AI tools (LLMs) while learning?**
Yes, but try the problem first. Ask an assistant to explain an error, check your reasoning, or make a practice set harder. Don't let it write your projects for you: you learn by doing. Verify anything it tells you, because models make confident mistakes.

**Do I need a GPU for AI?**
Not to learn. Colab and Kaggle give free GPU time for the course projects. A local GPU becomes useful when you want to train or fine-tune often.

## Study habits

**How do I avoid "tutorial hell"?**
Use the 70/30 rule: spend about 30% of time reading and watching, and 70% building and breaking things. Stop watching a course when you can't yet explain the last lesson without it.

**What should I do when I'm stuck?**
Give it 30 minutes. Then write down exactly what you tried and what you expected. Search the error message, check the matching tutorial, and if you're still stuck, open an issue with that note. A clear question gets a faster answer.

**How do I stay motivated?**
Build something you care about, even if it's small. Share a small result publicly, and keep a progress log in [progress/TRACKER.md](progress/TRACKER.md).

**Should I take courses or do projects?**
Both, in that order: take a short course for a concept, then build a project using it. Projects show what you can actually do.

## Careers and goals

**Do I need a degree?**
Many people get jobs without one. A degree helps with structure and with some doors. Projects, a clear portfolio and good fundamentals help more than credentials alone, in most fields.

**What should my portfolio look like?**
Three or four finished projects, each with a README that explains the problem, the choices you made, what didn't work, and how to run it. Put them on GitHub.

**Do I need to memorise algorithms for interviews?**
For many software jobs, yes, at least the basics: arrays, hash maps, trees, graphs and dynamic programming. The [DSA](foundations/algorithms/dsa/README.md) practice sets are a good way in. Interviews also test communication, so practise talking through your solutions.

**Is it worth learning blockchain?**
I think the core ideas (hashing, signatures, consensus) are worth understanding, and some jobs use them. I don't think learning it is a financial plan, and this repo does not give investment advice. Use testnets only, and never put a real seed phrase into a learning project.

**Is quantum computing a good career bet?**
It's a fascinating field with few jobs today. I'd learn it because you're curious, or for research. For most careers, post-quantum cryptography is the more practical link to learn.

## About this repo

**Why aren't the books and papers in the repo?**
Most of them are copyrighted, so I can't publish copies. `scripts/fetch-library.sh` downloads the free ones to your own machine, and the paid ones you buy yourself. Every book and paper is linked from its subject page.

**Can I use this for teaching?**
Yes. The content is licensed under CC BY-SA 4.0 (see [LICENSE](LICENSE)). Credit the project, and share any changes under the same licence.

**How do I suggest something new?**
Open an issue. You can ask for anything: a subject, a tutorial, a practice set, a correction. If you want to write it, see [CONTRIBUTING.md](CONTRIBUTING.md).

**Are the personal takes my own?**
They're the author's opinions, written to be argued with. Treat them as one view, and form your own.

## More questions

**How do I know which level to start at?**
Try Level 1 of a subject's `practice.md`. If you finish it comfortably in under an hour, move to Level 2. If Level 1 feels hard, go back to the syllabus and the first tutorial in [tutorial.md](tutorial.md).

**Where are the answers to the practice tasks?**
The quiz at the end of each practice file has answers. The tasks don't, on purpose: you check them with tests, a known result, or by comparing with a friend. Worked solutions are on the [roadmap](ROADMAP.md). If you're stuck, [open an issue](https://github.com/aryank2212/Learning-Tech/issues/new/choose) and say what you tried.

**Is there a recommended order?**
Yes, see [PATHS.md](PATHS.md). It has eight tracks (backend, systems, AI, security, hardware, compilers, data, quantum), each with checkpoints.

**What does this word mean?**
Check the [glossary](GLOSSARY.md). If a term is missing, ask for it.

**How do you keep the links working?**
A GitHub Actions workflow checks the Markdown links every week, and `scripts/check_repo.py` checks the structure and internal links on every pull request. If you find a dead link before we do, please report it.

**Can I get a certificate for finishing something?**
No. This is a self-study resource, and your progress is tracked by you. A finished project in a public repository says more than a certificate.

**Can I use this in a class or a study group?**
Yes. The licence allows teaching and adapting, as long as you credit the project and share changes under the same licence. The paths and practice sets work well for a weekly study night.

**Can I translate it?**
Yes, and it's on the roadmap. Open an issue so we don't duplicate work.

**What if someone behaves badly in an issue?**
Read the [Code of Conduct](CODE_OF_CONDUCT.md). You can report a problem by opening an issue marked as a conduct concern or by contacting the maintainer on GitHub.

# Changelog

All notable changes to Learning-Tech. Newest first.

## 2026-11-19 — ML frameworks
- Added four guides under `ai/frameworks/`: scikit-learn, PyTorch, TensorFlow and Keras, and ML libraries in other languages (Rust, C and C++, Java, Go, JavaScript, R, Julia, C#, mobile and ONNX).
- Added 12 runnable, tested example scripts (scikit-learn, PyTorch, TensorFlow and Keras, and an ONNX export and parity check that runs from Node.js).
- A "Libraries for data, ML and AI" section on every language page.
- New glossary terms, learning-path steps, FAQ answers, tutorials, practice sets and tracker rows.
- The repo checker now compiles every example script and understands repeated headings in anchors.

## 2026-11-19 — Quizzes, paths, glossary and automation
- Added quick quizzes with answers to every `practice.md`.
- Added [PATHS.md](PATHS.md) (guided learning tracks), [GLOSSARY.md](GLOSSARY.md) and [LIBRARY.md](LIBRARY.md).
- Added [ROADMAP.md](ROADMAP.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), issue and pull request templates.
- Added `scripts/check_repo.py` and a GitHub Actions workflow that checks structure and links.
- Practice columns and subject links added to the progress tracker.
- More FAQ answers.
- Library script: the site mirror now reads `robots.txt` with its own user agent (some sites block Python's default one), and the arXiv finder only matches real paper IDs. A dead PDF link for *The Elements of Statistical Learning* was removed.
- Readable link labels (for example "Python" instead of `languages/python`) after the folder reorganisation.

## 2026-11 — Reorganisation and open-source launch
- Subjects grouped into categories: foundations, software, systems, web, data, ai, security, emerging, languages.
- Open-source note, contribution guide, FAQ, tutorials, practice sets, personal takes and a CC BY-SA 4.0 licence.
- Repository made public with commit emails set to the GitHub noreply address.
- Local-only `library/` of free books and papers, rebuilt with `scripts/fetch-library.sh` (not committed, for copyright reasons).

## 2026-11 — Growth
- Added Computer Architecture, Theory of Computation, Software Engineering, Parallel & Distributed Computing and Quantum Computing.
- Added DSA, Operating Systems, Networking, Compiler Design, Digital Electronics, Maths, Data Science, Predictive & Big Data, Statistical Computing, Agentic AI, Research, Cryptography, Blockchain, Tech Ethics, Web Technology and Java.

## 2026-11 — First version
- Languages (Rust, C, C++, Python, CUDA, Go, SQL), AI/ML, System Architecture and Web Development, with setup guide and progress tracker.
